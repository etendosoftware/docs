---
title: Movimiento entre almacenes
tags:
 - Goods Movement
 - Warehouse Management
 - Inventory
 - Transactions
---

# Movimiento entre almacenes { #goods-movement }

## Descripción general { #overview }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Movimiento entre almacenes`

La ventana **Movimiento entre almacenes** permite registrar y procesar movimientos internos de inventario entre almacenes y huecos (ubicaciones concretas dentro de un almacén, como una estantería o posición de rack — consulte [Almacén y huecos](../setup.md#warehouse-and-storage-bins)). Utilícela para transferir productos de una ubicación a otra y mantener los niveles de stock actualizados en todos los almacenes. Para una introducción al flujo de trabajo de almacén recomendado, consulte [Primeros pasos](../getting-started.md).

<iframe width="560" height="315" src="https://www.youtube.com/embed/yW4Bv6bORk0" title="reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Cómo registrar un movimiento entre almacenes { #how-to-record-a-goods-movement }

1. Vaya a `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Movimiento entre almacenes`.
2. Haga clic en **Nuevo** para crear un registro. Los campos **Nombre** y **Fecha del movimiento** se rellenan automáticamente — modifíquelos si es necesario.
3. Añada los productos a mover. Dispone de dos opciones:
    - **Un producto a la vez:** vaya a la solapa Líneas, haga clic en **Nuevo** y rellene el producto, la cantidad, el **Hueco** de origen y el **Movido a** (destino).
    - **Todos los productos de un hueco a la vez:** haga clic en **Mover un hueco entero**, seleccione los huecos de origen y destino, y confirme. El sistema añade una línea por producto automáticamente.
4. Revise las líneas para confirmar que las cantidades y ubicaciones son correctas.
5. Haga clic en **Procesar movimientos**. Los niveles de stock se actualizan de inmediato.

!!! info
    Antes de crear un Movimiento entre almacenes, asegúrese de que los almacenes y huecos correspondientes estén configurados. Consulte [Almacén y huecos](../setup.md#warehouse-and-storage-bins).

## Cabecera { #header }

Los movimientos internos de inventario pueden realizarse añadiendo productos en la solapa Líneas o moviendo todos los artículos a la vez mediante el botón **Mover un hueco entero**.

![Cabecera](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-3.png)

Todos los campos se rellenan automáticamente al crear un registro **nuevo**. Algunos a tener en cuenta:

- **Organización:** La organización a la que pertenece este movimiento entre almacenes. Se rellena automáticamente según la sesión del usuario.
- **Nombre:** este campo se utilizará para referenciar este movimiento entre almacenes, no solo en los informes de almacén sino también en el libro mayor; por lo tanto, es importante utilizar un nombre significativo.  
  Este campo toma por defecto la fecha actual, pero siempre puede modificarse según sea necesario.
- **Fecha del movimiento:** La fecha de la transferencia. Por defecto toma la fecha actual, pero puede modificarse. Importante: esta es la fecha en la que el movimiento aparece en los registros contables. Compruebe que es correcta antes de procesar.
- **Descripción:** Campo de texto libre opcional para añadir notas sobre el movimiento.
- **Proyecto** *(bajo Dimensiones):* Campo opcional para asociar este movimiento a un proyecto con fines contables y de informes.

Existen 2 formas de introducir líneas (o productos a mover entre almacenes y huecos):

1.  Añadiendo productos individuales en la solapa Líneas.
2.  Moviendo todos los artículos de un hueco a otro mediante el botón [**Mover un hueco entero**](#move-a-storage-bin).

![Cabecera](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-2.png)

## Líneas { #lines }

La solapa Líneas lista todos los productos que se van a mover, junto con su ubicación de origen, destino y cantidad.

![Líneas](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-1.png)

Algunos campos a tener en cuenta:

- **Producto:** El artículo a mover. Al seleccionar un producto, los campos Hueco y Cant. movida se rellenan automáticamente con los datos de stock actuales.
- **Cant. movida:** es la cantidad de producto a mover.  
  Por defecto, toma la cantidad total del **Producto** en el Hueco.
- **Hueco:** es el hueco del que se retiran los productos.  
  Por defecto, toma el Hueco seleccionado en el selector de **Producto**.
- **Movido a:** es el hueco de destino de los productos.
- **Nuevo Valor atributos:** Este campo solo aparece cuando el movimiento está vinculado a una operación de empaquetado o desempaquetado (consulte [Inventario referenciado](referenced-inventory.md)). Muestra la nueva etiqueta asignada al artículo tras ser colocado o retirado de un contenedor. No es necesario rellenarlo: se actualiza automáticamente.

Para revisar el historial de movimientos de productos, consulte [Informe de movimientos de productos](../analysis-tools/product-movements-report.md).

## Botones { #buttons }

### Mover un hueco entero { #move-a-storage-bin }

Utilice este botón para mover todos los productos de un hueco a otro en una sola acción. Al hacer clic, el sistema rellena la solapa Líneas con todos los productos del hueco de origen. Al hacer clic en Procesar movimiento, el sistema mueve todos esos productos al hueco de destino.

![](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-4.png)

### Generar tarea de reubicación { #generate-relocation-task }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Permite crear una tarea de reubicación desde el documento **Movimiento entre almacenes**. El sistema toma la información cargada en el registro y sus líneas y la envía a Etendo Mobile, donde el operario puede ejecutar el movimiento desde la subaplicación correspondiente. Al pulsarlo, se abre el pop-up de asignación automática o manual.

!!! info
    Para más información, visite [Tarea de reubicación](../../../optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#relocation-tasks)

### Procesar movimiento { #process-movement }

Este botón procesa el documento Movimiento entre almacenes. Al ejecutarlo, el sistema valida la información del movimiento y actualiza el stock en las ubicaciones correspondientes.

Para verificar los niveles de stock resultantes, consulte [Informe de stock](../analysis-tools/stock-report.md) o [Informe de transacciones de material](../analysis-tools/material-transaction-report.md).

![](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-5.png)


## Contabilidad { #accounting }

!!! info
    Antes de que un Movimiento entre almacenes pueda contabilizarse en el libro mayor, debe estar habilitado en el Esquema contable. Si el botón Contabilizar no está disponible, contacte con su administrador del sistema y pídale que active la tabla de Movimiento entre almacenes en la solapa Tablas a contabilizar del Esquema contable de la organización.

La contabilización de Movimiento entre almacenes crea los siguientes asientos contables.

Fecha de contabilización del registro: Fecha del movimiento.

|               |                           |                           |                             |
| ------------- | ------------------------- | ------------------------- | --------------------------- |
| Cuenta       | Débito                     | Crédito                    | Comentario                     |
| Inmovilizado del producto | Importe de coste de la línea de movimiento |                           | Una por cada línea de Movimiento entre almacenes |
| Inmovilizado del producto |                           | Importe de coste de la línea de movimiento | Una por cada línea de Movimiento entre almacenes |

Antes de contabilizar un Movimiento entre almacenes, el sistema debe calcular el coste de los artículos movidos. Para ello deben cumplirse dos condiciones:

- Debe existir una [Regla de cálculo de costes](../setup.md#costing-rules) validada para la empresa (entidad legal) propietaria de este movimiento entre almacenes.
- El [Proceso de background del cálculo de costes](../../general-setup/process-scheduling/process-request.md#costing) debe haberse ejecutado al menos una vez tras la creación del movimiento. Este proceso se ejecuta automáticamente según una programación. Si la contabilización falla, contacte con su administrador del sistema para confirmar que el proceso se ha ejecutado.

Una vez cumplidas ambas condiciones, el Movimiento entre almacenes puede contabilizarse.

Para consultar los niveles de stock a una fecha determinada, consulte [Historial de stock](../analysis-tools/stock-history.md).

## Cómo reactivar movimientos entre almacenes { #how-to-reactivate-goods-movements }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}

Desde la ventana Movimiento entre almacenes, el usuario puede reactivar un movimiento generado previamente simplemente seleccionando el movimiento necesario y haciendo clic en el botón Reactivar.

Una vez que el movimiento se reactiva correctamente, el estado del documento cambia a No procesado, tal y como puede observarse en la barra de estado.

![](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-6.png)

!!! warning
    No es posible reactivar documentos que incluyan transacciones con cantidades que superen la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando el hueco está configurado para permitir envíos que superen el stock disponible (Estado de inventario Stock Negativo). Para más información, visite [Estado de inventario](../../../../../developer-guide/etendo-classic/concepts/inventory-status.md).

La reactivación de un movimiento procesado puede afectar a los cálculos de costes. Consulte [Ajuste de costes](cost-adjustment.md) para más información.

## Contabilización masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro(s) se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo de Contabilización masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
