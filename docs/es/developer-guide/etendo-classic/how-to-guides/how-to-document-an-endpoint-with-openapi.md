---
tags:
  - How to
  - Infrastructure
  - OpenAPI
  - Swagger

title: Cómo documentar un endpoint con OpenAPI
---

# Cómo documentar un endpoint con OpenAPI

## Visión general

Esta documentación detalla los pasos para documentar endpoints de API utilizando la especificación OpenAPI. Al aprovechar Swagger, los desarrolladores pueden garantizar que sus API estén bien documentadas, estandarizadas y sean fáciles de integrar.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Platform Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Platform Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

## Definir una solicitud OpenAPI por defecto

Este tipo requiere implementar el endpoint de forma programática. Cree una nueva clase Java que extienda la clase abstracta `OpenAPIDefaultRequest` e implemente los métodos requeridos (por ejemplo: `getClasses()`, `getEndpointPath()` y los métodos de operación como `getPOSTEndpoint()`).

La clase abstracta `OpenAPIDefaultRequest` proporciona la funcionalidad base para añadir endpoints de API por defecto a la documentación de Swagger. Esta:

- Recupera las etiquetas y flujos relacionados.
- Añade definiciones al objeto OpenAPI.
- Soporta operaciones `GET`, `POST` y `PUT`.

A continuación se muestra un ejemplo:

```java
package com.etendoerp.etendorx.openapi;

public class ImageUploadOpenAPI extends OpenAPIDefaultRequest {
    public static final String ETENDO_ID_PATTERN = "^[0-9a-fA-F]{1,32}$";

    @Override
    protected Class<?>[] getClasses() {
        return new Class<?>[]{ com.etendoerp.etendorx.services.ImageUploadServlet.class };
    }

    @Override
    protected String getEndpointPath() {
        return "/sws/com.etendoerp.etendorx.imageUpload/";
    }

    @Override
    Operation getPOSTEndpoint() {
        Operation endpoint = new Operation();
        endpoint.setSummary("Upload an image to EtendoERP");
        endpoint.setDescription("Upload an image to EtendoERP, it can use a configuration associated with a Column ID to automatically resize the image.");

        Schema reqSchema = new Schema()
            .addProperty("filename", new StringSchema().description("The name of the file").example("image.jpg"))
            .addProperty("columnId", new StringSchema().description("The column ID where the size and resize configuration is stored").pattern(ETENDO_ID_PATTERN))
            .addProperty("base64Image", new StringSchema().description("The base64 encoded image"));
        reqSchema.required(List.of("filename", "base64Image"));

        RequestBody requestBody = new RequestBody().content(new Content()
            .addMediaType("application/json", new MediaType().schema(reqSchema)));
        endpoint.requestBody(requestBody);

        return endpoint;
    }
}
```

Esta clase especifica un endpoint POST para subir imágenes. Define la ruta del endpoint, el esquema del cuerpo de la solicitud y las propiedades obligatorias.

La clase `ImageUploadOpenAPI` muestra:

- **Ruta del endpoint**: `/sws/com.etendoerp.etendorx.imageUpload/`
- **Operación POST**: define las propiedades obligatorias (`filename`, `base64Image`) y valida la entrada.
- **Asociación de clase Java**: enlaza con `ImageUploadServlet` para gestionar las solicitudes.

### Ventana Solicitud OpenAPI

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `OpenAPI Request`

Un registro de Solicitud OpenAPI representa un único endpoint de API en su aplicación.

![Ventana Solicitud OpenAPI mostrando campos y opciones](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi/how-to-document-an-endpoint-with-openapi.png)

Campos a tener en cuenta:

1. **Tipo**: establezca el tipo en `Default`.
2. **Descripción**: añada la descripción general del endpoint. Esta descripción se añade a la descripción principal de OpenAPI.
3. **Clase Java**: especifique la clase Java creada que extiende la clase `OpenAPIDefaultRequest`.
4. **Descripción GET**: proporcione una descripción para el método GET del endpoint. Esta descripción se utiliza si el endpoint soporta el método GET.
5. **Descripción GET por ID**: proporcione una descripción para el método GET por ID del endpoint. Esta descripción se utiliza si el endpoint soporta el método GET por ID.
6. **Descripción POST**: proporcione una descripción para el método POST del endpoint. Esta descripción se utiliza si el endpoint soporta el método POST.
7. **Descripción PUT**: proporcione una descripción para el método PUT del endpoint. Esta descripción se utiliza si el endpoint soporta el método PUT.

### Ventana Flujo OpenAPI

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `OpenAPI Flow`

Un **Flujo OpenAPI** agrupa endpoints de API relacionados bajo una única categoría o _flujo_. Estos flujos facilitan la organización y navegación de la documentación de la API.

Cada registro de Flujo OpenAPI puede:

- Definir un nombre y una descripción del flujo.
- Incluir una o más Solicitudes OpenAPI mediante la solapa `Endpoints`.
- Especificar qué métodos HTTP (GET, GET por ID, POST, PUT) soportan los endpoints usando los campos de la solapa `Endpoints`. Cuando estos campos están marcados, generan la documentación de los métodos de endpoint correspondientes.

![Ventana Flujo OpenAPI listando endpoints relacionados](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi/how-to-document-an-endpoint-with-openapi-1.png)

Para garantizar que una Solicitud OpenAPI aparezca en la documentación de Swagger, debe estar enlazada a un Flujo OpenAPI. Esto asegura un agrupamiento lógico y visibilidad.

