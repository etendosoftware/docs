---
title: Reserva de existencias
tags:
 - Reserva de existencias
 - Gestión de almacén
 - Inventario
 - Transacciones
---

# Reserva de existencias { #stock-reservation }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Reserva de existencias`

## Descripción general { #overview }

La ventana Reserva de existencias permite a los usuarios revisar y gestionar las reservas de existencias existentes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Be_9LXecJY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Las reservas de existencias se utilizan principalmente para garantizar la disponibilidad de stock al entregar un Pedido de venta. Con esta funcionalidad, también es posible bloquear stock no relacionado con ningún Pedido de venta para evitar su consumo.

!!! note
    Las reservas están deshabilitadas por defecto. Solicite a su administrador del sistema que habilite la preferencia [_Habilitar reserva de existencias_](../../../../../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#initial-setup) y confirme cuándo está activa. Deberá cerrar sesión e iniciar sesión de nuevo antes de que las reservas estén disponibles.

Esta funcionalidad cubre los siguientes flujos:

1.  [Ventas](#sales-flow)
2.  [Compras](#procurement-flow)
3.  [Planificación de compras (MRP)](#purchasing-plan-mrp)

## Conceptos clave { #key-concepts }

Una reserva identifica determinadas existencias en el almacén que quedan reservadas y no pueden ser consumidas por nadie excepto por el propietario de la reserva. Las reservas tienen un propietario: la parte autorizada a utilizar el stock reservado. El propietario puede ser una _línea de Pedido de venta_ específica (lo que significa que el stock solo puede enviarse contra ese pedido) o el _Sistema_. Una reserva del _Sistema_ bloquea el stock por completo: nadie puede enviarlo ni consumirlo. Esto se utiliza cuando el stock debe retenerse físicamente en el almacén por cualquier motivo no relacionado con un pedido específico.

Esta funcionalidad incluye dos tipos de reservas:

- Pre-reserva: son reservas de stock que aún no está físicamente en el almacén, sino pedido a un proveedor, y en las que existe una relación entre la línea del pedido de compra y una línea de pedido de venta. Una vez que se recibe la línea del pedido de compra, esta pre-reserva se convierte automáticamente en una reserva.
- Reserva: se refiere a existencias almacenadas en el almacén que ya están reservadas por una línea de pedido de venta.

Una reserva siempre se define por el producto que se desea reservar, pero también pueden definirse otras dimensiones como el almacén, el hueco y el atributo del producto (p. ej., color, número de lote o número de serie).

Las reservas también pueden configurarse como asignadas o no asignadas:

- El stock _Asignado_ significa que se reserva un stock específico para un pedido de venta, en lugar de ser una reserva general. Ese stock concreto no puede reservarse para ningún otro pedido de venta.
- El stock de una reserva _No asignada_ puede cambiarse en cualquier momento por otras existencias disponibles, garantizando siempre que la línea del Pedido de venta mantenga su reserva.

## Cabecera de reserva { #reservation-header }

El producto que se desea reservar se define en la solapa principal.

![Cabecera de Reserva de existencias](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-1.png)

Rellene la _Organización_, el _Producto_ y la _Cantidad_ que desea reservar. Si la reserva está vinculada a una línea de Pedido de venta, estos campos se completan automáticamente a partir de esa línea. A continuación, especifique la línea de Pedido de venta que utilizará el stock reservado. Si se deja en blanco, el sistema lo trata como una reserva del _Sistema_: el stock queda completamente bloqueado y no puede enviarse ni consumirse hasta que la reserva se cierre o se libere. Por último, es posible definir ciertas dimensiones para restringir el stock que puede utilizarse para satisfacer la reserva:

- _Almacén_
- _Hueco_
- _Valor atributos_

!!! note
    Solo es posible seleccionar almacenes marcados como activos para su organización (denominados almacenes disponibles en la configuración del sistema), y huecos ubicados dentro de esos almacenes. Si el almacén que necesita no aparece, contacte con su administrador del sistema para revisar la configuración del almacén.

La reserva puede tener distintos estados:

- **Borrador**: la reserva puede tener ya algunas líneas de stock, pero estas aún no se consideran stock reservado y están disponibles para todos.
- **Completada**: la reserva se ha procesado. Si aún quedaba stock pendiente de reservar, el proceso _Completar_ intentará reservar el stock disponible. Este stock reservado automáticamente queda como no asignado.
- **Bloqueada**: cualquier reserva puede establecerse en estado bloqueado. Esto significa que el stock queda completamente bloqueado y ni siquiera es posible generar un albarán para el pedido de venta consumiendo el stock reservado. En este estado, el botón _Bloquear_ es reemplazado por _Desbloqueada_, permitiendo al usuario revertir la acción.
- **Cerrado**: una reserva cerrada no puede reactivarse posteriormente. Además, cuando una reserva se cierra, su Cantidad se establece con el mismo valor que la Cantidad distribuida, evitando problemas adicionales de inconsistencia.

Una reserva tiene 3 cantidades principales:

**Cantidad**

Determina la cantidad que se desea reservar. Si la reserva está relacionada con una línea de Pedido de venta, esta cantidad debe ser la misma que la Cant. pedido.

**Cantidad reservada**

Es la cantidad total que realmente está reservada. Cuando no hay suficiente stock disponible, es posible tener una _Cantidad reservada_ inferior a la _Cantidad_.

**Cantidad distribuida**

Es la cantidad que se ha entregado y distribuida de la reserva. Cuando se procesa un Albarán (Cliente) para un Pedido de venta reservado, la Cantidad distribuida de la reserva se incrementa con la cantidad entregada.

### Gestionar stock { #manage-stock }

Cuando la reserva está en estado _Borrador_ o _Completada_, es posible modificar el stock reservado haciendo clic en el botón **Gestionar stock**, que abre una ventana de selección donde se elige qué líneas de stock incluir y se confirman los cambios.

![Ventana de seleccionar y ejecutar de Gestionar stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-3.png)

Esta ventana muestra todo el stock ya reservado, además de otro stock disponible y líneas de pedido de compra no recibidas que pueden utilizarse para satisfacer la reserva. El stock disponible se filtra por los almacenes configurados como activos (disponibles) para su organización —los mismos almacenes visibles en la cabecera de la reserva— y por las dimensiones que puedan estar establecidas; las líneas de pedido de compra también se filtran por las mismas dimensiones. Para cada línea seleccionada, debe establecerse la cantidad a reservar y si el stock está asignado o no. Al establecer cantidades, siga estas reglas:

- La cantidad que introduzca para cada línea no debe superar el stock disponible para esa línea (el sistema resta del total disponible el stock ya reservado en otras reservas).
- El total de todas las líneas seleccionadas no debe superar la cantidad total indicada en la cabecera de la reserva.
- Si el stock de esta reserva ya ha sido enviado (la cantidad distribuida es mayor que cero), la cantidad que asigne a esas líneas enviadas debe ser al menos igual a la cantidad ya enviada.

## Stock { #stock }

La solapa Stock lista cada línea de stock o línea de Pedido de compra seleccionada para satisfacer la reserva.

![Solapa Stock mostrando líneas de stock reservado](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-2.png)

En la solapa _Stock_ se muestra el stock realmente reservado. El stock debe cumplir las dimensiones definidas en la cabecera. Cuando el stock está físicamente en el almacén, el stock reservado se identifica por el Hueco y el Valor atributos cuando aplique. En el caso de pre-reservas, el stock aún no está en el almacén, por lo que la propiedad _Hueco_ está en blanco y se establece la _Línea de pedido de compra_. Cuando una pre-reserva se recibe y se convierte en una reserva, se establece el hueco donde se ha almacenado el stock, manteniendo la línea del pedido de compra.

El stock reservado tiene 2 cantidades:

**Cantidad**

La cantidad reservada.

**Cantidad distribuida**

La cantidad distribuida o entregada.

### Movimiento entre almacenes { #goods-movement }

Si el stock reservado necesita reubicarse dentro del almacén (por ejemplo, para trasladar artículos a una zona de almacenamiento diferente), utilice el botón **Movimiento entre almacenes**. Este abre una ventana con todos los huecos donde actualmente se encuentra el producto reservado. Puede seleccionar un hueco, ajustar la cantidad a mover y elegir el hueco de destino.

![Ventana de Movimiento entre almacenes para stock reservado](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-4.png)

## Flujo de ventas { #sales-flow }

Un pedido de venta puede reservarse cuando el documento está contabilizado y pendiente de entrega. La forma de realizar la reserva es:

- Manual: no se genera ninguna reserva automáticamente. Tras contabilizar el pedido, cree la reserva utilizando el botón **Gestionar reserva** en la línea del Pedido de venta o abriendo directamente la ventana Reserva de existencias, especificando el almacén, el hueco, el atributo del producto y la cantidad.

- Automática: la reserva se crea y procesa automáticamente, reservando el stock disponible. Esta opción reserva stock de cualquiera de los almacenes disponibles pertenecientes a la organización del pedido de venta creado, no solo del almacén definido en la cabecera del pedido.

- Automática - Solo almacén por defecto: la reserva se limita únicamente al almacén especificado en la cabecera del pedido. Esto permite optimizar la asignación de inventario y garantizar que los productos se asignen según las preferencias de almacén definidas en cada transacción.

    !!! info
        Esta última opción solo está disponible si el módulo [Automated Warehouse Reservation](../../../optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation) está instalado, como parte del Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

El modo de reserva se configura en el campo **Reserva** de la cabecera del Pedido de venta.

Para más información, visite [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order).

## Flujo de compras { #procurement-flow }

Las pre-reservas también pueden realizarse desde el Pedido de compra. Desde la línea del pedido de compra, los usuarios pueden seleccionar cualquier línea de pedido de venta pendiente de entrega que esté esperando recibir la mercancía en el almacén. Una vez que se reciben los artículos, la pre-reserva se convierte en una reserva y las existencias quedan reservadas para esa línea de pedido de venta.

Para más información, visite [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order).

## Planificación de compras (MRP) { #purchasing-plan-mrp }

Al lanzar la [Planificación de compras](../../../../../user-guide/etendo-classic/basic-features/material-requirement-planning/transactions.md#purchasing-plan), existe la posibilidad de realizar reservas para Pedidos de venta y pre-reservas; es decir, crear pedidos de compra vinculados a pedidos de venta.

## Consumo de reservas { #reservation-consumption }

Cuando se crea automáticamente un [Albarán (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#goods-shipment) de un Pedido de venta reservado, consumirá el stock reservado. El proceso propondrá primero el posible stock asignado y, posteriormente, cualquier stock disponible basado en las reglas estándar de obtención de stock, incluyendo stock reservado pero no asignado (incluso de otras reservas). Si el Pedido de venta relacionado no tiene ninguna reserva, solo se propone stock no reservado.

Cuando se procesa el Albarán (Cliente), la reserva se actualiza para reflejar el stock que finalmente se ha entregado y la cantidad distribuida se ajusta en consecuencia. El resultado depende de si el stock enviado coincide con el stock reservado y de si está involucrado en otra reserva:

- Todo el stock del albarán coincide con el stock reservado. La cantidad distribuida se actualiza en consecuencia.
- Se envía un stock diferente. El resultado depende de cómo está reservado ese stock:

| Situación | Qué hace el sistema | Qué puede necesitar hacer |
|---|---|---|
| El stock enviado no está reservado por nadie más | Actualiza la reserva para que coincida con el stock enviado automáticamente | Nada: la reserva se ajusta sola |
| El stock enviado pertenece a otra reserva que NO está bloqueada (no asignada) | Intenta encontrar stock de reemplazo para esa otra reserva | Nada si se encuentra stock; si no, edite la otra reserva o cambie el stock del albarán |
| El stock enviado pertenece a otra reserva que SÍ está bloqueada (asignada) | Muestra un error y se detiene | Cambie el stock en el Albarán (Cliente), o solicite al propietario de la otra reserva que libere el stock en conflicto |

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
