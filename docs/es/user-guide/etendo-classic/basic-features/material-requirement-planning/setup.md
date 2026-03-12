---
title: Configuración de Gestión de MRP
tags:
    - Gestión de MRP
    - Método de planificación
    - Planificación de la producción
    - Planificación de compras
    - Configuración del Planificador
---
## Visión general

Para iniciar el proceso de Gestión de MRP (MRP), deben configurarse las secciones Método de planificación y Planificador:

!!! info
    Para ello, se requieren configuraciones adicionales. Consulte la información en la [sección Visión general del módulo de MRP](../../../../user-guide/etendo-classic/basic-features/material-requirement-planning/transactions.md).

## Método de planificación

:material-menu: `Aplicación` > `Gestión de MRP` > `Configuración` > `Método de planificación`

### Visión general

Defina cómo se tratarán los tipos de transacción en la aplicación.

Un Método de planificación se utiliza para definir los **componentes opcionales de oferta y demanda y su porcentaje a tener en cuenta** durante la ejecución del proceso de MRP, creando la **Planificación de la producción** y la **Planificación de compras**. Cada producto que se planifica en la Planificación de la producción o en la Planificación de compras tiene un Método de planificación definido en la configuración del producto.

Por **valor por defecto**, MRP tiene en cuenta el **stock** y el **stock mín.** al crear los planes, pero las siguientes transacciones son opcionales y se configuran en el Método de planificación:

-   **Necesidad de material**: demanda del producto en necesidades de material en estado completado.
!!! info
    Para más detalles, consulte la sección [_Necesidad de material_](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#requisition).

- **Previsión de ventas**: previsión de demanda futura del producto.
!!! info
    Para más detalles, consulte la sección [_Previsión de ventas_](../../../../user-guide/etendo-classic/basic-features/material-requirement-planning/transactions.md#mrp-forecast).

-   **Pedido de venta pendiente**: demanda del producto en pedidos de venta en estado reservado que aún no se han enviado.
!!! info
    Para más detalles, consulte la sección [_Pedido de venta_](../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order).

-   **Fases de OF a realizar**: oferta del producto en una orden de fabricación procesada.
!!! info
    Para más detalles, consulte la sección [_Orden de Fabricación_](../../../../user-guide/etendo-classic/basic-features/production-management/transactions.md#work-requirement).

-   **Pedido de compra pendiente**: oferta del producto en un pedido de compra reservado que aún no se ha recibido.
!!! info
    Para más detalles, consulte la sección [_Pedido de compra_](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order).

### Cabecera

Utilice la cabecera para crear un método de planificación.

En esta solapa, se introducen la organización y el **nombre del método de planificación**. Se puede introducir un método de planificación general para incluir todos los componentes de la demanda y la oferta opcionales, ya que cualquier componente que no sea aplicable para un producto determinado simplemente no aparecerá en el plan, mientras que cualquier componente que se omita por error dará lugar a cálculos incorrectos e incompletos del plan.

![](../../../../assets/drive/r-sIhmWnmoYNZsemrEKq3Il7LQsg1iDrcrq5K3H2HprddfyVZa7wiE5nmb6uaDHTpzSWHiHnvCetwhHQ_RBq1NJP3cIv17F96ZxBnqmyeWowc_zmB432U68KEEtdZbheLdRHdx9w00xaewhcEybYe4E.png)

### Líneas

Añada transacciones para incluirlas en su plan. Cada transacción se muestra en su propia línea.

En esta solapa, las transacciones aplicables se introducen en líneas separadas. Para cada tipo de transacción, es posible definir si las transacciones se consideran para todo el **horizonte** en la Planificación de la producción y la Planificación de compras o solo para una parte:

-   **días desde**: el número de días desde el inicio del horizonte hasta el inicio del intervalo temporal de la transacción que se está considerando.
-   **días hasta**: el número de días desde el inicio del horizonte hasta el final del intervalo temporal de la transacción que se está considerando.

Además, se configura un porcentaje de la cantidad a considerar por MRP con el **Porcentaje**. Si se introduce una previsión de ventas de 100 unidades con un porcentaje de 0.9, solo 90 unidades se reflejan en la Planificación de la producción o en la Planificación de compras. Del mismo modo, se puede introducir un valor superior a 1 para incluir un número mayor en los planes.

![](../../../../assets/drive/r3xp-vXHNSPnrw9FA7ashqCDRgL0s5LE9i_8sNTRssgBQiOX5bDavCyyxMCmCXIUKzvbPdxvrp6wkfXKLFftUwcqNn3u57H56hpHgKp4z0YkfjBobN-fV1M_gGf09M7MyrjutIBaZzR40_IdhQn8fb0.png)

## Planificador

:material-menu: `Aplicación` > `Gestión de MRP` > `Configuración` > `Planificador`

### Visión general

Defina la entidad encargada de gestionar la compra o la producción de productos específicos.

Un **filtro opcional tanto en la Planificación de la producción como en la Planificación de compras** es el planificador. La información que se introduce en esta pantalla no tiene relación con la configuración del tercero. Después de crear el planificador, la información del planificador se introduce en la solapa [Producto](../master-data-management/master-data.md#product) en la sección de Gestión de datos maestros.

### Planificador

Defina el planificador encargado de gestionar la compra o la producción de productos específicos.

![](../../../../assets/drive/2IK-YKaAHZYtnh4V1r_P9QgY4oU3-wDlu73TD8YZffxiibZ-JWkhjD_fCnJLzntBSgBhJSLbMx3IOsYOPFoDahYodIPGEq1P8LytGAg9aCEylB2iknxNfhnwCH8MgxgF1F6CYXVQxBPfF7KuArrucc4.png)

---

- Este trabajo es una obra derivada de [Material_Requirement_Planning](https://wiki.openbravo.com/wiki/Material_Requirement_Planning){target="_blank"} de [Openbravo S.L.U](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, con licencia [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}.