---
tags:
    - Copilot
    - IA
    - Tool
    - File Copy
---

# Herramienta de copia de archivos

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de copia de archivos** recibe dos rutas: una de un archivo y otra de un directorio. Su función es copiar el archivo especificado al directorio especificado y devolver la ruta del archivo copiado.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta es útil cuando necesita duplicar archivos en diferentes ubicaciones dentro del sistema de archivos. Esto puede ser esencial para tareas de copia de seguridad, organización de archivos o preparación de archivos para su procesamiento en ubicaciones específicas. Esto simplifica el proceso de copiar archivos y gestionar directorios, garantizando la existencia del directorio de destino y proporcionando una respuesta clara con la ruta del archivo copiado.

Este proceso consta de las siguientes acciones:

- **Recepción de parámetros**

    La herramienta recibe un objeto de entrada que contiene dos claves:

    - `source_path`: ruta al archivo de origen que se va a copiar.
    - `destination_directory`: ruta al directorio de destino donde desea copiar el archivo.

- **Creación del directorio de salida**

    Si el directorio de salida no existe, la herramienta lo crea automáticamente para garantizar que la operación de copia no falle debido a una ruta inexistente.

- **Copia del archivo**

    Utilice la función `shutil.copy` de Python para copiar el archivo de origen al directorio de destino.

- **Devolución del resultado**

    Una vez completado el proceso, la herramienta devuelve un objeto que contiene la ruta completa al archivo copiado en el directorio de salida.

## Ejemplo de uso

Si tiene un archivo en `/home/user/file.txt` y desea copiarlo al directorio `/home/user/destination_directory`, utilizaría la herramienta de la siguiente manera:

- **Entrada**
```
{"source_path": "/home/user/file.txt", "destination_directory": "/home/user/destination_directory"}
```

- **Salida**
```
{"file_path": "/home/user/destination_directory/file.txt"}
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.