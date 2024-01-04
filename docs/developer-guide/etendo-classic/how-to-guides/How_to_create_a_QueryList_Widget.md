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

  

#  How to create a QueryList Widget

##  Contents

  * 1  Introduction 
  * 2  Developing the widget 
    * 2.1  Create the widget 
    * 2.2  Create the query 
    * 2.3  Create the columns 
  * 3  Adding the widget to your workspace 

  
---  
  
##  Introduction

This HowTo describes how to create a new widget that implements the Query/List
Widget superclass. The generic documentation about what are widgets can be
found  here  .

A related Howto explaining how to embed a widget into a generated Window/Tab
can be found in  this  other document.

  

##  Developing the widget

The new widget like all developments must belong to a module.  Create a new
one  if you still don't have it.

####  Create the widget

All the widget definition is done in the _Widget_ window.

Create a new _widget class_ :

Widget title

     is the title that appear on the widget header. Put here a short sentence that describes the widget. 
Superclass & Widget superclass

     leave the flag unchecked and select the _Query/List_ superclass widget from the drop/down menu. 
Height

     set up any value, the Query/List override this value setting up the height based on the number of rows. 
Enable for all users

     Check it if the widget has to be available to all roles. Otherwise leave unchecked and give access to the desired roles on the _Widget Access_ tab. 

As the widget is implementing a superclass widget some parameters might have
been created to the new widget. On the _Query/List_ case the _Number of Rows_
parameter is created automatically. This sets the number of rows visible on
the grid.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-0.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-1.png){: .legacy-image-style}

Pending goods receipt widget class definition.

####  Create the query

The HQL query is defined on the _Query_ tab. At this moment it is not possible
to validate the _HQL_ from the application so it is recommended to design it
on an external tool. Eclipse has a nice  plugin for it  . All columns on the
select clause must have a unique alias. These aliases are used later to define
the grid columns.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-2.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-3.png){: .legacy-image-style}

Pending goods receipt HQL query definition.

As the screenshot doesn't show the full text of the _HQL_ used in our HowTo
the following shows it in more detail. In query there are a few special things
to notice:

  * Use of named aliases like **orderId** and **organizationName** . Those relate to the columns of the HQL-result to the grid-columns visible for the user which are explained further down in the _Column_ section. 
  * Expressions like **:productname** -> _HQL_ named parameters which relate to defined _Parameters_ of the widget explained in the following. 
  * **@optional_filters@** keyword, which defines the position where the Widget will automatically add extra filters like the standard client & organization filters. 

    
    
     
    SELECT ol.salesOrder.id AS orderId, ol.salesOrder.organization.name AS organizationName,
           ol.salesOrder.orderDate AS dateordered,  ol.salesOrder.scheduledDeliveryDate AS plannedDeliveryDate,
           ol.salesOrder.documentNo AS salesorder, ol.salesOrder.businessPartner.name AS bpartner,
           ol.product.name AS productname, ol.attributeSetValue.description AS attribute,
           ol.uOM.name AS uom, ol.orderedQuantity AS totalqty,    
           (SELECT coalesce(sum(po.quantity),0) 
            FROM ProcurementPOInvoiceMatch po 
            WHERE po.goodsShipmentLine IS NOT NULL AND po.salesOrderLine = ol) AS qtyReceived,
           (SELECT ol.orderedQuantity-coalesce(sum(po2.quantity),0) 
            FROM ProcurementPOInvoiceMatch po2 
            WHERE po2.goodsShipmentLine IS NOT NULL AND po2.salesOrderLine = ol) AS qtyPending
    FROM   OrderLine AS ol 
           LEFT JOIN ol.attributeSetValue 
    WHERE  ol.salesOrder.client.id =:client AND 
           ol.salesOrder.organization.id IN (:organizationList) AND 
           ol.salesOrder.documentStatus='CO' AND 
           ol.salesOrder.salesTransaction=false AND
           ol.orderedQuantity <> (SELECT coalesce(sum(po3.quantity),0) 
                                  FROM ProcurementPOInvoiceMatch po3 
                                  WHERE po3.goodsShipmentLine IS NOT NULL
                                  AND po3.salesOrderLine = ol) AND 
           ol.salesOrder.scheduledDeliveryDate<=now() AND 
           ol.product.name LIKE :productname AND 
           ol.salesOrder.businessPartner.name LIKE :suppliername AND 
           ol.salesOrder.documentNo LIKE :documentno AND 
           ol.salesOrder.organization.name LIKE :organizationName AND 
           @optional_filters@
    ORDER BY ol.salesOrder.scheduledDeliveryDate, ol.salesOrder.documentNo

