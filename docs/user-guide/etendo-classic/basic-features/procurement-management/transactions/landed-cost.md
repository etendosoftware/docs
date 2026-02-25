---
title: Landed Cost
tags:
    - Procurement Process
---

# Landed Cost

:material-menu: `Application` > `Procurement Management` > `Transactions` > `Landed Cost`

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
    - This action creates a *landed cost adjustmen* linked to the landed cost document.
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
    - and landed cost posting gets landed cost invoice *accounting dimensions*.

## Header

A Landed Cost document can be created, processed and posted in this window.

![Landed cost header](../../../../../assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

Some fields to note are:

- **Organization**: that is the organization or legal entity for which landed cost needs to be booked.
- **Reference date**: that is the date when the landed cost document is being created.

**Cost**

A Landed Cost Document can have as many cost (lines) as landed cost types to allocate to the Goods Receipt(s) selected.

![Landed cost tabs](../../../../../assets/drive/1jbfoYTDqyRZiF3bTwPQkG8OmjpLr0zau.png)

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
| [*Product Asset*] | "Estimated" Landed Cost Amount.<br><br>(\*)This ledger entry gets goods receipt "accounting dimensions" such as "Vendor" or "Product". See "Detail" link. |                                |
| [*G/L Item*]      |                                                                                                                                                           | "Estimated" Landed Cost Amount |

#### Process Matching

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

#### Post Matching

A landed cost matching can be posted, after being processed. This posting will have different ledger entries depending on the scenarios listed below:

1\. "**Estimated**" landed cost **equal** to "**invoiced**" landed cost

- In the case of a "product" landed cost type

|                     |                                           |                                                                                                                                                                        |
| ------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                                     | Credit                                                                                                                                                                 |
| [*Product Expense*] | "Estimated"="Invoiced" Landed Cost Amount |                                                                                                                                                                        |
| [*Product Expense*] |                                           | "Estimated"="Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

- In the case of an "account" landed cost type

|              |                                           |                                                                                                                                                                        |
| ------------ | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account      | Debit                                     | Credit                                                                                                                                                                 |
| [*G/L Item*] | "Estimated"="Invoiced" Landed Cost Amount |                                                                                                                                                                        |
| [*G/L Item*] |                                           | "Estimated"="Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

The purpose of above ledger entries is to get that landed cost expense accounting gets invoice landed cost "accounting dimensions".

2\. "**Estimated" landed cost not equal to "invoiced" landed cost** & **"Is matching adjusted" = No**.

This last setup ("Is matching adjusted" = No) leads to NOT creating a landed cost adjustment which takes the difference to the product cost (product accounting), therefore that difference remains either in the credit side (estimated>invoiced) or in the debit side (estimated<invoiced) of the product expense account.

- In the case of a "product" landed cost type

|                     |                               |                                                                                                                                                            |
| ------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                         | Credit                                                                                                                                                     |
| [*Product Expense*] | "Invoiced" Landed Cost Amount |                                                                                                                                                            |
| [*Product Expense*] |                               | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

- In the case of an "account" landed cost type

|              |                               |                                                                                                                                                            |
| ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account      | Debit                         | Credit                                                                                                                                                     |
| [*G/L Item*] | "Invoiced" Landed Cost Amount |                                                                                                                                                            |
| [*G/L Item*] |                               | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

3\. "**Estimated**" landed cost **higher** than "**invoiced**" landed cost. **"Is matching adjusted" = Yes**

This last setup ("Is matching adjusted" = Yes) leads to creating a landed cost adjustment which takes the difference to the product cost (credit side of product accounting).

- In the case of a "product" landed cost type

|                     |                                |                                                                                                                                                            |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                          | Credit                                                                                                                                                     |
| [*Product Expense*] | "Estimated" Landed Cost Amount |                                                                                                                                                            |
| [*Product Expense*] |                                | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |
| [*Product Asset*]   |                                | Difference (estimated>invoiced) Landed Cost Amount                                                                                                         |

- In the case of an "account" landed cost type

|                   |                                |                                                                                                                                                            |
| ----------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account           | Debit                          | Credit                                                                                                                                                     |
| [*G/L Item*]      | "Estimated" Landed Cost Amount |                                                                                                                                                            |
| [*G/L Item*]      |                                | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |
| [*Product Asset*] |                                | Difference (estimated>invoiced) Landed Cost Amount                                                                                                         |

4\. "**Estimated**" landed cost **smaller** than "**invoiced**" landed cost. **"Is matching adjusted" = Yes**

This last setup ("Is matching adjusted" = Yes) leads to creating a landed cost adjustment which takes the difference to the product cost (debit side of product accounting).

- In the case of a "product" landed cost type

|                     |                                                    |                                                                                                                                                            |
| ------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account             | Debit                                              | Credit                                                                                                                                                     |
| [*Product Asset*]   | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [*Product Expense*] | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [*Product Expense*] |                                                    | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

- In the case of an "account" landed cost type.

|                   |                                                    |                                                                                                                                                            |
| ----------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account           | Debit                                              | Credit                                                                                                                                                     |
| [*Product Asset*] | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [*G/L Item*]      | Difference (estimated<invoiced) Landed Cost Amount |                                                                                                                                                            |
| [*G/L Item*]      |                                                    | "Invoiced" Landed Cost Amount<br><br>(\*)This ledger entry gets landed cost invoice "accounting dimensions" such as "Business Partner". See "Detail" link. |

#### Cancel Matching

A landed cost matched can be canceled by using header process button "**Cancel Matching**". Before that landed cost matching needs to be "Unpost".

Cancel matching action implies that:

- Current matched amounts are not removed from Matched Amount tab.
- A new matching needs to be executed in the corresponding landed cost purchase invoice(s).
- Correct matching amounts will then be updated in Matched Amount tab.

### Matched Amount

Matched Amount tab is a read only tab that allows to review the purchase invoice lines matched against landed cost lines.

### Accounting Cost

This tab provides Landed Cost document accounting information.

As any other accounting tabs, this tab shows the ledger journal entries of landed cost posting.

### Receipt

Receipt tab allows the user to select either the receipt(s) or receipt line(s) to which landed cost types booked are going to be allocated.

Once **Landed Cost** header has been properly filled in and saved, a receipt(s) line can be registered in this tab.

Landed cost amounts entered in the "Cost" tab can then be allocated/distributed among the receipt(s) entered here.

Some relevant fields to note are:

- **Good Receipt**: that is to select a goods receipt, therefore landed cost amounts will be distributed among all the lines of the goods receipt.
- **Good Receipt Line**: that is to select a specific good receipt line.

Note that either a good receipt or a good receipt line needs to be selected in a record.

### Receipt Line Amount

Receipt Line Amount is a read only tab that shows detailed information about the landed cost type line allocated to each receipt line, as well as the landed cost amount distributed to each receipt line.

It is important to remark that the "Amount" distributed is calculated by taking into account "Costing" precision defined for the Currency.

### Accounting

This tab provides Landed Cost Matching accounting information.

## Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk posting** button. In this case, this functionality can be used in the **Landed Cost** window and in the **Cost** tab.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
