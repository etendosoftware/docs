---
tags:
- Contabilización masiva
- Contabilidad
- Financiero
---

# Contabilización masiva
:octicons-package-16: Paquete Java: `com.etendoerp.bulk.posting` 

## Visión general
Esta sección describe el módulo de Contabilización masiva incluido en el bundle Financial Extensions de Etendo.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning
    Antes de utilizar esta funcionalidad, recuerde que el proceso en segundo plano de este módulo puede afectar al rendimiento del sistema.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**. Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

![](../../../../../assets/drive/17KafE0qvtuAe21aVvs7mDN58V_BCDScO.png)

## Ventanas disponibles

Esta funcionalidad está disponible en las siguientes ventanas:

- [Amortización](../../../basic-features/financial-management/assets/overview.md#bulk-posting)
- [Movimiento entre almacenes](../../../basic-features/warehouse-management/transactions/purchase-invoice.md)
- [Cuenta financiera](../../../basic-features/financial-management/receivables-and-payables/transactions/matched-purchase-invoices.md)
- [Facturas cuadradas](../../../basic-features/procurement-management/transactions/matched-purchase-invoices.md)
- [Ajuste de Costes](../../../basic-features/warehouse-management/transactions/return-to-vendor-shipment.md)
- [Producción LDM](../../../basic-features/warehouse-management/transactions/matched-purchase-invoices.md)
- [Consumo interno](../../../basic-features/production-management/transactions/purchase-invoice.md)
- [Dudoso cobro](../../../basic-features/financial-management/receivables-and-payables/transactions/return-to-vendor-shipment.md)
- [Landed Cost](../../../basic-features/procurement-management/transactions/landed-cost.md)
- [Asientos manuales](../../../basic-features/financial-management/accounting/transactions/purchase-invoice.md)
- [Asientos Manuales Simplificados](../../../basic-features/financial-management/accounting/transactions/goods-receipt.md)
- [Parte de Trabajo](../../../basic-features/production-management/transactions/goods-receipt.md)
- [Albarán (Proveedor)](../../../basic-features/procurement-management/transactions/goods-receipt.md)
- [Albarán (Cliente)](../../../basic-features/sales-management/transactions/goods-receipt.md)
- [Recibo devolución de material](../../../basic-features/sales-management/transactions/purchase-invoice.md)
- [Devolución a albarán de proveedor](../../../basic-features/procurement-management/transactions/return-to-vendor-shipment.md)
- [Factura (Cliente)](../../../basic-features/sales-management/transactions/matched-purchase-invoices.md)
- [Factura (Proveedor)](../../../basic-features/procurement-management/transactions/purchase-invoice.md)
- [Cobros](../../../basic-features/financial-management/receivables-and-payables/transactions/purchase-invoice.md)
- [Pago](../../../basic-features/financial-management/receivables-and-payables/transactions/goods-receipt.md)
- [Inventario físico](../../../basic-features/warehouse-management/transactions/goods-receipt.md)

### Columna Estado contable

Todos los registros existentes previamente a la instalación de esta nueva funcionalidad tienen un valor por defecto **pending refresh** en la columna **Estado contable**. Para establecer el valor correcto para esta columna, es necesario configurar la siguiente preferencia para indicar la cantidad de días que debe considerar el proceso para establecer los valores correctos de los registros anteriores.

#### Configuración de preferencias

Para configurar la preferencia, vaya a la ventana **Preferencias** y cree un nuevo registro con la propiedad **Amount of Days** y el valor por defecto **90**. Si fuera necesario, es posible crear otra preferencia introduciendo un nuevo valor y marcando la casilla **Seleccionado**.

#### Proceso en segundo plano

Es necesario ejecutar el proceso en segundo plano **Days Back to Refresh Accounting** para actualizar la columna de estado contable.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting/daysbacktorefreshaccounting.png)

## Not Posted Documents Window

El módulo de Contabilización masiva incluye la funcionalidad de Documentos no contabilizados. Esta se utiliza para encontrar todos los documentos no contabilizados en la misma ventana y contabilizarlos de forma masiva.

!!!info
    Para más información, visite la guía de usuario de [Documentos no contabilizados](../../../basic-features/financial-management/accounting/transactions.md#not-posted-documents).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

---

---