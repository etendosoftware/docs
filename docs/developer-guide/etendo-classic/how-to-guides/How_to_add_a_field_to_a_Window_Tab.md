---
tags:
 - Etendo
 - Etendo Classic
 - Customization
 - UI Design
 - Application Dictionary
 - Modules
---

#  How to add a field to a Window Tab

##  Objective

The objective of this section is to show how you can add a new  field  to a tab  in Etendo Classic.

It is closely related to the previous [How to add Columns to a Table](/developer-guide/etendo-classic/how-to-guides/How_to_add_Columns_to_a_Table/) section which showed how to add new columns to a table.

In that previous section, the following three new columns were added to the
_ht_salary_ table.

  1. _ValidTo_ , a simple date-field matching the ValidFrom date already present in this table 
  2. _Payment Schedule_ , shown as a combobox to the user to be able to choose from three values defined in a list-reference. 
    1. First day of the month 
    2. Mid of the month 
    3. Last day of the month 
  3. _Payment Category_, a link to another existing table which allows selecting among the values present in that table. 

The task of adding those new columns to the existing _Employee Salary_ window
which was created in [this](/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window/) other section is now fairly simple as most of the work
(like defining references, elements) has been already done when adding the
columns to the table.

In this section, we will place the new fields in the module with dbprefix HT2 which already contains the new columns.

###  Add the fields to the window

The process to add new fields to an existing window is the same as the one to add fields to a new (empty) window. Going to Application Dictionary | Window, Tabs and Fields, we need to search for the _Employee Salary_ window. Then, for that window, mark its _Salary_ tab.

Now, we use the Create Fields process on this tab to let it add all columns
of the underlying _ht_salary_ table to this tab if they have not been previously
added.

This will then add three new fields to the tab matching the three new columns
and automatically place those three fields into the module with prefix HT2.

The next step is to configure those new fields to get a better layout:

  * _EM_Ht2_ValidTo_ change Sequence Number' _=_  _72_ , to place it right after the _ValidFrom_ field 
  * _EM_Ht2_Payment_Schedule_ change Sequence Number = 76 and Start in new Line Line = Yes to place it into a new line after the ValidTo field 
  * _EM_Ht2_C_Salary_Category_ID_ change Sequence Number = 78 to place it after the _Payment Schedule_ field 

After this change, the list of columns should look similar to the following screenshot: 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_add_a_field_to_a_Window_Tab-0.png){: .legacy-image-style}

  
As a last step, the Synchronize Terminology process should be run to
synchronize our newly added fields to the elements created for the columns
they are based on, so that the UI labels for the new fields get the names
defined in those elements.

If this window should also be used in _classic UI mode_ then now _ant
smartbuild_ should be execute to compile the changed window.

To see the changes in the new UI just switch role away from the _System
Administrator_ role used for this section and go to the changed window to see it
having the new field as the one shown here:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_add_a_field_to_a_Window_Tab-1.png){: .legacy-image-style}

---

This work is a derivative of [How to add a field to a window tab](http://wiki.openbravo.com/wiki/How_to_add_a_field_to_a_Window_Tab){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 