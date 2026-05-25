---
title: Business Partner Info
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Orders
  - Invoices
---

## Business Partner Info

:material-menu: `Application` > `Master Data Management` > `Business Partner Info`

### Overview

The Business Partner Info window is a consolidated, read-only view of all transaction activity recorded for a given [business partner](./business-partner.md). It centralizes four types of information in a single place: orders, shipments and receipts, invoices, and assets. Sales, purchasing, and accounts teams use this window to get a quick summary of a partner's activity without navigating to each individual transaction window. No data entry is possible here; the window is intended strictly for consultation and review.

### Partner Selection

Select a business partner from the list to load their transaction data in the tabs below.

Fields to note:

- **Active**: indicates whether the business partner is currently active.
- **Search Key**: short identifier used to search for the business partner.
- **Commercial Name**: the business partner's commercial name.
- **Business Partner Category**: classifies the partner, for example Customer - Tier 1, Supplier, or Employee.
- **Sales Representative**: the sales representative assigned to the business partner, if any.
- **Payment Method**: the default payment method for the business partner, for example Wire Transfer.
- **Payment Terms**: the agreed payment terms, for example 30 days.

Once a record is selected, the **Partner Orders**, **Partner Shipments**, **Partner Invoices**, and **Partner Assets** tabs at the bottom of the screen are populated with the corresponding transaction data.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-1.png)

### Partner Orders

This tab lists all orders associated with the selected business partner, covering both [sales](../../sales-management/transactions.md#sales-order) and [purchase orders](../../procurement-management/transactions.md#purchase-order).

Fields to note:

- **Document No.**: the order document number.
- **Document Status**: the current status of the order, for example Booked.
- **Order Date**: the date the order was placed.
- **Total Gross Amount**: the total gross amount of the order.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-2.png)

### Partner Shipments

This tab lists all [shipments](../../sales-management/transactions.md#goods-shipment) and [receipts](../../procurement-management/transactions.md#goods-receipts) associated with the selected business partner.

Fields to note:

- **Document No.**: the shipment document number.
- **Document Status**: the current status, for example Completed.
- **Movement Type**: the type of movement, for example Customer Shipment.
- **Movement Date**: the date the movement occurred.
- **Warehouse**: the warehouse from which the shipment was dispatched.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-3.png)

### Partner Invoices

This tab lists all invoices associated with the selected business partner, covering both [sales (AR)](../../sales-management/transactions.md#sales-invoice) and [purchase (AP) invoices](../../procurement-management/transactions.md#purchase-invoice).

Fields to note:

- **Document Type**: the type of invoice document, for example AR Invoice.
- **Document No.**: the invoice document number.
- **Document Status**: the current status, for example Completed.
- **Invoice Date**: the date the invoice was issued.
- **Total Gross Amount**: the total gross amount of the invoice.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-4.png)

### Partner Assets

This tab lists all [assets](../../financial-management/assets/assets.md) associated with the selected business partner, such as equipment or property that the organization tracks in relation to that partner.

---

This work is a derivative of [Master Data Management](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
