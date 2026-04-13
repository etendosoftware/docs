---
title: Gestión de Almacén - Primeros pasos
tags: 
 - primeros pasos
 - gestión de almacén
 - precisión del inventario
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Gestión de Almacén - Primeros pasos

## Visión general

<iframe width="720" height="480" src="https://www.youtube.com/embed/l7RMb0Oz7Wo?si=ngxYnwDkiDqwRkLO" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

En Etendo, la mayoría de los movimientos de almacén se crean automáticamente en función de las transacciones de los procesos de [Ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/getting-started.md) y [Gestión de Compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/getting-started.md). Sin embargo, la operativa de un almacén también implica varias actividades manuales, como el inventario físico, los movimientos de mercancía y su seguimiento, y la valoración del inventario. Estas actividades se ejecutan en el área de aplicación Gestión de Almacén y se agrupan en el flujo de negocio Precisión del inventario, que se describe a continuación.

## Precisión del inventario

![](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/getting-started/walltowallaccubusprocess.png)

Los principales subprocesos del flujo de negocio Precisión del inventario son:

- *Inventario físico*: es un proceso en el que una empresa cuenta físicamente los artículos individuales en stock en un momento determinado y actualiza su recuento de inventario dentro del sistema (si es necesario). Representa una oportunidad para corregir cualquier inexactitud en los registros. A continuación se indican varias razones para realizar un inventario físico:
    - Iniciar el stock
    - Verificar la cantidad física, el estado y la ubicación de los artículos de inventario
    - Identificar, documentar y añadir a su lista de inventario artículos disponibles que cumplan los criterios de calificación, pero que actualmente no se muestran como parte del inventario
    - Asegurar que los artículos transferidos o dados de baja legítimamente ya no se mantienen en el listado de inventario
    - Identificar cualquier artículo faltante o dañado que deba localizarse, repararse o sustituirse.
- *Movimiento entre almacenes*: transfiere inventario entre huecos de almacenamiento o almacenes. Algunas razones posibles para un movimiento de mercancía son:
    - Mercancía recibida en el almacén desde otra parte o almacén.
    - Movimiento de inventario debido a la conversión de mercancía.
- *Seguimiento de mercancías*: muestra todos los diferentes tipos de movimiento que ocurren en el almacén para verificar el historial, la ubicación o la aplicación de un artículo mediante una identificación registrada y documentada.
- *Valoración del inventario*: permite a una empresa asignar un valor monetario a los artículos que componen su inventario.
- *Actualización de inventario*: permite a una empresa cambiar el importe actual del inventario o el coste unitario actual de los productos en stock.
- *Revisión de ajustes de costes*: permite a una empresa revisar los ajustes de coste de producto causados por cambios en los precios de compra, la asignación de landed costs o correcciones manuales / negativas de coste.

### Configuración

