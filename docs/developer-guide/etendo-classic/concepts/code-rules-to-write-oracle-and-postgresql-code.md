---
tags: 
  - Oracle
  - PostgreSQL
  - Database Development
  - SQL Standards
  - Translation
  - Cursors
---

#  Code Rules to Write Oracle and Postgresql Code

##  Procedure Language Rules

Etendo supports Oracle and `PostgreSQL` database engines.

!!!info
    Check for the minimum required versions to install Etendo in [Requirements](../../../getting-started/requirements.md).

This is a set of recommendations for **writing Procedure Language** that works on both database backends (when possible) or that can be automatically translated by `DBSourceManager`.

These recommendations assume that code in Oracle is written and that the user wants to port it to `PostgreSQL`. So, many features/constructs are pointed out which Oracle adds on top of the SQL standard and which are thus Oracle
specific and not available in `PostgreSQL`.

To help developers to test if their code can be translated by `dbsourcemanager` the `_ant export.database_ command` contains a **Translation consistency check** which does the complete standardization/translation cycle once and reports differences found (ignoring whitespace).

  
!!!note
      It is strongly recommended to avoid (when possible) using PL/SQL when writing new code and write it using DAL instead.  
  
  
####  General rules

This a list of general rules that assure that PL runs properly on different database backgrounds.

  * JOIN statement. Change the code replacing the (+) by `LEFT JOIN` or `RIGHT JOIN` 
  * In XSQL use a questionmark (?) as parameter placeholder. If it is a `NUMERIC` variable use `TO_NUMBER(?)`. For dates use `TO_DATE(?)`. 
  * Do not use GOTO since `PostgreSQL` does not support it. To get the same functionality that GOTO use boolean control variables and `IF/THEN` statements to check if the conditions are `TRUE/FALSE`. 
  * Replace oracle specific `NVL` commands by `COALESCE`. 
  * Replace oracle specific `DECODE` commands by `CASE`. If the `CASE` is `NULL` the format is: 

    
    
    CASE WHEN variable IS NULL THEN X ELSE Y END
    

If the variable is the result of concatenating several strings () are
required.

  * Replace `SYSDATE` commands by `NOW()` 
  * `PostgreSQL/SQL` standard treat _(empty string) and `NULL` differently. When checking for a null variable special care is required._
  * When a `SELECT` is inside a `FROM` clause a synonym is needed. 

    
    
    SELECT * FROM (SELECT 'X' FROM DUAL) A
    

  * When doing `SELECT` always use `AS`. 

    
    
    SELECT field AS field_name FROM DUAL
    

  * `PostgreSQL` does not support synonyms of tables in `UPDATE`, `INSERT` or `DELETE` operations. 

  * `PostgreSQL` does not support using the table name in the fields to update. 
  * `PostgreSQL` does not support the `DELETE TABLE` command. `DELETE FROM` Table should be used instead. 
  * `PostgreSQL` does not support parameters like '1' in the `ORDER BY` or `GROUP BY` clause. A numeric without quotes can be used. 
  * `PostgreSQL` does not support the `CURRENT OF` clause. An active checking of register to update should be used. 
  * `PostgreSQL` does not support `COMMIT`. It does automatically an explicit `COMMIT` between `BEGIN END` blocks. Throwing an exception produces a `ROLLBACK`. 
  * `PostgreSQL` does not support `SAVEPOINT`. `BEGIN`, `END` and `ROLLBACK` should be used instead to achieve the same functionality. 
  * `PostgreSQL` does not support `CONNECT`. 
  * Both Oracle and `PostgreSQL` do not support using variable names that match column table names. For example, use `v_IsProcessing` instead of `IsProcessing`. 
  * `PostgreSQL` does not support `EXECUTE IMMEDIATE` ... `USING`. The same functionality can be achieved using `SELECT` and replacing the variables with parameters manually. 
  * `PostgreSQL` requires () in calls to functions without parameters. 
  * DBMS_OUTPUT should be done in a single line to enable the automatic translator building the comment. 
  * In `PostgreSQL` any string concatenated to a `NULL` string generates a `NULL` string as result. It is is recommended to use a `COALESCE` or initialize the variable to ''. 

