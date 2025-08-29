---
title: How to use an agent as MCP Server
status: beta
tags:
    - Copilot
    - MCP
    - Model Context Protocol
    - Server
    - Tools
    - Agents
---

## Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

This guide provides detailed instructions on how to connect to and use the **Model Context Protocol (MCP) Server** provided by Etendo Copilot agents. MCP is an open protocol developed by Anthropic that standardizes how AI applications connect to external data sources and tools, enabling composable, secure, and extensible AI workflows.

The MCP Server in Etendo Copilot exposes the tools and capabilities of each agent through a standardized interface, allowing you to integrate Copilot agents with various MCP-compatible clients like Claude Desktop, Gemini CLI, Cursor IDE, and custom applications.

## What is Model Context Protocol (MCP)?

Model Context Protocol (MCP) is an open-source protocol that enables seamless integration between Large Language Models (LLMs) and external tools, data sources, and services. More information can be found in the [Model Context Protocol (MCP)](../concepts/model-context-protocol.md) concept page.

## MCP Server Architecture in Etendo Copilot

Each Etendo Copilot agent automatically exposes an MCP server endpoint that provides:

  - **Interaction Tools**: Tools that facilitate communication between the agent and the MCP Client, like `ask_agent` for sending questions and receiving answers.
  - **Agent Tools**: Functions that the agent can execute.
  - **Resources**: Static or dynamic data that can be accessed (documents, configurations, logs, etc.).
  - **Prompts**: Pre-configured prompt templates for common tasks.

The MCP server runs alongside the agent and communicates using HTTP transport with optional Server-Sent Events (SSE) for streaming responses.

## Summary: Agent Types and Connection Modes

### Quick Reference Matrix

| Agent Type | Simple Mode | Direct Mode |
|------------|-------------|-------------|
| **Multi-Model Agent** | `ask_agent` → Communicate with the agent | All agent tools + `get_agent_prompt` → Use tools directly + adopt agent personality |
| **LangGraph Agent** | `ask_agent_supervisor` → Talk to supervisor | `ask_agent_<MemberName>` for each team member + `get_agent_prompt` → Direct team access |

### Key Differences by Agent Type

#### Multi-Model Agent
- **Purpose**: Single intelligent agent that can use multiple AI models and tools
- **Simple Mode**: Delivers `ask_agent` tool for natural conversation with automatic tool selection
- **Direct Mode**: Delivers all agent tools directly + `get_agent_prompt` to understand the agent's personality and instructions
- **Best for**: General-purpose tasks, knowledge-based queries, automated workflows

#### LangGraph Agent
- **Purpose**: Supervisor agent that coordinates a team of specialized sub-agents
- **Simple Mode**: Delivers `ask_agent_supervisor` tool to talk with the supervisor who routes tasks to team members
- **Direct Mode**: Delivers individual `ask_agent_<MemberName>` tools for each team member + `get_agent_prompt` for supervisor insights
- **Best for**: Complex multi-step tasks requiring different areas of expertise

### Choosing the Right Combination

| Use Case | Recommended Setup |
|----------|-------------------|
| **User-facing chat interface** | Any Agent Type + Simple Mode |
| **Automated business workflows** | Multi-Model Agent + Direct Mode |
| **Complex analysis requiring multiple skills** | LangGraph Agent + Simple Mode |
| **Development and debugging** | Any Agent Type + Direct Mode |
| **API integrations** | Multi-Model Agent + Direct Mode |
| **Multi-domain problem solving** | LangGraph Agent + Simple Mode |

## Connecting to Etendo Copilot MCP Server

### Token-Based Authentication

The MCP server uses token-based authentication via the `etendo-token` header, using the SWS (Secure Web Service) token of the user. This token can be obtained through the Etendo Classic `/sws/login` endpoint.
A quick way to obtain the MCP configuration used to be via a Gradle task, but the module now provides a UI action directly
from the Agents screen which is easier to use. To generate the MCP JSON configuration for an agent:

  - Open the Agents window in the Etendo UI and select the agent you want to configure.
  - Click the "Server MCP Config" (or similar) button in the toolbar. A small dialog will open with the configuration options.

