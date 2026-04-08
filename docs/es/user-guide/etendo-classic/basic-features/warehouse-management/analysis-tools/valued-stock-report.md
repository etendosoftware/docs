---
title: Informe de Valuación de Existencias
---

## Informe de Valuación de Existencias

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe de Valuación de Existencias`

### **Resumen**

El **Informe de Valuación de Existencias** proporciona una vista completa del inventario mantenido en cada almacén junto con su valor monetario. Es una herramienta esencial para comprender cuánto capital está inmovilizado en existencias, y da soporte a procesos empresariales clave como:

- **Informes financieros**: Determinar el valor total del inventario para balances y cierres de periodo.
- **Conciliación contable**: Comparar las valoraciones de existencias con los asientos del libro mayor para identificar discrepancias.
- **Análisis de costes**: Evaluar los costes unitarios entre productos y almacenes para apoyar decisiones de compra y precios.
- **Visibilidad multi-almacén**: Revisar los valores de existencias en varios almacenes, ya sea consolidados a nivel de organización o desglosados por almacén individual.

La valoración se calcula sumando el coste de cada [transacción de material](../transactions.md) de cada producto en el almacén. Los costes de las transacciones se determinan mediante el proceso [Costing Server](../getting-started.md).

### **Ventana de parámetros**

![Informe de Transacción de Material](../../../../../assets/drive/1HGDsUBdSrfe3_Nzk_ojKq3Ck-aGvIAdx.png)

Antes de generar el informe, configure los siguientes parámetros:

-   **Organización**: Seleccione la organización sobre la que informar. Solo están disponibles las organizaciones de tipo *Legal con Contabilidad* o *Genérica*.
-   **Almacén**: Cuando se selecciona una organización *Genérica*, se listan todos los almacenes pertenecientes a esa organización. Cuando se selecciona una organización *Legal con Contabilidad*, no está disponible la selección de un almacén específico.
-   **Fecha**: El informe muestra la información de inventario hasta esta fecha, incluida.
-   **Almacén consolidado**: Cuando está marcado, la información de existencias se consolida a nivel de organización. Cuando no está marcado, el informe muestra un desglose por almacén individual.
-   **Categoría de producto**: Filtra opcionalmente el informe para mostrar solo los productos pertenecientes a una [categoría](../../master-data-management/product-setup.md#product-category) específica.
-   **Moneda**: Establece la [moneda](../../general-setup/application/currency.md) en la que se muestran todos los valores monetarios (como coste y valoración).

!!! warning
    Debe definirse un [ratio de conversión](../../general-setup/application/conversion-rates.md) a la moneda seleccionada para que el informe se genere correctamente. Verifique que los ratios de conversión de moneda adecuados estén configurados antes de ejecutar el informe.

### **Ventana de salida**

![Informe de Transacción de Material](../../../../../assets/drive/1btCDeLvHaczMWt9lE05E0J8RFjePTZFM.png)

La salida del informe incluye las siguientes columnas:

-   **Producto**: El nombre del producto.
-   **Cantidad**: La cantidad de existencias del producto a la fecha seleccionada.
-   **Unidad de medida**: La unidad de medida en la que se expresa la cantidad de existencias.
-   **Coste Unitario**: El coste por unidad individual. Se calcula dividiendo la valoración total entre la cantidad de existencias.
-   **Valoración**: El valor monetario total de las existencias. Se calcula sumando las valoraciones de todas las transacciones de material que han ocurrido en el almacén para ese producto.
-   **Coste real del algoritmo de promedio/estándar**: El coste de promedio o estándar calculado más recientemente para el producto.
-   **Valoración real del algoritmo de promedio/estándar**: La valoración de existencias basada en el coste actual de promedio o estándar. Se calcula multiplicando la cantidad de existencias por el coste actual.

### **Mejorar el rendimiento del informe (pre-cálculo de datos)**

!!! note
    Este paso es **opcional**. El Informe de Valuación de Existencias funciona sin él. Sin embargo, si su informe tarda mucho en generarse porque su sistema tiene un gran volumen de transacciones, habilitar el pre-cálculo de datos puede reducir significativamente los tiempos de espera.

El sistema puede resumir (precalcular) los datos de inventario de cada [periodo contable](../../financial-management/accounting/setup/openclose-period-control.md) cerrado con antelación, de modo que el informe no tenga que procesar cada transacción individual cada vez que se ejecuta. Para que esta funcionalidad funcione:

- Los periodos contables deben estar definidos en el [Calendario anual y periodos](../../financial-management/accounting/setup/fiscal-calendar.md).
- Al menos algunos periodos deben estar en estado *Cerrado* o *Cerrado permanentemente*.

!!! info
    Para habilitar esta funcionalidad, programe el proceso en segundo plano denominado *Generate Aggregated Data Background* a través de la ventana [Procesamiento de Peticiones](../../general-setup/process-scheduling/process-request.md).

El pre-cálculo cubre todas las transacciones hasta el periodo cerrado más reciente. Las transacciones que ocurren después de ese periodo siguen calculándose en tiempo real. Si existe un largo intervalo de periodos abiertos con muchas transacciones, el informe aún puede experimentar un rendimiento más lento.

La imagen siguiente muestra la ventana de Procesamiento de Peticiones configurada para ejecutar el proceso de pre-cálculo de datos.

![Informe de Valuación de Existencias - ventana de programación de Procesamiento de Peticiones](../../../../../assets/drive/1_mjP-Y6k-QGbCLm8FeIQI08YLJghMAfM.png)

!!! info
    Se recomienda programar este proceso para que se ejecute diariamente durante un periodo de baja actividad del sistema. El proceso solo genera nuevos datos precalculados cuando se ha cerrado o cerrado permanentemente un periodo adicional desde la última ejecución.

#### **Limitaciones**

Cuando el sistema precalcula datos para un periodo cerrado, combina todas las transacciones de ese periodo en un único resumen. No se conserva la fecha original de cada transacción individual.

**Qué significa esto para los informes multimoneda:** Si ejecuta el informe en una moneda distinta de la moneda base de su organización, el sistema convierte los totales precalculados utilizando el tipo de cambio de la fecha de cierre del periodo, no el tipo de cambio de la fecha en que ocurrió originalmente cada transacción.

Como resultado, puede ver pequeñas diferencias en los valores de moneda en comparación con ejecutar el informe sin el pre-cálculo habilitado, donde cada transacción se convertiría al tipo de cambio de su propia fecha.

---

Este trabajo es un derivado de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.