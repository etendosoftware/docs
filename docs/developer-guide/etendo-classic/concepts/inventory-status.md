---
title: Inventory Status
---
## Overview

This section explains the Inventory Status concept that is part of Etendo.

## Configuration

The Inventory Status will be available and configured as part of Etendo.

By default, all the Bins will be in an undefined Inventory Status. There are two possibilities:

-   **Undefined**. Available and Nettable, but not possible to go to Over Issue.
-   **Undefined OverIssue**. Available and Nettable and possible to go to Over Issue.

The initial status of the Bins will depend on the previous configuration of the Client. For those clients which were configured to Allow Negative Stock, the Undefined OverIssue Inventory Status will be set. For the rest, it will be the Undefined Inventory Status. 

!!! info
        For more information, visit the [Allow Negative Stock user guide](/docs/products/etendo-classic/user-guide/general-setup/client/).

## Functionality

The Inventory Status concept is part of the inventory management of Etendo and includes the dimensions for Available, Nettable, and OverIssue to the storage bin and all stock in this bin has the same Inventory Status. The semantics of the Inventory Status refers to the condition of a specific inventory and can be configured. See examples at the end of this section.

The master data for inventory status is maintained on system-level and the most typical values come predefined with the Etendo dataset. It is possible to add new and/or translate existing inventory status.

!!! info
    To have access to this window, it is necessary to log in as system administrator.


![](/docs/assets/drive/0n3Ivd3Cp7mA5Q7vAbIhorgapjwAxb6ybg6_fqwlpmzwe4FcL3RV2o6AIqsR2cFEdXKSRtzToRe9E5lLZsdoDCGZmM0toNmJZKURGVZxNStUoQW_ocSMxgcB4KjV_ARl4TTg0GWncx0ONJ1GzIfAHsJxNIs38iEekvloTzKkUdFIjICAn0YUklI1ThE-tg.png)

In the image above, the various Inventory Status values that are supplied with the installation of the software are shown.

The inventory status allows or disallows certain business processes.

-   Ability to create/modify/delete Inventory Status with the following attributes:
    -   **Available**: Inventory that is available for reservations and picking.
    -   **Nettable**: Inventory that is available for planning of future supply (MRP).
    -   **OverIssue**: Inventory that is allowed to go negative during the Issue of stock (not during the picking).
        -   Note: It is not possible to go to negative if there are reservations against a particular stock. The reservation is always respected, regardless of the inventory status.
-   Add an Inventory Status value to each location or bin record.
-   Add the possibility to manually update the Inventory Status of a Storage Detail by moving it to a virtual, AdHoc created, bin.
-   A new process that identifies affected reservations when a change of the inventory status reduces/increases the quantity available. (Once identified, the relevant users could receive an alert about the consequence of the change in availability).

### Inventory Status Change

In the Warehouse and Storage Bins window, It is possible to check the Inventory Status of a Storage Bin and also to modify it.

By selecting a Storage Bin in this window, it is possible to check its current Inventory Status.

![](/docs/assets/drive/J6y4kVfAaNOLqMAlBOJxByWBUkIA-lgdT1RM4HHn2jLkwJhzf0efsUgT78F77DEvT9UT9j_8RCRLnaNFVm-kWhGMRRaYf9thzTnAWN2fvBVsKx4aJX6xc4mb1qPlwH46AUwHc5D3v8Xye_ONWikm3ZKGaCTojkJMeTxkBBoLvSEnXoy_Gp85Ws-FY_1yAQ.png)

Also, by selecting a Storage Bin, a button named Change Status appears. By clicking it, it is possible to select a different Inventory Status for the selected Storage Bin.

There are some restrictions:

-   If there are existing Reservations against the Stock of the Storage Bin, this Storage Bin can not be changed to an Inventory Status that does not have the Available flag checked
-   If there is negative stock in the Storage Bin, it is not possible to change the Inventory Status to one that does not have the Over Issue flag checked

![](/docs/assets/drive/tchXpNhj5d5jez97SiLuvXUJJNbHIhHgLfDfU4e2hw2Q5tCqACZLE_daLM920HKiFuYVgQAwZoKpTkdw-pICFn8MVz3Y7TuM04CaWGjxclVXTzqz03ZNxpxj3PWkKwX8KB259JYTGJNeWTIRr1rkzAkaAQppROV4yfDIa6qBWHZVfgJA4xjFO84kb41EjQ.png)

### Examples

Examples of inventory status values:

-   **Available** (YYN -> Available, Nettable, Not OverIssue, Owned/Not-Owned) can be set for all inventory that is free to be picked, for sales, production or any other purpose.
-   **In Transit** (NYN) is not free to be sold or shipped but is expected within a limited time and for that, we will take it into account for planning.
-   **Quarantine or Blocked** (NNN) is not available nor nettable since we expect a larger duration of this status.
-   **Inspect** (NYN) is also not available but is expected to be freed in a limited time and for that reason visible for planning/MRP.
-   **BackFlush** (YYY) will allow going negative due to unexpected waste in manufacturing environments.
-   **Public** (YYY) will allow going negative due to unexpected stock in public picking areas.
> 
!!! info
    The inventory status does not have an effect on the inventory value.
