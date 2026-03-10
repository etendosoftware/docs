---
tags:
  - Cómo hacer
  - Facturas prepagadas
  - Pedido de compra
  - Pagos a proveedores
---

## Visión general

Hay proveedores que no desean conceder crédito a sus clientes:

- Podría ser una cuestión de confianza al inicio de una relación comercial
- O podría ser una cuestión de una falta temporal de capacidad financiera.

En estas situaciones, la empresa y el proveedor acuerdan unas condiciones de pago específicas que implican un pago contra un **Pedido de compra** o una **Factura (Proveedor)**; de lo contrario, el proveedor no entregará los bienes a la empresa. Las partes pueden acordar un prepago total o un prepago parcial.

!!! note
        Una factura de compra creada a partir del pedido de compra prepagado heredará la información de pago, tanto si se trata de un prepago total como de un prepago parcial.

## Artículos recomendados

La gestión de facturas prepagadas requiere una comprensión clara de cómo crear un [Pedido de compra](../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order) y una [Factura (Proveedor)](../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-invoice), así como de cómo registrar un [Pago a proveedor](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-out).

También se recomienda comprender cómo configurar unas [Condiciones de pago](../../../user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup.md#payment-term) y cómo lanzar el [Informe de pagos y cobros](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/analysis-tools.md#payment-report).

## Prepago de pedido: pasos de ejecución

En Etendo, la empresa de este ejemplo deberá reconocer unas condiciones de pago específicas acordadas con su proveedor, crear un **Pedido de compra** y realizar un pago antes de que se le entreguen los bienes.

### Configuración de condiciones de pago

Tal y como se ha mencionado, la empresa de este ejemplo necesita crear unas condiciones de pago específicas para reflejar lo acordado con su proveedor.

Se pueden crear unas condiciones de pago de tipo "Prepago" como se muestra en la imagen siguiente:
 
![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/paymentterm.png)

Lo anterior significa que la empresa deberá pagar el 25% del importe total del pedido y el resto 30 días después de la fecha de factura del proveedor.

Tenga en cuenta que las condiciones de pago de prepago tienen una cabecera y una línea:

- en la línea, se configura el prepago del 25% y el campo "Días de plazo" se establece en 0 días.
- en la cabecera, se configura la segunda parte de este pago; en este caso, el campo "Días de plazo" es de 30 días para el importe restante.

### Creación del Pedido de compra

Tal y como se ha mencionado, el primer paso es crear un [Pedido de compra](../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order) que contenga los bienes que la empresa necesita.

En este escenario, las partes han acordado unas condiciones de pago específicas que pueden informarse en el campo correspondiente de la cabecera del pedido de compra.

Una vez que todos los datos requeridos se han informado según corresponda, el **Pedido de compra** debe contabilizarse, ya que cada vez que se completa un pedido se crea un plan de pagos para ese pedido.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/purchaseorder2.png)

!!! note
        No es posible registrar pagos contra pedidos que no estén completados y, por tanto, que no tengan ya un plan de pagos vinculado.

### Creación del pago y contabilidad

Los pagos realizados a un proveedor se registran en la ventana de [Pago](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-out). Etendo permite registrar pagos a proveedores creados contra pedidos de compra y/o facturas.

Los principales campos a informar en la sección de cabecera del pago son:

- Tercero, el proveedor al que la empresa está pagando
- Pagar desde, la cuenta bancaria financiera desde la que se retira el dinero.
- y el **Método de pago**, que en el ejemplo es "Transferencia bancaria"

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/paymentout2.png)

A continuación, es posible registrar los detalles del pago al proveedor utilizando el botón de proceso denominado “Añadir detalles”.

Se muestra una nueva ventana en la que es necesario especificar el "Tipo de Transacción" al que está relacionado el pago, que puede ser pedidos y/o facturas.

La empresa de este ejemplo debe elegir "Parte" y, a continuación, el pedido que se va a pagar parcialmente.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/adddetails2.png)

Una vez que todo esté informado, pulse el botón Procesar.

