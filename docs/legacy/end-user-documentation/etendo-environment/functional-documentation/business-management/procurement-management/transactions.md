---
title: Transactions
---
Procurement management deals with all the activities related to the purchase of goods and services from external suppliers and the corresponding reporting.

This Etendo Application area covers two main functionalities:

- Transactions
- Analysis Tools

Within Transactions, the following functionalities are displayed:
- Requisition
- Manage Requisitions
- Requisition To Order
- Purchase Order
- Goods Receipt
- Pending Goods Receipts
- Purchase Invoice
- Matched invoices
- Return to Vendor
- Return to Vendor Shipment
- Landed Cost

The process starts by the creation and management of purchase requisitions and corresponding purchase orders to the moment the warehouse staff receives the merchandise. 

### Requisition

A Requisition is a document that specifies a request to order products.

The user can create requisitions and monitor them in this window.  
Requisition header allows entering the following data:

-   The business partner or **supplier**, this is an optional field that could be filled in by the requester in case it is known, therefore:
    -   The **supplier entered in the header** will be the one **used for every requisition line unless it is changed** at lines level for a particular line.
    -   If there is **no supplier entered in the requisition header** the **one setup by default for the product** in its master data window, "**Purchasing**" tab will be used.
    -   If **there is no business partner or supplier** in the header, or in the lines, or setup in the product, **the user will have to enter it while creating the purchase order from the requisition**.
-   The **purchase price list**. This is also an optional field to be filled-in, in case it is known by the requester and its behaviour is the same as described above as it is linked to the Business Partner.

Besides, the system populates the following data:

-   The **document No.**, which is the Requisition number.
-   The **requester**, which is the user entering the requisition.

The requester can then move to the "**Lines**" tab to enter **additional data**.

#### **Lines**

Each requisition line shows a product demand for a specific date.

Requisition "Lines" tab collects the following demand data:

-   The **need by date**, that is the date when the product is required to arrive.
-   The **product**, items/products which need to be purchased.
-   The **quantity** requested, or the **operative quantity** requested if the product has an *alternative unit of measure (AUM)* configured.
-   The product's **UOM**, or product's **Alternative UOM** depending on product configuration in regards to measure unit.
-   The **business partner:** This is an optional field the user can enter if the supplier entered at the requisition header needs to be changed for a particular line.

!!! warning
    If there is not a supplier entered at the requisition header, neither at the requisition line, the supplier used will be the one setup by default for the product, therefore this field at line level can also be used to overwrite that defaulted one.



-   The **purchase price list**: This is also an optional field that can be entered if the price list entered at the header level or the default product price list information should be overwritten for a particular line.
-   The **net list price**: This one is the price of the corresponding price list for a given date. It's an optional field that can be filled in automatically based on the price list entered at the header level or it could be overwritten by the user for a particular product line.
-   The **net unit price:** This one can be either equal to the net list price or not, based on the formula: \[net unit price = net list price - discount\]. It is an optional field that can be filled in automatically based on the price list entered at the header level or it could be overwritten by the user for a particular product line.
-   The **discount**, if any, is based on a used price list.

It is possible to enter as many requisition lines as products demand.

The last step is to register the "**Requisition**" as "**Complete**" by using the header button "Complete", then:

-   **Requisition header status bar** informs us that the Requisition is "**Completed**".
-   **Requisition lines status bar** informs us that the "**Matched purchase order quantity" for each line is equal to 0**, as there is no purchase order linked to each requisition line yet, and the requisition line/s status is "**Open**".

It is important to remark that "**Requisitions**" does not have any impact on:

-   Items quantity on hand
-   Items costing

### Manage Requisitions

Manage Requisitions window is intended to be used to provide an overall picture of the items needed.

#### Header

This window allows the user to manage requisitions regardless of their current status, therefore they can change or close a requisition and create purchase orders for those demands.

A **requisition** with status "Completed" **can always be changed**, if required. The user needs to reactivate it and then change it and book it.

It is also possible to **close a requisition in case there is no need of the included item/s anymore**, by using the menu button "**Close**" and then select the action "**Close**".

Requisition lines status will then be changed to "Cancelled".

Finally, it is also possible to **create purchase orders** for those **requisitions in status "Complete"**, by using the menu button "**Create Purchase Order**".

In this case, a new window is shown for the user to fill in some data by taking into account that:

-   If there are **different suppliers in the requisition lines as well as price list**:
    -   the **defaulted ones** entered in the window "Create Purchase Order" **will be the ones used** in the purchase order.
-   If there are **different suppliers in the requisition lines as well as price list**, and the user does not enter any defaulted ones in the window "Create Purchase Order":
    -   **the ones in the requisition lines will be the ones used** in the purchase orders.
