---
tags:
    - Copilot
    - Task Management
    - Workflow
    - Utilities
---

# Task Management Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot`

## Overview

The Task Management Tool is a utility for managing tasks dynamically within a conversation state. It provides flexible task queue operations such as adding, retrieving, checking status, and marking tasks as completed. This tool is particularly useful in orchestrated workflows where multi-step task handling is required.

!!!info
    This tool is part of the Copilot Framework and is typically used inside multi-agent or workflow-based agents.

## Functionality

This tool allows for **centralized task queue management** using different operation modes:

### Supported Modes:
- `get_next`: Retrieves and sets the next task to be processed.
- `add_tasks`: Adds one or more new tasks to the processing queue.
- `status`: Retrieves the current task queue status, including current, pending, and completed tasks.
- `mark_done`: Marks the current task as completed and moves it to the finished list.

The tool works by modifying and storing task-related data in the agent's shared state, making it ideal for orchestrating step-by-step workflows in multi-agent systems.

### Parameters

| Name        | Type   | Description                                                                 |
|-------------|--------|-----------------------------------------------------------------------------|
| `mode`      | string | Operation mode: `get_next`, `add_tasks`, `status`, or `mark_done`.         |
| `state`     | dict   | Injected state containing task queues and statuses.                         |
| `tool_call_id` | string | Unique tool call ID used for message tracking.                           |
| `new_tasks` | list   | Optional. List of new tasks to add (required for `add_tasks` mode).         |

## Behavior Summary

- **get_next**: Pops the next task from the queue and sets it as `current_task`.
- **add_tasks**: Appends a list of tasks to the task queue.
- **status**: Returns a count and current snapshot of all task queues.
- **mark_done**: Moves the current task to the list of completed tasks.

## Example Use Case

A typical example could be a multi-step invoice validation process. Each invoice is a separate task, and this tool helps to:

- Feed all invoice tasks at once.
- Retrieve each task sequentially.
- Track and mark them as completed as they are processed.

## Tool Response Format

The tool returns a **Command** object that includes:

- Updated shared state (task lists).
- A `ToolMessage` describing what was done (used for logging or further routing).

!!!note
    This tool should be used with LangGraph or other LangChain multi-step orchestration engines.