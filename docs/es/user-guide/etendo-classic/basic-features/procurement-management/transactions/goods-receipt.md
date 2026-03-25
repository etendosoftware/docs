---
title: Albaranes pendientes de recibir
tags:
    - Albaranes pendientes de recibir
    - Proceso de Compras
---

# Albaranes pendientes de recibir

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Albarán (Proveedor)`

Un albarán (proveedor) es un documento emitido para reconocer la recepción de los artículos listados en él. En otras palabras, es un documento utilizado para registrar en Etendo los detalles de los artículos recibidos físicamente en el almacén.

## Cabecera

Los albaranes pendientes de recibir pueden emitirse y contabilizarse en la sección de cabecera de la ventana de albarán (proveedor).

![Cabecera de albaranes](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/goodsreceipt2.png)

Los campos a cumplimentar en la **cabecera del albarán (proveedor)** son:

- **Tipo de documento**, que se rellena por defecto como "MM Receipt".
- **Almacén**, donde se ubicarán las mercancías.
- **Tercero**, tercero que entrega las mercancías.
- **Fecha del movimiento**, fecha de entrega de las mercancías.
- **Fecha contable**, fecha contable en caso de contabilizar el albarán (proveedor).
- **Pedido de compra**, número de pedido de compra enlazado automáticamente por Etendo, en caso de que el albarán (proveedor) se cree automáticamente a partir de un pedido de compra.
- **Nº de referencia**, el equipo de almacén puede indicar aquí el número de albarán del proveedor; de este modo, el número interno del albarán (proveedor) y el número de albarán del proveedor quedan vinculados.

En la **barra de estado** de la cabecera, el usuario puede encontrar la siguiente información:

- **Estado doc.**: estado del documento del albarán.
- **Estado de factura**: indica en % qué cantidad del albarán ha sido facturada.

**Una vez que la información de cabecera se ha cumplimentado correctamente, puede ir a la pestaña "Líneas" para introducir la/s "Línea/s de albarán (proveedor)"**.

!!! info
    Para aprender cómo introducir líneas de albarán, visite la siguiente sección [Líneas](goods-receipts.md#lines)

Si un **albarán (proveedor)** se completa y, por tanto, queda **contabilizado**:

- **La cantidad disponible del/de los artículo/s recibidos se incrementa** en la cantidad recibida.

Si un **albarán (proveedor) "Completada" se anula** porque las mercancías han sido devueltas al proveedor:

- **La cantidad disponible del/de los artículo/s devueltos se reduce** en la cantidad de mercancía devuelta. Etendo crea automáticamente un nuevo "albarán (proveedor)" para exactamente los mismos artículos pero con cantidades "negativas".

!!! info
    Para saber más sobre devoluciones de mercancía, visite *Devolución a proveedor* y *Envío de devolución a proveedor*.

El proveedor puede enviar una "Factura (Proveedor)" junto con las "Observaciones entrega" de las mercancías entregadas; por tanto:

- Desde la ventana de albarán (proveedor), es posible generar la factura del proveedor correspondiente utilizando el botón de proceso de cabecera "**Crear factura del albarán**".

Esta acción implica un **enlace entre el albarán (proveedor) y la factura (proveedor)**, de modo que el usuario puede conocerlo al consultar la factura (proveedor) correspondiente.

!!! info
    Para saber más, visite [Factura (Proveedor)](purchase-invoice.md).

## Líneas

Una vez que la cabecera del albarán (proveedor) se ha cumplimentado correctamente y guardado, cada artículo recibido puede listarse como una línea de albarán (proveedor) independiente.

Existen varias formas de crear líneas de albarán (proveedor).

1.**El usuario siempre puede crear manualmente líneas de albarán (proveedor).**  
Esta es la forma a la que el usuario podría recurrir en caso de que no exista un pedido de compra contabilizado ni una factura (proveedor) completada de la que recuperar datos para las mercancías recibidas.

Como consecuencia, la información a cumplimentar manualmente es:

- la mercancía o artículos recibidos
- la cantidad recibida
- el hueco donde se almacenarán los artículos

El botón **Explotar** se muestra al seleccionar una línea con un producto LdM (BOM) no almacenable y el producto no ha sido ya explotado. Al explotar un producto, los componentes de la lista de materiales de los que consta el producto seleccionado se muestran en el albarán. Una vez explotado, no puede comprimirse. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y después el producto LdM) e insertar de nuevo el producto LdM no almacenable.

2.Por otro lado, también es posible **crear "automáticamente" líneas de albarán (proveedor)** utilizando el botón de proceso de cabecera **"Crear líneas de"**.

Esto permite al usuario seleccionar los pedidos o facturas pendientes de recibir.

Por ejemplo, una vez seleccionado un pedido de compra, se muestran las líneas del pedido de compra pendientes de recibir.

Entonces, el usuario puede seleccionar las líneas de compra recibidas, cambiar la cantidad si es necesario y ubicarlas en el almacén.

Finalmente:

- Si se selecciona un pedido de compra/línea, esta acción **vincula cada línea de albarán (proveedor) con la línea de pedido de compra correspondiente**; lo mismo aplica a la factura (proveedor).

En la **barra de estado** de cada línea, puede encontrar información sobre la **Cant.facturada**, el número de productos facturados de la línea.

### Contabilidad

Información contable relacionada con la recepción de material.

Un **"Albaranes pendientes de recibir" puede contabilizarse** si la tabla "**MaterialMgmtShipmentInOut**" está configurada como Activa para contabilidad en la pestaña \[*Active Tables*\] de la configuración del libro mayor de la organización.

La contabilización de un "albarán (proveedor)" tiene este aspecto:

![Contabilización de albaranes](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/goodsreceipt3.png)

Contabilizar un "albarán (proveedor)" requiere el cálculo del coste del/de los producto/s incluidos.

En el caso de un albarán (proveedor), esto es:

- el precio de compra del/de los producto/s
- o el *coste estándar* por defecto del/de los producto/s en caso de calcular el coste usando un *algoritmo de costeo* estándar.

Si no existe un pedido de compra relacionado, el proceso Costing Server utiliza el más reciente de los siguientes tres valores:

- el último precio de pedido de compra del proveedor del albarán para el producto.
- la tarifa de compra del producto.
- o el *coste por defecto* del producto.

Además:

- La organización **Entidad Legal** debe tener una *Regla de Coste* validada configurada.
- Y el *Proceso en segundo plano de Coste* debe estar planificado para el *Cliente*, para que pueda buscar y permitir que el proceso *Costing Server* calcule el coste de las transacciones.

Una vez calculados los costes, el **albarán (proveedor) puede contabilizarse** en el libro mayor.

En el caso de un albarán que contenga productos de tipo **Gasto** sin la casilla **Ventas** seleccionada, es posible utilizar el precio de compra del producto en lugar del coste del producto para contabilizar el albarán.

Esto funciona si la casilla *Book Using Purchase Order Price* está seleccionada para el/los producto/s.

En este caso, es necesario que exista un **Pedido de compra** relacionado con el "albarán (proveedor)" contabilizado.

### Anulación

Es posible anular totalmente un albarán (proveedor) utilizando el botón de cabecera **"Close"** y después seleccionando la acción "**Anular**".

Esta acción crea un **nuevo documento** que **revierte el albarán (proveedor).**

La acción de anulación permite especificar una "**Void Date**" y una "**Void Accounting Date**" del nuevo documento:

- **Void Date**: es la fecha del movimiento del nuevo documento que revierte el albarán (proveedor).
- **Void Accounting Date**: es la fecha contable del nuevo documento que revierte el albarán (proveedor).

Ambos campos anteriores toman por defecto las fechas del documento original y validan que las fechas introducidas no sean anteriores a la "Fecha del movimiento" y a la "Fecha contable" del albarán (proveedor), respectivamente.

La acción de anulación implica que:

- Etendo genera automáticamente un **nuevo documento** en la ventana "albarán (proveedor)" e **informa del número de documento** creado. El número de documento también se muestra en el campo descripción del albarán (proveedor). Este nuevo documento se crea como se describe a continuación:
  - El "**Documento transacción**" utilizado por Etendo es "**MM Receipt**".
  - Este documento es **exactamente igual que el original** que se está revirtiendo, **pero la cantidad del movimiento es negativa.**
  - Una vez creado el **nuevo documento**, puede **Cambiar Estado** tanto la "**Fecha del movimiento**" como la "**Fecha contable**" del nuevo documento antes de contabilizarlo.

### Landed Cost

La pestaña Landed Cost permite asignar costes adicionales al albarán (proveedor).

![Ventana de Landed cost](../../../../../assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

Es posible introducir tantos tipos/líneas de landed cost como sea necesario.

Algunos campos relevantes a tener en cuenta son:

- **Tipo de Landed Cost**: es el tipo de landed cost que se va a asignar al albarán (proveedor).
- **Línea de la factura**: sirve para seleccionar la línea de factura de landed cost correspondiente, si existe, que coincida con el tipo de landed cost que se está introduciendo.  
  Si se selecciona una línea de factura, el importe de la línea de factura se rellena en el siguiente campo "Importe".
- **Importe**: es el importe del landed cost. Este importe puede ser una "estimación" o un importe de "Pago Real" en caso de seleccionar una línea de factura.
- **Algoritmo de Distribución de Landed Cost**: es el distribuido por Etendo "Distribution by Amount", lo que significa que el importe del landed cost se distribuirá entre las líneas del albarán (proveedor) proporcionalmente por el importe de la línea del albarán.

Una vez cumplimentados todos los elementos anteriores, incluida la línea de factura (proveedor) de landed cost correspondiente, se ejecutan tanto el proceso de "albarán (proveedor)" como el *process matching* de Landed Cost haciendo clic en el botón de proceso "**Completada**".

## Cómo reactivar albaranes pendientes de recibir

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Desde la ventana de albarán (proveedor), es posible reactivar un movimiento generado previamente simplemente seleccionando el documento correspondiente y haciendo clic en el botón Reactivate.

Una vez que el albarán se reactiva correctamente, el estado del documento cambia a Borrador, tal y como puede observarse en la barra de estado.

![](../../../../../assets/drive/1-Z-wUYZfcGDizQ_Kkp8TUYXTs-KnM67H.png)

!!! warning
    Nota: No es posible reactivar documentos que incluyan transacciones con cantidades que excedan la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando la configuración del hueco permite Over Issue. Para más información, visite [Hueco](../../warehouse-management/setup.md#storage-bin).

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado contable del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

## Bulk Completion

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Essential Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad Bulk Completion permite al usuario completar, reactivar o anular múltiples registros seleccionándolos y haciendo clic en el botón **Bulk Completion**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [the Bulk Completion module user guide](../../../optional-features/bundles/essentials-extensions/bulk-completion.md).

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.