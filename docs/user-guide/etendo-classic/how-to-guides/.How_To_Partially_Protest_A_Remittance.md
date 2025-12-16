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

  

#  How To Partially Protest A Remittance

**Languages:** |

** English  ** |  Translate this article...  
  
---|---  
  
##  Contents

  * 1  Objective 
  * 2  Recommended articles 
  * 3  Execution Steps 

  
---  
  
##  Objective

The objective of this article it to provide the necessary steps to partially
protest a remittance.

##  Recommended articles

Please read this article about  Remittances  in Openbravo ERP. It explains
everything you need to know about remittances.

##  Execution Steps

  1. First create a remittance for discount 
  2. Add the invoices to the remittance and process it. A payment will be created that shows the total amount, as well as the amount due of each line of the remittance. If the payment method of the discount remittance is configured as **"Automatic Deposit"** , the total will be deposited in the financial account. Check if it matches with the bank statement line. The rest of the individual payments will be in **"Remitted"** status. 
  3. We recommend not to settle the invoices until it is certain that there will be no refundings to avoid further steps. Then, it comes the day that you receive a refunding for one of the invoices, so you should open the form for **Settle/Protest** of remittances and settle the corresponding single invoice(s) from the remittance (you can select multiple while holding down the **CTRL-Key** ) and subsequently refund the invoice, which will set the status of the individual payment to **"Awaiting Execution"** . 
  4. Navigate to the payment of the refunded invoice with the status **"Awaiting Execution"** and void it. The invoice will pending to be paid. 
  5. In this same window **"Payment In"** , create a new register, adding a **GL Item** with the negative amount of the refund and using the payment method **"Automatic Deposit"** . As a result of that after completing it, the payment will be deposited in the financial account, and it will be available to match it with the bank statement line of the refund. 

Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Partially_Protest_A_Remittance  "

This page has been accessed 5,125 times. This page was last modified on 22 May
2013, at 08:52. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

