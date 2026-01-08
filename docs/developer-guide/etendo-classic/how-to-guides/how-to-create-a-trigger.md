---
title: How to Create a Trigger
tags: 
    - Data Integrity
    - Triggers
    - Modular Customization
    - PostgreSQL 
    - Oracle
status: beta
---

# How to Create a Trigger

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

## Overview

This section builds on the `HT_Salary` table created in the [How to Create a Table](../how-to-guides/how-to-create-a-table.md) guide and explains how to enforce a business rule at the database level: salary records can only be assigned to business partners marked as Employees. The system must therefore prevent the entry of salary information for business partners defined solely as customers or vendors.

Because this rule depends on querying related data, it cannot be implemented using a standard database check constraint. Instead, it is enforced using a **database trigger**, which is code that automatically executes when the table is modified through **INSERT, UPDATE, or DELETE** operations.

!!!info
    For more information about Triggers visit, [Constraints](../concepts/constraints.md).

## Module

All new developments must belong to a module that is not the **core** module.

!!!info
    Follow the [How to create a module](../how-to-guides/how-to-create-a-module.md) section to create a new module.


## Adding the Trigger to Database

Triggers do not require any description within the application dictionary. They only need to be added to the **database**, following the `DB Prefix` rule that indicates which module they belong to.

Let's first add the trigger to the database and comment on it afterwards. Note that the actual **SQL code** varies depending on the database engine used, **Postgres or Oracle**. Here is an example for both:

``` SQL title="Oracle"
        
    CREATE OR REPLACE TRIGGER ht_salary_trg
    AFTER INSERT OR UPDATE
    ON ht_salary FOR EACH ROW
    
    DECLARE
        v_IsEmployee CHAR(1);
        
    BEGIN
            
        IF AD_isTriggerEnabled()='N' THEN 
            RETURN;
        END IF;

        SELECT IsEmployee
            INTO v_IsEmployee
            FROM C_BPartner
        WHERE C_BPartner_ID = :new.C_BPartner_ID;
    
        IF v_IsEmployee = 'N' THEN
            RAISE_APPLICATION_ERROR(-20000, '@HT_SALARY_NOT_EMPLOYEE@');
        END IF;
    
    END ht_salary_trg;
```


```SQL title="Postgres"        

    CREATE OR REPLACE FUNCTION ht_salary_trg()
        RETURNS TRIGGER AS
    $BODY$ DECLARE 
    
    DECLARE
        v_IsEmployee CHAR(1);
    
    BEGIN
    
        IF AD_isTriggerEnabled()='N' THEN IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF; 
        END IF;
    
        SELECT IsEmployee
            INTO v_IsEmployee
            FROM C_BPartner
        WHERE C_BPartner_ID = NEW.C_BPartner_ID;
        
        IF v_IsEmployee = 'N' THEN
            RAISE EXCEPTION '%', '@HT_SALARY_NOT_EMPLOYEE@'; --OBTG:-20000--
        END IF;
    
        IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF; 
    
    END; 
    $BODY$ LANGUAGE plpgsql;
    
    CREATE TRIGGER ht_salary_trg AFTER INSERT OR UPDATE ON ht_salary
            FOR EACH ROW EXECUTE PROCEDURE ht_salary_trg();
```

Rough breakdown of the structure from beginning to end is:

- **Trigger name**: The name of the trigger follows the modularity naming conventions, so if we want to include the trigger in our module for which `DBprefix` is **HT**, the trigger will start with **HT**. In this case, its name is `HT_SALARY_TRG`. 
- **When it is executed and for which table**: After the trigger name, define when the trigger is going to be executed. In this case, define that it will be raised each time there is an insertion or update on our `HT_SALARY` table. Notice the difference between Oracle and Postgres. 
- **Define variables**: Define the local variables you require, in this case we only need one variable to store the flag if the partner is an employee or not. 
- **Enable soft trigger disable**: This code enables the soft trigger disable, which is used to disable all triggers in the application within a particular session:

     
    ``` SQL title="Oracle"
    IF AD_isTriggerEnabled()='N' THEN 
        RETURN;
    END IF;
    ```

    ```SQL title="Postgres"    
    IF AD_isTriggerEnabled()='N' THEN
        IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;
    END IF;
    ```
        

