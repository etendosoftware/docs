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

  

#  How to implement a new Discount and Promotion Type

##  Contents

  * 1  Introduction 
  * 2  Implementation 
    * 2.1  Type specification 
    * 2.2  Infrastructure 
    * 2.3  Discount and Promotion Type definition 
    * 2.4  PL/SQL Implementation 
      * 2.4.1  Code explanation 
        * 2.4.1.1  Parameters 
        * 2.4.1.2  1\. Get rule configuration 
        * 2.4.1.3  2\. Get line information 
        * 2.4.1.4  3\. Decide whether the rule can be applied 
        * 2.4.1.5  4\. Calculate the discount 
        * 2.4.1.6  5\. Return 
      * 2.4.2  When this code is executed 

  
---  
  
##  Introduction

A discount and promotion type is an implementation of a rule for  Discounts
and Promotions  . These rules define the logic to be applied to calculate the
discount when the discount or promotion can be applied.

This how to targets developers wanting to implement these kind of rules. Users
that need to configure existent ones should read  this other document
instead.

It is possible to define types that take care of a single line, such as _X per
cent discount_ in a single product, and types that look to the whole order or
invoice to determine if the discount is applicable, for example _buying
product X and Y, Z is free_ .

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  In
case the Discount and Promotion Type is intended to be used not only in back
office, but also in Web POS, it is necessary to implement it in both sides.
Here is the how to  to do so.  
---|---  
  
##  Implementation

The implementation of a Discount and Promotion Type is done within a module.
This how to assumes there is already a  module  created.

###  Type specification

This document explains how to create a "Buy X pay Y of same product" type.
This rule applies when there are at least X units in a line, in this case for
each group of X units, only Y are payed.

For example, if the rule can be applied to product A (which price is 10€), X
is 4, and Y is 3. An order including 4 units of A, would have a discount of
10€. An order including 9 units of A, would have a discount of 20€.

###  Infrastructure

The first thing to do is to extend the table that defines Discounts and
Promotions ( ` M_Offer ` ) in case the columns it has do not support the
requirements for our Discount type. In this case we need ` X ` and ` Y `
columns.

    
    
     
    ALTER TABLE M_Offer ADD COLUMN em_obdisc_X numeric;
    ALTER TABLE M_Offer ADD COLUMN em_obdisc_Y numeric;

Note in this case our module's DBPrefix is ` OBDISC ` .

Now columns in Application Dictionary for ` M_Offer ` table should be created:
go to _Tables and Columns_ window, look for ` M_Offer ` table and click on
_Create Columns from DB_ button.

After that, their corresponding fields in _Discounts and Promotions_ window:
go to _Windows, Tabs and Fields_ window, look for ` Discounts and Promotions `
window, ` Discounts and Promotions ` tab and click on _Create Fields_ button.

###  Discount and Promotion Type definition

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_Discount_and_Promotion_Type-1.png){: .legacy-image-style}

To make available the new Type, you just need to register it in _Discounts and
Promotions Types_ window. Create a new record there, select the module you are
working in, and add a descriptive name.

The _PL/SQL Implementor_ field indicates which is the PL function that
implements this type. In this case we have named it ` OBDISC_XY_Same_Product `
.

Once it is created, this Type will be available from _Discounts and
Promotions_ window when defining new rules.

Note it is a good practice, in order to keep this window available, to show
the fields created in the section above just in case this type is selected.
This can be accomplished by adding them a _Display Logic_ which should look
similar to ` @M_Offer_Type_ID@='E08EE3C23EBA49358A881EF06C139D63' ` where `
'E08EE3C23EBA49358A881EF06C139D63' ` is the UUID of the record that has just
been created in _Discounts and Promotions Types_ .

###  PL/SQL Implementation

