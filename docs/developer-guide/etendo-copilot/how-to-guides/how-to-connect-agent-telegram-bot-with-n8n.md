---
title: How to Connect an Etendo Copilot Agent to a Telegram Bot with n8n
status: beta
tags:
  - Etendo Copilot
  - Telegram
  - n8n
  - Automation
  - Bot Integration
---

# How to Connect an Etendo Copilot Agent to a Telegram Bot with n8n

## Overview

This guide explains how to expose an existing **Etendo Copilot Agent** as an interactive **Telegram bot** using the automation platform **n8n**. 

Users send messages to a Telegram bot. n8n receives them, forwards the text to the Copilot endpoint, and returns the generated response to the same chat. The same pattern can be adapted to other channels (e.g. WhatsApp via Twilio) by replacing the trigger / send nodes.

## Architecture

```
Telegram User  →  Telegram Bot  →  n8n Workflow  →  Etendo Copilot (Agent)
      ↑                                                     ↓
      └──────────────────────── Response (text) ────────────┘
```

Key concepts:

- **Telegram Trigger** node listens for new messages.
- **HTTP Request** node calls the Etendo Copilot REST endpoint.
- **Send Message** node replies back to the originating chat.
- **conversation_id** keeps conversational context per Telegram chat.

## Prerequisites

- An operational **Etendo Classic** instance with **Etendo Copilot** installed and configured.
- A configured **Copilot Agent** (obtain its internal ID from the Agent window header).
- A **Telegram Bot Token** (create a bot with `@BotFather`).
- A running **n8n** instance (cloud or self‑hosted) with access to the Etendo instance URL.
- A dedicated **Etendo user + Bearer token** (or API token) with only the permissions required for the agent use case (principle of least privilege).
- Network access: n8n must reach `ETENDO_INSTANCE_URL` over HTTPS.

!!! warning "Security"
    For public bots create a minimal‑privilege Etendo user (e.g. read‑only access to stock inquiries) to avoid exposing sensitive data.

## Endpoint Specification

Etendo Copilot question endpoint:

`POST ETENDO_INSTANCE_URL/etendo/sws/copilot/question`

Headers:

- `Authorization: Bearer <TOKEN>`
- `Content-Type: application/json`

Body (JSON):
```json
{
  "question": "<user message>",
  "app_id": "<AGENT_ID>",
  "conversation_id": "<CHAT_ID>"
}
```

Field description:

- **question**: Raw text from the Telegram user.
- **app_id**: Internal ID of the Copilot Agent to invoke.
- **conversation_id**: Stable identifier to maintain threaded context. Use the Telegram `chat.id`.

## n8n Workflow: Step by Step

### 1. Telegram Trigger Node

Purpose: Capture inbound messages.

Configuration:

- Resource: `Message`
- Operation: `On Update` (default new messages)
- Credentials: Your Telegram Bot credential (e.g. `Telegram account 2`).
- Update Types: `message`

No custom parameters are required for a basic text flow.

### 2. HTTP Request Node (Bridge to Etendo Copilot)

Purpose: Send the user's message to the Copilot Agent.

Configuration:

- **Method**: `POST`
- **URL**: `ETENDO_INSTANCE_URL/etendo/sws/copilot/question`
- **Authentication**: HTTP Bearer (supply the Etendo token)
- **Response Format**: `JSON`
- **Body Content Type**: `JSON / Application JSON`
- **JSON Body** (expressions enabled):

  - `question`: `={{ $json["message"]["text"] }}`
  - `app_id`: Hardcode your Agent ID (e.g. `1234567890`) or use an environment variable.
  - `conversation_id`: `={{ $json["message"]["chat"]["id"] }}`

Example raw body (with expressions):
```json
{
  "question": "={{ $json.message.text }}",
  "app_id": "1234567890",
  "conversation_id": "={{ $json.message.chat.id }}"
}
```

!!! note "Error Handling"
    Add an additional **IF** (or **Switch**) node after the HTTP Request to detect non‑2xx statuses. Route failures to a fallback message (e.g. "Service temporarily unavailable").

### 3. Send Telegram Message Node

Purpose: Deliver the Copilot response back to the user.

Configuration:

- **Chat ID**: `={{ $json["message"]["chat"]["id"] }}` (or from the first node depending on connections)
- **Text**: `={{ $json["response"] }}` (assuming the Copilot service returns `{ "response": "..." }`).

If the HTTP Request node output structure nests the JSON (e.g. in `data`), adjust the expression accordingly (`={{ $json.data.response }}`).

### 4. (Optional) Rate Limiting / Moderation

Insert a Function or Code node to:

- Throttle requests (avoid abuse)
- Filter empty / command‑only messages
- Enforce a maximum message length

## Minimal Example Workflow (n8n Export)

Replace placeholders before importing.

```json
{
  "name": "Copilot Telegram Bridge",
  "nodes": [
    {
      "id": "TelegramTrigger",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [200, 300],
      "parameters": {
        "updates": ["message"]
      },
      "credentials": {
        "telegramApi": "YOUR_TELEGRAM_CREDENTIAL"
      }
    },
    {
      "id": "CopilotRequest",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [520, 300],
      "parameters": {
        "method": "POST",
        "url": "https://ETENDO_INSTANCE_URL/etendo/sws/copilot/question",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpBearerAuth",
        "jsonParameters": true,
        "options": {},
        "bodyParametersJson": "{\n  \"question\": \"={{ $json.message.text }}\",\n  \"app_id\": \"1234567890\",\n  \"conversation_id\": \"={{ $json.message.chat.id }}\"\n}"
      },
      "credentials": {
        "httpBearerAuth": "ETENDO_BEARER_TOKEN"
      }
    },
    {
      "id": "SendMessage",
      "name": "Send Telegram Message",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [840, 300],
      "parameters": {
        "resource": "message",
        "operation": "sendMessage",
        "chatId": "={{ $json.message.chat.id }}",
        "text": "={{ $json.response }}"
      },
      "credentials": {
        "telegramApi": "YOUR_TELEGRAM_CREDENTIAL"
      }
    }
  ],
  "connections": {
    "Telegram Trigger": { "main": [ [ { "node": "HTTP Request", "type": "main", "index": 0 } ] ] },
    "HTTP Request": { "main": [ [ { "node": "Send Telegram Message", "type": "main", "index": 0 } ] ] }
  }
}
```

!!! info "Adjusting Field Names"
    If the Copilot service changes its response schema, inspect the HTTP Request node output and update the expression used in the send node.

## Testing

1. Activate the workflow in n8n (`Active = true`).
2. Send a message to the Telegram bot (e.g. `Hello` or a domain question like: *List open sales orders*).
3. Observe the execution log in n8n. Confirm:
   - Status 200 from the HTTP Request
   - Response JSON contains a `response` field
4. Validate that the bot replies in the same chat.
5. Send multiple messages to confirm conversation continuity (context reuse via `conversation_id`).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.