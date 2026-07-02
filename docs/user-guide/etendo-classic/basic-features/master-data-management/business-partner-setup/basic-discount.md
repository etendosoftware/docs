---
title: Basic Discount
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Discount
---

## Basic Discount

:material-menu: `Application` > `Master Data Management` > `Business Partner Setup` > `Basic Discount`

A Basic Discount is a deduction from the total amount of an order or an invoice.

### Overview

Discounts of this type means a sum of the total order / invoice discount amounts, excluding taxes per each tax rate.

Discounts tab can be found in the Purchase & Sales Order / Invoice windows and allows the user to add discounts manually or to review the ones automatically applied by Etendo based on the Business Partner Discount tab configuration.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/basic-discount/basic-discount-1.png)

Discounts

- When an order or an invoice is in _Draft_ status, the total amounts are the totals amounts including tax, but excluding discounts.
- Once the order/invoice is _Processed_, Etendo calculates the monetary value of the corresponding discounts and shows them as new order/invoice lines.
  - Discount lines have no product nor account but the discount product (see below).
  - Besides, Etendo creates as many new invoice lines as discounts included in the invoice as well as tax rates (%).
  - Discount lines have an ordered quantity equal to "1" and a Net Unit Price equal to the calculated discount amount with an opposite sign to the invoice amount (normally negative) in order to reduce it.
- Finally, discounts can be calculated in cascade.
  - Cascade calculation implies that the first discount is applied to the total net amount and the second discount is applied to the total net amount already decreased by the first discount amount, and so on. Configured in the Business Partner Discount tab.

**Example 1. Purchase invoice containing just one tax rate:**

- Let us imagine a purchase invoice containing two invoice lines for a net line amount of _1,000.00_ each.
- A _18%_ tax rate applies to both purchase order lines.
- There is a _10%_ Discount assigned to the supplier, therefore that discount is shown in the Discounts tab.
- Once above purchase invoice is booked:
  - Etendo shows just one new line with below information:
    - **Product** named _Discount 10%_ which is the one created and linked to the discount.
    - **Invoiced Quantity** equals to _1_.
    - **Net Unit price** equal to the applicable discount amount, which in our example is _\-200_ (10% of the total net amount _2,000.00_).

**Example 2. Purchase invoice containing two different tax rates:**

- Let us imagine a purchase invoice containing two invoice lines for a net line amount of _1,000.00_ each.
- A _18%_ tax rate applies to the first purchase invoice line, and an _8%_ tax rate applies to the second one.
- There is a _5%_ Discount assigned to the supplier, therefore that discount is shown in the **Discounts** tab.
- Once above purchase invoice is booked:
  - Etendo shows two new lines, each of them with below information:
    - **Product** named _Discount 5%_ which is the one created and linked to the "Discount".
    - **Invoiced Quantity** equals to _1_.
    - **Net Unit Price** equals the applicable discount amount, which in our example is _\-50_ (_5%_ of the total net amount at a given tax rate _1,000.00_).

### Basic Discount

A total discount can be created and configured by entering a discount name, a discount product and a discount %.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/basic-discount/basic-discount-2.png)

Fields to note:

- Previously created Product you could name the same as the discount name. That product is the one to be filled in the new orders / invoice line/s to manage this type of discounts (see above).
