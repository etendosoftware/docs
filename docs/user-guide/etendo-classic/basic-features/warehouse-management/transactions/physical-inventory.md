---
title: Physical Inventory
tags:
 - Physical Inventory
 - Warehouse Management
 - Inventory Count
 - Transactions
---

# Physical Inventory

:material-menu: `Application` > `Warehouse Management` > `Transactions` > `Physical Inventory`

**Physical Inventory** window allows the user to execute goods count process in Etendo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xqE_UnYO6cM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Header

Goods count process requires creating an inventory count to check or to update stock quantities.

These are the steps that must be followed in order to create an inventory count:

**1.** The **Header** section identifies the "Physical Inventory" process and lists its main parameters.

![Header](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-1.png)

All fields are pre-filled automatically when a new record is created.

Some of the fields to note are:

- **Name:** This field is used to reference the physical movement not only in warehouse reports but also on general ledger, therefore it is important to use a significant name.
- **Movement Date:** This is the date when the movement is created and it is defaulted to the current date. This date is also used in the posting record of the Physical Inventory document to the general ledger, if any. It can always be changed, but the user should keep in mind that it is not possible to register physical inventories in the past (the "Process Inventory Count" always takes the current date and not the Movement Date to update the stock). The Movement Date should be the current date unless the user can ensure that no warehouse transactions have been processed in the meanwhile.
- **Warehouse:** warehouse in which the physical inventory takes place. Defaulted to the session value from the top navigation User Preferences menu.

**2.** There are 2 ways of **entering lines** into the physical inventory document:

1.  Automatically, by creating a list of the products available in the warehouse and storage bins defined in the physical inventory header that fulfill the filtering conditions specified by the **Create Inventory Count List** button.
2.  Manually, line by line for certain products. This is used whenever only some products need updating.

**Create Inventory Count List** process can be executed more than once for the same physical inventory. Although lines are created automatically by using the **Create Inventory Count List** process, these lines can later on be updated manually. **Create Inventory Count List** filter dialog has the following parameters:

![Header 2](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-2.png)

The fields to note are:

- **Storage Bin:** Only products on this storage bin will be filtered.
- **Product Category:** Only products belonging to a given product category will be filtered, otherwise all products will be shown.
- **Inventory quantity:** Includes or excludes products on physical inventory depending on actual quantities. The options available are:
    - empty - all product on physical inventory will be shown regardless its quantity
    - 0 - only products on physical inventory having 0 quantity in stock will be shown.
    - <0 - only products on physical inventory having a negative quantity in stock will be shown.
    - \>0 - only products on physical inventory having a positive quantity in stock will be shown.
    - not 0 - only products on physical inventory having a quantity in stock different to 0 will be shown.
- **Set Book Quantity to Zero:** this checkbox sets the **Quantity Count** field on the count list to zero. When the checkbox is not selected, the **Quantity Count** is defaulted to the same value as the **Book Quantity** (On Hand Quantity) of the product.
    - First option (checkbox selected): used for blind physical inventories where the people counting items do not need to know the expected quantities.
    - Second option (checkbox not selected): allows the user to enter the real quantity counted in the warehouse. Once the inventory count is processed, the system updates the book quantity to match the quantity count entered.
- **ABC:** Filters by product priority category based on Pareto analysis of stock value (A = high value/high turnover, B = medium, C = low). See [Pareto Product Report](../analysis-tools/pareto-product-report.md).

## Lines

Lines tab allows the user to add or to edit individual products to be included in the inventory count list. It represents the inventory count list of a given warehouse.

Some relevant fields to note are:

- **Quantity Count:** that is the actual (physically counted) product stock in the **Storage Bin** of the warehouse.
- **Book Quantity:** that is the product stock in the **Storage Bin** according to Etendo.
- **Cost:** that is the unit cost of the product.  
  This field is optional. It can be filled in with the cost if known whenever the stock of a product is increased, otherwise the Default Cost method is used to valuate that transaction which increases the stock of the product.

The process buttons are:

- **Update Quantity** updates current **Book Quantity** field with latest product quantity from the application. This is used in case it has changed since the count list was generated. It is useful for situations when there is a significant amount of time in between generating physical inventory in Etendo and real physical count.
- **Process Inventory Count** finishes Physical Inventory count process after all corrections have been entered and updates the stock.
- **Post** allows to account the inventory count once processed.

## Accounting

A physical inventory can only be posted to the ledger in case there is a difference between "Quantity count" and "Book Quantity" for a product. Otherwise there will not be anything to post to the ledger.

For instance, a product whose "Quantity count" is 6700 units at a given date, while "Book Quantity" in Etendo is 6000 units.

That physical inventory can be posted once processed, if the cost of the product has been calculated.

**Physical Inventory posting creates the following accounting entries if inventory increases:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Account               | Debit                                                   | Credit                                                  |
| Product Asset         | (Quantity Count - Book Quantity) \* Cost of the Product |                                                             |
| Warehouse Differences |                                                             | (Quantity Count - Book Quantity) \* Cost of the Product |

**Physical Inventory posting creates the following accounting entries if inventory decreases:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Account               | Debit                                                   | Credit                                                  |
| Warehouse Differences | (Quantity Count - Book Quantity) \* Cost of the Product |                                                             |
| Product Asset         |                                                             | (Quantity Count - Book Quantity) \* Cost of the Product |

## How to Reactivate Physical Inventories

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

From the Physical Inventory window, it is possible to reactivate a previously generated inventory just by selecting the corresponding document and clicking the Reactivate button.

Once the Inventory is successfully reactivated, the state of the document changes to Not processed as it can be observed in the status bar.

![Physical Inventory document showing Not processed status after reactivation](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-3.png)

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