!!!note
      In Oracle null||'a' will return 'a' but in PostgrSQL null, so the solution would be coalesce(null,'')||'a' that will return the same for both. But if the we are working with Oracle's NVarchar type this will cause an ORA-12704: character set mismatch error, to fix it it is possible to use coalesce(to_char(myNVarCharVariable), _)||'a'._


  * Instead of doing 

    

    COALESCE(variable_integer, _)_
    

do

    
    
    COALESCE(variable_integer, 0)
    

to guarantee that it will also work in `PostgreSQL`.

  * `PostgreSQL` does the `SELECT FOR UPDATE` at a table level while Oracle does it at a column level. 
  * `PostgreSQL` does not support `INSTR` command with three parameters. `SUBSTR` should be used instead. 
  * `PostgreSQL/SQL` standard count characters in `SUBSTR` starting from 1. Oracle allows `SUBSTR(text, 0, Y)` also and treats its like `SUBSTR(text, 1, Y)`. If you use this form fix it to use 1 as start character instead of 0 to guarantee that it works in both databases. 
  * `PostgreSQL` does not support labels like <<LABEL>> (but it can be commented out). 
  * In dates comparisons is often needed a default date when the reference is null, **January 1, 1900** or **December 31, 9999** should be used. 
  * When is specified a **date as a literal** it is necessary to use **always** the to_date function **with** the correspondent **format mask** . 

    
    
    `RIGHT: COALESCE(movementdate, TO_DATE('01-01-1900', 'DD-MM-YYYY'))`
    

  

#####  Cursors

There are two different ways of using cursors: in `FETCH` clauses and in `FOR` loops. For `FETCH` cursor type no changes are required (except for `%ISOPEN` and `%NOTFOUND` methods that are explained below).

Oracle `FETCH` cursor declarations:

    
    
    CURSOR	Cur_SR IS
    

should be translated in `PostgreSQL` into:

    
    
    DECLARE Cur_SR CURSOR FOR
    

For cursors in FOR loops the format suggested is:

    
    
    TYPE RECORD IS REF CURSOR;
    	Cur_Name RECORD;
    

that is both accepted by Oracle and `PostgreSQL`.

  

#####  Arrays

!!!info
      Currently Arrays are not supported by dbsourcemanager so cannot be used in PL-SQL code.  

  
In Oracle, arrays are defined in the following way:

    
    
    TYPE ArrayPesos IS VARRAY(10) OF INTEGER;
      v_pesos ArrayPesos;
    v_dc2 := v_dc2 + v_pesos(v_contador)*v_digito;
    

but in `PostgresSQL` they are defined as:

    
    
    v_pesos integer[];
    v_dc2 := v_dc2 + v_pesos[v_contador]*v_digito;
    

#####  ROWNUM

To limit the number of registers that a `SELECT` command returns, a cursor needs to be created and read the registers from there. The code could be similar to:

    
    
    --Initialize counter
    v_counter := initial_value;
    --Create the cursor
    FOR CUR_ROWNUM IN (SELECT CLAUSE)
    LOOP
      -- Some sentences
      --Increment the counter
      v_counter := v_counter + 1;
      --Validate condition
      IF (v_counter = condition_value) THEN
        EXIT;
      END IF;
    END LOOP;
    

  

#####  %ROWCOUNT

`SQL%ROWCOUNT` cannot be used directly in `PostgreSQL`. To convert the `SQL%ROWCOUNT` into `PostgreSQL` its value should be defined in a variable. For example:

    
    
    GET DIAGNOSTICS rowcount := ROW_COUNT;
    

In place of `SQL%ROWCOUNT` the previously declared variable should be used.

  

#####  %ISOPEN, %NOTFOUND

`PostgreSQL` cursors do not support `%ISOPEN` or `%NOTFOUND`. To address this problem `%ISOPEN` can be replaced by a boolean variable declared internally in the procedure and is updated manually when the cursor is opened or closed.

  

