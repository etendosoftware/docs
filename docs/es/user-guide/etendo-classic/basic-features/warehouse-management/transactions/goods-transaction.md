---
title: Operaciones de material (uso indirecto)
tags:
 - Operaciones de material
 - Gestión de almacén
 - Inventario
 - Transacciones
---

# Operaciones de material (uso indirecto) { #goods-transaction }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Operaciones de material (uso indirecto)`

## Descripción general { #overview }

La ventana **Operaciones de material (uso indirecto)** es el registro central de cada movimiento de inventario en Etendo. Proporciona un historial completo, con la fecha y hora exactas de cada movimiento — qué se movió, cuándo, dónde y por qué — de modo que se pueda rastrear cualquier cambio hasta su origen.

Esta ventana captura todos los movimientos de inventario registrados en el sistema, incluyendo [Albaranes (Proveedor)](../../procurement-management/transactions.md#goods-receipts), [Albaranes (Cliente)](../../sales-management/transactions.md#goods-shipment), [Inventarios físicos](physical-inventory.md), [Movimientos entre almacenes](goods-movement.md), [Partes de Trabajo](../../production-management/transactions.md#work-effort), [Consumos internos](../../production-management/transactions.md#internal-consumption), [Devolución a proveedor](../../procurement-management/transactions.md#return-to-vendor-rtv) y [Devolución de cliente](../../sales-management/transactions.md#return-from-customer). Cada movimiento aparece aquí como una línea individual en cuanto se procesa en el sistema — sin pasos adicionales.

Esta ventana se puede filtrar por almacén, producto, rango de fechas o tipo de movimiento y ver los resultados de inmediato — no es necesario ejecutar ni generar un informe. La ventana es de solo lectura: puede ver y filtrar registros, pero no puede crearlos ni editarlos aquí.

<figure markdown="span">
  ![Operaciones de material (uso indirecto)](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-transaction/goods-transaction-1.png)
  <figcaption>La ventana Operaciones de material muestra los registros de movimientos de inventario con su tipo de movimiento, fecha, producto y cantidad.</figcaption>
</figure>

### Cuándo utilizar esta ventana { #when-to-use-this-window }

- **Investigar una discrepancia de stock**: filtre por producto y rango de fechas para encontrar todos los movimientos que afectaron un nivel de stock e identificar qué causó el cambio. Utilice el [Informe Stock](../analysis-tools/stock-report.md) para ver los niveles de stock actuales resultantes por hueco.
- **Auditar una transacción específica**: confirme la cantidad exacta y el tipo de movimiento registrados después de procesar un albarán de proveedor, un albarán de cliente o un inventario físico. Utilice el [Informe Transacción de Material](../analysis-tools/material-transaction-report.md) para obtener el coste y los detalles de contabilidad asociados.
- **Rastrear un lote o número de serie**: filtre por **Valor atributos** para ver el historial completo de movimientos de un artículo con seguimiento desde la recepción hasta el envío. El [Informe Movimiento de Productos](../analysis-tools/product-movements-report.md) proporciona el mismo historial con filtrado adicional por almacén y fecha.
- **Verificar la actividad de un hueco**: filtre por **Hueco** para revisar todos los movimientos que han afectado a una ubicación de almacén específica. Utilice el [Historial de existencias](../analysis-tools/stock-history.md) para ver cómo eran los niveles de stock en cualquier momento del pasado.

## Columnas { #columns }

Cada fila de la ventana **Operaciones de material (uso indirecto)** representa una línea de movimiento de inventario. Las columnas que se describen a continuación muestran la información disponible para cada entrada.

- **Ubicación de almacén (hueco)**: La estantería, rack o ubicación específica dentro del almacén de donde se tomó o donde se depositó el stock.
- **Fecha del movimiento**: La fecha en que se registró el movimiento en Etendo, utilizada con fines de costeo y contabilidad.
- **Producto**: El producto implicado en la transacción.
- **Valor atributos**: El número de lote o número de serie del producto, cuando el producto está configurado para seguimiento de lote o serie en Etendo. Este campo está vacío si el producto no utiliza seguimiento.
- **Tipo de movimiento**: La categoría de la transacción de inventario (por ejemplo, Albarán proveedor, Albarán cliente o Inventario físico).
- **Cant. movida**: La cantidad movida. Los valores positivos indican un aumento de stock; los valores negativos indican una disminución de stock.
- **Unidad**: La unidad de medida del producto.
- **Cant. pedido**: La cantidad de la línea de pedido de compra o venta original que generó este movimiento, cuando el movimiento proviene de un pedido. Este campo puede estar vacío en los ajustes de inventario físico.

### Tipo de movimiento { #movement-type }

La columna **Tipo de movimiento** identifica la categoría de cada transacción de inventario. Los posibles valores son:

- **Albarán proveedor**: stock recibido de un proveedor.
- **Devolución proveedor**: stock devuelto a un proveedor.
- **Devolución del cliente**: stock devuelto por un cliente.
- **Albarán cliente**: stock enviado a un cliente.
- **Traslado entrada**: stock que llega a la ubicación de destino tras un traslado interno.
- **Traslado salida**: stock que sale de la ubicación de origen durante un traslado interno.
- **Entrada inventario**: aumento de stock registrado durante un inventario físico.
- **Salida inventario**: disminución de stock registrada durante un inventario físico.
- **Entrada de producción**: stock añadido como resultado de una orden de trabajo de producción.
- **Salida de producción**: stock consumido como insumo de una orden de trabajo de producción.
- **Consumo interno**: stock retirado para uso interno.
- **Reversión de consumo interno**: stock reincorporado al inventario tras anular un consumo interno.

## Filtros { #filters }

Los filtros se aplican directamente en la fila de encabezados de la tabla de resultados. Escriba un valor o seleccione un rango en el encabezado de cualquier columna y la tabla se actualiza de inmediato, sin necesidad de pasos adicionales.

Combinaciones de filtros útiles para tareas habituales de almacén:

- **Producto** + rango de **Fecha del movimiento**: rastrea toda la actividad de un artículo específico durante un período determinado. Use esta combinación para la conciliación de stock o las reclamaciones a proveedores.
- **Tipo de movimiento**: aísla una categoría de transacción — por ejemplo, todos los albaranes de proveedor o todos los albaranes de cliente. Use este filtro para revisar un flujo específico sin interferencias de otros tipos de movimiento.
- **Hueco**: audita todos los movimientos que afectaron a una ubicación de almacén específica. Use este filtro para identificar stock fuera de lugar o confirmar que un hueco está vacío.
- **Valor atributos**: rastrea el historial completo de movimientos de un lote o número de serie específico desde la recepción hasta el envío. Use este filtro para la trazabilidad e investigaciones de calidad.

*[UOM]: Unidad de medida
*[RTV]: Devolución a proveedor

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
