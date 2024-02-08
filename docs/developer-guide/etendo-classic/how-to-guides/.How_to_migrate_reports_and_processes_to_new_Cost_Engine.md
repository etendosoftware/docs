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

  

#  How to migrate reports and processes to new Cost Engine

##  Contents

  * 1  Objective 
  * 2  Acknowledgments 
  * 3  New Data structure 
    * 3.1  New columns in M_Transaction 
    * 3.2  New table M_Transaction_Cost 
    * 3.3  New database function M_Get_Transaction_Cost 
    * 3.4  New database function M_Get_No_Trx_Product_Cost 
    * 3.5  New database function M_Get_Trx_And_Product_Cost 
    * 3.6  New CostingUtils class 
  * 4  Migration 

  
---  
  
##  Objective

The objective of this article is to describe how to migrate existing reports
and processes to the new Cost Engine.

  

##  Acknowledgments

Since Openbravo 3 MP13 it is available a new Cost Engine. This new engine has
many improvements over the old one:

  * Costs is calculated by legal entity. 
    * It is also possible to calculate them by warehouse 
  * Costs are not recalculated, avoiding the need to reset accounting. 
  * It is possible to develop new costing algorithm using extension modules. 
  * Costs are calculated in the legal entity currency 

Refer to  Costing Server  document for extended information.

##  New Data structure

In the new engine the source of the costs has changed because it has to be
independent of the Costing Algorithm used. This means that it cannot be a date
range based cost as in the _M_Costing_ table which works for _Average_ or
_Standard_ costs. Forced by this requirement a new table _M_Transaction_Cost_
has been created. With the new _Costing Engine_ the cost of each material
transaction is calculated, and the result is stored in the new table.
Posterior cost adjustments will also be stored on that table. All costs are
calculated in the legal entity currency. The currency is stored with each cost
calculation to avoid inconsistencies by currency changes in the legal entity.
Existing report and processes need to be adjusted to get the cost information
from these new tables.

###  New columns in _M_Transaction_

_Transaction Process Date (trxprocessdate)_

     The date when the material transaction is processed. All transactions are calculated ordered by this date. 
_Is Cost Calculated (iscostcalculated)_

     Flag that determines that the transaction cost has been calculated. If this is false the cost of the transaction is unknown. 
_Costing Algorithm (m_costing_algorithm_id)_

     Indicates the algorithm used to calculate the cost of the transaction. 
_Transaction cost (transactioncost)_

     The total cost amount of the transaction. This cost does not include subsequent cost adjustments. The cost is always calculated in absolute amounts, this means that when it is an outgoing transaction (negative movement quantity) the cost has to be negated. 
_Currency_

     The currency of the calculated cost amount. It corresponds with the legal entity currency when the cost was calculated. 

###  New table _M_Transaction_Cost_

Main columns:

_Transaction_

     Material transaction that the cost applies to. 
_Cost_

     Total cost amount related to the transaction. 
_Cost Date_

     The date when the cost is recognized. Usually is the transaction process date, but cost adjustments might have later dates. 
_Currency_

     The currency of the calculated cost amount. It corresponds with the legal entity currency when the cost was calculated. 

###  New database function _M_Get_Transaction_Cost_

This function returns the cost of a transaction summing all its transaction
costs with date equals or before the given one and converted to the given
currency. As it is based in the m_transaction table it only returns cost for
products that are Item type and stocked.

Parameters:

_Transaction id_

     Identifier of the transaction whose cost is desired to get. 
_Date_

     Date limit to include all the costs related with the transaction. 
_Currency_

     Currency of the output cost amount. 

###  New database function _M_Get_No_Trx_Product_Cost_

This function is intended to by used to get the products that are not stocked
and Item type. These products won't have records in the m_transaction. It's
cost is defined as _Standard_ cost in the _Costing_ tab of the Product window.
This function can also get costs of _Average_ type. It returns the
corresponding unit cost converted to the given currency.

Parameters:

