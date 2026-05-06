---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - Not Posted Documents
  - Bulk Posting
---

# Documentos No Contabilizados

:material-menu: `Application` > `Financial Management` > `Accounting` > `Transactions` > `Not Posted Documents`

!!!info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Visión General

La ventana Documentos No Contabilizados, parte del módulo Contabilización Masiva, centraliza todos los documentos no contabilizados en un único lugar. Permite a los usuarios encontrar, revisar y contabilizar múltiples documentos a la vez de forma rápida. Los filtros ayudan a refinar las búsquedas y las acciones de contabilización masiva agilizan el procesamiento, haciendo la gestión de documentos más eficiente.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/not-posted-docs/not-posted-window-1.png)

## Filtros

- **Organización**: filtra los documentos según la organización a la que pertenecen. Por defecto se establece la organización de la sesión.

- **Documento**: (opcional) tipo de documento que el usuario está buscando. Las opciones disponibles son:

    - Amortización
    - Extractos Bancarios
    - Producción de Lista de Materiales
    - Ajuste de Coste
    - Deuda Dudosa
    - Asiento de Diario
    - Recepción de Mercancías
    - Envío de Mercancías
    - Consumo Interno
    - Inventario
    - Coste de Aterrizaje
    - Coste de Coste de Aterrizaje
    - Facturas de Compra Emparejadas
    - Movimientos
    - Cobro
    - Pago
    - Factura (Proveedor)
    - Conciliación
    - Recepción de Devolución de Material
    - Envío de Devolución a Proveedor
    - Factura (Cliente)
    - Transacción
    - Esfuerzo de Trabajo

- **Estado de Contabilización**: (obligatorio) muestra los posibles estados de los documentos contables. Permite selecciones múltiples. Esto es útil en casos en que el documento ya intentó contabilizarse pero falló y su estado no es **Sin Contabilizar** sino otro, como **Deshabilitado para Contabilización**.

- **Fecha Contable (Desde/Hasta)**: filtros para definir un período de búsqueda.

## Botones

### Botón Buscar

Al hacer clic en el botón Buscar se aplican los filtros seleccionados y se muestran los documentos coincidentes en la grilla de resultados. Desde los resultados se puede navegar a un documento haciendo clic en su Fecha Contable, inspeccionar detalles y seleccionar registros para la contabilización masiva.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/not-posted-docs/not-posted-window-2.png)

### Botón Contabilización Masiva

Una vez utilizados los campos para buscar los documentos no contabilizados, el usuario puede seleccionar masivamente los documentos necesarios y utilizar el botón **Contabilización Masiva** para contabilizar múltiples documentos a la vez, como se muestra a continuación.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/not-posted-docs/not-posted-bulk-posting-1.png)
![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/not-posted-docs/not-posted-bulk-posting-2.png)

Como puede observarse, este desarrollo facilita enormemente la gestión de los documentos a contabilizar, permitiendo a los usuarios no solo identificarlos rápidamente, sino también contabilizarlos de forma masiva y organizada directamente desde una única interfaz.

!!! info
    Para más información sobre la funcionalidad de Contabilización Masiva, visite [la guía del usuario de Contabilización Masiva](../../../optional-features/bundles/financial-extensions/bulk-posting.md).

## Filtrado en la grilla

En la grilla donde se muestran los documentos tras la búsqueda, los usuarios pueden filtrarlos usando los siguientes criterios:

- Organización
- Tipo de documento
- Descripción del documento
- Fecha Contable

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
