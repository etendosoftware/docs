---
title: Element and Synchronize Terminology
---
  
##  Element

Elements  define the text in the label to be displayed for each field in the
application as well as its related help. Each column in the Application
Dictionary is linked to an element, note that more than one column can be
linked to a single element, this is the way to reuse the same text for
different columns (and finally fields) in the application. For example,
_C_BPartner_ID_ is the name for a number of columns in the application, all of
them are a reference to a business partner, thus the text to be displayed as
well as the help for all of them is the same; instead of maintaining that
information redundantly in each column all these columns use the same element.

###  Element maintenance

Elements can be edited in **Application Dictionary || Setup || Element**
window (as _System Administrator_ ); but, usually, elements are not directly
created using this window but by the _Synchronize terminology_ . Once the
element is created this window is used to edit its contents.

###  Synchronize Terminology

It is the process that creates the elements for the columns that do not
already have an associated one and copies the information in the elements to
the columns and fields which are linked to them.

To run it go to **Application Dictionary || Synchronize Terminology** as
_System Administrator_ . Basically this process looks for all the columns that
have no linked element, in case the there is an element with the same column
name that the orphan column's one this element is linked to that column, other
case a new element is created with the same column name the column has. All
that is done taking into account module, thus an element is only reused if it
is defined in the same module as the column's one or in another one dependent
from the column's module. It also copies the text in the elements to the
fields that represent the columns for those elements.

!!! note  
    When creating/editing fields is worthless to write a good text for name, description and help fields since they will be overwritten with the ones in the element when the this process is run, so just leave them empty (or with some letters for mandatory ones). On the other hand, when creating a new column, if it is created a new element from this column the element will have the contents of those fields in the column, note that once the element is created the changes in the column fields will also be overwritten in this process.  

  
####  In detail

Here are all the steps the _Synchronize Terminology_ process executes.

  1. For all the columns and process parameters in the dictionary without element, create an element in case there is no element with the same column name in the same module or in a dependent one, copying to the new element name, help and description from the column/parameter. 
  2. Delete all the elements that are not used anymore. 
  3. For the rest of columns and process parameters without elements associate the existent element in the same module or in a dependent one having the same column name. 
  4. Update columns and process parameters with the name, help and description values in their associated elements. 
  5. Update centrally maintained fields with the name, help and description for the elements associated with their associated columns. 
  6. Update workflow nodes with the name and description in their linked windows. 
  7. Update menu entries with the name and description in their linked windows, processes, forms or workflows. 

###  Central Maintenance for fields

In most cases the previously defined process fits all the requirements for
field labels. But in some occasions, it is wanted to have a field with a
different set of label, help and description than the rest of fields
associated to the same column. For these cases it is possible to set no to the
_Central Maintenance_ check in **Application Dictionary || Windows, Tabs, and
Fields || Window >> Tab >> Field ** , doing so name, help and description in
the field will not be overwritten with the element's ones.

Let's see how it is used in with an example. A very common column name is
_AD_Language_ , these columns are a reference to languages stored in
_AD_Language_ table. The name for the _AD_Language_ element is _Language_ and
its help is _The Language identifies the language to use for display_ which is
very general. Modules have a language (which might be different to English)
which they have the UI defined in, the label and help for _AD_Language_ field
in _Application Dictionary || Module_ are _Module Language_ and _This language
defines the language used as base for the user interface elements in the
module_ , this is done by setting the field for _AD_Language_ column in
_Module_ tab as not centrally maintained and writing directly in the field the
name and help.

###  Translations

As elements are used to define text to be displayed in UI they can be
translated to different languages. The text in the element must be written in
the language its module defines, and the it can be translated to other ones.
The standard way to translate is by creating a new module with no additional
functionality but just translations for the module.

###  Purchase entries

If you look the fields in the **Application Dictionary || Setup || Element**
you will notice there are standard fields (name, help...) and the sames ones
but for purchases.

In Etendo Classic there are some tables that are used for sales and purchases
transactions, for example _C_Invoice_ table contains both sales and purchases
invoices. This means that _Purchase Invoice || Header_ and _Sales Invoice ||
Header_ tabs use the same table. But it is very usual to label fields for the
same column in a different way depending on whether it is a sales or purchase
window. Instead of doing it setting all the fields in the purchase windows as
not centrally maintained this is achieved by populating in the correspondent
elements the standard names and the purchase ones. Then the windows are
distinguished between sales and purchases using the _Sales Transaction_ check
in the **Application Dictionary || Windows, Tabs, and Fields || Window** tab.

Retrieved from "
http://wiki.openbravo.com/wiki/Element_and_Synchronize_Terminology  "