### Interfaz de endpoint OpenAPI

Esta interfaz garantiza un comportamiento consistente de los endpoints de API definiendo métodos como:

- `boolean isValid(String tag)`
- `void add(OpenAPI openAPI)`

Por ejemplo, la clase `ImageUploadOpenAPI` implementa estos métodos para validar etiquetas y añadir definiciones de endpoints al objeto OpenAPI.

![Ejemplo de Swagger para el endpoint de subida de imagen con esquemas de solicitud y respuesta](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi/swagger-imageupload-example.png)

## Otros tipos de Solicitud OpenAPI

=== "Solapa"

    Este tipo se utiliza para documentar entidades existentes o tablas de base de datos sin crear una clase personalizada que extienda `OpenAPIDefaultRequest`. Permite exponer datos del ERP como endpoints de API, soportando operaciones completas de **CRUD** (Crear, Leer, Actualizar, Eliminar).

    **Funcionalidades clave**:

    - Todos los campos de la solapa seleccionada están disponibles automáticamente en el endpoint de API.
    - La lógica de negocio como `callouts`, `event handlers`, `triggers` y `default values` se aplica automáticamente al crear, actualizar o eliminar registros.
    - Los endpoints son conscientes de la sesión, lo que garantiza consistencia de datos y acceso seguro.
    - La especificación OpenAPI se genera automáticamente. Por defecto, incluye los campos obligatorios para las operaciones `POST` y `PUT`, pero puede simplificarla especificando solo los campos requeridos en la sub-solapa **Campo** de la ventana Solicitud OpenAPI.
    - Dado que los endpoints de tipo Solapa reutilizan la misma lógica de negocio que las Solapa de Etendo, se comportan de forma consistente. Por ejemplo, puede crear una cabecera de *Pedido de venta* proporcionando únicamente el ID del tercero, y el sistema aplicará la misma lógica que al crearlo a través de la UI del ERP.

    Para configurar una Solicitud OpenAPI de tipo **Solapa**:

    ![Configurar una Solicitud OpenAPI de tipo Solapa mostrando el selector de solapa y la configuración](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi/how-to-document-an-endpoint-with-openapi-2.png)

    1. **Crear un nuevo registro en la ventana `OpenAPI Request`**:

        - **Tipo**: establezca el tipo en _Solapa_.
        - **Descripción**: proporcione una descripción del endpoint, incluyendo su propósito y funcionalidad.
        - **Solapa**: se mostrará una nueva solapa de ventana. Añada un nuevo registro y seleccione la solapa de ventana deseada desde el selector de solapa.
        - **Descripción GET**: proporcione una descripción para el método GET del endpoint. Se recomienda incluir detalles sobre los parámetros esperados de la solicitud y el formato de la respuesta.
        - **Descripción GET por ID**: proporcione una descripción para el método GET por ID del endpoint. Se recomienda incluir detalles sobre los parámetros esperados de la solicitud y el formato de la respuesta.
        - **Descripción POST**: proporcione una descripción para el método POST del endpoint. Se recomienda incluir detalles sobre los parámetros esperados de la solicitud y el formato de la respuesta.
        - **Descripción PUT**: proporcione una descripción para el método PUT del endpoint. Se recomienda incluir detalles sobre los parámetros esperados de la solicitud y el formato de la respuesta.

    2. **Enlazar la solicitud a un Flujo OpenAPI**:

        - Abra la ventana `OpenAPI Flow`.
        - Añada un nuevo registro.
        - Enlace la Solicitud OpenAPI en la solapa hija.

=== "Webhook"

    Utilice este tipo para documentar eventos de webhook sin escribir una clase personalizada. Simplifica la integración y mantiene un formato consistente.

    **Funcionalidades clave**:

    - Proporciona documentación clara de los eventos de webhook.
    - Sigue formatos estándar para facilitar la integración.
    - Visible y fácil de probar en la UI de Swagger.

    Para configurar una Solicitud OpenAPI de tipo **Webhook**:

     ![texto alternativo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi/how-to-document-an-endpoint-with-openapi-3.png)

    1. **Crear un nuevo registro en la ventana `OpenAPI Request`**:
        
        - **Tipo**: establezca el tipo en _Webhook_.
        - **Descripción**: proporcione una descripción del webhook.
        - **Solapa Webhook**: se mostrará una nueva solapa de ventana. Añada un nuevo registro y seleccione el webhook deseado desde el selector.
        - **Descripción POST**: proporcione una descripción para el método POST del webhook. Se recomienda incluir detalles sobre los parámetros esperados de la solicitud y el formato de la respuesta. Esta es la única descripción de método requerida, debido a la naturaleza de los webhooks, que son únicamente POST.

    2. **Enlazar la solicitud a un Flujo OpenAPI**:
     
        - Abra la ventana `OpenAPI Flow`.
        - Añada un nuevo registro.
        - Enlace la Solicitud OpenAPI en la solapa hija.

## Comprobar Swagger

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `OpenAPI Flow`

La nueva documentación del endpoint debería ser visible en la UI de Swagger. Ejecute el botón **Abrir Swagger** para abrir Swagger en una nueva pestaña.

![Botón Abrir Swagger en la interfaz de Etendo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi/swagger-button.png)

Verifique que el nuevo endpoint aparece bajo la etiqueta definida y muestra los esquemas correctos de solicitud y respuesta.

Se verá así:
![UI de Swagger mostrando el nuevo endpoint bajo el flujo/etiqueta definido](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi/swagger-flow-example.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.