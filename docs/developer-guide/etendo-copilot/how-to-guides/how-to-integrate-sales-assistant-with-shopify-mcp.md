---
title: Integrate a Sales Assistant with Shopify MCP
status: beta
tags: 
  - How to
  - MCP Server
  - Shopify
  - Sales Assistant
  - E-commerce
  - Copilot Integration
  - Agent Prompting
---

# How to Integrate a Sales Assistant with Shopify MCP

## Overview

!!!example "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

This guide explains how to configure an **intelligent Sales Assistant** in **Etendo Copilot** that connects to a **Shopify Model Context Protocol (MCP) server** to deliver a guided, conversational buying experience.

The assistant can:

- Search the product catalog in real time
- Retrieve detailed product information
- Manage the shopping cart
- Access policies and FAQs
- Provide contextual, consultative recommendations

## Prerequisites

- Etendo Copilot installed and configured
- At least one working OpenAI / compatible LLM provider configured (or an internal model via Ollama)
- A functioning Shopify MCP server endpoint exposing tools (HTTP or SSE transport)
- Network access from the Copilot backend to the Shopify MCP endpoint

## Supported Shopify MCP Tools (Examples)

Typical Shopify MCP server implementations expose tools similar to:

| Purpose | Example Tool Name |
|---------|-------------------|
| Catalog search | `search_shop_catalog` |
| Product details | `get_product_details` |
| Cart state | `get_cart` |
| Update cart | `update_cart` |
| Policies & FAQs | `search_shop_policies_and_faqs` |

Tool names may vary depending on the MCP server implementation. Confirm by inspecting the server's capabilities response.

## Step 1. Configure the Shopify MCP Server

:material-menu: `Application` > `Service` > `Copilot` > `MCP Servers Configuration`

1. Open the **MCP Servers Configuration** window (System Administrator role).
2. Create a new record and paste the JSON configuration.
3. Save. The system validates and normalizes the structure.

### JSON Configuration Examples

Minimal HTTP-based configuration:

```json
{
  "mcp": {
    "servers": {
      "shopify": {
        "url": "https://your-shop.example/api/mcp",
        "transport": "streamable_http"
      }
    }
  }
}
```

## Step 2. Link the MCP Server to an Agent

:material-menu: `Application` > `Service` > `Copilot` > `Agent`

1. Open (or create) an Agent.
2. Go to the **MCP** tab.
3. Add a new record selecting the Shopify MCP configuration.
4. Save.

## Step 3. Author a Specialized Prompt

Provide clear behavioral instructions so the assistant acts as a consultative digital salesperson.

Suggested base prompt:

```text
You are a professional e-commerce sales assistant for a Shopify-powered store integrated into Etendo.
Objectives:
- Understand the user's intent (need, preference, constraints: price, category, use case).
- Use catalog search BEFORE answering if more context is required.
- When recommending products: list 3–5 options (if available) with: Name | Key benefit | Differentiator.
- When the user asks for differences: respond with a concise comparison table (textual) and a short recommendation.
- Always confirm before adding or updating cart items.
- Use cart tools to reflect real state before confirming.
- If policy / FAQ info is requested, call the policies/faq tool.
- Ask one clarifying question if intent is ambiguous.
- Avoid hallucinating unavailable products.
Tools to consider (call only when needed): search_shop_catalog, get_product_details, get_cart, update_cart, search_shop_policies_and_faqs.
Return final answers in clear, concise business English.
```

!!!tip "Prompt Refinement"
    Iterate based on transcripts. Add guardrails for pricing, availability disclaimers, or upsell logic.

## Step 4. Test the Assistant

1. Start a conversation with the configured agent.
2. Try discovery queries first (e.g. *"I need a lightweight running shoe"*).
3. Ask for comparisons (e.g. *"Compare the first two you suggested"*).
4. Add to cart (e.g. *"Add the second shoe in size 42"*). The agent should call `update_cart` after confirmation.
5. Ask for policies (e.g. *"What is the return policy?"*).

## Example Conversation

**User**: *"What product do you recommend for home coffee brewing?"*

**Agent**: *(Calls `search_shop_catalog`)*

*"Here are three options: ... Would you like a comparison or more details on one of them?"*

**User**: *"Compare the first two."*

**Agent**: *(Calls `get_product_details` twice)*

*"Comparison: 1) Model A – Compact | Fast heat | Best for beginners. 2) Model B – Larger capacity | Dual temperature control | Better for experimentation. Recommendation: If you value simplicity choose Model A; for control choose Model B."*

**User**: *"Add Model B to my cart."*

**Agent**: *"Confirm: add Model B (default configuration) to cart?"*

**User**: *"Yes."*

**Agent**: *(Calls `update_cart`, then `get_cart`)*

*"Added. Your cart now contains: ..."*


## Related Pages

- [Model Context Protocol (MCP)](../concepts/model-context-protocol.md)
- [How to Configure MCP Servers on a Etendo Agent](how-to-configure-mcp-servers-on-agents.md)
- [How to Create an Agent](how-to-create-an-agent.md)
