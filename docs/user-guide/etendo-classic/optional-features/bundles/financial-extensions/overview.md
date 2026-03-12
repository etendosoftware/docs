---
title: Financial Extensions Bundle
tags:
 - Financial Management
 - Etendo Features
 - Banking
 - Accounting Enhancements
 - Automated Processes
 - Bank Integration
 - Salt Edge
 - Open Banking
 - Financial Account
---

:octicons-package-16: Javapackage: `com.etendoerp.financial.extensions`

:material-store: Etendo Marketplace:  [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}

## Overview
This bundle includes enhancements for Financial Management functionalities in Etendo.

## Translations
-  :material-translate: Spanish: [Financial Extensions Bundle ES](https://marketplace.etendo.cloud/#/product-details?module=0E104B3E36C84992BD7A6D941FBC7AB9){target="_blank"}

## Modules

### Account Structure Validation

:octicons-package-16: Javapackage: `com.etendoerp.account.structure.validation`

This module helps prevent common configuration errors when creating or modifying subaccounts in the Account Tree. It validates the structure and configuration to avoid mismatches in financial reports such as the Income Statement or Balance Sheet.

!!! info
    For more information, visit [the Account Structure Validation Module user guide](../../../optional-features/bundles/financial-extensions/account-structure-validation.md).

### Accounting Dimensions Assets

:octicons-package-16: Javapackage: `com.etendoerp.accounting.dimensions.assets.template`

:octicons-package-16: Javapackage: `com.etendoerp.accounting.dimensions.assets`

<iframe width="560" height="315" src="https://www.youtube.com/embed/1a1UNCnNNcI?si=DbicgZnWjtmkScDh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The Accounting Dimensions Assets module improves asset management and amortization by allowing the user to specify all **available accounting dimensions** during asset creation and management. Also, the Amortization window guarantees more accurate assets tracking **grouped by periods** and more complete amortization calculations.

!!! info
    For more information, visit the [Accounting Dimensions Assets user guide](../../../basic-features/financial-management/assets/overview.md#accounting-dimensions-assets).


### Accounting Templates

:octicons-package-16: Javapackage: `com.etendoerp.accounting.templates`

This module allows setting a non deductible tax's amount to a specified financial account.

!!! info
    For more information, visit the [Accounting Templates user guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/tax-rate.md#purchase-invoice-which-includes-not-deductible-tax-amount).


### Adjust Invoice Tax

:octicons-package-16: Javapackage: `com.etendoerp.adjust.invoice.tax`

This extension enables controlled adjustments to invoice tax amounts to reconcile small **rounding differences** with external systems; it supports both **sales** and **purchase** invoices, offers **manual and automated adjustments** for minimal corrections at cents level, and records all changes for **auditability**, ensuring the final invoice total matches external or regulatory requirements.

!!! info
    For more information, visit the [Adjust Invoice Tax user guide](./adjust-invoice-tax.md).


### Advanced Bank Account Management

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/7AtGyQ62FHs?si=HisPbmd0KzblSq0O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

This module enhances the bank account management enabling greater customization and control over bank account selection associated with customers and vendors. Also, the Modify Payment Plan button is added for better payment management.

!!! info
    This functionality is available in the following windows:

    - [Business Partner](../../../basic-features/master-data-management/master-data.md#advanced-bank-account-management_1)
    - [Sales invoice](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management_1)
    - [Purchase Invoice](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management_1)
    - [Sales order](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management)
    - [Purchase order](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management)
    - [Payment In](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management_1)
    - [Payment Out](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management)

    For more information, visit the [Advanced Bank Account Management](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).

### Advanced Financial Docs. Processing

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pnE-nePaTEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality is part of the Financial Extensions Bundle and it is useful when the user needs to reactivate voided invoices (either Sales or Purchase) and closed orders (either Sales or Purchase) as well as amortizations.

!!! warning "Dependency Notice"
    This module depends on the [**Bulk Completion**](../../optional-features/bundles/essentials-extensions/bulk-completion.md) module, as **order** processing actions must be performed using modern processes that allow the triggering of Hooks, instead of legacy processing. Due to this requirement, the legacy **close/reactivate** actions for orders will be hidden and these actions will only be available through the **Bulk Completion** button.

!!! info
    For more information, visit:

    - [Sales Order](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-closed-sales-order) 
    - [Sales Invoice](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-voided-sales-invoice)
    - [Purchase Order](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-closed-purchase-order)
    - [Purchase Invoice](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-voided-purchase-invoice)
    - [Amortization](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#how-to-reactivate-amortizations)
    - and the [Advanced Financial Docs. Processing developer guide](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle.md#advanced-financial-docs-processing)

### Asset Amortization Report

:octicons-package-16: Javapackage: `com.smf.asset.amortization.report`

The new Amortization report allows downloading excel reports about information on amortization created for a selected year.

!!! info
    For more information, visit [the Asset Amortization Report user guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#asset-amortization-report-excel).

### Automated Remittance

:octicons-package-16: Javapackage: `com.etendoerp.automated.remittance`

This functionality allows the user to automatically process and protest remittances.

!!! info
    For more information, visit [the Automated Remittance user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).

# Bank Integration Overview

:octicons-package-16: Javapackage: `com.etendoerp.psd2.bank.integration`

## Introduction

The Bank Integration module provides **automatic bank integration** for Etendo ERP through two main capabilities:

- **AIS (Account Information Service)**: Securely connect your bank accounts and automatically download bank transactions.
- **PIS (Payment Initiation Service)**: Initiate bank payments directly from Etendo, with authorization handled securely through your bank.

The integration is powered by [Salt Edge](https://www.saltedge.com/){target="_blank"}, a leading Open Banking platform that provides secure access to thousands of banks worldwide, and uses a **centralized middleware** developed by Etendo that manages all communication, security, and compliance.

## Architecture

The integration uses a **three-tier architecture**:

1. **Etendo ERP**: User interface and business logic
2. **Etendo Middleware**: Centralized integration layer (managed by Futit Services)
3. **Salt Edge Platform**: Open Banking connectivity to banks

```
┌─────────────────┐
│   Etendo ERP    │
│  (User Layer)   │
└────────┬────────┘
         │
         │ API Calls
         ▼
┌─────────────────┐
│   Middleware    │
│ (Security Layer)│
└────────┬────────┘
         │
         │ Salt Edge API
         ▼
┌─────────────────┐
│   Salt Edge     │
│ (Open Banking)  │
└────────┬────────┘
         │
         │ Bank APIs
         ▼
┌─────────────────┐
│  Banks / ASPSPs │
└─────────────────┘
```

### Benefits of this Architecture

- **Separation of Concerns**: Etendo focuses on ERP functionality while middleware handles integration complexity
- **Security**: Sensitive credentials and certificates are managed at the middleware level
- **Scalability**: Multiple Etendo instances can share the same middleware
- **Maintainability**: Banking API changes are handled centrally without affecting Etendo instances
- **Compliance**: PSD2 and Open Banking requirements are met at the middleware level

## Key Features

### Account Information (AIS)

- **Automatic transaction import**: Download transactions directly from bank accounts — no need to manually upload bank statement files
- **Configurable date ranges**: Control how far back transactions should be retrieved on initial setup
- **Duplicate prevention**: Automatically filters out duplicate transactions using Salt Edge transaction IDs
- **Statement grouping**: Configure how transactions are grouped into bank statements (per run, per week, or per month)
- **Scheduled processing**: Background process for automatic import across all connected accounts

### Bank Connection Management

- **Secure authentication**: Bank credentials are entered directly on the bank's website via the Salt Edge widget — never stored in Etendo
- **Thousands of banks**: Support for banks worldwide through Salt Edge
- **Connection lifecycle**: Monitor, sync, reconnect, and disconnect bank connections from within Etendo
- **Automatic account sync**: Bank accounts are retrieved automatically when a connection is established

### Payment Initiation (PIS)

- **Direct bank payments**: Initiate payments from Payment OUT records without leaving the ERP
- **Multi-template support**: SEPA (EUR), FPS (GBP), and DOMESTIC payment templates — automatically selected based on currency
- **Bank authorization**: Secure payment authorization through the bank's own authentication page
- **Real-time status tracking**: Monitor payment progress from initiation to execution
- **Automatic status updates**: Receive payment status updates via webhooks and a pre-configured scheduled refresh process
- **Bank Provider management**: Maintain an up-to-date list of banks that support payment initiation

### Monitoring and Logs

- **PSD2 Logs window**: Centralized view of all integration activity and error logs
- **Detailed log entries**: Each log includes financial account, execution date, status, source, description, and raw API response
- **Bank Provider window**: View and manage the list of available bank providers

## User Workflow

### AIS (Account Information)

1. **Setup**:
    - Administrator obtains Salt Edge API Key from Futit Services
    - User configures API Key in their profile (**PSD2 API Key** field)
    - Financial accounts are configured with import date ranges, bank provider, and statement frequency

2. **Connection**:
    - User clicks **Connect Bank Account** on the Financial Account
    - Salt Edge widget opens for bank selection and authentication
    - User authenticates with their bank credentials (entered on the bank's own website)
    - Connection is established and bank accounts are synchronized automatically

3. **Transaction Import**:
    - **Manual**: User clicks **Get Bank Statement** on the Financial Account
    - **Automatic**: Schedule the **Get Bank Statements** process to run periodically
    - Transactions are imported and bank statements are created automatically

4. **Ongoing Use**:
    - Scheduled process imports transactions automatically
    - User reconciles imported transactions using Etendo's reconciliation features
    - Connections are renewed via **Reconnect Connection** when they expire

### PIS (Payment Initiation)

1. **Setup**:
    - Run the **Synchronize Bank Providers** process to populate the provider list
    - Optionally assign a **Bank Provider** to each financial account

2. **Payment**:
    - User creates a **Payment OUT** record as usual
    - Clicks **Generate Bank Payment** — a form appears with pre-filled values
    - Reviews and confirms — a bank authorization popup opens
    - User authorizes the payment in their bank's secure environment

3. **Tracking**:
    - Payment status is updated automatically via webhooks
    - A pre-configured **Refresh Pending Payments** process runs every 10 minutes as a safety net
    - User can also refresh status manually from the **Bank Payments** tab

## Security & Privacy

- **No Credential Storage**: Bank credentials are never stored in Etendo or middleware — users authenticate directly with their bank
- **API Key Security**: Each user has their own API Key for middleware access
- **Encrypted Communication**: All data transmission is encrypted
- **Audit Logging**: All operations are logged in the **PSD2 Logs** window for compliance and troubleshooting

## PSD2 Compliance

The module uses Salt Edge, which is PSD2-compliant, and supports the following Open Banking standards:

- **Account Information Services (AIS)**: Read access to account data and transactions
- **Payment Initiation Services (PIS)**: Initiate payments through the bank
- **Strong Customer Authentication (SCA)**: Bank-level authentication for both connections and payments
- **Connection Lifecycle**: Consent expiration, renewal, and reconnection

## Prerequisites

To use this module, you need:

1. **Financial Extensions Bundle** installed in Etendo
2. **Salt Edge API Key** provided by Futit Services
3. **Financial Accounts** created in Etendo
4. **User permissions** to access Financial Management

!!!info
    For detailed setup and usage instructions, visit the [Bank Integration User Guide](ser-guide-bank-integration.md).

### Banking Pool

:octicons-package-16: Javapackage: `com.etendoerp.bankingpool`

<iframe width="560" height="315" src="https://www.youtube.com/embed/sdPnyewiPbc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This feature allows entering in the system all the financings the company has. It is possible to exploit the information through the bank pool report.

!!! info
    For more information, visit [the Banking Pool user guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#financial-type-configuration) and the [Banking Pool developer guide](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle.md#banking-pool).

### Bulk Posting

:octicons-package-16: Javapackage: `com.etendoerp.bulk.posting`

<iframe width="560" height="315" src="https://www.youtube.com/embed/mgE-NnDLlA0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality allows the user to post or unpost multiple records at the same time. Also included in this module is the **Not Posted Documents** window, which allows users to identify and post all pending transactions directly from one window. 

!!! info
    For more information, visit [the Bulk Posting Module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Business Partner Settlement

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bpsettlement`

:octicons-package-16: Javapackage: `org.openbravo.financial.bpsettlement`

<iframe width="560" height="315" src="https://www.youtube.com/embed/Gh6G1i3Iyts" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality allows the user to create settlements for invoices, both sales and purchase, from the Payment In and Payment Out windows. Also a netting can be performed by creating a settlement from a bank reconciliation for credit in / out from the Financial Account window.

!!! info
    For more information, visit:

    - [Business Partner Settlement - User Guide](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).
    - [Payment In](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-1)
    - [Payment Out](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement)
    - [Financial Account](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-2)

### Conversion Rate Downloader

:octicons-package-16: Javapackage: `com.smf.currency.conversionrate`

:octicons-package-16: Javapackage: `com.smf.currency.apiconfig`

This process allows keeping currency conversions up to date by generating conversion ranks automatically with a background process using apilayer.

!!! info
    For more information, visit the [Conversion Rate Downloader -  User guide](./conversion-rate-downloader.md).

### Deferred GL Journal

:octicons-package-16: Javapackage: `com.etendoerp.gljournal.advanced`

<iframe width="560" height="315" src="https://www.youtube.com/embed/K7XOBkmRLAQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality allows the user to duplicate a journal entry as many times as required, indicating the regularity and the period in which the first copy must be made. Follow the process to create a journal entry from the beginning and duplicate it later.

!!! info
    For more information, visit [the Deferred GL Journal user guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#deferred-gl-journal).


### Financial Advanced Reports

:octicons-package-16: Javapackage: `com.etendoerp.financial.reports.advanced`

:octicons-package-16: Javapackage: `com.etendoerp.financial.reports.advanced.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The **Balance Sheet and P&L Structure Advanced**, **Customer Statement** **General Ledger Report Advanced**, **Journal Entries Report Advanced**, **Purchase Invoice Dimensional Report** and **Trial Balance** reports are an enhanced version of the previous reports including new filters according to the reports accounting dimensions.

!!! info
    For more information, visit:
    
    - [Balance Sheet and P&L Structure Advanced ](../../../basic-features/financial-management/accounting/analysis-tools.md#balance-sheet-and-pl-structure-advanced) user guide.
    - [Customer Statement](../../../basic-features/financial-management/accounting/analysis-tools.md#customer-statement) user guide.
    - [General Ledger Report Advanced](../../../basic-features/financial-management/accounting/analysis-tools.md#general-ledger-report-advanced) user guide.
    - [Journal Entries Report Advanced](../../../basic-features/financial-management/accounting/analysis-tools.md#journal-entries-report-advanced) user guide.
    - [Purchase Invoice Dimensional Report](../../../basic-features/procurement-management/analysis-tools.md#purchase-invoice-dimensional-report) user guide.
    - [Trial Balance](../../../basic-features/financial-management/accounting/analysis-tools.md#trial-balance) user guide.

### Financial Report Budget

:octicons-package-16: Javapackage: `com.etendoerp.financial.report.budget`

<iframe width="560" height="315" src="https://www.youtube.com/embed/2VFxpx8j8Sk?si=TuLZUdBGrOCSpXIE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

This functionality allows creating and managing budgets for reporting purposes, offering users the possibility to compare budgeted values with actual values posted in the corresponding General Ledger.

!!! info
    For more information, visit the [Financial Report Budget guide](../../../basic-features/financial-management/accounting/transactions.md#budget).

### G/L Journal Clone

:octicons-package-16: Javapackage: `com.etendoerp.gljournal.clone`

This functionality allows the user to clone a G/L journal in the Simple G/L Journal window, part of the accounting transactions of financial management.

!!! info
    For more information, visit the [G/L Journal Clone user guide](../../../basic-features/financial-management/accounting/transactions.md#gl-journal-clone).

### Intercompany

:octicons-package-16: Javapackage: `com.etendoerp.advanced.intercompany`

<iframe width="560" height="315" src="https://www.youtube.com/embed/bQjT7iPkYtQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In case the user has to create orders or invoices among two or more organizations that are different but belong to the same client, this functionality allows automatically generating the corresponding inverse document.

!!! info
    For more information, visit [the Intercompany Module user guide](../../../optional-features/bundles/financial-extensions/intercompany.md).

### Payment Removal

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal`

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/TLbjMLjGYwo?si=uGtWnNHNa7gV4_l5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The aim of this functionality is to delete and reactivate payments in an agile and easy way. Also, it allows eliminating and reactivating bank transactions and reconciliations.

The payments to be deleted or reactivated can be found in different statuses: Awaiting execution, Payment made, Payment received, Withdrawn not cleared, Deposited not cleared, Payment cleared (provided that the payment has been reconciled by an automatic method and not by a manual method), Post and Unpost.

The button Remove Payment is available in the Sales Order, Purchase Order, Sales Invoice, Purchase Invoice, Payment In y Payment Out windows.The Reactivate and the Advanced reactivation buttons are only available in the Payment In and Payment Out windows. Finally, the buttons Reactivate Transaction, Remove Transaction, Reactivate Reconciliation and Remove Reconciliation are available in the Financial Account window.


!!! info
    For more information, visit:

    - [Sales Order](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal)
    - [Purchase Order](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal)
    - [Sales Invoice](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal_1)
    - [Purchase Invoice](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal_1)
    - [Payment In](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_1)
    - [Payment Out](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal)
    - [Financial Account](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_2)

### Remittances

:octicons-package-16: Javapackage: `org.openbravo.module.remittance`

:octicons-package-16: Javapackage: `org.openbravo.module.remittance.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/6z3t-E_sV0E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality allows creating a remittance which is a group of "payments" (in/out) or "orders/invoices" that can be remitted to the bank for its payment. The bank will then manage either the collection of the money from the customers or the payment to the vendors/suppliers.

!!! info
    For more information, visit [the Remittances Module user guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#remittance).


### Reverse GL Journal

:octicons-package-16: Javapackage: `com.smf.gljournal.reverse`

:octicons-package-16: Javapackage: `com.smf.gljournal.reverse.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pfqClq8HD6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality is specifically useful for companies that have a month close, instead of an end year close, but with pending payments (in or out). It allows the user to open or close the period without taking into account the payments until they are made.

!!! info
    For more information, visit the [GL Journal user guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#gl-journal) and the [Simple GL Journal user guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#simple-gl-journal).


### VAT Regularization 

:octicons-package-16: Javapackage: `com.etendoerp.vat.regularization`

<iframe width="560" height="315" src="https://www.youtube.com/embed/udarQ6h6EXQ?si=4CNi7Qgi2_yHdW5z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

This functionality enables the user to adjust accounts, ensuring the VAT balance is accurate and correctly aligned.

!!!info
    For more information, visit the [VAT Regularization User Guide](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#vat-regularization).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.