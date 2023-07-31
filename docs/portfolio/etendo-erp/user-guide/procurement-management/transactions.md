---
title: Procurement Management
---

## Overview

Procurement management deals with all the activities related to the purchase of goods and services from external suppliers and the corresponding reporting.

The process starts by the creation and management of purchase requisitions and corresponding purchase orders to the moment the merchandise is received in the warehouse.

<iframe width="560" height="315" src="https://www.youtube.com/embed/tMCSh8W1YnQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Requisition

A Requisition is a document that specifies a request to order products.

The user can create requisitions and monitor them in this window:

![Requisition window](/docs.etendo.software/assets/drive/1ihaEseE5RnNH7INNbaRLyvZC0P2q-hTl.png)

### Header

Requisition header allows entering the following data:

- The business partner or **supplier**, this is an optional field that could be filled in by the requester in case it is known, therefore:
  - The **supplier entered in the header** will be the one **used for every requisition line unless it is changed** at lines level for a particular line.
  - If there is **no supplier entered in the requisition header** the **one setup by default for the product** in its master data window, "**Purchasing**" tab will be used.
  - If **there is no business partner or supplier** in the header, or in the lines, or setup in the product, **the user will have to enter it while creating the purchase order from the requisition**.
- The **purchase price list**. This is also an optional field to be filled-in, in case it is known by the requester and its behaviour is the same as described above as it is linked to the Business Partner.

Besides, the system populates the following data:

- The **document No.**, which is the Requisition number.
- The **requester**, which is the user entering the requisition.

![Requisition](/docs.etendo.software/assets/drive/1G5HR3bMmJXW837o-6qzZ0CTe418q5JB7.png)

The requester can then move to the "**Lines**" tab to enter **additional data**.

### **Lines**

Each requisition line shows a product demand for a specific date.

Requisition "Lines" tab collects the following demand data:

- The **need by date**, that is the date when the product is required to arrive.
- The **product**, items/products which need to be purchased.
- The **quantity** requested, or the **operative quantity** requested if the product has an _alternative unit of measure (AUM)_ configured.
- The product's **UOM**, or product's **Alternative UOM** depending on product configuration in regards to measure unit.
- The **business partner:** This is an optional field the user can enter if the supplier entered at the requisition header needs to be changed for a particular line.

!!! info
    If there is not a supplier entered at the requisition header, neither at the requisition line, the supplier used will be the one setup by default for the product, therefore this field at line level can also be used to overwrite that defaulted one.

- The **purchase price list**: This is also an optional field that can be entered if the price list entered at the header level or the default product price list information should be overwritten for a particular line.
- The **net list price**: This one is the price of the corresponding price list for a given date. It's an optional field that can be filled in automatically based on the price list entered at the header level or it could be overwritten by the user for a particular product line.
- The **net unit price:** This one can be either equal to the net list price or not, based on the formula: \[net unit price = net list price - discount\]. It is an optional field that can be filled in automatically based on the price list entered at the header level or it could be overwritten by the user for a particular product line.
- The **discount**, if any, is based on a used price list.

![Requisition Lines](/docs.etendo.software/assets/drive/1CtrCvBCrvUuxYDlaFysmkKu0-0XhemfC.png)

It is possible to enter as many requisition lines as products demand.

The last step is to register the "**Requisition**" as "**Complete**" by using the header button "Complete", then:

- **Requisition header status bar** informs us that the Requisition is "**Completed**".
- **Requisition lines status bar** informs us that the "**Matched purchase order quantity" for each line is equal to 0**, as there is no purchase order linked to each requisition line yet, and the requisition line/s status is "**Open**".

It is important to remark that "**Requisitions**" does not have any impact on:

- Items quantity on hand
- Items costing

## Manage Requisitions

Manage Requisitions window is intended to be used to provide an overall picture of the items needed.

### Header

This window allows the user to manage requisitions regardless of their current status, therefore they can change or close a requisition and create purchase orders for those demands.

![Requisition window Header](/docs.etendo.software/assets/drive/1yuE4xa0usvVzSdmthjDWdi12OAqTuJTe.png)

A **requisition** with status "Completed" **can always be changed**, if required. The user needs to reactivate it and then change it and book it.

It is also possible to **close a requisition in case there is no need of the included item/s anymore**, by using the menu button "**Close**" and then select the action "**Close**".

Requisition lines status will then be changed to "Cancelled".

Finally, it is also possible to **create purchase orders** for those **requisitions in status "Complete"**, by using the menu button "**Create Purchase Order**".

In this case, a new window is shown for the user to fill in some data by taking into account that:

- If there are **different suppliers in the requisition lines as well as price list**:
  - the **defaulted ones** entered in the window "Create Purchase Order" **will be the ones used** in the purchase order.
- If there are **different suppliers in the requisition lines as well as price list**, and the user does not enter any defaulted ones in the window "Create Purchase Order":
  - **the ones in the requisition lines will be the ones used** in the purchase orders.
- If **all the requisition lines have the same supplier and price list**:
  - **there will not be any need for selected defaulted ones** in the window "Create Purchase Order", besides only one purchase order will be created.

![Purchase order](/docs.etendo.software/assets/drive/17OuNS8YpM0VC3MUkLO25DPPHCMwWjq8u.png)

Etendo provides information about the purchase order/s number/s created after pressing the OK button in the "Create Purchase Order" window.

This action links the requisition and the purchase order, and besides a purchase order line is created for each requisition line:

- A **requisition** linked to a purchase order changes its status from **Completed** to **Closed**.
- A **requisition line** linked to a purchase order line changes its status from **Open** to **Closed**.

Any **purchase order** created from a **Requisition**:

- will be listed in the **"Purchase Order" window**.
- will have a "**Booked**" status
- and will contain **data inherited from the Requisition**, data such as:
  - Order Date
  - Scheduled Delivery Date
  - Business Partner
  - Price List
  - Product/s

### **Lines**

The user can perform a set of actions regarding requisition lines. It is possible for them to either create lines or product demands or to cancel them.

- **New product demands can be manually created** within a requisition by just **adding new requisition lines** before creating a purchase order.
- **Existing product demands or requisition lines can be cancelled**, if they are not required anymore, by using the header button "**Change Status**".

#### **Matched PO (Purchase order) Lines**

This tab allows the user to either review the purchase order line automatically linked to a requisition line or to manually link an existing purchase order line to the corresponding requisition line.

## Requisition to Order

Requisition to Order window shows all the "Completed" requisitions which match the criteria used in the "filter" section and it also shows the requisition lines selected as locked, therefore the same product demand can not be included more than once in a purchase order.

