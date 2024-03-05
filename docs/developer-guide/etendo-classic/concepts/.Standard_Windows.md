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

  

#  Standard Windows

##  Contents

  * 1  Introduction 
  * 2  Structure: Windows, tabs and fields 
  * 3  Windows 
    * 3.1  Menu 
  * 4  Tabs 
    * 4.1  Tabs hierarchy 
    * 4.2  Tab common elements 
      * 4.2.1  Locking mechanism 
        * 4.2.1.1  Transactional Windows 
        * 4.2.1.2  High Volume Tables 
        * 4.2.1.3  Filter Clause in Tab 
  * 5  Fields 
  * 6  Classic Window Visualization 

  
---  
  
##  Introduction

_Standard Windows_ are the windows completely defined in Application
Dictionary. They allow to view and edit records in tables.

After defining (or modifying) a standard window, the system must be rebuilt (
_ ant smartbuild  _ ). During this process _WAD_ generates automatically the
Java, XSQL, HTML and XML code for that window and it is compiled. This means
that the complete definition for standard windows is within Application
Dictionary without any need of manual developments. This has a number of
benefits:

  * No need to write manual code. This reduces the possibility of introducing bugs. 
  * Faster development. As a window creation consists only in defining it in Application Dictionary, it is faster that doing it manually. 
  * Automatic inclusion of new features and bug fixes. Whenever _WAD_ fixes a bug or adds a new feature, this is automatically propagated to all standard windows when the system is rebuilt without needing to re-code or re-define anything. 

Because of all this, it is a best practice to use standard windows, if
possible, rather than manual ones.

##  Structure: Windows, tabs and fields

The structure for standard windows consists in _Windows_ , _Tabs_ and _Fields_
.

  * _ Windows  _ : Windows are holders for tabs. Their main purpose is to group a set of related tabs. They can be added to the application's menu. 
  * _ Tabs  _ : Tabs are placed inside windows and can be ordered hierarchically. Each tab is linked to a unique  Application Dictionary Table  and contains a number of fields. 
  * _ Fields  _ : Fields are contained within tabs. Each field is associated to a  Column  in the same table than its tab. 

  

![](/assets/developer-guide/etendo-classic/concepts/Standard_Windows-0.png){: .legacy-image-style}

  
The following sections explain how _Windows_ , _Tabs_ and _Fields_ are
defined. They are managed from **Application Dictionary || Windows, Tabs, and
Fields** window.

##  Windows

A complete description for all fields involved in the definition of a window
can be found in the  Database Model  document.

Windows are generated automatically by WAD from their definition in
Application Dictionary, all windows have a common  layout  .

###  Menu

Windows can be added to  Application Menu  .

##  Tabs

Tabs are included within windows. Each tab is limited to a single Application
Dictionary table.

A complete description for all fields involved in the definition of a window
can be found in the  Database Model  document. The following subsections
detail some important topics to be taken into account when creating a tab.

###  Tabs hierarchy

Tabs are shown hierarchically, they are defined in a tree way. This means that
a tab can have subtabs (it is the parent tab for them), consequently a tab can
also be a child for another one and it is possible to have several tabs at the
same level.

This hierarchy is specified using two fields in the tab:

  * Tab Level  : Indicates the level in the hierarchy, being 0 the top level, 1 child tabs for ones in 0, etc. Usually there is a single tab at 0 level and the rest of tabs in the window are subtabs for this one. 
  * Sequence Number  : It is a number that defines the order tabs are displayed. They are sorted ascendantly, so lower ones and in the left side and higher ones in the right. It is a good idea not to use consecutive numbers in order to allow new tabs inclusions between existent ones. 

The conjunction of these two values gives the position and hierarchy for each
tab. Let's see through an example how the following tab structure could be
defined:

    
    
     A
     |-A1
     |  |-A11
     |-A2
     |  |-A21
     |  |-A22
     |     |-A221
     |-A3
    

Tab  |  Sequence number  |  Tab level  
---|---|---  
A  |  10  |  0  
A1  |  20  |  1  
A11  |  30  |  2  
A2  |  40  |  1  
A21  |  50  |  2  
A22  |  60  |  2  
A221  |  70  |  3  
A3  |  80  |  1  
  
When creating subtabs, it is necessary to set which column in the parent
column is going to be the master for the subtab. In order to show in the
subtabs only the records that are linked to the current record in the parent
one.

For example let's suppose tab A is a tab for _C_Invoice_ table and tab A1 is
for _C_InvoiceLine_ , in this case _C_Invoice.C_Invoice_ID_ in tab A must be
the master column for tab A1, showing in A1 only the records linking to the
selected record in A.

