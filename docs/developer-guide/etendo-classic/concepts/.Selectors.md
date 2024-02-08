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

  

#  Selectors

##  Contents

  * 1  Introduction 
  * 2  Selector Example Module 
  * 3  Selector Concept 
  * 4  Defining a Selector 
    * 4.1  Step 1: Define a Reference 
    * 4.2  Step 2: Define the Selector 
    * 4.3  Step 3: Defining Selector Fields 
    * 4.4  Property paths, showing linked information 
    * 4.5  Table and Datasource 
    * 4.6  Translated information 
    * 4.7  Selector Examples 
  * 5  Using a Selector 
  * 6  Changing a selector at runtime 
  * 7  Defining Out Fields 
    * 7.1  Using Out Fields in manual code (advanced) 
      * 7.1.1  Example of function 
  * 8  Providing a new Selector Template (advanced) 
  * 9  Customizing the look and feel of the selector 
  * 10  Troubleshooting 
    * 10.1  The suggestion box does not filter 
    * 10.2  The suggestion box is always empty 
  * 11  Advanced Topics 
    * 11.1  HQL Transformers 
    * 11.2  Using foreign keys in HQL Custom queries 

  
---  
  
##  Introduction

The Selector described in this manual combines a suggestion box with a popup
window with filter and sorting capabilities. This selector has a number of
important features:

  * it can be defined completely without manual coding. 
  * the selector definition (columns, search criteria, where clause) can be changed at runtime without re-compiling or re-starting the system. 
  * the selector makes it very easy to show linked information of a selected entity or search, sort and filter on linked information. 
  * the selector suggestion box as well as the popup grid support paging with lookahead, this makes them also suitable for large datasets. 

This manual is targeted at consultants who want to define selectors in the
Openbravo system.

##  Selector Example Module

The manual refers to and uses screenshots from the  Selector Example  module.
To follow this manual it can make sense to install this module from the
central repository.

After installing this module and rebuilding you can try out the selector
functionality. Change Role to Openbravo Admin (or another user role having
access to the example window). You can find the selector example in 'General
Setup > Examples > SelectorExample'. Click on this menu option. A grid view
opens, click new to open the edit form.

The form shows three selector fields: 2 business partner fields and one
product field. The product field gets enabled after you have entered a value
in the second business partner field.

![](/assets/developer-guide/etendo-classic/concepts/Selectors-0.png){: .legacy-image-style}

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-1.png){: .legacy-image-style}

A suggestion box is dropped-down when you start typing in the fields. You can
also click on the magnifier icon to show a popup window with several filter
and sorting possibilities.

##  Selector Concept

A selector is defined within the  Application Dictionary  of Openbravo. A
selector is used for representing foreign key references in the Openbravo user
interface. A selector is defined as part of a  Reference  (a domain type)
definition within Openbravo.

A selector consists of three parts:

  * the reference definition 
  * the selector header defining which table to select from and the where clause to use 
  * the selector fields which define which columns are searched and what columns are shown in the popup window. 

##  Defining a Selector

To define a new selector go to the Application Dictionary > Reference window.
Defining the selector is a three-step procedure:

  * create a new reference 
  * create a selector header 
  * create zero or more selector fields 

This manual guides you through all three steps.

###  Step 1: Define a Reference

The reference is used in the column definition. The definition is shown below
in the screenshot.

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-2.png){: .legacy-image-style}

  
A description of the fields:

  * Name, Description and Help should be set to a value specific for the reference you are creating 
  * Base Reference **must** be set to false 
  * Parent Reference **must** be set to OBUISEL_Selector_Reference 
  * Model, WAD and Runtime UI Implementation can be left empty most of the time, for more information on the meaning of these fields see  this  manual 

###  Step 2: Define the Selector

