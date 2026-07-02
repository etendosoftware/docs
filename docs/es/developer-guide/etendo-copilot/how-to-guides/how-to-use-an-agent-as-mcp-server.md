---
title: Cómo usar un agente como servidor MCP
status: beta
tags:
    - Cómo hacer
    - Copilot
    - Servidor MCP
    - Model Context Protocol
    - Herramientas
    - Agentes
---

# Cómo usar un agente como servidor MCP { #how-to-use-an-agent-as-mcp-server }

## Descripción general { #overview }

!!! example  "Versión Beta — Aviso importante"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

Esta guía muestra cómo conectarse a agentes de Etendo Copilot usando el [Model Context Protocol (MCP)](../concepts/model-context-protocol.md). Cada agente expone automáticamente un servidor MCP al que puede conectarse desde varios clientes compatibles con MCP como Claude Desktop, VS Code, Gemini CLI y aplicaciones personalizadas.

| Modo | Descripción | Mejor para |
|------|-------------|------------|
| **Simple** | Chatear de forma natural con el agente | Conversaciones, preguntas, uso general |
| **Direct** | Ejecutar herramientas específicas directamente | Automatización, flujos de trabajo, desarrollo |

## Conceptos { #concepts }

### Modos de conexión { #connection-modes }

Existen dos tipos de comunicación con el servidor MCP, ambos establecidos a través de la API expuesta por cada agente:

- **Modo Simple**: proporciona acceso al agente como una "caja negra" externa. El cliente interactúa de forma natural con el agente, sin visibilidad de su configuración interna, herramientas o prompt.
    - **URL**: `http://HOST:PORT/AGENT_ID/mcp`
- **Direct Mode**: proporciona acceso directo al prompt y a las herramientas del agente. En este modo, el cliente externo se comporta como si fuera un agente de Etendo, con acceso a las mismas herramientas, datos y definiciones disponibles para el agente interno.
    - **URL**: `http://HOST:PORT/AGENT_ID/direct/mcp`

!!! tip
    En **Direct Mode**, llame a `get_agent_prompt` antes de usar otras herramientas. El prompt explica el propósito del agente, sus capacidades y el uso esperado de las herramientas expuestas.

### Modos de autenticación { #authentication-modes }

El diálogo de configuración de MCP le permite elegir cómo se autentica el cliente contra el servidor MCP del agente:

| Tipo de autenticación | Cómo funciona | Mejor para |
|-----------------------|---------------|------------|
| **OAuth 2.1** | Usa una URL MCP limpia y permite que el cliente complete la autenticación mediante un flujo de inicio de sesión en el navegador | Clientes con compatibilidad nativa con OAuth de MCP |
| **Token en encabezado** | Envía el token de Etendo en el encabezado HTTP personalizado `etendo-token` | Clientes que admiten encabezados personalizados |
| **Token en URL** | Añade el token como `?token=...` en la URL del endpoint MCP | Clientes que no pueden enviar encabezados personalizados |

### Tipos de agente { #agent-types }

Etendo Copilot admite dos tipos de agentes, cada uno con dos modos de conexión. El tipo de agente define el rol, y el modo define cómo interactúa con él.

| Tipo de agente     | Modo Simple (Hablar)                               | Modo Directo (Controlar)                                              |
|--------------------|----------------------------------------------------|--------------------------------------------------------------------|
| **Multi-Model**    | Usar `ask_agent` para chatear de forma natural     | Acceder a todas las herramientas directamente + `get_agent_prompt` para la configuración |
| **LangGraph**      | Usar `ask_agent_supervisor` para hablar con el supervisor | Usar `ask_agent_<MemberName>` para miembros del equipo + `get_agent_prompt` |

**Agente Multi-Model**: un único agente que combina múltiples modelos de IA y herramientas.

- **Modo Simple**: mejor para conversaciones naturales. El agente elige automáticamente las herramientas adecuadas.
- **Modo Directo**: mejor para flujos de trabajo o integraciones. Usted ejecuta las herramientas y puede leer las instrucciones del agente.

**Agente LangGraph**: un supervisor que gestiona un equipo de agentes especializados.

