---
tags:
    - Copilot
    - Memory
    - Tool
    - Vector Database
    - CRUD
    - Chroma
---

# Memory Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Memory Tool** is a comprehensive tool for managing user memories in a vector database using Chroma as the backend storage. It provides CRUD operations (Create, Read, Update, Delete) for user-specific memories with vector similarity search capabilities, allowing assistants to store and retrieve contextual information across conversations.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool enables assistants to maintain persistent memory across conversations by storing important information in a vector database. It supports semantic search capabilities, allowing for intelligent retrieval of relevant memories based on context and similarity. The tool is user-scoped, ensuring data isolation and privacy.

Key features include:

- **Memory Persistence**: Store important information that persists across conversation sessions
- **Semantic Search**: Find relevant memories using vector similarity search
- **User Isolation**: Each user's memories are stored separately and securely
- **CRUD Operations**: Complete set of operations for memory management
- **Automatic ID Generation**: Unique identifiers are automatically assigned to each memory

## Supported Operations

### Add Mode
Creates a new memory with automatic ID generation.

- **Required Parameters**: `mode` (set to "add"), `memory` (content to store)
- **Returns**: Success message with the generated memory ID

### Search Mode
Finds memories using vector similarity search.

- **Required Parameters**: `mode` (set to "search"), `query` (search string)
- **Optional Parameters**: `k` (maximum number of results, default: 3)
- **Returns**: List of matching memories with their IDs

### Update Mode
Modifies existing memory content while preserving metadata.

- **Required Parameters**: `mode` (set to "update"), `memory_id` (target memory), `memory` (new content)
- **Returns**: Success message confirming the update

### Delete Mode
Removes a specific memory from the database.

- **Required Parameters**: `mode` (set to "delete"), `memory_id` (target memory)
- **Returns**: Success message confirming deletion

## Usage Examples

### Adding a Memory

To store a new memory:

```json
{
    "mode": "add",
    "memory": "User prefers dark theme and 24-hour time format"
}
```

**Expected Output:**
```json
{
    "result": "Memory added for user_id user123: User prefers dark theme and 24-hour time format (memory_id: 550e8400-e29b-41d4-a716-446655440000)"
}
```

### Searching Memories

To find relevant memories:

```json
{
    "mode": "search",
    "query": "user preferences",
    "k": 5
}
```

**Expected Output:**
```json
{
    "result": "- User prefers dark theme and 24-hour time format (memory_id: 550e8400-e29b-41d4-a716-446655440000)\n- User likes concise responses (memory_id: 550e8400-e29b-41d4-a716-446655440001)"
}
```

### Updating a Memory

To modify existing memory content:

```json
{
    "mode": "update",
    "memory_id": "550e8400-e29b-41d4-a716-446655440000",
    "memory": "User prefers dark theme, 24-hour time format, and compact layout"
}
```

**Expected Output:**
```json
{
    "result": "Memory updated for user_id user123: User prefers dark theme, 24-hour time format, and compact layout (memory_id: 550e8400-e29b-41d4-a716-446655440000)"
}
```

### Deleting a Memory

To remove a specific memory:

```json
{
    "mode": "delete",
    "memory_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Expected Output:**
```json
{
    "result": "Memory with memory_id 550e8400-e29b-41d4-a716-446655440000 deleted for user_id user123"
}
```

## Technical Implementation

### Vector Database
The tool uses Chroma as the vector database backend, configured with:
- Persistent storage in user-specific directories
- Embedding functions for semantic search
- Automatic document vectorization

### User Isolation
Memories are isolated by user through:
- User-specific vector store collections (`{assistant_id}_memories`)
- Metadata filtering based on `user_id` from thread context
- Secure access control ensuring users can only access their own memories

### Context Variables
The tool requires the following context variables:
- `assistant_id`: Unique identifier for the assistant instance
- `ad_user_id`: User identifier from Active Directory

## Error Handling

The tool includes comprehensive error handling for:
- Invalid operation modes
- Missing required parameters
- Context variable validation
- Database operation failures
- User permission verification

Common error responses:
- `"Invalid mode 'xyz'. Use 'add', 'search', 'update', or 'delete'."`
- `"The 'memory' parameter is required for 'add' mode."`
- `"No memory found with memory_id xyz for user_id user123"`
- `"assistant_id or ad_user_id not found in Payload."`
