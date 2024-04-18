---
title: "Purchase Assistant for Copilot"
tags:
    - Copilot
    - IA
    - Machine Learning
    - OpenAPI
    - Swagger
    - API
    - Purchase
    - Assistant
---
:octicons-package-16: Javapackage: com.etendoerp.copilot.openapi

:octicons-package-16: Javapackage: com.etendoerp.copilot.openapi.purchase


## Overview
By using certain Tools and a prompt that gives the Assistant sufficient context, it is possible to make an assistant that can perform a certain task in a satisfactory and intelligent way.

For this particular case we have configured a wizard with the functional methodology of creating purchase orders, and we have equipped it with 2 tools:

**Etendo API Tool**: This tool explains to the assistant how to interact with the Etendo API, and what are the available endpoints and their descriptions.

**API Call Tool**: This tool allows to Copilot to make a call to a API, and read and write data in Etendo.

This tool will be the responsible to make the call to the API endpoint, and will return the response.


### Configuration:
 - In the module ```com.etendoerp.copilot.openapi.purchase``` there is a dataset with the basic configuration of the purchase assistant. It can be imported in the "Enterprise module management" window. 
 
 - After import the configuration, it is necessary to config the OpenAI model for the assistant and Sync the assistant.
 
 - Finally, give access to the role, configure the permissions in "Role" Window.

!!! note
    In the last paragraph of the prompt, the link "http://localhost:8080/etendo/?tabId=294&recordId={ORDER_HEADER_ID}" is a link for localhost, it is necessary to replace it with the real link of the Etendo system.


## Functionality

When interacting with the assistant, you may be asked to insert a purchase order to a Business Partner, indicating the date and other general data, the items and their quantities for each one. The assistant will then make calls to Etendo API to search and read the info needed to create the purchase order. After that, the assistant will make the call to the API to insert the purchase order in Etendo.
For the items, the assistant will search the items in the Etendo API for the products information, and will insert the items in the purchase order.
Finally, the assistant will return the link to the purchase order created in Etendo.

## Technical details for Developers
- More information about how to integrate Copilot with other API's can be found in the [OpenAPI interaction with Copilot](../../../developer-guide/etendo-copilot/available-tools/openapi-tool.md) page.

   

