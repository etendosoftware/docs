---
title: Developer Guide - Model Context Protocol (MCP)
status: beta
tags:
    - Copilot
    - MCP
    - Model Context Protocol
    - Architecture
    - Overview
    - IA
---

## Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

The **Model Context Protocol (MCP)** is an open protocol developed by Anthropic that standardizes how AI applications provide context to Large Language Models (LLMs). MCP acts as a USB-C port for AI applications, enabling models to connect uniformly with external data sources, tools, and services.

This guide provides a comprehensive introduction to MCP concepts, architecture, and its implementation within the Etendo Copilot ecosystem, helping developers understand how to leverage this protocol for building scalable and secure AI integrations.

## What is MCP?

MCP is a protocol that solves the fragmentation problem in the AI ecosystem, where each application required custom integrations to connect with different data sources and tools. With MCP, both developers and organizations can create reusable connectors that work across multiple applications and platforms. Key features include:

- **Open Protocol**: Available to the entire developer community
- **Standardization**: Uniform interface for context and tool integration
- **Scalability**: Modular architecture that allows easy extension
- **Security**: Built-in permission controls and authentication
- **Flexibility**: Support for multiple transport types and data formats

## MCP Architecture

MCP uses a client-server architecture that facilitates communication between AI applications and external data sources.

### Core Components

**Hosts**
Hosts are the primary applications through which users interact with the protocol:
- **Function**: Execute AI models and manage user interface.

- **Responsibilities**: 
    - Initiate connections with MCP servers.
    - Control permissions and security constraints.
    - Manage conversation flow.
    - Handle user consent for data sharing.

**Clients**
Clients act as intermediaries between hosts and MCP servers:

- **Function**: Facilitate communication between hosts and servers.

- **Responsibilities**:
    - Send requests to servers.
    - Negotiate capabilities with servers.
    - Manage tool execution requests.
    - Process and display responses to users.

**Servers**
MCP servers provide access to specific tools, resources, and data:

- **Function**: Handle client requests and provide appropriate responses.

- **Responsibilities**:
    - Register available features (resources, prompts, tools).
    - Execute tool calls from the client.
    - Provide contextual information.
    - Maintain state across interactions when needed.

### Information Flow

1. **Connection Initiation**: The host establishes a connection with an MCP server
2. **Capability Negotiation**: Client and server exchange information about supported features
3. **User Request**: The user interacts with the host by providing a prompt or command
4. **Resource/Tool Usage**: The client requests additional context or executes server tools
5. **Server Execution**: The server executes requested operations and returns results
6. **Response Generation**: The client integrates server responses into model interaction
7. **Result Presentation**: The host presents the final output to the user

## Technical Features

### Base Protocol
- **Message Format**: JSON-RPC 2.0 for consistent structure
- **Stateful Connections**: MCP sessions maintain state across multiple requests
- **Capability Negotiation**: Exchange of information about supported features during setup

### Server Features

**Resources** represent contextual data and information sources available to models:

- Local files (`file://log.txt`)
- Database schemas (`database://schema`)
- External APIs
- Knowledge bases

**Tools** enable models to perform specific actions:

- Web searches
- Mathematical calculations
- Database access
- File system operations

**Prompts** are predefined templates that streamline workflows:

```markdown
Generate a product slogan based on the following {{product}} with the following {{keywords}}
```

### Client Features

**Sampling** enables servers to initiate autonomous behaviors and recursive LLM interactions, allowing:

- Server-initiated agent behaviors
- Recursive LLM interactions
- Requests for additional model completions

## Supported MCP Input Types for Etendo Copilot

To accommodate configurations coming from different editors/clients (which often use different structures and field names), **Etendo Copilot** includes a configuration normalizer called **`MCPConfigNormalizer`**. This class accepts *any* MCP server `JSON`, converts it into a **unified schema**, and applies sensible defaults and lightweight validations so integrations remain consistent and reliable.

**Accepted Input Formats**

Multiple shapes and nestings are recognized:

- `mcpServers: { <name>: { ... } }`
- `mcp.servers` as an **array** or a **map**
- `servers` at the root level (**array** or **map**)
- `context_servers` (the **Zed** format)
- Wrappers such as `{ mcp: { ... } }`, `{ server: { ... } }`

