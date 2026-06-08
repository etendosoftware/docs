---
title: Reserva de existencias
tags:
 - Stock Reservation
 - Warehouse Management
 - Inventory
 - Transactions
---

# Reserva de existencias { #stock-reservation }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Reserva de existencias`

## Visión general { #overview }

En esta ventana, es posible revisar y gestionar las Reservas existentes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Be_9LXecJY" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Las reservas de existencias se utilizan principalmente para garantizar la disponibilidad de stock al entregar un **Pedido de venta**. Con esta funcionalidad, también es posible bloquear stock no relacionado con ningún **Pedido de venta** para evitar su consumo.

Una reserva identifica determinadas existencias en el almacén que quedan reservadas y no pueden ser consumidas por nadie excepto por el propietario de la reserva. Actualmente, hay dos posibles propietarios: una _línea de Pedido de venta_ o el _Sistema_. Una reserva para una línea de **Pedido de venta** identifica existencias que solo pueden consumirse en albaranes relacionados con el **Pedido de venta**. Una reserva del _Sistema_ es un tipo especial de reserva que no puede ser consumida por nadie. Las reservas del _Sistema_ se utilizan para reservas en _Retención_ cuando es necesario bloquear existencias en el almacén.

!!! note
    Las reservas están deshabilitadas por defecto. Para poder utilizarlas, inserte una nueva _Preferencias_ usando la propiedad _Habilitar reservas de existencias_ con valor _Y_. A continuación, cierre la sesión e inicie sesión de nuevo para continuar con el proceso.

Esta funcionalidad incluye dos tipos de reservas:

- Pre-reserva: son reservas que no están físicamente en el almacén, sino pedidas a un proveedor, y cuando existe una relación entre la línea del pedido de compra y una línea de pedido de venta. Una vez que se recibe la línea del pedido de compra, esta pre-reserva se convierte automáticamente en una reserva.
- Reserva: se refiere a existencias almacenadas en el almacén que ya están reservadas por una línea de pedido de venta.

Una reserva siempre se define por el producto que se desea reservar, pero también pueden definirse otras dimensiones como el almacén, el hueco y el atributo (p. ej., color, lotes, número de serie).

Otro aspecto interesante es la posibilidad de asignar o no la reserva:

- El stock _Asignado_ significa que se reserva un stock específico para un pedido de venta, en lugar de ser una reserva general. Ese stock concreto no puede reservarse para ningún otro pedido de venta.
- Un stock reservado _No asignado_ puede cambiarse en cualquier momento por otras existencias disponibles, garantizando siempre que la línea del **Pedido de venta** mantenga la reserva.

Esta funcionalidad intenta cubrir varios flujos:

1.  Ventas
2.  Compras
3.  Plan de compras (MRP)

## Flujo de ventas { #sales-flow }

Un pedido de venta puede reservarse cuando el documento está contabilizado y pendiente de entrega. La forma de realizar la reserva es:

- Manual: no se genera ninguna reserva automáticamente. Por tanto, cuando el pedido se contabiliza, las reservas deben realizarse manualmente seleccionando el hueco, el atributo, etc.

- Automática: la reserva se crea y procesa automáticamente, reservando el stock disponible. Esta opción reserva stock de cualquiera de los almacenes disponibles pertenecientes a la organización del pedido de venta creado, no solo del almacén definido en la cabecera del pedido.

- Automática - Solo almacén por defecto: la reserva se limita únicamente al almacén especificado en la cabecera del pedido. Esto permite optimizar la asignación de inventario y garantizar que los productos se asignen según las preferencias de almacén definidas en cada transacción.

    !!!info
        Esta última opción solo está disponible si el módulo [Automated Warehouse Reservation](../../../optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation) está instalado, como parte del Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

Para más información, visite [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order).

## Flujo de compras { #procurement-flow }

Las pre-reservas también pueden realizarse desde el **Pedido de compra**. Estando en la línea del pedido de compra, existe la posibilidad de seleccionar cualquier línea de pedido de venta pendiente de entrega que esté esperando recibir la mercancía en el almacén. Una vez que se reciben los artículos, la pre-reserva se convierte en reserva y las existencias quedan reservadas para esa línea de pedido de venta.

Para más información, visite [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order).

## Plan de compras (MRP) { #purchasing-plan-mrp }

Al lanzar el plan de compras, ahora existe la posibilidad de realizar reservas para **Pedido de venta** y pre-reservas; es decir, crear pedidos de compra vinculados a pedidos de venta.

## Consumo de reservas { #reservation-consumption }

Cuando se crea automáticamente un **Albarán (Cliente)** de un **Pedido de venta** reservado, consumirá el stock reservado. El proceso propondrá primero el posible stock asignado y, posteriormente, cualquier stock disponible basado en las reglas estándar de obtención de stock, incluyendo stock reservado pero NO asignado (incluso de otras reservas). Si el **Pedido de venta** relacionado no tiene ninguna reserva, solo se propone stock no reservado.

Cuando se procesa el **Albarán (Cliente)**, la reserva se actualiza para reflejar el stock que finalmente se ha entregado y actualizar la cantidad liberada. En este paso, existen varios casos:

