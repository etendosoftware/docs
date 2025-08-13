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

## Connecting to Etendo Copilot MCP Server

### Token-Based Authentication

The MCP server uses token-based authentication via the `etendo-token` header, using the SWS (Secure Web Service) token of the user. This token can be obtained through the Etendo Classic `/sws/login` endpoint.
A quick way to get the basic config of the MCP server can be get using the Gradle task called `copilot.mcp.config`.

``` bash
./gradlew copilot.mcp.config -Pusername=youruser -Ppassword=yourpass [-Prole=yourrole] -PagentId=YOUR_AGENT_ID [-Pmode=simple|direct]
```

Where:

  - `YOUR_AGENT_ID` is the unique identifier of the Etendo Copilot agent you want to connect to.
  - `yourrole` is the role you want to assume when connecting to the agent (optional). If not specified, the default role will be used.
  - `youruser` is the username of the Etendo user account you want to use for authentication.
  - `yourpass` is the password of the Etendo user account you want to use for authentication.
  - `mode` is the connection mode (optional): `simple` or `direct`. If not specified, defaults to `simple` mode.

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

### Mode Selection

When running the configuration task, you'll be prompted to select a mode:

```
🔧 Select connection mode:
  1. Simple mode - Exposes a single tool to talk to the Copilot agent (recommended)
  2. Direct mode - Exposes all agent tools for direct execution + prompt reader
Please enter mode (1 for simple, 2 for direct) [default: 1]:
```

You can also specify the mode directly via command line parameter:

```bash
# Simple mode (default)
./gradlew copilot.mcp.config -PagentId=MY_AGENT -Pmode=simple

# Direct mode  
./gradlew copilot.mcp.config -PagentId=MY_AGENT -Pmode=direct
```

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

The MCP server exposes different sets of tools depending on the connection mode selected:

### Simple Mode Tools

In simple mode, the following tools are available:

#### ask_agent
  **Purpose**: Allows MCP clients to send questions directly to the connected Etendo Copilot agent. Its behavior is the same as the Etendo Classic pop-up.

  **Parameters:**

    - `question` (string): The question to ask the agent
    - `conversation_id` (optional string): Conversation ID to maintain context across multiple interactions

  **Functionality:**

    - Forwards the question to the Etendo Copilot agent using the authenticated user's token.
    - Maintains conversation context when conversation_id is provided.
    - Returns the agent's response along with status information.
    - Handles authentication and error scenarios.
    - The agent internally uses its configured tools to answer your question.

  **Example Usage:**
  ```json
  {
    "question": "What are the latest sales reports?",
    "conversation_id": "conv_123"
  }
  ```

  **Response Format:**
  ```json
  {
    "success": true,
    "answer": {
      "response": "Here are the latest sales reports...",
      "conversation_id": "conv_123"
    },
    "status_code": 200
  }
  ```

#### Basic Utility Tools (Simple Mode)
- **ping**: Simple connectivity test tool
- **hello_world**: Welcome message with server information  
- **server_info**: Provides basic information about the MCP server

### Direct Mode Tools

In direct mode, the following tools are available:

#### All Agent-Specific Tools

These are the tools that belong to each individual agent, automatically loaded from the agent configuration stored in Etendo Classic. When you connect to an agent's MCP server in direct mode, you get access to all the tools that have been configured for that specific agent in the Agent window.

**Types of Agent Tools:**

  - **Business Logic Tools**: Tools configured for the agent via the Skills & Tools tab in the Agent window
  - **API Integration Tools**: Automatically generated tools from OpenAPI specifications when Knowledge Base files are configured with the behavior `[Agent] SPEC: Add as agent specification`
  - **Knowledge Base Search Tool**: Automatically included when the agent has a Knowledge Base configured, allowing semantic search through the agent's knowledge

**Examples of Common Agent Tools:**

  - **API Call Tool**: Enables HTTP requests to external APIs and Etendo Classic endpoints
  - **Read File Tool**: Reads the contents of files from the local filesystem  
  - **Write File Tool**: Creates and modifies files with backup functionality
  - **Docker Tool**: Executes Python or Bash code in isolated Docker containers
  - **OCR Tool**: Extracts text and information from images
  - **XLS Tool**: Processes Excel and CSV files
  - **Task Management Tool**: Creates and manages background tasks in Etendo
  - **Database Query Tools**: Executes controlled database queries (when configured)

#### get_agent_prompt
  **Purpose**: Retrieves the system prompt and configuration of the connected agent

  **Parameters:** None

  **Functionality:**

    - Returns the agent's system prompt (the instructions that define the agent's behavior)
    - Provides agent metadata like name and description
    - Useful for understanding how the agent is configured and what it can do

  **Response Format:**
  ```json
  {
    "success": true,
    "agent_name": "Sales Assistant",
    "agent_prompt": "You are a sales assistant that helps users analyze sales data and generate reports..."
  }
  ```

#### Basic Utility Tools (Direct Mode)
- **ping**: Simple connectivity test tool
- **hello_world**: Welcome message with server information (shows "Direct Mode")
- **server_info**: Provides basic information about the MCP server (includes mode indicator)

### Tool Comparison by Mode

| Feature | Simple Mode | Direct Mode |
|---------|-------------|-------------|
| **ask_agent tool** | ✅ Available | ❌ Not available |
| **Agent-specific tools** | ❌ Not directly accessible | ✅ Full access |
| **get_agent_prompt tool** | ❌ Not available | ✅ Available |
| **Basic utility tools** | ✅ Available | ✅ Available |
| **Use case** | Talk to agent naturally | Execute tools directly |
| **Control level** | Agent handles tools | You choose tools |
| **Complexity** | Simple | Advanced |
### Tool Discovery and Usage

When connecting to an Etendo Copilot MCP server, clients can:

1. **List Available Tools**: Use the MCP `list_tools` operation to see all available tools
2. **Inspect Tool Schemas**: Each tool includes detailed parameter schemas and descriptions
3. **Execute Tools**: Call tools using the standard MCP tool execution protocol
4. **Access Agent Capabilities**: 
   - In **Simple Mode**: Use `ask_agent` to leverage the full conversational capabilities of the agent
   - In **Direct Mode**: Execute specific agent tools directly and use `get_agent_prompt` to understand agent behavior

### Mode Selection Guidelines

**Choose Simple Mode when:**
- You want to interact with the agent conversationally
- You prefer natural language queries over technical tool execution
- You want the agent to handle tool selection and orchestration
- You're building user-facing applications that need conversational interfaces
- You want to leverage the agent's full reasoning capabilities

**Choose Direct Mode when:**
- You need precise control over tool execution
- You're building developer tools or integrations
- You want to understand the agent's system prompt and configuration
- You need to execute specific tools without conversational overhead
- You're creating workflows that require deterministic tool execution

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

