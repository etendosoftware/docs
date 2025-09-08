---
title: Stock Logistic Unit
tags:
    - Logistics Unit
    - Unit
    - AUOM
    - Stock
    - Etendo Mobile
---
# Stock Logistic Unit
:octicons-package-16: Javapackage: `com.etendoerp.stock.logisticunit`

## Overview
The **Stock Logistic Unit** module extends Etendo's standard functionality to manage logistics units within inventory, receiving, and stock reservation processes. Specifically, this module adds the unit of measure Box and the reference inventory types Box and Pallet.

Its objective is to integrate Alternative Units of Measure (AUOM) with the Referenced Inventory (RI) model, so that logistics units are recognized, recorded, and managed as traceable entities in all warehouse operations. This module adds the Pallet and Box reference inventory.

Also, incorporates advanced stock reservation logic that prioritizes complete logistics units over individual units. This means that when processing a sales order with automatic quantity reservation in AUOM, the system prioritizes this condition and only completes the reservation with individual units if the required quantity is not reached. This priority rule ensures more efficient stock management and ensures that operations respect the original condition of the sale by AUOM, while maintaining traceability at the logistics unit level. Enable the Enable UOM Management preference to view and manage alternative UOMs.

This module:

- Adds the UOM **Box** unit of measure. These are available in the system to configure product AUOMs without manual user intervention. 
- Aggregates the Referenced Inventory Type of **Box** and **Pallet** with their corresponding sequences. 
- Each AUOM is linked to a referenced inventory type, ensuring that stock creation in RI complies with the defined logistics unit. It includes validations in the user interface and back-end logic to prevent inconsistencies.
- Introduce smart reservation rules that respect the logic of boxes, and units, reducing stock allocation errors. With this logic, when a sales order is automatically reserved, the system attempts to fulfill the quantity requested in the order with complete logistics units if possible, before resorting to individual units. For example: if 2 boxes of a product are requested and there is only 1 box + 12 individual units in stock, the system will reserve the box first and complete the second with the individual units.
- Add the preference Generate logistics unit automatically, with a default value of ‘Y’. This preference controls whether, upon completing a receipt, the system should automatically create Referenced Inventory records for entered logistics units.
- Set the preference Enable UOM Management, with a value of ‘Y’. 
- The generated RI retains all relevant attributes, ensuring traceability from the moment it enters the warehouse.

## Initial Setup

To start using this module correctly, the following installation and configuration steps must be completed:

- [x] Install the **Warehouse Extensions** bundle.
- [x] Install dataset **Stock Logistic Unit**
- [x] Verify that the preference **Generate logistics unit automatically** is set to **Y**.
- [x] Verify that the preference **Enable UOM Management** is set to **Y**.

## Module Impact

The Stock Logistic Unit module affects several standard Etendo windows, as it introduces new logistic units and their integration with referenced inventory and alternative units of measure.

In the Unit of Measure window, the module adds the units of measure Box to facilitate the management of logistics units within the system. These UOM serve as the basis for configuring products with alternative units, while the user can create as many additional variants as needed based on the different box format used.

In the Referenced Inventory Type window, the module adds the referenced inventory types Box and Pallet, each with its corresponding sequence. In this way, the referenced inventory retains traceability at the logistics unit level, ensuring consistency between the defined AUOMs and stock records.

Reservations are updated using logic that allows alternative units of measurement to be taken into account.

Finally, in the Alternate UOM tab of the Product window, by enabling the Enable UOM Management preference, it is possible to assign Box or Pallet as alternative units of measure. The user can define the necessary conversions and determine in which processes they are applied (sales, purchasing, or logistics). Based on this configuration, stock reservation rules automatically prioritize the use of pallets and full boxes before resorting to individual units, thus optimizing inventory management.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.