-   If **all the requisition lines have the same supplier and price list**:
    -   **there will not be any need for selected defaulted ones** in the window "Create Purchase Order", besides only one purchase order will be created.

Etendo provides information about the purchase order/s number/s created after pressing the OK button in the "Create Purchase Order" window.

This action links the requisition and the purchase order, and besides a purchase order line is created for each requisition line:

-   A **requisition** linked to a purchase order changes its status from **Completed** to **Closed**.
-   A **requisition line** linked to a purchase order line changes its status from **Open** to **Closed**.

Any **purchase order** created from a **Requisition**:

-   will be listed in the **"Purchase Order" window**.
-   will have a "**Booked**" status
-   and will contain **data inherited from the Requisition**, data such as:
    -   Order Date
    -   Scheduled Delivery Date
    -   Business Partner
    -   Price List
    -   Product/s

#### **Lines**

The user can perform a set of actions regarding requisition lines. It is possible for them to either create lines or product demands or to cancel them.

-   **New product demands can be manually created** within a requisition by just **adding new requisition lines** before creating a purchase order.
-   **Existing product demands or requisition lines can be cancelled**, if they are not required anymore, by using the header button "**Change Status**".

#### **Matched PO (Purchase order)  Lines**

This tab allows the user to either review the purchase order line automatically linked to a requisition line or to manually link an existing purchase order line to the corresponding requisition line.

### Requisition to Order
Requisition to Order window shows all the "Completed" requisitions which match the criteria used in the "filter" section and it also shows the requisition lines selected as locked, therefore the same product demand can not be included more than once in a purchase order.

In other words, the upper section of this window shows the requisition lines found that are not linked to an order yet.
Those are the lines which can be added by the user to the "Lock" area in the bottom section of the window.
 
A requisition line locked can not be changed by any other user, until the one who locked it gets it unlocked.
That way, during the time that the requisition lines are locked:
 
- The same product demand will not be included in a purchase order, by mistake.
- The purchase team will have the opportunity to review the stock and contact different vendors if required to negotiate a price for the products.
- If there is no activity during 3 days, the system removes the lock from the lines.
 
A requisition can be unlocked manually by the purchase manager or the one who locked it by moving it back to the upper part of the "Requisition to Order" screen by using the "Remove" button.
 
Once the product demands are clear and locked,  the last step to take in this window is to create a purchase order for those needs using the process button "Create".


### Purchase Order

Purchase Order window allows you to create and manage orders which once booked will be sent to the external suppliers. In other words, it is a document to register products and/or services to be purchased and documented.

Once the document is booked, it can be sent to the external supplier and it can be prepaid if required.

Purchase orders can be created and booked in the header section of the purchase order window.

The **Purchase order header** allows you to enter the following information:

-   **Organization:** Organizational entity within client.
-   **Transaction Document**, which in this case is defaulted as "**Purchase Order**".
-   **Document No**, or the Company purchase order number.
-   **Order date:** This date is also defaulted by Etendo based on the system date, but it can always be changed.
-   **Business Partner**: End-user needs to select the supplier to which the purchase order is being issued.
-   **Partner Address**: Automatically populated once the business partner is selected based on the address or location set us "Ship to Address".
-   **Warehouse**: Regardless it is defaulted by Etendo based on the "Profile" selected options, it must be verified by the end-user.
-   **Scheduled Delivery Date**: This is the date when the organization or legal entity requires the items to be delivered.
-   **Payment Method**, **Payment Terms** and **Price List**: These ones are defaulted by Etendo once a business partner is selected.
-   **Order Reference**, free text which can be found under "More Information" section, you can use it to save the supplier order number, if any.

**Once header information is properly filled-in, you can go to the "Lines" tab in order to enter purchase order line/s information**.

!!! info
    To learn how to enter purchase order lines, visit the next section "Lines".


It is possible to take up to **three possible actions regarding a purchase order**, by using the **header button "Book"**:

-   **Process it**, in case you might want to process it but not to book it as final, because it could be you might need to change it later on.
-   **Void it**, in case that purchase order is not required anymore and therefore needs to be voided.
-   **Book it**, in case it is correct and final.

!!! warning
    If there are non-stockable BOM products and they have not been exploded, the Book button explodes them automatically.


#### **Lines**

Once the purchase order header has been properly filled in and saved, each purchase order line can be created in this tab.

Purchase order lines can be created in three different ways:

**1\. By manually creating new record/s in the "Lines" tab**.

The purchase order fields you can fill in are described below:

