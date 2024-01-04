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

  

#  How to add a rich text field and column

##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  Adding a column 
  * 4  Create a field - set col and rowspan 
  * 5  The result 

  
---  
  
##  Introduction

This howto explains how to add a rich text field and column to the Openbravo
system.

The steps to get a rich text field in your window consists of 2 steps: 1) add
a column to a table, and 2) add a field to a tab.

You can also create a new table and a new window/tab ofcourse. These 2 steps
are described in detail in the following howtos:

  * Add a new column to a table in the system 
  * Define and add a new field to a tab 

This howto will only focus on the specific part of a rich text field.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Rich text fields are available in MP20 and later MPs.  
---|---  
  
##  Example Module

This howto is supported by an example module which shows example of the code
shown and discussed in this howto.

The example module adds a rich text field to the sales order header window.
Please use an example module version of a release/implementation date of 23rd
of January or later.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
example module also contains implementations of other howtos.  
---|---  
  
##  Adding a column

First, you have to  add a new column to the existing table  .

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  As
rich text is stored as HTML inside the database, the varchar column type
should be used. What is more, the developer needs to keep in mind that 100
characters of rich text requires more that 100 chars of storage inside the
database due to html markup. Usually, a factor of 2 will suffice, for example,
if one wants to allow the user to enter 1000 characters of rich formatted
text, the database column should have a type of varchar(2000).  
---|---  
  
When introducing the new column to the application dictionary, the correct
reference must be selected, i.e. the new _Rich Text_ reference:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_add_a_rich_text_field_and_column-3.png){: .legacy-image-style}

##  Create a field - set col and rowspan

Then  create a field  within the tab/window. For a rich text field you can
also set the col and rowspan (these are only shown when the corresponding
column is defined as rich text):

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_add_a_rich_text_field_and_column-4.png){: .legacy-image-style}

##  The result

The result is visualized as a rich text editor in form view:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_add_a_rich_text_field_and_column-5.png){: .legacy-image-style}

  

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  For
now rich text fields can not be edited in grid mode (a hoover shows the
content). They are always displayed as read-only fields.  
---|---  
  
Retrieved from "
http://wiki.openbravo.com/wiki/How_to_add_a_rich_text_field_and_column  "

This page has been accessed 9,020 times. This page was last modified on 3
April 2013, at 14:06. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

