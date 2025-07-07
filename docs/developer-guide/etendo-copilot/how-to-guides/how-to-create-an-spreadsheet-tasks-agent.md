Based on the official guide on [How to Create an Agent](https://docs.etendo.software/latest/developer-guide/etendo-copilot/how-to-guides/how-to-create-an-agent/), this document provides a detailed walkthrough for creating a sophisticated agent that can leverage Google Drive, manage Google Sheets, and incorporate Etendo's task creation functionality.

### 1\. Defining the Agent's Core Prompt

The first step is to establish the agent's primary purpose and operational rules. This is achieved through a clear, concise prompt that serves as its core instruction set.

**Core Prompt:**

```
You are an agent that can interact with Google Sheets and Google Drive. For this, you can load an OAuth token and receive an "alias" for the token. This alias is for security purposes, so you can use it in the future without exposing the token directly.
```

This prompt defines the agent's identity and its secure method for handling authentication credentials.

### 2\. Configuring the Required Tools

To interact with Google services, the agent needs the appropriate tools. You must define these in the **Tool** window in Etendo.

  * **GoogleDriveTool**: Manages files and folders in Google Drive.

      * **Name:** `GoogleDriveTool`
      * **Description:** A tool to interact with Google Drive.
      * **Java Class:** `com.etendo.copilot.tools.googledrive.GoogleDriveTool`

  * **GoogleSpreadsheetsTool**: Reads and writes data in Google Sheets.

      * **Name:** `GoogleSpreadsheetsTool`
      * **Description:** A tool to interact with Google Spreadsheets.
      * **Java Class:** `com.etendo.copilot.tools.googlespreadsheets.GoogleSpreadsheetsTool`

#### Authentication

These tools require a Google OAuth 2.0 token to function. The agent uses this token to authenticate its requests to Google's APIs. To obtain a token, please follow the steps in this guide: `[How to Obtain a Google OAuth Token](link-to-your-guide)`.

#### Usage Examples

Once the tools are configured, you can interact with the agent using natural language. The agent will interpret your request and use the appropriate tool.

**Example 1: Creating a File**

You can instruct the agent to create a new Google Sheet.

  * **Your Prompt:**
    ```
    Create a new Google Sheet named 'Q3 Sales Report'.
    ```
  * **Agent's Response:**
    ```
    The Google Sheet 'Q3 Sales Report' has been created successfully. You can access it here: [link](https://docs.google.com/spreadsheets/d/your-new-sheet-id)
    ```

**Example 2: Writing Data to a File**

After creating the file, you can ask the agent to add data to it.

  * **Your Prompt:**
    ```
    In the 'Q3 Sales Report' sheet, add a header row with the following columns: 'ProductID', 'Region', 'UnitsSold', 'SaleDate'.
    ```
  * **Agent's Response:**
    ```
    The header row has been added to the 'Q3 Sales Report' sheet.
    ```

### 3\. Extending Functionality with Tasks

You can further enhance the agent by enabling it to create tasks within Etendo. This is done by expanding its core prompt.

**Prompt Extension:**

Add the following text to the agent's prompt defined in the first step:

```
Additionally, you can create tasks in Etendo. The Task Creation Tool requires a csv to create the tasks, so if you want to use a Google Sheet, you must download it as a csv first.

The ID of the agent that can create products (Product Creator):"767849A7D3B442EB923A46CCDA41223C"
```

This snippet provides the agent with crucial context:

1.  It specifies the **workflow** for creating tasks from a Google Sheet (i.e., it must be converted to CSV).
2.  It provides the **ID of another agent**, which can be used for context or inter-agent communication.

This allows for integration with the asynchronous task system. For more information, visit the link: `[Asynchronous Tasks Documentation](link-to-async-tasks-guide)`

### 4\. Finalizing the Agent Setup

Once the agent's prompt is fully defined and all necessary tools are associated, the final step is to link them.

Navigate to the **Agent** window in Etendo and, in the **Tools** tab, assign the `GoogleDriveTool`, `GoogleSpreadsheetsTool`, and the `Task Creation Tool` to your agent.

By completing this step, you activate the agent's full capabilities. It can now seamlessly orchestrate workflows between Google Drive and Etendo, such as reading data from a Google Sheet and using that data to create tasks automatically.