---
title: Gestión de Ventas
---

## Visión general

Gestión de Ventas se ocupa de todas las actividades relacionadas con el proceso de ventas al cliente y los informes correspondientes.

## Presupuesto de ventas

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Presupuesto de ventas`

Un presupuesto no es un tipo de documento de pedido de venta, sino un tipo de documento diferente denominado "Presupuesto", vinculado a una secuencia de documento específica.

Para poder crear un pedido de venta a partir de un presupuesto de ventas, el tipo de documento del presupuesto debe estar configurado correctamente. Esto significa que requiere que se defina un tipo de documento (p. ej., Pedido estándar) en el campo "Tipo de documento para pedido".

El flujo general es el siguiente:

- Crear un presupuesto de ventas.
- Crear un pedido de venta a partir del presupuesto de ventas o rechazar el presupuesto.

![Acciones y estados en presupuestos](../../../../assets/drive/1Ebptd-ihEnTZ0PicQvT4HmTHI0bAu52y.png)

1\. Acciones en presupuestos:

- **Registrar**: esta acción permite al usuario procesar el presupuesto.
- **Reactivar**: esta acción permite al usuario añadir, eliminar o modificar una o varias líneas del presupuesto.
- **Crear un pedido de venta**: esta acción convierte el presupuesto en un pedido de venta.
- **Rechazar**: esta acción cancela/rechaza el presupuesto.

2\. Estados del presupuesto:

- **Borrador**: en este estado se permite introducir, eliminar y modificar líneas. Se alcanza tras hacer clic en Nuevo o reactivar el documento.
- **En evaluación**: después de registrar el presupuesto. En este estado el documento no se puede modificar. Las acciones posteriores son:  
    - **Reactivar**  
    - **Crear un pedido de venta**  
    - **Rechazar el presupuesto**
- **Cerrado - Pedido creado**: después de crear el pedido de venta, el documento pasa a este estado. No se permiten más acciones.

!!! info
    Un presupuesto, un pedido de venta. No se pueden crear varios pedidos de venta a partir del mismo presupuesto.

- **Cerrado - Rechazado**: cuando el presupuesto finalmente no es aceptado por el cliente. Es obligatorio introducir un motivo de rechazo. No se permiten más acciones.

### Cabecera

El usuario puede crear un presupuesto de ventas y procesarlo cuando esté listo.

![Cabecera de presupuestos de ventas](../../../../assets/drive/1mGI2PwGXX8NokA5eSauNdO3hpyCM1lH9.png)

La cabecera enumera los principales términos y condiciones relacionados con el presupuesto del cliente que se utilizan en el encabezado de su copia impresa y posteriormente en su proceso de pedido, envío y facturación.  
En la mayoría de los casos, el campo principal y único necesario para crear un nuevo presupuesto es el campo Terceros. Todos los demás campos se completan automáticamente en función del Terceros seleccionado, las preferencias del usuario conectado y otros parámetros por defecto del sistema.

Otros campos a tener en cuenta son:

**Válido hasta:** este campo proporciona información sobre la fecha límite de validez del presupuesto.  
**Motivo del rechazo:** este campo informa del motivo por el cual un presupuesto ha sido rechazado por un cliente. Es obligatorio al rechazar un presupuesto.

**Aspectos a tener en cuenta:**

Aparece un nuevo botón Crear pedido cuando el estado es En evaluación. Al pulsar el botón, se crea un pedido de venta basado en el presupuesto.

!!! info
    Los impuestos siempre se recalculan en función de la fecha de la transacción (fecha en la que ejecuta el botón).

El estado del pedido de venta recién creado es Registrado. Es posible cambiar la "Facturación" del pedido de venta, así como "Reactivar" el pedido si necesita ser modificado.

Antes de crear un pedido de venta, el sistema muestra un indicador denominado Presupuesto en firme, que está marcado por defecto:

![Presupuesto en firme](../../../../assets/drive/1zRP6rz_UJ-8Y9tdp9l6XCHP_QU7DrN9B.png)

- Si está seleccionado, establece un compromiso con el cliente para el suministro de una cantidad determinada de bienes a un precio presupuestado; por lo tanto, el pedido de venta será idéntico al presupuesto.
- Si no está seleccionado, un cambio posterior en la tarifa modificará los precios presupuestados, del mismo modo que en el pedido de venta. La Modificación de precios también se recalculará aplicando las nuevas en función de la fecha de la transacción (la fecha en la que se ejecuta el botón).

### Líneas

Añada productos que se incluirán en su presupuesto de ventas. Cada producto se puede añadir creando una nueva línea.  
La solapa Líneas lista cada producto a presupuestar y sus características.  
El botón Registrar completa el presupuesto de ventas cuando se han introducido todos los productos.

#### Línea de impuesto

Esta solapa muestra los impuestos relacionados con la línea del presupuesto.  
La solapa de solo lectura Línea de impuesto detalla la información de impuestos para cada línea de un pedido de venta en función de su campo Impuesto, que se completa automáticamente según la configuración de impuestos.

#### Descuentos

Esta solapa del presupuesto de ventas lista información sobre los descuentos aplicados automáticamente y/o introducidos manualmente para el documento.

#### Impuesto

El usuario puede editar los impuestos aplicados al presupuesto.  
Resume la información relacionada con impuestos para todo el presupuesto de ventas. Contiene tantos registros como tipos impositivos utilizados en el presupuesto.

### **Presupuesto de ventas avanzado**

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Sales Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Sales Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/sales-extensions/release-notes.md).

A través de esta ventana, el usuario puede generar presupuestos de ventas y crear los pedidos correspondientes a partir de dichos presupuestos.

#### Cabecera

La cabecera principal enumera los términos y condiciones relacionados con el presupuesto de ventas que se utilizan en el encabezado de la copia impresa y, posteriormente, en su proceso de pedido, recepción de mercancía y factura.

![](../../../../assets/drive/1S8cwq-7SwxMd-0JDD6uzDfTDtSOGn_8b.png)

La solapa principal lista los términos y condiciones principales relacionados con el presupuesto de ventas que se utilizan en el encabezado de la copia impresa y posteriormente en el proceso de pedido, albarán y facturación.
En esta sección, los campos a cumplimentar son los siguientes:

- Documento transacción: será el tipo de documento específico a utilizar. En este caso, se denomina "Presupuesto".
- Nº de documento: el número de identificación del presupuesto se genera automáticamente.
- Fecha de presupuesto: la fecha del presupuesto. Por defecto, será la fecha actual.
- Terceros: se seleccionará el cliente al que se realiza el presupuesto.
- Dirección del tercero: en la lista desplegable, seleccione aquellas direcciones del cliente que tengan marcada la opción "Dir.envíos".
- Tarifa: seleccione entre todas las tarifas de ventas disponibles. Por defecto, se trae la tarifa configurada para ese tercero en su ficha.
- Vincular pedido (casilla de verificación): si esta casilla está marcada, al ejecutar el proceso "Cambiar cliente, tarifa y moneda", el campo "Pedido de origen" del nuevo presupuesto se crea modificando el anterior. Se establecerá con el número del presupuesto original, es decir, el que se está modificando, que estará en estado "Cerrado - Rechazado". A su vez, se generará un registro en la solapa Historial de este último (presupuesto original) cada vez que haya modificaciones relacionadas con él.
- Unidad de cantidad/tiempo: la fecha de validez del presupuesto se define en función de un periodo de tiempo: 10 días, 1 semana, 2 meses, etc.
- Válido hasta: fecha de vencimiento del presupuesto estipulada según los campos Unidad de cantidad/tiempo.
- Plazo de entrega/Unidad de medida del plazo de entrega: la fecha de entrega se define a partir de un periodo de tiempo. Por ejemplo: 3 semanas.
- Método de pago: se completa por defecto con el método de pago asociado al tercero seleccionado, con posibilidad de edición.
- Condiciones de pago: se completa por defecto con las condiciones de pago asociadas al tercero seleccionado, con posibilidad de edición.
- Almacén: el almacén desde el cual se enviarán los productos a entregar al cliente.
- Motivo del rechazo: es un menú desplegable donde se puede seleccionar un motivo de rechazo en caso de que el presupuesto sea rechazado. Los distintos motivos de rechazo serán definidos por el usuario.
- Agente comercial: puede seleccionar en una lista desplegable el empleado que está realizando el presupuesto al cliente. Debe estar configurado como un tercero con la marca "Operarios" y "Agente comercial".
- Pedido de origen: cuando se ejecuta el botón "Cambiar cliente, tarifa y moneda" y está marcada la casilla "Vincular pedido", el nuevo presupuesto creado se establece en este campo, modificando el anterior, con el número del presupuesto original, es decir, el que se está modificando; que estará en estado "Cerrado - Rechazado".
- Descripción: espacio para escribir información adicional relacionada.

#### Barra de estado

Esta barra muestra la siguiente información:

- Los posibles estados de documento para un presupuesto serán:

**Borrador**: permite introducir, eliminar y modificar líneas en este estado. Se alcanza tras hacer clic en el botón Nuevo o al reactivar el documento.<br>
**En evaluación**: este estado se alcanza después de registrar el presupuesto. En esta fase, el documento no se puede modificar.<br>
**Cerrado - Pedido creado**: después de crear el pedido de venta, el documento alcanza este estado. Una vez alcanzado, no se permiten más acciones.<br>
**Cerrado - Rechazado**: este estado aparece en caso de que el presupuesto sea rechazado por el cliente. Es obligatorio introducir un motivo de rechazo.
Una vez alcanzado este estado, no se permiten más acciones. <br>

- Importe total: indica el importe monetario final del presupuesto, incluidos los impuestos.
- Importe neto total: indica el importe monetario final del presupuesto, excluidos los impuestos.
- Moneda: indica en qué moneda se define el presupuesto. Este campo se completa según la tarifa seleccionada.

#### Solapa Líneas

Una vez completada la cabecera, deben añadirse las líneas.

**Descuentos** <br>
-Descuento: es la reducción porcentual aplicada al precio de tarifa.<br>
-Cascada: es cualquier descuento adicional basado en el total restante tras aplicar los descuentos anteriores.
Activo: es una marca que indica si este registro está disponible para su uso o está deshabilitado.<br>

**Impuesto** <br>
Esta solapa resume la información relacionada con los impuestos implicados en el presupuesto.
Contiene tantos registros como categorías de impuestos estén implicadas en el presupuesto.

- Número de línea: indica la posición de la línea en el documento.<br>
- Impuesto: indica el tipo impositivo aplicable a un producto determinado.<br>
- Base imponible: indica el importe sobre el que se calculará el impuesto.<br>
- Impuestos: indica el importe del impuesto resultante de los campos Impuesto y Base imponible.<br>

**Solapa Historial**
Cuando se hace clic en el botón "Cambiar cliente, tarifa y moneda" en un presupuesto y está marcada la casilla "Vincular pedido", se crea un registro en esta solapa con los datos del nuevo presupuesto creado y, a su vez, uno por cada una de las modificaciones sucesivas del presupuesto original.

La información mostrada en cada registro es la siguiente:

- Número de documento del nuevo presupuesto.
- Fecha del presupuesto.
- Importe original del presupuesto.

![](../../../../assets/drive/1XoFvD98AeaJDehEjw0rJtqNyzo8GaeeW.png)

**Acción**<br>

- Registrar: esta acción permite al usuario generar el presupuesto.<br>
- Reactivar: esta acción permite al usuario añadir, eliminar o modificar una o varias líneas del presupuesto.<br>
- Crear un pedido de venta: esta acción convierte el presupuesto en un pedido de venta. Para ello, el tipo de documento del presupuesto debe estar configurado correctamente. Esto significa que requiere que se defina un tipo de documento (p. ej., pedido estándar) en el campo "Tipo de documento de pedido". Este botón aparece cuando el estado del presupuesto es "En evaluación".<br>

El estado del pedido de venta recién creado será "Registrado". En este caso, es posible cambiar las "Condiciones de facturación", así como "Reactivar" si necesita ser modificado.

!!! info
    Solo se puede crear un pedido de venta para el mismo presupuesto.

- Rechazar: esta acción permite cancelar o rechazar el presupuesto. Para esta acción es obligatorio indicar un motivo de rechazo.

Etendo también permite generar pedidos de venta parciales, ya sea para las líneas que el usuario necesita convertir o para la cantidad de producto que necesita convertir. Aplique esta funcionalidad seleccionando la(s) línea(s) necesaria(s) y editando el importe del producto en la solapa Importe a generar.

![](../../../../assets/drive/1epl5s-9vyWosFF7SwSlkvIccNRQtUOA3.png)

![](../../../../assets/drive/1xnqd0rhg4x4qkkafts9k15cIH2Ta2QxP.png)

![](../../../../assets/drive/1iXJD_abYYG0cdIPP2CASxhkFIKx3IuGh.png)

El presupuesto se mantendrá disponible para generar pedidos futuros con el importe restante. Para crear un pedido con el importe restante, siga el mismo procedimiento desde la ventana Presupuesto de ventas.

![](../../../../assets/drive/172BWCl-99Q1DuAUL9gIlB0PjVnP2irou.png)

![](../../../../assets/drive/1O0s-75pITf1xHcBXYQnYS0TxiRXvRPxx.png)

**Botón Cambiar cliente, tarifa y moneda**

Este proceso permite realizar cambios en el tercero, la tarifa y/o la moneda del documento, tanto si el documento está en borrador como si está registrado. Se pueden modificar una o varias variables al mismo tiempo.
Si se cambia el tercero, el impuesto se actualizará en las líneas (si es necesario).

En la ventana emergente que se abre al ejecutar este proceso, el usuario verá la marca “no aplicar tipo de conversión”. Si se pretende cambiar la moneda del presupuesto incluyendo la conversión al tipo de cambio oficial, la casilla debe desmarcarse al seleccionar la opción Moneda. En caso contrario, la casilla debe marcarse para que el sistema muestre el importe del presupuesto en la moneda deseada, definiendo los precios de acuerdo con la tarifa configurada por defecto en dicha moneda.

!!! info
    Una vez ejecutado, el presupuesto se cerrará y se creará uno nuevo con los cambios realizados en el estado “en evaluación”. En el presupuesto cerrado, se establece un motivo de rechazo por defecto y, si no existe ninguno, se establece el primero que se encuentre.

![](../../../../assets/drive/1iid--FWuwlYd-vW3S6kQ6zlIftnNgXlP.png)

**Botón Ajustar**<br>

Este proceso permite al usuario ajustar el precio de una o varias líneas del presupuesto, ya sea aplicando un descuento o un recargo mediante un factor de ajuste.

!!! info
    Esto solo se puede ejecutar mientras el documento esté en estado borrador.

![](../../../../assets/drive/1AI28ZDh33qlFigapI41CdMpg6Eeb3bGN.png)

### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad Finalización masiva permite al usuario completar, reactivar o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita una gestión de registros más sencilla y eficiente, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).
## Pedido de venta

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Pedido de venta`