![Requisition to order](/docs.etendo.software/assets/drive/1Xl_R8oaUrOaO0SK4wB5BYNw3wJDEjHBX.png)

In other words, the upper section of this window shows the requisition lines found that are not linked to an order yet.  
Those are the lines which can be added by the user to the "Lock" area in the bottom section of the window.

A requisition line locked can not be changed by any other user, until the one who locked it gets it unlocked.  
That way, during the time that the requisition lines are locked:

- The same product demand will not be included in a purchase order, by mistake.
- The purchase team will have the opportunity to review the stock and contact different vendors if required to negotiate a price for the products.
- If there is no activity during 3 days, the system removes the lock from the lines.

A requisition can be unlocked manually by the purchase manager or the one who locked it by moving it back to the upper part of the "Requisition to Order" screen by using the "Remove" button.

Once the product demands are clear and locked, the last step to take in this window is to create a purchase order for those needs using the process button "Create".

## Purchase Order

Purchase Order window allows the user to manage orders which once booked will be sent to the external suppliers. In other words, it is a document to register products and/or services to be purchased and documented.

Once the document is booked, it can be sent to the external supplier and it can be prepaid if required.

Purchase orders can be created and booked in the header section of the purchase order window.

### Header

The **Purchase order header** allows you to enter the following information:

- **Organization:** Organizational entity within client.
- **Transaction Document**, which in this case is defaulted as "**Purchase Order**".
- **Document No**, or the Company purchase order number.
- **Order date:** This date is also defaulted by Etendo based on the system date, but it can always be changed.
- **Business Partner**: End-user needs to select the supplier to which the purchase order is being issued.
- **Partner Address**: Automatically populated once the business partner is selected based on the address or location set us "Ship to Address".
- **Warehouse**: Regardless it is defaulted by Etendo based on the "Profile" selected options, it must be verified by the end-user.
- **Scheduled Delivery Date**: This is the date when the organization or legal entity requires the items to be delivered.
- **Payment Method**, **Payment Terms** and **Price List**: These ones are defaulted by Etendo once a business partner is selected.
- **Order Reference**, free text which can be found under "More Information" section, you can use it to save the supplier order number, if any.

**Once header information is properly filled-in, you can go to the "Lines" tab in order to enter purchase order line/s information**.

!!! info
    To learn how to enter purchase order lines, visit the next section "Lines".

It is possible to take up to **three possible actions regarding a purchase order**, by using the **header button "Book"**:

- **Process it**, in case you might want to process it but not to book it as final, because it could be you might need to change it later on.
- **Void it**, in case that purchase order is not required anymore and therefore needs to be voided.
- **Book it**, in case it is correct and final.

![Purchase order window](/docs.etendo.software/assets/drive/1_Jv8WvA53fVRV82tDordRVxJa6xmTEh2.png)

!!! info
    If there are non-stockable BOM products and they have not been exploded, the Book button explodes them automatically.

#### Advanced Remittance

!!! info
    To be able to include this functionality, the Advanced Remittance module of the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}.

The Advanced Remittance module provides the header of the Purchase Order with a new field: “Bank account”.

![bank_account_3.png](/docs.etendo.software/assets/legacy/bank_account_3.png)

This field defines the corresponding bank account for transactions. Each business partner can have more than one bank account and, in this field, the user can select which of them to use.

### **Lines**

Once the purchase order header has been properly filled in and saved, each purchase order line can be created in this tab.

Purchase order lines can be created in three different ways:

**1\. By manually creating new record/s in the "Lines" tab**.

The purchase order fields you can fill in are described below:

- **Product**. You can select an item or product from the list or use the product selector icon.
- **Ordered quantity**, or **Operative Quantity** if the product has an _alternative unit of measure (AUM)_ configured. This is the quantity needed of the product/item.
- Product's **UOM**, or product's **Alternative UOM** depending on product configuration in regards to unit of measure.
- **Attribute Set Value. An attribute associated with a product as part of an attribute set.**
- **Net Unit Price**. This one is coming from the Price List selected in the header, but it could always be changed.
- **Line Net Amount. The final amount of a specified line, based only on quantities and prices.**
- **Tax**. Purchase tax is normally filled in by the system, depending on Taxes setup.

**2\. By retrieving all the lines from previously created purchase orders.** In this case, you must use the process button "**Copy from Orders**".

This process button enables the **Copy from Orders Pick and Edit** window.

"Copy from Orders Pick and Edit" window allows you to search the orders to copy by using the filter options available.

The lines information of the selected orders will be inserted in the purchase order line/s, then that information can be manually changed.

**3\. By copying lines from other purchase orders.**

In this case, you must use the process button **"Copy Lines".**

This process button enables a new window named "Copy Lines from order" which allows you to create order lines by selecting the products already purchased from the supplier of the order by taking into account the _Consumption days_ configured for the supplier.

#### **Explode button**

Explode button is shown when selecting a line with a non-stockable BOM product and the product has not already been exploded. When exploding a product, the bill of materials components the selected product consists of are shown in the order.

!!! info
    Once you have exploded it, you cannot comprime it. You should delete all the lines (first bill of materials components and then the BOM product), and insert again the non-stockable BOM product.

#### **Line Tax**

For each purchase order line, Etendo automatically populates the line tax related information in this tab.

Line tax tab informs about each purchase order line:

- **applied tax rate**
- **calculated tax amount**
- **taxable amount**

!!! info
    It is not possible to either manually create a new line or modify existing ones.

#### **Basic Discounts**

Lists information about discounts automatically applied based on the supplier configuration and / or manually entered for the purchase order.

![Basic discounts](/docs.etendo.software/assets/drive/1AavUV8S8kQ2dp0P_W9lw06XfmAf5d_g-.png)

#### **Payment Plan**

This shows the total amount expected to be paid upon order booking as well as the amount/s pre-paid or paid against the invoice/s for the order.

Payment Plan information is required at order level because suppliers could ask for a **pre-payment** of all or part of a debt prior to its due date.

Purchase order payment plans **do not show nor manage valid due dates**, but the payment plan of the corresponding purchase invoice/s.

This tab also shows information about the regular payments received against the invoice/s for this order, as amounts paid.

Finally, a payment plan of a purchase order will be **removed**:

- if the purchase order is **reactivated**
- or if the purchase order is **voided**

#### **Payment Details**

Displays the details of the payments (pre-payments or regular payments) made for the order or for the invoice/s of the order.

### How to Reactivate a Closed Purchase Order

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}.

Etendo allows the user to reactivate closed purchase orders by selecting the needed one/s and clicking the Undo Close button.

![](/docs.etendo.software/assets/drive/1cyLa7pjnsNgXtnSEK2lZX9s35imhD2Kq.png)

