---
title: Informes de Compras 
---
## Visión general

Esta sección describe las ventanas relacionadas con los informes de compras en Etendo. Estas son:

[:material-file-document-outline: Informe pedidos de compra](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#purchase-order-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Análisis dimensional pedidos compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#purchase-dimensional-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Análisis dimensional albaranes compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#goods-receipts-dimensional-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Análisis dimensional facturas compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#purchase-invoice-dimensional-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Pedidos de compra cuadrados](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#matched-purchase-orders){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Facturas](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#vendor-invoice-report){ .md-button .md-button--primary } <br>


## Informe pedidos de compra

:material-menu: `Aplicación` > `Gestión de Compras` > `Herramientas de análisis` > `Informe pedidos de compra`

Este informe muestra una lista detallada de los pedidos de compra emitidos a los proveedores. 

## Análisis dimensional pedidos compras

:material-menu: `Aplicación` > `Gestión de Compras` > `Herramientas de análisis` > `Análisis dimensional pedidos compras`

### Visión general

Este informe muestra información sobre los pedidos de compra emitidos y enviados a los proveedores.

Es un informe de tipo dimensional que muestra información sobre las compras registradas (Pedidos de compra en estado Reservado o Cerrado) durante un periodo de tiempo seleccionado.

Este informe puede mostrar información sobre los proveedores utilizados con mayor frecuencia, así como los bienes comprados con mayor frecuencia, junto con información de importes de compra y cantidades pedidas.

### Ventana de parámetros

![](../../../../assets/drive/1tfjdJFeCwoMFq7Osb7iA4oCx8AQtsO5M.png)


No hay ningún campo específico a destacar, salvo los filtros dimensionales primarios y secundarios que pueden utilizarse para acotar la información a mostrar.

### Ejemplo de salida del informe

![](../../../../assets/drive/1HteUH5sPx3PmrHdRqlR8S6l0EzDizuUu.png)

-   **Importe:** es el importe **neto** del Pedido de compra convertido a la **Moneda** del informe.

## Análisis dimensional albaranes compras

:material-menu: `Aplicación` > `Gestión de Compras` > `Herramientas de análisis` > `Análisis dimensional albaranes compras`

### Visión general

Este informe muestra información sobre los bienes recibidos en la organización.

Es un informe de tipo dimensional que muestra información sobre las recepciones registradas durante un periodo de tiempo seleccionado.

Este informe puede mostrar información sobre los proveedores utilizados con mayor frecuencia, así como los bienes recibidos con mayor frecuencia, junto con información de importes y cantidades recibidas.

### Ventana de parámetros

No hay ningún campo específico a destacar, salvo los filtros dimensionales primarios y secundarios que pueden utilizarse para acotar la información a mostrar.

![](../../../../assets/drive/1ihcncYc8rQoONnKy5KzGqN2IaYw5r18f.png)

!!! tip
    El resultado de este informe puede visualizarse en formato HTML y en formato PDF.

### Ejemplo de salida del informe

![](../../../../assets/drive/1lvq1Mtz7ed_qJW40ezxrQvqa5ssh5NgM.png)

## Análisis dimensional facturas compras

:material-menu: `Aplicación` > `Gestión de Compras` > `Herramientas de análisis` > `Análisis dimensional facturas compras`

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning
    Si no dispone del [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}, el informe permanecerá en una versión legacy.

### Visión general

Este informe muestra información sobre las facturas de compra recibidas en la organización. Es un informe de tipo dimensional que muestra información sobre las facturas de compra registradas (Facturas de compra en estado *Completada* o *Anulada*) durante un periodo de tiempo seleccionado.

Este informe puede mostrar el importe total de compra de un proveedor determinado, desglosado por producto y factura de compra.

### Ventana de parámetros

![](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/analysis-tools/purchase-invoice-dimensional-report-0.png)

Este informe incluye varios filtros y opciones de configuración que le permiten personalizar la información mostrada:

**Filtros primarios:**

- **Fecha desde / Fecha hasta** *(Obligatorio)*: definen el periodo de tiempo para el que desea generar el informe. Estos campos filtran las facturas en función de su fecha de factura.
- **Importe mayor que / menor que**: establecen filtros de rango monetario para incluir solo facturas por encima o por debajo de importes específicos. 
- **Informe comparativo**: casilla de verificación para habilitar el análisis comparativo entre distintos periodos o criterios. Cuando está habilitada, se muestran campos de fecha adicionales para definir el periodo de comparación *(Por defecto: No)*.
- **Mostrar líneas financieras**: casilla de verificación para incluir o excluir líneas financieras en la visualización del informe *(Por defecto: Sí)*.

**Filtros secundarios:**

- **Organización** *(Obligatorio)*: filtra las facturas por la organización específica.
- **Grupos de Terceros**: filtra las facturas por la categoría asignada al tercero (proveedor).
- **Terceros**: seleccione uno o varios proveedores para ver únicamente sus facturas. Se pueden seleccionar varios terceros para un filtrado más amplio.
- **Tipo de producto**: filtra por el tipo de productos incluidos en las facturas. Las opciones disponibles son:
    - **Tipo de gasto**: productos clasificados como artículos de gasto.
    - **Artículo**: artículos o bienes estándar de inventario.
    - **Recurso**: recursos utilizados en producción o servicios.
    - **Servicios**: productos de tipo servicio.
- **Categoría del producto**: filtra por la categoría de los productos incluidos en las facturas.
- **Producto**: seleccione uno o varios productos para ver facturas que contengan esos artículos concretos. Se pueden seleccionar varios productos para un filtrado más amplio.
- **Moneda** *(Obligatorio)*: filtra para incluir solo facturas registradas en la moneda especificada.

**Dimensiones:**

- **Agrupación dimensional** *(Obligatorio)*: configura cómo se agrupan y se muestran los datos en el análisis dimensional. Esto determina tanto las dimensiones por las que se agrupan los datos como el orden en el que se aplican. Las opciones de dimensión disponibles son:
    - **Terceros**: agrupa los datos por proveedor.
    - **Grupo de terceros**: agrupa los datos por categorías de terceros.
    - **Producto**: agrupa los datos por productos individuales.
    - **Grupo de productos**: agrupa los datos por categorías de producto.
    - **Nº de documento**: agrupa los datos por números de documento de factura.

**Ordenar:**

- **Ordenar** *(Obligatorio)*: define el criterio de ordenación para los resultados del informe. Las opciones de ordenación disponibles son:
    - **Estándar**: orden alfabético por defecto según las dimensiones seleccionadas.
    - **Por importe ascendente**: ordena los resultados por importe de menor a mayor.
    - **Por importe descendente**: ordena los resultados por importe de mayor a menor.

### Ejemplo de salida del informe

![](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/analysis-tools/purchase-invoice-dimensional-report-1.png)

Este ejemplo de salida muestra la agrupación dimensional con cuatro niveles de agrupación tal y como se indica en la cabecera: "1.- Terceros, 2.- Grupo de terceros, 3.- Nº de documento, 4.- Producto". El informe muestra:

- **Nivel 1 (Terceros)**: "Be Soft Drinker, Inc." como la agrupación principal del proveedor con un importe total de $1,328,580.00
- **Nivel 2 (Grupo de terceros)**: categoría "Proveedor" que muestra la clasificación del proveedor
- **Nivel 3 (Nº de documento)**: números de factura (10001680, 10001694, 10001708, 10001722, 10001736) con sus respectivos subtotales
- **Nivel 4 (Producto)**: productos individuales (Cherry Cola, Cola, Energy Drink, Lemonade, Plain Water) mostrando importes y cantidades para cada factura

Cada nivel de agrupación muestra subtotales, y el informe concluye con un total general de $1,328,580.00, lo que demuestra la estructura jerárquica del análisis dimensional.

También existe la posibilidad de exportar este informe a un archivo PDF o XLS.

El formato PDF muestra los mismos campos explicados anteriormente, pero en formato XLS muestra información relacionada con las columnas de las facturas seleccionadas:

-   Organización
-   Grupo de terceros
-   Terceros
-   Nº de documento.
-   Fecha de factura
-   Categoría del producto
-   Producto
-   Clave de búsqueda del producto
-   Precio unitario
-   Importe
-   Cantidad

## Pedidos de compra cuadrados

:material-menu: `Aplicación` > `Gestión de Compras` > `Herramientas de análisis` > `Pedidos de compra cuadrados`

### Visión general

Esta ventana informa sobre el emparejamiento entre cada pedido de compra, albarán de recepción de mercancías y línea de factura.

### Pedidos de compra cuadrados

La vista Pedidos de compra cuadrados informa sobre qué línea de pedido de compra está vinculada a qué línea de recepción y línea de factura, si existe.

![](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/analysis-tools/matched-purchase-orders.png)

En otras palabras, esta ventana proporciona información valiosa que ayuda a obtener una comprensión rápida de qué líneas de pedido de un producto ya han sido recibidas y facturadas.

## Facturas

:material-menu: `Aplicación` > `Gestión de Compras` > `Herramientas de análisis` > `Facturas`

### Visión general

Este informe proporciona información sobre el importe total facturado por cada proveedor dentro de un periodo de tiempo determinado y para una moneda determinada.

Muestra información de facturas de proveedor, que puede acotarse para obtener información sobre aquellas facturas relacionadas con un proyecto determinado y/o con un tercero determinado dentro de un periodo de tiempo determinado.

### Ventana de parámetros

![](../../../../assets/drive/1V8A7QEZI3fa7ecV6W-VK-ki_VXx_8Ii8.png)

Campo a destacar:

-   Moneda: funciona de la misma manera que ya se ha descrito en el informe de pedidos de compra.

### Ejemplo de salida del informe

![](../../../../assets/drive/1U3Fx3IPP0R9acd8XMPXhtBR5qQFoj2Am.png)

---

Este trabajo es una obra derivada de [Gestión de Compras](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.