Un pedido de venta es un documento que especifica los productos y/o servicios solicitados por un tercero (cliente) específico, así como el precio y los términos y condiciones.  

La ventana **Pedido de venta** permite al usuario registrar documentos relacionados con ventas con diferentes propósitos, lo cual está regulado por el campo **Documento transacción**. En función del valor seleccionado, las consecuencias al registrar el pedido de venta son diferentes. Estos son los tipos de documentos de pedido de venta disponibles:

**Pedido estándar:** Cuando el documento de transacción es estándar, al registrar el documento no se crean documentos adicionales. El **Albarán (Cliente)** y la **Factura (Cliente)** todavía deben crearse.

![Sales Order.png](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/sales-order.png)

**Pedido de almacén:** Un pedido de almacén se utiliza para la situación en la que el albarán tiene lugar en el momento en que se registra el pedido de venta (por ejemplo, el cliente se lleva la mercancía inmediatamente directamente desde el almacén). Esto también significa que ambos documentos tienen las mismas fechas de pedido/entrega.

![Warehouse order document.png](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/warehouse-order.png)
### Cabecera

La cabecera del **Pedido de venta** permite al usuario crear un pedido de venta y procesarlo cuando esté listo.  
Esta cabecera lista los principales términos y condiciones relacionados con el pedido del cliente que se utilizan en el encabezado de su copia impresa y posteriormente en su proceso de envío y facturación.

![Líneas de cabecera del pedido de venta](../../../../assets/drive/1YzfkXDdYYV0VsKh_Pf9EuVeFzOhGUSjy.png)

Es posible crear nuevos pedidos de venta estándar, de almacén y TPV como conversión a partir de un **Presupuesto de ventas** existente.

Al crear un nuevo pedido de venta en esta ventana:

!!! info
    En la mayoría de los casos, el campo principal y el único necesario para crear un nuevo documento de transacción de ventas es el campo **Terceros**. El resto de campos se completan automáticamente en función del **Terceros** seleccionado, las preferencias del usuario conectado y otros parámetros por defecto del sistema.

Algunos otros campos a tener en cuenta son:

- **Fecha comprometida:** indica la fecha en la que el pedido debe enviarse al cliente. Por defecto, la fecha actual.
- **Almacén:** indica desde qué almacén debe enviarse un pedido. Por defecto, el valor de la sesión del menú superior de navegación **Preferencias de usuario**.  
- **Estado del envío:** indica en % cuánta cantidad se ha entregado.
- **Estado de factura:** indica en % cuánta cantidad se ha facturado.

