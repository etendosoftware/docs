---
title: Cómo usar un Agente como servidor MCP
status: beta
tags:
    - Cómo hacer
    - Copilot
    - Servidor MCP
    - Model Context Protocol (MCP)
    - Herramientas
    - Agentes
---

# Cómo usar un Agente como servidor MCP

## Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

Esta guía muestra cómo conectarse a agentes de Etendo Copilot usando el [Model Context Protocol (MCP)](../concepts/model-context-protocol.md). Cada agente expone automáticamente un servidor MCP al que puede conectarse desde varios clientes compatibles con MCP como Claude Desktop, VS Code, Gemini CLI y aplicaciones personalizadas.

Cada agente de **Etendo Copilot** proporciona un endpoint de servidor MCP que expone:

- **Herramientas**: capacidades del agente (llamadas a API, operaciones de archivos, búsqueda de conocimiento).
- **Prompts**: plantillas preconfiguradas para tareas comunes.
- **Recursos**: acceso a documentos, configuraciones y datos.

### Modos de conexión

Existen dos tipos de comunicación con el servidor MCP, ambos establecidos a través de la API expuesta por cada agente:

- **Modo Simple**: proporciona acceso al agente como una "caja negra" externa. El cliente interactúa de forma natural con el agente, sin visibilidad de su configuración interna, herramientas o prompt.  
- **Modo Directo**: proporciona acceso directo al prompt y a las herramientas del agente. En este modo, el cliente externo se comporta como si fuera un agente de Etendo, con acceso a las mismas herramientas, datos y definiciones disponibles para el agente interno.

Elija cómo desea interactuar con el agente:

| Modo | Descripción | Mejor para |
|------|-------------|----------|
| **Simple** | Chatear de forma natural con el agente | Conversaciones, preguntas, uso general |
| **Directo** | Ejecutar herramientas específicas directamente | Automatización, flujos de trabajo, desarrollo |


### Arquitectura del servidor MCP en Etendo Copilot

Cada agente de Etendo Copilot expone automáticamente un endpoint de servidor MCP que proporciona:

- **Herramientas de interacción**: herramientas que facilitan la comunicación entre el agente y el cliente MCP, como `ask_agent` para enviar preguntas y recibir respuestas.
- **Herramientas del agente**: funciones que el agente puede ejecutar.
- **Recursos**: datos estáticos o dinámicos a los que se puede acceder (documentos, configuraciones, logs, etc.).
- **Prompts**: plantillas de prompt preconfiguradas para tareas comunes.

El servidor MCP se ejecuta junto al agente y se comunica usando transporte `HTTP` con `Server-Sent Events (SSE)` opcional para respuestas en streaming.

### Tipos de agente y modos de conexión

Etendo Copilot admite dos tipos de agentes, cada uno con dos modos de conexión. El tipo de agente define el rol, y el modo define cómo interactúa con él.

| Tipo de agente     | Modo Simple (Hablar)                              | Modo Directo (Control)                                              |
|-------------------|---------------------------------------------------|---------------------------------------------------------------------|
| **Multi-Model**   | Usar `ask_agent` para chatear de forma natural    | Acceder a todas las herramientas directamente + `get_agent_prompt` para la configuración |
| **LangGraph**     | Usar `ask_agent_supervisor` para hablar con el supervisor | Usar `ask_agent_<MemberName>` para miembros del equipo + `get_agent_prompt` |


**Agente Multi-Model**: un único agente que combina múltiples modelos de IA y herramientas.

- **Modo Simple**: mejor para conversaciones naturales. El agente elige automáticamente las herramientas adecuadas.  
- **Modo Directo**: mejor para flujos de trabajo o integraciones. Usted ejecuta las herramientas y puede leer las instrucciones del agente.  

**Agente LangGraph**: un supervisor que gestiona un equipo de agentes especializados.

- **Modo Simple**: hable con el supervisor, que delega tareas a los miembros adecuados del equipo.  
- **Modo Directo**: hable directamente con miembros individuales del equipo y vea cómo el supervisor los organiza.  

**Cómo elegir la configuración adecuada**

| Caso de uso                         | Configuración recomendada      |
|------------------------------------|--------------------------------|
| Interfaz de chat conversacional    | Cualquier agente + Modo Simple |
| Flujos de trabajo empresariales automatizados | Multi-Model + Modo Directo |
| Análisis complejo, con múltiples habilidades | LangGraph + Modo Simple |
| Desarrollo y depuración            | Cualquier agente + Modo Directo |
| Integraciones de API               | Multi-Model + Modo Directo |
| Resolución de problemas multidominio | LangGraph + Modo Simple |


## Guía paso a paso

