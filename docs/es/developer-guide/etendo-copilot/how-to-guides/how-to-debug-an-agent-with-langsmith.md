---
tags:
  - Copilot
  - LangSmith
  - SDK
  - Observability
---

# Cómo depurar un agente con LangSmith

## Introducción
LangSmith es una potente herramienta de observabilidad que le permite realizar el seguimiento y analizar el rendimiento de sus aplicaciones de IA, si están basadas en LangChain/LangGraph. Proporciona una visión integral del comportamiento de su aplicación, lo que le permite identificar cuellos de botella, optimizar el rendimiento y mejorar la experiencia de usuario.
Este tutorial le guía a través de la configuración del SDK de observabilidad para realizar el seguimiento de Copilot en LangSmith.

## Crear una clave de API
Vaya al [Sitio web de LangSmith](https://smith.langchain.com/){target=_isblank} e inicie sesión. Si no tiene una cuenta, cree una.

Para crear una clave de API, navegue a la página de configuración de LangSmith. A continuación, haga clic en **Crear clave de API** y siga las instrucciones.

## Configurar su entorno

Configure su archivo `gradle.properties` para incluir las siguientes variables de entorno:

```properties
LANGSMITH_TRACING=true
LANGSMITH_API_KEY="your-langsmith-api-key"
LANGSMITH_WORKSPACE_ID="your-workspace-id"
```

- `LANGSMITH_TRACING`: Establézcalo en `true` para habilitar el trazado.
- `LANGSMITH_API_KEY`: Su clave de API de LangSmith.
- `LANGSMITH_WORKSPACE_ID` (Opcional): Su ID de espacio de trabajo en LangSmith. Si no se proporciona, se utilizará el espacio de trabajo "valor por defecto". Las ejecuciones, denominadas trazas, y los eventos se almacenarán bajo este espacio de trabajo.

Asegúrese de reiniciar Copilot para establecer las variables de entorno en el contenedor.

``` bash title="Terminal"
./gradlew resources.up --info
```

## Visualización desde LangSmith

- Una vez en LangSmith, estará disponible el acceso a los proyectos de su organización.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith.png)
- En *Proyectos de trazado*, las trazas se almacenarán bajo el espacio de trabajo definido en la variable `LANGSMITH_WORKSPACE_ID`.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-1.png)
- Seleccionar su espacio de trabajo le permite ver la traza de las consultas realizadas en Copilot y evaluar las respuestas.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-2.png)

## Ejemplo de uso

1. Realice una solicitud a cualquier agente de Copilot.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-3.png)
2. Al recibir una respuesta, si desea evaluar procesos internos o investigar incidencias, consulte la traza en LangSmith. 
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-4.png)
3. La entrada más reciente será la última solicitud realizada al agente. Acceda a ella para ver información detallada:
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-5.png)
    - A la izquierda, consulte todos los puntos de control desde la interacción del usuario hasta la respuesta.
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-6.png)
    - Acceda a cada endpoint, webhook o herramienta para ver cómo se forman las consultas.
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-7.png)
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-8.png)

    - Para las interacciones con OpenAI, hay disponible una opción llamada **Playground**.
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-9.png)

### Uso del Playground

Acceder al Playground le permite experimentar, probar y depurar cadenas de prompts e interacciones con modelos de lenguaje. Esta herramienta permite:

- Visualización de la ejecución de tareas en tiempo real.
- Análisis del rendimiento del modelo.
- Detección de errores e ineficiencias para la optimización y mejora de Copilot.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-10.png)

- Puede probar diferentes prompts o interacciones de usuario sin volver al agente. Por ejemplo, si desea ver cómo responde un agente con un prefijo como "ETHRT":

- Busque la sección de consulta del usuario en el Playground y modifique el prefijo.

    === "ANTES"
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-11.png)

    === "AHORA"
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-12.png)

- Seleccione **Iniciar** para volver a ejecutar con el prefijo.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-13.png)

- De forma inmediata, observe la traza ejecutándose con el prefijo **ETHRT**.
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-14.png)

- Para ejecutar múltiples interacciones para probar la consistencia del agente:

    - Haga clic en la flecha junto a **Iniciar**.
    - Deseleccione **Habilitar streaming**.
    - Ajuste las **Repeticiones** al número deseado, por ejemplo, tres veces.
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-15.png)
        ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-16.png)
    - Pulse **Iniciar** de nuevo. La consulta se ejecutará tres veces.
        ![ alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-17.png)
Esta funcionalidad es crucial para probar diversas solicitudes y modificar prompts para cumplir los requisitos.

## Depuración del prompt del sistema
El Playground le permite depurar el prompt utilizado en el agente. Esto es útil para mejorar el comportamiento del agente en caso de resultados inesperados.
Como hemos visto anteriormente, en LangSmith puede ver las ejecuciones de herramientas y otras acciones realizadas por el agente, según lo determinado por el LLM. Dado que el razonamiento se origina en el LLM, estos son los puntos clave en los que podemos intervenir para optimizar el comportamiento. 

Al cargar el Playground, verá:

- El prompt del sistema.
- La secuencia de mensajes, ejecuciones de herramientas y respuestas hasta ese momento.

Al ejecutar **Iniciar**, solicita la respuesta del LLM en función del prompt del sistema y la conversación. A partir de ahí, puede recibir una respuesta de texto o una instrucción para ejecutar una herramienta con parámetros específicos.

Entonces, si al analizar la traza de ejecución encontramos dónde el agente "cometió un error" o "decidió incorrectamente", podemos ir a ese punto y ajustar el prompt para mejorar su razonamiento. Además, podemos ejecutar la solicitud varias veces para asegurarnos de que la decisión correcta sea consistente y no se deba al azar, ya que los LLM no son deterministas en situaciones definidas de forma imprecisa.

### Ejemplo

En este ejemplo, veremos cómo mejorar el prompt de un agente que no está proporcionando la respuesta esperada.
En este caso, utilizaremos el **Agente redactor** con el siguiente prompt:

```text
Your task is to write notes.
The path must be ./[filename].txt
```
La solicitud es:
```text
Create a note that reminds me to "call my boss tomorrow"
```

Al inspeccionar la traza, puede ver la decisión del LLM de ejecutar **WriteFileTool** con estos parámetros:
```text
filepath: ./reminder.txt
content: call to my boss, tomorrow
override: false
```
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-18.png)

Suponga que queremos que el agente utilice snake_case para los nombres de archivo y un formato más formal y estructurado para las notas.
Podemos abrir el Playground, ver el prompt del sistema y cambiarlo a:
```text
Your task is to write notes.
The path must be ./[filename].txt

- The file name must be in snake_case.
- The format of the note is: 
DATE: 
DESCRIPTION:

```
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-19.png)

Para verificar el cambio, podemos volver a ejecutar la solicitud. Para obtener resultados más fiables, podemos ejecutarla varias veces para asegurarnos de que el comportamiento sea consistente.

Después de ejecutar la solicitud, podemos ver que el nombre del archivo ahora está en snake_case y el formato de la nota está más estructurado con los requisitos que establecimos en el prompt.
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-debug-an-agent-prompt-with-langsmith/how-to-debug-an-agent-prompt-with-langsmith-20.gif)

Si el resultado no es consistente, podemos seguir iterando sobre el prompt hasta obtener el resultado esperado.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.