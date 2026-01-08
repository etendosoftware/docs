---
tags:
  - Copilot
  - Organization Initialization
  - Organization
  - Setup
---

# Organization Initial Setup Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.devassistant`

## Overview

The **OrgInitTool** assists with initializing or creating a new organization in the Etendo system. It interactively gathers all required information, invokes the backend function to provision the organization and its administrator, and validates successful creation.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).


## Functionality

This tool automates the **organization provisioning** process in Etendo by:

- **Receiving Parameters**
    - Accepts an input object with:
        - `org_name` (string)
        - `org_username` (string)
        - `password` (string)
        - `confirm_password` (string)
        - `client_admin_user` (string or null)
        - `client_admin_password` (string or null)
        - `remote_host` (string or null)

- **Creating the Organization**
    - Validates matching passwords.  
    - Calls the `OrgInitTool` function to:
        - Create the organization environment.
        - Set up the administrator account.

- **Returning the Result**
    - Returns a JSON response indicating success or failure.  
    - On success: includes a confirmation message, the new organization ID, and admin username.

## Usage Example

### Creating a new organization

**Input**
```json
{
  "org_name": "EventsCo",
  "org_username": "eventsadmin",
  "password": "Passw0rd!",
  "confirm_password": "Passw0rd!",
  "client_admin_user": "acmeadmin"
}
```

**Output**
```json title="Output Json"
{
  "status": "success",
  "org_id": "67890",
  "admin_username": "eventsadmin",
  "message": "Organization 'EventsCo' initialized successfully."
}
```

!!!note
    After successful creation, instruct the user to log in with the administrator credentials to continue setting up the organization.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
