---
tags: 
  - Etendo Classic
  - Localization
  - Chart of Accounts
  - Modules
  - Module Creation
---

# How to Create a Chart of Accounts Module

## Overview

The chart of accounts (also called account tree) is a list of the accounts available to post entries which can be structured in a way to get meaningful financial reports such as Balance Sheet and P&L.

In some countries, it is required to have a specific chart of accounts to be used in the statutory books; in some other countries this legal requirement does not exist and a “sample” chart of accounts should be enough. Finally it should also be possible for a country to have more than one official chart of accounts, depending for example on the organization's size or main activity.

!!!important
    A Chart of Accounts Module for Etendo can only contain one chart of accounts. So, if you are working in a localization project for a country where several chart of accounts can be used, you must create independent modules including each chart of accounts CSV file. It will be up to the user to install and apply the chart of accounts module that fits particular needs.

## Creating the CSV file

The first step for creating a chart of accounts module is to write the CSV file with the list of accounts we want to include. All the information can be found in [Creating Accounts Files]().

## Testing the CSV file

Before creating the Chart of Accounts module, we should first check that the CSV file has no structural or logical errors. This can be easily done in two steps:

1. The first one is using a testing spreadsheet provided by Etendo that will detect any structural error, like missing search keys, wrong values in Element Level, Parent_Value or Show Value Condition columns, etc.

2. The second check can be directly executed through the ERP. It just consists on importing our CSV file when running the Initial Client Setup process.
Finally, there is also recommended to create some accounting entries for every transactional document and ensure the accounting report information is OK.

!!!info
    Please visit [Chart of Accounts Testing]() to learn more about these steps.

## Creating the Chart of Accounts module

The remaining step is clearly the easiest one, which is just including the CSV file into our Chart of Accounts module.

A Chart of Accounts module is like any other module, but it has just the following considerations:

- The CSV file must be included into the `referencedata/accounts/` directory of our module.

- The file must be renamed to COA.csv. So the directory structure for our module should look like:

```java
 <module java package name>
   ├── referencedata 
   │   └── accounts 
   │       └── COA.csv 
   └── src-db 
       └──  database 
           └── sourcedata 
             ├── AD_DATASET.xml 
             ├── AD_MENU.xml 
             ├── AD_MODULE_DBPREFIX.xml 
             ├── AD_MODULE_DEPENDENCY.xml 
             ├── AD_MODULE.xml 
             ├── AD_PACKAGE.xml 
             ├── AD_PROCESS_PARA.xml 
             ├── AD_PROCESS.xml 
             └── AD_TREENODE.xml            
```

- When defining the module inside the Application Dictionary, the only important considerations we must have are:

    - Set the module type to *Module*

    - Set the *Has Chart of Account* checkbox

    - Remember to add the *dependency to Core*

### Publishing the Chart of Accounts Module

The way to package a chart of accounts module is similar to the [standard publishing process](.How_To_Create_and_Package_a_Module.md) for any module, just taking into account the previous particular considerations.

The summarized process is:

- Create the module's definition in the Application Dictionary. You should follow the [Naming guidelines for modules](../../../developer-guide/etendo-classic/concepts/naming-guidelines-for-modules.md). Remember to register the module in case you want to publish it in the Forge.

- Set the *Has Chart of Account* checkbox and add a *dependency to Core*.

- Export the database to create the file structure

        `gradle export.database`

- Save the COA.csv file inside the module's `referencedata/accounts/` directory. You should manually create this directory structure if necessary.

- Generate the obx file

        `gradle package.module -Dmodule=<module's java package name>`

## Translating a Chart of Accounts

In some countries it can be useful to have the same chart of accounts translated into several languages. Unfortunatelly Etendo does not support yet the translation of chart of accounts, although it is in our roadmap.

If you are in this situation, you have two possible workarounds:

- Create several chart of accounts modules for different languages. The structure of the chart of accounts file will be exactly the same, just changing the account names and descriptions for each language. This solution is perfect for companies that want to work in just one language, although there are several official languages in the country. In this case the administrator must decide at the beginning of the ERP implementation, the language to use for the chart of accounts and he will not be able to change it in the future.

- The other possibility is to create just one chart of accounts module and, once applied in an instance, manually translate the elements value inside the Account Tree window. The drawback of this method is that the translation can't be distributed to other instances and the process of translating must be repeated manually, or by the implementation of a script that automatically translates the elements based on the Element Value search key.

---

This work is a derivative of [How to create a chart of accounts module](https://wiki.openbravo.com/wiki/How_to_create_a_Chart_of_Accounts_Module){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.