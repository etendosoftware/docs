---
title: Platform Extensions Bundle
tags:
    - Etendo Platform
    - Extension Bundle
    - Docker Management
    - Advanced Security
    - Webhook Events
---

:octicons-package-16: Javapackage: `com.etendoerp.platform.extensions`

:material-store: Etendo Marketplace:  [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}

## Visión general
Este bundle incluye mejoras para las funcionalidades de la plataforma en Etendo.

## Traducción
-  :material-translate: Español: [Platform Extensions Bundle ES](https://marketplace.etendo.cloud/#/product-details?module=3789DBA46FC54FDF96CD7D298203A3E9){target="_blank"}

## Módulo

### Gestor de dependencias

:octicons-package-16: Javapackage: `com.etendoerp.dependencymanager`

El usuario puede acceder a todas las dependencias disponibles para añadirlas, configurarlas y consultar información sobre versiones, validaciones, etc.

!!! info
    Para más información, visite la [Guía del desarrollador de Dependency Manager](../../../../../developer-guide/etendo-classic/bundles/platform/dependency-manager.md).

### Gestión de Docker 

:octicons-package-16: Javapackage: `com.etendoerp.docker`

Este módulo permite el uso de contenedores dockerizados en Etendo.

!!!info
    Para más información, visite la [Guía del desarrollador de Docker Management](../../../../../developer-guide/etendo-classic/bundles/platform/docker-management.md). 

### Servicio de Tomcat dockerizado

:octicons-package-16: Javapackage: `com.etendoerp.tomcat`

Este módulo permite la dockerización de Tomcat dentro de Etendo.

!!!info
    Para más información, visite la [Guía del desarrollador de Dockerized Tomcat Service](../../../../../developer-guide/etendo-classic/bundles/platform/dockerized-tomcat-service.md).

### Aplicación dinámica 

:octicons-package-16: Javapackage: `com.etendoerp.dynamic.app`

Dynamic App permite crear subaplicaciones en Etendo Mobile.

!!! info
    Para más información, visite la [Guía del desarrollador de Dynamic App](../../../../../developer-guide/etendo-classic/bundles/platform/dynamic-app.md)

### EAN 128

:octicons-package-16: Javapackage: `com.smf.ean128`

EAN 128 permite utilizar código de barras en su aplicación

!!! info
    Para más información, visite la [Guía del desarrollador de EAN 128](../../../../../developer-guide/etendo-classic/bundles/platform/overview.md#ean-128).

### Etendo Advanced Security

:octicons-package-16: Javapackage: `com.etendoerp.advanced.security`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.security.template`

Etendo Advanced Security permite ampliar y mejorar algunas de las funcionalidades de seguridad del sistema.

!!! info
    Para más información, visite la [Guía de usuario de Etendo Advanced Security](../../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-advanced-security.md) y lea la [Guía del desarrollador de Etendo Advanced Security](../../../../..//developer-guide/etendo-classic/bundles/platform/overview.md#etendo-advanced-security).

### Etendo Async Processes

:octicons-package-16: Javapackage: `com.etendoerp.asyncprocess`

### Etendo Reactor

:octicons-package-16: Javapackage: `com.etendoerp.reactor`

### Etendo RX

:octicons-package-16: Javapackage: `com.etendoerp.etendorx`

Este módulo garantiza un método de autenticación que permite a los usuarios autenticarse de forma segura y autorizar el acceso a su información utilizando su proveedor preferido.

!!!info
    Para más información, visite la [Guía de usuario de Etendo RX](../platform-extensions/etendo-rx.md).


### Número a palabra (inglés)

:octicons-package-16: Javapackage: `org.openbravo.numbertoword_en`

:octicons-package-16: Javapackage: `org.openbravo.numbertoword`

Proporciona la infraestructura para convertir un número en su equivalente en palabras. Esta funcionalidad es especialmente útil al imprimir cheques.

!!! info
    Para más información, visite la [Guía de usuario de Number To Word Converter](../../../../../user-guide/etendo-classic/basic-features/general-setup/application/number-to-word-converter.md) y la [Guía del desarrollador de Number To Word Converter](../../../../../developer-guide/etendo-classic/bundles/platform/overview.md#number-to-word-english).

### Servicio web de impresión de documentos

:octicons-package-16: Javapackage: `com.etendoerp.printdocumentws`

:octicons-package-16: Javapackage: `com.smf.ws.printdocument`

Permite descargar un PDF de algunos documentos de transacción mediante un servicio web y devolver un PDF con el pedido, la factura o el albarán. Esto es útil para empresas que utilizan aplicaciones de terceros y requieren que los imprimibles sean accesibles desde dichas aplicaciones.

!!! info
    Para más información, visite la [Guía del desarrollador de Print Document Web Service](../../../../../developer-guide/etendo-classic/bundles/platform/overview.md#print-document-web-service). 


### Proveedor de impresión
:octicons-package-16: Javapackage: `com.etendoerp.print.provider`

Conecta Etendo con plataformas de impresión externas para habilitar la generación e impresión centralizada de documentos con un solo clic en todo el sistema. Permite que cada organización configure su propio proveedor de impresión, gestione catálogos de impresoras y plantillas, y ejecute trabajos de impresión directa desde ventanas específicas. El módulo incluye una integración por defecto con PrintNode y admite proveedores personalizados mediante servicios de backend reutilizables y una API pública, garantizando una gestión de impresión flexible, segura y automatizada dentro de Etendo.

!!! info
    - Para más información, visite la [Print Provider - User Guide](./print-provider.md).
    - Para más información, visite la [Guía del desarrollador de Print Provider](../../../../../developer-guide/etendo-classic/bundles/platform/print-provider.md).


### Gestión de caché de informes

:octicons-package-16: Javapackage: `com.exos.erp.reportcachemanagement`

Este módulo permite cambiar o actualizar un informe Jasper en un entorno Etendo sin detener el servidor.

!!! info
    Para más información, visite la [Guía del desarrollador de Clear Report Cache](../../../../../developer-guide/etendo-classic/bundles/platform/overview.md#report-cache-management).  

### Mantenimiento

:octicons-package-16: Javapackage: `com.etendoerp.task`

El módulo **Mantenimiento** en Etendo proporciona un marco flexible para crear, asignar y automatizar tareas basadas en eventos de negocio. Este módulo permite a las organizaciones definir tipos de tareas, algoritmos de asignación de usuarios y acciones automatizadas desencadenadas por cambios en la base de datos o interacciones del usuario. Es ideal para automatizar flujos de trabajo como seguimientos de pedidos, gestión de incidencias o procesos de interacción con clientes.

!!! info
    Para más información, consulte la [Guía de usuario de Task](./task.md) para el uso funcional y la [Guía del desarrollador de Task](../../../../../developer-guide/etendo-classic/bundles/platform/task.md) para la configuración y personalización.

### Eventos de webhook

:octicons-package-16: Javapackage: `com.etendoerp.webhookevents`

Los eventos de webhook permiten ejecutar acciones mediante una llamada a una URL, proporcionando una forma potente de integrarse con servicios externos.

!!! info
    Para más información, visite la [Guía del desarrollador de Webhook Events](../../../../../developer-guide/etendo-classic/bundles/platform/etendo-webhooks.md).  

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.