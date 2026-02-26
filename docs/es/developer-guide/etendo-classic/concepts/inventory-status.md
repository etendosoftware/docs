---
title: Estado de inventario
tags:
    - Conceptos
    - Gestión de inventario
    - Estado de inventario
    - Control de stock
    - Operaciones de almacén
---
## Visión general

Esta sección explica el concepto de Estado de inventario que forma parte de Etendo.

## Configuración

El Estado de inventario estará disponible y se configurará como parte de Etendo.

De forma predeterminada, todas las ubicaciones estarán en un Estado de inventario indefinido. Hay dos posibilidades:

-   **Indefinido**. Disponible y Planificable, pero no es posible pasar a Stock Negativo.
-   **Indefinido Stock Negativo**. Disponible y Planificable y es posible pasar a Stock Negativo.

El estado inicial de las ubicaciones dependerá de la configuración previa del Cliente. Para aquellos clientes que estaban configurados para Permitir stock negativo, se establecerá el Estado de inventario Indefinido Stock Negativo. Para el resto, será el Estado de inventario Indefinido. 

!!! info
    Para más información, visite la [guía de usuario de Permitir stock negativo](../../../user-guide/etendo-classic/basic-features/general-setup/client.md).

## Funcionalidad

El concepto de Estado de inventario forma parte de la gestión de inventario de Etendo e incluye las dimensiones para Disponible, Planificable y Stock Negativo en la ubicación de almacenamiento, y todo el stock en esta ubicación tiene el mismo Estado de inventario. La semántica del Estado de inventario se refiere a la condición de un inventario específico y puede configurarse. Consulte los ejemplos al final de esta sección.

Los datos maestros del estado de inventario se mantienen a nivel de sistema y los valores más típicos vienen predefinidos con el conjunto de datos de Etendo. Es posible añadir nuevos estados de inventario y/o traducir los existentes.

!!! info
    Para tener acceso a esta ventana, es necesario iniciar sesión como administrador del sistema.


![](../../../assets/drive/0n3Ivd3Cp7mA5Q7vAbIhorgapjwAxb6ybg6_fqwlpmzwe4FcL3RV2o6AIqsR2cFEdXKSRtzToRe9E5lLZsdoDCGZmM0toNmJZKURGVZxNStUoQW_ocSMxgcB4KjV_ARl4TTg0GWncx0ONJ1GzIfAHsJxNIs38iEekvloTzKkUdFIjICAn0YUklI1ThE-tg.png)

En la imagen anterior se muestran los distintos valores de Estado de inventario que se suministran con la instalación del software.

El estado de inventario permite o no permite determinados procesos de negocio.

-   Capacidad para crear/modificar/eliminar Estados de inventario con los siguientes atributos:
    -   **Disponible**: inventario que está disponible para reservas y preparación.
    -   **Planificable**: inventario que está disponible para la planificación del suministro futuro (MRP).
    -   **Stock Negativo**: inventario al que se le permite pasar a negativo durante la salida de stock (no durante la preparación).
        -   Nota: no es posible pasar a negativo si existen reservas contra un stock en particular. La reserva siempre se respeta, independientemente del estado de inventario.
-   Añadir un valor de Estado de inventario a cada registro de ubicación o ubicación de almacenamiento.
-   Añadir la posibilidad de actualizar manualmente el Estado de inventario de un Detalle de almacenamiento moviéndolo a una ubicación virtual creada AdHoc.
-   Un nuevo proceso que identifica las reservas afectadas cuando un cambio del estado de inventario reduce/aumenta la cantidad disponible. (Una vez identificadas, los usuarios relevantes podrían recibir una alerta sobre la consecuencia del cambio en la disponibilidad).

### Cambio de estado de inventario

En la ventana Almacén y ubicaciones de almacenamiento, es posible comprobar el Estado de inventario de una Ubicación de almacenamiento y también modificarlo.

Al seleccionar una Ubicación de almacenamiento en esta ventana, es posible comprobar su Estado de inventario actual.

![](../../../assets/drive/J6y4kVfAaNOLqMAlBOJxByWBUkIA-lgdT1RM4HHn2jLkwJhzf0efsUgT78F77DEvT9UT9j_8RCRLnaNFVm-kWhGMRRaYf9thzTnAWN2fvBVsKx4aJX6xc4mb1qPlwH46AUwHc5D3v8Xye_ONWikm3ZKGaCTojkJMeTxkBBoLvSEnXoy_Gp85Ws-FY_1yAQ.png)

Además, al seleccionar una Ubicación de almacenamiento, aparece un botón denominado Cambiar estado. Al hacer clic, es posible seleccionar un Estado de inventario diferente para la Ubicación de almacenamiento seleccionada.

Existen algunas restricciones:

-   Si existen Reservas contra el stock de la Ubicación de almacenamiento, esta Ubicación de almacenamiento no puede cambiarse a un Estado de inventario que no tenga marcada la opción Disponible
-   Si hay stock negativo en la Ubicación de almacenamiento, no es posible cambiar el Estado de inventario a uno que no tenga marcada la opción Stock Negativo

![](../../../assets/drive/tchXpNhj5d5jez97SiLuvXUJJNbHIhHgLfDfU4e2hw2Q5tCqACZLE_daLM920HKiFuYVgQAwZoKpTkdw-pICFn8MVz3Y7TuM04CaWGjxclVXTzqz03ZNxpxj3PWkKwX8KB259JYTGJNeWTIRr1rkzAkaAQppROV4yfDIa6qBWHZVfgJA4xjFO84kb41EjQ.png)

### Ejemplos

Ejemplos de valores de estado de inventario:

-   **Disponible** (YYN -> Disponible, Planificable, No Stock Negativo, Propio/No propio) puede establecerse para todo el inventario que esté libre para ser preparado, para ventas, producción o cualquier otro propósito.
-   **En tránsito** (NYN) no está libre para ser vendido o enviado, pero se espera dentro de un tiempo limitado y, por ello, lo tendremos en cuenta para la planificación.
-   **Cuarentena o bloqueado** (NNN) no está disponible ni es planificable, ya que esperamos una mayor duración de este estado.
-   **Inspección** (NYN) tampoco está disponible, pero se espera que se libere en un tiempo limitado y, por esa razón, es visible para la planificación/MRP.
-   **Consumo retroactivo** (YYY) permitirá pasar a negativo debido a mermas inesperadas en entornos de fabricación.
-   **Público** (YYY) permitirá pasar a negativo debido a stock inesperado en áreas públicas de preparación.
> 
!!! info
    El estado de inventario no tiene efecto sobre el valor del inventario.