-   **Product**. You can select an item or product from the list or use the product selector icon.
-   **Ordered quantity**, or **Operative Quantity** if the product has an *alternative unit of measure (AUM)*  configured. This is the quantity needed of the product/item.
-   Product's **UOM**, or product's **Alternative UOM** depending on product configuration in regards to unit of measure.
-   **Attribute Set Value. **An attribute associated with a product as part of an attribute set.****
-   **Net Unit Price**. This one is coming from the Price List selected in the header, but it could always be changed.
-   **Line Net Amount. The final amount of a specified line, based only on quantities and prices.**
-   **Tax**. Purchase tax is normally filled in by the system, depending on Taxes setup.

**2\. By retrieving all the lines from previously created purchase orders.** In this case, you must use the process button "**Copy from Orders**".

This process button enables the **Copy from Orders Pick and Edit** window.

"Copy from Orders Pick and Edit" window allows you to search the orders to copy by using the filter options available.

The lines information of the selected orders will be inserted in the purchase order line/s, then that information can be manually changed.

**3\. By copying lines from other purchase orders.**

In this case, you must use the process button **"Copy Lines".**

This process button enables a new window named "Copy Lines from order" which allows you to create order lines by selecting the products already purchased from the supplier of the order by taking into account the *Consumption days* configured for the supplier.

##### **Explode button**

Explode button is shown when selecting a line with a non-stockable BOM product and the product has not already been exploded. When exploding a product, the bill of materials components the selected product consists of are shown in the order. 
!!! warning
    Once you have exploded it, you cannot comprime it. You should delete all the lines (first bill of materials components and then the BOM product), and insert again the non-stockable BOM product.


#### **Line Tax**

For each purchase order line, Etendo automatically populates the line tax related information in this tab.

Line tax tab informs about each purchase order line:

-   **applied tax rate**
-   **calculated tax amount**
-   **taxable amount**

!!! warning
    It is not possible to either manually create a new line or modify existing ones.


#### **Basic Discounts**

Lists information about discounts automatically applied based on the supplier configuration and / or manually entered for the purchase order.

#### **Payment Plan**

Shows the total amount expected to be paid upon order booking as well as the amount/s pre-paid or paid against the invoice/s for the order.

Payment Plan information is required at order level because suppliers could ask for a **pre-payment** of all or part of a debt prior to its due date.

Purchase order payment plans **do not show nor manage valid due dates**, but the payment plan of the corresponding purchase invoice/s.

This tab also shows information about the regular payments received against the invoice/s for this order, as amounts paid.

Finally, a payment plan of a purchase order will be **removed**:

-   if the purchase order is **reactivated**
-   or if the purchase order is **voided**

#### **Payment Details**

Displays the details of the payments (pre-payments or regular payments) made for the order or for the invoice/s of the order.

### Goods Receipts

A Goods Receipt is a document issued to acknowledge the receipt of the items listed in it. In other words, it is a document used to register in Etendo the specifics of items physically received in the warehouse.

#### **Header**

Goods Receipts can be issued and booked in the header section of the goods receipt window.

The fields to fill in the **Goods Receipt header** are:

-   **Document Type**, which is filled in by default as "MM Receipt".
-   **Warehouse**, where goods are going to be located.
-   **Business Partner**, third party which delivers the goods.
-   **Movement Date**, delivery date of the goods.
-   **Accounting Date**, accounting date in case of posting the Goods Receipt.
-   **Purchase Order**, purchase order number linked automatically by Etendo, in case the Goods Receipt is automatically created from a Purchase Order.
-   **Order Reference**, Warehouse team can fill in here the Supplier's Delivery Note number, this way the internal Goods Receipt number and the Supplier's Delivery Note number are linked.



**Once header information is properly filled-in, you can then go to the "Lines" tab in order to enter "Goods Receipt Line/s"**.

!!! info
    To learn how to enter goods receipt lines, visit the next section "Lines".


If a **Goods Receipt** is completed and therefore **booked**:

-   The **quantity on hand of the item/s received is increased** by the quantity received.

If a **"Completed" Goods Receipt is voided** because the goods have been returned to the supplier:

-   **The quantity on hand of the items/s returned is decreased** by the quantity of the goods returned. Etendo automatically creates a new "Goods Receipt" for exactly the same items but with "negative" quantities. 

!!! info
    To learn more about Goods Returns, visit *Return to Vendor* and *Return to Vendor Shipment*.


Supplier can send a "Purchase Invoice" together with the "Delivery Note" of the goods delivered, therefore:

-   From the Goods Receipt window, it is possible to generate the corresponding supplier's invoice, by using the header process button "**Generate Invoice from Receipt**".

