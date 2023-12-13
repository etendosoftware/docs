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

  

#  Constraints and Triggers

##  Contents

  * 1  Introduction 
  * 2  Naming 
  * 3  Constraints 
    * 3.1  Messages 
    * 3.2  Backwards compatibility 
  * 4  Indexes 
    * 4.1  Operator Classes 
    * 4.2  Function based indexes 
    * 4.3  Partial indexes 
      * 4.3.1  Not Null Partial Indexes On Nullable Columns 
    * 4.4  Indexes for Contains Search 
  * 5  Triggers 
    * 5.1  Syntax 
    * 5.2  OB Conventions 
      * 5.2.1  Exceptions and messages 
      * 5.2.2  Oracle's laziness 
      * 5.2.3  Soft disabling 
      * 5.2.4  Object returning 

  
---  
  
##  Introduction

Both check constraints and triggers are objects defined physically in
database. This document will not explain the basis for triggers and
constraints but just the particularities Openbravo ERP has in their usage.

##  Naming

When adding a check constraint, triggers and indexes modularity naming rules
have to be taken into account. This because triggers and indexes are global
objects for a database. The modularity naming rule is as follows: the
constraint /index/trigger name must start with the DB Prefix of the module the
constraint belongs to. For instance, _MYMODULEDBPREFIX_CONSTRAINTNAME_ .

In the case of indexes and constraints, if the index/constraint is added to a
table of another module then an additional _EM__ prefix is required:
_EM_MYMODULEDBPREFIX_CONSTRAINTNAME_ .

By following this naming rule the index/trigger/constraint is exported to the
module directory and packaged with the module.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  The name
of the constraints and triggers must not exceed the 30 characters as the
maximum length of an object name in oracle is 30 characters.  
---|---  
  
##  Constraints

Check constraints do not have any particularity in Openbravo, except how they
should be named and how the back-end treats them to show messages.

A step by step HowTo on _How to add a Constraint_ can be found:  here

###  Messages

It is possible to define a message to be shown when the rule defined by the
constraint is not satisfied. How to do that is explained in the  Messages
documentation.

###  Backwards compatibility

Modules should allow compatibility for other ones built on top of them at
least between minor versions, additionally there could be user data already in
the application if it is in a productive environment. This means that user
data or other module's could rely in the current database model and in case a
new constraint is added or an existent one is modified to be more restrictive
than it was, backwards compatibility could be broken. Therefore it should be
avoided to add new constraints or to modify existent ones to make them more
restrictive during between versions.

##  Indexes

###  Operator Classes

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR15Q4  ** .  
---|---  
  
In PostgreSQL  Operator Classes  certain operator classes (text_pattern_ops,
varchar_pattern_ops, and bpchar_pattern_ops) enables using indexes in queries
involving pattern matching expressions. For instance, the following query:

    
    
    SELECT name
    FROM c_bpartner
    WHERE name LIKE 'John%'

would not use an index created like this:

    
    
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (name COLLATE pg_catalog."default");

but would use an index defined with an operator class:

    
    
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (name COLLATE pg_catalog."default" varchar_pattern_ops);

Operator Classes are not needed in Oracle to use an index in the previously
defined query, in that case if the index column defines an operator class, the
operator class will have no effect.

###  Function based indexes

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR15Q4  ** .  
---|---  
  
Openbravo supports the use of functions in indexes. For instance, this, along
with the use of an operator class would enable the use of indexes in case
insensitive queries that use the iStartsWith operator, like this one:

    
    
    SELECT name
    FROM c_bpartner
    WHERE UPPER(name) LIKE 'JOHN%'

The following index could be used by the previous query:

    
    
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (upper(name) COLLATE pg_catalog."default" varchar_pattern_ops);

Any function can be used in the indexes, as long as it is deterministic. Even
needed functions are supported:

    
    
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (UPPER(REPLACE(name, 'a', 'b')));

Until  3.0PR17Q2  only one function expression can be used per index, so the
following index it was not supported, starting from 3.0PR17Q2 it is valid.

    
    
    CREATE INDEX c_bpartner_name_id
      ON c_bpartner
      USING btree
      (UPPER(REPLACE(name, 'a', 'b')),
       UPPER(c_bpartner_id));

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |
Functions used in indexed  must be immutable  . Starting from 3.0PR19Q3, it is
possible to define  custom immutable functions  , previously only built-in
immutable functions could be used in indexes.  
---|---  
  