- **Modo Simple**: hable con el supervisor, que delega tareas a los miembros adecuados del equipo.
- **Modo Directo**: hable directamente con miembros individuales del equipo y vea cómo el supervisor los organiza.

| Caso de uso                                  | Configuración recomendada          |
|----------------------------------------------|------------------------------------|
| Interfaz de chat conversacional              | Cualquier agente + Modo Simple     |
| Flujos de trabajo empresariales automatizados | Multi-Model + Modo Directo        |
| Análisis complejo con múltiples habilidades  | LangGraph + Modo Simple            |
| Desarrollo y depuración                      | Cualquier agente + Modo Directo    |
| Integraciones de API                         | Multi-Model + Modo Directo         |
| Resolución de problemas multidominio         | LangGraph + Modo Simple            |

### Arquitectura { #architecture }

El servidor MCP se ejecuta junto al agente y se comunica usando transporte `HTTP` con `Server-Sent Events (SSE)` opcional para respuestas en streaming.

Cuando OAuth está habilitado, el servidor MCP también expone los endpoints de descubrimiento y autorización OAuth requeridos por clientes MCP compatibles. Los usuarios se autentican a través de una página de inicio de sesión de Etendo, y el cliente recibe automáticamente el resultado de la autorización.

El flujo de inicio de sesión OAuth incluye dos posibles rutas de interfaz:

- **Organización y rol predeterminados**: el usuario introduce nombre de usuario y contraseña, activa **Use default role and organization** y completa la autenticación directamente.
- **Selección manual de organización y rol**: el usuario introduce nombre de usuario y contraseña sin activar la casilla. Si las credenciales son válidas, el flujo continúa a una segunda pantalla donde el usuario debe elegir un **Rol** y una **Organización** antes de completar la autenticación.

## Configuración { #setup }

!!! info "Requisitos previos"
    - Etendo Copilot está instalado y en funcionamiento.
    - Al menos un agente está configurado en la ventana Agente.
    - Usted dispone de un token de sesión de Etendo o de credenciales de cliente MCP con capacidad OAuth.

### Paso 1: Obtener el fragmento de configuración de MCP { #step-1-get-the-mcp-configuration-snippet }

:material-menu: `Application` > `Service` > `Copilot` > `Agent`

1.  Abra la ventana Agente en **Etendo**.
2.  **Seleccione su agente** y haga clic en el botón **Server MCP Config**.
3.  **Configure las opciones de conexión**:

    <figure markdown="span">
      ![Diálogo de configuración de MCP que muestra el modo de conexión, el tipo de autenticación y valores personalizados opcionales](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/how-to-use-an-agent-as-mcp-server-1.png)
      <figcaption>Diálogo de configuración de MCP: modo de conexión, tipo de autenticación y valores personalizados opcionales.</figcaption>
    </figure>

    - **Direct Mode**: márquelo para ejecución de herramientas, desmárquelo para conversación.
    - **Authentication Type**: elija `OAuth 2.1`, `Token in Header` o `Token in URL`.
    - **MCP-remote compatibility**: márquelo para una mejor compatibilidad con el cliente.
    - **Custom values**: sobrescrituras opcionales de URL y nombre. Si define una **Custom URL**, esta tiene prioridad sobre la resolución de URL predeterminada usada por Etendo.

    !!! info "Authentication Type"

        **OAuth 2.1**

        - Genera una URL MCP limpia sin insertar el token.
        - El cliente MCP gestiona la autenticación y abre un flujo de inicio de sesión en el navegador cuando es necesario.
        - La interfaz de inicio de sesión solicita primero nombre de usuario y contraseña.
        - Si **Use default role and organization** está activado, la autenticación finaliza inmediatamente después de un inicio de sesión correcto.
        - Si la casilla no está activada, el flujo continúa a una segunda página donde el usuario selecciona el rol y la organización.
        - Recomendado cuando su cliente MCP admite OAuth 2.1 para servidores MCP.

        **Token en encabezado**

        - Envía el token a través del encabezado HTTP personalizado `etendo-token`.
        - Esta es la opción predeterminada.
        - Recomendado para clientes que admiten encabezados HTTP personalizados.

        **Token en URL**

        - Añade el token como `?token=...` en la URL MCP generada.
        - Útil para clientes que no pueden enviar encabezados personalizados.
        - Úselo solo en entornos de confianza porque el token pasa a formar parte de la URL.

    !!! info "Modo de compatibilidad con MCP-remote"

        **Qué hace**: usa la biblioteca `mcp-remote` para añadir compatibilidad con clientes MCP que no gestionan directamente el transporte `HTTP` de MCP de Etendo.

        **Cuándo usarlo**:

        - Claude Desktop y clientes similares que necesitan un puente compatible con stdio.
        - Extensiones de IDE o herramientas con compatibilidad nativa limitada con MCP `HTTP`.

        **Diferencia de configuración**:

        - **Modo estándar**: configuración HTTP directa de MCP.
        - **Modo de compatibilidad**: usa `npx mcp-remote` como envoltorio alrededor del endpoint MCP generado.

