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
./gradlew copilot.mcp.config -Pusername=youruser -Ppassword=yourpass [-Prole=yourrole] -PagentId=YOUR_AGENT_ID
```

Where:

  - `YOUR_AGENT_ID` is the unique identifier of the Etendo Copilot agent you want to connect to.
  - `yourrole` is the role you want to assume when connecting to the agent (optional). If not specified, the default role will be used.
  - `youruser` is the username of the Etendo user account you want to use for authentication.
  - `yourpass` is the password of the Etendo user account you want to use for authentication.

### Connection Configuration

To connect to an Etendo Copilot agent's MCP server, you need the following configuration (if you used the `copilot.mcp.config` task, you will have this information):

```json
"etendoMCPName": {
  "type": "http",
  "httpUrl": "http://0.0.0.0:5006/ID/mcp/",
  "note": "For Streamable HTTP connections, add this URL directly in your MCP Client",
  "headers": {
    "etendo-token": "Bearer token"
  }
}
```

**Parameters:**

  - **etendoMCPName**: A unique name for this MCP server configuration, this can be any identifier you choose
  - **ID**: The unique identifier of the Etendo Copilot agent
  - **token**: The SWS (Secure Web Service) token of the user (without the "Bearer" prefix in the configuration)
  - **httpUrl**: The MCP endpoint URL following the pattern `http://{COPILOT_HOST}:{COPILOT_PORT}/{AGENT_ID}/mcp/`. The Copilot host will depend on your specific deployment and where the connection is being made from.

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

```json
{
  //Another Gemini config..
  "mcpServers": {
    //Another mcp server config..
    "etendoAgent": {
      "type": "http",
      "httpUrl": "http://localhost:5006/11A747307CC543B48DC6A996DB4CAB37/mcp/",
      "note": "For Streamable HTTP connections, add this URL directly in your MCP Client",
      "headers": {
        "etendo-token": "Bearer <your-sws-token-here>"
      }
    }
  }
}
```

Then run Gemini CLI and the client will connect automatically to the configured MCP server:

```bash
gemini
```

<!-- SCREENSHOT: Gemini CLI connecting -->



### Visual Studio Code Configuration

Add this to your VS Code MCP config file. See [VS Code MCP docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more info.

#### VS Code Remote Server Connection

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

<!-- SCREENSHOT DE CURSOR CONFIG -->

## Available Tools and Capabilities

The MCP server exposes a comprehensive set of tools that enable interaction with Etendo Copilot agents. These tools are divided into three main categories:

### 1. Agent-Specific Tools

These are the tools that belong to each individual agent, automatically loaded from the agent configuration stored in Etendo Classic. When you connect to an agent's MCP server, you get access to all the tools that have been configured for that specific agent in the Agent window.

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

### 2. Server-Level Extra Tools

These are additional tools provided by the MCP server itself, regardless of the specific agent configuration:

#### ask_agent
  **Purpose**: Allows MCP clients to send questions directly to the connected Etendo Copilot agent. It behaviour its the same as the Etendo Classic pop-up.

  **Parameters:**

    - `question` (string): The question to ask the agent
    - `conversation_id` (optional string): Conversation ID to maintain context across multiple interactions

  **Functionality:**

    - Forwards the question to the Etendo Copilot agent using the authenticated user's token.
    - Maintains conversation context when conversation_id is provided.
    - Returns the agent's response along with status information.
    - Handles authentication and error scenarios.

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

### 3. Basic Utility Tools

These are general-purpose tools for testing and server information:

#### `ping`
**Purpose**: Simple connectivity test tool

**Response**: Returns "pong" to confirm MCP connectivity

#### `hello_world`  
**Purpose**: Welcome message with server information

**Response**: Returns a greeting message including the agent identifier

#### `server_info`
**Purpose**: Provides basic information about the MCP server

**Response Format:**
```json
{
  "name": "etendo-copilot-mcp",
  "version": "0.1.0", 
  "description": "Etendo Copilot MCP Server with HTTP streaming",
  "transport": "http-streaming",
  "status": "running"
}
```

### Tool Discovery and Usage

When connecting to an Etendo Copilot MCP server, clients can:

1. **List Available Tools**: Use the MCP `list_tools` operation to see all available tools
2. **Inspect Tool Schemas**: Each tool includes detailed parameter schemas and descriptions
3. **Execute Tools**: Call tools using the standard MCP tool execution protocol
4. **Access Agent Capabilities**: Use `ask_agent` to leverage the full conversational capabilities of the agent

### Authentication and Security

All tools respect the authentication provided via the `etendo-token` header:

- **User Context**: Tools execute with the permissions of the authenticated user
- **Data Access**: Database and API access is filtered according to user roles and permissions  
- **Security**: Sensitive operations require appropriate user privileges

### Dynamic Tool Loading

The MCP server dynamically loads tools based on:

- **Agent Configuration**: Tools are loaded from the agent's configuration in Etendo Classic
- **User Permissions**: Only tools the user has access to are exposed
- **Module Dependencies**: Tools are available based on installed Etendo modules

This dynamic approach ensures that each user sees only the tools they're authorized to use, and the tool set reflects the current state of the agent configuration in Etendo Classic. 

