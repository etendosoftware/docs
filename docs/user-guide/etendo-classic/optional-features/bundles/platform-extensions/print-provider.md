---
title: Print Provider
tags:
    - Warehouse Management
    - Print Provider
    - Print
    - Stock
    - PrintNode
---

# Print Provider
:octicons-package-16: Javapackage: `com.etendoerp.print.provider`

## Overview
The **Print Provider** module connects Etendo ERP with printing platforms, offering a unified solution for creating and printing barcode labels directly from different areas of the system.

It allows each organization to configure its print provider credentials, manage and synchronize the catalog of available printers, administer print templates, and execute on-demand printing from specific windows.

!!! info
    Each organization must register and maintain its own API key. Sharing credentials between companies is not recommended, as it would affect traceability and security.

The system offers a simple one-click printing workflow, in which the user selects the printer and template, and the ERP generates the label in the corresponding format (PDF, PNG, or ZPL) and sends it directly to the print provider for immediate printing.

In addition, it exposes reusable backend services that can be consumed by different modules, including real-time barcode validation for GS1/EAN codes and a public API for printing from custom developments.

## Initial Setup

To start using this module correctly, the following installation and configuration steps must be completed:

- [x] **Integrating PrintNode with Etendo**

The system allows integration with different print providers. PrintNode is presented as an example of integration, but its use is not mandatory. However, it is essential that at least one print provider be configured to ensure the proper functioning of the print module within the system.

Below are the steps required to integrate PrintNode with Etendo, which will allow administrators to configure and connect printers within the platform.

1. Go to the PrintNode website: Go to the official PrintNode website: https://www.printnode.com

2. Create an account on PrintNode: If you do not have an account, register with PrintNode. Complete the required information to create a new user account. 

3. Download the installation file: Once registration is complete, download the file corresponding to your operating system (Windows, macOS, Linux, etc.) from the PrintNode download page.

4. Install the downloaded file: Run the downloaded file to start the installation process. Follow the wizard's instructions until the installation is complete.

5. Log in to PrintNode: Once the application is installed, open it and log in with the credentials used during registration (username and password).

6. Perform a test print (optional): Optionally, perform a test print to verify that the printer is configured correctly. You can also fill in your personal details in the corresponding section of the application.

7. Select the appropriate version: PrintNode offers different versions of the service. If a free option is required, the free version can be used, which is limited to 50 prints per month and a single connected device. For companies that need a higher volume of prints or devices, it is necessary to purchase a paid plan.

8. Generate an API Key in PrintNode: Generate an API Key by following these steps

    - Access the API Keys menu within the PrintNode platform.
    - Enter the password to continue with the creation of the API key.
    - Assign a name to the API key.
    - Click the Create button to generate the key.

9. Upload the API Key to Etendo: Once the API Key has been generated, it must be uploaded to Etendo to complete the integration

    - Go to the Print Providers window in Etendo.
    - In the Provider Params section, locate the Param Content field.
    - Copy and paste the generated API Key into this field and save the changes.


## Workflow

The process begins with the initial configuration, carried out by the system administrator, who accesses the **Provider Implementations** window for API key management and saves an encrypted API key from the print provider for each organization, ensuring that each company uses its own account, with the key masked for security. From this window, the administrator registers any external print provider, such as PrintNode, CUPS, or Labelary, configuring credentials, endpoint URLs, and associating the implementation that complies with the PrintProviderStrategy contract.

Before entering the **Printers** window, go to the **Check and Register Printers** menu to search for active printers from the desired provider.
The administrator can then view the printers by provider and launch an update process to synchronize the printer list from the provider API, ensuring that all active printers are reflected in Etendo. In addition, there is a registry of print templates in Etendo that allows administrators to associate one or more Jasper templates with any ERP table without the need for code.

Once the system has been configured, users can print labels from relevant windows, depending on the module being used. For example, with the warehouse module, labels can be printed from windows such as Product, Packing, or Locator by clicking the **Print Label** button.Clicking this button opens a pop-up window where the user can select the printing provider and the desired printer from the synchronized list. If there is a printer marked as Default, it will load automatically. Upon confirmation, the backend generates the label in PDF, PNG, or ZPL format and sends the job to the print provider via its API, providing the operator with immediate feedback on the success or failure of the process.


## Provider Implementation Window

:material-menu: `General Setup` > `Print Provider Configuration` > `Provider Implementation`

Allows to register third-party print providers such as PrintNode. Here you can configure credentials, endpoint URLs, and the specific Java implementation that complies with the PrintProviderStrategy contract. Each organization can maintain its own print providers. Only users with the System Administrator (Sys) role can access this window and modify the mappings.

!!! note
    Access to this window is restricted to users with the System Administrator (Sys) role. Operational users will not be able to modify these settings.

