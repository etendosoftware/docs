---
title: Informe de Valuación de Existencias
---

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe de Valuación de Existencias`

### **Overview**

El Informe de Valuación de Existencias muestra el stock de un almacén concreto, así como el valor del stock.

El coste se calcula como la suma del coste de cada transacción de material del producto en el almacén. El coste de las transacciones del producto lo calcula el proceso Costing Server.

### **Parameters Window**

![Informe de Valuación de Existencias](../../../../../assets/drive/1HGDsUBdSrfe3_Nzk_ojKq3Ck-aGvIAdx.png)



-   **Organización**: Este campo permite al usuario seleccionar entre organizaciones de tipo "Legal with Accounting" y "Generic".
-   **Almacén**: Si la organización seleccionada es "Generic", entonces muestra todos los almacenes que le pertenecen; en caso contrario, si la organización es "Legal with accounting", no se muestra ningún almacén para seleccionar.
-   **Fecha**: El informe mostrará la información hasta la fecha seleccionada.
-   **Almacén consolidado**: Si se marca, la información del stock se consolidará a nivel de organización; en caso contrario, la información se desglosará por almacén.
-   **Categoría del Producto**: Permite mostrar información solo de la Categoría del Producto seleccionada.
-   **Moneda**: Define la moneda en la que se muestran todos los valores monetarios (como Coste, Valoración) del informe.

!!! warning
    Tenga en cuenta que para que el informe funcione debe especificarse el tipo de cambio a la Moneda del informe.

### **Output Window** 

![Informe de Valuación de Existencias](../../../../../assets/drive/1btCDeLvHaczMWt9lE05E0J8RFjePTZFM.png)


-   **Producto**: Nombre del producto.
-   **Cantidad**: Stock del producto en la fecha seleccionada.
-   **Unidad** : Unidad en la que se mide el stock.
-   **Coste Unitario**: Coste de cada unidad concreta. Es el resultado de dividir la Valoración entre el stock.
-   **Valoración**: Valoración del stock. Se calcula sumando todas las valoraciones de cada transacción que ha tenido lugar en el almacén.
-   **Actual Average/Standard Algorithm Cost**: Coste medio/estándar actual, el último cálculo de su valor.
-   **Actual Average/Standard Algorithm Valuation**: Valoración del stock basada en el Coste medio/estándar actual. Es el resultado de multiplicar el stock por el coste actual.

### **Persisted Information**

Este paso no es necesario para lanzar el informe. Sin embargo, si existen problemas de rendimiento, esto puede ayudar a mejorar considerablemente el rendimiento del informe.

Es posible agregar información que permita realizar consultas más rápidas. Esta información se agrega para cada período contable cerrado, lo que significa que los períodos contables deben estar definidos y, al menos algunos de ellos, deben estar en un estado *Cerrado* o *Cerrado permanentemente*. 

La información persistirá hasta el primer período no cerrado. De este modo, es posible evitar recorrer muchos registros. Sin embargo, no se agregará información después del primer período cerrado y esto puede provocar un rendimiento no óptimo del informe si necesita recuperar mucha información.

!!! info
    Para usar esta funcionalidad es necesario programar el proceso en segundo plano llamado *Generate Aggregated Data Background*. Esto se puede hacer a través de la ventana *Process Request*.

![Informe de Valuación de Existencias](../../../../../assets/drive/1_mjP-Y6k-QGbCLm8FeIQI08YLJghMAfM.png)

!!! info
    Se recomienda programarlo diariamente, en un momento en que el sistema no tenga mucha actividad. Solo agregará datos cuando se cierre un nuevo período o se cierre permanentemente.


### **Limitations**

Al agregar la información por cada período cerrado, no es posible conservar la fecha de cada transacción. Por lo tanto, cuando se lance el informe para una moneda diferente, toda esa información se convertirá en la fecha de cierre del período. Esto puede provocar pequeñas discrepancias con la versión anterior debido a conversiones entre monedas en fechas diferentes.

---

Este trabajo es un derivado de [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.