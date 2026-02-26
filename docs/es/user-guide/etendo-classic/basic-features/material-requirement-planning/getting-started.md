---
title: Gestión de MRP - Primeros pasos
tags: 
    - Primeros pasos
    - Gestión de MRP
    - Plan de Producción
    - Producto
    - Necesidad
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)

# Gestión de MRP - Primeros pasos

## Visión general

<iframe width="560" height="315" src="https://www.youtube.com/embed/2fGUSzo2ACI?si=h1BqAWPYXf6S1Pnj" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

En Gestión de MRP, la aplicación se utiliza para *revisar automáticamente la demanda y mostrar sugerencias relativas al suministro requerido*. En el *Planificación de la producción*, la aplicación sugiere *Orden de Fabricación* y *Necesidad de material* requeridas. En el *Planificación de compras*, la aplicación sugiere *Pedido de compra* requeridos.

## Gestión de MRP

La Gestión de MRP consta de dos planes:

- Planificación de la producción: plan para mostrar cálculos relacionados con productos que pasan por Producción. Los documentos sugeridos para crear en este plan son la [Orden de Fabricación](../production-management/transactions.md#work-requirement) y la [Necesidad de material](../procurement-management/transactions.md#requisition).
- Planificación de compras: plan para mostrar cálculos relacionados con productos que se aprovisionan. El documento sugerido para crear en este plan es el [Pedido de compra](../procurement-management/transactions.md#purchase-order).

Los **Método de planificación** se introducen para definir qué componentes de suministro se tienen en cuenta en los cálculos de estos planes.

![](../../../../assets/user-guide/etendo-classic/basic-features/material-requirement-planning/mrp0.png)

### **Configuración**

!!!info
    Además de las pantallas de configuración del módulo de MRP que se configuran, se requieren configuraciones adicionales.
    Para los productos que se planifican en el *Planificación de la producción*, se requieren las siguientes configuraciones:

- el [Plan de Producción](../production-management/setup.md#process-plan) está configurado para el producto.
- la *casilla de verificación de producción* y el nombre del Plan de Producción se seleccionan en la pantalla [Producto](../master-data-management/master-data.md#product).
La solapa [Producción](../master-data-management/master-data.md#manufacturing) en la pantalla de Producto se completa con la información requerida para que MRP realice los cálculos para el plan de Planificación de la producción.

Para los productos que se planifican en el *Planificación de compras*, se requieren las siguientes configuraciones:

- la casilla de verificación de compra se selecciona en la pantalla [Producto](../master-data-management/master-data.md#product).
- el [Precio](../master-data-management/master-data.md#price) del producto se define para la lista de precios del proveedor que se introduce en la solapa Compras.
- la solapa [Compras](../master-data-management/master-data.md#purchasing) en la pantalla de Producto se completa con la información requerida para que MRP realice los cálculos para el Planificación de compras.
- el proveedor que se refleja como el Tercero en la solapa Compras mencionada anteriormente se completa en la pantalla de Tercero:

    - solapa [Proveedor/Acreedor](../master-data-management/master-data.md#vendorcreditor) con, al menos, los siguientes campos completados:
        - Lista de precios de compra
        - Método de pago de pedido de compra
        - Condiciones de pago de pedido de compra
    - solapa [Direcciones](../master-data-management/master-data.md#locationaddress)

- La solapa [Producción](../master-data-management/master-data.md#manufacturing) en la pantalla de Producto se completa con la información de *Método de planificación* y *Planificador*.

### **Ejecución** 

El planificador de material introduce una Planificación de la producción para un producto para un determinado período de tiempo y procesa el plan.

En la visión general creada, el *planificador de material revisa y analiza* las líneas. En función de la información procesada por MRP, el plan sugiere *Orden de Fabricación* y *Necesidad de material* para determinadas cantidades y determinadas fechas.

- Si es necesario, se realizan ajustes en las configuraciones, por ejemplo, el método de planificación. Las líneas del plan se recalculan haciendo clic en el botón *Recalcular fechas y cantidades*.
- Si es necesario, se realizan cambios manuales en las líneas creadas en lo relativo a cantidades y fechas.
- Una vez que el plan es correcto, se crean las necesidades de material sugeridas haciendo clic en el botón *Lanzar necesidad de material* y se crean las órdenes de fabricación sugeridas haciendo clic en el botón *Lanzar Orden de Producción*.
- El planificador de material completa la(s) necesidad(es) de material creada(s) y procesa la(s) Orden de Fabricación creada(s).

El planificador de material introduce entonces una Planificación de compras para un producto para un determinado período de tiempo y procesa el plan.
En la visión general creada, el planificador de material revisa y analiza las líneas. En función de la información procesada por MRP, el plan sugiere *Pedido de compra* para determinadas cantidades y determinadas fechas.

- Si es necesario, se realizan ajustes en las configuraciones, por ejemplo, el método de planificación. Las líneas del plan se eliminan y el plan se vuelve a procesar.
- Si es necesario, se realizan cambios manuales en las líneas creadas en lo relativo a cantidades y fechas.
- Una vez que el plan es correcto, se crean los pedidos de compra sugeridos haciendo clic en el botón *Lanzar Orden de Compra*.
- El planificador de material completa el pedido de compra creado.

## Relación con otras áreas

El MRP interactúa con los siguientes módulos:

- [Gestión de Compras](../procurement-management/getting-started.md):
    - [Necesidad de material](../procurement-management/transactions.md#requisition) se crean desde la Planificación de la producción
    - [Pedido de compra](../procurement-management/transactions.md#purchase-order) se crean desde la Planificación de compras
- [Gestión de Ventas](../sales-management/getting-started.md):
    - [Pedido de venta](../sales-management/transactions.md#sales-order) se tienen opcionalmente en cuenta en los cálculos de ambos planes
- [Gestión de Almacén](../warehouse-management/getting-started.md):
    - los [niveles de stock](../warehouse-management/analysis-tools.md#stock-report) se tienen automáticamente en cuenta en los cálculos de ambos planes
- [Gestión de Producción](../production-management/getting-started.md):
    - el [Plan de Producción](../production-management/setup.md#process-plan) se utiliza para el cálculo de la Planificación de la producción
    - [Orden de Fabricación](../production-management/transactions.md#work-requirement) se crean desde la Planificación de la producción

---

- Este trabajo es una obra derivada de [Gestión de MRP](https://wiki.openbravo.com/wiki/Material_Requirement_Planning){target="_blank"} de [Openbravo S.L.U](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, con licencia [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}.