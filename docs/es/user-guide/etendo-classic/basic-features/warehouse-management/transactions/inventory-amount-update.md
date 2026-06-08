---
title: Ajuste de Valor del Inventario
tags:
 - Inventory Amount Update
 - Warehouse Management
 - Cost
 - Transactions
---

# Ajuste de Valor del Inventario { #inventory-amount-update }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Ajuste de Valor del Inventario`

## Visión general { #overview }

La ventana **Ajuste de Valor del Inventario** permite al usuario cambiar el **Valor del Inventario Actual** o el **Coste Unitario actual** de los productos en stock en una **Fecha de Referencia** determinada.

Una vez creado y procesado, genera un inventario de cierre y un inventario de apertura para el/los producto(s), que pueden revisarse en la solapa **Inventarios**.

- **Inventario de cierre** elimina el valor de inventario "actual" del producto (al coste actual, ya sea "medio" o "estándar")
- **Inventario de apertura** añade el valor de inventario "nuevo" del producto (al coste actual, ya sea "medio" o "estándar")

Siempre que se cree un ajuste de valor del inventario en la fecha actual, por lo tanto la **Fecha del movimiento** es la misma que la fecha de proceso de la transacción, todas las transacciones existentes permanecen valoradas al coste existente, pero las nuevas contabilizadas a partir de la fecha actual se valorarán al nuevo coste.

Siempre que se cree un ajuste de valor del inventario en el pasado, esos inventarios de cierre/apertura tendrán una **Fecha del movimiento** en el pasado y una fecha de proceso de la transacción. Estos inventarios se establecerán como transacciones "**Retroactivas**" por el proceso de cálculo de costes en segundo plano, por lo tanto se podrá crear el correspondiente ajuste de costes retroactivo.

Estas dos transacciones de inventario, inventario de apertura/cierre, pueden revisarse en la solapa **Transacción** de la ventana de producto y pueden contabilizarse en el libro mayor en la ventana **Inventario físico**.

## Cabecera { #header }

Un **Ajuste de Valor del Inventario** puede crearse y procesarse en la sección de cabecera de la ventana **Ajuste de Valor del Inventario**.

Un ajuste de valor del inventario puede crearse, gestionarse y procesarse en la sección de cabecera de la ventana **Ajuste de Valor del Inventario**.

![Cabecera](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/inventory-amount-update/inventory-amount-update-1.png)

Algunos campos a tener en cuenta son:

- **Tipo de documento**: es el tipo de documento del ajuste de valor del inventario
- **Nº de documento**: es la secuencia del documento del ajuste de valor del inventario
- **Fecha del documento**: es la fecha del ajuste de valor del inventario.

## Líneas { #lines }

Una vez que la cabecera del ajuste de valor del inventario se ha creado y guardado correctamente, pueden crearse líneas del ajuste de valor del inventario en esta solapa.

Un ajuste de valor del inventario puede tener tantas líneas como productos cuyo coste actual o valor de inventario necesite modificarse por cualquier motivo.

Al seleccionar un producto e introducir una fecha de referencia determinada, el valor de inventario actual, la **Cant. Disponible** y el coste unitario actual del producto se completan automáticamente.

Para completar la línea es necesario informar **Valor del Inventario** o **Coste Unitario**.

!!! info
    Es importante remarcar que la cantidad disponible del producto mostrada en un **Ajuste de Valor del Inventario** puede variar si el indicador **Ajuste Retroactivo de Transacciones** está activo/no activo en la regla de cálculo de costes correspondiente.

Por ejemplo, se contabiliza una entrega de 100 unidades para un producto en la fecha actual y, después, se contabiliza otra entrega de 50 unidades para un producto con una fecha de movimiento en el pasado. Esta última entrega es una transacción "retroactiva".

Se lanza un **Ajuste de Valor del Inventario** para el producto con fecha entre medias, anterior a la fecha actual:

- si **Ajuste Retroactivo de Transacciones** está activo, el **Ajuste de Valor del Inventario** lanzado para el producto tendrá en cuenta las transacciones "retroactivas" contabilizadas para ese producto, por lo tanto el stock mostrado será de 50 unidades. En este caso se considera la "fecha del movimiento" de la transacción retroactiva.
- si **Ajuste Retroactivo de Transacciones** no está activo, el **Ajuste de Valor del Inventario** lanzado para el producto no tendrá en cuenta las transacciones "retroactivas" contabilizadas para ese producto, por lo tanto el stock mostrado será de 0 unidades. En este caso no se considera la "fecha del movimiento" de la transacción retroactiva, sino la "fecha de proceso" de la transacción (fecha actual).

Algunos campos a tener en cuenta son:

- **Fecha de Referencia**: es la fecha en la que el ajuste de valor del inventario debe registrarse/contabilizarse en el libro mayor; por lo tanto, podría impactar en el coste de las transacciones de producto con fecha posterior.
- **Producto**: es el producto cuyo valor de inventario necesita cambiar.
- **Valor del Inventario Actual**: una vez seleccionado el producto, este campo muestra el valor de inventario actual del producto en la fecha de referencia indicada.
- **Coste Unitario actual**: una vez seleccionado el producto, este campo muestra el coste unitario actual del producto.
- **Cant. Disponible**: una vez seleccionado el producto, este campo muestra la cantidad disponible del producto en la fecha de referencia indicada.
- **Valor del Inventario**: este campo permite introducir un valor de inventario "nuevo" para el producto. Una vez introducido, el campo **Coste Unitario** se completa en consecuencia, teniendo en cuenta el campo **Cant. Disponible**.
- **Coste Unitario**: este campo permite introducir un coste unitario "nuevo" para el producto. Una vez introducido, el campo **Valor del Inventario** se completa en consecuencia, teniendo en cuenta el campo **Cant. Disponible**.

![Líneas](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/inventory-amount-update/inventory-amount-update-2.png)

Una vez creado, un ajuste de valor del inventario puede procesarse usando el botón de proceso **Proceso**.

Esa acción crea una transacción de inventario de cierre y otra de apertura que pueden revisarse en la solapa **Inventarios**.

## Inventarios { #inventories }

Se crean un inventario de cierre y uno de apertura para cada producto cuyo coste unitario o valor de inventario haya sido modificado.

Esta solapa de solo lectura contiene enlaces a información detallada como:

- **Almacén**: es el almacén donde ha tenido lugar el ajuste de valor del inventario.
- **Cerrar inventario**: es la transacción de inventario de cierre que elimina el inventario actual del producto al coste unitario actual.
- **Iniciar inventario**: es la transacción de inventario de apertura que añade el nuevo inventario del producto al nuevo coste unitario.

![Inventarios](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/inventory-amount-update/inventory-amount-update-3.png)

El inventario de apertura y cierre puede revisarse y contabilizarse en el libro mayor en la ventana **Inventario físico**.

La contabilización del inventario de cierre crea los siguientes asientos contables:

|                         |                          |                          |
| ----------------------- | ------------------------ | ------------------------ |
| Cuenta                 | Debe                    | Haber                   |
| _Diferencias de almacén_ | Valor del Inventario Actual |                          |
| _Inmovilizado del producto_         |                          | Valor del Inventario Actual |

La contabilización del inventario de apertura crea los siguientes asientos contables:

|                         |                      |                      |
| ----------------------- | -------------------- | -------------------- |
| Cuenta                 | Debe                | Haber               |
| _Inmovilizado del producto_         | Nuevo Valor del Inventario |                      |
| _Diferencias de almacén_ |                      | Nuevo Valor del Inventario |
