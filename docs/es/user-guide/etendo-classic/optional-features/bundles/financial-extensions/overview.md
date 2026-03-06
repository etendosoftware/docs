---
title: Financial Extensions Bundle
tags:
 - Gestión Financiera
 - Funcionalidades de Etendo
 - Banca
 - Mejoras contables
 - Procesos automatizados
 - Integración bancaria
 - Salt Edge
 - Open Banking
 - Cuenta financiera
---

:octicons-package-16: Javapackage: `com.etendoerp.financial.extensions`

:material-store: Etendo Marketplace:  [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}

## Visión general
Este bundle incluye mejoras para las funcionalidades de Gestión Financiera en Etendo.

## Traducciones
-  :material-translate: Español: [Financial Extensions Bundle ES](https://marketplace.etendo.cloud/#/product-details?module=0E104B3E36C84992BD7A6D941FBC7AB9){target="_blank"}

## Módulos

### Accounting Dimensions Assets

:octicons-package-16: Javapackage: `com.etendoerp.accounting.dimensions.assets.template`

:octicons-package-16: Javapackage: `com.etendoerp.accounting.dimensions.assets`

<iframe width="560" height="315" src="https://www.youtube.com/embed/1a1UNCnNNcI?si=DbicgZnWjtmkScDh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

El módulo Accounting Dimensions Assets mejora la gestión de activos y la amortización, permitiendo al usuario especificar todas las **dimensiones contables disponibles** durante la creación y gestión del activo. Además, la ventana Amortización garantiza un seguimiento más preciso de los activos **agrupado por periodos** y cálculos de amortización más completos.

!!! info
    Para más información, visita la [guía de usuario de Accounting Dimensions Assets](../../../basic-features/financial-management/assets/overview.md#accounting-dimensions-assets).


### Plantillas de Contabilidad

:octicons-package-16: Javapackage: `com.etendoerp.accounting.templates`

Este módulo permite establecer el importe de un impuesto no deducible en una cuenta financiera especificada.

!!! info
    Para más información, visita la [guía de usuario de Plantillas de Contabilidad](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/tax-rate.md#purchase-invoice-which-includes-not-deductible-tax-amount).


### Ajustar impuesto de factura
:octicons-package-16: Javapackage: `com.etendoerp.adjust.invoice.tax`


Esta extensión permite ajustes controlados en los importes de impuestos de las facturas para conciliar pequeñas **diferencias de redondeo** con sistemas externos; es compatible con facturas de **ventas** y de **compra**, ofrece **ajustes manuales y automatizados** para correcciones mínimas a nivel de céntimos y registra todos los cambios para garantizar la **auditabilidad**, asegurando que el total final de la factura coincida con los requisitos externos o regulatorios.

!!! info
    Para más información, visita la [guía de usuario de Ajustar impuesto de factura](./adjust-invoice-tax.md).


### Advanced Bank Account Management

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/7AtGyQ62FHs?si=HisPbmd0KzblSq0O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Este módulo mejora la gestión de cuentas bancarias, permitiendo una mayor personalización y control sobre la selección de la cuenta bancaria asociada a clientes y proveedores. Además, se añade el botón Modify Payment Plan para una mejor gestión de pagos.

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


### Liquidaciones de Terceros

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bpsettlement`

:octicons-package-16: Javapackage: `org.openbravo.financial.bpsettlement`

<iframe width="560" height="315" src="https://www.youtube.com/embed/Gh6G1i3Iyts" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario crear liquidaciones para facturas, tanto de venta como de compra, desde las ventanas Cobros y Pago. Además, se puede realizar una compensación creando una liquidación desde una conciliación bancaria para abonos/cargos desde la ventana Cuenta financiera.

!!! info
    Para más información, visita:

    - [Liquidaciones de Terceros - Guía de usuario](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).
    - [Cobros](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-1)
    - [Pago](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement)
    - [Cuenta financiera](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-2)

### Advanced Financial Docs. Processing

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pnE-nePaTEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad forma parte del Financial Extensions Bundle y es útil cuando el usuario necesita reactivar facturas anuladas (tanto de Venta como de Compra) y pedidos cerrados (tanto de Venta como de Compra), así como amortizaciones.

!!! warning "Aviso de dependencia"
    Este módulo depende del módulo [**Bulk Completion**](../../optional-features/bundles/essentials-extensions/bulk-completion.md), ya que las acciones de procesamiento de **pedido** deben realizarse usando procesos modernos que permitan el disparo de Hooks, en lugar del procesamiento legacy. Debido a este requisito, las acciones legacy de **cerrar/reactivar** para pedidos se ocultarán y estas acciones solo estarán disponibles mediante el botón **Bulk Completion**.

!!! info
    Para más información, visita:

    - [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-closed-sales-order) 
    - [Factura (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-voided-sales-invoice)
    - [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-closed-purchase-order)
    - [Factura (Proveedor)](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-voided-purchase-invoice)
    - [Amortización](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#how-to-reactivate-amortizations)
    - y la [guía de desarrollador de Advanced Financial Docs. Processing](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle.md#advanced-financial-docs-processing)

### Informe de Activos - Amortización

:octicons-package-16: Javapackage: `com.smf.asset.amortization.report`

El nuevo informe de Amortización permite descargar informes en Excel con información sobre la amortización creada para un año seleccionado.

!!! info
    Para más información, visita la [guía de usuario del Informe de Activos - Amortización](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#asset-amortization-report-excel).

### Automated Remittance

:octicons-package-16: Javapackage: `com.etendoerp.automated.remittance`

Esta funcionalidad permite al usuario procesar y protestar remesas automáticamente.

!!! info
    Para más información, visita la [guía de usuario de Automated Remittance](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).

# Visión general de la integración bancaria

:octicons-package-16: Javapackage: `com.etendoerp.psd2.bank.integration`

## Introducción

El módulo de Integración bancaria proporciona **integración bancaria automática** para Etendo ERP mediante dos capacidades principales:

- **AIS (Account Information Service)**: conecta de forma segura tus cuentas bancarias y descarga automáticamente las transacciones bancarias.
- **PIS (Payment Initiation Service)**: inicia pagos bancarios directamente desde Etendo, con la autorización gestionada de forma segura a través de tu banco.

La integración está impulsada por [Salt Edge](https://www.saltedge.com/){target="_blank"}, una plataforma líder de Open Banking que proporciona acceso seguro a miles de bancos en todo el mundo, y utiliza un **middleware centralizado** desarrollado por Etendo que gestiona toda la comunicación, la seguridad y el cumplimiento.

## Arquitectura

La integración utiliza una **arquitectura de tres capas**:

1. **Etendo ERP**: interfaz de usuario y lógica de negocio
2. **Etendo Middleware**: capa de integración centralizada (gestionada por Futit Services)
3. **Plataforma Salt Edge**: conectividad Open Banking con bancos

```
┌─────────────────┐
│   Etendo ERP    │
│ (Capa de usuario)│
└────────┬────────┘
         │
         │ Llamadas API
         ▼
┌─────────────────┐
│   Middleware    │
│ (Capa de seguridad)│
└────────┬────────┘
         │
         │ API de Salt Edge
         ▼
┌─────────────────┐
│   Salt Edge     │
│ (Open Banking)  │
└────────┬────────┘
         │
         │ APIs bancarias
         ▼
┌─────────────────┐
│ Bancos / ASPSPs │
└─────────────────┘
```

### Beneficios de esta arquitectura

- **Separación de responsabilidades**: Etendo se centra en la funcionalidad del ERP mientras que el middleware gestiona la complejidad de la integración
- **Seguridad**: las credenciales y certificados sensibles se gestionan a nivel de middleware
- **Escalabilidad**: múltiples instancias de Etendo pueden compartir el mismo middleware
- **Mantenibilidad**: los cambios en las APIs bancarias se gestionan de forma centralizada sin afectar a las instancias de Etendo
- **Cumplimiento**: los requisitos de PSD2 y Open Banking se cumplen a nivel de middleware

## Funcionalidades clave

### Información de cuenta (AIS)

- **Importación automática de transacciones**: descarga transacciones directamente desde las cuentas bancarias — sin necesidad de subir manualmente ficheros de extractos bancarios
- **Rangos de fechas configurables**: controla hasta qué fecha atrás deben recuperarse las transacciones en la configuración inicial
- **Prevención de duplicados**: filtra automáticamente transacciones duplicadas usando los IDs de transacción de Salt Edge
- **Agrupación de extractos**: configura cómo se agrupan las transacciones en extractos bancarios (por ejecución, por semana o por mes)
- **Procesamiento programado**: proceso en segundo plano para la importación automática en todas las cuentas conectadas

### Gestión de conexiones bancarias

- **Autenticación segura**: las credenciales bancarias se introducen directamente en la web del banco mediante el widget de Salt Edge — nunca se almacenan en Etendo
- **Miles de bancos**: soporte para bancos de todo el mundo a través de Salt Edge
- **Ciclo de vida de la conexión**: monitoriza, sincroniza, reconecta y desconecta conexiones bancarias desde Etendo
- **Sincronización automática de cuentas**: las cuentas bancarias se recuperan automáticamente cuando se establece una conexión

### Iniciación de pagos (PIS)

- **Pagos bancarios directos**: inicia pagos desde registros de Pago sin salir del ERP
- **Soporte multi-plantilla**: plantillas de pago SEPA (EUR), FPS (GBP) y DOMESTIC — seleccionadas automáticamente según la divisa
- **Autorización bancaria**: autorización segura del pago a través de la propia página de autenticación del banco
- **Seguimiento de estado en tiempo real**: monitoriza el progreso del pago desde la iniciación hasta la ejecución
- **Actualizaciones automáticas de estado**: recibe actualizaciones del estado del pago mediante webhooks y un proceso de refresco programado preconfigurado
- **Gestión de proveedores bancarios**: mantén una lista actualizada de bancos que soportan iniciación de pagos

### Monitorización y logs

- **Ventana PSD2 Logs**: vista centralizada de toda la actividad de integración y logs de error
- **Entradas de log detalladas**: cada log incluye cuenta financiera, fecha de ejecución, estado, origen, descripción y respuesta API en bruto
- **Ventana Bank Provider**: visualiza y gestiona la lista de proveedores bancarios disponibles

## Flujo de trabajo del usuario

### AIS (Información de cuenta)

1. **Configuración**:
    - El administrador obtiene la Salt Edge API Key de Futit Services
    - El usuario configura la API Key en su perfil (campo **PSD2 API Key**)
    - Las cuentas financieras se configuran con rangos de fechas de importación, proveedor bancario y frecuencia de extractos

2. **Conexión**:
    - El usuario hace clic en **Connect Bank Account** en la Cuenta financiera
    - Se abre el widget de Salt Edge para la selección del banco y la autenticación
    - El usuario se autentica con sus credenciales bancarias (introducidas en la propia web del banco)
    - Se establece la conexión y las cuentas bancarias se sincronizan automáticamente

3. **Importación de transacciones**:
    - **Manual**: el usuario hace clic en **Get Bank Statement** en la Cuenta financiera
    - **Automática**: programa el proceso **Get Bank Statements** para que se ejecute periódicamente
    - Se importan las transacciones y se crean automáticamente los extractos bancarios

4. **Uso continuado**:
    - El proceso programado importa transacciones automáticamente
    - El usuario concilia las transacciones importadas usando las funcionalidades de conciliación de Etendo
    - Las conexiones se renuevan mediante **Reconnect Connection** cuando caducan

### PIS (Iniciación de pagos)

1. **Configuración**:
    - Ejecuta el proceso **Synchronize Bank Providers** para poblar la lista de proveedores
    - Opcionalmente asigna un **Bank Provider** a cada cuenta financiera

2. **Pago**:
    - El usuario crea un registro de **Payment OUT** como de costumbre
    - Hace clic en **Generate Bank Payment** — aparece un formulario con valores precargados
    - Revisa y confirma — se abre un popup de autorización bancaria
    - El usuario autoriza el pago en el entorno seguro de su banco

3. **Seguimiento**:
    - El estado del pago se actualiza automáticamente mediante webhooks
    - Un proceso preconfigurado **Refresh Pending Payments** se ejecuta cada 10 minutos como red de seguridad
    - El usuario también puede refrescar el estado manualmente desde la pestaña **Bank Payments**

## Seguridad y privacidad

- **Sin almacenamiento de credenciales**: las credenciales bancarias nunca se almacenan en Etendo ni en el middleware — los usuarios se autentican directamente con su banco
- **Seguridad de la API Key**: cada usuario tiene su propia API Key para el acceso al middleware
- **Comunicación cifrada**: toda la transmisión de datos está cifrada
- **Registro de auditoría**: todas las operaciones se registran en la ventana **PSD2 Logs** para cumplimiento y resolución de incidencias

## Cumplimiento PSD2

El módulo utiliza Salt Edge, que cumple con PSD2, y soporta los siguientes estándares de Open Banking:

- **Account Information Services (AIS)**: acceso de lectura a datos y transacciones de la cuenta
- **Payment Initiation Services (PIS)**: iniciación de pagos a través del banco
- **Strong Customer Authentication (SCA)**: autenticación a nivel bancario tanto para conexiones como para pagos
- **Ciclo de vida de la conexión**: caducidad del consentimiento, renovación y reconexión
## Requisitos previos

Para utilizar este módulo, necesitas:

1. **Financial Extensions Bundle** instalado en Etendo
2. **Salt Edge API Key** proporcionada por Futit Services
3. **Cuentas financieras** creadas en Etendo
4. **Permisos de usuario** para acceder a Gestión Financiera

!!!info
    Para obtener instrucciones detalladas de configuración y uso, visita la [Guía de Usuario de Integración Bancaria](ser-guide-bank-integration.md).

### Banking Pool

:octicons-package-16: Javapackage: `com.etendoerp.bankingpool`

<iframe width="560" height="315" src="https://www.youtube.com/embed/sdPnyewiPbc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite introducir en el sistema todas las financiaciones que tiene la empresa. Es posible explotar la información a través del informe de banking pool.

!!! info
    Para más información, visita [la guía de usuario de Banking Pool](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#financial-type-configuration) y la [guía de desarrollador de Banking Pool](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle.md#banking-pool).

### Bulk Posting

:octicons-package-16: Javapackage: `com.etendoerp.bulk.posting`

<iframe width="560" height="315" src="https://www.youtube.com/embed/mgE-NnDLlA0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario contabilizar o deshacer la contabilización de múltiples registros al mismo tiempo. También se incluye en este módulo la ventana **Not Posted Documents**, que permite a los usuarios identificar y contabilizar todas las transacciones pendientes directamente desde una única ventana. 

!!! info
    Para más información, visita [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Conversion Rate Downloader

:octicons-package-16: Javapackage: `com.smf.currency.conversionrate`
:octicons-package-16: Javapackage: `com.smf.currency.apiconfig`

Este proceso permite mantener actualizadas las conversiones de divisa generando rangos de conversión automáticamente mediante un proceso en segundo plano usando apilayer.

!!! info
    Para más información, visita la [guía de usuario de Conversion Rate Downloader](./conversion-rate-downloader.md).

### Deferred GL Journal

:octicons-package-16: Javapackage: `com.etendoerp.gljournal.advanced`

<iframe width="560" height="315" src="https://www.youtube.com/embed/K7XOBkmRLAQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario duplicar un asiento tantas veces como sea necesario, indicando la regularidad y el periodo en el que debe realizarse la primera copia. Sigue el proceso para crear un asiento desde el principio y duplicarlo posteriormente.

!!! info
    Para más información, visita [la guía de usuario de Deferred GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#deferred-gl-journal).

### Financial Advanced Reports

:octicons-package-16: Javapackage: `com.etendoerp.financial.reports.advanced`

:octicons-package-16: Javapackage: `com.etendoerp.financial.reports.advanced.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Los informes **Cuadros plan general contable avanzado**, **Customer Statement** **Libro mayor avanzado**, **Diario asientos avanzado**, **Purchase Invoice Dimensional Report** y **Balance sumas y saldos** son una versión mejorada de los informes anteriores, incluyendo nuevos filtros según las dimensiones contables de los informes.

!!! info
    Para más información, visita:
    
    - Guía de usuario de [Cuadros plan general contable avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#balance-sheet-and-pl-structure-advanced).
    - Guía de usuario de [Customer Statement](../../../basic-features/financial-management/accounting/analysis-tools.md#customer-statement).
    - Guía de usuario de [Libro mayor avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#general-ledger-report-advanced).
    - Guía de usuario de [Diario asientos avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#journal-entries-report-advanced).
    - Guía de usuario de [Purchase Invoice Dimensional Report](../../../basic-features/procurement-management/analysis-tools.md#purchase-invoice-dimensional-report).
    - Guía de usuario de [Balance sumas y saldos](../../../basic-features/financial-management/accounting/analysis-tools.md#trial-balance).

### Financial Report Budget

:octicons-package-16: Javapackage: `com.etendoerp.financial.report.budget`

<iframe width="560" height="315" src="https://www.youtube.com/embed/2VFxpx8j8Sk?si=TuLZUdBGrOCSpXIE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta funcionalidad permite crear y gestionar presupuestos con fines de reporting, ofreciendo a los usuarios la posibilidad de comparar los valores presupuestados con los valores reales contabilizados en el Libro mayor correspondiente.

!!! info
    Para más información, visita la [guía de Financial Report Budget](../../../basic-features/financial-management/accounting/transactions.md#budget).

### G/L Journal Clone

:octicons-package-16: Javapackage: `com.etendoerp.gljournal.clone`

Esta funcionalidad permite al usuario clonar un diario de mayor (G/L) en la ventana Simple G/L Journal, que forma parte de las transacciones contables de gestión financiera.

!!! info
    Para más información, visita la [guía de usuario de G/L Journal Clone](../../../basic-features/financial-management/accounting/transactions.md#gl-journal-clone).

### Intercompany

:octicons-package-16: Javapackage: `com.etendoerp.advanced.intercompany`

<iframe width="560" height="315" src="https://www.youtube.com/embed/bQjT7iPkYtQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones diferentes pero que pertenecen al mismo cliente, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visita [la guía de usuario del módulo Intercompany](../../../optional-features/bundles/financial-extensions/intercompany.md).

### Payment Removal

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal`

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/TLbjMLjGYwo?si=uGtWnNHNa7gV4_l5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

El objetivo de esta funcionalidad es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

Los pagos a eliminar o reactivar pueden encontrarse en diferentes estados: Pendiente de ejecución, Pago realizado, Cobro recibido, Retirado no compensado, Depositado no compensado, Pago compensado (siempre que el pago haya sido conciliado mediante un método automático y no mediante un método manual), Contabilizar y Descontabilizar.

El botón Remove Payment está disponible en las ventanas Pedido de venta, Pedido de compra, Factura (Cliente), Factura (Proveedor), Cobro y Pago. Los botones Reactivate y Advanced reactivation solo están disponibles en las ventanas Cobro y Pago. Por último, los botones Reactivate Transaction, Remove Transaction, Reactivate Reconciliation y Remove Reconciliation están disponibles en la ventana Cuenta financiera.

!!! info
    Para más información, visita:

    - [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal)
    - [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal)
    - [Factura (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal_1)
    - [Factura (Proveedor)](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal_1)
    - [Payment In](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_1)
    - [Pago](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal)
    - [Cuenta financiera](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_2)

### Remittances

:octicons-package-16: Javapackage: `org.openbravo.module.remittance`

:octicons-package-16: Javapackage: `org.openbravo.module.remittance.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/6z3t-E_sV0E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite crear una remesa, que es un grupo de «pagos» (entrada/salida) o «orders/invoices» que pueden remitirse al banco para su cobro/pago. El banco gestionará entonces el cobro del dinero a los clientes o el pago a los proveedores.

!!! info
    Para más información, visita [la guía de usuario del módulo Remittances](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#remittance).

### Reverse GL Journal

:octicons-package-16: Javapackage: `com.smf.gljournal.reverse`

:octicons-package-16: Javapackage: `com.smf.gljournal.reverse.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pfqClq8HD6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad es especialmente útil para empresas que realizan cierres mensuales, en lugar de cierres anuales, pero con pagos pendientes (de entrada o de salida). Permite al usuario abrir o cerrar el periodo sin tener en cuenta los pagos hasta que se realicen.

!!! info
    Para más información, visita la [guía de usuario de GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#gl-journal) y la [guía de usuario de Simple GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#simple-gl-journal).

### Regularización del IVA 

:octicons-package-16: Javapackage: `com.etendoerp.vat.regularization`

<iframe width="560" height="315" src="https://www.youtube.com/embed/udarQ6h6EXQ?si=4CNi7Qgi2_yHdW5z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta funcionalidad permite al usuario ajustar cuentas, garantizando que el saldo de IVA sea preciso y esté correctamente alineado.

!!!info
    Para más información, visita la [Guía de Usuario de Regularización del IVA](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#vat-regularization).

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.