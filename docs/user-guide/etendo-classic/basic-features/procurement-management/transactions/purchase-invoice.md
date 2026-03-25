---
title: Purchase Invoice
tags:
    - Procurement Process
    - Purchase Orders
---

# Purchase Invoice

:material-menu: `Application` > `Procurement Management` > `Transactions` > `Purchase Invoice`

## Overview

The **Purchase Invoice** window is used to create, register, and manage supplier invoices for purchased goods and services.

Purchase invoices are typically generated after a Goods Receipt is completed, ensuring that received quantities match the supplier's billing information.

Invoices are created in two ways:

1. Automatically, from a related Goods Receipt using the **Generate Invoice from Receipt** button in the Goods Receipt window.
2. Manually, by entering the invoice directly in this window.

Each invoice defines the products or services, quantities, prices, taxes, and amounts to be paid to the supplier.

When the invoice is posted, the corresponding purchase expenses are recognized in accounting. If a deferred expense plan is configured, expense recognition is distributed over time according to the defined schedule.

!!! example "Typical Purchase Invoice Workflow"
    1. A Goods Receipt is completed for an existing Purchase Order.
    2. Open the **Purchase Invoice** window and create a new invoice record.
    3. Select the **Business Partner** (supplier). The system fills in the payment terms, payment method, and price list automatically.
    4. Go to the **Lines** tab and click **Create Lines From Receipt** to pull in the received items.
    5. Review the lines, verify quantities and prices, then click **Complete**.
    6. Post the invoice to the ledger using the **Post** button.
    7. Register the payment using the **Add Payment** button.

## Header

The **Header** contains the basic information for a purchase invoice. In most cases, select the **Business Partner**; the system fills the remaining fields from defaults and the selected partner's configuration.

![Purchase invoice window](../../../../../assets/drive/1JvS1mOjiiyATJENTs5SuQIyEAr-UHmE3.png)

Fields to note:

- **Transaction Document**: defaults to *AP Invoice* (purchase invoice [document type](../../financial-management/accounting/setup/document-type.md)). Change it to *AP Credit Memo* (positive-credit type, not linked to orders or shipments) or *Reversed Purchase Invoice* (negative amounts, for returns).
- **Document No.**: supplier invoice number if allowed by sequence, otherwise an internal number is assigned.
- **Invoice Date**: date of the invoice, used to calculate the due date.
- **Accounting Date**: posting date for the ledger (defaults to Invoice Date).
- **Payment Terms**: defines when payment is due (for example, net 30 days). Automatically populated from the Business Partner configuration.
- **Payment Method**: defines the payment mechanism (for example, bank transfer or check). Automatically populated from the Business Partner configuration.
- **Supplier Reference**: optional reference number provided by the supplier.

### Adding Lines

Add invoice lines using one of the following methods:

1. Click **Create Lines From Order** or **Create Lines From Receipt** to pull in pending items from a related document.
2. Click **Copy Lines** to copy lines from an existing invoice.
3. Add lines manually in the **Lines** tab when there is no related order or receipt.

### Completing the Invoice

Click **Complete** to finish the invoice. This creates the Payment Plan and updates the Payment Monitor. If the invoice contains a bundled product (a product made up of multiple components, also called a Bill of Materials or BOM), the system automatically breaks it down into its individual component lines.

After completing the invoice, the following actions are available:

