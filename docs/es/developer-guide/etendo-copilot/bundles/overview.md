---
title: Guía del desarrollador - Extensiones de Copilot
tags: 
    - Extensiones de Copilot
    - AI
    - Herramientas
    - Agentes
    - Desarrollador
---


# Extensiones de Copilot

:octicons-package-16: Javapackage: `com.etendoerp.copilot.extensions`

:material-store: Etendo Marketplace:  [Bundle de Copilot Extensions](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}

!!! warning
    Actualmente, estamos migrando la terminología de *Assistant* a *Agent*. Este cambio se reflejará en la documentación pronto. Donde vea *Assistant*, considérelo como *Agent* y viceversa.

## Visión general

El Bundle de Copilot Extensions incluye funcionalidades para desarrolladores para ayudarles a desarrollar agentes de AI que puedan asistir a los usuarios en sus tareas diarias.

## Módulo (menu)

### Etendo Copilot

:octicons-package-16: Javapackage: `com.etendoerp.copilot`

El módulo Etendo Copilot incluye un conjunto de ventanas donde puede crear, gestionar e interactuar con Agentes impulsados por AI. Por defecto, el módulo incluye **Bastian**, que es un agente con la documentación de Etendo indexada como base de conocimiento.

**Agentes incluidos**
 
- **Bastian**: es un agente con la documentación de Etendo indexada como base de conocimiento.
    - **Prompt**: El agente tiene un prompt que explica su propósito, la solicitud que el usuario puede realizar y la respuesta que el agente proporcionará. Por ejemplo, en su prompt hay indicaciones para recuperar el enlace del artículo al responder una pregunta. Además, incluye una breve explicación de particularidades de la Wiki de Etendo y del formato de los artículos.
    - **Base de conocimiento**: El agente tiene una base de conocimiento compuesta por la Wiki de Etendo, indexada en el agente. El archivo de Base de conocimiento es de tipo `Remote File`, apuntando al repositorio de GitHub de la Wiki de Etendo. Cuando el agente se sincroniza, el agente descargará el archivo y lo indexará. 
    
    !!! info 
        Para más información, visite la guía [Cómo crear un agente](../../etendo-copilot/how-to-guides/how-to-create-an-agent.md#add-a-knowledge-base).

### Etendo Copilot Toolpack

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

**Herramientas incluidas**

!!!info
    Puede ver la lista completa de herramientas en la sección [Herramientas](../available-tools/overview.md).
    
!!! note
    Para más información, visite la guía [Cómo crear herramientas de Copilot](../how-to-guides/how-to-create-copilot-tools.md).

**Agentes incluidos**

- [Experto SQL](../../../user-guide/etendo-copilot/bundles/sql-expert.md): Este agente está diseñado para ayudar a los usuarios a leer información de la base de datos. Permite a los usuarios hacer preguntas en lenguaje natural y obtener la consulta SQL que recupera la información que necesitan. Para preservar la seguridad de la base de datos, la consulta se preprocesa con filtros para recuperar únicamente los datos accesibles por el usuario.

    - **Prompt**: El agente tiene un prompt que explica su propósito, la solicitud que el usuario puede realizar y la respuesta que el agente proporcionará. Incluye una breve explicación de particularidades de la base de datos de Etendo Classic. Además, incluye una lista de ejemplos de funciones y columnas comunes que tienen las tablas.
    - **Base de conocimiento**: El agente tiene una base de conocimiento compuesta por una especificación OpenAPI (de un flujo con los endpoints que el agente puede usar) que se añade al prompt.
    - **Herramienta de llamada a API**: El agente utiliza la Herramienta de llamada a API para realizar las solicitudes a Etendo Classic. 

    !!! note
        Para más información, visite la guía [Cómo permitir que Copilot interactúe con Etendo Classic](../how-to-guides/how-to-create-an-agent.md#how-to-allow-copilot-to-interact-with-etendo-classic).


### Etendo Copilot Agents

:octicons-package-16: Javapackage: `com.etendoerp.copilot.agents`

**Agentes incluidos**

El módulo de agentes incluye un conjunto de agentes que pueden utilizarse para asistir a los usuarios en sus tareas diarias. El módulo incluye los agentes descritos en la [Guía de usuario - Etendo Copilot Agents](../../../user-guide/etendo-copilot/bundles/overview.md#etendo-copilot-agents)

- **Prompt**: Los agentes tienen un prompt que explica su propósito, la solicitud que el usuario puede realizar y la respuesta que el agente proporcionará. Además, incluye una breve explicación de las particularidades de cada agente, explicando cómo buscar información, qué debe indicarse puntualmente y qué debe averiguarse. También incluyen información sobre el orden en el que deben realizarse las solicitudes a Etendo Classic, y de cuáles debemos usar qué valores de una a otra. 
- **Base de conocimiento**: La mayoría de estos agentes utilizan especificaciones OpenAPI en su base de conocimiento, añadiéndolas a su prompt para entender cómo usarlo. Puede encontrar más información sobre cómo permitir que el agente interactúe con Etendo Classic en la guía [Cómo permitir que Copilot interactúe con Etendo Classic](../how-to-guides/how-to-create-an-agent.md#how-to-allow-copilot-to-interact-with-etendo-classic).
- **[Herramienta de llamada a API](../available-tools/api-call-tool.md)**: Los agentes utilizan la Herramienta de llamada a API para realizar las solicitudes a Etendo Classic.
- **[Herramienta OCR](../available-tools/ocr-tool.md)**: Los agentes utilizan la Herramienta OCR para leer la información de las imágenes que se adjuntan a las solicitudes. Esta herramienta es necesaria si el modelo seleccionado para el agente no es capaz de leer por sí mismo la información de las imágenes.
- **[Herramienta de creación masiva de tareas](../available-tools/task-creator-tool.md)**: El agente llamado `Bulk task creator` utiliza la Herramienta de creación masiva de tareas para crear tareas masivas basadas en un archivo `ZIP` o un archivo `CSV/XLSX`. Este agente permite crear tareas de forma masiva para cargar grandes cantidades de datos en segundo plano.
- **Arquitectura Langgraph Supervisor**: Los agentes supervisores se construyen utilizando la arquitectura Langgraph Supervisor. Puede encontrar más información sobre esta arquitectura en la guía [Cómo crear un agente - Arquitectura Langgraph Supervisor](../../etendo-copilot/how-to-guides/how-to-create-an-agent.md#Langgraph-Supervisor-architecture).


### Dev Assistant

:octicons-package-16: Javapackage: `com.etendoerp.copilot.devassistant`

<iframe width="560" height="315" src="https://www.youtube.com/embed/58U9LThdTGo?si=kSxA3MAf22U8fdHh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

El módulo **Dev Assistant** incluye múltiples **agentes de desarrollo** que facilitarán a los desarrolladores los procesos de creación de botones, ventanas, solapas, campos, procesos en segundo plano, Event Handlers, informes Jasper y mucho más.

!!!info
    Para más información, visite [Dev Assistant - Guía del desarrollador](../bundles/dev-assistant.md).

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.