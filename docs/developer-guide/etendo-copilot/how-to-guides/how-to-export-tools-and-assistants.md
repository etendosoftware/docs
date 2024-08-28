---
tags:
    - Copilot
    - IA
    - Tools
    - Datasets
---

# How to Export Tools and Assistants

## Overview

When developing in Etendo Copilot, it is possible to export assistants and tools. This documentation details how to export them and how to make sure that, when installing the module, the configurations are ready to use, allowing a **plug and play** process.

## Exporting Assistants

There are two main methods for exporting assistants: export it as a dataset where the configured assistant is exported within an Etendo Classic dataset or export as a System Administrator, where the assistant(s) defined with the System Administrator role are exported directly together with the module.

### Exporting Assistants as Datasets

1. Initial setup of the assistant:
    - Configure the assistant and tools in the environment where the development takes place.
    - Make sure to include all the necessary fields to be exported. Make sure to configure correctly the **Knowledge Base**, **Skills/Tools** and **Team Members** tabs, as well as the records in the **Knowledge Base File** window.

    
    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/exportcopilot1.png)
  <figcaption>Assistant example with complete tabs.</figcaption>
</figure>

2. Create and Configure a Dataset:
    - As System Administrator, go to the **Dataset** window and create a new record by selecting the module under development.
    - Define the **Search Key** and **Name** of the dataset.
    - Set the **Data Access Level** to **System/Organization** (recommended for user assistants).

3. Add Tables to the Dataset

    For each window or tab to be exported, create a record in the **Table** tab. Specify the corresponding table and add the appropriate **HQL/SQL Where** clause.

    - **Assistant:** Table `etcop_app` 
    ```sql title="Where Clause"
    id in ('<AssistantID>')
    ```
    - **Knowledge Base:** Table `etcop_app_source`
    ```sql title="Where Clause"
    etcopApp.id in ('<AssistantID>')
    ```
    - **Skills/Tools:** Table `etcop_app_tool`
    ```sql title="Where Clause"
    `copilotApp.id in ('<AssistantID>')
    ```
    - **Team Members:** Table `ETCOP_Team_Member`
    ```sql title="Where Clause"
    copilotApp.id in ('<AssistantID>')
    ```
    - **Knowledge Base File:** Table `etcop_file`
    ```sql title="Where Clause"
    id in ('<knowladgeBaseFileID>')
    ```
    
    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/exportcopilot2.png)
    <figcaption>Dataset window configuration example in the module Copilot Purchase Expert</figcaption>
    </figure>

4. Export Reference Data Button
    - Execute the **Export Reference Data** process, which will create the `referencedata/` folder inside the selected module, with all the records that were exported according to the dataset configuration. 

    !!!note
        Verify that all the required records are generated in the `.XML` file.


5. Include Reference Data in the Module
    - Check the **Include Reference Data** checkbox in the module definition and add a description to the dataset referring to the exported assistant.

    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/exportcopilot3.png)
    <figcaption>Configuration example in the module Copilot Purchase Expert</figcaption>
    </figure>

    - When the module is installed, the dataset will be available for application in the **Enterprise Module Management** window.

    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/exportcopilot4.png)
    <figcaption>Distributed datasets example</figcaption>
    </figure>


### Exporting Assistants as System Administrator

1. Define Assistant with System Administrator Role

    - Log in with the **System Administrator** role.
    - Configure the assistant and its tabs. Select the module (under development) in the **Module** field.
    - Optionally, check the **System App** checkbox to restrict the use of the assistant to the administrator role only.

    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/exportcopilot5.png)
    <figcaption>Exported assistant example and available only as System Administrator</figcaption>
    </figure>

2. **Export the Database**.
    - Execute the command `./gradlew export.database` to export the assistant together with the module.

## Exporting Tools

**Tool configuration**: When defining a tool, select the module (under development) in the **Module** field, and run `./gradlew export.database` command to export the tool together with the module.

<figure markdown="span">
![](../../../assets/developer-guide/etendo-copilot/exportcopilot6.png)
<figcaption>Tool configuration example</figcaption>
</figure>

!!!info
    For more information, visit [How to create a Copilot Tool](../../../developer-guide/etendo-copilot/how-to-guides/how-to-create-copilot-tools.md).