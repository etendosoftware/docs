---
tags:
    - Copilot
    - IA
    - Tool
    - Machine Learning
    - Assistant
    - Create Reference
    - Add lists
---

## Overview

The **Create Reference Tool** is an Etendo Copilot tool developed by Python to create references in the database. This tool is useful to automate the creation of references saving time and manual effort.  

## Functionality

This process consists of the following actions:

- **Argument Processing** 

Takes various input parameters defined in a pydantic model:

    - `i_prefix`: The prefix of the module in the database.
    - `i_name`: The name of the reference.
    - `i_reference_list`: A comma-separated list of reference items.
    - `i_help` (optional): Help text for the reference.
    - `i_description` (optional): Description of the reference.

- **Access Token Verification**

Gets and verifies the access token from the thread context (`ThreadContext`).

- **Request Body Construction**

Constructs the body of the request parameters for the webhook.

- **Webhook Call**

Uses the `call_webhook` function to make an `HTTP POST` request to the Etendo webhook endpoint, providing the necessary parameters and the access token.

- **Result Handling**

Returns the result of the request to the webhook, which may contain a success message or an error in JSON format.


The system returns a dictionary with the result of the operation. For example:

- If the request was successful:

```
 { `success: true, message: Reference created successfully`}

```

- If there was an error:

```
 { `error: Description of the error`}

```