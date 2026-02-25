---
title: Goods Receipts
tags:
    - Goods Receipts
    - Procurement Process
---

# Goods Receipts

:material-menu: `Application` > `Procurement Management` > `Transactions` > `Goods Receipt`

A Goods Receipt is a document issued to acknowledge the receipt of the items listed in it. In other words, it is a document used to register in Etendo the specifics of items physically received in the warehouse.

## Header

Goods Receipts can be issued and booked in the header section of the goods receipt window.

![Good receipts header](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/goodsreceipt2.png)

The fields to fill in the **Goods Receipt header** are:

- **Document Type**, which is filled in by default as "MM Receipt".
- **Warehouse**, where goods are going to be located.
- **Business Partner**, third party which delivers the goods.
- **Movement Date**, delivery date of the goods.
- **Accounting Date**, accounting date in case of posting the Goods Receipt.
- **Purchase Order**, purchase order number linked automatically by Etendo, in case the Goods Receipt is automatically created from a Purchase Order.
- **Order Reference**, Warehouse team can fill in here the Supplier's Delivery Note number, this way the internal Goods Receipt number and the Supplier's Delivery Note number are linked.

In the **Status Bar** of the header, the user can find the following information:

- **Document Status**: Document status of the receipt.
- **Invoice Status**: It indicates in % how much quantity of the receipt has been invoiced.

**Once header information is properly filled-in, you can then go to the "Lines" tab in order to enter "Goods Receipt Line/s"**.

