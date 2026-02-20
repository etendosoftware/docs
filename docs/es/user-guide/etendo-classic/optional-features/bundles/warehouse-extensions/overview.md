---
title: Warehouse Extensions Bundle
tags:
    - Gestión de almacenes
    - Reserva automatizada
    - Historial de existencias
    - Reactivación de documentos
    - Operaciones de producto
    - Preparación de pedidos
    - Empaquetado
    - Reglas de gestión de materiales
---
:octicons-package-16: Javapackage: `com.etendoerp.warehouse.extensions`

:material-store: Etendo Marketplace:  [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}

## Visión general
Este bundle incluye mejoras para las funcionalidades de gestión de almacenes en Etendo.

## Traducción

-  :material-translate: Español: [Warehouse Extensions Bundle ES](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}

## Módulo

### Gestión avanzada de almacenes

:octicons-package-16: Javapackage: `com.etendoerp.advanced.warehouse.management`

Amplía Etendo con una gestión de inventario completa, flexible y automatizada, totalmente sincronizada con Etendo Mobile para la trazabilidad en tiempo real. Admite estados de inventario configurables, reglas de movimiento automáticas (incluyendo ubicaciones virtuales), reservas basadas en AUOM que respetan cajas/palés y conversiones, y un flujo de recepción de entrada que crea Inventario referenciado por unidad logística.  

La gestión de códigos de barras incluye AIs GS1-128 (p. ej., GTIN, lote, caducidad, ubicador, unidad logística) y búsqueda por código relacionado. Un motor de tareas permite la autogeneración y asignación de tareas de almacén, y desde móvil los usuarios pueden gestionar tareas de Preparación de pedidos, Empaquetado y tareas de inventario —en concreto, Ajuste de inventario y Reubicación de inventario— con validación basada en escaneo, control estricto de cantidades y cumplimiento exacto de las reservas para operaciones más rápidas, resistentes a errores y con trazabilidad de extremo a extremo.  

!!! info
    Para más información, visite [Gestión avanzada de almacenes](./advanced-warehouse-management.md).

### Reserva automatizada de almacén

:octicons-package-16: Javapackage: `com.etendoerp.automated.warehouse.reservation`

Este módulo añade la opción Automática - Solo almacén por defecto al campo Reserva de existencias de la solapa líneas en la ventana Pedido de venta. Esto se utiliza para limitar la reserva únicamente al almacén especificado en la cabecera del pedido.

