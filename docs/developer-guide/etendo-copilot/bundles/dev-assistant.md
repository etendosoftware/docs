---
tags:
    - Beta
    - Copilot
    - IA
    - Windows, tabs and fields
    - Creator
    - Assistants
---

# Dev Assistant

:octicons-package-16: Javapackage:  `com.etendoerp.copilot.devassistant`

## Overview

The **Dev Assistant section** provides an overview of the tools, functionality, and usage examples for various development assistants available in Etendo. Dev Assistant streamlines workflow management for developers by offering **specialized assistants** that simplify tasks such as creating buttons, windows, tabs and tables, Event Handlers, Jasper Reports, background processes, and more. These assistants are designed to enhance productivity and reduce complexity, making it easier for developers to efficiently build and manage different components within the Etendo platform.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).


## Assistants

### Etendo Code Expert 

**Etendo Code Expert** is an assistant designed to read previously indexed files and provide answers related to their content. It can summarize, answer technical questions, suggest programming code improvements, and offer general assistance about files.

This assistant is useful for avoiding the need to manually review all files. There is no need to load the files directly into the system since it will have Etendo Classic code preconfigured. Also more files can be configured if neccesary.

#### Functionality

With this assistant it is possible to: 

- Ask code development questions and based on Etendo code previously indexed, the assistant will give possible code suggestions or solutions. 

#### Usage Example 

1. To use this assistant, it is necessary to log in as `System Administrator` role and set the role access. For this, go to the **Assistant** window, configure Etendo Code Expert and synchronize it. Then, go to the **Assistant Access** window and give access to the role.  

2. Open Copilot and select Etendo Code Expert

    ![code-expert.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/etendo-code-expert1.png)

3. Ask the assistant for what you need to create.

    ![code-expert.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/etendo-code-expert2.png)

### Event Handler Creator

This assistant is capable of creating Event Handlers in Etendo Classic. You only need to provide the Java package of the module where it should be exported and specify the action to be performed. 

#### Tools

- [Read File Tool](../available-tools/read-file-tool.md)
  
- [Write File Tool](../available-tools/write-file-tool.md)

#### Functionality

**Event Handler Creator** is an assistant designed to automatically create event handlers in Java. It uses code indexed in its knowledge base to read classes that extend `EntityPersistenceEventObserver`, providing examples to build a new event handler. To generate an event handler, the wizard requires the following parameters:
  
- **Java package**: The package where the file will be saved.
- **File name**: The name of the file to create.
- **Entity**: The entity to observe.
- **Description**: A description of the functionality to be implemented by the event handler.

#### Usage Example

1. To use this assistant, it is necessary to log in as `System Administrator` role and set the role access. For this, go to the **Assistant** window, configure Event Handler Creator and synchronize it. Then, go to the **Assistant Access** window and give access to the role.  

2. Open Copilot and select Event Handler Creator, then ask to the assistant what you need to create.

    ![eventhandler.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/EH1.png)

3. Then this is the result given by the assistant.

    ![eventhandler.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/EH2.png)

### Background Process Creator

**Background Process Creator** is an assistant specialized in the automatic creation of Background Processes in Java. The assistant reads previously indexed code and uses examples of classes extending `DalBaseProcess` to build new Background Processes.

#### Tools

- [API Call Tool](../available-tools/openapi-tool.md)

- [Read File Tool](../available-tools/read-file-tool.md)
  
- [Write File Tool](../available-tools/write-file-tool.md)

#### Functionality.

Background Process Creator generate Background Processes in Java using indexed examples of classes that extend `DalBaseProcess`. To configure the assistant properly, you need to provide the following parameters:

- **Java package**: The Java package where the new process will be saved. It should follow the format `java.package.of.the.module`.
- **Name**: The name of the Java file to be created.
- **Search Key**: A key that will be used to locate the process in other windows when necessary.
- **Code description**: The purpose and logic that the Background Process should fulfill.

#### Usage Example

1. To use this assistant, it is necessary to log in as `System Administrator` role and set the role access. For this, go to the **Assistant** window, configure Background Process Creator and synchronize it. Then, go to the **Assistant Access** window and give access to the role.

    ![background.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/BG1.png)


2. Open Copilot and select Background Process Creator, then ask to the assistant what you need to create.

3. Then this is the result given by the assistant.

    ![background.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/BG2.png)

    ![background.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/BG3.png)

### Webhook Creator

