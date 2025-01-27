---
tags:
  - How to
  - Etendo classic
  - Create a stored procedure
---

# How to create a Stored Procedure

## How to create a Stored Procedure

Stored procedures are one of the mechanisms Openbravo ERP provides in order to implement business logic. Stored procedures are executed by the database engine and are implemented in the standard PL/pgSQL (for PostgreSQL) or PL/SQL (for Oracle) language. One must understand the particularities about how these PL/SQL procedures are integrated with the rest of the application. It is also necessary to follow some coding rules in order to make it possible to export/import to XML files using DBSourceManager.

This document discusses the Openbravo infrastructure for stored PL/SQL procedures. These act as Processes in the Application Dictionary.

## AD_PInstance and AD_PInstance_Para tables

Before implementing a PL/SQL procedure it is important to understand how it will be called from the application.

When a PL/SQL procedure is called a new record is created inside the _AD_PInstance_ table. This record contains the information about the ID of the record that the PL/SQL procedure was called from (in case the process is invoked from a button inside a window/tab). This record in the _AD_PInstance_ table is also used by the user interface to retrieve and display the resulting message the procedure generates when it completes (error or success).

In case the process has additional parameters entered by the user a new record is created for each of them inside the _AD_PInstance_Para_ table. Each record contains the information related to one of the parameters such as its name (_DB Column name_) and the value the user assigned to it.

Finally, note that the ID of the newly created record in _AD_PInstance_ table is the ONLY parameter passed to the PL/SQL procedure. It is the stored
procedure's responsibility to read the AD_PInstance and AD_PInstance_Para record(s) to obtain any parameters it requires and writes the resulting message back into the _AD_PInstance_ table.

## Procedure definition

The header for a PL/SQL procedure implementing a process looks like:

**PostgreSQL**

```
CREATE OR REPLACE FUNCTION HR_TEST(p_PInstance_ID character varying) RETURNS void
```

**Oracle**

```
CREATE OR REPLACE PROCEDURE HR_TEST(p_PInstance_ID IN VARCHAR2)
```

First of all take a look to the PL/SQL procedure name, it follows the modularity naming rules, this is, it starts with the module's _DBPrefix_.

Note that the only parameter the PL/SQL procedure receives is a string one, it will contain the UUID for the key of the _AD_PInstance_ record generated for its invocation.

## Retrieving parameters

**PostgreSQL** and **Oracle**

```
SELECT 
  Record_ID, 
  CreatedBy
INTO 
  v_Record_ID, 
  v_User_ID
FROM 
  AD_PInstance
WHERE 
  AD_PInstance_ID = p_PInstance_ID;

FOR Cur_Parameter IN 
(
  SELECT 
    p.ParameterName,
    p.P_String,
    p.P_Number,
    p.P_Date
  FROM 
    AD_PInstance_Para p
  WHERE 
    AD_PInstance_ID=p_PInstance_ID
  ORDER BY 
    p.SeqNo
)
LOOP
  IF(Cur_Parameter.ParameterName='DateFrom') THEN
    v_DateFrom:=Cur_Parameter.P_Date;
  ELSIF(Cur_Parameter.ParameterName='Activate') THEN
    v_Activate:=Cur_Parameter.P_String;
  END IF;
END LOOP; -- Get Parameter
```

The snippet of code above is an example of how the parameters can be retrieved.

The first select obtains from _AD_PInstance_ the IDs (UUIDs) for the user that invoked the process and the record ID it was called from. The record ID only makes sense in case the process is called using a button in a tab. In this case this ID identifies the record in the table that the tab with the button is based on. This is used for processes that affect the current record.

Afterwards, a loop obtains all the parameters and iterates only in case the process has parameters defined. Notice that the parameter is identified by _ParameterName_ which matches _DB Column name_ defined in the parameter. Depending on its type the actual value is stored in one of the following columns: `P_String` , `P_Number` or `P_Date` . The stored procedure needs to know what to expect and retrieve it accordingly.

## Updating _AD_PInstance_

_AD_PInstance_ table has a `IsProcessing` column, which indicates whether an instance is currently being processed or not. At the beginning of the process the instance should be set as processing with:

```
AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL);
```

Once the process is finished, the instance should be set again to not processing. Not only that, this instance will be used to display the result of the process which will be shown in the user interface. This is done with:

```
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', v_Result, v_Message);
```

Here the `v_Result` parameter is a numeric value, it can be 0 for error or 1 for success. The `v_Message` is the message that will be shown, for further information about how to manage messages read the section below.

## Managing exceptions

The exceptions in a PL/SQL procedure should be captured in order to insert the proper message in the _PInstance_ table to be correctly displayed to the user. Thus is a good practice to have an _EXCEPTION_ section to catch all the exceptions in the body of the procedure.

This would be a complete procedure with the _EXCEPTION_ section.

**PostgreSQL**

```
CREATE OR REPLACE FUNCTION HR_TEST(p_PInstance_ID character varying)
RETURNS void
$BODY$
  BEGIN
  -- Your code here

  EXCEPTION
  WHEN OTHERS THEN
    v_ResultStr:= '@ERROR=' || SQLERRM;
  RAISE NOTICE '%',v_ResultStr;
  IF(p_PInstance_ID IS NOT NULL) THEN
    PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'N', 0, v_ResultStr);
  END IF;
  RETURN;
  END; 
$BODY$
LANGUAGE 'plpgsql' VOLATILE
```

**Oracle**

```
CREATE OR REPLACE PROCEDURE HR_TEST(p_PInstance_ID IN VARCHAR2)

BEGIN

  -- Your code here

  EXCEPTION
  WHEN OTHERS THEN
    v_ResultStr:= '@ERROR=' || SQLERRM;
  DBMS_OUTPUT.PUT_LINE(v_ResultStr);
  IF(p_PInstance_ID IS NOT NULL) THEN
    ROLLBACK;
    AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'N', 0, v_ResultStr);
  ELSE
    RAISE;
  END IF;
END HR_TEST;
```

As all exceptions in the body are caught to correctly take the message from it and add it to the _PInstance_ setting it to result 0 (error), it is possible to raise custom exceptions when some logical error happens during the execution, because they will also be caught. For example the following piece of code does some checks and in case they fail an exception is thrown.

**PostgreSQL**

```
IF checkFails THEN
  RAISE EXCEPTION '%', '@HR_SomeNiceMessage@';
END IF;
```

**Oracle**

```
IF checkFails THEN
  RAISE_APPLICATION_ERROR(-20000, '@HR_SomeNiceMessage@');
END IF;
```

For further explanations on messages read the Messages documentation.

## Functions

Database functions are also supported.

### Volatility

Functions can define different volatility levels. Note Oracle does not implement any equivalent for stable functions, in case a function is marked in
PostgreSQL as stable, it will be implemented as a standard function in Oracle adding a comment so that the exported xml keeps this information.

PostgreSQL - Oracle equivalences:

| PostgreSQL         | Oracle        |
|--------------------|---------------|
| Volatile (default) | Default       |
| Stable             | N/A           |
| Immutable          | Deterministic |

---
This work is a derivative of [How to Create a Stored Procedure](http://wiki.openbravo.com/wiki/How_to_create_a_Stored_Procedure){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
