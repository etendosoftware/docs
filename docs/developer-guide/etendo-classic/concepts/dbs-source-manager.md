---
tags: 
  - Java
  - Database Management
  - Database Independence
  - Oracle
  - PostgreSQL
---

#  DBSourceManager
  
  
##  Overview

DBSourceManager is a **Java library** that helps with database tasks related to development. Its most important feature is **database independence**. The user will be able to focus in the development of database features and let DBSourceManager deal with the database implementations details.

DBSourceManager is based on **DDLUtils** and the database model used by DBSourceManager is an extension of the model used by DDLUtils. DDLUtils supports a large list of database engines but all the extensions created in DBSourceManager only work for **Oracle and PostgreSQL**.

The main goal of DBSourceManager is to aid the developer in the creation and maintenance of **Database physical objects and data**. The way this works is via an array of `XML files` which represent database physical objects, or table records. DBSourceManager contains utilities which allow the developer to
export its objects into this `XML files`, and which allow modifications into these `XML files` to be moved into the database by updating it.

Therefore, the developer can focus on **creating and changing** its components (either in the database or in the `XML files`), and DBSourceManager can automatically move the changes in either place to the other.

##  Architecture

As previously stated, DBSourceManager is based on the **ddlutils Apache project**.
Internally, its structure can be described as a series of classes to handle the Database model, and a series of classes which are related to how the objects and its changes are transformed into `RDBMS-specific` commands.


##  Common tasks

The main tasks which DBSourceManager allows the developer to do are the following:

  * `export.database`: this task generates XML files corresponding with the database physical objects and the Application Dictionary table contents. 
  * `update.database`: this task updates the database applying the changes which are necessary to transform it so that it follows the model described in the XML files. 
  * `export.config.script`: this task generates a configuration script of the current system. 

!!!info
    You can find more information about the Etendo build tasks which are related to these tasks in [Development Build Tasks](../../etendo-classic/concepts/development-build-tasks.md). 

These tasks are very related to the **modularity concepts** in Etendo, so it is also worth to read more about them. 

!!!info
    For more information, visit: [modularity concepts](../../etendo-classic/concepts/Modularity_Concepts.md).

##  More information

DBSourceManager uses a mechanism which is called **Model filters**, to purposely remove some unwanted objects from the physical database model. These filters can be extended by modules. 

!!!info
    For more information, visit [How to Exclude Database Physical Objects from Model](../../etendo-classic/how-to-guides/How_To_Exclude_Database_Physical_Objects_From_Model.md).


This work is a derivative of [DBSourceManager](http://wiki.openbravo.com/wiki/DBSourceManager){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

