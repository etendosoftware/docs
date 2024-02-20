---
title: How to Create a Window
tags: 
  - window creation
  - module development
  - field management
  - UI design
  - Database table creation
---

  
##  Overview

The objective of this how-to is to show how you can create a new  window  from
scratch. The how-to builds on top of two previous how-to's which explained
How to create a module  and  How to create a table.

Let's have a reminder scenario to base this process on:

Imagine we are developing an HR module and we need a window that will enable
the user to input salaries of employees. We also need to track the employee's
salary so history records need to be preserved. Each salary record needs to
have a Valid From Date field that indicates when a particular salary came into
being. The record belonging to a particular employee with the latest Valid
From Date is the salary that is valid today. Note that employees are already
inside the system contained in the C_BPARTNER database table and indicated by
the `C_BPARTNER.ISEMPLOYEE` column. Therefore, we only need to create a database
table that will hold the actual salaries.

##  Module & Table

As mentioned above, this tutorial is based on two previous tutorials
and assumes that the following objectives have been already completed:

  * Creation of a new module with _dbprefix_ _HT_
  * Creation + Registration in the AD of a new table _ht_salary_

##  Creating the New Window

Using the *System Administrator* role navigate to `Application Dictionary` > `Windows, Tabs and Fields `. 
Create a new record as indicated by the screenshot below:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_0.png) 


The main fields of this window are:
(for more information see the  AD_Window  table
description)

  * *Name*: defines the name that Etendo uses to recognize this window. 
  * *Description*: gives a small description of the table. 
  * *Help/Comments*: defines the text that is displayed in Help window. 
  * *Window Type*: defines some user interface specifics for a window: 
    * _Maintain_ : is used for windows with few entries. 
    * _Transaction_ : for transactional windows. 
      * The header tab's underlying table must contain the PROCESSED and UPDATED columns 
      * by default this window filters out old (n days – `General Setup` > `Application ` >`Session Preferences` window setting) and processed documents. 
    * _Query Only_ : for read-only windows that only enable viewing of data. 

  
Save this record and move to *Tab* tab. Create a new record as shown
below, creating the first tab to show the employee information:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_2.png)  


Main fields of this window are (for more information see the  AD_Tab  table
description):

  * *Name*: defines the name that Etendo uses to recognize this tab. 
  * *Description*: gives a small description of the table. 
  * *Help/Comments*: defines the text that is displayed in Help window. 
  * *Table*: specifies the table that the tab will show the data from. 
  * *Table Level*: defines the hierarchy of tabs, _0_ being the highest level. 
  * *UI Pattern* This dropdown offers the following options: 
    * _Standard_ \- standard interface where multiple records can be added, viewed and edited 
    * _Read Only_ \- this option disables any editing/creating capabilities for any user within this tab 
    * _Single Record_ \- this option enforces a one-to-one relationship between a parent and a child tab, allowing the user to enter maximum one record in the tab 
  * *HQL Where Clause*: by using this HQL filter, the user will never be able to see data that does not fit the criteria. When referring to properties of the entity shown in the tab then use the prefix *e* . In our case, we use this field to display only business partners that are our employees (using the _employee_ property). 
  * *SQL Where Clause* Same like HQL Where Clause but using SQL syntax and used for filtering in _classic windows_ . 

Save this record and then click the *Copy Tab Fields* button to copy
fields from the existing main tab of the Business Partner window into our new
one. Select the *Business Partner-Business Partner* Tab - Window combination
and confirm the dialog with OK.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_2.png) 


  
Move to *Field* tab to see the created fields.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_3.png)  


  
If required, changes to these fields could be made or new ones could be added manually. 

!!!note
    For not header tabs, it is very important not to remove the field
    that point the to the ID field of its parent tab, as it would made not possible to create records in this tab using the grid view. 

!!!info
    For more information, see the  AD_Field  table description.



Now, go back to *Tab* tab and create a new record that will represent the
child tab of the Employee tab where salaries will be managed:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_4.png) 


  
Most importantly, make sure you select:

  * *Table* = _HT_Salary_
  * *Tab Level* = _1_

!!!info
    For more information see the  AD_Tab  table description.

By clicking and confirming the *Create Fields* dialog, the application will
automatically insert the columns of the selected table into the fields tab of
the *Salary* one.

  
To arrange the columns according to common look and feel of other windows, we now change a view field properties as can be seen in following screenshot.

  * Hide field _c_bpartner_id_
  * Reorder fields (using sequence), to have _isactive_ after all other fields 
  * Mark _amount_ and _isactive_ as *Start in new line*

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_5.png) 


  
For Etendo, to create links (labels that appear blue) to table elements, the system needs to know which window represents the table where a certain element resides. In our case, the *Employee Salary* window is used to manage the content of the *HT_Salary* database table. Hence, all salary records need to be shown within that window. 

To indicate that, go to the `Application Dictionary` > `Tables and Columns` window, find our HT_Salary table and set the *Window* as indicated below:

  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_6.png)

##  Creating the Menu Item

A menu item is required for the user to be able to call up the new window we developed. Using the System Administrator role navigate to `General Setup` > `Application` >`Menu` and create a new record:

  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_7.png)


  
Main fields of this window are (for more information see the  AD_Menu  table
description):

  * *Name*: defines the name that Etendo uses to recognize this menu item. 
  * *Description*: gives a small description of the table. 
  * *Summary level*: defines a folder containing menu items (windows, processes, reports and so on). 
  * *Action*: defines the type of menu item. 
  * *URL* If _Action_ is _External link_ or _Internal link_ , defines the _URL_ to be linked. 
  * *Special Form*: If _Action_ is _Form_ , defines the form to be linked. 
  * *Process*: If _Action_ is _Process_ , defines the process to be launched. 
  * *Report*: If _Action_ is _Report_ , defines the report to be linked. 
  * *Window*: If _Action_ is _Window_ , defines the window to be linked. 

Save this record then click on _Tree_ icon ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_8.png)


Here you can drag and drop the new Employee Salary menu item to any of the
other menu groups.

  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_9.png)
##  Compiling the Application with the New Window

Finally, the application needs to be recompiled in order to generate the new window's code and deploy it to Tomcat. 

```bash
./gradlew smartbuild
```

##  The Result

Using the *F &B International Group Admin* role, select the link to the new window from the menu. 

Notice the new window and the two tabs hierarchically positioned one above another (one Employe can have one or more salary records):

  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_10.png)

  
By double clicking Juan Lopez , details of this employee appear, however in a read-only mode (notice all fields are gray).

By clicking 'New in form' while having the _Salary_ tab in focus a salary record can be created for this employee.

  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_11.png)

  
!!!success
    You have now successfully created your own new window and seen how it came to life within Etendo. 

This work is a derivative of [How to create a window](http://wiki.openbravo.com/wiki/How_to_Create_a_Window){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.


