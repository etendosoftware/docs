---
title: Informes de ventas
---
## Visión general


Esta sección describe las ventanas relacionadas con los informes de ventas en Etendo. Estas son:

[:material-file-document-outline: Análisis dimensional pedidos ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#sales-dimensional-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Análisis dimensional albaranes ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#shipments-dimensional-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Descuentos](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#discount-invoice-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe pedidos pendientes y stock](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#stock-for-open-orders){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Pedidos no facturados](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#orders-awaiting-invoice-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe de Pedidos a la Espera de Entrega](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#orders-awaiting-delivery-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Análisis dimensional facturas ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#sales-invoice-dimensional-report){ .md-button .md-button--primary } <br>


## Análisis dimensional pedidos ventas

:material-menu: `Aplicación` > `Gestión de Ventas` > `Herramientas de análisis` > `Análisis dimensional pedidos ventas`

### Visión general

Este es un informe de tipo dimensional que muestra información principalmente sobre el "**Imp. total líneas**" de los pedidos de venta registrados (Pedidos de venta en estado *Reservado* o *Cerrado*) durante un periodo de tiempo seleccionado.

Este informe puede mostrar los productos más vendidos y los principales clientes, y responder a muchas otras preguntas relacionadas con la actividad de registro de ventas de la empresa.

### Ventana de parámetros

![Sales Dimensional Report](../../../../assets/drive/1hUSiwTVhtzym77PrGRYXNcTx4jRqX3Ur.png)

Campos a tener en cuenta:

-   **Almacén:** acota los resultados para un almacén concreto desde el que se envía un pedido (campo **Almacén** en el Pedido de venta).
-   **Documento comercial:** permite al usuario filtrar los resultados por el campo **Agente comercial** de la ventana **Pedido de venta**, que normalmente refleja la persona que registró el pedido.
-   **Archivo comercial:** permite al usuario filtrar los resultados por el campo **Agente comercial** de la pestaña **Cliente** de la ventana **Terceros**, que normalmente contiene la persona responsable de este cliente (por ejemplo, el gestor de la cuenta).
!!! info
    En la mayoría de los casos, filtrar por los campos mencionados anteriormente ofrece los mismos resultados. Podrían diferir si un cliente tiene una persona responsable principal, pero distintos miembros del equipo de ventas pueden registrar pedidos. O si un cliente se traslada de un agente comercial a otro. Los nuevos agentes comerciales podrían querer utilizar el segundo filtro para ver las actividades de todos sus clientes (independientemente de quién cerró la operación), mientras que los antiguos agentes comerciales podrían querer utilizar el primer filtro para ver los pedidos que cerraron, independientemente de quién gestione actualmente al cliente.


### Ejemplo de salida del informe

![Sample Report Output](../../../../assets/drive/1ZYCoYa83A96xOFcOfd6-qIFTr81ymJ2S.png)

Información a tener en cuenta:

-   **Importe:** es el importe **neto** del Pedido de venta convertido a la **Moneda** del informe.
-   **Peso:** del producto vendido si se especifica en la ventana **Producto**.

## Análisis dimensional albaranes ventas

:material-menu: `Aplicación` > `Gestión de Ventas` > `Herramientas de análisis` > `Análisis dimensional albaranes ventas`

### Visión general

Este informe muestra información sobre los bienes enviados a los clientes (albaranes de salida en estado Completada o Anulada) durante un periodo de tiempo seleccionado. Es un informe de tipo dimensional.

### Ventana de parámetros

No hay ningún campo específico a destacar, solo los filtros dimensionales primario y secundario que pueden utilizarse para acotar la información que se va a mostrar.

![Shipments Dimensional Report](../../../../assets/drive/1A3OFI-84W20Lz_6zBXcFraHkHMOhWZKN.png)

El resultado de este informe puede visualizarse en formato HTML, formato XLS y formato PDF.

### Ejemplo de salida del informe

Algunos datos a tener en cuenta:

-   **Importe:** es el importe **neto** (coste de los bienes para los clientes) enviado a estos, convertido a la **Moneda** del informe. Este importe se obtiene del Pedido de venta que corresponde al albarán de salida. Si un albarán de salida no está vinculado a ningún Pedido de venta, este campo estará vacío.
-   **Peso:** del producto enviado, si se especifica en la ventana Producto.

![Sample Report Output](../../../../assets/drive/1TD2GMryWaNAeWDcX10o7t7qmMdkpZ6Jx.png)

## Descuentos

:material-menu: `Aplicación` > `Gestión de Ventas` > `Herramientas de análisis` > `Descuentos`

### Visión general

Este informe muestra información sobre las facturas de venta registradas (facturas de venta en estado Completada o Anulada) durante un periodo de tiempo seleccionado, agrupando la información por tercero y producto.

El informe muestra información sobre el precio medio por producto, el precio neto y el descuento aplicado en cada producto.

### Ventana de parámetros

![Discount Invoice Report](../../../../assets/drive/1ghqLTYaD2stIcN7FmRjo8EIxsP7CP1Jy.png)

Campos a tener en cuenta:

-   **Desde fecha:** permite filtrar los resultados por el campo **Fecha de la factura** de la ventana Factura de venta. Es obligatorio y el informe resultante mostrará información sobre facturas de venta con una fecha de factura posterior al parámetro.
-   **Hasta fecha:** permite filtrar los resultados por el campo **Fecha de la factura** de la ventana de facturas de venta. También es obligatorio, y el informe resultante mostrará información sobre facturas de venta con una fecha de factura anterior al parámetro.
-   **Moneda:** los importes se mostrarán en la moneda seleccionada. Para facturas en otra moneda, el importe se convertirá a la moneda seleccionada, teniendo en cuenta el tipo de cambio para la fecha de la factura.
-   **Terceros:** permite filtrar los resultados por **Terceros**. El informe resultante solo mostrará información sobre facturas de venta de los terceros seleccionados. No es un parámetro obligatorio, por lo que si no se selecciona ningún tercero, las facturas de venta no se filtrarán por ese campo.
-   **Mostrar solo con descuento:** si está marcado, solo se mostrarán los artículos con descuento.

### Ejemplo de salida del informe

![](../../../../assets/drive/1ycGDW3jPjlFaRlhOW4CxRZ4cxFfdW0iP.png)

Para el ejemplo de la imagen anterior, según los filtros, el resultado mostrará información sobre facturas de venta para el tercero “Alimentos y Supermercados, S.A.” desde la fecha “01-06-2021” hasta la fecha “01-01-2022”. Los importes estarán en USD.


Columnas a tener en cuenta:

-   **Cantidad:** es la cantidad total vendida para cada producto y tercero.
-   **Precio medio:** es el precio medio de un producto y tercero sin tener en cuenta los descuentos.
-   **Importe:** es el Precio medio multiplicado por la cantidad.
-   **Precio neto medio:** es el precio medio real de un producto y tercero, teniendo en cuenta los descuentos.
-   **Importe real:** el importe real vendido para un producto y tercero sin impuestos.
-   **Descuento (%):** es el descuento aplicado para el producto y el tercero.

En la imagen siguiente se muestra el mismo informe, pero habiendo marcado el filtro “Mostrar solo con descuento”. En comparación con el informe anterior, este informe muestra solo aquellas líneas en las que el descuento no es igual a cero.

![](../../../../assets/drive/1Z36B4O0Ih4xnuLhT_HYRHJfP0QlZDeiG.png)


## Informe pedidos pendientes y stock

:material-menu: `Aplicación` > `Gestión de Ventas` > `Herramientas de análisis` > `Informe pedidos pendientes y stock`

### Visión general

Esta sección muestra las líneas de los pedidos pendientes con el stock actual de cada producto.


## Pedidos no facturados

:material-menu: `Aplicación` > `Gestión de Ventas` > `Herramientas de análisis` > `Pedidos no facturados`

### Visión general

**Pedidos no facturados** muestra la información sobre los pedidos de venta que aún no están completamente facturados.

Solo los pedidos de venta con el término de facturación *No facturar* no se muestran en el informe, pero el resto de pedidos aparecen en la salida, independientemente de si se cumple o no la condición del término de facturación. Por ejemplo, si **Término de facturación** es "Después de la entrega" y los productos aún no se han enviado, el Pedido de venta se muestra.

![Orders Awaiting Invoice Report](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/analysis-tools/orders-awaiting-invoice-report.png)

### Ventana de parámetros

![Orders Awaiting Invoice](../../../../assets/drive/1m5K-52iabxWTBcYXnuBxhisNKIiOPhlP.png)

Todos los filtros hacen referencia a los campos correspondientes del **Pedido de venta**.

Todos los valores monetarios (como **Importe**, **Precio**, **Base**) del informe se muestran en dos monedas. La primera es la moneda del Pedido de venta, y la segunda está regulada por el campo parámetro Moneda (por defecto, la moneda del sistema). 

!!! warning
    Tenga en cuenta que debe especificarse el tipo de cambio a la Moneda del informe para que el informe funcione.

### Ejemplo de salida del informe

![Sample Report Output](../../../../assets/drive/1OTwoN7NttxZipv10smwuOv6ET_2OtddS.png)

!!! info
    Tenga en cuenta que el informe proporciona información sobre los pedidos de venta y los productos incluidos en ellos sin reflejar la información de las cantidades ya entregadas y facturadas.


## Informe de Pedidos a la Espera de Entrega

:material-menu: `Aplicación` > `Gestión de Ventas` > `Herramientas de análisis` > `Informe de Pedidos a la Espera de Entrega`

### Visión general

**Informe de Pedidos a la Espera de Entrega** muestra la información sobre los pedidos de venta que están a la espera (pendientes) de ser entregados (enviados).

![](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/analysis-tools/orders-awaiting-delivery-report-18.png)


### Ventana de parámetros

![Orders Awaiting Delivery](../../../../assets/drive/1hbLnfh3onAAqN6yKjgUh2VCPlgDrG8XK.png)

Todos los filtros hacen referencia a los campos correspondientes del Pedido de venta.

### Ejemplo de salida del informe

![Sample Report Output](../../../../assets/drive/1Liay4G2dIvO513rwpadunx-v0ud0rs87.png)


## Análisis dimensional facturas ventas

:material-menu: `Aplicación` > `Gestión de Ventas` > `Herramientas de análisis` > `Análisis dimensional facturas ventas`

### Visión general

Este es un informe de tipo dimensional que muestra información sobre las facturas de venta registradas (facturas de venta en estado *Completada* o *Anulada*) durante un periodo de tiempo seleccionado.

Este informe puede mostrar clasificaciones de productos y principales clientes en función de los ingresos por ventas, mostrar el beneficio y el margen de las ventas y responder a muchas otras preguntas relacionadas con la actividad de facturación de ventas de la empresa.

### Ventana de parámetros

![Sales Invoice Dimensional](../../../../assets/drive/1u4QnUnLSo4PvVzeduFYZDQgs3FKZwJMG.png)

Campos a tener en cuenta:

-   **Documento comercial:** permite al usuario filtrar los resultados por el campo Agente comercial de la ventana Factura de venta, que normalmente se hereda del Pedido de venta.
-   **Archivo comercial:** permite al usuario filtrar los resultados por el campo Agente comercial de la pestaña Cliente de la ventana Terceros, que normalmente contiene la persona responsable de este cliente (por ejemplo, el gestor de la cuenta).

!!! info
    En la mayoría de los casos, filtrar por los campos mencionados anteriormente ofrece los mismos resultados. Podrían diferir si un cliente tiene una persona responsable principal, pero distintos miembros del equipo de ventas pueden registrar pedidos. O si un cliente se traslada de un agente comercial a otro. Los nuevos agentes comerciales podrían querer utilizar el segundo filtro para ver las actividades de todos sus clientes (independientemente de quién cerró la operación), mientras que los antiguos agentes comerciales podrían querer utilizar el primer filtro para ver los pedidos que cerraron, independientemente de quién gestione actualmente al cliente.

-   **Proyecto:** permite al usuario mostrar información de facturación para un proyecto concreto.
-   **Tipo de producto:** filtro que muestra resultados para los tipos de producto seleccionados.

### Ejemplo de salida del informe

![Sample Report Output](../../../../assets/drive/19rJehYODpxaL4CHLStphythhzfSAswSq.png)

Columnas a tener en cuenta:

-   **Columna de moneda, p. ej. (EUR-€):** porcentaje del **Importe** de la fila concreta sobre el **Imp.total** del informe. Todas las filas deben sumar 100%.
-   **Importe:** es el importe **neto** de la Factura de venta convertido a la **Moneda** del informe.
-   **Costo:** coste de los bienes vendidos (según el coste correspondiente del producto).
    -   Puede haber transacciones de producto cuyo coste aún no se haya calculado; por lo tanto, el coste de esas transacciones se estima como un coste "proporcional" basado en el coste conocido de la transacción.
        -   En este caso, el coste estimado se muestra en color rojo.
-   **Beneficio:** es la diferencia entre **Importe** y **Costo**.
-   **M.%:** margen de ventas como ratio de **Beneficio** sobre **Importe**.
-   **Peso:** del producto facturado si se especifica en la ventana **Producto**.

**Cómo se calcula el coste estimado:**

En caso de que no exista un coste calculado para algunos de los registros recuperados, es necesario estimarlo. Para ello, se obtiene un coste unitario genérico para los registros con coste calculado y, utilizándolo, se realiza la estimación. La fórmula funciona de la siguiente manera:

Ejemplo: si existe un producto con una línea de factura de 100€ y tiene un coste calculado de 30€, para una línea de 200€, el coste estimado debería ser 60€.

Importe neto de la línea de 200€ \* (30€ de coste calculado/100€ de transacciones con coste calculado) = 60€. (30€ de coste calculado/100€ de transacciones con coste calculado) es el coste unitario.

En un escenario genérico, que no depende de ninguna dimensión como Producto:

**Coste estimado = Imp. total líneas \* (Coste calculado total/Imp. total líneas de transacciones con coste calculado)**, siendo (Coste calculado total/Imp. total líneas de transacciones con coste calculado) el coste unitario

Esto significa que la estimación depende de los registros recuperados. Cuantos más registros haya y más agrupados estén, más precisa será la estimación. Si el informe se divide por distintas dimensiones, las estimaciones pueden ser diferentes y, por lo tanto, los totales pueden tener una variación menor.

También existe la posibilidad de exportar este informe a un archivo PDF o XLS:

![Buttons](../../../../assets/drive/1SM0X-gfBBOlwyaKionNpxbUc_IVgK2L9.png)

El formato PDF muestra los mismos campos explicados anteriormente, pero en formato XLS se añaden nuevos campos relacionados con la factura seleccionada:

-   **Organización**
-   **Grupo de terceros**
-   **Terceros**
-   **Nº de documento**
-   **Fecha de la factura**
-   **Categoría de producto**
-   **Producto**
-   **Clave de búsqueda del producto**
-   **Precio unitario**
-   **Agente comercial**
-   **Proyecto**
-   **Dirección de envío**

En la parte superior del informe, ahora se muestran los filtros secundarios.

Además, este informe ahora muestra el total de coste, beneficio, margen-% y cantidad.

Al final del informe, hay una nueva tabla que muestra el número de documentos por tipo de documento.

---

Este trabajo es una obra derivada de [Gestión de Ventas](http://wiki.openbravo.com/wiki/Sales_Management){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.