!!! warning
    A partir de Etendo 25.4, si estos campos muestran 0% pero las cantidades están realmente entregadas/facturadas, debe ejecutar el proceso [Conciliar líneas de pedido de venta, factura y albarán](../general-setup/process-scheduling/process-request.md#match-sales-order-invoice-and-shipment-lines) para actualizar el estado correctamente.

- **Estado de la reserva:** define si el pedido de venta está totalmente reservado (todas las líneas totalmente reservadas) o parcialmente reservado.

!!! info
    Las reservas están deshabilitadas por defecto. Para poder utilizarlas, inserte una nueva Preferencia usando la propiedad Enable Stock Reservations con valor Y. Para más información, consulte la sección [Reserva de existencias](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#stock-reservations).

- **Estado de pago:** indica en % cuánto del total del pedido ha sido pagado. 
    
Los campos siguientes se establecen por defecto según las solapas **Cliente** y **Ubicación** de la ventana **Terceros**.

- **Método de pago**: indica cómo debe pagarse un pedido (y una factura).

- **Condiciones de pago**: define cuándo debe pagarse una factura de ventas generada a partir de este pedido.

- **Facturación**: define cómo se factura a un **Terceros** y la frecuencia de facturación. Se utiliza en procesos automatizados: **Facturar** y **Crear facturas desde pedidos**, y mediante el botón **Crear Líneas Desde** en la **Factura (Cliente)**.

- **Los distintos términos de facturación son:**

- **Después de la entrega:** los productos del pedido de venta se facturan en cuanto se envían; por ejemplo, si hay un envío parcial del pedido, se factura. En este caso, pueden crearse varias facturas de ventas para un único pedido de venta, correspondientes a todos los bienes enviados antes de cada ejecución de facturación.  

- **Después de entregar el pedido:** la factura se generará después de que se hayan enviado todos los productos del pedido de venta, por lo que un pedido = una factura.  

- **Planificación del cliente después de la entrega:** en lugar de enviar facturas cada vez que se entrega cualquier producto del pedido de venta, se crea una factura que combina las distintas entregas de un determinado cliente según la planificación definida (semanal o mensual en un día concreto).  

- **No facturar:** no se genera ninguna factura automáticamente. Normalmente se utiliza cuando existe algún evento externo que desencadena la creación de la factura (por ejemplo, el cliente VIP indica que está bien hacerlo).  

- **Inmediato:** la factura se genera en la siguiente ejecución de la generación automática de facturas, independientemente de si se ha realizado o no algún envío de los productos pedidos.

- **Agente comercial**: comercial responsable del cliente en el pedido. Normalmente se utiliza para reflejar la persona que registró el pedido.

- **Dirección de factura**: dirección que se utiliza al generar una factura.

- **Dirección de entrega**: dirección que se utiliza al generar un envío. Si no se especifica, se utiliza el campo **Dirección del tercero**.

**Hay 3 formas de introducir líneas en un pedido de venta:**

- Copiando productos seleccionados desde un historial de productos pedidos por este cliente mediante el botón **Copiar líneas**.
- Copiando todos los productos de los pedidos elegidos seleccionados en el historial de todos los pedidos para distintos terceros mediante el botón **Copiar desde pedidos**.
- Manualmente, línea a línea, en la solapa **Líneas**.

![Introducir líneas en un pedido de venta](../../../../assets/drive/1Bq1FwcWOeR06AAL0mzBPd6S7ooG4InmF.png)

**Anticipo del pedido de venta**  
Una vez que un pedido de venta está registrado, es posible anticipar el pago de un pedido utilizando el botón de proceso **"Añadir pago"**.

Tal y como se describe para el pago de la **Factura (Cliente)**, la ventana **"Añadir pago"** permite anticipar total o parcialmente el pedido creado más de una vez, e incluso pagar otros pedidos y/o facturas al mismo tiempo.

![Anticipo del pedido de venta](../../../../assets/drive/1BnzwqpcKn8kECP1Ce2jhl8ctZHGTVAB0.png)

También es posible añadir cualquier tipo de gasto relacionado con el pago de ese pedido como un apunte de mayor (G/L) e incluso utilizar el crédito disponible generado previamente para el cliente.

![Apunte de mayor (G/L)](../../../../assets/drive/1N4z10sAm_RRtVotpa28cRSwQ4wpuABO-.png)

Una vez que todo lo anterior se ha cumplido correctamente, el pago puede procesarse y depositarse desde la cuenta financiera.

!!! warning
    Es importante tener en cuenta que la factura de ventas creada a partir del pedido heredará el pago realizado para el pedido.

#### Proceso de cancelación y reemplazo del pedido de venta

La cancelación y reemplazo del pedido de venta es una funcionalidad avanzada oculta por defecto, que puede habilitarse mediante una preferencia denominada **"Enable Cancel and Replace”**.

Una vez habilitada, se muestra un nuevo botón de proceso denominado **"Cancel and Replace"** solo para pedidos de venta registrados.

La funcionalidad **Cancelar y reemplazar** permite cerrar un pedido de venta registrado y reemplazarlo por una "copia" del mismo en estado "Temporal", de modo que pueda modificarse.

**Por ejemplo:**

- **"Condiciones de pago"**, **"Fecha de pedido"** y algunos otros campos pueden cambiarse si es necesario
- y, a nivel de la solapa **"Líneas"**, es posible añadir nuevas líneas de pedido. También es posible modificar o eliminar líneas existentes que no tengan cantidades pedidas ya enviadas/entregadas.

Una vez modificado el nuevo pedido temporal, es posible confirmar los cambios haciendo clic en el botón de proceso **"Confirm Cancel and Replace"**.

El proceso de cancelación y reemplazo del pedido de venta finaliza con tres documentos:

- El **Pedido original** (o pedido reemplazado) en estado "Cerrado".  
  Este pedido es el pedido cancelado y reemplazado por uno nuevo. No se puede ejecutar ninguna acción adicional sobre este pedido.
- Un **Pedido nuevo** (o **Pedido de Reemplazo**) en estado "Registrado".  
  Este pedido es una copia del pedido original, creada para reemplazar al pedido original incluyendo los cambios requeridos.
- Y un **Pedido inverso** en estado "Cerrado".  
  Este pedido cancela el pedido original; por tanto, es una copia del mismo pero con el signo opuesto. No se puede ejecutar ninguna acción adicional sobre este pedido.

El número de documento del pedido de reemplazo es el número de documento del pedido reemplazado y un sufijo que es el número de veces que el pedido ha sido cancelado y reemplazado.

En caso de que el número de veces sea solo una, el número de documento del pedido de reemplazo es \[número de documento del pedido reemplazado/original-1\].

También es posible cancelar y reemplazar un pedido de reemplazo. En ese caso, el nuevo número de documento del pedido de reemplazo es \[número de documento del pedido reemplazado/original-2\].

Del mismo modo, el número de documento del pedido inverso es el número de documento del pedido reemplazado y un sufijo, que es _R_.

Existen algunos indicadores y campos ubicados bajo la sección **"Más información"**, a nivel de pedido de venta, que contienen información sobre las relaciones entre los distintos pedidos implicados en el proceso de cancelación y reemplazo.

El **Pedido Reemplazado (original)** tiene el indicador y el campo que se listan a continuación:

- **IsCanceled**, este es el indicador que señala que el pedido original ha sido cancelado.
- **Pedido de Reemplazo**, este campo almacena el número de documento del pedido que reemplaza al pedido original cancelado.

El **Pedido de Reemplazo (nuevo)** tiene el campo que se lista a continuación:

- **Pedido Reemplazado**, este campo almacena el número de documento del pedido reemplazado, es decir, el pedido original.

El **Pedido inverso** tiene los campos que se listan a continuación:

IsCanceled, este es el indicador que señala que este también es un pedido cancelado.

**Pedido Cancelado**, este campo almacena el número de documento del pedido original cancelado por el pedido inverso.
### Líneas

La solapa **Líneas** permite al usuario añadir los productos que se incluirán en su **Pedido de venta**. Cada producto se añade creando una línea. La solapa **Líneas** lista cada producto pedido y sus características.

![Líneas del pedido de venta](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/salesorderlines.png)

Campos a tener en cuenta:

- **Cant. pedido**, o **Cantidad Operativa** si el producto tiene configurada una unidad de medida alternativa (AUM). Esta es la cantidad necesaria del producto/artículo.
- **Unidad** del producto, o **Unidad Alternativa** del producto dependiendo de la configuración del producto respecto a la unidad de medida.
- **Valor atributos:** este campo se muestra si el producto de la línea tiene atributos (color, talla, número de serie o varios de ellos a la vez, etc.).
- **Descuento:** indica el descuento aplicado como porcentaje del precio de tarifa.
- **Cant.facturada** y **Cant.entregada:** se muestran en la barra de estado cuando se guarda la línea con un producto y se actualizan cuando se emite una factura o un albarán relacionado con esta línea.
- **Regla de almacén:** definición de una regla de almacén a aplicar cuando el albarán se genera automáticamente. Esta regla sobrescribe cualquier regla definida en el *almacén*. Si no se define ninguna regla de almacén en el pedido de venta, se aplica la regla definida en el *almacén*.
- **Cancelar Modificación de Precio:** con esta casilla es posible cancelar promociones definidas previamente en la ventana [Modificación de precios](../master-data-management/pricing.md#discounts-and-promotions). Solo estas, no los descuentos definidos en la ventana [Descuentos](../master-data-management/business-partner-setup.md#basic-discount). Si esta casilla está marcada, estas promociones para esta línea se cancelan; en caso contrario, se calculan con normalidad.

El botón **Explotar** se muestra al seleccionar una línea con un producto LdM (BOM) no almacenable y el producto aún no ha sido explotado. Al explotar un producto, los componentes de la lista de materiales de los que se compone el producto seleccionado se muestran en el pedido. Una vez explotado, no se puede comprimir. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y después el producto LdM) e insertar de nuevo el producto LdM no almacenable.

El botón **Registrar** completa el pedido de venta cuando se han introducido todos los productos. Si hay productos LdM no almacenables y no han sido explotados, el proceso de registro los explotará.

El botón **Cerrar** cierra un pedido, lo que implica que:

- no pueden realizarse más acciones salvo prepagar ese pedido si aplica, si se cierra un pedido de venta **totalmente entregado**
- la cantidad pedida pasa a ser la cantidad entregada y no pueden realizarse más acciones salvo prepagar ese pedido, si se cierra un pedido de venta **parcialmente entregado**
- la cantidad pedida pasa a 0 y no pueden realizarse más acciones, si se cierra un pedido de venta **no entregado**

#### **Reserva de existencias**

Las líneas del pedido de venta pueden reservarse cuando el pedido de venta se registra y está pendiente de entrega.

Campos a tener en cuenta:

- **Reserva de existencias**: define si se desea reservar automáticamente la línea del pedido de venta cuando se registra. Los valores disponibles son:
    - *Manual*: no es necesario generar ninguna reserva automáticamente. Por tanto, cuando el pedido se registra, usted crea la reserva manualmente.
    - *Automático*: la reserva se crea y procesa automáticamente, reservando el stock disponible. Esta opción reserva stock de cualquiera de los almacenes disponibles pertenecientes a la organización del pedido de venta creado, no solo del almacén definido en la cabecera del pedido.
    - *Automático - Solo almacén por defecto*: la reserva se limita únicamente al almacén especificado en la cabecera del pedido. Esto permite optimizar la asignación de inventario y asegurar que los productos se asignan según las preferencias de almacén definidas en cada transacción.

        !!!info
            Esta última opción solo está disponible si el módulo [Automated Warehouse Reservation](../../optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation) está instalado, como parte del Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

- **Estado de la reserva**: define si la línea está *Totalmente reservada* o *Parcialmente reservada* o *No reservada*.

**Gestionar reserva: Recoger y ejecutar**

Mediante el botón *Gestionar reserva* es posible abrir una ventana de *Recoger y ejecutar* para crear y modificar la reserva de la **Línea pedido de venta**. La rejilla muestra todo el stock disponible que puede entregarse y los pedidos de compra pendientes de recibir.

En la rejilla, es posible seleccionar y establecer la cantidad deseada sobre cualquier stock disponible. Existen validaciones para evitar establecer cantidades superiores a las disponibles para ese stock específico o superiores a la cantidad pedida. El botón *Hecho* creará y procesará una reserva si no existe ninguna con las opciones seleccionadas; tenga en cuenta que, si la reserva no existe y se pulsa el botón *Hecho* sin seleccionar ningún stock o seleccionando una cantidad inferior a la cantidad pedida, cuando se procese la reserva el sistema reservará la cantidad restante con el stock disponible. Si ya existe una reserva, el stock reservado aparecerá automáticamente seleccionado y el botón *Hecho* actualizará la reserva con los cambios realizados. También es posible marcar un stock como asignado.

!!! warning
    Cuando el producto seleccionado tiene la marca Cantidad variable establecida como verdadera, es posible reservar más cantidad que la cantidad pedida. Pero tenga cuidado: cuando se genera un albarán contra esta línea de pedido y se completa (con la misma cantidad o una superior a la de la línea de pedido), la reserva se cerrará y la cantidad reservada se establecerá con el mismo valor que la cantidad pedida para evitar problemas de inconsistencias posteriores. Por tanto, es posible reservar más cantidad que la pedida cuando un producto está configurado como Cantidad variable, pero la reserva se ajustará a la **Cant. pedido** original cuando se realice un albarán.

#### **Línea de impuesto**

Para cada línea del pedido de venta, Etendo rellena automáticamente en esta solapa la información relacionada con el impuesto de la línea.

La solapa de solo lectura **Línea de impuesto** detalla la información de impuestos para cada línea de un pedido de venta en función de su campo de impuesto, que se rellena automáticamente según la configuración de impuestos.

#### **Stock reservado**

Relación del stock reservado y de los pedidos de compra pre-reservados relacionados con la **Línea pedido de venta**.

Para cada línea de pedido de venta reservada, es posible revisar el stock reservado. Se muestran la cantidad, el hueco y el valor de atributos cuando aplica. Si existe parte del pedido de venta pre-reservada, también se mostrará la línea del pedido de compra. Cuando una pre-reserva se convierte en una reserva, seguirá teniendo la línea del pedido de compra original, pero esta última también tendrá un hueco definido. Todas las pre-reservas tienen el hueco en blanco.

#### **Productos Relacionados**

En esta tabla se añaden las líneas de pedido relacionadas con una línea de pedido de tipo «Servicio».

Esta solapa solo se mostrará para aquellas líneas con un servicio Vinculado a producto. Mostrará las líneas de producto relacionadas de un servicio. La rejilla tiene los mismos campos que utiliza Elegir/Editar lineas para añadir las líneas. Esta solapa no es editable.

Para relacionar líneas de producto con líneas de servicio, existe un botón Seleccionar línea de pedido. Este botón se mostrará cuando se seleccione una línea con un servicio Vinculado a producto.

Al hacer clic en el botón, se muestra un Elegir/Editar lineas con registros del mismo pedido de productos que podrían relacionarse con el servicio. Por defecto, muestra registros del mismo pedido, pero al eliminar la expresión de filtro, muestra registros de pedidos ya registrados que también podrían relacionarse con el servicio.

Para cada línea seleccionada en esta solapa, se crea una nueva relación entre el servicio y la línea de producto seleccionada. Si ya existe una relación, aparecerá como seleccionada en la rejilla. Para eliminar la relación, simplemente deseleccione el registro deseado. Deben cumplirse algunos requisitos para poder crear una relación:

- El servicio necesita tener un precio en la tarifa.
- Si el servicio está marcado como **Basado en Regla de Precio**:
  - Tener una versión de regla de precio válida.
  - Tener rangos de regla de precio correctos, si aplica.
- Si la línea seleccionada pertenece a un pedido de venta ya completado, el servicio debe estar marcado como **Permitir venta diferida**.

Si no se cumplen estas condiciones, la línea seleccionada se deseleccionará, no permitiendo que se seleccione para relacionarla con el servicio.

Campos de Elegir/Editar lineas:

- **Nº de documento**: número de documento del pedido al que pertenece la línea de pedido.
- **Fecha de pedido**: fecha del pedido.
- **Nivel**: número de línea de la línea de pedido seleccionada.
- **Producto**: producto relacionado.
- **Valor atributos**: valor de atributos del producto.
- **Importe**: importe de la línea a relacionar.
- **Importe del descuento**: importe de los descuentos aplicados a la línea. Este importe se utilizará para calcular el importe del servicio, dependiendo del valor del campo «Después de descuentos» en las reglas de precio de servicio (si aplica).
- **Cant. pedido**: cantidad del producto en la **Línea pedido de venta**.
- **Cantidad Relacionada**: cantidad a relacionar con el servicio. Este campo es editable; es posible relacionar una cantidad menor que la cantidad pedida original, nunca mayor. Si se asigna más, aparecerá un error. Cuando se selecciona un registro, se establece automáticamente la **Cant. pedido** en este campo.
- **Cantidad devuelta en otras devoluciones**: no aplica en este flujo de trabajo (solo para la ventana de devoluciones).

Sección de totales:

- **Importe de líneas sumado**: suma de los importes de línea seleccionados.
- **Importe de descuentos sumado**: suma de los importes de descuento de línea seleccionados.
- **Importe de servicio sumado**: precio del servicio basado en las líneas seleccionadas en la rejilla. Este importe se añadirá al importe total de la línea de servicio al crear las relaciones.

#### **Modificar impuesto**

Si el servicio está configurado para modificar el impuesto, se aplican automáticamente nuevos impuestos durante la operación; por tanto, después de vincular el servicio configurado a un producto, se aplicará la nueva configuración de impuestos.

No se recomienda modificar el impuesto manualmente después, ya que el sistema puede crear inconsistencias. Sin embargo, es posible eliminar el producto de servicio y entonces el impuesto vuelve a su valor original.

#### **Servicios Relacionados**

En esta tabla se muestran las líneas de pedido de producto de tipo «Servicio» relacionadas con una línea de pedido.

Esta solapa solo se muestra para aquellas líneas con productos relacionados con servicios. Muestra los servicios relacionados. La rejilla tiene los mismos campos que utiliza Elegir/Editar lineas para añadir las líneas. Esta solapa no es editable.

#### **Descuentos**

Esta sección lista información sobre descuentos aplicados automáticamente en función de la configuración del cliente y/o introducidos manualmente para el pedido de venta.

#### **Impuesto**

El usuario puede editar los impuestos aplicados a su pedido. Resume la información relacionada con impuestos para todo el pedido de venta. Contiene tantos registros como tipos impositivos utilizados en el pedido.

#### **Plan de pagos**

Esta sección muestra el importe total que se espera cobrar al registrar el pedido, así como el/los importe/s prepagados o pagados contra la/s factura/s del pedido.

Muestra el importe total de pago esperado para el pedido y su cumplimiento. Esta solapa es de solo lectura y se rellena tras procesar el documento.

#### **Detalles del pago**

Muestra los detalles de los pagos (prepago o pagos regulares) recibidos para el pedido o para la/s factura/s del pedido.

#### **Pedidos de Reemplazo**

Conjunto de pedidos que sustituyen a un pedido cancelado.
### Cómo reactivar un Pedido de venta cerrado

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning "Aviso de dependencia"
    Este módulo depende del módulo [**Finalización masiva**](../../optional-features/bundles/essentials-extensions/bulk-completion.md), ya que las acciones de procesamiento del **Pedido de venta** deben realizarse utilizando procesos modernos que permitan el disparo de Hooks, en lugar del procesamiento heredado. Debido a este requisito, las acciones heredadas de **cerrar/reactivar** para pedidos se ocultarán y estas acciones solo estarán disponibles a través del botón **Finalización masiva**.

Etendo permite al usuario reactivar pedidos de venta cerrados seleccionando el/los necesario/s y haciendo clic en el botón **Deshacer cierre**.

![](../../../../assets/drive/14S-_sqqQcDlJqhtFt_L9GVSZ6U-jH4Yo.png)

Una vez finalizado el proceso, el estado del pedido de venta pasa a *registrado*.

!!! info
    Consulte la documentación técnica sobre el procesamiento avanzado de documentos financieros para ampliar el proceso.
### Eliminación de pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de una forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde esta ventana, es posible eliminar pagos asociados a un **Pedido de venta** seleccionando el documento correspondiente y, a continuación, haciendo clic en el botón **Eliminar pago**. Si existe una factura asociada al pedido, también se eliminará la relación de esta factura con el pago en cuestión (ventana **Factura (Cliente)** > solapa **Plan de pagos**).

Si el pago está incluido en la cuenta financiera, es decir, si está en estado Depositado/Retirado no conciliado, también se eliminará la transacción asociada (ventana Cuenta financiera > solapa Transacción).

Si el pago está conciliado mediante un método automático, entonces, además de la transacción en la cuenta financiera, se eliminará la línea del extracto bancario a la que estaba vinculada (ventana Cuenta financiera > Extractos bancarios importados) y la línea correspondiente de la conciliación bancaria (Cuenta financiera > Conciliaciones).

!!! info
    Si el pago está **Contabilizado**, también se elimina el asiento contable.

![](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/PRpic1.png)
### Intercompany

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones que son diferentes pero pertenecen al mismo cliente, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visite [la guía de usuario del módulo Intercompany](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany.md).

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).
### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de **Finalización masiva** permite al usuario completar, **Reactivar** o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).
### Gestión avanzada de cuentas bancarias

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del bundle Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Este módulo añade un nuevo campo a la cabecera de la ventana Pedido de venta: **Cuenta bancaria**. Este campo se rellena automáticamente con la cuenta bancaria relacionada con la dirección o el tercero del pedido.

![bank-account-4.png](../../../../assets/legacy/bank-account-4.png)

!!! info
    Para más información, visite la [Guía de usuario de Advanced Bank Account Management](../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).
## Albarán (Cliente)

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Albarán (Cliente)`

En esta sección, puede crear y gestionar albaranes de mercancía para sus clientes. Un **Albarán (Cliente)** es un documento que registra los detalles de los artículos enviados a un cliente.

Esta ventana permite al usuario consultar información sobre todos los **Albaranes (Cliente)** registrados en el sistema y crear manualmente nuevos documentos de envío. Es útil si se requiere la ejecución de algún escenario que no esté soportado por el proceso de generación automática de albaranes (por ejemplo, el envío parcial del pedido o la agrupación de varios pedidos y/o facturas en un único albarán). Para la creación automática, utilice **Generar albaranes (manualmente)**.

Tal y como se describe en el artículo de Costing Server, el coste de un "Albarán (Cliente)" se calcula como cualquier otra transacción de salida, en función del Algoritmo de Coste utilizado.

El coste calculado de un "Albarán (Cliente)" se utiliza al contabilizarlo en el libro mayor.

### **Cabecera**

El usuario puede crear y procesar un albarán.

![Creación de albaranes](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/goodsshipment.png)

La Cabecera lista los principales términos y condiciones relacionados con la entrega al cliente que aplican a todos los productos (Líneas) incluidos en el documento.

En la mayoría de los casos, el campo principal y único necesario para crear un nuevo **Albarán (Cliente)** es el campo **Terceros**. El resto de campos se rellenan automáticamente en función del **Terceros** seleccionado, las preferencias del Usuario conectado y otros parámetros por defecto del sistema.

Otros campos a tener en cuenta:

- **Almacén:** el almacén desde el cual se envía la mercancía. Se informa por defecto con el valor de la sesión desde la navegación superior.
- **Fecha del movimiento:** la fecha en la que la mercancía sale físicamente del almacén. Se informa por defecto con la fecha actual.
- **Dirección de entrega:** dirección que se utilizará al generar un albarán. Si no se especifica, se utilizará el campo de dirección del tercero. Se informa por defecto según las solapas Cliente y Ubicación de la ventana **Terceros**.
- **Fecha contable:** fecha que se utilizará en el asiento de contabilización del **Albarán (Cliente)** en el libro mayor.
- **Pedido de venta:** referencia al pedido que se está enviando. Si el **Albarán (Cliente)** incluye productos de varios **Pedidos de venta**, los campos se dejan vacíos (aun así, se mantiene la trazabilidad a nivel de Líneas).
- **Estado de factura:** indica en % qué cantidad ha sido facturada.  
  Si creamos dos o más líneas en el albarán relacionadas con una línea de factura de ventas, solo una de esas líneas de albarán mostrará **Estado de factura** 100% y el resto mostrará **Estado de factura** 0%.

    !!! warning
        A partir de Etendo 25.4, si este campo muestra 0% pero las cantidades están realmente facturadas, ejecute el proceso [Match Sales Order Invoice and Shipment Lines](../general-setup/process-scheduling/process-request.md#match-sales-order-invoice-and-shipment-lines) para actualizar el estado correctamente.

Hay 2 formas de introducir líneas en el pedido de venta:

1.  Seleccionando productos de pedidos o facturas pendientes de envío y especificando el **Hueco** (campo **Almacén**) desde el cual debe enviarse mediante el botón **Crear Líneas Desde**. Esta opción puede utilizarse varias veces para agrupar varios pedidos y/o facturas en un único albarán. Este es el enfoque más habitual.
2.  Manualmente, línea a línea. Se utiliza si el documento subyacente (**Pedido de venta** o **Factura**) no existe en el sistema antes de que se realice el envío.

![Líneas de albarán](../../../../assets/drive/1gksOh0asH-Vye9WoBJa2q04TUyDh-aUC.png)

### **Líneas**

El usuario puede añadir o ver los productos incluidos en su albarán. Cada producto se muestra en su propia línea. Las líneas listan cada producto a entregar y sus características.

Campos a tener en cuenta:

- **Valor atributos:** este campo se muestra si el producto a enviar en la línea tiene atributos (color, talla, número de serie o varios de ellos a la vez, etc.).
- **Hueco:** desde donde se toma el producto para el envío. Se rellena automáticamente en función del campo Producto, que incluye el hueco como parte de su selector.
- **Línea pedido de venta:** referencia a la línea del pedido de venta que se está enviando.

En la **Barra de estado** de cada línea, puede encontrar información sobre la **Cant.facturada**, el número de productos facturados de la línea.

El botón **Explotar** se muestra al seleccionar una línea con un producto LdM no almacenable y el producto aún no ha sido explotado. Al explotar un producto, los componentes de la lista de materiales de los que consta el producto seleccionado se muestran en el albarán. Una vez explotado, no puede comprimirse. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y después el producto LdM) e insertar de nuevo el producto LdM no almacenable.

El botón **Completar** finaliza el envío de los productos al cliente y la información de stock se actualiza en consecuencia (los niveles de producto disminuyen).

#### **Contabilidad**

Información contable relacionada con el envío de material.

Un "Albarán (Cliente)" puede contabilizarse si la tabla "MaterialMgmtShipmentInOut" está configurada como Activa para contabilidad en la solapa Tablas Activas del **Esquema contable** de la organización.

La contabilización de **Albarán (Cliente)** crea los siguientes asientos contables.

Fecha del asiento: **Fecha contable**.

|                                   |                           |                           |                             |
| --------------------------------- | ------------------------- | ------------------------- | --------------------------- |
| Cuenta                           | Debe                      | Haber                     | Comentario                  |
| Product COGS (Cost of Goods Sold) | Shipment Line Cost Amount |                           | One per Goods Shipment Line |
| Inmovilizado del producto         |                           | Shipment Line Cost Amount | One per Goods Shipment Line |

La contabilización de un _Albarán (Cliente)_ requiere que el usuario calcule el coste del/de los producto/s contenidos en el mismo.

En el caso de un albarán, se trata del coste medio o del coste estándar calculado en función del Algoritmo de Coste utilizado.

Además:

- la organización "Entidad legal" necesita tener configurada una Regla de Coste validada
- y el Proceso en segundo plano de Coste debe estar planificado para el Cliente; de este modo, puede buscar y permitir que el proceso Costing Server calcule el coste de las transacciones.

Una vez calculado el coste, el **Albarán (Cliente)** puede contabilizarse en el libro mayor.

#### **Factura automática desde Albarán (Cliente)**

Al completar un albarán, el popup de confirmación muestra una casilla llamada _Facturar si es posible_. Si se marca, la UI permite al usuario introducir una Tarifa válida, la **Fecha de la factura** y si desea completar la nueva factura de ventas o dejarla como borrador.

![Factura automática desde albarán](../../../../assets/drive/10fOmotum_TzbMXcsEfiX7w89dAmgWGpk.png)

Las líneas no vinculadas a un pedido de venta siempre se facturarán automáticamente. Para las líneas vinculadas a un pedido de venta, se tendrán en cuenta sus condiciones de facturación correspondientes, generando las líneas de factura solo para las líneas de pedido válidas. En ambos casos, solo se facturará la cantidad aún no facturada.

Además, la ventana muestra un nuevo botón **Generar factura desde albarán** que permite al usuario facturar el albarán en cualquier momento, siempre que el albarán aún no esté completamente facturado. En este proceso también se proporcionan los campos **Fecha de la factura**, Tarifa y Procesar factura, siguiendo la misma lógica explicada anteriormente.

### Cómo reactivar Albaranes (Cliente)

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, consulte [Warehouse Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Desde la ventana **Albarán (Cliente)**, es posible reactivar un movimiento generado previamente seleccionando el documento correspondiente y haciendo clic en el botón **Reactivar**.

Una vez que el albarán se reactiva correctamente, el estado del documento cambia a Borrador, tal y como puede observarse en la barra de estado.

![](../../../../assets/drive/1Ldt_3_sf1I-i3eJxxcsU-VT36TooiagO.png)

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, consulte [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado de contabilidad del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, consulte [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, consulte [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de finalización masiva permite al usuario completar, reactivar o anular múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, consulte [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).
## Devolución de cliente

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Devolución de cliente`

### **Cabecera**

El usuario puede crear un pedido de venta y procesarlo cuando esté listo.

![Cabecera de devolución de cliente](../../../../assets/drive/1d5KfWff5kX53_F_hC_crAGPoIMUaj9sV.png)

Una vez que el documento de Devolución es aceptado, puede procesarlo haciendo clic en el botón **Registrar**. Siguiendo el estándar, el documento cambia de _Borrador_ a _Registrado._

Solo los documentos *registrados* pueden ser recibidos.

!!! warning
    Tenga en cuenta que el botón **Elegir/Editar lineas** desaparece cuando el documento Devolución de cliente está en estado _Registrado._

![Elegir/Editar lineas](../../../../assets/drive/1jTtMk3mx1PnV_e2KcSI9H10cz1Z5HaRA.png)

**Aspectos a tener en cuenta:**

- **Estado del envío**: indica en % qué cantidad ha sido entregada.
- **Estado de factura**: indica en % qué cantidad ha sido facturada.
- Puede aparecer o no un nuevo botón **Crear crédito** en función del pedido de venta original. Si el pedido ya está facturado, entonces estará presente; si no, no lo estará.  
  A través de este botón, puede facturar el pedido de devolución siguiendo los estándares, es decir, en función de la facturación.
- Con este botón también puede crear una factura y dejarla como crédito para usarla más adelante. La forma de hacerlo es:
  - Existe un nuevo proceso de ejecución llamado _Dejar como crédito_. Puede configurar un nuevo método de pago con este proceso.
  - Si el método de pago utilizado en el pedido de devolución de material tiene este proceso de ejecución, se crea una _Factura (Cliente) inversa_ pero dejándola como crédito para que el crédito pueda liquidarse posteriormente con otra factura.
- El botón **Crear crédito** deja de mostrarse una vez que el documento está completamente facturado.
- Además del botón **Crear crédito**, puede seguir los estándares (facturación) para facturar estos documentos. Se cubren todos los escenarios:
  - Proceso Facturar: si la facturación es _Planificación del cliente después de la entrega_ y usted tiene pedidos de venta y RMAs, el proceso agrupará todo en una única Factura (Cliente) estándar y no en una _Factura (Cliente) inversa_.
  - También puede usar la ventana Factura (Cliente) para elegir líneas y, o bien agrupar líneas de pedidos de venta estándar y líneas de pedidos de devolución, o bien crear una _Factura (Cliente) inversa_ individual para los pedidos de devolución.
  - También puede crear una _Factura (Cliente) de devolución de material_ a través de la ventana Factura (Cliente) y dejarla como crédito para usarla posteriormente. Tenga en cuenta que esta factura debe crearse con importes negativos.

### **Líneas**

El usuario puede añadir productos para incluirlos en su pedido de venta. Cada producto se añade creando una línea.

La solapa Líneas no es editable, ya que las líneas devueltas siempre provienen de líneas de albarán, para evitar:

- Ver valores positivos mientras son negativos en la BD.
- Introducir líneas que no estén vinculadas a la línea de albarán original.
- Editar atributos, productos, etc., teniendo productos o atributos diferentes de la línea de albarán.

Para introducir líneas que provienen de un albarán, debe hacer clic en el botón “**Elegir/Editar lineas**”.

**Aspectos a tener en cuenta:**

  - Los únicos campos editables son:
    - **Devuelto**: cantidad que desea devolver. Al seleccionar la fila, la cantidad no se establece por defecto, ya que el sistema no puede saber cuántos artículos se están devolviendo.
    - **Precio unitario**: precio del pedido de venta original.
    - **Motivos de devolución:** el motivo por el que devuelve el artículo.
    - **Unidad de Devolución**, solo en caso de que esté habilitada la preferencia de unidad de medida alternativa (AUM).  
      En ese caso, se muestra la AUM "principal" del producto para el flujo de ventas si existe; en caso contrario, se muestra la unidad del producto. El usuario siempre puede cambiarla a la unidad del producto.
- Puede definir los Motivos de devolución a nivel de cabecera. En este caso, al elegir una línea, hereda lo seleccionado en la cabecera, pero puede modificarlo si lo desea.
- Solo se pueden elegir documentos de albarán que aún no hayan sido devueltos. En caso de que una línea de albarán haya sido devuelta completamente, no se mostrará.
- Cuando una línea de albarán ha sido devuelta parcialmente, el resto todavía puede devolverse. Lo que ya ha devuelto para esa línea se muestra en el campo Cantidad devuelta en otras devoluciones.

**Validación:**

- No se permite devolver más cantidad que la **Cant.envío/recibo**. En caso de hacerlo, se muestra un mensaje.
- Tenga en cuenta que esta validación tiene en cuenta el campo **Cantidad devuelta en otras devoluciones**.

Se ha añadido una restricción en Elegir/Editar lineas para evitar añadir líneas de servicio no “Devolvibles” a documentos de Devolución de cliente.

Para introducir líneas que no provienen de ningún documento presente en el sistema, debe hacer clic en el botón “Insertar línea huérfana”.

!!! tip
    Dado que este flujo no es habitual, el botón está oculto por defecto. Para mostrarlo, es necesario configurar una preferencia llamada **RM Allow Orphan Line**. Para ello, vaya a la ventana de preferencias y selecciónela de la lista. El valor debe ser _Y_. A continuación, cierre sesión e inicie sesión de nuevo.

**Aspectos a tener en cuenta:**

- **Producto**: es obligatorio.
- **Devuelto**: la cantidad devuelta.
- **Precio unitario**: puede dejarse en blanco. En ese caso, el sistema calcula el precio en base a la tarifa definida en la cabecera del documento.
- **Impuesto**: puede dejarse en blanco. En ese caso, el sistema calculará el impuesto.
- **Motivos de devolución**: el motivo por el que se devolvió el producto.

Este flujo (insertar línea huérfana) no admite productos con atributos.

!!! info
    Para editar una línea, debe hacer clic de nuevo en el botón **Elegir/Editar lineas**; la línea aparece seleccionada y entonces puede modificar cualquiera de los campos editables.

!!! info
    Para eliminar una línea, debe desmarcar la línea y luego hacer clic en Hecho.

#### **Línea de impuesto**

Impuestos relacionados con la línea del pedido.

#### **Productos Relacionados**

En esta tabla se añaden las Líneas de pedido relacionadas con una Línea de pedido de tipo 'Servicio'.

Se ha añadido la posibilidad de seleccionar el servicio relacionado con el cual se desea devolver las líneas de producto originales. Para ello, se ha añadido el nuevo botón “Seleccionar línea de pedido” en la solapa Línea de Devolución de cliente. Este botón se muestra cuando se selecciona una línea con un Servicio ‘Vinculado a producto’.

La solapa es similar a la implementada en la ventana Línea pedido de venta. La única diferencia es que las relaciones se crean con valores negativos (importe, cantidad), pero la ventana se ha adaptado para ver esos valores en positivo (en la base de datos, son negativos).

La rejilla implementada en este Elegir/Editar es la misma que se utiliza en la ventana Línea pedido de venta, con algunas diferencias:

- **Cantidad Relacionada**: cantidad a relacionar con el Servicio. Este campo es editable; es posible relacionar menos cantidad que la cantidad pedida original, nunca más. Aparece un error si se asigna más cantidad. Este campo tiene en cuenta el campo Cantidad devuelta en otras devoluciones, por lo que nunca permite devolver más de lo pedido teniendo en cuenta la cantidad devuelta en otros documentos de devolución. Cuando se selecciona un registro, establece automáticamente 0 en este campo.
- **Cantidad devuelta en otras devoluciones**: muestra la cantidad devuelta de la línea en otros documentos de devolución diferentes.
- **Ventas diferidas**: no aplican en esta ventana porque se están realizando devoluciones, no ventas.

#### **Descuentos**

Muestra el descuento aplicado a la factura original del producto devuelto.

#### **Impuesto**

El usuario puede editar los impuestos aplicados al pedido.

### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de Finalización masiva permite al usuario completar, reactivar o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita una gestión de registros más sencilla y eficiente, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).
## Recibo devolución de material

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Recibo devolución de material`

En esta ventana, el usuario recibe el material que ha sido devuelto por el cliente.

### **Cabecera**

El usuario puede crear y procesar un recibo devolución de material.

![Cabecera de recibo devolución de material](../../../../assets/drive/1RFybl7rWjhc3_RmUza0dIbmR7kcpyuJo.png)

Una vez que el documento está listo, puede procesarlo haciendo clic en el botón **Completar**. Siguiendo el estándar, el documento cambia de _Borrador_ a _Completada._

El campo **Estado de factura**: indica en % qué cantidad ha sido facturada.

!!! warning
    Tenga en cuenta que el botón **Elegir/Editar lineas** desaparece cuando el documento está en estado _Completada._

### **Líneas**

El usuario puede añadir o ver productos que están incluidos en el recibo. Cada producto se muestra en su propia línea.

La solapa Líneas no es editable, ya que las líneas siempre provienen de las líneas de **Devolución de cliente**, para evitar:

- Ver valores positivos mientras que en la BD son negativos
- Introducir líneas que no estén vinculadas a líneas de devolución
- Editar atributos, productos, etc., teniendo productos o atributos diferentes de la línea de devolución

Para introducir nuevas líneas, el usuario debe hacer clic en el botón “**Elegir/Editar lineas**”.

![Recibo devolución de material - Líneas](../../../../assets/drive/11Lihjkh1OeoX08nlz39SCLW3QhC_CCHz.png)

**Aspectos a tener en cuenta:**

- Los únicos campos editables son:
  - **Recibo**: cantidad que está recibiendo en el almacén. Este valor se establece por defecto con la cantidad pendiente cuando se selecciona la fila.
  - **Hueco**: este valor se establece por defecto con el hueco de devolución configurado en el almacén.
  - **Estado del producto**: el usuario puede definirlo a nivel de cabecera. En este caso, al seleccionar una línea, hereda lo seleccionado en la cabecera, pero las condiciones pueden modificarse.
  - **Unidad de Devolución**, solo en caso de que esté habilitada una preferencia de unidad de medida alternativa (AUM).  
    En ese caso, se muestra la AUM "principal" del producto para el flujo de ventas si existe; en caso contrario, se muestra la unidad del producto. El usuario siempre puede cambiarla a la unidad del producto.

**Validación**

- El usuario no puede recibir una cantidad mayor que la cantidad **Pendiente**. En caso de hacerlo, se muestra un mensaje.

!!! info
    Para editar una línea, es necesario volver a hacer clic en el botón **Elegir/Editar lineas** y la línea aparece seleccionada. Entonces, el usuario puede modificar cualquiera de los campos editables.

!!! info
    Para eliminar una línea, el usuario debe desmarcar la línea y luego hacer clic en Hecho.

**Contabilidad**

La contabilización de **Recibo devolución de material** crea los siguientes asientos contables.

Fecha del registro contable: **Fecha contable**.

|                                                                             |                                  |                                  |                                      |
| --------------------------------------------------------------------------- | -------------------------------- | -------------------------------- | ------------------------------------ |
| Cuenta                                                                       | Debe                             | Haber                            | Observaciones                        |
| Devolución de COGS del producto (Coste de bienes devueltos) o, si no está definido, COGS del producto |                                  | Coste del producto x Cantidad del movimiento | Uno por cada línea de Recibo devolución de material |
| Inmovilizado del producto                                                   | Coste del producto x Cantidad del movimiento |                                  | Uno por cada línea de Recibo devolución de material |

##### **Configuración**

- Active la tabla **MaterialMgmtShipmentInOut** en la solapa Tablas activas de la pantalla **Esquema contable**.

#### **Contabilidad**

Información contable relacionada con el recibo devolución de material.

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado de contabilización del/de los registro(s) se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Generar albaranes (manualmente)

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Generar albaranes (manualmente)`

Generar albaranes (manualmente) permite al usuario ver los Pedidos de venta pendientes de ser enviados y generar automáticamente Albaranes (Cliente) basados en ellos.

![Generar albaranes (manualmente)](../../../../assets/drive/1wtJV_ZpJ4eAlSCNqf69SOvq52h6dfAZV.png)

Todos los Pedidos de venta de tipo _Pedido estándar_ y en estado *registrado* se consideran que cumplen los criterios para ser enviados.

Se puede generar un Albarán (Cliente) para uno o varios Pedidos de venta o para todos los Pedidos de venta que estén pendientes de ser enviados. Hay filtros disponibles para acotar los resultados mostrados.

Se crea un Albarán (Cliente) por cada Pedido de venta seleccionado, pero para el pedido completo (para todas sus líneas). No es posible realizar un envío parcial a través de esta ventana (utilice Albarán (Cliente) en su lugar).

!!! info
    Tenga en cuenta el campo **Prioridad relativa** en la solapa Hueco de la ventana Almacén y Huecos, que se utiliza para determinar qué hueco usar en las Líneas de albarán generadas. El almacén a utilizar se hereda del Pedido de venta de origen.

### **Formulario**

Campos a tener en cuenta:

- **Desde fecha** y **Hasta fecha:** especifican rangos del campo Fecha de pedido para el filtrado.
- **Importe líneas:** importe neto total del pedido de venta (de todas sus líneas).
- **Entrega pendiente:** el importe neto que aún está pendiente de entregar para el pedido específico (por ejemplo, cuando hubo una entrega parcial previa).

Seleccione el/los pedido(s) que desea enviar y haga clic en el botón Procesar para generar el/los documento(s) de Albarán (Cliente) subyacente(s). El mensaje de ejecución del proceso muestra el/los número(s) de pedido de venta y el/los número(s) de albarán correspondiente(s) que se acaba(n) de crear.
## Factura (Cliente)

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)`

La Factura (Cliente) es un documento detallado de los bienes o servicios proporcionados a un tercero. Indica la cantidad y el precio de cada producto entregado.

La ventana Factura (Cliente) permite al usuario emitir y gestionar las facturas de clientes. También permite al usuario consultar información sobre el historial de todas las facturas de venta registradas en el sistema y crear manualmente nuevos documentos de factura. Resulta útil si se requiere la ejecución de algún escenario específico que no esté gestionado por procesos automáticos de generación de facturas como Facturar o Crear facturas desde pedidos.

Los ingresos por ventas pueden reconocerse tan pronto como la factura de venta se contabiliza; no obstante, si se configura un plan de ingresos diferidos, es posible diferir el reconocimiento de ingresos según sea necesario.
### **Cabecera**

Las facturas de cliente se pueden registrar, contabilizar y gestionar en la sección de cabecera de la ventana de **Factura (Cliente)**.

La **Cabecera** lista los principales términos y condiciones relacionados con la factura de cliente que se utilizarán en el encabezado de su copia impresa y posteriormente en su proceso de cobro.

![Cabecera de factura de cliente](../../../../assets/drive/1-51np9T_CKeVAuAlTaRQn8UdUKz2JArH.png)

En la mayoría de los casos, el campo principal y el único necesario para crear un nuevo documento de factura de cliente es el campo **Terceros**. El resto de campos se completan automáticamente en función del Tercero seleccionado, las preferencias del Usuario conectado y otros parámetros por defecto del sistema.

Algunos otros campos a tener en cuenta son:

- **Documento transacción** con valor por defecto "AR Invoice" o el tipo de documento de Factura (Cliente), que se puede cambiar manualmente a "AR Credit Memo" o "Factura (Cliente) rectificativa".
  - Los tipos de documento "AR Credit Memo" y "Factura (Cliente) rectificativa" pueden considerarse facturas de cliente de abono; la diferencia entre ellas es:
    - El tipo "AR Credit Memo" debe contener o bien una "Cant.facturada" > 0 o bien "Imp. línea" >0.  
      Lo anterior implica que las facturas configuradas como "credit memo" no deberían estar relacionadas con "Pedidos" o "Albaranes".
    - El tipo "Factura (Cliente) rectificativa" debe contener o bien una "Cant.facturada" <0 o bien "Imp. línea" < 0.  
      Estos son los tipos de factura que pueden estar relacionados con "Pedidos" o "Albaranes" de devolución.
- **Fecha de la factura:** la fecha en la que se emite la factura. Se utiliza para calcular cuándo vence el pago de la factura. Por defecto, la fecha actual.
- **Fecha contable:** fecha que se utilizará en el registro de contabilización de la Factura (Cliente) en el libro mayor. Por defecto, el valor del campo Fecha de la factura.
- **Método de pago:** indica cómo debe pagarse una factura. Por defecto, según la solapa Cliente de la ventana Terceros.
- **Condiciones de pago:** define cuándo debe pagarse una factura de cliente. Por defecto, según la solapa Cliente de la ventana Terceros.
- **Pedido de venta:** referencia a un pedido que se está facturando. Si la Factura (Cliente) incluye productos de varios Pedidos de venta, el campo se deja vacío (aun así, la trazabilidad existe a nivel de Líneas).

Hay 3 formas de introducir líneas en la factura de cliente: dos desde la cabecera de la factura y la última desde la solapa Líneas:

1. Seleccionando productos de pedidos o albaranes pendientes de facturar (que cumplan los criterios de **Facturación** del **Pedido de venta**) mediante los botones **Crear Líneas Desde Pedido** y **Crear Líneas Desde Albarán**. Estas opciones pueden utilizarse varias veces para agrupar varios pedidos y/o albaranes en una única factura. Este es el enfoque más habitual. Solo es posible crear líneas a partir de documentos que compartan la misma Moneda y el mismo Tercero.
2. Copiando **todos** los productos de la factura elegida seleccionada en el **histórico de todas las facturas** para distintos terceros mediante el botón **Copiar líneas**.
3. Manualmente, línea a línea, en la solapa Líneas. Esta opción se utiliza si el documento subyacente (Pedido de venta o Albarán) no existe en el sistema antes de que se realice la facturación.

El botón **Completar** finaliza la creación del documento de factura con la cumplimentación de la solapa **Plan de pagos** y de la sección **Monitor de pagos** en la Cabecera. Si en las líneas hay productos BOM no almacenables y no se han explotado, el botón Completar los explotará automáticamente.

Una vez completada, una factura de cliente puede:

- ser **contabilizada** en el libro mayor mediante el botón Contabilizar
- ser **anulada** mediante el botón **Reactivar**
- ser **pagada** mediante el botón **Añadir pago**.
### Líneas

**Líneas** lista cada producto a entregar y sus características.

Una vez que la cabecera de la factura de ventas se ha cumplimentado correctamente y se ha guardado, cada línea de factura de ventas puede registrarse en esta solapa una a una.

![Líneas de factura de ventas](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/salesinvoicelines.png)

Campos a tener en cuenta:

- **Valor atributos:** el campo se muestra si el producto de la línea tiene atributos (color, talla, número de serie o varios de ellos a la vez, etc.).
- **Línea pedido de venta** y **Línea de albarán:** referencias a la línea del pedido de venta y a la línea del albarán que se está facturando.
- **Línea de factura financiera:** se selecciona cuando la línea de factura no es un producto, sino una cuenta no configurada como producto sino como un apunte de mayor (G/L), o un inmovilizado no configurado como producto. Al seleccionarla, el campo de producto desaparece de la pantalla y aparece un campo de cuenta que quedará relacionado con la línea de la factura de ventas.
- **Cancelar Modificación de Precio:** con esta casilla de verificación, es posible cancelar las promociones definidas previamente en la ventana [Modificación de precios](../master-data-management/pricing.md#discounts-and-promotions). Solo estas, no los descuentos definidos en la ventana [Descuentos](../master-data-management/business-partner-setup.md#basic-discount). Si esta casilla está marcada, estas promociones para esta línea se cancelan; en caso contrario, se calculan normalmente.

Como ya se ha mencionado, los ingresos por ventas pueden periodificarse, por lo que no se reconocen en la fecha contable de ventas, sino dentro de un número determinado de periodos contables.

Cuando se crea una línea de factura de ventas, es posible definir a nivel de línea si la línea va a provocar que el ingreso se periodifique o no. Los campos relevantes son:

- **Ingreso postpuesto**: cuando este indicador está marcado, el grupo de campos del plan de ingresos pasa a ser visible, permitiendo a los usuarios configurar los tres campos siguientes.
  - **Tipo de plan de ingresos**: este campo especifica la frecuencia de la distribución del ingreso, que actualmente es "mensual".
  - **Número de periodo**: este campo especifica la duración de un plan de ingresos.  
    Por ejemplo, si una empresa vende y factura un producto que solo estará disponible para entregarse a sus clientes dentro de 3 meses, querría reconocer el ingreso de una sola vez, pero dentro de 3 meses.  
    En esta situación, el número de periodo a introducir sería 1.
  - **Periodod inicial**: el primer periodo abierto en el que se va a reconocer el ingreso.  
    En nuestro ejemplo, el periodo inicial a introducir sería el correspondiente a 3 periodos contables después de contabilizar la factura de ventas.

Estos campos pueden establecerse por defecto si están configurados para el producto.

Si se configura un plan de ingresos, eso implica una contabilidad específica de la factura de ventas.

El botón **Explotar** se muestra al seleccionar una línea con un producto LdM (BOM) no almacenable y el producto aún no está explotado. Al explotar un producto, los componentes de la lista de materiales de los que consta el producto seleccionado se muestran en la factura. Una vez explotado, no puede comprimirse. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y después el producto LdM) e insertar de nuevo el producto LdM no almacenable.

#### Línea de impuesto

La información de impuestos de línea se completa automáticamente para cada línea de factura de ventas al completar la factura.

La solapa de solo lectura **Línea de impuesto** detalla la información de impuestos para cada línea de una factura de ventas en función de su campo de impuesto, que se rellena automáticamente según la configuración de impuestos.
### Impuesto

Esta sección resume la información relacionada con los impuestos para toda la Factura (Cliente). Contiene tantos registros como tipos impositivos utilizados en la factura.

El campo **Impuestos** refleja el valor del impuesto calculado automáticamente en función del tipo impositivo y de la configuración de la base imponible.

!!! info 

    Es posible añadir una funcionalidad que permita ajustes controlados en los importes de impuestos de la factura para conciliar pequeñas **diferencias de redondeo** con sistemas externos o cuando las facturas se presentan a **entidades gubernamentales**. Es compatible tanto con facturas de **Ventas** como de **Compra**, ofrece **ajustes manuales y automatizados** para correcciones mínimas a nivel de céntimos, y registra todos los cambios para garantizar la **auditabilidad**, asegurando que el total final de la factura coincida con requisitos externos, gubernamentales o regulatorios.
    
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. 
    
    Para más información, visite: [Guía de usuario de Ajustar Impuesto de Factura](../../optional-features/bundles/financial-extensions/adjust-invoice-tax.md)
    
    Esta funcionalidad es compatible a partir de Etendo 23.
### Descuentos

Esta solapa lista información sobre los descuentos aplicados automáticamente en base a la configuración del cliente y/o introducidos manualmente para la **Factura (Cliente)**.

### Plan de pagos

La solapa **Plan de pagos** lista los pagos programados esperados contra la factura.

El plan de pagos de una factura no pagada puede modificarse:

- el pago "**fecha esperada**" puede cambiarse directamente si es necesario en esta solapa
- el pago "**fecha esperada**", el "**método de pago**" y el **"importe pendiente de pago",** entre otros, pueden cambiarse si es necesario utilizando la funcionalidad avanzada **Plan de pagos editable**.

#### Detalles del pago

Esta subsolapa muestra los detalles de los pagos realizados contra la factura.

#### Pago

Los pagos pueden recibirse contra una factura de ventas utilizando el botón **Añadir pago**, que abre la **ventana Añadir pago**.

![Pagos](../../../../assets/drive/1VElsFedveUr6Wfn-e9M7Fvf7PTcl8rL8.png)

Todos los campos de la ventana **Añadir pago** se rellenan automáticamente a partir de la Factura. El campo "Tipo de transacción" también se establece por defecto como "Facturas".

Los campos "Pago esperado", "Pago real" e "Importe" toman el mismo valor, que es el total general de la factura (**Importe total**).

Otros campos importantes a tener en cuenta son:

- **Cobrado de**: es el pagador de la factura. Se establece por defecto con el **Terceros** de la Factura.
- **Depositar en**: es la cuenta financiera en la que se va a depositar el importe.
- **Fecha de cobro**: es la fecha del evento de pago. Se utiliza en el registro de contabilización del Pago en el libro mayor. Se establece por defecto con el campo **Fecha de la factura**.

##### **Añadir pedido/factura**

Si la ventana "Añadir pago" se abre desde una "Factura (Cliente)", todos los pagos programados de la factura se seleccionan por defecto si hay más de uno.

Además, el importe de "Pago esperado" y el importe de "Pago real" se establecen como iguales al "Importe" (de la factura), y el campo "Tipo de transacción" se establece como "Facturas".

El motivo de lo anterior es que Etendo entiende que la factura se va a pagar completamente, pero obviamente podría no ser el caso. Por lo tanto, el campo más habitual a cambiar es el Pago real recibido del cliente:

- En caso de que el importe de "Pago real (entrada)" sea mayor que el total general de la factura seleccionada, se repartirá entre los siguientes documentos pendientes de pago hasta consumir el importe completo.  
  Si no hay documentos pendientes de pago, el sistema ofrece las opciones de:
  - "Dejar el crédito para usarlo más tarde", lo que significa que habrá crédito disponible para el cliente.
  - o "Reembolsar el importe al cliente", lo que significa que se crea un pago de reembolso además del pago de la factura en la ventana de Pago (entrada).  
    Un pago reembolsado tiene un importe negativo, lo que implica la creación de una transacción de retirada en la cuenta financiera en lugar de un depósito.
- En caso de que el importe de "Pago real (entrada)" sea menor que el total general de la factura seleccionada, el sistema ofrece opciones para gestionarlas en la rejilla de pedido/factura.
  - Dar de baja la diferencia (simplemente marcando el campo **Writeoff**), lo que implica que:
    - la factura del cliente se establece como totalmente pagada.
    - la contabilización de la factura en el libro mayor liquida el total del importe a cobrar del cliente.
    - mientras que la contabilización del pago en el libro mayor utiliza la cuenta de baja para contabilizar el importe dado de baja.
  - "Dejar el importe como un pago insuficiente" (si el campo **Writeoff** no está marcado), lo que implica que el importe restante será pagado más adelante por el cliente en un nuevo pago.

##### **Añadir apuntes de libro mayor**

La sección de apuntes de libro mayor permite al usuario introducir cualquier tipo de gasto relacionado con el pago pero no incluido en la factura, haciendo clic en \[Add New\].

Lo primero que debe hacerse es seleccionar el apunte de libro mayor para el gasto y, a continuación, introducir el importe del gasto en el campo "Recibido en", tal y como se muestra en la imagen siguiente:

Una vez hecho,

- la contabilización de la factura en el libro mayor liquida el total del importe a cobrar del cliente,
- mientras que la contabilización del pago en el libro mayor utiliza, además, la cuenta del apunte de libro mayor para contabilizar el importe del gasto pagado.

##### Revisión de los totales y procesamiento del pago

Tal y como ya se ha mencionado, la sección "Totales" permite revisar:

- el importe total a pagar en apuntes de libro mayor,
- el importe total a pagar en Facturas y/o Pedidos,
- el total general,
- y la diferencia entre el "Pago real" y el "Pago esperado" (solo en caso de sobrepago)

Además, la sección "Totales" permite al usuario procesar un pago seleccionando una opción en el campo "Acción respecto al documento".

- _Procesar pago(s) recibido(s):_ el Pago se procesa.
- _Procesar pago(s) recibido(s) y depositar:_ el Pago se procesa y el importe del pago se deposita en la cuenta financiera.

El número de opciones anteriores depende de la configuración del método de pago:

- Si la opción _Depósito automático en cuenta_ ya se hubiera seleccionado dentro del método de pago para el Pago, solo se muestra la opción _Procesar pago(s) recibido(s) y depositar_. Sin embargo,
- si la opción _Depósito automático en cuenta_ no se hubiera seleccionado, se ofrecen ambas acciones, dando al usuario la opción de elegir si desea que el depósito se ejecute también o no.

Por último, cualquiera de estas acciones actualiza la sección de monitor de pagos de la Cabecera de la Factura. El importe pagado también se refleja en la solapa **Plan de pagos** de la **Factura (Cliente)** (y del **Pedido de venta** si existe). Los detalles del pago pueden encontrarse en la solapa **Detalles del pago**.

##### **Pago con crédito**

Siempre que exista crédito disponible para un cliente, se abre automáticamente una nueva ventana al completar una nueva factura de ventas del cliente, para permitir al usuario seleccionar si desea utilizar el crédito disponible para pagar esa nueva factura o no.

- Si se utiliza el crédito disponible:
  - el estado de pago de la factura cambia a Pago completo = Sí,
  - un literal como "Factura pagada usando crédito:Pago Nº (Pago con crédito)" se rellena automáticamente en el campo de descripción de la factura,
  - se crea automáticamente un nuevo pago en la ventana de Pago (entrada). Este pago indica claramente la factura pagada en el campo "Descripción" y el pago con crédito utilizado se muestra en la solapa de origen de crédito utilizado del pago (salida).
- Si no se utiliza el crédito disponible:
  - no ocurre nada, la nueva factura sigue sin estar pagada y el importe de crédito disponible permanece igual.

Además, también es posible utilizar el crédito disponible generado para ese cliente más adelante al "Añadir un pago" para ese cliente.

Si ese es el caso, se muestra una nueva sección en la ventana "Añadir pago", que es la sección "Crédito a utilizar".

La sección "Crédito a utilizar" muestra todos los pagos con crédito creados para un cliente determinado (si hay más de uno), por lo que es posible seleccionar uno o varios, e incluso cambiar el importe de crédito a utilizar para el pago, en el campo "Importe del pago".

![](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/newcredittouse.png)

Una vez procesado el pago, se crea un nuevo pago en la ventana de Pago (entrada). Ese pago indica en la parte superior el importe de "Crédito utilizado".

##### **Pagos en múltiples monedas**

Etendo permite al usuario recibir pagos en una moneda diferente a la moneda de la cuenta financiera.

Para ello, el método de pago asignado a la cuenta financiera utilizada para recibir el pago debe configurarse para permitirlo; esto implica seleccionar la casilla "Recibir pagos en múltiples monedas".

!!! example

    Tomemos como ejemplo una organización como "F&B US Inc".

    Esta organización está ubicada en EE. UU., por lo que es probable que la moneda del libro mayor de la organización, así como la moneda de la cuenta financiera, esté configurada como USD.

    F&B US Inc hace negocios con un cliente ubicado en el extranjero. Este cliente requiere pagar la(s) factura(s) emitida(s) en moneda EUR. Esto significa que:

    - La organización F&B US Inc necesita emitir la factura del cliente en EUR, al igual que el pago recibido del cliente.

    Si el pago del cliente se registra en la ventana "Añadir pago" mostrada desde esta ventana "Factura (Cliente)", Etendo permite al usuario introducir un tipo de cambio; por lo tanto, el importe "Convertido real" a pagar en EUR puede modificarse si es necesario.
### Factura Rectificativa

Esta solapa permite al usuario seleccionar las facturas (si las hubiera) que están siendo rectificadas por la factura que se está creando. Cuando el usuario anula una factura existente, Etendo crea automáticamente la factura rectificativa y la vincula con la factura original que se está rectificando. En caso de crear una factura rectificativa de ventas que anule parcialmente una o varias facturas existentes, el usuario debe seleccionar manualmente en esta solapa la(s) factura(s) que se está(n) rectificando.
### Tipos de cambio

La solapa **Tipos de cambio** permite al usuario introducir un tipo de cambio entre la moneda del libro mayor de la organización y la moneda de la factura del cliente, que se utilizará al contabilizar la factura en el libro mayor.

Etendo permite al usuario gestionar diferentes monedas dentro de una organización o unidad de negocio.

Hoy en día, es muy habitual que las organizaciones ubicadas en un país hagan negocios con terceros ubicados en el extranjero y, además, también puede ocurrir que una organización necesite contabilizar las transacciones en libros mayores configurados en diferentes monedas.

El escenario de negocio descrito anteriormente implica la necesidad de gestionar tipos de cambio entre la(s) moneda(s) del/de los libro(s) mayor(es) de la organización y la moneda de la factura del cliente, para utilizarlos al contabilizar la factura del cliente en el/los libro(s) mayor(es).

Esta solapa permite al usuario introducir:

- o bien un tipo de cambio entre la(s) moneda(s) del/de los libro(s) mayor(es) de la organización y la moneda de la factura del cliente
- o bien el/los importe(s) total(es) de la factura en moneda extranjera; por tanto, Etendo puede calcular los tipos de cambio correspondientes.

Adicionalmente, Etendo dispone de un repositorio "central" de tipos de cambio que se utiliza en caso de que no exista un tipo de cambio definido a nivel de documento.

#### Contabilidad

Información contable relacionada con la **Factura (Cliente)**.

Una **Factura (Cliente)** puede contabilizarse en el libro mayor cuando sea necesario, en una **Fecha contable** determinada, utilizando el botón **Contabilizar**.

La contabilización de la **Factura (Cliente)** crea los siguientes asientos contables:

Fecha de registro de la contabilización: **Fecha contable**.

|                          |                    |                 |                                           |
| -------------------------| ------------------ | --------------- | ----------------------------------------- |
| Cuenta                   | Debe               | Haber           | Observaciones                             |
| Cliente deudor           | Importe total      |                 | Uno por línea del Plan de pagos (TB verificado)   |
| Ingresos por descuento del producto | Importe del descuento    |                 | Uno por Línea de factura (si existe descuento) |
| Ingresos por el producto |                    | Imp. línea      | Uno por Línea de factura                  |
| Impuesto repercutido     |                    | Impuestos       | Uno por línea de impuesto                 |

Del mismo modo, una **Factura (Cliente)** que incluya una línea de factura con un plan de ingresos configurado crea los siguientes asientos contables.

Por ejemplo, un distribuidor de alimentación y bebidas que vende y factura un producto que solo podrá entregar a sus clientes en 3 meses querría diferir el reconocimiento del ingreso hasta la entrega.

Fecha de registro de la contabilización: **Fecha contable**:

|                              |                        |                     |             |
| ---------------------------- | ---------------------- | ------------------- | ----------- |
| Cuenta                       | Debe                   | Haber               | Observaciones |
| Clientes deudores            | Importe total          |                     |             |
| Ingreso de producto a periodificar |                        | Imp. línea          |             |
| Impuesto repercutido         |                        | Impuestos           |             |

Fecha de registro de la contabilización: **Fecha contable** + 3 meses:

|                              |                     |                     |
| ---------------------------- | ------------------- | ------------------- |
| Cuenta                       | Debe                | Haber               |
| Ingreso de producto a periodificar | Imp. línea      |                     |
| Ingresos por el producto     |                     | Imp. línea          |

La contabilización de una **Factura (Cliente)** de devolución de material crea los siguientes asientos contables.

!!! note

     Tenga en cuenta que esta factura debe crearse con importes negativos.

Fecha de registro de la contabilización: **Fecha contable**.

|                                                              |                     |                        |                                             |
| ------------------------------------------------------------ | ------------------- | ---------------------- | ------------------------------------------- |
| Cuenta                                                       | Debe                | Haber                  | Observaciones                               |
| Cliente deudor                                               |                     | Importe total          | Uno por línea del Plan de pagos (TB verificado) |
| Devolución de ingresos por el producto o, si no está definido, Ingresos por el producto | Imp. línea |                        | Uno por Línea de factura                    |
| Impuesto repercutido                                         | Impuestos           |                        | Uno por línea de impuesto.                  |

#### Anulación

Es posible anular totalmente una **Factura (Cliente)** utilizando el botón de cabecera **Reactivar** y, a continuación, la acción **Anular**; esta acción implica:

- Etendo genera automáticamente un nuevo documento revertido en la ventana **Factura (Cliente)** e informa del número de documento revertido creado. Este nuevo documento revertido se crea tal y como se describe a continuación:
  - El **Documento transacción** utilizado por Etendo es **Factura de ventas revertida**.
  - Este documento es exactamente igual que el original que se está revirtiendo, pero la **Cant.facturada** es negativa.
  - Puede cambiar tanto la **Fecha de la factura** como la **Fecha contable** del documento revertido antes de contabilizarlo.
  - La solapa **Factura Rectificativa** lista la factura original que se está revirtiendo, ya que ahora ambas quedan enlazadas.

La contabilización del documento revertido crea los siguientes asientos contables:

|                      |                 |                    |                                          |
| -------------------- | --------------- | ------------------ | ---------------------------------------- |
| Cuenta               | Debe            | Haber              | Observaciones                            |
| Ingresos por el producto      | Imp. línea      |                    | Uno por línea de factura                 |
| Impuesto repercutido          | Impuestos       |                    | Uno por línea de impuesto.               |
| Clientes deudores             |                 | Importe total      | Uno por factura                          |
| Ingresos por descuento        |                 | Importe del descuento | Uno por Línea de factura (si existe descuento) |

También es posible anular parcialmente una factura de cliente mediante:

- la creación manual de cualquiera de los documentos de ventas revertidos disponibles, en la ventana **Factura (Cliente)**:
  - **Abono de clientes (AR Credit Memo)** o
  - **Factura de ventas revertida**
- que deben enlazarse manualmente con la(s) factura(s) que se está(n) revirtiendo en la solapa **Factura Rectificativa**.

La contabilización del **Abono de clientes (AR Credit Memo)** es igual que la contabilización de la **Factura de compra revertida**.

La principal diferencia entre esos dos tipos de documento revertido es:

- en el **Abono de clientes (AR Credit Memo)** la **Cant.facturada** es una cantidad positiva
- y en la **Factura de ventas revertida** la **Cant.facturada** es una cantidad negativa.

Se recomienda encarecidamente al usuario utilizar el tipo de documento **Factura de ventas revertida** al anular parcialmente facturas de cliente.
### Cómo reactivar una Factura (Cliente) anulada

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Etendo permite al usuario reactivar Facturas (Cliente) anuladas seleccionando la(s) necesaria(s) y haciendo clic en el botón **Desanular**.

![](../../../../assets/drive/1ylCS2UH_L4XkR02QV8XLqI1rduhcpfIe.png)

Una vez finalizado el proceso, el estado de la Factura (Cliente) pasa a **Completada**.

!!! warning "Importante"
    
    - En el caso de la versión estándar del módulo, es necesario que el usuario también desanule la correspondiente factura rectificativa.
    - Recuerde que este proceso de reactivación afecta a la contabilidad, ya que, si la información original no se elimina manualmente del documento reactivado, la información contable se duplicará.

!!! info
    Consulte la documentación técnica sobre el procesamiento avanzado de documentos financieros (Advanced Financial Docs Processing) para ampliar el proceso.
### Eliminación de pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de una forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde esta ventana, es posible eliminar pagos asociados a una **Factura (Cliente)** seleccionando el documento correspondiente y, a continuación, haciendo clic en el botón **Eliminar pago**. Si existe un pedido asociado a la factura, también se eliminará la relación de este pedido con el pago en cuestión (ventana **Pedido de venta** > solapa **Plan de pagos**).

Si el pago está incluido en la cuenta financiera, es decir, si está en estado **Depositado/Retirado no conciliado**, también se eliminará la transacción en la misma (ventana **Cuenta financiera** > solapa **Transacción**).

Si el pago está conciliado mediante un método automático, entonces, además de la transacción en la cuenta financiera, se eliminará la línea del extracto bancario a la que estaba vinculada (ventana **Cuenta financiera** > **Extractos bancarios importados**) y la línea correspondiente de la conciliación bancaria ( **Cuenta financiera** > **Conciliaciones**).

!!! info
    Si el pago está **Contabilizado**, también se elimina el asiento contable.

![](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/PRpic3.png)
### Intercompany

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones que son diferentes pero pertenecen al mismo cliente, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visite [la guía de usuario del módulo Intercompany](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany.md).

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).
### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado de contabilización del/de los registro(s) se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
### Rappels avanzados

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Rappels del bundle Sales Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Sales Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/sales-extensions/release-notes.md).

Al utilizar esta funcionalidad, en la ventana Factura (Cliente), el usuario puede encontrar las facturas de venta correspondientes a los rappels creados.

![sales_invoice.png](../../../../assets/legacy/sales_invoice.png)

Estas facturas de venta tienen un importe negativo que representa el descuento del rappel, pueden incluir un prefijo en su código para distinguirlas del resto y su estado es “borrador”.

!!! info
    Para más información, visite [Rappels avanzados](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#advanced-rappels).
### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de Finalización masiva permite al usuario completar, **Reactivar** o anular múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).
### Gestión avanzada de cuentas bancarias

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Este módulo añade un nuevo campo a la cabecera de la ventana Factura (Cliente): **Cuenta bancaria**. Este campo se completa automáticamente con la cuenta bancaria relacionada con la dirección o el tercero de la factura. Además, se añade el botón Modificar plan de pagos para una mejor gestión de pagos.

![bank-account-2.png](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/bank-account-2.png)

!!! info
    Para más información, visite la [Guía de usuario de Advanced Bank Account Management](../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).
## Crear facturas desde pedidos

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Crear facturas desde pedidos`

