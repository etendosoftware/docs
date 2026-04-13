---
title: Gestión de Ventas - Primeros pasos
tags: 
    - primeros pasos
    - gestión de ventas
    - factura
    - presupuesto
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Gestión de Ventas - Primeros pasos

## Visión general

<iframe width="720" height="480"  src="https://www.youtube.com/embed/JxTGQIJ9JqQ" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


La Gestión de Ventas se ocupa de todas las actividades relacionadas con el proceso de ventas al cliente y los informes correspondientes.

Esta área de aplicación de Etendo cubre las partes de Pedido a albarán e Invoicing del flujo de negocio [Order to Cash](../../../../user-guide/etendo-classic/basic-features/sales-management/getting-started.md#order-to-cash-business-flow) y el proceso de negocio [Devoluciones de cliente](../../../../user-guide/etendo-classic/basic-features/sales-management/getting-started.md#customer-returns-business-flow). 

!!! Info
    Para la gestión de pagos de Order to Cash, consulte el área de aplicación [Gestión Financiera](../../../../user-guide/etendo-classic/basic-features/financial-management/getting-started.md).

## Flujo de negocio Order to Cash

El flujo de trabajo *Order to Cash* gestiona el ciclo de vida de un proceso de ventas.

Debido a su complejidad y a los diferentes roles implicados, resulta conveniente dividir Order to Cash en dos subprocesos principales:

1. El proceso *Pedido a albarán* comienza cuando un cliente solicita un presupuesto o pide mercancía, hasta el momento en que el personal de almacén envía la mercancía.

    ![ord-to-ship-bus-pro](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/ord-to-ship-bus-pro.png)

2. *Factura de cliente a cobro* continúa el subproceso anterior facturando las entregas al cliente y lo cierra recibiendo los pagos de los compradores.

![cust-inv-bus-proc](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/cust-inv-bus-proc.png)

### Configuración

La siguiente configuración debe realizarse antes de ejecutar el proceso:

- Productos de venta.
- Configuración de tarifas.
- Terceros (clientes).
- Configuración del tipo de documento de Presupuesto de ventas.

Los productos de venta deben configurarse antes de cualquier venta en la aplicación.  
Cada producto que se venda debe tener un *precio* en la lista de precios de venta para poder seleccionarse en cualquier documento transaccional como un pedido de venta o una factura (cliente).  
Del mismo modo, cada producto que se venda debe definirse en una *unidad de medida* ("UOM") y, si es necesario, en una *unidad de medida alternativa* (AUM).

!!! Info
    Para más información, visite [Configuración de productos](../../../../user-guide/etendo-classic/basic-features/master-data-management/product-setup.md), [Producto](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product) y [Tarifas](../../../../user-guide/etendo-classic/basic-features/master-data-management/pricing.md). 

Los Terceros (clientes) deben configurarse antes de que cualquier venta pueda convertirse automáticamente en un presupuesto de ventas o un pedido de venta. 

!!! Info
    Para más información, visite [Configuración de terceros](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md) y [Terceros](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner).

La configuración anterior es una parte del flujo general de configuración del negocio dentro de la configuración de Gestión de datos maestros.

Por último, el [tipo de documento](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/document-type.md) de Presupuesto requiere que se defina un tipo de documento de pedido de venta (p. ej., Pedido estándar) como Tipo de documento para pedido, para permitir la conversión de un presupuesto de ventas en un pedido de venta.

!!!Note
    No es necesario realizar ninguna configuración adicional para el área de aplicación Gestión de Ventas si se va a utilizar el cliente de ejemplo Food & Beverage (F&B) que Etendo incluye por defecto para explorarlo. El conjunto de datos de ejemplo ya contiene los roles, almacenes, terceros, productos y precios preconfigurados.

### Ejecución

En Gestión de Ventas, el proceso de negocio Order to Cash se ejecuta de la siguiente manera.

Los clientes pueden solicitar directamente un Pedido de venta o pedir un Presupuesto. Si el Tercero solicita un presupuesto, el personal de ventas:

- Crea un nuevo documento en la ventana [Presupuesto de ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md) y busca el nombre del cliente en el campo Terceros. Si el Tercero no existe, se introduce en la aplicación con la ventana [Terceros](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner).
- A continuación, el personal de ventas completa la ventana [Presupuesto de ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md). El documento de transacción se establece por defecto como Presupuesto. Y continúa añadiendo, para cada producto, una línea con el producto, la cantidad y, si es necesario, su atributo (talla y/o color y/o número de serie, etc.).
- Una vez que el presupuesto está listo, se contabiliza. El Estado del documento del presupuesto cambia a En evaluación. El Presupuesto puede imprimirse y enviarse al Tercero por correo electrónico.
- Cuando el Presupuesto es aceptado por el Tercero, puede crearse un pedido de venta basado en este presupuesto. Cuando esto se realiza, el estado del presupuesto cambia a *Cerrado - Pedido* creado y el Pedido de venta puede imprimirse y enviarse al Tercero por correo electrónico como confirmación.

Si el Tercero realiza un pedido directamente, el personal de ventas:

- Lo crea con la misma ventana [Pedido de venta](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order), estableciendo el Documento de transacción en el tipo de pedido deseado (*Pedido estándar, Pedido de almacén*). Las líneas se completan como en el caso del Presupuesto. Una vez que el Pedido de venta está listo, se procesa pulsando el botón Contabilizar.
- Cuando el Pedido de venta se procesa, reserva el material para su envío.
- Para revisar ventas anteriores del Tercero, el personal de ventas utiliza [Análisis dimensional pedidos ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#sales-dimensional-report).

El personal de almacén:

- Busca pedidos pendientes de preparación en la ventana [Generar albaranes (manualmente)](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-shipments-from-orders) o con la ayuda del [Informe de Pedidos a la Espera de Entrega](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#orders-awaiting-delivery-report).
- El personal de almacén puede crear un albarán de 2 formas:

Con la ventana [Generar albaranes (manualmente)](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-shipments-from-orders). Crea un albarán completado para los pedidos de venta seleccionados.

Con la ventana [Albarán (Cliente)](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#goods-shipment), en la que el personal de almacén crea el albarán de forma manual.

- El albarán completado actualiza la información de stock (los niveles de producto disminuyen) y puede contabilizarse para crear los asientos contables del albarán.
- [Análisis dimensional albaranes ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#shipments-dimensional-report) se utiliza para revisar albaranes anteriores del Tercero.

El personal de finanzas puede generar facturas de diferentes maneras:

- Con la ventana [Facturar](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#generate-invoices), en la que genera facturas en bloque para todos los pedidos de venta pendientes de facturar (en función de sus reglas de facturación).
- Con la ventana [Crear facturas desde pedidos](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-invoices-from-orders). Muestra pedidos pendientes de facturar y crea facturas para los pedidos de venta seleccionados.
- Con la ventana [Factura (Cliente)](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice), en la que el personal de finanzas crea la factura de forma manual.
- La Factura (Cliente) procesada crea el Plan de pagos de la factura, el impuesto de la factura y puede contabilizarse para crear los asientos contables de la factura. Posteriormente, el [plan de pagos](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment) puede modificarse.
- [Pedidos no facturados](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#orders-awaiting-invoice-report) ayuda al personal de finanzas a planificar y verificar la facturación de los Terceros.
- El personal de finanzas puede revisar información histórica de facturación de clientes en el [Análisis dimensional facturas ventas](../../../../user-guide/etendo-classic/basic-features/sales-management/analysis-tools.md#sales-invoice-dimensional-report).


Los ingresos y gastos de ventas pueden reconocerse de diferentes maneras:

- En la mayoría de los casos, las empresas querrán reconocer los ingresos en cuanto se complete una factura. Por ejemplo, un distribuidor de food and beverage que vende bebidas querrá reconocer el ingreso en cuanto la mercancía salga del almacén.  
En Etendo, en esta situación, el ingreso se genera como parte de la contabilidad de la factura (cliente) correspondiente a la transacción.
- Sin embargo, en algunas circunstancias es necesario diferir el reconocimiento del ingreso. Por ejemplo, un distribuidor de food and beverage que vende y factura un producto que solo podrá entregar a sus clientes en 3 meses necesita diferir el reconocimiento del ingreso hasta la entrega.

En Etendo, en esta situación, el ingreso puede diferirse hasta un periodo de inicio determinado y durante un número determinado de periodos introduciendo un plan de ingresos diferidos en las [líneas de factura (cliente)](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines-5).

!!!info
    Para una descripción completa de esta funcionalidad, visite el artículo [Cómo gestionar ingresos y gastos diferidos](../../../../user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses.md).


Límite de crédito para terceros

- Cada [Terceros](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner) puede configurarse con un Límite de línea de crédito. Cuando el saldo del cliente (importe pendiente de pago del cliente) es superior al límite de la línea de crédito, se muestra un mensaje informativo correspondiente cuando se selecciona un tercero durante la creación de un pedido de venta, una factura (cliente) o un albarán (cliente). De este modo, Etendo ayuda en el análisis de riesgos al realizar pedidos de clientes o ejecutar otros pasos del flujo de negocio Order to Cash.


Por último, el personal de finanzas se encarga de registrar y gestionar los pagos de los clientes:

- Cuando se recibe un pago contra una factura, puede registrarse en la ventana Factura (Cliente) utilizando el botón Añadir pago. También es posible recibir un anticipo para el Pedido de venta.  
Para más información sobre la documentación de gestión de pagos, visite [Gestión Financiera](../../../../user-guide/etendo-classic/basic-features/financial-management/getting-started.md) y [Cómo gestionar facturas prepagadas en cuentas a cobrar](../../../../user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables.md).


## Flujo de negocio de devoluciones de cliente

El flujo de trabajo de Devoluciones de cliente gestiona los procesos de negocio para devolver artículos desde los clientes, ya sea para abono

![cust-ret-cr-business-process](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/cust-ret-cr-business-process.png)

o para sustitución.

![cus-ret-replace-business-process](../../../../assets/user-guide/etendo-classic/basic-features/sales-management/getting-started/cus-ret-replace-business-process.png)

### Configuración

En este proceso están disponibles las siguientes opciones de configuración:

- [Motivos de devolución](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md#return-reasons)
- [Estado del producto](../../../../user-guide/etendo-classic/basic-features/sales-management/setup/setup.md#condition-of-the-goods)
- Cuentas para [Coste de los bienes vendidos](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting) (COGS) para devoluciones e [Ingresos por devoluciones](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)

### Ejecución

En Gestión de Ventas, el proceso de negocio de Devoluciones de cliente se ejecuta de la siguiente manera.  
Los clientes pueden solicitar una [devolución de material](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md#return-reasons) por cualquier motivo.  
El personal de ventas:

- Crea un nuevo documento en la ventana [Devolución de cliente](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-from-customer) y busca el nombre del cliente en el campo Terceros.
- Y continúa añadiendo líneas haciendo clic en el botón [Elegir/Editar lineas](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines-3).  
Selecciona líneas de albarán (cliente) y edita la cantidad que el cliente desea devolver, el precio y los motivos de devolución.
- Una vez aceptado el documento de Recibo devolución de material, procéselo haciendo clic en el botón Contabilizar. El estado del documento cambia de Borrador a Contabilizado.

El personal de almacén:

- Crea un nuevo documento en la ventana [Recibo devolución de material](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-material-receipt) y busca el nombre del proveedor en el campo Terceros.
- Y continúa añadiendo líneas haciendo clic en el botón [Elegir/Editar lineas](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines-4).  
Selecciona las líneas creadas en la ventana Devolución de cliente.  
Si es necesario, edite la cantidad recibida y su ubicación (ubicación).
- Una vez que el documento está listo, procéselo haciendo clic en el botón Completar. El estado del documento cambia de Borrador a Completado
- El recibo completado actualiza la información de stock (los niveles de producto aumentan).

El personal de finanzas:  
Para facturar estos documentos puede hacerlo desde varias ventanas / procesos:

- Con la ventana [Devolución de cliente](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-from-customer), donde puede aparecer o no un nuevo botón Crear crédito en función del pedido de venta original. Si el pedido ya está facturado, entonces estará presente; si no, no lo estará. Usando este botón es posible facturar el pedido de devolución siguiendo el proceso estándar, es decir, dependiendo de las condiciones de facturación.
- Con el mismo botón [Crear crédito](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#return-from-customer) también es posible crear una factura y dejarla como crédito para usarla más adelante.
- Usando el proceso [Facturar](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#generate-invoices): si las condiciones de facturación son Programación de cliente después de la entrega y existen tanto pedidos de venta como RMAs, el proceso agrupa todos ellos en una Factura (Cliente) estándar (no en un [Facturas de venta de devolución de material](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/document-type.md)).
- Con la ventana [Factura (Cliente)](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice), seleccionando líneas y agrupándolas desde pedidos de venta estándar y pedidos de devolución, o creando [Facturas de venta de devolución de material](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/document-type.md) individuales solo a partir de pedidos de devolución.
- Con la ventana [Factura (Cliente)](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice), creando una Factura de venta de devolución de material y asegurándose de que el importe de la factura sea negativo.


## Relación con otras áreas de aplicación

Gestión de Ventas tiene conexión con otras áreas de aplicación:

- [Gestión de Almacén](../../../../user-guide/etendo-classic/basic-features/warehouse-management/getting-started.md), ya que el albarán modifica la cantidad de stock y su valor.
- [Gestión Financiera](../../../../user-guide/etendo-classic/basic-features/financial-management/getting-started.md), en lo relativo a la gestión de pagos.
- [Gestión de MRP](../../../../user-guide/etendo-classic/basic-features/material-requirement-planning/getting-started.md) (MRP), porque los pedidos de venta pendientes son una de las entradas para el proceso de producción.

---

Este trabajo es una obra derivada de [Gestión de Ventas](http://wiki.openbravo.com/wiki/Sales_Management){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.