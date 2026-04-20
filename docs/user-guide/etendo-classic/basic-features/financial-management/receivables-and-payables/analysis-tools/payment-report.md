---
tags:
  - Etendo Classic
  - Financial Management
  - Payment Report
  - Receivables and Payables
  - Financial Analysis
---

# Payment Report

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Analysis Tools` > `Payment Report`

## Overview

The Payment Report displays Receivables and/or Payables information, which can be filtered by an extensive set of available filters.

Receivables and/or Payables information is shown grouped by the payment status, besides additional grouping and ordering criteria can also be defined.

The Payment Report is an Etendo dimensional report which contains below specific filtering options:

![](../../../../../assets/drive/1PX-rtKZBix9j8-LmDamIE90SjBybrPpM.png)

-   **Dates**: enter a **Date From** and a **Date To** to be used while retrieving the payment's data, in relation to:
    -   the payment due date
    -   the document paid date
    -   and the payment date
-   **Amounts**: enter an **Amount From** and an **Amount To** to be used while retrieving the payment's data
-   **Empty Business Partner**: select whether it is required or not to include in the report payments not related to a business partner but to a **G/L item** or a **Fee**. The options available are:
    -   **Include Empty Business Partner**: if this selection is made, the report includes also payments not related to a business partner.
    -   **Exclude Empty Business Partner**: if this selection is made, the report excludes any payment not related to a single business partner.
    -   **Only Empty Business Partner**: if this selection is made, the report only includes payments not related to a single business partner.
-   the Payment Status: the options available are:
    -   Awaiting Payment
    -   Awaiting Execution
    -   Voided
    -   Payment Made
    -   Payment Received
    -   Deposited not Cleared
    -   Withdrawn not Cleared
    -   Payment Cleared
-   the **Sales Representative.** It will show only Payments related to Invoices that have been invoiced for this Sales Representative.
-   the **Payment Method** and the **Financial Account** of the payment
-   the checkbox **"Include Payments Using Credit"** allows to
-   the **"Convert to Currency"** field allows the user to select a currency, therefore the "Transaction Amounts" in other currency than the one chosen are converted to the chosen currency and displayed in the field "Base Amount".
-   the "**Conversion date**" field allows the user to define a date to select the system conversion rate to exchange transaction amounts.
-   the **Payment Type**: the options available are:
    -   Receivables
    -   Payables
    -   Receivables & Payables
-   the checkbox "**Overdue**" allows the user to include in the report just overdue payments.
-   Finally, it is also possible to define an additional **Grouping Criteria** and **Ordering Criteria** to be used while showing the payment data output.
    -   **Grouping criteria** such as:
        -   Business Partner
        -   Project
        -   Business Partner Category
        -   Currency
        -   Account (Financial Account)
    -   **Ordering criteria** such as:
        -   Date (Payment Date)
        -   Project
        -   Business Partner Category
        -   Currency
        -   Due date (Payment due date)
        -   Account (Financial Account)
        -   Business Partner

!!! warning
    Note that if "Business Partner" for instance is selected as grouping criteria, it will be removed from the ordering criteria list, as grouping implies ordering.


The Payment Report is launched by pressing the process button "**Search**". An example of the output of the report is shown in the image below:

![](../../../../../assets/drive/1c5purjJlxqlGJ5jZjeFLEW0IfBPMWBXX.png)

Some relevant fields to note are:

-   **Invoice Number**: the green arrow allows the user to navigate to the payment plan of the sales/purchase invoice if there is only one invoice number shown in this field.
-   **Payment**: the green arrow allows the user to navigate to the invoice/document's payment
-   **PlannedDSO** (Planned Days Sales Outstanding): the number of days between the date of the invoice and the date it was due to be paid, calculated with the formula **(Invoice) Due date - Invoice Date**.
-   **CurrentDSO** (Current Days Sales Outstanding):
    -   if there is a payment, this field shows the number of days between the date of the invoice and the date of the payment, calculated with the formula **Payment Date - Invoice Date**.
    -   if there is not a payment, this field shows the number of days the invoice is pending to be paid, calculated with the formula **Current Date - Invoice Date**.
-   **Overdue** this fields indicates whether a payment was received on time (overdue number is set to zero), early (overdue number is a negative number) or late (overdue number is a positive number)

An invoice marked with an (*) means that the invoice has been paid by using a credit payment.

Several invoices marked with (**) means that the invoices have been paid by using the same credit payment.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
