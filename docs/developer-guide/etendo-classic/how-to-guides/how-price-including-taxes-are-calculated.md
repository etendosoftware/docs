---
tags: 
  - price
  - taxes
  - price lists
  - net amount calculation
---

#  How Price Including Taxes are Calculated

##  Overview

This section is aimed to explain the **Price Lists Including Taxes** feature in a simple way and revise how net prices/amounts and tax amounts are calculated.


The calculation can be split into two steps:

  1. The first one is to calculate the **Net Amount** based on a given **Gross Amount** and then the corresponding **Tax Rate**.
  2. The second one is to calculate the **Tax Amount** based on the newly calculated **Net Amount** which then needs to be adjusted so the **Net Amount** plus the **Tax Amount** is equal to the **Gross Amount**. 

##  Net Amount Calculation

In Etendo Classic, [cascade taxes](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup.md#tax-rate) calculation is supported. This means that when the **Net Amount** is being calculated, we might not have a single rate to work with, but a relation of different tax rates.

Cascade taxes make the calculation of a net amount from a given gross amount a bit more difficult. You would normally divide the gross amount by the rate to get the net amount, but the rate might not be a unique one, in other words it might not be available therefore it has to be calculated.

To calculate the tax rate, we need to calculate the tax amount that corresponds to the gross price. If we divide that tax amount by the gross price, we get the tax rate.

``` 
  
              tax amount of gross price
  tax rate = -------------------------
                    gross price
``` 

Having the tax rate, we can calculate the net price:

```

                gross price  
  net price =  -------------
                  tax rate
``` 

If we substitute the tax rate by the previous formula and simplify it, we get:

```
  
                                      gross price
  net price = gross price * ( -------------------------- )
                                gross price + tax amount
```  

This method returns the exact result, but its implementation requires to round the calculated tax amount. A 50 decimals precision is used.
  
To help reducing the impact of this rounding issue instead of using the price, the total gross amount is used to calculate the net amount which once divided by the quantity, allow us to obtain the net price. The formula used then is:

```
  
                                              gross amount 
  net price = gross amount * ( ------------------------------------------- ) / quantity
                                gross amount + tax amount of gross amount
```

##  Taxes Calculation

Once the net amount is calculated, it is time to calculate the final tax amount of the Order or the Invoice.

When taxes are calculated, we also need to consider different possible configurations. Tax amounts might be rounded either at line or document level.

Besides, a single line might have tax amounts of different tax rates, if cascade tax rates are being used. So subtracting the net amount to the gross amount is not a valid option.

As the net amounts are known, the standard methods to calculate the tax amounts based on net amounts are used. However, the calculated net amount has to be rounded to the standard precision of the currency.

### Rounding Issues

We can have some rounding issues when working with taxes calculated at document level.

In some cases, the sum of the tax amounts and the net amount might not be equal to the total gross amount. The difference will be adjusted when completing the document in the tax amounts, by adding or subtracting the difference to the higher tax amount so the final sum is correct.

It is also possible that the sum of line net amounts is not equal to the total net amount. The difference will be adjusted when completing the document, by adding or subtracting the difference to the higher line net amount so the final sum is correct.

**Some examples with different taxes and gross prices** 

Tax Example  |  Gross Amt  |  Net Amt  |  Rounded Net  |  Tax Amount  |  Adjusted Tax  
---|---|---|---|---|---  
Simple 21%  |  1.53  |  1.26446  |  1.26  |  0.26  |  0.27  
Simple 21%  |  1.21  |  1.00  |  1.00  |  0.21  |  0.21  
Simple 21%  |  1.64  |  1.35537  |  1.36  |  0.29  |  0.28  
6.25% + 1%  |  1.56  |  1.454545  |  1.45  |  0.09+0.01  |  0.10+0.01  
6.25% + 1%  |  1.61  |  1.501165  |  1.50  |  0.10+0.01  |  0.10+0.01  
6.25% + 1%  |  1.65  |  1.538461  |  1.54  |  0.10+.0.02  |  0.09+0.02  

---

This work is a derivative of [How Price Including Taxes are Calculated](http://wiki.openbravo.com/wiki/How_Price_Including_Taxes_are_Calculated){target="blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 