Dialog parameters (fields shown in the dialog)

  - Direct Mode (checkbox): when checked the generated endpoint URL will use the `/direct/mcp` path; when unchecked it will use `/mcp` (simple mode).
  - MCP-remote compatibility mode (checkbox): when checked the generated configuration will be the "remote example" form (suitable for `npx mcp-remote ...`) which renders a JSON object with a `command: "npx"` entry and an `args` array. When unchecked a standard HTTP MCP server configuration is produced (with `url`, `type` and `headers`).
  - Custom values (collapsible section): optional overrides for the generated configuration
    - Custom name (text): a human-friendly display name to use in the MCP configuration. If provided it replaces the agent name in the generated `name` field. 
    - Custom URL (text): when provided, this URL is used as the base `contextUrl` for the MCP configuration instead of deriving it from system properties. Use this when the Copilot host is reachable under a different public address.

{ADD SNAPSHOT}

Behavior after accepting the dialog

  When you click Done/OK the process generates the configuration and shows a small pop-up with everything you need to get started.

  {ADD SNAPSHOT}
  - What you'll see:
    - A short explanation of what the snippet is for and how to use it.
    - A clear notice if the generated address is local-only (e.g. starts with "localhost") so you know it won't be reachable from other machines.
    - A button to import or install the configuration into VS Code (when available).
    - A nicely formatted, copyable JSON snippet you can paste into any MCP client.

  - Two simple options are offered depending on the selected mode:
    - Standard: a ready-to-use HTTP configuration you can paste into client settings.
    - mcp-remote compatibility layer : Using the library `mcp-remote` to add compatibility for MCP clients that do not handle correctly the `streamable-http` transport with authentication with headers. Try to use this by default, but if you encounter issues, you may need to switch to the standard mode.

  - Quick tips:
    - If you entered a Custom URL the snippet will use that address.
    - If you see the local-only notice, update your Copilot host settings if you need external access.

  This UI flow replaces the need to run the Gradle task manually in most cases and is the recommended approach for interactive use.

    - **`simple`**: Delivers conversation tools (`ask_agent` or `ask_agent_supervisor`)
    - **`direct`**: Delivers direct tool access + `get_agent_prompt` for personality adoption

## Connection Modes

The Etendo Copilot MCP server supports two distinct connection modes, each designed for different use cases:

### Simple Mode (Recommended)

**URL Pattern**: `http://{HOST}:{PORT}/{AGENT_ID}/mcp`

Simple mode provides a straightforward interface for talking to the Copilot agent using natural language.

**Features:**
- ✅ **ask_agent tool**: Send questions directly to the Copilot agent using natural language
- ✅ **Basic tools**: ping, hello_world, server_info for connectivity testing
- ✅ **Simplified interface**: Just talk to the agent, it handles tool execution internally
- 🎯 **Best for**: General users who want to interact with the agent conversationally

**When to use Simple Mode:**
- You want to ask questions and get answers from the agent
- You prefer natural language interaction over direct tool execution
- You want the agent to handle tool selection and execution automatically
- You're integrating with clients that work better with conversational interfaces

### Direct Mode (Advanced)

**URL Pattern**: `http://{HOST}:{PORT}/{AGENT_ID}/direct/mcp`

Direct mode exposes all agent tools for direct execution from the MCP client.

**Features:**
- ✅ **All agent-specific tools**: Direct access to every tool configured for the agent
- ✅ **get_agent_prompt tool**: Read the agent's system prompt to understand how it works
- ✅ **Basic tools**: ping, hello_world, server_info for connectivity testing
- ❌ **NO ask_agent tool**: You execute tools directly instead of talking to the agent
- 🎯 **Best for**: Advanced users and developers who need precise control

