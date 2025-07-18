---
title: Warehouse Extensions Bundle
tags:
    - Warehouse Management
    - Automated Reservation
    - Stock History
    - Document Reactivation
    - Product Operations
---
:octicons-package-16: Javapackage: `com.etendoerp.warehouse.extensions`

:material-store: Etendo Marketplace:  [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}

## Overview
This bundle includes enhancements for the Warehouse Management functionalities in Etendo.

## Translations

-  :material-translate: Spanish: [Warehouse Extensions Bundle ES](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}

## Modules

### Advanced Warehouse Management

:octicons-package-16: Javapackage: `com.etendoerp.advanced.warehouse.management`

The **Advanced Warehouse Management** module extends the standard capabilities of Etendo to offer comprehensive, flexible, and automated inventory management, adding integration with mobile devices. Every action performed from the Etendo Mobile is automatically synchronized with Etendo, ensuring complete traceability and consistent updates in the corresponding system windows.

!!! info
    For more information, visit [Advanced Warehouse Management](./advanced-warehouse-management.md).

### Automated Warehouse Reservation

:octicons-package-16: Javapackage: `com.etendoerp.automated.warehouse.reservation`

This module adds the option Automatic - Only Default Warehouse to the Stock Reservation field of the lines tab in the Sales Order window. This is used to limit the reservation only to the warehouse specified in the header of the order.

!!! info
    For more information, visit [Sales Order](../../../basic-features/sales-management/transactions.md#stock-reservations) and [Stock Reservation](../../../basic-features/warehouse-management/transactions.md#stock-reservation).

### Packing 

:octicons-package-16: Javapackage: `org.openbravo.warehouse.packing`

The Packing functionality in Etendo focuses on helping warehouse staff pack products in an efficient and organized way. This functionality facilitates staff to concentrate on packaging items accurately once they have been picked. 
If both modules picking and packing are installed, the workflow begins with picking and continues with packing, ensuring a smooth and organized order fulfillment process. However, it is also possible to use the modules separately.

!!! info
    For more information, visit [Packing](packing.md). 

### Picking 

:octicons-package-16: Javapackage: `org.openbravo.warehouse.pickinglist`

:octicons-package-16: Javapackage: `org.openbravo.warehouse.structure`

In Etendo, the Picking functionality is designed to help warehouse staff manage and deliver picking lists efficiently. This module facilitates users to access and organize the items that need to be collected from storage. By streamlining the picking process, it reduces errors and improves the overall speed of order preparation. Picking is typically the first step in the order fulfillment workflow when both Picking and Packing modules are installed.

!!! info
    For more information, visit [Picking](picking.md).

### Product Operations

:octicons-package-16: Javapackage: `com.etendoerp.product.operations`

This module allows you to observe and analyze in detail all transactions associated with the selected product. 

!!! info
    For more information, visit [Product Operations user guide](../../../basic-features/warehouse-management/analysis-tools.md/#product-operations).


### Reactivate Warehouse Documents

:octicons-package-16: Javapackage: `com.etendoerp.reactivate.warehouse.documents`

:octicons-package-16: Javapackage: `com.etendoerp.reactivate.warehouse.documents.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/ghH3tBjoN9c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality is part of the Warehouse Extensions Bundle and it is useful when the user needs to reactivate documents such as Goods Movements, Goods Receipts, Goods Shipments and Physical Inventories. 

!!! info
    For more information, visit the user guide for:

    - [Goods Movements](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#how-to-reactivate-goods-movements)
    - [Goods Receipts](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-goods-receipts)
    - [Goods Shipments](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-goods-shipments)
    - [Physical Inventory](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#how-to-reactivate-physical-inventories)

### Stock History

:octicons-package-16: Javapackage: `com.etendoerp.stock.history`

This module provides updated information about the daily history stock of the products. 

!!! info
    For more information, visit [the Stock History user guide](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#stock-history) and [the Stock History developer guide](../../../../../developer-guide/etendo-classic/bundles/warehouse-extensions-bundle.md#stock-history).

## Uninstall bundle

To uninstall the bundle and prevent future problems with orphan records, a sequence of steps must be followed:

1. Run the following query in the environment's database
```
DELETE FROM OBUIAPP_GC_TAB 
WHERE AD_TAB_ID = 'C3DB551F2BCA40A79AAF21DBD6D06309';
```

2. After the query successfully finishes, delete the bundle by the way corresponding to the installation method (Sources/JARs)