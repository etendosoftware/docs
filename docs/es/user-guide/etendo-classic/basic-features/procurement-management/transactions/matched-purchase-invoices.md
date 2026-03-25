---
title: Facturas cuadradas
tags:
    - Proceso de Compras
    - Pedidos de compra
---

# Facturas cuadradas

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Facturas cuadradas`

Esta ventana ayuda al usuario a contabilizar las discrepancias entre el inventario y la contabilidad financiera de aquellos artículos para los que se contabilizaron los correspondientes albaranes.

Las discrepancias mencionadas anteriormente se deben principalmente a diferencias entre:

- el **precio neto unitario del artículo registrado al contabilizar el pedido de compra** y posteriormente **al contabilizar el correspondiente Albarán.**
- y el **precio neto unitario "final" del artículo registrado al contabilizar la factura de compra.**

En la ventana, hay un listado de todas las facturas que están cuadradas con albaranes. El cuadre de los documentos se realiza cuando los documentos se crean utilizando la información del otro documento: por ejemplo, haciendo clic en Generar factura desde albarán en el albarán o haciendo clic en el botón Crear líneas desde al crear un albarán para seleccionar la factura.

![Ventana Facturas cuadradas](../../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/matched-purchase-invoices.png)

### Factura de compra cuadrada

La pestaña Factura de compra cuadrada lista cada línea de factura contabilizada vinculada a las correspondientes líneas de albarán, que también podrían estar contabilizadas o no.

Hay un botón de cabecera "**Post**" que es el que contabiliza las discrepancias entre inventario y contabilidad financiera, si las hubiera, una vez seleccionada la línea adecuada.

El proceso general para contabilizar las discrepancias en contabilidad se detalla a continuación:

Un documento *Matching Invoice* puede contabilizarse si se ha calculado el coste de los productos incluidos en un *Albarán*. Para obtenerlo:

- Se requiere una *Regla de Coste* validada en la entidad legal de la Factura Cuadrada,
- y debe ejecutarse el proceso en segundo plano *Costing Background Process*.

En el caso de productos de "Gasto" que no tengan seleccionada la casilla de verificación "Ventas", es posible utilizar el precio de compra del producto en lugar del coste del producto siempre que esté seleccionada la casilla *Book Using Purchase Order* Price. En este caso, es necesario que un "Pedido de compra" esté relacionado con el "Albarán".

### Contabilidad

Información contable relacionada con las facturas de compra cuadradas.

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización Masiva**.

Además, el Estado Contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de rejilla.

!!! info
    Para más información, visite [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.