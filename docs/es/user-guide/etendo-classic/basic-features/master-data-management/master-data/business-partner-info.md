---
title: Información de terceros
tags:
  - Gestión de datos maestros
  - Etendo Classic
  - Tercero
  - Pedidos
  - Facturas
---

## Información de Terceros { #business-partner-info }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Información de terceros`

### Descripción general { #overview }

La ventana Información de terceros es una vista consolidada de solo lectura de toda la actividad de transacciones registrada para un [tercero](./business-partner.md) determinado. Centraliza cuatro tipos de información en un único lugar: pedidos, albaranes y recepciones, facturas y activos. Los equipos de ventas, compras y contabilidad utilizan esta ventana para obtener un resumen rápido de la actividad de un tercero sin necesidad de navegar a cada ventana de transacción individual. No es posible introducir datos aquí; la ventana está destinada estrictamente a la consulta y revisión.

### Selección de tercero { #business-partner-selection }

Seleccione un tercero de la lista para cargar sus datos de transacciones en las solapas inferiores.

![Ventana Información de terceros mostrando los campos de cabecera para la selección del tercero](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-1.png)

Campos a tener en cuenta:

- **Activo**: indica si el tercero está actualmente activo.
- **Identificador**: identificador corto utilizado para buscar el tercero.
- **Nombre comercial**: el nombre comercial del tercero.
- **Grupos de Terceros**: clasifica al tercero. Por ejemplo: Cliente - Nivel 1, Proveedor o Empleado.
- **Agente Comercial**: el representante de ventas asignado al tercero, si existe.
- **Método de Pago**: el método de pago predeterminado para el tercero. Por ejemplo: Transferencia bancaria.
- **Condiciones de Pago**: las condiciones de pago acordadas. Por ejemplo: 30 días.

Una vez seleccionado un registro, las solapas **Pedidos tercero**, **Albaranes tercero**, **Facturas tercero** y **Activos tercero** en la parte inferior de la pantalla se rellenan con los datos de transacciones correspondientes.

### Pedidos del Tercero { #partner-orders }

Esta solapa muestra todos los pedidos asociados al tercero seleccionado, tanto [pedidos de venta](../../sales-management/transactions.md#sales-order) como [pedidos de compra](../../procurement-management/transactions.md#purchase-order).

![Solapa Pedidos tercero con la lista de pedidos de venta y compra del tercero seleccionado](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-2.png)

Campos a tener en cuenta:

- **Nº de documento**: el número de documento del pedido.
- **Estado del documento**: el estado actual del pedido. Por ejemplo: Registrado.
- **Fecha del pedido**: la fecha en que se realizó el pedido.
- **Importe bruto total**: el importe bruto total del pedido.

### Albaranes del Tercero { #partner-shipments }

Esta solapa muestra todos los [albaranes](../../sales-management/transactions.md#goods-shipment) y [recepciones](../../procurement-management/transactions.md#goods-receipts) asociados al tercero seleccionado.

![Solapa Albaranes tercero con la lista de albaranes y recepciones del tercero seleccionado](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-3.png)

Campos a tener en cuenta:

- **Nº de documento**: el número de documento del albarán.
- **Estado del documento**: el estado actual. Por ejemplo: Completado.
- **Tipo de movimiento**: el tipo de movimiento. Por ejemplo: Albarán cliente.
- **Fecha del movimiento**: la fecha en que se produjo el movimiento.
- **Almacén**: el almacén desde el que se expidió el albarán.

### Facturas del Tercero { #partner-invoices }

Esta solapa muestra todas las facturas asociadas al tercero seleccionado, tanto [facturas de venta](../../sales-management/transactions.md#sales-invoice) (denominadas AR — Cuentas a cobrar — en el sistema) como [facturas de compra](../../procurement-management/transactions.md#purchase-invoice) (denominadas AP — Cuentas a pagar — en el sistema).

![Solapa Facturas tercero con la lista de facturas de venta y compra del tercero seleccionado](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-4.png)

Campos a tener en cuenta:

- **Tipo de documento**: el tipo de documento de factura. Por ejemplo: AR Factura.
- **Nº de documento**: el número de documento de la factura.
- **Estado del documento**: el estado actual. Por ejemplo: Completado.
- **Fecha de la factura**: la fecha en que se emitió la factura.
- **Importe bruto total**: el importe bruto total de la factura.

### Activos del Tercero { #partner-assets }

Esta solapa muestra todos los [activos](../../financial-management/assets/assets.md) asociados al tercero seleccionado, como equipos o propiedades que la organización registra en relación con ese tercero.

![Solapa Activos tercero con la lista de activos vinculados al tercero seleccionado](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner-info/business-partner-info-5.png)

Campos a tener en cuenta:

- **Producto**: el producto vinculado al activo.
- **Categoría del activo**: la categoría a la que pertenece el activo. Por ejemplo: Vehículos.
- **Nombre**: el nombre que identifica el activo. Por ejemplo: Coche.
- **Descripción**: información adicional sobre el activo, si existe.
- **Nombre de lote**: el número de lote asociado al activo, si corresponde.
- **Nº de serie**: el número de serie del activo, si corresponde.
- **Fecha de entrada en servicio**: la fecha en que el activo fue puesto en servicio.
- **Fecha de expiración**: la fecha en que el activo vence o se da de baja, si corresponde.

*[AR]: Accounts Receivable (Cuentas a cobrar) — facturas de venta pendientes de cobro
*[AP]: Accounts Payable (Cuentas a pagar) — facturas de compra pendientes de pago

---

This work is a derivative of [Master Data Management](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