4.  **Copie la configuración generada** desde el popup.

    <figure markdown="span">
      ![Fragmento de configuración de MCP generado listo para copiar y pegar en el archivo de configuración del cliente](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/how-to-use-an-agent-as-mcp-server-2.png)
      <figcaption>Fragmento de configuración de MCP generado listo para copiar y pegar en el archivo de configuración del cliente.</figcaption>
    </figure>

### Paso 2: Configurar el cliente { #step-2-configure-your-client }

Elija el ejemplo que coincida con su cliente y el **Authentication Type** seleccionado.

!!! note "Acerca de AGENT_ID"
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

**Configuración de VS Code con Token en encabezado**

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

**Configuración de VS Code con Token en URL**

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

**Configuración de Gemini CLI con Token en encabezado**

Cree o actualice la configuración de Gemini CLI:

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

**Configuración de Gemini CLI con Token en URL**

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

Añada a la configuración de Claude Desktop:

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

**Configuración de Claude Desktop con MCP-remote y Token en encabezado**

Añada a la configuración de Claude Desktop:

```json
{
    "mcpServers": {
        "etendoAgent": {
            "command": "npx",
            "args": ["mcp-remote", "http://localhost:5006/AGENT_ID/mcp", "--header", "etendo-token: Bearer your-token-here"]
        }
    }
}
```

**Configuración de Claude Desktop con MCP-remote y Token en URL**

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

### Paso 3: Exponer el puerto { #step-3-expose-the-port }

!!! warning "Advertencia de desarrollo con localhost"

    Si ve este mensaje: *"The MCP URL begins with `http://localhost`, which only works in development environments"*

    - **Qué significa**: el endpoint MCP generado usa `localhost`, por lo que solo los clientes que se ejecuten en la misma máquina pueden conectarse a él.
    - **Cuándo se notará más**: esta advertencia es especialmente relevante para las configuraciones **Token en encabezado** y **Token en URL**, porque esos modos generan un endpoint concreto al que el cliente debe llamar directamente.
    - **Dónde se configura**: `context.url.copilot.mcp` se lee desde `gradle.properties`, no desde el servidor web ni desde la configuración de Apache.
    - **Qué hace `context.url.copilot.mcp`**: esta propiedad define la URL base pública que Etendo usa al generar fragmentos de configuración MCP y metadatos OAuth.
    - **Orden de resolución**: Etendo usa primero el campo **Custom URL** del popup si se proporcionó, después `context.url.copilot.mcp` de `gradle.properties` y, por último, recurre a `http://localhost:<copilot.port.mcp>`, donde el puerto MCP predeterminado es `5006`.
    - **Para producción o clientes remotos**: configure `context.url.copilot.mcp` en `gradle.properties` con la URL de Copilot accesible externamente, por ejemplo `https://your-domain.example.com:5006`.
    - **Para tests puntuales**: también puede usar el campo **Custom URL** en el diálogo para sobrescribir la URL base generada sin cambiar la propiedad global.
    - **Ejemplo**: si Copilot está expuesto en `https://copilot.example.com`, el endpoint generado debería parecerse a `https://copilot.example.com/AGENT_ID/mcp` en lugar de `http://localhost:5006/AGENT_ID/mcp`.

    Entrada de ejemplo en `gradle.properties`:

    ```properties
    context.url.copilot.mcp=https://your-external-host:5006
    ```

