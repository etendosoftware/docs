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

The **Print Provider** module connects Etendo with printing platforms, offering a unified solution for generating printables directly from different areas of the system.

It allows each organization to configure its print provider, manage and synchronize the catalog of available printers, administer print templates, and execute on-demand printing from specific windows.

!!! info
    This module includes by default the implementation of a specific print provider [Print Node](https://www.printnode.com/){target="_blank"}, and all configuration and usage examples are based on this provider. This service includes a free plan, although if you require large print volumes, you should consult the [service pricing](https://www.printnode.com/pricing){target="_blank"}.    


!!! tip
    In addition, this module enables the implementation of custom print providers, exposes reusable back-end services that can be consumed by different modules, and a public API for printing from custom developments. For more information, visit: [Print Provider - Developer Guide](../../../../../developer-guide/etendo-classic/bundles/platform/print-provider.md)


## Initial Setup

Before using the **Print Provider** module, an initial configuration must be completed to establish the connection between Etendo and the selected printing service.

The following example integrates the **PrintNode** service with Etendo. This provider is included with the module, but its use is optional.

Integration with PrintNode requires following the [official documentation](https://www.printnode.com/docs){target="_blank"}. In general terms, you must create an account, install the management software on the device responsible for printing, and generate an API key that we will then use from Etendo to connect to the service.

This process includes:

- [x] Create **PrintNode** account and get the **API key**.
- [x] Install the **provider settings** and **print templates** in Etendo.
- [x] Configure **provider access**.
- [x] Searching for and synchronizing available printers. 
 
Once these steps are complete, the system will be ready to execute prints centrally and securely.


### Install Provider and Print Template Dataset

:material-menu: `Application`>`General Setup` > `Enterprise Model` > `Enterprise Module Management`

Open the **Enterprise Module Management** window and install the **Etendo Print Provider** reference data included in the module; this will set up the configurations with the PrintNode provider and the sample print templates.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/install-dataset.png)

### Print Providers

:material-menu: `General Setup` > `Print Provider Configuration` > `Print Providers`

This window is used to register print providers. In this case, the **PrintNode** provider configuration is already created with the installation of the data set.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/print-provider-window.png)

Here, general information such as **Search Key** and **Name** is displayed. It also includes the specific **Provider Implementation** field that refers to the record created in the Provider Implementation window. For more information on how to create a print provider, visit [Print Provider - Developer Guide](../../../../../developer-guide/etendo-classic/bundles/platform/print-provider.md)


#### Provider Params

This tab defines the configuration values required for integration with a printing provider. This configuration is essential for the system to communicate correctly with your services.

The system allows the user to create any parameter that the printing provider requires, adapting to their needs. To add a new parameter, use the following fields:

   - **Search Key**: A unique name that identifies the parameter.
   - **Param Content**: The value or information required for the parameter.
   - **Description**: A brief explanation of the parameter's function.

In the **PrintNode** example, the **apiKey** parameter must be configured with the corresponding key to establish communication with the provider.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/api-key-param.png)

!!! info
    Each organization must register and maintain its own API key. Sharing credentials between companies is not recommended, as it would affect traceability and security.


### Check and Register Printers

:material-menu: `General Setup` > `Print Provider Configuration` > `Check and Register Printers`

This process type window searches for and refreshes the list of printers available for a specific provider.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/check-and-register-printers.png)

- **Provider**: drop-down menu listing all printer providers that have been previously configured in the system. The field is always loaded with a default value, but the user has the option to modify it.

- **Done**: when you click this button, the system searches for available printers and updates the information according to the selected provider.

### Printers

:material-menu: `General Setup` > `Print Provider Configuration` > `Printers`

This window provides a view of the printers available by provider and allows you to update the list directly from the corresponding API, ensuring that you always work with active and synchronized devices.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/printers-window.png)

The printer registry is read-only, except for the **Active** and **Default** fields. Only one printer can be set as Default. If none is designated, the system selects one automatically.

The header displays general information such as **Search Key**, **Name**, and **Provider**, based on previously defined records. 

- **Refresh Print**: clicking this button refreshes the list of printers by consulting the endpoint defined in the Print Providers window. The printers obtained will depend on each provider and may be local or in the cloud.

### Print Templates

:material-menu: `General Setup` > `Print Provider Configuration` > `Print Templates`

This window manages print templates. These templates are associated with the related table from which the information to generate the printable will be obtained. By default, the module includes a template to generate a printable from the **Product** window, using the *m_product* table.

This configurations are automatically distributed and installed with the dataset.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/print-template-window.png)

Fields to note:

- **Table**: Associated table, from which information will be obtained to generate the printable document.
- **Name**: Print template name. 
- **Template Line**: Template location.


## Generate Printables

This **button** is a reusable component of the print provider module that can be configured in Etendo windows according to business needs. It allows multiple selection of records and, when pressed, opens a pop-up window where the user can optionally select a provider and printer, specify the number of copies, and choose whether to download the generated file.

!!!info 
    When selecting multiple records, the Number of Copies field indicates the number of copies of each selected record.

For example, the **Print Provider** module integrates this button into the **Product** window, generating a barcode printable for the product.

![generate-printable](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/generate-printable.png)

The pop-up presents the following fields. Multiple record selection is allowed.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/generate-printable-popup.png)

   - **Provider**: (Optional) Select a previously configured print provider. When left empty, the system operates in **download-only mode**: it generates the document and downloads it as a PDF without sending it to any printer.
   - **Printers**: Only visible when a Provider is selected. Displays printers associated with the selected provider. Loads the default printer, if available.
   - **Number of Copies**: Only visible when a Provider is selected. Number of copies to be printed. In download-only mode this field is hidden and defaults to one copy.
   - **Download**: When set to **Yes**, the generated printable PDF file is also downloaded to the browser. This option is enabled by default and is always visible regardless of whether a provider is selected. In download-only mode (no provider selected), this field must remain set to **Yes**; otherwise, no action will be performed and a warning will be displayed.

### Download-only Mode

- If multiple records are selected, all generated labels are merged into a single PDF for download.
- If some records fail to generate, the successfully generated labels are still downloaded and a warning is displayed indicating how many failed.
- If all records fail to generate, an error message is shown.

!!! tip
    This mode is ideal for users who only need digital copies of their printables, for example to attach them to emails, archive them, or print them manually from a different device or application.

### Print & Download Mode

- If the print job is sent successfully, a success message is displayed with the print job ID.
- If the print job fails but the label was generated, the PDF is still available for download (when Download is enabled) and a warning is shown.
- If all print jobs fail and no labels were retained, an error message is displayed.

!!! Warning
    The Print Providers module acts as a bridge between Etendo and the printer. Printer operational issues, such as low paper, low ink, or network connectivity problems, are not managed by this system.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/send-impresion.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/barcode.png)
---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.