!!! info
    Para más información, visite [Pedido de venta](../../../basic-features/sales-management/transactions.md#stock-reservations) y [Reserva de existencias](../../../basic-features/warehouse-management/transactions.md#stock-reservation).

### Empaquetado 

:octicons-package-16: Javapackage: `org.openbravo.warehouse.packing`

La funcionalidad de Empaquetado en Etendo se centra en ayudar al personal de almacén a empaquetar productos de forma eficiente y organizada. Esta funcionalidad facilita que el personal se concentre en empaquetar los artículos con precisión una vez que han sido preparados. 
Si ambos módulos, preparación de pedidos y empaquetado, están instalados, el flujo de trabajo comienza con la preparación de pedidos y continúa con el empaquetado, garantizando un proceso de cumplimiento de pedidos fluido y organizado. No obstante, también es posible utilizar los módulos por separado.

!!! info
    Para más información, visite [Empaquetado](packing.md). 

### Preparación de pedidos 

:octicons-package-16: Javapackage: `org.openbravo.warehouse.pickinglist`

:octicons-package-16: Javapackage: `org.openbravo.warehouse.structure`

En Etendo, la funcionalidad de Preparación de pedidos está diseñada para ayudar al personal de almacén a gestionar y tramitar listas de preparación de forma eficiente. Este módulo facilita a los usuarios el acceso y la organización de los artículos que deben recogerse del almacenamiento. Al optimizar el proceso de preparación, reduce errores y mejora la velocidad general de preparación de pedidos. La preparación de pedidos suele ser el primer paso en el flujo de cumplimiento del pedido cuando están instalados los módulos de Preparación de pedidos y Empaquetado.

!!! info
    Para más información, visite [Preparación de pedidos](picking.md).

### Operaciones de producto

:octicons-package-16: Javapackage: `com.etendoerp.product.operations`

Este módulo le permite observar y analizar en detalle todas las transacciones asociadas al producto seleccionado. 

!!! info
    Para más información, visite la [Guía de usuario de Operaciones de producto](../../../basic-features/warehouse-management/analysis-tools.md/#product-operations).


### Reactivar documentos de almacén

:octicons-package-16: Javapackage: `com.etendoerp.reactivate.warehouse.documents`

:octicons-package-16: Javapackage: `com.etendoerp.reactivate.warehouse.documents.template`

<iframe width="560" height="315" src="https://www.youtube.com/embed/ghH3tBjoN9c" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Esta funcionalidad forma parte de Warehouse Extensions Bundle y es útil cuando el usuario necesita reactivar documentos como Movimiento entre almacenes, Albarán (Proveedor), Albarán (Cliente) e Inventario físico. 

!!! info
    Para más información, visite la guía de usuario de:

    - [Movimiento entre almacenes](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#how-to-reactivate-goods-movements)
    - [Albarán (Proveedor)](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#how-to-reactivate-goods-receipts)
    - [Albarán (Cliente)](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#how-to-reactivate-goods-shipments)
    - [Inventario físico](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#how-to-reactivate-physical-inventories)

### Historial de existencias

:octicons-package-16: Javapackage: `com.etendoerp.stock.history`

Este módulo proporciona información actualizada sobre el historial diario de existencias de los productos. 

!!! info
    Para más información, visite la [Guía de usuario de Historial de existencias](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#stock-history) y la [Guía del desarrollador de Historial de existencias](../../../../../developer-guide/etendo-classic/bundles/warehouse-extensions-bundle.md#stock-history).

### Unidad logística de existencias

<iframe width="560" height="315" src="https://www.youtube.com/embed/yrP1iPmCk_U?si=Riy5plMo7lVDjVWS" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:octicons-package-16: Javapackage: `com.etendoerp.stock.logisticunit`

El módulo **Unidad logística de existencias** amplía la funcionalidad estándar de gestión de almacenes de Etendo integrando Unidades de medida alternativas (AUOM) con el modelo de Inventario referenciado. Introduce nuevos tipos de unidad logística como **Empaquetar** y **Palé**, habilitando la trazabilidad y un control eficiente de existencias en todas las operaciones de almacén.  
Este módulo también mejora la lógica de reserva de existencias, priorizando unidades logísticas completas (Empaquetar o Palés) frente a unidades individuales para optimizar la asignación de existencias y mantener la coherencia con las condiciones del pedido de venta.  

!!! info
    Para más información, visite la [Guía de usuario de Unidad logística de existencias](./stock-logistic-unit.md).

### Reglas de gestión de materiales

:octicons-package-16: Javapackage: `com.etendoerp.materialmgmt.rules`

!!! info
    Disponible desde la versión 3.6.0 de Warehouse Extensions Bundle

Este módulo le permite configurar si el sistema permite transacciones de material con fechas anteriores a la fecha actual.

La preferencia **Permitir transacciones de coste con fecha anterior** se establece en **Y** por defecto, lo que significa que se permiten transacciones con fechas anteriores a la fecha actual. 

Cuando la preferencia se establece en **N**, los siguientes documentos estarán restringidos a utilizar únicamente la fecha actual: [Albarán (Proveedor)](../../../basic-features/procurement-management/transactions.md#goods-receipts), [Albarán (Cliente)](../../../basic-features/sales-management/transactions.md#goods-shipment), [Movimiento entre almacenes](../../../basic-features/warehouse-management/transactions.md#goods-movement), [Inventarios físicos](../../../basic-features/warehouse-management/transactions.md#physical-inventory), [Parte de Trabajo](../../../basic-features/production-management/transactions.md#work-effort) y [Consumo interno](../../../basic-features/production-management/transactions.md#internal-consumption).

!!! warning
    Si necesita crear una nueva configuración para esta preferencia, debe establecerse únicamente a nivel global, sin distinguir ningún nivel de visibilidad específico (Organización, Usuario, Rol, etc.), ya que podría afectar al correcto funcionamiento de la validación.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/material-mgmt-rules-preference.png)

## Desinstalar bundle

Para desinstalar el bundle y evitar problemas futuros con registros huérfanos, debe seguirse una secuencia de pasos:

1. Ejecute la siguiente consulta en la base de datos del entorno
```
DELETE FROM OBUIAPP_GC_TAB 
WHERE AD_TAB_ID = 'C3DB551F2BCA40A79AAF21DBD6D06309';
```

2. Una vez que la consulta finalice correctamente, elimine el bundle según el método correspondiente a la instalación (Sources/JARs)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.