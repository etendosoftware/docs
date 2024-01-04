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

  

#  How to create a Computed Column

##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  Defining a computed column 
  * 4  Use case: show totals on a header 
  * 5  Performance implications 
    * 5.1  Filtering and sorting 
    * 5.2  Lazy evaluation 
      * 5.2.1  Limitations 

  
---  
  
##  Introduction

In MP13 the new concept: **computed column** , was introduced. A computed
column is a column of a table which is computed using a sql expression and
which does not exist explicitly in the database schema.

Computed columns have these characteristics:

  * computed when a record is read from the database 
  * not persisted, there is no real column in the database schema for a computed column 
  * is computed using a sql expression which can use columns from the application dictionary table definition in which the column is defined 
  * can be used in the definition of a field (in the same way as a 'normal' column), is sortable and filterable but not editable 

##  Example Module

This howto is supported by an example module which shows example of the code
shown and discussed in this howto.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), for more information see the  Examples Client
Application  project page.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
example module also contains implementations of other howtos.  
---|---  
  
##  Defining a computed column

Defining a computed column is quite easy. Goto the 'Tables and Columns' window
to the table in which you want to add the computed column.

Then in the column child tab create a new column and set the sqllogic field.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Computed_Column-1.png){: .legacy-image-style}

  
The sqlLogic field must be a sql expression:

  * If it is a select sql expression then the tables in the from clause all need to use an alias. 
  * you can refer to other columns of the table using their non-aliased name 

This is an example of the total line quantity column shown above:

    
    
    (SELECT sum(ol.qtyOrdered) FROM c_orderline ol WHERE ol.c_order_id=c_order_id)

What you can see is that the from clause uses an aliased table, the c_order_id
at the end is the non-aliased column of the main table.

**Note:**

  * a computed column can be used in the definition of a field for an Openbravo column, just like every other column. 
  * a computed column that uses a String reference should have a length greater than zero. Because this is the number of characters which are going to be displayed in form view. 
  * the field is always read-only, it is recomputed/set automatically when updating or inserting a record. 
  * filtering and sorting on computed columns/fields is possible. Note: see the performance section at the end of this wiki document. 

##  Use case: show totals on a header

In the 'Defining a computed column' section an example sql expression was
shown. The above example computes the sum of the quantities of a line. You can
add a computed column as a field to a tab/window:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Computed_Column-2.png){: .legacy-image-style}

  
and display it in the grid:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Computed_Column-3.png){: .legacy-image-style}

  
or the form:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Computed_Column-4.png){: .legacy-image-style}

##  Performance implications

###  Filtering and sorting

When computed columns are used to filter or sort the grid, their value need to
be computed for all existing rows before any pagination limit can be applied,
this can have a very important impact in terms of performance.

In general, when defining computed columns, they should be made  not
filterable nor sortable  . The only exception to this rule would be when it is
guaranteed the number of records in the table they are created for is going to
be always reduced or it will always be displayed as a subtab where the number
of rows per parent record cannot be big.

###  Lazy evaluation

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
_Lazy evaluation_ of computed columns is introduced starting in **3.0MP27**  
---|---  
  
Computed columns are lazily evaluated. This means their query is not executed
when the entity they are defined in is retrieved but when one of them is
accessed.

For example, _Delivery Status_ is a computed column of _Order_ entity:

` `

    
    
       // load one order
       OBCriteria<Order> qOrder = OBDal.getInstance().createCriteria(Order.class);
       qOrder.setMaxResults(1);
       Order order = qOrder.list().get(0);
    

The code above loads an order, at this stage _Delivery Status_ is not already
computed meaning the SQL has not been executed in database.

If afterwards we have this code:

` `

    
    
      // load computed columns
      System.out.println(order.getDeliveryStatus());
    

is at this point when the computed column query is executed in database and
_Delivery Status_ property takes value.

Note that in case there are many computed columns in the same entity, they are
evaluated all together when the first one is calculated.

####  Limitations

In order to make computed columns lazy, they are mapped in their entity as a `
many-to-one ` property (named ` _computedColumns ` ) linked to a virtual
entity, is this virtual entity where the actual computed columns are located
as hibernate formula properties.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Computed_Column-6.png){: .legacy-image-style}

This extra complexity is transparent when working with generated DAL Java
classes, as seen before, ` order.getDeliveryStatus() ` populates the value of
the computed column, though behind the scenes it is retrieving it from the
virtual entity.

But this model imposes also some limitations to be taken into account when
manipulating computed columns in filters or sorting.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Note that when using computed columns in HQL to do filtering or sorting, they
are evaluated. This needs to be done carefully (or even avoided if possible)
because it might have  performance implications  .  
---|---  
  
When working with _HQL_ (i.e. ` OBQuery ` ) computed columns cannot be
directly accessed as they are not properties of the entity.

So this valid query in versions prior to _MP27_ :

    
    
     
    -- NOTE: this code is not valid after 3.0MP027
    FROM ORDER o WHERE o.deliveryStatus = 100

doesn't work anymore starting from _MP27_ , its equivalent would be:

    
    
     
    FROM ORDER o WHERE o._computedColumns.deliveryStatus = 100

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Computed_Column-8.png){: .legacy-image-style} |  Starting from **3.0MP27** ,
computed columns cannot be used anymore in ` OBCriteria ` , if needed `
OBQuery ` should be used instead.  
---|---  
  
Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Computed_Column  "

This page has been accessed 24,989 times. This page was last modified on 10
January 2019, at 10:06. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

