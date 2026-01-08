---
title: How to Create a Spreadsheet and Tasks Agent
tags:
    - How to
    - Etendo Copilot
    - Agent
    - Spreadsheet
    - Tasks
    - Google Drive
---


# How to Create a Spreadsheet and Tasks Agent

## Overview

Based on the official guide on [How to Create an Agent](./how-to-create-an-agent.md), this document provides a detailed walkthrough for creating an agent that can leverage Google Drive, manage Google Sheets, and incorporate Etendo's task creation functionality.

1.  ### Defining the Agent Prompt

	The first step is to establish the agent's primary purpose and operational rules. This is achieved through a clear, concise prompt that serves as its core instruction set.

	**Prompt:**

	```title="Prompt"
	You are an agent that can interact with Google Sheets and Google Drive.
	For this, you can load an OAuth token and receive an "alias" for the token. 
	This alias is for security purposes, so you can use it in the future without exposing the token directly.
	```

	This prompt defines the agent's identity and its secure method for handling authentication credentials.

2. ### Authentication

	These tools require a Google OAuth 2.0 token to function. The agent uses this token to authenticate its requests to Google's APIs. To obtain a token, please follow the steps in the [OAuth Provider](../../etendo-classic/bundles/platform/etendo-rx.md#oauth-provider) guide.

	#### Usage Examples

	Once the tools are configured, you can interact with the agent using natural language. The agent will interpret your request and use the appropriate tool.

	1. **Example: Creating a File**

		You can instruct the agent to create a new Google Sheet.

		* **Your Prompt:**
			```
			Create a new Google Sheet named 'Q3 Sales Report'.
			```
		* **Agent's Response:**
			```
			The Google Sheet 'Q3 Sales Report' has been created successfully. You can access it here: [link](https://docs.google.com/spreadsheets/d/your-new-sheet-id)
			```

	2. **Example: Writing Data to a File**

		After creating the file, you can ask the agent to add data to it.

		* **Your Prompt:**
			```
			In the 'Q3 Sales Report' sheet, add a header row with the following columns: 'ProductID', 'Region', 'UnitsSold', 'SaleDate'.
			```
		* **Agent's Response:**
			```
			The header row has been added to the 'Q3 Sales Report' sheet.
			```

3. ###  Extending Functionality with Tasks

	You can further enhance the agent by enabling it to create tasks within Etendo. Add the following text to the agent's prompt defined in the first step:

	```title="Prompt"
	Additionally, you can create tasks in Etendo. The Task Creation Tool requires a csv to create the tasks, so if you want to use a Google Sheet, you must download it as a csv first.

	The ID of the agent that can create products (Product Creator):"767849A7D3B442EB923A46CCDA41223C"
	```

	This snippet provides the agent with crucial context:

	1.  It specifies the **workflow** for creating tasks from a Google Sheet (i.e., it must be converted to CSV).
	2.  It provides the **ID of another agent**, which can be used for context or inter-agent communication.

	To interact with Task, the agent needs the appropriate tools. You must define these in the **Skill/Tool** tab.
	
	!!! info 
		For more information, visit the link: [Asynchronous Tasks Documentation](../../etendo-classic/bundles/platform/task.md)

4. ### Finalizing the Agent Setup

	Once the agent's prompt is fully defined and all necessary tools are associated, the final step is to link them.

	Navigate to the **Agent** window in Etendo and, in the **Skill/Tools** tab, assign:
	
	- [GoogleDriveTool](../available-tools/google-drive-tool.md): Manages files and folders in Google Drive.
	- [Google Spreadsheets Tool](../available-tools/google-spreadsheet-tool.md): Reads and writes data in Google Sheets.
	- [Task Creation Tool](../available-tools/task-creator-tool.md): Automates the creation of tasks based on the content of a file. It supports **ZIP**, **CSV**, **XLS**, and **XLSX** formats.
		
	By completing this step, you activate the agent's full capabilities. It can now seamlessly orchestrate workflows between **Google Drive** and **Etendo**, such as reading data from a **Google Sheet** and using that data to **create tasks** automatically.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.