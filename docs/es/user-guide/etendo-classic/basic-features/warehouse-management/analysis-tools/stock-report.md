---
title: Informe Stock
---

## Informe Stock

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Stock`

### **Overview**

El Informe Stock muestra los niveles de stock actuales de todos los productos que tienen inventario disponible (cantidad mayor que cero). Los datos se agrupan por categoría de producto, y cada fila muestra el producto, el almacén y la ubicación del hueco. Este informe proporciona una visibilidad rápida de cómo se distribuye el inventario entre almacenes y huecos.

Revisar periódicamente el Informe Stock ayuda a mantener la exactitud del inventario y favorece mejores decisiones de compra. Al identificar productos que están bajando de nivel o acumulándose por encima de lo esperado, los usuarios pueden actuar a tiempo para evitar roturas de stock que retrasen las operaciones o situaciones de sobrestock que inmovilicen capital y espacio de almacén. Esto convierte al informe en una herramienta práctica para mantener el inventario alineado con la demanda real del negocio.

### **Parameters Window**

El resultado de este informe puede filtrarse utilizando los siguientes parámetros:

-   **Date**: Filtra las transacciones hasta la fecha seleccionada.
-   **Product Category**: Limita el informe a una categoría de producto específica.
-   **Product**: Filtra el informe a un producto específico.
-   **Storage Bin**: Limita el informe a una ubicación de hueco específica.

![Stock Report](../../../../../assets/drive/1OgkmMsGjuADw-Sbqn1tfJ5WkCbq_AGx5.png)

El resultado de este informe puede visualizarse en formato HTML, PDF y Excel.

### **Sample Report Output**

![Stock Report](../../../../../assets/drive/1jjN-TjQjeY-38odbT6xBRYCpACEmMUxz.png)

La salida del informe incluye las siguientes columnas:

-   **Article**: Nombre o código del artículo.
-   **Quantity**: Cantidad actual disponible.
-   **Unit**: Unidad de medida del producto.
-   **Attribute**: Características del producto, como tamaño, color o número de lote, si están definidas para el producto.
-   **X**: Posición de fila dentro del hueco (ubicación horizontal).
-   **Y**: Posición de pila dentro del hueco (ubicación en profundidad).
-   **Z**: Posición de nivel dentro del hueco (ubicación vertical).
-   **Other**: Información adicional del producto, si aplica.
-   **Warehouse**: Almacén donde se encuentra el stock.

!!! info
    Las columnas **X**, **Y** y **Z** del informe corresponden a **Fila (X)**, **Pila (Y)** y **Nivel (Z)** del Hueco.

---

Este trabajo es un derivado de [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.