---
tags:
    - Copilot
    - IA
    - Tool
    - Load OAuth Token 
---

# Load OAuth Token Tool
:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Load OAuth Token Tool** is a crucial security and session management utility. Its primary function is to securely fetch a pre-configured **OAuth Token** from the Etendo backend and load it into the current conversation's memory.

This tool does not perform an action on its own but acts as a necessary first step for any workflow requiring **OAuth2 authentication** (e.g., accessing Google Drive or Google Sheets). By loading the token and returning only an `alias`, it allows other tools to use the credential without ever exposing the sensitive token value to the AI model or the user.

## Intended Workflow

This tool is designed to be the first call in a multi-step process. The typical workflow is as follows:

1.  A user asks the assistant to perform an action that requires an external authenticated service (like Google Drive).
2.  The assistant first calls the `LoadOAuthTokenTool`.
3.  This tool fetches the OAuth token from Etendo and stores it in the conversation's memory, returning a safe `alias`.
4.  The assistant then calls the required tool (e.g., `GoogleDriveTool`) and passes the `alias` it just received.
5.  The `GoogleDriveTool` uses the `alias` to retrieve the actual token from the conversation's memory and completes the user's request.

## Parameters

  - `al` (string, optional): An alias (a custom name) for the OAuth token.
      - If an alias is provided, the token will be loaded into memory under that specific name.
      - If this parameter is **not provided**, a unique, random alias (e.g., `TOKEN_1234abcd-....`) will be generated automatically.
      - In either case, the alias that was used is returned in the final success message.

## Functionality

The tool executes the following steps:

1.  **Determines the Alias**: It uses the user-provided `al` or generates a new one if it's absent.
2.  **Fetches the Token**: It makes a secure, server-side call to an Etendo webhook (`/webhooks/ReadOAuthToken`) to retrieve the pre-configured OAuth token. An organization's administrator must have configured this token in the Etendo backend beforehand.
3.  **Stores the Token**: It stores the fetched token in the current conversation's context (`ThreadContext`) in a dictionary, using the alias as the key.
4.  **Returns the Alias**: It returns a success message to the assistant, confirming that the token is loaded and ready for use via the returned alias.

## Usage Examples

### Example 1: Loading a Token with a Generated Alias

When you don't need a specific name for the token, you can call the tool without parameters.

**Request:**

```json
{}
```

**Example Success Response:**

```
OAuth token loaded successfully with alias: TOKEN_a1b2c3d4-e5f6-7890-gh12-i3j4k5l6m7n8. You can now use this alias to access the token.
```

### Example 2: Loading a Token with a Custom Alias

This is useful if you want to refer to the token with a memorable name.

**Request:**

```json
{
  "al": "my_work_google_account"
}
```

**Example Success Response:**

```
OAuth token loaded successfully with alias: my_work_google_account. You can now use this alias to access the token.
```

### Example 3: Conceptual Two-Step Workflow

Here is how an assistant would use this tool in practice to list files from Google Drive.

  - **Step 1: Load the token**

      - **Tool Call:** `LoadOAuthTokenTool()`
      - **Result:** The assistant receives the message: "OAuth token loaded successfully with alias: `TOKEN_a1b2...`"

  - **Step 2: Use the alias in the target tool**

      - **Tool Call:** `GoogleDriveTool(alias="TOKEN_a1b2...", mode="list")`
      - **Result:** The `GoogleDriveTool` successfully lists the files because it could access the token using the provided alias.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.