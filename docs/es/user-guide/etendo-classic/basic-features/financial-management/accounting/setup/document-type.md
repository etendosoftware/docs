---
title: Tipo de documento
tags:
    - Documento
    - Tipo
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Tipo de documento

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Tipo de documento`

## Visión general

**Cada tipo de documento en Etendo hace referencia a una transacción empresarial** como pedidos de compra, albaranes o facturas de venta, entre otros. Etendo incluye un conjunto completo de Tipos de documento estándar necesarios para que la aplicación funcione correctamente.

Este conjunto se incluye en dos conjuntos de datos de referencia:

- Tipos de documento estándar para pedidos, facturas, etc. y configuración - Core - English (USA)
- Tipos de documento y algoritmo por defecto para el emparejamiento automático de extractos bancarios - Advanced Payables

!!!info
    Estos conjuntos de datos se pueden importar en la aplicación durante su configuración inicial mediante los procesos [Crear entidad](../../../general-setup/getting-started.md#initial-client-setup) o [Crear organización](../../../general-setup/enterprise-model/initial-organization-setup.md). O, si la aplicación ya está en funcionamiento, estos conjuntos de datos o sus actualizaciones pueden instalarse mediante la ventana [Gestión del módulo de Empresa](../../../general-setup/enterprise-model/enterprise-module-management.md).

La lista completa de tipos de documento estándar es la siguiente:

|     |     |     |
|-----|-----|-----|
| **Nombre del tipo de documento**  | **Tipo doc. base**  | **Transacción empresarial** |
| AP CreditMemo | Nota de abono de proveedor | [Nota de crédito de compra](../../../procurement-management/transactions.md#reactivate) |
| AP Invoice | Factura de proveedor | [Factura (Proveedor)](../../../procurement-management/transactions.md#purchase-invoice) |
| AR CreditMemo | Nota de abono de cliente | [Nota de crédito de venta](../../../sales-management/transactions.md#header-6) |
| AR Invoice | Factura de cliente | [Factura (Cliente)](../../../sales-management/transactions.md#sales-invoice) |
| Return Material Sales Invoice | Factura de devolución de material (cliente) | [Factura de venta de devolución de material](../../../sales-management/transactions.md#a) |
| Reversed Sales Invoice | Factura de cliente | [Factura de venta revertida](../../../sales-management/transactions.md#header-6) |
| MM Receipt | Recepción de material | [Albarán (Proveedor)](../../../procurement-management/transactions.md#goods-receipts) |
| RTV Shipment | Recepción de material | [Devolución a albarán de proveedor](../../../procurement-management/transactions.md#return-to-vendor-shipment) |
| MM Shipment | Entrega de material | [Albarán (Cliente)](../../../sales-management/transactions.md#goods-shipment) |
| RFC Receipt | Entrega de material | [Recepción de devolución de cliente](../../../sales-management/transactions.md#return-material-receipt) |
| Pedido de compra | Pedido de compra | [Pedido de compra](../../../procurement-management/transactions.md#purchase-order) |
| RTV Order | Pedido de compra | [Devolución a proveedor](../../../procurement-management/transactions.md#return-to-vendor-rtv) |
| Presupuesto | Pedido de venta | [Presupuesto de ventas](../../../sales-management/transactions.md#sales-quotation) |
| RFC Order | Pedido de venta | [Pedido de venta de devolución de cliente](../../../sales-management/transactions.md#return-from-customer) |
| POS Order | Pedido de venta | [Pedido de punto de venta](../../../sales-management/transactions.md#sales-invoice) |
| Warehouse Order | Pedido de venta | [Pedido de almacén](../../../sales-management/transactions.md#sales-invoice) |
| Standard Order | Pedido de venta | [Pedido de venta](../../../sales-management/transactions.md#sales-invoice) |
| AP Payment | Pago a proveedor | [Pago](../../../financial-management/receivables-and-payables/transactions.md#payment-out) |
| AR Receipt | Cobro de cliente | [Cobros](../../../financial-management/receivables-and-payables/transactions.md#payment-in) |
| Financial Account Transaction | Transacción de cuenta financiera | [Transacción de cuenta financiera](../../../financial-management/receivables-and-payables/transactions.md#transaction) |
| Bank Statement File | Archivo de extracto bancario | [Extracto bancario](../../../financial-management/receivables-and-payables/transactions.md#imported-bank-statements) |
| Propuesta de Pago | Propuesta de pago a proveedor | [Propuesta de Pago](../../../financial-management/receivables-and-payables/transactions.md#payment-proposal) |
| Conciliación | Conciliación | [Conciliación](../../../financial-management/receivables-and-payables/transactions.md#reconciliations) |
| Dudoso cobro | Dudoso cobro | [Dudoso cobro](../../../financial-management/receivables-and-payables/transactions.md#doubtful-debt) |
| Ajuste de Costes | Ajuste de Costes | [Ajuste de Costes](../../../warehouse-management/transactions.md#cost-adjustment) |
| Landed Cost | Landed Cost | [Landed Cost](../../../procurement-management/transactions.md#landed-cost-1) |
| Coste de Landed Cost | Coste de Landed Cost | [Coste de Landed Cost](../../../procurement-management/transactions.md#header-7) |
| Ajuste de Valor del Inventario | Ajuste de Valor del Inventario | [Ajuste de Valor del Inventario](../../../warehouse-management/transactions.md#inventory-amount-update) |

!!! note "Importante"
    **Se podrían añadir nuevos tipos de documento a la lista anterior**. Si ese fuera el caso, Etendo proporcionará una versión actualizada de los Datos de referencia que contenga los nuevos tipos de documento en nuevas versiones. Esos Datos de referencia recién creados deberán aplicarse a la Organización correspondiente en la [Gestión del módulo de Empresa](../../../general-setup/enterprise-model/enterprise-module-management.md). También es posible **crear manualmente nuevos tipos de documento**, pero este proceso debe ser realizado por un usuario avanzado, tal y como se explica a continuación.

## Guía avanzada de usuario

### Cabecera

La ventana Tipo de documento permite a los usuarios avanzados configurar cómo se va a comportar cada tipo de documento en términos de contabilidad y secuenciación, entre otros.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/document-type/document-type-1.png)

Campos a tener en cuenta:

- Una **Organización** es una unidad de su entidad o persona jurídica.
- El **Nombre** del documento.
- La **Categoría de LM** es un método opcional, definido por el usuario, para agrupar líneas de asiento.
- La **Etiqueta de impresión**, que es el nombre del documento que se va a imprimir.
- Un **Tipo doc. base** es el tipo base de documento que identifica un documento. Varios tipos de documento pueden compartir un único tipo doc. base.
- El **Subtipo SSO** indica el tipo de pedido de venta al que hace referencia este documento.

    !!! info
        Este campo solo aparece cuando el Tipo doc. base es *Pedido de venta*. 

    La selección realizada aquí determinará qué documentos se generarán cuando se procese un pedido y qué documentos deben generarse manualmente o por lotes. A continuación se describe este proceso.

    - La opción **Pedido estándar** genera únicamente el documento Pedido cuando se procesa el pedido. El albarán, la factura y el recibo deben generarse mediante otros procesos. 
    - La opción **Pedido de almacén** genera el Pedido y el albarán. La factura y el recibo deben generarse mediante otros procesos.
    - La opción **Pedido a crédito** genera el Pedido, el albarán y la factura. El recibo debe generarse mediante otros procesos.

- El indicador **Doc.numéricamente controlado** puede deshabilitarse o habilitarse si es necesario
    
    - numerar manualmente un tipo de documento
    - o numerar automáticamente un tipo de documento de acuerdo con una [secuencia de documento](../../../financial-management/accounting/setup/document-sequence.md).

- La **Secuencia de documento (numeración)** indica la regla de secuenciación que se utilizará para este tipo de documento.

    !!!info
        Este campo solo se muestra cuando se selecciona la casilla **Doc.numéricamente controlado**. 

- La **Tabla** indica la tabla a la que corresponde el tipo de documento. 
- La casilla **Operación de venta** indica si este elemento es una operación de venta. Si no está marcada, por defecto el elemento hace referencia a una transacción de compra.
- La casilla **Devolución** indica si el documento es de tipo reversión. Los documentos con este indicador permiten utilizar cantidades negativas.
- La casilla **Nota de crédito** está habilitada por defecto para los tipos de documento **Nota de crédito** como **Nota de abono de cliente** y **Nota de abono de proveedor**:
    
    - Los tipos de documento **Nota de crédito** también son tipos de documento **revertidos** o **anulados**; sin embargo, se comportan de forma diferente a los tipos de documento **de devolución**, por ejemplo:

        - generan facturas con cantidad(es) facturada(s) **positiva(s)**
        - por lo tanto, la contabilización es siempre la opuesta a la de las facturas, independientemente de la configuración de la casilla [**Permitir negativos**](../../../financial-management/accounting/setup/general-ledger-configuration.md#general-ledger-configuration):

            |     |     |     |     |
            | --- | --- | --- | --- |
            | **Cuenta** | **Débito contabilizado** | **Crédito contabilizado** | **Observaciones** |
            | [Cuentas a cobrar de clientes](../../../master-data-management/master-data.md#customer) |     | Imp. línea | Una por línea de factura |
            | [Débito de impuestos](../../../financial-management/accounting/setup/tax-rate.md#accounting) | Impuestos |     | Una por línea de impuesto |
            | [Ingresos por el producto](../../../master-data-management/product-setup.md#accounting) | Importe total |     | Una por factura |

- **Doc. anulacion**, si existe, es el documento que se utilizará para anular un tipo de documento determinado. 

    Por ejemplo, un tipo de documento **Factura de venta revertida** puede configurarse como el documento anulado de una **Factura de cliente**; por lo tanto, ese será el que se utilizará al anular una **Factura de cliente** (o factura de venta).
    
    - Un tipo de documento **Factura de venta revertida** también es un tipo de documento **Factura de cliente**, pero puede tener una secuenciación diferente simplemente vinculándolo a una secuencia de documento distinta.
    - además, se configura como un tipo de documento **Devolución**, lo que significa que:
        
        - genera una factura de venta **Negativo** con una(s) cantidad(es) facturada(s) negativa(s)
        - por lo tanto, la contabilización será la opuesta a la de la factura de venta, tal y como se describe a continuación, en caso de que la casilla [**Permitir negativos**](../../../financial-management/accounting/setup/general-ledger-configuration.md#general-ledger-configuration) esté habilitada y en caso de que no lo esté:

        |     |     |     |     |
        | --- | --- | --- | --- |
        | **Cuenta** | **Débito contabilizado** | **Crédito contabilizado** | **Observaciones** |
        | [Cuentas a cobrar de clientes](../../../master-data-management/master-data.md#customer) | (-) Imp. línea |     | Una por línea de factura |
        | [Débito de impuestos](../../../financial-management/accounting/setup/tax-rate.md#accounting) |     | (-) Impuestos | Una por línea de impuesto |
        | [Ingresos por el producto](../../../master-data-management/product-setup.md#accounting) |     | (-) Importe total | Una por factura |

        |     |     |     |     |
        | --- | --- | --- | --- |
        | **Cuenta** | **Débito contabilizado** | **Crédito contabilizado** | **Observaciones** |
        | [Cuentas a cobrar de clientes](../../../master-data-management/master-data.md#customer) |     | Imp. línea | Una por línea de factura |
        | [Débito de impuestos](../../../financial-management/accounting/setup/tax-rate.md#accounting) | Impuestos |     | Una por línea de impuesto |
        | [Ingresos por el producto](../../../master-data-management/product-setup.md#accounting) | Importe total |     | Una por factura |

- La casilla **Activo** puede utilizarse para activar o desactivar este tipo de documento.
- La casilla **Valor por defecto** indica si este registro se va a utilizar como valor por defecto.

    !!!info
        Los siguientes campos **solo se muestran cuando el tipo doc. base seleccionado es Pedido de venta**.

- El campo **Tipo doc.factura** indica el tipo de documento que se utilizará cuando se genere una factura a partir de este documento de ventas. Permite definir el documento (p. ej., Factura de venta de devolución de material) que se utilizará al crear un Pedido de venta a partir de un Tipo de documento de devolución de material, como Devolución de cliente.
- El campo **Tipo de documento para pedido** permite al usuario definir, para el **Tipo de documento** Presupuesto, el documento (p. ej., Pedido estándar) que se utilizará al crear un pedido de venta a partir de un presupuesto de ventas.
- El campo **Tipo doc.albarán** indica el tipo de documento que se utilizará cuando se genere un albarán a partir de este documento de ventas. 
- El campo **Tipo de Documento para Factura Simplificada** indica el tipo de documento que se utilizará cuando se genere una factura simplificada a partir de este documento de ventas.
- **Tipo de Documento de Factura Agregada** indica el tipo de documento que se utilizará cuando se genere una factura agregada a partir de este documento de ventas.

### Plantillas para Informes

La solapa **Plantillas para Informes** permite al usuario configurar un aspecto diferente para los **documentos imprimibles** relacionados con cada tipo de documento mediante la configuración de plantillas Jasper `.jrxml`.

!!!info
    Por defecto, estas plantillas se incluyen en los conjuntos de datos mencionados en la [visión general](#visión-general).

Es posible imprimir tipos de documento como [Albarán (Cliente)](../../../sales-management/transactions.md#goods-shipment) o [Factura (Cliente)](../../../sales-management/transactions.md#sales-invoice) utilizando el botón de acción **Imprimir**, que se puede encontrar en la barra de herramientas de la ventana correspondiente.

En Etendo, cada documento apto para ser impreso está vinculado a una plantilla de informe *estándar*.

Si es necesario, **las plantillas de informe se pueden personalizar** e incluso se pueden crear nuevas y, por lo tanto, vincularlas a un tipo de documento determinado.

!!! warning
    Aunque esta opción está disponible en esta solapa funcional, esta configuración debe ser realizada por un desarrollador.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/document-type/document-type-2.png)

#### Definiciones del correo electrónico

La solapa Definiciones del correo electrónico permite la creación de tantas plantillas de correo electrónico como sea necesario, dependiendo del idioma que se vaya a utilizar para enviar los documentos por correo electrónico. Los documentos pueden enviarse por correo electrónico utilizando el botón de acción **Correo electrónico**, que se puede encontrar en la barra de herramientas correspondiente.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/document-type/document-type-3.png)

Tal y como se muestra en la imagen anterior, es posible definir:

- Una **Plantilla de asunto** para que se rellene con datos reales cada vez que se envía por correo electrónico un documento determinado.

    Por ejemplo: `New Invoice (@our_ref@)` se convertirá en *Nueva factura (SI/2589)*, donde *SI/2589* es el número de la factura enviada por correo electrónico.

- Una **Plantilla de cuerpo** para que se rellene con datos reales cada vez que se envía por correo electrónico un documento determinado.
    
    Por ejemplo: `Dear @cus_nam@, Find attached the invoice @our_ref@ corresponding to the products you received from F&B International Group.` se convertirá en *Estimado/a Healthly Food Supermarkets Co., adjunta encontrará la factura SI/2589 correspondiente a los productos que recibió de F&B International Group.*

Esta es la lista de etiquetas posibles:

- `@cus_ref@`: La referencia del documento del cliente.
- `@our_ref@`: La referencia del documento.
- `@cus_nam@`: El nombre del cliente.
- `@sal_nam@`: El nombre del representante de ventas.
- `@bp_nam@`: El nombre del tercero.
- `@doc_date@`: La fecha del documento.
- `@doc_desc@`: La descripción del documento.
- `@doc_nextduedate@`: La siguiente fecha de vencimiento (si el documento tiene asociado algún plan de pagos).
- `@doc_lastduedate@`: La última fecha de vencimiento (si el documento tiene asociado algún plan de pagos).

### Traducción

En esta solapa, los tipos de documento pueden traducirse a cualquier idioma requerido. Para ello, cree un nuevo registro y rellene los campos correspondientes, tal y como se muestra a continuación.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/document-type/document-type-4.png)

---
Este trabajo es una obra derivada de [Document Type](https://wiki.openbravo.com/wiki/Document_Type){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.