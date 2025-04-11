---
tags:
    - Etendo Copilot
    - API Integration
    - HTTP Requests
    - REST API
    - Tool
---

# API Call Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **API Call Tool** is designed to execute HTTP requests to external APIs. It enables developers to connect their applications to external services using RESTful methods. The tool accepts input parameters such as the API URL, endpoint, HTTP method, query parameters, body content, and an optional authorization token. As output, it returns the response body and the status code of the API call.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

This tool provides the assistant with:

- Integration: It allows applications to consume external REST APIs easily.
- Flexibility: Supports GET, POST, and PUT methods with customizable headers and payloads.
- Automation: Facilitates interaction with external systems from within Etendo Copilot.

This tool is ideal for developers integrating third-party services, internal APIs, or microservices.

## Setup

No specific environment variables are required to use this tool. However, if a bearer token is needed for authorization, it can be passed in the input as the `token` parameter.

Additionally, if you use the special token value `ETENDO_TOKEN`, the tool will fetch the token using Etendo's token management utility.

## Functionality

This tool enables execution of RESTful requests through the following steps:

- **Processing Arguments**

    It processes input parameters such as:
    - `url`: API base URL (required)
    - `endpoint`: Specific API endpoint (required)
    - `method`: HTTP method (`GET`, `POST`, or `PUT`) (required)
    - `body_params`: Payload (for POST and PUT)
    - `query_params`: Query string as a JSON object
    - `token`: Optional bearer token

- **Handling Query Parameters**

    If provided, query parameters are appended to the endpoint with appropriate URL encoding.

### Using ETENDO_TOKEN

If you set the `token` parameter to the special value `ETENDO_TOKEN`, Copilot will automatically replace it with a secure token retrieved from the Etendo environment. This approach ensures the token is **not exposed to the language model** and remains secure during execution.

Example:

```json
{
    "method": "GET",
    "url": "https://my.etendo.instance/etendo",
    "endpoint":"/sws/mySecureWebservice",
    "token": "ETENDO_TOKEN"
}
```

- **Replacing Base64 Placeholders**

    If the body contains `@BASE64_filepath@` placeholders, they are replaced with the base64-encoded content of the specified file.

    ```json
        {
            "method": "POST",
            "url": "https://my.etendo.instance/etendo",
            "endpoint":"/sws/UploadFile",
            "token": "ETENDO_TOKEN",
            "body_params": {
                "file": "@BASE64_filepath@"
            }
        }
    ```
    The API Call Tool will replace `@BASE64_filepath@` with the base64-encoded content of the file specified in the `file` parameter without exposing the file content or base64 to the model (not only for security reasons but also to avoid model confusion).

- **Executing the Request**

    Based on the method, the tool performs the corresponding request using the `requests` library.

- **Returning the Response**

    Returns a structured response with:
    
    ```
    {
        "requestResponse": "<response body>",
        "requestStatusCode": 200
    }
    ```

    In case of error:
    
    ```
    {
        "error": "Detailed error message"
    }
    ```

## Usage Example

Imagine you want to send a POST request to an external API for creating a new user. The input parameters for the assistant would be:

- `url`: https://api.example.com
- `endpoint`: /users/create
- `method`: POST
- `body_params`: 
    ```json
    {
        "name": "John Doe",
        "email": "john@example.com"
    }
    ```
- `token`: YOUR_BEARER_TOKEN

The API Call Tool will format and send the request with the appropriate headers and body, and return the result including the response status code and body content.