###  Obtener la configuración de MCP
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Agente`

1.  Abra la ventana Agente en **Etendo**
2.  **Seleccione su agente** y haga clic en el botón **"Server MCP Config"**.
3.  **Configure las opciones de conexión**:
    
    ![Diálogo de configuración de MCP](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/mcp-config-dialog.png)

    - **Modo Directo**: márquelo para ejecución de herramientas, desmárquelo para conversación.
    - **Compatibilidad con MCP-remote**: márquelo para una mejor compatibilidad con el cliente.
    - **Valores personalizados**: sobrescrituras opcionales de URL y nombre.
    
    !!! info "Modo de compatibilidad con MCP-remote"
    
        **Qué hace**: usa la librería `mcp-remote` para añadir compatibilidad con clientes MCP que no gestionan correctamente el transporte `HTTP` con cabeceras de autenticación.
        
        **Cuándo usarlo**: 
        
        - Claude Desktop: requiere este modo para una autenticación correcta.
        - Algunas extensiones de IDE que tienen limitaciones de transporte `HTTP`.
        
        **Diferencia de configuración**:

        - **Modo estándar**: configuración HTTP directa con cabeceras.
        - **Modo de compatibilidad**: usa el comando wrapper `npx mcp-remote`.
    

4.  **Copie la configuración generada** desde el popup

    ![Configuración MCP generada](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/mcp-config.png)

    !!! warning "Advertencia de desarrollo con localhost"
        
        Si ve este mensaje: *"The MCP URL begins with `http://localhost`, which only works in development environments"*
        
        - **Qué significa**: la URL generada solo es accesible desde la misma máquina
        - **Para uso en producción**: configure la propiedad `context.url.copilot.mcp` en Etendo para usar su dominio público en lugar de localhost
        - **Para acceso externo**: use el campo **URL personalizada** en el diálogo para especificar la dirección pública de su host de Copilot

    !!! info "Configuraciones de ejemplo" 

        **Configuración de VS Code**

        Añada a la configuración de VS Code:

        ```json
        "mcp": {
        "servers": {
            "etendoAgent": {
            "type": "http",
            "url": "http://localhost:5006/AGENT_ID/mcp",
            "headers": {
                "etendo-token": "Bearer your-token-here"
            }
            }
        }
        }
        ```

        **Configuración de Gemini CLI**

        Cree o actualice su configuración de Gemini CLI:

        ```json
        {
        "mcpServers": {
            "etendoAgent": {
            "type": "http", 
            "httpUrl": "http://localhost:5006/AGENT_ID/mcp/",
            "headers": {
                "etendo-token": "Bearer your-token-here"
            }
            }
        }
        }
        ```

        **Configuración de Claude Desktop**

        Añada a su configuración de Claude Desktop:

        ```json
        {
        "mcpServers": {
            "etendoAgent": {
            "command": "npx",
            "args": ["mcp-remote", "http://localhost:5006/AGENT_ID/mcp", "--headers", "etendo-token=Bearer your-token-here"]
            }
        }
        }
        ```

### Probar la conexión

1. **Inicie su cliente MCP** [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers){target="_blank"}, [Gemini CLI](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server){target="_blank"}, [Claude Desktop](https://modelcontextprotocol.io/docs/develop/connect-local-servers){target="_blank"}, etc.

2. **Pruebe la conectividad básica**:

    ```
    Use the ping tool to test connection
    ```

3. **Pruebe la interacción con el agente**:
   
    **Modo Simple**:
    ```
    Ask the agent: "What can you help me with?"
    ```

    **Modo Directo**:
    ```
    Use get_agent_prompt to see agent capabilities
    Execute specific tools directly
    ```

## Explicación de los modos de conexión

### Modo Simple
- **URL**: `http://HOST:PORT/AGENT_ID/mcp`
- **Herramientas**: `ask_agent`, utilidades básicas.
- **Uso**: conversación natural con el agente.

### Modo Directo  
- **URL**: `http://HOST:PORT/AGENT_ID/direct/mcp`
- **Herramientas**: todas las herramientas del agente + `get_agent_prompt`.
- **Uso**: ejecución directa de herramientas y acceso al sistema.

## Casos de uso

### Interfaz de chat simple

- **Usuario**: *"What can you help me with?"*
- **Agente**: *"Puedo ayudarle con operaciones de Etendo, análisis de datos, informes y más. ¿Qué le gustaría saber?"*
- **Usuario**: *"Show me recent sales data"*
- **Agente**: 
    
    [Usa herramientas internas] 
    
    *"Here's the recent sales data: [displays results]"*

### Ejecución directa de herramientas

- **Desarrollador**: 

    *Usa la herramienta `get_agent_prompt`*

- **Resultado**: "Soy un asistente de ventas de Etendo con acceso a datos de clientes y herramientas de informes..."*

- **Desarrollador**:
    
    *Usa la herramienta `search_customers` directamente*

    *Parámetros: {"query": "enterprise clients", "limit": 10}*

- **Resultado**: *Devuelve una lista de clientes empresariales sin envoltorio conversacional*

## Resolución de problemas

### Problemas comunes

**Falla la conexión:**

- Verifique que el token de Etendo sea válido.
- Compruebe que el ID del agente sea correcto.
- Asegúrese de que el servicio de Copilot esté en ejecución.

**Herramientas no disponibles:**

- Compruebe los permisos del usuario en Etendo.
- Verifique que la configuración del agente incluya las herramientas necesarias.
- Confirme que el modo de conexión coincide con sus necesidades.

**Errores de autenticación:**

- Regenere el token SWS mediante `/sws/login`.
- Compruebe que el formato del token incluya el prefijo "Bearer ".
- Verifique que el usuario tenga permisos de acceso al agente.

!!! warning "Nota de seguridad"
    Use siempre HTTPS en entornos de producción. Mantenga sus tokens SWS seguros y nunca los exponga en código del lado del cliente o repositorios públicos.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.