It is possible to use _named parameters_ on the query. Each _named parameter_
must have a matching _Parameter_ defined on the _Parameter_ tab:

DB Column name

     it must match the name used on the named parameter. 
Fixed & Fixed Value & Evaluate Fixed Value

     when the flag is checked it is mandatory to enter the fixed value. If the _Evaluate Fixed Value_ is checked the value has to be a javascript expression that it is validated on real time. It is recommended to add a filter by client id on all your queries using a named parameter and a fixed value with the following javascript expression: _OB.getContext().getCurrentClient().id_ . If the parameter is not fixed it will be prompted to the user on the _Edit settings_ window. 
Name

     is the label of the field of the parameter on the _Edit Settings_ window. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-4.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-5.png){: .legacy-image-style}

Pending goods receipt parameters list.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-6.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-7.png){: .legacy-image-style}

Pending goods receipt client parameter definition.

####  Create the columns

Once the query is defined and the necessary parameters created is time to
define the columns that will be available on the grid on the _Column_ tab:

Name

     is the label of the column. 
Display expression

     it has to match an alias of the query, it is the column of the query that will be displayed on the grid. 
Reference

     it sets the type of cell on the grid. 
Include in

     sets where is included the column. _Widget view_ : included in all cases, _Maximized view_ : not shown on the widget view and _Exported File_ only included on the exported file. 
Sequence number

     sets the order of the columns. 
Width

     sets the width of the column on the grid in percentage. 
Has link & Link Expression & Tab

     it is possible to set up links on the cells to tabs of the application. The _Link Expression_ has to be an alias of the query that returns a record id of the selected tab. 
Summarize Type

     numeric columns can be summarized on the summary row. Available options are _sum_ , _average_ and _count_ . It is not supported using summaries in columns that are defined using subqueries or using a summary function. For instance, if the _qtyonhand_ column is defined in the query like this _sum(ps.quantityOnHand) as qtyonhand_ , it will not be supported using it with a not empty summarize type. If you set the summarize type of a column that is defined using an alias, you must also set the _Where Clause Left Part_ field. 
Can be filtered & Where Clause Left Part

     configures the ability to filter the grid by the column on the maximized view using the filter row of the grid. It is mandatory to define the left part of the where clause. This is usually the expression of the select clause identified by the alias set on the _Display Expression_ field. It is also mandatory to define where in the HQL has to be included the where clause. There are 2 possibilities to achieve this: including the _Display Expression_ value enclosed in "@" symbols in the where clause of the HQL or including the _@optional_filters@_ string. 
Clientclass

     (Since 3.0MP20. Issue  22902  ) In the same way that in the  from/grid view  , a custom canvas item can be added within the Quert List grid. 
     Example 1: To add a % sign in an existing field: 

     Set as "Clientclass" the following value "OBAddPercentageSign" 
     Example 2: To add a 'Print' link button in a new column 

     Create the new column 
     Name: the column header title 
     Display Column Alias: it doesn't mind the value, but ensure that is not used in any other column 
     Reference: it doesn't mind the value, but 'String' works ok 
     Width: the desired column width. "15" should be enough 
     Has Link: checked 
     Link Column Alias: point to the hql result matching the id of the record you want to print 
     Tab: point to the tab which belongs the record you want to print 
     Clientcanvas: set the following value "OBQLCanvasItem_Print" 
    
     Note that this 'Print' button works for PDF documents (like, for example, 'Sales Invoice' print behavior). For in-screen cards (like, for example, 'Business Partners' print behavior), the "Clientcanvas" value should be "OBQLCanvasItem_Print {"isDirectPDF": false, "title": "Print BP"}" 

In the example of the image. The display expression alias is _salesorder_ . In
the HQL this alias is defined like: _ol.salesOrder.documentNo as salesorder_ .
So in the _Where Clause Left Part_ is set _ol.salesOrder.documentNo_ . In the
HQL as we want to be able to filter by all the columns and all the where
clauses have to be set on the same where statement it is added _AND
@optional_filters@_ . For this column we could have added as well the
following code: _AND @salesorder@_ .

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-8.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-9.png){: .legacy-image-style}

Pending goods receipt column definition.

##  Adding the widget to your workspace

Once the widget is done if you have access to it you are able to add it to
your workspace. It is not needed to compile anything.

On the _Add widget_ menu select your new widget. If all the parameters have a
default value or are fixed you will see the widget added on the workspace.
Otherwise you will be prompted to fill the parameters.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-10.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-11.png){: .legacy-image-style}

Pending goods receipt setting parameters.

And the final result:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_QueryList_Widget-12.png){: .legacy-image-style}

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_QueryList_Widget  "

This page has been accessed 17,238 times. This page was last modified on 11
March 2015, at 17:21. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