_Product id_

     Product to get the cost. 
_Movement Date_

     Date when the cost is desired to be valid. 
_Cost Type_

     Cost type of the _M_Costing_ cost. Possible values are AVA ( _Average_ ) and STA ( _Standard_ ) 
_Org id_

     Organization where the cost has to be valid. 
_Warehouse id_

     Warehouse where the cost has to be valid, in case it is defined at warehouse level. 
_Currency id_

     Currency to get the cost in. 
_islegalentity_

     Optional flag that can be used when a legal entity is passed as org id to avoid calculating it inside the function. 

###  New database function _M_Get_Trx_And_Product_Cost_

Common function that returns the total cost amount in the given currency.
Based on the transaction id parameter calls the _M_Get_No_Trx_Product_Cost_
function when its value is null and the _M_Get_Transaction_Cost_ when it is
not null. This function can be used to avoid the complexity of checking the
product type and whether transactions exists or not. Returns the total cost
amount in the given currency.

Parameters:

_Transaction id_

     Identifier of the transaction whose cost is desired to get. 
_Product id_

     Product to get the cost. 
_Movement Date_

     Date when the cost is desired to be valid. 
_Cost Type_

     Cost type of the _M_Costing_ cost. Possible values are AVA ( _Average_ ) and STA ( _Standard_ ) 
_Org id_

     Organization where the cost has to be valid. 
_Warehouse id_

     Warehouse where the cost has to be valid, in case it is defined at warehouse level. 
_Qty_

     Quantity of the movement whose cost is desired to known. Used to calculate the total cost amount when the _M_Get_No_Trx_Product_Cost_ is used. 
_Precision_

     Standard precision of the currency to round the amounts. 
_Currency id_

     Currency to get the cost in. 

###  New CostingUtils class

This utility class has several public methods. Main methods:

_getTransactionCost(MaterialTransaction transaction, Date date, boolean
calculateTrx)_

     Calculates the total cost amount of a transaction including the cost adjustments done until the given date. 
_getStandardCost(Product product, Organization org, Date date, HashMap
<CostDimension, BaseOBObject> costDimensions, boolean
recheckWithoutDimensions) _

     Calculates the standard cost of a product on the given date and cost dimensions. 
_getCurrentValuedStock(Product product, Organization org, Date date, HashMap
<CostDimension, BaseOBObject> costDimensions, Currency currency) _

     Calculates the value of the stock of the product on the given date, for the given cost dimensions and for the given currency. It only takes transactions that have its cost calculated. 

##  Migration

One of the main changes that needs to be considered is that cost is not
dependent of the date as it happens with Average and Standard cost. The costs
have to be retrieved material transaction by material transaction. Existing
reports and processes need to be updated to use the new source instead of the
_M_Costing_ table or _M_Get_Product_Cost(product id, date, cost type)_
database function. In the new cost engine it is needed to get the _Material
Transaction (M_Transaction_ID)_ related to the document. Once we have it is
possible to use the public methods of CostingUtils, the database functions or
a join to the _M_Transaction_Cost_ table. Developer can choose based on
performance or ease criteria.

There are a few things that need to be considered and managed:

  * Only products in the _M_Transaction_ are calculated by new engine. This is only products with product type _Item_ and _stocked_
    * Remaining products cost is defined as a Standard Cost (STA) in the m_costing table.  M_Get_No_Trx_Product_Cost  function is available to calculate it. 
  * There can be transactions that do not have the cost calculated. 
  * Costs are calculated in the currency of the _Legal Entity_ . 
    * This currency is stored with the all the costs. When retrieving those values from the tables it has to be checked if a currency conversion is needed. 
    * Available db functions and methods in CostingUtils class already manage the conversions. 
    * There are related utility methods in FinancialUtils and OrganizationStructureProvider classes. 

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_migrate_reports_and_processes_to_new_Cost_Engine
"

This page has been accessed 6,663 times. This page was last modified on 9
August 2012, at 11:05. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