**Webhook Creator** is an assistant designed to facilitate the creation and registration of webhooks in Java. A webhook acts as a communicator between applications or services, allowing data to be automatically sent from one system to another in real-time when a specific event occurs.

#### Tools

- [API Call Tool](../available-tools/openapi-tool.md)

- [Read File Tool](../available-tools/read-file-tool.md)
  
- [Write File Tool](../available-tools/write-file-tool.md)

#### Functionality

This assistant simplifies webhook creation by automatically generating the necessary Java files and registering them in the Etendo ERP system, taking examples of indexing code readeing the classes extends of `BaseWebhookService`. It is necessary give some useful information:

- **Module Package**: The Java package where the new process will be saved. It should follow the format `java.package.of.the.module`.
- **Webhook Name**: The name of the Java file to be created.
- **Parameters**: The parameters will be added to the webhook for the use.

#### Usage Example

1. To use this assistant, it is necessary to log in as `System Administrator` role and set the role access. For this, go to the **Assistant** window, configure Webhook Creator and synchronize it. Then, go to the **Assistant Access** window and give access to the role.

    ![webhook.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/WH1.png)


2. Open Copilot and select Webhook Creator, then ask to the assistant what you need to create.

3. Then this is the result given by the assistant.

    ![webhook.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/WH2.png)

    ![webhook.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/WH3.png)

### Reference Creator

The Reference Creator assistant that **creates references** in the Etendo Application Dictionary. This tool allows for example the addition of new list references to a specific module within the Etendo database via an HTTP request to a webhook.

It is particularly useful in the development process, enabling system administrators or developers to define new references that can later be utilized in applications. This tool automates the creation of these references, ensuring **consistency and adherence** to quality standards in the configuration.

#### Tools

- [Create Reference Tool](../available-tools/create-reference-tool.md): This tool allows to create references on Etendo and on the database using queries generated with the parameters given in the tool. 

#### Functionality

The **Reference Creator** assistant is designed to facilitate the creation of references, for example, it is possible to create list of references in the Etendo Application Dictionary by providing the assistant the necesary input parameters. 

Let's see an example about how the user can interact with the assistant and create the needed references in Etendo.

#### Usage Example 

1. To use this assistant, it is necessary to log in as `System Administrator` role and set the module in which the changes will be exported in development.

2. Open Copilot and select Reference Creator Assistant

    ![alt text](../../../assets/developer-guide/etendo-copilot/bundles/create-references/create-references-0.png)

3. Ask the assistant which reference type you need to create

    ![alt text](../../../assets/developer-guide/etendo-copilot/bundles/create-references/create-references1.png)

4. The Create References Tool will process these parameters, verify the access token, build the request body and call the Etendo webhook to create the reference.

    In the Reference window, Etendo shows all the fields with the corresponding information generated and in the List Reference tab, it is possible to see the new list reference created. 

    ![alt text](../../../assets/developer-guide/etendo-copilot/bundles/create-references/create-references-2.png)


5. Once the development is validated by the developer, and the necessary manual modifications are made, it is possible to export the changes in the corresponding module.

    ```title="Terminal"
    ./gradlew export.database --info
    ```

### Tables, Windows and Tabs Creator

The **Tables, Windows and Tabs Creator** is designed to help developers and speed up the process of creating windows, tabs, fields, system elements, menu entries, etc.  as well as tables and columns in the database.
It is possible to give an input with all the necessary information, or the assistant will go step by step, asking for more information. Also, depending on the context, the assistant can make suggestions that the developer must confirm.

!!!warning
    This Assistant is currently in its beta testing phase. While it is designed to automate the process of creating windows and tables, there are instances where tasks may not be fully completed. Specifically, there may be issues with adding foreign keys, correctly naming elements, etc.

    For optimal results, it is recommended to proceed step-by-step and be as specific as possible in your instructions to the Assistant. This will help mitigate potential errors and ensure more accurate task completion.

    Thank you for your understanding as we continue to improve the functionality and reliability of this assistant.


#### Tools

- [**DDL Tool**](../../etendo-copilot/available-tools/ddl-tool.md): This tool allows to registering and creating tables on Etendo and on the database using queries generated with the parameters given on the tool. The query is adjusted for the user needs, for example, if the user wants to add a column with a default value, the tool can receive a value or not if the element should not has a default value.

