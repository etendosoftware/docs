---
title: Devolución a proveedor
tags:
    - Proceso de Compras
---

# Devolución a proveedor (RTV)

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Devolución a proveedor`

Esta ventana permite al usuario crear un documento de Devolución de Material en caso de que un producto determinado deba enviarse de vuelta, ya sea para su devolución con reembolso o sustitución, o para ser reparado.

## Cabecera

El usuario puede crear una orden de compra y procesarla.

Una vez que el documento de Devolución de Material es aceptado por el proveedor, el usuario puede procesarlo haciendo clic en el botón **Book**. El documento cambia de *Borrador* a *Booked*.

![Ventana de devolución a proveedor](../../../../../assets/drive/1PKb2NIyq5HtvO_4abDPQjajObdcGFiPH.png)

Solo los documentos *Booked* pueden enviarse al proveedor.

!!! warning
    Ten en cuenta que el botón **Elegir/Editar líneas** desaparece cuando el documento de Devolución a proveedor está en estado *Booked*.

## Líneas

Añade productos para incluirlos en tu orden de compra. Cada producto se añade creando una línea.

La pestaña Líneas no es editable, ya que las líneas devueltas siempre provienen de líneas de recepción, para evitar:

- Ver valores positivos mientras son negativos en la BD.
- Introducir líneas que no estén vinculadas a las líneas de recepción originales.
- Editar atributos, productos, etc., y que los productos o atributos difieran de la línea de albarán.

Para introducir nuevas líneas debes hacer clic en el botón de proceso PICK/EDIT Lines.

**Aspectos a tener en cuenta:**

- Los únicos campos editables son:
  - **Devuelto**: cantidad que deseas devolver. Al seleccionar la fila, la cantidad no se establece por defecto ya que el sistema no puede saber cuántos artículos se devuelven.
  - **Precio unitario**: precio de la orden de compra original.
  - **Motivos de devolución**: el motivo por el que devuelves el artículo.
  - y **Unidad de Devolución**, solo en caso de que esté habilitada la preferencia de \*unidad de medida alternativa (AUM)*.
    En ese caso, se muestra la AUM "primary" del producto para el flujo de compra si existe; en caso contrario, se muestra la UdM del producto. El usuario siempre puede cambiarla a la UdM del producto.

Puedes definir el Motivo de devolución a nivel de cabecera. En este caso, al elegir una línea hereda lo seleccionado en la cabecera, pero puedes modificarlo como desees.

- Solo se pueden seleccionar documentos de recepción de material que aún no hayan sido devueltos; en caso de que una línea de recepción se haya devuelto completamente, no se mostrará.
- Cuando una línea de recepción se ha devuelto parcialmente, aún puedes devolver el resto. Lo que ya has devuelto para esa línea se muestra en el campo **Return Qty other R.**

**Validaciones:**

- No está permitido devolver una cantidad mayor que la **Ship/Receipt Qty**. En caso de hacerlo, se muestra un mensaje.
- Ten en cuenta que esta validación tiene en cuenta el campo **Return Qty other RM**

!!! info
    Para editar una línea debes volver a hacer clic en el botón **Elegir/Editar líneas**; la línea aparecerá seleccionada y entonces podrás modificar cualquiera de los campos editables.

!!! info
    Para eliminar una línea debes desmarcar la línea y luego hacer clic en Done.

## Bulk Completion

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, sigue las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visita [Essential Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad Bulk Completion permite al usuario completar, reactivar o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Bulk Completion**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visita [the Bulk Completion module user guide](../../../optional-features/bundles/essentials-extensions/bulk-completion.md).

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.

---