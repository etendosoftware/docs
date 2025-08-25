---
tags:
    - How to
    - Fund Transfers
    - Financial Accounts
    - Bank Transactions
    - Cash Management
---

## Overview

There are many situations in which a company needs to transfer funds to modify or adjust bank and/or cash accounts balance:


- a check deposited in the wrong bank account
- a bank account out of funds...etc.

In Etendo bank and cash accounts are represented as [Financial Accounts](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account).

There are several kinds of funds transfers depending on the financial account type used and the organization for which the transfer of funds takes place:

- From a bank account to another bank account within the same organization.
- From an organization bank account to another organization bank account.
- Same applies to cash accounts.

## Recomended articles

Transferring funds between financial accounts requires a clear understanding on how to create a [G/L Item](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#gl-item).

It is highly recommended as well to understand how [Financial Accounts](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account) and [Account Combination](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#account-combination) work in Etendo.

## Execution Steps

In Etendo, the company in the example will have to withdraw money from one bank or cash account and get it deposited into another bank or cash account.
In other words, the company needs to alter either bank or cash accounts balance whenever it is required. That action could or could not have fees.
Anyway, the steps to follow are:

- GL item creation
        as it is necessary to keep somewhere the funds in-transit balance from the time it is withdrawn from one financial account until the time it is deposited in another financial account.
- Creation of a withdrawal transaction
        in the bank account where funds are taken from.
- Creation of a deposit transaction
        in the bank account where funds are going to be deposited.


## G/L Item creation

A [G/L Item](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#gl-item) is the accounting item to use for accounting in-transit funds. It is key to configure the GL item with the right debit and credit accounts in the Accounting tab. The way to do that is:

- Once the GL item has been created, click on the *Accounting tab* of the [G/L Item](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#gl-item) window.
- Create a new record for each organization's general ledger and assign the same [Account Combination](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#account-combination) for debit and credit.

For instance, the sample account combinations which could be used are:

- US General Ledger configuration:
        1140 Checking In-Transfer
- Spanish General Ledger configuration:
        55500 - Partidas pendientes de aplicación

## Creation of the withdrawal transaction

A withdrawal transaction needs to be created in the Financial Account where the funds are going to be taken from. This step in the process could or could not have fees.

The company in this example needs to:

- navigate to the [Financial Accounts](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account) window
- select the bank to take the money from, for instance Bank A
- press the process button *Add Transaction*
- once in that new window select the *Transaction Type* GL Item
- enter a *Transaction Date*
- select the *GL Item* previously created
- and finally indicate the *Paid Out* amount, for instance 100,00 USD.

This new transaction is then shown in the *Transaction tab* of the *Financial Account* window. Etendo clearly shows the Withdrawal Amount recorded.
The next step is to post the withdrawal transaction. 

!!!note
        It is possible to manually post it by using the process button Post or it could be automatically posted if the Accounting Server Process is enabled in the [Process Request](../../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling.md#process-request) window.

The posting will look like:

| Account                          | Debit  | Credit |
|----------------------------------|--------|--------|
| [GL Item Debit](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#accounting)   | Paid Out Amount |        |
| [Bank A - Withdrawal account](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)              |        | Paid Out Amount |


### Creation of the bank fee

The company in this example needs to create the withdrawal transaction as described previously and an additional transaction to reflect the bank fee. The way to do that is:

- press once more the process button *Add Transaction*
- select the *Transaction Type* Fee
- enter a *Transaction Date*
- and finally indicate the *Paid Out* amount, for instance 1,00 USD.

!!!info
        A bank fee can also be registered in a financial account by using a previously created G/L Item named Bank Interest.Bank Interest accounting could be configured as '7010 Interest income' for credit and '7020 Interest expense' for debit.


In this example, there will be two transactions created in the *Transaction* tab of the *Financial Account*, one for the withdrawal and one for the fee.
Fee transactions can also be posted the same way as the withdrawal transaction.



| Account                          | Debit  | Credit |
|----------------------------------|--------|--------|
| [Bank A -Bank Fee Account](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)   | Paid Out Amount |        |
| [Payment Out-Withdrawal](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)              |        | Paid Out Amount |


## Creation of the deposit transaction

The final step is to create a deposit transaction in the Financial Account where the funds must be deposited.
The company in this example needs to:

- navigate to the [Financial Accounts](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account) window
- select the bank to deposit the money, for instance Bank B
- press the process button *Add Transaction*
- once in that new window select the *Transaction Type* GL Item
- enter a *Transaction Date*
- select the *GL Item* previously created
- and finally indicate the *Received In* amount, in this example 100,00 USD.

This new transaction is then shown in the *Transaction* tab of the *Financial Account* window. Etendo clearly shows the Deposit Amount recorded.
The next step is to post the deposit transaction. It is possible to manually post it by using the process button *Post* or it could be automatically posted if the Accounting Server Process is enabled in the [Process Request](../../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling.md#process-request) window.


The posting will look like:


| Account                          | Debit  | Credit |
|----------------------------------|--------|--------|
| [Bank B - Deposit Account](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)   | Received In Amount |        |
| [GL Item Credit](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#accounting)              |        | Received In Amount |

## Transfer of funds between cash accounts

The company in this example needs to follow exactly the same execution steps. The only difference is the *Financial Account Type* to use. This time a *Cash* financial account type will be used while creating the withdrawal transaction and the deposit transaction.
Transfer of funds between different organizations

## Transfer of funds between different organizations 

The company in this example needs to follow exactly the same execution steps. The only difference is the *Organization* to be used. This time:

- the *GL Item for the in-transit amount to be withdrawn* needs to be created in *Organization A*
- the *withdrawal transaction* needs to be created in a *Financial Account* of *Organization A*
- the *GL item for the in-transit amount to be deposited* needs to be created in *Organization B*
- and finally, the *deposit transaction* needs to be created in a *Financial Account* of *Organization B*

Withdrawal transaction posting in Organization A will look like:

| Account                          | Debit  | Credit |
|----------------------------------|--------|--------|
| [GL Item Debit](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#accounting)   | Paid Out Amount |        |
| [Bank A - Withdrawal account](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)              |        | Paid Out Amount |

Deposit transaction posting in Organization B will look like:


| Account                          | Debit  | Credit |
|----------------------------------|--------|--------|
| [Bank B - Deposit Account](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)   | Received In Amount |        |
| [GL Item Credit](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#accounting)              |        | Received In Amount |

## Result

This completes the transfer of funds between financial accounts. As a result:

- Bank A balance is reduced in 101,00 USD
- Bank B balance is increased in 100,00 USD

Above scenario is just a transfer of funds between financial accounts of the same organization.

In the case of transfer of funds between financial accounts of different organizations:

- Bank A balance of the organization A is reduced in 101,00 USD
- Bank B balance of the organization B is increased in 100,00 USD

Above scenario would somehow mean an expense in Organization A and a revenue in Organization B.

---

This work is a derivative of [How To Guides](https://wiki.openbravo.com/wiki/How_To){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
