---
tags: 
 - copilot
 - ai
 - ai tools
 - setup
---

# Copilot Setup

## Initial Configuration

In order to use Copilot, the user must access the Etendo Classic under the role *System Administrator* and generate a token in `Client`>`Secure Web Service Configuration`, clicking **generate key**.

![](../../assets/drive/FsABaJyI_6qxEtcAclALLbHXvoZbuMyyj9Md6M4_7ohvisQ3GVMEjCX05xjdPzRmvgcNqbMku306aaQTxrh34HckHZHBnXcy9iOXQypHsJSGLroa2lGI4Mzr_qPEOiWVc7JYEEGl.png)

## How to Set up Assistants

In this case, Etendo Copilot has two alternatives:

1. *Dataset installation*: Etendo provides dataset options to install predetermined assistants. In case of installing Etendo Copilot, for example, Bastian dataset(?) is available, to answer your questions about Etendo documentation.


    ![](../../assets/user-guide/etendo-copilot/setup/dataset-installing.png)

    !!!info
        To check the list of available assistants, visit [Default Copilot Apps](../../user-guide/etendo-copilot/bundles/overview.md#default-copilot-apps)(?)

    Once the reference data is applied, it is necessary to go to the **Assistant Window**, select the corresponding Assistant and click [Sync Assistant](#sync-assistant-button).

2. *Create your own Assistant*: Use the Assistant window to set up a new assistant with all the specific necessary characteristics.

## Assistant Window

:material-menu: `Application` > `Service` > `Copilot` > `Assistant`

The Assistant window allows you to define and configure assistants:

<figure markdown>
  ![Copilot App](../../assets/user-guide/etendo-copilot/getting-started/copilot-app.png)
  <figcaption> Open AI assistant type example</figcaption>
</figure>


- **Name**: Assistant name
- **Description**: Assistant description
- **App Type**: Langchain Agent, Open AI Assistant or Langgraph

    **Open AI Assistant**

    These assistants leverage OpenAI technology to provide assistance with a variety of tasks, from natural language processing to complex calculations. The assistants are able to train themselves with their own knowledge base and customized instructions.

    **Langchain Agent**

    These assistants can perform specific tasks in natural language and provide contextualized responses, enabling the implementation of multiple AI models, the use of a proprietary vector database and internal memory management. As well as the use of tools developed to solve specific problems. Some examples of these tools are XML Translation Tool, DB Query Tool, etc. The difference between Langchain and Open AI is that Langchain can save the information locally and it is a multiprovider agent.

    **LangGraph**

    This option works as a manager of other assistants and allows to select team members. (?)



In case of defining an **Open AI Assistant** type app, the following fields will be enabled: 

- **Prompt**: Specific instructions of the assistant. These instructions can be written in English or Spanish. 
- **Description**: The description of the assistant so that the manager can choose the appropriate assistant for each case.
- **Model**: Dropdown with the Open AI models available. If none of the options are selected, the model defined by default for the Etendo Copilot module in the [preference](../../user-guide/etendo-classic/basic-features/general-setup/application.md#preference) (?)window is to be used.
- **Retrieval**: If this checkbox is selected, the assistant can retrieve information from the app source. 
- **Open AI Assistant ID**: Read-only field in which the ID of the assistant once created is displayed.
- **Code interpreter**: Code Interpreter enables the assistant to write and run code. This tool can process files with diverse data and formatting, and generate files such as graphs.
- **Open AI Vectordb ID**: Read-only field in which the ID of the vector database(?) is displayed.
- **Temperature**: This controls randomness, lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.

In case of defining an **Langchain Agent** type app, the following fields will be enabled: 

- **Prompt**: Specific instructions of the assistant. These instructions can be written in English or Spanish.
- **Description**: The description of the assistant so that the manager can choose the appropriate assistant for each case. 
- **Provider**: (?)
- **Model**: Dropdown with the models available according to the selected provider.
- **Temperature**: This controls randomness, lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.

In case of defining an **LangGraph** type app, the following fields will be enabled: 

- **Prompt**: Specific instructions of the assistant. These instructions can be written in English or Spanish. 
- **Description**: The description of the assistant so that the manager can choose the appropriate assistant for each case.
- **Graph Preview**: It shows the tree of assistants under a certain manager.
- **Provider**: (?)
- **Model**: Dropdown with the models available according to the selected provider.
- **Temperature**: This controls randomness, lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.

    !!!info
        If this option is chosen, the **Refresh Preview** is shown, allowing the user to refresh the Graph Preview when changes to the team members are introduced.

If the App types Open AI Assistant or Langchain Agent are chosen, the tabs shows are [Knowledge](#knowledge-tab) and [skill and tools](#skills-and-tools-tab). If the LangGraph option is chosen, the [Team Members tab](#team-members-tab) is shown.

### Sync Assistant Button

This process takes care of updating or creating a new assistant, in case it does not exist. In addition to creating the assistant based on the configurations, it initially gets or updates the list of Open AI Models(?), and finally gets and uploads the files used as knowledge base.

### Knowledge Tab

In this tab, you can define the files that will be used by the assistant as knowledge base, in prompts or questions. 

!!!warning "File Limitation for Code Interpreter"
    If an assistant has the Code Interpreter check enabled, a maximum of 20 files is supported. Although it is possible to include more files in the knowledge base, exceeding this limit means that some files must be excluded. To do this, use the **Exclude from Code Interpreter** option on the files that you do not want to be processed by the Code Interpreter.



![](../../assets/user-guide/etendo-copilot/setup/app-source-tab.png)

!!!info
    To load new files, you must do it from the [Knowledge Base File](#knowledge-base-file).

Fields to note:

- **File**: The file selected as knowledge base.
- **Behaviour**: The way in which the assistant will use the file. It has three available options:
    - Add to the assistant as knowledge base: before using this option, it is necessary to synchronize the assistant with the [Sync Assistant](#sync-assistant-button). This behaviour is possible only with **Retrieval** checked.
    - Append the file content to the prompt: In this option, Etendo fails if the file is too large and exceeds the token limit allowed by the assistant. Then, this option is suitable for small files only. The file must be in text format.
    - Add content to each question: In this case, the same restrictions from the previous option apply. 
- **Type**: read-only field showing the type of file selected in the [Knowledge Base File window](#knowledge-base-file-window).
- **Active**: checkbox to activate the knowledge base file.
- **Exclude from Code Interpreter**: Checkbox to exclude files from being processed by the Code Interpreter during synchronization. This checkbox is only editable if the assistant has the Code Interpreter option enabled.
- **Exclude from Retrieval**: Checkbox to exclude files from being considered in the Retrieval process during synchronization.This checkbox is only editable if the assistant has the Retrieval option enabled.

### Skills and Tools Tab

In this tab, you can define the tools to be used by the assistant.

Fields to note:

- **Copilot Tool**: The user can select any of the options available in this field, as many as necessary but one at the time.
- **Description**: The description of the tool so that the assistant can choose the appropriate one for each case. (?)

![](../../assets/user-guide/etendo-copilot/setup/tool-tab.png)

!!!info
    To enter new tools, you must do it from the [Skill/Tool window](#skilltool-window)

### Team Members Tab

In this tab, the team members for the LangGraph manager (?) are defined.

Fields to note:

- **Member**: The user can select one or more assistants for the manager. 
- **Description**:  The description of the assistant so that the manager can choose the appropriate one for each case. (?)

## Knowledge Base File Window

:menu-material: `Application`>`Service`>`Copilot`>`Knowledge Base File`

In the Knowledge Base File window,  you can define the files with which the assistants can interact.

![](../../assets/user-guide/etendo-copilot/setup/copilot-file.png)

- **Name**: File Name.
- **Description**: File description.
- **Type**:
    - *Attached File* 
    This allows you to upload files directly into Copilot for later use during interactions with the assistants.
    - *HQL Query*
    This allows using an HQL query result as a file for app source.
    - *Remote File* 
    You can provide a public URL from which Copilot will retrieve the file when needed. This makes it easy to access documents and external resources.
- **Open AI File ID**: Read-only field showing the Open AI ID of the file once it is created.
- **Last Synchronization**: Read-only field displaying the date of the last update with OpenAI.
- **File name**: Name of the remote file in case you want to modify it.
- **URL**: Source file URL

## Skill/Tool Window

:menu-material: `Application`>`Service`>`Copilot`>`Skill/Tool`

In this window , the user can find available tools to be used in Copilot assistants.

![](../../assets/user-guide/etendo-copilot/setup/copilot-tool-window.png)

!!!info
    In case you want to define new tools, visit [How to Create Copilot Tools](../../developer-guide/etendo-copilot/how-to-create-copilot-tools.md)

### Webhooks Tab

(from previous webhooks window reference)
Some tools require to communicate with Etendo through WebHooks, so it is necessary to configure the access for each role in the WebHook window.
For example, for the Database Query Tool, the WebHook "DBQueryExec" is used, to the Role that will use this tool in an assistant, it is necessary to configure the access to this WebHook.
![WebHook](../../assets/developer-guide/etendo-copilot/available-tools/database-query-tool.png)

## Assistant Access Window

:menu-material: `Application`>`Service`>`Copilot`>`Assistant Access`

In this window, it is possible to give access to certain assistants to certain roles. 

## Role Window (?)

In the Role window `Application`>`General Setup`>`Security`>`Role`, you can configure access roles for each Copilot App. This means you can control who has permission to interact with each application. This feature is useful for ensuring that users only have access to applications and functions relevant to their responsibilities.

In the *Role* window, select a role and in the *Copilot App* tab add a new record for each Copilot App you want to give access to.

![Copilot Role](../../assets/user-guide/etendo-copilot/getting-started/copilot-role.png)

!!!info
    For more information, visit [Role](../../user-guide/etendo-classic/basic-features/general-setup/security.md#role).


## Process Request Window

Open `Application`>`General Setup`>`Process Scheduling`>`Process Request`. In this window, the user can schedule Etendo Copilot background processes by selecting the Copilot Apps Schedule option in the Process field and using all the provided options such as timing, start date, frequency, etc.

!!!info
    For more information, visit [Process Request](../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling.md#process-request).

### Copilot App Tab

!!! Info
    This tab is only visible when a **Copilot Apps Schedule** process is selected.

In this tab, the process to be scheduled can be configured. 

![](../../assets/user-guide/etendo-copilot/setup/process-request-copilot.png)

Fields to note:

- **Name**: Name description.
- **Copilot App**: Corresponding assistant for the process.
- **Prompt**: Instruction for the process.
- **Active**: Checkbox to select if this tool is active or not.