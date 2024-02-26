---
title: Tables
---
  
##  Introduction

Physical database tables are the basis  Application Dictionary Data Model  is
built on. This document discusses the particularities all tables in Etendo Classic must have.

##  Common Columns

All tables in Etendo Classic must have some common columns. All these columns
must be defined as not nullable.

###  Primary Key

All tables in Etendo Classic have a single column primary key. This column will
be automatically populated with a generated  UUID  therefore the type for this
column must be _VARCHAR2(32)_ .

Primary Key column must be named like its table with an __ID_ suffix. Thus the
primary key column for _HT_Salary_ table would be _HT_Salary_ID_ .

This column must be also set as primary key in database, it is not enough with
defining it as ID in Application Dictionary.

###  Client/Organization

As Etendo Classic is a  multi client and multi organization  application, all
data belongs to a client and an organization, so all tables must have these
two columns:

  * _AD_Client_ID_
  * _AD_Org_ID_

These columns are a foreign key to  AD_Client  and  AD_Org  tables. So their
types must also be _VARCHAR2(32)_ , and there must be a foreign key to these
tables.

###  Audit Information

Finally there are some columns that store information about whether a record
is active and when and who created and last modified it. This information is
maintained in the following columns:

  * _IsActive_ : It is a boolean value (Y/N) indicating whether the record is active or not. Its type must be _CHAR(1)_ and generally, its default value is 'Y'. It is also good practice to create a check constraint forcing its value to be either 'Y' or 'N'. 
  * _Created_ : It contains the date and time when the record was created. Its type is _DATE_ . 
  * _CreatedBy_ : Indicates the user that created the record. It is a foreign key to  AD_User  so its type is _VARCHAR2(32)_ . 
  * _Upated_ : It contains the last date and time when the record was modified (or created if no modification was performed later). Its type is _DATE_ . 
  * _UpdatedBy_ : Indicates the last user that updated the record. It is a foreign key to  AD_User  so its type is _VARCHAR2(32)_ . 

##  Naming conventions

When creating new tables it is necessary to pay special attention to the names
given to tables and columns, particularly regarding modularity.

###  Tables

The only element to take into consideration is the module's  DB Prefix  . The
table's name must start with this DB prefix followed by underscore character
(_).

The following table prefixes are used by Etendo Classic and are not allowed to be used by any modules:

  

Table prefix  |  Description  
---|---  
A  |  asset management  
AD  |  application dictionary  
C  |  core functionality  
I  |  import temporary tables and processes  
M  |  material management  
FACT  |  accounting  
GL  |  general ledger  
MA  |  manufacturing  
MRP  |  material resource  
S  |  service management  
AT,AU,EM,FIN,I,MA,R,RV,T  |  other Core prefixes  
CUS, PD, US, ZZ  |  personal developments  
APRM  |  Advanced Payables and Receivables Mngmt  
OBUIAPP, NAVBA  |  User Interface Application  
OBCHW  |  HTML Widget  
OBCLFRE, OBCLKER  |  User Interface Client Kernel  
OBKMO  |  Workspace & Widgets  
OBCQL  |  Query/List Widget  
OBSERDS  |  JSON Datasource  
OBJSON  |  JSON REST Webservice  
OBUISEL  |  User Interface Selector  
OBUISC  |  Smartclient  
FINPR  |  Orders Awaiting Delivery  
  
###  Columns

####  Modularity

In case the column belongs to the same module than its table no special rule
must be followed for its name. But if the column is going to be added to a
table belonging to a different module, the column name must start with _EM__
plus the DB Prefix of the module the column belongs to. For instance,
_EM_MYMODULEDBPREFIX_COLUMNNAME_ .

!!!notes
    The column name must not exceed the 30 characters long, that includes the
    "EM_" plus the DB Prefix of the module.

    In PostgreSQL, **all column names must be defined in lower case**  

This restriction also applies for naming constraints, triggers and functions.

####  Primary Key Column

Naming for primary key column is explained in  Primary Key  section of this
document.

####  Foreign Key Columns

It is a best practice to name, if possible, foreign key columns in the same
manner than the primary key column of the table they link to. The reason for
this is that in Oracle, foreign key (and the rest of the db contraints) names must be unique at a database-level. 
So, for example if we have in our table a column that contains a business partner it should be named _C_BPartner_ID_ because it is a foreign key to _C_BPartner.C_BPartner_ID_ column. This is not possible when there is the same table more than one column linking to the same table or when adding columns in a different module than the table's one.

Following this naming rule allows to define standard references as _TableDir_ when the column is defined in Application Dictionary.

####  Naming of Columns and the Data Access Layer

In Etendo, Java classes are generated from the tables definition. A DAL
entity is generated from every table defined in the Application Dictionary.
You can find more information about this  here  .

It is important you take this into account when thinking about the names for
your columns. The columns you define in a table will correspond to Java
properties in a generated Java class. Therefore, **you must not choose names
which collide with Java keywords** , such as _class_ , _if_ , _int_ , ...

You can find a list of the Java keywords  here  .

##  Supported Column Data types

DBSourceManager, the utility that Openbravo uses to manage database related
operations, supports a subset of the datatypes that Oracle and PostgreSQL
databases support. Below we include the currently supported data types:


Oracle  |  PostgreSQL  
---|---  
(n)char  |  char  
(n)varchar(2)  |  varchar  
blob  |  bytea  
date  |  timestamp  
number  |  numeric  
clob  |  text  
  
Retrieved from "  http://wiki.openbravo.com/wiki/Tables  "

This page has been accessed 23,942 times. This page was last modified on 12
July 2011, at 09:09. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

