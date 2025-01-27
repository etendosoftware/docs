---
tags:
  - How to
  - Column
  - Application Dictionary
  - Column Size
---

# How to Change the Size of a Column

## Overview

This section explains **how to change the size of a column** inside the database. It enables the user to have a certain amount of flexibility within the database.

## Execution Steps

In Etendo, it is possible to **change the size of a column**. To achieve this, these steps must be followed:

  1. Create a template and set its status as **In Development**.
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

  3. Update the new column size in the **Application Dictionary**. For this, go to the **Tables and Columns** window, find the column definition and specify the new size there.
  4. Export the database: `./gradlew export.database` (with this action, the template definitions are being exported).
  5. Export the configuration script: `./gradlew export.config.script` (with this action, the core changes into the template are being exported).
  6. Check the generated configuration script and verify that the change regarding the new column size appears in the first lines.

!!!note
    If the column that has been modified is being used by a database function by giving its value to another variable, this variable must have an equal or greater size (at least the size of the new modified column). Since if not, the process would fail. This means, if the variable's size was not enough to store the columns content, the function as well must be modified by adjusting the size of the variable in question and exporting this change into the template.

As a last consideration, **verify that the new column size does not affect** functions or triggers working with the database.

---

This work is a derivative of [How To Change The Size of a Column](https://wiki.openbravo.com/wiki/How_To_Change_The_Size_of_a_Column){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.