There are three possible ways of setting which is the master column in the
parent tab:

  1. Using the _ AD_Column.IsParent  _ check in the table used in the subtab. When a table in a tab contains columns checked as _Link to Parent Column_ , it is looked in the parent tab a column with the same name and if found that one will be the master. 
  2. By name. In case the table in subtab has a column with the same name as the parent's primary key one, the link will be generated using them. 
  3. Using _ AD_Tab.WhereClause  _ . In case it is not possible to use #1 or #2, the relation must be set in the child tab's _Where Clause_ field. For more info about this clause, read the document about  Dynamic Expressions  . In these cases, starting from **3.0MP30** , it is possible to mark the _Disable Parent Key Property_ flag, doing so only where clause will be used to create the relationship not adding any other criteria. 

###  Tab common elements

####  Locking mechanism

All WAD generated tabs implement a simple  Optimistic locking mechanism  .

When a record is loaded in edition mode, its _updated_ timestamp is stored. If
the record is modified and saved, this stored timestamp is compared with the
current one in database for that record. In case they are different, that
record has been modified by another user or process and the application does
not allow to save the current modifications. Because otherwise, the
modifications done from the record was loaded till the current time would be
overwritten.

  

![](/assets/developer-guide/etendo-classic/concepts/Standard_Windows-1.png){: .legacy-image-style}

  

#####  Transactional Windows

Windows for documents can be set as _Transactional_ . Documents have a status,
which initially is _Draft_ .

When a transactional window is accessed, by default it appears filtered. This
is visualized using a message and a small funnel icon on the top right

  

![](/assets/developer-guide/etendo-classic/concepts/Standard_Windows-2.png){: .legacy-image-style}

  
The applied filter is all the documents with status Draft or which date is in
the defined _Transaction Range_ . To clear the filter click the funnel icon.

To define a window as transactional go to **Application Dictionary || Windows,
Tabs, and Fields || Window** tab and select the _ Window Type  _ as
_Transaction_ .

To define the _Transaction Range_ go to **General Setup || Application ||
Session Preferences** and define in the _Transaction Range_ the maximum number
of days that processed documents will be shown in.

#####  High Volume Tables

When a table is set defined as _ High Volume  _ (in **Application Dictionary
|| Tables and Columns || Table** tab) and the tab that displays it is set to
by default be shown in edition mode ( _ Default Edit Mode  _ in **Application
Dictionary || Windows, Tabs, and Fields || Window >> Tab ** tab), when the tab
is accessed a filter is shown.

#####  Filter Clause in Tab

In **Application Dictionary || Windows, Tabs, and Fields || Window >> Tab **
tab there is a _ Filter Clause  _ field,  HQL Filter Clause  starting from
Openbravo 3. This field allows HQL where clauses to be used as default filter
for the tab. When the tab is accessed this filter is applied, to remove it
just click on the funnel filter icon.

Note that this field is different than the _ HQL Where Clause  _ which also
accepts where clauses, but this clause is permanent and cannot be removed by
user.

##  Fields

Fields are contained in tabs, each field has a column (from the same table as
the tab's one) associated. It displays and allows to edit the column's value.

The way a field is displayed within the tab is determined by the  reference
its associated column has.

Some (the definition for all fields involving a field definition are listed
here  ) of the things to take into account when configuring a field are:

  * Read Only Logic  which allows to determine if field is read only (applies only when field is read-write).The Read Only indicates that this field may only be Read. It may not be updated. Note that it is defined at Column level in the Application Dictionary. It is a  Dynamic Expression  . 
  * Display logic  which allows to show or hide the field depending on other fields' values. It is a  Dynamic Expression  . 
    * From 16Q1, Display logic is taken into account in grid view as read only logic, being solely applied when a record is edited in grid view. 
  * Central Maintenance  how it works it is explained in the docuement about  Elements and Synchronize Terminology  . 
  * Callout  , although it is not defined in the fields, it affects them directly becuse they are raised when fields' values are modified. 
  * Field group  , fields can be assigned to a field group, when a group of fields has a field group a separator is showed in the tab. Field Groups are defined in **Application Dictionary || Setup || Field Category** tab. 

##  Classic Window Visualization

As a default Openbravo will visualize windows using rich internet technology.
There are however some situations in which Openbravo will use classic servlet
based technology (i.e. classic mode):

  * in case of a specific preference setting, see this  howto  for more information 
  * when the window has a tab with one of the following settings: 
    * a manual form 
    * a SQL filterClause but the HQL filter clause field is empty 
    * a SQL order by clause but the HQL order by clause is empty 
    * a SQL where clause set but the HQL where clause is empty 

In this second case, you will notice the following warning message when
compiling: _INFO org.openbravo.wad.Wad - Window: WindowName is needed in
classic 2.50 mode._

Retrieved from "  http://wiki.openbravo.com/wiki/Standard_Windows  "

This page has been accessed 14,443 times. This page was last modified on 30
November 2015, at 11:30. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

