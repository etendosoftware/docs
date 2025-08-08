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

The **Model Context Protocol (MCP)** is an open protocol developed by Anthropic that standardizes how AI applications provide context to Large Language Models (LLMs). MCP acts as a "USB-C port for AI applications," enabling models to connect uniformly with external data sources, tools, and services.

This guide provides a comprehensive introduction to MCP concepts, architecture, and its implementation within the Etendo Copilot ecosystem, helping developers understand how to leverage this protocol for building scalable and secure AI integrations.

## What is MCP?

MCP is a protocol that solves the fragmentation problem in the AI ecosystem, where each application required custom integrations to connect with different data sources and tools. With MCP, both developers and organizations can create reusable connectors that work across multiple applications and platforms.

### Key Features

- **Open Protocol**: Available to the entire developer community
- **Standardization**: Uniform interface for context and tool integration
- **Scalability**: Modular architecture that allows easy extension
- **Security**: Built-in permission controls and authentication
- **Flexibility**: Support for multiple transport types and data formats

## MCP Architecture

MCP uses a client-server architecture that facilitates communication between AI applications and external data sources.

### Core Components

#### 1. Hosts
Hosts are the primary applications through which users interact with the protocol:
- **Function**: Execute AI models and manage user interface.

- **Responsibilities**: 
    - Initiate connections with MCP servers.
    - Control permissions and security constraints.
    - Manage conversation flow.
    - Handle user consent for data sharing.

#### 2. Clients
Clients act as intermediaries between hosts and MCP servers:

- **Function**: Facilitate communication between hosts and servers.

- **Responsibilities**:
    - Send requests to servers.
    - Negotiate capabilities with servers.
    - Manage tool execution requests.
    - Process and display responses to users.

#### 3. Servers
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

#### Resources
Resources represent contextual data and information sources available to models:

  - Local files (`file://log.txt`)
  - Database schemas (`database://schema`)
  - External APIs
  - Knowledge bases

#### Tools
Tools enable models to perform specific actions:

  - Web searches
  - Mathematical calculations
  - Database access
  - File system operations

#### Prompts
Prompts are predefined templates that streamline workflows:
```markdown
Generate a product slogan based on the following {{product}} with the following {{keywords}}
```

### Client Features

#### Sampling
Enables servers to initiate autonomous behaviors and recursive LLM interactions, allowing:

  - Server-initiated agent behaviors
  - Recursive LLM interactions
  - Requests for additional model completions

## Security and Authorization

MCP includes multiple security mechanisms to ensure safe interactions:

### Tool Permission Control

  - Clients can specify which tools a model is allowed to use during a session
  - Dynamically configurable permissions based on organizational policies
  - Reduced risk of unintended or unsafe operations

### Authentication

  - Servers can require authentication before granting access
  - Support for API keys, OAuth tokens, and other authentication schemes
  - Ensuring only trusted clients and users can invoke server-side capabilities

### Parameter Validation

  - Enforced validation for all tool invocations
  - Each tool defines expected types, formats, and constraints for its parameters
  - Prevention of malformed or malicious input

### Rate Limiting

  - Implementation of rate limits for tool calls and resource access
  - Limits applicable per user, per session, or globally
  - Protection against denial-of-service attacks

## Use Cases

### In Etendo Copilot Context

MCP in Etendo Copilot allows agents to access in a standardized way:

- **Databases**: Etendo database schemas and queries
- **APIs**: Etendo web services and external systems
- **Files**: Documents, logs, and system configurations
- **Custom Tools**: Etendo-specific functionalities

### Benefits for Developers

1. **Reusability**: Create connectors once and use them across multiple applications
2. **Interoperability**: Compatibility between different AI tools and platforms
3. **Simplified Maintenance**: Centralized updates instead of multiple integrations
4. **Scalability**: Easy addition of new capabilities without modifying existing applications

## Implementation

### Supported Languages

MCP has official SDKs for multiple programming languages:

  - **TypeScript/JavaScript**
  - **Python**
  - **C#/.NET**
  - **Java**
  - **Kotlin**
  - **Swift**
  - **Rust**
  - **Go**

### Transport Types

MCP supports various communication methods:

  - **STDIO**: For command-line tools and local integrations
  - **Server-Sent Events (SSE)**: For web applications with server-to-client streaming
  - **WebSockets**: For bidirectional real-time communication

## Conclusion

The Model Context Protocol represents a significant advancement in AI integration standardization. By providing a common framework for language models to access external data and tools, MCP facilitates the development of more robust, scalable, and maintainable AI applications.

In the context of Etendo Copilot, MCP enables smoother integration between AI agents and enterprise systems, providing standardized access to Etendo data and functionalities while maintaining the security and control necessary for enterprise environments.

## Additional Resources

  - [Official MCP Documentation](https://modelcontextprotocol.io/){target="_blank"}
  - [MCP Specification Repository](https://github.com/modelcontextprotocol/specification){target="_blank"}
  - [MCP Server Guide](../concepts/model-context-protocol.md){target="_blank"}
