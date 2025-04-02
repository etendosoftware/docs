---
title: Developer Guide - Copilot Extensions
tags: 
    - Copilot Extensions
    - AI
    - Tools
    - Assistants
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

Etendo Copilot module include a set of windows where you can create, manage, and interact with AI-driven Agents. By default, the module includes "Bastian" that is an agent with the Etendo Wiki indexed as a knowledge base. This agent can be used to search for information in the Etendo Wiki.

#### Agents included
##### Bastian
Bastian is an agent with the Etendo Wiki indexed as a knowledge base. This agent can be used to search for information in the Etendo Wiki.
####### Components
- **Prompt**: The agent has a prompt that explain it purpose, the request that the user can make and the response that the agent will give. i.e. in it prompt there are indication to retrieve the article link when anwering a question. Additionally, has a brief explanation of particularities of the Etendo Wiki and the format of the articles.
- **Knowledge Base**: The agent has a knowledge base composed of the Etendo Wiki, indexed in the agent. The Knowledge Base file is of type `Remote File`, pointing to the GitHub repository of the Etendo Wiki. When the agent is synchronized, the agent will download the file and index it. More information in the [How to create an agent](../../etendo-copilot/how-to-guides/how-to-create-an-agent.md#Add-a-Knowledge-Base).

### Etendo Copilot Toolpack

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

#### Tools included
- [API Call Tool](../available-tools/api-call-tool.md)
- [Attach File Tool](../available-tools/attach-file-tool.md)
- [Audio Tool](../available-tools/audio-tool.md)
- [Code Bar Tool](../available-tools/codbar-tool.md)
- [Docker Tool](../available-tools/docker-tool.md)
- [Copy File Tool](../available-tools/file-copy-tool.md)
- [File Download Tool](../available-tools/file-downloader-tool.md)
- [Read File Tool](../available-tools/read-file-tool.md)
- [Write File Tool](../available-tools/write-file-tool.md)
- [XLS/CSV Reader Tool](../available-tools/xls-tool.md)
- [Uncompress Tool](../available-tools/uncompress-tool.md)
- [OCR Tool](../available-tools/ocr-tool.md)
- [PDF to Image Tool](../available-tools/pdf-to-images-tool.md)
- [Send Email Tool](../available-tools/send-email-tool.md)
- [Task Creator Tool](../available-tools/task-creator-tool.md)
- [Tavily Tool](../available-tools/tavily-tool.md)

#### Agents included
##### SQL Expert
Its an agent oriented to help users read information from the database. ![alt text](../../../assets/developer-guide/etendo-mobile/getting-started/image.png)
![alt text](../../../assets/image.png)
###### Components
- **Prompt**: The agent has a prompt that explain it purpose, the request that the user can make and the response that the agent will give. Has a brief explanation of particularities of the Etendo Classic database. Additionally, has a list of examples of common functions and columns that the tables have.
- **Knowledge Base**: The agent has a knowledge base composed by a OpenAPI Specification (of a flow with the endpoints that the agent can use) that is appended to the prompt.
- **API Call Tool**: The agent uses the API Call Tool to make the requests to Etendo Classic. 

More information about how to allow the agent to interact with Etendo Classic can be found in the [How to allow Copilot to interact with Etendo Classic](../how-to-guides/how-to-create-an-agent.md#how-to-allow-copilot-to-interact-with-etendo-classic
) guide.


### Etendo Copilot Agents

:octicons-package-16: Javapackage: `com.etendoerp.copilot.agents`

#### Agents included
The agents module includes a set of agents that can be used to assist users in their daily tasks. The agents included are:
The module includes the following agents:

- **Zip Reader**: This agent reads a zip file and returns the paths of the files inside the zip. Its usefull to add to a supervisor agent to chain the unzip and retrieve the files paths.
- **Client Initialization Supervisor**: This is a supervisor agent that delegates and orchestrates initialization tasks for the client (creation of initial business partners, products, etc.).
    ![alt text](../../../assets/user-guide/etendo-copilot/bundles/overview/client-initialization-graph.png)
    This supervisor has the following agents:

    - **Business Partner Generator**: This agent creates business partners.
    - **Product Generator**: This agent creates products.
    - **Physical Inventory Generator**: This agent creates physical inventories to add stock to the products.
    - **Bulk task creator**: This agent creates bulk tasks based on a zip file or a CSV/XLSX file. This agent allows to create tasks in bulk to load big amounts of data in the other agents. For example, it can be used to create a big amount of business partners, products from a CSV file, etc.

- **Order Expert**: This agent is a supervisor agent that delegates and orchestrates the creation of purchase and sales orders. 
    ![alt text](../../../assets/user-guide/etendo-copilot/bundles/overview/order-expert-graph.png)

    This supervisor has the following agents:

    - **Purchase Order Expert**: This agent creates purchase orders.
    - **Sales Order Expert**: This agent creates sales orders.

#### Components
- **Prompt**: The agents have a prompt that explains their purpose, the request that the user can make and the response that the agent will give. In addition, it has a brief explanation of the particularities of each agent, explaining how to search for information, which has to be indicated punctually and which has to be found out. They also include information about the order in which the requests to Etendo Classic have to be made, from which we have to use which values from one to the other. 
- **Knowledge Base**: Most of these agents use OpenAPI Specifications in their knowledge base, appending them to their prompt to understand how to use it. More information about how to allow the agent to interact with Etendo Classic can be found in the [How to allow Copilot to interact with Etendo Classic](../how-to-guides/how-to-create-an-agent.md#how-to-allow-copilot-to-interact-with-etendo-classic) guide.
- **API Call Tool**: The agents use the API Call Tool to make the requests to Etendo Classic.
- **OCR Tool**: The agents use the OCR Tool to read the information from the images that are attached to the requests. This tool is necessary if the model selected for the agent is not capable of reading the information from the images by itself.
- **Bulk Task Creator Tool**: The agent called `Bulk task creator` uses the Bulk Task Creator Tool to create bulk tasks based on a zip file or a CSV/XLSX file. This agent allows to create tasks in bulk to load big amounts of data in background. More information about this tool and strategies to use it can be found in the [Bulk Task Creator Tool](../available-tools/task-creator-tool.md) guide.
- **Langgraph Supervisor architecture**: The supervisor agents are built using the Langgraph Supervisor architecture. More information about this architecture can be found in the [How to create an agent](../../etendo-copilot/how-to-guides/how-to-create-an-agent.md#Langgraph-Supervisor-architecture) guide.


### Dev Assistant

:octicons-package-16: Javapackage: `com.etendoerp.copilot.devassistant`

<iframe width="560" height="315" src="https://www.youtube.com/embed/58U9LThdTGo?si=kSxA3MAf22U8fdHh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The **Dev Assistant** module includes various development assistants that will facilitate developers the processes of creating buttons, windows, tabs, fields, background processes, Event Handlers, Jasper reports and much more.

!!!info
    For more information, visit [Dev Assistant developer guide](../../etendo-copilot/bundles/dev-assistant.md).
