---
title: Informe Transacción de Material
---

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Transacción de Material`

### **Overview**

El **Informe Transacción de Material** proporciona una vista consolidada de todos los movimientos de material registrados en el sistema, incluidas las expediciones de salida y las recepciones de entrada. Las transacciones se agrupan por Terceros y por documento, lo que facilita el seguimiento de qué productos se enviaron o recibieron, en qué cantidades y a través de qué almacén.

Este informe es útil para:

- Hacer seguimiento de los movimientos de material de entrada y salida durante un período específico.
- Auditar las transacciones de inventario para verificar que las expediciones y recepciones coincidan con las cantidades esperadas.
- Conciliar documentos por Terceros para garantizar la integridad y exactitud de las transacciones registradas.

### **Parameters Window**

![Material Transaction Report](../../../../../assets/drive/1B8aETuwl82fGlqe_SQLX3VAFz_2x6Tv2.png)

Los siguientes parámetros permiten filtrar los datos incluidos en el informe:

-   **Movement Date (From / To):** Define el rango de fechas del informe. Solo aparecerán las transacciones que se hayan producido dentro de este rango.
-   **Business Partner:** Filtra las transacciones por un proveedor o cliente específico. Si se deja vacío, se incluyen las transacciones de todos los Terceros.
-   **Warehouse:** Restringe el informe a las transacciones que se hayan producido en el almacén seleccionado.
-   **Project:** Filtra las transacciones asociadas a un proyecto específico.

El informe se puede generar en formato **HTML** o **PDF**.

### **Sample Report Output**

![Material Transaction Report](../../../../../assets/drive/1DxL6-LHWr4QxeYT1F1y0SbAT3-szlkGW.png)

La salida del informe se organiza por **Terceros** y, dentro de cada tercero, por **Número de Documento**. Para cada línea de transacción, se muestran las siguientes columnas:

-   **Número de Documento:** El identificador del documento de expedición o recepción.
-   **Producto:** El nombre del producto involucrado en la transacción.
-   **Almacén:** El almacén donde tuvo lugar la transacción.
-   **Hueco:** La ubicación específica (estante, rack o sección) dentro del almacén donde se almacenó o retiró el producto.
-   **Cantidad:** La cantidad del producto movida en la transacción.

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.