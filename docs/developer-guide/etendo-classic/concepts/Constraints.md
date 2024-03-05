---
tags: 
  - constrains
  - indexes
  - naming
  - modularity
  - messages
---


## Overview

Both check constraints and triggers are objects defined physically in database. This document will not explain the basis for constraints but just the particularities Etendo Classic has in their usage.

##  Naming

When adding a check constraint, triggers and indexes modularity naming rules have to be taken into account. This is necessary because triggers and indexes are global objects for a database. 

The modularity naming rule is as follows: 
the constraint, index or trigger name must start with the DB Prefix of the module the constraint belongs to. 

For instance,`MYMODULEDBPREFIX_CONSTRAINTNAME`.

In the case of indexes and constraints, if the index/constraint is added to a
table of another module then an additional `EM_` prefix is required:

`EM_MYMODULEDBPREFIX_CONSTRAINTNAME`.

By following this naming rule, the index/trigger/constraint is exported to the
module directory and packaged with the module.

!!!info
    The name of the constraints must not exceed the 30 characters as the maximum length of an object name in oracle is 30 characters.  

##  Constraints

Check constraints do not have any particularity in Etendo, except for how they should be named and how the back-end treats them to show messages.

!!!info
    For more information, read [How to add a Constraint](../how-to-guides/How_to_add_a_Constraint.md).

###  Messages

It is possible to define a message to be shown when the rule defined by the constraint is not satisfied. 

!!!info
    How to do that is explained in the [Messages](Messages.md#checks) documentation.

###  Backwards compatibility

Modules should allow compatibility for other ones built on top of them at least between minor versions, additionally there could be user data already in the application if it is in a productive environment. 
This means that user data or other module's could rely on the current database model and in case a new constraint is added or an existent one is modified to be more restrictive
than it was, backwards compatibility could be broken. Therefore, it should be avoided to add new constraints or to modify existent ones to make them more restrictive during between versions.

##  Indexes

###  Operator Classes

  
In PostgreSQL [Operator Classes](https://www.postgresql.org/docs/9.3/indexes-opclass.html){target="\_blank"} certain operator classes (`text_pattern_ops`,
`varchar_pattern_ops`, and `bpchar_pattern_ops`) enables using indexes in queries
involving pattern matching expressions. For instance, the following query:

    
```sql   
    SELECT name
    FROM c_bpartner
    WHERE name LIKE 'John%'
```
would not use an index created like this:

    
```sql   
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (name COLLATE pg_catalog."default");
```

but would use an index defined with an operator class:

    
```sql 
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (name COLLATE pg_catalog."default" varchar_pattern_ops);
```

Operator Classes are not needed in Oracle to use an index in the previously defined query, in that case if the index column defines an operator class, the operator class will have no effect.

###  Function based indexes

  
Etendo  supports the use of functions in indexes. For instance, this along with the use of an operator class, would enable the use of indexes in case insensitive queries that use the iStartsWith operator, like this one:

    
```sql
    SELECT name
    FROM c_bpartner
    WHERE UPPER(name) LIKE 'JOHN%'
```

The following index could be used by the previous query:

    
```sql
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (upper(name) COLLATE pg_catalog."default" varchar_pattern_ops);
```

Any function can be used in the indexes, as long as it is deterministic. Even
needed functions are supported:

    
```sql 
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (UPPER(REPLACE(name, 'a', 'b')));
```
The following index can also be used.

    
```sql
    CREATE INDEX c_bpartner_name_id
      ON c_bpartner
      USING btree
      (UPPER(REPLACE(name, 'a', 'b')),
       UPPER(c_bpartner_id));
```


  
###  Partial indexes
  
`PostgreSQL` supports the definition of [partial indexes](https://www.postgresql.org/docs/9.3/indexes-partial.html){target="\_blank"}. A partial index is an index where it is possible to specify the rows that are indexed. This kind of indexes are useful for commonly used _WHERE_ conditions that use constant values.

Thus, with a partial index it is possible to index just the table data that is most commonly used, helping to reduce the amount of disk space used by the index.

A partial index can be created as follows:

    
```sql
    CREATE INDEX a_amortization_active 
      ON a_amortization (isactive)
      WHERE isactive = 'Y';
```

Oracle does not support the creation of partial indexes in an explicit way yet. For this reason, if a partial index is found in the Etendo XML model when using an Oracle database, the partial index definition is not taken into account and it is created as a regular index.
  
####  Not Null Partial Indexes On Nullable Columns

In an Oracle database, it does not include rows in an index if the indexed columns are NULL. That means that for the case where we are indexing a nullable foreign key column every index is a partial index.

This is not the behavior in `PostgreSQL databases`, where we will need to define the index as partial to get the same behavior. For example:

    
```sql 
    CREATE INDEX c_order_return_reason 
      ON c_order (c_return_reason_id)
      WHERE c_return_reason_id IS NOT NULL;
```

###  Indexes for Contains Search

  
The indexes for *contains* search are those intended to provide fast searching of sub-strings within the values stored in a particular database column.

In PostgresSQL we can define a contains search index as follows:

    
```sql
    CREATE INDEX c_bpartner_value_basic ON c_bpartner USING gin (value gin_trgm_ops);
```

!!!note
    To define this kind of indexes, we have to make use of the ` gin `
    access method together with the ` gin_trgm_ops ` operator class for
    the indexed column. Both elements are available thanks to the ` pg_trgm `
    extension which is included in Etendo distribution by default.

Besides, this feature allows defining a [function based index](#function-based-indexes) to improve icontains (case-insensitive) searching:

    
```sql
    `CREATE INDEX c_bpartner_value_basic ON c_bpartner USING gin (UPPER(value) gin_trgm_ops);`
```

!!!info
    This kind of indexes are not supported in Oracle yet: if they are present in the XML model, they will be created as regular indexes in the database.


This work is a derivative of [Constraints_and_Triggers](http://wiki.openbravo.com/wiki/Constraints_and_Triggers){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 