Once the process is finished, the purchase order status turns to booked.

!!! info
    Check the Technical documentation about Advanced Financial Docs Processing to extend the process.

### Payment Removal

The aim of this functionality is to delete and reactivate payments in an agile and easy way. Also, it allows eliminating and reactivating bank transactions and reconciliations.

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

From this window, it is possible to remove payments associated with a purchase order by selecting the corresponding document and then clicking on the Remove Payment button. If there is an invoice associated with the order, the relationship of this invoice to the payment in question will also be removed (Purchase Invoice window > Payment Plan tab).

If the payment is included in the financial account, i.e., if it is in Deposited/Withdrawn not cleared status, the transaction in it will also be deleted (Financial account window > Transaction tab).

If the payment is reconciled through an automatic method, then in addition to the transaction in the financial account, the line of the bank statement to which it was linked (Financial Account window > Imported Bank Statements) and the corresponding line of the bank reconciliation (Financial Account > Reconciliations) will be deleted.

!!! info
    If the payment is posted, the accounting entry is deleted too.

![](/docs.etendo.software/assets/drive/1vTIb8zM4yW3ZXKULoxF96N8nbZdWB0dr.png)

### Intercompany

In case the user has to create orders or invoices among two or more organizations that are different but belong to the same client, this functionality allows automatically generating the corresponding inverse document.

