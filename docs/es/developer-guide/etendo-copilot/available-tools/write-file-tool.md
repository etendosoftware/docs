---
tags:
    - Copilot
    - Tool
    - Write
    - File
---

# Herramienta de escritura de archivos

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de escritura de archivos** es una herramienta para escribir y editar archivos. Permite especificar el archivo que desea escribir, el contenido a escribir y la opción de sobrescribir el archivo o no. También le permite especificar la línea exacta en la que desea escribir el contenido. Esta herramienta devuelve un mensaje indicando el resultado de la operación.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta es útil en cualquier aplicación o sistema que necesite manipular archivos de texto mediante programación. Puede utilizarse para editar configuraciones, registrar datos, crear archivos de log, entre otras cosas. Esto facilita al usuario la gestión de:

- Manipulación de archivos: facilita la edición y manipulación de archivos de texto sin necesidad de abrir manualmente los archivos en un editor.
- Estandarización de tareas: estandariza la escritura de archivos desde diferentes partes de una aplicación.
- Seguridad: crea copias de seguridad automáticas al escribir archivos existentes, evitando la pérdida de datos.

El uso de esta herramienta consiste en las siguientes acciones:

- **Procesamiento de argumentos**

    Toma los siguientes parámetros de entrada:

    - `filepath`: especifica el archivo (ruta del archivo)
    - `content`: el contenido a escribir
    - `override`: si el archivo debe sobrescribirse
    - `lineno`: la línea en la que debe escribirse el contenido

- **Creación del archivo**

    Si el archivo especificado no existe, lo crea.

- **Copia de seguridad**

    Si el archivo existe, lo lee y crea una copia de seguridad añadiendo una marca de tiempo al nombre del archivo (`.bak%timestamp%`).

- **Escritura del contenido**
    - Sobrescribir: si la opción de sobrescritura está habilitada, el archivo se limpia y se escribe el contenido especificado, ya sea al final del archivo (si no se especifica el número de línea) o en una línea concreta.
    - No sobrescribir: si no se elige sobrescribir, el contenido se añade al final del archivo existente.

- **Devolución del resultado**
    Devuelve un mensaje que incluye la ruta del archivo y si se creó una copia de seguridad. Por ejemplo:
    ```
    { “message”: “File /tmp/test.txt written successfully, backup: True”}
    ```
    si el archivo se modificó y se creó una copia de seguridad.
    ```
    { “message”: “File /tmp/test.txt written successfully, backup: False”}
    ```
    si no fue necesario crear una copia de seguridad.

## Permisos de escritura

Para gestionar los permisos de archivos y carpetas, la Herramienta de escritura de archivos utiliza la variable de entorno `COPILOT_WRITE_RULE`. Añada esta variable al archivo `gradle.properties` si fuese necesario.

Esta variable le permite especificar los permisos de archivo (en formato octal) que se aplicarán a los archivos y carpetas creadados por la herramienta. Es opcional y, si no se configura, se utilizarán los permisos de archivo predeterminados del sistema.

- **Creación de carpetas**: si la carpeta especificada no existe, se creará. Si `COPILOT_WRITE_RULE` está configurada, la herramienta aplica los permisos correspondientes a la carpeta recién creada.
- **Creación de archivos**: cuando se crea un archivo nuevo, la herramienta aplica los permisos especificados en `COPILOT_WRITE_RULE`.

El valor de `COPILOT_WRITE_RULE` debe ser una representación octal válida de los permisos de archivo (p. ej., `777` para acceso completo de lectura/escritura/ejecución).

## Ejemplo de uso

Imagine que queremos escribir *Hola Mundo* en el archivo `/tmp/test.txt`, sobrescribiendo su contenido, en la primera línea del archivo. Nuestra entrada podría ser:

- filepath: /tmp/test.txt
- content: Hola Mundo
- override: True
- lineno: 1

La Herramienta de escritura de archivos procesará estos parámetros, escribirá *Hola Mundo* en la primera línea del archivo `/tmp/test.txt` y devolverá un mensaje indicando que la operación se completó correctamente y si se creó una copia de seguridad.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.