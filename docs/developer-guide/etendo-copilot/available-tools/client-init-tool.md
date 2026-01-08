---
tags:
  - Copilot
  - Client Initialization
  - Client
  - Setup
---

# Client Initial Setup Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.devassistant`

## Overview

The **ClientInitTool** assists with initializing a new client in the Etendo system. It interactively collects all required information, invokes the backend function to provision the client and its administrator, and validates successful creation.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool automates the **client provisioning** process in Etendo by:

- **Receiving Parameters**
    
    - Accepts an input object with:
        
        - `client_name` (string)
        - `client_username` (string)
        - `password` (string)
        - `confirm_password` (string)
        - `currency` (string)
        - `sysadmin_user` (string or null)
        - `sysadmin_password` (string or null)
        - `remote_host` (string or null)

- **Creating the Client**

    - Validates matching passwords.  
    - Calls the `ClientInitTool` function to create the client environment and administrator account, using inferred host and credentials if not supplied.

- **Returning the Result**

    - Returns a JSON response indicating success or failure.  
    - On success: includes a confirmation message, the new client ID, and admin username.

## Usage Example

### Provisioning a new client

**Input**
```json
{
  "client_name": "ACME Corp",
  "client_username": "acmeadmin",
  "password": "Secret123!",
  "confirm_password": "Secret123!",
  "currency": "USD"
}
```

**Output**
```json title="Output Json"
{
  "status": "success",
  "client_id": "12345",
  "admin_username": "acmeadmin",
  "message": "Client 'ACME Corp' initialized successfully."
}
```

!!!note
    After successful creation, instruct the user to log in with the newly created administrator credentials, configure wizard access for the client, and proceed with organization setup.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
