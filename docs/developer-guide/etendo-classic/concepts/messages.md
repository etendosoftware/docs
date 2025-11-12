---
title: Messages
tags:
    - Messages 
    - Types
    - Information
    - Success
    - Failure
    - Warning

status: beta
---

#  Messages

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

Messages are used to display information to the user, they are typically shown when a process is completed or when an event occurs (for example an error).

##  Types of messages

The different types of messages that can be shown with Openbravo are:

* Success messages 
* Failure messages 
* Warning messages 
* Information messages 

###  Success messages

These messages will be shown after the execution of a process in case of success.

![](/assets/developer-guide/etendo-classic/concepts/Messages-0.png){: .legacy-image-style}

###  Failure messages

These messages will be shown after the execution of a process in case of error.

![](/assets/developer-guide/etendo-classic/concepts/Messages-1.png){: .legacy-image-style}

###  Warning messages

These messages will be shown when certain conditions have to be taken into account by the user, as for example a message indicating that there are still some actions to be processed, etc.

![](/assets/developer-guide/etendo-classic/concepts/Messages-2.png){: .legacy-image-style}

###  Information messages

These messages will be shown in order to communicate any information to the user, as for example the functionality of the window, etc.

![](/assets/developer-guide/etendo-classic/concepts/Messages-3.png){: .legacy-image-style}

##  Application Dictionary definition

All messages are maintained in the **Application Dictionary || Message** window ( _ AD_Message table  _ ). Basically a message consists of a _Search Key_ or value, a _Message Type_ which sets the type of message - the look of the displayed message (as described in the previous section) depends on that - and a _Message Text_ containing the text that will be displayed within the box. Additionally, messages can be translated to different languages. To add
translations to a message use the **Translation** tab.

The _Search Key_ field is a unique identifier for the message, it is not displayed to the user but it is used internally to identify the message. Thus, for example, when a java class needs to show a message it is the search key value used to select the message.

The Search Key field follows the modularity naming rules. Therefore, it has to start with the module dbprefix, followed by a "_". So a correct value for a message in the org.openbravo.client.application module would be _OBUIAPP_MyMessage_

##  Message usage

Depending on the object raising the message, some different considerations must be taken into account.

###  Database

####  Processes

As explained in the PL/SQL processes section of this guide, the final result as well as the message to be shown to the user from a PL process is stored in the _ AD_PInstance record  _ that was used to invoke it.

This message can be a static string which will be displayed as is in UI:
 
```     
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', 1, 'Show this static text');
```

This kind of message does not make use of the messages defined in _Message_ window. To use them it is necessary to set the message identifier ( _Search key Value_ ) surrounded by _at_ symbols (@):

    
```     
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', 1, '@HR_MyMessage1@');
```
  
In the line above when the process is finished the application will try to find a message which value is _HR_Message1_ and it will display the text it contains. Note that as messages are translatable, if user is logged in the application with one of the languages the message has been translated to, they will see the text in that language.

Furthermore, it is possible to combine more than one message and static text.
For example:
 
```     
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', 1, '@Success@, 5 @LinesCreated@');
```

This message will concatenate the text in message with identifier _Success_ with the static text ', 5 ' and with the text for message _LinesCreated_.

All exceptions raised by processes should be caught to manage them and insert a proper message in _PInstance_

####  Exceptions

Exceptions are specially useful for triggers, when an exception is raised within a trigger the current transaction is rolled back. This allows to do some checks before updating or inserting a row in a table and in case some verifications are not satisfied an exception can be raised provoking the row not to be inserted/updated.

**Oracle**

Oracle identifies each error by a numeric code, range between -20000 and -20999 belongs to custom errors, and using the RAISE_APPLICATION_ERROR procedure they can be associated to a message.

When Openbravo ERP catches one of these errors it tries to find a message with the same _Search Key_ as the code number, if it exists it will display the text in the same way as explained in the previous version to replace the message between at symbols (@) with the matching message.

It is not allowed to use these code numbers to manage messages because:

* They cannot be defined within modules. As the only identifier they have is a numeric value there's no way to include them in modules without the risk of two different modules using the same number for different purposes. 
* This is Oracle specific and cannot be used in PostgreSQL, thus they will not work in the same way in PostgreSQL. 

So the correct way to do this is to use a number which has no associated message and insert within the text the identifier for the message to be used. With this intention there is not message for value _20000_ , so when it is used the message will be taken from the second parameter:

```    
RAISE_APPLICATION_ERROR(-20000, '@HR_MyErrorMessage@');
```

**PostgreSQL**

The only way to identify a message to be displayed when working with Openbravo in PostgreSQL is identifying it by its _Search Key_ .
 
```     
RAISE EXCEPTION '%', '@HR_MyErrorMessage@';
```

####  Checks and Foreign Keys

Check restrictions are defined in database to ensure data integrity, they define some restriction that data must be fulfill. In case when inserting or updating some data in database it does not satisfy a constraint, an error is raised.

When a piece of data is tried to be inserted in a table with a check constraint and that data does not follow the rules defined by that constraint, a database error is raised. By default, if there is no an Application Dictionary Message associated to that constraint a generic error message will be shown in the UI.

It is possible to refine that error by adding a new message with the same _Search Key_ as the constraint's name. In this case instead of appearing that generic message, it will be showed the new one.

The same thing applies to Foreign Keys. When data is inserted, modified or deleted, a foreign key might be violated. In that case, if there is an specific message for it in the Application Dictionary, it will be shown. Otherwise, a generic error will be shown.


---

This work is a derivative of [Messages](http://wiki.openbravo.com/wiki/Messages){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.