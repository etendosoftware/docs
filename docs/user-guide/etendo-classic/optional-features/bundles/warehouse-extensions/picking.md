---
title: Warehouse Extensions Bundle
tags: 
    - Picking
    - Lists
    - Pick shipments
    - Products
    - Warehouse
    - Stock

---

# Picking


:octicons-package-16: Javapackage: `org.openbravo.warehouse.pickinglist`

:octicons-package-16: Javapackage: `org.openbravo.warehouse.structure`

## Overview

This section describes the Etendo Picking module included in the Warehouse Extensions bundle.

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}.  For more information about the available versions, core compatibility and new features, visit [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

This module implements and enhances the management of the **picking operations** within a warehouse. To manage and deliver the picking lists the module makes intensive use of 2 core features that must be enabled:

- [Stock reservations](../../../basic-features/warehouse-management/transactions.md#stock-reservation): When picking lists are created the products included in them are reserved. This means that no other picking list or any other process can use those products.

- [Document status project](): With this feature the user can easily know whether a sales order is pending to be delivered or not.

In Etendo there are 2 types of picking lists available: 

- **Direct Picking List to Customer**: **Outbound picking** is a process within warehouse management that involves the preparation and movement of products from their storage bins in the warehouse to a **specific outbound location** for subsequent packaging and shipment to the customer. Outbound picking is a type of pick list that is used to move products included in a sales order from storage bins within the warehouse to a predefined outbound storage bin. 

- **Outbound Picking Lists**: **Direct Picking List to Customer** is a process where products are shipped without going through an **intermediate outbound bin**.

## Configuration

In order to generate picking lists, some configuration is needed:

- **Document type**: The Picking list document type must be defined for each organization.
The module provides a dataset with basic document types that can be applied. Go to [Enterprise module management](../../../basic-features/general-setup/enterprise-model.md#enterprise-module-management) and apply the **Warehouse Picking List dataset** for each organization using Picking Lists. Once it is applied, the document types are created.

![picking1](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking1.png)


The dataset adds two new document types, with their own Document Sequences which will apply the following on each organization:

**Picking List**: Used for **Direct Picking List to Customer** picking list type. Picking List using this document type creates the shipments from the picking location. When they are completed the Goods Shipment is completed.

**Picking List outbound**: Used for **Outbound Picking List**, therefore **Use Outbound location** flag is set as **Yes** by default. This means that a Goods Movement needs to be created to move the goods from goods' storage bin to outbound storage bin. In this case, a storage bin of the warehouse needs to be defined as **Outbound**.

 - Generate Shipment on PL Completion flag if check generates Goods Shipments if Picking List is completed. A Goods Shipment document type needs to be selected in the field **Shipment for Picking**.

**Grouping Pick List**: Using Outbound location and the **Is Grouping Picking List** flag checked. This document type is used when grouping different picking list in one list.

!!! note
    These document types can be modified or new ones created manually. For example, if it is not desired to generate the Goods Shipment when they are completed or to modify the document sequences format.


- **Warehouse Outbound Location**: When using Outbound Picking List it is needed to configure the **outbound locations on each warehouse** that ships goods to customers. In **Warehouse and Storage Bins** window, select the warehouse and in the Storage Bin tab create or select the storage bin that represents the outbound location of that warehouse. Fill the type field selecting Outbound.

![picking4](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking4.png)

- **Picking List Auto Close Preference**: When using Outbound Picking List, in order to set automatically Picking List status from All Confirmed to Closed, a preference Picking List Auto Close with default value N is available. Users could enable this preference to automatically close picking when all lines are confirmed.

**Reservations Preference**: A preference needs to be configured in order to enable Stock Reservations feature.
As Client Admin, go to the [Preference window](../../../basic-features/general-setup/application.md#preference) and create a new one as shown below:

![picking2](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking2.png)


## Warehouse Picking List

**Picking Lists** can be created manually from the **Warehouse Picking List** window and/ or generated by the **Generate Picking List button** available in the [Sales Order](../../../basic-features/sales-management/transactions.md#sales-order) window. 

From the Warehouse Picking List window, only outbound picking lists can be generated. 

![picking5](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking5.png)

Fields to note: 

- Organization:
- Document No.: 
- Document Type:
- Outbound Storage Bin: It is necessary to set up an outbound storage bin in each warehouse that ships. This bin is defined in the **Warehouse and Storage Bins** window by selecting a bin with the type **Outbound**.
- Document Date:
- Description:
- Date printed:
- User/contact: 

!! info
    When an outbound picking list is generated, Goods Movements are created in draft status to move the products from the storage bins to the outbound bin.

!! info
    Products included in the outbound picking list are automatically reserved, ensuring that they cannot be used by other processes or picking lists.



In both cases the user has to select the Sales Orders to be included in the Picking List. The sales order needs to be **Booked and pending to be shipped**, that is, the delivery status must be below 100%.

The module adds a flag **In Picking List** in the Sales Order Header. This is checked when one of the lines of the sales order is present in a Picking List that is not closed. Using this flag and the Delivery Status and Delivery Date fields, it is possible to filter the Sales Order window to identify the Sales Orders needed to be included in a Picking List.

!!!info
    The module does not support the creation of Picking List for the same Sales Order for multiple Warehouses. Since the Sales Order has already a Warehouse assigned in the header, the Picking List will be created against this Warehouse only.


The flow to verify and process a picking list is:

- The picking list is in draft status.
- The warehouse manager prints the document. The date printed field is updated.
- The warehouse worker picks the items.
- If there are issues (not enough stock, items in different locators, etc.) prior to validating the picking list the warehouse manager edits/updates the corresponding lines.
- The warehouse manager validates the document and processes it.

Document no: The document number is usually automatically generated by the system and determined by the document type of the document.

Status: There are different status: Completed, draft and cancelled.

Document type: The Document Type determines document sequence and processing rules.

Document date: The date when the document was created.

Description: A description is limited to 255 characters.

Date printed: Indicates the Date that a document was printed.

VA 


### Buttons

- **Generate Picking List** button from the Sales Order window supports multiple selection and is visible when all selected orders are **booked and they are not completely shipped**. 

When the button is clicked a new window is opened. The first field to be filled is the Picking List type. Based on the selected type additional fields need to be set.
When a Sales Order line is included in a Picking List it must have a related reservation. The stock reserved is the one used in the Picking List. The processes that generate the Picking Lists automatically create the reservations if the Sales Order Line does not have one.

When **Direct Picking List to Customer type** is selected the process generates a Good Shipment in **Draft status** for each selected Sales Order. The Picking Lists are generated also in Draft status using a Document Type that has the Use Outbound Location flag unchecked.

The generated Picking Lists can be grouped using the Grouping Criteria field on Generate Picking List process window. 

The available options are:

- **Not Group** (default option): A Picking List is generated for each Sales Order selected.

- **Group by Business partner**: The picking lists are grouped by Sales Order's Business Partner and Organization. One Picking List is created for each customer and organization.

- **Group by Organization**: The picking lists are grouped by Sales Order's Organization. One Picking List is created for each organization.

The default Grouping Criteria can be configured using a preference:

- Name of the preference: Group Picking List

- Values:

        - Not Group: NG
        - Group by Business partner: GBP
        - Group by Organization: GO

!!!info
    If there is no stock for at least one of the products a message is shown telling that a partial Picking List is created. Reservation, picking list and good shipment are created with the available stock.


!!!info
    If none of the products has stock, no picking list, no good shipment and no reservation is created.And an error message is shown.


- **Process**: The selected picking list and its associated good shipment are processed.

- **Cancel**: The associated goods shipment and the picking list header are deleted. Except when the lines are in a Goods Shipment that is processed. Those lines, its processed goods shipment and picking list header are not deleted. In that case, the status of the picking list is set as Canceled.

- **Validate**: When the warehouse worker has picked all the items, the manager can verify them using this process.
The button opens a window showing all the items, for each one the **Qty Verified** field has to be set . There are several ways to do it:

        - Using a bar-code reader scanner. If a product with that bar-code exists in the grid it increases the quantity by 1 unit.

        - Manually changing the quantity in the line.

        - Typing the bar-code and pressing Validate Barcode. If a product with that bar-code exists, it increases the Qty Verified by the quantity set in the Quantity field.

!!!note
    When the Qty Verified is the Quantity, the Qty Pending is zero and the line is marked as verified (green color). When all the lines are verified, the picking list can be processed. It also processes the related Good Shipments.

- **Edit Lines**: A window is opened in order to be able to update the movement quantity.

Lines can **only be edited** by pressing the Edit Lines button. There it is possible to select different storage bins and modify the quantity that is going to move from each of the storage bins. When updating the movement quantity there are some conditions to fulfill:


        - The sum of Quantity cannot be higher than ordered quantity.

        - The Quantity cannot be higher than Available Quantity in the storage bin.

        - Once the quantities are modified, the Done button needs to be pressed in order to save the changes and update the reservation quantities of each storage bin.

## Sales Order for Picking 

The Sales Order for Picking window allows **filtering from all the sales orders** that are in the system which are ready for picking.

The sales orders must be:

- Completed

- Have the box Exclude from Picking List unchecked

When the sales orders are created, the Reservation Status is Not  Reserved. 

![picking3](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking3.png)

!!!info
    Once the picking process is complete, the user may continue with the packing process. 
    
    For more information visit: [packing](../../bundles/warehouse-extensions/packing.md)

