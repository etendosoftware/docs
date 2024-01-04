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

  

#  How To Create a Trigger

**Languages:** |

****English** ** |  Translate this article...  
  
---|---  
  
##  Contents

  * 1  Objective 
  * 2  Module 
  * 3  Adding the Trigger to Database 
  * 4  Adding translatable message 
  * 5  Oracle vs Postgres 
  * 6  Exporting Triggers as Part of the Module 

  
---  
  
##  Objective

Within this howto article we will use the _HT_Salary_ table created in the
How to Create a Table  howto. Once we have that table created we want to
**ensure that salaries can only be entered within business partners that are
marked as Employees** and not other ones. The system must prevent us from
entering salary information for business partners that are only marked as
customers or vendors.

This constraint cannot be defined as a database check constraint because it
requires a SQL query which is not allowed within checks. To implement this
constraint a trigger must be used. A trigger is a piece of code that is
executed whenever a table is modified (on INSERT, UPDATE and/or DELETE
events).

The generic documentation about Triggers in Openbravo can be found  here  .

##  Module

All new developments must belong to a  module  that is not the _core_ module.
Please follow the  How to create and package a module  section to create a new
module.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Note the **DB Prefix** defined there is **HT** which will explicitely indicate
the prefix of our new trigger! Through this prefix, Openbravo will know to
package this trigger along with the howto module.  
---|---  
  
  

##  Adding the Trigger to Database

Triggers do not require any description within the application dictionary.
They only need to be added to the database, following the DB Prefix rule that
indicates which module they belong to.

Let's first add the trigger to the database and we'll comment on it
afterwards. Note that the actual SQL code varies depending on the database
engine used, Postgres or Oracle. Here is an example for both:

**Oracle**

    
    
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

**Postgres**

    
    
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

Rough breakdown of the structure from beginning to end is:

  * **Trigger name** The name of the trigger follows the modularity naming conventions, so if we want to include the trigger in our module for which DBprefix is HT, the trigger will start with HT. In this case its name is _HT_SALARY_TRG_ . 
  * **When it is executed and for which table.** After the trigger name we define when the trigger is going to be executed. In this case we define that it will be raised each time there is an insertion or update on our _HT_SALARY_ table. Notice the difference between Oracle and Postgres. 
  * **Define variables** Define the local variables you require - in this case we only need one variable to store the flag if the partner is an employee or not. 
  * **Enable soft trigger disable** . This code enables the soft trigger disable, which is used to disable all triggers in the application within a particular session in Oracle: 

    
    
        IF AD_isTriggerEnabled()='N' THEN 
          RETURN;
        END IF;
    

You should use this code if you are working with PostgreSQL:

    
    
        IF AD_isTriggerEnabled()='N' THEN
           IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;
        END IF;
    

  * **Select if it is an employee** . The following saves the flag IsEmployee to a local variable that indicates if the current record is an employee or not. Note that to get the values in the current record we can use the _:New.C_BPartner_ID_ variable, in case it is an update (not an insert) there is also an _:Old_ set of variables with the old values before the update takes place. 

    
    
        SELECT IsEmployee
          INTO v_IsEmployee
          FROM C_BPartner
         WHERE C_BPartner_ID = **:new.C_BPartner_ID** ;
    

  * **Raise an error if it is not correct and rollback the transaction** . Once we have the _v_IsEmployee_ we can check whether it is employee or not, and in case it is not raise an error and abort the transaction. Note that whenever a trigger raises an error the transaction is rolled back. There is a restriction with modularity here. Oracle allows a range of error codes from -20000 to -20999 for custom message, but modules cannot define custom messages in application dictionary because they cannot follow the naming rules. So when raising an error in a trigger within a module it must use one of the existing codes (and to emphasize that no special code is used -20000 should be used always), but the message shown in the UI will not be as useful as if it were created specifically for this case. 

    
    
       IF v_IsEmployee = 'N' THEN
         RAISE_APPLICATION_ERROR(-20000, '@HT_SALARY_NOT_EMPLOYEE@');
       END IF;
    

  * To export properly a RAISE EXCEPTION from postgresql to xml files you have to add the following comment at the end of the command; --OBTG:-20000-- 

    
    
    RAISE EXCEPTION '%', '@HT_SALARY_NOT_EMPLOYEE@' ; --OBTG:-20000--
    

  * **Return the correct version of the object** in case of **Postgres** where a trigger consists of a function plus a trigger assignment 

    
    
       IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;
    

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Note: If one needs to set/change the values of the record that is being
updated/inserted within the trigger, the _**BEFORE** INSERT OR UPDATE _
statement MUST be used instead of the _**AFTER** INSERT OR UPDATE _ .  
---|---  
  
##  Adding translatable message

In the trigger created above the message text shown for the user is not
hardcoded but rather just a name of an  Message  entry from the _Application
Dictionary_ . Defining the message this way allows adding translations for the
message for different languages.

Details on how to create a new Message entry can be found  here  .

As a short summary:

In the **Application Dictionary || Message** window create a new record using
the following details:

  * **Module** _Openbravo Howtos_ as this is the module containing the constraint also. 
  * **Search key** : **HT_SALARY_NOT_EMPLOYEE** as this is the value we use to lookup the message in the trigger. 

  * **Message type** : Depending on the type the UI for the message box will be different (green for success, yellow for warning...), in our case we want a red error message box, so we select _Error_ . 
  * **Message text** : It is the user friendly message that will be displayed inside the message box. So let's enter: _Cannot add salary for non-employee._ . 

##  Oracle vs Postgres

Writing triggers for Postgres or Oracle is somewhat different so let's
describe the main differences:

  * trigger's in Postgres are functions that return a trigger object associated with a table for a specific action (INSERT, UPDATE or/and DELETE). In Oracle, their definition is slightly simpler. Hence there are two CREATE statements required in Postgres (one for the function and one for assigning the function as the trigger of a table) versus one in Oracle. 
  * the use of NEW/OLD reserved words to reference the new record (that is being inserted or updated to) or the old one (that is being deleted or updated) is different (:NEW in Oracle vs NEW in Postgres) 
  * Postgres trigger function must explicitly take care of returning the trigger object, also depending on the type of the trigger (e.g. the last line is IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF; ) 

For more details on database differences, please see the following  article  .

##  Exporting Triggers as Part of the Module

Whenever application dictionary or physical database is modified, it is
possible to export that information to xml files belonging to the specific
module. This way you can maintain Openbravo ERP database data as source code
XML files (that can then be source controlled).

To do so, execute:

    
    
     ant export.database
    

This will **export all artifacts of the module currently marked as In
Development** within the application dictionary.

For further explanations read the  Development tasks document  .

Retrieved from "  http://wiki.openbravo.com/wiki/How_To_Create_a_Trigger  "

This page has been accessed 15,918 times. This page was last modified on 26
June 2013, at 08:50. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

