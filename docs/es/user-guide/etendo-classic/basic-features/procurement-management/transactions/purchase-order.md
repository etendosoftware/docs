---
title: Pedido de compra
tags:
    - Pedidos de compra
    - Proceso de Compras
---

# Pedido de compra

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Pedido de compra`

La ventana Pedido de compra permite al usuario gestionar pedidos que, una vez contabilizados, se enviarán a los proveedores externos. En otras palabras, es un documento para registrar productos y/o servicios que se van a comprar y documentar.

![Purchase order window](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/purchaseorder.png)

Una vez que el documento está contabilizado, puede enviarse al proveedor externo y puede pagarse por adelantado si es necesario.

Los pedidos de compra pueden crearse y contabilizarse en la sección de cabecera de la ventana de pedido de compra.

## Cabecera

La **cabecera del pedido de compra** permite introducir la siguiente información:

- **Organización:** entidad organizativa dentro del cliente.
- **Documento transacción**, que en este caso se establece por defecto como "**Pedido de compra**".
- **Nº documento**, o el número de pedido de compra de la compañía.
- **Fecha de pedido:** esta fecha también se establece por defecto por Etendo en base a la fecha del sistema, pero siempre puede modificarse.
- **Terceros**: el usuario final debe seleccionar el proveedor al que se emite el pedido de compra.
- **Dirección**: se completa automáticamente una vez seleccionado el tercero, en base a la dirección o ubicación configurada como "Dirección de envío".
- **Almacén**: aunque Etendo lo establece por defecto según las opciones seleccionadas en el "Perfil", debe ser verificado por el usuario final.
- **Fecha comprometida**: es la fecha en la que la organización o entidad legal requiere que se entreguen los artículos.
- **Método de pago**, **Condiciones de pago** y **Tarifa**: se establecen por defecto por Etendo una vez seleccionado un tercero.
- **Nº de referencia**, texto libre que puede encontrarse en la sección "Más información"; puede usarse para guardar el número de pedido del proveedor, si existe.

En la **barra de estado** de la cabecera, el usuario puede encontrar la siguiente información:

- **Estado doc.**: estado del documento del pedido. El pedido puede estar en estado contabilizado, borrador, cerrado, entre otros.
- **Importe total**: importe bruto total del pedido.
- **Imp. total líneas**: importe neto total del pedido.
- **Moneda**: moneda del pedido.
- **Estado del envío**: indica en % qué cantidad del pedido se ha recibido.
- **Estado de factura**: indica en % qué cantidad del pedido se ha facturado.

**Una vez que la información de cabecera esté correctamente cumplimentada, puede ir a la pestaña "Líneas" para introducir la información de la(s) línea(s) del pedido de compra**.

!!! info
    Para aprender cómo introducir líneas de pedido de compra, visite la siguiente sección [Líneas](purchase-order.md#lines).

Es posible realizar hasta **tres acciones posibles respecto a un pedido de compra**, usando el **botón de cabecera "Registrar"**:

- **Procesarlo**, en caso de que quiera procesarlo pero no registrarlo como definitivo, porque podría necesitar cambiarlo más adelante.
- **Anularlo**, en caso de que el pedido de compra ya no sea necesario y, por tanto, deba anularse.
- **Registrarlo**, en caso de que sea correcto y definitivo.

!!! info
    Si existen productos LdM (BOM) no almacenables y no se han desglosado, el botón Registrar los desglosa automáticamente.

## Líneas

Una vez que la cabecera del pedido de compra se ha cumplimentado correctamente y se ha guardado, cada línea del pedido de compra puede crearse en esta pestaña.

Las líneas del pedido de compra pueden crearse de tres formas diferentes:

**1\. Creando manualmente nuevos registro(s) en la pestaña "Líneas"**.

Los campos de la línea del pedido de compra que puede cumplimentar se describen a continuación:

- **Producto**. Puede seleccionar un artículo o producto de la lista o usar el icono del selector de producto.
- **Cant. pedido**, o **Cantidad Operativa** si el producto tiene configurada una *unidad de medida alternativa (AUM)*. Esta es la cantidad necesaria del producto/artículo.
- **Unidad** del producto, o **Unidad Alternativa** del producto dependiendo de la configuración del producto respecto a la unidad de medida.
- **Valor del conjunto de atributos. Un atributo asociado a un producto como parte de un conjunto de atributos.**
- **Precio unitario**. Este proviene de la **Tarifa** seleccionada en la cabecera, pero siempre puede modificarse.
- **Importe neto de línea. El importe final de una línea especificada, basado únicamente en cantidades y precios.**
- **Impuesto**. El impuesto de compra normalmente lo completa el sistema, dependiendo de la configuración de impuestos.

**2\. Recuperando todas las líneas de pedidos de compra creados previamente.** En este caso, debe usar el botón de proceso "**Copiar desde pedidos**".

Este botón de proceso habilita la ventana **Copiar desde pedidos (seleccionar y editar)**.

La ventana "Copiar desde pedidos (seleccionar y editar)" permite buscar los pedidos a copiar usando las opciones de filtro disponibles.

La información de líneas de los pedidos seleccionados se insertará en la(s) línea(s) del pedido de compra; después, esa información puede modificarse manualmente.

**3\. Copiando líneas de otros pedidos de compra.**

En este caso, debe usar el botón de proceso **"Copiar líneas"**.

Este botón de proceso habilita una nueva ventana llamada "Copiar líneas desde pedido", que permite crear líneas de pedido seleccionando los productos ya comprados al proveedor del pedido, teniendo en cuenta los *días de consumo* configurados para el proveedor.

En la **barra de estado** de cada línea, puede encontrar información sobre:

- **Cant.entregada**: número de productos recibidos de la línea.
- **Cant.facturada**: número de productos facturados de la línea.

### Botón Desglosar

El botón Desglosar se muestra al seleccionar una línea con un producto LdM (BOM) no almacenable y el producto aún no se ha desglosado. Al desglosar un producto, los componentes de la lista de materiales de los que consta el producto seleccionado se muestran en el pedido.

!!! info
    Una vez desglosado, no puede comprimirse. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y luego el producto LdM) e insertar de nuevo el producto LdM no almacenable.

### Línea de impuesto

Para cada línea del pedido de compra, Etendo completa automáticamente en esta pestaña la información relacionada con el impuesto de línea.

La pestaña de impuesto de línea informa sobre cada línea del pedido de compra:

- **tipo impositivo aplicado**
- **importe de impuesto calculado**
- **Base imponible**

!!! info
    No es posible crear manualmente una nueva línea ni modificar las existentes.

### Descuentos básicos

Lista información sobre los descuentos aplicados automáticamente en base a la configuración del proveedor y/o introducidos manualmente para el pedido de compra.

![Basic discounts](../../../../../assets/drive/1AavUV8S8kQ2dp0P_W9lw06XfmAf5d_g-.png)

### Plan de pagos

Muestra el importe total previsto a pagar al registrar el pedido, así como el/los importe(s) pagados por adelantado o pagados contra la(s) factura(s) del pedido.

La información del plan de pagos es necesaria a nivel de pedido porque los proveedores podrían solicitar un **pago por adelantado** de toda o parte de una deuda antes de su fecha de vencimiento.

Los planes de pago de pedidos de compra **no muestran ni gestionan fechas de vencimiento válidas**, sino el plan de pagos de la(s) factura(s) de compra correspondiente(s).

Esta pestaña también muestra información sobre los pagos regulares recibidos contra la(s) factura(s) de este pedido, como importes pagados.

Por último, el plan de pagos de un pedido de compra será **eliminado**:

- si el pedido de compra es **Reactivated**
- o si el pedido de compra es **Voided**

### Detalles de Pago

Muestra los detalles de los pagos (pagos por adelantado o pagos regulares) realizados para el pedido o para la(s) factura(s) del pedido.

## Cómo reactivar un pedido de compra cerrado

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning "Aviso de dependencia"
    Este módulo depende del módulo [**Bulk Completion**](../../../optional-features/bundles/essentials-extensions/bulk-completion.md), ya que las acciones de procesamiento de **pedido** deben realizarse usando procesos modernos que permitan el disparo de Hooks, en lugar del procesamiento legacy. Debido a este requisito, las acciones legacy de **cerrar/reactivar** para pedidos se ocultarán y estas acciones solo estarán disponibles a través del botón **Bulk Completion**.

Etendo permite al usuario reactivar pedidos de compra cerrados seleccionando el/los necesario(s) y haciendo clic en el botón Deshacer cierre.

![](../../../../../assets/drive/1cyLa7pjnsNgXtnSEK2lZX9s35imhD2Kq.png)

Una vez finalizado el proceso, el estado del pedido de compra pasa a contabilizado.

!!! info
    Consulte la documentación técnica sobre Advanced Financial Docs Processing para ampliar el proceso.

## Eliminación de pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde esta ventana, es posible eliminar pagos asociados a un pedido de compra seleccionando el documento correspondiente y luego haciendo clic en el botón Eliminar pago. Si existe una factura asociada al pedido, también se eliminará la relación de esta factura con el pago en cuestión (ventana Factura de compra > pestaña Plan de pagos).

Si el pago está incluido en la cuenta financiera, es decir, si está en estado Depositado/Retirado no conciliado, también se eliminará la transacción en ella (ventana Cuenta financiera > pestaña Transacción).

Si el pago está conciliado mediante un método automático, entonces, además de la transacción en la cuenta financiera, se eliminará la línea del extracto bancario a la que estaba vinculada (ventana Cuenta financiera > Extractos bancarios importados) y la línea correspondiente de la conciliación bancaria (Cuenta financiera > Conciliaciones).

!!! info
    Si el pago está contabilizado, también se elimina el asiento contable.

![](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/PRpic2.png)

## Intercompany

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones diferentes pero que pertenecen al mismo cliente, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visite [la guía de usuario del módulo Intercompany](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany.md).

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Bulk Completion

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Essential Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad Bulk Completion permite al usuario completar, reactivar o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Bulk Completion**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../../optional-features/bundles/essentials-extensions/bulk-completion.md).

## Advanced Bank Account Management

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Este módulo añade un nuevo campo a la cabecera de la ventana Pedido de compra: **Cuenta Bancaria**. Este campo se completa automáticamente con la cuenta bancaria relacionada con la dirección o el tercero del pedido.

![bank-account-3.png](../../../../../assets/legacy/bank-account-3.png)

!!! info
    Para más información, visite la [guía de usuario de Advanced Bank Account Management](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.