This action implies a **link between the goods receipt and the purchase invoice**, the user can be aware of when inquiring about the corresponding purchase invoice.

!!! info
    To Learn more, visit *Purchase Invoice.*


#### **Lines**

Once the goods receipt header has been properly filled in and saved, each item received can be listed as a separate goods receipt line.

There are several ways of creating goods receipt lines.

1.**Warehouse management team can always manually create goods receipt lines.**
That is the way warehouse management team could use in case there is no a booked purchase order nor a completed purchase invoice for the goods received, they can retrieve data from.


As a consequence of that, the information to manually fill in is:

-   the goods or items received
-   the quantity received
-   the storage bin where the items are going to be stored

**Explode** button is shown when selecting a line with a non-stockable BOM product and the product has not already been exploded. When exploding a product, the bill of materials components the selected product consists of are shown in the shipment. Once you have exploded it, you cannot comprime it. You should delete all the lines (first bill of materials components and then the BOM product), and insert again the non-stockable BOM product.


2.On the other hand, it is also possible to **"automatically" create goods receipt lines**, by using the header process button **"Create Lines From"**.

This allows the user to select the orders or invoices pending to be received.


For instance, once a purchase order is selected, the purchase order lines pending to be received are shown.

Then, the user is able to select the purchase lines received, change the quantity if required, and get them located in the warehouse.

Finally:

-   If a purchase order/line is selected, this action **links each good receipt line to the corresponding purchase order line**, same applies to purchase invoice.


#### **Accounting**

Accounting information related to the material receipt.

!!! info
    For more details please review the accounting article.


A **"Goods Receipts" can be posted** if the "**MaterialMgmtShipmentInOut**" table is set to Active for accounting in the [*Active Tables*] tab of the organization's  general ledger configuration.

A "Goods Receipt" posting looks like:



Posting a "Goods Receipt" requires the calculation of the cost of the contained product/s.

In the case of a goods receipt, that is:

-   the purchase price of the product/s
-   or the default *standard cost* of the product/s in case of calculating cost by using an Standard *costing algorithm*.

If there is not a related purchase order, the Costing Server process uses the newer of the following three values:

-   the last purchase order price of the receipt's vendor for the product.
-   the purchase price list of the product.
-   or the *default cost* of the product.

Moreover:

-   The "Legal Entity" organization needs to have a validated *Costing Rule* configured.
-   And the *Costing Background Process* needs to be scheduled for the *Client*, therefore it can search and allow that the *Costing Server* process calculates the cost of the transactions.

Once the costs have been calculated, the **Goods Receipt can be posted** to the ledger.

In the case of a receipt containing "Expense" product/s without the "Sales" checkbox selected, it is possible to use the product's purchase price instead of the product's cost to post the goods receipt.

This works if the checkbox *Book Using Purchase Order Price* is selected for the product/s.

In this case, it is required that a "Purchase Order" is related to the posted "Goods Receipt".

#### **Voiding**

It is possible to totally void a goods receipt by using the header button **"Close"** and then selecting the action "**Void**".

This action creates a **new document** that **reverses the goods receipt.**

Void action allows to specify a "**Void Date**" and a "**Void Accounting Date**" of the new document:

-   **Void Date**: that is the movement date of the new document that reverse the goods receipt.
-   **Void Accounting Date**: that is the accounting date of the new document that reverse the goods receipt.

Both fields above take original document dates as default date and validate that the dates entered are not prior to the "Movement Date" and the "Accounting Date" of the Goods Receipt, respectively.

Void action implies that:

-   Etendo automatically generates a **new document** in the "Goods Receipt" window, and **informs about the document number** created. The document number is also displayed in the description field of the Goods Receipt. This new document is created as described below:
    -   The "**transaction document**" used by Etendo is "**MM Receipt**".
    -   This document is **exactly the same as the original** one being reversed **but the movement quantity is negative.**
    -   Once the **new document** has been created, you can **change** both the "**Movement Date**" and the "**Accounting Date**" of the new document prior to getting it posted.

#### **Landed Cost**

Landed Cost tab allows to allocate additional costs to the goods receipt.

It is possible to enter as many landed cost types/lines as required.

Some relevant fields to note are:

-   **Landed Cost Type**: that is the landed cost type that is going to be allocated to the goods receipt.
-   **Invoice line**: that is to select the corresponding landed cost invoice line if any, that matches the landed cost type being entered.  
    If an invoice line is selected, the invoice line amount gets populated in the next field "Amount".
-   **Amount**: that is the landed cost amount. This amount can be an "estimation" or a "real" amount in case of selecting an invoice line.
-   **Landed Cost Distribution Algorithm**: that is the one distributed by Etendo "Distribution by Amount", which means that the landed cost amount is going to be distributed among the goods receipt lines proportionally by receipt line amount.

