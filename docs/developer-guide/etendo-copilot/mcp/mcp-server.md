---
title: Developer Guide - MCP Server
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

Model Context Protocol (MCP) is an open-source protocol that enables seamless integration between Large Language Models (LLMs) and external tools, data sources, and services. It acts as a standardized "USB-C port for AI applications," allowing different AI systems to interact with various resources in a unified way.

Key benefits of MCP include:

- **Standardized Interface**: Consistent way to expose tools and resources to AI models
- **Security**: Built-in authentication and authorization mechanisms
- **Extensibility**: Easy to add new tools and capabilities
- **Interoperability**: Works with multiple AI providers and clients
- **Real-time Communication**: Supports both synchronous and asynchronous operations

## MCP Server Architecture in Etendo Copilot

Each Etendo Copilot agent automatically exposes an MCP server endpoint that provides:

- **Tools**: Functions that the agent can execute (database queries, API calls, calculations, etc.)
- **Resources**: Static or dynamic data that can be accessed (documents, configurations, logs, etc.)
- **Prompts**: Pre-configured prompt templates for common tasks

The MCP server runs alongside the agent and communicates using HTTP transport with optional Server-Sent Events (SSE) for streaming responses.

## Connecting to Etendo Copilot MCP Server

### Connection Configuration

To connect to an Etendo Copilot agent's MCP server, you need the following configuration:

```json
"etendo": {
  "type": "http",
  "httpUrl": "http://0.0.0.0:5006/ID/mcp/",
  "note": "For Streamable HTTP connections, add this URL directly in your MCP Client",
  "headers": {
    "etendo-token": "Bearer token"
  }
}
```

**Parameters:**

- **ID**: The unique identifier of the Etendo Copilot agent
- **token**: The SWS (Secure Web Service) token of the user (without the "Bearer" prefix in the configuration)
- **httpUrl**: The MCP endpoint URL following the pattern `http://{COPILOT_HOST}:{COPILOT_PORT}/{AGENT_ID}/mcp/`

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

[SCREENSHOT DE GEMINI CLI CONFIG FILE]

```json
{
  "servers": {
    "etendo-copilot": {
      "transport_type": "streamable_http",
      "url": "http://localhost:5005/my-agent-id/mcp/",
      "headers": {
        "etendo-token": "Bearer your-sws-token-here"
      },
      "timeout": 60
    }
  }
}
```

Then run Gemini CLI with the MCP server:

```bash
gemini-cli --mcp-server etendo-copilot
```

[SCREENSHOT DE GEMINI CLI CONECTANDO]

### Claude Desktop Configuration

For Claude Desktop, add the configuration to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
    "etendo-copilot": {
      "command": "npx",
      "args": [
        "-y", 
        "@modelcontextprotocol/client-stdio"
      ],
      "env": {
        "MCP_SERVER_URL": "http://localhost:5005/my-agent-id/mcp/",
        "MCP_AUTH_TOKEN": "Bearer your-sws-token-here"
      }
    }
  }
}
```

[SCREENSHOT DE CLAUDE DESKTOP CONFIG]

### Cursor IDE Configuration

In Cursor IDE, configure the MCP server in your `.cursorrules` or MCP settings:

```json
{
  "mcp": {
    "servers": {
      "etendo": {
        "url": "http://localhost:5005/my-agent-id/mcp/",
        "headers": {
          "etendo-token": "Bearer your-sws-token-here"
        }
      }
    }
  }
}
```

[SCREENSHOT DE CURSOR CONFIG]

## Available Tools and Capabilities

The MCP server exposes all tools available to the specific Etendo Copilot agent. Common categories include:

### Database Tools
- **Query Execution**: Run read-only queries on Etendo database
- **Schema Inspection**: Access table schemas and relationships
- **Data Analysis**: Aggregate and analyze business data

### Business Process Tools
- **Document Management**: Create, read, update documents
- **Workflow Operations**: Trigger and monitor business processes
- **Reporting**: Generate custom reports and analytics

### Integration Tools
- **API Calls**: Execute external API requests
- **Data Synchronization**: Sync data with external systems
- **Notification Services**: Send alerts and messages

### Analysis Tools
- **Financial Calculations**: Perform accounting and financial operations
- **Statistical Analysis**: Run statistical computations on data
- **Forecasting**: Generate predictions based on historical data

[SCREENSHOT DE TOOLS LIST EN MCP CLIENT]

## Discovering Available Tools

To see what tools are available from an agent's MCP server, you can use the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:5005/my-agent-id/mcp/ \
  --headers "etendo-token: Bearer your-token" \
  --method tools/list
```

This will return a list of all available tools with their descriptions and parameters:

