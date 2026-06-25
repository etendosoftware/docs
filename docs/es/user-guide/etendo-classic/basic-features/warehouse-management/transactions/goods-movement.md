---
title: Movimiento entre almacenes
tags:
 - Movimiento entre almacenes
 - Gestión de Almacén
 - Inventario
 - Transacciones
---

# Movimiento entre almacenes { #goods-movement }

## Descripción general { #overview }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Movimiento entre almacenes`

La ventana **Movimiento entre almacenes** registra y procesa movimientos internos de inventario entre almacenes y huecos (ubicaciones específicas dentro de un almacén, como la posición de una estantería o un rack — véase [Almacén y huecos](../setup.md#warehouse-and-storage-bins)). Úsela para transferir productos de una ubicación a otra y mantener los niveles de stock precisos en todos los almacenes. Para una introducción al flujo de trabajo de almacén recomendado, véase [Primeros pasos](../getting-started.md).

<iframe width="560" height="315" src="https://www.youtube.com/embed/yW4Bv6bORk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cómo registrar un movimiento entre almacenes { #how-to-record-a-goods-movement }

1. Vaya a `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Movimiento entre almacenes`.
2. Haga clic en **Nuevo** para crear un registro. Los campos **Nombre** y **Fecha del movimiento** se completan automáticamente — actualícelos si es necesario.
3. Agregue los productos a mover. Dispone de dos opciones:
    - **Un producto a la vez:** vaya a la pestaña **Líneas**, haga clic en **Nuevo** y complete el producto, la cantidad, el **Hueco** de origen y el **Movido a** (destino).
    - **Todos los productos de un hueco a la vez:** haga clic en **Mover un hueco entero**, seleccione los huecos de origen y destino y confirme. El sistema agrega una línea por producto de forma automática.
4. Revise las líneas para confirmar que las cantidades y ubicaciones son correctas.
5. Haga clic en **Procesar movimientos**. Los niveles de stock se actualizan de inmediato.

## Cabecera { #header }

El registro de cabecera contiene la fecha, el nombre y el contexto organizativo del movimiento. Todos los campos se completan previamente al crear un nuevo registro.

![goods-movement-3](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-3.png)

- **Organización:** La organización a la que pertenece este movimiento entre almacenes. Se completa previamente según la sesión del usuario.
- **Nombre:** El nombre de referencia de este movimiento entre almacenes. Aparece en los informes de almacén y en el libro mayor, por lo que se recomienda usar un nombre descriptivo. Por defecto, toma la fecha actual.
- **Fecha del movimiento:** La fecha de la transferencia. Por defecto, es la fecha de hoy. Esta es la fecha con la que el movimiento aparece en los registros contables — confirme que es correcta antes de procesar.
- **Descripción:** Campo de texto libre opcional para notas sobre el movimiento.
- **Proyecto** *(bajo Dimensiones):* Campo opcional para asociar este movimiento con un proyecto a efectos contables y de reporte.



## Líneas { #lines }

La pestaña **Líneas** lista todos los productos a mover, junto con su ubicación de origen, destino y cantidad.

Existen dos formas de agregar líneas (productos a mover entre almacenes y huecos):

1. Agregar productos individuales en la pestaña **Líneas**.
2. Mover todos los artículos de un hueco a otro mediante el botón [**Mover un hueco entero**](#move-a-storage-bin).


![goods-movement-1](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-1.png)

Algunos campos a tener en cuenta:

- **Producto:** El artículo a mover. Al seleccionar un producto, se completan automáticamente los campos **Hueco** y **Cant. movida** con los datos de stock actuales.
- **Cant. movida:** La cantidad a mover. Por defecto, toma la cantidad total del producto en el **Hueco** seleccionado.
- **Hueco:** La ubicación desde la que se toman los productos. Se completa previamente según el producto seleccionado. Modifíquelo si es necesario.
- **Movido a:** El hueco de destino para los productos.
- **Nuevo Valor atributos:** No es necesario completar este campo — se actualiza automáticamente. Aparece únicamente cuando el almacén utiliza funciones de seguimiento de contenedores (véase [Inventario Referenciado](referenced-inventory.md)).

Para revisar el historial de movimientos de productos, véase [Informe de movimientos de productos](../analysis-tools/product-movements-report.md).

## Botones { #buttons }

### Mover un hueco entero { #move-a-storage-bin }

Use este botón para mover todos los productos de un hueco a otro en una sola acción. Al hacer clic, el sistema completa la pestaña **Líneas** con todos los productos encontrados en el hueco de origen. Al hacer clic en **Procesar movimientos**, el sistema mueve todos esos productos al hueco de destino.

![goods-movement-4](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-4.png)

### Generar tarea de reubicación { #generate-relocation-task }

!!! info
    Para incluir esta funcionalidad, debe estar instalado el Warehouse Extensions Bundle. Siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Warehouse Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Crea una tarea de reubicación a partir del documento **Movimiento entre almacenes**. El sistema lee el registro y sus líneas y envía los datos del movimiento a Etendo Mobile. Desde allí, un operador de almacén lleva a cabo el movimiento físico utilizando la aplicación móvil correspondiente. Al hacer clic, se abre el pop-up de asignación automática o manual.

!!! info
    Para más información, visite [Tarea de reubicación](../../../optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#relocation-tasks).

### Procesar movimientos { #process-movement }

Este botón procesa el documento **Movimiento entre almacenes**. El sistema valida la información del movimiento y actualiza el stock en las ubicaciones correspondientes.

Para verificar los niveles de stock resultantes, véase [Informe de stock](../analysis-tools/stock-report.md) o [Informe de transacciones de materiales](../analysis-tools/material-transaction-report.md).

![goods-movement-5](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-5.png)

## Contabilidad { #accounting }

!!! info
    Antes de que un Movimiento entre almacenes pueda contabilizarse en el libro mayor, debe estar habilitado en la configuración del libro mayor. Si el botón **Contabilizar** no está disponible, contacte con su administrador del sistema y solicítele que active la tabla **Movimiento entre almacenes** en la pestaña **Tablas a contabilizar** de la configuración del libro mayor de la organización.

La contabilización del Movimiento entre almacenes genera los siguientes asientos contables.

Fecha de contabilización del registro: Fecha del movimiento.

|                              |                                              |                                              |                                                           |
| ---------------------------- | -------------------------------------------- | -------------------------------------------- | --------------------------------------------------------- |
| Cuenta                       | Débito                                       | Crédito                                      | Comentario                                                |
| Inmovilizado del producto    | Importe de coste de la línea de movimiento   |                                              | Una por cada línea de Movimiento entre almacenes          |
| Inmovilizado del producto    |                                              | Importe de coste de la línea de movimiento   | Una por cada línea de Movimiento entre almacenes          |

La contabilización requiere que su administrador del sistema haya configurado dos aspectos:

1. Se ha configurado y aprobado una regla de cálculo de costes para su empresa. Véase [Regla de cálculo de costes](../setup.md#costing-rules).
2. El proceso automatizado de cálculo de costes del sistema se ha ejecutado desde que se guardó el movimiento. Véase [Proceso en segundo plano de cálculo de costes](../../general-setup/process-scheduling/process-request.md#costing).

Si la contabilización falla, contacte con su administrador del sistema para confirmar que ambos aspectos están configurados.

Una vez cumplidas ambas condiciones, el Movimiento entre almacenes puede contabilizarse.

Para revisar los niveles de stock a una fecha determinada, véase [Historial de stock](../analysis-tools/stock-history.md).

## Cómo reactivar movimientos entre almacenes { #how-to-reactivate-goods-movements }

!!! info
    Para incluir esta funcionalidad, debe estar instalado el Warehouse Extensions Bundle. Siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

Para corregir un movimiento entre almacenes que ya ha sido procesado — por ejemplo, tras detectar un error en las cantidades transferidas — reactívelo para realizar cambios. Desde la ventana **Movimiento entre almacenes**, seleccione el documento correspondiente y haga clic en **Reactivar**.

Una vez que el movimiento se reactiva correctamente, la barra de estado del documento muestra *No procesado*, confirmando que la reactivación fue exitosa.

![goods-movement-6](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-6.png)

!!! warning
    No es posible reactivar documentos que incluyan transacciones con cantidades que superen la cantidad de stock existente para un producto en un hueco determinado. La única excepción es cuando el hueco está configurado para permitir envíos que superen el stock disponible (conocido como Over Issue). Esta configuración la realiza su administrador del sistema. Para más información, visite [Estado de inventario](../../../../../developer-guide/etendo-classic/concepts/inventory-status.md).

Reactivar un movimiento procesado puede afectar a los cálculos de costes. Véase [Ajuste de costes](cost-adjustment.md) para más información.

## Contabilización Masiva { #bulk-posting }

!!! info
    Para incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

Use esta opción cuando necesite contabilizar un gran número de movimientos en el libro mayor en un solo paso, en lugar de procesar cada uno individualmente.

Seleccione los registros correspondientes y haga clic en **Contabilización Masiva**. El estado contable de cada registro se muestra en la barra de estado en la vista de formulario, o en una columna en la vista de grilla.

!!! info
    Para más información, visite [la guía de usuario del módulo de Contabilización Masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
