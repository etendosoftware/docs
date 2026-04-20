---
tags:
  - Etendo Classic
  - Financial Management
  - Remittance
  - Bank Remittance
  - Receivables and Payables
---

# Remittance

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Transactions` > `Remittance`

<iframe width="560" height="315" src="https://www.youtube.com/embed/6z3t-E_sV0E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Overview

In the Remittance window, the user is able to create remittances to manage payments in or out to customers or suppliers.

A remittance is a group of payments (in/out) or orders/invoices which can be remitted to the bank for its payment. The bank will then manage either the collection of the money from the customers or the payment to the vendors/suppliers.

## Configuration

To be able to use this functionality, it is necessary to configure some aspects first.

- Remittance Dataset: it is necessary to install the Remittance dataset before using the Remittance window. 

    For this, go to the *Enterprise Module Management* window and select the corresponding dataset as shown below.

    ![emm.png](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/enterprise-module-management.png)

    !!! info
        For more information, visit [Enterprise Module Management](../../general-setup/enterprise-model/enterprise-module-management.md).

- Remittance Type: It is necessary to define a remittance type with a certain payment method in the *Remittance Type* window.

    !!! info
        For more information, visit [Remittance Type window](../../financial-management/receivables-and-payables/setup/remittance-type.md).

- Business Partner default bank account: For each business partner, it is possible to   define a bank account that is selected by default each time creating a remittance is necessary.

    !!! info
        To read more, visit [Bank Account](../../master-data-management/master-data.md#remittance) in the Business Partner section.


## Remittance window

![Remittance window](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/remittance-window.png)


As shown in the image above, it is necessary to fill in the fields in the window and different buttons appear so as to continue with the process.


### Buttons

**Select Payments**

Using this button, the user is able to select a payment to be included in the remittance.

**Process**

Using this button, the user processes the payments and groups lines according to the options shown in its corresponding pop-up window. 

!!! info
    If the Automated Remittance module in the Financial Extensions Bundle is installed, this process includes the date setting and the settlement of the remittance.  For more information, visit [the Automated Remittance user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).
   

**Select Invoices and Orders**

In the Remittance window, the *select invoices and orders* button is shown. With this button, the user is able to select not only invoices, but also orders to include in the remittance. In the pop-up window shown when this button is clicked, the user can order and filter each column, payments in and out are shown at the same time and, orders and invoices are shown together.

![filter.png](../../../../../assets/legacy/filter.png)

**Protest Remittance**

!!!info
    This button is only available if the Automated Remittance module in the Financial Extensions Bundle is installed. To install it, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

The Protest Remittance button allows the automatic protest of remittances. This function facilitates the management of protests and the re-settlement of future remittances.

!!! info
    For more information, visit [the Automated Remittance user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).

## Types of Remittances

There are two types of remittances:

**Non-Discount Remittances:** orders/invoices and purchases and/or payments (in/out) are grouped in a remittance that is sent to the bank to be managed.

- The remittance generates a series of payments according to the grouping required by the user (by business partner, due date, among others). The bank usually charges a certain amount for the management of each of these payments, hence the attempt to group them.
- The bank deducts the amount of the remittance from the financial account at the time the remittance is sent, taking care of managing the payments.

**Remittances for Discount:** sales orders/invoices and/or payments are grouped in a remittance that is sent to the bank. The bank advances the amount of the remittance and then manages it itself.

- The remittance generates as many payments (in/out) as those incorporated in the remittance plus one for the global amount, which is the one that is taken to the financial account due to the advance of such amount.
- The bank informs of the payments (in/out) that have been settled (normally, if in one month the bank does not respond, these payments are considered settled) and of those that have been protested.

=== "Non-Discount Remittance"
    To create a Non-Discount remittance follow these steps:

    1. Add a new remittance to the Remittance window and select "printable Remittance" as remittance type since it indicates it is a non-discount remittance.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va.png)

    2. By clicking the "Select Invoices and Orders" button, the system displays a pop up with, by default, the "Show collections/payments for alternative payment methods" selector unchecked, displaying only invoices that have Remittance payment method.
        By checking this checkbox, the system shows all the invoices and orders pending to be taken to the bank. Select those operations needed to remit and process.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va2.png)

        So the system inserts the selected lines:

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va3.png)

    3. If no further operations to the remittance are to be added, process the payment clicking the "Process" button.

        !!! warning
            When using the "process" button and grouping lines, it is necessary for the bank accounts of those lines of a remittance document to coincide. If they are different from one another, Etendo shows an error notification as seen below.

        ![error.png](../../../../../assets/legacy/error.png)

        !!! info
            Bank accounts can be defined in the header of [purchase](../../procurement-management/transactions.md#remittance_1) and [sales](../../sales-management/transactions.md#remittance_1) invoices as well as in [purchase](../../procurement-management/transactions.md#remittance) and [sales](../../sales-management/transactions.md#remittance) orders.


    4. When processing, the system shows the following options:

        - No grouping: generates a payment for each of the selected lines.
        - Group by invoice: generates a payment for each invoice (in case there is more than one).
        - Group by invoice and due date: generates a payment for each invoice and due date.
        - Group by business partner: generates as many payments as there are business partners on the selected lines. It allocates the total amount of all lines that apply to each business partner.
        - Group by business partner and due date: creates as many payments as there are business partners and payment dates on the selected lines.
        - Group by order: generates a payment for each order (in case there is more than one).
        - Group by order and due date: generates a payment for each order and due date.


        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va7.png)

    **Example**

    As an example, let us create the payment by selecting the Group by business partner option.  
    When processing, the 3 payments have been created for the 3 lines included in the remittance due to the fact that all of them correspond to the same business partner.

    ![](../../../../../assets/drive/1-UUBayBZD-1QRbyj3yj62RmFsdw5tkE6.png)

    When navigating to the payment, it can be observed that the status of the payments created is "Remitted".

    ![](../../../../../assets/drive/11-m5CC8wd0k4YLB3BjnqKq9ujwa-GJfm.png)

    When the remittance is posted, an accounting entry is obtained, according to the accounts defined.

    #### Settle/ Protest Remittance

    Once the bank confirms the corresponding payments, access the "Settle/Protest Remittances" window and check the settled and protested remittances.

    !!! info
        The selected date is the posting date of the created document.

    ![](../../../../../assets/drive/1wK9U8kZzmOuxtNJAwZ02iWEgYpYRPrSN.png)

    By settling the first line, it is observed that the line has been added to the settled tab of the corresponding remittance.

    ![](../../../../../assets/drive/1QpvCzdNsUsa4FJBZwvJWH7YfxuapHAO4.png)

    Once the remittance is posted, the accounting entry is obtained according to the indicated configuration. The posting should be line by line of the settled transactions.
    The returned remittance lines will appear in the returned tab.

    The accounting of returned operations are accounted for in the same way as settled operations, from the 401 of the remittance statement to the 400, leaving the outstanding debt again.

    !!! info
        The returned transactions may be managed again later in other remittances or directly in the financial accounts.

    The status of settled remittance transactions is changed to "Withdrawn not Cleared" and in the case of payment outs to "Deposited not Cleared".

    If one of the payments has been returned, the status of the document is set to "Awaiting Execution".

    ![](../../../../../assets/drive/1YZ5mcnLw9KQ5KZ4svYJF9S8vrR-xuvzf.png)

    !!! info
        It is possible to print the Non-discount remittances as well as the Remittances for Discount from the printer in the toolbar.

    #### Settled payments to the financial account

    !!! info
        After the settlement, the system has automatically transferred these payments to the financial account indicated in the payments.

    ![](../../../../../assets/drive/1HAoN4VJmSrj-MdVzuICt4x0pKUt6_fvN.png)

    ##### Reconcile Payments

    The Reconcile Payments option in any remittance process refers to the action of comparing and adjusting financial records to ensure that payments are accurately and properly recorded. By using the *reconcile* button in the *financial account* window, it is possible to access the window shown below.

    ![](../../../../../assets/drive/1B-eqtToHww-gMuD5CldZ2fwBm2x5-OIu.png)

=== "Remittance for Discount"

    To create a remittance for discount follow these steps:

    1. Create a remittance from the Remittances window. Select as type of remittance "Remittances for Discount". Once the header has been   created, add the lines, either invoices, orders or payments, that are to be included in this remittance.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va4.png)

    2. By clicking "Select Invoices and Orders" the system displays a pop up with, by default, the "Show collections/payments for alternative payment methods" selector unchecked, displaying only invoices that have Remittance payment method.
        By checking this check box, the system shows all the invoices and orders pending to be taken to the bank. Select those operations needed to remit and process.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va5.png)

        The system inserts the selected lines:

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va6.png)

    3. If no further operations to the remittance are to be added, process the payment clicking the "Process" button.

        !!! warning
            When using the "process" button and grouping lines, it is necessary for the bank accounts of those lines of a remittance document to coincide. If they are different from one another, Etendo shows an error notification as seen below.

        ![error.png](../../../../../assets/legacy/error.png)

        !!! info
            Bank accounts can be defined in the header of [purchase](../../procurement-management/transactions.md#remittance_1) and [sales](../../sales-management/transactions.md#remittance_1) invoices as well as in [purchase](../../procurement-management/transactions.md#remittance) and [sales](../../sales-management/transactions.md#remittance) orders.


    4. When processing, the system shows the following options:
        - No grouping: generates a payment for each of the selected lines.
        - Group by invoice: generates a payment for each invoice (in case there is more than one).
        - Group by invoice and due date: generates a payment for each invoice and due date.
        - Group by business partner: generates as many payments as there are third parties on the selected lines. It allocates the total amount of all lines that apply to each third party.
        - Group by business partner and due date: creates as many payments as there are third parties and payment dates on the selected lines.
        - Group by order: generates a payment for each order (in case there is more than one).
        - Group by order and due date: generates a payment for each order and due date.

        In this case, it is recommended to select the option "No grouping", since as many payments as operations of the remittance will be generated and a payment sum of all the operations which is the one that the bank will advance. The rest of the payments will be settled as known.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va7.png)

    5. The next step is to take to the bank the sum payment of the remittance transactions, as in these cases the bank advances the money. From the financial account window, add the payment to the transaction and reconcile it with the bank statement.
      ![](../../../../../assets/drive/1jeThcgRV1wHyXRiOZpG2N-w-uuMVgAqo.png)

    6. Finally, settle the executed payments and/or return the necessary ones.
      ![](../../../../../assets/drive/1ZbcAE5TCXIEo4wQU6AHrdtlhaQAVmZeC.png)
      The status of the settled collections changed to Settled in Remittance and the status of the total payments of the remittance operations changed to Payment cleared.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