!!! warning "Exposición del puerto requerida para producción"
    El puerto `5006` es el puerto MCP predeterminado de Copilot. En entornos de producción o despliegues remotos, este puerto debe ser accesible desde la máquina del cliente.

    Según la infraestructura:

    - **Firewall**: abra el puerto `5006` para tráfico TCP de entrada.
    - **Docker**: añada `-p 5006:5006` al comando de ejecución del contenedor.
    - **Grupo de seguridad en la nube**: añada una regla de entrada que permita TCP en el puerto `5006`.
    - **Proxy inverso (Apache/Nginx)**: configure el proxy para redirigir el tráfico a Copilot en el puerto `5006`. En este caso, el puerto no necesita estar expuesto públicamente de forma directa.

    El puerto puede modificarse mediante la propiedad `copilot.port.mcp` en `gradle.properties`:

    ```properties
    copilot.port.mcp=XXXX
    ```

### Paso 4: Probar la conexión { #step-4-test-the-connection }

1. **Inicie su cliente MCP** — [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers){target="_blank"}, [Gemini CLI](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server){target="_blank"}, [Claude Desktop](https://modelcontextprotocol.io/docs/develop/connect-local-servers){target="_blank"}, etc.

2. **Confirme que el servidor está disponible**: en la lista de herramientas o inspector del cliente, verifique que aparezca al menos una herramienta — por ejemplo, `ask_agent` en Modo Simple, o las herramientas propias del agente en Modo Directo. Si no aparece ninguna herramienta, consulte la sección de Resolución de problemas.

3. **Pruebe la interacción con el agente**:

    **Modo Simple**:
    ```
    Pregunta al agente: "¿Con qué puedes ayudarme?"
    ```

    **Modo Directo**: en la lista de herramientas del cliente, invoque `get_agent_prompt` sin parámetros. Revise la salida devuelta para comprender las herramientas disponibles del agente y las entradas esperadas. Después invoque cualquier herramienta de la lista directamente — por ejemplo, una herramienta `search_customers` con `{"query": "test", "limit": 1}`.

4. **Si seleccionó OAuth 2.1**:

    ```
    Complete el flujo de inicio de sesión en el navegador cuando el cliente solicite autenticación
    ```

    El flujo de inicio de sesión OAuth funciona de la siguiente manera:

    1. El cliente MCP abre la página de inicio de sesión de Etendo en el navegador.
    2. Introduzca su nombre de usuario y contraseña.

        <figure markdown="span">
          ![Página de inicio de sesión de Etendo con los campos de nombre de usuario y contraseña y la casilla Use default role and organization](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/how-to-use-an-agent-as-mcp-server-3.png)
          <figcaption>Página de inicio de sesión OAuth de Etendo: introduzca nombre de usuario y contraseña y active opcionalmente Use default role and organization.</figcaption>
        </figure>

    3. Si **Use default role and organization** está activado, Etendo completa la autenticación inmediatamente.
    4. Si la casilla no está activada y las credenciales son válidas, Etendo abre una segunda página.
    5. En la segunda página, seleccione un **Rol** y una **Organización**.

        <figure markdown="span">
          ![Página de selección de Rol y Organización en el flujo de inicio de sesión OAuth de Etendo](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-an-agent-as-mcp-server/how-to-use-an-agent-as-mcp-server-4.png)
          <figcaption>Pantalla de selección de Rol y Organización que se muestra cuando Use default role and organization no está activado.</figcaption>
        </figure>

    6. Después de confirmar la selección, el flujo OAuth se completa y el cliente MCP continúa la conexión.

## Casos de uso { #use-cases }

### Interfaz de chat simple { #simple-chat-interface }

- **Usuario**: *"¿Con qué puedes ayudarme?"*
- **Agente**: *"Puedo ayudarle con operaciones de Etendo, análisis de datos, informes y más. ¿Qué le gustaría saber?"*
- **Usuario**: *"Muéstrame los datos de ventas recientes"*
- **Agente**:

    [Usa herramientas internas]

    *"Aquí están los datos de ventas recientes: [muestra los resultados]"*

### Ejecución directa de herramientas { #direct-tool-execution }

- **Desarrollador**:

    *Usa la herramienta `get_agent_prompt`*

- **Resultado**: *"Soy un asistente de ventas de Etendo con acceso a datos de clientes y herramientas de informes..."*

- **Desarrollador**:

    *Usa la herramienta `search_customers` directamente*

    *Parámetros: {"query": "enterprise clients", "limit": 10}*

- **Resultado**: *Devuelve una lista de clientes empresariales sin envoltorio conversacional*

## Resolución de problemas { #troubleshooting }

### Problemas comunes { #common-issues }

**Puerto no accesible:**

- El cliente agota el tiempo de espera o no puede conectarse pese a una configuración correcta.
- Causa probable: el puerto `5006` no está abierto en el servidor.
- Solución: abra el puerto en el firewall, añada un mapeo de puertos de Docker (`-p 5006:5006`) o configure un proxy inverso para redirigir el tráfico a Copilot. Consulte la nota **Exposición del puerto requerida para producción** más arriba.

**Falla la conexión:**

- Verifique que el tipo de autenticación seleccionado coincida con las capacidades de su cliente.
- Si usa `Token in Header`, verifique que el token de Etendo sea válido.
- Compruebe que el ID del agente sea correcto.
- Asegúrese de que el servicio de Copilot esté en funcionamiento.

**El inicio de sesión OAuth no comienza:**

- Confirme que su cliente MCP admite OAuth 2.1 para servidores MCP.
- Verifique que la URL generada no incluya un token si seleccionó `OAuth 2.1`.
- Asegúrese de que el navegador pueda acceder a la página de inicio de sesión de Etendo expuesta por el servidor MCP.

**El inicio de sesión OAuth se interrumpe después de introducir las credenciales:**

- Si **Use default role and organization** está desactivado, espere una segunda página que solicite **Rol** y **Organización**.
- Si esa segunda página no aparece, verifique que el usuario tenga asignaciones válidas de rol y organización en Etendo.
- Si **Use default role and organization** está activado pero la autenticación aún no continúa, verifique que el usuario tenga configurados un rol y una organización predeterminados válidos.

**El cliente no puede enviar encabezados:**

- Use `Token in URL` en lugar de `Token in Header`.
- Si es necesario, active **MCP-remote compatibility mode** y regenere la configuración.

**Herramientas no disponibles:**

- Compruebe los permisos del usuario en Etendo.
- Verifique que la configuración del agente incluya las herramientas necesarias.
- Confirme que el modo de conexión coincide con sus necesidades.
- En Modo Directo, llame primero a `get_agent_prompt` para entender cómo debe usarse el conjunto de herramientas.

**Errores de autenticación:**

- Si usa autenticación basada en token y recibe un error 401, regenere el token de sesión de Etendo. Envíe una solicitud `POST` a `/etendo/sws/login` con un cuerpo JSON que contenga `username` y `password`. La respuesta devuelve un nuevo token. Actualice el token en la configuración del cliente a continuación.
- Compruebe que el formato del token incluya `Bearer ` cuando lo envíe en un encabezado.
- Verifique que el usuario tenga acceso al agente seleccionado.
- Si usa `Token in URL`, confirme que el endpoint generado siga incluyendo el parámetro de consulta `token`.

!!! warning "Nota de seguridad"
    Use siempre HTTPS en entornos de producción. Mantenga sus tokens SWS seguros y nunca los exponga en código del lado del cliente o repositorios públicos. Prefiera **OAuth 2.1** o **Token en encabezado** frente a **Token en URL** siempre que el cliente los admita.

## Artículos relacionados { #related-articles }

[:material-file-document-outline: Model Context Protocol (MCP)](../concepts/model-context-protocol.md){ .md-button .md-button--primary }

[:material-file-document-outline: Cómo configurar servidores MCP en agentes de Etendo](how-to-configure-mcp-servers-on-agents.md){ .md-button .md-button--primary }

[:material-file-document-outline: Cómo crear un agente](how-to-create-an-agent.md){ .md-button .md-button--primary }

[:material-file-document-outline: Cómo configurar tokens de API para Etendo Copilot](how-to-configure-api-tokens.md){ .md-button .md-button--primary }

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
