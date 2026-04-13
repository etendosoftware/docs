---
title:  Gestión de Compras - Primeros pasos
tags: 
 - primeros pasos
 - gestión de compras
 - procure to pay
 - devoluciones a proveedor
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Gestión de Compras - Primeros pasos

## Visión general

<iframe width="720" height="480"  src="https://www.youtube.com/embed/d33J6fTMEqM?si=NlHOoCq82bCJG3Rg" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Gestión de Compras se ocupa de todas las actividades relacionadas con la compra de bienes y servicios a proveedores externos y de los informes correspondientes.

Esta área de aplicación de Etendo cubre las partes de Necesidad a Albarán (Proveedor) y Facturación del [flujo de negocio Procure To Pay](../../../../user-guide/etendo-classic/basic-features/procurement-management/getting-started.md#procure-to-pay-business-flow) y el [flujo de negocio de Devoluciones a proveedor](../../../../user-guide/etendo-classic/basic-features/procurement-management/getting-started.md#supplier-returns-business-flow).

Para la gestión de pagos de Procure To Pay, consulte el área de aplicación Gestión Financiera / Cuentas a cobrar y a pagar.

## Flujo de negocio Procure to Pay

El flujo de trabajo *Procure to Pay* gestiona el ciclo de vida de un proceso de compras.

Debido a su complejidad y a los diferentes roles implicados, es conveniente dividir Procure to Pay en dos subprocesos principales:
    
1. El proceso *Necesidad a Albarán (Proveedor)* comienza con la creación y gestión de necesidades de material y los correspondientes pedidos de compra, hasta el momento en que el personal de almacén recibe la mercancía.
2. *Factura de proveedor a Pago* continúa el subproceso anterior registrando las facturas del proveedor y lo cierra pagando dichas facturas.

![procure-to-pay](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/getting-started/procure-to-pay-business-flow.png)

### Configuración

La siguiente configuración debe realizarse antes de ejecutar el proceso:

- Productos
- Reglas de cálculo de costes
- Tipos de Landed Cost
- Terceros (vendedores y proveedores).
- Configuración de tarifas

Los productos deben configurarse antes de emitir cualquier necesidad de material.

Cada producto que se vaya a comprar debe tener un precio en la lista de precios de compra para poder seleccionarse en cualquier documento transaccional como un pedido de compra o una factura de proveedor.

Del mismo modo, cada producto que se compra debe definirse en una unidad de medida (UdM) y, si es necesario, en una unidad de medida alternativa (UdMA).

!!!info
    Consulte [Configuración de productos](../../../../user-guide/etendo-classic/basic-features/master-data-management/product-setup.md), [Producto](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product) y [Tarifas](../../../../user-guide/etendo-classic/basic-features/master-data-management/pricing.md) para más información.

El coste de una transacción de entrada como un "Albarán (Proveedor)" puede calcularse utilizando el precio de compra del producto sin impuestos.

Además, el coste de los productos incluidos en un Albarán (Proveedor) puede ajustarse como resultado de la imputación de diferentes tipos de [Landed Cost](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#landed-cost-type) en el albarán.

El proceso "Costing Server" es el proceso "Costing Engine" de Etendo que calcula y ajusta el coste de transacción de un producto.
Este proceso requiere que la entidad legal/organización tenga una [regla de cálculo de costes](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#costing-rule) configurada y aplicada a los productos configurados como "Almacenado".
Los terceros deben configurarse antes de que una necesidad de material pueda convertirse automáticamente en un pedido de compra.

!!!info
    Para más información, visite [Configuración de terceros](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md) y [Terceros](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner).

La configuración anterior forma parte del flujo general de configuración del negocio dentro de la configuración de "Gestión de Datos Maestros".

!!!note 
    No es necesario realizar ninguna configuración adicional para el área de aplicación Gestión de Compras si va a explorarla basándose en el cliente de ejemplo Food & Beverage (F&B) que Etendo incluye por defecto.
    El conjunto de datos de ejemplo ya contiene los roles, terceros, productos, almacenes y precios preconfigurados.

### Ejecución

En Gestión de Compras, el proceso de negocio Procure to Pay se ejecuta del siguiente modo:

Cualquier miembro de la organización autorizado puede emitir directamente una Necesidad de material como resultado de una necesidad de la organización o de una unidad de negocio.

- El solicitante crea un nuevo documento en la ventana [Necesidad de material](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#requisition), introduce una "Fecha de necesidad" y después busca el producto o servicio necesario.
Si el producto no existe, puede introducirse en ese momento en la ventana [Producto](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product).
- El solicitante continúa añadiendo, para cada producto necesario, una nueva línea con la fecha de necesidad, el producto, la cantidad, el precio si se conoce y, si es necesario, su atributo (talla y/o color, etc.).
También puede añadirse un proveedor preferente si se conoce.
- Una vez hecho, la necesidad de material se guarda en estado "Borrador", lo que permite que el usuario la modifique posteriormente si fuera necesario.

Las necesidades de material notifican al personal de compras los productos a pedir, su cantidad y el plazo de entrega. El personal de compras se encarga entonces de gestionar las necesidades de material ya creadas o incluso de crear nuevas, si fuera necesario.

- El personal de compras gestiona las necesidades en la ventana [Administrar necesidades](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#manage-requisitions).
- El personal de compras puede cambiar cualquier dato de las necesidades creadas en estado borrador y, además, puede buscar el proveedor que se utilizará en el campo Terceros. Si el tercero no existe, puede introducirse en ese momento en la ventana [Terceros](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#business-partner).
- El personal de compras también puede introducir el precio neto unitario de compra y los descuentos, si los hubiera, una vez se conozcan.
- Una vez que la necesidad está lista, se completa. El estado del documento de la necesidad cambia a Completado y entonces puede convertirse en un pedido de compra.

El personal de compras:

- puede crear de forma masiva Pedido/s de compra para las necesidades completadas en la ventana [Necesidad a Pedido](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#requisition-to-order), buscando y añadiendo líneas de necesidad que aún no estén vinculadas a un pedido.
Los pedidos de compra creados de este modo se muestran en la ventana Pedido de compra en estado Reservado.
- y también puede crear directamente pedidos de compra en la ventana [Pedido de compra](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order). Las líneas de compra se rellenan como en el caso de la necesidad. Una vez que el pedido de compra está listo, se procesa haciendo clic en el botón Reservar.
- Para revisar compras pasadas y presentes del proveedor, el personal de compras utiliza el [Análisis dimensional pedidos compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#purchase-dimensional-report).

El personal de almacén:

- Recibe la mercancía, así como los albaranes adjuntos, de 2 formas:
    - Con la ventana [Albarán (Proveedor)](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#goods-receipts), el personal de almacén busca los pedidos pendientes de entrega uno a uno y obtiene la cantidad de las líneas de pedido correspondientes, ubicándola en un almacén y una ubicación.
    Esta ventana también permite crear un albarán de forma manual.
    - Con la ventana [Albarán (Proveedor) pendiente](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#pending-goods-receipts). El personal de almacén puede seleccionar masivamente las líneas de pedido de compra que se están entregando y ubicar la cantidad recibida en un almacén y una ubicación.
- Imputa Landed Cost, si lo hubiera, a los productos incluidos en un albarán mediante:
    - la selección de un tipo de Landed Cost e introduciendo un importe de Landed Cost "estimado" que se distribuirá entre las líneas del albarán
    - o seleccionando un tipo de Landed Cost e introduciendo un importe de Landed Cost ya facturado, que también se distribuirá entre las líneas del albarán.
- Completa los albaranes.
    - Los albaranes completados actualizan la información de stock (aumentan los niveles de producto) y pueden ser [contabilizados](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#goods-receipts) en el libro mayor, por lo que aumenta la contabilidad de activos del producto.
    - Un Albarán (Proveedor) solo puede contabilizarse si se ha calculado el coste de los productos recibidos. Para ello, debe ejecutarse el [proceso en segundo plano de cálculo de costes](../../../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request.md#costing).
- La ventana [Facturas cuadradas](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#matched-invoices) ayuda a gestionar y contabilizar las discrepancias, si las hubiera, entre la contabilidad del albarán y la contabilidad de la factura correspondiente posteriormente, debido a diferencias de precio de compra.
- El [Análisis dimensional albaranes compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#goods-receipts-dimensional-report) se utiliza para revisar albaranes anteriores del tercero.

El personal de finanzas:

- Registra facturas de proveedor de diferentes maneras:
    - Con la ventana [Albarán (Proveedor)](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#goods-receipts), el personal de finanzas puede generar una factura a partir de un albarán en estado Completado.
    - Con la ventana [Factura (Proveedor)](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-invoice), el personal de finanzas puede introducir facturas de proveedor:
        - de forma manual
        - o recuperando líneas de pedidos de compra o de albaranes pendientes de facturar
        - o copiando líneas de factura de facturas de proveedor existentes.
- Registra facturas de Landed Cost y concilia esos Landed Cost "facturados" con los Landed Cost:
    - registrados directamente en un/unos [albarán/es](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#landed-cost).
    - o registrados mediante un [documento de Landed Cost](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#landed-cost_1).
- [Procesa](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#process-matching) y [contabiliza](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#post-matching) la conciliación de Landed Cost.
- Una vez que una Factura (Proveedor) se procesa, se crea un plan de pagos de la factura basado en las condiciones de pago acordadas con el proveedor y la factura de proveedor puede contabilizarse para crear los asientos contables de la factura. Posteriormente, el plan de pagos puede modificarse.

Adicionalmente:

- La vista [Pedidos de compra cuadrados](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#matched-purchase-orders) ayuda al personal de finanzas a revisar las líneas de pedido o de albarán que aún no han sido facturadas por un proveedor.
- El personal de finanzas puede revisar información histórica de facturación de proveedores en el [Análisis dimensional facturas compras](../../../../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#purchase-invoice-dimensional-report).

Los gastos de compra pueden reconocerse de diferentes maneras:

- En la mayoría de los casos, las empresas reconocerían el gasto tan pronto como se realiza la compra. Por ejemplo, una empresa que compra productos consumibles que no se capitalizan.
En Etendo, en esta situación, el gasto se genera como parte de la contabilidad de la factura de proveedor correspondiente a la transacción.
- En algunas circunstancias, sin embargo, se requiere diferir el reconocimiento del gasto. Por ejemplo, una empresa que compra un seguro empresarial por la duración de un año querría
distribuir ese gasto durante 12 meses.
En Etendo, en esta situación, el gasto puede diferirse dentro de un número determinado de periodos introduciendo un plan de diferimiento de gastos en las [líneas de factura de proveedor](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#lines_4).

!!!info
    Para una descripción completa de esta funcionalidad, visite la sección [Cómo gestionar ingresos y gastos diferidos](../../../../user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses.md).

Finalmente, el personal de finanzas se encarga de realizar y gestionar los pagos a proveedores:

- Los pagos a proveedores pueden realizarse en la ventana Factura (Proveedor) utilizando el botón Añadir pago. También es posible realizar un prepago contra un Pedido de compra.
La documentación detallada de la gestión de pagos está disponible en el área de aplicación Gestión Financiera / Cuentas a cobrar y a pagar y en la sección [Cómo gestionar facturas prepagadas en cuentas a pagar](../../../../user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables.md).

## Flujo de negocio de Devoluciones a proveedor

Este flujo de trabajo gestiona la devolución de bienes comprados al proveedor. Debido a las consecuencias de la devolución, es conveniente dividir las devoluciones a proveedor en dos subprocesos principales:

1. *Devolución de proveedor a Cargo*: este proceso gestiona la devolución de bienes al vendedor y la solicitud de un cargo.

2. *Devolución de proveedor a Sustitución*: este proceso gestiona la devolución de bienes al vendedor y la solicitud de una sustitución del producto.

![supplier-returns](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/getting-started/supplier-return-debit.png)

### Configuración
La ventana [Motivos de devolución](../../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md#return-reasons) es la única que requiere configuración antes de ejecutar este proceso.

### Ejecución

En Gestión de Compras, el *flujo de negocio de Devolución a proveedor* se ejecuta del siguiente modo.

El personal de compras:

- Crea un nuevo documento en la ventana [Devolución a proveedor](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#return-to-vendor-rtv) y busca el nombre del vendedor en el campo Terceros.
- Y continúa añadiendo líneas haciendo clic en el botón [Elegir/Editar lineas](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#lines_5)
    - Es posible seleccionar líneas de albarán de proveedor y editar la cantidad que desea devolver y el precio
- Una vez que el documento de devolución de material es aceptado por el vendedor, puede procesarlo haciendo clic en el botón Reservar. El estado del documento cambia de Borrador a Reservado.
- Solo los documentos Reservados pueden enviarse al vendedor

El personal de almacén:

- Crea un nuevo documento en la ventana [Devolución a albarán de proveedor](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#return-to-vendor-shipment) y busca el nombre del vendedor en el campo Terceros.
- Y continúa añadiendo líneas haciendo clic en el botón [Elegir/Editar lineas](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#lines_6)
    - Se seleccionan líneas de Devolución a proveedor
    - Es posible editar la cantidad a enviar
- Una vez que el documento está listo, procéselo haciendo clic en el botón Completar. El estado del documento cambia de Borrador a Completado
- El envío completado actualiza la información de stock (disminuyen los niveles de producto)

Personal de finanzas: para facturar estos documentos, vaya a la ventana [Factura (Proveedor)](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-invoice). Se cubren todos los escenarios:

- Si el vendedor envía una factura solo para ese documento específico, debe seleccionar un tipo de documento de factura de compra revertida y después seleccionar las líneas mediante el botón *Crear líneas de*
- Si el vendedor envía una factura con el pedido de compra original más el pedido de devolución de material, debe seleccionar un tipo de documento de Factura (Proveedor) y después seleccionar las líneas mediante el botón *Crear líneas de*
- Si el vendedor no envía una factura para el pedido de devolución de material pero quiere mantenerlo como crédito para que pueda usarlo más adelante, debe:
    - Crear una *factura de compra revertida* para estos materiales devueltos
    - Dejarla como crédito para usarla más adelante mediante la ventana [Pago](../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-out)
    - Una nueva factura de compra basada en el pedido de compra original puede consumir ese crédito

## Relación con otras áreas de aplicación

Gestión de Compras tiene relación con otras áreas de aplicación: 

- [Gestión de Almacén](../warehouse-management/getting-started.md) ya que los Albaranes (Proveedor) cambian la cantidad disponible de los artículos y su valor.
- [Gestión Financiera](../financial-management/getting-started.md) en lo relativo a la gestión de pagos de cuentas a pagar.
- [Gestión de MRP](../material-requirement-planning/getting-started.md) ya que la planificación de compras permite la creación de pedidos de compra basados en necesidades de material.

---

Este trabajo es una obra derivada de [Gestión de Compras](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.