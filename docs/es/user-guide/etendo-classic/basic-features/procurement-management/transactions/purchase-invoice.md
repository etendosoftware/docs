---
title: Factura (Proveedor)
tags:
    - Proceso de Compras
    - Pedidos de compra
---

# Factura (Proveedor)

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Factura (Proveedor)`

## Visión general

La ventana **Factura (Proveedor)** se utiliza para crear, registrar y gestionar facturas de proveedor de bienes y servicios adquiridos.

Las facturas de proveedor normalmente se generan después de completar un Albarán, asegurando que las cantidades recibidas coinciden con la información facturada por el proveedor.

Las facturas se crean de dos formas:

1. Automáticamente, desde un Albarán relacionado usando el botón **Crear factura del albarán** en la ventana de Albarán.
2. Manualmente, introduciendo la factura directamente en esta ventana.

Cada factura define los productos o servicios, cantidades, precios, impuestos e importes a pagar al proveedor.

Cuando la factura se contabiliza, los gastos de compra correspondientes se reconocen en contabilidad. Si se configura un plan de gasto diferido, el reconocimiento del gasto se distribuye en el tiempo según la planificación definida.

!!! example "Flujo de trabajo típico de Factura (Proveedor)"
    1. Se completa un Albarán para un **Pedido de compra** existente.
    2. Abra la ventana **Factura (Proveedor)** y cree un nuevo registro de factura.
    3. Seleccione el **Tercero** (proveedor). El sistema rellena automáticamente las condiciones de pago, el método de pago y la tarifa.
    4. Vaya a la pestaña **Líneas** y haga clic en **Crear Líneas Desde Albarán** para traer los artículos recibidos.
    5. Revise las líneas, verifique cantidades y precios y, a continuación, haga clic en **Complete**.
    6. Contabilice la factura en el libro mayor usando el botón **Post**.
    7. Registre el pago usando el botón **Añadir pago**.

## Cabecera

La **Cabecera** contiene la información básica de una factura de proveedor. En la mayoría de los casos, seleccione el **Tercero**; el sistema rellena el resto de campos a partir de los valores por defecto y de la configuración del tercero seleccionado.

![Purchase invoice window](../../../../../assets/drive/1JvS1mOjiiyATJENTs5SuQIyEAr-UHmE3.png)

Campos a tener en cuenta:

- **Documento transacción**: por defecto es *AP Invoice* (factura de proveedor [tipo de documento](../../financial-management/accounting/setup/document-type.md)). Cámbielo a *AP Credit Memo* (tipo crédito positivo, no vinculado a pedidos o envíos) o a *Reversed Purchase Invoice* (importes negativos, para devoluciones).
- **Nº documento**: número de factura del proveedor si la secuencia lo permite; en caso contrario, se asigna un número interno.
- **Fecha de la factura**: fecha de la factura, utilizada para calcular la fecha de vencimiento.
- **Fecha contable**: fecha de contabilización en el libro mayor (por defecto, la Fecha de la factura).
- **Condiciones de pago**: define cuándo vence el pago (por ejemplo, neto 30 días). Se rellena automáticamente desde la configuración del Tercero.
- **Método de Pago**: define el mecanismo de pago (por ejemplo, transferencia bancaria o cheque). Se rellena automáticamente desde la configuración del Tercero.
- **Referencia del Proveedor**: número de referencia opcional proporcionado por el proveedor.

### Añadir líneas

Añada líneas de factura usando uno de los siguientes métodos:

1. Haga clic en **Crear Líneas Desde Pedido** o **Crear Líneas Desde Albarán** para traer elementos pendientes desde un documento relacionado.
2. Haga clic en **Copiar líneas** para copiar líneas desde una factura existente.
3. Añada líneas manualmente en la pestaña **Líneas** cuando no exista un pedido o albarán relacionado.

### Completar la factura

Haga clic en **Complete** para finalizar la factura. Esto crea el Plan de Pago y actualiza el Monitor de Pagos. Si la factura contiene un producto empaquetado (un producto compuesto por múltiples componentes, también llamado lista de materiales o BOM), el sistema lo desglosa automáticamente en sus líneas de componentes individuales.

Tras completar la factura, están disponibles las siguientes acciones:

- **Post** la factura en el libro mayor usando el botón [Post/Unpost](#postunpost).
- **Anular o Reactivar** la factura usando el botón [Reactivar](#reactivate).
- **Registrar un pago** usando el botón [Añadir pago](#add-payment).

## Líneas

Una vez guardada la cabecera de la Factura (Proveedor), añada una o más líneas de factura para los productos o gastos que se están facturando.

Campos a tener en cuenta:

- **Línea de factura financiera**: seleccione esto para líneas que no son productos físicos; por ejemplo, una cuenta contable (apunte de mayor) o un cargo de inmovilizado. El campo Producto se sustituye por un campo Cuenta.
- **Valor atributos**: se muestra si el producto utiliza atributos (color, talla, número de serie, etc.).
- **Línea de Pedido de compra / Línea de Albarán**: vincula la línea de factura con la línea del Pedido de compra o del Albarán relacionada, si existe.

### Diferir gastos

Use gastos diferidos para repartir un coste en varios periodos contables en lugar de reconocerlo todo de una vez.

- **Gasto postpuesto**: seleccione esto para distribuir el gasto en el tiempo y mostrar los campos del plan de gastos.
- **Tipo de plan de gastos**: frecuencia de reconocimiento (actualmente: mensual).
- **Número de periodo**: número de periodos en los que se distribuye el gasto.
- **Periodod inicial**: primer periodo contable abierto en el que comienza el reconocimiento.

Estos valores del plan de gastos pueden venir por defecto desde la configuración del producto. Si se utiliza un plan de gastos, la contabilidad de la factura sigue dicho plan.

!!! example "Gasto diferido: seguro anual"
    Una empresa compra un seguro para el negocio por un año completo con un coste de 1.200 USD.

    - **Gasto postpuesto**: seleccionado
    - **Tipo de plan de gastos**: Mensual
    - **Número de periodo**: 12
    - **Periodod inicial**: Enero

    El sistema reconoce 100 USD al mes durante 12 meses en lugar de imputar los 1.200 USD completos en un único periodo.

### Explotar

El botón **Explotar** aparece cuando la línea de factura seleccionada contiene un producto empaquetado (lista de materiales) que todavía no se ha desglosado en sus componentes. Al hacer clic en este botón, la línea del paquete se sustituye por una línea por componente, de modo que cada artículo aparece individualmente en la factura.

!!! warning
    Esta acción no se puede deshacer. Para revertirla, elimine primero las líneas de componentes y luego vuelva a añadir el producto empaquetado.

### Asociar Costes LC

El botón **Asociar Costes LC** asocia el **coste de entrega estimado** definido en la ventana de Coste en destino con el **coste de entrega facturado** introducido en una línea de factura.

Esta opción está disponible cuando la línea del pedido de compra o de la factura contiene un **producto** o una **cuenta** configurados como tipo de coste en destino. Ambos costes deben pertenecer al **mismo tipo de coste en destino** para poder asociarse.

La asociación ayuda a:

- Conciliar costes en destino estimados y facturados.
- Mantener los costes de producto precisos.
- Generar los asientos contables correctos.

Tras hacer clic en **Asociar Costes LC**, se abre la ventana de selección y edición. Solo se muestran **documentos de Coste en destino procesados**.

Desde esta ventana:

- Seleccione el documento de coste en destino correspondiente.
- Introduzca el importe en **Imp. Asociado**.
- Active **Procesar Asociación** para completar el proceso inmediatamente.

La casilla **Ajustar Asociación** controla cómo se gestionan las diferencias entre costes estimados y facturados:

- **Marcada**: crea un ajuste adicional de coste en destino para actualizar el coste del producto.
- **Desmarcada**: no se crea ningún ajuste de coste.

#### Escenarios de asociación

| Escenario | Ajustar Asociación | Resultado |
|---|---|---|
| Estimado = Facturado | Cualquiera | Solo se contabiliza la asociación en el libro mayor. No se crean ajustes. |
| Estimado ≠ Facturado | Marcada | Se crea un ajuste de coste en destino. El coste del producto se actualiza al importe facturado. Se contabilizan la asociación y el ajuste. |
| Estimado ≠ Facturado | Desmarcada | Solo se contabiliza la asociación. El coste del producto no se modifica. |

### Línea de impuesto

La pestaña **Línea de impuesto** es de solo lectura y se rellena automáticamente para cada línea de factura cuando se completa la factura. Detalla la información de impuestos de cada línea en base al campo Impuesto, que se rellena previamente según la configuración de impuestos.

## Impuesto

La pestaña **Impuesto** resume la información relacionada con impuestos para toda la factura de proveedor. Contiene un registro por cada tipo impositivo utilizado en la factura.

El campo **Impuestos** refleja el valor del impuesto calculado automáticamente en base al tipo impositivo y a la configuración de la base imponible.

!!! info
    Si su organización necesita ajustar importes de impuestos en facturas para que coincidan con sistemas externos o requisitos regulatorios (por ejemplo, para corregir diferencias de redondeo de unos céntimos), esta funcionalidad está disponible a través del **Financial Extensions Bundle**.

    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

    Para más información, visite: [Adjust Invoice Tax user guide](../../../optional-features/bundles/financial-extensions/adjust-invoice-tax.md)

    Esta funcionalidad es compatible desde Etendo 23.

## Descuentos

Esta pestaña lista los descuentos aplicados a la factura de proveedor. Los descuentos pueden ser:

- **Aplicados automáticamente** en base a la configuración del Tercero del proveedor.
- **Introducidos manualmente** para ajustes específicos de la factura.

Cada registro de descuento muestra el porcentaje de descuento y si se aplica **en cascada** (cada descuento se calcula sobre el precio ya reducido por el descuento anterior; por ejemplo, 10% sobre 100 USD = 90 USD, luego 5% sobre 90 USD = 85,50 USD) o **de forma independiente** (cada descuento se calcula sobre el precio original; 10% + 5% = 15% sobre 100 USD = 85 USD).

!!! info
    Para más información sobre la configuración de descuentos, visite [Descuentos](../../master-data-management/master-data.md#basic-discount).

## Plan de Pago

La pestaña **Plan de Pago** lista los pagos programados esperados contra la factura. Los registros del plan de pagos se generan automáticamente cuando se completa la factura, en base a las **Condiciones de pago** definidas en la cabecera.

Cada registro muestra:

- **Fecha esperada**: la fecha en la que vence el pago.
- **A liquidar**: el importe a pagar en esa fecha.
- **Método de Pago**: el mecanismo de pago a utilizar.
- **Importe Pendiente**: el importe restante aún no pagado.

El plan de pagos de una factura no pagada puede modificarse:

- La **Fecha esperada** puede cambiarse directamente en esta pestaña.
- La **Fecha esperada**, el **Método de Pago** y el **Importe Pendiente** también pueden cambiarse usando el botón [Modificar Plan de Pagos](#modify-payment-plan), si está instalado el módulo Advanced Bank Account Management.

## Factura Rectificativa

La pestaña **Factura Rectificativa** vincula un documento de reversión con la factura original que revierte. Esta pestaña se utiliza en dos escenarios:

**Anulación completa de una factura**

Cuando una factura se anula usando el botón [Reactivar](#reactivate) con la acción **Anular**:

- Etendo crea automáticamente una *Reversed Purchase Invoice* y la vincula a la factura original.
- La factura original aparece en la pestaña **Factura Rectificativa** del documento de reversión.

**Anulación parcial de una factura**

Al crear manualmente una reversión parcial (*AP Credit Memo* o *Reversed Purchase Invoice*):

- Para vincular una reversión parcial con la factura original: abra el documento de reversión (el AP Credit Memo o Reversed Purchase Invoice que acaba de crear), vaya a su pestaña **Factura Rectificativa** y añada el número de la factura original. Este paso es necesario para mantener la trazabilidad entre ambos documentos.

## Tipos de cambio

La pestaña **Tipos de cambio** permite introducir un tipo de cambio entre la divisa del libro mayor de la organización y la divisa de la factura del proveedor, que se utilizará al contabilizar la factura en el libro mayor.

Esta pestaña es relevante cuando la divisa de la factura del proveedor difiere de la divisa del libro mayor de la organización; por ejemplo, al comprar bienes a un proveedor extranjero.

La pestaña permite introducir:

- Un **Tipo de Cambio** entre la divisa del libro mayor y la divisa de la factura del proveedor.
- O el **importe total de la factura en divisa extranjera**, para que Etendo calcule automáticamente el tipo de cambio correspondiente.

!!! info
    Etendo también mantiene un repositorio central de tipos de cambio, que se utiliza cuando no se define un tipo de cambio a nivel de documento. Para más información, visite [Esquema contable](../../financial-management/accounting/setup/general-ledger-configuration.md).

## Contabilidad

Una factura de proveedor puede contabilizarse en el libro mayor en una **Fecha contable** determinada usando el botón [Post/Unpost](#postunpost).

### Contabilización estándar de Factura (Proveedor)

| Cuenta | Debe | Haber | Comentarios |
|---|---|---|---|
| Gasto de producto | Importe neto de línea | | Una por línea de factura |
| IVA soportado | Impuestos | | Una por línea de impuesto |
| Descuento en gasto de producto | | Importe de descuento | Una por línea de factura (si existe descuento) |
| Deuda con proveedor | | Importe bruto total | Una por factura |

### Contabilización de gasto diferido

Cuando una línea de factura de proveedor tiene configurado un [plan de gastos](#diferir-gastos), la contabilización se distribuye en múltiples periodos en lugar de reconocer el gasto completo de una vez.

**Contabilización inicial (Fecha contable):**

| Cuenta | Debe | Haber |
|---|---|---|
| Gasto diferido de producto | Importe neto de línea | |
| IVA soportado | Impuestos | |
| Deuda con proveedor | | Importe bruto total |

**Cada periodo posterior (Fecha contable + 1 mes, + 2 meses, ..., + N meses):**

| Cuenta | Debe | Haber |
|---|---|---|
| Gasto de producto | Importe neto de línea / N | |
| Gasto diferido de producto | | Importe neto de línea / N |

Donde **N** es el número de periodos definido en el plan de gastos.

!!! info
    Para más información, visite [How to Manage Deferred Revenue and Expenses](../../../how-to-guides/how-to-manage-deferred-revenue-and-expenses.md).

### Contabilización de factura revertida

Cuando una factura se anula, el documento de reversión crea los siguientes asientos contables:

| Cuenta | Debe | Haber | Comentarios |
|---|---|---|---|
| Gasto de producto | | Importe neto de línea | Una por línea de factura |
| IVA soportado | | Impuestos | Una por línea de impuesto |
| Deuda con proveedor | Importe bruto total | | Una por factura |

La contabilización de *AP Credit Memo* sigue la misma estructura que la contabilización de *Reversed Purchase Invoice*.

!!! info
    Para detalles sobre cómo anular o anular parcialmente una factura, consulte la sección del botón [Reactivar](#reactivate).
## Botones

### Post/Unpost

Contabilice una factura de proveedor en el libro mayor en una **Fecha contable** determinada usando este botón. Una vez contabilizada, deshaga la contabilización usando el mismo botón.

### Reactivar

![pop-up-reactivate](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/pop-up-reactivate.png)

Este botón proporciona dos opciones para una factura Completada:

- **Reactivar**: devuelve el registro del estado *Completado* a *Borrador*, permitiendo ediciones sin crear un nuevo documento. Use esta opción cuando la factura contenga errores que deban corregirse antes de volver a contabilizar.
- **Anular**: crea un nuevo documento que revierte completamente la factura. Use esta opción cuando la factura ya no sea válida y deba cancelarse.

!!! example "Cuándo usar cada opción"
    - Use **Reactivar** cuando se haya introducido incorrectamente un precio o una cantidad y la factura aún no se haya pagado.
    - Use **Anular** cuando se devuelvan mercancías al proveedor y sea necesario cancelar la factura completa.

**Anulación de una factura**

![pop-up-void](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/popup-void.png)

Al anular, especifique los siguientes campos para el documento de reversión:

- **Fecha de anulación**: fecha de movimiento del documento de reversión. Por defecto es la fecha actual y no puede ser anterior a la **Fecha de la factura** original.
- **Fecha contable de anulación**: fecha contable del documento de reversión. Por defecto es la fecha actual y no puede ser anterior a la **Fecha contable** original.
- **Referencia del Proveedor**: número de referencia opcional para el documento revertido. Introdúzcalo aquí o deje el campo en blanco para completarlo más tarde.

Etendo genera automáticamente un nuevo documento en la ventana *Factura (Proveedor)* que revierte la factura original e informa del nuevo número de documento.

El documento de reversión utiliza el tipo de documento de transacción *Reversed Purchase Invoice*, que es idéntico al original pero con cantidades facturadas negativas.

Una vez creado el documento de reversión, cambie la *Fecha de la factura* y la *Fecha contable* si es necesario antes de contabilizar.

La pestaña *Factura Rectificativa* enlaza tanto el documento original como el de reversión.

**Anulación parcial de una factura**

También es posible anular parcialmente una factura de proveedor creando manualmente uno de los siguientes documentos de compra revertidos en la ventana Factura (Proveedor):

- **AP Credit Memo**: la cantidad facturada es positiva.
- **Reversed Purchase Invoice**: la cantidad facturada es negativa.

Para enlazar una reversión parcial con la factura original: abra el documento de reversión (el AP Credit Memo o Reversed Purchase Invoice que acaba de crear), vaya a su pestaña **Factura Rectificativa** y añada el número de la factura original. Este paso es obligatorio para mantener la trazabilidad de auditoría entre ambos documentos.

Para saber más, visite [Factura Rectificativa](#reversed-invoices).

La contabilización de **AP Credit Memo** se ve igual que la contabilización de **Reversed Purchase Invoice**. La principal diferencia entre los dos tipos de documento es:

- **AP Credit Memo**: la cantidad facturada es una cantidad positiva.
- **Reversed Purchase Invoice**: la cantidad facturada es una cantidad negativa.

!!! note
    Use el tipo de documento **Reversed Purchase Invoice** al anular parcialmente facturas de proveedor.

### Añadir pago

Registre uno o más pagos contra una factura de proveedor usando el botón **Añadir pago**, que abre la ventana emergente Añadir pago.

### Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad Contabilización Masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización Masiva**.

El Estado contable de cada registro se muestra en la barra de estado en la vista de formulario, o en una columna en la vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Bulk Completion

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Essential Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad Bulk Completion permite al usuario completar, reactivar o anular múltiples registros seleccionándolos y haciendo clic en el botón **Bulk Completion**. Esto facilita la gestión de registros y la hace más eficiente.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../../optional-features/bundles/essentials-extensions/bulk-completion.md).

!!! warning
    **Nota:** Si el módulo [Purchase Invoice Validation](../../../optional-features/bundles/procurement-extensions/purchase-invoice-validation.md) está activo en su sistema, la anulación masiva no funcionará. En ese caso, anule cada factura individualmente usando la opción **Reactivar > Anular**, que permite introducir una referencia de proveedor única para cada reversión.
    ![popup-bulk-void](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/popup-bulk-void.png)

### Eliminar Pago

La funcionalidad de eliminación de pagos borra y reactiva pagos. También permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Para eliminar un pago, seleccione el documento correspondiente y haga clic en el botón **Eliminar Pago**. También se eliminan los siguientes registros relacionados:

- Si hay un pedido asociado a la factura, se elimina el enlace entre el pedido y el pago (ventana **Pedido de compra** > pestaña **Plan de Pago**).
- Si el pago está en estado *Depositado/Retirado no conciliado* en la cuenta financiera, la transacción también se elimina (ventana **Cuenta financiera** > pestaña **Transacción**).
- Si el pago está conciliado mediante un método automático, también se eliminan la línea de extracto bancario y la línea de conciliación bancaria (ventana **Cuenta financiera** > **Extractos bancarios importados** y **Reconciliaciones**).

!!! info
    Si el pago está contabilizado, el asiento contable también se elimina.

![Remove Payment confirmation dialog](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/PRpic4.png)

### Deshacer anulación

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

El botón **Deshacer anulación** reactiva facturas de proveedor anuladas. Seleccione la factura y haga clic en **Deshacer anulación** para restaurarla.

![Unvoid button restoring a voided purchase invoice to Complete status](../../../../../assets/drive/1UisxZzbpppLvN_rdL__TJg8tLeh5sMfW.png)

Una vez finalizado el proceso, el estado de la factura de proveedor pasa a *Completado*.

!!! note
    En el caso de la versión estándar del módulo, deshaga también la anulación de la factura revertida correspondiente.

!!! warning
    **Importante:** Cuando deshace la anulación de una factura, el sistema restaura los asientos contables originales. Si la factura revertida ya estaba contabilizada, esos asientos pueden seguir existiendo, lo que provocaría asientos contables duplicados.

    Antes de contabilizar la factura reactivada, revise la pestaña **Contabilidad** y elimine cualquier asiento existente que se haya creado por la anulación previa. Si no está seguro de si existen asientos, contacte con su administrador del sistema antes de continuar.

!!! info
    Consulte la documentación técnica sobre [Advanced Financial Docs Processing](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle/overview.md#advanced-financial-docs-processing) para ampliar el proceso.

### Modificar Plan de Pagos

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

El módulo Advanced Bank Account Management añade un campo **Cuenta bancaria** a la cabecera de la Factura (Proveedor). Este campo se rellena automáticamente con la cuenta bancaria relacionada con la dirección o el tercero de la factura. También se añade el botón **Modificar Plan de Pagos** para una gestión flexible de pagos.

![bank-account.png](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/bank-account.png)

!!! info
    Para más información, visite la [guía de usuario de Advanced Bank Account Management](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).

## Intercompany

Si su empresa opera con múltiples entidades legales dentro de Etendo (por ejemplo, una empresa matriz que compra en nombre de una filial), la funcionalidad Intercompany crea automáticamente la factura de venta asociada en la organización receptora cuando se contabiliza una factura de proveedor, eliminando la necesidad de registrar la transacción dos veces.

Cuando los pedidos o las facturas implican a dos o más organizaciones que pertenecen al mismo cliente, esta funcionalidad genera automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visite [la guía de usuario del módulo Intercompany](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany.md).

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.

---