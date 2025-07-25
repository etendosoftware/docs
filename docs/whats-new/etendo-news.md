---
title: Etendo News
tags:
  - Etendo News
  - New Features
  - Release Notes
  - Functional Documentation
  - Versions
---

![](../assets/whats-new/etendo-news/etendo-news-0.png)

#

## May 2025

### Etendo Classic

<div class="grid cards" markdown>

- :octicons-rocket-24: **New Etendo Classic Release: Version 25.1.x Now Available!**

    ---
    The latest version [25.1.x](./release-notes/etendo-classic/release-notes.md) of Etendo Classic is here! This release brings compatibility updates with **Java 17**, **PostgreSQL 16**, **Tomcat 9** and third-party dependencies, ensuring a modern and robust tech stack. All supported modules have been updated for full integration.  
    Want to know more? Check out the [developer updating guide](../developer-guide/etendo-classic/eveloper-changelog/apichanges.md).

    ---

    <iframe width="560" height="315" src="https://www.youtube.com/embed/OtHb45n2dgU?si=dttVeLQxnf97HGjN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


</div>

<div class="grid cards" markdown>

- :octicons-rocket-24: **New Shipment and Invoicing Statuses in Purchase Orders and Goods Receipts**

    ---  
    This release introduces improved visibility in procurement processes. In the [Purchase Order](../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order) window, the status bar now shows shipment and invoicing percentages. At the line level, you’ll see detailed quantities for what has been invoiced and shipped.  
    Similarly, the [Goods Receipt](../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#goods-receipts) window shows invoicing percentages at both header and line levels.

- :octicons-rocket-24: **Easily Exclude Promotions and Discounts with a Simple Checkbox**

    ---
    A new checkbox in the *More Information* section of [Sales Order](../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines_1) and [Sales Invoice](../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines_5) lines allows users to **cancel automatic discounts and promotions**. This gives you more control over pricing on a per-line basis.

- :octicons-rocket-24: **Improved Navigation in the Create Invoices from Orders Process**

    ---
    Now it’s easier to work with orders! The [Create Invoices from Orders](../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-invoices-from-orders) process includes improved navigation features that let you access filtered orders more efficiently.

- :octicons-rocket-24: **Enhanced Purchase Invoice Voiding with Supplier Reference**

    ---  
    When canceling a purchase invoice, Etendo creates a reverse document that now references the supplier’s cancellation document. The [invoice reactivation](../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#reactivate) process includes a new `Supplier Reference` field to ensure clear traceability and alignment.

</div>

## April 2025

### Etendo Classic

<div class="grid cards" markdown>

- :octicons-rocket-24: **Remember: You can simplify the calculation of commissions with Etendo Classic**

    ---

    With **Etendo Classic**, managing [sales commissions](../user-guide/etendo-classic/basic-features/sales-management/setup.md#commission) is streamlined and flexible. Commissions can be calculated based on sales orders or invoices, using diffrent criteria and filters such as quantities sold or amounts invoiced: 

    ![Commission Criteria](../assets/whats-new/etendo-news/commission-criteria.png)

    Once calculated, sales agent payments can be generated automatically. 
    You can configure commissions to apply to all invoices or only paid ones, and decide whether to include invoices without an assigned sales agent.
    <br>
    --- 

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vQGzo7cbCYQ?si=2zC3RQmYD1ImkoLo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>

### Copilot Extensions

<div class="grid cards" markdown>

- :material-robot: **Copilot supports multi-vendor models such as  OpenAI, Ollama, Anthropic, and Deepseek, also image input for compatible models**

    ---

    ![alt text](../assets/whats-new/etendo-news/multi-models-support.png)
    
    - In version [1.13.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, Etendo Copilot expands its capabilities by supporting multiple vendors, including:

        - **Anthropic**: Specializes in code generation, making it the best choice for code-related tasks.
        - **Deepseek**: A cost-effective alternative for generative tasks similar to OpenAI.
        - **Ollama (self-hosted models)**: Ideal for users running their own models on their infrastructure.

    - Additionally, images can now be processed directly by language models without requiring a separate tool for pre-processing.


</div>

## March 2025

### Etendo Mobile

<div class="grid cards" markdown>

- :material-share: **Receive and share files with Etendo Mobile**

    ---

    ![](../assets/whats-new/etendo-news/share-files-mobile.png)

    A new feature has been added to Etendo Mobile to streamline integration with external applications. With the new [Share files](../user-guide/etendo-mobile/) option, you can now receive files from outside apps and use them directly in subapplications like:

    - **Documents Manager**, where you can view files right in Etendo Mobile.
    - **Copilot**, where specialized agents can extract information from images, transform audios into sales orders, and much more.

    This feature improves data flow and efficiency across your platform.

    Try it now using the *Demo Try* button in the app, or download the latest version from the App Store or Play Store.

</div>

### Financial Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **Now in the advanced financial reports you can view accounting dimensions.**
    ---

    ![alt text](../assets/whats-new/etendo-news/financial-reports-advanced.png)

    In version [1.25.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) of the Financial Extensions bundle, improvements to advanced financial reporting are included.In this version, the [General Ledger Report Advanced](../user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/#general-ledger-report-advanced) and [Journal Entries Report Advanced](../user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/#journal-entries-report-advanced) will allow you to view and filter by the desired accounting dimensions.
    In addition, you can navigate to related entities in each report!

</div>

### Etendo Classic

<div class="grid cards" markdown>

- :octicons-rocket-24: **25.1 Release Candidate Now Available!**

    The new version [25.1](./release-notes/etendo-classic/release-notes.md) of Etendo Classic introduces the latest stack enhancements. While this version is currently in Release Candidate (RC) status, you can already explore the detailed [API changelog](../developer-guide/etendo-classic/developer-changelog/apichanges.md) to review the changes and improvements included in this release.

- :material-trending-up: **Fixed Issue**
    
    ---
    As of version [24.3.7](./release-notes/etendo-classic/release-notes.md), a bug affecting dropdown selectors in dimensional reports has been fixed. In environments running Etendo 24.3.6 or earlier, the first record in combo boxes was displayed incorrectly, showing a concatenation of all values instead of the correct individual value. This issue was caused by improper handling of `<option>` tags in HTML.

    The bug has been resolved in 24.3.7, and Etendo 24.4.0 or later was not affected, as the refactor to fix the issue was already included in that version. 
    
    *See more details in Issue [#629](https://github.com/etendosoftware/etendo_core/issues/629)*.

</div>

## February 2025

### Etendo ISO

<div class="grid cards" markdown>

- :material-trending-up: **Optimizations**
    
    ---
    As of version [24.4.3](https://etendo-appliances.s3.eu-west-1.amazonaws.com/etendo/iso/etendo-24Q4.3.iso), the Etendo ISO includes performance improvements with optimized memory and database settings to enhance system efficiency. *See more details in Issue [#573](https://github.com/etendosoftware/etendo_core/issues/573)*.

</div>

### Copilot Extensions

<div class="grid cards" markdown>

- :material-robot: **Now, you can clone agents in one click**

    ---

    ![copilot-clone.png](../assets/whats-new/etendo-news/copilot-clone.png)
    
    In version [1.12.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the functionality to [clone agents](../user-guide/etendo-copilot/setup-and-usage.md#buttons) and knowledge bases is added, allowing you to modify and customize the agents' wizards according to your needs.

</div>

<div class="grid cards" markdown>

-   :material-robot: **Improvements in agent knowledge bases**

    --- 

    In version [1.12.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, new capabilities are added:

    ![knowledge-base-files-news.png](../assets/whats-new/etendo-news/knowledge-base-files-news.png)

    For more info visit [Knowledge Base File](../user-guide/etendo-copilot/setup-and-usage.md#knowledge-base-file-window) windows documentation.

</div>

### Financial Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Enhanced asset management with accounting dimensions**

    ---

    ![dimension.png](../assets/whats-new/etendo-news/financial-dimension.png)

    In version [1.22.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) of the Financial Extensions bundle, with the [Accounting Dimensions Assets](../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#accounting-dimensions-assets) module improves asset management by allowing users to assign accounting dimensions to assets like Business Partner, Activity, and Cost Center among others. These dimensions transfer to amortization lines. Also, amortizations are now grouped by period (monthly or yearly), enhancing financial reporting accuracy and ensuring consistent asset depreciation tracking.

- :octicons-package-16: **Gain better control with the Not Posted Documents window**

    ---

    ![](../assets/whats-new/etendo-news/financial-not-posted.png)

    In version [1.22.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) of the Financial Extensions bundle, with the last version of [Bulk Posting](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md#not-posted-documents-window), the Not Posted Documents windows provides a comprehensive view of all completed financial transactions that have not yet been posted. This report ensures that no pending transactions are overlooked before closing an accounting period or running financial reports.

    Users can filter by date range and navigate directly to unposted documents, including journals, invoices, payments, and financial transactions, among others streamlining the posting process.

</div>


## January 2025

### Copilot Extensions 

<div class="grid cards" markdown>

- :material-robot: **You can now use multiple files in conversations with an agent**

    ---

    ![](../assets/whats-new/etendo-news/attach-multiple-files-copilot.png)

    In version [1.10.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, new functionalities have been added:

</div>

<div class="grid cards" markdown>

-   :material-robot: **[Upload multiple files](../user-guide/etendo-copilot/getting-started.md#attach-files)**
    
    ---
    
    It is now possible to attach multiple files at once in Etendo Copilot, optimizing document management and improving the user experience.

-   :octicons-package-16: **Automatic permissions management**
    
    ---

    When creating a new agent, the necessary permissions will be automatically generated for its execution in the current role, reducing friction in the configuration.

-   :octicons-package-16: **Optimized visualization**
    
    ---
    
    The agent window now shows the module to which each agent belongs, improving organization and navigation.

-  :material-tools: **Tool Pack: New tool to read Excel and CSV files** 
    
    ---
    
    [XLS Tool](../developer-guide/etendo-copilot/available-tools/xls-tool.md) has been added in the available Tools, allowing agents to read and process data directly from Excel or CSV files, facilitating automation and integration of structured information.

</div>


## December 2024

### Etendo Classic

<div class="grid cards" markdown>

- :octicons-rocket-24: **New Etendo Classic Release Available!**

    Version [24.4.0](./release-notes/etendo-classic/release-notes.md) of Etendo Classic has been released for the last quarter of the year. All packages have been updated to ensure integration with this new release.  In addition this release includes all bugs resolved in the quarter.

- **The document completion process allows the use of Credit Payment as a payment method again.** 

    From now on, the completion is again one record at a time and is added to the [Bulk Completion](../user-guide/etendo-classic/optional-features/bundles/essentials-extensions/bulk-completion.md) button by installing the Essential Extensions bundle.

</div>

### Essentials Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Managing documents has never been so fast and easy**

    ![](../assets/whats-new/etendo-news/bulk-completion.png)
    
    In version [1.7.0](./release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md) of the Essentials Extensions bundle, you can effortlessly manage multiple records with the [Bulk Completion](../user-guide/etendo-classic/optional-features/bundles/essentials-extensions/bulk-completion.md) feature. Select the records you want to complete, reactivate, or close, and process them all at once with a single click.
</div>


### Warehouse Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **More accurate automatic stock reservation**

    ![](../assets/whats-new/etendo-news/automatic-warehouse-reservation.png)

    In version [1.10.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) of the Warehouse Extensions bundle, with the [Automatic Warehouse Reservation](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation) module the stock reservations can be limited only to the warehouse specified in the order header. This way you can ensure that your orders always use the right warehouse.
</div>

### Financial Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Automated remittances: Simplify remittance management by automating the settlement and protest process.**

    ---

    ![](../assets/whats-new/etendo-news/automated-remittances.png)

    In version [1.21.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) of the Financial Extensions bundle, with the [Automated remittances](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md) module, when processing remittances, bank instructions are created and automatically settled with the current date. 

    The Protest Remittance button has also been added, making it possible to return receipts in collection remittances from a single place.

- :octicons-package-16: **Bank account and payment management allows for more automation**
    
    --- 

    ![](../assets/whats-new/etendo-news/advanced-bank-account.png )

    In version [1.21.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) of the Financial Extensions bundle, with the [Advanced Bank Account Management](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management.md) module, added the possibility to set a default bank account in the busines partner configuration, as well as to define bank accounts for each location. 
    The possibility to select the bank account when adding payments and even edit payment plans with the Modify Payment button has also been added.
</div>

### Copilot Extensions 

<div class="grid cards" markdown>

- :material-robot: **Copilot allows the use of multiple AI models from different suppliers.**
    
    ---

    In version [1.9.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, Multi-Model Assistant type was added, this agents extends the `Langchain` type with the particularity that it can be used with models from various suppliers such as Anthropic or Gemini, in addition to the existing OpenAI models.
    In addition, the AI Models window was added where the user can manage the models to be used by the different agents.
</div>

## November 2024

### Copilot Extensions

:material-robot: **New Etendo Copilot Release Available!**

New Copilot Extensions bundle version [1.8.0](./release-notes/etendo-copilot/bundles/release-notes.md) 

<div class="grid cards" markdown>
-  **Improve your Python Tools development with the Code Run agent**

    ---
    The [Code Run](../developer-guide/etendo-copilot/bundles/dev-assistant.md#code-run) agent combined with the [Docker Tool](../developer-guide/etendo-copilot/available-tools/docker-tool.md) introduces a safe and efficient way to run Python and Bash code inside isolated Docker containers. This tool revolutionizes the way coding tasks are handled. The wizard specializes in managing Docker containers to execute Python scripts, ensuring a reliable and isolated environment.

    Equipped with advanced capabilities, the agent prioritizes Python for troubleshooting, manages library installations dynamically, integrates Bash commands for flexible operations and handles file processing with precision. Whether you are troubleshooting, automating tasks or testing scripts, this tool ensures efficiency and security. Transform your development workflow with this powerful addition to Etendo.
</div>

## October 2024

### Copilot Extensions

:material-robot: **New Etendo Copilot Release Available!**

New Copilot Extensions bundle version [1.7.0](./release-notes/etendo-copilot/bundles/release-notes.md)  

<div class="grid cards" markdown>
-  **Boost Your Development Workflow with the New Dev Assistant!**

    ---
    The [Dev Assistant](../developer-guide/etendo-copilot/bundles/dev-assistant.md) module streamlines and accelerates your development workflow in Etendo Classic. With specialized agents, you can now easily create buttons, windows, tabs, tables, event controllers, Jasper reports, and background processes. 

    This agents are designed to enhance productivity and reduce complexity, enabling efficient management and construction of all components within Etendo. Take your development process to the next level!
</div>

<div class="grid cards" markdown>
-  **Copilot in Mobile: Try Copilot on Your Mobile Devices and Tablets!**

    ---
    The new [Etendo Copilot sub-application](../user-guide/etendo-copilot/bundles/overview.md#etendo-copilot-subapp) enables you to interact with AI-powered agents from anywhere. Now, you can attach files, access role-specific windows, and receive real-time, personalized assistance directly on your mobile or tablet. Enjoy seamless integration with all the familiar features of Etendo, right from your fingertips!

</div>

### Dependency Manager
:octicons-package-16: **Managing Etendo modules and dependencies has never been so easy**
![](../assets/whats-new/etendo-news/devassistant.png)

The [Dependency Manager](../developer-guide/etendo-classic/getting-started/installation/dependency-manager.md) module allows users to access all published packages in Etendo Software repositories directly from the Etendo Classic interface. With the Dependency Management window, you can browse available bundles, check version details and dependencies, and easily install new packages. The module also supports updating, removing, and modifying installed modules, giving you full control over your environment.


## September 2024

### Etendo Classic

:octicons-rocket-24: **New Etendo Classic Release Available!**

Version [24.3.0](./release-notes/etendo-classic/release-notes.md) of Etendo Classic has been released for the third quarter of the year. All packages have been updated to ensure integration with this new release.  In addition this release includes all bugs resolved in the quarter.


### Copilot Extensions

:material-robot: **New Etendo Copilot Release Available!**

New Copilot Extensions bundle version [1.5.0](./release-notes/etendo-copilot/bundles/release-notes.md)  

<div class="grid cards" markdown>
- **New Feature Update: Zip File Support for LangChain Agents**
    
    ![](../assets/whats-new/etendo-news/LangChain.png)

    We are excited to announce a new functionality in LangChain agents: the ability to upload `.zip` files directly into the knowledge base! These `.zip ` files can contain a variety of file formats, including `.txt`, `.pdf`, `.md`, `.py`, `.java`, and `.js`.
    This enhancement allows developers to train agents with example source code.
    Boost your agent’s capabilities with this powerful new feature!

</div>

## August 2024

### Copilot Extensions

[:material-robot: **New Etendo Copilot Release Available!**](../user-guide/etendo-copilot/getting-started.md): Boost Your Productivity

![](../assets/whats-new/etendo-news/copilot.png)

The newest version [1.4.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle brings the following key enhancements in Etendo Copilot:

<div class="grid cards" markdown>

-   **New Capabilities:**
    
    ---
    - **Database Queries:** Use system database queries as knowledge bases to automate tasks under specific conditions.
    -  **Copilot Stream:** Track in real-time which agent or tool is working.
    -  **Improved UX:** The chat now retains the last agent used for seamless interaction.

-   **Agents Updates:**
    
    ---
    -  **Langchain Agents:** Now manage local knowledge bases, keeping your data secure.
    -  **LangGraph Agents:** Manage a team of agents, delegating tasks efficiently. 
     
</div>

These updates make Etendo Copilot more powerful, secure, and user-friendly, driving efficiency to new heights.


### Platform Extensions



[:simple-docker: **Docker Management**](../developer-guide/etendo-classic/bundles/platform/docker-management.md)

![](../assets/whats-new/etendo-news/docker.gif){align=right width=400}

- In version [1.18.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) of the Platform Extensions bundle, the new **Docker Management** module has been introduced.
- This module simplifies the deployment of services by allowing you to configure the entire infrastructure your service requires using Etendo modules.
- PostgreSQL Database Service is included in the module, making service installation faster and easier than ever.

[:simple-apachetomcat: **Tomcat Dockerized Service**](../developer-guide/etendo-classic/bundles/platform/dockerized-tomcat-service.md)

- In version [1.18.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) of the Platform Extensions bundle, the new **Tomcat Dockerized Service** module has been introduced, which simplifies the installation of Etendo on any server.
- With this module, setting up Etendo becomes a quick and straightforward process, removing the complexities typically associated with server configuration. 



### Warehouse Extensions
[:octicons-package-16: **Product Operations**](../user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchase-invoice-validation.md)

![](../assets/whats-new/etendo-news/product-operation.png)

In the version [1.8.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) of the Warehouse Extensions bundle, the **Product Operations** functionality has been included. This module allows you to centralize and control all your product movements with Products Operations. View every transaction, from shipments and receipts to costs and location, in one place. Simplify analysis and get a clear view of your operations' performance.


## July 2024

### Copilot Extensions

<div class="grid cards" markdown>

-   [:material-tools: **Tool Pack**](../developer-guide/etendo-copilot/available-tools/overview.md)

    ---
    
    The Tool Pack module, available from version [1.3.1](./release-notes/etendo-copilot/bundles/release-notes.md) of the Etendo Copilot bundle, includes a collection of tools designed to enhance the capabilities of Etendo Copilot agents. This module enables functionalities such as file reading and writing, directory navigation, and email sending, thereby significantly expanding the operational scope of the agents.

-   [:material-tools: **OCR Tool**](../developer-guide/etendo-copilot/available-tools/ocr-tool.md)

    ---

    From version [1.3.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the possibility to add a parameter to the OCR Tool to specify and detail the analysis on images has been included, and Codbar tool reader has been added to the tool capable of reading barcodes on images.

-   [:material-robot: **Purchase Expert**](../user-guide/etendo-copilot/bundles/copilot-purchase-expert.md)
    
    ---   

    As of version [1.3.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot bundle, the [Attach File tool](../developer-guide/etendo-copilot/available-tools/attach-file-tool.md) was included, a tool capable of adding attachments to any record in Etendo.

-   [:material-robot: **Dev Assistant**](../developer-guide/etendo-copilot/bundles/dev-assistant.md)

    ---

    From version [1.1.0](./release-notes/etendo-copilot/bundles/release-notes.md) onwards, the [Reference Creator](../developer-guide/etendo-copilot/bundles/dev-assistant.md#reference-creator) agent was included, capable of creating list type references to be used in the development process.

</div>

:material-bug: **Fixed Issues**

In version [1.2.1](./release-notes/etendo-copilot/bundles/release-notes.md), Issue [#5](https://github.com/etendosoftware/com.etendoerp.copilot.extensions/issues/5){target="_blank"} which caused incorrect rendering of line breaks in code blocks, has been resolved.

### Financial Extensions

[:octicons-package-16: **VAT Regularization**](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/overview.md/#vat-regularization)

In version [1.16.1](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) of this bundle, the [VAT Regularization](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/overview.md/#vat-regularization) module has been included, which allows you to **easily adjust the accounts** to ensure that the **VAT balance is adjusted**.

---

## June 2024

### Etendo Classic

:octicons-rocket-24: **New Release Available!**

Etendo Classic version [24.2.0](./release-notes/etendo-classic/release-notes.md) has been released, corresponding to the second quarter of the year. All bundles have been updated to ensure seamless integration with this new version.

:material-bug: **Fixed Issues**

In version [24.1.8](./release-notes/etendo-classic/release-notes.md), Issue [#270](https://github.com/etendosoftware/etendo_core/issues/270){target="_blank"}, which caused **unexpected execution of callouts** in the **Sales Order** window, has been resolved.

### Copilot Extensions

:material-trending-up: **Optimizations**

Starting with version [1.2.0](./release-notes/etendo-copilot/bundles/release-notes.md) of this package, bugs have been fixed and stability improvements have been made to Copilot. This update also introduces visual improvements to the chat by making it possible to enter **text on more than one line**.

### Financial Extensions

[:octicons-package-16: **G/L Journal Clone**](../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md/#gl-journal-clone)

Starting with version [1.15.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) of this bundle, the GL Journal Clone module is included, which makes it possible to clone the Simple GL Journal.

---

## May 2024

### Copilot Extensions

[:material-robot: **SQL Expert**](../user-guide/etendo-copilot/bundles/sql-expert.md)

In the version [1.1.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the SQL Expert has been included.
With this agent, you will be allowed to **formulate questions** in natural language, and the system will automatically generate the necessary SQL query to return data in code or natural language.

---

## April 2024

### Copilot Extensions

[:material-robot: **Purchase Expert Agent**](../user-guide/etendo-copilot/bundles/overview.md#order-expert)

In the version [1.1.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the Purchase Expert Agent has been included.
Your purchase orders are made easier with the new Copilot agent. Interact via **text or by uploading images or PDFs** with the purchase order data, and the agent will automatically generate a draft.

### Spanish Localization

:material-trending-up: **Optimizations**

As of version [1.9.4](./release-notes/etendo-classic/bundles/localization-spain-extensions/release-notes.md) of this bundle, we have simplified maintenance by replacing the `org.openbravo.util.saaj.impl` and `org.openbravo.util.javax.xml.soap` module dependencies with the new Maven dependencies [Jakarta SOAP Implementation](https://mvnrepository.com/artifact/com.sun.xml.messaging.saaj/saaj-impl/1.5.3){target="_blank"} and [Jakarta SOAP with Attachments API](https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2){target="_blank"}.

To take advantage of these enhancements, when upgrading to version [1.9.4](./release-notes/etendo-classic/bundles/localization-spain-extensions/release-notes.md) or higher, be sure to manually remove the old modules from the `/modules` directory so that the new build will use the new dependencies.

---

## March 2024

### Etendo Classic

:material-trending-up: **Optimizations**

As of version [24.1.0](./release-notes/etendo-classic/release-notes.md), the support for [Tomcat 9](https://tomcat.apache.org/download-90.cgi){target="_blank"} has been updated.

### Copilot Extensions

[:material-tools: **OCR Tool**](../developer-guide/etendo-copilot/available-tools/ocr-tool.md)

In the version [1.0.0](./release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the OCR Tool has been included.
With this tool designed for **optical character recognition**, you will be able to extract text from images or PDF files.

### Procurement Extensions

[:octicons-package-16: **Purchase Invoice Validation**](../user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchase-invoice-validation.md)

In the version [1.0.0](./release-notes/etendo-classic/bundles/procurement-extensions/release-notes.md) of the Procurement Extensions bundle, the Purchase Invoice Validation functionality has been included. Now, you will be able to **avoid the duplication of purchase invoices** through established rules and automatic validations.

### Platform Extensions

:material-trending-up: **Optimizations**

As of version [1.13.2](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) of this bundle, the module dependency `org.openbravo.util.javax.xml.soap` has been removed as it was not needed for any module in this bundle. In case this dependency is needed for development, we recommend using the Maven dependency [Jakarta SOAP with Attachments API](https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2){target="_blank"}