!!! info
    To learn how to enter goods receipt lines, visit the next section [Lines](goods-receipts.md#lines)

If a **Goods Receipt** is completed and therefore **booked**:

- The **quantity on hand of the item/s received is increased** by the quantity received.

If a **"Completed" Goods Receipt is voided** because the goods have been returned to the supplier:

- **The quantity on hand of the items/s returned is decreased** by the quantity of the goods returned. Etendo automatically creates a new "Goods Receipt" for exactly the same items but with "negative" quantities.

!!! info
    To learn more about Goods Returns, visit *Return to Vendor* and *Return to Vendor Shipment*.

Supplier can send a "Purchase Invoice" together with the "Delivery Note" of the goods delivered, therefore:

- From the Goods Receipt window, it is possible to generate the corresponding supplier's invoice, by using the header process button "**Generate Invoice from Receipt**".

This action implies a **link between the goods receipt and the purchase invoice**, the user can be aware of when inquiring about the corresponding purchase invoice.

!!! info
    To learn more, visit [Purchase Invoice](purchase-invoice.md).

## Lines

Once the goods receipt header has been properly filled in and saved, each item received can be listed as a separate goods receipt line.

There are several ways of creating goods receipt lines.

1.**The user can always manually create goods receipt lines.**
That is the way the user could turn to in case there is not a booked purchase order nor a completed purchase invoice for the goods received they can retrieve data from.

As a consequence, the information to manually fill in is:

- the goods or items received
- the quantity received
- the storage bin where the items are going to be stored

**Explode** button is shown when selecting a line with a non-stockable BOM product and the product has not already been exploded. When exploding a product, the bill of materials components the selected product consists of are shown in the shipment. Once you have exploded it, you cannot comprime it. You should delete all the lines (first bill of materials components and then the BOM product), and insert again the non-stockable BOM product.

2.On the other hand, it is also possible to **"automatically" create goods receipt lines**, by using the header process button **"Create Lines From"**.

This allows the user to select the orders or invoices pending to be received.

For instance, once a purchase order is selected, the purchase order lines pending to be received are shown.

Then, the user is able to select the purchase lines received, change the quantity if required, and get them located in the warehouse.

Finally:

- If a purchase order/line is selected, this action **links each good receipt line to the corresponding purchase order line**, same applies to purchase invoice.

In the **Status Bar** of each line, you can find information about the **Invoiced quantity**, the number of invoiced products of the line.

### Accounting

Accounting information related to the material receipt.

A **"Goods Receipts" can be posted** if the "**MaterialMgmtShipmentInOut**" table is set to Active for accounting in the \[*Active Tables*\] tab of the organization's general ledger configuration.

A "Goods Receipt" posting looks like:

![Good receipts posting](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/goodsreceipt3.png)

Posting a "Goods Receipt" requires the calculation of the cost of the contained product/s.

In the case of a goods receipt, that is:

- the purchase price of the product/s
- or the default *standard cost* of the product/s in case of calculating cost by using an Standard *costing algorithm*.

If there is not a related purchase order, the Costing Server process uses the newer of the following three values:

- the last purchase order price of the receipt's vendor for the product.
- the purchase price list of the product.
- or the *default cost* of the product.

Moreover:

- The "Legal Entity" organization needs to have a validated *Costing Rule* configured.
- And the *Costing Background Process* needs to be scheduled for the *Client*, therefore it can search and allow that the *Costing Server* process calculates the cost of the transactions.

Once the costs have been calculated, the **Goods Receipt can be posted** to the ledger.

In the case of a receipt containing "Expense" product/s without the "Sales" checkbox selected, it is possible to use the product's purchase price instead of the product's cost to post the goods receipt.

This works if the checkbox *Book Using Purchase Order Price* is selected for the product/s.

In this case, it is required that a "Purchase Order" is related to the posted "Goods Receipt".

### Voiding

It is possible to totally void a goods receipt by using the header button **"Close"** and then selecting the action "**Void**".

This action creates a **new document** that **reverses the goods receipt.**

Void action allows to specify a "**Void Date**" and a "**Void Accounting Date**" of the new document:

- **Void Date**: that is the movement date of the new document that reverse the goods receipt.
- **Void Accounting Date**: that is the accounting date of the new document that reverse the goods receipt.

Both fields above take original document dates as default date and validate that the dates entered are not prior to the "Movement Date" and the "Accounting Date" of the Goods Receipt, respectively.

Void action implies that:

- Etendo automatically generates a **new document** in the "Goods Receipt" window, and **informs about the document number** created. The document number is also displayed in the description field of the Goods Receipt. This new document is created as described below:
  - The "**transaction document**" used by Etendo is "**MM Receipt**".
  - This document is **exactly the same as the original** one being reversed **but the movement quantity is negative.**
  - Once the **new document** has been created, you can **change** both the "**Movement Date**" and the "**Accounting Date**" of the new document prior to getting it posted.

### Landed Cost

Landed Cost tab allows to allocate additional costs to the goods receipt.

![Landed cost window](../../../../../assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

It is possible to enter as many landed cost types/lines as required.

Some relevant fields to note are:

- **Landed Cost Type**: that is the landed cost type that is going to be allocated to the goods receipt.
- **Invoice line**: that is to select the corresponding landed cost invoice line if any, that matches the landed cost type being entered.
  If an invoice line is selected, the invoice line amount gets populated in the next field "Amount".
- **Amount**: that is the landed cost amount. This amount can be an "estimation" or a "real" amount in case of selecting an invoice line.
- **Landed Cost Distribution Algorithm**: that is the one distributed by Etendo "Distribution by Amount", which means that the landed cost amount is going to be distributed among the goods receipt lines proportionally by receipt line amount.

Once all items above are filled in, including corresponding landed cost purchase invoice line, both "Goods Receipt" and Landed Cost *process matching* are executed by clicking on the "**Complete**" process button.

## How to Reactivate Goods Receipts

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

From the Goods Receipt window, it is possible to reactivate a previously generated movement just by selecting the corresponding document and clicking the Reactivate button.

Once the receipt is successfully reactivated, the state of the document changes to Draft as it can be observed in the status bar.

![](../../../../../assets/drive/1-Z-wUYZfcGDizQ_Kkp8TUYXTs-KnM67H.png)

!!! warning
    Note: It is not possible to reactivate documents that include transactions with quantities exceeding the existing stock quantity for a certain product in a certain storage bin. The only exception is when the configuration of the storage bin allows Over Issue. For more information, visit [Storage Bin](../../warehouse-management/setup.md#storage-bin).

## Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk posting** button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

## Bulk Completion

!!! info
    To be able to include this functionality, the Essentials Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Essential Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

The Bulk Completion functionality allows the user to complete, reactivate or void multiple records by selecting them and clicking the **Bulk Completion** button. This makes records management easier and more efficient, reducing the time spent processing individual records.

!!! info
    For more information, visit [the Bulk Completion module user guide](../../../optional-features/bundles/essentials-extensions/bulk-completion.md).

---

This work is a derivative of [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
