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

- **Outbound Picking** is a process within warehouse management that involves the preparation and movement of products from their storage bins in the warehouse to a **specific outbound location** for subsequent packaging and shipment to the customer. Outbound picking is a type of pick list that is used to move products included in a sales order from storage bins within the warehouse to a predefined outbound storage bin. 

- **Direct Picking List to Customer** is a process where products are shipped without going through an **intermediate outbound bin**.

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

**Picking Lists** can be created manually from the **Warehouse Picking List** window and/ or generated by the **Generate Picking List button** available in the [Sales Order](../../../basic-features/sales-management/transactions.md#sales-order) window. In both cases the user has to select the Sales Orders to be included in the Picking List. The sales order needs to be **Booked and pending to be shipped**, that is, the delivery status must be below 100%.

!!!info
    From the Warehouse Picking List window, only outbound picking lists can be generated. 


![picking5](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking5.png)

Fields to note: 

- Organization: an organization is a unit of your client or legal entity.
- Document No.: picking identification number is generated automatically.
- Document Type: it determines document sequence and processing rules.
- Outbound Storage Bin: it is necessary to set up an outbound storage bin in each warehouse that ships. This bin is defined in the **Warehouse and Storage Bins** window by selecting a bin with the type **Outbound**.
- Document Date: date when the Picking List is done and is expected to be completed.
- Description: an optional description limited to 255 characters.
- Date printed: indicates the Date that a document was printed. 
- User/contact: the User identifies a unique user in the system. This could be an internal user or a business partner contact. 


!!! info
    When an outbound picking list is generated, Goods Movements are created in draft status to move the products from the storage bins to the outbound bin.

!!! info
    Products included in the outbound picking list are automatically reserved, ensuring that they cannot be used by other processes or picking lists.

Once the header is manually created click on the Select Sales Orders button. This opens a window with a grid containing all the Sales Orders pending to be delivered that are not on an open Picking List. The sales orders that are shown are filtered by the warehouse of the outbound bin defined in the header of the picking list.

It could happen that a sales order has items reserved in a warehouse **different than the warehouse defined in its header (due to definition of "qty on hand" per organization and priorities). In that case the picking list will try to re-allocated items from that warehouse to the warehouse of the outbound bin. If there is no way to perform this action the system will throw an error.

!!!note
    The system assumes that picking bins (from where you get the items) and the outbound bin must belong to the same warehouse. That's the reason why the system always try to reallocated items in the above scenario and also filters sales orders based on the warehouse of the outbound bin.

From the **Sales Order** window, it is possible to select multiple orders which must be booked and they are not completely shipped. Using this process **both type of Picking Lists can be created**.


The module adds a flag **In Picking List** in the Sales Order Header. This is checked when one of the lines of the sales order is present in a Picking List that is not closed. Using this flag and the Delivery Status and Delivery Date fields, it is possible to filter the Sales Order window to identify the Sales Orders needed to be included in a Picking List.

!!!info
    The module does not support the creation of Picking List for the same Sales Order for multiple Warehouses. Since the Sales Order has already a Warehouse assigned in the header, the Picking List will be created against this Warehouse only.

When a Sales Order line is included in a Picking List it must have a related reservation. The stock reserved is the used in the Picking List. The processes that generate the Picking Lists automatically create the reservations if the Sales Order Line does not have one.

### Buttons

- **Generate Picking List**: When the button is clicked a new window is opened. The first field to be filled is the Picking List type. Based on the selected type additional fields need to be set.

    - **Direct Picking List to Customer type**: it means that the products are picked directly from the storage locations (e.g. shelves or bins) and prepared for shipment to the customer without moving them to a specific intermediate location within the warehouse. When selected, the process generates a Goods Shipment in **Draft status** for each selected Sales Order. The Picking Lists are generated also in Draft status using a Document Type that has the Use Outbound Location flag unchecked.

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

    ![picking.6](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking6.png)

    !!!info
        If there is no stock for at least one of the products a message is shown telling that a partial Picking List is created. Reservation, picking list and good shipment are created with the available stock.


    !!!info
        If none of the products has stock, no picking list, no good shipment and no reservation is created.And an error message is shown.


    - **Outbound Picking List**:

##### Buttons from the Warehouse Picking List window

- **Assign**: This button assigns the selected picking list to the warehouse agent chosen in the popup window. 

- **Process**: The selected picking list and its associated good shipment are processed.

- **Cancel**: The associated goods shipment and the picking list header are deleted. Except the lines is in a good shipment that is processed. Those lines, its processed goods shipment and picking list header are not deleted. In that case, the status of the picking list is set as Canceled.

- **Validate**: When the warehouse worker has picked all the items the manager can verify them using this process.

    The button opens a window showing all the items, for each one it has to be set the Qty Verified field. There are several ways to do it:

    - Using a bar-code reader scanner. If a product with that bar-code exists in the grid it increases the quantity by 1 unit.
    - Manually changing the quantity in the line.
    - Typing the bar-code and pressing Validate Barcode. If a product with that bar-code exists, it increases the Qty Verified by the quantity set in the Quantity field.

    !!! info
        When the Qty Verified is the Quantity, the Qty Pending is zero and the line is marked as verified (green color). When all the lines are verified, the picking list can be processed. It also processes the related Good Shipments.

   ![picking7](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking7.png)


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

