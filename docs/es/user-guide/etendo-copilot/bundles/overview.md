---
title: Copilot Extensions Bundle
tags: 
    - Extensiones de Copilot
    - Herramientas de IA
    - Funcionalidades de agentes
    - Módulos de Etendo
    - Guía de integración
---

!!! warning
    Actualmente, estamos migrando la terminología de *Asistente* a *Agente*. Este cambio se reflejará en la documentación pronto. Donde vea *Asistente*, considérelo como *Agente* y viceversa.

# Paquete de extensiones de Copilot

:octicons-package-16: Javapackage: `com.etendoerp.copilot.extensions`

:material-store: Etendo Marketplace:  [Paquete de extensiones de Copilot](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}

## Visión general

El Paquete de extensiones de Copilot incluye funcionalidades que le ayudan a agilizar sus tareas diarias utilizando inteligencia artificial.


## Módulo

### Etendo Copilot

:octicons-package-16: Javapackage: `com.etendoerp.copilot`

Etendo Copilot es una plataforma que optimiza el tiempo de desarrollo con herramientas habilitadas por IA para reducir el tiempo de desarrollo y mejorar la calidad del desarrollo. Además, permite la creación de agentes para automatizar procesos o incluso trabajar con bases de conocimiento especializadas.
Como módulo principal del Paquete de extensiones de Copilot, **Etendo Copilot** contiene un conjunto de ventanas donde puede crear, gestionar e interactuar con Agentes impulsados por IA.

!!! info
    Para más información, visite [Etendo Copilot - Guía de usuario](../../../user-guide/etendo-copilot/setup-and-usage.md).


#### Agentes

##### Bastian

Este módulo incluye **Bastian**, un agente equipado con la documentación de Etendo indexada como base de conocimiento. Bastian permite a los usuarios buscar información dentro de la documentación utilizando consultas en lenguaje natural, proporcionando respuestas rápidas y precisas a sus preguntas.

### Agentes de Etendo Copilot

:octicons-package-16: Javapackage: `com.etendoerp.copilot.agents`

El módulo **Agentes de Copilot** es una colección de agentes que pueden utilizarse para realizar tareas básicas interactuando con Etendo, pero el propósito principal es utilizarse como base (o plantilla) para crear nuevos agentes. Aprovechando la funcionalidad de clonación en los agentes y la base de conocimiento, pueden replicarse y crearse agentes personalizados muy fácilmente.


#### Agentes

##### Supervisor de inicialización de datos

<iframe width="560" height="315" src="https://www.youtube.com/embed/cn__oNPH5X0?si=yPiVW3to9X7UOsG6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Este es un agente supervisor que delega y orquesta tareas de inicialización para el cliente (creación de terceros iniciales, productos, etc.).
![alt text](../../../assets/user-guide/etendo-copilot/bundles/overview/client-initialization-graph.png)
Este supervisor tiene los siguientes agentes:

- **Generador de terceros**: Este agente crea terceros.
- **Generador de productos**: Este agente gestiona los productos y las entidades relacionadas en el sistema. Proporciona una funcionalidad completa para:
    - **Creación de productos**: Crear nuevos productos con categorías, unidades de medida y asociaciones con tarifas.
    - **Gestión de categorías de producto**: Crear nuevas categorías o buscar las existentes para organizar los productos de forma eficiente.
    - **Gestión de precios**: Asignar precios a los productos en diferentes versiones de tarifa.
    - **Búsqueda**: Encontrar productos o categorías existentes en función de varios criterios.
    - **Actualización**: Modificar la información del producto, las categorías o los detalles de precios.
    - **Consulta de información**: Mostrar detalles de productos, categorías, precios y tarifas.
    - **Automatización de procesos**: Automatizar flujos de trabajo repetitivos dentro de estas funciones de gestión de productos.
- **Generador de inventario físico**: Este agente crea inventarios físicos para añadir stock a los productos.
- **Creador de tareas masivas**: Este agente crea tareas masivas basadas en un archivo zip o en un archivo CSV/XLSX. Este agente permite crear tareas en masa para cargar grandes cantidades de datos en los otros agentes. Por ejemplo, puede utilizarse para crear una gran cantidad de terceros, productos a partir de un archivo CSV, etc. Además, este agente tiene la posibilidad de obtener información directamente desde Google Spreadsheets.

    !!! info
        Para más información, puede leer [Cómo crear un agente de tareas de hoja de cálculo](../../../developer-guide/etendo-copilot/how-to-guides/how-to-create-an-spreadsheet-tasks-agent.md)

##### Supervisor de facturas

<iframe width="560" height="315" src="https://www.youtube.com/embed/65PPI9PN7f4?si=G7tS_GO1HKWRztQD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

El Supervisor de facturas es un agente de orquestación responsable de gestionar la creación de facturas de compra en Etendo. Este supervisor decide cómo enrutar los datos entrantes (archivos ZIP, archivos individuales o entrada del usuario) hacia los agentes adecuados. 
    
![alt text](../../../assets/user-guide/etendo-copilot/bundles/overview/invoice-expert-graph.png)

- Gestionar la creación de facturas de compra individuales o masivas.
- Extraer y validar los datos de la factura.
- Delegar la creación de tareas para el procesamiento por lotes.

Este supervisor tiene los siguientes agentes:

