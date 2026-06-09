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

Goods Movement window allows the user to make internal inventory movements among warehouses and storage bins.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yW4Bv6bORk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Header

Internal inventory movements can be made by adding products to the lines tab or by moving all items at once.

![Header](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-1.png)

All fields are automatically pre-filled in when a **new** record is created. Some of them to note:

- **Name:** This field will be used to reference this goods movement, not only in warehouse reports but also in the general ledger, therefore it is important to use a significant name.  
  This field is defaulted to the current date but it can always be changed as required.
- **Movement Date:** that is the date of the goods movement transaction.  
  This field is defaulted to the current date but it can always be changed as required.  
  From an accounting point of view, goods movement will be reflected on this date.

As already mentioned, there are 2 ways of entering lines (or products to be moved between warehouses and storage bins):

1.  By adding individual products to the Lines tab.
2.  By moving all items from one bin (**Storage Bin From**) to another (**Storage Bin To**) by using the **Move Storage Bin** button.  
    The system automatically inserts one line per every storage bin and product.

![Header](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-2.png)

## Lines

Lines tab is a list of the products moved between warehouses and storage bins.

This tab also includes information about the source, destination and the respective quantity.

![Lines](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-3.png)

Some fields to note:

- **Movement Quantity:** that is the product amount to be moved.  
  Defaulted to the total quantity of the **Product** in the Storage Bin.
- **Storage Bin:** that is the bin products are taken from.  
  Defaulted to the Storage Bin selected in the **Product** selector.
- **New Storage Bin:** that is the destination bin for the products.
- **New Attribute Set Instance:** A read-only field that appears only when this goods movement is part of a box or unbox operation (see [Referenced Inventory](referenced-inventory.md)). It displays the updated item identifier — including the container reference — after the boxing or unboxing is complete.

Once **Process Movements** process is executed, the stock is updated.

## Buttons

### Move a Storage Bin

This button allows you to quickly transfer all products located in a Storage Bin A to another destination Storage Bin B.
When you click it, the system automatically displays a list of products from the selected source location in the lines.
When processing the transfer, all products are transferred from the source to the destination.

![Move Storage Bin popup showing the source and destination bin selectors](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-4.png)

### Generate Relocation Task

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Allows you to create a relocation task from the **Goods Movement** document. The system takes the information loaded in the record and its lines and sends it to Etendo Mobile, where the operator can execute the movement from the corresponding sub-application. When pressed, the automatic or manual assignment pop-up opens.

!!! info
    For more information, visit [Relocation Task](../../../optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#relocation-tasks)

### Process Movement

This button processes the Goods Movement document. When executed, the system validates the movement information and updates the stock in the corresponding locations.

![Process Movement button confirmation dialog in the Goods Movement window](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-5.png)


## Accounting

!!! info
    Before a Goods Movement can be posted to the ledger, it must be enabled in the general ledger configuration. If the Post button is unavailable, contact your system administrator and ask them to activate the Goods Movement table in the Active Tables tab of the organization's general ledger configuration.

Goods Movement posting creates following accounting entries.

Posting record date: Movement Date.

|               |                           |                           |                             |
| ------------- | ------------------------- | ------------------------- | --------------------------- |
| Account       | Debit                     | Credit                    | Comment                     |
| Product Asset | Movement Line Cost Amount |                           | One per Goods Movement Line |
| Product Asset |                           | Movement Line Cost Amount | One per Goods Movement Line |

Posting a _Goods Movement_ implies to have its cost calculated:

- A validated Costing Rule in the _Goods Movement_ legal entity is required.
- The background process Costing Background Process must be run.
- Once the cost has been calculated, the Goods Movement can be posted.

## How to Reactivate Goods Movements

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

From the Goods Movement window, the user is able to reactivate a previously generated movement just by selecting the needed movement and clicking the Reactivate button.

Once the movement is successfully reactivated, the state of the document changes to Not processed as it can be observed in the status bar.

![Goods Movement document showing Not processed status after reactivation](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-6.png)

!!! warning
    It is not possible to reactivate documents that include transactions with quantities exceeding the existing stock quantity for a certain product in a certain storage bin. The only exception is when the configuration of the storage bin allows Over Issue. For more information, visit [Storage Bin](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

## Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk posting** button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.