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

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Be_9LXecJY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

La ventana **Reserva de existencias** es donde se gestionan todas las reservas de stock del sistema. Desde aquí es posible crear, modificar, completar, bloquear o cerrar cualquier reserva, tanto si está vinculada a una línea de pedido de venta como si es un bloqueo de stock sin pedido asociado.

Una reserva garantiza que una cantidad de un producto quede retenida para un propósito específico y no pueda ser consumida por nadie más. Existen dos tipos:

- **Reserva**: stock ya presente en el almacén, reservado para una línea de pedido de venta o bloqueado para uso interno (reserva del sistema).
- **Pre-reserva**: stock aún no recibido pero ya solicitado a un proveedor. La línea de pedido de compra está vinculada a una línea de pedido de venta y el sistema la convierte en una reserva completa de forma automática una vez que se reciben las mercancías.

Las reservas se originan desde distintos puntos — un pedido de venta, un pedido de compra o una planificación de compras — pero todas son visibles y se gestionan desde esta ventana. Cada sección a continuación cubre el flujo correspondiente en detalle.

!!! note
    Las reservas están deshabilitadas por defecto. Para habilitarlas, inserte una nueva Preferencia con la propiedad `Enable Stock Reservations` (*Habilitar reserva de existencias*) y el valor `Y`.

## Cabecera { #header }

Esta ventana muestra todas las reservas del sistema: las creadas automáticamente desde pedidos de venta y las creadas manualmente como reservas del sistema.

<figure markdown="span">
  ![Vista de listado de Reserva de existencias](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-0.png)
  <figcaption>La ventana Reserva de existencias mostrando el listado de reservas existentes.</figcaption>
</figure>

