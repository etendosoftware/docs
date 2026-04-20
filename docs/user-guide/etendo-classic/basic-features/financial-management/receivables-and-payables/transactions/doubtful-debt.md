---
tags:
  - Etendo Classic
  - Financial Management
  - Doubtful Debt
  - Bad Debt
  - Receivables and Payables
---

# Doubtful Debt

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Transactions` > `Doubtful Debt`

## Overview

Doubtful debts are those debts which the company is unlikely to be able to collect. Moreover, a doubtful debt becomes a bad debt when there is no longer any doubt that the debt is uncollectible, therefore:

- **Doubtful Debt**: receivable that might become a bad debt at some point in the future.
- **Bad debt**: receivable that has been clearly identified as not being collectible.

Doubtful debts are useful in order to make provisions for possible losses beforehand.

### User Story

The following example illustrates how Etendo manages Doubtful Debts posting to the ledger.

The Client Healthy Food Supermarkets, Co. who owes the company 1,000 EUR is going through a difficult situation, hence its debt is considered doubtful.

|                       |       |        |
| --------------------- | ----- | ------ |
| Account               | Debit | Credit |
| Doubtful Debt Account | 1000  |        |
| Customer Receivables  |       | 1000   |

|                                     |       |        |
| ----------------------------------- | ----- | ------ |
| Account                             | Debit | Credit |
| Bad Debt Expense Account            | 1000  |        |
| Allowance For Doubtful Debt Account |       | 1000   |

The Client Healthy Food Supermarkets, Co. makes a Payment of 350 EUR:

|                               |       |        |
| ----------------------------- | ----- | ------ |
| Account                       | Debit | Credit |
| In Transit Payment IN Account | 350   |        |
| Doubtful Debt Account         |       | 350    |

|                                     |       |        |
| ----------------------------------- | ----- | ------ |
| Account                             | Debit | Credit |
| Allowance For Doubtful Debt Account | 350   |        |
| Bad Debt Revenue Account            |       | 350    |

Later, the client becomes bankrupt, so its debt is considered bad:

|                       |       |        |
| --------------------- | ----- | ------ |
| Account               | Debit | Credit |
| Write-off             | 650   |        |
| Doubtful Debt Account |       | 650    |

|                                     |       |        |
| ----------------------------------- | ----- | ------ |
| Account                             | Debit | Credit |
| Allowance For Doubtful Debt Account | 650   |        |
| Bad Debt Revenue Account            |       | 650    |

### Configuration

Before starting working with Doubtful Debt, some previous configuration steps are required:

- To configure Accounting for Doubtful Debts. The accounts that need to be configured are:
  - Doubtful Debt Account
  - Bad Debt Expense Account
  - Bad Debt Revenue Account
  - and Allowance for Bad Debts Account.
- To create a Preference in order to be able to see the amount of a debt that has been classified as doubtful when receiving a Payment.  
  This preference must be defined for the Client and the Organization that needs to see it.  
  This preference is an Attribute 'Doubtful_Debt_Visibility' which Value needs to be 'Y'
- To create a Document Type for Doubtful Debts.  
  This step is not a must, since there is already a Standard Document Type defined for Doubtful Debts.

### Doubtful Debt

Doubtful Debts are defined in the Doubtful Debt Run Window. After being created, a record will appear in the grid of this window.

Fields to note:

- **Doubtful Debt Run:** A link to the Doubtful Debt Run that generated this Doubtful Debt
- **Invoice Payment Schedule:** A link to the Payment Plan of the Invoice to which this Doubtful Debt is related.
- **Outstanding Doubtful Debt Amount:** Doubtful Debt Amount which remains pending.

Possible Actions:

- **Reactivate:** A Doubtful Debt can be Reactivated in order to be modified or deleted afterwards. Notice that, like every other document, it cannot be Reactivated if it is Posted. In that case, it is necessary to Unpost it first.
- **Post:** A Doubtful Debt can be posted, creating an entry in the Journal that should look like this:

|                       |                      |                      |
| --------------------- | -------------------- | -------------------- |
| Account               | Debit                | Credit               |
| Doubtful Debt Account | Doubtful Debt Amount |                      |
| Customer Receivables  |                      | Doubtful Debt Amount |

|                                     |                      |                      |
| ----------------------------------- | -------------------- | -------------------- |
| Account                             | Debit                | Credit               |
| Bad Debt Expense Account            | Doubtful Debt Amount |                      |
| Allowance For Doubtful Debt Account |                      | Doubtful Debt Amount |

### Accounting

Accounting information related to the doubtful debt.

## Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk posting** button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
