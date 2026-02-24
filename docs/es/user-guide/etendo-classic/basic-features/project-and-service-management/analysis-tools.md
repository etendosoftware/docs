---
title: Herramientas de análisis de Gestión de Proyectos y Servicios
tags: 
    - Proyecto multifase
    - Servicio
    - Servicios y gastos planificados
    - Herramientas de análisis
    - Progreso de Proyectos
    - Informe de gastos
    - Gastos no reembolsados
---

# Herramientas de análisis de Gestión de Proyectos y Servicios

## Visión general

Esta sección describe las ventanas relacionadas con los informes de gestión de proyectos y servicios en Etendo. Estas son:

[:material-file-document-outline: Progreso de Proyectos](#progreso-de-proyectos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Rentabilidad de Proyectos](#rentabilidad-de-proyectos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe de gastos](#informe-de-gastos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Gastos para facturar](#gastos-para-facturar){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Gastos no reembolsados](#gastos-no-reembolsados){ .md-button .md-button--primary } <br>

## Progreso de Proyectos

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Herramientas de análisis` > `Progreso de Proyectos`

El informe **Progreso de Proyectos** permite realizar el seguimiento del progreso de los proyectos con indicadores útiles como el tiempo consumido o el porcentaje de finalización. Se utiliza para supervisar los plazos de los proyectos.

La información principal que se puede obtener del informe es:

- días de retraso para cada tarea y cada fase
- retraso acumulado para todo el proyecto

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/analysis-tools/project-progress.png)

## Rentabilidad de Proyectos

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Herramientas de análisis` > `Rentabilidad de Proyectos`

El informe **Rentabilidad de Proyectos** se utiliza para supervisar el coste planificado y el coste real relacionados con un proyecto.

En el informe se muestra la siguiente información:

**Servicios y gastos planificados**:

- Ingresos: el importe del campo *Service Revenue* en el proyecto multifase.
- Coste: el importe del campo *Services Provided Cost* en el proyecto multifase.
- Subcontratación: el importe del campo *Outsourced Cost* en el proyecto multifase.
- Margen%: el margen del campo *Planned Service Margin %* en el proyecto multifase. El % de margen del servicio planificado se calcula usando la fórmula: (Service Revenue - Services Provided Cost - Outsourced Cost) x 100/Service Revenue.
- Refacturación: el importe del campo *Reinvoiced Expenses* en el proyecto multifase.
- Gastos: el importe del campo *Planned Expenses* en el proyecto multifase.
- Margen%: el margen del campo *Planned Expenses Margin %* en el proyecto multifase. El % de margen de gastos planificados se calcula usando la fórmula: (Reinvoiced Expenses - Planned Expenses) x 100/Reinvoiced Expenses.
- Margen bruto: margen planificado global del proyecto
    - Importe del margen bruto: calculado usando la fórmula: (Service Revenue - Services Provided Cost - Outsourced Cost) + (Reinvoiced Expenses - Planned Expenses).
    - Porcentaje de margen bruto: calculado usando la fórmula: ((Service Revenue - Services Provided Cost - Outsourced Cost) + (Reinvoiced Expenses - Planned Expenses)) x100/(Service Revenue + Reinvoiced Expenses)

Servicios y gastos reales:

- Ingresos: coste reflejado en las facturas de venta al cliente para:
    - refacturación de trabajo subcontratado por un tercero.
    - facturación del coste de fases del proyecto completadas.
    - solo se tendrán en cuenta las líneas de factura de venta con productos de tipo servicio.
- Coste: coste de las horas trabajadas basado en partes de horas procesados multiplicado por el coste que está vinculado a la categoría salarial del empleado en la fecha del gasto.
- Subcontratación: coste de las horas trabajadas ejecutadas por un tercero basado en facturas de compra.
- Margen%: margen real de servicios basado en la fórmula: (Ingresos - Coste - Subcontratación) x 100/Ingresos
- Refacturación: gastos facturados al cliente en facturas de venta para:
    - bienes comprados relacionados con el proyecto.
    - gastos de artículos facturables.
    - solo se tendrán en cuenta las líneas de factura de venta con productos cuyo tipo no sea servicio.
- Gastos: gastos reales basados en facturas de compra para:
    - bienes comprados relacionados con el proyecto a un proveedor.
    - reembolso de gastos de artículos para un empleado.
- Margen%: margen real de gastos basado en la fórmula: (Refacturación - Gastos) x 100/Refacturación
- Margen bruto: margen real global del proyecto.
    - Importe del margen bruto: calculado usando la fórmula: (Ingresos - Coste - Subcontratación) + (Refacturación - Gastos)
    - Porcentaje de margen bruto: calculado usando la fórmula: ((Ingresos - Coste - Subcontratación) + (Refacturación - Gastos)) x 100/(Ingresos + Refacturación)
- Cobrado: importe que se cobró al cliente por las facturas de venta relacionadas con el proyecto.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/analysis-tools/project-profitability.png)

## Informe de gastos

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Herramientas de análisis` > `Informe de gastos`

El **Informe de gastos** muestra un listado de hojas de gastos con sus detalles. Se pueden aplicar filtros para mostrar informes de gastos para determinados terceros, proyectos o empleados. También se puede aplicar un filtro para seleccionar partes de horas u hojas de gastos.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/analysis-tools/expense-report.png)

## Gastos para facturar

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Herramientas de análisis` > `Gastos para facturar`

En esta ventana, el usuario puede ver los gastos antes de facturarlos a los clientes. Esta es una vista de solo lectura de todos los costes facturables relacionados con proyectos. Los costes que aparecen están marcados como refacturación en hojas de gastos que están procesadas. Todos los elementos que se muestran son para facturar a los clientes relacionados con los proyectos.

Cliente

En la vista de cuadrícula se lista una visión general de todos los clientes a los que se deben facturar gastos relacionados con proyectos. En los registros se muestran la Tarifa y las Condiciones de pago que se utilizarán para la creación del Pedido de venta.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/analysis-tools/invoiceable-expenses.png)

### Solapa Líneas

En esta solapa, el usuario puede ver cada línea de gasto que se incluirá en la factura de venta.

La información mostrada en la solapa de líneas se toma de la solapa de líneas de las Hojas de gastos. Todas las líneas están relacionadas con el tercero seleccionado, pero distintas líneas pueden estar relacionadas con distintos proyectos.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/analysis-tools/invoiceable-expenses-lines.png)

## Gastos no reembolsados

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Herramientas de análisis` > `Gastos no reembolsados`

En esta ventana, el usuario puede ver los gastos internos de empleados antes de procesarlos. Esta es una vista de solo lectura de todos los gastos que deben reembolsarse a un empleado.

Empleado

En la vista de cuadrícula se lista una visión general de todos los empleados que tienen gastos pendientes de reembolso. En cada registro se muestran la Tarifa de compra y las Condiciones de pago del pedido de compra, que se utilizarán para la creación de la Factura de compra.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/analysis-tools/employee-expenses.png)

### Solapa Líneas

En esta solapa, el usuario puede ver cada línea de gasto del empleado.

La información mostrada en la solapa de líneas se toma de la solapa de líneas de la Hoja de gastos. Todas las líneas están relacionadas con el empleado, pero distintas líneas pueden estar relacionadas con distintos proyectos.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/analysis-tools/employee-expenses-lines.png)

---

Este trabajo es una obra derivada de [Gestión de Proyectos y Servicios](https://wiki.openbravo.com/wiki/Project_and_Service_Management){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.