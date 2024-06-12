---
tags:
  - Etendo classic
  - Column
  - Application Dictionary
---

# How To Change The Size of a Column

## Overview

The objective of this article is to show you how to change the size of a column inside the database. It enables the user to have a certain amount of flexibility within his/her database.

## Recommended articles

Before reading this guide, it is necessary to have a proper understanding of Etendo Modularity concept and how to create and package a module, as we take the knowledge from these articles as a given in this guide.

In case you are working with configuration scripts or templates on a regular basis, the following link to an article might be of interest to you, since it describes how to create a configuration script.

## Execution Steps

In Etendo you are able to change the size of a column. To achieve this you must follow the following steps:

  1. Create a template and set its status as _In Development_.
  2. Modify the column size within the database with the **ALTER TABLE** SQL command.

    !!!info
        The new value must be greater than the old one.

    - Postgres:
    ```SQL
    ALTER TABLE <table_name> ALTER COLUMN <column_name> type <type>(<new_size>)
    ```
    - Oracle:
    ```SQL
    ALTER TABLE <table_name> MODIFY <column_name> <type>(<new_size>)
    ```

  3. Update the new column size in the **Application Dictionary**. For this, we go to the _Tables and Columns_ window, find the column definition and specify the new size there.
  4. Export the database: _./gradlew export.database_ (with this you are exporting the template definitions).
  5. Export the configuration script: _./gradlew export.config.script_ (with this you are exporting the core changes into the template).
  6. Check the generated configuration script and verify that the change regarding the new column size appears in the first lines.

!!!note
    As a final remark with great importance: If the column that has been modified is being used by a database function by giving its value to another variable for example, you must check that this variable has an equal or greater size (at least the size of the new modified column). Because if not, the process would fail. This means, if the variable's size wasn't enough to store the columns content, you have to modify the function as well, by adjusting the size of the variable in question and exporting this change into your template.

So please verify that your new column size does not affect you in any way (functions or triggers) working with your database.

---

This work is a derivative of [How To Change The Size of a Column](https://wiki.openbravo.com/wiki/How_To_Change_The_Size_of_a_Column){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.