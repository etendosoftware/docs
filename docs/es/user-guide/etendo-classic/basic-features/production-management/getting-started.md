---
title: Gestión de Producción - Primeros pasos
tags: 
 - primeros pasos
 - gestión de producción
 - plan de producción
 - orden de fabricación
 - parte de trabajo
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Gestión de Producción - Primeros pasos

## Visión general

<iframe width="560" height="315" src="https://www.youtube.com/embed/LujFoXYv-XA?si=i8cKV41eHUdipMHh" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

El módulo de Gestión de Producción permite gestionar el proceso productivo estándar: plan de producción, orden de fabricación, informe de productos finales y sus costes directos e indirectos. También es posible gestionar el control de calidad y el mantenimiento de máquinas en producción.

Los principales documentos para gestionar el proceso de producción son:

- [Plan de Producción](./setup.md#process-plan)
- [Orden de Fabricación](./transactions.md#work-requirement)
- [Parte de Trabajo](./transactions.md#work-effort)

!!! tip
    Es importante tener claros estos conceptos y ventanas antes de continuar leyendo. 


![](../../../../assets/drive/1lCJc82jrHhfKt3KS2Eg9SS0aoPpYMsD7.png)

## Configuración inicial

Además de las [ventanas de configuración](./setup.md) del módulo de Producción, se requieren configuraciones adicionales.

1. Para Producción, se configuran diferentes productos:

    - Materia prima utilizada en producción:
        - Se selecciona la casilla de verificación **producción** para indicar que el producto se utiliza para producción.
        - Se selecciona el plan de producción.
        - El almacén por defecto utilizado para almacenar las materias primas utilizadas (P-), se define en la solapa [Producción](../master-data-management/master-data.md#manufacturing).

    - Cualquier **producto semielaborado** se crea directamente en el plan de producción copiando la información de un producto de materia prima utilizado en la operación mediante el botón [Crear copia de producto](./setup.md#io-products). Una vez creado, el almacén por defecto se define en la solapa [Producción](../master-data-management/master-data.md#manufacturing).

    - Productos terminados fabricados en producción:
        - Se selecciona la casilla de verificación **producción** para indicar que el producto se fabrica en producción.
        - Se selecciona el plan de producción.
        - El almacén por defecto que se utiliza para los productos terminados (P+), se define en la solapa [Producción](../master-data-management/master-data.md#manufacturing).
        - En base a los [cálculos de costes](transactions.md#calculate-standard-costs), se puede determinar un coste estándar **teórico** para el producto terminado.
        - Se determina e introduce un nivel de stock de seguridad para el producto.


    !!! info
        Para más información sobre la configuración de productos, consulte la sección [Producto](../master-data-management/master-data.md#product).


2. Asimismo, se configuran Terceros para producción:

    - En la solapa Empleado, cualquier empleado que esté involucrado en el proceso de producción tiene seleccionada la casilla de verificación **operario**.
    - La [Categoría Salarial](../master-data-management/master-data.md#salary-category) configurada para los empleados es muy importante, ya que se incluye en los cálculos de costes finales.

    !!! info
        Para más información sobre la configuración de terceros, consulte la sección [Terceros](../master-data-management/master-data.md#business-partner).

3. Los Partes de Trabajo se pueden contabilizar en el [Diario del libro mayor](../financial-management/accounting/transactions.md#gl-journal). Para facilitar la contabilización, se activa la tabla **MaterialMgmtProductionTransaction** en la solapa [Tablas a contabilizar](../financial-management/accounting/setup/general-ledger-configuration.md) de la configuración del libro mayor.

## Ejecución

1. El personal de ventas introduce el **Pedido de venta** del producto con la cantidad requerida y la fecha en la que debe entregarse. Si el producto no está en stock, debe producirse. Asimismo, si el nivel de stock está por debajo del nivel de stock de seguridad, deben producirse productos.

    La información sobre la demanda procedente de pedidos de venta y el stock de seguridad se gestiona de 2 formas:

    - Automáticamente en [Gestión de MRP (MRP)](../material-requirement-planning/getting-started.md).
    - Manualmente por un responsable de producción.

2. Idealmente, la información se gestiona mediante MRP. Si no es así, un responsable de producción revisa si se requiere la producción del producto revisando la demanda total:

    - Los pedidos de venta pendientes
    - El nivel de stock de seguridad

    y la compara con el suministro total:

    - El nivel de stock.
    - Órdenes de Fabricación planificadas.

3. Si la demanda es superior al suministro, o las fechas de las Órdenes de Fabricación planificadas no coinciden con las fechas de los pedidos de venta pendientes, el producto debe producirse y un responsable de producción ejecuta:

    - Revisión del stock de la materia prima. Si es necesario, la materia prima se solicitará y se utilizará en el proceso de [Gestión de Compras](../procurement-management/getting-started.md).
    - Introducción de la **Orden de Fabricación** para la cantidad requerida con la cantidad requerida y la fecha planificada.
    - Generación de **Partes de Trabajo** a partir de la Orden de Fabricación.

4. El personal responsable de ejecutar la producción puede ver en el **Informe Partes de Fabricación** qué producción debe ejecutarse.

5. Al final de cada turno, los responsables de producción introducen la información de lo que se ha producido en las ventanas de [Parte de Fabricación](transactions.md#production-run-1).

## Relación con otras áreas

Gestión de Producción interactúa con los siguientes módulos:

- [Gestión de Compras](../procurement-management/getting-started.md): la materia prima necesaria para su uso en producción se compra utilizando el proceso de aprovisionamiento a pago.
- [Gestión de Ventas](../sales-management/getting-started.md): la demanda de los productos que se producen se genera a través del proceso de pedido a cobro.
- [Gestión de Almacén](../warehouse-management/getting-started.md):
    - La materia prima se retira del almacén para utilizarse en producción
    - Los productos finales que salen de producción se introducen en stock
- [Gestión de MRP](../material-requirement-planning/getting-started.md): las Órdenes de Fabricación pueden ser el resultado de MRP
- [Gestión Financiera](../financial-management/getting-started.md): el coste relacionado con Producción se calcula para finanzas.

---

- Este trabajo es una obra derivada de [Gestión de Producción](http://wiki.openbravo.com/wiki/Production_Management){target="_blank"} de [Openbravo S.L.U](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, con licencia [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}.

- Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.