Los campos descritos a continuación son comunes a todas las reservas independientemente de su origen. **Crear un nuevo registro directamente desde esta ventana solo es necesario para las reservas del sistema** — bloqueos de stock no vinculados a ningún pedido de venta. Para las reservas vinculadas a un pedido de venta, el registro se crea desde la línea del pedido mediante el botón **Gestionar reserva** (véase [Flujo de ventas](#sales-flow)).

<figure markdown="span">
  ![Cabecera de Reserva de existencias](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-1.png)
  <figcaption>Campos de la cabecera de Reserva de existencias.</figcaption>
</figure>

Los campos de la cabecera son:

- **Organización** y **Producto** — definen qué se está reservando. Se heredan automáticamente de la línea de pedido de venta cuando la reserva se origina desde allí.
- **Cantidad** — la cantidad a reservar. También se hereda de la línea de pedido de venta cuando corresponde.
- **Línea pedido de venta** — el propietario de la reserva. Actualmente, solo las líneas de pedido de venta pueden establecerse como propietarias. Si se deja en blanco, la reserva actúa como un bloqueo de stock: no es posible generar ningún albarán contra ese stock hasta que la reserva se cierre o se libere. Este tipo se denomina *reserva del sistema* — la organización propietaria retiene el stock pero no puede enviarlo.

Por último, opcionalmente restrinja qué stock puede utilizarse para satisfacer la reserva especificando una o más dimensiones:

- **Almacén**
- **Hueco**
- **Valor atributos**

!!! note
    En la selección solo aparecen los almacenes definidos como almacenes disponibles para la organización, junto con los huecos que pertenecen a ellos.

Una reserva puede tener los siguientes estados:

- **Borrador**: La reserva puede ya tener líneas de stock, pero esas líneas aún no se consideran stock reservado y permanecen disponibles para todos.
- **Completada**: La reserva ha sido procesada. Si aún quedaba stock pendiente de reservar, el proceso *Completar* reserva el stock disponible automáticamente, dejándolo como no asignado.
- **Bloqueada**: El stock queda completamente bloqueado. No es posible generar un albarán para el pedido de venta que consume el stock reservado mientras se encuentre en este estado. El botón **Bloquear** es reemplazado por **Desbloquear**, lo que revierte la acción.
- **Cerrado**: Una reserva cerrada no puede reactivarse. Cuando una reserva se cierra, su **Cantidad** se establece con el mismo valor que la **Cantidad distribuida**, evitando posteriores inconsistencias.

Una reserva registra tres cantidades principales:

- **Cantidad** *(cabecera de reserva)* — la cantidad a reservar. Cuando está vinculada a una línea de pedido de venta, debe coincidir con la cantidad pedida.
- **Cantidad reservada** *(barra de estado)* — la cantidad total realmente reservada. Puede ser inferior a la **Cantidad** cuando no hay suficiente stock disponible.
- **Distribuido** *(barra de estado)* — la cantidad entregada y liberada de la reserva. Se incrementa cada vez que se procesa un albarán (cliente) para el pedido de venta reservado.

## Stock { #stock }

La solapa **Stock** lista cada línea de stock o línea de pedido de compra seleccionada para satisfacer la reserva. Estas líneas se añaden y editan mediante el botón [**Gestionar stock**](#manage-stock).

<figure markdown="span">
  ![Solapa Stock mostrando líneas de stock reservado](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-2.png)
  <figcaption>Solapa Stock con las líneas de stock reservado.</figcaption>
</figure>

Cada línea representa un lote específico de stock asignado a la reserva. Los campos son:

- **Hueco** — la ubicación del almacén donde se encuentra el stock. Se completa cuando el stock ya está en el almacén. Vacío para las pre-reservas (stock aún no recibido); el sistema lo completa automáticamente una vez que llegan y se reciben las mercancías.
- **Valor atributos** — el número de lote, número de serie u otro atributo de seguimiento del producto. Se completa solo cuando el producto está configurado para el seguimiento por atributo. Vacío en caso contrario.
- **Línea pedido compra** — la línea del pedido de compra vinculada a esta reserva. Se completa solo para pre-reservas. Vacío para reservas estándar de stock ya presente en el almacén.
- **Cantidad** — la cantidad asignada a esta línea.
- **Distribuido** — la cantidad de esta línea que ya ha sido enviada. Se incrementa cada vez que se procesa un albarán (cliente) que consume esta reserva.
- **Asignado** — controla si este stock específico queda bloqueado exclusivamente para esta reserva (*Asignado*) o puede ser reemplazado por el sistema con stock disponible equivalente si fuera necesario (*No asignado*). Use *Asignado* cuando deba enviarse exactamente ese lote; use *No asignado* cuando cualquier stock equivalente sea aceptable. Si el stock asignado entra en conflicto con otra reserva bloqueada, el sistema muestra un error en lugar de realizar el envío.

## Botones { #buttons }

### Gestionar stock { #manage-stock }

Cuando la reserva está en estado *Borrador* o *Completada*, modifique el stock reservado haciendo clic en **Gestionar stock**. Esto abre una ventana de selección donde se elige qué líneas de stock incluir y se confirman los cambios.

<figure markdown="span">
  ![Ventana de seleccionar y ejecutar de Gestionar stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-3.png)
  <figcaption>Ventana de selección de Gestionar stock.</figcaption>
</figure>

Esta ventana muestra todo el stock ya reservado, el stock disponible y las líneas de pedido de compra no recibidas que pueden satisfacer la reserva. El stock disponible se filtra por los almacenes configurados como activos (disponibles) para su organización — los mismos almacenes visibles en la cabecera de la reserva — y por las dimensiones que puedan estar establecidas. Las líneas de pedido de compra también se filtran por las mismas dimensiones. Para cada línea seleccionada, establezca la cantidad a reservar y si el stock está asignado o no. Al establecer cantidades, siga estas reglas:

- La cantidad introducida para cada línea no debe superar el stock disponible para esa línea. El sistema resta del total disponible el stock ya reservado en otras reservas.
- El total de todas las líneas seleccionadas no debe superar la cantidad total indicada en la cabecera de la reserva.
- Si el stock de esta reserva ya ha sido enviado (la cantidad distribuida es mayor que cero), la cantidad asignada a esas líneas enviadas debe ser al menos igual a la cantidad ya enviada.

### Procesar { #process }

Mueve la reserva del estado *Borrador* al estado *Completada*. Si aún quedaba stock pendiente de reservar, el sistema reserva el stock disponible automáticamente en ese momento, dejándolo como no asignado.

### Bloquear { #put-on-hold }

Bloquea la reserva completamente. Mientras está bloqueada, no es posible generar ningún albarán contra el stock reservado. El botón cambia a **Desbloquear** una vez que la reserva está bloqueada.

### Desbloquear { #unhold }

Elimina el bloqueo y devuelve la reserva al estado *Completada*, permitiendo que se vuelvan a generar albaranes.

### Movimiento entre almacenes { #goods-movement }

Use el botón **Movimiento entre almacenes** cuando los artículos se trasladen físicamente a una ubicación diferente del almacén y la reserva deba reflejar ese cambio.

Este botón abre una ventana con todos los huecos donde actualmente se encuentra el producto reservado. Seleccione un hueco, ajuste la cantidad a mover y elija el hueco de destino.

<figure markdown="span">
  ![Ventana de Movimiento entre almacenes para stock reservado](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-4.png)
  <figcaption>Ventana de Movimiento entre almacenes para stock reservado.</figcaption>
</figure>

## Consumo de reserva { #reservation-consumption }

Cuando se crea automáticamente un [Albarán (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#goods-shipment) de un pedido de venta reservado, este consume el stock reservado. El sistema propone primero el stock asignado (bloqueado). Si no es suficiente, obtiene stock de cualquier otro disponible, incluido stock no bloqueado reservado para otros pedidos. Si el pedido de venta relacionado no tiene ninguna reserva, solo se propone stock no reservado.

Cuando se procesa el albarán (cliente), la reserva se actualiza para reflejar el stock finalmente entregado y la cantidad distribuida se ajusta en consecuencia. El resultado depende de si el stock enviado coincide con el stock reservado y de si está involucrado en otra reserva:

- Todo el stock del albarán coincide con el stock reservado. La cantidad distribuida se actualiza en consecuencia.
- Se envía un stock diferente. El resultado depende de cómo está reservado ese stock:

| Situación | Qué hace el sistema | Qué puede necesitar hacer |
| :--- | :--- | :--- |
| El stock enviado no está reservado por nadie más | Actualiza la reserva para que coincida con el stock enviado automáticamente | Nada: la reserva se ajusta sola |
| El stock enviado pertenece a otra reserva que NO está bloqueada (no asignada) | Intenta encontrar stock de reemplazo para esa otra reserva | Nada si se encuentra stock; si no, edite la otra reserva o cambie el stock del albarán |
| El stock enviado pertenece a otra reserva que SÍ está bloqueada (asignada) | Muestra un error y se detiene | Cambie el stock en el albarán (cliente), o solicite al propietario de la otra reserva que libere el stock en conflicto |

## Procesos relacionados { #related-processes }

Las reservas también pueden crearse y gestionarse desde otras ventanas del sistema. Las secciones a continuación describen cada punto de entrada.

### Flujo de ventas { #sales-flow }

Un pedido de venta puede reservarse cuando el documento está contabilizado y pendiente de entrega. Hay tres modos de reserva disponibles:

- **Manual**: No se crea ninguna reserva automáticamente. Tras contabilizar el pedido, cree la reserva usando el botón **Gestionar reserva** en la línea del pedido de venta, o abra directamente la ventana **Reserva de existencias** y especifique el almacén, el hueco, el atributo del producto y la cantidad.

- **Automatic**: La reserva se crea y procesa automáticamente, reservando el stock disponible. Este modo reserva stock de cualquier almacén disponible perteneciente a la organización del pedido de venta, no solo del almacén definido en la cabecera del pedido.

- **Automático - solo almacén predeterminado**: La reserva se limita al almacén especificado en la cabecera del pedido. Esto optimiza la asignación de inventario y garantiza que los productos se asignen según las preferencias de almacén definidas en cada transacción.

    !!! info
        Esta opción solo está disponible si el módulo [Automated Warehouse Reservation](../../../optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation) está instalado, como parte del Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

Configure el modo de reserva en el campo **Reserva** de la cabecera del pedido de venta.

Para más información, visite [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order).

### Flujo de aprovisionamiento { #procurement-flow }

Las pre-reservas también pueden realizarse desde el pedido de compra. Desde la línea del pedido de compra, seleccione cualquier línea de pedido de venta pendiente de entrega que esté esperando recibir mercancía en el almacén. Una vez que se reciben los artículos, el sistema convierte la pre-reserva en una reserva y reserva las mercancías para esa línea de pedido de venta.

Para más información, visite [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order).

### Planificación de compras (MRP) { #purchasing-plan-mrp }

Al lanzar la [Planificación de compras](../../../../../user-guide/etendo-classic/basic-features/material-requirement-planning/transactions.md#purchasing-plan), pueden crearse reservas para pedidos de venta y pre-reservas — es decir, pedidos de compra vinculados a pedidos de venta.

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
