---
Title: Ajustar Impuesto de Factura
Tags:
    - Ajustar importe
    - Impuesto
    - Redondeo
    - Ajustes
    - Factura
    - Factura (Proveedor)
    - Factura (Cliente)
    - Corrección de céntimos
---

# Ajustar Impuesto de Factura

:octicons-package-16: Javapackage: `com.etendoerp.adjust.invoice.tax`

## Visión general

Este módulo permite realizar ajustes controlados en los importes de impuestos de las facturas para conciliar pequeñas **diferencias de redondeo** con sistemas externos o cuando las facturas se presentan ante **entidades gubernamentales**. Es compatible tanto con facturas de **Ventas** como de **Compra**, ofrece **ajustes manuales y automatizados** para correcciones mínimas a nivel de céntimos y registra todos los cambios para garantizar la **auditabilidad**, asegurando que el total final de la factura coincida con requisitos externos, gubernamentales o regulatorios.

!!! info
    
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. 
    
    Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).
    
!!! example "Compatibilidad"
    Esta funcionalidad es compatible desde Etendo 23.


## Factura (Proveedor)

En la solapa **Impuesto**, Etendo agrupa una línea de impuesto por cada tipo de impuesto en la factura. Esta funcionalidad permite ajustar cada línea de impuesto hasta un céntimo (±0.01), modificando la diferencia de redondeo o el propio importe del impuesto, pero únicamente cuando la factura de compra se encuentra en estado Borrador.

El sistema aplica validaciones estrictas: el importe del impuesto no puede modificarse si el **Impuestos** calculado es cero, si la **Base Impuesto** es cero o si el ajuste supera el rango permitido de ±0.01. Estos controles garantizan que los ajustes sean mínimos, controlados y coherentes con los requisitos regulatorios.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/adjust-invoice-tax/adjust-purchase-invoice-tax.png)


## Factura (Cliente)

En la solapa **Impuesto**, Etendo agrupa una línea de impuesto por cada tipo de impuesto en la factura. Esta funcionalidad permite ajustar cada línea de impuesto hasta un céntimo (±0.01), modificando la diferencia de redondeo o el propio importe del impuesto, pero únicamente cuando la factura de ventas se encuentra en estado Borrador.

El sistema aplica validaciones estrictas: el importe del impuesto no puede modificarse si el **Impuestos** calculado es cero, si la **Base Impuesto** es cero o si el ajuste supera el rango permitido de ±0.01. Estos controles garantizan que los ajustes sean mínimos, controlados y coherentes con los requisitos regulatorios.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/adjust-invoice-tax/adjust-sales-invoice-tax.png)


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

---