### Header

- Module: Indicates the module used by the Print Provider module.
- Name: Descriptive name of the provider.
- Java Implementation: Path to the Java file where the provider implementation is located. This must comply with the established contract, defining how printers are displayed, how the printout is generated, and how it is sent to the printer.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/provider-implementation-window-1.png)


## Print Providers Window

:material-menu: `General Setup` > `Print Provider Configuration` > `Print Providers`

This window is used to register a provider, taking the information from the record created in the Provider Implementation window. From here, provider data management is centralized, ensuring consistency with the defined technical configuration.

### Header

The Header displays general information such as Search Key and Name. It also includes the specific Provider Implementation field that refers to the record created in the Provider Implementation window.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/print-provider-window-1.png)

### Tab

Provider Params: This tab is designed to set the configuration values necessary for integration with a printing provider. This configuration is essential for the system to communicate correctly with your services.

The system allows you to create any parameter that the printing provider requires, adapting to their needs. To add a new parameter, use the following fields:

   - Search Key: A unique name that identifies the parameter.
   - Param Content: The value or information required for the parameter.
   - Description: A brief explanation of the parameter's function.

In the PrintNode example, the parameters that need to be configured are:

   - apikey: value provided by the printing provider.
   - printersurl: path to access the provider's printers.
   - printjoburl: path used to send print jobs.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/print-provider-tab-1.png)

## Check and Register Printers Window

:material-menu: `General Setup` > `Print Provider Configuration` > `Check and Register Printers`

This window allows you to search and refresh the list of printers enabled for a specific provider.

### Header

The Header displays the Provider field as a drop-down menu listing all printer providers that have been previously configured in the system. The field is always loaded with a default value, but the user has the option to modify it.

### Button
Done: When you click, the system searches for available printers and updates the information according to the selected provider.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/check-and-register-printers-1.png)

## Printers Window

:material-menu: `General Setup` > `Print Provider Configuration` > `Printers`

This window provides a view of the printers available by provider and allows you to update the list directly from the corresponding API, ensuring that you always work with active and synchronized devices.

The printer registry is read-only, with the exception of the **Active** and **Default** fields, which are editable. Only one printer marked as Default is allowed but if no printer is designated as such, the system will automatically select one.

When an ERP module uses the printing functionality, it typically incorporates a set of configurations that include the dataset, APIs, and addresses needed to send documents to the printing provider, along with the contract and additional integration parameters.

### Header

The Header displays general information such as Search Key, Name, and Provider, based on previously defined records. 

### Button

- Refresh Print: refreshes the list of printers by consulting the endpoint defined in the Print Providers window. The printers obtained will depend on each provider and may be local or in the cloud.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/printers-window-1.png)


## Print Templates Window

:material-menu: `General Setup` > `Print Provider Configuration` > `Print Templates`

It allows you to manage print templates and, optionally, link a set of them to a specific supplier. This is particularly useful as different suppliers may require different formats (e.g., ZPL or PDF) or specific templates. The information in this window is loaded through the dataset of the module that uses this functionality.

### Header

The main fields are defined in the Header:

- Table: associated reference table.
- Name: name of the template. 

### Tab

- Template Line: ubicación donde se encuentra alojada la plantilla.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/print-templates-window-1.png)

Example of Locator Label Printing

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/locator-label-example-1.png){width=300}

## Print Label Buttom

This button is a reusable component of the print module that can be configured in a specific ERP window according to business needs. It allows multiple selection of records to be printed, and when the button is pressed, a pop-up window opens allowing the supplier, desired printer, and number of copies to be selected. Once the selection is confirmed, the system generates the label according to the corresponding template and sends the print job to the configured supplier, receiving instant feedback on success or failure.

When selecting multiple records to print, the Number of Copies field indicates the number of copies of each selected record. That is, if I select 2 records and enter 4 in the number of copies field, I will get 4 printouts of each record.

As an example of use, the Warehouse module integrates this button into the **Product**, **Packing**, and **Warehouse and Storage Bin** windows. In this context, barcode validation services are also reused, allowing specific attributes of GS1/EAN codes to be verified in real time, facilitating the identification of errors before printing.
![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/product-window-1.png)

The **pop-up** allows you to select a previously configured print provider, assign the corresponding printer from the list of available devices, and specify the number of copies. Multiple selections are allowed.

   - Provider: Select the previously configured print provider.
   - Printers: Only displays printers associated with the selected provider. Loads the default printer, if available.
   - Number of Copies: Number of copies to be printed.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/print-provider/print-label-popup-1.png)

!!! Important
    The Print Providers module acts as a bridge between the ERP and the printer. It is important to note that printer operational issues, such as low paper, low ink, or network connectivity problems, cannot be managed through this system.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.