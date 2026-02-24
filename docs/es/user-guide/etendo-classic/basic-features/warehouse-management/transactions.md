---
title: Gestión de Almacén
---

## Visión general

Gestión de Almacén se ocupa de todas las actividades relacionadas con las acciones de almacén necesarias para los procesos de ventas y aprovisionamiento.

## Inventario físico

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Inventario físico`

La ventana **Inventario físico** permite al usuario ejecutar el proceso de conteo de mercancías en Etendo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xqE_UnYO6cM" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Cabecera

El proceso de conteo de mercancías requiere crear un conteo de inventario para comprobar o actualizar las cantidades de stock.

Estos son los pasos que deben seguirse para crear un conteo de inventario:

**1.** La sección **Cabecera** identifica el proceso de "Inventario físico" y lista sus parámetros principales.

![Cabecera](../../../../assets/drive/1mrD0K5quoU7vF0d3WNeOwW0u_n4vGLWf.png)

Todos los campos se rellenan automáticamente cuando se crea un registro nuevo.

Algunos de los campos a tener en cuenta son:

- **Nombre:** este campo se utiliza para referenciar el movimiento físico no solo en los informes de almacén, sino también en el libro mayor; por lo tanto, es importante usar un nombre significativo.
- **Fecha del movimiento:** es la fecha en la que se crea el movimiento y, por defecto, es la fecha actual. Esta fecha también se utiliza en el registro de contabilización del documento de Inventario físico en el libro mayor, si aplica. Siempre puede modificarse, pero el usuario debe tener en cuenta que no es posible registrar inventarios físicos en el pasado (el **Proceso de Conteo de Inventario** siempre toma la fecha actual y no la Fecha del movimiento para actualizar el stock). La Fecha del movimiento debería ser la fecha actual, a menos que el usuario pueda garantizar que no se han procesado transacciones de almacén mientras tanto.
- **Almacén:** almacén en el que tiene lugar el inventario físico. Por defecto, toma el valor de la sesión desde el menú superior de navegación Preferencias de Usuario.

**2.** Hay 2 formas de **introducir líneas** en el documento de inventario físico:

1.  Automáticamente, creando una lista de los productos disponibles en el almacén y en los huecos definidos en la cabecera del inventario físico que cumplan las condiciones de filtrado especificadas por el botón **Crear lista de conteo de inventario**.
2.  Manualmente, línea a línea para determinados productos. Esto se utiliza cuando solo es necesario actualizar algunos productos.

El proceso **Crear lista de conteo de inventario** puede ejecutarse más de una vez para el mismo inventario físico. Aunque las líneas se crean automáticamente mediante el proceso **Crear lista de conteo de inventario**, estas líneas pueden actualizarse posteriormente de forma manual. El diálogo de filtros de **Crear lista de conteo de inventario** tiene los siguientes parámetros:

![Cabecera 2](../../../../assets/drive/1CWBqL3eiqKbFJ8RTqSJaf1iB2_ltvJp3.png)

Los campos a tener en cuenta son:

- **Hueco:** solo se filtrarán los productos de este hueco.
- **Categoría del producto:** solo se filtrarán los productos que pertenezcan a una categoría de producto determinada; en caso contrario, se mostrarán todos los productos.
- **Cantidad de inventario:** incluye o excluye productos en el inventario físico en función de las cantidades reales. Las opciones disponibles son:
    - vacío - se mostrarán todos los productos en el inventario físico independientemente de su cantidad
    - 0 - se mostrarán solo los productos en el inventario físico que tengan cantidad 0 en stock.
    - <0 - se mostrarán solo los productos en el inventario físico que tengan una cantidad positiva en stock.
    - \>0 - se mostrarán solo los productos en el inventario físico que tengan una cantidad negativa en stock.
    - distinto de 0 - se mostrarán solo los productos en el inventario físico que tengan una cantidad en stock distinta de 0.
- **Establecer Cantidad teórica a cero:** esta casilla establece el campo **Cant.total** de la lista de conteo a cero. Cuando la casilla no está seleccionada, la **Cant.total** toma por defecto el mismo valor que la **Cantidad teórica** (Cantidad disponible) del producto.
    - La primera opción se utiliza para inventarios físicos ciegos, en los que las personas que cuentan los artículos en el almacén no necesitan conocer las cantidades esperadas.
    - La primera opción se utiliza para permitir al usuario introducir el conteo de cantidad "real" en el almacén y el hueco. Una vez procesado el conteo de inventario, la cantidad teórica mostrada por el sistema se actualizará a la cantidad contada introducida por el usuario.
- **ABC:** informe de productos Pareto

### Líneas

La solapa Líneas permite al usuario añadir o editar productos individuales que se incluirán en la lista de conteo de inventario. Representa la lista de conteo de inventario de un almacén determinado.

Algunos campos relevantes a tener en cuenta son:

- **Cant.total:** es el stock real (contado físicamente) del producto en el **Hueco** del almacén.
- **Cantidad teórica:** es el stock del producto en el **Hueco** según Etendo.
- **Costo:** es el coste unitario del producto.  
  Este campo es opcional. Puede rellenarse con el coste si se conoce cuando el stock de un producto se incrementa; en caso contrario, se utiliza el método de Coste por defecto para valorar esa transacción que incrementa el stock del producto.

Los botones de proceso son:

- **Actualizar cantidad** actualiza el campo **Cantidad teórica** actual con la última cantidad del producto desde la aplicación. Esto se utiliza en caso de que haya cambiado desde que se generó la lista de conteo. Es útil en situaciones en las que transcurre un tiempo significativo entre la generación del inventario físico en Etendo y el conteo físico real.
- **Proceso de Conteo de Inventario** finaliza el proceso de conteo de Inventario físico después de que se hayan introducido todas las correcciones y actualiza el stock.
- **Contabilizar** permite contabilizar el conteo de inventario una vez procesado.

### Contabilidad

Un inventario físico solo puede contabilizarse en el libro mayor en caso de que exista una diferencia entre "Cant.total" y "Cantidad teórica" para un producto. De lo contrario, no habrá nada que contabilizar en el libro mayor.

Por ejemplo, un producto cuya "Cant.total" es de 6700 unidades en una fecha determinada, mientras que la "Cantidad teórica" en Etendo es de 6000 unidades.

Ese inventario físico puede contabilizarse una vez procesado, si se ha calculado el coste del producto.

**La contabilización del Inventario físico crea los siguientes asientos contables si el inventario aumenta:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Cuenta               | Débito                                                   | Crédito**                                                  |
| Inmovilizado del producto         | (Cant.total - Cantidad teórica) \* Coste del producto |                                                             |
| Diferencias de almacén |                                                             | (Cant.total - Cantidad teórica) \* Coste del producto |

**La contabilización del Inventario físico crea los siguientes asientos contables si el inventario disminuye:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Cuenta               | Débito                                                   | Crédito                                                  |
| Diferencias de almacén | (Cant.total - Cantidad teórica) \* Coste del producto |                                                             |
| Inmovilizado del producto         |                                                             | (Cant.total - Cantidad teórica) \* Coste del producto |

### Cómo reactivar inventarios físicos

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

Desde la ventana Inventario físico, es posible reactivar un inventario generado previamente con solo seleccionar el documento correspondiente y hacer clic en el botón Reactivar.

Una vez que el inventario se reactiva correctamente, el estado del documento cambia a No procesado, tal y como puede observarse en la barra de estado.

![](../../../../assets/drive/1WBA34PF6dwDGKc8HW0tC8iuzD_CR-9I2.png)

!!! warning
    No es posible reactivar documentos que incluyan transacciones con cantidades que excedan la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando la configuración del hueco permite Over Issue. Para más información, visite [Hueco](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Contabilización masiva](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Movimiento entre almacenes

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Movimiento entre almacenes`

