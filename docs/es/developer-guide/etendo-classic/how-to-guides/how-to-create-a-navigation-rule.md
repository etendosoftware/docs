---
title: Cómo crear una Regla de Navegación
tags: 
    - Reglas de Navegación
    - Reglas de Campo
    - Reglas de Tabla 
    - Solapas personalizadas
status: beta
---

# Cómo crear una Regla de Navegación

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.


## Visión general

Las **reglas de navegación** permiten a Etendo dirigir dinámicamente a los usuarios a diferentes solapas en función de los datos visualizados. Estas reglas pueden definirse tanto a **nivel de campo y a nivel de tabla**, proporcionando a los administradores un control flexible sobre cómo se abren los registros. Cada regla puede especificar una solapa de destino, su prioridad y, cuando sea necesario, una condición de **Lógica HQL** que determina cuándo debe aplicarse la regla. Al combinar estos elementos, Etendo puede gestionar escenarios de navegación complejos, como abrir diferentes ventanas en función del tipo de documento o del registro al que se accede.


## Definición de reglas a nivel de campo

Estas reglas se definen en la solapa **Reglas de Navegación** de la ventana **Windows, Tabs and Fields**, debajo de la solapa **Campo**. El administrador del sistema puede añadir reglas a un campo para que navegue a una solapa personalizada.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-navigation-rule/how-to-create-a-navigation-rule-1.png)

Los campos principales que deben configurarse son:

- **Secuencia**: prioridad de la regla. Las reglas se aplican en orden ascendente. 
- **Solapa**: solapa de destino que se abrirá si se cumple la regla. 
- **Navegación Directa**: indicador que determina si se ejecuta la cláusula `HQL Logic` o si la regla se aplica siempre. 
- **Lógica HQL**: cláusula where HQL que debe cumplir el registro que se está abriendo para abrir la solapa especificada en la regla. 

## Definición de reglas a nivel de tabla

Las reglas a nivel de tabla para el **Modelo de Navegación Extendido** se definen en una nueva solapa de la ventana **Tablas y columnas** llamada **Reglas de Navegación**. El administrador del sistema puede añadir nuevas reglas a una tabla para que los enlaces que tengan esa tabla como referencia naveguen a una solapa personalizada.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-navigation-rule/how-to-create-a-navigation-rule-2.png)

Las reglas se definen siguiendo la misma lógica que las *Reglas a nivel de campo*.

## Creación de reglas

Para crear una regla que no sea de **Navegación Directa**, defina el campo **Lógica HQL** con una expresión de cláusula where. Esta expresión se añade a un HQL que se ejecuta sobre la tabla donde se almacena el registro que se está abriendo. El HQL también se filtra por el **id** del registro, de modo que solo pueda devolver ese registro. Si el HQL devuelve el registro, entonces la regla es válida y se abre en su **solapa**. Si no se devuelven resultados, se ejecuta la siguiente regla.

La `Lógica HQL` debe ser una cláusula where HQL válida. El alias de la tabla principal es `e`; usándolo es posible acceder a las propiedades de esa tabla.

Por ejemplo, la tabla `C_OrderLine` tiene diferentes tipos de pedido que se gestionan en distintas ventanas. Los pedidos de venta que no son pedidos de devolución deben abrirse en la ventana **Pedido de venta**. Es necesario crear una regla con una Lógica HQL que devuelva la línea de pedido solo en caso de que sea un Pedido de venta y no sea una Devolución. La Lógica HQL es:
 
``` java    
    e.salesOrder.salesTransaction=true AND e.salesOrder.documentType.return=false
```

---
Este trabajo es una obra derivada de [Cómo crear una Regla de Navegación](http://wiki.openbravo.com/wiki/How_to_create_a_navigation_rule){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.