After defining the reference the selector information can be entered. This is
done in the reference window also. Make sure that the reference window shows
the reference you have created in step 1 then click on the _Defined Selector_
in the top right of the window. Next press the new button.

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-3.png){: .legacy-image-style}

  
A description of the fields:

  * Name and Help/Comment: set these to values describing the 
  * Description: this is used as the title of the popup window 
  * Template: there should normally be only one option: Selector Template. Multiple options are possible if additional templates have been installed for selectors. 
  * Table: normally a selector selects from a table, select the relevant table from the list 
  * Column: the column in the referenced table to which the foreign key column points. If nothing is set here (the default) then the primary key column is used. 
  * Datasource: can be set when no table is selected. A data source can be used to provide data which is not read from the database but is for example computed at runtime. For more information on Datasources see the the  Datasource  Developers Manual. 
  * HQL Where Clause: this where clause is used to filter the data read from the database. 

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |
Currently it is not possible to use session variables in the where clause!  
---|---  
  
![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  When
using properties of the entity in the whereclause always the prefix 'e.' has
to be used, for example 'e.seqno'  
---|---  
  
  * Display Field: this selector field is displayed in the drop-down of the suggestion box. Some specific aspects: 
    * an empty value (the default) means that the identifier columns of the referenced table are used to display information in the suggestion box. This default is often a good choice. 
    * initially when creating a selector it is not possible to select a field here as no selector fields have been defined yet (see next section). After defining one or more selector fields it is possible to choose one of these fields here. 
  * Value Field: this selector field is set as the value and stored in the database as the foreign key field. Some specific aspects: 
    * an empty value (the default) means that the primary key column of the referenced table is used. This is by far the most common case and therefore a good choice for most if not practically all cases. 
    * initially when creating a selector it is not possible to select a field here as no selector fields have been defined yet (see next section). After defining one or more selector fields it is possible to choose one of these fields here. 
  * Sort By Field: this selector field is used to sort the records in the drop-down of the suggestion box. Some specific aspects: 
    * an empty value (the default) means that the records are ordered by the values of the display field. And in case the display field is neither defined, the identifier columns of the referenced table are used to sort information in the suggestion box. This default is often a good choice. 
    * initially when creating a selector it is not possible to select a field here as no selector fields have been defined yet (see next section). After defining one or more selector fields it is possible to choose one of these fields here. 

###  Step 3: Defining Selector Fields

After defining the selector header the next step is to define the selector
field. A selector field is used for the following things:

  * to define a column in the popup search grid 
  * to define a column of the target table which is searched for the suggestion box 
  * to define the display field of the suggestion box (what gets displayed when a user types in values in the field) 
  * to define the value field, the column which is used to set the value in the foreign key column 
  * to define the sort by field of the suggestion box 

A selector can have zero or more selector fields. It is perfectly fine to
define a selector without selector fields. The system will use the defaults
which is show the identifier in the suggestion box and use the primary key of
the referenced table as the value. The suggestion box is shown in the field
but no popup window is shown. So this is a light-weight selector definition.

To define a selector field click on the 'Defined Selector Field' link shown in
the top-right of the Defined Selector tab.

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-6.png){: .legacy-image-style}

  
The description of the fields of the Defined Selector Field:

  * name: use a descriptive name here 
  * property: is a column/property from the table set in the selector header. This field is implemented using the selector itself. This makes it easy for a consultant to select the correct model property. It is possible to enter a so-called property path. For the business partner table it is for example possible to specify bankAccount.bank.name which will show the name of the bank of the bank account of the business partner. See the next section on Property Paths for more information. 

![](/assets/developer-guide/etendo-classic/concepts/Selectors-7.png){: .legacy-image-style}

  * Description and Help/Comment: set these to meaningful values for your specific case (see also the 'Central Maintenance' field below). The description field is for future usage. 
  * Show in grid: if checked then the field is visible in the popup grid. If not checked then the field is not shown in the popup grid. It can still be used as the value field, display field, sort by field or as a search field for the suggestion box. 
  * Sorting of columns in a grid: the order in which the columns are shown in the popup grid. Only relevant if 'Show in grid' is checked. 
  * Sortable: determines if the user can sort on this column in the popup grid. Only relevant if 'Show in grid' is checked. 
  * Filterable: determines if the user filter on this column in the popup grid. Only relevant if 'Show in grid' is checked. 
  * Central Maintenance: if checked then the name, description and help/comment are copied/used from the column. This is handled by the  Synchronize Terminology  process. 
  * Search in suggestion box: as a default, the suggestion box will use the string entered by the user to search in the display field (set in the selector header) or identifier. You can select additional fields to search in by setting this field (Search in suggestion box) to yes/checking it. To make search field invisible just uncheck the field 'show in grid', then the field is only used to search and not displayed in the popup grid. 

