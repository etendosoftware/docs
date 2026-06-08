---
title: Movimiento entre almacenes
tags:
 - Goods Movement
 - Warehouse Management
 - Inventory
 - Transactions
---

# Movimiento entre almacenes { #goods-movement }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Movimiento entre almacenes`

La ventana Movimiento entre almacenes permite al usuario realizar movimientos internos de inventario entre almacenes y huecos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yW4Bv6bORk0" title="reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cabecera { #header }

Los movimientos internos de inventario pueden realizarse añadiendo productos en la solapa Líneas o moviendo todos los artículos a la vez.

![Cabecera](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-1.png)

Todos los campos se rellenan automáticamente al crear un registro **nuevo**. Algunos a tener en cuenta:

- **Nombre:** este campo se utilizará para referenciar este movimiento entre almacenes, no solo en los informes de almacén sino también en el libro mayor; por lo tanto, es importante utilizar un nombre significativo.  
  Este campo toma por defecto la fecha actual, pero siempre puede modificarse según sea necesario.
- **Fecha del movimiento:** es la fecha de la transacción del movimiento entre almacenes.  
  Este campo toma por defecto la fecha actual, pero siempre puede modificarse según sea necesario.  
  Desde el punto de vista contable, el movimiento entre almacenes se reflejará en esta fecha.

Como ya se ha mencionado, existen 2 formas de introducir líneas (o productos a mover entre almacenes y huecos):

1.  Añadiendo productos individuales en la solapa Líneas.
2.  Moviendo todos los artículos de un hueco (**Hueco origen**) a otro (**Hueco destino**) mediante el botón **Mover un hueco entero**.  
    El sistema inserta automáticamente una línea por cada hueco y producto.

![Cabecera](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-2.png)

## Líneas { #lines }

La solapa Líneas es una lista de los productos movidos entre almacenes y huecos.

Esta solapa también incluye información sobre el origen, el destino y la cantidad correspondiente.

![Líneas](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-3.png)

Algunos campos a tener en cuenta:

- **Cant. movida:** es la cantidad de producto a mover.  
  Por defecto, toma la cantidad total del **Producto** en el Hueco.
- **Hueco:** es el hueco del que se retiran los productos.  
  Por defecto, toma el Hueco seleccionado en el selector de **Producto**.
- **Movido a:** es el hueco de destino de los productos.
- **Nuevo Valor atributos:** campo de solo lectura que solo es visible para transacciones de empaquetado/desempaquetado relacionadas con *Inventario Referenciado*. Muestra el nuevo valor de atributos tras realizarse el proceso de empaquetado/desempaquetado.

Una vez ejecutado el proceso **Procesar movimientos**, el stock se actualiza.

## Botones { #buttons }

### Mover un hueco entero { #move-a-storage-bin }

Este botón le permite transferir rápidamente todos los productos ubicados en un Hueco A a otro Hueco B de destino.  
Al hacer clic, el sistema muestra automáticamente en las líneas una lista de productos de la ubicación de origen seleccionada.  
Al procesar la transferencia, todos los productos se transfieren del origen al destino.

![](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-4.png)

### Generar tarea de reubicación { #generate-relocation-task }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Permite crear una tarea de reubicación desde el documento **Movimiento entre almacenes**. El sistema toma la información cargada en el registro y sus líneas y la envía a Etendo Mobile, donde el operario puede ejecutar el movimiento desde la subaplicación correspondiente. Al pulsarlo, se abre el pop-up de asignación automática o manual.

!!! info
    Para más información, visite [Tarea de reubicación](../../../optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#relocation-tasks)

### Procesar movimiento { #process-movement }

Este botón procesa el documento Movimiento entre almacenes. Al ejecutarlo, el sistema valida la información del movimiento y actualiza el stock en las ubicaciones correspondientes.

![](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-5.png)

## Contabilidad { #accounting }

!!! info
    Un Movimiento entre almacenes puede contabilizarse en el libro mayor si la tabla MaterialMgmtInternalMovement está configurada como Activa en la solapa Tablas activas de la configuración del libro mayor de la organización.

La contabilización de Movimiento entre almacenes crea los siguientes asientos contables.

Fecha de contabilización del registro: Fecha del movimiento.

|               |                           |                           |                             |
| ------------- | ------------------------- | ------------------------- | --------------------------- |
| Cuenta       | Débito                     | Crédito                    | Comentario                     |
| Inmovilizado del producto | Importe de coste de la línea de movimiento |                           | Una por cada línea de Movimiento entre almacenes |
| Inmovilizado del producto |                           | Importe de coste de la línea de movimiento | Una por cada línea de Movimiento entre almacenes |

La contabilización de un _Movimiento entre almacenes_ implica tener su coste calculado:

- Se requiere una Regla de costes validada en la entidad legal de _Movimiento entre almacenes_.
- Debe ejecutarse el proceso en segundo plano Proceso en segundo plano de cálculo de costes.
- Una vez calculado el coste, el Movimiento entre almacenes puede contabilizarse.

## Cómo reactivar movimientos entre almacenes { #how-to-reactivate-goods-movements }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}

Desde la ventana Movimiento entre almacenes, el usuario puede reactivar un movimiento generado previamente simplemente seleccionando el movimiento necesario y haciendo clic en el botón Reactivar.

Una vez que el movimiento se reactiva correctamente, el estado del documento cambia a No procesado, tal y como puede observarse en la barra de estado.

![](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/goods-movement/goods-movement-6.png)

!!! warning
    No es posible reactivar documentos que incluyan transacciones con cantidades que superen la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando la configuración del hueco permite la sobreemisión. Para más información, visite [Hueco](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

## Contabilización masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro(s) se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo de Contabilización masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.