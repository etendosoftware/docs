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

  

#  How to create a navigation rule

##  Contents

  * 1  Introduction 
  * 2  Navigation Model 
  * 3  Rules definition at field level 
  * 4  Rules definition at table level 
  * 5  Creating Rules 

  
---  
  
##  Introduction

This document describes how to create a navigation rule.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This functionality is available since Openbravo 3.0PR15Q4  
---|---  
  
##  Navigation Model

The navigation model is explained deeply in the following document:
Navigation Model Documentation

##  Rules definition at field level

These rules are defined in the _Navigation Rules_ tab of the _Windows, Tabs
and Fields_ window, below the _Field_ tab.

System administrator can add rules to a field in order to make it navigate to
a custom tab.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_navigation_rule-1.png){: .legacy-image-style}

Main fields that have to be set are:

**Sequence Number**

     Priority of the rule. The rules are applied in ascending order. 
**Tab**

     Destination tab that will be opened if the rule is met. 
**Direct Navigation**

     Flag that determines whether the _HQL Logic_ clause is executed or if the rule is always applied. 
**HQL Logic**

     HQL where clause that the record being opened has to meet in order to open the specified tab of the rule. 

##  Rules definition at table level

The rules at table level for the Extended Navigation Model are defined in a
new tab of the _Tables and Columns_ window called _Navigation Rules_

System administrator can add new rules to a table in order to make the links
which have that table as a reference navigate to a custom tab.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_navigation_rule-2.png){: .legacy-image-style}

The rules are defined following the same logic than Field Level Rules.

##  Creating Rules

To create a rule that it is not of _Direct Navigation_ you have to define the
_HQL Logic_ field with a where clause expression. This expression is appended
to a HQL that it is executed on the table where the record that it is being
opened is stored. The HQL is also filtered by the _id_ of the record so it can
only return that record. If the HQL returns the record then the rule is valid
and it is opened on its _tab_ . If no results are returned it is executed the
next rule.

The _HQL Logic_ has to be a valid HQL where clause. The alias of the main
table is **e** , using it it is possible to access the properties of that
table.

For example the _C_OrderLine_ table has different Order types that are managed
on different windows. Sales orders that are not return orders have to be
opened in the _Sales Order_ window. It is needed to create a rule with an HQL
Logic that returns the order line only in case it is a Sales Order and it is
not a Return. The HQL Logic looks like:

    
    
    e.salesOrder.salesTransaction=true AND e.salesOrder.documentType.return=false
    

You can check in the Application Dictionary how this rule is created and how
there are other rules for purchase and/or return orders.

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_navigation_rule  "

This page has been accessed 4,986 times. This page was last modified on 5
August 2015, at 11:59. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

