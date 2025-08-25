---
tags:
    - Copilot
    - Jasper Reports
    - Application Dictionary
    - Reporting
---

# Jasper Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.devassistant`

## Overview

The Jasper Tool allows developers to create process definitions for **Jasper Reports** directly into the **Etendo Application Dictionary**. It simplifies the integration of reporting capabilities by automating the configuration of key attributes and parameters needed for Jasper-based processes.

!!!info
    This tool is especially useful when automating or configuring reports as part of module installation or deployment scripts.

## Functionality

This tool automates the creation of **Process Definitions** for Jasper reports in Etendo. It uses the provided metadata (search key, report path, parameters, etc.) and sends the corresponding API request to Etendo to register the new report process.

### Key Capabilities:

- Adds a new Jasper report entry to the Application Dictionary.
- Supports semicolon-delimited parameter strings for easy batch configuration.
- Automatically formats the search key and trims the report path.
- Uses a webhook to register the process definition.

### Parameters

| Name            | Type   | Description |
|-----------------|--------|-------------|
| `i_prefix`      | string | Prefix of the module in the database. |
| `i_searchkey`   | string | Search key of the process definition. |
| `i_report_name` | string | User-friendly name of the report. |
| `i_help_comment`| string | Optional help comment for the report. |
| `i_description` | string | Optional report description. |
| `i_parameters`  | string | Semicolon-separated list of parameters using format: `BD_NAME-NAME-LENGTH-SEQNO-REFERENCE`. |
| `i_report_path` | string | Path to the stored report, truncated after `/web/` for internal reference. |

## Usage Example

You want to register a Jasper report named `Sales Overview` with the following data:

- Prefix: `SALES`
- Search Key: `Overview`
- Parameters:  
  ```
  C_BPARTNER_ID-Business Partner-32-10-30;DATEFROM-Start Date-10-20-15;DATETO-End Date-10-30-15
  ```
- Report Path: `/opt/etendo/modules/com.etendoerp.sales/web/jasper/sales_overview.jrxml`

```json title="Input"
{
  "i_prefix": "SALES",
  "i_searchkey": "Overview",
  "i_report_name": "Sales Overview",
  "i_help_comment": "Generates a report for all sales per customer.",
  "i_description": "This report provides summarized sales per partner.",
  "i_parameters": "C_BPARTNER_ID-Business Partner-32-10-30;DATEFROM-Start Date-10-20-15;DATETO-End Date-10-30-15",
  "i_report_path": "/opt/etendo/modules/com.etendoerp.sales/web/jasper/sales_overview.jrxml"
}
```

## Result

The tool will:

- Format the search key to `SALES_Overview`
- Parse and structure the provided parameters
- Truncate the path to: `web/jasper/sales_overview.jrxml`
- Call the webhook `ProcessDefinitionJasper` with the processed payload

!!!note
    Ensure that the provided path starts with `/web/` at some point so it can be correctly truncated for Etendo.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