!!! info
    For more information, visit [Functional Documentation about the Intercompany module](/docs.etendo.software/portfolio/etendo-erp/optional-features/bundles/financial-extensions#intercompany)

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

## Goods Receipts

A Goods Receipt is a document issued to acknowledge the receipt of the items listed in it. In other words, it is a document used to register in Etendo the specifics of items physically received in the warehouse.

### **Header**

Goods Receipts can be issued and booked in the header section of the goods receipt window.

![Good receipts header](/docs.etendo.software/assets/drive/1cfAL8uTJ79GodTUOh9qoE66rQ2Me9yG9.png)

The fields to fill in the **Goods Receipt header** are:

- **Document Type**, which is filled in by default as "MM Receipt".
- **Warehouse**, where goods are going to be located.
- **Business Partner**, third party which delivers the goods.
- **Movement Date**, delivery date of the goods.
- **Accounting Date**, accounting date in case of posting the Goods Receipt.
- **Purchase Order**, purchase order number linked automatically by Etendo, in case the Goods Receipt is automatically created from a Purchase Order.
- **Order Reference**, Warehouse team can fill in here the Supplier's Delivery Note number, this way the internal Goods Receipt number and the Supplier's Delivery Note number are linked.

**Once header information is properly filled-in, you can then go to the "Lines" tab in order to enter "Goods Receipt Line/s"**.

!!! info
    To learn how to enter goods receipt lines, visit the next section "Lines".

If a **Goods Receipt** is completed and therefore **booked**:

- The **quantity on hand of the item/s received is increased** by the quantity received.

If a **"Completed" Goods Receipt is voided** because the goods have been returned to the supplier:

- **The quantity on hand of the items/s returned is decreased** by the quantity of the goods returned. Etendo automatically creates a new "Goods Receipt" for exactly the same items but with "negative" quantities.

!!! info
    To learn more about Goods Returns, visit _Return to Vendor_ and _Return to Vendor Shipment_.

Supplier can send a "Purchase Invoice" together with the "Delivery Note" of the goods delivered, therefore:

- From the Goods Receipt window, it is possible to generate the corresponding supplier's invoice, by using the header process button "**Generate Invoice from Receipt**".

This action implies a **link between the goods receipt and the purchase invoice**, the user can be aware of when inquiring about the corresponding purchase invoice.

!!! info
    To learn more, visit _Purchase Invoice._

### **Lines**

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

#### **Accounting**

Accounting information related to the material receipt.

A **"Goods Receipts" can be posted** if the "**MaterialMgmtShipmentInOut**" table is set to Active for accounting in the \[_Active Tables_\] tab of the organization's general ledger configuration.

A "Goods Receipt" posting looks like:

![Good receipts posting](/docs.etendo.software/assets/drive/1mZK5uBnpjcdWbDli0tdWrJc3fCvmR4bg.png)

Posting a "Goods Receipt" requires the calculation of the cost of the contained product/s.

In the case of a goods receipt, that is:

- the purchase price of the product/s
- or the default _standard cost_ of the product/s in case of calculating cost by using an Standard _costing algorithm_.

If there is not a related purchase order, the Costing Server process uses the newer of the following three values:

- the last purchase order price of the receipt's vendor for the product.
- the purchase price list of the product.
- or the _default cost_ of the product.

Moreover:

- The "Legal Entity" organization needs to have a validated _Costing Rule_ configured.
- And the _Costing Background Process_ needs to be scheduled for the _Client_, therefore it can search and allow that the _Costing Server_ process calculates the cost of the transactions.

Once the costs have been calculated, the **Goods Receipt can be posted** to the ledger.

In the case of a receipt containing "Expense" product/s without the "Sales" checkbox selected, it is possible to use the product's purchase price instead of the product's cost to post the goods receipt.

This works if the checkbox _Book Using Purchase Order Price_ is selected for the product/s.

In this case, it is required that a "Purchase Order" is related to the posted "Goods Receipt".

#### **Voiding**

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

#### **Landed Cost**

Landed Cost window allows to allocate additional costs to the goods receipt.

![Landed cost window](/docs.etendo.software/assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

It is possible to enter as many landed cost types/lines as required.

Some relevant fields to note are:

- **Landed Cost Type**: that is the landed cost type that is going to be allocated to the goods receipt.
- **Invoice line**: that is to select the corresponding landed cost invoice line if any, that matches the landed cost type being entered.  
  If an invoice line is selected, the invoice line amount gets populated in the next field "Amount".
- **Amount**: that is the landed cost amount. This amount can be an "estimation" or a "real" amount in case of selecting an invoice line.
- **Landed Cost Distribution Algorithm**: that is the one distributed by Etendo "Distribution by Amount", which means that the landed cost amount is going to be distributed among the goods receipt lines proportionally by receipt line amount.

Once all items above are filled in, including corresponding landed cost purchase invoice line, both "Goods Receipt" and Landed Cost _process matching_ are executed by clicking on the "**Complete**" process button.

### How to Reactivate Goods Receipts

!!! info
    To be able to include this functionality, the Warehouse Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="\_blank"}

From the Goods Receipt window, it is possible to reactivate a previously generated movement just by selecting the corresponding document and clicking the Reactivate button.

Once the receipt is successfully reactivated, the state of the document changes to Draft as it can be observed in the status bar.

![](/docs.etendo.software/assets/drive/1-Z-wUYZfcGDizQ_Kkp8TUYXTs-KnM67H.png)

!!! warning
    Note: It is not possible to reactivate documents that include transactions with quantities exceeding the existing stock quantity for a certain product in a certain storage bin. The only exception is when the configuration of the storage bin allows Over Issue. For more information, visit [Storage Bin](/docs.etendo.software/portfolio/etendo-erp/user-guide/warehouse-management/setup#storage-bin).

### Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [Bulk Posting](/docs.etendo.software/portfolio/etendo-erp/optional-features/bundles/financial-extensions#bulk-posting) in the Financial Extensions Bundle Documentation.

## Pending Goods Receipts

This window allows the user to:

- **Use the Filter options** to narrow down the search of pending purchase orders to be delivered. It is possible to search by:
  - Business Partner
  - From Purchase Order Date -> To Purchase Order Date
  - Purchase Order number
- Enter a **"Reception date".**
- **Select** the "**Order line/s of a purchase order/s" delivered** which are shown grouped by Business Partner and Purchase Order.
- **Change** the "**Quantity**" of the goods being receipt if needed.
- **Enter** the "**Goods receipt location**" or storage bin within a warehouse.
- **Process it** in order to create the corresponding goods receipts.

![Pending goods receipts window](/docs.etendo.software/assets/drive/1hGrJ6YXXd1p20ZdLQefX1o6_8nVogOd8.png)

## Purchase Invoice

The Purchase Invoice window allows the user to register and manage supplier's invoices.

This stage of the chain **usually comes after "Goods Receipts" booking and management**.

A purchase invoice is an itemized statement of the goods or services provided by a vendor or supplier. It indicates the quantity and price of each product or service provided or to be provided.

Suppliers could send the corresponding purchase invoice/s together with the delivery note/s attached to the goods, that implies that "Purchase Invoices" can be automatically generated from the "Goods Receipt" window, but it is possible that this is not the case, therefore a Purchase Invoice can also be created from scratch in the "Purchase Invoice" window.

The purchase expenses can be recognized as soon as the purchase invoice is accounted, however if an expense deferred plan is configured, it is possible to defer the expense recognition as required.

Supplier invoices can be registered, booked and managed in the header section of the purchase invoice window.

### Header

**Header** lists the main terms and conditions related to the purchase invoice.

!!! info
    In the majority of cases, the main (and the only) field needed to create a new purchase invoice document is the Business Partner field. All other fields will be pre-filled automatically based on the selected Business Partner, logged in User preferences and other system default parameters.

Some other fields to note are:

- **Transaction document** defaulted as "AP Invoice" or purchase invoice _document type_ which can be manually changed to either "AP Credit Memo" or "Reversed Purchase Invoice".
  - "AP Credit Memo" and "Reversed Purchase Invoice" document types can be considered credit purchase invoices, the difference between them is that:
    - "AP Credit Memo" type must contain either an "Invoiced Quantity" > 0 or "line Net Amounts" >0.  
      Above implies that invoices set as "Credit Memo" should not be related to "Orders" or "Shipments".
    - "Reversed Purchase Invoice" type must contain either an "Invoiced Quantity" <0 or "line Net Amounts" < 0. These are the invoice types that can be related to return "Orders" or "Shipments".
- **Document No**. you could manually fill in the supplier's invoice number in this field, if the document sequence number associated with the transaction document "AP Invoice" is set up to allow you to do that; otherwise it will be automatically provided by the system as an "Internal" purchase invoice number.
- **Invoice Date**: the date the invoice is registered. It is used to calculate when the payment of the invoice is due. Defaults to the current date can always be changed.
- **Accounting Date**: the date to be used in the posting record of the Purchase Invoice to the general ledger. Defaults to the Invoice Date field can always be changed.
- **Payment Terms**: indicates **how** an invoice should be paid. Defaulted according to the Vendor/Creditor tab of the _Business Partner_ window.
- **Payment Method**: defines **when** a purchase invoice needs to be paid. Defaulted according to the Vendor/Creditor tab of the _Business Partner_ window.
- **Supplier Reference**: this is a not-mandatory field which can be used to enter the supplier invoice number.

There are 3 ways of entering lines into the purchase invoice, two of them from the invoice header and the last one from the **Lines** tab:

1.  Selecting products from pending to be invoiced orders or receipts using the _Create Lines From Order and Create Lines From Receipt_ buttons.
2.  Copying all products from the chosen invoice selected in the history of all invoices for different business partners using the _Copy Lines_ button.
3.  Manually, line by line in the _Lines_ tab. This option is used if the underlying document (Purchase Order or Goods Receipt) does not exist in the system prior invoicing takes place.

The **Complete** button finishes the creation of the invoice document with the fulfillment of the _Payment Plan_ tab and the _Payment Monitor_ section in the Header. If there are non-stockable BOM products in the lines and they have not been exploded, the Complete button will explode them automatically.

Once completed, a purchase invoice can be:

- **posted** to the ledger by using the button _Post_
- **voided** by using the button _Reactivate_
- and **paid** by using the button _Add Payment_.

![Purchase invoice window](/docs.etendo.software/assets/drive/1JvS1mOjiiyATJENTs5SuQIyEAr-UHmE3.png)

#### Advanced Remittance

!!! info
    To be able to include this functionality, the Advanced Remittance module of the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}.

The Advanced Remittance module provides the header of the Purchase Invoice with a new field: “Bank account”.

![bank_account.png](/docs.etendo.software/assets/legacy/bank_account.png)

This field defines the corresponding bank account for transactions. Each business partner can have more than one bank account and, in this field, the user can select which of them to use.


???+ note
    When using the option “Create lines from orders”, if all orders have the same bank account, the invoice uses that bank account. If not, it uses the default one.

### **Lines**

Once the purchase invoice header has been properly filled in and saved purchase invoice lines can be registered in this tab.

Lines list each product to be purchased and its characteristics.

The fields to note are:

- **Financial Invoice Line** is selected when the invoice line is not a product but an account not set up as a product but as a _G/L Item_, or an asset not set up as a product.  
  When selected, the product field disappears from the screen and an account field appears related to the purchase invoice line.
- **Attribute Set Value**: field is displayed if the product in the line has _attributes_ (color, size, serial number or several of them together etc).
- **Purchase Order Line and Goods Receipt Line**: references to the purchase order and goods receipt line that is being invoiced.

As already mentioned, purchase expenses can be deferred therefore they are not recognized at the purchase accounting date but within a given number of accounting periods.

When a purchase invoice line is created, it is possible to define at line level whether the line is going to cause the expense to be deferred. The relevant fields are:

- **Deferred Expense**: When this flag is checked, the Expense Plan field group becomes visible, allowing users to configure the next three fields.
- **Expense Plan Type**: This field specifies the frequency of the expense distribution which currently is "monthly".
- **Period Number**: This field specifies the duration of an expense plan.  
  For instance, if a company purchases business insurance for the duration of the year, the period number to enter would be 12 as the company would like to distribute that expense over 12 months.
- **Starting Period**: The first open period in which the expense is going to be recognized.

These fields can be defaulted if configured for the _product_.

If an expense plan is configured, it implies a specific _purchase invoice accounting_.

**Explode** button is shown when selecting a line with a non-stockable BOM product and the product is not already exploded. When exploding a product, the bill of materials components the selected product consists of are shown in the invoice. Once you have exploded it, you cannot comprime it. You should delete all the lines (first bill of materials components and then the BOM product), and insert again the non-stockable BOM product.

**Match LC Cost** button is shown when the purchase order line contains either an "account" or a "product" setup as _landed cost type_.

This process button allows to **match** both the "**estimated**" landed cost booked in the _landed cost_ window, and the one being **invoiced** in the invoice line. Both need to be of the very **same landed cost type**.

Once selected, **"Match LC Cost**" button opens the **"Match LC Cost" pick and edit window**.

Only processed Landed Cost documents will be shown in this Window. It allows you to pick the corresponding landed cost, to enter an amount to match in the field "Matched Amt", and then to select the "**Process Matching**" check-box.

!!! warning
    Note that if the "Process Matching" check-box is not selected here, landed cost matching will have to be processed in the _landed cost_ window by using **Process Matching** button.

### How to Reactivate a Voided Purchase Invoice

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}.