- Multiples Webhooks: These webhooks are used to run the java files that create or modify the fields on the Etendo Classic and execute process or queries. These webhooks are: `RegisterTable`, `CreateTable`, `RegisterFields`, `RegisterWindowAndTab`, `RegisterColumns`, `ElementsHandler`, `SyncTerms`.


#### Functionality

!!! info
    With this assistant, it is possible to create: 

    - **Tables and Columns**: both tables and columns are created based on user specification and the supported types are `string`, `number`, `tableDir`, `date`, `text` and `boolean` (each field will have default lengths unless specified).  
    - **Windows**: only Mantein type windows are supported
    - **Tabs**: Can be created at multiple levels, although it is important to make it clear to the assistant to add the corresponding foreign keys.
    - **Fields**: Fields are created from columns, respecting the same name but without *"_"*.
    - **Elements**: The elements will be created automatically, sharing the name of the columns, but replacing the *"_"* with spaces. The help and description fields will also be added automatically.
    - **Menu**: A menu entry is automatically created, the developer must manually place it in the desired position.

 - Ask the **Tables, Windows and Tabs Creator** for a window to add in the system and the module database prefix where the table will be exported. The assistant will then register in the system the table and create it in database, including the mandatory columns. At this stage the assistant checks if the module is in development. If is not, the assistant prompts the user for a correct prefix from a module in development. Additionaly, the assistant checks if the table name is already in use; if it is, asks the user to provide a new name. In case the window belongs to the module under development, new columns, tabs and fields can be added.

- The assistant will ask to the user for information to add, like columns, data types, help and description, etc.

- The user must confirm the steps or set up a modification about the given information.


#### Usage Example 

1. To use this assistant, it is necessary to log in as `System Administrator` role and set the module in which the changes will be exported in development.

2. Open Copilot, and select Tables, Windows and Tabs Creator 
    ![dev-assistant.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant-1.png)

3. Ask the assistant for what you need to create.
    ![dev-assistant.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant5.png)


4. With the task complete, it is necessary recompile with a smartbuild and restart Tomcat

    ```title="Terminal"
    ./gradlew smartbuild --info
    ```
    ![dev-assistant2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant2.png)

5. Window in the System, the window can be viewed with the user role.
    ![dev-assistant3.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant3.png)
    ![dev-assistant4.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant4.png)

6. Once the development is validated by the developer, and the necessary manual modifications are made, it is possible to export the changes in the corresponding module.

```title="Terminal"
./gradlew export.database --info
```

---

## Assistants

The Dev Assistant is not just a single tool; it is a complete ecosystem of interconnected assistants working together seamlessly. Each assistant specializes in a specific area of development, enabling you to tackle complex tasks with speed and precision. Think of it as a team of experts, each enhancing your workflow, removing obstacles, and ensuring that every step you take is more agile and efficient. Whether generating queries, managing files, or orchestrating complex configurations, the Dev Assistant and its suite of complementary tools have your back, making development not only faster but also more intuitive and enjoyable.

---

### Jasper Report Creator

#### Overview

The **Jasper Assistant** is designed to facilitate the creation, editing, and registration of reports within the Etendo platform. Using JasperReports, it allows developers to define the structure of the report, apply styles, manage parameters, and register the reports in the system for use in different modules.

!!!info
    This assistant simplifies the process by verifying that all fields used in a report are correctly defined in the database, thus avoiding common errors such as 'Field not found'. It also supports integrating logos, applying styles, and performing data grouping to ensure that the reports meet business requirements.

#### Purpose

The **Jasper Assistant** is useful for generating custom reports within Etendo. It allows developers and system administrators to create detailed reports by applying a wide range of styles and configurations and registering these reports in the Etendo database so they are available in different modules and functionalities of the platform.

#### Components

The Jasper Assistant is composed of the following tools:

- **DBQueryGeneratorTool**:
    - `SHOW_TABLES` mode: Returns the database tables with their name and description.
    - `SHOW_COLUMNS` mode: Returns the columns of a table with their name and description. This mode requires the `p_data` parameter with the table name.
    - `EXECUTE_QUERY` mode: Executes the SQL query provided by the user. This mode requires the `p_data` parameter with the query.

- **JasperTool**:
    - Allows creating, editing, or registering reports in Etendo based on the provided data.

- **OCRTool**:
    - Returns a JSON object with information from a local file (image or PDF). This tool can extract the JRXML from an already created report or edit a report using an image.

