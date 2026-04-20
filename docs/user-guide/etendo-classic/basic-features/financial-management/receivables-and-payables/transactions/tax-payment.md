---
tags:
  - Etendo Classic
  - Financial Management
  - Tax Payment
  - VAT Settlement
  - Receivables and Payables
---

# Tax Payment

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Transactions` > `Tax Payment`

## Overview

The "Tax Payment" process helps to calculate the amount of taxes to be paid to or received from the tax authority.

Taxes such as the VAT are settled as the difference between:

- the VAT that is charged by an organization and paid by its customers, that is the Output VAT or VAT collected on Sales
- and the VAT that is paid by an organization to other businesses on the supplies that it receives, that is the Input VAT or VAT paid on purchases

Tax payment process can be run after below detailed configuration is done:

- A Tax Authority business partner needs to be created in the business partner window. This business partner needs to be setup as both "Customer" and "Vendor" because sometimes the organization will have to pay to the tax authority and the other way around.
- A G/L item needs to be created and then linked to each Tax Register Type. The G/L item is going to be used to post the corresponding tax payment to the ledger.
  - The "**G/L item Debit Account**" of the G/L item is the account to use while posting a tax payment to be received from the tax authority.
  - The "**G/L item Credit Account**" of the G/L item is the account to use while posting a tax payment to be made to the tax authority.
- As many Tax Register Type as required are linked to the tax rates of each type to take into account for the calculation of the tax payment.

## Header

The tax payment window allows the user to calculate the amount of taxes to be paid to or received from the tax authority within a given period of time. It also allows the user to generate the corresponding payment to/from the tax authority.

![Tax Payment Header](../../../../../assets/drive/1YLUngAGz6MvriT9nplSWvYYnkY7pMnJt.png)

As shown in the image above, the fields to fill in are:

- **Organization**: which is the organization for which the tax payment needs to be calculated
- **Name**: the name of the tax payment calculation
- **Business Partner**: that is the tax authority business partner who either receive the tax payment or make the tax payment.
- **Currency**: the currency of the tax payment
- **Starting Date**: that is the first date to take into account for the tax calculation.
  - Taxes such as the VAT are settled on a monthly basis, therefore the starting date can be the first day of a given month.
- **Ending Date**: that is the last date to take into account for the tax calculation.
  - Taxes such as the VAT are settled on a monthly basis, therefore the ending date can be the last day of a given month.
- **Journal Entry**: that is a read-only field which links to the journal entry created once the tax payment is processed and therefore included in a G/L Journal.
- **Generate Payment checkbox**: this checkbox allows the user to configure if a payment in/out is going to be created after processing the tax payment.
- This checkbox should not be selected in those cases where the tax authority needs to pay to the organization but instead of doing that, it compensates the amounts to be paid to it by the organization.

The **Create VAT Registers button** run the tax payment process and gets the tax amount of each "Tax Register Type" automatically populated in the "Tax Register Header" tab.

The **Process** button process the tax payment and includes the tax settlement posting in a **G/L Journal** accessible from the "**Journal Entry**" field of the Tax Payment window.

The "**Unprocess**" button undoes the tax payment and deletes the G/L Journal created.

## Tax Register Header

Tax Register Header tab allows the user to see the calculated tax amount per each configured "Tax Register Type".

![Tax Register Header](../../../../../assets/drive/1WDw5E4PuOhtmQemNXGYCGt40woWtWUYO.png)

## Lines

The lines tab is a read-only tab which lists all the tax transactions related to the tax rates configured as part of a "Tax Register Type".

![Tax Register Lines](../../../../../assets/drive/1JAQeiows8-fzEHJq0r3TYYD6zWlzRLQ5.png)

Some relevant fields to note are:

- **Tax**: that is the tax rate included as part of the "Tax Register Type".
- **Invoice Tax**: that is the invoice linked to the tax rate.
- **Invoice Date**: that is the invoice date.
- **Document No.**: that is the document number for instance an invoice number.
- **Exempt Amount**: that is an exempt tax amount which will not be included in the tax payment. The set-up is in the customer tab of the business partner.
- **No VAT Amount**: amount that is not included in the tax calculation.
- **Nondeductible Amount**: amount that is non deductible.
- **Taxable Amount**: that is the taxable amount used for the calculation of the tax amount.
- **Tax Amount**: that is the tax amount.
- **Total Amount**: that is the total gross amount of the document/invoice.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
