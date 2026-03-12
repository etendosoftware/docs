---
title: Guía de usuario - Etendo Copilot - Primeros pasos
tags: 
 - Etendo Copilot
 - Integración de IA
 - Herramientas inteligentes
 - Agentes
 - Guía de usuario
---

![cover-getting-started.png](../../assets/getting-started/overview/cover-getting-started.png)

# Guía de usuario - Etendo Copilot - Primeros pasos

## Visión general

Etendo Copilot es una potente herramienta integrada en la interfaz de Etendo, o accesible vía API, que proporciona una forma eficiente de interactuar con agentes y utilizar herramientas desarrolladas para resolver problemas específicos. Es un proyecto innovador diseñado para agilizar sus procesos aprovechando el poder de la Inteligencia Artificial. Esta página le guiará a través de las principales funcionalidades de Etendo Copilot.

!!! info
    Para instalar Etendo Copilot, puede leer la guía de [Instalación de Copilot](../../developer-guide/etendo-copilot/installation.md) en la sección de la guía del desarrollador.

!!! note
    Recuerde que, para utilizar esta funcionalidad, es necesario configurar una API Key. Para ello, puede usar una propia, o puede ponerse en contacto con el equipo de soporte de Etendo para adquirir una.


![Chat de Copilot](../../assets/user-guide/etendo-copilot/getting-started/copilot.png){align=right  width="300"}

## ¿Qué es Etendo Copilot?

En esencia, Etendo Copilot es una iniciativa pionera que redefine cómo los desarrolladores y los usuarios interactúan con herramientas e información. Gira en torno a un componente central, el *Agente*, que actúa como el cerebro detrás de la delegación de tareas. Este Agente cuenta con módulos secundarios denominados *Herramientas*. La comunicación fluida entre estos componentes se facilita mediante una API RESTful, garantizando un modelo de interacción sin estado y escalable.

<br clear="all"> 

### Funcionalidades clave

- **Integración sin esfuerzo**: Etendo Copilot se integra de forma fluida en su entorno, añadiendo una capa adicional de inteligencia a su flujo de trabajo.
- **Asistencia bajo demanda**: Envíe sus consultas a Etendo Copilot, y el Agente le guiará hacia la Herramienta más adecuada para el trabajo.
- **Experiencia diversa**: Nuestra selección de Herramientas, en constante crecimiento, cubre una amplia gama de dominios, garantizando que siempre tenga la solución adecuada.
- **Agente LangGraph**: Este tipo de agente funciona como gestor de otros agentes y le permite crear equipos de trabajo.
- **Asistente multimodelo**: Estos agentes pueden realizar tareas específicas en lenguaje natural y proporcionar respuestas contextualizadas, permitiendo la implementación de múltiples modelos de IA, el uso de una base de datos vectorial propietaria y la gestión interna de memoria. Este tipo de agente puede utilizarse con modelos de múltiples proveedores como *Anthropic*, *Gemini* o *OpenAI*, entre otros.
- **Adjuntar archivos**: Etendo Copilot permite a los usuarios adjuntar uno o varios archivos en la conversación.
- **Compartición de contexto**: Etendo Copilot puede capturar y compartir automáticamente el contexto de su sesión actual de Etendo, como registros seleccionados o ventanas activas. Esto elimina la necesidad de introducir información manualmente, agilizando los flujos de trabajo y mejorando la eficiencia.




## Asistente (Agente)

Los agentes son entidades inteligentes que toman decisiones en tiempo real sobre qué Herramienta es la más adecuada para responder a una consulta específica. Esto garantiza que siempre reciba la asistencia más precisa y eficiente.

<figure markdown="span">
  ![Diagrama de Copilot](../../assets/user-guide/etendo-copilot/getting-started/copilot-diagram.png)
  <figcaption>Diagrama del Asistente multimodelo</figcaption>
</figure>


Cada agente se configura con un conjunto de instrucciones denominado **Prompt**, una base de conocimiento (denominada en Etendo como **Archivo de KnowledgeBase**) y una colección de **Habilidades o herramientas**.

- Cuando usted realiza una pregunta, el agente evalúa su solicitud y selecciona la base de conocimiento o la herramienta más adecuada para proporcionar una respuesta relevante.
- Además, los agentes de tipo LangGraph actúan como **gestores**, capaces de delegar consultas a otros agentes especializados y coordinar las respuestas entre ellos. Esto permite respuestas asertivas y colaborativas. 
- También existen **Asistentes multimodelo**, que pueden gestionar tareas o flujos de trabajo específicos utilizando múltiples modelos de IA.

Los agentes pueden organizarse en módulos o crearse directamente dentro de sus entornos de Etendo, ofreciendo flexibilidad en la forma en que estructura sus flujos de trabajo impulsados por IA.