La ventana Movimiento entre almacenes permite al usuario realizar movimientos internos de inventario entre almacenes y huecos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yW4Bv6bORk0" title="reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Cabecera

Los movimientos internos de inventario pueden realizarse añadiendo productos en la solapa Líneas o moviendo todos los artículos a la vez.

![Cabecera](../../../../assets/drive/1kfjIQpgySwJygR6UxhnTHrLbFkseEEDf.png)

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

![Cabecera](../../../../assets/drive/170LDHuomqrUcv0OHXssJuBjXJlyzg8H0.png)

### Líneas

La solapa Líneas es una lista de los productos movidos entre almacenes y huecos.

Esta solapa también incluye información sobre el origen, el destino y la cantidad correspondiente.

![Líneas](../../../../assets/drive/18SSKl05H6kTiVvZfZteK0MeJnb787F6p.png)

Algunos campos a tener en cuenta:

- **Cant. movida:** es la cantidad de producto a mover.  
  Por defecto, toma la cantidad total del **Producto** en el Hueco.
- **Hueco:** es el hueco del que se retiran los productos.  
  Por defecto, toma el Hueco seleccionado en el selector de **Producto**.
- **Movido a:** es el hueco de destino de los productos.
- **Nuevo Valor atributos:** campo de solo lectura que solo es visible para transacciones de empaquetado/desempaquetado relacionadas con *Inventario Referenciado*. Muestra el nuevo valor de atributos tras realizarse el proceso de empaquetado/desempaquetado.

Una vez ejecutado el proceso **Procesar movimientos**, el stock se actualiza.

### Botones

#### Mover un hueco entero

Este botón le permite transferir rápidamente todos los productos ubicados en un Hueco A a otro Hueco B de destino.  
Al hacer clic, el sistema muestra automáticamente en las líneas una lista de productos de la ubicación de origen seleccionada.  
Al procesar la transferencia, todos los productos se transfieren del origen al destino.

![](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/move-storage-bin-button-1.png)

#### Generar tarea de reubicación

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Permite crear una tarea de reubicación desde el documento **Movimiento entre almacenes**. El sistema toma la información cargada en el registro y sus líneas y la envía a Etendo Mobile, donde el operario puede ejecutar el movimiento desde la subaplicación correspondiente. Al pulsarlo, se abre el pop-up de asignación automática o manual.

!!! info
    Para más información, visite [Tarea de reubicación](../../optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#relocation-tasks)

#### Procesar movimiento

Este botón procesa el documento Movimiento entre almacenes. Al ejecutarlo, el sistema valida la información del movimiento y actualiza el stock en las ubicaciones correspondientes.

![](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/process-movement-button-1.png)

### Contabilidad

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

### Cómo reactivar movimientos entre almacenes

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}

Desde la ventana Movimiento entre almacenes, el usuario puede reactivar un movimiento generado previamente simplemente seleccionando el movimiento necesario y haciendo clic en el botón Reactivar.

Una vez que el movimiento se reactiva correctamente, el estado del documento cambia a No procesado, tal y como puede observarse en la barra de estado.

![](../../../../assets/drive/1tHX7U3NNVTlZ83m_Ql4RFEL52gsgy81B.png)