**Accepted Property Aliases**

Common aliases are recognized and mapped to the standard schema:

- **URL**: `url` | `uri` | `endpoint` | `baseUrl` | `serverUrl` | `httpUrl`
- **Command**: `command` | `cmd` | `bin` | `executable` | `path`
- **Args**: `args` | `argv` | `arguments` | `cmdArgs`
- **Headers**: `headers` | `httpHeaders`
- **Other**: `cwd` | `workingDir` | `workdir`, `env` | `environment` | `envVars`

**Transport Detection and Normalization**

All sources are normalized to the set supported by the Python client:

- `stdio`, `sse`, `websocket`, `streamable_http`

Recognized aliases:

- `http`/`https` → **`streamable_http`** (avoids “Unsupported transport: http”)
- `ws` → **`websocket`**

If `transport` is omitted, it is **inferred** from the available fields:

- Presence of `command` ⇒ `stdio`
- `ws://` or `wss://` ⇒ `websocket`
- URL containing `/sse` ⇒ `sse`
- `host`/`port` ⇒ `streamable_http`
- Last resort ⇒ `stdio`

**Unified Output Schema**

The result always includes a **`name`** (from the DB record). If the source used a subkey (e.g., `context7`), the name is **namespaced** as `DBName::context7`.

- **STDIO**
  ```json
  {
    "name": "DBName[::subkey]",
    "transport": "stdio",
    "command": "…",
    "args": ["…"],
    "env": { "…": "…" },
    "cwd": "…"
  }
  ```

- **SSE / WebSocket / Streamable HTTP**
  ```json
  {
    "name": "DBName[::subkey]",
    "transport": "sse | websocket | streamable_http",
    "url": "https://…",
    "headers": { "Authorization": "…" },
    "timeoutMs": 120000
  }
  ```

**Normalization Example**

Input (VS Code / remote):
```json
{
  "mcp": {
    "servers": {
      "context7": {
        "type": "http",
        "url": "https://mcp.context7.com/mcp"
      }
    }
  }
}
```

Normalized output:
```json
{
  "name": "DBName::context7",
  "transport": "streamable_http",
  "url": "https://mcp.context7.com/mcp"
}
```

**Guarantees and Behavior**

- `getMCPConfigurations()` returns **uniform and reliable** configurations, regardless of the original format.
- Names are **preserved**, sensible **defaults** are applied, and invalid entries **do not break** the rest.
- Basic parameters are validated, and “unsupported transport” errors are mitigated via aliases and inference.

## Security and Authorization

MCP includes multiple security mechanisms to ensure safe interactions:

**Tool Permission Control**

- Clients can specify which tools a model is allowed to use during a session.
- Dynamically configurable permissions based on organizational policies.
- Reduced risk of unintended or unsafe operations.

**Authentication**

- Servers can require authentication before granting access.
- Support for API keys, OAuth tokens, and other authentication schemes.
- Ensuring only trusted clients and users can invoke server-side capabilities.

**Parameter Validation**

- Enforced validation for all tool invocations.
- Each tool defines expected types, formats, and constraints for its parameters.
- Prevention of malformed or malicious input.

**Rate Limiting**

- Implementation of rate limits for tool calls and resource access.
- Limits applicable per user, per session, or globally.
- Protection against denial-of-service attacks.

## Use Cases

### In Etendo Copilot Context

MCP in Etendo Copilot allows agents to access in a standardized way:

- **Databases**: Etendo database schemas and queries
- **APIs**: Etendo web services and external systems
- **Files**: Documents, logs, and system configurations
- **Custom Tools**: Etendo-specific functionalities

In the context of Etendo Copilot, MCP enables smoother integration between AI agents and enterprise systems, providing standardized access to Etendo data and functionalities while maintaining the security and control necessary for enterprise environments.

!!!info
    For more information about the MCP, visit:

    - [Official MCP Documentation](https://modelcontextprotocol.io/){target="_blank"}
    - [MCP Specification Repository](https://github.com/modelcontextprotocol/specification){target="_blank"}
    - [MCP Server Guide](../concepts/model-context-protocol.md){target="_blank"}

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.