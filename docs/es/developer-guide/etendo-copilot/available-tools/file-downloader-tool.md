---
tags:
    - Copilot
    - IA
    - Tool
    - File Downloader
---

# Herramienta de descarga de archivos

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de descarga de archivos** está diseñada para recibir una URL y descargar el archivo correspondiente en un directorio temporal, devolviendo la ruta al archivo temporal. Esta herramienta es extremadamente valiosa para cualquier aplicación que necesite interactuar dinámicamente con archivos en la web. Le permite descargar archivos de forma eficiente y almacenarlos temporalmente, facilitando su uso y manipulación posteriores sin necesidad de preocuparse por la gestión de archivos en el sistema. Además, gestiona automáticamente distintos tipos de contenido (texto y binario), haciendo que la operación sea transparente y sencilla para el usuario.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta es especialmente útil cuando necesita descargar archivos desde la web para su posterior procesamiento sin preocuparse por gestionar los archivos en el sistema local. Puede ser útil para tareas como:

- Descargar imágenes, documentos u otros archivos para su análisis y procesamiento.
- Obtener archivos para almacenamiento temporal, evitando la necesidad de una gestión directa del sistema de archivos.

Este proceso consta de las siguientes acciones:

- **Recepción de parámetros**
    
    La herramienta recibe una URL como una cadena mediante el parámetro `file_path_or_url`.

- **Verificación de la URL**
    
    Comprueba si la entrada es una URL válida (comienza por `http://` o `https://`).

- **Descarga del archivo**

    - Realiza una solicitud HTTP GET a la URL.
    - Si la solicitud es correcta (código de estado 200):
        - Intenta determinar el nombre del archivo a partir de la URL.
        - Si no se puede determinar el nombre, determina un nombre genérico como
        `downloaded_file`.
        - Determina el tipo de contenido del archivo (texto u otro):
            - Si es texto, escribe el contenido en un archivo temporal con la extensión `.txt`, si no tiene otra extensión.
            - Si es otro, copia el contenido en un archivo temporal con la extensión correspondiente.

- **Devolución del resultado**
    
    Devuelve un diccionario con la ruta al archivo temporal creado bajo la clave `temp_file_path`.

- **Gestión del error**

    Si la URL no es válida o la descarga falla, devuelve un mensaje de error relevante.

## Ejemplo de uso

Si hay un archivo alojado en `https://example.com/file.txt` y es necesario descargarlo temporalmente:

- **Entrada**

```
file_path_or_url: "https://example.com/file.txt"
```

- **Salida**

```
{"temp_file_path": "/path/to/temp/downloaded_file.txt"}
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.