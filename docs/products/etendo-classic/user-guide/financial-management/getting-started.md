---
tags: 
    - getting started
    - sales management
    - invoice
    - quotation
---

![cover-getting-started.png](/assets/getting-started/overview/cover-getting-started.png)
#

## Overview

Etendo automatically generates an accounting representation of all the transactions within the enterprise that have an economic relevance.

Accounting is the system of tracking the assets, the debts, the income and the expenses of a business.
In Etendo, most of the accounting entries are automatically created while posting [documents]()

- [Goods Receipts]() and [Purchase Invoices]() in the [Procurement Management]() business area
- [Goods Shipments]() and [Sales Invoices]() in the [Sales Management]() business area.

Accounting entries not directly related to [documents]() managed within a given application area can be created and posted in a [G/L Journal](). For instance a provision for stock depreciation accounting entry.

There are three ways of accounting in Etendo:

- To manually post each document by using the process button *Post*.
The process button *Post* can be found in the window used to create a given document. For instance a purchase invoice is created and therefore could be posted in the [Purchase Invoice window]().

   This button is shown for accounting users if the Attribute "ShowAcct" is visible for them. This configuration is enabled through a [Preference]().

- To manually post all the documents/transactions related to a given database table for instance the table *Invoices*, by using the process [GL posting by DB Tables]()

- or to automatically post accounting transactions of any type by scheduling the "Accounting Server Process" in the [Process Request]() window.

Accounting activities such as:

- creating and opening of the accounting periods
- entering and posting accounting transactions
- managing payables and receivables accounts as well as the asset depreciation
- reviewing and submitting financial and tax reports to the official authorities
- and closing the accounting year

are performed within the Financial Management application area.

Finally Etendo has an *integrated accounting system* that combines general accounting and analytical accounting:

- *General accounting* aims to primary exploit dimensions such as *Account* (or *Subaccount* in Etendo terms)
- *Analytical accounting* aims to exploit other dimensions such as *Cost Center* or *Campaign* to get a slightly different but also rich financial information.

In other words, Etendo allows to post transactions to the ledger which can include different dimensions:

- Those dimensions can be centrally maintained in the [Client]() therefore are available to all the organizations within that Client.
Moreover Organizations of that Client can also have additional dimensions configured separately in its [General Ledger Configuration]().

Those dimensions are then available just for that Organization.