Es necesario crear y configurar [Almacén y huecos](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#warehouse-and-storage-bins) antes de ejecutar el flujo de negocio.
Además, es necesario definir y validar una [Regla de cálculo de costes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#costing-rules) para la entidad legal. Cada regla de cálculo de costes requiere una fecha de inicio a partir de la cual será válida, así como un [Algoritmo de cálculo de costes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#costing-algorithm) que será utilizado por el proceso [Costing Background Process](../../../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request.md#costing), que debe planificarse.

Además, es necesario configurar [Tipo de Landed Cost](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#landed-cost-type), por lo que podrán seleccionarse al asignar este tipo de coste a [Albarán (Proveedor)](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#goods-receipts).

Por último, pueden configurarse [Reglas de almacén](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#warehouse-rules) para que se apliquen al recuperar stock del inventario de forma automática.

!!!note
        No es necesario realizar ninguna configuración adicional para el área de aplicación Gestión de Almacén si se va a utilizar el cliente de ejemplo Food & Beverage (F&B) que Etendo incluye por defecto para explorarlo. El conjunto de datos de ejemplo ya contiene los roles, almacenes y productos preconfigurados.

La configuración anterior forma parte del flujo general de configuración del negocio dentro de la configuración de "Almacén".

### Ejecución

En Gestión de Almacén, las principales operaciones de Precisión del inventario se ejecutan de la siguiente manera.

Para realizar el *Inventario físico*, el personal de almacén:

- Comienza con las clasificaciones de productos y ejecuta el [Informe Pareto de Productos](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#pareto-product-report), que distribuye los productos en tres clases (A, B o C) según su porcentaje de coste en el almacén.
En función de la clasificación, puede decidirse la frecuencia del ciclo de recuento (p. ej., los productos A se cuentan semanalmente, los productos B mensualmente y los productos C anualmente).
A continuación, la clasificación ABC se rellena en la pestaña [Producción](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#manufacturing) de la ventana Producto haciendo clic en el botón Update ABC.
    - Tenga en cuenta que la clasificación ABC se basa en el coste de las transacciones del producto. Por eso debe configurarse y validarse una [Regla de cálculo de costes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#costing-rules) para la entidad legal y debe planificarse el proceso [Costing Background Process](../../../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request.md#costing).
- Tras este procedimiento, el personal de almacén crea el documento de inventario físico en la ventana [Inventario físico](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#physical-inventory) seleccionando el Almacén donde ejecutar esta actividad y pulsando el botón Create Inventory Count List. Definen los criterios para los productos que se incluirán en la lista de recuento (por ejemplo, la clasificación ABC) y el resultado es la [Lista](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#lines) de productos con sus cantidades actuales, que se lleva al almacén y se verifica frente al inventario físico.
- Para actualizar el stock en Etendo, si se encuentran diferencias, primero el personal de almacén selecciona el [Inventario físico](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#physical-inventory) que se creó previamente. A continuación, en la pestaña [Líneas](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#lines), encuentran los productos requeridos y actualizan el campo Quantity Count con un nuevo valor. Después, finalizan el recuento de inventario haciendo clic en el botón Process Inventory Count, que actualiza el inventario y lanza el contabilizado del documento (si está configurado).

Para ejecutar *Movimiento entre almacenes*, el personal de almacén:

- En la ventana [Movimiento entre almacenes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#goods-movement), lista los productos a mover con la información de origen y destino y la cantidad correspondiente, y luego procesa el documento, lo que actualiza todas las cantidades de producto listadas en la pestaña Líneas en el almacén y lanza el contabilizado del documento (si está configurado).

Para *Seguimiento de mercancías*, el personal de almacén utiliza:

- [Informe Stock](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#stock-report), que proporciona el nivel de stock de todos los productos (que tienen inventario distinto de cero) y su ubicación (almacén y hueco) agrupados por categoría de producto.
- La ventana [Operaciones de material (uso indirecto)](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#goods-transaction), que ofrece una vista de solo lectura con amplias capacidades de filtrado y muestra todas las transacciones de inventario.
- [Informe Movimiento de Productos](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#product-movements-report), que muestra todas las recepciones, envíos, movimientos e inventarios físicos agrupados por Tipo de transacción y Tercero.
- [Informe Transacción de Material](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#material-transaction-report), que lista todos los documentos (envíos o recepciones) agrupados por Tercero.

La *Valoración del inventario* se realiza con la ayuda del [Informe de Valuación de Existencias](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#valued-stock-report).
Este informe muestra el coste del stock calculado por el proceso Costing Server.

La *Actualización de inventario* se realiza con la ayuda de la ventana [Ajuste de Valor del Inventario](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#inventory-amount-update).
Esta ventana permite cambiar el valor total del inventario o el coste unitario de uno o varios productos en una fecha de referencia determinada; por tanto, se crean automáticamente un inventario de cierre y uno de apertura en la ventana [Inventario físico](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#physical-inventory).

Para la *Revisión de ajustes de costes*, el personal de almacén utiliza la ventana [Ajuste de Costes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#cost-adjustment).
Esta ventana permite revisar diferentes tipos de orígenes de ajuste de costes junto con las transacciones del producto cuyos costes se están ajustando, así como los importes del ajuste.

## Relación con otras áreas de aplicación

Gestión de Almacén tiene conexión con otras áreas de aplicación:

- [Gestión de Compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/getting-started.md) ya que la mercancía recibida cambia la cantidad de stock y su valor.
- [Gestión de Ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/getting-started.md) ya que el envío cambia la cantidad de stock y su valor.
- *Gestión de Producción* porque las materias primas se retiran del almacén y los productos fabricados se devuelven al stock durante el proceso de producción.

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.