Crear facturas desde pedidos permite al usuario ver los **Pedidos de venta** pendientes de facturar y genera automáticamente las correspondientes **Factura (Cliente)** en base a ellos.

Con esta ventana, se pueden generar **Factura (Cliente)** para uno o varios **Pedidos de venta** o para todos los **Pedidos de venta** que estén pendientes de facturar.

!!!info
    Por defecto, este proceso filtra los registros de acuerdo con la Organización definida en las variables de configuración de sesión. Esto significa que solo se muestran esos registros.

![](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/createinvoicesfromorders.png)


Como se ve arriba, es posible navegar directamente al pedido correspondiente desde el número de documento en la columna Número de documento.

Filtros como `Terceros`, Tipo de documento y Organización, entre otros, están disponibles para acotar los resultados mostrados.

En general, este formulario muestra:

- **Pedidos de venta** con una Facturación **Inmediata**, sin necesidad de tener un **Albarán (Cliente)** relacionado.
- **Pedidos de venta** con una Facturación **Después de la entrega**, siempre que exista un **Albarán (Cliente)** relacionado con al menos algunos productos incluidos en el **Pedido de venta** que ya hayan sido entregados.
- **Pedidos de venta** con una Facturación **Después de la entrega del pedido**, siempre que exista(n) **Albarán (Cliente)** relacionado(s) con todos los productos incluidos en el **Pedido de venta**, que ya hayan sido entregados.
- **Pedidos de venta** con una Facturación **Planificación del cliente después de la entrega**, siempre que exista(n) **Albarán (Cliente)** de acuerdo con la planificación definida y acordada con el cliente.

