---
tags:
    - How to
    - Account Tree
    - Chart of Accounts
    - Accounting setup
    - Financial Management
---

## Overview

In Etendo, an Account Tree defines the structure of the Chart of Accounts (CoA) used by an organization. When creating a CoA from scratch, each element must be created **individually** and then organized into a **hierarchical structure** that reflects the organization’s financial statements.

The process starts by defining the main nodes for the Balance Sheet and Income Statement, and then progressively creating sub-nodes (Assets, Liabilities, Equity, Revenues, Expenses, etc.) until the full structure is built. 


#### Account Tree creation

A chart of accounts creation from scratch implies to create each chart of accounts element one by one:

-   Once created, the elements can be arranged in a hierarchical way according to the corresponding financial statement structure by using the **Drag & Drop** function of the Tree Structure feature.
-   Moreover, Etendo considers the elements created in an alphanumerical order as a sorted list and finds the position in that sorted list where the new element needs to be positioned.

The steps to follow for the creation of a chart of accounts (CoA) are:

-   select the **Organization** for which the CoA is going to be used while posting to ledger, for example F&B US Inc.
-   enter the **Name** of the Chart of Accounts, for example Test CoA
-   set it up as **User Defined Type** to distinguish it from the imported Chart of Accounts
-   select the **Tree** as B&F International Group Element Value (Account, etc.).

Move to **Element Value** tab.

The first thing to do in this tab is to create all the **Heading** elements one per each financial statement, for instance **Balance Sheet** and **Income Statement**.

**Balance Sheet Node:**

-   create a new record
-   enter **B** value in the field Search Key
-   enter **Balance Sheet** value in the field Name
-   select **Heading** in the Element Level field
-   select **Memo** in the Account Type field
-   select the value **Algebraic** in the field Show Value Condition
-   set the field **Summary Level** to Yes

**Profit and Loss Node:**

-   create a new record
-   enter **P&L** value in the field Search Key
-   enter **Profit and Loss** value in the field Name
-   select **Heading** in the Element Level field
-   select **Memo** in the Account Type field
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

The next thing to do in this tab is to create one element value per each financial statement node:

-   Balance Sheet nodes are **Assets**, **Liabilities** and **Owner's Equity**
-   Profit and Loss nodes are **Revenue** and **Cost of Goods Sold** among others

##### Balance Sheet Elements

Let us focus first on explaining the creation of the nodes/elements of a **Balance Sheet** financial statement.

An organization's balance sheet shows its financial situation at a given point in time, the three sections of a balance sheet are:

-   **Assets**
-   **Liabilities**
-   and **Owner's equity**

therefore the next step to take is to create one chart of account element per each balance sheet node:

**Assets Node:**

To create a new record, enter a value in the field **Search Key**, this value could be a number for instance (1000) or a name (Assets).

!!! info
    It is recommended to use a number as that helps while creating a new chart of accounts elements. The following rule is considered while creating new chart of accounts elements:    
        Etendo first considers the elements in an alphanumerical order as a sorted list, finds the position in that sorted list where the new element needs to be positioned, looks at the element that precedes it and if that element is a summary element and the current element is not a summary one, adds the element as a children of that node otherwise add the element as a sibling of that node.

-   enter **Assets** value in the field Name
-   select **Heading** in the Element Level field
-   select the value **Asset** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

Once done, this node is dragged and dropped under the **Balance Sheet node**.

**Liabilities Node:**

-   create a new record
-   enter the value (2000) in the field Search Key
-   enter **Liabilities** value in the field Name
-   select **Heading** in the Element Level field
-   select the value **Liability** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

**Owners Equity Node:**

-   create a new record
-   enter the value (3000) in the field Search Key
-   enter **Owner's Equity** value in the field Name
-   select **Heading** in the Element Level field
-   select the value **Owner's Equity** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

!!! info
    This time there is no need to drag and drop these two last nodes as Etendo does it according to the rule explained above.


Both the Liabilities Node and the Owner's Equity Node are summary nodes, therefore they are added as a sibling of the Asset Node (element that precedes them).

It is very common to break down assets and liabilities into current assets (or liabilities) and long-term assets (or liabilities).

Moreover, **Assets** can be split into **Cash, Inventory and Accounts Receivable**, **Liabilities** can be split into **Accounts Payable** and **Note Payable** and finally **Owner's Equity** can be split into **Common Stock** and **Retained Earnings** among others.