Once all items above are filled in, including corresponding landed cost purchase invoice line, both "Goods Receipt" and Landed Cost *process matching* are executed by clicking on the "**Complete**" process button.

### Pending Goods Receipts

This window allows the user to:

-   **Use the Filter options** to narrow down the search of pending purchase orders to be delivered. It is possible to search by:
    -   Business Partner
    -   From Purchase Order Date -> To Purchase Order Date
    -   Purchase Order number
-   Enter a **"Reception date".**
-   **Select** the "**Order line/s of a purchase order/s" delivered** which are shown grouped by Business Partner and Purchase Order.
-   **Change** the "**Quantity**" of the goods being receipt if needed.
-   **Enter** the "**Goods receipt location**" or storage bin within a warehouse.
-   **Process it** in order to create the corresponding goods receipts.

### Purchase Invoice

The Purchase Invoice window allows you to register and manage supplier's invoices.

This stage of the chain **usually comes after "Goods Receipts" booking and management**.

A purchase invoice is an itemized statement of the goods or services provided by a vendor or supplier. It indicates the quantity and price of each product or service provided or to be provided.

Suppliers could send the corresponding purchase invoice/s together with the delivery note/s attached to the goods, that implies that a "Purchase Invoices" can been automatically generated from the "Goods Receipt" window, but it could be that is not the case, therefore a purchase Invoice can also be created from scratch in the "Purchase Invoice" window.

The purchase expenses can be recognized as soon as the purchase invoice is accounted, however if an expense deferred plan is configured, it is possible to defer the expense recognition as required.

Supplier invoices can be registered, booked and managed in the header section of the purchase invoice window.

**Header** lists the main terms and conditions related to the purchase invoice.

!!! info
    In the majority of cases, the main (and the only) field needed to create a new purchase invoice document is the Business Partner field. All other fields will be pre-filled automatically based on the selected Business Partner, logged in User preferences and other system default parameters.



Some other fields to note are:

-   **Transaction document** defaulted as "AP Invoice" or purchase invoice *document type* which can be manually changed to either "AP Credit Memo" or "Reversed Purchase Invoice".
    -   "AP Credit Memo" and "Reversed Purchase Invoice" document types can be considered credit purchase invoices, the difference between them is that:
        -   "AP Credit Memo" type must contain either an "Invoiced Quantity" > 0 or "line Net Amounts" >0.  
            Above implies that invoices set as "Credit Memo" should not be related to "Orders" or "Shipments".
        -   "Reversed Purchase Invoice" type must contain either an "Invoiced Quantity" <0 or "line Net Amounts" < 0. These are the invoice types that can be related to return "Orders" or "Shipments".
-   **Document No**. you could manually fill in the supplier's invoice number in this field, if the document sequence number associated with the transaction document "AP Invoice" is set up to allow you to do that; otherwise it will be automatically provided by the system as an "Internal" purchase invoice number.
-   **Invoice Date**: the date the invoice is registered. It is used to calculate when the payment of the invoice is due. Defaults to the current date can always be changed.
-   **Accounting Date**: the date to be used in the posting record of the Purchase Invoice to the general ledger. Defaults to the Invoice Date field can always be changed.
-   **Payment Terms**: indicates **how** an invoice should be paid. Defaulted according to the Vendor/Creditor tab of the *Business Partner* window.
-   **Payment Method**: defines **when** a purchase invoice needs to be paid. Defaulted according to the Vendor/Creditor tab of the *Business Partner* window.
-   **Supplier Reference**: this is a not-mandatory field which can be used to enter the supplier invoice number.

There are 3 ways of entering lines into the purchase invoice, two of them from the invoice header and the last one from the **Lines** tab:

1.  Selecting products from pending to be invoiced orders or receipts using the *Create Lines From Order and Create Lines From Receipt* buttons.
2.  Copying all products from the chosen invoice selected in the history of all invoices for different business partners using the *Copy Lines* button.
3.  Manually, line by line in the *Lines* tab. This option is used if the underlying document (Purchase Order or Goods Receipt) does not exist in the system prior invoicing takes place.

The **Complete** button finishes the creation of the invoice document with the fulfillment of the *Payment Plan* tab and the *Payment Monitor* section in the Header. If there are non-stockable BOM products in the lines and they have not been exploded, the Complete button will explode them automatically.

Once completed, a purchase invoice can be:

-   **posted** to the ledger by using the button *Post*
-   **voided** by using the button *Reactivate*
-   and **paid** by using the button *Add Payment*.

