---
tags:
  - Cómo hacer
  - Cuentas a cobrar prepagadas
  - Cobros de clientes
  - Pedido de venta
---

# Cómo gestionar facturas prepagadas en Cuentas a cobrar

## Visión general

Hay empresas que no desean conceder crédito a determinados clientes:

- Podría ser una cuestión de confianza al inicio de una relación comercial.
- O podría ser una cuestión de falta temporal de capacidad financiera.

En estas situaciones, las partes acuerdan unas condiciones de pago específicas que implican el pago total o parcial de un pedido o de una factura; de lo contrario, la mercancía no se entregará al cliente.

Es importante señalar que una factura de venta creada a partir de un pedido de venta prepagado heredará la información de pago del pedido, sea cual sea.

## Artículos recomendados

La gestión de facturas prepagadas requiere una comprensión clara de cómo crear un [Pedido de venta](../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order) y una [Factura (Cliente)](../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice), así como de cómo registrar un [Cobro de cliente](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-in).

También se recomienda entender cómo configurar las [Condiciones de pago](../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md#payment-term) y cómo lanzar el [Informe de pagos y cobros](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/analysis-tools.md#payment-report).

## Prepago de pedido: pasos de ejecución

En Etendo, la empresa de este ejemplo deberá acordar unas condiciones de pago específicas con su cliente, crear un pedido de venta para los bienes solicitados y, a continuación, registrar un pago parcial del pedido antes de emitir posteriormente la correspondiente factura de venta.

### Configuración de condiciones de pago

Como ya se ha mencionado, la empresa de este ejemplo necesita crear unas condiciones de pago específicas para reflejar lo acordado con su cliente.

Se pueden crear unas condiciones de pago de tipo "Prepago" como se muestra en la imagen siguiente:

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/paymenttermsm.png)

Lo anterior significa que el cliente deberá prepagar el 50% del importe total del pedido y el resto 30 días después de la fecha de la factura.

Tenga en cuenta que las condiciones de pago de prepago tienen una cabecera y una línea:

- En la línea, el prepago del 50% se configura estableciendo **Días de plazo** en 0 días.
- En la cabecera, la segunda parte de este pago se configura estableciendo **Días de plazo** en 30 días para el importe restante.

### Creación del Pedido de venta

Como ya se ha mencionado, el primer paso es crear un Pedido de venta de acuerdo con las necesidades del cliente.

En este escenario, las partes han acordado unas condiciones de pago específicas que pueden informarse en el campo correspondiente de la cabecera del [Pedido de venta](../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order).

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/salesordersm.png)

El campo principal que debe tenerse en cuenta al gestionar prepagos es el campo **Invoice Terms**, que debe seleccionarse como “Immediate”; de lo contrario, no sería posible prepagar ese pedido. En Etendo, eso significa que el pedido no se mostrará como un pedido apto para ser pagado en la ventana [Cobros](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-in), donde se registran los cobros de clientes.

Una vez informados todos los datos requeridos, el Pedido de venta debe contabilizarse (Booked), ya que cada vez que se completa un pedido se crea un Plan de pagos para ese pedido.

En otras palabras, no es posible registrar pagos contra pedidos que no estén completados y, por tanto, que no tengan ya un plan de pagos vinculado.

### Creación del cobro y contabilización

Los cobros recibidos del cliente se registran en la ventana [Cobros](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-in). Etendo permite registrar cobros de clientes recibidos contra pedidos de venta y/o facturas.

Los principales campos a informar en la sección de cabecera de la ventana de cobros son:

- Tercero, el cliente que realmente está realizando el pago.
- Importe, el importe exacto pagado (en nuestro caso, el 50% de USD 1,726.40).
- Ingresar en, la cuenta bancaria financiera donde se ha recibido el dinero.
- y el **Método de pago**, que en el ejemplo es "Transferencia bancaria"

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/paymentinsm.png)

A continuación, es posible registrar los detalles del cobro del cliente utilizando el botón de proceso “**Añadir Detalles de Pago**”.

Se muestra una nueva ventana denominada "**Añadir Detalles de Pago**", donde es necesario especificar el "**Tipo de Transacción**" al que está relacionado el cobro; este puede ser pedidos y/o facturas.

La empresa de este ejemplo debe elegir "**Parte**" y, a continuación, el pedido que se va a pagar parcialmente.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/adddetailssm.png)

Una vez completado todo, pulse el botón Hecho.

El cobro se recibe y se deposita en el banco al mismo tiempo; eso significa que se crea una transacción de depósito en la ventana [Cuenta financiera](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#transaction), en la pestaña "**Transacción**".

El cobro recién creado puede contabilizarse en la ventana Cobros pulsando el botón de proceso Contabilizar si:

- el **Método de pago** utilizado tiene la configuración adecuada en la pestaña [Método de pago](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-method) de la cuenta financiera utilizada para realizar el cobro.
- la empresa de este ejemplo necesita establecer el campo **Cuenta del cobro** como "Cuenta de pagos en tránsito"
- además, debe existir una **Cuenta de pagos en tránsito** en la pestaña [Configuración de Contabilidad](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration) de la cuenta financiera utilizada para realizar el cobro.

La contabilización tendrá este aspecto:

| Cuenta                          | Debe   | Crédito contabilizado |
|----------------------------------|--------|------------------------|
| [Cuenta de pagos en tránsito](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)   | 863.20 |                        |
| [Prepago del cliente](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#customer-accounting)              |        | 863.20                 |

Es posible comprobar una vez más el Plan de pagos del pedido de venta de este ejemplo.

El plan de pagos del pedido de venta incluye el pago registrado en la pestaña Detalles de pago.

### Comprobación del cobro

De vuelta en el [Pedido de venta](../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order), es posible comprobar el Plan de pagos creado recientemente con sus Detalles de pago.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/paymentplansm.png)

En resumen:

- la pestaña Plan de pagos nos informa sobre:

    - el importe esperado a pagar
    - el importe recibido, si lo hubiera
    - y el importe pendiente de pago en caso de que ya se haya registrado un pago parcial.

- y la pestaña Detalles de pago registra cada cobro recibido contra el pedido.

### Gestión y contabilización de factura prepagada

Existen varias formas de crear una factura de venta a partir de un pedido; una de ellas es [Crear facturas desde pedidos](../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-invoices-from-orders).

Este proceso permite introducir datos como el tercero y un rango de fechas determinado para acotar los pedidos a facturar.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/createinvoicesfromorderssm.png)