- **Creador de tareas masivas**: Creador de tareas masivas para iterar sobre archivos ZIP o Excel/CSV, utilizado cuando se recibe un archivo ZIP con múltiples facturas. Además, este agente tiene la posibilidad de obtener información directamente desde Google Spreadsheets.
    
    !!! info
        Para más información, puede leer [Cómo crear un agente de tareas de hoja de cálculo](../../../developer-guide/etendo-copilot/how-to-guides/how-to-create-an-spreadsheet-tasks-agent.md)

- **Experto en Factura (Proveedor)**: Agente experto en la gestión de facturas de compra para Etendo. Gestiona todo el proceso de creación de la factura, extrae y valida la cabecera y las líneas de la factura. Finalmente, invoca APIs para insertar datos y proporciona una validación final.

    Cuando este agente procesa una factura, realiza una validación del importe total. Para proporcionar feedback al usuario, se añade una sección **Copilot** a la ventana **Factura (Proveedor)** con un campo llamado **Feedback de Copilot**. El agente actualiza este campo con el resultado de la validación:
    ![Feedback de Copilot](../../../assets/user-guide/etendo-copilot/bundles/overview/copilot-feedback.png)
    
    - **Correcto**: El total de la factura coincide con los datos extraídos y está listo para su procesamiento.
    - **Requiere revisión manual**: Existe una discrepancia o un problema que requiere que un usuario humano verifique los detalles de la factura.

    !!! tip
        Para mejorar la precisión de la extracción de datos, consulte la guía [Cómo mejorar el reconocimiento OCR](../../../developer-guide/etendo-copilot/how-to-guides/how-to-improve-ocr-recognition.md).


##### Experto en pedidos

Este agente es un agente supervisor que delega y orquesta la creación de pedidos de compra y de venta. 
    
![alt text](../../../assets/user-guide/etendo-copilot/bundles/overview/order-expert-graph.png)

Este supervisor tiene los siguientes agentes:

- **Experto en pedidos de compra**: Este agente crea pedidos de compra.
- **Experto en pedidos de venta**: Este agente crea pedidos de venta.

##### Lector de ZIP

Este agente lee un archivo zip y devuelve las rutas de los archivos dentro del zip. Es útil para añadirlo a un agente supervisor para encadenar el resultado de descompresión con otros agentes.  

!!! info
    Todos los subagentes presentados pueden utilizarse de forma individual si es necesario.

### Etendo Copilot Toolpack

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

El **Etendo Copilot Toolpack** es una colección de herramientas que ayudan a los **desarrolladores** a añadir funcionalidades a los agentes, como solicitar a una API, enviar un correo electrónico, leer un archivo, escribir un archivo y más.

!!! info 
    Para más información, visite la [Toolpack - Guía del desarrollador](../../../developer-guide/etendo-copilot/bundles/overview.md#etendo-copilot-toolpack), donde encontrará una lista detallada de las herramientas disponibles, instrucciones sobre cómo utilizarlas y una guía para desarrollar nuevas herramientas.


#### Agentes

##### Experto en SQL

Este agente está diseñado para ayudar a los usuarios a leer información de la base de datos. Permite a los usuarios hacer preguntas en lenguaje natural y obtener la consulta SQL que recupera la información que necesitan. Para preservar la seguridad de la base de datos, la consulta se preprocesa con filtros para recuperar únicamente los datos accesibles por el usuario.

!!!info
    Para más información, visite [Experto en SQL](sql-expert.md).



### Subapp de Etendo Copilot

:octicons-package-16: Javapackage: `com.etendoerp.subapp.copilot`

La **Subapp de Etendo Copilot** está diseñada para integrarse sin problemas con las funcionalidades existentes de Etendo Copilot, ampliando su funcionalidad a dispositivos móviles y tabletas. Esta subaplicación permite a los usuarios interactuar con agentes de Copilot impulsados por IA directamente desde sus dispositivos móviles, mejorando la productividad y la accesibilidad en movilidad.

La Subapp de Etendo Copilot ofrece funcionalidades clave como la capacidad de **adjuntar archivos, interactuar con agentes de Copilot y acceder a datos específicos** en función del rol del usuario. Los agentes aparecen dinámicamente según el rol asignado al usuario, garantizando una experiencia personalizada adaptada a sus responsabilidades dentro del sistema.

Con compatibilidad tanto para teléfonos móviles como para tabletas, esta subaplicación garantiza flexibilidad en la forma en que los usuarios pueden acceder y aprovechar los agentes de Copilot, facilitando flujos de trabajo más fluidos en diferentes dispositivos.

!!! info
    Para más información sobre las configuraciones de subaplicaciones, visite [Configurar roles y subapps dinámicas](../../etendo-mobile/getting-started.md#configure-roles-and-dynamic-subapps).


![alt text](../../../assets/user-guide/etendo-copilot/bundles/overview/etendo-copilot-subapp2.png){ width="500" }
![alt text](../../../assets/user-guide/etendo-copilot/bundles/overview/etendo-copilot-subapp1.jpg){ width="170" }



### Asistente de desarrollo

:octicons-package-16: Javapackage: `com.etendoerp.copilot.devassistant`

El **Asistente de desarrollo** es un conjunto de agentes que ayuda a realizar tareas relacionadas con el desarrollo en Etendo, como crear una nueva ventana, crear un nuevo módulo, crear procesos, etc.

!!!info
    Para más información, visite la guía del desarrollador: [Asistente de desarrollo](../../../developer-guide/etendo-copilot/bundles/dev-assistant.md).


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.