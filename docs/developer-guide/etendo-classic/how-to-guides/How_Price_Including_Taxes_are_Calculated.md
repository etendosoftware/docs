![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  How Price Including Taxes are Calculated

##  Introduction

Since the availability of the " **Price Lists Including Taxes** " feature,
there has been some doubts on how net prices/amounts and tax amounts are
calculated.

This how is aimed to explain these calculations in a simple way.

The calculation can be split into two steps:

  1. First one is to calculate the **Net Amount** based on a given **Gross Amount** and then the corresponding **Tax Rate**
  2. Second one is to calculate the **Tax Amount** based on the newly calculated **Net Amount** which then needs to be adjusted so the **Net Amount** plus the **Tax Amount** is equal to the **Gross Amount** . 

##  Net Amount Calculation

In _Openbravo_ cascade taxes  calculation is supported. This means that when
the _Net Amount_ is being calculated we might not have a single rate to work
with, but a relation of different tax rates.

Cascade taxes make the calculation of a net amount from a given gross amount a
bit more difficult. You would normally divide the gross amount by the rate to
get the net amount, but the rate might not be a unique one, in other words it
might not be available therefore it has to be calculated.

To calculate the tax rate we need to calculate the tax amount that corresponds
to the gross price. If we divide that tax amount by the gross price we get the
tax rate.

` `

    
    
               tax amount of gross price
    tax rate = -------------------------
                      gross price
    

Having the tax rate we can calculate the net price:

` `

    
    
                  gross price  
    net price =  -------------
                   tax rate
    

If we substitute the tax rate by the previous formula and simplify it we get:

` `

    
    
                                        gross price
    net price = gross price * ( -------------------------- )
                                 gross price + tax amount
    

This method returns the exact result, but its implementation requires to round
the calculated tax amount.

In former Openbravo MPs this was rounded to the _Price Precision_ of the
currency, thus having a higher price precision was recommended.

After solving the issue  24378  , a 50 decimals precision is used.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q2  ** .  
---|---  
  
After solving the issue  32265  , to help reducing the impact of this rounding
issue instead of using the price, the total gross amount is used to calculate
the net amount which once divided by the quantity, allow us to obtain the net
price. The formula used then is:

` `

    
    
                                                gross amount 
    net price = gross amount * ( ------------------------------------------- ) / quantity
                                  gross amount + tax amount of gross amount
    

##  Taxes Calculation

Once the net amount is calculated it is time to calculate the final tax amount
of the Order or the Invoice.

When taxes are calculated we also need to consider different possible
configurations. Tax amounts might be rounded either at line or document level.

Besides, a single line might have tax amounts of different tax rates, if
cascade tax rates are being used. So subtracting the net amount to the gross
amount is not a valid option.

As the net amounts are known, the standard methods to calculate the tax
amounts based on net amounts are used. However, the calculated net amount has
to be rounded to the standard precision of the currency.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q2  ** .  
---|---  
  
We can have some rounding issues when working with taxes calculated at
document level. This is solved in issue  32265  :

In some cases, the sum of the tax amounts and the net amount might not be
equal to the total gross amount. The difference will be adjusted when
completing the document in the tax amounts, by adding or subtracting the
difference to the higher tax amount so the final sum is correct.

It is also possible that the sum of line net amounts is not equal to the total
net amount. The difference will be adjusted when completing the document, by
adding or subtracting the difference to the higher line net amount so the
final sum is correct.

  

**Some examples with different taxes and gross prices** Tax Example  |  Gross
Amt  |  Net Amt  |  Rounded Net  |  Tax Amount  |  Adjusted Tax  
---|---|---|---|---|---  
Simple 21%  |  1.53  |  1.26446  |  1.26  |  0.26  |  0.27  
Simple 21%  |  1.21  |  1.00  |  1.00  |  0.21  |  0.21  
Simple 21%  |  1.64  |  1.35537  |  1.36  |  0.29  |  0.28  
6.25% + 1%  |  1.56  |  1.454545  |  1.45  |  0.09+0.01  |  0.10+0.01  
6.25% + 1%  |  1.61  |  1.501165  |  1.50  |  0.10+0.01  |  0.10+0.01  
6.25% + 1%  |  1.65  |  1.538461  |  1.54  |  0.10+.0.02  |  0.09+0.02  
  
Retrieved from "
http://wiki.openbravo.com/wiki/How_Price_Including_Taxes_are_Calculated  "

This page has been accessed 23,102 times. This page was last modified on 22
March 2017, at 11:54. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

