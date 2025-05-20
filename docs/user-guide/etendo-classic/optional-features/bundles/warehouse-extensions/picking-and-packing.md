---
tags: 
    - Picking
    - Packing
    - Goods Shipment
    - Lists
    - Pick shipments
---

# Picking 

:octicons-package-16: Javapackage: `org.openbravo.warehouse.pickinglist`

## Overview

This section describes the Etendo Picking module included in the Warehouse Extensions bundle.

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}.For more information about the available versions, core compatibility and new features, visit [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

# Packing

:octicons-package-16: Javapackage: `org.openbravo.warehouse.packing`

## Overview

This section describes the Etendo Packing module included in the Warehouse Extensions bundle.

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}.For more information about the available versions, core compatibility and new features, visit [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

This module streamlines and enhances the management of **packing operations** within the warehouse. Once a goods shipment has been processed, the packing process begins. Packing is carried out based on each individual goods shipment document. For every product, the warehouse worker determines the appropriate handling unit (box) in which to pack the item. Only products classified as items are eligible for packing.

## Packing window

The packing process can be initiated from the **Goods Shipment** window and/or from the **Packing** window. From either window, the packing procedure will be the same as well as the information about packing shown through the Packing Box and Content tabs which are displayed in both windows.

If the process is initiated from the Goods Shipment window, it is possible to just do the packing for **one specific shipment**. When doing the packing through the Packing window, it is possible to select **more than one shipment to pack**, since several documents are grouped to be packed all at once or individually. 
Either way, one record is created in the Packing window. So, this is a centralized window where it is possible to check all packs done and complete the packing process. 
When the process is initiated from the Goods Shipment window, the document must have a status of **Completed**, and the **Packing Required** field must be selected. Once these conditions are met, the Pack button becomes available, allowing the user to proceed with packing the products.

### Packing Box Tab

The Packing Box tab from the Goods Shipment and from the Packing window is an **informative** tab which shows the newly packing boxes with the following:

- **Box Number**: the box number of the Shipment
- **Weight**: indicates the weight of the box
- **UOM**: the UOM of the weight of the box
- **Tracking No**: number to track the shipment

VA

### Content Tab

In the Packing Box tab, there is a child tab where the **content of the box** is shown.

- **Product**: identifies an item which is either purchased or sold in this organization.
- **Quantity**: indicates the quantity of product in the box
- **UOM**: the UOM defines a unique non monetary unit of measure

### Buttons

Once the mentioned above procedures are done (either initiated from the Packing window or the Goods Shipment window), continue the process from the Packing window in order to pack the products. 

- **Pick Shipments**: from the Packing window, it is allowed to select all the available goods shipments that need to be packed. To do so, press the button Pick Shipments. The criteria to show which goods shipments can be selected is the following:

  - Goods shipments that belong to that business partner and that address.

  - Goods shipments that are marked as Packing Required.

  - Goods shipments that have not been packed.


- **Pack**: if the user starts the process from the Goods Shipment window, this button becomes available once the document is in **Completed** status and the **Packing Required** field is checked. If the process is innitiated from the Packing window, this button is visible allowing the user to proceed with packing the products.

When pressing the Pack button:

A pop up is opened showing all the products with their quantities. The user needs to **type the quantity** for each product in every box. There are three different ways of entering the quantity:

- Using a **barcode reader scanner**: If a product with a barcode exists, it updates the quantity in the corresponding box. Using the barcode reader scanner will be useful in case of packing many products. 
- Manually typing the **quantity in the box**.
- Typing the **barcode number** and pressing **Validate Barcode**. If a product with that barcode exists, it updates the quantities in the corresponding box.

Let’s consider that new boxes can be added by pressing Add Box.

!!! note
    When the sum of the quantities of all boxes is the same as the Quantity of the product, then it is marked as validated (green color). Packing will be possible once all the products are validated. 

When packing is completed the button **Pack inside the popup** is not shown. This button only makes sense for:
   - Create the boxes
   - Recalculate the weight

So, when it is completed no further actions are allowed.

!!! info
    After adding the goods shipment and the packing action has been performed if the user removes any of the goods shipments from being packed then, all boxes are deleted and the packing must start again. 


- **Complete Pack**: Once everything is ok and all boxes and their content have been created, press the button Complete Pack. The information of the boxes such as the weight, UOM and Tracking No. cannot be edited. This button **completes** all boxes at once.

- **Reactivate Pack**: Once everything has been completed the Reactivate pack button allows the user to **reactivate** the packing and **edit** whatever information is needed.  