```json
{
  "tools": [
    {
      "name": "query_database",
      "description": "Execute read-only SQL queries on Etendo database",
      "inputSchema": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "SQL query to execute"
          }
        },
        "required": ["query"]
      }
    },
    {
      "name": "create_sales_order",
      "description": "Create a new sales order in Etendo",
      "inputSchema": {
        "type": "object",
        "properties": {
          "customer_id": {
            "type": "string",
            "description": "Customer identifier"
          },
          "products": {
            "type": "array",
            "description": "List of products to order"
          }
        },
        "required": ["customer_id", "products"]
      }
    }
  ]
}
```

[SCREENSHOT DE TOOLS DISCOVERY]

## Using MCP Tools in Practice

### Example: Querying Business Data

```bash
# Using MCP Inspector to call a tool
npx @modelcontextprotocol/inspector --cli http://localhost:5005/sales-agent/mcp/ \
  --headers "etendo-token: Bearer your-token" \
  --method tools/call \
  --tool-name query_database \
  --tool-arg query="SELECT COUNT(*) FROM c_order WHERE created >= '2024-01-01'"
```

### Example: Python Client

```python
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def main():
    # Connect to Etendo Copilot MCP server
    headers = {"etendo-token": "Bearer your-sws-token-here"}
    
    async with streamablehttp_client(
        "http://localhost:5005/my-agent-id/mcp/",
        headers=headers
    ) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")
            
            # Call a specific tool
            result = await session.call_tool(
                "query_database",
                {"query": "SELECT name FROM ad_client WHERE isactive='Y'"}
            )
            print(f"Query result: {result.content}")

if __name__ == "__main__":
    asyncio.run(main())
```

[SCREENSHOT DE PYTHON CLIENT EXECUTION]

## Advanced Configuration

### Custom Transport Settings

For production environments or specific network configurations, you can customize transport settings:

```json
{
  "transport_type": "streamable_http",
  "url": "https://your-domain.com/copilot/agent-id/mcp/",
  "headers": {
    "etendo-token": "Bearer your-token",
    "User-Agent": "MyApp/1.0"
  },
  "timeout": 120,
  "retry_attempts": 3,
  "retry_delay": 5
}
```

### SSL/TLS Configuration

For secure connections, ensure your MCP client supports HTTPS and proper certificate validation:

```json
{
  "url": "https://secure.etendo.com/copilot/agent-id/mcp/",
  "ssl_verify": true,
  "ssl_cert_path": "/path/to/client.crt",
  "ssl_key_path": "/path/to/client.key"
}
```

[SCREENSHOT DE HTTPS CONNECTION]

## Troubleshooting

### Common Connection Issues

1. **401 Unauthorized**: Check your SWS token validity and user permissions
2. **404 Not Found**: Verify the agent ID and MCP endpoint URL
3. **Connection Timeout**: Check network connectivity and firewall settings
4. **SSL Certificate Errors**: Verify certificate configuration for HTTPS connections

### Debug Mode

Enable debug logging to troubleshoot connection issues:

```bash
# Set environment variable for debug logging
export MCP_DEBUG=true

# Run your MCP client with verbose output
npx @modelcontextprotocol/inspector --cli http://localhost:5005/agent/mcp/ \
  --headers "etendo-token: Bearer token" \
  --debug
```

### Checking Agent Status

Verify that your Etendo Copilot agent is running and accessible:

```bash
# Check agent health endpoint
curl -H "etendo-token: Bearer your-token" \
  http://localhost:5005/my-agent-id/health
```

[SCREENSHOT DE TROUBLESHOOTING PANEL]

## Best Practices

### Security
- Always use HTTPS in production
- Rotate SWS tokens regularly
- Implement proper access controls
- Monitor and log MCP server access

### Performance
- Use connection pooling for multiple requests
- Implement request timeouts
- Cache frequently accessed data
- Monitor server performance metrics

### Development
- Test MCP connections before deploying
- Use MCP Inspector for development and debugging
- Document your custom tools and their parameters
- Implement proper error handling in client applications

## Integration Examples

### Node.js Application

```javascript
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

class EtendoCopilotClient {
  constructor(agentId, token) {
    this.baseUrl = `http://localhost:5005/${agentId}/mcp/`;
    this.headers = { 'etendo-token': `Bearer ${token}` };
  }

  async connect() {
    const transport = new StreamableHTTPClientTransport(
      new URL(this.baseUrl),
      { headers: this.headers }
    );

    this.client = new Client({
      name: 'etendo-mcp-client',
      version: '1.0.0'
    });

    await this.client.connect(transport);
    return this.client;
  }

  async executeQuery(sql) {
    const result = await this.client.callTool('query_database', { query: sql });
    return result.content;
  }
}
```

### Integration with Business Intelligence Tools

The MCP server can be integrated with BI tools that support custom data connectors, enabling real-time access to Etendo data through natural language queries.

[SCREENSHOT DE BI INTEGRATION]

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
