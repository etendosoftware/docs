---
title: How to define an on Create Default
tags:
    - define 
    - on create
    - default
    - development
    - howto

status: beta
---
#  How to define an on Create Default

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

In this section, it is briefly explained what an **onCreateDefault** is, in what situations it is useful, and how to correctly define one.

##  Concept

`OnCreateDefaults` are SQL statements which are executed by the `update.database` task when a database column is created. They are normally used to insert data into a newly created column. It is important to note that they are only executed when the column is being created. If the column is already in the database, `update.database` will not execute the `onCreateDefault` statement. To fill data into an already created column, you can use a Module Script. For more information about the Module Scripts, visit [How to Create Build Validations and Module Scripts](../how-to-guides/how-to-create-build-validations-and-module-scripts.md).

##  Development Process

`onCreateDefault` statements are added directly to the XML file of the table. This means that the main development steps should be:

* Add the new column in the database 
* Run export.database to export the column to the XML file 
* Edit the xml file to add the onCreateDefault 

An `onCreateDefault` statement should be valid SQL which can be appended in two different kinds of SQL commands. Let us assume that the table `C_BPARTNER` is going to be extended, adding a `MYCOLUMN` column. We need to design an `onCreateDefault` statement which works with the following two kinds of SQL commands:

```
INSERT INTO C_BPARTNER (Column1, Column2, ..., MYCOLUMN) SELECT (Column1, Column2, ..., MYCOLUMN_ONCREATEDEFAULT) FROM C_BPARTNER_
 
UPDATE C_BPARTNER SET Column1=ValueForCol1, Column2=ValueForCol2, ..., MYCOLUMN=(MYCOLUMN_ONCREATEDEFAULT)
```

So, in this case, let us imagine that MYCOLUMN is a Yes/No column, and we want to set it as 'N' for the existing rows of C_BPARTNER when the column is first created. We would modify the column definition, so it looks like this:

```
<column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
<default><![CDATA[N]]></default>
<onCreateDefault><![CDATA['N']]></onCreateDefault>
</column>
```

Notice the difference in syntax in the `onCreateDefault`, compared to the standard default. We need to add quotes there, because of the type of SQL command the `onCreateDefault` will be inserted in.

!!!note "Important"
        
    * The `onCreateDefault` SQL statement **must return only one row**. 

    * The execution of the `onCreateDefault` takes place while the table is being rebuilt. This means that if the statement fails, there could be data loss in the customer database when the module is installed. Therefore **the statement must be built so that it always can be executed**. 

  
One limitation of the current implementation of `onCreateDefaults` is that, due to having to support the two different kinds of SQL syntax, you cannot make reference to a different column of the table you are modifying. This means that it can be very tricky to design a correct `onCreateDefault` in situations in which you need to make a link to a different table. For these situations, a Module Script could be used instead of an `onCreateDefault`, and the same result can be achieved this way.

##  How to Correctly Remove an `onCreateDefault`

`onCreateDefaults` are also removed by editing the XML file. The correct way to remove it is to delete the contents inside the <onCreateDefault> tag, but leave the tag itself there. If you delete everything, including the tag, next time you export the module (or Core, if you are editing a Core column), there will be an inconsistency, as [`DBSourceManager`](../concepts/dbsourcemanager.md) will create an empty `onCreateDefault` element. In a practical example, the following column has an `onCreateDefault`:

```
<column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
<default><![CDATA[N]]></default>
<onCreateDefault><![CDATA['N']]></onCreateDefault>
</column>
```

If we want to remove it, the correct way would be to leave the column like this:

```
<column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
<default><![CDATA[N]]></default>
<onCreateDefault/>
</column>
```

---

This work is a derivative of [How to Define an on Create Default](http://wiki.openbravo.com/wiki/How_to_define_an_on_Create_Default){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 