Note:

  * If none of the selector fields have 'show in grid' checked/set to yes, then no popup grid is available and the magnifier icon is not shown, the user can only select data through the suggestion box. 
  * when setting a column to filterable or sortable it is possible that a decreasing performance is encountered with a table with many thousands of records. If this happens contact the database administrator to optimize the table by adding indexes. Note that these new indexes have to exported to the Openbravo metadata using standard export.database procedures. 

###  Property paths, showing linked information

The selector has a very powerful feature that makes it easy to show linked
information in the suggestion box and popup windows.

To give an example of linked information. For a business partner selector it
is quite easy to show the identifier of the business partner category. This
linked information can take multiple 'steps', so it is possible to show the
name of the bank of the bankaccount of the business partner. These two
examples are entered like this in the property field of the Defined Selector
Field:

  * businessPartnerCategory._identifier 
  * bankAccount.bank.name 

By using the dot (.) the path takes the next step in the model. The suggestion
box in the Defined Selector Field window gives support in entering the correct
path.

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-8.png){: .legacy-image-style}

  
This is then displayed like this in the popup window (see the bank and the
business partner category columns):

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-9.png){: .legacy-image-style}

  
The fields which use such a property path can be used as the display field,
sort by field or value field and can be used to filter and sort on in the
popup grid. So they are treated as standard normal properties.

###  Table and Datasource

A selector can retrieve its content from a table or from a Datasource. When in
the selector definition a table is defined then on the server Openbravo will
create a datasource for this table. So internally for Openbravo there is no
real difference between a table or datasource for the selector.

There are a number of use-cases for which using a datasource makes sense:

  * when the data for a selector requires preprocessing after retrieval from the database. 
  * when the data in a selector is not even read from the database but computed in memory by the system. 

A datasource is implemented by a developer and then defined in the Application
Dictionary. After this it can be used by consultants to define selectors.

For more information on how to implement a datasource see its  Datasources
page.

###  Translated information

The Selector and Selector Fields also allow you to specify translated versions
of names and titles shown in the user interface. To use translated names and
titles go to the 'Defined Selector Translation' and 'Defined Selector Field
Translation' tabs. These tabs are available in the top of the window when
editing a Selector or Selector Field.

###  Selector Examples

The Selector Example module installs a number of different selectors. These
selectors can be studied to see how they are defined and what the result in
the user interfac is. When you filter the reference grid on the word
'Selector' they will show up:

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-10.png){: .legacy-image-style}

##  Using a Selector

The next step is make use of the selector in the data model. The selector is
the same as any other Reference in the Openbravo system. The Reference is used
in the definition of a Column. To use the defined selector and set it in a
column, go to Application Dictionary > Tables and Columns. Then select the
table and the column you want to set the reference for.

Then in the reference field choose OBUISEL_Selector Reference. Then in the
next combo box 'Reference Search Key' select the specific selector. In the
screenshot below a Business Partner Selector is chosen.

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-11.png){: .legacy-image-style}

  
The column can be used to define a field in the Openbravo window in a standard
way. So in the Openbravo Window/Tab/Field definition there is no special
setting or handling required for the selector.

After setting the reference in the column and using it in a specific window
you need to restart Openbravo to see it in action.

##  Changing a selector at runtime

The selector definition itself can be changed at runtime without re-compiling
the system. There are no real limits to what part of the selector definition
which can be changed at runtime, a non-excluding list:

  * add/remove columns from the popup grid 
  * change the whereclause 
  * change the fields which are searched as part of the suggestion box display 
  * etc. 

Note to change a selector the module it belongs to needs to be in development.
If not then it is possible that the client-side javascript (representing the
selector) is not refreshed automatically.

##  Defining Out Fields

The usual return values from a Selector is the record _id_ and _indentifier_ .
In some cases the developer wants to return more fields and not only this two.
You can mark a Selector Field as _Out Field_ and we'll be part of the
JavaScript returned object.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Note: By
default the **id** and **_identifier** fields are part of the returned object  
---|---  
  
![](/assets/developer-guide/etendo-classic/concepts/Selectors-13.png){: .legacy-image-style}

  

