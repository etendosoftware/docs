---
tags:
    - Copilot
    - References
    - IA
    - Webhook
    - Automation
    - Add Lists
---

# Create References

## Overview

The Create References Tool is a tool that **creates a reference** in the Etendo Application Dictionary. With this tool, it is for example, possible to add new list references to a specific module within the Etendo database via an HTTP request to a webhook.

This tool is useful in the context of module administration and configuration on the Etendo platform. It allows system administrators or developers to define new references that can be used later in applications. It is especially useful to **automate the creation of these references and ensure consistency** in the configuration.


## Installation
You can install only the module containing the **Create References** by following the guide on [How to install modules in Etendo](../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md), looking for the GitHub Package `com.etendoerp.copilot.devassistant`.


## Functionality

With this tool, it is possible to: 

1. **Argument Processing**: Takes various input parameters defined in a pydantic model:

    - `i_prefix`: The prefix of the module in the database.
    - `i_name`: The name of the reference.
    - `i_reference_list`: A comma-separated list of reference items.
    - `i_help` (optional): Help text for the reference.
    - `i_description` (optional): Description of the reference.

2. **Access Token Verification**: Gets and verifies the access token from the thread context (ThreadContext).
3. **Request Body Construction**: Constructs the body of the request parameters for the webhook.
4. **Webhook Call**: Uses the `call_webhook` function to make an `HTTP POST` request to the Etendo webhook endpoint, providing the necessary parameters and the access token.
5. **Result Handling**: Returns the result of the request to the webhook, which may contain a success message or an error in JSON format.


The system returns a dictionary with the result of the operation. For example:

- If the request was successful:
 { `success: true, message: Reference created successfully`}

- If there was an error:
 { `error: Description of the error`}

## Usage Example 

!!!info
    To use this assistant, it is necessary to log in as **System Administrator** role and set the module in which the changes will be exported in development.

In case the user wants to create a new reference in Etendo, the input parameters could be:

- `i_prefix`: MOD
- `i_name`: Document type
- `i_reference_list`: Invoice, Receipt
- `i_help`: Supported document types
- `i_description`: List of document types that can be issued.

The Create References Tool will process these parameters, verify the access token, build the request body and call the Etendo webhook to create the reference.


## Utility

1. **Automation**: Makes it easy to automate the process of creating list references in Etendo, saving time and manual effort.

2. **Consistency**: Ensures that list references are created consistently and following a predefined format.

3. **Easy Integration**: Provides an integrated way to interact with the Etendo Application Dictionary through calls to webhooks.

3. **Error Handling**: Provides a structured way to handle errors and receive feedback on the executed operation.


The Create References Tool is a specialized tool designed to facilitate the creation of **references in the Etendo Application Dictionary**. By providing an automated interface for creating these references and properly managing access tokens and webhook call results, this tool is essential for administrators and developers looking to **maintain and extend** the functionality of their applications on the Etendo platform.

