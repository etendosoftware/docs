---
tags:
- advanced
- bank account
- financial
- extensions
- bundle
---

# Advanced Bank Account Management

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management.template`

## Overview
This section describes the Advanced Bank Account Management module included in the Etendo Financial Extensions bundle.

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

This functionality enhances the bank account management enabling greater customization and control over bank account selection associated with customers and vendors.

This functionality is available in the following windows: 

- [Business Partner](../../../basic-features/master-data-management/master-data.md#advanced-bank-account-management)
- [Sales invoice]()
- [Purchase Invoice]()
- [Sales order]()
- [Purchase order]()
- [Payment In]()
- [Payment Out]()

## Business Partner - Bank Account

This module introduces the possibility to mark a bank account as Default within the Bank Account tab of the Business Partner window. Here, in the Advanced Bank Account Management field it is possible to check the Default Account checkbox in order to set the account to be used in the documents for different transactions. 

VA

## Business Partner - Location/Address 

The Advanced Bank Account Management field is introduced in the Location/ Address tab of the Business Partner window to associate specific bank accounts to the different locations.  

The default account will always be used when generating a new document unless an account is set up in a specific location. 

VA

## Sales/Purchase Order

A Bank Account field has also been added to the Purchase and Sales Order windows. 

This field is automatically filled based on the selected address. If a specific account is associated with the address, that account is used; if no account is configured, the default account is selected. In cases where neither option is configured, the field remains blank. Payment plans generated from these Purchase and Sales Orders now include the bank account information, inheriting it from the corresponding order.

VA

## Sales/Purchase Invoice

Similarly, a Bank Account field has been added to the Purchase and Sales Invoice windows, which functions in the same manner as in orders. The field is auto-filled based on the selected address, using a specific account if associated, falling back to the default account if none is specified, or remaining blank otherwise. Payment plans created from these invoices inherit the bank account information from the invoices themselves. Additionally, invoices created from Purchase and Sales Orders inherit the bank account information from the respective orders.

VA?

The Payment Plan in Sales Invoice and Purchase Invoice windows now displays the associated bank account information. 

VA?

### Add Payment button

Furthermore, the Add Payment button has been enhanced to include a Bank Account field, allowing users to filter payments by bank account.

VA?

### Modify Payment button

A Modify Payment button is found in both the Purchase and Sales Invoice windows. This feature enables users to specify a bank account for a payment plan and even create multiple payment plans for a single invoice, each associated with a different bank account.

VA?