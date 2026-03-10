---
title: Cómo añadir un campo a una solapa de ventana
tags:
  - Cómo hacer
  - Etendo Classic
  - Personalización
  - Diseño de UI
  - Diccionario de aplicación
  - Módulos
---

# Cómo añadir un campo a una solapa de ventana

## Visión general

El objetivo de esta sección es mostrar cómo puede añadir un nuevo campo a una solapa en Etendo Classic.

Está estrechamente relacionada con la sección anterior [Cómo añadir columnas a una tabla](how-to-add-columns-to-a-table.md).

La tarea de añadir columnas a una ventana existente ahora es muy sencilla, ya que la mayor parte del trabajo (como definir referencias, elementos) ya se ha realizado al añadir las columnas a la tabla.

En esta página mostraremos un ejemplo de cómo colocar el campo `example_column` en la ventana `Production Run` usando el botón `create fields`.

### Ejemplo: añadir los campos a la ventana

El proceso para añadir nuevos campos a una ventana existente es el mismo que para añadir campos a una ventana nueva (vacía). Accediendo a `Application Dictionary` > `Window, Tabs and Fields`, necesitamos buscar la ventana `Production Run`. A continuación, para esa ventana, marque su solapa `Incidence`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_field_to_a_Window_tab_0.png)

Ahora, usamos el proceso Create Fields en esta solapa para que añada todas las columnas
de la tabla subyacente _MA_WEIncidence_ a esta solapa si no se han añadido previamente.

Esto añadirá entonces un nuevo campo a la solapa que coincida con la nueva columna
y colocará automáticamente el campo dentro del módulo.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_field_to_a_Window_tab_1.png)

Como último paso, se debe ejecutar el proceso Synchronize Terminology para sincronizar nuestros campos recién añadidos con los elementos creados para las columnas en las que se basan, de modo que las etiquetas de la UI para los nuevos campos obtengan los nombres definidos en esos elementos.

Si esta ventana también debe usarse en _modo de UI clásica_, entonces ahora se debe ejecutar `./gradlew smartbuild` para compilar la ventana modificada.

Para ver los cambios en la nueva interfaz de usuario, simplemente cambie el rol `System Administrator` usado para esta sección (seleccione un rol donde tenga acceso a la ventana) y vaya a la ventana modificada para ver que tiene el nuevo campo como se muestra aquí:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_field_to_a_Window_tab_2.png)

---

Este trabajo es una obra derivada de [Cómo añadir un campo a una solapa de ventana](http://wiki.openbravo.com/wiki/How_to_add_a_field_to_a_Window_Tab){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.