- Todo el stock del albarán coincide con el stock reservado. La cantidad liberada se actualiza en consecuencia.
- Se envía un stock diferente.
  - El stock no está reservado por ninguna otra reserva. La reserva se actualiza para reservar el stock enviado y, si había otro stock reservado, se elimina de la reserva para que la cantidad reservada permanezca igual.
  - El stock está reservado y no asignado en otra reserva. La otra reserva se actualiza para buscar otro stock disponible.
    - Si se encuentra stock disponible, la otra reserva se actualiza para reservar el stock encontrado y el stock se reasigna a la reserva actual.
    - Si no se encuentra stock disponible, se muestra un error indicando que el stock no está disponible. El usuario debe cambiar el stock del **Albarán (Cliente)** o editar la otra reserva para buscar manualmente o liberar el stock en conflicto.
  - El stock está reservado y asignado en otra reserva. Se muestra un error indicando que el stock no está disponible. El usuario debe cambiar el stock del **Albarán (Cliente)** o editar la otra reserva para buscar manualmente o liberar el stock en conflicto.

## Reserva { #reservation }

El producto que se desea reservar se define en la solapa principal.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-1.png)

La cabecera de la reserva define cada reserva. En primer lugar, se definen la _Organización_ donde se realiza la reserva y el _Producto_ y la _Cantidad_ que se desea reservar. Cuando la reserva es para una línea de **Pedido de venta**, estos campos se heredan de la línea. Posteriormente, se define el propietario de la reserva; actualmente solo es posible definir líneas de **Pedido de venta**. Si se deja en blanco, la reserva se considera una reserva del _Sistema_ donde el propietario es la _Organización_. Por último, es posible definir ciertas dimensiones para restringir el stock que puede utilizarse para satisfacer la reserva:

- _Almacén_
- _Hueco_
- _Valor atributos_

!!! note
    Solo es posible seleccionar almacenes que estén definidos como almacenes _disponibles_ de la organización y huecos que pertenezcan a ellos.

La reserva puede tener distintos estados:

- **Borrador**: la reserva puede tener ya algunas líneas de stock, pero estas aún no se consideran stock reservado y están disponibles para todos.
- **Completada**: la reserva se ha procesado. Si aún quedaba stock pendiente de reservar, el proceso _Completar_ intentará reservar el stock disponible. Este stock reservado automáticamente queda como no asignado.
- **Retención**: cualquier reserva puede establecerse en estado de retención. Esto significa que el stock queda completamente bloqueado y ni siquiera es posible generar un albarán para el pedido de venta consumiendo el stock reservado. En este estado, el botón anteriormente denominado "Poner en retención" cambia a "Quitar retención" y ofrece al usuario la posibilidad de deshacer la acción.
- **Cerrado**: una Reserva cerrada no puede reactivarse posteriormente. Además, cuando una Reserva se cierra, su **Cantidad** se establece con el mismo valor que la Cantidad liberada, evitando problemas adicionales de inconsistencia.

Una reserva tiene 3 cantidades principales:

**Cantidad**

Determina la cantidad que se desea reservar. Si la reserva está relacionada con una línea de **Pedido de venta**, esta cantidad debe ser la misma que la cantidad pedida.

**Cantidad reservada**

Es la cantidad total que realmente está reservada. Cuando no hay suficiente stock disponible, es posible tener una _Cantidad reservada_ inferior a la _Cantidad_.

**Cantidad liberada**

Es la cantidad que se ha entregado y liberada de la reserva. Cuando se procesa un **Albarán (Cliente)** para un **Pedido de venta** reservado, la Cantidad liberada de la reserva se incrementa con la cantidad entregada.

## Stock

La solapa **Stock** identifica cada Stock existente o **Línea de pedido de compra** seleccionada para satisfacer la reserva.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-2.png)

En la solapa _Stock_ se muestra el stock realmente reservado. El stock debe cumplir las dimensiones definidas en la cabecera. Cuando el stock está físicamente en el almacén, el stock reservado se identifica por el **Hueco** y el _Valor atributos_ cuando aplique. En el caso de pre-reservas, el stock aún no está en el almacén, por lo que la propiedad _Hueco_ está en blanco y se establece la _Línea de pedido de compra_. Cuando una pre-reserva se recibe y se convierte en reserva, se establece el hueco donde se ha almacenado el stock, manteniendo la línea del pedido de compra.

El stock reservado tiene 2 cantidades:

**Cantidad**

La cantidad reservada.

**Cantidad liberada**

La cantidad que se ha liberado o entregado.

## Gestionar stock { #manage-stock }

Cuando la reserva está en estado _Borrador_ o _Completada_, es posible modificar el stock reservado mediante un proceso de _seleccionar y ejecutar_.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-3.png)

Esta ventana muestra todo el stock ya reservado, además de otro stock disponible y líneas de pedido de compra no recibidas que pueden utilizarse para satisfacer la reserva. El stock disponible se filtra por los almacenes disponibles de la organización de la reserva y por las dimensiones que puedan estar establecidas. Las líneas de pedido de compra también se filtran por estas dimensiones. Para cada línea seleccionada, debe establecerse la cantidad a reservar y si el stock está asignado o no. La cantidad debe ser inferior a la cantidad disponible, considerando también la cantidad que pueda estar reservada en otras reservas, y la suma de todas las líneas seleccionadas debe ser inferior a la cantidad que se desea reservar. Si la reserva ya tiene alguna cantidad liberada, la cantidad del stock liberado debe ser mayor o igual que la cantidad liberada.

## Movimiento entre almacenes { #goods-movement }

Se permite mover un artículo que está reservado desde su hueco actual a otro. El botón _Movimiento entre almacenes_ muestra todos los huecos donde el producto está reservado, es decir, las líneas de stock, y también es posible editar la cantidad a mover y el nuevo hueco.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-4.png)

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.