- **ReadFileTool**:
    - Reads JRXML files from the path provided by the user.

- **WriteFileTool**:
    - Saves reports to the specified path or rewrites files with the requested modifications.

#### Functionality

##### Report Creation

The Jasper Assistant requests the following parameters to create a report:

- **Report storage path**: The location in the file system where the report file will be saved.
- **Report name**: The name that will be assigned to the report.
- **Report encoding language**: The language in which the report will be encoded (default is UTF-8).
- **Report parameters**: A list of parameters that the report will accept.
- **SQL query**: The SQL query that will provide data to the report.
- **Report styles**: Definition of the visual styles applied to the report.
- **Data grouping**: Configuration of data grouping within the report.
- **Image or logo in the report**: Specification of images or logos to include.
- **Data distribution**: Structure of how the data will be organized in the report.

##### Report Registration

Once the report is created, it can be registered in the system. The assistant requests the following arguments:

- **Report name**: Name that will be used to register the report in the system.
- **Module prefix**: Prefix that identifies the module where the report will be registered.
- **Search key**: Unique key to identify the report in the system.
- **Help comments**: Additional information to help understand the purpose of the report.
- **Description**: Detailed description of the report.
- **Report path**: Path where the report is stored.
- **Parameters**: List of registered parameters that can be used when executing the report.

##### Report Editing

The assistant also allows editing existing reports. Available actions include:

- **Parameter Modification**: Allows editing any already registered report parameter.
- **SQL Query Update**: Modification of the SQL query used by the report.
- **Change of Styles and Groupings**: Update of visual styles and data grouping configuration.

#### Output

Depending on the request, the Jasper Assistant will return:

- A created report, saved in the path indicated by the user.
- The edition of a specific report, with the changes applied as requested.
- The registration of a report in Etendo, ready to be used in the system.

#### Utility

- **Automation**: Facilitates automated creation and registration of reports in Etendo, reducing manual intervention.
- **Consistency**: Ensures that reports are created and registered uniformly and following best practices.
- **Flexibility**: Allows the creation of highly customized reports to meet specific needs.
- **Error Handling**: Provides clear feedback on any issues encountered during the creation or registration of the report.

#### Usage Example

##### 1. Report Creation
**User**: *"Create a sales report with the fields: customer name, sales date, and total amount. Group the data by customer name and include a summary of total sales. Add the company logo to the report header and export the report to the 'salmod' module."*

**Jasper Assistant**: *"The sales report has been created with the specified fields and grouped by customer name. The company logo has been added to the report header. The report has been registered in the system under the 'salmod' module. Please compile and restart Etendo to ensure the changes take effect. If you need further modifications, please let me know."*

![CreateReport.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/CreateReport.png)


##### 2. Report Registration
**User**: *"I want to register a report in Etendo."*

**Jasper Assistant**: *"Please provide the following details: Report name, module prefix, search key, parameters, and report path."*

![RegistrateReport.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport.png)

Once the report is created the assistant will respond:

![RegistrateReport2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport2.png)

After running the smartbuild we will be able to see the process of the created report:

![RegistrateReport3.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport3.png)

As you can see in the image, it also adds the parameters and even in the "Report Definition" tab it defines the PDF Template of the report and in the "Menu" it creates the Process definition that we defined in the previous step.

![RegistrateReport4.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport4.png)

![RegistrateReport5.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport5.png)


Finally, we can observe the created report and set the chosen parameter to see the printed version.

![RegistrateReport6.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport6.png)

##### 3. Report Editing
**User**: *"I want to update the sales report by changing the style and adding a new field 'discount'."*

**Jasper Assistant**: *"The sales report has been updated with the new style and the 'discount' field has been added."*

![EditReport.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/EditReport.png)

#### Conclusion

The **Jasper Assistant** is an essential tool for managing reports on the Etendo platform. By automating and simplifying the process of creating, editing, and registering reports, it allows developers and system administrators to optimize the workflow related to generating custom reports and integrating them into Etendo modules.

---

### Module Creator


#### How to Create a Module in Etendo Classic

Etendo Classic allows you to create modules that provide additional functionality that can be deployed independently. These modules can range from additional reports to content packs (translations, chart of accounts, etc.). In this guide, we will walk through the process of creating a module using the **CreateModuleWebHook**.

##### Steps to Create a Module

To start creating your module in Etendo, follow the steps below.

###### 1. Gather Required Information

