---
tags:
  - Property field
  - Derived information
  - Validation rules
  - Form display
  - Grid display
  - Child records
--- 

#  How to Use Property Fields

##  Overview


A **property field** allows you to show derived information in a grid/form. A property field is very similar to a normal field in a tab. The only difference is that instead of the column, a property (path) is defined.

Property fields make it possible to:

  * show related information in a grid/form 
  * filter and sort by this related information 
  * show parent information in a child tab and filter/sort by this parent information 
  * create Etendo windows which show a child table in the root of the window, making it for example possible to create a single grid showing all sales invoice lines accross multiple sales invoice and filter using parent as well as child information. 

##  Example Module

This section is supported by an example module which shows example of the code
shown and discussed in this section.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), 

!!!info
      For more information see the  Examples Client Application  project page.

The example module also contains implementations of other sections.  

  
##  Defining property fields

Property fields are defined in the same way as a normal field in an Etendo
tab. The only difference is that instead of selecting a column a property is
set.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_use_property_fields-1.png){: .legacy-image-style}

  
The property can consist of multiple steps separated by a dot, the system will
help you to set the correct property value. If you make a typo then the system
will report an error.

Property fields are not editable in the user interface, they are however
automatically updated when inserting or updating a record in the system.

!!!note
      Property fields are meant to show derived information. They should not be used
      to show the contents of a column stored in the table associated with the tab
      where the property field is being defined.  

  
###  Using in validation rules

Property fields can be used in  Validations. In this case the
validation code referencing the property field should look like `
@_propertyField_ _fieldName_ _ _columnname_ @ ` where ` fieldname ` is the
name of the field property (lower case and removing blank spaces) and `
columnname ` is the name of the referenced column.

As field properties are only computed when the record is saved, but they are
not reevaluated on field changes, only in case they refer a path coming from
the record header should be used in validations. Example in Order Line you
could use any property field taking the data from its order header.

##  Using in display logic

You can set a display logic that references a property field. The way of
setting the display logic which references a property field is the following
one: `@inp_propertyField_NameOfThePropertyField_ColumnName@`. For example:

  * Imagine that you have a property field called Document with column name **DocumentStatus**. 
  * You have another field *Field A* which you want to display only when the property field **Document** has the status **DR**. 
  * In the display logic of the *Field A* field, you should write: `@inp_propertyField_Document_DocumentStatus@ = 'DR'`

##  Use case: show related information

The first usage of a property field is to show related information in the user
interface. The example in the previous section showed how to define a new
business partner category field in the sales invoice header window/tab. This
is visualized as follows in the user interface:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_use_property_fields-3.png){: .legacy-image-style}

  
And you can sort and filter on the related/derived field:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_use_property_fields-4.png){: .legacy-image-style}

  
And also display it in the form:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_use_property_fields-5.png){: .legacy-image-style}

  
!!!note
      Note that direct linking also works for derived fields, so in this example you
      can 'jump' directly to the business partner category window for the business
      partner category.


##  Use case: show child table in top of the window

A great usage of the property field concept is to show child records (for
example: sales invoice lines) in the root of a window. This then makes it
possible to filter and sort the child records accross multiple parents (for
example: sales invoice headers).

The screenshot below shows an example of a sales invoice line window which
shows all sales invoice lines accross multiple sales invoice headers. It makes
it really easy to filter and sort accross all sales invoice lines in the
system.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_use_property_fields-6.png){: .legacy-image-style}

  
Some things to note when creating these type of windows:

  * The main restriction for these types of grids is that insertion of records is not possible, editing and deletion are however no problem. So, for these types of windows/tabs set the UI pattern to **Edit Only**. 
  * For editing it is possible that certain fields need parent or other context information. This context information needs to be added as fields to the tab. If you do not want these context info fields to show up in the grid or form set the following properties to no (unchecked): displayed and show in grid view. 
  See the screenshot below which shows how the organization is added to the tab as a field, so that combos show the correct information when editing the sales invoice lines: 

  

This work is a derivative of [How to add a canvas field to a form or grid](http://wiki.openbravo.com/wiki/How_to_use_property_fields){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 





