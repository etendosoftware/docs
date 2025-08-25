---
title: Developer Guide - Copilot Extensions
tags: 
    - Copilot Extensions
    - AI
    - Tools
    - Agents
    - Developer
---


# Copilot Extensions

:octicons-package-16: Javapackage: `com.etendoerp.copilot.extensions`

:material-store: Etendo Marketplace:  [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}

!!! warning
    Currently, we are migrating the terminology from *Assistant* to *Agent*. This change will be reflected in the documentation soon. Where you see *Assistant*, consider it as *Agent* and vice versa.

## Overview

The Copilot Extensions Bundle includes functionalities for developers to help them develop AI agents that can assist users in their daily tasks.

## Modules

### Etendo Copilot

:octicons-package-16: Javapackage: `com.etendoerp.copilot`

Etendo Copilot module include a set of windows where you can create, manage, and interact with AI-driven Agents. By default, the module includes **Bastian** that is an agent with the Etendo Documentation indexed as a knowledge base.

**Agents included**
 
- **Bastian**: is an agent with the Etendo Documentation indexed as a knowledge base.
    - **Prompt**: The agent has a prompt that explain it purpose, the request that the user can make and the response that the agent will give. i.e. in it prompt there are indication to retrieve the article link when anwering a question. Additionally, has a brief explanation of particularities of the Etendo Wiki and the format of the articles.
    - **Knowledge Base**: The agent has a knowledge base composed of the Etendo Wiki, indexed in the agent. The Knowledge Base file is of type `Remote File`, pointing to the GitHub repository of the Etendo Wiki. When the agent is synchronized, the agent will download the file and index it. 
    
    !!! info 
        For more information visit, [How to create an agent](../../etendo-copilot/how-to-guides/how-to-create-an-agent.md#add-a-knowledge-base) guide.

### Etendo Copilot Toolpack

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

**Tools Included**

!!!info
    You can see the complete list of tools in the [Tools](../available-tools/tool-full-list.md) section.
    
!!! note
    For more information visit, [How to Create Copilot Tools](../how-to-guides/how-to-create-copilot-tools.md) guide.

**Agents Included**

- [SQL Expert](../../../user-guide/etendo-copilot/bundles/sql-expert.md): This agent is designed to help users read information from the database. It allows users to ask questions in natural language and get the SQL query that retrieves the information they need. In order to preserve the security of the database, the query is pre-processed with filters to only retrieve data accessible by the user.

    - **Prompt**: The agent has a prompt that explain it purpose, the request that the user can make and the response that the agent will give. Has a brief explanation of particularities of the Etendo Classic database. Additionally, has a list of examples of common functions and columns that the tables have.
    - **Knowledge Base**: The agent has a knowledge base composed by a OpenAPI Specification (of a flow with the endpoints that the agent can use) that is appended to the prompt.
    - **API Call Tool**: The agent uses the API Call Tool to make the requests to Etendo Classic. 

    !!! note
        For more information visit, [How to allow Copilot to interact with Etendo Classic](../how-to-guides/how-to-create-an-agent.md#how-to-allow-copilot-to-interact-with-etendo-classic) guide.


### Etendo Copilot Agents

:octicons-package-16: Javapackage: `com.etendoerp.copilot.agents`

**Agents included**

The agents module includes a set of agents that can be used to assist users in their daily tasks. The module includes the agents descripted un the [Etendo Copilot Agents - User Guide](../../../user-guide/etendo-copilot/bundles/overview.md#etendo-copilot-agents)

- **Prompt**: The agents have a prompt that explains their purpose, the request that the user can make and the response that the agent will give. In addition, it has a brief explanation of the particularities of each agent, explaining how to search for information, which has to be indicated punctually and which has to be found out. They also include information about the order in which the requests to Etendo Classic have to be made, from which we have to use which values from one to the other. 
- **Knowledge Base**: Most of these agents use OpenAPI Specifications in their knowledge base, appending them to their prompt to understand how to use it. More information about how to allow the agent to interact with Etendo Classic can be found in the [How to allow Copilot to interact with Etendo Classic](../how-to-guides/how-to-create-an-agent.md#how-to-allow-copilot-to-interact-with-etendo-classic) guide.
- **[API Call Tool](../available-tools/api-call-tool.md)**: The agents use the API Call Tool to make the requests to Etendo Classic.
- **[OCR Tool](../available-tools/ocr-tool.md)**: The agents use the OCR Tool to read the information from the images that are attached to the requests. This tool is necessary if the model selected for the agent is not capable of reading the information from the images by itself.
- **[Bulk Task Creator Tool](../available-tools/task-creator-tool.md)**: The agent called `Bulk task creator` uses the Bulk Task Creator Tool to create bulk tasks based on a `ZIP` file or a `CSV/XLSX` file. This agent allows to create tasks in bulk to load big amounts of data in background.
- **Langgraph Supervisor architecture**: The supervisor agents are built using the Langgraph Supervisor architecture. More information about this architecture can be found in the [How to Create an Agent - Langgraph Supervisor Architecture](../../etendo-copilot/how-to-guides/how-to-create-an-agent.md#Langgraph-Supervisor-architecture) guide.


### Dev Assistant

:octicons-package-16: Javapackage: `com.etendoerp.copilot.devassistant`

<iframe width="560" height="315" src="https://www.youtube.com/embed/58U9LThdTGo?si=kSxA3MAf22U8fdHh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The **Dev Assistant** module includes multiple **development agents** that will facilitate developers the processes of creating buttons, windows, tabs, fields, background processes, Event Handlers, Jasper reports and much more.

!!!info
    For more information, visit [Dev Assistant - Developer Guide](../bundles/dev-assistant.md).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

