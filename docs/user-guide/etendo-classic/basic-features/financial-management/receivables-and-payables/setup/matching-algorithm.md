---
tags:
  - Etendo Classic
  - Financial Management
  - Matching Algorithm
  - Bank Reconciliation
  - Receivables and Payables
---

# Matching Algorithm

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Setup` > `Matching Algorithm`

## Overview

Etendo allows the user to reconcile deposit and withdrawal transactions of a financial account in two ways:

1.  **Automatically** by matching up the bank statement lines (imported or not) with the financial account transactions.  
    In this case, a matching algorithm is necessary to drive the matching process.
2.  **Manually** by using the Reconcile process button of the financial account window.  
    This way of reconciliation does not require a matching algorithm.

Etendo delivers out of the box the "**Standard**" matching algorithm, which can be found and configured in the **Matching Algorithm** window.

## Matching Algorithm

The matching algorithm window lists and allows the user to configure the algorithm/s to use while matching up bank statement lines with financial account transactions.

As shown in the image above, the "**Standard**" matching algorithm has three checkboxes which allow the user to configure the financial account transactions matching process:

-   **Match BP Name:** This option gets a strong match if the business partner name of the bank statement line matches the business partner name of the financial account transaction.
-   **Match Reference:** This option gets a strong match if the reference of the bank statement line matches the reference of the financial account transaction.
-   **Match Transaction Date:** This option gets a strong match if the business partner name of the bank statement line matches the business partner name of the financial account transaction.

!!! info
    It is possible to select all the above checks at once or just some of them in order to configure how to get a strong match.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
