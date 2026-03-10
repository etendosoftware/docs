---
tags:
    - Tool
    - Etendo Copilot
    - File Upload
    - Webhook Integration
    - Base64 Encoding
---

# Herramienta Adjuntar archivo

:octicons-package-16: Javapackage: `com.etendoerp.copilot.openapi.purchase`

## Visión general

La **herramienta Adjuntar archivo** carga un archivo mediante el webhook `AttachFile` tras verificar su existencia y accesibilidad. Implica leer el archivo desde una ruta especificada, codificarlo en base64 y, a continuación, enviarlo a Etendo usando el webhook, junto con los identificadores necesarios y un token de acceso.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

El propósito principal de la herramienta Adjuntar archivo es facilitar el proceso de adjuntar archivos a registros en Etendo, garantizando que el archivo sea accesible y esté correctamente codificado antes de la carga. Es muy valiosa en procesos automatizados que requieren adjuntar archivos a registros. 

Este proceso consta de las siguientes acciones:

- **Recepción de parámetros**

    La herramienta recibe un objeto de entrada que contiene las siguientes claves:

    - `filepath` : La ruta del archivo que se va a cargar.

    - `ad_tab_id` : Una cadena de 32 caracteres que es el ID de la solapa.

    - `record_id` : Una cadena de 32 caracteres que es el ID del registro.

- **Verificación del archivo**

    La herramienta comprueba si el archivo en la ruta especificada existe y es legible. Si el archivo no existe o no es accesible, devuelve un error.

- **Lectura y codificación del archivo**

    Si el archivo está disponible, lee el contenido del archivo y lo codifica en formato base64.

- **Autenticación**

    La herramienta recupera un token de acceso de la información adicional almacenada en el contexto del hilo. Si no se proporciona ningún token de acceso, devuelve un error.

- **Comunicación con la API**

    La herramienta construye las cabeceras y los parámetros del cuerpo necesarios y envía el archivo codificado al endpoint de la API especificado mediante una solicitud HTTP POST.

- **Devolución del resultado**

    Una vez completada la operación, la herramienta devuelve el resultado de la llamada a la API, que podría ser un mensaje de éxito o de error.

## Ejemplo de uso

Imagine que existe un archivo en `/home/user/document.pdf` y que es necesario cargarlo en un registro específico identificado por su ID de solapa y su ID de registro. La herramienta se utiliza del siguiente modo:

- **Entrada**:

    ```
    {
    "filepath": "/home/user/document.pdf",
    "ad_tab_id": "1234567890abcdef1234567890abcdef",
    "record_id": "abcdef1234567890abcdef1234567890"
    }
    ```

- **Salida**:

    ```
    {
    "result": { "message", "Attachment created successfully"}
    }
    ```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.