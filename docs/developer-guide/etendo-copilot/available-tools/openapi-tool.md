---
title: "OpenAPI interaction with Copilot"
tags:
    - Copilot
    - IA
    - Machine Learning
    - OpenAPI
    - Swagger
    - API
---
:octicons-package-16: Javapackage: com.etendoerp.copilot.openapi

:octicons-package-16: Javapackage: com.etendoerp.copilot.openapi.purchase


## Overview
The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. When properly defined, a consumer can understand and interact with the remote service with a minimal amount of implementation logic. Similar to what interfaces have done for lower-level programming, OAS removes the guesswork in calling the service. For more information, see the [OpenAPI Initiative](https://www.openapis.org/).

This Specification can be very usefull for Copilot, because can be used as guide to Copilot to interact with the services, without the need to know the implementation details and will not be necessary to implement specific code for each service.


## Tools

**Etendo API Tool**: This tool returns the OpenAPI Specification of the Etendo API, can be used by Copilot to ask for the general information of the API (endpoints, and the descriptions of the endpoints) or the specific information of the endpoints(Parameters, responses, etc). At this moment, the Etendo API Tool only returns the OpenAPI Specification of the Etendo API for insert purchase orders in Etendo.

**API Call Tool**: This tool allows to Copilot to make a call to a API endpoint. 
This tool will be the responsible to make the call to the API endpoint, and will return the response.

## Assistant defined
In the basic use case, a "Purchase Assistant" was implemented, in which an assistant is defined that knows the flow of how purchase orders are loaded. And it was provided with a Tool that allows to read the API specification (Etendo API Tool) and "understand" it. It was also given access to a Tool to make the API calls (APICallTool).

### Configuration:
 - In the module ```com.etendoerp.copilot.openapi.purchase``` there is a dataset with the basic configuration of the purchase assistant. It can be imported in the "Enterprise module management" window. 
 - After import the configuration, it is necessary to config the OpenAI model for the assistant and Sync the assistant.
 - Finally, give access to the role, configure the permissions in "Role" Window.
!!! note
    In the last paragraph of the prompt, the link "http://localhost:8080/etendo/?tabId=294&recordId={ORDER_HEADER_ID}" is a link for localhost, it is necessary to replace it with the real link of the Etendo system.

### Other Configurations:
- Its necessary to add the ```gradle.properties``` file with the following configuration:
``` properties
    ETENDO_HOST=http://localhost:8080/etendo
```
!!! warning
    Replace http://localhost:8080/etendo with the real link of the Etendo system.


## Functionality

The combination of the prompt with the functional concepts, the tool that allows to read and analyze the OpenAPI Spec to see the available endpoints and the tool to make the API calls, allows the defined assistant to load the purchase and its lines.

## How to integrate Copilot with other API's
The case of the purchase assistant is just an implementation to respond to a need. But, the usefulness of this is that, using the OpenAPI Spec reading tool as a base, the same dynamics can be replicated for a different API. For example, if we want to integrate Copilot with a currency exchange rate API, what we should do is the following:
- Create an App, describing in the App prompt the functionality we want the helper to perform. In this case, describing that we need the assistant to know how to look up the exchange rates for us.
- Create a tool, using the example of the EtendoAPITool, that reads the OpenAPI Spec file, that can be remote or local. This tool should provide the API information. If it is an external API, it is recommended that it reads the remote file provided by the API, so that it is updated on the fly, if the API changes.
- Configure the Tool created in the App, together with the APICallTool, which is a tool included in the module () and is generic for any simple API.
- Sync the assistant and try it out.

This way, we can create assistants for any API, as long as we have the OpenAPI Spec file. The assistant will be able to read the API and make the calls, without the need to know the implementation details of the API. 

    

   

