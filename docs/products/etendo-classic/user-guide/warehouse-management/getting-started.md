---
tags: 
 - getting started
 - warehouse management
 - inventory accuracy
---

![cover-getting-started.png](/assets/getting-started/overview/cover-getting-started.png)
#

## Overview

In Etendo, most of the warehouse movements are created automatically based on the transactions of [Sales]() and [Procurement]() processes. However, operating a warehouse also involves several manual activities, such as physical inventory, goods movements and their tracking and inventory valuation. These activities are executed in the Warehouse Management application area and are gathered in the [Inventory Accuracy]() business flow which is described below.

## Inventory Accuracy

![](/assets/products/etendo-classic/user-guide/warehouse-management/getting-started/walltowallaccubusprocess.png)

Main sub-processes of the Inventory Accuracy business flow are:

- *Physical Inventory*: This is a process where a business physically counts individual items in stock at a particular point in time and updates their inventory count within the system (if needed). It represents an opportunity to correct any inaccuracies in the records. Here are several reasons to conduct a physical inventory:
    - To initiate the stock
    - To verify the physical amount, condition, and location of inventory items
    - To identify, document, and add items to its inventory list that are on-hand and meet qualifying criteria, but are not currently shown as part of the inventory
    - To ensure that legitimately transferred or disposed items are no longer carried on the inventory listing
    - To identify any missing or damaged items that need to be located, repaired, or replaced.
- *Goods Movement*: Transfers inventory between storage bins or warehouses. Possible reasons for goods movement are:
    - Goods received at warehouse from another party or warehouse.
    - Inventory movement due to conversion of goods.
- *Goods Tracking*: Displays all of the different movement types that happen in warehouse to verify the history, location, or application of an item by means of documented recorded identification.
- *Inventory Valuation*: Allows a company to provide a monetary value for items that make up their inventory.
- *Inventory Update*: Allows a company to change either current inventory amount or current unit cost of products in stock.
- *Cost Adjustments Review*: Allows a company to review product cost adjustments caused by changes in purchase prices, landed cost allocation or manual / negative cost corrections.

### Configuration

[Warehouse and Storage Bins]() need to be created and configured before performing the business flow.
In addition to this, a [Costing Rule]() needs to be defined and validated for the legal entity. Each costing rule requires a starting date from when it is going to be valid as well as a [Costing Algorithm]() to be used by the [Costing Background Process](), which has to be scheduled.

Besides, [Landed Cost Types]() need to be configured here therefore can be selected while allocating this type of cost to [goods receipts]().

Finally, [Warehouse Rules]() can be configured to be applied while retrieving stock from the inventory automatically.

!!!note
        It is not required to do any additional setup for the Warehouse Management application area if Food & Beverage (F&B) sample client shipped with Etendo by default is going to be used to explore it. The sample data set already contains the roles, warehouses, and products pre-configured.

Above configuration is part of the overall Business setup flow within "Warehouse" setup.

### Execution

In Warehouse Management main Inventory Accuracy operations are executed as follows.
To get the *Physical Inventory* Warehouse Staff:

- Starts with the products classifications and runs [Pareto Product Report]() which distributes products into three classes (A, B or C) according to their cost percentage in the warehouse.
Based on the classification, the frequency of counting cycle can be decided (e.g. A products are counted weekly, B products monthly and C products yearly).
The ABC classification is then populated to the [Manufacturing]() tab of the Product window by clicking the Update ABC button.
    - Note that the ABC classification is based on the cost of the product's transactions. That is why a [Costing Rule]() for the legal entity must be configured and validated and the [Costing Background Process]() process has to be scheduled.
- After this procedure, the Warehouse Staff creates the physical inventory document in the [Physical Inventory]() window by selecting the Warehouse where to execute this activity and pressing the Create Inventory Count List button. They define the criteria for the products to be included in the count-list (for example ABC classification) and it results in the [list]() of products with their current quantities that is brought to the warehouse and verified against physical inventory.
- In order to update Etendo stock, if differences are found, first the Warehouse Staff selects the [Physical Inventory]() that was previously created. Then in the [Lines]() tab, they find the required products and update the Quantity Count field with a new value. After that, they finish the inventory count by clicking the Process Inventory Count button which updates inventory and triggers document posting (if configured).

To execute *Goods Movement* Warehouse Staff:

- In the [Goods Movements]() window, lists products to be moved with source and destination information and the respective quantity and then processes the document which updates all product quantities listed under Lines tab in the warehouse and triggers document posting (if configured).

For *Goods Tracking* Warehouse Staff uses:

- [Stock Report]() that gives a stock level of all products (that have inventory different from zero) and their location (warehouse and storage bin) grouped by product category.
- [Goods Transaction]() window that offers a read-only view with extensive filtering capabilities that shows all inventory transactions.
- [Product Movements Report]() shows all receipts, shipments, moves and physical inventories grouped by Transaction Type and Business Partner.
- [Material Transaction Report]() lists all documents (shipments or receipts) grouped by Business Partner.

*Inventory Valuation* is done with the help of the [Valued Stock Report]() .
This report shows the cost of the stock calculated by the [Costing Server]() process.

*Inventory Update* is done with the help of the [Inventory Amount Update]() window.
This window allows changing either the total inventory value or the unit cost of a product(s) at a given reference date, therefore a closing and an opening inventory are automatically created in the [Physical Inventory]() window.

For *Cost Adjustments Review*, Warehouse Staff uses the [Cost Adjustment]() window.
This window allows reviewing different types of cost adjustment sources together with the product's transactions whose costs are being adjusted, as well as adjustment amounts.

## Relationship with other application areas

Warehouse Management has a connection with other application areas:

- *Procurement Management* as goods received change stock quantity and its value.
- *Sales Management* as shipment changes stock quantity and its value.
- *Production Management* because raw materials are taken out of warehouse and produced goods are sent back to the stock during production process.