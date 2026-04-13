---
title: Devolución a albarán de proveedor
tags:
    - Proceso de Compras
---

# Devolución a albarán de proveedor

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Devolución a albarán de proveedor`

Desde esta ventana, el usuario puede entregar al proveedor los bienes devueltos.

## Cabecera

El usuario puede crear y editar un albarán de entrada.

El campo **Referencia de devolución de material de proveedor** se completa automáticamente o no en función de:

- Si se rellena antes de seleccionar una línea, entonces no se completará automáticamente para evitar sobrescribirlo.
- Si selecciona una/s línea/s donde todas pertenecen al mismo documento de Devolución a proveedor, se completará automáticamente.
- Si selecciona una/s línea/s pero alguna de ellas pertenece a un documento de Devolución a proveedor diferente, entonces no se completará automáticamente.

Una vez que el documento está listo, puede procesarlo haciendo clic en el botón **Completada**. El documento cambia de *Borrador* a *Completado*.

!!! warning
    Tenga en cuenta que el botón **Elegir/Editar líneas** desaparece cuando el documento de Devolución a proveedor está en estado *Completado*.

![Devolución a albarán de proveedor](../../../../../assets/drive/1wuiYHH8xsIwjLRgp0VzWUqAtev43BzD8.png)

Para facturar estos documentos debe usar la ventana **Factura de compra**. Se cubren todos los escenarios:

- Si el proveedor envía una factura solo para ese documento específico, necesita seleccionar un tipo de documento *Factura de compra inversa* y luego seleccionar las líneas mediante el botón *Crear líneas*.
- Si el proveedor envía una factura con el pedido de compra original más el pedido de devolución de materiales, necesita seleccionar un tipo de documento *Factura de compra* y luego seleccionar las líneas mediante el botón *Crear líneas*.
- Si el proveedor no envía una factura por el pedido de devolución de materiales pero quiere mantenerlo como crédito para poder usarlo más adelante, tiene que:
  - Crear una *Factura de compra inversa* para estos materiales devueltos.
  - Dejarlo como crédito para usarlo más adelante mediante la ventana **Pago**.
  - Cuando cree la Factura de compra para el Pedido de compra original, puede consumir ese crédito.

## Líneas

Añada productos que estén incluidos en su albarán de entrada. Cada producto se muestra en su propia línea.

La pestaña Líneas no es editable, ya que las líneas siempre provienen de las líneas de devolución a proveedor, para evitar:

- Ver valores positivos mientras que en la BD son negativos.
- Introducir líneas que no estén vinculadas a líneas de devolución.
- Editar atributos, productos y, por tanto, tener productos o atributos diferentes a los de la línea de devolución.

!!! info
    Para introducir nuevas líneas, el usuario debe hacer clic en el botón ELEGIR/EDITAR Líneas.

**Aspectos a tener en cuenta:**

- Los campos editables son:
  - **Enviar cantidad**, ese valor se establece automáticamente cuando selecciona la línea,
  - y **Unidad de Devolución**, solo en caso de que esté habilitada la preferencia de unidad de medida alternativa (AUM); independientemente de ello, la UdM del producto siempre se muestra ahí por defecto.
    El usuario puede cambiarla si es necesario, a la AUM principal del producto configurada para el flujo de compras.
- El usuario solo puede seleccionar líneas de Devolución a proveedor que estén pendientes de ser enviadas a ese proveedor específico.
- El sistema propone los diferentes ubicaciones de almacén desde donde se puede recoger el artículo. Dependiendo de cómo esté configurado el producto, podríamos tener tres escenarios:
  - Producto con un atributo de instancia (p. ej.: número de serie): el sistema propondrá solo una ubicación, tal y como se muestra arriba.
  - Producto con un atributo no de instancia (p. ej.: color): el sistema podría proponer varias ubicaciones. Véase la imagen inferior.
  - Producto sin atributos. Similar al segundo escenario.

**Validaciones:**

- No está permitido enviar más que la **Cantidad disponible**.
- No está permitido enviar más que la cantidad **Pendiente**.
- El sistema también valida que no puede enviar más que la cantidad **Pendiente** al seleccionar ambas líneas.

!!! info
    Para editar una línea, debe hacer clic de nuevo en el botón **Elegir/Editar líneas**; la línea aparece seleccionada y entonces puede modificar cualquiera de los campos editables.

!!! info
    Para eliminar una línea, debe desmarcar la línea y luego hacer clic en Hecho.

Si no hay suficiente stock disponible para un producto en una línea seleccionada, entonces será posible definir una Cantidad a enviar y seleccionarla, si existe al menos una ubicación con estado de inventario de sobreemisión para el almacén de la Devolución a albarán de proveedor; en este caso, la nueva línea la usará como ubicación y creará un stock negativo cuando se procese el documento.

### Contabilidad

El albarán de devolución a proveedor puede contabilizarse **si la tabla "MaterialMgmtShipmentInOut" está** activa para contabilidad **en la configuración correspondiente del libro mayor.**

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización Masiva**.

Además, el Estado de Contabilidad del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo de Contabilización Masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo"){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.

---

---