- **Post** the invoice to the ledger using the [Post/Unpost](#postunpost) button.
- **Void or Reactivate** the invoice using the [Reactivate](#reactivate) button.
- **Register a payment** using the [Add Payment](#add-payment) button.

## Lines

Once the Purchase Invoice header is saved, add one or more invoice lines for the products or expenses being billed.

Fields to note:

- **Financial Invoice Line**: Select this for lines that are not physical products — for example, a general ledger account (G/L item) or a fixed asset charge. The Product field is replaced by an Account field.
- **Attribute Set Value**: Shown if the product uses attributes (color, size, serial number, etc.).
- **Purchase Order Line / Goods Receipt Line**: Links the invoice line to the related Purchase Order or Goods Receipt line, if any.

### Deferring Expenses

Use deferred expenses to spread a cost over multiple accounting periods instead of recognizing it all at once.

- **Deferred Expense**: Select this to spread the expense over time and reveal the expense-plan fields.
- **Expense Plan Type**: Frequency of recognition (currently: monthly).
- **Period Number**: Number of periods over which to distribute the expense.
- **Starting Period**: First open accounting period when recognition begins.

These expense-plan values can be defaulted from the product configuration. If an expense plan is used, the invoice accounting follows that plan.

!!! example "Deferred Expense: Annual Insurance"
    A company purchases business insurance for a full year at a cost of 1,200 USD.

    - **Deferred Expense**: selected
    - **Expense Plan Type**: Monthly
    - **Period Number**: 12
    - **Starting Period**: January

    The system recognizes 100 USD per month over 12 months instead of expensing the full 1,200 USD in a single period.

### Explode

The **Explode** button appears when a selected invoice line contains a bundled product (Bill of Materials) that has not yet been broken down into its components. Clicking this button replaces the bundle line with one line per component, so each item appears individually on the invoice.

!!! warning
    This action cannot be undone. To revert it, delete the component lines first and then re-add the bundled product.

### Match LC Cost

The **Match LC Cost** button matches the **estimated landed cost** defined in the Landed Cost window with the **invoiced landed cost** entered in an invoice line.

This option is available when the purchase order or invoice line contains a **product** or **account** configured as a landed cost type. Both costs must belong to the **same landed cost type** to be matched.

Matching helps to:

- Reconcile estimated and invoiced landed costs.
- Keep product costs accurate.
- Generate the correct accounting entries.

After clicking **Match LC Cost**, the pick-and-edit window opens. Only **processed Landed Cost documents** are displayed.

From this window:

- Select the corresponding landed cost document.
- Enter the amount in **Matched Amt**.
- Enable **Process Matching** to complete the process immediately.

The **Is Matching Adjusted** checkbox controls how differences between estimated and invoiced costs are handled:

- **Checked**: creates an additional landed cost adjustment to update the product cost.
- **Unchecked**: no cost adjustment is created.

#### Matching Scenarios

| Scenario | Is Matching Adjusted | Result |
|---|---|---|
| Estimated = Invoiced | Any | Only matching is posted to the ledger. No adjustments are created. |
| Estimated ≠ Invoiced | Checked | A landed cost adjustment is created. Product cost is updated to the invoiced amount. Matching and adjustment are posted. |
| Estimated ≠ Invoiced | Unchecked | Only matching is posted. Product cost is not modified. |

### Line Tax

The **Line Tax** tab is read-only and is automatically populated for each invoice line when the invoice is completed. It details the tax information for each line based on the Tax field, which is pre-filled according to the Taxes Setup.

## Tax

The **Tax** tab summarizes tax-related information for the whole purchase invoice. It contains one record per tax rate used in the invoice.

The **Tax Amount** field reflects the tax value calculated automatically based on the tax rate and tax base settings.

!!! info
    If your organization needs to adjust tax amounts on invoices to match external systems or regulatory requirements (for example, to correct rounding differences of a few cents), this functionality is available through the **Financial Extensions Bundle**.

    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

    For more information, visit: [Adjust Invoice Tax user guide](../../../optional-features/bundles/financial-extensions/adjust-invoice-tax.md)

    This functionality is compatible from Etendo 23.

## Basic Discounts

This tab lists the discounts applied to the purchase invoice. Discounts can be:

- **Automatically applied** based on the supplier's Business Partner configuration.
- **Manually entered** for specific invoice adjustments.

Each discount record shows the discount percentage and whether it is applied in **cascade** (each discount is calculated on the price already reduced by the previous discount — for example, 10% off 100 USD = 90 USD, then 5% off 90 USD = 85.50 USD) or **independently** (each discount is calculated on the original price — 10% + 5% = 15% off 100 USD = 85 USD).

!!! info
    For more information about discount configuration, visit [Basic Discount](../../master-data-management/master-data.md#basic-discount).

## Payment Plan

The **Payment Plan** tab lists the scheduled payments expected against the invoice. Payment plan records are automatically generated when the invoice is completed, based on the **Payment Terms** defined in the header.

Each record shows:

- **Expected Date**: the date when the payment is due.
- **Expected Amount**: the amount to be paid on that date.
- **Payment Method**: the payment mechanism to be used.
- **Outstanding Amount**: the remaining amount not yet paid.

The payment plan of an unpaid invoice can be modified:

- The **Expected Date** can be changed directly in this tab.
- The **Expected Date**, **Payment Method**, and **Outstanding Amount** can also be changed using the [Modify Payment Plan](#modify-payment-plan) button, if the Advanced Bank Account Management module is installed.

## Reversed Invoices

The **Reversed Invoices** tab links a reversal document to the original invoice it reverses. This tab is used in two scenarios:

**Fully voiding an invoice**

When an invoice is voided using the [Reactivate](#reactivate) button with the **Void** action:

- Etendo automatically creates a *Reversed Purchase Invoice* and links it to the original invoice.
- The original invoice appears in the **Reversed Invoices** tab of the reversal document.

**Partially voiding an invoice**

When manually creating a partial reversal (*AP Credit Memo* or *Reversed Purchase Invoice*):

- To link a partial reversal to the original invoice: open the reversal document (the AP Credit Memo or Reversed Purchase Invoice you just created), go to its **Reversed Invoices** tab, and add the original invoice number. This step is required to keep the audit trail between both documents.

## Exchange Rates

The **Exchange Rates** tab allows entering an exchange rate between the organization's general ledger currency and the supplier's invoice currency, to be used when posting the invoice to the ledger.

This tab is relevant when the supplier's invoice currency differs from the organization's general ledger currency, for example, when purchasing goods from a foreign supplier.

The tab allows entering:

- An **exchange rate** between the general ledger currency and the supplier's invoice currency.
- Or the **total foreign invoice amount**, so that Etendo calculates the corresponding exchange rate automatically.

!!! info
    Etendo also maintains a central repository of exchange rates, which is used when no exchange rate is defined at the document level. For more information, visit [General Ledger Configuration](../../financial-management/accounting/setup/general-ledger-configuration.md).

## Accounting

A purchase invoice can be posted to the ledger at a given **Accounting Date** using the [Post/Unpost](#postunpost) button.

### Standard Purchase Invoice Posting

| Account | Debit | Credit | Comments |
|---|---|---|---|
| Product Expense | Line Net Amount | | One per invoice line |
| Tax Credit | Tax Amount | | One per tax line |
| Discount Product Expense | | Discount Amount | One per invoice line (if discount exists) |
| Vendor Liability | | Total Gross Amount | One per invoice |

### Deferred Expense Posting

When a purchase invoice line has an [expense plan](#deferring-expenses) configured, the posting is distributed over multiple periods instead of recognizing the full expense at once.

**Initial posting (Accounting Date):**

| Account | Debit | Credit |
|---|---|---|
| Product Deferred Expense | Line Net Amount | |
| Tax Credit | Tax Amount | |
| Vendor Liability | | Total Gross Amount |

**Each subsequent period (Accounting Date + 1 month, + 2 months, ..., + N months):**

| Account | Debit | Credit |
|---|---|---|
| Product Expense | Line Net Amount / N | |
| Product Deferred Expense | | Line Net Amount / N |

Where **N** is the number of periods defined in the expense plan.

!!! info
    For more information, visit [How to Manage Deferred Revenue and Expenses](../../../how-to-guides/how-to-manage-deferred-revenue-and-expenses.md).

### Reversed Invoice Posting

When an invoice is voided, the reversal document creates the following accounting entries:

| Account | Debit | Credit | Comments |
|---|---|---|---|
| Product Expense | | Line Net Amount | One per invoice line |
| Tax Credit | | Tax Amount | One per tax line |
| Vendor Liability | Total Gross Amount | | One per invoice |

The *AP Credit Memo* posting follows the same structure as the *Reversed Purchase Invoice* posting.

!!! info
    For details on how to void or partially void an invoice, see the [Reactivate](#reactivate) button section.


## Buttons

### Post/Unpost

Post a purchase invoice to the ledger at a given Accounting Date using this button. Once posted, unpost it using the same button.

### Reactivate

![pop-up-reactivate](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/pop-up-reactivate.png)

This button provides two options for a Completed invoice:

- **Reactivate**: returns the record from *Completed* to *Draft* status, allowing edits without creating a new document. Use this option when the invoice contains errors that need correction before reposting.
- **Void**: creates a new document that fully reverses the invoice. Use this option when the invoice is no longer valid and needs to be cancelled.

!!! example "When to Use Each Option"
    - Use **Reactivate** when a price or quantity was entered incorrectly and the invoice has not been paid yet.
    - Use **Void** when goods are returned to the supplier and the entire invoice needs to be cancelled.

**Voiding an invoice**

![pop-up-void](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/popup-void.png)

When voiding, specify the following fields for the reversal document:

- **Void Date**: movement date of the reversal document. Defaults to the current date and cannot be prior to the original Invoice Date.
- **Void Accounting Date**: accounting date of the reversal document. Defaults to the current date and cannot be prior to the original Accounting Date.
- **Supplier Reference**: optional reference number for the reversed document. Enter it here or leave the field blank to complete it later.

Etendo automatically generates a new document in the *Purchase Invoice* window that reverses the original invoice and informs about the new document number.

The reversal document uses the *Reversed Purchase Invoice* transaction document type, which is identical to the original but with negative invoiced quantities.

Once the reversal document is created, change the *Invoice Date* and *Accounting Date* if needed before posting.

The *Reversed Invoices* tab links both the original and the reversal documents.

**Partially voiding an invoice**

It is also possible to partially void a supplier invoice by manually creating one of the following reversed purchase documents in the Purchase Invoice window:

- **AP Credit Memo**: invoiced quantity is positive.
- **Reversed Purchase Invoice**: invoiced quantity is negative.

To link a partial reversal to the original invoice: open the reversal document (the AP Credit Memo or Reversed Purchase Invoice you just created), go to its **Reversed Invoices** tab, and add the original invoice number. This step is required to keep the audit trail between both documents.

To learn more, visit [Reversed Invoices](#reversed-invoices).

The **AP Credit Memo** posting looks the same as the **Reversed Purchase Invoice** posting. The main difference between the two document types is:

- **AP Credit Memo**: invoiced quantity is a positive quantity.
- **Reversed Purchase Invoice**: invoiced quantity is a negative quantity.

!!! note
    Use the **Reversed Purchase Invoice** document type when partially voiding supplier invoices.

### Add Payment

Register one or more payments against a purchase invoice using the **Add Payment** button, which opens the Add Payment pop-up window.

### Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk Posting** button.

The Accounting Status of each record is shown in the status bar in form view, or in a column in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Bulk Completion

!!! info
    To be able to include this functionality, the Essentials Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Essential Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

The Bulk Completion functionality allows the user to complete, reactivate, or void multiple records by selecting them and clicking the **Bulk Completion** button. This makes records management easier and more efficient.

!!! info
    For more information, visit [the Bulk Completion module user guide](../../../optional-features/bundles/essentials-extensions/bulk-completion.md).

!!! warning
    **Note:** If the [Purchase Invoice Validation](../../../optional-features/bundles/procurement-extensions/purchase-invoice-validation.md) module is active in your system, bulk voiding will not work. In that case, void each invoice individually using the **Reactivate > Void** option, which allows entering a unique supplier reference for each reversal.
    ![popup-bulk-void](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/popup-bulk-void.png)

### Remove Payment

The Payment Removal functionality deletes and reactivates payments. It also allows eliminating and reactivating bank transactions and reconciliations.

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

To remove a payment, select the corresponding document and click the **Remove Payment** button. The following related records are also removed:

- If an order is associated with the invoice, the link between the order and the payment is removed (**Purchase Order** window > **Payment Plan** tab).
- If the payment is in *Deposited/Withdrawn not cleared* status in the financial account, the transaction is also deleted (**Financial Account** window > **Transaction** tab).
- If the payment is reconciled through an automatic method, the bank statement line and the bank reconciliation line are also deleted (**Financial Account** window > **Imported Bank Statements** and **Reconciliations**).

!!! info
    If the payment is posted, the accounting entry is deleted too.

![Remove Payment confirmation dialog](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/PRpic4.png)

### Unvoid

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The **Unvoid** button reactivates voided purchase invoices. Select the invoice and click **Unvoid** to restore it.

![Unvoid button restoring a voided purchase invoice to Complete status](../../../../../assets/drive/1UisxZzbpppLvN_rdL__TJg8tLeh5sMfW.png)

Once the process is finished, the purchase invoice status turns to *Complete*.

!!! note
    In the case of the standard version of the module, also unvoid the corresponding reversed invoice.

!!! warning
    **Important:** When you unvoid an invoice, the system restores the original accounting entries. If the reversed invoice was already posted, those entries may still exist, which would cause duplicate accounting entries.

    Before posting the reactivated invoice, check the **Accounting** tab and delete any existing entries that were created by the prior void. If you are unsure whether entries exist, contact your system administrator before proceeding.

!!! info
    Check the Technical documentation about [Advanced Financial Docs Processing](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle/overview.md#advanced-financial-docs-processing) to extend the process.

### Modify Payment Plan

!!! info
    To be able to include this functionality, the Advanced Bank Account Management module of the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The Advanced Bank Account Management module adds a **Bank Account** field to the Purchase Invoice header. This field is automatically filled with the bank account related to the address or business partner of the invoice. The **Modify Payment Plan** button is also added for flexible payment management.

![bank-account.png](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/bank-account.png)

!!! info
    For more information, visit the [Advanced Bank Account Management user guide](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).

## Intercompany

If your company operates multiple legal entities within Etendo (for example, a parent company that purchases on behalf of a subsidiary), the Intercompany functionality automatically creates the matching sales invoice in the receiving organization when a purchase invoice is posted — eliminating the need to register the transaction twice.

When orders or invoices involve two or more organizations that belong to the same client, this functionality automatically generates the corresponding inverse document.

!!! info
    For more information, visit [the Intercompany module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany.md).

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

---

This work is a derivative of [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