#####  Formating code

  * To export properly a `RAISE NOTICE` from `postgresql` to `xml` files you have to follow this syntax: 

    
    
    `RAISE NOTICE '%', '@Message@'` ;
    

  * To export properly a `RAISE EXCEPTION` from `postgresql` to `xml` files you have to add the following comment at the end of the command; `--OBTG:-20000--` 

    
    
    `RAISE EXCEPTION '%', '@Message@' ; --OBTG:-20000--`
    

  * In a IF clause is very important to indent the lines within the IF. 

    
    
     `IF (CONDITION) COMMAND; END IF` ;
    

  * The functions with output parameters have to be invoked with select * into. 

    
    
     `SELECT * into VAR from FUNCTION()`;
    

  * The end of the functions have to be defined as following to be exported properly: 

    
    
     `END ; $BODY$ LANGUAGE 'plpgsql' VOLATILE COST 100` ;
    

  * The cast used by `postgresql` is not supported by `Dbsourcemanager`. Instead of using :: type, use a function to convert the value 

    
    
      `:: interval -> to_interval(,) :: double precision -> to_number()`
    

#####  Elements not supported by dbsource manager

  * Functions that return **set of tablename** 
  * Functions that return and array 
  * Functions using regular expresions 
  * Column with type not included on the table. 

!!!info
    For more information, see [Tables](Tables.md#supported-column-data-types).

####  Functions

`PERFORM` and `SELECT` are the two commands that allow calling a function. Since `PostgreSQL` does not accept default function parameters, we define an overloaded function with default parameters.

To allow the automatic translator to do its job the following recommendations should be followed:

  * The AS and the IS should not contain spaces to the left 
  * The function name should not be quoted 
  * In functions, the END should go at the beginning of the line without any spaces to the left and with the function name. 

  

####  Procedures

There are two ways of invoking procedures from `PosgreSQL`:

  * Using the format `variable_name` : `= Procedure_Name(...)`; 
  * Using a `SELECT`. This is the method used for procedures that return more than one parameter. 

  

####  Views

`PostgreSQL` does not support update for the views. If there is the need of updating a view a set of rules should be created for the views that need to be updated.

In `PostgreSQL` there are no table/views `USER_TABLES` or `USER_TAB_COLUMNS`. They should be created from `PostgreSQL` specific tables like `pg_class` or `pg_attribute`.

  

####  Triggers

Rules that the triggers should follow:

  * As general rule, is not desirable to modify child columns in a trigger of the parent table, because it is very usual that child trigger have to consult data from parent table, originating a **mutating table error**. 
  * The name should not be quoted (") because `PostgreSQL` interprets it literally. 
  * All the triggers have a `DECLARE` before the legal notice. In `PostgreSQL` it is necessary to do a function declaration first and then the trigger's declaration that executes the function. 
  * `PostgreSQL` does not support the OF ..(columns).. ON Table definition. It is necessary to include the checking inside the trigger. 
  * `PostgreSQL` does not support lazy evaluation. For example, the following sentence works in Oracle but not in `PostgreSQL`: 

    
    
    `IF INSERTING OR (UPDATING AND :OLD.FIELD = _) THEN_`
    

The correct way of expressing this is:

    
    
    IF INSERTING THEN   
     ... IF UPDATING THEN   
     IF :OLD.NAME = _THEN_
    

  * Triggers in `PostgreSQL` always return something. Depending on the type of operation it returns `OLD (DELETE)` or `NEW (INSERT/UPDATE)`. It should be placed at the end of the trigger and before the exceptions if there are any. 

If you are using the automatic translator consider that:

  * The last `EXCEPTION` in the trigger should not have spaces to its left. The translator considers this the last exception and uses it to setup the right return value. 
  * The last `END` should not have spaces to its left. The indentation is used to determine where function ends. 
  * Beware that if you add an statement like `IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;` just before the `EXCEPTION` statement, it might be removed by the automatic translator. 



This work is a derivative of [PL-SQL code rules to write Oracle and Postgresql code](http://wiki.openbravo.com/wiki/PL-SQL_code_rules_to_write_Oracle_and_Postgresql_code){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