###  Using Out Fields in manual code (advanced)

You can use the New Selectors in manual code (not generated by WAD). You must
include all the necessary JS imports. There is a 'empty' hook function
**onValueChanged** that you can override in your manual window, to perform any
custom action. When the user picks a row, this function gets executed. By
default it doesn't do anything.

####  Example of function

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  To test
this code, you must have a browser with console enabled, e.g.  Firefox  with
Firebug  
---|---  
      
    
     
    isc.OBSelectorLinkWidget.addProperties({
       onValueChanged: function(selected) {
           // selected is an object with members id and _identifier
           // plus all Out Fields
           window.console.log("%o", selected); 
         }
       }
    });

In this case all instances of the OBSelectorLinkWidget will execute the same
function, this example function just prints the object passed as parameter.

You can also only override the function on a particular instance.

    
    
     
    // sc_C_Bpartner_One_ID is an instance of OBSelectorWidget or OBSelectorLinkWidget
    sc_C_Bpartner_One_ID.onValueChanged = function(selected) {
     window.console.log("%o", selected);
    };

##  Providing a new Selector Template (advanced)

The selector definition is converted to javascript code using a template. The
template is selected in the selector (see step 2 above). It is possible for a
module to add a new template which can be used for creating selectors.
Creating a new template needs to be done by a developer with a good
understanding of Openbravo.

Also to implement a new template it is necessary to understand the template
processing and template handling functionality used by Openbravo. The
Openbravo_3_Architecture  page provides detailed information. It discusses
both template processing, caching, i18n and also gives pointers on how to
implement a custom template.

The template used for the selector can be found in the source tree of the
org.openbravo.userinterface.selector module inside the
org.openbravo.userinterface.selector.templates package in the selector.ftl
file.

A custom template should be created inside a separate module. To make use of
it define it inside the Application Dictionary > Templates.

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-15.png){: .legacy-image-style}

  
The main fields to set:

  * The TemplateClasspathLocation should point to the location in the source tree of the custom template. 
  * The ComponentType **must** be set to selector. The ComponentType determines if the template can be selected in the selector definition. 

  

![](/assets/developer-guide/etendo-classic/concepts/Selectors-16.png){: .legacy-image-style}

  
Then when defining selectors a consultant can select the custom template.

##  Customizing the look and feel of the selector

The styling of the selector is mostly automatically derived from the styling
of other components. Only the icon on the right of the field needs to be
styled, see  this page  for more information.

##  Troubleshooting

###  The suggestion box does not filter

**Symptom** : When typing in values in the selection box it does not filter,
all records are shown.

**Cause** : This can happen when you have accidentally added boolean/yes/no
fields to be 'search in suggestionbox'.

**Solution** : uncheck the 'search in suggestionbox' fields for the
boolean/yes/no fields, searching these fields is not supported by the selector
in the suggestion box.

  

###  The suggestion box is always empty

**Symptom** : When typing values in the selection field the suggestion box is
empty or shows much less results than expected, also selecting the direct drop
down results in an empty/smaller than expected list.

**Cause** : this happens because there are 'search in suggestionbox' fields
which require a join to a table while the foreign key is not always set. Only
the records which have a value in the foreign key are shown.

**Solution** : if the foreign key selection field is the only one on which is
filtered this is fine, however if there are multiple search fields then
searching on non-mandatory foreign key fields is not supported by the
selector.

##  Advanced Topics

###  HQL Transformers

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 22Q4  ** .  
---|---  
  
Since version 22Q4, it is possible to modify an hql query entirely via java
and dependency injection using transformers. To implement the new
functionality follow this how to:
http://wiki.openbravo.com/wiki/How_to_create_a_HQL_Based_Table#HQL_Transformers

###  Using foreign keys in HQL Custom queries

Since version 23Q2, it is possible to define HQL queries with foreign key
columns, that is, columns that will have a combo on the column filter.

In order to do that, the HQL select clause for that property needs to point to
an entity (i.e. e.organization, instead of e.organization.name). Then in the
definition of the selector field we have to select a Table reference that
points to the target entity.

Retrieved from "  http://wiki.openbravo.com/wiki/Selectors  "

This page has been accessed 31,018 times. This page was last modified on 9 May
2023, at 16:59. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

