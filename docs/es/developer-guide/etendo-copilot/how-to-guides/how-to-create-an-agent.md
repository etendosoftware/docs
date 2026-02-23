---
tags:
    - How to
    - Etendo Copilot
    - Agent
    - Create
    - LLM
    - Agent
---

# Cómo crear un Agent

## Visión general

Este artículo explica cómo crear un nuevo agent en Etendo Copilot desde cero. El agent podrá interactuar con el usuario y proporcionar respuestas basadas en la entrada del usuario. Este artículo te guiará a través del proceso de crear un nuevo agent, añadir una base de conocimiento y seleccionar un model.

La explicación completa de las ventanas utilizadas en esta guía se puede encontrar en el artículo [Setup and Usage](../../../user-guide/etendo-copilot/setup-and-usage.md).

## Creación de un Agent de respuesta básica
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Agent`

La ventana Agent permite definir y configurar Agents.

Algunos de los campos principales a completar son:

- **Nombre**
- **Prompt**
- **App Type**:

    - **Multi-Model Agent**
    - **LangGraph**

- **Model**: desplegable con los modelos disponibles, como OpenAI, Anthropic, etc. Ve a la sección [¿Qué model debería elegir?](#which-model-should-i-choose) para más información.

!!!info
    El campo **Prompt** puede tener las siguientes variables dinámicas: @ETENDO_HOST@, @ETENDO_HOST_DOCKER@ y @source.path@  
    Estas variables se sustituirán por los valores definidos en las propiedades.

!!!note
    Para más información sobre para qué se utiliza cada campo, visita la guía [Setup and Usage - Agents](../../../user-guide/etendo-copilot/setup-and-usage.md#header).

### Ejemplo de definición de Agent

Por ejemplo, para crear un nuevo agent llamado **Task Definition Agent** para ayudar a los usuarios a definir una incidencia con el formato obligatorio para su equipo. El propósito del agent es recibir una descripción de la tarea y devolver la definición de la tarea con el formato obligatorio. Crearemos un nuevo agent con la siguiente información:

- **Nombre**: Task Definition Agent
- **Descripción**: Este agent ayuda a los usuarios a definir una descripción de tarea con el formato obligatorio para su equipo.
- **Model**: no es necesario seleccionar un model específico, se utilizará el model [por defecto](#default-model).
- **Temperature**: establecer en `0.5` porque queremos tener baja **creativity** en las respuestas.
- **Módulo**: este agent no se exportará a un módulo.
- **Prompt**:
    
    ```
    You are an agent to generate a task description based on the client's conveyed needs. This definition is intended for a developer.

    The description should follow this format:

    # Title
    - Title of the Task

    # Issue Description
    - State the primary need expressed, the problem to solve or the context of the change.

    # Solution Design
    - Outline what needs to be developed.

    # Use Cases
    * **Given**: Describe the initial context or precondition.
    * **When**: Explain the event or action taken.
    * **Then**: Describe the expected outcome.


    The goal is to generate a concise description. Be succinct and to the point.

    After creating the initial description, please answer the following questions to refine it further:
    1. Is the primary need of the client clearly and accurately stated?
    2. Does the solution design provide sufficient detail for development without ambiguity?
    3. Are the use cases comprehensive and cover all possible scenarios?
    4. Are there any assumptions or dependencies that need to be clarified?

    Separate the proposal of task  definition and the refinement questions with ---------------- for a better view

    Please provide your response in Markdown format, adhering strictly to the given template so it can be easily pasted into the issue.

    Once you respond with your answers, I will revise the description accordingly and provide additional questions for further refinement.

    Translate everything to English, because the issues must be in English.
    ```

Después de guardar el agent, el sistema concederá automáticamente acceso al mismo. Abre el Copilot Chat con el botón `✨Copilot` y selecciona el agent `Task Definition Agent`. Puedes empezar a interactuar con el agent.

![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent.png)

!!! tip
    Desde el agent más básico, su comportamiento está determinado por su system prompt. Por lo tanto, en caso de un funcionamiento no deseado, es importante verificar que el fallo no esté en un prompt incorrecto, ineficiente o poco claro. Es posible depurar llamadas LLM con Langsmith. Lee el artículo [How to debug an agent with Langsmith](./how-to-debug-an-agent-with-langsmith.md) para más información.

## Which Model Should I Choose?
Actualmente, Copilot soporta los siguientes proveedores:

- **OpenAI**: este proveedor es el predeterminado y el más utilizado. Es el más versátil y tiene el mejor rendimiento en la mayoría de los casos.
- **Google Gemini**: este proveedor está especializado en tareas generales como OpenAI, pero con mejor rendimiento en algunos casos.
- **Anthropic**: este proveedor está especializado en generación de código. Es la mejor opción para tareas relacionadas con código.
- **Deepseek**: este proveedor es para tareas generales como OpenAI, pero más barato.
- **Ollama (Self-hosted models)**: este proveedor es para usuarios que tienen sus propios modelos ejecutándose en su propia infraestructura. El soporte para este proveedor está en fase experimental. Para más información visita la guía [How to Use and Run Self Hosted Models with Ollama](how-to-use-run-self-hosted-models-with-ollama.md).

### Default Model
El model por defecto para Etendo Copilot es `gpt-4.1` de **OpenAI**. Este model se selecciona automáticamente si el agent no tiene un model específico seleccionado.

### AI Models Window - What Model are Available?
Etendo Copilot proporciona una ventana donde puedes ver los modelos disponibles y sus detalles. Esta ventana se rellena al sincronizar los modelos. Además, si el proveedor ofrece modelos que no están presentes en esta lista, se pueden añadir manualmente.

!!! info
    Más información aquí [AI Models](../../../user-guide/etendo-copilot/setup-and-usage.md#ai-models)

### Entrada de imagen

![Image Input](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-11.png){align=right width=250}

Los modelos que soportan entradas de imagen pueden trabajar con imágenes adjuntas a la conversación. Si el model no soporta entradas de imagen, es posible solucionarlo añadiendo al agent la `OCR Tool`, que permite extraer texto de imágenes.

Esta herramienta está disponible en el módulo [Etendo Copilot ToolPack](../../../developer-guide/etendo-copilot/bundles/overview.md#etendo-copilot-toolpack). Puede que necesites **explain** al agent cómo usarla en el prompt.

<br clear="all">

## Añadir una base de conocimiento
Los LLM son el cerebro detrás del agent y, por defecto, vienen con conocimiento adquirido del propio entrenamiento del model. Sin embargo, en muchos casos necesitamos que tengan información específica que no tienen, por lo que recurrimos al Knowledge Base File para conformar su base de conocimiento. Esto nos permitirá **train** nuestro agent con cierta información.

Lo más crucial es determinar:

- Knowledge Base File Type: básicamente es el origen o cómo Etendo puede obtener ese archivo. Esto se configura en la ventana `Knowledge Base File`.
- Knowledge Base File behavior: que es la forma en que este archivo se integra en el agent o en la conversación. Esto se configura en la pestaña `Knowledge` de la ventana `Agent`.

### Knowledge Base File Type

| Tipo | Cuándo usarlo | Información necesaria |
|--|--|------|
|**Attached File** | Úsalo cuando el archivo es uno que nunca cambia. | El propio archivo, que debe adjuntarse al registro de Knowledge Base File. |
|**Remote File** | Muy recomendable cuando el archivo puede cambiar y se puede acceder a la última versión desde la misma url. Por ejemplo, un archivo en un repositorio en GitHub. | URL del archivo |
|**Consulta HQL** | Se utiliza cuando quieres que el agent pueda leer información de una tabla o del resultado de una consulta a base de datos. Por ejemplo, una lista de terceros o pedidos. | Consulta HQL |
|**Texto** | Cuando la información es estática y se puede escribir directamente en la ventana. | El propio texto |
|**OpenAPI Flow Specification** | Úsalo cuando el archivo de base de conocimiento es la especificación OpenAPI de un Etendo Flow. Consulta [How to allow Copilot to interact with Etendo](#how-to-allow-copilot-to-interact-with-etendo-classic) para más información. | Seleccionar el flow en el selector |
|**Code Index** | Cuando el agent necesita conocer código almacenado **Locally**. | Especificar las rutas de las carpetas |

!!! info
    Se puede encontrar más información sobre esta ventana en el artículo [Knowledge Base File Window](../../../user-guide/etendo-copilot/setup-and-usage.md#knowledge-base-file-window).

!!!info "Image Files in Knowledge Base"
    Cuando los archivos se indexan en la base de conocimiento de un agent, **image files are handled separately** de los documentos de texto:
    
    - Los **Text documents** se indexan en la base de datos vectorial principal para búsqueda semántica
    - Los **Image files** (PNG, JPG, JPEG) se indexan en una **separate image database** para búsqueda de similitud visual
    - Esta base de datos de imágenes es utilizada por herramientas como la [OCR Tool](../available-tools/ocr-tool.md) para encontrar plantillas de referencia con marcadores visuales
    - La OCR Tool busca automáticamente en esta base de datos para encontrar imágenes de referencia similares que guían la extracción de datos
    - Cada agent mantiene su propia base de datos de imágenes, independiente de su base de conocimiento de texto

### Configuración avanzada
En la ventana Knowledge Base File, hay una sección de configuración avanzada que permite configurar las siguientes opciones en el algoritmo de splitting del contenido del archivo:
![Advanced features](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-12.png)

- **Skip Splitting**: recupera el documento completo como un único chunk, lo cual es útil para archivos pequeños.
- **Max. Chunk Size**: esta opción permite establecer el tamaño máximo (en tokens) de los chunks que se crearán cuando se divida el contenido. Esto es útil para evitar chunks muy grandes que pueden causar problemas de rendimiento. Dependiendo de los tipos de archivo, el algoritmo de splitting comprueba **separators** para dividir el contenido de forma semántica. Por ejemplo, en archivos markdown, el splitting se hace por encabezados, por lo que cada chunk contendrá el contenido de un encabezado y sus subencabezados. O en el caso de archivos Java, el splitting se hace por clases, por lo que cada chunk contendrá el contenido de una clase y sus métodos. Cuando se alcanza el tamaño del chunk, el contenido se divide en un nuevo chunk en el siguiente separator encontrado. Esto es útil para evitar chunks muy grandes que pueden causar problemas con el límite de tokens del model.  
- **Chunk Overlap**: esta opción permite establecer el solapamiento entre chunks para evitar perder información al dividir. El solapamiento es el número de tokens repetidos en cada chunk. Por ejemplo, si el tamaño del chunk es  100 y el solapamiento es 10, cada chunk contendrá 90 tokens únicos y 10 tokens repetidos del chunk anterior. Puede ser 0 si no quieres solapamiento entre chunks.
## Añadir Structured Outputs (JSON Schema)

A partir de la última versión, la ventana de configuración del Agent incluye un nuevo campo en la sección **Advanced Settings** llamado **`JSON Schema for Structured Outputs`**. Este campo acepta un objeto JSON Schema que el agent utilizará para validar y dar formato a sus respuestas.

Cómo usar el campo:

1. Abre la ventana de Agent y cambia a la pestaña **Advanced Settings**.
2. Localiza el campo **`JSON Schema for Structured Outputs`**.
3. Pega un objeto JSON Schema válido en el campo.
4. Guarda la configuración del agent y prueba con prompts de ejemplo.

Detalles importantes:

- El contenido debe ser un JSON válido que represente un JSON Schema. Usa un validador JSON si tienes dudas.
- El agent validará e intentará dar formato a su respuesta para que coincida con el schema.
- Si el agent no consigue satisfacer completamente el schema, devolverá un error estructurado describiendo los problemas de validación.

Ejemplo de schema (registro de Persona):

```json
{
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "department": {"type": "string"}
    },
    "required": ["name", "email"]
}
```

Casos de uso:

- Devolver datos estructurados de clientes para procesamiento posterior.
- Asegurar que la extracción de tareas siga un schema predecible para integraciones.
- Producir objetos de eventos listos para ser ingeridos por sistemas posteriores.

### Ejemplo: Contenido multilingüe (agent Bastian)

A continuación se muestra un ejemplo de JSON Schema usado en el agent `Bastian` (la wiki de Etendo indexada) para devolver contenido multilingüe y preguntas sugeridas.

```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/content-object.schema.json",
    "title": "Multilingual Content Object",
    "description": "An object containing content in English, its Spanish translation, and related suggested questions.",
    "type": "object",
    "properties": {
        "content_en": {
            "type": "string",
            "description": "The primary content of the object in the English language."
        },
        "suggested_questions": {
            "type": "array",
            "description": "A list of suggested questions related to the main content.",
            "items": {
                "type": "string",
                "description": "A single suggested question string."
            },
            "minItems": 1,
            "uniqueItems": true
        }
    },
    "required": [
        "content_en",
        "suggested_questions"
    ],
    "additionalProperties": false
}
```

#### Explicación de la estructura:

- **$schema / title / description**: Metadatos que documentan el schema y el draft utilizado.
- **type: object**: La respuesta debe ser un objeto JSON.
- **properties**:
    - `content_en` (string): Contenido principal en inglés.
    - `suggested_questions` (array[string]): Una o más cadenas de preguntas sugeridas relacionadas con el contenido. `minItems: 1` obliga a que haya al menos una sugerencia; `uniqueItems: true` evita duplicados.
- **required**: Garantiza que `content_en` y `suggested_questions` estén siempre presentes.
- **additionalProperties: false**: Evita campos extra más allá de los declarados; ayuda a mantener la salida estrictamente tipada.

Por qué este schema es útil:

- Garantiza que el agent siempre devuelva el texto en inglés más preguntas sugeridas accionables.
- Asegura el parseo programático sin extracción frágil de texto.

Ejemplo de uso (Bastian):

- Configura en **Advanced Settings** del agent `Bastian` el campo `JSON Schema for Structured Outputs` con el schema anterior.
- Haz al agent una pregunta como: `Summarize the Etendo installation steps for end users and suggest follow-up questions.`
- El agent responderá con un objeto JSON que coincide con el schema.

Campo JSON Schema configurado en Advanced Settings del Agent:

![Screenshot - JSON Schema field configured](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/agent-json-schema-field.png)

Pregunta realizada a `Bastian` y respuesta JSON estructurada recibida:

![Screenshot - Agent question and structured response](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/agent-bastian-response.png)

### Comportamiento del archivo de Knowledge Base

| Behavior | Cuándo usarlo | Funcionalidad | Limitaciones |
|--|--|------|--|
|**[Agent] Append the file content to the prompt**| Se recomienda cuando el volumen del contenido del archivo puede ser manejado por el model o la información es crucial para el trabajo del agent.| Cuando se construye el prompt, el contenido del archivo se insertará en cada ocurrencia de @alias@ dentro del prompt. Si el alias no estaba definido, el contenido del archivo se añade al final del prompt.| La longitud del archivo impacta directamente en la longitud del system prompt, que tiene un límite en cada módulo. Además, un prompt muy grande puede ralentizar las respuestas del agent.|
|**[Agent] Add to the agent as Knowledge Base**| Se recomienda usarlo cuando el volumen de información es mayor que el límite de tokens que el model puede manejar como 'prompt'. | El agent no "sabrá" el contenido del archivo de knowledge base desde el inicio de la ejecución, sino que estará equipado con una herramienta `Knowledge base Search` para buscar información en la knowledge base, funcionando como un motor de búsqueda. Esto es así porque la información se indexa en una base de datos de vectores, propia del agent, y la herramienta de búsqueda es la que permite buscar en ella por "Meaning". | El agent no podrá usar la información de la knowledge base para generar respuestas sin usar la herramienta `Knowledge base Search`. La herramienta devolverá un array de resultados, que puede usarse para generar una respuesta. La cantidad de resultados devueltos puede [configurarse](#advanced-settings) en la configuración del agent. El agent necesita **buscar** en el archivo de knowledge base para encontrar la información. Esto no se recomienda debido al rendimiento del agent.|
|**[User question] Append content to each question**| Se recomienda cuando los datos cambian con mucha frecuencia y necesitas disponer de los datos en el momento de cada pregunta. El contenido del archivo debe ser lo más corto posible.|Añade el contenido del archivo al final de cada mensaje.| Tiene un impacto directo en la longitud de los mensajes, que tienen límites de caracteres. También puede ralentizar las respuestas del agent si el mensaje es muy grande.|
|**[Agent] SPEC: Add as agent specification**| Puede usarse cuando el contenido del archivo es una OpenAPI Specification| La especificación no se añade a la solicitud, sino que se envía a Copilot. Cuando se construye el agent, la especificación se procesa y se generan herramientas automáticamente (para cada método y cada endpoint), que luego se añaden al agent. De este modo, el agent tiene herramientas para poder usar la Call Tool API sin necesidad de usar la Call Tool API y tener toda la OpenAPI Spec en el prompt.| Actualmente está en fase experimental.|

!!! info
    Puedes encontrar más información sobre esta ventana en la sección [Knowledge Tab](../../../user-guide/etendo-copilot/setup-and-usage.md#knowledge-tab).

!!! tip
    - **Remember the Synchronization**: Después de añadir/modificar/eliminar un archivo de knowledge base de un Agent, es necesario sincronizar el agent para aplicar los cambios. Esto no solo regenera/recarga el archivo de Knowledge Base, sino que también actualiza el Agent con los últimos cambios.
    - **Splitting**: Cuando se realiza la indexación en el archivo de knowledge base, el contenido se divide en chunks dependiendo del tipo de archivo. Por ejemplo, si el archivo es un markdown, el contenido se divide en chunks por los encabezados. Si los archivos no son grandes, es posible marcar `Skip Splitting` en la configuración del archivo de knowledge base. Esto evitará la división del contenido en chunks. Esto provoca que el contenido de los documentos se recupere como un único chunk, lo cual puede ser útil en algunos casos.

### Ejemplo: Añadir una Knowledge Base

El agent Copilot por defecto `Bastian` tiene un archivo de knowledge base basado en la documentación de Etendo desde su repositorio de GitHub. Copilot soporta el formato `.zip` para el comportamiento del archivo de knowledge base, extrayéndolo automáticamente e indexando los archivos internos.
En este caso, el archivo `ZIP` contiene la documentación de Etendo en formato markdown. El agent tiene el archivo de knowledge base configurado como `Remote File` y el comportamiento como `Add to the agent as Knowledge Base`. El agent tiene la siguiente configuración:

- Configurar el archivo de Knowledge Base:
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-1.png)

- Configurar el comportamiento del archivo de Knowledge Base (conectar el archivo de Knowledge Base con el Agent):
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-2.png)


    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-3.png){align=right width=250}

- Tras pedir al agent información sobre un tema, el agent buscará en el archivo de knowledge base y devolverá la información. El agent usará la herramienta `Knowledge Base Search` para buscar en el archivo de knowledge base.
    
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 


    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-4.png){align=right width=250}

- El agent devolverá una respuesta con la información encontrada en el archivo de knowledge base.
   <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
    <br> 
     

!!! tip
    Recuerda: explica en el prompt que el agent debe buscar en el archivo de knowledge base para encontrar la información. Esto ayudará al agent a saber cómo trabajar con el archivo de knowledge base.


## Añadir Tools
Al crear un agent, es posible añadir tools. Las tools son funcionalidades que permiten al agent realizar tareas específicas. Estas tools pueden usarse para interactuar con sistemas externos, manipular archivos u otras acciones. Las tools se añaden en la pestaña `Skills and Tools` de la ventana `Agent`.

!!! info "Available Tools"
    Las siguientes tools están disponibles en Etendo Copilot y se listan en la documentación del módulo [Etendo Copilot - ToolPack](../../../developer-guide/etendo-copilot/bundles/overview.md#etendo-copilot-toolpack). En el módulo **Etendo Copilot Toolpack** hay un conjunto de tools que pueden usarse para asistir en múltiples casos.

### Ejemplo: Añadir una Tool

Para añadir una tool a un agent, sigue estos pasos:

1. Abre la ventana `Agent`.
2. Ve a la pestaña `Skills and Tools`.
3. Añade la tool creando un registro en la pestaña `Skills and Tools`.

Por ejemplo, añadiremos una tool al agent `Task Definition Agent` para permitir escribir un archivo con la definición de la tarea. La tool será `Write File Tool`, que permite escribir un archivo con el contenido proporcionado.
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-5.png)

Después de añadir la tool, el agent la tendrá disponible para usarla. El agent puede usar la tool para escribir un archivo con la definición de la tarea.
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-6.png)

Podemos comprobar el archivo creado:
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-7.png)


## ¿Cómo permitir que Copilot interactúe con una API o con Etendo?
La funcionalidad más potente y útil de Etendo Copilot es la capacidad de interactuar con APIs (incluida la API de Etendo). Actualmente, el paradigma de los AI agents es automatizar y/o reutilizar lo que ya está **already done**. En otras palabras, la utilidad surge del hecho de que los AI agents pueden usar toda la lógica de negocio que ya está disponible.

### External API
La forma más habitual se basa en una combinación de una OpenAPI Specification y una tool que permite realizar solicitudes a esa API. Para ello, se necesitan los siguientes pasos:
- **Add the OpenAPI Specification**: La OpenAPI Specification es una forma estándar de describir una API. Esta especificación se añade como un archivo de Knowledge Base. Y se configura como `[Agent] Append the file content to the prompt`. Esto permitirá al agent conocer los endpoints y métodos de la API.
- **Add the API Call Tool**: La API Call Tool es una tool que permite realizar solicitudes a una API. Esta tool se añade como una tool en el agent. El agent puede usar esta tool para realizar solicitudes a la API.

### Etendo
Para Etendo, el proceso es un poco diferente. La principal diferencia es que podemos aprovechar la OpenAPI Specification generada automáticamente por los `Flows`, donde podemos definir un conjunto de endpoints a los que queremos dar acceso a nuestro agent.
Para saber más sobre cómo crear un flow en Etendo, consulta la guía [How to Document an Endpoint with OpenAPI](../../etendo-classic/how-to-guides/how-to-document-an-endpoint-with-openapi.md).
Los pasos para permitir que un agent interactúe con Etendo son:

- **Add the OpenAPI Specification**: Esta especificación se añade como un archivo de Knowledge Base de tipo `OpenAPI Flow Specification`. Cuando se selecciona este tipo, se muestra un selector con los flows disponibles, para seleccionar el flow que queremos usar. El comportamiento de este archivo puede ser `[Agent] Append the file content to the prompt`. Esto permitirá al agent conocer los endpoints y métodos de la API.
- **Add the API Call Tool**: La API Call Tool es una tool que permite realizar solicitudes a una API. Esta tool se añade como una tool en el agent. El agent puede usar esta tool para realizar solicitudes a la API.

!!!warning
    Si el comportamiento del archivo de Knowledge Base es `[Agent] Add to the agent as Knowledge Base`, el agent no podrá usar la información del archivo de knowledge base para generar respuestas sin usar la herramienta `Knowledge base Search`. Por lo tanto, el agent necesita **buscar** en el archivo de knowledge base para encontrar la información. Esto no se recomienda debido al rendimiento del agent.

### Auto Generation of Tools

Cuando la OpenAPI Specification se añade como un archivo de Knowledge Base de tipo `OpenAPI Flow Specification`, el agent generará automáticamente tools para cada método y endpoint de la API. Estas tools pueden usarse para realizar solicitudes a la API sin necesidad de configurar la API Call Tool. El agent tendrá una tool para cada método y endpoint de la API. Esta funcionalidad está actualmente en fase experimental.


### Ejemplo de interacción de Copilot con Etendo
Por ejemplo, crearemos un agent para crear Productos en Etendo, usando un flow ya definido con los endpoints necesarios para crear Productos, Categorías de Producto y Precios.

1. Primero, crearemos un nuevo archivo de Knowledge Base de tipo `OpenAPI Flow Specification` y seleccionaremos el flow `Product Flow`.

    !!!info
        Asegúrate de usar el agent que tenga los permisos necesarios para interactuar con los datos. En este caso, el agent debe tener los permisos necesarios para crear productos, categorías y precios en Etendo.

    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-8.png)

2. Después de añadir el archivo de Knowledge Base, crearemos el agent con un prompt que explique su alcance, estrategia y la solicitud que el usuario puede realizar. Además, añadiremos la OpenAPI Specification al prompt para permitir que el usuario conozca los endpoints y métodos de la API.

    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-9.png)

    !!!warning
        Recuerda sincronizar el agent para aplicar los cambios. Esto no solo regenera/recarga el archivo de Knowledge Base, sino que también actualiza el Agent con los últimos cambios.


3. Abre el Copilot Chat con el botón `✨Copilot` y selecciona el agent `Product Creator Agent` (si no aparece, asegúrate de tener acceso a él).

4. Puedes empezar a interactuar con el agent. El agent tendrá la OpenAPI Specification en el prompt y podrá usar la API Call Tool para realizar solicitudes a la API.

    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/how-to-create-an-agent-10.png)

## Problemas comunes

1. **Orphan Records After Module Uninstallation**

    Al desinstalar un módulo personalizado que contiene un agent con el que los usuarios han interactuado, el comando `./gradlew update.database` puede fallar debido a registros huérfanos en la tabla `ETCOP_CONVERSATION`.

    **Problema**: Aunque la tabla tiene configurada una restricción `onDelete=setNull`, el comando `update.database` no ejecuta esta acción automáticamente cuando se desinstala el módulo.

    **Solución**: Establece manualmente la columna `ETCOP_APP_ID` a `null` en la tabla `ETCOP_CONVERSATION` antes de ejecutar el comando update.database:

    ```sql
    UPDATE ETCOP_CONVERSATION 
    SET ETCOP_APP_ID = NULL 
    WHERE NOT EXISTS (
        SELECT 1 
        FROM ETCOP_APP 
        WHERE ETCOP_APP.ETCOP_APP_ID = ETCOP_CONVERSATION.ETCOP_APP_ID
    );
    ```

    Después de ejecutar esta sentencia SQL, puedes continuar con el comando `./gradlew update.database`.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.