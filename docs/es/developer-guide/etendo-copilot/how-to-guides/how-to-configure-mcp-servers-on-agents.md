---
title: Configurar servidores MCP en agentes de Etendo
status: beta
tags:
    - Cómo
    - Servidor MCP
    - Model Context Protocol
    - Integración con Copilot
    - Configuración de agente
---

# Cómo configurar servidores MCP en agentes de Etendo

## Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

Esta guía proporciona instrucciones paso a paso para ayudarle a crear y configurar **servidores Model Context Protocol (MCP)** para **Etendo Copilot**.

Los servidores MCP amplían la funcionalidad del agente proporcionando herramientas y recursos externos que pueden cargarse dinámicamente y utilizarse durante las interacciones del agente.

### ¿Qué es Model Context Protocol?

MCP es un protocolo de código abierto que permite una integración fluida entre modelos de lenguaje de gran tamaño (LLM) y herramientas externas, fuentes de datos y servicios. Puede encontrar más información en la página de concepto [Model Context Protocol (MCP)](../concepts/model-context-protocol.md).

## Guía paso a paso

### Crear configuración de servidor MCP
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Configuración de servidores MCP`

1. Abra la ventana **Configuración de servidores MCP** (rol Administrador del sistema)
2. **Cree un nuevo registro** con la siguiente información:

    ![Configuración de servidor MCP](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-configure-mcp-servers-on-agents/mcp-server-configuration.png)

    - **Nombre**: Un nombre descriptivo para su servidor MCP.
    - **Descripción**: Una breve descripción de lo que proporciona el servidor MCP.
    - **Estructura JSON**: El JSON de configuración del servidor MCP.

### Configurar la estructura JSON

El campo **Estructura JSON** contiene la configuración del servidor MCP. Puede pegar configuraciones MCP exactamente como aparecen en documentación y sitios web, incluidas configuraciones completas con claves envolventes.

!!! info "Repositorio de servidores MCP disponibles"
    Puede encontrar una lista seleccionada de servidores MCP en el repositorio oficial [Model Context Protocol Servers repository](https://github.com/modelcontextprotocol/servers), que agrupa muchos servidores disponibles.

Ejemplos:

**Configuración simple de servidor**:

```json
{
  "command": "npx",
  "args": ["@modelcontextprotocol/server-filesystem", "/tmp/mcp-test"],
  "transport": "stdio"
}
```

**Configuración MCP completa** (como se encuentra en la mayoría de la documentación):

```json
{
  "mcp": {
    "servers": {
      "context7": {
        "command": "npx",
        "args": ["-y", "@upstash/context7-mcp"]
      }
    }
  }
}
```

El sistema normaliza automáticamente diferentes estructuras `JSON` y tipos de `transport`. Si se omite `transport` y `command` está presente, el valor por defecto es `stdio`.

!!! warning "Servidores MCP con Docker no compatibles"
    Los servidores MCP que usan Docker no son compatibles actualmente. En este momento, dado que es una funcionalidad beta, en Etendo solo funcionan los servidores MCP que usan `NPX`, `HTTP`, `SSE`, `UV` o `UVX`.

!!! note "Importante"
    - El sistema valida y normaliza automáticamente la estructura `JSON` cuando guarda la configuración MCP.
    - Si el `JSON` no es válido, recibirá un mensaje de error y el registro no se guardará hasta que se corrija.
    - Cuando se definen varios servidores en una única configuración, cada servidor se tratará como una configuración MCP independiente.
    - El nombre del servidor de las estructuras anidadas se combinará con el nombre del registro MCP (p. ej., "MyMCP::filesystem").

### Vincular servidor MCP al agente

:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Agent`

1. **Abra la ventana Agent** en **Etendo**.
2. **Seleccione un agente existente** o cree uno nuevo.
3. **Vaya a la pestaña MCP** dentro de la ventana Agent y **cree un nuevo registro**.

    ![Configuración MCP del agente](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-configure-mcp-servers-on-agents/agent-mcp-configuration.png)
   
    **Servidor MCP**: Seleccione el servidor MCP recién creado.

### Probar la integración MCP

1. **Inicie una conversación** con su agente configurado

2. **Solicite acciones** que utilicen herramientas MCP:
   
   ```
   "Search in context7, how to create an event handler in Etendo?"
   ```

3. **Observe el comportamiento del agente**:

    - El agente detectará automáticamente las herramientas MCP disponibles
    - Las herramientas MCP se invocarán cuando sea apropiado para la solicitud del usuario
    - Los resultados de la ejecución de herramientas se integrarán en la respuesta del agente

## Ejemplo: servidor MCP de sistema de archivos

A continuación se muestra un ejemplo completo de configuración de un servidor MCP de sistema de archivos:

### Configuración del servidor MCP

- **Nombre**: `Filesystem MCP Server`
- **Descripción**: `Node.js server implementing Model Context Protocol (MCP) for filesystem operations.`
- **Estructura JSON**:

    ```json
    {
        "command": "npx",
        "args": ["@modelcontextprotocol/server-filesystem", "/tmp/mcp-test"],
        "transport": "stdio"
    }
    ```

### Integración del agente

1. Vincule el servidor MCP de sistema de archivos a un agente.
2. Sincronice la configuración del agente.
3. Pruebe con operaciones del sistema de archivos.

### Ejemplo de uso

- **Usuario**: *"What files are in the working directory?"*
- **Agente**: *"I'll check the files in the directory for you."* 
    
    [Invokes filesystem MCP tool]
    
    *"Here are the files I found: config.txt, data.json, readme.md"*

- **Usuario**: *"Can you read the contents of config.txt?"*
- **Agente**:

    [Invokes filesystem read tool]

    *"Here's the content of config.txt: [file contents]"*


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.