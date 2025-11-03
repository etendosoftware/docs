import os
import argparse
import logging
import re
import yaml
from algoliasearch.search.client import SearchClientSync

# --- Configuración del Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_markdown(text):
    """
    Limpia el texto de la sintaxis común de Markdown para indexar contenido puro.
    """
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'!\[[^\]]*\]\([^\)]+\)', '', text)
    text = re.sub(r'(\*\*|__|\*|_|~~|`)(.*?)\1', r'\2', text)
    text = re.sub(r'^\s*#+\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)
    return ' '.join(text.split())

def parse_markdown_file(file_path):
    """
    Parsea un archivo Markdown, separando el frontmatter YAML del contenido.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.match(r'---\s*\n(.*?)---\s*\n', content, re.DOTALL)
        if match:
            frontmatter = yaml.safe_load(match.group(1)) or {}
            markdown_content = content[match.end():]
            return frontmatter, markdown_content
        return {}, content
    except Exception as e:
        logging.error(f"Error al leer el archivo {file_path}: {e}")
        return {}, None

def parse_nav_section(nav_data, docs_dir):
    """
    Recorre la sección 'nav' para mapear rutas de archivo a su jerarquía de títulos.
    """
    nav_map = {}
    def get_title_from_md(file_path):
        try:
            frontmatter, _ = parse_markdown_file(file_path)
            return frontmatter.get('title')
        except Exception: return None
    def recurse_nav(items, prefix):
        for item in items:
            if isinstance(item, str):
                title = get_title_from_md(os.path.join(docs_dir, item)) or \
                        os.path.splitext(os.path.basename(item))[0].capitalize()
                nav_map[item] = prefix + [title]
            elif isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str): nav_map[value] = prefix + [title]
                    elif isinstance(value, list): recurse_nav(value, prefix + [title])
    recurse_nav(nav_data, [])
    return nav_map

def create_records(markdown_content, hierarchy_titles, page_url, tags):
    """
    Segmenta el contenido, añadiendo un group_id para la deduplicación.
    """
    RECORD_SIZE_LIMIT = 7000

    records = []
    base_hierarchy = {f'lvl{i}': title for i, title in enumerate(hierarchy_titles)}
    max_lvl = len(base_hierarchy) - 1

    h2s = re.findall(r'^##\s+(.*)', markdown_content, re.MULTILINE)
    h3s = re.findall(r'^###\s+(.*)', markdown_content, re.MULTILINE)
    h4s = re.findall(r'^####\s+(.*)', markdown_content, re.MULTILINE)

    def add_records_from_content(content_chunk, base_url, hierarchy):
        title_parts = [hierarchy.get(f'lvl{i}') for i in range(7)]
        if max_lvl + 1 < len(title_parts) and title_parts[max_lvl] and title_parts[max_lvl + 1]:
            page_title = title_parts[max_lvl].lower()
            h1_title = title_parts[max_lvl + 1].lower()
            if h1_title.startswith(page_title):
                title_parts[max_lvl] = None
        
        final_parts = [part for part in title_parts if part]
        record_title = final_parts[-1] if final_parts else ''
        
        # group id is base_url without fragment
        group_id = base_url.split('#')[0]
        # --- NUEVO: Objeto base con group_id y otros atributos ---
        base_record = {
            'title': record_title,
            'tags': tags,
            'h2': h2s,
            'h3': h3s,
            'h4': h4s,
            'group_id': group_id
        }

        if len(content_chunk.encode('utf-8')) <= RECORD_SIZE_LIMIT:
            if content_chunk:
                record = base_record.copy()
                record.update({'objectID': base_url, 'url': base_url, 'content': content_chunk})
                records.append(record)
            return

        words = content_chunk.split()
        current_chunk_words = []
        sub_chunk_index = 0
        
        for word in words:
            current_chunk_words.append(word)
            current_chunk_str = ' '.join(current_chunk_words)
            if len(current_chunk_str.encode('utf-8')) > RECORD_SIZE_LIMIT:
                valid_chunk_words = current_chunk_words[:-1]
                if valid_chunk_words:
                    valid_chunk_str = ' '.join(valid_chunk_words)
                    object_id = f"{base_url}_{sub_chunk_index}"
                    record = base_record.copy()
                    record.update({'objectID': object_id, 'url': base_url, 'content': valid_chunk_str})
                    records.append(record)
                    sub_chunk_index += 1
                current_chunk_words = [word]

        if current_chunk_words:
            last_chunk_str = ' '.join(current_chunk_words)
            object_id = f"{base_url}_{sub_chunk_index}"
            record = base_record.copy()
            record.update({'objectID': object_id, 'url': base_url, 'content': last_chunk_str})
            records.append(record)

    # El resto de la función (el cuerpo principal) no necesita cambios...
    chunks = re.split(r'\n(#+)\s+', markdown_content)
    intro_content = clean_markdown(chunks[0])
    if intro_content:
        hierarchy = base_hierarchy.copy()
        for i in range(max_lvl + 1, 6): hierarchy[f'lvl{i}'] = None
        add_records_from_content(intro_content, page_url, hierarchy)

    current_headings, i = {}, 1
    while i < len(chunks):
        level = len(chunks[i])
        parts = chunks[i+1].split('\n', 1)
        header_text = parts[0].strip()
        content = clean_markdown(parts[1]) if len(parts) > 1 else ""
        
        current_headings[level] = header_text
        for l in range(level + 1, 7): current_headings.pop(l, None)
        if content:
            hierarchy = base_hierarchy.copy()
            for l in range(1, 7): hierarchy[f'lvl{max_lvl + l}'] = current_headings.get(l)
            
            anchor = re.sub(r'[^\w\s-]', '', header_text).strip().lower()
            anchor = re.sub(r'[-\s]+', '-', anchor)
            record_url = f"{page_url}#{anchor}"
            add_records_from_content(content, record_url, hierarchy)
        i += 2
        
    return records

def index_docs(app_id, api_key, index_name, docs_dir, site_url, config_file):
    """
    Función principal que usa el cliente SÍNCRONO para indexar los documentos.
    """
    client = SearchClientSync(app_id, api_key)
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config_content = f.read()
        cleaned_content = re.sub(r'!!python/name:.*', '', config_content)
        config = yaml.load(cleaned_content, Loader=yaml.FullLoader)
        nav_map = parse_nav_section(config.get('nav', []), docs_dir) if 'nav' in config else {}
    except FileNotFoundError:
        logging.error(f"Archivo de configuración no encontrado: {config_file}")
        return

    all_records = []
    if not site_url.endswith('/'): site_url += '/'

    for relative_path, hierarchy_titles in nav_map.items():
        file_path = os.path.join(docs_dir, relative_path)
        if not os.path.exists(file_path): continue
        
        frontmatter, markdown_content = parse_markdown_file(file_path)
        
        if frontmatter.get('title'): hierarchy_titles[-1] = frontmatter.get('title')
        
        page_slug = os.path.splitext(relative_path)[0].replace('index', '')
        page_url = f"{site_url}{page_slug}"
        if not page_url.endswith('/'): page_url += '/'
        
        if markdown_content:
            # --- NUEVO: Obtener tags del frontmatter ---
            tags = frontmatter.get('tags', [])
            
            # --- MODIFICADO: Pasar tags a create_records ---
            records = create_records(markdown_content, hierarchy_titles, page_url, tags)
            all_records.extend(records)
            logging.info(f"Procesado: {relative_path} -> {len(all_records)} registros totales.")

    if not all_records:
        logging.info("No se encontraron registros para indexar.")
        return
    try:
        index = client.init_index(index_name) # Asegúrate de inicializar el índice
        logging.info(f"Limpiando y enviando {len(all_records)} registros a Algolia...")
        index.clear_objects()
        index.save_objects(all_records)
        logging.info("¡Proceso de indexación completado exitosamente!")
    except Exception as e:
        logging.error(f"Error al enviar registros a Algolia: {e}")
        
def index_docs(app_id, api_key, index_name, docs_dir, site_url, config_file):
    """
    Función principal que usa el cliente SÍNCRONO para indexar los documentos.
    """
    client = SearchClientSync(app_id, api_key)
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config_content = f.read()
        cleaned_content = re.sub(r'!!python/name:.*', '', config_content)
        config = yaml.load(cleaned_content, Loader=yaml.FullLoader)
        nav_map = parse_nav_section(config.get('nav', []), docs_dir) if 'nav' in config else {}
    except FileNotFoundError:
        logging.error(f"Archivo de configuración no encontrado: {config_file}")
        return

    all_records = []
    if not site_url.endswith('/'): site_url += '/'

    for relative_path, hierarchy_titles in nav_map.items():
        file_path = os.path.join(docs_dir, relative_path)
        if not os.path.exists(file_path): continue
        
        frontmatter, markdown_content = parse_markdown_file(file_path)
        
        if frontmatter.get('title'): hierarchy_titles[-1] = frontmatter.get('title')
        
        page_slug = os.path.splitext(relative_path)[0].replace('index', '')
        page_url = f"{site_url}{page_slug}"
        if not page_url.endswith('/'): page_url += '/'
        
        if markdown_content:
            # --- NUEVO: Obtener tags del frontmatter ---
            tags = frontmatter.get('tags', [])
            
            # --- MODIFICADO: Pasar tags a create_records ---
            records = create_records(markdown_content, hierarchy_titles, page_url, tags)
            all_records.extend(records)
            logging.info(f"Procesado: {relative_path} -> {len(all_records)} registros totales.")

    if not all_records:
        logging.info("No se encontraron registros para indexar.")
        return
    try:
        # Inicializar el índice para una mejor interacción con la API
        logging.info(f"Limpiando y enviando {len(all_records)} registros a Algolia...")
        client.clear_objects(index_name=index_name)
        client.save_objects(index_name=index_name, objects=all_records)
        logging.info("¡Proceso de indexación completado exitosamente!")
    except Exception as e:
        logging.error(f"Error al enviar registros a Algolia: {e}")

def main():
    parser = argparse.ArgumentParser(description="Indexa archivos Markdown de MkDocs en Algolia (versión síncrona).")
    parser.add_argument("api_key", help="La clave de escritura (Write API Key) de Algolia.")
    parser.add_argument("--app-id", required=True, help="El ID de la aplicación de Algolia.")
    parser.add_argument("--index-name", required=True, help="El nombre del índice en Algolia.")
    parser.add_argument("--config-file", default="mkdocs.yml", help="Ruta a mkdocs.yml.")
    parser.add_argument("--docs-dir", default="docs", help="Directorio de los archivos Markdown.")
    parser.add_argument("--site-url", required=True, help="La URL base del sitio.")
    args = parser.parse_args()
    index_docs(args.app_id, args.api_key, args.index_name, args.docs_dir, args.site_url, args.config_file)

if __name__ == "__main__":
    main()
