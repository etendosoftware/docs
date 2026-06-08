---
title: How to Connect Etendo Copilot with Gmail via Pipedream
tags:
    - Etendo Copilot
    - Gmail
    - Pipedream
status: beta
---

# How to Connect Etendo Copilot with Gmail via Pipedream

## Overview

<iframe width="560" height="315" src="https://www.youtube.com/embed/taAPYMPWpLM?si=_xZf1LQUnPAmQcHF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Imagine a department manager working with Etendo Copilot who suddenly needs to check their email to review the latest client messages before making a decision.  

In the past, this required switching tabs, searching for the Gmail thread, and then returning to Copilot — a typical flow interruption.  

With the **Gmail integration** via [Pipedream](https://pipedream.com){target="_blank"}, you can simply ask the agent:

- *“List my recent Gmail emails”*
- *“Summarize all unread emails and order them by relevance”*
- *“Search sent emails to `client@example.com` and list their latest purchases”*
- *“Send an email to `client@example.com` with the most recent price list”*

The agent connects securely to your **Gmail** account (with your prior authorization), retrieves the messages, and responds inline in the chat. All without leaving Copilot.

This guide walks you through three steps: connecting your Gmail account in Pipedream, registering that connection in Etendo, and linking it to your agent.

**Why is this useful?**

- **Centralized information**: Access ERP data and emails in the same place.  
- **Time savings**: No need to switch apps or copy/paste information.  
- **More efficient**: Your agent has all the context of your emails and can assist you in composing emails, using information from any agent, and even using attachments.


## How it Works

The flow is simple but powerful:

1. [Pipedream](https://mcp.pipedream.com/){target="_blank"} manages the secure connection with Gmail and exposes the MCP (Model Context Protocol) configuration — a standard way for AI assistants to securely connect to external services like Gmail.  
2. In **Etendo**, you register that configuration as an MCP Server.  
3. Finally, you link the MCP to your Copilot agent.  

From that point on, any Gmail-related query is automatically redirected to the Pipedream MCP, which fetches the data and returns the response to the chat.



## Prerequisites

- Etendo and [Etendo Copilot](../installation.md) installed.  
- A Google account to connect.  
- A free [Pipedream](https://pipedream.com){target="_blank"} account.


!!! info 
	For more information, visit [How to configure MCP servers on Etendo agents](./how-to-configure-mcp-servers-on-agents.md).  



## Connect Gmail in Pipedream

1. Open [Gmail MCP Server | Pipedream](https://mcp.pipedream.com/app/gmail).  
2. Connect your Gmail account and accept Google’s consent screen.  
	![Gmail account connection screen in Pipedream](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/sign-in.png)
3. In the configuration panel, select the option labeled **VS Code** from the dropdown (this format is required for Etendo to read the configuration), then click **Copy** to copy the **MCP Server Config** text that appears.
	![MCP Server Config panel in Pipedream](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/mcp-server-config.png)

## Create the MCP Server in Etendo 
:material-menu: `Application` > `Service` > `Copilot` > `MCP Servers Configuration`

1. Log in to **Etendo** with the **System Administrator** role.  
2. Navigate to `MCP Servers Configuration` window.  
3. Create a new record with the following values:  

![New MCP Server record form in Etendo](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/create-mcp-server.png)

   - **Name**: e.g., *Pipedream Gmail*  
   - **Description**: (Optional) e.g., *Connecting to Gmail through Pipedream MCP*
   - **JSON Structure**: Paste the code text you copied from Pipedream in the previous step. This is the configuration Etendo uses to connect to your Gmail account.
   - **Module**: Leave this blank unless your technical team has asked you to fill it in.


## Link the MCP to the Agent
:material-menu: `Application` > `Service` > `Copilot` > `Agent`

1. Navigate to `Agent` window.  
2. Open the agent to which you want to grant Gmail access (or create a new one) and go to the **MCP Servers** tab.  
3. Add a new line selecting the MCP Server just created.  
4. Click **Save** to record your changes, then click **Sync Agent** — this applies the new Gmail connection to the agent so it can start using it immediately.

![MCP Servers tab on the Agent record in Etendo](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/add-mcp-to-agent.png)


## Test the Gmail Integration

1. Start a conversation with the agent and ask something Gmail-related, for example:

   ![Agent chat showing a Gmail query example](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/mcp-gmail-use-example.png)

2. Send emails directly from the agent:

   ![Send email from agent example](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/send-email.png)

   ![Resulting sent email example](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/example-email.png)


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.