**When to use Direct Mode:**
- You want to execute specific agent tools directly
- You need to understand the agent's configuration via the system prompt
- You're building integrations that require precise tool control
- You want to bypass the conversational interface for specific workflows

### Mode Selection by Agent Type

The available connection modes depend on the **Agent Type** configured in Etendo Classic:

#### Multi-Model Agent

Multi-Model Agents support both connection modes:

- **Simple Mode** ✅ - Recommended for conversational interaction
- **Direct Mode** ✅ - For direct tool execution and system prompt access

#### LangGraph Agent

LangGraph Agents (supervisor/team-based) have specific mode behavior:

- **Simple Mode** ✅ - Talk to the supervisor agent who will coordinate team members
- **Direct Mode** ✅ - Access supervisor tools and view the orchestration prompt

Selecting the connection mode is now done through the Agents UI dialog (see above). Choose "Direct Mode" in the dialog to
generate a direct-mode configuration (URL pattern ending in `/direct/mcp`) or leave it unchecked for simple mode (`/mcp`).

For automation or headless environments you can still use the Gradle task if needed, but the UI is the preferred path
for interactive configuration inside Etendo.

### Connection Configuration

To connect to an Etendo Copilot agent's MCP server, you need the following configuration (if you used the `copilot.mcp.config` task, you will have this information):

#### Simple Mode Configuration
```json
"etendoAgentSimple": {
  "type": "http",
  "httpUrl": "http://0.0.0.0:5006/ID/mcp/",
  "note": "Simple mode - talk to the Copilot agent using natural language",
  "mode": "Simple mode (talk to Copilot agent)",
  "headers": {
    "etendo-token": "Bearer token"
  }
}
```

#### Direct Mode Configuration
```json
"etendoAgentDirect": {
  "type": "http", 
  "httpUrl": "http://0.0.0.0:5006/ID/direct/mcp/",
  "note": "Direct mode - execute agent tools directly + read system prompt",
  "mode": "Direct mode (direct tool execution + prompt reader)",
  "headers": {
    "etendo-token": "Bearer token"
  }
}
```

**Parameters:**

  - **etendoMCPName**: A unique name for this MCP server configuration, this can be any identifier you choose
  - **ID**: The unique identifier of the Etendo Copilot agent
  - **token**: The SWS (Secure Web Service) token of the user (without the "Bearer" prefix in the configuration)
  - **httpUrl**: The MCP endpoint URL following the pattern:
    - Simple mode: `http://{COPILOT_HOST}:{COPILOT_PORT}/{AGENT_ID}/mcp/`
    - Direct mode: `http://{COPILOT_HOST}:{COPILOT_PORT}/{AGENT_ID}/direct/mcp/`
  - The Copilot host will depend on your specific deployment and where the connection is being made from.

### Authentication

The MCP server uses token-based authentication via the `etendo-token` header. You need:

1. A valid Etendo user account
2. SWS token for that user
3. Appropriate permissions to access the agent's tools

!!! warning "Security"
    Always use HTTPS in production environments and keep your SWS tokens secure. Never expose tokens in client-side code or public repositories.

## Configuring MCP Clients

### Gemini CLI Configuration

To connect Gemini CLI to an Etendo Copilot agent, create or update your Gemini CLI configuration file:

<!-- SCREENSHOT: Gemini CLI config file -->

#### Simple Mode (Recommended)
```json
{
  "mcpServers": {
    "etendoAgent": {
      "type": "http",
      "httpUrl": "http://localhost:5006/11A747307CC543B48DC6A996DB4CAB37/mcp/",
      "note": "Simple mode - talk to the Copilot agent using natural language",
      "headers": {
        "etendo-token": "Bearer <your-sws-token-here>"
      }
    }
  }
}
```