El pago se realiza y se retira del banco al mismo tiempo; esto significa que se crea una transacción de retirada en la ventana de [Cuenta financiera](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#transaction), en la solapa "Transacción".

El pago recién creado puede contabilizarse en la ventana **Pago** pulsando el botón de proceso Contabilizar si:

- el **Método de pago** utilizado tiene la configuración adecuada en la solapa [Método de pago](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-method) de la [Cuenta financiera](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account) utilizada para realizar el pago.
     - la empresa de este ejemplo necesita establecer el campo "Cuenta de pago" como "Cuenta de pagos en tránsito"
- además, debe existir una "Cuenta de pagos en tránsito" en la solapa [Configuración de Contabilidad](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration) de la cuenta financiera utilizada para realizar el pago.

La contabilización tendrá el siguiente aspecto:

| Cuenta                    | Debe | Crédito contabilizado |
|----------------------------|-------|--------|
| [Pagos por adelantado del proveedor](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#vendor-accounting)          | 50    |        |
| [Cuenta de pagos en tránsito](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration) |       | 50     |


Es posible volver a comprobar el plan de pagos de salida del pedido de compra de este ejemplo.

El plan de pagos del pedido de compra incluye el pago registrado en la solapa Detalles de pago de salida.

### Comprobación del pago

De vuelta al [Pedido de compra](../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order), es posible comprobar el plan de pagos creado recientemente con sus detalles de pago.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/paymentdetails.png)

En resumen:

- la solapa Plan de pagos nos informa sobre:
    - el Importe esperado a pagar
    - el importe pagado, si lo hubiera
    - y el importe pendiente de pago en caso de que ya se haya registrado un pago parcial.
- y la solapa Detalles de pago registra cada pago realizado contra el pedido.

### Gestión y contabilidad de facturas prepagadas

La empresa de este ejemplo puede registrar el [Albarán (Proveedor)](../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#goods-receipts) antes de registrar la factura del proveedor utilizando el proceso [Albaranes pendientes de recibir](../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#pending-goods-receipts).

Este proceso permite introducir la cantidad exacta de bienes recibidos del proveedor contra cada línea del pedido de compra.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/pendinggoodsreceipts2.png)

Una vez procesado, Etendo informa del número de albarán recién registrado.

El siguiente paso es introducir la factura del proveedor. Hay varias formas de introducir una factura de proveedor.

La empresa de este ejemplo utiliza, por ejemplo, el proceso "Crear líneas de", que se puede encontrar en la ventana [Factura (Proveedor)](../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#lines-4). Este proceso puede utilizarse una vez que la información de cabecera de la factura de compra se haya introducido correctamente. Recupera información del pedido o del albarán para copiarla en la factura introducida.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/createfrom.png)

La factura creada, una vez completada, heredará el plan de pagos del pedido.

En este ejemplo:

- el plan de pagos de la factura ya reflejará el importe ya pagado contra el pedido, que es 50 USD
- y, además, también reflejará el importe pendiente de pago, que es 60 USD

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/purchaseinvoice.png)

La situación anterior también se refleja en contabilidad, ya que la contabilización de la factura de compra tendrá el siguiente aspecto:

| Cuenta              | Debe | Crédito contabilizado |
|----------------------|-------|--------|
| [Gastos del producto](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#accounting)      | 110   |        |
| [Pasivo del proveedor](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#vendor-accounting)     |       | 60     |
| [Pagos por adelantado del proveedor](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#vendor-accounting)    |       | 50     |


Existe un informe denominado [Informe de pagos y cobros](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/analysis-tools.md#payment-report) que permite monitorizar cada pago recibido o realizado.

En este ejemplo, este informe muestra de forma intuitiva:

- el estado del pago realizado contra el pedido y posteriormente heredado por la factura como "Retirado no conciliado"; esto significa que el pago se ha retirado de una cuenta bancaria financiera, pero aún no está conciliado
- y el importe pendiente de pago de la factura como "Pendiente de pago".

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/paymentreport.png)

En este ejemplo, el último paso es registrar el pago del importe restante de la factura del proveedor 30 días después de la fecha de la factura. Un pago realizado a una factura de proveedor puede registrarse en el sistema de dos maneras:

- en la ventana **Pago**, de la misma forma que se describe aquí, pero esta vez el pago debe estar relacionado con un "Tipo de Transacción" igual a "Factura"
- o en la ventana **Factura (Proveedor)**, utilizando el botón de proceso "Añadir pago".

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/addpayment.png)

Una vez procesado este nuevo pago, la factura de compra pasa a estar totalmente pagada. En otras palabras, la casilla de verificación "Pagado" de la factura queda ahora seleccionada.

Por último, el "Informe de pagos y cobros" muestra ahora la factura como totalmente pagada; en términos de Etendo, se muestra como "Retirado no conciliado".

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/paymentreport2.png)

## Prepago de factura: pasos de ejecución

En Etendo, la empresa de este ejemplo deberá configurar un método de pago que permita contabilizar el prepago en cuanto se realice, crear una factura de compra para los bienes requeridos y registrar el prepago de la factura en una fecha anterior a la fecha de la factura.

### Configuración del método de pago
El método de pago que se va a utilizar debe configurarse para permitir la contabilización del prepago en cuanto se realice; por tanto, se puede especificar la "Cuenta de pago retirada" en el campo 'Cuenta de pago'.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/paymentmethod.png)

!!! note
    La casilla de verificación "Reintegro automático en cuenta" también está seleccionada. Esto significa que el pago se retirará automáticamente de la cuenta financiera.

### Creación de la factura de compra

El primer paso es emitir la factura de compra con fecha 6 de noviembre de 2023, por ejemplo. La factura emitida puede completarse en cuanto se haya informado correctamente.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/purchaseinvoice3.png)

### Creación del pago y contabilidad

El siguiente paso es registrar el prepago de la factura en una fecha anterior a la fecha de la factura, por ejemplo el 1 de noviembre de 2023.

Lo anterior se realiza utilizando el botón "Añadir pago". El campo "Fecha de cobro" debe modificarse según sea necesario.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/addpayment3.png)

Una vez procesado, se crea un pago en la ventana "Pago" y, además, la retirada de ese pago se registra automáticamente en la cuenta financiera correspondiente.

El pago puede contabilizarse desde la ventana "Pago".

La contabilización del pago tiene el siguiente aspecto:

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/journalentriesreport.png)

La contabilización anterior refleja el momento en el que el pasivo del proveedor se cancela mediante el prepago, que también se cancela mediante el reconocimiento del pago retirado.

### Contabilización de la Factura (Proveedor)

El último paso es contabilizar la factura de compra en el libro mayor.
La contabilización de la factura tiene el siguiente aspecto:

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-prepaid-invoices-in-payables/journalentriesreport2.png)

La contabilización anterior refleja el momento en el que se contabiliza el pasivo del proveedor; sin embargo, el pasivo del proveedor ya está cancelado por el prepago.

### Resultado

Esto completa la creación y el procesamiento de:

- un pedido parcialmente prepagado en Etendo. Como resultado, una factura ha sido pagada parcialmente tras registrar un prepago contra el pedido correspondiente.
- una factura prepagada en Etendo. Como resultado, el pasivo del proveedor se cancela en el momento de registrar y contabilizar el prepago de la factura.

---

Este trabajo es una obra derivada de [Guías prácticas](https://wiki.openbravo.com/wiki/How_To){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.