All of the above guides the creation of the following sub-nodes at a lower level underneath the heading nodes.

**Current Assets Node:**

-   create a new record
-   enter the value (1100) in the field Search Key
-   enter **Current Assets** value in the field Name
-   select **Breakdown** in the Element Level field
-   select the value **Assets** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

Once done, drag this node under the 1000-Assets node.

**Long-Term Assets Node:**

-   create a new record
-   enter the value (1500) in the field Search Key
-   enter **Long-term Assets** value in the field Name
-   select **Breakdown** in the Element Level field
-   select the value **Assets** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

!!! info
    This time, there is no need to drag and drop this last node as Etendo does it according to the rule explained above.


The Long-term Asset Node is a summary node, therefore it is added as a sibling of the Current Asset Node (element that precedes it).

**Current Liabilities Node:**

-   create a new record
-   enter the value (2100) in the field Search Key
-   enter **Current Liabilities** value in the field Name
-   select **Breakdown** in the Element Level field
-   select the value **Liability** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

Once done, drag this node under the 2000-Liabilities node.

**Long-Term Liabilities Node:**

-   create a new record
-   enter the value (2500) in the field Search Key
-   enter **Long-term Liabilities** value in the field Name
-   select **Breakdown** in the Element Level field
-   select the value **Liability** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

!!! info
    This time, there is no need to drag and drop this last node as Etendo does it according to the rule explained above.


The Long-term Liabilities Node is a summary node, therefore it is added as a sibling of the Current Liabilities Node (element that precedes it).

**Cash Node:**

-   create a new record
-   enter the value (1110) in the field Search Key
-   enter **Cash** value in the field Name
-   select **Account** in the Element Level field
-   select the value **Asset** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

Once done, drag this node under the 1100-Current Assets node.

**Accounts Receivable Node:**

-   create a new record
-   enter the value (1120) in the field Search Key
-   enter **Accounts Receivable** value in the field Name
-   select **Account** in the Element Level field
-   select the value **Asset** in the field Account Type
-   select the value **Algebraic** in the field Show Value Condition
-   and set the field **Summary Level** to Yes

!!! info
    This time, there is no need to drag and drop this last node as Etendo does it according to the rule explained above.


The Accounts Receivable Node is a summary node, therefore it is added as a sibling of the Cash Node Node (element that precedes it).

Cash Node needs to have subaccounts elements underneath, for instance:

**111200 Checking Account**

-   create a new record
-   enter 111200 in the field Search Key
-   enter **Checking Account** value in the field Name
-   select **Subaccount** in the Element Level field
-   select the value **Asset** in the field Account Type
-   and select the value **Algebraic** in the field Show Value Condition

**111300 Checking In-Transfer**

-   create a new record
-   enter 111300 in the field Search Key
-   enter **Checking In-Transfer** value in the field Name
-   select **Subaccount** in the Element Level field
-   select the value **Asset** in the field Account Type
-   and select the value **Algebraic** in the field Show Value Condition

**111400 Petty Cash**

-   create a new record
-   enter 111400 in the field Search Key
-   enter **Petty Cash** value in the field Name
-   select **Subaccount** in the Element Level field
-   select the value **Asset** in the field Account Type
-   and select the value **Algebraic** in the field Show Value Condition

Above subaccounts are the ones used while posting ledger entries into the ledger.

!!! info
    There is no need to drag and drop the three subaccounts above into the corresponding node as Etendo does it.


Accounts Receivable Node needs to have subaccounts elements underneath, for instance:

**112100 Trade Receivable**

-   create a new record
-   enter 112100 in the field Search Key
-   enter **Trade Receivable** value in the field Name
-   select **Subaccount** in the Element Level field
-   select the value **Asset** in the field Account Type
-   and select the value **Algebraic** in the field Show Value Condition

**112200 Tax Receivables**

-   create a new record
-   enter 112200 in the field Search Key
-   enter **Tax Receivables** value in the field Name
-   select **Subaccount** in the Element Level field
-   select the value **Asset** in the field Account Type
-   and select the value **Algebraic** in the field Show Value Condition

Above subaccounts are the ones used while posting ledger entries into the ledger.

There is no need to drag and drop the two subaccounts above into the corresponding node as Etendo does it as explained above.

The same steps need to be followed for the creation of other Account and Subaccount node types under the nodes:

-   Long-term Assets
-   Current Liabilities
-   Long-term Liabilities
-   and Owner's Equity

