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

!!! example  "Beta Version — Important Notice"
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

### Modos de autenticación

El diálogo de configuración de MCP ahora le permite elegir cómo se autentica el cliente contra el servidor MCP del agente:

| Tipo de autenticación | Cómo funciona | Mejor para |
|----------------------|--------------|----------|
| **OAuth 2.1** | Usa una URL MCP limpia y permite que el cliente complete la autenticación mediante un flujo de inicio de sesión en el navegador | Clientes con compatibilidad nativa con OAuth de MCP |
| **Token in Header** | Envía el token de Etendo en la cabecera HTTP personalizada `etendo-token` | Clientes que admiten cabeceras personalizadas |
| **Token in URL** | Añade el token como `?token=...` en la URL del endpoint MCP | Clientes que no pueden enviar cabeceras personalizadas |

### Arquitectura del servidor MCP en Etendo Copilot

El servidor MCP se ejecuta junto al agente y se comunica usando transporte `HTTP` con `Server-Sent Events (SSE)` opcional para respuestas en streaming.

Cuando OAuth está habilitado, el servidor MCP también expone los endpoints de descubrimiento y autorización OAuth requeridos por clientes MCP compatibles. Los usuarios se autentican a través de una página de inicio de sesión de Etendo, y el cliente recibe automáticamente el resultado de la autorización.

El flujo de inicio de sesión OAuth incluye dos posibles rutas de interfaz:

- **Organización y rol predeterminados**: el usuario introduce nombre de usuario y contraseña, activa **Usar organización y rol predeterminados** y completa la autenticación directamente.
- **Selección manual de organización y rol**: el usuario introduce nombre de usuario y contraseña sin activar la casilla. Si las credenciales son válidas, el flujo continúa a una segunda pantalla donde el usuario debe elegir un **Rol** y una **Organización** antes de completar la autenticación.

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
2.  **Seleccione su agente** y haga clic en el botón **Server MCP Config**.
3.  **Configure las opciones de conexión**:
    
    ![Diálogo de configuración de MCP](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/mcp-config-dialog.png)

    - **Modo Directo**: márquelo para ejecución de herramientas, desmárquelo para conversación.
    - **Tipo de autenticación**: elija `OAuth 2.1`, `Token in Header` o `Token in URL`.
    - **Compatibilidad con MCP-remote**: márquelo para una mejor compatibilidad con el cliente.
    - **Valores personalizados**: sobrescrituras opcionales de URL y nombre. Si define una **URL personalizada**, esta tiene prioridad sobre la resolución de URL predeterminada usada por Etendo.

    !!! info "Tipo de autenticación"

        **OAuth 2.1**

        - Genera una URL MCP limpia sin incrustar el token.
        - El cliente MCP gestiona la autenticación y abre un flujo de inicio de sesión en el navegador cuando es necesario.
        - La interfaz de inicio de sesión solicita primero nombre de usuario y contraseña.
        - Si **Usar organización y rol predeterminados** está activado, la autenticación finaliza inmediatamente después de un inicio de sesión correcto.
        - Si la casilla no está activada, el flujo continúa a una segunda página donde el usuario selecciona la organización y el rol.
        - Recomendado cuando su cliente MCP admite OAuth 2.1 para servidores MCP.

        **Token in Header**

        - Envía el token a través de la cabecera `etendo-token`.
        - Esta es la opción predeterminada.
        - Recomendado para clientes que admiten cabeceras HTTP personalizadas.

        **Token in URL**

        - Añade el token como `?token=...` en la URL MCP generada.
        - Útil para clientes que no pueden enviar cabeceras personalizadas.
        - Úselo solo en entornos de confianza porque el token pasa a formar parte de la URL.
    
    !!! info "Modo de compatibilidad con MCP-remote"
    
        **Qué hace**: usa la biblioteca `mcp-remote` para añadir compatibilidad con clientes MCP que no gestionan directamente el transporte `HTTP` de MCP de Etendo.
        
        **Cuándo usarlo**: 
        
        - Claude Desktop y clientes similares que necesitan un puente compatible con stdio.
        - Extensiones de IDE o herramientas con compatibilidad nativa limitada con MCP `HTTP`.
        
        **Diferencia de configuración**:

        - **Modo estándar**: configuración HTTP directa de MCP.
        - **Modo de compatibilidad**: usa `npx mcp-remote` como envoltorio alrededor del endpoint MCP generado.
    