Before you can create your module, you need to provide the following information:

- **Javapackage**: The Java package of the module (e.g., `com.etendoerp.copilot.prueba`).
- **Module Name**: A name for your module (e.g., `Test Module`).
- **Description**: A brief description of the module's functionality.
- **Help/Comment**: Additional help text or comments regarding the module (optional).
- **Version**: The version of the module (e.g., `1.0.0`).
- **DBprefix**: A prefix for the database objects associated with the module (must be in uppercase, e.g., `FJTS`).
- **License**: The license type for the module. Options are:
    - `Apache License 2.0`
    - `Openbravo Public License`
    - `Mozilla Public License 1.1`
    - `Etendo Commercial License`

###### 2. Call the `CreateModuleWebHook`

The `CreateModuleWebHook` simplifies the creation process by automating various steps. This webhook will:

- Validate all the parameters (such as module name, version, and license).
- Assign the database prefix.
- Register the module.
- Optionally, add module dependencies.

###### 3. Webhook Call Example

When invoking the webhook, the **body parameters** should follow this structure:

```json
body_params = {
  "Javapackage": "com.etendoerp.copilot.test",
  "SearchKey": "testmodule",
  "ModuleName": "Test Module",
  "HelpComment": "This is a test module created for demonstration purposes.",
  "Description": "This module adds test functionality to Etendo Classic.",
  "Version": "1.0.0",
  "Prefix": "FJTS",
  "ModuleLicense": "Etendo Commercial License"
}
```

**Note**: The database prefix must always be in uppercase.

###### 4. Example Interaction with the Assistant

Here is an example interaction with the module creation assistant:

**User Input:**
```
I need to create a new module in Etendo. The data is as follows:
- Javapackage: com.etendoerp.copilot.test
- Module Name: Test Module
- Description: Infer the description
- Help/Comment: Infer the help/comment
- Version: 1.0.0
- DBprefix: FJTS
- License: Etendo Commercial License
```

**Assistant Response:**
```
To create your module in Etendo, I have inferred the following:

- Description: "This module adds test functionality to Etendo Classic."
- Help/Comment: "This is a test module created for demonstration purposes."

Your module has been created successfully, and it only depends on the Core module. If it depends on other modules, you should add them yourself.
```

![ModuleCreation.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/ModuleCreation.png)

If we go to the "Module" window we can find the created record.

![ModuleCreation2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/ModuleCreation2.png)

The module will also have the dependency, in this case "Core" with the prefix and data package mentioned by the user.

![ModuleCreation3.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/ModuleCreation3.png)

![ModuleCreation4.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/ModuleCreation4.png)

![ModuleCreation5.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/ModuleCreation5.png)

###### Components

The Module Creator Assistant is composed of the following tools:

- **ApiCallTool**:
    - This tool executes a call to an API and returns the response.

###### 6. Validation and Registration

Once the webhook has been called, it will automatically:

- Register the module in Etendo.
- Assign the **Java package** and **database prefix**.
- Handle the specified **license**.
- Set up basic **module dependencies**.

You can confirm that the module has been created by navigating to the `Module` window in Etendo.

##### Additional Information

###### Managing Dependencies

If your module depends on other modules (besides the Core module), you need to manually add these dependencies in the `Dependency` tab of the module window.

###### Editing the Module

You can further edit the module properties, such as changing descriptions or adding more complex logic, through the Etendo development environment.

###### License Handling

The license you choose will determine how the module is handled legally. Ensure you select the appropriate license based on your module's distribution needs.

##### Conclusion

The **CreateModuleWebHook** greatly simplifies the process of creating and registering modules in Etendo. By providing the necessary parameters, you can quickly deploy your functionality without extensive manual setup.

