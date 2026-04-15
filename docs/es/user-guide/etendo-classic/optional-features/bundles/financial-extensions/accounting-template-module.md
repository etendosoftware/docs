---
title: Módulo de plantilla contable
tags:
    - Impuesto no deducible
    - Factura de compra
    - Contabilidad
    - Tipo de impuesto
    - Gestión financiera
---

# Módulo de plantilla contable

:octicons-package-16: Javapackage: `com.etendoerp.accounting.templates`

## Resumen

Esta sección describe el Módulo de plantilla contable incluido en el paquete Financial Extensions de Etendo.

!!! info
    Para poder usar la funcionalidad descrita a continuación, el paquete Financial Extensions debe estar instalado. Para ello, siga las instrucciones en marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con core y las nuevas funcionalidades, visite [Financial Extensions - Release notes](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).  

El Módulo de plantilla contable permite asignar el **importe del impuesto no deducible** a una **cuenta financiera específica**.

De forma predeterminada, cuando se aplica un impuesto no deducible, Etendo contabiliza el importe del impuesto en la cuenta de gasto definida en la solapa Contabilidad del producto, tratando el impuesto como parte del coste del producto. Aunque este comportamiento es adecuado en muchos escenarios, puede limitar la capacidad de distinguir claramente entre los gastos del producto y los gastos relacionados con impuestos.

Este módulo introduce la posibilidad de contabilizar el importe del impuesto no deducible en una **cuenta financiera específica** configurada directamente en el Tipo de impuesto, en lugar de en la cuenta de gasto del producto.

Para habilitar este comportamiento, debe activarse la casilla **Use the configured account** en la solapa Contabilidad de la ventana Tipo de impuesto. Cuando está habilitada, el sistema contabiliza el **importe del impuesto no deducible** en la cuenta definida en la configuración del impuesto.

!!!note
    Esta funcionalidad se aplica solo a las **facturas cuadradas**.



## Configuración inicial

:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Ventanas, solapas y campos` 

Para asignar un impuesto no deducible a una cuenta financiera específica, hay una configuración preliminar que debe realizarse bajo el **rol System Administrator**.

Como System Admin, vaya a **Ventanas, solapas y campos** y, en la ventana Configuración del libro mayor, en la solapa Tablas activas, establezca el campo Plantilla contable como **Yes**. Esto permite que más adelante se pueda definir la plantilla contable necesaria desde la ventana Configuración del libro mayor.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/accounting-template-module/accounting-template-module1.png)

## Configuración GL

El **campo Plantilla contable** de la solapa Tabla activa de la ventana Configuración del libro mayor debe activarse y, a continuación, establecer la plantilla llamada **Purchase Invoice Not Deductible**.

Por último, la casilla **Use the configured account** debe marcarse en la ventana Tipo de impuesto. Solo será visible si previamente se ha marcado la casilla bajo el encabezado **Non-deductible tax**. El valor predeterminado de esta casilla será NO.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/accounting-template-module/accounting-template-module-3.png)

## Ejemplo

![Captura de pantalla de ejemplo del módulo de plantilla contable 1](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/accounting-template-module/accounting-template-module2.png)

![Captura de pantalla de ejemplo del módulo de plantilla contable 2](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/accounting-template-module/accounting-template-module3.png)

El importe del IVA debe contabilizarse en el libro mayor en una cuenta de crédito de impuestos; por lo tanto, la contabilización de la factura de compra tiene este aspecto:

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Debe | Haber | Comentarios |
| Gasto de producto | Importe neto de línea |     | Uno por línea de factura |
| Crédito de impuestos | Importe del impuesto |     | Uno por línea de impuesto |
| Deuda con proveedor |     | Importe bruto total | Uno por factura |


---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.