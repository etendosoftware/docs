---
title: Bill of Materials Production
tags:
 - Bill of Materials
 - BOM Production
 - Warehouse Management
 - Transactions
---

# Bill of Materials Production

:material-menu: `Application` > `Warehouse Management` > `Transactions` > `Bill of Materials Production`

## Overview

Create and run production processes using the previously defined bills of materials.

Unlike the name suggests, this process is **not part of production**. This setup is used to combine different end products into another **bundled product**. For example, for a computer that is shipped with different keyboards or products that are shipped with different power cables. There is no actual production involved for the creation of the new product.

The set up of this screen is combined with setups in the product screen:

- the bill of materials checkbox is selected for the product
- the bill of materials tab is filled out

## BOM Production

The BOM Production header is the first section to fill out when creating a new bundling record. Select the organization, enter a name that identifies this bundling run, and set the date on which it will be executed.

## Production Plan

Add bills of materials to be produced in a specified production plan.

In this section, the product is selected and the number that is executed. Also, the storage bin in which the result of the Production will be stored must be selected.

As indicated in the Overview, the product that is selected needs to be set up correctly first:

- the bill of materials checkbox is selected
- the bill of materials tab is filled out with the information of the components that are combined plus the quantity for each component
- the Verify Bom button was clicked to set the product ready to be used

## I/O Products

Create and edit the products that are going to be used in the production.

After the Production Plan tab is filled out, the **Create/Process Production** button is clicked to generate the information in this section. Based on the setup of the information in the bill of materials tab of the product combined with the production quantity in the production plan tab, the information of the **components to be used and which quantity** was generated.

Clicking **Create/Process Production** the first time generates a list of components and quantities based on the bill of materials setup. Review this list and make any adjustments needed. Clicking the button a second time confirms and executes the production, deducting the components from stock and adding the bundled product.

In the popup, the checkbox 'Product quantity must be on stock' can be selected, so the process is only executed if the components are in stock. After successfully processing, the stock of the components decreases and the stock of the bundled product increases.

!!! warning
    Currently, processes involved in the Bill Of Materials Production do not support negative stock. For this reason, if the checkbox 'Product quantity must be on stock' is not selected and there is not enough stock of the consumed products, the available quantity in stock will be used to fill the quantities in the \[I/O Products\] tab lines.

There is a check named **Force Use Of Warehouse Of Selected Storage Bin.** When enabled, the same Warehouse of the selected Storage Bin will be used to retrieve the stock to be consumed. If it is not enabled, the process will take into account all available Warehouses for the set in the header of the Document.

## Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk posting** button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.