###  Partial indexes

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR17Q1  ** .  
---|---  
  
PostgreSQL supports the definition of  partial indexes  . A partial index is
an index where it is possible to specify the rows that are indexed. This kind
of indexes are useful for commonly used _WHERE_ conditions that use constant
values.

Thus, with a partial index it is possible to index just the table data that is
most commonly used, helping to reduce the amount of disk space used by the
index.

A partial index can be created as follows:

    
    
    CREATE INDEX a_amortization_active 
      ON a_amortization (isactive)
      WHERE isactive = 'Y';

For the moment Oracle does not support the creation of partial indexes in a
explicit way. For this reason, if a partial index is found in the Openbravo
XML model when using an Oracle database, the partial index definition will not
be taken into account and it will be created as a regular index.

####  Not Null Partial Indexes On Nullable Columns

In an Oracle database, it does not include rows in an index if the indexed
columns are NULL. That means that for the case where we are indexing a
nullable foreign key column **every index is a partial index** .

This is **not** the behavior in PostgresSQL databases, where we will need to
define the index as partial to get the same behavior. For example:

    
    
    CREATE INDEX c_order_return_reason 
      ON c_order (c_return_reason_id)
      WHERE c_return_reason_id IS NOT NULL;

###  Indexes for Contains Search

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR17Q2  ** .  
---|---  
  
The indexes for _contains_ search, are those intended to provide fast
searching of sub-strings within the values stored in a particular database
column.

In PostgresSQL we can define a **contains** search index as follows:

    
    
    CREATE INDEX c_bpartner_value_basic ON c_bpartner USING gin (value gin_trgm_ops);

Note that to define this kind of indexes we have to make use of the **` gin `
** access method together with the **` gin_trgm_ops ` ** operator class for
the indexed column. Both elements are available thanks to the  pg_trgm
extension which is included in Openbravo distribution by default.

Besides, this feature allows to define a  function based index  to improve
**icontains** (case insensitive) searching:

    
    
    CREATE INDEX c_bpartner_value_basic ON c_bpartner USING gin (UPPER(value) gin_trgm_ops);

For the moment, this kind of indexes are **not** supported in Oracle: if they
are present in the XML model, they will be created as regular indexes in the
database.

##  Triggers

A step by step HowTo on _How to add a Trigger_ can be found:  here

###  Syntax

Triggers, as the rest of PL code in Openbravo ERP, should be written following
some restrictions in order to make them compatible between PostgreSQL and
Oracle and to make it possible to correctly export and import them using
DBSourceManager  . These rules are detailed in the  PL-SQL code rules
document.

###  OB Conventions

####  Exceptions and messages

Triggers can raise exceptions (it is the common practice to abort a
transaction), the back-end captures that exception in order to show a proper
message. Read in the  messags documentation  how to do it.

####  Oracle's laziness

Whereas oracle evaluates expressions in a lazy manner PostgreSQL does not do
so. This specially important for triggers that are for _insert_ and _delete_
because in the first case there are :new variables and in the second one there
are :old ones, so when writing if clauses (even in Oracle if we want to do
compatible code) this must be taken into account writing two clauses instead
of just one.

####  Soft disabling

All triggers in Openbravo ERP must be able to be disabled softly. This means
not disabling it in database but just in a logic way. This is used by DAL when
it is importing data: triggers must be disabled in order to allow data
imporation without triggering them, but that only should affect to the session
that it is executing the importation. To add this capability to triggers, the
first lines of each of them should look like:

In Oracle

    
    
     
        IF AD_isTriggerEnabled()='N' THEN 
          RETURN;
        END IF;

In PostgreSQL

    
    
     
         IF AD_isTriggerEnabled()='N' THEN
            IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;
         END IF;

####  Object returning

PostgreSQL trigger function must explicitly take care of returning the trigger
object, also depending on the type of the trigger. This means that the last
line of the trigger function must be something like:

    
    
     
         IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;

Retrieved from "  http://wiki.openbravo.com/wiki/Constraints_and_Triggers  "

This page has been accessed 9,431 times. This page was last modified on 2
April 2019, at 07:59. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

