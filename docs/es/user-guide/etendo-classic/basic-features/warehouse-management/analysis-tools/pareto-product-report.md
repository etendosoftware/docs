---
title: Informe Pareto de Productos
---

## Informe Pareto de Productos

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Pareto de Productos`

### **Overview**

**Informe Pareto de Productos** distribuye los productos en tres clases (A, B o C) según el valor del costo que tiene el inventario de cada producto en el almacén. En función de esta clasificación se puede decidir la frecuencia del ciclo de conteo (por ejemplo, los productos A se cuentan semanalmente, los B mensualmente y los C anualmente).

Se utiliza la siguiente distribución: los productos A representan el 80% del valor del almacén, los B el 15% y los C el 5%.

!!! info
    La clasificación se basa en el costo del producto. Por eso es necesario tener una Regla de Costeo validada y los costos de las transacciones de material del producto calculados y actualizados.


### **Parameters window**

El campo **Moneda** define la moneda en la que se muestran todos los valores monetarios (como **Costo**, **Valor**) del informe. El campo toma por defecto la moneda del sistema.

!!! warning
    Tenga en cuenta que se debe especificar el **Ratio de conversión** a la **Moneda** del informe para que este funcione.

El botón **Update ABC** completa el campo **ABC** (actualiza el valor si el registro existe o crea un nuevo registro en caso contrario) de la pestaña Org. Specific de la ventana **Producto** para las organizaciones de la salida del informe.

### **Sample Report Output**

![Pareto Product Report sample output](../../../../../assets/drive/1DpBnQAG8Xyk9rM5xKhQvdKNt8p-bm4tj.png)


Columnas a tener en cuenta:

-   **Cantidad:** es el stock actual del producto (Quantity on Hand) en el almacén seleccionado.
-   **Valor:** es la suma de todos los costos de las transacciones de material del producto.
-   **Costo:** este costo se calcula como la relación entre el valor del producto y la cantidad del producto indicada arriba.
-   **Porcentaje:** este porcentaje es la relación entre el valor del producto y el Valor Total del almacén (que es la suma de todas las líneas del informe).

### **Persisted information**

Se puede utilizar la información agregada calculada para el Valued Stock. Consulte la documentación del Valued Stock Report para obtener más detalles sobre cómo generar la información agregada.

!!! note
    Exactamente igual que en el Valued Stock Report, el Informe Pareto de Productos también se puede ejecutar sin datos agregados. Sin embargo, esta función es especialmente útil en entornos de alto volumen cuando se experimentan problemas de rendimiento al ejecutar el informe.

---

Este trabajo es una derivación de [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.