!!! info 
    Para más información, visite la documentación de la ventana [Agente](../etendo-copilot/setup-and-usage.md#agent-window).


### Habilidad/Herramienta

Cada herramienta representa un proyecto dedicado y autónomo, diseñado para destacar en tareas especializadas. Ya sea traducción, análisis de texto o manipulación de datos, el conjunto diverso de herramientas opera en coordinación fluida.  

!!! info 
    Para una visión general de las herramientas disponibles y sus detalles técnicos, consulte [Herramientas de Copilot](../../developer-guide/etendo-copilot/available-tools/overview.md) en la sección de la Guía del desarrollador.

### Base de conocimiento

En muchos casos, necesitamos que el agente disponga de información específica que el modelo no tiene por defecto, por lo que generamos una Base de conocimiento. Esto nos permitirá **entrenar** a nuestro agente con información específica.

!!! info 
    Para más información visite la documentación de la ventana [Archivo de Knowledge Base](../etendo-copilot/setup-and-usage.md#knowledge-base-file-window).


## Interfaz de Copilot

### Barra de navegación

En la barra de navegación principal de Etendo, encontrará un icono de Copilot que le lleva al pop-up del chat.

Aquí, puede seleccionar un agente e iniciar una conversación con él. Copilot facilita la comunicación con tipos `Langchain Agent` o `Multi-Model Assistant`.
!!!note
    De forma predeterminada, Copilot abrirá el último agente utilizado previamente.

![Barra de navegación de Copilot](../../assets/user-guide/etendo-copilot/getting-started/copilot-navbar.png)

### Barra de herramientas

En cualquier ventana de Etendo, haga clic en el botón de Copilot en la barra de herramientas para abrir el chat. Copilot recibirá automáticamente el contexto de su pestaña actual o de los registros seleccionados, por lo que no necesita introducir los detalles manualmente.

![Barra de herramientas](../../assets/user-guide/etendo-copilot/getting-started/toolbar.png)

**Conciencia de contexto**

Etendo Copilot puede aprovechar el contexto de la ventana o del registro actualmente activo en Etendo. Al hacer clic en el botón de la barra de herramientas, el contexto actual se actualiza automáticamente.

- **Contexto de formulario**: Si tiene un formulario abierto (por ejemplo, un pedido de venta o un registro de cliente), Copilot recupera los campos clave y cualquier edición no guardada, ofreciéndole sugerencias o validaciones en tiempo real.
- **Contexto de rejilla**: Cuando se selecciona una fila en una rejilla, Copilot captura los detalles de esos registros específicos, enviando a Copilot toda la información relevante para que usted pueda recibir recomendaciones relevantes basadas en IA.
- **Contexto de pestaña y ventana**: En entornos con múltiples pestañas, el contexto debe enviarse a Copilot cada vez que usted cambie de una vista a otra (p. ej., de Pedidos a Productos).



### Adjuntar archivos

![Ejemplo de pedido de compra](../../assets/user-guide/etendo-copilot/getting-started/purchase-order-example.png){align=left  width="400"}

Etendo Copilot permite a los usuarios adjuntar uno o más archivos para que los agentes los procesen. Esta funcionalidad admite varios formatos de archivo, como `.pdf`, `.csv`, `.jpg`, y más, lo que aporta flexibilidad a los casos de uso. Sin embargo, la capacidad de interpretar y procesar estos archivos depende de la configuración específica del agente, de las herramientas definidas y del modelo subyacente utilizado.

Esta funcionalidad garantiza que los usuarios puedan incorporar datos externos de forma fluida en sus flujos de trabajo, ya sea para analizar documentos, analizar hojas de cálculo o procesar imágenes. Los agentes y las herramientas pueden adaptarse para abordar requisitos específicos en función del tipo de archivos adjuntos, proporcionando respuestas contextualizadas e inteligentes.

Por ejemplo, puede adjuntar un pedido de compra en formato PDF y pedir al agente que cree el pedido de compra en Etendo. Como se muestra, el agente genera el pedido respetando el tercero, las fechas, los productos y los importes.  

![Experto de compras](../../assets/user-guide/etendo-copilot/getting-started/purchase-expert.png)


### Modo de visualización


#### Modos de visualización

<figure markdown>
![](../../assets/user-guide/etendo-copilot/getting-started/regular-size-copilot.png){align=right width=300}
<br><br>
**Pop-up** <br>
De forma predeterminada, Copilot funciona como una ventana pop-up, proporcionando un acceso cómodo como agente integrado en cualquier ventana activa.
</figure>

<figure markdown>
**Pantalla completa** <br>
Utilice el modo de pantalla completa para una experiencia más cómoda durante conversaciones largas cuando no sea necesario visualizar Etendo.

Etendo Copilot ofrece gestión de conversaciones mediante un **selector de conversaciones** para revisar y cambiar entre interacciones anteriores, un botón de **Nueva conversación** para iniciar temas o tareas nuevas, y la **generación automática de títulos de conversación**, que crea títulos significativos para facilitar la identificación y organización de los diálogos.
![Chat a pantalla completa](../../assets/user-guide/etendo-copilot/getting-started/full-screen-copilot.png)
</figure>

<figure markdown>
![](../../assets/user-guide/etendo-copilot/getting-started/minimized-copilot.png){align=right width=200} <br>
**Minimizado** <br>
La interfaz de Copilot también puede minimizarse. En este caso, una burbuja de Copilot estará activa en la parte inferior derecha de la pantalla.
</figure>

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.