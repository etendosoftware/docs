---
title: Developer Guide - Configure API Tokens for Etendo Copilot
status: beta
tags:
    - How to
    - API Tokens
    - Authentication
    - Copilot Integration
    - Security
---

# How to configure API tokens for Etendo Copilot

## Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

This guide explains how to configure and use **API Tokens** in **Etendo Copilot** for secure authentication with external services. API tokens allow agents to authenticate with third-party APIs while maintaining security through proper token management and replacement mechanisms.

## What are API Tokens in Etendo Copilot?

API Tokens in Etendo Copilot are secure credentials that allow agents to authenticate with external services and APIs. These tokens are:

- **Context-aware**: Different tokens can be assigned based on user, role, or global settings
- **Prioritized**: The system automatically selects the most appropriate token based on context
- **Secure**: Tokens are stored securely and only exposed during prompt processing
- **Flexible**: Supports multiple aliases for different services

## API Token Priority System

The system implements a sophisticated priority mechanism for token selection:

1. **User + Role specific**: Tokens assigned to both a specific user and role (highest priority)
2. **User specific**: Tokens assigned only to a specific user 
3. **Role specific**: Tokens assigned only to a specific role
4. **Global**: Tokens with no user or role assignment (lowest priority)

This ensures that the most contextually appropriate token is always used.

## Step-by-Step Configuration

### 1. Access API Token Configuration

1. **Open Etendo Classic** with the role you want to add the key.
2. **Navigate** to **Service** → **Copilot** → **API Token**

### 2. Create a New API Token

![API Token Configuration](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-configure-api-tokens/api-token-configuration.png)

Create a new record with the following fields:

#### Required Fields

- **Alias**: A unique identifier for the token (e.g., "OPENAI_API", "GITHUB_TOKEN")
- **Token**: The actual API key or token value
- **Client**: The client organization (automatically set)
- **Organization**: The organization scope

#### Optional Context Fields

- **User Contact**: Assign to a specific user (leave empty for broader scope)
- **Role**: Assign to a specific role (leave empty for broader scope)

#### Field Descriptions

| Field | Description | Example |
|-------|-------------|---------|
| **Alias** | Unique identifier for referencing the token in prompts | `OPENAI_API` |
| **Token** | The actual API key or authentication token | `sk-abc123...` |
| **User Contact** | Specific user who can use this token | John Doe |
| **Role** | Specific role that can use this token | Sales Manager |

### 3. Token Scope Examples

#### Global Token (Available to All)
```
Alias: WEATHER_API
Token: abc123def456
User Contact: (empty)
Role: (empty)
```

#### User-Specific Token
```
Alias: GITHUB_TOKEN
Token: ghp_xyz789
User Contact: developer@company.com
Role: (empty)
```

#### Role-Specific Token
```
Alias: SALESFORCE_API
Token: sfdc_abc123
User Contact: (empty)
Role: Sales Manager
```

#### User + Role Specific Token
```
Alias: ADMIN_API
Token: admin_secret123
User Contact: admin@company.com
Role: System Administrator
```

## Token Usage in Prompts

### Token Placeholder Format

API tokens are referenced in prompts using the following format:
```
@TOKEN_ALIAS@
```

The alias is automatically converted to uppercase for placeholder matching.

### Example Usage

#### In Agent Prompts
```
Use the OpenAI API with key @OPENAI_API@ to generate a response.
Access GitHub repository using token @GITHUB_TOKEN@.
Connect to Salesforce with @SALESFORCE_API@ credentials.
```

#### In Tool Configurations
```json
{
  "api_key": "@OPENAI_API@",
  "base_url": "https://api.openai.com/v1",
  "headers": {
    "Authorization": "Bearer @OPENAI_API@"
  }
}
```

### Token Replacement Process

When prompts are processed, the system:

1. **Identifies** all token placeholders in the format `@ALIAS@`
2. **Evaluates** the current user and role context
3. **Selects** the highest priority token for each alias
4. **Replaces** placeholders with actual token values
5. **Processes** the prompt with authenticated credentials

## Security Best Practices

### Token Management

- **Use specific scopes**: Assign tokens to specific users/roles when possible
- **Regular rotation**: Update tokens periodically for security
- **Minimal permissions**: Use tokens with the least required permissions
- **Monitor usage**: Track token usage through system logs

### Access Control

- **Role-based access**: Leverage Etendo's role system for token access
- **User assignments**: Assign personal tokens to individual users
- **Client separation**: Tokens are automatically scoped to the current client

### Storage Security

- **Encrypted storage**: Tokens are stored securely in the database
- **No logging**: Token values are never logged in plain text
- **Memory protection**: Tokens are only loaded during prompt processing

## Troubleshooting

### Common Issues

#### Token Not Being Replaced

**Problem**: Placeholder `@MY_TOKEN@` is not being replaced

**Solutions**:
1. Verify the alias exactly matches (case-insensitive)
2. Check that an active token exists for your context
3. Ensure the token is assigned to your user/role or is global

#### Wrong Token Being Used

**Problem**: A different token than expected is being used

**Solutions**:
1. Review the priority system - more specific tokens override general ones
2. Check if multiple tokens exist with the same alias
3. Verify your current user and role context

#### Token Access Denied

**Problem**: Cannot access or use a specific token

**Solutions**:
1. Verify you have the correct role assigned
2. Check if the token is user-specific and assigned to another user
3. Ensure the token is active and properly configured

### Debugging Token Resolution

To debug which token is being selected:

1. **Check your context**:
   - Current user: `@USERNAME@`
   - Current role: `@ROLE_NAME@`

2. **Review token configurations** for the same alias
3. **Verify priority order** based on user/role assignments

## Advanced Configuration

### Multiple Tokens for Different Environments

```
# Development Environment
Alias: OPENAI_API
Token: sk-dev123...
Role: Developer

# Production Environment  
Alias: OPENAI_API
Token: sk-prod456...
Role: System Administrator
```

### Service-Specific Token Organization

```
# GitHub Integration
Alias: GITHUB_TOKEN
Token: ghp_github123...

# OpenAI Services
Alias: OPENAI_API
Token: sk-openai456...

# Custom API
Alias: CUSTOM_SERVICE
Token: custom_abc789...
```

## Integration with Other Features

### MCP Server Authentication

API tokens can be used in MCP server configurations:

```json
{
  "command": "npx",
  "args": ["custom-mcp-server"],
  "env": {
    "API_KEY": "@CUSTOM_API@",
    "AUTH_TOKEN": "@SERVICE_TOKEN@"
  }
}
```

### Agent Tool Authentication

Agents can use tokens for external API calls:

```
Agent instruction: "When making API calls, use @OPENAI_API@ for authentication"
```

## See Also

- [How to Configure MCP Servers on Agents](how-to-configure-mcp-servers-on-agents.md)
- [Model Context Protocol (MCP)](../concepts/model-context-protocol.md)
- [Agent Configuration Guide](how-to-configure-agents.md)
