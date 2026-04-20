---
tags:
  - Etendo Classic
  - Financial Management
  - Tax Register Type
  - Tax Payment
  - Receivables and Payables
---

# Tax Register Type

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Setup` > `Tax Register Type`

## Overview

A tax register type is used to collect all the tax rates of a type to take into account while calculating the total tax amount of a given tax register type within a period of time.

Tax register types are a key variable of the Tax Payment process as that is the process which calculates the total tax amount of each tax register type created and configured.

In other words, the "Tax Payment" process helps to calculate the amount of taxes to be paid to or to be received from the corresponding tax authority as the difference between:

-   the "Sales" tax register types or the total tax amount that is charged by an organization and paid by its customers
-   and the "Purchase" tax register types or the total tax amount that is paid by an organization to other businesses on the supplies that it receives.

## Header

The tax register type window allows the user to create tax register types.

![Tax Register Type Header](../../../../../assets/drive/1wwI271qWNtJQmMZxupMktzWI6S3ByU6w.png)

As shown in the image above, it is possible to create:

-   "**Sales**" related tax register types which will therefore include **sales related "Tax Rates"** in the "**Lines**" tab
-   as well "**Purchase**" related tax register types which will therefore include **purchase related "Tax Rates"** in the "**Lines**" tab

Besides, every tax register type needs to be linked to a G/L Item.

The ledger accounts defined for that G/L Item will be the ones to use while posting the tax payment calculated as the difference between the "Sales" tax register type and the "Purchase" tax register type.

## Lines

The lines tab allows the user to associate tax rates to the tax register type.

![Tax Register Type Lines](../../../../../assets/drive/1O_4QacWfrELWWRoG5Ye2E73Fa8AIi8i1.png)

As shown in the image above, each tax rate selected needs also to be linked to a document type.

Therefore, it is not only possible to configure the tax rates which will be taken by the tax payment process as part of a tax register type but also the document types which will be taken into account.

**Sales document types** which can be linked to the corresponding sales tax are:

-   AR Invoice
-   AR Credit Note
-   Reversed Sales Invoice
-   ES Return Material Sales Invoice

**Purchase document types** which can be linked to the corresponding sales tax are:

-   AP Invoice
-   AP Credit Note
-   Reversed Purchase Invoice

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
