---
title: Warehouse Extensions Bundle
tags: 
    - Picking
    - Lists
    - Pick shipments
    - Products
    - Warehouse

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

Type of picking lists available: 

**Direct Picking List to Customer**: These picking lists generate the Goods Shipments from the locations where the items are stored. The Goods Shipments are created in Draft status when the Picking List is created. Picking List is completed once Goods Shipments are processed.

## Configuration

In order to generate a picking list, some configuration is needed.

- **Document type**: The Picking list document type must be defined for each organization.
The module provides a dataset with basic document types that can be applied. Go to [Enterprise module management](../../../basic-features/general-setup/enterprise-model.md#enterprise-module-management) and apply the **Warehouse Picking List dataset** for each organization using Picking Lists. Once it is applied, the document types are created.

![picking](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking1.png)

The dataset adds two new document types, with their own Document Sequences which will apply the following on each organization:

- **Picking List**: Used for **Direct Picking List to Customer** picking list type. Picking List using this document type creates the shipments from the picking location. When they are completed the Goods Shipment is completed.

- **Grouping Pick List**: Using Outbound location and the Is Grouping Picking List flag checked. This document type is used when grouping different picking lists in one list.