!!! warning
    No es posible reactivar documentos que incluyan transacciones con cantidades que superen la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando la configuración del hueco permite la sobreemisión. Para más información, visite [Hueco](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro(s) se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo de Contabilización masiva](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Producción LDM

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Producción LDM`

### Visión general

Cree y ejecute procesos de producción utilizando las listas de materiales definidas previamente.

A diferencia de lo que sugiere el nombre, este proceso **no forma parte de la producción**. Esta configuración se utiliza para combinar diferentes productos finales en otro **producto empaquetado**. Por ejemplo, para un ordenador que se envía con diferentes teclados o productos que se envían con diferentes cables de alimentación. No hay una producción real implicada en la creación del nuevo producto.

La configuración de esta pantalla se combina con configuraciones en la pantalla de producto:

- la casilla de verificación de lista de materiales está seleccionada para el producto
- la pestaña de lista de materiales está cumplimentada

### Cabecera

En esta sección se selecciona la organización, un nombre del empaquetado que se ejecutará, así como una fecha en la que tendrá lugar.

### Plan de producción

Añada listas de materiales a producir en un plan de producción especificado.

En esta sección, se selecciona el producto y el número que se ejecuta. Además, debe seleccionarse el hueco en el que se almacenará el resultado de la Producción.

Tal y como se indica en la Visión general, el producto que se selecciona debe configurarse correctamente primero:

- la casilla de verificación de lista de materiales está seleccionada
- la pestaña de lista de materiales está cumplimentada con la información de los componentes que se combinan más la cantidad para cada componente
- se ha hecho clic en el botón Verificar LDM para dejar el producto listo para su uso

### Líneas

Cree y edite los productos que se van a utilizar en la producción.

Después de cumplimentar la pestaña Plan de producción, se hace clic en el botón **Crear/Procesar producción** para generar la información en esta sección. En base a la configuración de la información en la pestaña de lista de materiales del producto combinada con la cantidad de producción en la pestaña del plan de producción, se generó la información de los **componentes a utilizar y qué cantidad**.

Después de hacer clic en el botón **Crear/Procesar producción** por segunda vez, se ejecutan los cambios.

En el popup, puede seleccionarse la casilla de verificación 'La cantidad del producto debe estar en stock', de modo que el proceso solo se ejecute si los componentes están en stock. Tras procesarse correctamente, el stock de los componentes disminuye y el stock del producto empaquetado aumenta.

!!! warning
    Actualmente, los procesos implicados en la Producción LDM no admiten stock negativo. Por este motivo, si la casilla de verificación 'La cantidad del producto debe estar en stock' no está seleccionada y no hay suficiente stock de los productos consumidos, se utilizará la cantidad disponible en stock para completar las cantidades en las líneas de la pestaña \[Líneas\].

Existe una verificación denominada **Forzar el uso del almacén del hueco seleccionado.** Cuando está habilitada, se utilizará el mismo Almacén del Hueco seleccionado para obtener el stock que se va a consumir. Si no está habilitada, el proceso tendrá en cuenta todos los Almacenes disponibles para el establecido en la cabecera del Documento.

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Operaciones de material

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Operaciones de material (uso indirecto)`

### Visión general

La ventana **Operaciones de material** proporciona una vista de solo lectura con amplias capacidades de filtrado que muestra todas las transacciones de inventario.

Todos los movimientos reales de almacén pueden verse en esta ventana: entradas, salidas, movimientos entre almacenes, inventarios físicos, etc.

![Operaciones de material](../../../../assets/drive/1rGnZndz2vH5AEMTbBc1xVao-TLFT1N_r.png)
## Reserva de existencias

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Reserva de existencias`

### Visión general

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

### Flujo de ventas

Un pedido de venta puede reservarse cuando el documento está contabilizado y pendiente de entrega. La forma de realizar la reserva es:

- Manual: no se genera ninguna reserva automáticamente. Por tanto, cuando el pedido se contabiliza, las reservas deben realizarse manualmente seleccionando el hueco, el atributo, etc.

- Automática: la reserva se crea y procesa automáticamente, reservando el stock disponible. Esta opción reserva stock de cualquiera de los almacenes disponibles pertenecientes a la organización del pedido de venta creado, no solo del almacén definido en la cabecera del pedido.

- Automática - Solo almacén por defecto: la reserva se limita únicamente al almacén especificado en la cabecera del pedido. Esto permite optimizar la asignación de inventario y garantizar que los productos se asignen según las preferencias de almacén definidas en cada transacción.

    !!!info
        Esta última opción solo está disponible si el módulo [Automated Warehouse Reservation](../../optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation) está instalado, como parte del Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

Para más información, visite [Pedido de venta](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order).

### Flujo de compras

Las pre-reservas también pueden realizarse desde el **Pedido de compra**. Estando en la línea del pedido de compra, existe la posibilidad de seleccionar cualquier línea de pedido de venta pendiente de entrega que esté esperando recibir la mercancía en el almacén. Una vez que se reciben los artículos, la pre-reserva se convierte en reserva y las existencias quedan reservadas para esa línea de pedido de venta.

Para más información, visite [Pedido de compra](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order).

### Plan de compras (MRP)

Al lanzar el plan de compras, ahora existe la posibilidad de realizar reservas para **Pedido de venta** y pre-reservas; es decir, crear pedidos de compra vinculados a pedidos de venta.

### Consumo de reservas

Cuando se crea automáticamente un **Albarán (Cliente)** de un **Pedido de venta** reservado, consumirá el stock reservado. El proceso propondrá primero el posible stock asignado y, posteriormente, cualquier stock disponible basado en las reglas estándar de obtención de stock, incluyendo stock reservado pero NO asignado (incluso de otras reservas). Si el **Pedido de venta** relacionado no tiene ninguna reserva, solo se propone stock no reservado.

Cuando se procesa el **Albarán (Cliente)**, la reserva se actualiza para reflejar el stock que finalmente se ha entregado y actualizar la cantidad liberada. En este paso, existen varios casos:

- Todo el stock del albarán coincide con el stock reservado. La cantidad liberada se actualiza en consecuencia.
- Se envía un stock diferente.
  - El stock no está reservado por ninguna otra reserva. La reserva se actualiza para reservar el stock enviado y, si había otro stock reservado, se elimina de la reserva para que la cantidad reservada permanezca igual.
  - El stock está reservado y no asignado en otra reserva. La otra reserva se actualiza para buscar otro stock disponible.
    - Si se encuentra stock disponible, la otra reserva se actualiza para reservar el stock encontrado y el stock se reasigna a la reserva actual.
    - Si no se encuentra stock disponible, se muestra un error indicando que el stock no está disponible. El usuario debe cambiar el stock del **Albarán (Cliente)** o editar la otra reserva para buscar manualmente o liberar el stock en conflicto.
  - El stock está reservado y asignado en otra reserva. Se muestra un error indicando que el stock no está disponible. El usuario debe cambiar el stock del **Albarán (Cliente)** o editar la otra reserva para buscar manualmente o liberar el stock en conflicto.

### Reserva

El producto que se desea reservar se define en la solapa principal.

![Stock](../../../../assets/drive/1Z_fxaBhzcUR2exlgB69BDletxVUl_fiL.png)

La cabecera de la reserva define cada reserva. En primer lugar, se definen la _Organización_ donde se realiza la reserva y el _Producto_ y la _Cantidad_ que se desea reservar. Cuando la reserva es para una línea de **Pedido de venta**, estos campos se heredan de la línea. Posteriormente, se define el propietario de la reserva; actualmente solo es posible definir líneas de **Pedido de venta**. Si se deja en blanco, la reserva se considera una reserva del _Sistema_ donde el propietario es la _Organización_. Por último, es posible definir ciertas dimensiones para restringir el stock que puede utilizarse para satisfacer la reserva:

- _Almacén_
- _Hueco_
- _Valor atributos_

!!! note
    Solo es posible seleccionar almacenes que estén definidos como almacenes _disponibles_ de la organización y huecos que pertenezcan a ellos.

La reserva puede tener distintos estados:

- **Borrador**: la reserva puede tener ya algunas líneas de stock, pero estas aún no se consideran stock reservado y están disponibles para todos.
- **Completada**: la reserva se ha procesado. Si aún quedaba stock pendiente de reservar, el proceso _Completar_ intentará reservar el stock disponible. Este stock reservado automáticamente queda como no asignado.
- **Retención**: cualquier reserva puede establecerse en estado de retención. Esto significa que el stock queda completamente bloqueado y ni siquiera es posible generar un albarán para el pedido de venta consumiendo el stock reservado. En este estado, el botón anteriormente denominado “Poner en retención” cambia a “Quitar retención” y ofrece al usuario la posibilidad de deshacer la acción.
- **Cerrado**: una Reserva cerrada no puede reactivarse posteriormente. Además, cuando una Reserva se cierra, su **Cantidad** se establece con el mismo valor que la Cantidad liberada, evitando problemas adicionales de inconsistencia.

Una reserva tiene 3 cantidades principales:

**Cantidad**

Determina la cantidad que se desea reservar. Si la reserva está relacionada con una línea de **Pedido de venta**, esta cantidad debe ser la misma que la cantidad pedida.

**Cantidad reservada**

Es la cantidad total que realmente está reservada. Cuando no hay suficiente stock disponible, es posible tener una _Cantidad reservada_ inferior a la _Cantidad_.

**Cantidad liberada**

Es la cantidad que se ha entregado y liberado de la reserva. Cuando se procesa un **Albarán (Cliente)** para un **Pedido de venta** reservado, la Cantidad liberada de la reserva se incrementa con la cantidad entregada.

### Stock

La solapa **Stock** identifica cada Stock existente o **Línea de pedido de compra** seleccionada para satisfacer la reserva.

![Stock](../../../../assets/drive/1588n_FidAyqyw0WwUJ8-E3w_bMRv2MLF.png)

En la solapa _Stock_ se muestra el stock realmente reservado. El stock debe cumplir las dimensiones definidas en la cabecera. Cuando el stock está físicamente en el almacén, el stock reservado se identifica por el **Hueco** y el _Valor atributos_ cuando aplique. En el caso de pre-reservas, el stock aún no está en el almacén, por lo que la propiedad _Hueco_ está en blanco y se establece la _Línea de pedido de compra_. Cuando una pre-reserva se recibe y se convierte en reserva, se establece el hueco donde se ha almacenado el stock, manteniendo la línea del pedido de compra.

El stock reservado tiene 2 cantidades:

**Cantidad**

La cantidad reservada.

**Cantidad liberada**

La cantidad que se ha liberado o entregado.

### Gestionar stock

Cuando la reserva está en estado _Borrador_ o _Completada_, es posible modificar el stock reservado mediante un proceso de _seleccionar y ejecutar_.

![Stock](../../../../assets/drive/1U6xkkgtOgdwovTAP70Fo6JLSbfIf-UOZ.png)

Esta ventana muestra todo el stock ya reservado, además de otro stock disponible y líneas de pedido de compra no recibidas que pueden utilizarse para satisfacer la reserva. El stock disponible se filtra por los almacenes disponibles de la organización de la reserva y por las dimensiones que puedan estar establecidas. Las líneas de pedido de compra también se filtran por estas dimensiones. Para cada línea seleccionada, debe establecerse la cantidad a reservar y si el stock está asignado o no. La cantidad debe ser inferior a la cantidad disponible, considerando también la cantidad que pueda estar reservada en otras reservas, y la suma de todas las líneas seleccionadas debe ser inferior a la cantidad que se desea reservar. Si la reserva ya tiene alguna cantidad liberada, la cantidad del stock liberado debe ser mayor o igual que la cantidad liberada.

### Movimiento entre almacenes

Se permite mover un artículo que está reservado desde su hueco actual a otro. El botón _Movimiento entre almacenes_ muestra todos los huecos donde el producto está reservado, es decir, las líneas de stock, y también es posible editar la cantidad a mover y el nuevo hueco.

![Stock](../../../../assets/drive/1F6npvraIMx78-uaccl5Ibmqj8yY46wMX.png)
## Ajuste de Valor del Inventario

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Ajuste de Valor del Inventario`

### Visión general

La ventana **Ajuste de Valor del Inventario** permite al usuario cambiar el **Valor del Inventario Actual** o el **Coste Unitario actual** de los productos en stock en una **Fecha de Referencia** determinada.

Una vez creado y procesado, genera un inventario de cierre y un inventario de apertura para el/los producto(s), que pueden revisarse en la solapa **Inventarios**.

- **Inventario de cierre** elimina el valor de inventario "actual" del producto (al coste actual, ya sea "medio" o "estándar")
- **Inventario de apertura** añade el valor de inventario "nuevo" del producto (al coste actual, ya sea "medio" o "estándar")

Siempre que se cree un ajuste de valor del inventario en la fecha actual, por lo tanto la **Fecha del movimiento** es la misma que la fecha de proceso de la transacción, todas las transacciones existentes permanecen valoradas al coste existente, pero las nuevas contabilizadas a partir de la fecha actual se valorarán al nuevo coste.

Siempre que se cree un ajuste de valor del inventario en el pasado, esos inventarios de cierre/apertura tendrán una **Fecha del movimiento** en el pasado y una fecha de proceso de la transacción. Estos inventarios se establecerán como transacciones "**Retroactivas**" por el proceso de cálculo de costes en segundo plano, por lo tanto se podrá crear el correspondiente ajuste de costes retroactivo.

Estas dos transacciones de inventario, inventario de apertura/cierre, pueden revisarse en la solapa **Transacción** de la ventana de producto y pueden contabilizarse en el libro mayor en la ventana **Inventario físico**.

### Cabecera

Un **Ajuste de Valor del Inventario** puede crearse y procesarse en la sección de cabecera de la ventana **Ajuste de Valor del Inventario**.

Un ajuste de valor del inventario puede crearse, gestionarse y procesarse en la sección de cabecera de la ventana **Ajuste de Valor del Inventario**.

![Cabecera](../../../../assets/drive/159RjgB2ff5cOtrsCcE0TxlbT6WyEtVWz.png)

Algunos campos a tener en cuenta son:

- **Tipo de documento**: es el tipo de documento del ajuste de valor del inventario
- **Nº de documento**: es la secuencia del documento del ajuste de valor del inventario
- **Fecha del documento**: es la fecha del ajuste de valor del inventario.

### Líneas

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

![Líneas](../../../../assets/drive/1Y-fYqIyNmSDOIwtEW9bqoKgALlRbyv7M.png)

Una vez creado, un ajuste de valor del inventario puede procesarse usando el botón de proceso **Proceso**.

Esa acción crea una transacción de inventario de cierre y otra de apertura que pueden revisarse en la solapa **Inventarios**.

### Inventarios

Se crean un inventario de cierre y uno de apertura para cada producto cuyo coste unitario o valor de inventario haya sido modificado.

Esta solapa de solo lectura contiene enlaces a información detallada como:

- **Almacén**: es el almacén donde ha tenido lugar el ajuste de valor del inventario.
- **Cerrar inventario**: es la transacción de inventario de cierre que elimina el inventario actual del producto al coste unitario actual.
- **Iniciar inventario**: es la transacción de inventario de apertura que añade el nuevo inventario del producto al nuevo coste unitario.

![Inventarios](../../../../assets/drive/1Hk2DRSMCFD4FQ5HPkVnIOhbsRioCKeFS.png)

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
## Ajuste de Costes

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Ajuste de Costes`

### Visión general

La ventana **Ajuste de Costes** permite al usuario revisar los ajustes de costes de las transacciones de producto provocados por cambios en los precios de compra, la asignación de **Landed Cost** o correcciones manuales/de coste negativo.

Una vez que el coste de una **"Product Transaction"** ha sido calculado por el proceso de **Costing Background** y de acuerdo con lo configurado para el/los producto(s) en la **Regla de costes** correspondiente, no puede recalcularse ni eliminarse.

Sin embargo, y bajo determinadas circunstancias, el coste calculado de una transacción de producto necesitaría ajustarse; por ejemplo, el precio de compra de una transacción de compra cambia después de recibir el producto.

Si ese es el caso, el coste calculado de la recepción deberá ajustarse al nuevo precio de compra.

La funcionalidad de **Ajuste de Costes** se encarga de gestionar los ajustes creados sobre el coste de una transacción ya calculada.

Es importante remarcar que esta funcionalidad tiene en cuenta el **algoritmo de cálculo de costes** utilizado para calcular los costes; por lo tanto, se comporta de forma diferente en función de:

- Si el algoritmo de cálculo de costes utilizado es **"Average"**, el coste de una transacción cambia y, como consecuencia, cambia el coste del producto implicado.  
  En ese caso, se crea en esta ventana una transacción de ajuste de costes para reflejar ese cambio; dicha transacción de ajuste de costes puede contabilizarse en el libro mayor para que el valor de inventario del producto sea el mismo que su valor contable.
- Sin embargo, si el algoritmo de cálculo de costes utilizado es **"Standard"**, el coste de una transacción no puede cambiar ni ajustarse, del mismo modo que el coste **"Standard"** del producto implicado permanece igual.  
  En ese caso, no se creará ninguna transacción de ajuste de costes en esta ventana.

Como consecuencia de lo anterior, la ventana **Ajuste de Costes** gestiona los ajustes de costes creados para productos y, por tanto, para transacciones de producto valoradas con el algoritmo de coste **"Average"**.

Existen diferentes tipos de **"cost adjustments sources"** que conducen al coste **"average"** correcto de un producto.

Por ejemplo, transacciones de recepción que no se contabilizaron en el mismo orden en que ocurrieron, o transacciones de recepción a las que es necesario añadir **Landed Cost** a su coste ya calculado; todo ello impactará y, por tanto, requerirá que cambie el coste **"average"** del producto.

Es importante remarcar que:

- los ajustes de costes son acumulativos; por lo tanto, una transacción de producto puede tener más de un ajuste de cualquier tipo si es necesario para que el coste medio de esa transacción de producto sea el correcto.
- existen dos tipos de transacciones:
  - aquellas transacciones cuyos costes deben ajustarse como "**source**" del ajuste; por ejemplo, un albarán de proveedor cuyo coste debe ajustarse debido a un cambio del precio de compra
  - aquellas transacciones cuyos costes deben ajustarse "**not as source**", sino como consecuencia de ajustar las transacciones fuente; por ejemplo, un albarán de cliente cuyo coste debe ajustarse porque cambió el coste del albarán de proveedor correspondiente.

Lo anterior implica que, por ejemplo, una cabecera de ajuste de costes de **"Price Difference Correction"** puede tener dos líneas de ajuste: una marcada como **Fuente** = Yes y la otra marcada como **Fuente** = No.

- además, existen dos tipos de ajustes:
  - aquellos configurados como **"Unit Cost" = "Yes"**, lo que significa que el ajuste va a cambiar el **Coste Unitario** de la transacción que se está ajustando, además de su **Coste Total**.  
    Este es el caso de ajustes como **"Price Difference Correction"**, **"Backdated Transactions"** y **"Manual Cost Correction"** configurados como **unit cost**, ya que estos cambian el coste **"basic"** de una transacción.
  - aquellos configurados como **"Unit Cost" = "No"**, lo que significa que el ajuste no va a cambiar el **Coste Unitario** de la transacción que se está ajustando, sino únicamente su **Coste Total**.  
    Este es el caso de costes **"extra"** como **"Landed Cost"**, o ajustes realizados para gestionar el coste en escenarios de **"Negative Stock"**, o **"Manual Cost Correction"** no configurados como **unit cost**, sino como un coste **"extra"**.

Imaginemos un escenario en el que solo existe una transacción de recepción de 1 unidad de un producto, valorada a 10,00 €/unidad. En ese caso, los costes de la recepción son los siguientes, que pueden revisarse en la ventana **Producto**, solapa **Transacciones**:

- Trx Orginal Cost: 10,00
- Total Cost : 10,00
- Unit Cost : 10,00

Se contabiliza para la recepción una corrección manual de costes configurada como **"Unit Cost" = "Yes"** por un importe de 2,00 €. Esa corrección crea un ajuste de costes que cambia el coste de la recepción como se muestra a continuación:

- Trx Orginal Cost: 10,00
- Total Cost : 12,00 (10,00 + 2,00)
- Unit Cost : 12,00 (10,00 + 2,00)

Nuevo coste medio del producto = Coste Total / Stock = 12,00 € / 1 unidad = 12,00 €/unidad

Después de eso, el precio de compra cambia de 10,00 €/unidad a 12,00 €/unidad.

Ese cambio en el precio es un ajuste de coste unitario, que crea un ajuste de 0,00 € porque el coste unitario de la transacción ya es 12,00.

Esto implica que no hay cambio en el coste medio del producto; se mantiene en 12,00 €/unidad.

Sin embargo, imaginemos ahora que la corrección manual de costes contabilizada para la recepción por un importe de 2,00 € se configuró como **"Unit Cost" = No**; es decir, es un coste extra que también debe tenerse en cuenta. Esa corrección cambia el coste de la recepción como se muestra a continuación; el coste unitario no cambia:

- Trx Orginal Cost: 10,00
- Total Cost : 12,00 (10,00 + 2,00)
- Unit Cost : 10,00

Después de eso, el precio de compra cambia de 10,00 €/unidad a 12,00 €/unidad.

Ese cambio en el precio crea un ajuste de costes en la recepción de 2,00 = 12,00 - 10,00 €; por lo tanto, cambian los costes calculados de la recepción:

- Trx Orginal Cost: 10,00
- Total Cost : 14,00 (12,00 + 2,00)
- Unit Cost : 12,00 (10,00 + 2,00)

Ahora, este nuevo escenario implica un cambio en el coste medio a 14,00 €/unidad; este nuevo coste medio incluye un coste extra de 2,00 €/unidad.

Como se ha mencionado brevemente, Etendo admite diferentes fuentes de ajustes de costes con el objetivo de cubrir distintos escenarios reales. Esos diferentes tipos de fuentes de ajustes de costes se explican en la siguiente sección.
### Cabecera

Los documentos de ajuste de costes se crean automáticamente mediante el proceso **Costing Background** o el proceso **Price Correction Background**, según corresponda, en función del origen del ajuste.

Una vez creado automáticamente, puede revisarse en esta ventana.

![Ajuste de Costes](../../../../assets/drive/1nLK6s6vSfV3C3rDRIjFq2dVRGCi1S-t4.png)

Algunos campos relevantes a tener en cuenta son:

- **Tipo de documento**: este es el tipo de documento "Ajuste de Costes".
- **Fecha de Referencia**: esta es la fecha en la que se crea el ajuste de costes.
- **Proceso Fuente**: las opciones disponibles son:
    - Transacción retroactiva
    - Landed Cost
    - Corrección manual de costes
    - Corrección de stock negativo
    - Corrección de diferencia de precio

Todos ellos se explicarán en detalle en las siguientes secciones.
### Transacción retroactiva

El origen de este ajuste de costes es una transacción de producto (es decir, un **Albarán (Proveedor)**) que debería haberse contabilizado en una fecha anterior, pero no fue así.

Como consecuencia, el coste calculado de las transacciones fechadas con posterioridad a esa fecha anterior dada necesita ajustarse, al igual que el coste "Promedio" calculado del producto.

Este tipo de origen de ajuste de costes no aplica a productos valorados a coste "Estándar".

El coste "Estándar" de un producto permanece tal y como fue definido, porque el coste de un producto valorado a "Estándar" es siempre el mismo, independientemente de la fecha en la que se contabilice una transacción de ese producto.

En el caso de un producto valorado con el algoritmo de cálculo de costes "Promedio":

- Un **Albarán (Proveedor)** con fecha 06/01/2015 (**Fecha del movimiento**) se contabiliza con fecha 06/01/2015 (fecha de transacción). Una vez contabilizado, este **Albarán (Proveedor)** implica que el coste del producto (basado en el precio correspondiente de la **Línea de pedido de compra**) es 105,00 €/unidad.
- Un **Albarán (Cliente)** con fecha 07/01/2015 (**Fecha del movimiento**) también se contabiliza en Etendo con fecha 07/01/2015 (fecha de transacción). Una vez contabilizado, este **Albarán (Cliente)** implica que el coste del producto vendido es 105,00 €/unidad.
- Posteriormente, un **Albarán (Proveedor)** del mismo producto con fecha 02/01/2015 (**Fecha del movimiento**) se contabiliza en Etendo con fecha 07/01/2015 (fecha de transacción). Una vez contabilizado, este **Albarán (Proveedor)** implica que el coste del producto (basado en el precio correspondiente de la **Línea de pedido de compra**) es 100,00, a partir del 02/01/2015.
- Esta última entrega con **Fecha del movimiento** 02/01/2015 es el origen de un ajuste de costes por transacción retroactiva que ajusta el coste del producto vendido con fecha 07/01/2015 de 105,00 €/unidad a 102,50 €/unidad; además, el coste promedio calculado cambia de 105,00 a 102,50 a partir del 06/01/2015.

Las transacciones que deberían haberse contabilizado en una fecha anterior conllevan la creación de ajustes de costes de tipo "Transacción retroactiva".

!!! info
    Se crean automáticamente una cabecera y línea(s) en la ventana **Ajuste de Costes** con los ajustes correspondientes.

Este tipo de ajuste cambia el "Coste Unitario" de las transacciones del producto, así como el "Coste Total" y, por lo tanto, el coste "Promedio" del producto.

Los ajustes de costes por transacción retroactiva se crean:

- ejecutando el proceso "**Ajuste Retroactivo de Transacciones**" en las reglas de coste existentes
- o marcando la casilla "**Transacción Ajustada Retroactivamente**" al crear una nueva regla de coste.

De ambas formas, es posible introducir una fecha "Ajustar retroactivamente desde", que no debe formar parte de un período cerrado.

Una vez que el proceso **Ajuste Retroactivo de Transacciones** está habilitado en la regla de coste correspondiente, los ajustes de costes por transacción retroactiva se calculan automáticamente mediante el proceso **Costing background** cuando aplique.
### **Contabilización de ajustes retroactivos**

Un ajuste de costes retroactivo puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, la última entrega con **Fecha del movimiento** 02/01/2015 es la fuente de un ajuste de costes de transacción retroactivo que ajusta el coste del producto vendido de 105,00 €/unidad a 102,50 €/unidad.

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se verá como se muestra a continuación:

|                      |                   |                   |
| -------------------- | ----------------- | ----------------- |
| Cuenta               | Débito            | Crédito           |
| _Inmovilizado del producto_      | Importe del Ajuste |                   |
| _Costo del producto_ |                   | Importe del Ajuste |
### **Landed Cost**

El origen de este ajuste de costes es la contabilización de costes adicionales que deben distribuirse y, por tanto, asignarse como costes adicionales del producto.

Los *landed cost* son costes como el transporte, el seguro, los aranceles aduaneros y otros costes necesarios para colocar el producto en el almacén de la organización.

Los ajustes de *landed cost* modifican el coste calculado de las transacciones de recepción cambiando su "Coste Total", del mismo modo que también cambia el coste "Promedio" del producto implicado.

El "Coste Unitario" de la transacción de recepción no cambia, ya que este tipo de ajuste no es un ajuste de coste unitario, sino un coste extra.

Este tipo de origen de ajuste de costes no aplica a productos valorados a coste "Estándar", en el sentido de que:

- siempre que se añada un *landed cost* a un producto valorado a coste estándar, no se crea ningún ajuste de costes, pero la "Desviación" entre el coste "estándar" definido para el producto y su coste "real" se contabiliza en una cuenta de "Desviación de Landed Cost", para que pueda analizarse posteriormente.

Por ejemplo:

- se contabiliza un pedido de compra que contiene un producto. Después, se contabilizan el albarán (proveedor) correspondiente y la factura de compra del producto, y se contabilizan en el libro mayor.
- posteriormente, se contabiliza una factura de compra que incluye costes adicionales como el coste de transporte y los cargos aduaneros, y se contabiliza en el libro mayor.
- la ventana Landed Cost permite asignar los costes de transporte y los cargos aduaneros al albarán (proveedor), *landed cost* que también se concilian con la factura ya contabilizada.

No es necesario ejecutar ningún proceso en segundo plano específico ni habilitar ninguna preferencia para obtener un ajuste de costes de "Landed Cost".

Los ajustes de costes de "Landed Cost" se crean tras procesar el documento de *landed cost* correspondiente en la ventana Landed Cost, o tras procesar la conciliación de *landed cost*.

!!! info
    Se crea automáticamente una cabecera y línea(s) en la ventana Ajuste de Costes de este tipo de ajuste de costes con el ajuste correspondiente.

Tal y como se ha mencionado, el ajuste de *landed cost* no cambia el "Coste Unitario" de las transacciones de un producto, sino su "Coste Total", del mismo modo que el coste "Promedio" del producto. Esto significa que:

- el coste unitario de cada transacción es el original (precio \* unidades)
- y el coste total de cada transacción incluye los ajustes necesarios para obtener el coste promedio deseado del producto.
### **Contabilización de ajustes de Landed Cost**

Los ajustes de Landed Cost pueden contabilizarse en el libro mayor en la ventana **Landed Cost**, siempre que dichos ajustes se hayan creado para productos incluidos en una transacción de **Albarán (Proveedor)**.

- En este caso, la transacción de **Albarán (Proveedor)** es la fuente del ajuste.

Además, los ajustes de Landed Cost también pueden crearse para productos incluidos en una transacción de **Albarán (Cliente)**.

- En este caso, la transacción de **Albarán (Cliente)** no es la fuente del ajuste, sino el **Albarán (Proveedor)**.
- En este caso, los ajustes de Landed Cost deben contabilizarse en la ventana **Ajuste de Costes**.
### **Corrección manual de costes**

El origen de este ajuste de costes es un cambio manual del coste de una transacción de producto específica.

Este tipo de ajuste solo aplica a transacciones de producto valoradas a coste "Promedio". No tiene sentido cambiar manualmente el coste de una transacción valorada a coste "Estándar".

Por ejemplo:

- es necesario ajustar un movimiento entre almacenes, por lo que el coste de la transacción "Movimiento desde" se cambia (incrementa) manualmente por el usuario final
- el cambio anterior implica que el coste de la transacción "Movimiento a" también debe cambiarse (incrementarse), por lo que se crea el ajuste de costes correspondiente de tipo "Corrección manual de costes".

No es necesario ejecutar ningún proceso en segundo plano específico ni habilitar ninguna preferencia para obtener un ajuste de costes de tipo "Corrección manual de costes".

Los ajustes de costes de tipo "Corrección manual de costes" se crean después de cambiar el coste de una transacción de producto en la ventana Producto, solapa "Transacciones", utilizando el botón de proceso "Ajuste manual de costes".

Se crea automáticamente una cabecera y línea(s) en la ventana Ajuste de Costes de este tipo de ajuste de costes con el ajuste correspondiente.

Este tipo de ajuste cambia el "Coste Total" de la transacción de producto; sin embargo, el "Coste Unitario" de la transacción de producto puede cambiarse o no, dependiendo de lo que el usuario final desee obtener.

Hay una casilla de verificación llamada "**Coste Unitario**" que se muestra siempre que se seleccione la casilla de verificación "**Incremental**":

- Si el usuario no selecciona la casilla de verificación "**Incremental**", significa contabilizar un nuevo coste total de la transacción que permanecerá como "**Permanente**". Esto significa que ya no se modificará.
- Si el usuario selecciona la casilla de verificación "Incremental", significa contabilizar un coste adicional para asignar al coste total de la transacción. Además, este coste adicional puede formar parte del coste unitario (**casilla Coste Unitario = Sí**) de la transacción o no (**casilla Coste Unitario = No**). Este último caso significa un coste extra, como un landed cost.

**Contabilización del ajuste de Corrección manual de costes**

Este tipo de ajuste puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, el coste de la transacción "Movimiento desde" se cambia (incrementa) manualmente por el usuario final; por lo tanto, el coste de la transacción "Movimiento a" también debe cambiarse (incrementarse).

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se verá como se muestra a continuación:

Ajuste de la transacción **"Movimiento desde"**:

|                                                                                                 |                                                  |                                                |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------- |
| Cuenta                                                                                          | Débito                                           | Crédito                                        |
| [_Diferencias de almacén_](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#defaults-tab) | Importe del ajuste de la transacción "Movimiento desde" |                                                |
| [_Inmovilizado del producto_](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)                            |                                                  | Importe del ajuste de la transacción "Movimiento a" |

Ajuste de la transacción **"Movimiento a"**:

|                                                                                                 |                                                |                                                |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| Cuenta                                                                                          | Débito                                         | Crédito                                        |
| [_Inmovilizado del producto_](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)                            | Importe del ajuste de la transacción "Movimiento a" |                                                |
| [_Diferencias de almacén_](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#defaults-tab) |                                                | Importe del ajuste de la transacción "Movimiento a" |
### **Corrección de stock negativo**

El origen de este ajuste de costes es contabilizar una transacción, es decir, un albarán (cliente), que convierte el stock de un producto en una cantidad negativa. Este tipo de corrección solo está implementado para el cálculo de costes **"Promedio"**.

En el momento de contabilizar una nueva entrada de ese artículo, independientemente de si esa entrada convierte el stock del artículo en un valor positivo/negativo/cero, se crea un ajuste de corrección de coste negativo y se relaciona con esa nueva entrada, para conseguir que el stock restante de ese producto se valore al último precio de compra, en el caso del cálculo de coste **"Promedio"**.

Por ejemplo:

- se contabiliza un pedido de compra de 100 unidades a un precio de compra determinado
- después se recibe la mercancía y el coste de la mercancía se calcula en base al precio de compra del pedido
- a continuación se contabiliza un albarán (cliente) de 100 unidades
- y posteriormente se contabiliza otro albarán (cliente) de 5 unidades, lo que provoca un stock negativo del producto.

Se creará un ajuste de costes de corrección de stock negativo siempre que se contabilice una transacción de entrada del producto, como un albarán (proveedor). Ese ajuste se asignará al albarán (proveedor).

Este tipo de ajuste no cambia el **"Coste Unitario"** del albarán (proveedor), pero sí su **"Coste Total"**, del mismo modo que cambia el coste **"Promedio"** del producto implicado. Esto significa que:

- el coste unitario de cada transacción es el coste original (precio \* unidades)
- y el coste total de cada transacción incluye los ajustes necesarios para obtener el coste promedio deseado.

Hay dos acciones que debe realizar para obtener ajustes de costes de corrección de stock negativo:

- Configurar la preferencia **Permitir Correcciones de Stock Negativo** con Valor=Y en la ventana _Preferencias_
- Planificar el **proceso de Costing Background** en la ventana _Procesamiento de Peticiones_
### **Contabilización del Ajuste de Corrección de Stock Negativo**

Este tipo de ajuste puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, se crea un ajuste de este tipo cada vez que se contabiliza una nueva transacción de entrada, como un albarán (proveedor), para el producto que tiene stock negativo.

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se mostrará como se indica a continuación en el caso de un importe del ajuste negativo; en caso contrario, si el importe del ajuste es positivo:

|                                                                                                 |                   |                   |
| ----------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| Cuenta                                                                                          | Debe              | Haber             |
| [_Diferencias de almacén_](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#defaults-tab) | Importe del Ajuste |                   |
| [_Inmovilizado del producto_](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)                            |                   | Importe del Ajuste |
### **Corrección de diferencia de precio**

El origen de este ajuste de costes es un cambio en el precio de compra de un pedido o en el precio de compra de una factura después de recibir los bienes.

La Corrección de diferencia de precio se lanza únicamente para Transacciones de tipo _Entrega_. Otras transacciones, como devoluciones de material o transacciones de salida, no se tienen en cuenta, ya que no deberían modificar el coste "Promedio" debido a una corrección de precio.

Esos bienes se recibieron a un precio que ha cambiado; por lo tanto, el coste calculado de la entrega debe ajustarse, al igual que el coste calculado "Promedio" del producto.

El coste "Estándar" permanecería tal y como se estableció.

Por ejemplo:

- se contabiliza un pedido de compra para un producto a un precio de compra determinado
- después se recibe el producto y se calcula el coste "Promedio" del producto en base al precio de compra del pedido correspondiente.
- se contabiliza un albarán (cliente) de ese producto; por lo tanto, esa transacción de salida obtiene el coste "Promedio" calculado del producto.
- posteriormente se recibe y contabiliza una factura de compra para el producto a un precio superior al precio de compra del pedido
- es necesario crear un ajuste de costes de corrección de diferencia de precio para ajustar el Albarán (Proveedor) y, a continuación, afectar a la transacción de Albarán (Cliente) en base al nuevo coste Promedio calculado del producto.

Los cambios en el precio de compra conllevan la creación de ajustes de costes de "Corrección de diferencia de precio".

Se crea automáticamente una cabecera y línea(s) en la ventana **Ajuste de Costes** de este tipo de ajuste de costes con el ajuste correspondiente.

Este tipo de ajuste modifica el "Coste Unitario" y el "Coste Total" de las transacciones, al igual que el coste "Promedio" de los productos.

Los ajustes de corrección de "Diferencia de precio" pueden realizarse de forma automática o manual:

- para que Etendo realice automáticamente los ajustes de costes de corrección de diferencia de precio, es necesario activar y planificar el Proceso en segundo plano de corrección de precios
- para que el usuario pueda realizar manualmente los ajustes de costes de corrección de diferencia de precio, es necesario ejecutar manualmente el "Procesar ajuste de diferencia de precio"

Como se muestra en la imagen siguiente, este proceso permite seleccionar la Organización para la que debe ejecutarse, introducir una fecha de movimiento determinada y seleccionar un producto o conjunto de productos para los que deban crearse ajustes de costes de corrección de diferencia de precio.

![Ajuste de costes](../../../../assets/drive/18dMx0odX-PVVwMCGGtEnkfYNfctDa7o5.png)

Adicionalmente, el Proceso en segundo plano de cálculo de costes también puede crear ajustes de costes de corrección de diferencia de precio, solo si:

- la preferencia de propiedad "Habilitar correcciones automáticas de diferencia de precio" está establecida en "Y"
- y el Proceso en segundo plano de cálculo de costes se ejecuta después de contabilizar el Pedido de compra, el Albarán (Proveedor) y la Factura de compra correspondientes, incluyendo la diferencia de precio.
### **Contabilización del Ajuste de Corrección de Diferencia de Precio**

Este tipo de ajuste puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, un cambio en el precio del pedido de compra (incremento) implica que tanto el coste calculado del "**Albarán (Proveedor)**" como el coste calculado del "**Albarán (Cliente)**" deben ajustarse, al igual que el coste "**medio**" del producto.

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se verá como se muestra a continuación:

**Ajuste de Albarán (Proveedor)**

|                                                                                 |                                 |                                 |
| ------------------------------------------------------------------------------- | ------------------------------- | ------------------------------- |
| Cuenta                                                                           | Débito                          | Crédito                         |
| [_Product Asset_](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)            | Importe del ajuste de Albarán (Proveedor) |                                 |
| [_Invoice Price Difference_](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting) |                                 | Importe del ajuste de Albarán (Proveedor) |

**Ajuste de Albarán (Cliente)**

|                                                                           |                                  |                                  |
| ------------------------------------------------------------------------- | -------------------------------- | -------------------------------- |
| Cuenta                                                                     | Débito                            | Crédito                           |
| [_Cost of Goods Sold_](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting) | Importe del ajuste de Albarán (Cliente) |                                  |
| [_Product Asset_](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)      |                                  | Importe del ajuste de Albarán (Cliente) |

#### **Línea**

Un documento de ajuste de costes puede tener tantas líneas de ajuste como productos incluidos en las recepciones a las que se hayan asignado costes adicionales.

Existen dos tipos de transacciones de ajustes de costes:

- "**fuente**", por ejemplo una recepción de proveedor (V+) cuyo precio de compra ha cambiado
- "**no fuente**", por ejemplo un envío a cliente (C-) cuyo coste debe ajustarse debido a que se está ajustando el coste de la recepción del proveedor.

![Ajuste de costes](../../../../assets/drive/1vta9aBh20mSzCWRvr4jHKjwNMa5QtEyk.png)

Algunos campos relevantes a tener en cuenta son:

- **Operaciones de almacén**: las transacciones disponibles son:
    - Recepción de proveedor (V+)
    - Envío a cliente (C-)
    - Entrada de inventario (I+)
    - Salida de inventario (I-)
    - Movimiento desde (M-)
    - Movimiento hacia (M+)
    - Producción (P+)
    - Producción (P-)
    - Consumo interno (D-)
    - Consumo interno (D+)
- **Importe del Ajuste**: es el importe del ajuste de costes.  
  Un importe de ajuste también puede revisarse en la ventana **Producto**, en la solapa "**Transacción**", solapa "**Coste de la transacción**", siempre relacionado con una "**Línea de Ajuste de Coste**".
- **Fuente**: las opciones disponibles son "Sí" o "No", ya que una transacción de producto puede ser la fuente de un ajuste o no.
- **Línea de Ajuste de Costes Padre**: en el caso de un ajuste de costes que no es la fuente, este campo muestra la línea de ajuste de costes fuente.
- **Necesita contabilización**: las opciones disponibles son "Sí" o "No". La mayoría de los ajustes de costes deben contabilizarse en el libro mayor, ya que implican un incremento/disminución del valor del inmovilizado del producto; sin embargo, existen otros cuyo ajuste de costes es 0,00 y no requieren contabilización.
- **Coste Unitario**: las opciones disponibles son "Sí" o "No".
  - Existen ajustes de costes como la corrección de diferencia de precio que impactan en el coste unitario del producto.
  - Existen ajustes de costes como el coste adicional que no impactan en el coste unitario del producto.  
    Es importante remarcar que cada **Transacción de producto** tiene los costes que se listan a continuación:
    - "**Coste Original Trx**", que es el coste original de la transacción de producto
    - "**Coste Total**", que es la suma del coste original y todos los costes de ajuste
    - "**Coste Unitario**", que es la suma del coste original y todos los ajustes del coste unitario; es decir, el coste que no incluye el coste adicional.
- **Transacción Retroactiva**: un ajuste de costes puede marcarse como transacción retroactiva si aplica.  
  Por ejemplo, un ajuste de costes de una transacción retroactiva puede tener dos líneas: una que es la transacción retroactiva como fuente y otra que no es la fuente ni una transacción retroactiva.
- **Permitir Correcciones de Stock Negativo**: un ajuste de costes puede marcarse como corrección de stock negativo si aplica.  
  Por ejemplo, un ajuste de costes de una transacción retroactiva puede tener dos líneas: una que es la transacción retroactiva como fuente y otra que no es la fuente, pero sí una corrección de stock negativo.

#### **Contabilidad**

Esta solapa proporciona información contable del **Ajuste de Costes**.

![Ajuste de costes](../../../../assets/drive/1VeXLRgA1XTypzkIYGOloEycvI7i138Pi.png)

Los asientos mostrados en esta solapa son diferentes en función de la fuente del ajuste, pero la contabilización de coste adicional se gestiona en la ventana **Landed Cost**.

Las líneas de ajuste de coste adicional siempre se crean como "Necesita contabilización" = No.

A continuación se muestran algunos ejemplos de cada tipo de ajuste de costes:

**Corrección de precio**: ajuste de costes causado por una disminución del precio de compra

|                        |                        |                        |
| ---------------------- | ---------------------- | ---------------------- |
| Cuenta                 | Débito                 | Crédito                |
| Desviación pr. factura | Importe del ajuste de costes |                        |
| Inmovilizado del producto |                        | Importe del ajuste de costes |

**Corrección de precio**: ajuste de costes causado por un incremento del precio de compra

|                        |                        |                        |
| ---------------------- | ---------------------- | ---------------------- |
| Cuenta                 | Débito                 | Crédito                |
| Inmovilizado del producto | Importe del ajuste de costes |                        |
| Desviación pr. factura |                        | Importe del ajuste de costes |

**Transacciones retroactivas**: ajuste sobre una transacción de albarán de recepción del producto.

El coste del producto se reduce.

|                       |                        |                        |
| --------------------- | ---------------------- | ---------------------- |
| Cuenta                | Débito                 | Crédito                |
| Diferencias de almacén | Importe del ajuste de costes |                        |
| Inmovilizado del producto |                        | Importe del ajuste de costes |

**Transacciones retroactivas**: ajuste sobre una transacción de albarán de envío del producto.

El coste del producto se reduce.

|               |                        |                        |
| ------------- | ---------------------- | ---------------------- |
| Cuenta        | Débito                 | Crédito                |
| Costo del producto | Importe del ajuste de costes |                        |
| Inmovilizado del producto |                        | Importe del ajuste de costes |

**Corrección negativa**: ajuste que implica un incremento del coste del producto.

|                       |                        |                        |
| --------------------- | ---------------------- | ---------------------- |
| Cuenta                | Débito                 | Crédito                |
| Inmovilizado del producto | Importe del ajuste de costes |                        |
| Diferencias de almacén |                        | Importe del ajuste de costes |

**Corrección manual de costes**: ajuste causado por un incremento manual del coste del producto.

|                       |                        |                        |
| --------------------- | ---------------------- | ---------------------- |
| Cuenta                | Débito                 | Crédito                |
| Inmovilizado del producto | Importe del ajuste de costes |                        |
| Diferencias de almacén |                        | Importe del ajuste de costes |
### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de **contabilización masiva** permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Inventario Referenciado

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Inventario Referenciado`

### Visión general

En esta ventana, es posible definir los contenedores o cajas, lo cual incluye cualquier tipo de objeto que pueda contener mercancías.

Muchas empresas mueven y almacenan mercancías agrupadas en un RollTainer, caja o contenedor. Las cajas pueden ser reutilizables o desechables y tienen diferentes tamaños y propósitos, siendo adecuadas para distintos tipos de mercancías.

El Inventario Referenciado es la funcionalidad que identifica uno o varios detalles de almacenamiento (registros de stock) mediante un "Número de referencia".

El Inventario Referenciado para Core incluye la funcionalidad más básica para Empaquetar/Desempaquetar stock.

### Inventario Referenciado

Esta solapa muestra cualquier inventario referenciado, también conocido como caja, declarado en el sistema independientemente de si está vacío o tiene stock en su interior.

El usuario puede crear nuevas cajas en cualquier momento. Es obligatorio definir una organización, clave de búsqueda y el tipo de inventario referenciado.

Es importante destacar que:

1. No será posible eliminar un registro si el inventario referenciado está vinculado a alguna transacción de Empaquetar/Desempaquetar.
2. La clave de búsqueda es única por cliente. Para evitar esta limitación, puede declarar un prefijo/sufijo diferente en la secuencia del tipo de inventario referenciado.
3. La organización limita el stock que puede empaquetarse (solo el stock declarado en esta organización o en cualquier organización hija).

Desde esta ventana es posible vincular/desvincular stock a/desde un Inventario Referenciado usando los botones Empaquetar y Desempaquetar respectivamente.

### Empaquetar

Muestra un P&E con el stock aún no vinculado a ningún inventario referenciado (no es posible empaquetar un stock ya empaquetado).

![Empaquetar](../../../../assets/drive/1JQfT41NnGHscmbx1FygnOuvFwxi3co5v.png)

El usuario puede seleccionar uno o varios registros y especificar la cantidad a empaquetar. También es obligatorio declarar el campo **Movido a** donde se almacenará el stock empaquetado.

Si el hueco actual de cualquiera de los registros seleccionados es diferente de **Movido a**, el sistema realizará automáticamente un Movimiento entre almacenes al confirmar la acción para mover el stock.

La acción de empaquetado puede ejecutarse en diferentes lotes en cualquier momento; es decir, el usuario puede seleccionar cualquier inventario referenciado no vacío para añadir más stock.

!!! info
    Un Inventario Referenciado específico solo puede estar presente en un único hueco, no en varios huecos al mismo tiempo. En caso de que quiera añadir más stock a una caja no vacía, el selector **Movido a** solicitará al usuario que seleccione el hueco actual del inventario referenciado.

Cuando un stock se empaqueta, la clave de búsqueda del inventario referenciado se añadirá automáticamente al final del **Valor atributos** entre corchetes **\[\]** (representación gráfica de una caja). Ejemplo: L582\[1000584\]

Si el stock no tiene atributo, el inventario referenciado se mostrará igualmente en el campo **Valor atributos** para indicar que el stock está actualmente empaquetado. Ejemplo: \[1000584\]

De este modo, la información sobre el inventario referenciado es claramente visible en cualquier lugar donde sea necesario, como el Informe de stock.

### Desempaquetar

Muestra un P&E con el stock actualmente vinculado al inventario referenciado seleccionado.

![Desempaquetar](../../../../assets/drive/1sKmYK_BGCx8XXDXtuXJLcJ4dQ1pTa1-x.png)

El usuario puede seleccionar uno o varios registros y especificar la cantidad a desempaquetar (por lo que es posible ejecutar un desempaquetado parcial) y el nuevo hueco donde se almacenará el stock tras desempaquetarlo (por defecto se desempaquetará en la ubicación actual).

!!! note
    A diferencia del proceso de empaquetado explicado anteriormente, en el desempaquetado se pueden seleccionar distintos huecos para cada registro.

### Comportamiento de gestión de reservas

Al ejecutar un proceso de Empaquetar/Desempaquetar, el sistema siempre intentará trabajar primero con cantidades no reservadas. Ejemplo: si tenemos 10 unidades disponibles de un producto, de las cuales 2 están reservadas, e intentamos empaquetar/desempaquetar 1 unidad, el sistema intentará empaquetar/desempaquetar primero cualquiera de las 8 unidades no reservadas.

Si el proceso de Empaquetar/Desempaquetar necesita trabajar con cantidades ya reservadas (en el ejemplo anterior, porque estamos empaquetando/desempaquetando 9 o 10 unidades), el sistema intentará reasignar al vuelo cualquier reserva o mostrará un error cuando la reasignación no sea posible. Esto último puede ocurrir, por ejemplo, porque la reserva está forzada a un hueco concreto y el proceso de Empaquetar/Desempaquetar intenta mover el stock a otro hueco.

### Contenido

Stock actualmente vinculado a este Inventario Referenciado.

Tenga en cuenta que cualquier stock empaquetado tendrá un valor de atributos vinculado al inventario referenciado.

### Transacciones Empaquetado

Muestra cualquier transacción de empaquetado ejecutada en el pasado para este inventario referenciado.

Este tipo de transacciones son en realidad Movimientos entre almacenes creados al vuelo al confirmar el empaquetado, a los cuales el usuario puede acceder en cualquier momento para ver los detalles.

### Transacciones Desempaquetado

Muestra cualquier transacción de desempaquetado ejecutada en el pasado para este inventario referenciado.

Este tipo de transacciones son en realidad Movimientos entre almacenes creados al vuelo al confirmar el desempaquetado, a los cuales el usuario puede acceder en cualquier momento para ver los detalles.

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.