---
title: How to Automatically Populate Search Keys
tags: 
    - Search Keys
    - Sequences
    - Data Entry Optimization
    - Reference data
---

# How to Automatically Populate Search Keys
  
##  Overview

**Search keys** are user defined identifiers or codes that allow to easily retrieve **reference data** such as customers, suppliers, products, payment terms, etc. For example, while entering an invoice the customer could be selected by opening the selector window and searching for it or, if you knew the search key of the **customer** that you were looking for, you could enter it and press **ENTER**; the system would then search the right customer based on that key and replace the key you entered with the customer name.

By starting typing the **customer name** on the invoice, the system automatically suggests the customers that match that entry as you type; once you have typed enough characters to have a unique match, the selection can be confirmed by simply pressing **ENTER or TAB** and moving to the next field.

This functionality makes search keys no longer needed for most entities. You can repurpose the search key on product to store product codes, if product codes are used, or to store customer numbers on customers. 

Users usually end up entering the same value in the search key as they enter in the name.

This section explains how to configure Etendo to automatically populate the **Search Key fields** and save time for the users.

## Execution Steps

!!! warning 
    **Sequences** are specific fields and they need to obey to specific naming convention (the column needs to be named DocumentNo), so a regular sequence was not an option in this case.

In this case, take inspiration from the technique used to automatically number invoice lines (each invoice line has a number that automatically increases by 10 for every line) and apply it to search keys.

Let's suppose this example on how to generate the search key for **business partners**:

1. Login as **system administrator**.
2. Modification to core will be needed, so make sure that there is an **active configuration template** in the system with status **In Development**. 

    !!!info
        Configuration templates are modules that contain changes to either core or to other modules. Using configuration templates make it possible to personalize the core behavior of the system without affecting the ability to apply maintenance packs and updates. Create a configuration template either by manually creating a module of type template or by putting your system in configuration mode.  

  
3. Navigate to the **Windows, Tabs and Fields window** and query the **Business Partner window**. From there, choose the appropriate tab and then look into the **Field** tab. 

    There, find the field called Search Key and identify which column of which table it is based on. In this case the column is `C_BPARTNER.VALUE`. 

4. In that column, enter a new defaulting rule based on the following SQL statement: 

    ``` SQL
    @SQL=SELECT TO_CHAR(MAX(TO_NUMBER(value))+1,'FM00000000') FROM c_bpartner WHERE ad_client_id =@AD_CLIENT_ID@ AND value LIKE '0%'
    ```
    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-automatically-populate-search-keys.png)


5. Let's analyze this rule:
    - `@SQL` means that this default is not going to be interpreted as a constant but as a SQL statement to be executed and the default is the result of that statement. 
    - The select statement selects the maximum previous value of the search key for business partners in this same client and increments it by one. 
    - The where clause uses the `@AD_CLIENT_ID@` expression that identifies the current client at run time; this enables different clients in a multi-tenant environment to be agnostic to each other. 
    - The value `LIKE '0%'` clause is used to avoid interference with existing values; if you have already created business partners and they have search keys that start with anything else than **0**, this clause allows you to ignore them. 
    - The select statement needs to make a few data type conversions. Value is a string, so its content first needs to be converted to a number; the maximum value, need to be increased by one and converted back to string with a format of 8 digits. 
    - To figure out how many digits you need, think of what is the maximum number of business partners that you will ever have and add 2 or 3 orders of magnitude just to be on the safe side. 

6. Since you have created a configuration template, make sure to export it so that you will not have problems with your next update. Connect to the command line in your server and run the following command: 

    ```groovy title="Terminal"
    ./gradlew export.database export.config.script -Dforce=true
    ```

7. The next time that you go to the Business Partner window and start creating a customer, the system will generate the Search Key for you and your customers will be effortlessly numbered as 00000001, 00000002, 00000003, 00000004, etc.

8. Finally, the Search Key field is the **first focus field** for the Business Partner window. Since you will not need to enter it any more, you might want to skip it and put the focus straight into the Commercial Name
field, so that you can save one click at data entry time. 

  
This work is a derivative of [How to Automatically Populate Search Keys](http://wiki.openbravo.com/wiki/How_to_automatically_populate_search_keys){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

