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

  

#  How to Create a Window

##  Contents

  * 1  Objective 
  * 2  Module & Table 
  * 3  Creating the New Window 
  * 4  Creating the Menu Item 
  * 5  Compiling the Application with the New Window 
  * 6  The Result 

  
---  
  
##  Objective

The objective of this how-to is to show how you can create a new  window  from
scratch. The how-to builds on top of two previous how-to's which explained
How to create a module  and  How to create a table.

As a reminder the scenario this is based on:

Imagine we are developing an HR module and we need a window that will enable
the user to input salaries of employees. We also need to track the employee's
salary so history records need to be preserved. Each salary record needs to
have a Valid From Date field that indicates when a particular salary came into
being. The record belonging to a particular employee with the latest Valid
From Date is the salary that is valid today. Note that employees are already
inside the system contained in the C_BPARTNER database table and indicated by
the C_BPARTNER.ISMEPLOYEE column. Therefore, we only need to create a database
table that will hold the actual salaries.

##  Module & Table

As mentioned in the objective this tutorial is based on two previous tutorials
and assumes that the following objectives have been already completed:

  * Creation of a new module with dbprefix _HT_
  * Creation + Registration in the AD of a new table _ht_salary_

##  Creating the New Window

Using the _**System Administrator** _ role navigate to _**Application
Dictionary || Windows, Tabs and Fields** _ . Create a new record as indicated
by the screenshot below:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-0.png){: .legacy-image-style}

Main fields of this window are (for more information see the  AD_Window  table
description):

  * **Name** Defines the name that Openbravo uses to recognize this window. 
  * **Description** Gives a small description of the table. 
  * **Help/Comments** Defines the text that is displayed in Help window. 
  * **Window Type** Defines some user interface specifics for a window: 
    * _Maintain_ : is used for windows with few entries. 
    * _Transaction_ : for transactional windows. 
      * The header tab's underlying table must contain the PROCESSED and UPDATED columns 
      * by default this window filters out old (n days – _**General Setup > Application > Session Preferences ** _ window setting) and processed documents. 
    * _Query Only_ : for read-only windows that only enable viewing of data. 

  
Save this record and move to _**Tab** _ tab. Create a new record as shown
below, creating the first tab to show the employee information:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-1.png){: .legacy-image-style}

Main fields of this window are (for more information see the  AD_Tab  table
description):

  * **Name** Defines the name that Openbravo uses to recognize this tab. 
  * **Description** Gives a small description of the table. 
  * **Help/Comments** Defines the text that is displayed in Help window. 
  * **Table** Specifies the table that the tab will show the data from. 
  * **Table Level** Defines the hierarchy of tabs, _0_ being the highest level. 
  * **UI Pattern** This dropdown offers the following options: 
    * _Standard_ \- standard interface where multiple records can be added, viewed and edited 
    * _Read Only_ \- this option disables any editing/creating capabilities for any user within this tab 
    * _Single Record_ \- this option enforces a one-to-one relationship between a parent and a child tab, allowing the user to enter maximum one record in the tab 
  * **HQL Where Clause** By using this HQL filter, the user will never be able to see data that does not fit the criteria. When referring to properties of the entity shown in the tab then use the prefix **e** . In our case, we use this field to display only business partners that are our employees (using the _employee_ property). 
  * **SQL Where Clause** Same like HQL Where Clause but using SQL syntax and used for filtering in _classic windows_ . 

Save this record and then click the _**Copy Tab Fields** _ button to copy
fields from the existing main tab of the Business Partner window into our new
one. Select the _Business Partner-Business Partner_ _Tab - Window_ combination
and confirm the dialog with OK.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-2.png){: .legacy-image-style}

  
Move to _**Field** _ tab to see all the created fields.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-3.png){: .legacy-image-style}

  
If required, changes to these fields could be made or new ones could be added
manually. For not header tabs, it is very important not to remove the field
that point the to the ID field of its parent tab, as it would made not
possible to create records in this tab using the grid view. For more
information see the  AD_Field  table description. However, in our case we are
happy with the way they are.

