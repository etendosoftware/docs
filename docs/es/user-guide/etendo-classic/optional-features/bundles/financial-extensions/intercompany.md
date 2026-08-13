---
title: Intercompany
tags:
    - Intercompany
    - Organization
    - Reverse
    - Order
    - Invoice
    - Completado Masivo
    - Resolución de problemas
---
# Intercompañía { #intercompany }

:octicons-package-16: Javapackage: `com.etendoerp.advanced.intercompany`

## Visión general { #overview }

Esta sección describe el módulo de Intercompañía incluido en el bundle **Financial Extensions**.

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones que son diferentes pero pertenecen al mismo cliente, esta funcionalidad permite generar automáticamente el **documento inverso correspondiente**. 

Por ejemplo, si la organización *A* realiza una transacción de venta a la organización *B*, una vez que la factura de venta es creada manualmente por la organización *A*, esta funcionalidad creará automáticamente una factura de compra para la organización *B*.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Bundle Financial Extensions](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Configuración { #set-up }

### Ventana Organización { #organization-window }

Es necesario que cada organización que utilice este módulo tenga un tercero asignado.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany/organization-window.png)

### Ventana Tercero { #business-partner-window }

!!! info
    Al configurar un nuevo Tercero, tenga en cuenta que este tercero debe ser visible en la organización destino. 


El Tercero debe configurarse como **Proveedor** y **Cliente**, utilizando las casillas de verificación correspondientes.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany/business-partner-customer.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany/business-partner-vendor.png)

En la solapa **Documentos de Intercompañía**, es necesario seleccionar los tipos de documento requeridos para este tercero.

!!! warning
    La configuración de la solapa **Documentos de Intercompañía** debe existir en ambos terceros involucrados en la transacción: el tercero origen y el tercero destino. Configurar solo uno de ellos no es suficiente para generar el documento inverso.

!!! info
    No es obligatorio crear nuevos tipos de documento, pero se recomienda.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany/business-partner-intercompany-documents.png)

!!! info
    La información tanto en el tercero origen como en el tercero destino debe ser la misma.

Etendo utiliza la configuración de **Documentos de Intercompañía** del tercero asociado a la organización destino para determinar qué tipo de documento inverso crear. Si esta configuración falta o está incompleta en el tercero destino, Etendo no genera el documento inverso, o lo genera con un tipo de documento incorrecto.

## Facturas y pedidos { #invoices-and-orders }

!!! info
    La siguiente información puede aplicarse no solo a facturas de venta y compra, sino también a pedidos de venta y compra.

### Cabecera { #header }

Los campos relevantes se describen a continuación:

-   **Organización**: es necesario seleccionar una organización configurada para trabajar como una organización de intercompañía (en el siguiente ejemplo, la organización *F&B US East Coast*).
-   **Tercero**: es necesario seleccionar un tercero configurado para trabajar como un tercero de intercompañía (en el siguiente ejemplo, *Be Soft Drinker, Inc.*).
-   **Documento de transacción**: es necesario seleccionar el tipo de documento definido en la solapa **Documentos de Intercompañía** del tercero (en el siguiente ejemplo, el tipo de documento *AR Invoice Intercompany*).

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany/invoice-header.png)

### Líneas { #lines }

Los campos relevantes se describen a continuación:

-   **Producto**: el producto debe ser visible para ambas organizaciones (en el siguiente ejemplo, *Lemonade*). 
-   **Apuntes de mayor**: los apuntes de mayor necesarios deben ser visibles para ambas organizaciones.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany/invoice-lines.png)

**Producto**

Los campos relevantes se describen a continuación:

-   **Precio**: el precio debe ser equivalente y estar disponible en cada tarifa.
-   **Moneda**: la moneda debe ser la misma para ambas organizaciones.
-   **Impuesto**: Etendo no copia el impuesto del documento origen. Recalcula el impuesto utilizando la configuración propia de la organización destino (producto, almacén, direcciones y configuración de impuestos), por lo que el importe del impuesto en el documento inverso puede diferir del documento origen.

Etendo no copia el precio del documento origen automáticamente. Antes de crear el documento inverso, Etendo comprueba que el producto exista en la tarifa configurada en el tercero destino, y que el precio coincida. Si alguna de estas comprobaciones falla, Etendo no crea el documento inverso.

!!! warning
    Las promociones, descuentos o ajustes de precio activos pueden modificar el precio final de una línea, pero solo en el momento en que se completa el documento. Por este motivo, el documento inverso puede fallar al generarse incluso si el documento parecía correcto antes de completarlo. Si obtiene un error de totales, compruebe si una promoción, descuento o ajuste de precio activo modificó el precio al completar el documento.

### Completar o registrar documentos { #complete-or-book-documents }

Etendo solo genera el documento inverso cuando el documento origen se completa mediante la acción [**Completado Masivo**](../essentials-extensions/bulk-completion.md). Esto aplica tanto a facturas como a pedidos de intercompañía. La acción estándar **Completar** para facturas y la acción estándar **Registrar** para pedidos no aplican la lógica de intercompañía: completar o registrar un documento mediante la acción estándar no crea el documento inverso correspondiente.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany/complete-order.png)

!!! warning
    Si la factura origen tiene descuentos aplicados, configure los mismos descuentos en la organización destino. De lo contrario, la creación del documento inverso falla debido a una diferencia en los totales.

#### Reactivar documentos { #reactivate-documents }

Para reactivar documentos de intercompañía, ambos documentos no deben tener un pago asociado.

!!! info
    Este proceso solo está permitido para documentos origen.

## Resolución de problemas { #troubleshooting }

Utilice la siguiente lista de comprobación para identificar la causa cuando un documento de intercompañía no genera el documento inverso, o falla la validación.

### Flujo { #flow }

-   ¿El documento se completó utilizando la acción estándar **Completar** o **Registrar**, o mediante **Completado Masivo**? Tanto las facturas como los pedidos de intercompañía requieren **Completado Masivo**. La acción estándar **Completar** o **Registrar** nunca crea el documento inverso.
-   Al reactivar un documento, ¿es el documento origen el que se está reactivando? Etendo solo permite la reactivación en el documento origen. ¿Alguno de los documentos tiene un pago asociado?

### Configuración { #configuration }

-   ¿Ambos terceros, origen y destino, tienen configurada la solapa **Documentos de Intercompañía** con los tipos de documento requeridos?
-   ¿Ambas organizaciones están configuradas como organizaciones de intercompañía, cada una con su tercero asignado?
-   ¿El producto es visible en ambas organizaciones, y existe en la tarifa del tercero destino?
-   ¿La moneda coincide entre ambas organizaciones?
-   ¿Los apuntes de mayor son visibles en ambas organizaciones, si corresponde?
-   Para facturas con descuentos, ¿la organización destino tiene configurados los mismos descuentos?

### Validación { #validation }

-   Error: *"No se puede crear el documento inverso. Los importes finales del documento fuente y del documento inverso no coinciden."* Compruebe estas posibles causas:
    -   Una promoción, descuento o ajuste de precio activo modificó el precio al completar el documento (consulte la advertencia en [Líneas](#lines)).
    -   El producto o su precio no coincide con la tarifa destino.
    -   La factura tiene descuentos que no están configurados en la organización destino.
    -   El documento se completó con la acción estándar **Completar** o **Registrar** en lugar de **Completado Masivo**.
-   El importe del impuesto en el documento inverso es diferente de lo esperado. Etendo no copia el impuesto del documento origen; siempre recalcula el impuesto utilizando la configuración de la organización destino. Compruebe la configuración de impuestos, el producto, el almacén y las direcciones en la organización destino.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