#### **Lines**

Once the purchase invoice header has been properly filled in and saved purchase invoice lines can be registered in this tab.

Lines list each product to be purchased and its characteristics.

The fields to note are:

-   **Financial Invoice Line** is selected when the invoice line is not a product but an account not set up as a product but as a *G/L Item*, or an asset not set up as a product.  
    When selected, the product field disappears from the screen and an account field appears related to the purchase invoice line.
-   **Attribute Set Value**: field is displayed if the product in the line has *attributes* (color, size, serial number or several of them together etc).
-   **Purchase Order Line and Goods Receipt Line**: references to the purchase order and goods receipt line that is being invoiced.

As already mentioned, purchase expenses can be deferred therefore they are not recognized at the purchase accounting date but within a given number of accounting periods.

When a purchase invoice line is created, it is possible to define at line level, whether the line is going to cause the expense to be deferred. The relevant fields are:

-   **Deferred Expense**: When this flag is checked, the Expense Plan field group becomes visible, allowing users to configure the next three fields.
- **Expense Plan Type**: This field specifies the frequency of the expense distribution which currently is "monthly".
- **Period Number**: This field specifies the duration of an expense plan.  
        For instance, if a company purchases business insurance for the duration of the year, the period number to enter would be 12 as the company would like to distribute that expense over 12 months.
- **Starting Period**: The first open period in which the expense is going to be recognized.

These fields can be defaulted if configured for the *product*.

If an expense plan is configured that implies a specific *purchase invoice accounting*.

**Explode** button is shown when selecting a line with a non-stockable BOM product and the product is not already exploded. When exploding a product, the bill of materials components the selected product consists of are shown in the invoice. Once you have exploded it, you cannot comprime it. You should delete all the lines (first bill of materials components and then the BOM product), and insert again the non-stockable BOM product.

**Match LC Cost** button is shown when the purchase order line contains either an "account" or a "product" setup as *landed cost type*.

This process button allows to **match** both the "**estimated**" landed cost booked in the *landed cost* window, and the one being **invoiced** in the invoice line. Both need to be of the very **same landed cost type**.

Once selected, **"Match LC Cost**" button opens the **"Match LC Cost" pick and edit window**.

Only processed Landed Cost documents will be shown in this Window. It allows you to pick the corresponding landed cost, to enter an amount to match in the field "Matched Amt", and then to select the "**Process Matching**" check-box.

!!! warning
    Note that if the "Process Matching" check-box is not selected here, landed cost matching will have to be processed in the *landed cost* window by using **Process Matching** button.



### Matched Invoices

This window helps you to post the discrepancies between inventory and financial accounting of those items for which the corresponding goods receipts were posted.

Above mentioned discrepancies are mainly caused by differences between:

-   the **item's net unit price registered when booking the purchase order** and later on **posting the corresponding Goods Receipt.**
-   and the **"final" item's net unit price registered when posting the purchase invoice.**

In the window, there is a listing of all invoices that are matched to goods receipts. The matching of the documents is done when documents are created by using the information of the other document: for example by clicking the Generate Invoice from receipt on the goods receipt or by clicking the Create Lines from button when creating a goods receipt to select the invoice.

#### **Matched Invoice**

Matched invoice tab lists each invoice line posted linked to the corresponding goods receipt lines, which could also be posted or not.

There is a "**Post**" header button which is the one that posts the discrepancies between inventory and financial accounting if any, once the proper line has been selected.

Overall the process to post the discrepancies in accounting is detailed below:

A *Matching Invoice* document can be posted if the cost of the products included in a *Goods Receipt* has been calculated. To obtain that:

-   A validated *Costing Rule* is required in the Matched Invoice's legal entity,
-   and the background process *Costing Background Process* must be run.

In the case of "Expense" product/s do not having the "Sales" checkbox selected, it is possible to use the product's purchase price instead of the product's cost whenever the checkbox *Book Using Purchase Order Price* is selected. In this case, it is required that a "Purchase Order" is related to the "Goods Receipt".

#### **Accounting**

Accounting information related to the matched invoices

### Return to Vendor (RTV)

This window allows the user to create a Return Material document in case a given product needs to be sent back either to be returned for a refund or replacement, or to be repaired. 

#### **Header**

Create a purchase order and process it.

Once the Return Material document is accepted by the Vendor, you can process it by clicking the button **Book**. The document changes from *Draft* to *Booked.*

Only *Booked* documents can be shipped to the vendor. 
!!! warning
    Notice the button **Pick/Edit lines** disappears when the Return to vendor document is in status *Booked.*


#### **Lines**

Add products to be included in your purchase order. Each product is added by creating a line.