Now, go back to _**Tab** _ tab and create a new record that will represent the
child tab of the Employee tab where salaries will be managed:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-4.png){: .legacy-image-style}

  
Most importantly, make sure you select:

  * **Table** = _HT_Salary_
  * **Tab Level** = _1_

For more information see the  AD_Tab  table description.

By clicking and confirming the **Create Fields** dialog, the application will
automatically insert the columns of the selected table into the fields tab of
the _Salary_ one.

  
To arrange the columns according to common look and feel of other windows we
now change a view field properties as can be seen in following screenshot.

  * Hide field _c_bpartner_id_
  * Reorder fields (using sequence), to have _isactive_ after all other fields 
  * Mark _amount_ and _isactive_ as **Start in new line**

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-5.png){: .legacy-image-style}

  
For Openbravo to create links (labels that appear blue) to table elements, the
system needs to know which window represents the table where a certain element
resides. In our case, the **Employee Salary** window is used to manage the
content of the **HT_Salary** database table. Hence, all salary records need to
be shown within that window. To indicate that go to the _**Application
Dictionary || Tables and Columns** _ window, find our HT_Salary table and set
the **Window** as indicated below:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-6.png){: .legacy-image-style}

##  Creating the Menu Item

A menu item is required for the user to be able to call up the new window we
developed. Using the System Administrator role navigate to _**General Setup ||
Application || Menu** _ and create a new record:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-7.png){: .legacy-image-style}

  
Main fields of this window are (for more information see the  AD_Menu  table
description):

  * **Name** Defines the name that Openbravo uses to recognize this menu item. 
  * **Description** Gives a small description of the table. 
  * **Summary level** Defines a folder containing menu items (windows, processes, reports and so on). 
  * **Action** Defines the type of menu item. 
  * **URL** If _Action_ is _External link_ or _Internal link_ , defines the _URL_ to be linked. 
  * **Special Form** If _Action_ is _Form_ , defines the form to be linked. 
  * **Process** If _Action_ is _Process_ , defines the process to be launched. 
  * **Report** If _Action_ is _Report_ , defines the report to be linked. 
  * **Window** If _Action_ is _Window_ , defines the window to be linked. 

Save this record then click on _Tree_ icon  ![](/assets/developer-
guide/etendo-classic/how-to-guides/How_to_Create_a_Window-8.png){: .legacy-image-style} .

Here you can drag and drop the new Employee Salary menu item to any of the
other menu groups.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-9.png){: .legacy-image-style}

##  Compiling the Application with the New Window

Finally, the application needs to be recompiled in order to generate the new
window's code and deploy it to Tomcat. If using Eclipse, use the
**eclipse.compile** ant task, choose **eclipse.compile** as Ant Configuration
and enter '"Employee Salary"' into the dialog that pops up. If manually
compiling Openbravo, use the _**ant compile.development -Dtab="Employee
Salary"** _

**Important note** : once the compilation has finished, **restart Apache
Tomcat server** . In Windows, it is best to stop the Tomcat before running the
build task and the start it again afterwards since Windows locks certain files
the the _compile.development_ build task might not be able to copy over.  
  
---  
  
See more on  Build Tasks  .

##  The Result

Using the _**F &B International Group Admin ** _ role, select the link to the
new window from the menu. Notice the new window and the two tabs
hierarchically positioned one above another (one Employe can have one or more
salary records):

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-10.png){: .legacy-image-style}

  
By double clicking Juan Lopez , details of this employee appear, however in a
read-only mode (notice all fields are gray).

By clicking 'New in form' while having the _Salary_ tab in focus a salary
record can be created for this employee.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Window-11.png){: .legacy-image-style}

  

You have now successfully created your own new window and seen how it came to
life within Openbravo. Congratulations!

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_Create_a_Window  "

This page has been accessed 51,606 times. This page was last modified on 22
October 2019, at 20:26. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**
