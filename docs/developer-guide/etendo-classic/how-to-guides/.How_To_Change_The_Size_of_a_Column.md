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

  

#  How To Change The Size of a Column

**Languages:** |

** English  ** |  Translate this article...  
  
---|---  
  
##  Contents

  * 1  Objective 
  * 2  Recommended articles 
  * 3  Execution Steps 

  
---  
  
##  Objective

The objective of this article is to show you how to change the size of a
column inside the database. It enables the user to have a certain amount of
flexibility within his/her database.

##  Recommended articles

Before reading this guide, it is necessary to have a proper understanding of
Openbravo's  Modularity  concept and how to  create and package a module  ,  
as we take the knowledge from these articles as a given in this guide.

In case you are working with configuration scripts or templates on a regular
basis, the following link to an article might be of interest to you, since it
describes  how to create a configuration script  .

##  Execution Steps

In Openbravo you are able to change the size of a column. To achieve this you
must follow the following steps:

  1. Create a  template  and set its status as _**"In Development"** _ . 
  2. Modify the column size within the database with the **"ALTER TABLE"** SQL command. 

     **IMPORTANT** : The new value must be greater than the old one. 
    
    
    Postgres: ALTER TABLE <table_name> ALTER COLUMN <column_name> type <type>(<new_size>)
    Oracle:   ALTER TABLE <table_name> MODIFY <column_name> <type>(<new_size>)

  3. Update the new column size in the **Application Dictionary** . For this, we go to the _**"Tables and Columns"** _ window, find the column definition and specify the new size there 
  4. Export the database: _**"ant export.database"** _ (with this you are exporting the template definitions) 
  5. Export the configuration script: _**"ant export.config.script"** _ (with this you are exporting the core changes into the template) 
  6. Check the generated configuration script and verify that the change regarding the new column size appears in the first lines. 

|  ![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
**Note:** As a final remark with great importance: If the column that has been
modified is being used by a database function by giving its value to another
variable for example, you must check that this variable has an equal or
greater size (at least the size of the new modified column). Because if not,
the process would fail. This means, if the variable's size wasn't enough to
store the columns content, you have to modify the function as well, by
adjusting the size of the variable in question and exporting this change into
your template.

So please verify that your new column size does not affect you in any way
(functions or triggers) working with your database.  
  
---|---  
  
Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Change_The_Size_of_a_Column  "

This page has been accessed 23,704 times. This page was last modified on 22
May 2013, at 08:52. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

