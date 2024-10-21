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

  

#  How to Create a Tree Selector

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **Openbravo PR14Q2**  
---|---  
  
##  Contents

  * 1  Introduction 
  * 2  Defining a Tree Selector 
    * 2.1  Define a Reference 
    * 2.2  Define the Tree Selector 
    * 2.3  Define the Tree Selector Fields 
    * 2.4  Set the Value and Display Fields of the Tree Selector 

  
---  
  
##  Introduction

The Tree Selector described in this manual is a variant of the  Openbravo
Selector  . It can only be applied on tables with  trees defined  .

Both the implementation of the tree selector and its use is similar to the
standard selector. The main difference is that instead of using a grid for the
form item drop down and the popup, the Tree Selector uses a tree grid:

Drop down tree:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Tree_Selector-1.png){: .legacy-image-style}

Popup tree:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Tree_Selector-2.png){: .legacy-image-style}

##  Defining a Tree Selector

Defining a tree selector is very similar to defining a standard selector.

###  Define a Reference

Open the Reference window and create a new record in the header tab. This are
the most relevant fields:

  * Name, Description and Help should be set to a value specific for the reference you are creating 
  * Base Reference must be set to false 
  * Parent Reference must be set to Tree Reference 
  * Model, WAD and Runtime UI Implementation can be left empty most of the time if the reference is not a base reference. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Tree_Selector-3.png){: .legacy-image-style}

###  Define the Tree Selector

Create a new record in the Tree Reference tab.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Tree_Selector-4.png){: .legacy-image-style}

  * Table: Tree Table this selector points to. 
  * Table Tree Category: Table Tree Category that will be used to represent hierarchically the data of the selected table. 
  * Column: the column in the referenced table to which the foreign key column points. If nothing is set here (the default) then the primary key column is used. 
  * Value Field: this tree selector field is set as the value and stored in the database as the foreign key field. 
  * Display Field: this selector field is displayed in the drop-down of the suggestion box. 
  * HQL Where Clause: this where clause is used to filter the data read from the database. 
  * HQL Where Clause for Root Nodes: this where clause is used to specify what are the root nodes for this tree. If it is not set, then the root nodes will be those who have parentId = null or parentId = '0'. 

At this point no Tree Selector Fields have been defined yet, so the Value
Field and Display Field are empty.

###  Define the Tree Selector Fields

The next step is to define the Tree Selector Fields. A selector field can have
several purposes:

  * Be used as Value Field 
  * Be used as Display Field 
  * Be shown in the drop down tree 
  * Be shown in the popup tree. 

A selector must have at least two fields:

  * One field will be used as Value Field 
  * The other field will be used as Display Field and shown in the drop down tree and popup tree. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Tree_Selector-5.png){: .legacy-image-style}

  * Name: Name of the field. It will be used in the title of the column in the popup. 
  * Property: is a column/property from the table selected in the Tree Reference tab. 
  * Central Maintenance: if checked then the name, description and help/comment are copied/used from the column. 
  * Show in Picklist: if checked this field will be visible in the drop down tree. 
  * Search in Suggestion Box: if checked, this field will be used to filter the results when text is entered in the tree form item. 
  * Show in Grid: if checked this field will be visible in the popup tree. 
  * Record Sort No: Sequence number of the field. It is used to establish the field order in the drop down tree and the popup tree. 
  * Filter: If set, this field will be filterable in the popup 
  * Sort: If set, this field will be sortable in the popup 

###  Set the Value and Display Fields of the Tree Selector

Once the Tree Selector Fields have been defined, the Value Field and Display
Field fields of the Tree Reference tab can be set.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Tree_Selector-6.png){: .legacy-image-style}

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_Create_a_Tree_Selector
"

This page has been accessed 8,453 times. This page was last modified on 7
March 2014, at 09:21. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