Del mismo modo, este formulario no muestra **Pedidos de venta** con una Facturación **No facturar**, ya que esos pedidos no se supone que deban facturarse por cualquier tipo de motivo.

Para todas las condiciones de **Facturación** excepto **Planificación del cliente después de la entrega**, se crea una **Factura (Cliente)** para todos los **Albarán (Cliente)** enviados al cliente en la misma fecha que estén relacionados con un **Pedido de venta**.

Si existen varios **Albarán (Cliente)** que tienen lugar en fechas diferentes, se generan varias **Factura (Cliente)** por cada fecha de **Albarán (Cliente)**. Si no hay **Albarán (Cliente)**, se crea una **Factura (Cliente)** para un **Pedido de venta** completo.

Si la **Facturación** es **Planificación del cliente después de la entrega**, entonces se crea una factura de ventas agrupando entregas de diferentes pedidos para el mismo cliente.

**Las líneas incluyen impuestos**: si esta casilla está marcada, los importes de los pedidos mostrados incluyen impuestos.

**Fecha de la factura**: la **Fecha de la factura** para las **Factura (Cliente)** generadas (y, por tanto, el campo **Fecha contable** que se utiliza en el registro de contabilización de la factura en el libro mayor) se toma primero del campo **Fecha de la factura**. Si este campo no está informado, se hereda del campo **Fecha del movimiento** del **Albarán (Cliente)** relacionado con el **Pedido de venta**. Si no hay **Albarán (Cliente)**, entonces se utiliza el campo **Fecha de pedido** del **Pedido de venta** original como **Fecha de la factura**.

