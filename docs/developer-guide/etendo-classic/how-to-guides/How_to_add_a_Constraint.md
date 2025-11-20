---
title: How to add a Constraint
tags: 
  - Constraint
  - Table
  - Create message
  - Database


status: beta
---


#  How to add a Constraint

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.


###  Overview

When adding new columns to a table like the **Valid To date** in the **ht_salary table**, it is often necessary to enforce logical rules so the data remains consistent. In this case, the Valid To date must always be the same as or later than the Valid From date. This rule can be enforced by adding a **database constraint** which is a `SQL-Expression`, which checks the validity of data whenever rows are inserted or updated.

!!!info
    For more information visit, [How to Add Columns to a Table](../how-to-guides/how-to-add-columns-to-a-table.md).


###  Modularity


As the constraint will be placed in the module with dbprefix `HT2` but the table **ht_salary** is defined in another module `HT`, the constraint name must follow the usual rule and start with `EM_HT2` .

If the constraint would be added in the same module as its table, then this `EM_ naming-rule` would not be needed. However, the best practice is to let it start with the **full tablename** in that case to ensure its name will be unique across the database.

!!! info
    Remember that in all cases the full constraint-name (like any other `db-object` name) is not allowed to be longer then 30 characters.  
 
  
###  Add constraint to database

To add the constraint execute the following clause in database:

**PostgreSQL**

    
    
     
    ALTER TABLE ht_salary ADD constraint em_ht2_ht_salary_date_chk CHECK (em_ht2_validto>=validfrom);

**Oracle**

    
    
     
    ALTER TABLE HT_SALARY ADD CONSTRAINT EM_HT2_HT_SALARY_DATES_CHK CHECK  (VALIDTO>=VALIDFROM) ENABLE;

!!! note
    Adding a **unique constraint** to an existing module is considered as an API change and could affect to existing environments already populated. Before adding it, evaluate the risk and consider creating a buildvalidation to check if the existing data complies. If it does not, the buildvalidation can stop the update process and give a proper message.  
 
  
###  Adding a proper message

Now when editing data in the `Employee Salary > Salary` tab and trying to use a **Valid to** date lying before the **Valid from** date we get an error message like shown below.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_Constraint-2.png)

However, this error message is not too useful yet for the user as it does not indicate at all why the save action was not done.
  
It would be better if it said something like **The Valid To date cannot be before the Valid From date** to help the user to specify the two dates correctly.
This is done by adding a new  Message. This leverage the Etendo translation system so the message can be translated and shown in a users language.

!!! info
    For more information on how to create a new message entry visit, [Messages](https://docs.etendo.software/developer-guide/etendo-classic/concepts/messages/).

As a short summary:

In the `Application Dictionary > Message` window create a new record using the following details:

  * **Module** `Openbravo Howtos 2`as this is the module containing the constraint also. ???
  * **Search key** : The search key must be exactly the same as the constraint's one, in this case `_em_ht2_ht_salary_dates_chk_` as this is the link between the constraint and the message. 
  * **Message type** : Depending on the type the UI for the message box will be different (green for success, yellow for warning...), in our case we want a red error message box, so we select **Error**. 
  * **Message text** : It is the user friendly message that will be displayed inside the message box. So let's enter: **The Valid To date may not be before the Valid From date**. 

Then, we will have a message like:


![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_Constraint-3.png)

###  Export database

Whenever Application Dictionary or Physical database is modified, it is possible to export that information to `xml files`, this is the way Etendo maintains database data as part of its source code files. 
To do it just execute:

    
    
     ant export.database
    
!!! info
    For more information visit [Development Tasks Document](../concepts/development-build-tasks.md).



This work is a derivative of [How to Add a Constraint](http://wiki.openbravo.com/wiki/How_to_add_a_Constraint){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.


