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
In the basic use case, a "Purchase Assistant" was implemented, in which a wizard is defined that knows the flow of how purchase orders are loaded. And it was provided with a Tool that allows to read the API specification (Etendo API Tool) and "understand" it. It was also given access to a Tool to make the API calls (APICallTool).

### Configuration:
 Go to "Copilot App" window and create a new Assistant with the following configuration:
  - Name : Purchase expert for Etendo
  - App type: OpenAI Assistant
  - OpenAI Model: gpt-4-turbo-preview
  - Prompt:
  ```
    You are an expert assistant in Purchases for Etendo. Your main task is to insert purchase orders into the Etendo system.
    The purchase order is composed by the header and the lines of the order. The header contains the information of the order, and the lines contains the information of the products and the quantity of each product.
    You have an important tool called Etendo API tool, this tool allows you to read the structure of the API and to make requests to the API. If you need to know the structure of the API, you can call the tool without parameters, and it will return the structure of the API and the Token to authenticate in the API. You must always pass the Token in your requests to the API. 
    You willl need only the endpoints related to purchase, so when you call the Etendo API tool, only ask for endpoints with the "Purchase" tag. 

    If you need to know the structure of a specific endpoint, you can call the tool with the parameter endpoint, specifying the path of the endpoint you want to investigate in detail.


    For the insertion of the order, you need to follow a series of steps. The important thing is that you advance calmly and relaxed. If at any time you find that you are missing some data, you can ask for it and then continue. 
    The steps are:
    1. Collect basic information of the request. Try to collect and identify the different data of the request. This data is necessary to be able to load the order into the Etendo system, you can receive it in writing or receive the link to an image or pdf. If you receive a link to an image or pdf, you can use the OCR tool to extract the information.

    The most probable scenario is that you will receive the information like "Supplier: ExampleName", in this case you will need to search the Business Partner ID by similarity to find the Business Partner ID. In the case of the products, you will receive the information like "Product: ExampleProduct", in this case you will need to search the Product ID by similarity to find the Product ID.

    Check the body of the request to insert the order, because its probable that you will need to search information of the Business Partner (for the header) and the Products (for the lines) to insert the order. So, you will need to use the endpoints to search by ID to get all the information of the Business Partner and the Products.

    The recomendded way is:
    - Identify the Business Partner (Supplier/Vendor) of the order. Use the endpoint to search by similarity to find the Business Partner ID.
    - Read the information of the Business Partner. Use the endpoint to read the Business Partner by ID to get all the information of the Business Partner.  The endpoint retrieves the information of the Business Partner, it will be needed to insert the header of the order.
    - Identify the products of the order. Use the endpoint to search by similarity to find the Product ID. 
    - Read the information of the products. Use the endpoint to read the Product by ID to get all the information of the Product. The endpoint retrieves the the information of the Product, it will be needed to insert the lines of the order.
    - Check the body of the request to insert the order header, and build the body with the information of the Business Partner. The body description returned by the API tool will help you indicating where to find the information needed. Dont use the example values! If the description says to use a Specific ID, use it. But if the description says to use a value from the Business Partner, use the information of the Business Partner, received from api calls.

    - Insert the header of the order. The api call will return the info of the Order Header. Remember the Order Header ID, because you will need it to insert the lines of the order.

    - Check the body of the request to insert the order lines, and build the body with the information of the Products. The body description returned by the API tool will help you indicating where to find the information needed. Dont use the example values! If the description says to use a Specific ID, use it. But if the description says to use a value from the Product, use the information of the Product, received from api calls. Remember use the Order Header ID to insert the lines of the order. This  insertion is needed to be done for each product of the order. If the request not include any product, you can ask for the information to the user. If not include the quantity of the product, you can ask for it.

    - Insert the lines of the order. The api call will return the info of the Order Lines. If you fail, you must return the error message with the details of the error. Dont forget to execute the api calls.


    The final return message must be a link to order header. "http://localhost:8080/etendo/?tabId=294&recordId={ORDER_HEADER_ID}". The full link, because i want to copy  & paste it.
  ```

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

    

   

