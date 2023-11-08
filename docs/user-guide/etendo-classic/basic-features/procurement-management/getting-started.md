---
tags: 
 - getting started
 - procurement management
 - procure to pay
 - supplier returns
---

![cover-getting-started.png](/assets/getting-started/overview/cover-getting-started.png)
#

## Overview

<iframe width="720" height="480"  src="https://www.youtube.com/embed/d33J6fTMEqM?si=NlHOoCq82bCJG3Rg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Procurement Management deals with all the activities related to the purchase of goods and services from external suppliers and the corresponding reporting.

This application area of Etendo covers Requisition to Receipt and Invoicing parts of the [Procure To Pay business flow](/user-guide/etendo-classic/basic-features/procurement-management/getting-started/#procure-to-pay-business-flow) and [Supplier Returns business flow](/user-guide/etendo-classic/basic-features/procurement-management/getting-started/#supplier-returns-business-flow).

For Payments Management of Procure To Pay, see Financial Management / Receivables & Payables application area.

## Procure to Pay Business Flow

*Procure to Pay* workflow manages the life-cycle of a procurement process.

Due to its complexity and different roles involved, it is convenient to split Procure to Pay down into two main sub-processes:
    
1. *Requisition to Receipt* process starts by the creation and management of purchase requisitions and corresponding purchase orders to the moment the warehouse staff receives the merchandise.
2. *Supplier Invoice to Payment* continues the previous sub-process by registering the supplier invoices and closes it by paying supplier invoices.

![procure-to-pay](/assets/user-guide/etendo-classic/basic-features/procurement-management/getting-started/procure-to-pay-business-flow.png)

### Configuration

The following setup needs to be done before performing the process:

- Products
- Costing rules
- Landed Cost Types
- Business Partners (Vendors and Suppliers).
- Price configuration

Products need to be configured prior any purchase requisition is issued.

Each product being purchased needs to have a price in the purchase price list in order to be selectable in any transactional document like a purchase order or a purchase invoice.

Same way, each product that is being purchased needs to be defined in a unit of measure (UOM), and in an alternative unit of measure (AUM) if required.

!!!info
    Please refer to [Product Setup](/user-guide/etendo-classic/basic-features/master-data-management/product-setup/), [Product](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) and [Pricing](/user-guide/etendo-classic/basic-features/master-data-management/pricing/) for more information.

The cost of an input transaction such as a "Goods Receipt" can be calculated by using the product's purchase price excluding taxes.

Besides that, the cost of the products included in a Goods Receipt can be adjusted as a result of allocating different types of [Landed Costs](/user-guide/etendo-classic/basic-features/warehouse-management/setup/#landed-cost-type) in the receipt.

The "Costing Server" process is the Etendo "Costing Engine" process that calculates and adjusts a product's transaction cost.
This process requires that the legal entity/organization has a [costing rule](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#costing-rule) configured and applied to the products configured as "Stocked".
Business Partners need to be configured prior to any purchase requisition can automatically turn into a purchase order.

!!!info
    For more information, visit [Business Partner Setup](/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/) and [Business Partner](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#business-partner).

Above configuration is part of the overall Business setup flow within the "Master Data Management" setup.

!!!note 
    You are not required to perform any additional setups for the Procurement Management application area if you are going to explore it based on Food & Beverage (F&B) sample client shipped with Etendo by default.
    The sample data set already contains the roles, business partners, products, warehouses and prices pre-configured.

### Execution

In Procurement Management, the Procure to Pay business process is executed as follows:

Any member of the organization allowed to do so can directly issue a Requisition as a result of an organization or business unit need.

- The requestor creates a new document in the [Requisition](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#requisition) window, enters a "Need by date" and then looks for the product or service needed.
If the product does not exist it can be entered at that time in the [Product](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) window.
- The requestor continues by adding for each product needed a new line with the need by date, the product, the quantity, the price if known and if needed its attribute (size and/or color, etc).
A preferred supplier can also be added if known.
- Once done, the requisition is saved in "Draft" status allowing it could be changed later on by the user if needed.

Requisitions notify the purchase staff of products to order, their quantity and the time frame for its delivery. Purchase staff is then in charge of managing already created purchase requisitions or even creating new ones, if required.

- Purchase staff manages requisitions in the [Manage Requisitions](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#manage-requisitions) window.
- Purchase staff can change any data of the requisitions created in draft status, and besides can look for the supplier to be used in the Business Partner field. if the Business Partner does not exist, it can be entered at that time in the [Business Partner](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#business-partner) window.
- Purchase staff can also enter the purchase net unit price and discounts if any, once known.
- Once the requisition is ready, it is completed. The Document Status of the requisition changes to Completed and can then turn into a purchase order.

Purchase staff:

- can massively create Purchase Order/s for the Completed Requisitions in the [Requisition to Order](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#requisition-to-order) window by searching and then adding requisition lines not linked to an order yet.
The purchase order/s created that way are shown in the Purchase Order window in Booked status.
- and can also directly create Purchase Orders in the [Purchase Order](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#purchase-order) window. Purchase lines are filled as in the case of the Requisition. Once the Purchase Order is ready, it is processed clicking the Book button.
- To review past and present purchases of the supplier, purchase staff uses the [Purchase Dimensional Report](/user-guide/etendo-classic/basic-features/procurement-management/analysis-tools/#purchase-dimensional-report).

Warehouse staff:

- Receives the merchandise as well as the delivery notes attached in 2 ways:
    - With the [Goods Receipt](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#goods-receipts) window, Warehouse staff looks for the orders pending to be delivered one by one and then gets corresponding order lines quantity located in a warehouse and storage bin.
    This window also allows creating a receipt in a manual way.
    - With the [Pending Goods Receipt](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#pending-goods-receipts) window. Warehouse staff can massively select the purchase order lines being delivered and locate the quantity receipt in a warehouse and storage bin.
- Allocates landed cost, if any, to the products included in a receipt by:
    - selecting a landed cost type and entering an "estimated" landed cost amount which will be distributed among receipt lines
    - or by selecting a landed cost type and entering a landed cost amount already invoiced which will also be distributed among receipt lines.
- Completes the receipts.
    - Completed receipts updates stock information (product levels increase) and can be [posted](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#goods-receipts) to the ledger therefore product assets accounting is being increased.
    - A Goods receipt can only be posted if the cost of the products being received has been calculated. To do so, the [Costing Background process](/user-guide/etendo-classic/basic-features/general-setup/process-scheduling/#costing-background-process) needs to be run.
- [Matched Invoices](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#matched-invoices) window helps to manage and post the discrepancies, if any, between the accounting of the receipt and the accounting of the corresponding invoice later on, due to purchase price differences.
- [Goods Receipts Dimensional Report](/user-guide/etendo-classic/basic-features/procurement-management/analysis-tools/#goods-receipts-dimensional-report) is used to review past receipts of the Business Partner.

Finance staff:

- Registers supplier invoices in different ways:
    - With the [Goods Receipt](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#goods-receipts) window, Finance staff can generate an invoice from a Receipt in status Complete.
    - With the [Purchase Invoice](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#purchase-invoice) window, Finance staff can enter supplier invoices:
        - in a manual way
        - or by retrieving purchase orders or receipts lines pending to be invoiced
        - or by copying invoice lines from existing purchase invoices.
- Registers landed cost invoices and match those ["invoiced" landed costs](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#lines_4) with the landed costs:
    - booked directly in a [receipt(s)](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#landed-cost).
    - or booked through a [landed cost document](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#landed-cost_1).
- [Processes](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#process-matching) and [Posts](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#post-matching) landed cost matching.
- Once a Purchase Invoice is Processed, a Payment Plan of the invoice is created based on the payment terms agreed with the supplier and the purchase invoice can be posted to create the accounting entries of the invoice. Afterwards, the payment plan can be modified.

Additionally:

- The [Matched Purchase Orders](/user-guide/etendo-classic/basic-features/procurement-management/analysis-tools/#matched-purchase-orders) view helps Finance staff to have a look at the order or receipt lines which have not been invoiced yet by a supplier.
- Finance staff is able to review past supplier invoicing information in the [Purchase Invoice Dimensional Report](/user-guide/etendo-classic/basic-features/procurement-management/analysis-tools/#purchase-invoice-dimensional-report).

Purchase expenses can be recognized in different ways:

- In most cases companies would recognize the expense as soon as the purchase is made. For instance, a company buying consumable products that are not capitalized.
In Etendo, in this situation, the expense is generated as part of the accounting of the purchase invoice corresponding to the transaction.
- Under some circumstances, however, it is required to defer the expense recognition. For instance, a company purchasing a business insurance for the duration of a year would want
to distribute that expense over 12 months.
In Etendo, in this situation, the expense can be deferred within a given number of periods by entering an expense deferred plan in the [purchase invoice lines](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#lines_4).

!!!info
    For a full description of this functionality, please visit the [How to manage deferred revenue and expenses]() section.

Finally, the finance staff is in charge of making and managing the supplier payments:

- Supplier payments can be made in the Purchase Invoice window by using the Add Payment button. It is also possible to make a prepayment against a Purchase Order.
Detailed payment management documentation is available in the Financial Management / Receivables and Payables application area and in the [How to manage prepaid invoices in payables]() section.

## Supplier Returns Business Flow

This workflow manages the return of purchased goods back to the supplier. Due to the consequences of returning, it is convenient to split Supplier Returns down into two main sub-processes:

1. *Supplier Return to Debit*: This process manages the return of goods back to the vendor and the request of a debit.

2. *Supplier Return to Replacement*: This process manages the return of goods back to the vendor and the request of a goods replacement.

![supplier-returns](/assets/user-guide/etendo-classic/basic-features/procurement-management/getting-started/supplier-return-debit.png)

### Configuration
The [Return reasons](/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/#return-reasons) window is the only one that requires configuration before performing this process.

### Execution

In Procurement Management, the *Return to Vendor business flow* is executed as follows.

Procurement staff:

- Creates a new document in the [Return to Vendor](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#return-to-vendor-rtv) window and looks for the vendor name in the Business Partner field.
- And continues by adding lines clicking the button [Pick/Edit lines](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#lines_5)
    - It is possible to pick goods receipt lines and edit the quantity you want to return and the price
- Once the Return Material document is accepted by the Vendor, you can process it by clicking the Book button. The status of the document changes from Draft to Booked.
- Only Booked documents can be shipped to the vendor

Warehouse staff:

- Creates a new document in the [Return to Vendor Shipment](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#return-to-vendor-shipment) window and looks for the vendor name in the Business Partner field.
- And continues by adding lines clicking the [Pick/Edit lines](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#lines_6) button
    - Return to Vendor lines are picked
    - It is possible to edit the quantity to be shipped
- Once the document is ready, process it by clicking the button Complete. The status of the document changes from Draft to Completed
- Completed shipment updates stock information (product levels decrease)

Finance staff: To invoice these documents, go to the [Purchase invoice](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#purchase-invoice) window. All scenarios are covered:

- If the vendor sends an invoice just for that specific document, you need to select a Reverse purchase invoice document type and then select the lines through the *Create lines from* button
- If the vendor sends an invoice with the original purchase order plus the return materials order, you need to select a Purchase invoice document type and then select the lines through the *Create lines from* button
- If the vendor does not send an invoice for the return materials order but wants to keep it as credit so you can use it later, you have to:
    - Create a *Reverse purchase invoice* for these returned materials
    - Leave it as credit to be used later through the [Payment out](/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/#payment-out) window
    - A new purchase invoice based on the original purchase order can consume that credit

## Relationship with other application areas

Procurement Management has a relationship with other application areas: 

- [Warehouse Management](/user-guide/etendo-classic/basic-features/warehouse-management/getting-started/) as Goods Receipts changes items quantity on hand and its value.
- [Financial Management](/user-guide/etendo-classic/basic-features/financial-management/getting-started/) in terms of managing account payable payments.
- [MRP Management]() as purchase planning allows the creation of purchase orders based on material needs.