- On the other hand, those dimensions can not be centrally maintained in the [Client]() but independently maintained in the [Organization's General Ledger Configuration]().

This application area covers the [Period End Close to Financial Report]() business flow and the [Payables and Receivables Management]() business flow.

## Period End Close to Financial Report

*Period End Close to Financial Report* business flow manages the open and close of periods.

![periodendclose-tofinancialreport.png](/assets/products/etendo-classic/user-guide/financial-management/periodendclose-tofinancialreport.png)

## Configuration

This section details the basic and not that basic accounting configuration needed prior to the execution of the *Period End Close to Financial Report* business flow.

### Basic Configuration

There are three Etendo accounting concepts which need to be explained before describing the basic accounting configuration:

- Fiscal Calendar

A fiscal calendar in Etendo is the year and the periods, normally months, when financial transactions and journal entries are posted to the ledger.

- Account Tree

An account tree is the way Etendo captures the *Chart of Accounts* (CoA) of an Organization.
The Chart of Accounts is a list of all the accounts used in an organization's general ledger.
Accounts such as balance sheet accounts (assets, liabilities and owner's equity) and income statement accounts (revenues, expenses, gains and losses).

!!!Note 
    It is important to remark that in Etendo , the financial reports such as the Balance Sheet and the Income Statement are produced based upon the Chart of Accounts structure.

- General Ledger configuration

The general ledger configuration captures the accounting rules to use while posting the organization's financial transactions to the ledger. Accounting rules such as the *Currency* and the *Chart of Accounts* among others.

Having said that, the accounting configuration detailed in this section is the one required for *legal entities with accounting*, including the business units, because these organization types are the only ones which can have assigned:

- a Chart of Accounts
- a General Ledger configuration
- and a Fiscal Calendar

Obviously these organization types allow posting transactions to the ledger.
Rest of the Organization types behave as explained in the [Initial Organization Setup]() and in the Organization articles.

Very briefly:

- *Legal without accounting* organizations do not require accounting therefore do not require any basic nor advanced accounting configuration.
- *Generic* organizations however can have their own General Ledger configuration and Chart of Accounts but the accounting periods can not be opened and closed independently at its level.
This type of organization inherits the Fiscal Calendar of the *legal with accounting* organization they belong to.
- and finally *Organization* ones can have as well a general ledger configuration and a Chart of Accounts but with the aim of being shared among all the organizations underneath.
This organization type can not have a fiscal calendar assigned and besides the transactions within it are not allowed.

Additionally, some countries such as Spain or France require that a specific *Chart of Accounts* is used in the statutory books, therefore the authorities can see the same list of accounts and the same level of detail in the Income statement and in the Balance Sheet.

On the other hand, there are countries such as the USA where a specific *Chart of Accounts* is not required.

For those cases Etendo provides a [Generic Chart of Accounts]() module which includes a sample Chart of Accounts which can be modified as required.
It is recommended to start from a sample chart of accounts like the generic one and evolve it for the organization's needs rather than starting from scratch.

In-country taxes setup is another key element of the basic accounting configuration.
There can be Localization Packs which include the setup of the taxes for the country while there can be others which do not include the setup of the taxes for the country.
The Generic CoA module does not include any taxes setup.

Having said all of that, there are three possible *accounting* scenarios:

1. Etendo environments with a Localization Pack installed, for instance the Spanish Localization Pack.
A localization Pack which also includes the taxes setup for Spain.

2. Etendo environments with the Generic Chart of Accounts (CoA) installed, mainly in those countries where statutory CoA are not required.

3. and Etendo environments which do not have a Localization Pack installed neither the Generic Chart of Accounts module installed.

The basic accounting configuration is practically the same one for the three scenarios above but the level of defaulted configuration provided by Etendo . Obviously scenario 3 above requires an additional configuration effort.

!!!Info
    It is important to remark that the basic accounting configuration described here is obviously one part of the overall [Business setup]() flow.

### Scenario 1 and 2 - Localization Pack or Generic CoA module installed

These two scenarios can be grouped as the basis of the accounting configuration required for both of them is the same.

The configuration steps to follow are:

- To customize the defaulted *General Ledger configuration* as described in the  [General Ledger configuration maintenance]() article of the Quick Guide.
- To review and maintain the Chart of Accounts created by default as described also in the [Chart of Accounts Maintenance]() article of the Quick Guide.
- Finally, it is also required to set up the *Balance Sheet* and the *Income Statement* as described also in the [Quick Guide]().

It is important to remark that:

If the Localization Pack includes the *in-country taxes* setup, the only configuration left to do is:

  to assign the corresponding [Tax Categories]()to the products
  and to assign the corresponding [Business Partner Tax category]() to the business partners of the Organization, otherwise review the last step of scenario 3 below which describes how to create and set up the taxes.

### Scenario 3 - Localization Pack and Generic CoA do not installed

The enterprise in this scenario should follow below steps which implies an additional configuration effort:
- The creation, setup and maintenance of the [Account Tree]().
- The creation and setup of the [eneral Ledger configuration]().
- The setup of the *Balance Sheet* and the *Income Statement* in the [Balance Sheet and P&L Structure Setup]() window
- The creation and setup of the *Taxes*.

This step implies to create and properly configure three taxes dimensions which are:

  The [Tax Categories](). Tax categories are related to products. When you transact with a product, the tax category is used to determine the rate which gets applied.
Once created need to be linked to the [Products]().

  The [Business Partner Tax Categories]() as there are some business partners who are treated differently from others according to established legal provisions. Business Partner Tax Categories are used to identify these business partners and to incorporate these differences into tax calculations.
  Once created need to be linked to the [Customers]() and [Vendors]()

  And finally the [Tax Rates]() which are the applicable rates for a tax category within the context of a document and its elements (business partner, product, locations).

This scenario is covered in the corresponding articles of the User Guide.
Additionally, all of the three scenarios above require anyway below additional accounting configuration:

- The creation of a [Fiscal Calendar]()
- The creation of the [Years]() of the calendar and the Periods of each year.
The accounting periods of a year can follow the calendar year of January to December, or can differ.
- The opening of the accounting periods is the [Open/Close Period Control]() window.
Etendo  allows to open all the periods of a year at once or to open the first period of a year and later on the next/s, or even to open first a given set of periods.
If a period is not open it is not possible to make any journal entry within that period and get it posted.
- To allow the accounting users to *Post*/*Unpost* transactions as well as to view and edit the ledger accounts contained in the *Accounting* tabs such as the [Accounting]() tab in the product window.
Above is configured by setting for those user/s the [Preference]() *ShowAcct* to *Yes*.
- To schedule the [Accounting Server Process]() in case it is desired that Etendo searches and posts the transactions in status *Complete* suitable to be posted.

### Advanced Configuration

As already mentioned there is an additional accounting configuration which might be needed regardless of whether a localization pack is installed or not.

- The creation of the [G/L Items]().
A G/L item is an “alias” used in place of a sub-account number. A G/L Item can be used to post transactions related to invoices and payments. G/L items are used to account for financial obligations that are not ordinarily invoiced and other special procurement items which are invoiced but for which no ordinary master data (such as a Product) are maintained.

As a side note Etendo contains pre-seeded [Document Types]():

- Each document type in Etendo refers to a business transaction such as a purchase invoice or a sales order.
- The document types allow you to create specific printed formats for business documents and allow you to define sequence numbers for their use.

## Execution 

Overall the Period End Close to Financial Report business flow can be split into the following steps once the accounting period has been opened:

-the opening of the accounting
-the review of the accounting transactions
-the creation of accounting transactions and G/L item payments
-the printing of the Trial Balance
-the adjustments required prior to the income calculation
-the adjustments require prior to the closing of the accounting year
-the printing of the preliminary Income Statement and Balance Sheet
-the closing of the accounting year
-and the printing of the final Income Statement and Balance Sheet

#### Opening of the accounting

This very first step implies to initialize the balance of the ledger accounts and the financial accounts or banks. The way to do that in Etendo is:

- The ledger accounts balance can be initialized by using a [G/L Journal]() set us "Opening", therefore that ledger entry is set as the "Opening Ledger Entry".
A journal line can be created for each account and its opening balance, once done the G/L Journal will validate that the Total Debit of all the entries equals to the Total Credit.
- The financial accounts balance can be initialized in the [Financial Account]() window, in the "Initial Balance" field, therefore the corresponding financial account/s or banks need to be previously created.

!!!Info
    To learn more about this topic, please review the [How to initialize financial balances]() in Etendo article.

#### Review of the accounting transactions

As already mentioned in Etendo most of the accounting entries are automatically created while posting documents such as a purchase invoice or a sales invoice.
For instance the accounting of a purchase invoice will take:

- the expense account setup for the product being purchased in the [Accounting]() tab of the *Product* window
- the vendor liability account setup for the vendor in the [Vendor Accounting]() tab of the *Business Partner* window
- and the tax credit account setup in the [Accounting]() tab of the *Tax Rate* window.

Etendo allows reviewing and correcting if needed the accounting entries of transactional documents such as the Invoices.
Same way Etendo allows unposting wrongly posted transactional documents one by one to get them corrected and properly posted once more.
The way to do that is explained in the [Document-Post/Unpost]() article of the Common Concepts and Processes section.

Additionally, the [Accounting Transactions Details]() report shows all the transactions posted in the ledger with all the details and the [Not Posted Transactions]() report shows the transactions which need to be accounted for but have not been accounted yet.

Finally Etendo allows to massively fix accounting errors if any, for instance a vendor liability account wrongly assigned to a vendor or to a set of vendors.
The way to do that is:

- run the [Reset Accounting]()  process for the table being affected for instance the *C_Invoice* table (Purchase Invoice and Sales Invoice table).
- correct the accounting configuration
- get the transactions posted once again by using the [GL Posting by DB Tables]() feature.
This feature performs a massive posting of all the accounting or just the accounting of a table for instance the *C_Invoice* table (Purchase Invoice and Sales Invoice table).

#### Creation of accounting transactions and G/L item payments

As already mentioned, accounting entries not related to documents managed within a given application area can be created and posted to the ledger by using a [G/L Journal]().
A G/L Journal can also be used to make and/or receive payments do not related to orders/invoices but to G/L items.
G/L items payments are also managed within the [Payables and Receivables management]() area.

#### Printing of the Trial Balance to check that Debit=Credit

The [Trial Balance]() is a list indicating the balances of every single general ledger account at a given point in time.
The purpose of the trial balance is to check that debits are equal to credits. If debits do not equal credits that means that an erroneous journal entry must have been posted.
Etendo does not allow posting journal entries which do not balance. A G/L Journal can only be posted if Debit equals Credit, however there could be situations where while posting an invoice rounding differences drive that debit does not exactly equal credit. In these situations the difference is posted in a specific suspense account. [Suspense]() accounts are configured in the General Ledger configuration.

#### Adjustments required prior to the income calculation

An organization's income statement shows the organization's financial performance over a period of time (usually one year) as the difference between:

- the organization's revenue
- and the organization's expenses

In order to get an accurate income calculation, there are some adjustments required to be done first:

- the organization needs to *review the revenues and the expenses* to be sure that the ones accounted within the period which are going to be closed are the ones which should be accounted regardless whether they are paid or not. This kind of adjustment is not required if the organization follows the accrual method of accounting that is Etendo method of accounting.
Under the accrual method of accounting, revenue is recorded as soon as services are provided or goods are delivered and therefore invoiced, regardless of when cash is received.
Similarly, expenses are recognized as soon as the company receives goods or services and therefore gets invoiced, regardless of when it actually pays for them.

- the organization needs to calculate the *Cost of Goods Sold* (CoGS). The CoGS is the amount that the company paid for the goods that it sold over the course of the period. This calculation depends on the method of keeping track of inventory. There are two primary methods, the perpetual method and the periodic method:

   the perpetual method is used by any business that keeps real-time information on inventory levels and that tracks inventory on an item-by-item basis.
   This method allows very accurate recordkeeping as to the Cost of Goods Sold which is the sum of the cost of all the items sold over the period.

   the periodic method is used by any business that counts inventory at regular intervals.
   When using this method Cost of Goods Sold is calculated using the following equation:
   (Beginning Inventory + Inventory purchases - Ending Inventory = Cost of Goods Sold)
   Besides if a business is dealing with changing per-unit inventory costs, a specific method of calculating the CoGS needs to be used, that could either be FIFO, LIFO or Average Cost.

Finally an income statement can separate *Operating Expenses* such as salaries and rent from *Non-Operating Expenses* such as a lawsuit.

Operating Expenses are the expenses related to the normal operation of the business and are likely to be incurred in future periods as well.

This way allows the calculation of the *Operating Income* as the difference between the *Gross Profit* and the *Total Operating Expenses*.

#### Adjustments required prior to the closing of the accounting year

Other adjustments required can be:

- Long term amounts must be reclassified to short term amounts. The long term amount reclassified to short term amount is the amount due in the next year.
This process is usually done for long term doubts for instance. In Etendo this kind of transaction can be manually created by using a [GL Journal]().
- Taxes such as the VAT needs to be settled periodically.
The [How to Manage VAT settlement and payment]() article explains how to do that in Etendo.
It is important to remark that VAT accounts balance has to be equal to 0 in the last period of the year, as either the organization has to pay to the tax authorities or the other way around.
- Assets depreciation needs to be properly accounted within the period being closed as this adjustment will affect:

   the income statement as depreciation is an expense
   and the debit side of the balance sheet as assets will be decreased by the depreciation amount of the period

#### The printing of the preliminary Income Statement and Balance Sheet





