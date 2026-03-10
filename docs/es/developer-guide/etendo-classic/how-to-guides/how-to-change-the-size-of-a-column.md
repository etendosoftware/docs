---
tags:
  - How to
  - Column
  - Diccionario de la Aplicación
  - Tamaño de columna
---

# Cómo cambiar el tamaño de una columna

## Visión general

Esta sección explica **cómo cambiar el tamaño de una columna** dentro de la base de datos. Permite al usuario disponer de cierta flexibilidad dentro de la base de datos.

## Pasos de ejecución

En Etendo, es posible **cambiar el tamaño de una columna**. Para lograrlo, deben seguirse estos pasos:

  1. Cree una plantilla y establezca su estado como **En Desarrollo**.
  2. Modifique el tamaño de la columna en la base de datos con el comando SQL **ALTER TABLE**.

    !!!info
        El nuevo valor debe ser mayor que el anterior.

    - Postgres:
    ```SQL
    ALTER TABLE <table_name> ALTER COLUMN <column_name> type <type>(<new_size>)
    ```
    - Oracle:
    ```SQL
    ALTER TABLE <table_name> MODIFY <column_name> <type>(<new_size>)
    ```

  3. Actualice el nuevo tamaño de la columna en el **Diccionario de la Aplicación**. Para ello, vaya a la ventana **Tablas y columnas**, busque la definición de la columna y especifique allí el nuevo tamaño.
  4. Exporte la base de datos: `./gradlew export.database` (con esta acción, se exportan las definiciones de la plantilla).
  5. Exporte el script de configuración: `./gradlew export.config.script` (con esta acción, se exportan los cambios del core a la plantilla).
  6. Compruebe el script de configuración generado y verifique que el cambio relativo al nuevo tamaño de la columna aparece en las primeras líneas.

!!!note
    Si la columna que se ha modificado está siendo utilizada por una función de base de datos asignando su valor a otra variable, esta variable debe tener un tamaño igual o mayor (al menos el tamaño de la nueva columna modificada). De lo contrario, el proceso fallará. Esto significa que, si el tamaño de la variable no era suficiente para almacenar el contenido de la columna, la función también debe modificarse ajustando el tamaño de la variable en cuestión y exportando este cambio a la plantilla.

Como última consideración, **verifique que el nuevo tamaño de la columna no afecta** a funciones o triggers que trabajen con la base de datos.

---

Este trabajo es una obra derivada de [Cómo cambiar el tamaño de una columna](https://wiki.openbravo.com/wiki/How_To_Change_The_Size_of_a_Column){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.