The Lines tab is not editable, since the returned lines always come from receipt lines, to avoid:

-   Seeing positive values while negative in the DB.
-   Entering lines that are not linked to the original receipt lines.
-   Editing attributes, products and so having either the products or attributes different from the shipment line.

To enter new lines you need to click the process button PICK/EDIT Lines. 


**Things to consider:**

-   The only editable fields are:
    -   **Returned**: Quantity you wish to return. When selecting the row, the quantity is not set by default since the system cannot know how many items return.
    -   **Net Unit Price**: Price of the original purchase order.
    -   **Return reason**: The reason why you return the item.
    -   and **Returned UOM**, only in case *alternative unit of measure (AUM)*preference is enabled.  
        In that case, product's "primary" AUM for the purchase flow is shown if any, otherwise product's UOM is shown. The user can always change it to product's UOM.

You can define the Return Reason at header level. In this case when picking a line it inherits what selected in the header but you can modify it as you wish.

-   Only Material receipt documents that have not been still returned can be picked it, in case a Receipt line has been fully returned it will not be shown.
-   When a Receipt line has been partially returned you can still return the rest. What you have already returned for that line is shown in the field **Return Qty other R.**

**Validations:**

-   You are not allowed to return more quantity than the **Ship/Receipt Qty**. In case you do it a message is shown.
-   Notice that this validation takes into account the **Return Qty other RM** field

!!! info
    To edit a line you need to click again the **Pick/Edit Lines** button and the line appears selected and then you can modify any of the editable fields.


!!! info
    To delete a line you need to unmark the line and then click Done.


### Return to Vendor Shipment

From this window you deliver the returned goods to the vendor.

#### **Header**

Create and edit a goods receipt.

The **RMA vendor ref.** field is populated automatically or not based on:

-   If it is filled before selecting a line, then it will not be populated automatically to avoid override it.
-   If you select a line/s where all of them belong to the same Return to Vendor document, it will be populated automatically.
-   If you select a line/lines but one of them belongs to a different Return to Vendor document, then it will not be populated automatically.

Once the document is ready, you can process it by clicking the button **Complete**. The document changes from *Draft* to *Completed.*

!!! warning
    Notice the button **Pick/Edit lines** disappears when the Return to vendor document is in status *Completed.*


To invoice these documents you must use the **Purchase invoice** window. All scenarios are covered:

-   If the vendor sends an invoice just for that specific document you need to select a *Reverse purchase invoice* document type and then select the lines through the *Create lines* from button.
-   If the vendor sends an invoice with the original purchase order plus the return materials order you need to select a *Purchase invoice* document type and then select the lines through the *Create lines* from button.
-   If the vendor does not send an invoice for the return materials order but wants to keep it as credit where you can use it later, you have to:
    -   Create a *Reverse purchase invoice* for these returned materials.
    -   Leave it as credit to be used later through the **Payment out** window.
    -   When you create the Purchase invoice for the original Purchase order you can consume that credit.

#### **Lines**

Add products which are included in your goods receipt. Each product is shown on its own line.

The Lines tab is not editable, since the lines always come from return to vendor lines, to avoid:

-   Seeing positive values while negative in the DB.
-   Entering lines that are not linked to return lines.
-   Editing attributes, products and so having either the products or attributes different from the return line.

!!! info
    To enter new lines you need to click the button PICK/EDIT Lines. 



**Things to consider:**

-   Editable fields are:
    -   **Ship Qty**, that value is set automatically when you select the line,
    -   and **Returned UOM**, only in case an alternative unit of measure (AUM) preference is enabled, regardless product's UOM is always shown there by default.  
        The user can change it if required, to the product's primary AUM configured for the procurement flow.
-   You can only select Return to Vendor lines that are pending to be shipped to that specific vendor.
-   The system proposes the different storage bins from where the item can be picked. Depending how the product is configured we could have three scenarios:
    -   Product with an instance attribute (i.e: Serial number): The system will propose only one storage bin as it is shown above.
    -   Product with a non-instance attribute (i.e: Colour): The system could propose several storage bins. See below image
    -   Product without attributes. Similar to second scenario. 

**Validations:**

-   You are not allowed to ship more than the **Available Qty.**
-   You are not allowed to ship more than the **Pending** quantity.
-   The system also validates you cannot ship more than the **Pending** quantity when selecting both lines.

!!! info
    To edit a line, you need to click the **Pick/Edit Lines** button again, the line appears selected and then you can modify any of the editable fields.


!!! info
    To delete a line, you need to unmark the line and then click Done.


