---
tags:
    - Warehouse Management
    - Advanced
    - Inventory
    - Stock
    - Etendo Mobile
---

# Advanced Warehouse Management
:octicons-package-16: Javapackage: `com.etendoerp.advanced.warehouse.management`

## Overview

The Advanced Warehouse Management module extends the standard capabilities of Etendo to offer comprehensive, flexible, and automated inventory management, adding integration with mobile devices. Every action performed from the mobile application is automatically synchronized with Etendo, ensuring complete traceability and consistent updates in the corresponding system windows.

This module allows the user to:

- Manage inventory in multiple predefined and customized statuses.
- Make stock adjustments and physical inventories from mobile devices.
- Automate relocations and statuses with movement rules.
- Integrate traceability using barcodes, which can be scanned from the mobile app.

## Initial Setup

To start using this module correctly, the following installation and configuration steps must be completed:

-[x] Install the Warehouse Extensions Bundle.

-[x] Install the Etendo Mobile app.

-[x] Assign the mobile user role to the “Warehouse” SubApp.

-[x] Load the GS1 Barcode Configs barcode configuration DataSet.

-[x] Configure key parameters in Advanced Warehouse Configuration.

**Steps to follow:**

!!! info
    To be able to include this functionality, the Advanced Warehouse Management module of the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Warehouse Extensions - Release notes](../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

1. Install the mobile app on a device. Follow the instructions in [Getting Started - Etendo Mobile](../../../../etendo-mobile/getting-started.md)

2. Associate the Advanced Warehouse SubApp with the user's role so that they have access from the Etendo Mobile. SubApp configuration for roles:

    To allow access to the warehouse and inventory management subapp in Etendo Mobile, you need to configure the corresponding roles. Follow the steps described in Configure Roles and Dynamic SubApps to assign the subapp to the desired role.

    !!!Info
        This configuration ensures that only users with the appropriate role can access warehouse features from the mobile app.

3. Loading the GS1 Barcode Configs DataSet from the Enterprise Module Management window is required.

    VA

4. **Advanced Warehouse Configuration**

`Application` > `Warehouse Management` > `Setup` > `Advanced Warehouse Configuration`

Before using the module, in the Advanced Warehouse Configuration window, you must configure the key variables that define how inventory operations are managed for each organization.

VA
VA

Fields to note:

- **Organization**: allows you to manage which organization will apply the configuration.

- **Warehouse**: is a non-mandatory field that can be used to apply the configuration to a specific warehouse or to all warehouses in the organization.

- **Active**: is checked or unchecked to enable or disable the configuration.

Barcode Configuration section

- **Barcode algorithm**:

    - EAN 128 (Link to documentation - to create)

    - SimpleBarcode

- **Ai configuration**: (add concept) - Configured by default, it comes with the dataset. The value is...

- **Search Related Barcode**: checkbox, which allows you to search for the product by more than one barcode.

!!!Important
    It is mandatory to create a configuration for the organization you are working with. 

These configurations ensure that inventory adjustments, relocations, and barcode operations follow the logic defined by the organization.

## Master Data Configuration

### Creating Statuses from Etendo

`Application` > `Warehouse Management` > `Setup` > `Inventory Status`

Inventory statuses allow the user to classify and manage stock units according to their condition or operational availability. The system includes some predefined statuses (such as Blocked, Damaged, In Quality Control, etc.), but it is possible to create new custom statuses according to your needs.

!!!info
    For more information on How to setup inventory statuses, visit [Inventory Status](../../../../../developer-guide/etendo-classic/concepts/inventory-status.md)

CHECK THIS SECTION 

### Configuring Inventory Movement Rules in Etendo

`Application` > `Warehouse Management` > `Setup` > `Movement Rules Configuration`

Movement rules allow you to automate the relocation or status change of inventory based on the action being performed. The purpose of this functionality is to automate inventory movements when they change status, exclude certain locations from operations such as picking or reservations due to their status, avoid errors in product handling, manage special products (damaged, blocked, etc.), and automatically handle virtual locations when there is no defined destination.

A virtual storage bin is a location automatically generated by the system to correctly maintain inventory, even when no specific location has been defined for the status to which it is being moved. 

For example: If the “Available” status does not have an associated storage bin, and a user marks a product as “Damaged,” then the system creates a virtual location in which to deposit the affected inventory. This virtual location inherits the properties of the storage bin where the product was located and is associated exclusively with the new status (e.g., “Available”).

VA

This allows you to maintain inventory traceability and consistency, even if the team has not yet defined all physical locations. It also streamlines operations by avoiding errors or blockages when working with exceptional statuses.

VA

To define the movement rules mentioned above, you must enter the **Movement Rules Configuration** window in Etendo.

There you can select an **Organization**, define whether or not it is activated with the **Active** checkbox, which is selected by default. Select a Storage bin “from” in the **From Locator** field and “to” in the **To Locator** field, plus an inventory status in the **To State** field.

The application of these rules can be seen from two features of the mobile application:

- From the **Relocate** option, once you have selected the location defined in a rule, this will move the inventory to the new location and, according to the configured rule, change the inventory status.

- From the **Adjust** option, when you select the new status, this will update the status and, depending on the configured rule, move the inventory to the defined location.

VA

This creates a new record indicating:

- **From Locator**: source location

- **To Locator**: destination location

- **To State**: state to which the inventory will be transferred

!!!Note
    If the To State field is filled in first, the To Locator field will be limited to the Storage Bins that have that state assigned.

!!!Info
    Actions performed using movement rules impact both the mobile application and Etendo's Stock Report, reflecting the location.