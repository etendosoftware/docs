---
title: How to Integrate Copilot with Jira via MCP
status: beta
tags:
  - How to
  - Etendo Copilot
  - Jira
  - MCP
  - Integration
  - Automation
---

# How to Integrate Copilot with Jira via MCP

## Overview

!!! note "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

Integrating **Etendo Copilot** with **Jira** allows agents to create, update and query Jira issues directly from the ERP interface. This avoids switching between applications and enables a unified conversational workflow.

This guide explains how to configure a **Model Context Protocol (MCP)** server that bridges Copilot and the Jira REST API using the Atlassian MCP implementation.

### Key Capabilities

- Create single or bulk issues.
- Update issue fields (status transitions, comments, worklogs, links, versions, epics).
- Query issues, projects, boards, sprints and changelogs.
- Download attachments.
- Maintain contextual, secure access through Etendo Copilot.

### When to Use This Integration
Use it when development, support or operations teams manage their backlog in Jira and want conversational access from within Etendo to speed up task triage, follow up or reporting.

## Prerequisites

- Etendo and **Etendo Copilot** installed.
- Valid Jira user with API Token.
- Network access from the Etendo server to `*.atlassian.net`.
- API Token stored in Etendo as an **API Token** record (see below).

!!! info
    Store the Jira API token using the guide: [How to Configure API Tokens](./how-to-configure-api-tokens.md). Use alias `JIRA_TOKEN` (recommended).

## Step 1. Create (or Reuse) the Jira API Token

1. Open Atlassian Account Settings > Security > API tokens.
2. Create a new token (label it for Etendo Copilot usage).
3. Copy the token.
4. In Etendo open :material-menu: `Application` > `Service` > `Copilot API Tokens` and create a record:

   - Organization: Select proper scope.
   - Alias: `JIRA_TOKEN`.
   - Token: Paste the copied value.
   - (Optional) User / Role: Narrow scope if required.

## Step 2. Register the Jira MCP Server

:material-menu: `Application` > `Service` > `Copilot` > `MCP Servers Configuration`

Create a new record and paste the following JSON (adjust `JIRA_URL`, `JIRA_USERNAME` if needed). The token placeholder will be replaced automatically at runtime using the API Token priority system.

```json
{
  "transport": "stdio",
  "command": "uvx",
  "args": [
    "--from", "git+https://github.com/etendosoftware/etendo-mcp-atlassian.git@main",
    "etendo-mcp-atlassian",
    "--enabled-tools=jira_search,jira_get_issue,jira_get_all_projects,jira_get_project_issues,jira_get_worklog,jira_get_transitions,jira_search_fields,jira_get_agile_boards,jira_get_board_issues,jira_get_sprints_from_board,jira_get_sprint_issues,jira_get_link_types,jira_batch_get_changelogs,jira_get_user_profile,jira_download_attachments,jira_get_project_versions,jira_create_issue,jira_update_issue,jira_batch_create_issues,jira_add_comment,jira_transition_issue,jira_add_worklog,jira_link_to_epic,jira_create_issue_link"
  ],
  "env": {
    "JIRA_URL": "https://yourcompany.atlassian.net",
    "JIRA_USERNAME": "user@example.com",
    "JIRA_API_TOKEN": "@JIRA_TOKEN@",
    "LOG_LEVEL": "INFO"
  }
}
```

Fields explained:

- `transport`: STDIO-based MCP communication.
- `command` / `args`: Uses `uvx` to run the Atlassian MCP package at the specified version.
- `--enabled-tools`: Comma-separated list of Jira capabilities exposed to Copilot.
- `env` variables:
  - `JIRA_URL`: Base Jira Cloud (or Server) URL.
  - `JIRA_USERNAME`: Jira user (email for Cloud).
  - `JIRA_API_TOKEN`: Placeholder resolved to stored token.
  - `LOG_LEVEL`: Adjust (`DEBUG`, `INFO`, etc.).

!!! warning
    Do not paste the raw API token directly. Always use the placeholder (e.g. `@JIRA_TOKEN@`). This ensures proper scoping, priority handling and secret redaction.

## Step 3. Link the MCP to an Agent

:material-menu: `Application` > `Service` > `Copilot` > `Agent`

1. Open (or create) the target agent.
2. Go to the **MCP Servers** tab.
3. Add a new line selecting the Jira MCP server.
4. Save and click **Sync Agent**.

## Step 4. Test the Integration

Example prompts:

```
Create a Jira issue in project ERP with summary "Add tax validation" and assign it to me.
Search Jira issues with status = In Progress assigned to current user ordered by updated date.
Transition issue ERP-123 to In Progress and add a comment "Work started".
Add a worklog of 2h to issue ERP-456 for today's date.
Link issue ERP-789 to epic ERP-22.
```

!!! success
    If properly configured the agent responds with structured issue data (key, summary, status) or confirmation of actions performed.

## Available Jira Tools (Enabled in Example)

- Search / Query: `jira_search`, `jira_search_fields`
- Issues: `jira_get_issue`, `jira_create_issue`, `jira_update_issue`, `jira_batch_create_issues`
- Comments & Links: `jira_add_comment`, `jira_create_issue_link`, `jira_link_to_epic`
- Workflow: `jira_get_transitions`, `jira_transition_issue`
- Projects & Boards: `jira_get_all_projects`, `jira_get_project_issues`, `jira_get_agile_boards`, `jira_get_board_issues`
- Sprints: `jira_get_sprints_from_board`, `jira_get_sprint_issues`
- Changelogs: `jira_batch_get_changelogs`
- Worklogs: `jira_get_worklog`, `jira_add_worklog`
- Versions: `jira_get_project_versions`
- Attachments: `jira_download_attachments`
- User: `jira_get_user_profile`

Disable unused tools by removing them from the `--enabled-tools` list to reduce surface area and noise.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.