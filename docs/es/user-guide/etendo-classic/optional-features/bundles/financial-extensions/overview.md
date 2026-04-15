---
title: Financial Extensions Bundle
tags:
 - Gestión Financiera
 - Funcionalidades de Etendo
 - Bancario
 - Mejoras Contables
 - Procesos Automatizados
---

:octicons-package-16: Javapackage: `com.etendoerp.financial.extensions`

:material-store: Etendo Marketplace:  [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}

## Resumen
Este paquete incluye mejoras para las funcionalidades de Gestión Financiera en Etendo.

## Traducciones
-  :material-translate: Español: [Financial Extensions Bundle ES](https://marketplace.etendo.cloud/#/product-details?module=0E104B3E36C84992BD7A6D941FBC7AB9){target="_blank"}
## Módulos

### Account Structure Validation

:octicons-package-16: Javapackage: `com.etendoerp.account.structure.validation`

Este módulo ayuda a prevenir errores comunes de configuración al crear o modificar subcuentas en el Árbol de Cuentas. Valida la estructura y la configuración para evitar desajustes en informes financieros como la Cuenta de Pérdidas y Ganancias o el Balance.

!!! info
    Para más información, visita [the Account Structure Validation Module user guide](../../../optional-features/bundles/financial-extensions/account-structure-validation.md).

### Accounting Dimensions Assets

:octicons-package-16: Javapackage: `com.etendoerp.accounting.dimensions.assets.template`

:octicons-package-16: Javapackage: `com.etendoerp.accounting.dimensions.assets`

<iframe width="560" height="315" src="https://www.youtube.com/embed/1a1UNCnNNcI?si=DbicgZnWjtmkScDh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

El módulo Accounting Dimensions Assets mejora la gestión de activos y la amortización al permitir al usuario especificar todas las **dimensiones contables disponibles** durante la creación y gestión de activos. Además, la ventana de Amortización garantiza un seguimiento más preciso de los activos **agrupado por períodos** y cálculos de amortización más completos.

!!! info
    Para más información, visita la [guía de usuario de Accounting Dimensions Assets](../../../basic-features/financial-management/assets/overview.md#accounting-dimensions-assets).


### Accounting Template Module

:octicons-package-16: Javapackage: `com.etendoerp.accounting.templates`

El módulo Accounting Template Module permite asignar un **importe de impuesto no deducible** a una cuenta financiera específica. Esta funcionalidad solo se aplica a **facturas de compra**. 

!!! info
    Para más información, visita la [guía de usuario de Accounting Template Module](./accounting-template-module.md).


### Adjust Invoice Tax

:octicons-package-16: Javapackage: `com.etendoerp.adjust.invoice.tax`

Esta extensión permite realizar ajustes controlados en los importes de impuestos de las facturas para reconciliar pequeñas **diferencias de redondeo** con sistemas externos; admite tanto facturas de **ventas** como de **compra**, ofrece **ajustes manuales y automáticos** para correcciones mínimas a nivel de céntimos, y registra todos los cambios para garantizar la **auditabilidad**, asegurando que el total final de la factura coincida con los requisitos externos o normativos.

!!! info
    Para más información, visita la [guía de usuario de Adjust Invoice Tax](./adjust-invoice-tax.md).


### Advanced Bank Account Management

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/7AtGyQ62FHs?si=HisPbmd0KzblSq0O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Este módulo mejora la gestión de cuentas bancarias, permitiendo una mayor personalización y control sobre la selección de cuentas bancarias asociadas a clientes y proveedores. Además, se añade el botón Modificar plan de pagos para una mejor gestión de pagos.

!!! info
    Esta funcionalidad está disponible en las siguientes ventanas:

    - [Tercero](../../../basic-features/master-data-management/master-data.md#advanced-bank-account-management_1)
    - [Factura (Cliente)](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management_1)
    - [Factura (Proveedor)](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management_1)
    - [Pedido de venta](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management)
    - [Pedido de compra](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management)
    - [Cobro](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management_1)
    - [Pago](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management)

    Para más información, visita [Advanced Bank Account Management](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).

### Advanced Financial Docs. Processing

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pnE-nePaTEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad forma parte de Financial Extensions Bundle y resulta útil cuando el usuario necesita reactivar facturas anuladas (ya sean de Ventas o de Compra) y pedidos cerrados (ya sean de Ventas o de Compra), así como amortizaciones.

!!! warning "Aviso de dependencia"
    Este módulo depende del módulo [**Bulk Completion**](../essentials-extensions/bulk-completion.md), ya que las acciones de procesamiento de **pedido** deben realizarse mediante procesos modernos que permitan la activación de Hooks, en lugar del procesamiento heredado. Debido a este requisito, las acciones heredadas de **cerrar/reactivar** para pedidos se ocultarán y estas acciones solo estarán disponibles a través del botón **Bulk Completion**.

!!! info
    Para más información, visita:

    - [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-closed-sales-order) 
    - [Factura (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-voided-sales-invoice)
    - [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-closed-purchase-order)
    - [Factura (Proveedor)](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-voided-purchase-invoice)
    - [Amortización](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#how-to-reactivate-amortizations)
    - y la [guía para desarrolladores de Advanced Financial Docs. Processing](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle/overview.md#advanced-financial-docs-processing)

### Asset Amortization Report

:octicons-package-16: Javapackage: `com.smf.asset.amortization.report`

El nuevo informe de Amortización permite descargar informes en Excel con información sobre la amortización creada para un año seleccionado.

!!! info
    Para más información, visita [la guía de usuario de Asset Amortization Report](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#asset-amortization-report-excel).

### Automated Remittance

:octicons-package-16: Javapackage: `com.etendoerp.automated.remittance`

Esta funcionalidad permite al usuario procesar y protestar remesas automáticamente.

!!! info
    Para más información, visita [la guía de usuario de Automated Remittance](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).

### Banking Pool

:octicons-package-16: Javapackage: `com.etendoerp.bankingpool`

<iframe width="560" height="315" src="https://www.youtube.com/embed/sdPnyewiPbc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite introducir en el sistema todas las financiaciones de las que dispone la empresa. Es posible explotar la información a través del informe de Banking Pool.

!!! info
    Para más información, visita [la guía de usuario de Banking Pool](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#financial-type-configuration) y la [guía para desarrolladores de Banking Pool](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle/overview.md#banking-pool).

### Bulk Posting

:octicons-package-16: Javapackage: `com.etendoerp.bulk.posting`

<iframe width="560" height="315" src="https://www.youtube.com/embed/mgE-NnDLlA0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario contabilizar o deshacer la contabilización de varios registros al mismo tiempo. También se incluye en este módulo la ventana **Documentos no contabilizados**, que permite a los usuarios identificar y contabilizar todas las transacciones pendientes directamente desde una sola ventana. 

!!! info
    Para más información, visita [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Business Partner Settlement

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bpsettlement`

:octicons-package-16: Javapackage: `org.openbravo.financial.bpsettlement`

<iframe width="560" height="315" src="https://www.youtube.com/embed/Gh6G1i3Iyts" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario crear liquidaciones para facturas, tanto de ventas como de compra, desde las ventanas Cobro y Pago. También se puede realizar una compensación creando una liquidación a partir de una conciliación bancaria para cobros/pagos desde la ventana Cuenta financiera.

!!! info
    Para más información, visita:

    - [Business Partner Settlement - User Guide](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).
    - [Cobro](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-1)
    - [Pago](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement)
    - [Cuenta financiera](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-2)

### Conversion Rate Downloader

:octicons-package-16: Javapackage: `com.smf.currency.conversionrate`

:octicons-package-16: Javapackage: `com.smf.currency.apiconfig`

Este proceso permite mantener actualizadas las conversiones de divisas generando automáticamente tipos de conversión mediante un proceso en segundo plano usando apilayer.

!!! info
    Para más información, visita la [guía de usuario de Conversion Rate Downloader](./conversion-rate-downloader.md).

### Deferred GL Journal

:octicons-package-16: Javapackage: `com.etendoerp.gljournal.advanced`

<iframe width="560" height="315" src="https://www.youtube.com/embed/K7XOBkmRLAQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario duplicar un asiento contable tantas veces como sea necesario, indicando la periodicidad y el período en el que debe realizarse la primera copia. Siga el proceso para crear un asiento contable desde el principio y duplicarlo más adelante.

!!! info
    Para más información, visita [la guía de usuario de Deferred GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#deferred-gl-journal).


### Financial Advanced Reports

:octicons-package-16: Javapackage: `com.etendoerp.financial.reports.advanced`

:octicons-package-16: Javapackage: `com.etendoerp.financial.reports.advanced.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Los informes **Cuadros plan general contable avanzado**, **Customer Statement**, **Libro mayor avanzado**, **Diario asientos avanzado**, **Análisis dimensional facturas compras** y **Balance sumas y saldos** son una versión mejorada de los informes anteriores e incluyen nuevos filtros según las dimensiones contables de los informes.

!!! info
    Para más información, visita:
    
    - [Cuadros plan general contable avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#balance-sheet-and-pl-structure-advanced) guía de usuario.
    - [Customer Statement](../../../basic-features/financial-management/accounting/analysis-tools.md#customer-statement) guía de usuario.
    - [Libro mayor avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#general-ledger-report-advanced) guía de usuario.
    - [Diario asientos avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#journal-entries-report-advanced) guía de usuario.
    - [Análisis dimensional facturas compras](../../../basic-features/procurement-management/analysis-tools.md#purchase-invoice-dimensional-report) guía de usuario.
    - [Balance sumas y saldos](../../../basic-features/financial-management/accounting/analysis-tools.md#trial-balance) guía de usuario.

### Financial Report Budget

:octicons-package-16: Javapackage: `com.etendoerp.financial.report.budget`

<iframe width="560" height="315" src="https://www.youtube.com/embed/2VFxpx8j8Sk?si=TuLZUdBGrOCSpXIE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta funcionalidad permite crear y gestionar presupuestos con fines de reporting, ofreciendo a los usuarios la posibilidad de comparar los valores presupuestados con los valores reales contabilizados en el Libro mayor correspondiente.

!!! info
    Para más información, visita la [guía de Financial Report Budget](../../../basic-features/financial-management/accounting/transactions.md#budget).

### G/L Journal Clone

:octicons-package-16: Javapackage: `com.etendoerp.gljournal.clone`

Esta funcionalidad permite al usuario clonar un diario contable en la ventana Diario simple, parte de las transacciones contables de la gestión financiera.

!!! info
    Para más información, visita la [guía de usuario de G/L Journal Clone](../../../basic-features/financial-management/accounting/transactions.md#gl-journal-clone).

### Intercompany

:octicons-package-16: Javapackage: `com.etendoerp.advanced.intercompany`

<iframe width="560" height="315" src="https://www.youtube.com/embed/bQjT7iPkYtQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones diferentes pero pertenecientes al mismo cliente, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visita [la guía de usuario del módulo Intercompany](../../../optional-features/bundles/financial-extensions/intercompany.md).

### Payment Removal

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal`

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/TLbjMLjGYwo?si=uGtWnNHNa7gV4_l5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

El objetivo de esta funcionalidad es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones y conciliaciones bancarias.

Los pagos que se pueden eliminar o reactivar pueden encontrarse en distintos estados: Pendiente de ejecución, Pago realizado, Pago recibido, Retirado no compensado, Depositado no compensado, Pago compensado (siempre que el pago haya sido conciliado por un método automático y no manual), Contabilizar y Descontabilizar.

El botón Eliminar pago está disponible en las ventanas Pedido de venta, Pedido de compra, Factura (Cliente), Factura (Proveedor), Cobro y Pago. Los botones Reactivar y Reactivación avanzada solo están disponibles en las ventanas Cobro y Pago. Por último, los botones Reactivar transacción, Eliminar transacción, Reactivar conciliación y Eliminar conciliación están disponibles en la ventana Cuenta financiera.


!!! info
    Para más información, visita:

    - [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal)
    - [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal)
    - [Factura (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal_1)
    - [Factura (Proveedor)](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal_1)
    - [Cobro](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_1)
    - [Pago](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal)
    - [Cuenta financiera](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_2)

### Remittances

:octicons-package-16: Javapackage: `org.openbravo.module.remittance`

:octicons-package-16: Javapackage: `org.openbravo.module.remittance.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/6z3t-E_sV0E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite crear una remesa, que es un grupo de "pagos" (entrada/salida) o "pedidos/facturas" que pueden remitirse al banco para su pago. El banco se encargará entonces de gestionar el cobro del dinero a los clientes o el pago a los proveedores/suministradores.

!!! info
    Para más información, visita [la guía de usuario de Remittances](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#remittance).


### Reverse GL Journal

:octicons-package-16: Javapackage: `com.smf.gljournal.reverse`

:octicons-package-16: Javapackage: `com.smf.gljournal.reverse.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pfqClq8HD6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad resulta especialmente útil para empresas que realizan un cierre mensual, en lugar de un cierre de fin de año, pero con pagos pendientes (de entrada o de salida). Permite al usuario abrir o cerrar el período sin tener en cuenta los pagos hasta que se realicen.

!!! info
    Para más información, visita la [guía de usuario de GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#gl-journal) y la [guía de usuario de Simple GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#simple-gl-journal).


### VAT Regularization 

:octicons-package-16: Javapackage: `com.etendoerp.vat.regularization`

<iframe width="560" height="315" src="https://www.youtube.com/embed/udarQ6h6EXQ?si=4CNi7Qgi2_yHdW5z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta funcionalidad permite al usuario ajustar cuentas, garantizando que el saldo del IVA sea correcto y esté debidamente alineado.

!!!info
    Para más información, visita la [Guía de usuario de VAT Regularization](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#vat-regularization).

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.