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
- [Movimiento entre almacenes](../../../basic-features/warehouse-management/transactions.md#bulk-posting_1)
- [Cuenta financiera](../../../basic-features/financial-management/receivables-and-payables/transactions.md#bulk-posting_2)
- [Facturas cuadradas](../../../basic-features/procurement-management/transactions.md#bulk-posting_2)
- [Ajuste de Costes](../../../basic-features/warehouse-management/transactions.md#bulk-posting_3)
- [Producción LDM](../../../basic-features/warehouse-management/transactions.md#bulk-posting_2)
- [Consumo interno](../../../basic-features/production-management/transactions.md#bulk-posting_1)
- [Dudoso cobro](../../../basic-features/financial-management/receivables-and-payables/transactions.md#bulk-posting_3)
- [Landed Cost](../../../basic-features/procurement-management/transactions.md#bulk-posting_4)
- [Asientos manuales](../../../basic-features/financial-management/accounting/transactions.md#bulk-posting_1)
- [Asientos Manuales Simplificados](../../../basic-features/financial-management/accounting/transactions.md#bulk-posting)
- [Parte de Trabajo](../../../basic-features/production-management/transactions.md#bulk-posting)
- [Albarán (Proveedor)](../../../basic-features/procurement-management/transactions.md#bulk-posting)
- [Albarán (Cliente)](../../../basic-features/sales-management/transactions.md#bulk-posting)
- [Recibo devolución de material](../../../basic-features/sales-management/transactions.md#bulk-posting_1)
- [Devolución a albarán de proveedor](../../../basic-features/procurement-management/transactions.md#bulk-posting_3)
- [Factura (Cliente)](../../../basic-features/sales-management/transactions.md#bulk-posting_2)
- [Factura (Proveedor)](../../../basic-features/procurement-management/transactions.md#bulk-posting_1)
- [Cobros](../../../basic-features/financial-management/receivables-and-payables/transactions.md#bulk-posting_1)
- [Pago](../../../basic-features/financial-management/receivables-and-payables/transactions.md#bulk-posting)
- [Inventario físico](../../../basic-features/warehouse-management/transactions.md#bulk-posting)

### Columna Estado contable

Todos los registros existentes previamente a la instalación de esta nueva funcionalidad tienen un valor por defecto **pendiente de actualización** en la columna **Estado contable**. Para establecer el valor correcto para esta columna, es necesario configurar la siguiente preferencia para indicar la cantidad de días que debe considerar el proceso para establecer los valores correctos de los registros anteriores.

#### Configuración de preferencias

Para configurar la preferencia, vaya a la ventana **Preferencias** y cree un nuevo registro con la propiedad **Cantidad de días** y el valor por defecto **90**. Si fuera necesario, es posible crear otra preferencia introduciendo un nuevo valor y marcando la casilla **Seleccionado**.

#### Proceso en segundo plano

Es necesario ejecutar el proceso en segundo plano **Días anteriores para actualizar la contabilidad** para actualizar la columna de estado contable.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting/daysbacktorefreshaccounting.png)

## Ventana Documentos no contabilizados

El módulo de Contabilización masiva incluye la funcionalidad de Documentos no contabilizados. Esta se utiliza para encontrar todos los documentos no contabilizados en la misma ventana y contabilizarlos de forma masiva.

!!!info
    Para más información, visite la guía de usuario de [Documentos no contabilizados](../../../basic-features/financial-management/accounting/transactions.md#not-posted-documents).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.