!!!important
    Este proceso utiliza los valores especificados a nivel de producto para diferir los ingresos por ventas de las líneas correspondientes de la factura de ventas.

### Botones

- **Actualizar**: para actualizar los pedidos mostrados en esta ventana, utilice el botón de proceso **Actualizar**.

- **Hecho**: a continuación, seleccione el/los pedido(s) que desea facturar y haga clic en el botón **Hecho** para generar el/los documento(s) de **Factura (Cliente)** correspondiente(s). El mensaje de ejecución del proceso muestra el/los número(s) de pedido de venta y el/los número(s) de factura correspondiente(s) que se acaba(n) de crear.

![](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/createinvoicesfromorders3.png)
## Facturar

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Facturar`

Facturar ejecuta la generación automática masiva de **Factura (Cliente)** para todos los **Pedido de venta** pendientes de facturar que pertenezcan a la Organización seleccionada o, si la casilla **Include Child Org** está marcada, a la Organización seleccionada y sus organizaciones hijas. Las facturas generadas se crearán contra la Organización seleccionada.

El criterio principal para este proceso es el campo **Facturación** del Pedido de venta. Por ejemplo, si **Facturación** es _Después de la entrega del pedido_, entonces solo se generará una factura si todos los productos de este pedido de venta ya han sido enviados. Si **Facturación** es _Planificación del cliente después de la entrega_, se comprueba una planificación específica del cliente.

Todos los documentos creados se facturarán contra la Organización establecida en el parámetro **Organización de Factura**.

![Facturar](../../../../assets/drive/1wZBTbAZKVzWQjSWmFk-9YPcPlbUvcDMv.png)

Hay filtros disponibles para acotar las entradas del proceso de generación:

**Organización de Factura:** la Organización contra la cual se van a crear las facturas.

**Pedido de venta:** deje en blanco para considerar todos los pedidos de venta o seleccione uno específico para generar una factura. Tenga en cuenta que en este desplegable solo se incluyen pedidos pendientes.

**Date Invoice To:** solo los pedidos de venta con el campo **Fecha de pedido** hasta esta fecha se incluyen en el proceso de generación.

**Terceros:** si no se selecciona ninguno, se consideran todos los terceros con facturación pendiente. Si aquí se selecciona un cliente específico, solo se consideran para la facturación automática los pedidos de venta de ese tercero. Los terceros disponibles para seleccionar deben tener pedidos con la regla de facturación «Después de la entrega» o «Planificación del cliente después de la entrega».

**Include Child Org:** un indicador que señala si se tendrán en cuenta o no las organizaciones hijas del valor del campo Organización al generar facturas. Cuando **Include Child Org** está marcado y la regla de facturación es «Planificación del cliente después de la entrega», las facturas agruparán la organización hija.

!!! info
    Tenga en cuenta que el filtro **Organización de Factura** también se utiliza para establecer la Organización de las facturas que se van a crear. Esto es importante al generar facturas para organizaciones hijas, porque todas ellas se crearán contra la Organización padre.

Para todas las opciones de **Facturación** excepto _Planificación del cliente después de la entrega_, se crea una **Factura (Cliente)** para todos los **Albarán (Cliente)** enviados al cliente en la misma fecha y que estén relacionados con un Pedido de venta que cumpla los criterios del proceso Facturar. Si existen varios Albarán (Cliente) en fechas diferentes, se generan varias Factura (Cliente), una por cada fecha de Albarán (Cliente). Si no existe Albarán (Cliente), se crea una Factura (Cliente) para un Pedido de venta completo que cumpla los criterios del proceso Facturar. Si **Facturación** es _Planificación del cliente después de la entrega_, entonces solo se crea una factura de cliente agrupando entregas de distintos pedidos para el mismo cliente.

Por último, es importante remarcar que el proceso Facturar también utiliza los valores especificados a nivel de producto para diferir los ingresos por ventas de las líneas de factura de cliente correspondientes.

### **Formulario**

Un campo importante a tener en cuenta es **Fecha de la factura**. Si se especifica, esta fecha se transfiere como **Fecha de la factura** a las Factura (Cliente) generadas (y, por tanto, al campo **Fecha contable** que se utiliza en el registro de contabilización de la factura en el libro mayor). Si no se define, el campo **Fecha del movimiento** del Albarán (Cliente) relacionado con el Pedido de venta original se establece como Fecha de la factura. Si no existe Albarán (Cliente), entonces el campo **Fecha de pedido** del Pedido de venta original se utiliza como Fecha de la factura.

El botón **OK** lanza el proceso y todos los pedidos pendientes de facturar que coincidan con los filtros se facturan automáticamente.

Cuando el proceso finaliza, se muestra un mensaje con el número total de facturas creadas y sus números de documento.
## Procesar comisión

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Procesar comisión`

