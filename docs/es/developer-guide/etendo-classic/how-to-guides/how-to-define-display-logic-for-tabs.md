---
title: Cómo definir la Lógica para mostrar para solapas
tags:
    - definir 
    - mostrar
    - lógica
    - solapas
---

# Cómo definir la Lógica para mostrar para solapas

# Visión general

El objetivo de este procedimiento es mostrar cómo puede definir la lógica para mostrar para solapas, de modo que su visibilidad dependa del valor de los campos de sus solapas ancestro, de las preferencias y de las variables del sistema. 

!!!note
    La lógica para mostrar solo será aplicable para solapas que **no** sean solapas de cabecera.

Para ello, se ha añadido un nuevo campo denominado **Lógica para mostrar** a la solapa **Solapa** en la ventana **Ventanas, solapas y campos**:


![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-define-display-logic-for-tabs/display-logic.png)

# Cómo definir la Lógica para mostrar de la solapa

La sintaxis de la solapa **Lógica para mostrar** es la misma que la del campo Lógica para mostrar. Se pueden introducir valores booleanos (`true`, `false`), así como expresiones que se evalúen como un valor booleano.

- Si existe una referencia a un campo de una solapa de un nivel superior, el nombre del campo debe colocarse entre `@`. Es decir, si solo queremos mostrar la solapa Consulta de la ventana Widget cuando el widget seleccionado es un widget de Consulta, la lógica para mostrar de la solapa Consulta puede definirse como: `@Widget_Superclass_ID@='2A32CF26F3F64FE39C7F94E9D82497D1`.

- Si existe una referencia a una preferencia, el nombre de la preferencia también debe colocarse entre `@`. Es decir, si una solapa debe mostrarse solo si la propiedad `StockReservations` está configurada, puede utilizarse esta lógica para mostrar: `@StockReservations@`.

- Si dentro de la lógica para mostrar existe una referencia a una variable del sistema, su nombre debe colocarse entre `@#` y `@`, es decir, `@#ShowAcct@='Y'`.

---
Este trabajo es una obra derivada de [Cómo definir la Lógica para mostrar para solapas](http://wiki.openbravo.com/wiki/How_To_Define_Display_Logic_For_Tabs){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.