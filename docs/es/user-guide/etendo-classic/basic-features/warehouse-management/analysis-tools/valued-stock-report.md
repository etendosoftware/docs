---
title: Informe de Valuación de Existencias

tags:
    - Valued Stock
    - Inventory
    - Warehouse Management
    - Cost Analysis
    - Financial Reporting
---

# Informe de Valuación de Existencias

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe de Valuación de Existencias`

## Overview

El **Informe de Valuación de Existencias** proporciona una vista completa del inventario mantenido en cada almacén junto con su valor monetario. Es una herramienta esencial para comprender cuánto capital está inmovilizado en existencias, apoyando procesos empresariales clave como:

- **Financial reporting**: Determinar el valor total del inventario para balances y cierres de período.
- **Accounting reconciliation**: Comparar las valoraciones de existencias con los asientos del libro mayor para identificar discrepancias.
- **Cost analysis**: Evaluar los costes unitarios entre productos y almacenes para apoyar decisiones de compra y precios.
- **Multi-warehouse visibility**: Revisar los valores de existencias en varios almacenes, ya sea consolidados a nivel de organización o desglosados por almacén individual.

La valoración se calcula sumando el coste de cada [transacción de material](../transactions.md) de cada producto en el almacén. Los costes de las transacciones se determinan mediante el proceso [Costing Server](../getting-started.md).

## Parameters Window

![Valued Stock Report Parameters Window](../../../../../assets/drive/1HGDsUBdSrfe3_Nzk_ojKq3Ck-aGvIAdx.png)

Antes de generar el informe, configure los siguientes parámetros:

-   **Organización**: Seleccione la organización sobre la que informar. Solo están disponibles las organizaciones de tipo *Legal with Accounting* o *Generic*.
-   **Almacén**: Cuando se selecciona una organización *Generic*, se listan todos los almacenes que pertenecen a esa organización. Cuando se selecciona una organización *Legal with Accounting*, no hay disponible una selección específica de almacén.
-   **Fecha**: El informe muestra la información de inventario hasta esta fecha, inclusive.
-   **Consolidated Warehouse**: Cuando se marca, la información del stock se consolida a nivel de organización. Cuando no se marca, el informe muestra un desglose por almacén individual.
-   **Categoría del Producto**: Filtra opcionalmente el informe para mostrar solo productos pertenecientes a una [categoría](../../master-data-management/product-setup.md#product-category) específica.
-   **Moneda**: Define la [moneda](../../general-setup/application/currency.md) en la que se muestran todos los valores monetarios (como coste y valoración).

!!! warning
    Debe definirse un [tipo de cambio](../../general-setup/application/conversion-rates.md) a la moneda seleccionada del informe para que este se genere correctamente. Verifique que los tipos de cambio de moneda adecuados estén configurados antes de ejecutar el informe.

## Output 

![Valued Stock Report Output](../../../../../assets/drive/1btCDeLvHaczMWt9lE05E0J8RFjePTZFM.png)

La salida del informe incluye las siguientes columnas:

-   **Producto**: El nombre del producto.
-   **Cantidad**: La cantidad de stock del producto a la fecha seleccionada.
-   **Unidad de medida**: La unidad de medida en la que se expresa la cantidad de stock.
-   **Coste Unitario**: El coste por unidad individual. Se calcula dividiendo la valoración total entre la cantidad de stock.
-   **Valoración**: El valor monetario total del stock. Se calcula sumando las valoraciones de todas las transacciones de material que han tenido lugar en el almacén para ese producto.
-   **Actual Average/Standard Algorithm Cost**: El coste medio o estándar más recientemente calculado para el producto.
-   **Actual Average/Standard Algorithm Valuation**: La valoración del stock basada en el coste medio o estándar actual. Se calcula multiplicando la cantidad de stock por el coste actual.

## Improving Report Performance (Data Pre-Calculation)

!!! note
    Este paso es **opcional**. El Informe de Valuación de Existencias funciona sin él. Sin embargo, si su informe tarda mucho en generarse porque su sistema tiene un gran volumen de transacciones, habilitar el precálculo de datos puede reducir significativamente los tiempos de espera.

El sistema puede resumir (precálcular) los datos de inventario para cada [período contable](../../financial-management/accounting/setup/openclose-period-control.md) cerrado con antelación, de modo que el informe no tenga que procesar cada transacción individual cada vez que se ejecuta. Para que esta funcionalidad funcione:

- Los períodos contables deben estar definidos en el [Calendario anual y periodos](../../financial-management/accounting/setup/fiscal-calendar.md).
- Al menos algunos períodos deben estar en estado *Cerrado* o *Cerrado permanentemente*.

!!! info
    Para habilitar esta funcionalidad, programe el proceso en segundo plano llamado *Generate Aggregated Data Background* a través de la ventana [Procesamiento de Peticiones](../../general-setup/process-scheduling/process-request.md).

El precálculo cubre todas las transacciones hasta el período cerrado más reciente. Las transacciones que ocurren después de ese período siguen calculándose en tiempo real. Si existe un largo tramo de períodos abiertos con muchas transacciones, el informe aún puede experimentar un rendimiento más lento.

La siguiente imagen muestra la ventana de Procesamiento de Peticiones configurada para ejecutar el proceso de precálculo de datos.

![Valued Stock Report - Process Request scheduling window](../../../../../assets/drive/1_mjP-Y6k-QGbCLm8FeIQI08YLJghMAfM.png)

!!! info
    Se recomienda programar este proceso para que se ejecute diariamente durante un período de baja actividad del sistema. El proceso solo genera nuevos datos precalculados cuando se ha cerrado o cerrado permanentemente un período adicional desde la última ejecución.

### Limitations

Cuando el sistema precalcula datos para un período cerrado, combina todas las transacciones de ese período en un único resumen. No se conserva la fecha original de cada transacción individual.

**What this means for multi-currency reports:** Si ejecuta el informe en una moneda diferente de la moneda base de su organización, el sistema convierte los totales precalculados utilizando el tipo de cambio de la fecha de cierre del período, no el tipo de cambio de la fecha en que ocurrió originalmente cada transacción.

Como resultado, puede ver pequeñas diferencias en los valores de moneda en comparación con ejecutar el informe sin el precálculo habilitado, donde cada transacción se convertiría con el tipo de cambio de su propia fecha.

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.