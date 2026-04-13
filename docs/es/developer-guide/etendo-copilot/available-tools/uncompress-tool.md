---
tags:
    - Copilot
    - Herramienta
    - Descomprimir archivos
    - Zip
---

# Herramienta de descompresión

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de descompresión** es una utilidad diseñada para descomprimir varios tipos de archivos comprimidos y devolver las rutas de los archivos descomprimidos. Admite tipos de archivo comunes, incluidos `zip`, `gzip`, `bzip2` y `rar`.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

El propósito principal de esta herramienta es agilizar el proceso de extracción de archivos desde formatos comprimidos. Es especialmente útil en escenarios en los que se necesita una extracción automatizada de archivos, como canalizaciones de procesamiento de datos, restauración de copias de seguridad y sistemas de gestión de archivos. Al admitir múltiples formatos de compresión comunes y proporcionar una interfaz sencilla para la extracción de archivos, simplifica los flujos de trabajo que implican archivos comprimidos y garantiza un manejo eficiente de los archivos de datos.

Este proceso consta de las siguientes acciones.

- **Recepción de parámetros**
    La herramienta espera un único parámetro de entrada:

    `compressed_file_path` : Ruta al archivo comprimido que debe descomprimirse.

- **Determinación del tipo de archivo**

    La herramienta inspecciona la extensión del archivo para determinar el tipo de archivo comprimido y selecciona el método de descompresión adecuado.

- **Creación del directorio de salida**

    La herramienta crea un directorio de salida basado en el nombre del archivo comprimido para almacenar el contenido descomprimido.

- **Descompresión del archivo**

    La herramienta admite múltiples formatos de compresión y utiliza las bibliotecas de Python correspondientes para descomprimir archivos:

    - `gzip` : Utiliza la biblioteca `gzip` para descomprimir archivos `.gz`.

    - `bzip2` : Utiliza la biblioteca `bz2` para gestionar archivos `.bz2`.

    - `rar` : Emplea la biblioteca rarfile para extraer archivos `.rar`.

    - `zip` : Aprovecha la biblioteca `zipfile` para descomprimir archivos `.zip`.

- **Devolución del resultado**

    Tras descomprimir correctamente los archivos, la herramienta devuelve un objeto que contiene las rutas de los archivos descomprimidos.

## Ejemplo de uso

Si existe un archivo comprimido en `/home/user/archive.zip` y es necesario descomprimirlo, la herramienta se utilizaría de la siguiente manera:

- **Entrada**:

```
{"compressed_file_path": "/home/user/archive.zip"}
```

- **Salida**:

```
{"uncompressed_files_paths": ["/home/user/archive/file1.txt", "/home/user/archive/file2.jpg", ...]}
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.