4.  **Copie la configuración generada** desde el popup

    ![Configuración MCP generada](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/mcp-config.png)

    !!! warning "Advertencia de desarrollo con localhost"
        
        Si ve este mensaje: *"The MCP URL begins with `http://localhost`, which only works in development environments"*
        
        - **Qué significa**: el endpoint MCP generado usa `localhost`, por lo que solo los clientes que se ejecuten en la misma máquina pueden conectarse a él.
        - **Cuándo se notará más**: esta advertencia es especialmente relevante para las configuraciones **Token in Header** y **Token in URL**, porque esos modos generan un endpoint concreto al que el cliente debe llamar directamente.
        - **Dónde se configura**: `context.url.copilot.mcp` se lee desde `gradle.properties`, no desde el servidor web ni desde la configuración de Apache.
        - **Qué hace `context.url.copilot.mcp`**: esta propiedad define la URL base pública que Etendo usa al generar fragmentos de configuración MCP y metadatos OAuth.
        - **Orden de resolución**: Etendo usa primero el campo **URL personalizada** del popup si se proporcionó, después `context.url.copilot.mcp` de `gradle.properties` y, por último, recurre a `http://localhost:<copilot.port.mcp>`, donde el puerto MCP predeterminado es `5006`.
        - **Para producción o clientes remotos**: configure `context.url.copilot.mcp` en `gradle.properties` con la URL de Copilot accesible externamente, por ejemplo `https://your-domain.example.com:5006`.
        - **Para pruebas puntuales**: también puede usar el campo **URL personalizada** en el diálogo para sobrescribir la URL base generada sin cambiar la propiedad global.
        - **Ejemplo**: si Copilot está expuesto en `https://copilot.example.com`, el endpoint generado debería parecerse a `https://copilot.example.com/AGENT_ID/mcp` en lugar de `http://localhost:5006/AGENT_ID/mcp`.

        Entrada de ejemplo en `gradle.properties`:

        ```properties
        context.url.copilot.mcp=https://your-external-host:5006
        ```

    !!! info "Configuraciones de ejemplo" 

                Elija el ejemplo que coincida con el **Tipo de autenticación** seleccionado.

                !!!note "Acerca de AGENT_ID"
                    `AGENT_ID` en todos los ejemplos siguientes es un marcador de posición. El valor real es el identificador único asignado al agente en Etendo. Al usar el diálogo **Server MCP Config**, la configuración generada reemplaza automáticamente este marcador por el ID correcto del agente.

                **Configuración de VS Code con OAuth 2.1**

                Añada a la configuración de VS Code:

                ```json
                "mcp": {
                    "servers": {
                        "etendoAgent": {
                            "type": "http",
                            "url": "http://localhost:5006/AGENT_ID/mcp"
                        }
                    }
                }
                ```

                Esta configuración usa una URL limpia. Si el cliente admite OAuth de MCP, abrirá automáticamente el flujo de inicio de sesión en el navegador.

                **Configuración de VS Code con Token in Header**

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

                **Configuración de VS Code con Token in URL**

                ```json
                "mcp": {
                    "servers": {
                        "etendoAgent": {
                            "type": "http",
                            "url": "http://localhost:5006/AGENT_ID/mcp?token=your-token-here"
                        }
                    }
                }
                ```

                **Configuración de Gemini CLI con Token in Header**

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

                **Configuración de Gemini CLI con Token in URL**

                ```json
                {
                    "mcpServers": {
                        "etendoAgent": {
                            "type": "http",
                            "httpUrl": "http://localhost:5006/AGENT_ID/mcp?token=your-token-here"
                        }
                    }
                }
                ```

                **Configuración de Claude Desktop con MCP-remote y OAuth 2.1**

                Añada a su configuración de Claude Desktop:

                ```json
                {
                    "mcpServers": {
                        "etendoAgent": {
                            "command": "npx",
                            "args": ["mcp-remote", "http://localhost:5006/AGENT_ID/mcp"]
                        }
                    }
                }
                ```

                **Configuración de Claude Desktop con MCP-remote y Token in Header**

                Añada a su configuración de Claude Desktop:

                ```json
                {
                    "mcpServers": {
                        "etendoAgent": {
                            "command": "npx",
                            "args": ["mcp-remote", "http://localhost:5006/AGENT_ID/mcp", "--header", "Authorization: Bearer your-token-here"]
                        }
                    }
                }
                ```

                **Configuración de Claude Desktop con MCP-remote y Token in URL**

                ```json
                {
                    "mcpServers": {
                        "etendoAgent": {
                            "command": "npx",
                            "args": ["mcp-remote", "http://localhost:5006/AGENT_ID/mcp?token=your-token-here"]
                        }
                    }
                }
                ```

### Probar la conexión