<iframe width="560" height="315" src="https://www.youtube.com/embed/vQGzo7cbCYQ?si=1CLcSz5b4iY_J4hy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


En esta sección, el usuario puede crear comisiones y crear las facturas correspondientes.

Esta ventana no es editable, ya que los registros de **Comisión** se calculan en la ventana [Comisión](./setup/commission.md#commission); sin embargo, esta ventana permite crear una factura para las comisiones calculadas previamente.

Esta ventana debe interpretarse de la siguiente manera:

- La solapa **Cabecera** muestra el documento de comisión, la fecha de inicio y el importe neto total. En caso de que se cree una factura, ambos documentos quedan vinculados entre sí posteriormente.
- La solapa **Cuantía de la comisión** agrupa el resultado de todas las líneas consideradas para calcular este importe. Por tanto, por cada línea definida en la ventana de comisión, el usuario tiene una entrada en esta solapa.
- La solapa **Detalle de la comisión** muestra todas las líneas de pedido/líneas de factura tenidas en cuenta para calcular el importe.

### Cabecera

Desde esta ventana es posible visualizar las comisiones creadas.

![Cabecera de procesar comisión](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/commission-payment-1.png)


- El campo **Comisión** indica cuál es la comisión definida y, por tanto, las condiciones utilizadas para calcular el importe de la comisión.
- **Fecha de inicio** como la fecha utilizada al ejecutar el proceso; por ejemplo, una fecha de inicio del 1 de marzo con una frecuencia mensual implica tomar pedidos/facturas creados y contabilizados en marzo.
- El campo **Imp.total** muestra el importe de la comisión tras aplicar las condiciones configuradas. El importe de la comisión se calcula en base a importes sin impuestos.
- El campo **Factura** muestra la factura creada, si existe.

### Cuantía de la comisión

El usuario puede editar líneas individuales de pedido de venta que hayan generado una comisión seleccionada.

La solapa **Cuantía de la comisión** muestra el importe calculado por cada línea definida en la ventana de comisión.

![Solapa cuantía de la comisión](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/commission-payment-2.png)

Por ejemplo, si la comisión tiene dos líneas:

- Primera línea:
  - Categoría de producto: Alcohólicas
  - Importe multiplicador: 0.20
- Segunda línea:
  - Categoría de producto: Bio
  - Importe a restar: 12000
  - Importe multiplicador: 0.10

Entonces aparecerían dos líneas en esta solapa.

Campos a tener en cuenta:

- **Línea de comisión**: La línea utilizada para calcular el importe.
- **Importe**: El resultado de la comisión.
- **Imp. convertido**: El importe total sin aplicar las condiciones de la línea de comisión en la moneda correspondiente.
- **Cant.real**: La cantidad total. Cuando la **Unidad** es diferente entre productos, esta información no es relevante.

### Detalle de la comisión

Crear y editar el cálculo y la facturación de la comisión de ventas.

La solapa **Detalle de la comisión** muestra todas las líneas de ventas/factura tenidas en cuenta para calcular la línea de comisión correspondiente.

![Solapa detalle de la comisión](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/transactions/commission-payment-3.png)

Campos a tener en cuenta:

- **Referencia**: Número de documento
- **Línea pedido de venta**: Enlace a la línea de pedido tomada para calcular la comisión
- **Línea de factura de ventas**: Enlace a la línea de factura tomada para calcular la comisión
- **Observaciones**: Nombre del producto
- **Imp.real**: Importe neto de la línea en la moneda del documento de Pedido/Factura
- **Moneda**: Moneda de la comisión. Recuerde que la moneda se define en la ventana de comisión
- **Imp. convertido**: Importe en la moneda de la comisión
- **Cant.real**: Cantidad pedida en la línea de pedido/factura
- **Es coste calculado**: El valor por defecto de este campo es 'SÍ'. Solo se tiene en cuenta cuando la comisión se calcula en base al margen. Cuando este indicador no está marcado, el coste de la transacción no se calcula. Eso significa que no ha sido posible calcular su margen. Este indicador debe estar marcado en todos los detalles para poder generar la factura de la comisión.

### Botones

- **Crear factura**: Desde aquí se puede crear una factura de compra en caso de que sea necesario para pagar al agente comercial, utilizando el botón de proceso.


---

Este trabajo es una obra derivada de [Gestión de Ventas](http://wiki.openbravo.com/wiki/Sales_Management){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.