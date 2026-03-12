---
title: Financial Extensions Bundle
tags:
 - Gestión financiera
 - Funcionalidades de Etendo
 - Banca
 - Mejoras contables
 - Procesos automatizados
 - Integración bancaria
 - Salt Edge
 - Open Banking
 - Cuenta financiera
---

:octicons-package-16: Paquete Java: `com.etendoerp.financial.extensions`

:material-store: Etendo Marketplace:  [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}
## Visión general
Este bundle incluye mejoras para las funcionalidades de Gestión financiera en Etendo.

## Traducción
-  :material-translate: Español: [Financial Extensions Bundle ES](https://marketplace.etendo.cloud/#/product-details?module=0E104B3E36C84992BD7A6D941FBC7AB9){target="_blank"}
## Módulo

### Account Structure Validation

:octicons-package-16: Javapackage: `com.etendoerp.account.structure.validation`

Este módulo ayuda a prevenir errores comunes de configuración al crear o modificar subcuentas en el Árbol de cuentas. Valida la estructura y la configuración para evitar discrepancias en informes financieros como la Cuenta de resultados o el Balance de situación.

!!! info
    Para más información, visite [la guía de usuario del módulo Account Structure Validation](../../../optional-features/bundles/financial-extensions/account-structure-validation.md).

### Dimensiones contables de activos

:octicons-package-16: Paquete Java: `com.etendoerp.accounting.dimensions.assets.template`

:octicons-package-16: Paquete Java: `com.etendoerp.accounting.dimensions.assets`

<iframe width="560" height="315" src="https://www.youtube.com/embed/1a1UNCnNNcI?si=DbicgZnWjtmkScDh" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

El módulo Dimensiones contables de activos mejora la gestión de activos y la amortización al permitir al usuario especificar todas las **dimensiones contables disponibles** durante la creación y gestión del activo. Además, la ventana **Amortización** garantiza un seguimiento de activos más preciso **agrupado por períodos** y cálculos de amortización más completos.

!!! info
    Para más información, visite la [guía de usuario de Accounting Dimensions Assets](../../../basic-features/financial-management/assets/overview.md#accounting-dimensions-assets).
### Plantillas de Contabilidad

:octicons-package-16: Paquete Java: `com.etendoerp.accounting.templates`

Este módulo permite establecer el importe de un impuesto no deducible en una cuenta financiera específica.

!!! info
    Para más información, visite la [guía de usuario de Plantillas de Contabilidad](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/tax-rate.md#purchase-invoice-which-includes-not-deductible-tax-amount).
### Ajustar impuesto de factura
:octicons-package-16: Paquete Java: `com.etendoerp.adjust.invoice.tax`


Esta extensión permite realizar ajustes controlados en los importes de impuestos de las facturas para conciliar pequeñas **diferencias de redondeo** con sistemas externos; es compatible tanto con facturas de **Ventas** como de **Compra**, ofrece **ajustes manuales y automatizados** para correcciones mínimas a nivel de céntimos, y registra todos los cambios para garantizar la **auditabilidad**, asegurando que el total final de la factura coincida con requisitos externos o normativos.

!!! info
    Para más información, visite la [guía de usuario de Ajustar impuesto de factura](./adjust-invoice-tax.md).
### Gestión avanzada de cuentas bancarias

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/7AtGyQ62FHs?si=HisPbmd0KzblSq0O" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Este módulo mejora la gestión de cuentas bancarias, permitiendo una mayor personalización y control sobre la selección de cuentas bancarias asociadas a clientes y proveedores. Además, se añade el botón **Modificar plan de pagos** para una mejor gestión de pagos.

!!! info
    Esta funcionalidad está disponible en las siguientes ventanas:

    - [Terceros](../../../basic-features/master-data-management/master-data.md#advanced-bank-account-management_1)
    - [Factura (Cliente)](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management_1)
    - [Factura (Proveedor)](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management_1)
    - [Pedido de venta](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management)
    - [Pedido de compra](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management)
    - [Cobros](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management_1)
    - [Pago](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management)

    Para más información, visite [Gestión avanzada de cuentas bancarias](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).
### Liquidación de terceros

:octicons-package-16: Paquete Java: `com.etendoerp.advanced.bpsettlement`

:octicons-package-16: Paquete Java: `org.openbravo.financial.bpsettlement`

<iframe width="560" height="315" src="https://www.youtube.com/embed/Gh6G1i3Iyts" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario crear liquidaciones para facturas, tanto de ventas como de compra, desde las ventanas de Cobros y Pago. Además, se puede realizar una compensación creando una liquidación desde una conciliación bancaria para abonos/cargos desde la ventana de Cuenta financiera.

!!! info
    Para más información, visite:

    - [Business Partner Settlement - User Guide](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).
    - [Cobros](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-1)
    - [Pago](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement)
    - [Cuenta financiera](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-2)
### Procesamiento avanzado de documentos financieros

:octicons-package-16: Paquete Java: `com.etendoerp.advanced.financial.docs.processing`

:octicons-package-16: Paquete Java: `com.etendoerp.advanced.financial.docs.processing.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pnE-nePaTEI" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad forma parte de Financial Extensions Bundle y es útil cuando el usuario necesita reactivar facturas anuladas (tanto de Ventas como de Compra) y partes cerrados (tanto de Ventas como de Compra), así como amortizaciones.

!!! warning "Aviso de dependencia"
    Este módulo depende del módulo [**Finalización masiva**](../../optional-features/bundles/essentials-extensions/bulk-completion.md), ya que las acciones de procesamiento de **Parte** deben realizarse utilizando procesos modernos que permitan el disparo de Hooks, en lugar del procesamiento heredado. Debido a este requisito, las acciones heredadas de **cerrar/reactivar** para partes se ocultarán y estas acciones solo estarán disponibles a través del botón **Finalización masiva**.

!!! info
    Para más información, visite:

    - [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-closed-sales-order) 
    - [Factura (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-a-voided-sales-invoice)
    - [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-closed-purchase-order)
    - [Factura (Proveedor)](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-a-voided-purchase-invoice)
    - [Amortización](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#how-to-reactivate-amortizations)
    - y la [Guía del desarrollador de Procesamiento avanzado de documentos financieros](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle.md#advanced-financial-docs-processing)
### Informe de Amortización de Activos

:octicons-package-16: Paquete Java: `com.smf.asset.amortization.report`

El nuevo informe de Amortización permite descargar informes en Excel con información sobre la amortización creada para un año seleccionado.

!!! info
    Para más información, visite [la guía de usuario del Informe de Amortización de Activos](../../../../../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#asset-amortization-report-excel).
### Remesa automatizada

:octicons-package-16: Paquete Java: `com.etendoerp.automated.remittance`

Esta funcionalidad permite al usuario procesar y protestar remesas de forma automática.

!!! info
    Para más información, visite [la guía de usuario de Remesa automatizada](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).

# Visión general de la integración bancaria

:octicons-package-16: Javapackage: `com.etendoerp.psd2.bank.integration`

## Introducción

El módulo de Integración bancaria proporciona **integración bancaria automática** para Etendo ERP a través de dos capacidades principales:

- **AIS (Account Information Service)**: conecte de forma segura sus cuentas bancarias y descargue automáticamente las transacciones bancarias.
- **PIS (Payment Initiation Service)**: inicie pagos bancarios directamente desde Etendo, con la autorización gestionada de forma segura a través de su banco.

La integración está impulsada por [Salt Edge](https://www.saltedge.com/){target="_blank"}, una plataforma líder de Open Banking que proporciona acceso seguro a miles de bancos en todo el mundo, y utiliza un **middleware centralizado** desarrollado por Etendo que gestiona toda la comunicación, la seguridad y el cumplimiento.

## Arquitectura

La integración utiliza una **arquitectura de tres capas**:

1. **Etendo ERP**: interfaz de usuario y lógica de negocio
2. **Etendo Middleware**: capa de integración centralizada (gestionada por Futit Services)
3. **Plataforma Salt Edge**: conectividad Open Banking con los bancos

```
┌─────────────────┐
│   Etendo ERP    │
│  (User Layer)   │
└────────┬────────┘
         │
         │ API Calls
         ▼
┌─────────────────┐
│   Middleware    │
│ (Security Layer)│
└────────┬────────┘
         │
         │ Salt Edge API
         ▼
┌─────────────────┐
│   Salt Edge     │
│ (Open Banking)  │
└────────┬────────┘
         │
         │ Bank APIs
         ▼
┌─────────────────┐
│  Banks / ASPSPs │
└─────────────────┘
```

### Beneficios de esta arquitectura

- **Separación de responsabilidades**: Etendo se centra en la funcionalidad del ERP mientras que el middleware gestiona la complejidad de la integración
- **Seguridad**: las credenciales y certificados sensibles se gestionan a nivel de middleware
- **Escalabilidad**: varias instancias de Etendo pueden compartir el mismo middleware
- **Mantenibilidad**: los cambios en las API bancarias se gestionan de forma centralizada sin afectar a las instancias de Etendo
- **Cumplimiento**: los requisitos de PSD2 y Open Banking se cumplen a nivel de middleware

## Funcionalidades clave

### Información de cuenta (AIS)

- **Importación automática de transacciones**: descargue transacciones directamente desde las cuentas bancarias — sin necesidad de cargar manualmente ficheros de extractos bancarios
- **Rangos de fechas configurables**: controle hasta qué fecha se deben recuperar las transacciones en la configuración inicial
- **Prevención de duplicados**: filtra automáticamente las transacciones duplicadas utilizando los IDs de transacción de Salt Edge
- **Agrupación de extractos**: configure cómo se agrupan las transacciones en extractos bancarios (por ejecución, por semana o por mes)
- **Procesamiento programado**: proceso en segundo plano para la importación automática en todas las cuentas conectadas

### Gestión de conexiones bancarias

- **Autenticación segura**: las credenciales bancarias se introducen directamente en el sitio web del banco a través del widget de Salt Edge — nunca se almacenan en Etendo
- **Miles de bancos**: soporte para bancos de todo el mundo a través de Salt Edge
- **Ciclo de vida de la conexión**: supervise, sincronice, reconecte y desconecte conexiones bancarias desde Etendo
- **Sincronización automática de cuentas**: las cuentas bancarias se recuperan automáticamente cuando se establece una conexión

### Iniciación de pagos (PIS)

- **Pagos bancarios directos**: inicie pagos desde registros de **Pago** sin salir del ERP
- **Soporte multi-plantilla**: plantillas de pago SEPA (EUR), FPS (GBP) y DOMESTIC — seleccionadas automáticamente según la divisa
- **Autorización bancaria**: autorización segura del pago a través de la página de autenticación del propio banco
- **Seguimiento de estado en tiempo real**: supervise el progreso del pago desde la iniciación hasta la ejecución
- **Actualizaciones automáticas de estado**: reciba actualizaciones del estado del pago mediante webhooks y un proceso de actualización programado preconfigurado
- **Gestión de proveedores bancarios**: mantenga una lista actualizada de bancos que admiten iniciación de pagos

### Monitorización y registros

- **Ventana de registros PSD2**: vista centralizada de toda la actividad de integración y registros de errores
- **Entradas de registro detalladas**: cada registro incluye cuenta financiera, fecha de ejecución, estado, origen, descripción y respuesta API en bruto
- **Ventana de proveedor bancario**: visualice y gestione la lista de proveedores bancarios disponibles

## Flujo de trabajo del usuario

### AIS (Información de cuenta)

1. **Configuración**:
     - El administrador obtiene la API Key de Salt Edge de Futit Services
     - El usuario configura la API Key en su perfil (campo **PSD2 API Key**)
     - Las cuentas financieras se configuran con rangos de fechas de importación, proveedor bancario y frecuencia de extractos

2. **Conexión**:
     - El usuario hace clic en **Connect Bank Account** en la Cuenta financiera
     - Se abre el widget de Salt Edge para la selección del banco y la autenticación
     - El usuario se autentica con las credenciales de su banco (introducidas en el sitio web del propio banco)
     - Se establece la conexión y las cuentas bancarias se sincronizan automáticamente

3. **Importación de transacciones**:
     - **Manual**: el usuario hace clic en **Get Bank Statement** en la Cuenta financiera
     - **Automático**: programe el proceso **Get Bank Statements** para que se ejecute periódicamente
     - Las transacciones se importan y los extractos bancarios se crean automáticamente

4. **Uso continuado**:
     - El proceso programado importa transacciones automáticamente
     - El usuario concilia las transacciones importadas utilizando las funcionalidades de conciliación de Etendo
     - Las conexiones se renuevan mediante **Reconnect Connection** cuando caducan

### PIS (Iniciación de pagos)

1. **Configuración**:
     - Ejecute el proceso **Synchronize Bank Providers** para rellenar la lista de proveedores
     - Opcionalmente, asigne un **Bank Provider** a cada cuenta financiera

2. **Pago**:
     - El usuario crea un registro de **Pago** como de costumbre
     - Hace clic en **Generate Bank Payment** — aparece un formulario con valores pre-rellenados
     - Revisa y confirma — se abre un popup de autorización bancaria
     - El usuario autoriza el pago en el entorno seguro de su banco

3. **Seguimiento**:
     - El estado del pago se actualiza automáticamente mediante webhooks
     - Un proceso preconfigurado **Refresh Pending Payments** se ejecuta cada 10 minutos como medida de seguridad
     - El usuario también puede actualizar el estado manualmente desde la pestaña **Bank Payments**

## Seguridad y privacidad

- **Sin almacenamiento de credenciales**: las credenciales bancarias nunca se almacenan en Etendo ni en el middleware — los usuarios se autentican directamente con su banco
- **Seguridad de la API Key**: cada usuario tiene su propia API Key para el acceso al middleware
- **Comunicación cifrada**: toda la transmisión de datos está cifrada
- **Registro de auditoría**: todas las operaciones se registran en la ventana **PSD2 Logs** para cumplimiento y resolución de incidencias

## Cumplimiento PSD2

El módulo utiliza Salt Edge, que cumple con PSD2, y soporta los siguientes estándares de Open Banking:

- **Account Information Services (AIS)**: acceso de lectura a datos de cuenta y transacciones
- **Payment Initiation Services (PIS)**: iniciar pagos a través del banco
- **Strong Customer Authentication (SCA)**: autenticación a nivel bancario tanto para conexiones como para pagos
- **Ciclo de vida de la conexión**: caducidad del consentimiento, renovación y reconexión

## Requisitos previos

Para utilizar este módulo, necesita:

1. **Financial Extensions Bundle** instalado en Etendo
2. **Salt Edge API Key** proporcionada por Futit Services
3. **Cuentas financieras** creadas en Etendo
4. **Permisos de usuario** para acceder a Gestión financiera

!!!info
    Para obtener instrucciones detalladas de configuración y uso, visite la [Guía de usuario de Integración bancaria](ser-guide-bank-integration.md).

### Pool bancario

:octicons-package-16: Javapackage: `com.etendoerp.bankingpool`

<iframe width="560" height="315" src="https://www.youtube.com/embed/sdPnyewiPbc" title="reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite introducir en el sistema todas las financiaciones que tiene la empresa. Es posible explotar la información a través del informe del pool bancario.

!!! info
    Para más información, visite [la guía de usuario del Pool bancario](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#financial-type-configuration) y la [guía del desarrollador del Pool bancario](../../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle.md#banking-pool).
### Contabilización masiva

:octicons-package-16: Paquete Java: `com.etendoerp.bulk.posting`

<iframe width="560" height="315" src="https://www.youtube.com/embed/mgE-NnDLlA0" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario contabilizar o deshacer la contabilización de múltiples registros al mismo tiempo. También se incluye en este módulo la ventana **Documentos no contabilizados**, que permite a los usuarios identificar y contabilizar todas las transacciones pendientes directamente desde una única ventana.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
### Descargador de tipos de cambio

:octicons-package-16: Paquete Java: `com.smf.currency.conversionrate`  
:octicons-package-16: Paquete Java: `com.smf.currency.apiconfig`

Este proceso permite mantener actualizadas las conversiones de divisa generando automáticamente tipos de conversión con un proceso en segundo plano mediante apilayer.

!!! info
    Para más información, visite la [Guía de usuario - Conversion Rate Downloader](./conversion-rate-downloader.md).
### Diario diferido de mayor

:octicons-package-16: Paquete Java: `com.etendoerp.gljournal.advanced`

<iframe width="560" height="315" src="https://www.youtube.com/embed/K7XOBkmRLAQ" title="reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite al usuario duplicar un asiento contable tantas veces como sea necesario, indicando la periodicidad y el período en el que debe realizarse la primera copia. Siga el proceso para crear un asiento contable desde el principio y duplicarlo posteriormente.

!!! info
    Para más información, visite la [guía de usuario de Diario diferido de mayor](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#deferred-gl-journal).
### Informes financieros avanzados

:octicons-package-16: Paquete Java: `com.etendoerp.financial.reports.advanced`

:octicons-package-16: Paquete Java: `com.etendoerp.financial.reports.advanced.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Los informes **Balance de Situación y Estructura de PyG Avanzado**, **Extracto de cuenta de Cliente**, **Informe de Libro Mayor Avanzado**, **Informe de Asientos Avanzado**, **Análisis dimensional facturas compras** y **Balance sumas y saldos** son una versión mejorada de los informes anteriores, e incluyen nuevos filtros según las dimensiones contables de los informes.

!!! info
    Para más información, visite:
    
    - [Guía de usuario de Balance de Situación y Estructura de PyG Avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#balance-sheet-and-pl-structure-advanced).
    - [Guía de usuario de Extracto de cuenta de Cliente](../../../basic-features/financial-management/accounting/analysis-tools.md#customer-statement).
    - [Guía de usuario de Informe de Libro Mayor Avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#general-ledger-report-advanced).
    - [Guía de usuario de Informe de Asientos Avanzado](../../../basic-features/financial-management/accounting/analysis-tools.md#journal-entries-report-advanced).
    - [Guía de usuario de Análisis dimensional facturas compras](../../../basic-features/procurement-management/analysis-tools.md#purchase-invoice-dimensional-report).
    - [Guía de usuario de Balance sumas y saldos](../../../basic-features/financial-management/accounting/analysis-tools.md#trial-balance).
### Informe financiero de presupuesto

:octicons-package-16: Paquete Java: `com.etendoerp.financial.report.budget`

<iframe width="560" height="315" src="https://www.youtube.com/embed/2VFxpx8j8Sk?si=TuLZUdBGrOCSpXIE" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta funcionalidad permite crear y gestionar presupuestos con fines de informes, ofreciendo a los usuarios la posibilidad de comparar los valores presupuestados con los valores reales contabilizados en el Libro mayor correspondiente.

!!! info
    Para más información, visite la [guía de Informe financiero de presupuesto](../../../basic-features/financial-management/accounting/transactions.md#budget).
### Clonación de diario de libro mayor

:octicons-package-16: Paquete Java: `com.etendoerp.gljournal.clone`

Esta funcionalidad permite al usuario clonar un diario de libro mayor en la ventana Diario simple de libro mayor, que forma parte de las transacciones contables de la gestión financiera.

!!! info
    Para más información, visite la [Guía de usuario de G/L Journal Clone](../../../basic-features/financial-management/accounting/transactions.md#gl-journal-clone).
### Intercompañía

:octicons-package-16: Paquete Java: `com.etendoerp.advanced.intercompany`

<iframe width="560" height="315" src="https://www.youtube.com/embed/bQjT7iPkYtQ" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones que son diferentes pero pertenecen al mismo cliente, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visite la [guía de usuario del Módulo de Intercompañía](../../../optional-features/bundles/financial-extensions/intercompany.md).
### Eliminación de pagos

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal`

:octicons-package-16: Javapackage: `com.etendoerp.payment.removal.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/TLbjMLjGYwo?si=uGtWnNHNa7gV4_l5" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

El objetivo de esta funcionalidad es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

Los pagos que se van a eliminar o reactivar pueden encontrarse en diferentes estados: Pendiente de ejecución, Pago realizado, Pago recibido, Retirado no compensado, Depositado no compensado, Pago compensado (siempre que el pago haya sido conciliado mediante un método automático y no mediante un método manual), Contabilizado y No contabilizado.

El botón Eliminar pago está disponible en las ventanas Pedido de venta, Pedido de compra, Factura (Cliente), Factura (Proveedor), Cobros y Pago. Los botones Reactivar y Reactivación avanzada solo están disponibles en las ventanas Cobros y Pago. Por último, los botones Reactivar transacción, Eliminar transacción, Reactivar conciliación y Eliminar conciliación están disponibles en la ventana Cuenta financiera.


!!! info
    Para más información, visite:

    - [Pedido de venta](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal)
    - [Pedido de compra](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal)
    - [Factura (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#payment-removal_1)
    - [Factura (Proveedor)](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#payment-removal_1)
    - [Cobros](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_1)
    - [Pago](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal)
    - [Cuenta financiera](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#payment-removal_2)
### Remesas

:octicons-package-16: Paquete Java: `org.openbravo.module.remittance`

:octicons-package-16: Paquete Java: `org.openbravo.module.remittance.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/6z3t-E_sV0E" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad permite crear una remesa, que es un grupo de "pagos" (entrada/salida) o "partes/facturas" que pueden remitirse al banco para su pago. El banco gestionará entonces el cobro del dinero a los clientes o el pago a los proveedores/suministradores.

!!! info
    Para más información, visite [la guía de usuario del módulo Remesas](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#remittance).
### Asiento contable inverso

:octicons-package-16: Paquete Java: `com.smf.gljournal.reverse`

:octicons-package-16: Paquete Java: `com.smf.gljournal.reverse.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/pfqClq8HD6k" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad es especialmente útil para empresas que realizan un cierre mensual, en lugar de un cierre de fin de año, pero con pagos pendientes (cobros o pagos). Permite al usuario abrir o cerrar el período sin tener en cuenta los pagos hasta que se realicen.

!!! info
    Para más información, visite la [Guía de usuario de GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#gl-journal) y la [Guía de usuario de Simple GL Journal](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#simple-gl-journal).
### Regularización de IVA 

:octicons-package-16: Paquete Java: `com.etendoerp.vat.regularization`

<iframe width="560" height="315" src="https://www.youtube.com/embed/udarQ6h6EXQ?si=4CNi7Qgi2_yHdW5z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta funcionalidad permite al usuario ajustar cuentas, garantizando que el saldo de IVA sea preciso y esté correctamente alineado.

!!!info
    Para más información, visite la [Guía de usuario de Regularización de IVA](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#vat-regularization).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

---