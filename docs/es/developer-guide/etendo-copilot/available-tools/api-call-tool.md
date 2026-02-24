---
tags:
    - Etendo Copilot
    - Integración de API
    - Solicitudes HTTP
    - API REST
    - Herramienta
---

# Herramienta de llamadas a API

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de llamadas a API** está diseñada para ejecutar solicitudes HTTP a APIs externas. Permite a los desarrolladores conectar sus aplicaciones con servicios externos utilizando métodos REST. La herramienta acepta parámetros de entrada como la URL de la API, el endpoint, el método HTTP, los parámetros de consulta, el contenido del cuerpo y un token de autorización opcional. Como salida, devuelve el cuerpo de la respuesta y el código de estado de la llamada a la API.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

Esta herramienta proporciona al agente:

- Integración: permite que las aplicaciones consuman APIs REST externas fácilmente.
- Flexibilidad: admite los métodos GET, POST y PUT con cabeceras y payloads personalizables.
- Automatización: facilita la interacción con sistemas externos desde Etendo Copilot.

Esta herramienta es ideal para desarrolladores que integran servicios de terceros, APIs internas o microservicios.

## Configuración

No se requieren variables de entorno específicas para utilizar esta herramienta. Sin embargo, si se necesita un bearer token para la autorización, puede pasarse en la entrada como el parámetro `token`.

Adicionalmente, si utiliza el valor de token especial `ETENDO_TOKEN`, la herramienta obtendrá el token usando la utilidad de gestión de tokens de Etendo.

## Funcionalidad

Esta herramienta permite la ejecución de solicitudes REST mediante los siguientes pasos:

- **Procesamiento de argumentos**

    Procesa parámetros de entrada como:
    - `url`: URL base de la API (obligatorio)
    - `endpoint`: endpoint específico de la API (obligatorio)
    - `method`: método HTTP (`GET`, `POST` o `PUT`) (obligatorio)
    - `body_params`: payload (para POST y PUT)
    - `query_params`: cadena de consulta como un objeto JSON
    - `token`: bearer token opcional

- **Gestión de parámetros de consulta**

    Si se proporcionan, los parámetros de consulta se añaden al endpoint con la codificación de URL adecuada.

### Uso de ETENDO_TOKEN

Si establece el parámetro `token` con el valor especial `ETENDO_TOKEN`, Copilot lo sustituirá automáticamente por un token seguro recuperado del entorno de Etendo. Este enfoque garantiza que el token **no se expone al modelo de lenguaje** y permanece seguro durante la ejecución.

Ejemplo:

```json
{
    "method": "GET",
    "url": "https://my.etendo.instance/etendo",
    "endpoint":"/sws/mySecureWebservice",
    "token": "ETENDO_TOKEN"
}
```

- **Sustitución de placeholders Base64**

    Si el cuerpo contiene placeholders `@BASE64_filepath@`, se sustituyen por el contenido codificado en base64 del archivo especificado.

    ```json
        {
            "method": "POST",
            "url": "https://my.etendo.instance/etendo",
            "endpoint":"/sws/UploadFile",
            "token": "ETENDO_TOKEN",
            "body_params": {
                "file": "@BASE64_filepath@"
            }
        }
    ```
    La Herramienta de llamadas a API sustituirá `@BASE64_filepath@` por el contenido codificado en base64 del archivo especificado en el parámetro `file` sin exponer el contenido del archivo ni el base64 al modelo (no solo por motivos de seguridad, sino también para evitar confusión en el modelo).

- **Ejecución de la solicitud**

    En función del método, la herramienta realiza la solicitud correspondiente utilizando la librería `requests`.

- **Devolución de la respuesta**

    Devuelve una respuesta estructurada con:
    
    ```
    {
        "requestResponse": "<response body>",
        "requestStatusCode": 200
    }
    ```

    En caso de error:
    
    ```
    {
        "error": "Mensaje de error detallado"
    }
    ```

## Ejemplo de uso

Imagine que desea enviar una solicitud POST a una API externa para crear un nuevo usuario. Los parámetros de entrada para el agente serían:

- `url`: https://api.example.com
- `endpoint`: /users/create
- `method`: POST
- `body_params`: 
    ```json
    {
        "name": "John Doe",
        "email": "john@example.com"
    }
    ```
- `token`: YOUR_BEARER_TOKEN

La Herramienta de llamadas a API formateará y enviará la solicitud con las cabeceras y el cuerpo adecuados, y devolverá el resultado incluyendo el código de estado de la respuesta y el contenido del cuerpo.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.