1. **Inicie su cliente MCP** [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers){target="_blank"}, [Gemini CLI](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server){target="_blank"}, [Claude Desktop](https://modelcontextprotocol.io/docs/develop/connect-local-servers){target="_blank"}, etc.

2. **Confirme que el servidor está disponible**: En la lista de herramientas o inspector del cliente, verifique que aparezca al menos una herramienta — por ejemplo, `ask_agent` en Modo Simple, o las herramientas propias del agente en Modo Directo. Si no aparece ninguna herramienta, vaya a la sección de Resolución de problemas.

3. **Pruebe la interacción con el agente**:
   
    **Modo Simple**:
    ```
    Pregunta al agente: "¿Con qué puedes ayudarme?"
    ```

    **Modo Directo**: En la lista de herramientas del cliente, invoque `get_agent_prompt` sin parámetros. Revise la salida devuelta para comprender las herramientas disponibles del agente y las entradas esperadas. Después invoque cualquier herramienta de la lista directamente — por ejemplo, una herramienta `search_customers` con `{"query": "test", "limit": 1}`.

4. **Si seleccionó OAuth 2.1**:

    ```
    Completa el flujo de inicio de sesión en el navegador cuando el cliente solicite autenticación
    ```

    El flujo de inicio de sesión OAuth funciona de la siguiente manera:

    1. El cliente MCP abre la página de inicio de sesión de Etendo en el navegador.
    2. El usuario introduce nombre de usuario y contraseña.

        ![Página de inicio de sesión de Etendo mostrando los campos de nombre de usuario y contraseña con la casilla Usar organización y rol predeterminados](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/mcp-oauth-1.png)

    3. Si **Usar organización y rol predeterminados** está activado, Etendo completa la autenticación inmediatamente.
    4. Si la casilla no está activada y las credenciales son válidas, Etendo abre una segunda página.
    5. En la segunda página, el usuario selecciona un **Rol** y una **Organización**.

        ![Página de selección de Rol y Organización en el flujo de inicio de sesión OAuth de Etendo](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/mcp-oauth-2.png)

    6. Después de confirmar la selección, el flujo OAuth se completa y el cliente MCP continúa la conexión.

## Explicación de los modos de conexión

### Modo Simple
- **URL**: `http://HOST:PORT/AGENT_ID/mcp`

### Modo Directo  
- **URL**: `http://HOST:PORT/AGENT_ID/direct/mcp`

!!! tip
    En **Modo Directo**, llame a `get_agent_prompt` antes de usar otras herramientas. El prompt explica el propósito del agente, sus capacidades y el uso esperado de las herramientas expuestas.

## Casos de uso

### Interfaz de chat simple

- **Usuario**: *"¿Con qué puedes ayudarme?"*
- **Agente**: *"Puedo ayudarle con operaciones de Etendo, análisis de datos, informes y más. ¿Qué le gustaría saber?"*
- **Usuario**: *"Muéstrame los datos de ventas recientes"*
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

- Verifique que el tipo de autenticación seleccionado coincida con las capacidades de su cliente.
- Si usa `Token in Header`, verifique que el token de Etendo sea válido.
- Compruebe que el ID del agente sea correcto.
- Asegúrese de que el servicio de Copilot esté en ejecución.

**El inicio de sesión OAuth no arranca:**

- Confirme que su cliente MCP admite OAuth 2.1 para servidores MCP.
- Verifique que la URL generada no incluya un token si seleccionó `OAuth 2.1`.
- Asegúrese de que el navegador pueda acceder a la página de inicio de sesión de Etendo expuesta por el servidor MCP.

**OAuth login stops after credentials:**

- Si **Usar organización y rol predeterminados** está desactivado, espere una segunda página que solicite **Rol** y **Organización**.
- Si esa segunda página no aparece, verifique que el usuario tenga asignaciones válidas de rol y organización en Etendo.
- Si **Usar organización y rol predeterminados** está activado pero la autenticación aún no continúa, verifique que el usuario tenga configurados un rol y una organización predeterminados válidos.

**El cliente no puede enviar cabeceras:**

- Use `Token in URL` en lugar de `Token in Header`.
- Si es necesario, active el **Modo de compatibilidad con MCP-remote** y regenere la configuración.

**Herramientas no disponibles:**

- Compruebe los permisos del usuario en Etendo.
- Verifique que la configuración del agente incluya las herramientas necesarias.
- Confirme que el modo de conexión coincide con sus necesidades.
- En **Modo Directo**, llame primero a `get_agent_prompt` para entender cómo debe usarse el conjunto de herramientas.

**Errores de autenticación:**

- Si está utilizando autenticación basada en token y recibe un error 401, regenere el token de sesión de Etendo llamando a `/sws/login` con credenciales válidas de Etendo (este es el endpoint de inicio de sesión de servicios web de Etendo). Actualice el token en la configuración del cliente después.
- Compruebe que el formato del token incluya el prefijo `Bearer ` cuando lo envíe en una cabecera.
- Verifique que el usuario tenga acceso al agente seleccionado.
- Si usa `Token in URL`, confirme que el endpoint generado siga incluyendo el parámetro de consulta `token`.

!!! warning "Nota de seguridad"
    Use siempre HTTPS en entornos de producción. Mantenga sus tokens SWS seguros y nunca los exponga en código del lado del cliente o repositorios públicos. Prefiera **OAuth 2.1** o **Token in Header** frente a **Token in URL** siempre que el cliente los admita.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.