---
tags:
    - Copilot
    - IA
    - Machine Learning
    - Tool
    - Attach file
---

# Attach File Tool

## Overview

The **Attach File tool** uploads a file to an API after verifying its existence and accessibility. It involves reading the file from a specified path, encoding it in base64, and then sending it to the API endpoint along with necessary identifiers and an access token.

## Functionality

The primary purpose of the Attach File Tool is to facilitate the process of attaching files to records in remote systems, such as the Etendo API, by ensuring the file is accessible and correctly encoded before upload. It is highly valuable in automated processes that require attaching files to records in a remote system. 

This process consists of the following actions:

- **Receiving Parameters**

    The tool receives an input object containing the following keys:

    - `filepath` : The path of the file to upload.

    - `ad_tab_id` : A 32-character string which is the ID of the Tab.

    - `record_id` : A 32-character string which is the ID of the record.

- **File Verification**

    The tool checks if the file at the specified path exists and is readable. If the file does not exist or is not accessible, it returns an error.

- **File Reading and Encoding**

    If the file is available, it reads the file content and encodes it in base64 format.

- **Authentication**

    The tool retrieves an access token from the extra information stored in the thread context. If no access token is provided, it returns an error.

- **API Communication**

    The tool constructs the necessary headers and body parameters and sends the encoded file to the specified API endpoint using an HTTP POST request.

- **Returning the Result**

    Once the operation is completed, the tool returns the result of the API call, which could be a success or an error message.

## Usage Example

Imagine you have a file at `/home/user/document.pdf`, and you want to upload it to a specific record identified by its tab ID and record ID. You would use the tool as follows:

- **Input**:

    Copy code

    ```
    {
    "filepath": "/home/user/document.pdf",
    "ad_tab_id": "1234567890abcdef1234567890abcdef",
    "record_id": "abcdef1234567890abcdef1234567890"
    }
    ```

- **Output**:

    Copy code

    ```
    {
    "result": {
        // ...response from the API...
    }
    }
    ```