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

  

#  How to create a Multi Selector

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Contents in this document are available from **3.0MP20**  
---|---  
  
##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  Steps to implement the Process 
    * 3.1  Overview 
    * 3.2  Defining the Selector 
    * 3.3  Adding fields to Selector's Pop Up 
    * 3.4  Using the Selector 
    * 3.5  Retrieving values in backend 
  * 4  Advanced topics 
    * 4.1  Using custom query selector 
  * 5  Limitations 

  
---  
  
##  Introduction

_Multi Selector_ is a reference that allows to select multiple items at the
same time. It is intended to be used as parameter of _ Standard Process
Definition  _ .

Multi Selector reference is defined pretty much as regular selectors (which
allow to select a single value). For more information about selectors take a
look to this  example  .

##  Example Module

This howto is supported by an example module which shows examples of the code
shown and discussed.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), for more information see the  Examples Client
Application  project page.

##  Steps to implement the Process

###  Overview

This howto explains how to create a Multi Order selector.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Multi_Selector-1.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Multi_Selector-2.png){: .legacy-image-style}

###  Defining the Selector

  * As _System Administrator_ open _Reference_ window. 
  * Create a new record. 
    * Name: Multi Order Selector 
    * Parent Reference: OBUISEL_Multi Selector Reference 
  * In _Defined Selector_ tab, set the properties for the selector: 
    * Template: Selector Template 
    * Table: C_Order 

###  Adding fields to Selector's Pop Up

Last step is to define which are the fields that will be present in the popup
to select records.

  * Go to _Defined Selector Field_ tab 
  * Create records: 
    * Name: it is the name the use will see (i.e. Business Partner) 
    * Property: actual property to retrieve information from (i.e. businessPartner) 
    * Sorting of columns in the grid: Position of this column in the grid (i.e. 20) 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Multi_Selector-3.png){: .legacy-image-style}

###  Using the Selector

This selector can be used as parameter for a Process Definition. In  this
howto  it is used.

###  Retrieving values in backend

In backend, the Java implementing the process, receives an ` JSONArray ` with
the IDs of all selected rows. In case no row is selected, an empty array is
received.

    
    
     
          //...
          JSONArray orders = params.getJSONArray("orders"); // get the array
         
     
          // iterate it
          for (int i = 0; i < orders.length(); i++) {
             // ...
          }

##  Advanced topics

###  Using custom query selector

When using a  custom query to define the selector  , there must be an alias in
the query named ` _identifier ` which will be used as user readable identifier
for the selected records and another one named ` id ` which will be sent to
backend as id of the selected records. Fields for these query columns with the
same names are also required.

##  Limitations

Multi Selectors can only be used as parameters in _Standard Process
Definition_ , they cannot be included in _Standard Windows_ .

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Multi_Selector  "

This page has been accessed 12,527 times. This page was last modified on 30
January 2015, at 10:38. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