- **Select if it is an employee**: The following saves the flag `IsEmployee` to a local variable that indicates if the current record is an employee or not. Note that to get the values in the current record we can use the `:New.C_BPartner_ID` variable, in case it is an update (not an insert) there is also an `:Old` set of variables with the old values before the update takes place. 

        
    ```SQL           
        SELECT IsEmployee
        INTO v_IsEmployee
        FROM C_BPartner
        WHERE C_BPartner_ID = :new.C_BPartner_ID;
    ```
        

- **Raise an error if it is not correct and rollback the transaction**: Once we have the `v_IsEmployee` we can check whether it is employee or not, and in case it is not raise an error and abort the transaction. 

    !!!note
        Whenever a trigger raises an error the transaction is rolled back. There is a restriction with modularity here. Oracle allows a range of error codes from -20000 to -20999 for custom messages, but modules cannot define custom messages in application dictionary because they cannot follow the naming rules. So, when raising an error in a trigger within a module it must use one of the existing codes (and to emphasize that no special code is used -20000 should be used always), but the messages shown in the UI will not be as useful as if it were created specifically for this case. 

        ``` sql
        IF v_IsEmployee = 'N' THEN RAISE_APPLICATION_ERROR(-20000, '@HT_SALARY_NOT_EMPLOYEE@');END IF;
        ```

        

- To export properly a **RAISE EXCEPTION** from `postgresql` to `xml` files you have to add the following comment at the end of the command;        `--OBTG:-20000--`. 

    ``` SQL     
    RAISE EXCEPTION '%', '@HT_SALARY_NOT_EMPLOYEE@' ; --OBTG:-20000--
    ```    

- **Return the correct version of the object** in case of **Postgres** where a trigger consists of a function plus a trigger assignment. 

    ``` SQL 
    IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;
    ```
        

    !!! note
        If one needs to set/change the values of the record that is being updated/inserted within the trigger, the **BEFORE** INSERT OR UPDATE statement MUST be used instead of the **AFTER** INSERT OR UPDATE.  
 
    
## Adding Translatable Message

In the trigger created above the message text shown for the user is not **hardcoded** but rather just a name of a Message entry from the **Application Dictionary**. Defining the message this way, allows adding translations for the message for different languages.

!!!info
    For more information visit, [Messages](../concepts/messages.md). 

As a short summary:

In the `Application Dictionary > Message` window create a new record. 

Fields to note: 

- **Module**: `Etendo Howto` as this is the module containing the constraint. 
- **Search key**: `HT_SALARY_NOT_EMPLOYEE` as this is the value used to lookup the message in the trigger. 
- **Message type**: Depending on the type, the UI for the message box will be different (green for success, yellow for warning...), in our case we want a red error message box, so select **Error**. 
- **Message text**: It is the user friendly message that will be displayed inside the message box. So let's enter: **Cannot add salary for non-employee**. 

## Oracle vs Postgres

Writing triggers for **Postgres or Oracle** is somewhat different, so let's describe the main differences:

- **Trigger's in Postgres** are functions that return a trigger object associated with a table for a specific action (INSERT, UPDATE or/and DELETE). In **Oracle**, their definition is slightly simpler. Hence, there are two CREATE statements required in Postgres (one for the function and one for assigning the function as the trigger of a table) versus one in Oracle. 
- The use of **NEW/OLD** reserved words to reference the new record (that is being inserted or updated to) or the old one (that is being deleted or updated) is different (`:NEW` in Oracle vs `NEW` in Postgres). 
- **Postgres trigger function** must explicitly take care of returning the trigger object, also depending on the type of the trigger (e.g. the last line is `IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;`). 



## Exporting Triggers as Part of the Module

Whenever application dictionary or physical database is modified, it is possible to **export** that information to **xml files** belonging to the specific module. This way, it is possible to maintain Etendo database data as **source code XML files** that can then be source controlled.

To do so, execute:

        
``` bash title="Terminal"
./gradlew  export.database
```
        

This will export all artifacts of the module currently marked as **In Development** within the application dictionary.

!!!info
    For more information visit, [Development tasks](../developer-tools/etendo-gradle-plugin.md#detailed-build-tasks) documentation.

---
This work is a derivative of [How To Create a Trigger](https://wiki.openbravo.com/wiki/How_To_Create_a_Trigger){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/How_To_Create_a_Trigger){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
    


