---
title: Goods Movement
tags:
 - Goods Movement
 - Warehouse Management
 - Inventory
 - Transactions
---

# Goods Movement

:material-menu: `Application` > `Warehouse Management` > `Transactions` > `Goods Movement`

The **Goods Movement** window allows you to record and process internal inventory movements between warehouses and storage bins. Use it to transfer products from one location to another and keep stock levels accurate across the organization.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yW4Bv6bORk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Header

To record a goods movement, add products one by one in the Lines tab, or transfer all items from one bin to another at once using the **Move Storage Bin** button.

![goods-movement-1](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-1.png)

All fields are automatically pre-filled in when a **new** record is created. Some of them to note:

- **Name:** This field will be used to reference this goods movement, not only in warehouse reports but also in the general ledger, therefore it is important to use a significant name.  
  This field is defaulted to the current date but it can always be changed as required.
- **Movement Date:** that is the date of the goods movement transaction.  
  This field is defaulted to the current date but it can always be changed as required.  
  From an accounting point of view, goods movement will be reflected on this date.

There are 2 ways of entering lines (or products to be moved between warehouses and storage bins):

1.  By adding individual products to the Lines tab.
2.  By moving all items from one bin (**Storage Bin From**) to another (**Storage Bin To**) by using the **Move Storage Bin** button.  
    The system automatically inserts one line per every storage bin and product.

![goods-movement-2](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-2.png)

## Lines

Lines tab is a list of the products moved between warehouses and storage bins.

This tab also includes information about the source, destination and the respective quantity.

![goods-movement-3](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-3.png)

Some fields to note:

- **Movement Quantity:** that is the product amount to be moved.  
  Defaulted to the total quantity of the **Product** in the Storage Bin.
- **Storage Bin:** The location the products will be taken from. Pre-filled automatically based on the product selected, but it can be changed if needed.
- **New Storage Bin:** that is the destination bin for the products.
- **New Attribute Set Instance:** A read-only field that appears only when this goods movement is part of a box or unbox operation (see [Referenced Inventory](referenced-inventory.md)). It displays the updated item identifier — including the container reference — after the boxing or unboxing is complete.

## Buttons

### Move a Storage Bin

Allows quickly transferring all products located in a source storage bin to a destination storage bin.
When clicked, the system automatically displays a list of products from the selected source location in the lines.
When processing the transfer, all products are moved from the source to the destination.

![goods-movement-4](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-4.png)

### Generate Relocation Task

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Creates a relocation task from the **Goods Movement** document. The system takes the information loaded in the record and its lines and sends it to Etendo Mobile, where the operator can execute the movement from the corresponding sub-application. When clicked, the automatic or manual assignment pop-up opens.

!!! info
    For more information, visit [Relocation Task](../../../optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#relocation-tasks)

### Process Movement

This button processes the Goods Movement document. When executed, the system validates the movement information and updates the stock in the corresponding locations.

![goods-movement-5](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-5.png)


## Accounting

!!! info
    Before a Goods Movement can be posted to the ledger, it must be enabled in the general ledger configuration. If the Post button is unavailable, contact your system administrator and ask them to activate the Goods Movement table in the Active Tables tab of the organization's general ledger configuration.

Goods Movement posting creates the following accounting entries.

Posting record date: Movement Date.

|               |                           |                           |                             |
| ------------- | ------------------------- | ------------------------- | --------------------------- |
| Account       | Debit                     | Credit                    | Comment                     |
| Product Asset | Movement Line Cost Amount |                           | One per Goods Movement Line |
| Product Asset |                           | Movement Line Cost Amount | One per Goods Movement Line |

Before posting a Goods Movement, the system must calculate the cost of the moved items. This requires two conditions to be met:

- A validated [Costing Rule](../setup.md#costing-rules) must be active for the Goods Movement legal entity.
- The [Costing Background Process](../../general-setup/process-scheduling/process-request.md#costing) must have run.

Once both conditions are met, the Goods Movement can be posted.

## How to Reactivate Goods Movements

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

To correct a goods movement that has already been processed — for example, after an error is detected in the transferred quantities — reactivate it to make changes. From the Goods Movement window, select the corresponding document and click the Reactivate button.

Once the movement is successfully reactivated, the document status bar will show Not processed, confirming the reactivation was successful.

![goods-movement-6](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-6.png)

!!! warning
    It is not possible to reactivate documents that include transactions with quantities exceeding the existing stock quantity for a certain product in a certain storage bin. The only exception is when the configuration of the storage bin allows Over Issue. For more information, visit [Storage Bin](../setup.md#storage-bin).

## Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk posting** button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.