---
tags:
  - Cómo hacer
  - Etendo classic
  - Lógica de visualización
  - Campos
  - Diccionario de aplicación
---

# Cómo definir la lógica de visualización evaluada a nivel de servidor

## Visión general

Con la introducción de esta funcionalidad, es posible definir en Openbravo lógicas de visualización que se van a evaluar a nivel de servidor.

Esto significa que la expresión para esta lógica de visualización en particular se va a evaluar mientras se genera el código para la ventana final, en lugar de evaluarse cuando se carga la ventana.

Al hacerlo, es posible evitar campos en blanco cuando el campo no debería mostrarse. En su lugar, los campos se reorganizan y la ventana se ve más limpia.

### Uso

En la ventana **Ventanas, Pestañas y Campos**, hay un nuevo campo llamado _Mostrar Lógica Evaluada en el Servidor_.

En este campo, es posible definir una expresión que se evaluará para decidir si ese campo en particular debe mostrarse o no.

Esta expresión debe seguir las mismas reglas sintácticas que se utilizan en la lógica de visualización normal. La expresión puede evaluar Preferencias, pero solo aquellas definidas a nivel de sistema.

Un ejemplo de una expresión sería:
`@uomManagement@ = 'Y' & @enableNegativeStockCorrections@ = 'Y'`

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_define_Display_Logic_Evaluated_at_Server_Level-1.png)

### Limitaciones

Dado que esta funcionalidad se va a evaluar a nivel de sistema (la visibilidad de los campos va a ser la misma para todos los clientes, organizaciones y usuarios), es posible usar Preferencias, pero solo aquellas que se hayan definido a nivel de sistema.

Este trabajo es una obra derivada de [Cómo definir la lógica de visualización evaluada a nivel de servidor](http://wiki.openbravo.com/wiki/How_to_define_Display_Logic_Evaluated_at_Server_Level){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.