Una vez seleccionado un Pedido de venta, el botón Hecho genera automáticamente la factura correspondiente.

La factura creada heredará el plan de pagos del pedido.

En este ejemplo:

- el plan de pagos de la factura ya reflejará el importe ya pagado contra el pedido, que es USD 863.20
- y, además, también reflejará el importe pendiente de pago, que es USD 630.80

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/salesinvoicesm.png)

La situación anterior también se refleja en contabilidad, ya que la contabilización de la factura de compra tendrá este aspecto:

| Cuenta                | Debe   | Crédito  |
|------------------------|---------|---------|
| [Cuenta a cobrar del cliente](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#customer-accounting)    | 630.80  |         |
| Prepago del cliente    |         | 863.20  |

Existe un informe denominado [Informe de pagos y cobros](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/analysis-tools.md#payment-report) que permite monitorizar cada cobro recibido o pago realizado.

En este ejemplo, este informe muestra de forma intuitiva:

- el estado del cobro recibido contra el pedido y posteriormente heredado en la factura, como "Depositado no conciliado", lo que significa que el cobro se ha depositado en una cuenta bancaria financiera pero aún no se ha conciliado
- y el importe pendiente de pago de la factura como "Pendiente de pago".

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/paymentreportsm.png)

En este ejemplo, el último paso es registrar el cobro del cliente de la factura, 30 días después de la fecha de la factura. Un cobro recibido de un cliente puede registrarse en el sistema de dos formas:

- en la ventana [Cobros](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-in), de la misma manera que se describe aquí, pero esta vez el cobro debe estar relacionado con un "**Tipo de Transacción**" igual a "**Factura**"
- o en la ventana [Factura (Cliente)](../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-invoice), utilizando el botón de proceso "Añadir cobro/pago".

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/addpaymentsm.png)

Una vez procesado este nuevo cobro, la factura de venta pasa a estar totalmente pagada. En otras palabras, la casilla de verificación "**Pagado**" de la factura queda ahora seleccionada.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/paymentcompletesm.png)

Por último, el "**Informe de pagos y cobros**" muestra ahora la factura como totalmente pagada; en términos de Etendo se muestra como "Depositado no conciliado".

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/paymentcompletesm2.png)

## Prepago de factura: pasos de ejecución

En Etendo, la empresa de este ejemplo deberá configurar un método de pago que permita contabilizar el prepago en cuanto se reciba, crear una factura de venta para los bienes solicitados por su cliente y registrar el prepago de la factura en una fecha anterior a la fecha de la factura.

### Configuración del método de pago

El método de pago que se va a utilizar debe configurarse para permitir la contabilización del prepago en cuanto se reciba; por tanto, se puede especificar la "Cuenta de cobros depositados" en el campo **Cuenta del cobro**.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/paymentmethodconfsm.png)

!!! note
        La casilla de verificación "**Depósito automático en cuenta**" también está seleccionada. Eso significa que el cobro recibido se depositará automáticamente en la cuenta financiera.

### Creación de la factura de venta

El primer paso es emitir la factura de venta con fecha 13 de noviembre de 2023, por ejemplo. La factura emitida puede completarse en cuanto esté correctamente informada.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/salesinvoicecreationsm.png)

### Creación del cobro y contabilización

El siguiente paso es registrar el prepago de la factura en una fecha anterior a la fecha de la factura, por ejemplo el 1 de noviembre de 2023.

Lo anterior se realiza utilizando el botón "**Añadir pago**". El campo "**Fecha de cobro**" debe modificarse según sea necesario.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/addpaymentsm2.png)

Una vez procesado, se crea un cobro recibido en la ventana "**Cobros**" y, además, el depósito de ese cobro se registra automáticamente en la cuenta financiera correspondiente.

El cobro recibido puede contabilizarse desde la ventana "**Cobros**".

### Contabilización de la Factura (Cliente)

El último paso es contabilizar la factura de venta en el libro mayor.

La contabilización de la factura tiene este aspecto:

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-receivables/journalentriesreportsm.png)

La contabilización anterior refleja el momento en el que se contabiliza la cuenta a cobrar del cliente; sin embargo, la cuenta a cobrar del cliente ya está cancelada por el prepago.

## Resultado

Esto completa la creación y el procesamiento de:

- un pedido parcialmente prepagado en Etendo. Como resultado, una factura ha sido pagada parcialmente tras registrar un prepago contra el pedido correspondiente.
- una factura prepagada en Etendo. Como resultado, las cuentas a cobrar del cliente se cancelan en el momento de registrar y contabilizar el prepago de la factura.

---

Este trabajo es una obra derivada de [Guías prácticas](https://wiki.openbravo.com/wiki/How_To){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.