Etendo allows the user to reactivate voided purchase invoices by selecting the needed one/s and clicking the Unvoid button.

![](/docs.etendo.software/assets/drive/1UisxZzbpppLvN_rdL__TJg8tLeh5sMfW.png)

Once the process is finished, the sales invoice status turns to Complete.


???+ note 
    In the case of the standard version of the module, it is necessary for the user to also unvoid the corresponding reversed invoice.
!!! warning
    Remember that this reactivation process affects the accounting, since, if the original information is not manually removed from the reactivated document, the accounting information will be doubled.

!!! info
    Check the Technical documentation about Advanced Financial Docs Processing to extend the process.

### Payment Removal

The aim of this functionality is to delete and reactivate payments in an agile and easy way. Also, it allows eliminating and reactivating bank transactions and reconciliations.

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

From this window, it is possible to delete payments associated with a purchase invoice by selecting the corresponding document and then clicking on the Remove Payment button. If there is an order associated with the invoice, the relationship of this order to the payment in question will also be deleted (Purchase Order window > Payment Plan tab).

If the payment is included in the financial account, i.e., if it is in Deposited/Withdrawn not cleared status, the transaction in it will also be deleted (Financial account window > Transaction tab).

If the payment is reconciled through an automatic method, then in addition to the transaction in the financial account, the line of the bank statement to which it was linked (Financial Account window > Imported Bank Statements) and the corresponding line of the bank reconciliation (Financial Account > Reconciliations) will be deleted.

!!! info
    If the payment is posted, the accounting entry is deleted too.

![](/docs.etendo.software/assets/drive/1k1K_gD4JMVrUriXiCYzG_9RkYMwG8BZz.png)

### Intercompany

In case the user has to create orders or invoices among two or more organizations that are different but belong to the same client, this functionality allows automatically generating the corresponding inverse document.