The code implementing the type is:

    
    
     
    CREATE OR REPLACE FUNCTION obdisc_xy_same_product(p_type character varying, p_rule_id character varying, p_line_id character varying, p_priceprecision numeric, p_stdprecision numeric, p_user_id character varying, p_taxincluded character varying)
      RETURNS character varying AS
    $BODY$ DECLARE 
      v_x NUMERIC;
      v_y NUMERIC;
      v_apply_next VARCHAR(1);
      v_mod NUMERIC;
      v_chunks NUMERIC;
      v_tax VARCHAR(32);
      v_qty NUMERIC;
      v_unitPrice NUMERIC;
      v_newUnitPrice NUMERIC;
      v_newGrossAmt NUMERIC;
      v_newNetAmt NUMERIC;
      v_newNetLine NUMERIC;
      v_priceactual NUMERIC;
      v_basePrice NUMERIC;
      v_origGrossAmt NUMERIC;
      v_origLineNetAmt NUMERIC;
      v_totalPromotion NUMERIC;
    BEGIN
      -- 1. Obtain information about how the rule is configured
      SELECT em_obdisc_x, em_obdisc_y, apply_next
        INTO v_x, v_y, v_apply_next
        FROM m_offer
       WHERE m_offer_id = p_rule_id;
     
      -- 2. Obtain information about the line the promotion can be 
      -- applied to
      IF (p_type ='O') then -- Get info from Order
        SELECT gross_unit_price, c_tax_id, qtyordered, priceactual,
               line_gross_amount, linenetamt
          INTO v_unitprice, v_tax, v_qty, v_priceactual,
               v_origGrossAmt, v_origLineNetAmt
          FROM c_orderline
         WHERE c_orderline_id = p_line_id;
      else -- Get info from Invoice
       SELECT gross_unit_price, c_tax_id, qtyinvoiced, priceactual,
              line_gross_amount, linenetamt
         INTO v_unitprice, v_tax, v_qty, v_priceactual,
              v_origGrossAmt, v_origLineNetAmt
         FROM c_invoiceline
        WHERE c_invoiceline_id = p_line_id;
      end IF;
     
       -- 3. Decide whether the rule can be applied
       IF (v_qty < v_x) then
         RETURN 'Y'; -- rule not applied, apply next one if present
       end IF;
     
       -- 4. Calculate the discount
       v_mod := mod (v_qty, v_x); -- Units without discount
       v_chunks := floor(v_qty / v_x); -- How many times the discount is applied
       
       IF (p_taxIncluded = 'Y') then
         v_newGrossAmt := round(v_chunks * v_y * v_unitprice + v_unitprice * v_mod, p_stdprecision);
         v_newUnitPrice := round(v_newGrossAmt / v_qty, p_priceprecision);
     
         v_newNetLine := c_get_net_price_from_gross(v_tax, v_newGrossAmt, v_newGrossAmt, p_priceprecision, v_qty);
         v_newNetAmt := round(v_newNetLine * v_qty, p_stdprecision);
         v_basePrice := v_unitprice;
         v_totalPromotion := v_origGrossAmt - v_newGrossAmt;
       else
         v_newNetAmt := round(v_chunks * v_y * v_priceactual + v_priceactual * v_mod, p_stdprecision);
         v_newNetLine := round(v_newNetAmt / v_qty, p_priceprecision);
         v_basePrice := v_priceactual;
         v_totalPromotion := v_origLineNetAmt - v_newGrossAmt;
       end IF;
     
       PERFORM M_PROMOTION_ADD(p_type, p_line_id, p_rule_id, p_taxIncluded, 
                               v_newUnitPrice, v_newGrossAmt, v_newNetLine, 
                               v_newNetAmt, v_totalPromotion, v_totalPromotion, 
                               v_basePrice, p_user_id);
     
       -- 5. return whether other discounts can be applied to this same line                           
       RETURN v_apply_next;
    END ; $BODY$
      LANGUAGE plpgsql VOLATILE

####  Code explanation

The following sections explain this code. Numbers in the title refer to
numbers in comments above.

#####  Parameters

Any function implementing a Discount and Promotion Type, must receive the
following parameters:

  * ` p_type ` : Possible values are _O_ or _I_ . _O_ stands for Order and _I_ for Invoice. Indicates whether the rule is being applied to an Order or an Invoice line. 
  * ` p_rule_id ` : ID of the rule ( _M_Offer.M_Offer_ID_ ) that is being checked. 
  * ` p_line_id ` : ID of the line (Order line or Invoice line) the promotion is being applied to. 
  * ` p_priceprecision ` : Based on document's currency, the precision to be used when rounding prices. 
  * ` p_stdprecision ` : Based on document's currency, the precision to be used when rounding amounts. 
  * ` p_user_id ` : ID of the user that has invoked the process, used when creating the actual discount for audit purposes. 
  * ` p_taxincluded ` : Possible values are _Y_ or _N_ . Indicates whether the  Price List  that is applied to current document includes ( _Y_ ) or not ( _N_ ) taxes. 

#####  1\. Get rule configuration

The Discount and Promotion that is currently checked usually has some instance
configuration. In our case values for X and Y, and whether other Promotions
and Discounts can be chained to this same line after applying this one.

#####  2\. Get line information

Line information must be retrieved. Note that the same function is invoked for
Orders and Invoices, determined by ` p_type ` , so both cases must be taken
into account.

#####  3\. Decide whether the rule can be applied

This code is executed for all Promotions and Discounts that are _candidates_
to be applied to each line (see  next section  ). Depending on the rules the
type defines, it is possible this candidate rule to be rejected.

In this case, if the quantity in the line is lower than the value for _X_ ,
the rule is rejected. Note that as the rule is not applied _Y_ is returned,
this means other Discounts can always be applied.

#####  4\. Calculate the discount

At this point we know the Discount must be applied to this line. It is time to
actually implement the amounts to be discounted.

Here it is important to take into account differences between Price Lists that
include taxes and the ones not doing so, as well as correct rounding.

Finally, when everything is calculated the Discount is inserted by invoking `
M_Promotion_Add ` function. It will create a new record in ` C_OrderLine_Offer
` or ` C_InvoiceLine_Offer ` table.

#####  5\. Return

These functions are expected to return a boolean value ( _Y_ or _N_ ). If _Y_
is returned, the algorithm will continue looking for additional Discounts and
Promotions to be applied to this line; whereas in case of _N_ , the algorithm
will stop after applying this one.

####  When this code is executed

The code that checks Discounts and Promotions ( ` M_Promotion_Calculate ` ) is
executed when Order and Invoices are completed or when _Calculate Promotions_
button is clicked on any of these windows.

This code resets prices by removing all possible Discounts and Promotions
previously applied and looks for Discount and Promotions _candidates_ to be
applied to each line of the document.

A Discount _candidate_ is a discount that can be applied to the line based on
the general filters this discount defines. Finally, the PL/SQL that implements
the type is in charge to decide whether the discount is applied or not. For
example, if X is 4 and the rule can be applied to A, any line with product A
will have this rule as candidate, but only the ones with a quantity equals or
greater than 4 should be applied with the discount.

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_implement_a_new_Discount_and_Promotion_Type
"

This page has been accessed 11,163 times. This page was last modified on 7
November 2012, at 08:02. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

