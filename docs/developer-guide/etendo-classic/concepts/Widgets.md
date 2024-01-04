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

  

#  Widgets

![](/assets/developer-guide/etendo-classic/concepts/Widgets-0.png){: .legacy-image-style} |  This
document is still a work in progress. It may contain inaccuracies or errors.  
---|---  
  
##  Contents

  * 1  Introduction 
  * 2  Widget class & Widget Instance 
  * 3  Defining a new widget class 
    * 3.1  Extending a existing widget class 
    * 3.2  Defining widget parameters 
  * 4  Available Widget Superclasses 
  * 5  Defining a widget for use in a generated window 
    * 5.1  Use of current record in parameters 

  
---  
  
##  Introduction

In Openbravo 3 Widgets are UI elements which can be either placed in a Users'
Workspace tab or be part of a generated window. They can be used to display a
wide range of different information ranging from static content, over dynamic
database data in list form, custom html content, or complete external URL's.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Placing
Widget in a generated window is only available from version 3.0MP2 or later  
---|---  
  
The following images show two example widgets which are provided by the Widget
Collection module provided with the Openbravo 3 distribution.

The first one shows a list of invoices ready to be collected with live data
from the Openbravo database. The second example shows an interactive motion
chart.

![](/assets/developer-guide/etendo-classic/concepts/Widgets-2.png){: .legacy-image-style}
![](/assets/developer-guide/etendo-classic/concepts/Widgets-3.png){: .legacy-image-style}

The rest of this article explains how to define such a widget with its
parameters, the different available 'types' of widget and the differences in
widget definitions if those are to be placed in a generated window.

##  Widget class & Widget Instance

##  Defining a new widget class

###  Extending a existing widget class

###  Defining widget parameters

##  Available Widget Superclasses

##  Defining a widget for use in a generated window

If a widget is planned to be embed into a generated Window/Tab as explained in
this HowTo  then a few differences/restrictions must be observed.

  * User visible differences: Widgets embedded in a Tab do not have a titlebar/menu. This means that widgets embedded in a Tab do **not** offer the following customization/options: 
    * Edit of parameters 
    * Removing/moving/Maximizing the widget 
    * Use of custom menu items (i.e. Export as CSV) 
  * Differences in definition 
    * No _Widget Instance_ , all parameters must be defined on the Widget directly 
    * Parameters can use values of the currently displayed record 

###  Use of current record in parameters

When a widget is displayed inside a generated Window/Tab then it is possible
to define a parameters which will contain the field values of the currently
displayed record.

To do this the parameter needs to be declared as described above with the
following settings:

  * Fixed: not marked 
  * Default Value: **${formValues.name}**

The **name** in the expression for the Default Value refers to the _Name_
field of the current record. The name to be used for a field in this
expression is the _property_ name of the column, so the same which is also
used in an HQL query.

If the property is an Entity (i.e. Product) **${formValues.product}** will
contain the id (UUID) of the Entity

At runtime this parameter will automatically contain the fields' value as the
parameter value.

Note: If there is no current value (i.e. the form displayed in _New_ mode)
then the expression string is send as is to the widget. The widget
implementation is expected to handle such a case.

Retrieved from "  http://wiki.openbravo.com/wiki/Widgets  "

This page has been accessed 15,790 times. This page was last modified on 23
November 2011, at 17:41. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Categories  :  WorkInProgress  |  Concepts

**

