---
title: Sales Management - Getting Started
tags: 
    - getting started
    - sales management
    - invoice
    - quotation
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Sales Management - Getting Started

## Overview

<iframe width="720" height="480"  src="https://www.youtube.com/embed/JxTGQIJ9JqQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


Sales Management deals with all activities related to the customer sales process and corresponding reporting.

This application area of Etendo covers Order to Shipment and Invoicing parts of [Order to Cash](../../../../user-guide/etendo-classic/basic-features/sales-management/getting-started.md#order-to-cash-business-flow) business flow and [Customer Returns](../../../../user-guide/etendo-classic/basic-features/sales-management/getting-started.md#customer-returns-business-flow) business process. 

!!! Info
    For Payments Management of Order to Cash see the [Financial Management](../../../../user-guide/etendo-classic/basic-features/financial-management/getting-started.md) application area.

## Order to Cash Business Flow

*Order to Cash* workflow manages the life-cycle of a sales process.

Due to its complexity and different roles involved, it is convenient to split Order to Cash down into two main sub-processes:

1. *Order to Shipment* process starts when a customer requests a quotation or orders goods to the moment the warehouse staff ships the merchandise.

    ![ord-to-ship-bus-pro](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/ord-to-ship-bus-pro.png)

2. *Customer Invoice to Cash* continues the previous sub-process by invoicing customer deliveries and closes it by receiving payments from buyers.

![cust-inv-bus-proc](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/cust-inv-bus-proc.png)

### Configuration

The following setup needs to be done before performing the process:

- Sales Products.
- Price configuration.
- Business Partners (Customers).
- Sales Quotation document type configuration.

Sales products need to be configured prior to any sale in the application.
Each product that is being sold needs to have a *price* in the sales price list in order to be selectable in any transactional document like a sales order or a sales invoice.
Same way, each product that is being sold needs to be defined in a *unit of measure* ("UOM"), and in an *alternative unit of measure* (AUM) if required.

!!! Info
    For more information, visit [Product Setup](../../../../user-guide/etendo-classic/basic-features/master-data-management/product-setup.md), [Product](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product) and [Pricing](../../../../user-guide/etendo-classic/basic-features/master-data-management/pricing.md). 

Business Partners (customers) need to be configured prior any sales can automatically turn into a sales quotation or sales order. 

!!! Info
    For more information, visit [Business Partner Setup](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md) and [Business Partner](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner).

Above configuration is one part of the overall business setup flow within the Master Data Management setup.

Finally, the Quotation [document type](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#document-type) requires a sales order document type (i.e. Standard Order) to be defined as Document Type for Order to allow the conversion of a sales quotation into a sales order.

!!!Note
    It is not required to perform any additional setup for the Sales Management application area if Food & Beverage (F&B) sample client shipped with Etendo by default is going to be used to explore it. The sample data set already contains the roles, warehouses, business partners, products and prices pre-configured.

### Execution

In Sales Management the Order to Cash business process is executed as follows.

Customers can ask directly for a Sales Order or request a Quotation. If the Business Partner asks for a quotation, the sales staff:

- Creates a new document in the [Sales Quotation](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md) window and looks up the customer name in the Business Partner field. If the Business Partner does not exist, it is entered in the application with the [Business Partner](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner) window.
- Then Sales staff fills the [Sales Quotation](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md) window. The transaction document is set to Quotation by default. And continues by adding for each product a line with the product, quantity and if needed its attribute (size and/or color and/or serial number, etc.).
- Once the quotation is ready, it is booked. The Document Status of the quotation changes to Under Evaluation. The Quotation can be printed and sent to the Business Partner by email.
- When the Quotation is accepted by the Business Partner a sales order can be created based on this quotation. When this is done the status of the quotation changes to *Closed - Order* created and the Sales Order can be printed and sent to the Business Partner by email as a confirmation.

If the Business Partner places an order directly, the sales staff:

- Creates it with the same [Sales Order](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order) window setting the Transaction Document to the desired type of Order (*Standard Order, Warehouse Order*). Lines are filled as in the case of the Quotation. Once the Sales Order is ready, it is processed by pressing on the Book button.
- When the Sales Order is processed, it reserves the material for its shipment.
- To review past sales of the Business Partner Sales staff uses [Sales Dimensional Report](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#sales-dimensional-report).

Warehouse staff:

- Looks for orders pending for preparation in the [Create Shipments from Orders](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-shipments-from-orders) window or with the help of [Orders Awaiting Delivery Report](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#orders-awaiting-delivery-report).
- The Warehouse staff can create a Shipment in 2 ways:

With the [Create Shipments from Orders](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-shipments-from-orders) window. It creates a shipment completed for the selected Sales Orders.

With the [Goods Shipment](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#goods-shipment) window in which the Warehouse staff creates the shipment in a manual way.

- Completed shipment updates stock information (product levels go down) and can be posted to create the accounting entries of the shipment.
- [Shipments Dimensional Report](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#shipments-dimensional-report) is used to review past shipments to the Business Partner.

Finance staff can generate invoices in different ways:

- With the [Generate Invoices](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#generate-invoices) window, in which it generates invoices in bulk for all pending to be invoiced (based on their invoicing rules) Sales Orders.
- With the [Create Invoices from Orders](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-invoices-from-orders) window. It shows Orders pending to be invoiced and creates invoices for the selected Sales Orders.
- With the [Sales Invoice](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice) window in which the Finance staff creates the invoice in a manual way.
- Processed Sales Invoice creates the Payment Plan of the invoice, the Tax of the invoice and can be posted to create the accounting entries of the invoice. Afterwards, the [payment plan](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment) can be modified.
- [Orders Awaiting Invoice Report](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#orders-awaiting-invoice-report) helps Finance staff to plan and verify invoicing of the Business Partners.
- Finance staff is able to review past customer invoicing information in the [Sales Invoice Dimensional Report](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#sales-invoice-dimensional-report).


Sales revenues expenses can be recognized in different ways:

- In most cases companies would want to recognize revenues as soon as an invoice is completed. For instance a food and beverage distributor selling beverages would want to recognize the revenue as soon as the goods leaves the warehouse.
In Etendo, in this situation, revenue is generated as part of the accounting of the sales invoice corresponding to the transaction.
- Under some circumstances, however, it is required to defer the revenue recognition. For instance, a food and beverage distributor selling and invoicing a product that they will only be able to deliver to their customers in 3 months needs to defer revenue recognition till the delivery.

In Etendo, in this situation, the revenue can be deferred until a given starting period and within a given number of periods by entering a revenue deferred plan in the [sales invoice lines](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines-5).

!!!info
    For a full description of this functionality visit [How to manage deferred revenue and expenses](../../../../user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses.md) article.


Credit limit for business partner

- Each [Business Partner](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner) can be set up with a Credit Line Limit. When customer balance (amount that is outstanding for payment for the customer) is higher than the credit line limit a corresponding information message is shown when a business partner is selected during the creation of a sales order, sales invoice or goods shipment. This way Etendo assists in risk analysis while placing customer orders or executing other steps in the Order to Cash business flow.


Finally, the finance staff is in charge of recording and managing the customer payments:

- When a payment is received against an invoice it can be recorded in the Sales Invoice window by using the Add Payment button. It is also possible to receive a prepayment for the Sales Order. 
For more information about payment management documentation visit the [Financial Management](../../../../user-guide/etendo-classic/basic-features/financial-management/getting-started.md) and in the [How to manage prepaid invoices in receivables](../../../../user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables.md).


## Customer Returns Business Flow

Customer Returns workflow manages the business processes for returning items back from customers either for credit

![cust-ret-cr-business-process](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/cust-ret-cr-business-process.png)

or for replacement.

![cus-ret-replace-business-process](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/cus-ret-replace-business-process.png)

### Configuration

The following configuration options are available in this process:

- [Return reasons](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md#return-reasons)
- [Condition of the goods](../../../../user-guide/etendo-classic/basic-features/sales-management/setup.md#condition-of-the-goods)
- Accounts for [Cost of Goods Sold](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting) (COGS) for returns and [Revenue for returns](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)

### Execution

In Sales Management the Customer Returns business process is executed as follows.
Customers can request a [return material](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md#return-reasons) for whatever reason.
Sales staff:

- Creates a new document in the [Return from Customer](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-from-customer) window and looks for the customer name in the Business Partner field.
- And continues by adding lines clicking the button [Pick/Edit lines](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines-3).
Picks Goods shipment lines and edits the quantity the customer wants to return, price and return reasons.
- Once the Return Material document is accepted, process it by clicking the button Book. The status of the document changes from Draft to Booked.

Warehouse staff:

- Creates a new document in the [Return Material Receipt](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-material-receipt) window and looks for the vendor name in the Business Partner field.
- And continues by adding lines clicking the button [Pick/Edit lines](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines-4).
Picks lines created in the Return from Customer window.
If needed, edit the quantity received and its location (storage bin).
- Once the document is ready, process it by clicking the button Complete. The status of the document changes from Draft to Completed
- Completed receipt updates stock information (product levels go up).

Finance staff:
To invoice these documents can do it from several windows / processes:

- With [Return from Customer](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-from-customer) window where a new button Create Credit might appear or not based on the original sales order. If the order is already invoiced then it will be present, if not - it won't. Using this button it is possible to invoice the return order following the standard process, that is, depending on the invoice terms.
- With the same [Create Credit](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-from-customer) button it is also possible to create an invoice and leave it as credit to be used later.
- Using [Generate Invoices](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#generate-invoices) process: if the invoice terms is Customer Schedule After Delivery and both sales orders and RMAs exist the process groups all of them in one standard Sales Invoice (not in a [Return Material Sales Invoices](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#document-type)).
- With the [Sales Invoice](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice) window by picking lines and either grouping them from standard sales orders and return orders or by creating individual [Return Material Sales Invoices](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#document-type) only from return orders.
- With the [Sales Invoice](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice) window creating a Return Material Sales Invoice making sure that the amount of the Invoice is negative.


## Relationship with other application areas

Sales Management has a connection with other application areas:

- [Warehouse Management](../../../../user-guide/etendo-classic/basic-features/warehouse-management/getting-started.md) as shipment changes stock quantity and its value.
- [Financial Management](../../../../user-guide/etendo-classic/basic-features/financial-management/getting-started.md) in terms of managing payments.
- [Material Requirement Planning](../../../../user-guide/etendo-classic/basic-features/material-requirement-planning/getting-started.md) (MRP) because pending sales orders are one of the inputs for the production process.