---
tags:
  - Etendo Classic
  - Financial Management
  - Payment Run
  - Payment Execution
  - Receivables and Payables
---

# Payment Run

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Analysis Tools` > `Payment Run`

## Overview

The payment run window is a read-only window which shows relevant information of each payment run executed within an organization.

A payment run can contain only one payment or several payments grouped and executed together.

It is possible to check the status and result of the payment run as well as the result and message of every single payment inside each payment run.

## Payment Run

The execution date and the execution status of each payment run is shown in this window among other relevant data such as the source of the execution.

![](../../../../../assets/drive/1-_lia6e8AfC9M7ON-PzhrWoRitQW9sSs.png)

The Payment Run window only shows the payments received or made which required an additional execution step, therefore an Automatic Execution Type is configured for the payment method used while making/receiving those payments.

The source of the payment execution can be:

-   **Automatically from Invoice process** - which means that the payment is automatically executed upon invoice completion.
    -   To get this option, the payment method needs to be configured as described below:
        -   the Automatic Receipt check-box is selected for the payments received
        -   and/or the Automatic Deposit check-box is selected for the payments received
        -   and the Deferred checkbox is not selected.
-   **Automatically from Payment process** - which means that the payment is automatically executed upon payment creation.
    -   To get this option the Deferred checkbox needs to be selected.
-   **Execute Payment Form** - which means that the payment has been executed from the Payment Execution form.
    -   To get this option the Deferred checkbox needs to be selected, therefore the deferred payment can be later on executed in the payment execution form.
-   **Payment Proposal Window** - which means that the payment has been executed from the Payment Proposal window.
    -   To get this option the Deferred checkbox needs to be selected, therefore the deferred payment can be later on executed from the payment proposal window.
-   **Payments Window** - which means that the payment has been executed either in the payment out or in the payment in window.
    -   To get this option the Deferred checkbox needs to be selected, therefore the deferred payment can be executed later on in the corresponding payment window.

There are three "Status" available:

-   Executed, which means that the payment run has been executed. The automatic execution processes currently delivered by Etendo will all get an "Executed" status.
-   and "Partially Executed" and "Pending" which are status that can be used by modules such as the Check Printing module to manage those cases where a payment was not successfully executed due to any problem occurring due to a connection failure.

## Payments

The payment tab lists the payments executed in a payment run.

![](../../../../../assets/drive/1porA4UfbmvSes9QKVmxrwr6b8zRav5vK.png)

## Parameters

The parameters tab shows the value of the payment execution process parameter/s.

An Execution Process can have a set of parameters defined.

For instance, the "Print Check simple process" execution process delivered by Etendo only requires the check number upon execution of the payment.

![](../../../../../assets/drive/14j20K8igu1aLPxaZLE1jDu_9jG-ydeaj.png)

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