If there is not enough available stock for a product in a selected line, then it will be possible to define a Ship Quantity and select it. if there is at least one storage bin with overissue inventory status for the Return To Vendor Shipment's warehouse, in this case the new line will use it as storage bin and it will create a negative stock when the document is processed. 


#### **Accounting**

The RTV shipment can be posted **if the table "MaterialMgmtShipmentInOut" is** active for accounting **in the corresponding general ledger configuration.**

!!! info
    To learn more visit the *Active Tables* article.


Most cases the accounting manager should be the one to decide whether to post RTV shipment or not, as well as get them posted unless the background process is activated.




### Landed Cost

#### **Introduction**

Landed Cost window allows to allocate additional costs such as freight, insurance or duties to goods receipt(s) therefore the cost of the products included in the receipt(s) is adjusted as applicable.

All those costs are needed to place the product in the organization's warehouse.

Every time that a landed cost is booked for a product receipt valued at "Average" cost, a landed cost adjustment is created.

Landed costs distributed and allocated to products valued at "Average" cost implies a change in the inventory value of the product. In other words, the calculated cost ("Total Cost") of the product receipt will need to be adjusted the same as the "Average" cost of the product.

!!! warning
    Note that the "Unit Cost" of the receipt transaction will not change as this type of adjustment is not a unit cost adjustment type but an "extra" cost.


All of the above will have an accounting impact therefore, product inventory value can be the same as product accounting value.

On the other hand, if a landed cost is booked for a product receipt valued at "Standard" cost, no cost adjustment will be created but a "Variance" between the "standard" cost defined for the product and its "actual" cost. This variance which will need to be posted to a "Landed Cost Variance" account, so it can be later on analysed.

Landed cost window allows both:

-   either to book "**estimated**" landed cost that can be later on matched against "actual" landed cost by landed cost type,
-   or directly book "**actual**" landed cost by landed cost type.

Landed cost window also allows to post landed costs once processed.

"**Estimated**" Landed Cost scenario:

-   A purchase order is booked and after that the corresponding goods receipt and purchase invoice.  
    The "average" cost of the products included in the receipt is calculated at this point.
-   After that "estimated" landed costs (i.e freight costs) are allocated to the goods receipt and booked in the landed cost window.  
    The cost of the products included in the receipt is then adjusted the same as products asset accounting.
-   After that a purchase invoice including the actual amount of freight cost is booked and posted to the ledger.
-   Then, it is possible to match "estimated" landed cost against "invoiced" landed cost.  
    The cost of the products included in the receipt is adjusted once more if there are differences between estimated and actual landed cost amounts.

"**Actual**" Landed Cost scenario:

-   A purchase order is booked and after that the corresponding goods receipt and purchase invoice.  
    The "average" cost of the products included in the receipt is calculated at this point.
-   After that a landed cost document is created to record actual landed cost to the goods receipt.  
    The cost of the products included in the receipt is then adjusted the same as products asset accounting.

In Summary, landed cost feature follows below detailed steps:

-   **Landed Cost Process**:
    -   A landed cost document is created including as many different landed cost types and amounts as required.
    -   This landed cost document can be related to a single goods receipt, to several goods receipts or to specific goods receipts lines.
    -   This landed cost document can record "actual" landed cost in case of selecting the corresponding invoice, therefore the landed cost process and matching is done in one step.
    -   Landed cost is processed.
        -   This action creates a *landed cost adjustment* linked to the landed cost document.  
            This cost adjustment has as many adjustment lines as products included in the goods receipt(s) selected, therefore the cost of those products is adjusted as applicable.
-   **Landed Cost Post**:
    -   Once a landed cost document is processed it can be posted to the ledger, therefore product(s) asset accounting is adjusted as well.
-   **Landed Cost Matching**:
    -   Landed cost invoice is booked and posted to the ledger later on.
    -   After that the "estimated" landed cost booked in the landed cost document can be matched against actual landed costs by landed cost type in the landed cost invoice.
    -   Landed cost matching can generate an additional cost adjustment for the product(s) if estimated landed cost amounts were not the same as actual landed cost amounts.
-   **Landed Cost Matching Post**:
    -   Once landed cost(s) are matched can be posted therefore:
        -   product(s) asset accounting is adjusted once more if applicable,
        -   and landed cost posting gets landed cost invoice *accounting dimensions.*

**Header**

A Landed Cost document can be created, processed and posted in this window.

Some fields to note are:

-   **Organization**: that is the organization or legal entity for which landed cost needs to be booked.
-   **Reference date**: that is the date when the landed cost document is being created.



**Cost**

A Landed Cost Document can have as many cost (lines) as landed cost types to allocate to the Goods Receipt(s) selected.