For further customization and development, refer to the official [Etendo Developer Guide](https://docs.etendo.software/latest/developer-guide/etendo-classic/how-to-guides/how-to-create-a-page-in-etendo-documentation/) for more detailed steps.

---

### Button Process Creator


#### Button Process Creation Assistant for Etendo Classic

This assistant simplifies the process of creating and registering buttons and process definitions in **Etendo Classic**. By automating the workflow through webhooks, it removes the need for manual configuration, ensuring that your processes and buttons are set up correctly and efficiently.

##### Functionality Overview

The **Button Process Creation Assistant** automates the creation of a button and the registration of a process in **Etendo Classic** through a webhook call. Here's what it does:

1. **Validation of Parameters**:
    - Ensures that all required fields (such as module prefix, Java package, process name, etc.) are provided.
    - Validates that the search key is properly formed (e.g., including the module prefix).

2. **Process Button Creation**:
    - Creates a Java class for a process button that extends `BaseProcessActionHandler`.
    - Registers the button in the specified window, tab, and table of the Etendo system.

3. **Process Definition Creation**:
    - Registers the process in the system by creating a process definition.
    - Associates the process with parameters, if needed.

4. **Parameter Registration**:
    - Automatically registers any necessary parameters for the process with attributes such as database name, name, length, sequence number, and reference.

5. **Webhook Automation**:
    - The entire process is executed via a webhook, ensuring seamless and automated integration into Etendo Classic.

##### Required Data for Button and Process Creation

When creating a button or registering a process, the assistant will request the following information:

- **Java Package**: The Java package of the module where the button's class will be created (e.g., `com.etendoerp.module`).
- **Module Prefix**: A prefix for the module (e.g., `COPDEV`).
- **Window**: The window in Etendo where the button will appear.
- **Tab**: The specific tab within the window where the button will be located.
- **Table**: The table associated with the process.
- **Process Name**: The name of the process to be created.
- **Search Key**: A unique search key for the process that includes the module prefix (e.g., `COPDEV_ActualizarDescripciónPedido`).
- **Parameters**: Optional parameters for the process, including:
    - **BD_NAME**: The database column name.
    - **NAME**: The name of the parameter.
    - **LENGTH**: The length of the parameter field.
    - **SEQNO**: The sequence number of the parameter.
    - **REFERENCE**: A reference for the parameter (if it's linked to another field or table).
- **Help Comment**: An optional help comment for the process.
- **Description**: An optional description for the process.

##### Webhook Call for Process Definition

The webhook call used to register the process in Etendo will require the following body parameters:

```json
body_params = {
    "Prefix": "COPDEV",
    "SearchKey": "COPDEV_ActualizarDescripciónPedido",
    "ProcessName": "ActualizarDescripciónPedidos",
    "HelpComment": "This process updates the description of associated orders.",
    "Description": "A process to update the description of the associated sales orders based on a text input.",
    "Parameters": [
        {
            "BD_NAME": "text_parameter",
            "NAME": "Description Text",
            "LENGTH": 255,
            "SEQNO": 10,
            "REFERENCE": "Text"
        }
    ],
    "JavaPackage": "com.etendoerp.copilot.devassistant"
}
```

This call registers the process in the system and attaches the necessary parameters.

##### Example Usage

Here's an example of how the assistant is used to create and register a process in Etendo:

###### User Request:
```
I want to create a button for a process in the "Sales Invoice" window. The button will allow users to update the description of associated sales orders with a text input. Here are the details:

- Java package: com.etendoerp.copilot.devassistant
- Module prefix: COPDEV
- Window: Sales Invoice
- Tab: Header
- Table: C_invoices
- Process name: UpdateOrderDescriptions
- Search key: COPDEV_UpdateOrderDescriptions

Please infer the necessary parameters.
```

###### Assistant Response:

The assistant will infer that the process needs a text parameter and will generate the following response:

```
To create your button and register the process, I have inferred the following:

Process Name: UpdateOrderDescriptions
Search Key: COPDEV_UpdateOrderDescriptions
Parameters:
- BD_NAME: "description_text"
- NAME: "Order Description"
- LENGTH: 255
- SEQNO: 10
- REFERENCE: Text

Your process definition has been saved successfully.
```

The process and the button will be automatically registered, and the user will be notified.

![ButtonProcess.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/ButtonProcess.png)

At this point we will have the Java class of the button created along with the registered process.

![ButtonProcess2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/ButtonProcess2.png)


##### Components

The Button Process Assistant is composed of the following tools:

- **ApiCallTool**:
    - This tool executes a call to an API and returns the response.

- **ReadFileTool**:
    - Reads JRXML files from the path provided by the user.

- **WriteFileTool**:
    - Saves reports to the specified path or rewrites files with the requested modifications.

##### Conclusion

The **Button Process Creation Assistant** greatly simplifies the task of creating buttons and registering process definitions in Etendo. By automating this workflow through webhooks, you can focus on core development tasks, trusting that the setup and configuration are handled quickly and accurately.

For further customization and development, refer to the official Etendo documentation and API specifications.

---