#### Direct Mode (Advanced)
```json
{
  "mcpServers": {
    "etendoAgentDirect": {
      "type": "http",
      "httpUrl": "http://localhost:5006/11A747307CC543B48DC6A996DB4CAB37/direct/mcp/",
      "note": "Direct mode - execute agent tools directly + read system prompt",
      "headers": {
        "etendo-token": "Bearer <your-sws-token-here>"
      }
    }
  }
}
```
```

Then run Gemini CLI and the client will connect automatically to the configured MCP server:

```bash
gemini
```

<!-- SCREENSHOT: Gemini CLI connecting -->



### Visual Studio Code Configuration

Add this to your VS Code MCP config file. See [VS Code MCP docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more info.

#### VS Code Simple Mode Configuration

```json
"mcp": {
  "servers": {
    "etendoAgent": {
      "type": "http",
      "url": "http://localhost:5006/11A747307CC543B48DC6A996DB4CAB37/mcp",
      "headers": {
        "etendo-token": "Bearer your-sws-token-here"
      } 
    }
  }
}
```

#### VS Code Direct Mode Configuration

```json
"mcp": {
  "servers": {
    "etendoAgentDirect": {
      "type": "http",
      "url": "http://localhost:5006/11A747307CC543B48DC6A996DB4CAB37/direct/mcp",
      "headers": {
        "etendo-token": "Bearer your-sws-token-here"
      } 
    }
  }
}
```

<!-- SCREENSHOT DE CURSOR CONFIG -->

## Available Tools and Capabilities

The MCP server exposes different sets of tools depending on the agent type and connection mode selected:

### What MCP Delivers in Each Case

#### Multi-Model Agent + Simple Mode
**Tools delivered:**
- ✅ `ask_agent` - Send questions directly to the agent using natural language
- ✅ `ping`, `hello_world`, `server_info` - Basic connectivity tools

**How it works:** The agent receives your question and internally uses all its configured tools (API tools, file operations, knowledge base search, etc.) to provide a complete response.

#### Multi-Model Agent + Direct Mode  
**Tools delivered:**
- ✅ All agent's configured tools directly (API tools, file tools, knowledge base search, etc.)
- ✅ `get_agent_prompt` - Read the agent's system prompt and personality
- ✅ `ping`, `hello_world`, `server_info` - Basic connectivity tools
- ❌ NO `ask_agent` tool

**How it works:** You execute the agent's tools directly. Use `get_agent_prompt` to understand the agent's personality and follow the same instructions while using its tools.

#### LangGraph Agent + Simple Mode
**Tools delivered:**
- ✅ `ask_agent_supervisor` - Send questions to the supervisor agent
- ✅ `ping`, `hello_world`, `server_info` - Basic connectivity tools

**How it works:** The supervisor receives your question and coordinates with team members to provide comprehensive responses.

#### LangGraph Agent + Direct Mode
**Tools delivered:**
- ✅ `ask_agent_<MemberName>` - Individual tools for each team member (e.g., `ask_agent_DataAnalyst`, `ask_agent_ReportGenerator`)
- ✅ `get_agent_prompt` - Read the supervisor's orchestration prompt
- ✅ `ping`, `hello_world`, `server_info` - Basic connectivity tools
- ❌ NO `ask_agent_supervisor` tool

**How it works:** You can communicate directly with specific team members through their individual `ask_agent_<MemberName>` tools, bypassing the supervisor coordination.

### Tool Discovery and Usage

When connecting to an Etendo Copilot MCP server, clients can:

### Tool Comparison by Mode and Agent Type

| Feature | Simple Mode | Direct Mode |
|---------|-------------|-------------|
| **ask_agent tool** | ✅ Available | ❌ Not available |
| **Agent-specific tools** | ❌ Not directly accessible | ✅ Full access |
| **get_agent_prompt tool** | ❌ Not available | ✅ Available |
| **Basic utility tools** | ✅ Available | ✅ Available |
| **Use case** | Talk to agent naturally | Execute tools directly |
| **Control level** | Agent handles tools | You choose tools |
| **Complexity** | Simple | Advanced |

#### Multi-Model Agent Behavior

| Mode | Tools Delivered | Description |
|------|-----------------|-------------|
| **Simple** | `ask_agent` + basic tools | Send questions to the agent using natural language. The agent uses its configured tools internally to provide responses. |
| **Direct** | All agent tools + `get_agent_prompt` + basic tools | Direct access to all tools configured for the agent (API tools, file tools, knowledge base search, etc.) plus ability to read the agent's system prompt. This allows the MCP client to see and adopt the agent's personality and follow the same instructions while using its tools. |

#### LangGraph Agent Behavior

| Mode | Tools Delivered | Description |
|------|-----------------|-------------|
| **Simple** | `ask_agent_supervisor` + basic tools | Send questions to the supervisor agent who will coordinate with team members to provide comprehensive responses. |
| **Direct** | `ask_agent` tools for each team member + `get_agent_prompt` + basic tools | Direct access to individual team member agents through separate `ask_agent_<MemberName>` tools, allowing direct communication with specific team members plus access to the supervisor's orchestration prompt. |

!!! note "Agent Type Identification"
    You can identify the agent type in the Agent window in Etendo Classic:
    
    - **Multi-Model Agent**: Shows "Knowledge" and "Skills & Tools" tabs
    - **LangGraph**: Shows "Skills & Tools" and "Team Members" tabs
### Tool Discovery and Usage

When connecting to an Etendo Copilot MCP server, clients can:

1. **List Available Tools**: Use the MCP `list_tools` operation to see all available tools
2. **Inspect Tool Schemas**: Each tool includes detailed parameter schemas and descriptions
3. **Execute Tools**: Call tools using the standard MCP tool execution protocol
4. **Access Agent Capabilities**: 
   - In **Simple Mode**: Use `ask_agent` to leverage the full conversational capabilities of the agent
   - In **Direct Mode**: Execute specific agent tools directly and use `get_agent_prompt` to understand agent behavior

### Mode Selection Guidelines by Agent Type

#### For Multi-Model Agents

**Choose Simple Mode when:**
- You want to interact with the agent conversationally
- You prefer natural language queries over technical tool execution
- You want the agent to handle tool selection and orchestration automatically
- You're building user-facing applications that need conversational interfaces
- You want to leverage the agent's full reasoning capabilities with its knowledge base

**Choose Direct Mode when:**
- You need precise control over specific tool execution
- You're building developer tools or integrations
- You want to understand the agent's system prompt and configuration
- You need to execute specific tools (API calls, file operations, etc.) without conversational overhead
- You're creating workflows that require deterministic tool execution

#### For LangGraph Agents

**Choose Simple Mode when:**
- You want to leverage the full power of the supervisor-team coordination
- You prefer natural language queries that allow the supervisor to route to appropriate team members
- You want the supervisor to handle team member selection and task orchestration
- You're building user-facing applications that benefit from multi-agent collaboration
- You want comprehensive responses that combine expertise from multiple specialized agents

**Choose Direct Mode when:**
- You need to understand how the supervisor coordinates team members
- You want to access supervisor-level orchestration tools directly
- You're debugging or optimizing multi-agent workflows
- You need to see the supervisor's decision-making prompt and logic
- You're building integrations that require precise control over team coordination

### Authentication and Security

All tools respect the authentication provided via the `etendo-token` header:

- **User Context**: Tools execute with the permissions of the authenticated user
- **Data Access**: Database and API access is filtered according to user roles and permissions  
- **Security**: Sensitive operations require appropriate user privileges
- **Mode Isolation**: Each connection mode maintains separate instances for security and resource management

### Dynamic Tool Loading

The MCP server dynamically loads tools based on:

- **Agent Configuration**: Tools are loaded from the agent's configuration in Etendo Classic
- **User Permissions**: Only tools the user has access to are exposed
- **Module Dependencies**: Tools are available based on installed Etendo modules
- **Connection Mode**: Tool set varies between Simple and Direct modes

This dynamic approach ensures that each user sees only the tools they're authorized to use, and the tool set reflects the current state of the agent configuration in Etendo Classic.