Last but not least, it is required to create a node which summarizes assets, another one which summarizes liabilities and the last one which summarized owner's equity.

Let's take the creation of total assets node, for instance:

**Total Assets Node**

-   create a new record
-   enter 1900 in the field Search Key
-   enter **Total Assets** value in the field Name
-   enter 1100+1500 in the field Description as a way to describe that this node sums up current assets and long-term assets.
-   select **Heading** in the Element Level field
-   select the value **Asset** in the field Account Type
-   and select the value **Algebraic** in the field Show Value Condition
-   navigate to Customized Element tab
-   create a new record
-   enter **1** in the field Sign
-   select the Account **1100 - Current Assets**
-   create a new record
-   enter **1** in the field Sign
-   select the Account **1500 - Long-term Assets**

##### **Income Statement Elements**

Now, let us briefly explain the creation of the nodes/elements of an **Income Statement**.

An organization's income statement shows the company's financial performance over a period of time (usually one year), therefore it has two main sections:

-   the first section details the organization revenues
-   the second section details the organization expenses

The income statement also takes into account the cost of the goods sold, therefore the gross profit refers to the sum of an organization's revenues minus the cost of goods sold.

Besides, it is very common to separate the **Operating Expenses** from the **Non-Operating Expenses**, therefore it is possible to calculate the operating income as the difference between the gross profit and the operating expenses while the net income is the difference between the operating income and the non-operating expenses.

All of the above drives the creation of the nodes/ elements which once arranged will represent the structure of the organization's income statement.

The nodes to create for instance can be:

-   The **Revenue** node:
    -   this Heading and Revenue account type node can include all the revenue subaccounts.
-   The **Total Revenue** node:
    -   this Heading and Revenue account type node can include a customized element of the Revenue node above.
-   The **Cost of the Goods Sold** node:
    -   this Heading and Expense account type node needs can include all the cost of the goods sold related subaccounts.
-   The **Total Cost of the Goods Sold** node:
    -   this Heading and Expense account type node can include a customized element of the Cost of the Goods Sold node above.
-   The **Gross Margin** node:
    -   this Heading and Revenue account type node is a customized element of the Revenue node and the Cost of the Goods Sold node above.
-   the **Operating Expenses** node:
    -   this Heading and Expense account type node can include all the operating expense related subaccounts.
-   The **Total Operating Expense** node:
    -   this Heading and Expense account type node can include a customized element of the Operating Expenses node above.
-   The **Operating Income** node:
    -   this Heading and Revenue account type node can include a customized element of the Revenue node, the Cost of the Goods Sold node and the Operating Expenses node.
-   The **Non Operating Expense** node:
    -   this Heading and Expense account type node can include all the non operating expense related subaccounts.
-   The **Total Non Operating Expenses** node:
    -   this Heading and Expense account type node can include a customized element of the Non Operating Expense node above.
-   and finally the **Net Income** node:
    -   this Heading and Revenue account type node can include a customized element of the Operating Income node above and the Total Non Operating Expense node above.

##### **Temporary Elements**

As already explained, there is a close relationship between an **account tree** and the General Ledger configuration in Etendo, as the Account Tree is a Dimension of the General Ledger.

The General Ledger configuration also includes a set of default accounts (or subaccounts in Etendo terms) to use while posting certain type of transactions. Those accounts need to be created in the account tree first and then be configured in the General Ledger Configuration tabs listed below:

-   [General Accounts](#general-accounts)
-   [Defaults](#defaults)

Most of those defaults accounts are ledger accounts such as:

-   the Income Summary account
-   the Retained Earnings account
-   the Vendor Liability account
-   or the Customer Receivables account

However, there are a few of these accounts which are not ledger accounts but what we can call **Temporary** accounts such as the **Suspense Balancing** account.

!!! info
    It is not necessary to create a default ledger account as those are created as part of the account tree.


However, temporary default accounts need to be created in the account tree under a specific tree branch or node, in order to get that the balance of those temporary accounts is not taken while launching either the Balance Sheet or the Income Statement.

Therefore, a new **Heading** and **Summary** element needs to be created in the **Element Level** tab, that element can be named **Temporary Accounts**.

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-6.png)

Once created, the accounts below (subaccounts) can be created and move underneath it:

-   Suspense Balancing account
-   Suspense Error account

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-7.png)

---

This work is a derivative of [Financial Management](https://wiki.openbravo.com/wiki/Account_Tree){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.