!!! info
    For more information, visit [Functional Documentation about the Intercompany module](https://docs.etendo.software/en/modules/financial-extensions-bundle/intercompany)

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

### Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [Bulk Posting](/docs.etendo.software/portfolio/etendo-erp/optional-features/bundles/financial-extensions#bulk-posting) in the Financial Extensions Bundle Documentation.

## Matched Invoices

This window helps the user to post the discrepancies between inventory and financial accounting of those items for which the corresponding goods receipts were posted.

Above mentioned discrepancies are mainly caused by differences between:

- the **item's net unit price registered when booking the purchase order** and later on **posting the corresponding Goods Receipt.**
- and the **"final" item's net unit price registered when posting the purchase invoice.**

In the window, there is a listing of all invoices that are matched to goods receipts. The matching of the documents is done when documents are created by using the information of the other document: for example by clicking the Generate Invoice from receipt on the goods receipt or by clicking the Create Lines from button when creating a goods receipt to select the invoice.

![Matched invoices window](/docs.etendo.software/assets/drive/1AUhlJDfTAknIjUueLpm4QCCmZSwz1vBg.png)

#### **Matched Invoice**

Matched invoice tab lists each invoice line posted linked to the corresponding goods receipt lines, which could also be posted or not.

There is a "**Post**" header button which is the one that posts the discrepancies between inventory and financial accounting if any, once the proper line has been selected.

The general process to post the discrepancies in accounting is detailed below:

A _Matching Invoice_ document can be posted if the cost of the products included in a _Goods Receipt_ has been calculated. To obtain that:

- A validated _Costing Rule_ is required in the Matched Invoice's legal entity,
- and the background process _Costing Background Process_ must be run.

In the case of "Expense" product/s do not having the "Sales" checkbox selected, it is possible to use the product's purchase price instead of the product's cost whenever the checkbox _Book Using Purchase Order Price_ is selected. In this case, it is required that a "Purchase Order" is related to the "Goods Receipt".

#### **Accounting**

Accounting information related to the matched invoices

### Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [Bulk Posting](/docs.etendo.software/portfolio/etendo-erp/optional-features/bundles/financial-extensions#bulk-posting) in the Financial Extensions Bundle Documentation.

## Return to Vendor (RTV)

This window allows the user to create a Return Material document in case a given product needs to be sent back either to be returned for a refund or replacement, or to be repaired.

### **Header**

The user can create a purchase order and process it.

Once the Return Material document is accepted by the Vendor, the user can process it by clicking the button **Book**. The document changes from _Draft_ to _Booked._

![Return to vendor window](/docs.etendo.software/assets/drive/1PKb2NIyq5HtvO_4abDPQjajObdcGFiPH.png)

Only _Booked_ documents can be shipped to the vendor.

!!! warning
    Notice the button **Pick/Edit lines** disappears when the Return to vendor document is in status _Booked._

### **Lines**

Add products to be included in your purchase order. Each product is added by creating a line.

The Lines tab is not editable, since the returned lines always come from receipt lines, to avoid:

- Seeing positive values while negative in the DB.
- Entering lines that are not linked to the original receipt lines.
- Editing attributes, products and so having either the products or attributes different from the shipment line.

To enter new lines you need to click the process button PICK/EDIT Lines.

**Things to consider:**

- The only editable fields are:
  - **Returned**: Quantity you wish to return. When selecting the row, the quantity is not set by default since the system cannot know how many items return.
  - **Net Unit Price**: Price of the original purchase order.
  - **Return reason**: The reason why you return the item.
  - and **Returned UOM**, only in case \*alternative unit of measure (AUM)\*preference is enabled.  
    In that case, product's "primary" AUM for the purchase flow is shown if any, otherwise product's UOM is shown. The user can always change it to product's UOM.

You can define the Return Reason at header level. In this case when picking a line it inherits what selected in the header but you can modify it as you wish.

- Only Material receipt documents that have not been still returned can be picked it, in case a Receipt line has been fully returned it will not be shown.
- When a Receipt line has been partially returned you can still return the rest. What you have already returned for that line is shown in the field **Return Qty other R.**

**Validations:**

- You are not allowed to return more quantity than the **Ship/Receipt Qty**. In case you do it a message is shown.
- Notice that this validation takes into account the **Return Qty other RM** field

!!! info
    To edit a line you need to click again the **Pick/Edit Lines** button and the line appears selected and then you can modify any of the editable fields.

!!! info
    To delete a line you need to unmark the line and then click Done.

## Return to Vendor Shipment

From this window, the user can deliver the returned goods to the vendor.

### **Header**

The user can create and edit a goods receipt.

The **RMA vendor ref.** field is populated automatically or not based on:

- If it is filled before selecting a line, then it will not be populated automatically to avoid override it.
- If you select a line/s where all of them belong to the same Return to Vendor document, it will be populated automatically.
- If you select a line/lines but one of them belongs to a different Return to Vendor document, then it will not be populated automatically.

Once the document is ready, you can process it by clicking the button **Complete**. The document changes from _Draft_ to _Completed._

!!! warning
    Notice the button **Pick/Edit lines** disappears when the Return to vendor document is in status _Completed._

![Return to vendor shipment](/docs.etendo.software/assets/drive/1wuiYHH8xsIwjLRgp0VzWUqAtev43BzD8.png)

To invoice these documents you must use the **Purchase invoice** window. All scenarios are covered:

- If the vendor sends an invoice just for that specific document you need to select a _Reverse purchase invoice_ document type and then select the lines through the _Create lines_ from button.
- If the vendor sends an invoice with the original purchase order plus the return materials order you need to select a _Purchase invoice_ document type and then select the lines through the _Create lines_ from button.
- If the vendor does not send an invoice for the return materials order but wants to keep it as credit where you can use it later, you have to:
  - Create a _Reverse purchase invoice_ for these returned materials.
  - Leave it as credit to be used later through the **Payment out** window.
  - When you create the Purchase invoice for the original Purchase order you can consume that credit.

### **Lines**

Add products which are included in your goods receipt. Each product is shown on its own line.

The Lines tab is not editable, since the lines always come from return to vendor lines, to avoid:

- Seeing positive values while negative in the DB.
- Entering lines that are not linked to return lines.
- Editing attributes, products and so having either the products or attributes different from the return line.

!!! info
    To enter new lines, the user needs to click the button PICK/EDIT Lines.

**Things to consider:**

- Editable fields are:
  - **Ship Qty**, that value is set automatically when you select the line,
  - and **Returned UOM**, only in case an alternative unit of measure (AUM) preference is enabled, regardless product's UOM is always shown there by default.  
    The user can change it if required, to the product's primary AUM configured for the procurement flow.
- The user can only select Return to Vendor lines that are pending to be shipped to that specific vendor.
- The system proposes the different storage bins from where the item can be picked. Depending how the product is configured we could have three scenarios:
  - Product with an instance attribute (i.e: Serial number): The system will propose only one storage bin as it is shown above.
  - Product with a non-instance attribute (i.e: Colour): The system could propose several storage bins. See below image
  - Product without attributes. Similar to second scenario.

**Validations:**

- You are not allowed to ship more than the **Available Qty.**
- You are not allowed to ship more than the **Pending** quantity.
- The system also validates you cannot ship more than the **Pending** quantity when selecting both lines.

!!! info
    To edit a line, you need to click the **Pick/Edit Lines** button again, the line appears selected and then you can modify any of the editable fields.

!!! info
    To delete a line, you need to unmark the line and then click Done.

If there is not enough available stock for a product in a selected line, then it will be possible to define a Ship Quantity and select it. if there is at least one storage bin with overissue inventory status for the Return To Vendor Shipment's warehouse, in this case the new line will use it as storage bin and it will create a negative stock when the document is processed.

#### **Accounting**

The RTV shipment can be posted **if the table "MaterialMgmtShipmentInOut" is** active for accounting **in the corresponding general ledger configuration.**

### Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [Bulk Posting](/docs.etendo.software/portfolio/etendo-erp/optional-features/bundles/financial-extensions#bulk-posting) in the Financial Extensions Bundle Documentation.

## Landed Cost

Landed Cost window allows the user to allocate additional costs such as freight, insurance or duties to goods receipt(s), therefore the cost of the products included in the receipt(s) is adjusted as applicable.

All those costs are needed to place the product in the organization's warehouse.

Every time that a landed cost is booked for a product receipt valued at "Average" cost, a landed cost adjustment is created.

Landed costs distributed and allocated to products valued at "Average" cost imply a change in the inventory value of the product. In other words, the calculated cost ("Total Cost") of the product receipt will need to be adjusted the same as the "Average" cost of the product.

!!! info
    Note that the "Unit Cost" of the receipt transaction will not change as this type of adjustment is not a unit cost adjustment type but an "extra" cost.

All of the above will have an accounting impact, therefore product inventory value can be the same as product accounting value.

On the other hand, if a landed cost is booked for a product receipt valued at "Standard" cost, no cost adjustment will be created but a "Variance" between the "standard" cost defined for the product and its "actual" cost. This variance will need to be posted to a "Landed Cost Variance" account, so it can be later on analysed.

Landed cost window allows both:

- either to book "**estimated**" landed cost that can be later on matched against "actual" landed cost by landed cost type,
- or directly book "**actual**" landed cost by landed cost type.

Landed cost window also allows to post landed costs once processed.

"**Estimated**" Landed Cost scenario:

- A purchase order is booked and after that the corresponding goods receipt and purchase invoice.  
  The "average" cost of the products included in the receipt is calculated at this point.
- After that "estimated" landed costs (i.e freight costs) are allocated to the goods receipt and booked in the landed cost window.  
  The cost of the products included in the receipt is then adjusted the same as products asset accounting.
- After that, a purchase invoice including the actual amount of freight cost is booked and posted to the ledger.
- Then, it is possible to match "estimated" landed cost against "invoiced" landed cost.  
  The cost of the products included in the receipt is adjusted once more if there are differences between estimated and actual landed cost amounts.

"**Actual**" Landed Cost scenario:

- A purchase order is booked and after that, the corresponding goods receipt and purchase invoice.  
  The "average" cost of the products included in the receipt is calculated at this point.
- After that, a landed cost document is created to record actual landed cost to the goods receipt.  
  The cost of the products included in the receipt is then adjusted the same as products asset accounting.

In Summary, landed cost feature follows below detailed steps:

- **Landed Cost Process**:
  - A landed cost document is created including as many different landed cost types and amounts as required.
  - This landed cost document can be related to a single goods receipt, to several goods receipts or to specific goods receipts lines.
  - This landed cost document can record "actual" landed cost in case of selecting the corresponding invoice, therefore the landed cost process and matching is done in one step.
  - Landed cost is processed.
    - This action creates a _landed cost adjustment_ linked to the landed cost document.  
      This cost adjustment has as many adjustment lines as products included in the goods receipt(s) selected, therefore the cost of those products is adjusted as applicable.
- **Landed Cost Post**:
  - Once a landed cost document is processed it can be posted to the ledger, therefore product(s) asset accounting is adjusted as well.
- **Landed Cost Matching**:
  - Landed cost invoice is booked and posted to the ledger later on.
  - After that the "estimated" landed cost booked in the landed cost document can be matched against actual landed costs by landed cost type in the landed cost invoice.
  - Landed cost matching can generate an additional cost adjustment for the product(s) if estimated landed cost amounts were not the same as actual landed cost amounts.
- **Landed Cost Matching Post**:
  - Once landed cost(s) are matched can be posted therefore:
    - product(s) asset accounting is adjusted once more if applicable,
    - and landed cost posting gets landed cost invoice _accounting dimensions._

### Header

A Landed Cost document can be created, processed and posted in this window.

![Landed cost header](/docs.etendo.software/assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

Some fields to note are:

- **Organization**: that is the organization or legal entity for which landed cost needs to be booked.
- **Reference date**: that is the date when the landed cost document is being created.

**Cost**

A Landed Cost Document can have as many cost (lines) as landed cost types to allocate to the Goods Receipt(s) selected.

![Landed cost tabs](/docs.etendo.software/assets/drive/1jbfoYTDqyRZiF3bTwPQkG8OmjpLr0zau.png)

Some fields to note are:

- Landed Cost Type: that is the landed cost type that is going to be allocated to the receipt(s) or receipt line(s) selected in Receipt tab.
- **Invoice line**: that is to select the corresponding landed cost invoice line if already booked that matches the landed cost type being entered.  
  If an invoice line is selected,the invoice line amount gets populated in the next field "Amount".
- **Amount**: that is the landed cost type amount. This amount can be "estimated" or "actual" in case of selecting an invoice line.
- **Currency**: that is the currency of the landed cost type.
  - It is important to remark that a landed cost document can include as many landed cost types as required in the currency required.  
    For instance, a landed cost document can include two landed cost type lines one in USD and the other one in EUR.  
    In this scenario, a landed cost adjustment will be created including two lines. Cost adjustment amounts will be calculated in the currency configured for the legal entity product transaction belongs to.
- **Landed Cost Distribution Algorithm**: there is one algorithm available distributed by Etendo that is "Distribution by Amount".  
  This algorithm distributes landed cost type amount proportionally by receipt line(s) amount among the receipt(s) selected.

Once a receipt(s) has been selected in Receipt tab, landed cost document (header) can be processed by using the process button "**Process**".

This action creates a landed cost adjustment linked to the landed cost document.

This cost adjustment has as many adjustment lines as products included in the goods receipt(s) selected, therefore the cost of those products is adjusted as applicable.

Once processed, a landed cost document can be:

- **"Reactivated"**, this action voids the landed cost adjustment linked to the landed cost document.
- or **"Post"**, therefore product asset accounting is also adjusted accordingly.

**Landed Cost** posting creates the following accounting entries in case of a "Product" landed cost type:

|                 |                                                                                                                                                           |                                |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Account         | Debit                                                                                                                                                     | Credit                         |
| Product Asset   | "Estimated" Landed Cost Amount.<br><br>(\*)This ledger entry gets goods receipt "accounting dimensions" such as "Vendor" or "Product". See "Detail" link. |                                |
| Product Expense |                                                                                                                                                           | "Estimated" Landed Cost Amount |

**Landed Cost** posting creates the following accounting entries in case of an "Account" landed cost type:

|                   |                                                                                                                                                           |                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Account           | Debit                                                                                                                                                     | Credit                         |
| [_Product Asset_] | "Estimated" Landed Cost Amount.<br><br>(\*)This ledger entry gets goods receipt "accounting dimensions" such as "Vendor" or "Product". See "Detail" link. |                                |
| [_G/L Item_]      |                                                                                                                                                           | "Estimated" Landed Cost Amount |

##### **Process Matching**

Matching between an "estimated" landed cost and an "invoiced" landed cost can be processed in:

**1.** The **GOODS RECEIPT** window before processing and by using the process button "**Complete**"

This scenario takes place whenever all landed cost related information below is available and entered in the Landed Cost tab of the **Goods Receipt** :

- landed cost types
- landed cost amounts
- related landed cost invoice lines

This scenario automatically creates:

- a landed cost document in the **landed cost** window related to the goods receipt that contains all the information entered in the "Landed Cost" tab of the Goods Receipt.  
  This landed cost document is already processed and matched, therefore only actions missing are to post the landed cost document (header) and to post the landed cost matching.
- a landed cost adjustment that adjusts the cost of each product included in the Goods Receipt.

**2**. The **Landed Cost PURCHASE INVOICE** window, by using the process button Match LC Cost which can be found in each landed cost purchase invoice line. After that **"Process Matching" check-box** is selected.

This scenario takes place whenever:

- all landed cost related data but landed cost invoice line information was entered in the Landed Cost tab of **Goods Receipt** window.
- all landed cost related data but landed cost invoice line information was entered in the Cost tab of **Landed Cost** window.

This scenario automatically creates:

- a new landed cost adjustment that adjust once more the cost of each product included in the Goods Receipt if:
  - the landed cost type amount booked is not the same as the one invoiced
  - and the check-box "Is matching adjusted" is selected.
- only action missing is to post the landed cost matching.

**3.** The **LANDED COST** window, by using the process button "**Process Matching**"

This scenario takes place whenever the matching has been executed in the landed cost purchase invoice, see scenario 2 above, but the check-box "Process Matching" was not selected there.

This scenario automatically creates:

- a new landed cost adjustment that adjusts once more the cost of each product included in the Goods Receipt if the landed cost type amount booked is not the same as the one invoiced and the check-box "Is matching adjusted" is selected.
- only action missing is to post the landed cost matching.

**4.** The **LANDED COST** window, by using the process button "**Process**".

This scenario takes place whenever all landed cost related information is entered in the **landed cost** window.:

- landed cost types
- landed cost amounts
- related landed cost invoice lines
- and goods receipt(s)

This scenario automatically creates:

- a landed cost adjustment that adjust the cost of each product included in the Goods Receipt(s).
- only actions missing are to post the landed cost document (header) and to post the landed cost matching.

##### **Post Matching**

A landed cost matching can be posted, after being processed. This posting will have different ledger entries depending on the scenarios listed below:

1\. "**Estimated**" landed cost **equal** to "**invoiced**" landed cost

- In the case of a "product" landed cost type

|                     |                                           |                                                                                                                                                                        |
| ------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                                     | Credit                                                                                                                                                                 |
| [_Product Expense_] | "Estimated"="Invoiced" Landed Cost Amount |                                                                                                                                                                        |
| [_Product Expense_] |                                           | "Estimated"="Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

- In the case of an "account" landed cost type

|              |                                           |                                                                                                                                                                        |
| ------------ | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account      | Debit                                     | Credit                                                                                                                                                                 |
| [_G/L Item_] | "Estimated"="Invoiced" Landed Cost Amount |                                                                                                                                                                        |
| [_G/L Item_] |                                           | "Estimated"="Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

The purpose of above ledger entries is to get that landed cost expense accounting gets invoice landed cost "accounting dimensions".

2\. "**Estimated" landed cost not equal to "invoiced" landed cost** & **"Is matching adjusted" = No**.

This last setup ("Is matching adjusted" = No) leads to NOT creating a landed cost adjustment which takes the difference to the product cost (product accounting), therefore that difference remains either in the credit side (estimated>invoiced) or in the debit side (estimated<invoiced) of the product expense account.

- In the case of a "product" landed cost type

|                     |                               |                                                                                                                                                            |
| ------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                         | Credit                                                                                                                                                     |
| [_Product Expense_] | "Invoiced" Landed Cost Amount |                                                                                                                                                            |
| [_Product Expense_] |                               | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

- In the case of an "account" landed cost type

|              |                               |                                                                                                                                                            |
| ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account      | Debit                         | Credit                                                                                                                                                     |
| [_G/L Item_] | "Invoiced" Landed Cost Amount |                                                                                                                                                            |
| [_G/L Item_] |                               | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

3\. "**Estimated**" landed cost **higher** than "**invoiced**" landed cost. **"Is matching adjusted" = Yes**

This last setup ("Is matching adjusted" = Yes) leads to creating a landed cost adjustment which takes the difference to the product cost (credit side of product accounting).

- In the case of a "product" landed cost type

|                     |                                |                                                                                                                                                            |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                          | Credit                                                                                                                                                     |
| [_Product Expense_] | "Estimated" Landed Cost Amount |                                                                                                                                                            |
| [_Product Expense_] |                                | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |
| [_Product Asset_]   |                                | Difference (estimated>invoiced) Landed Cost Amount                                                                                                         |

- In the case of an "account" landed cost type

|                   |                                |                                                                                                                                                            |
| ----------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account           | Debit                          | Credit                                                                                                                                                     |
| [_G/L Item_]      | "Estimated" Landed Cost Amount |                                                                                                                                                            |
| [_G/L Item_]      |                                | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |
| [_Product Asset_] |                                | Difference (estimated>invoiced) Landed Cost Amount                                                                                                         |

4\. "**Estimated**" landed cost **smaller** than "**invoiced**" landed cost. **"Is matching adjusted" = Yes**

This last setup ("Is matching adjusted" = Yes) leads to creating a landed cost adjustment which takes the difference to the product cost (debit side of product accounting).

- In the case of a "product" landed cost type

|                     |                                                    |                                                                                                                                                            |
| ------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                                              | Credit                                                                                                                                                     |
| [_Product Asset_]   | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [_Product Expense_] | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [_Product Expense_] |                                                    | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

- In the case of an "account" landed cost type.

|                   |                                                    |                                                                                                                                                            |
| ----------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account           | Debit                                              | Credit                                                                                                                                                     |
| [_Product Asset_] | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [_G/L Item_]      | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [_G/L Item_]      |                                                    | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

##### **Cancel Matching**

A landed cost matched can be canceled by using header process button "**Cancel Matching**". Before that landed cost matching needs to be "Unpost".

Cancel matching action implies that:

- Current matched amounts are not removed from Matched Amount tab.
- A new matching needs to be executed in the corresponding landed cost purchase invoice(s).
- Correct matching amounts will then be updated in Matched Amount tab.

#### **Matched Amount**

Matched Amount tab is a read only tab that allows to review the purchase invoice lines matched against landed cost lines.

IMG

#### **Accounting Cost**

This tab provides Landed Cost document accounting information.

As any other accounting tabs, this tab shows the ledger journal entries of landed cost posting.

IMG

#### **Receipt**

Receipt tab allows the user to select either the receipt(s) or receipt line(s) to which landed cost types booked are going to be allocated.

Once **Landed Cost** header has been properly filled in and saved, a receipt(s) line can be registered in this tab.

Landed cost amounts entered in the "Cost" tab can then be allocated/distributed among the receipt(s) entered here.

Some relevant fields to note are:

- **Good Receipt**: that is to select a goods receipt, therefore landed cost amounts will be distributed among all the lines of the goods receipt.
- **Good Receipt Line**: that is to select a specific good receipt line.

Note that either a good receipt or a good receipt line needs to be selected in a record.

#### **Receipt Line Amount**

Receipt Line Amount is a read only tab that shows detailed information about the landed cost type line allocated to each receipt line, as well as the landed cost amount distributed to each receipt line.

It is important to remark that the "Amount" distributed is calculated by taking into account "Costing" precision defined for the Currency.

#### **Accounting**

This tab provides Landed Cost Matching accounting information.

### Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button. In this case, this functionality can be used in the "Landed Cost" window and in the "Cost" tab.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [Bulk Posting](/docs.etendo.software/portfolio/etendo-erp/optional-features/bundles/financial-extensions#bulk-posting) in the Financial Extensions Bundle Documentation.

---

This work is a derivative of ["Procurement Management"](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
