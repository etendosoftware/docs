---
title: Informe Pareto de Productos
---

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Pareto de Productos`

## Overview

El Informe Pareto de Productos clasifica los productos en tres categorías — A, B y C — en función de la proporción del valor total del almacén que representa cada producto. Esta técnica se conoce comúnmente como **ABC analysis**, y ayuda a las organizaciones a centrar los esfuerzos de gestión de inventario donde más importan.

Por ejemplo:

| Category | Share of warehouse value | Typical action |
|----------|--------------------------|----------------|
| **A** | ~80 % | Cycle-count weekly, negotiate supplier terms, keep safety stock tight |
| **B** | ~15 % | Cycle-count monthly, standard reorder rules |
| **C** | ~5 %  | Cycle-count yearly, consider consolidation or discontinuation |

!!! info "Prerequisites"
    La clasificación se basa en el coste de cada producto. Antes de ejecutar el informe, asegúrate de que se cumplen los siguientes requisitos:

    - Una [Regla de cálculo de costes](../setup.md#costing-rules) validada para la organización.
    - Costes de **Material Transaction** actualizados (se encuentran en `Gestión de Almacén` > `Transactions` > `Material Transaction`) — estas son las entradas de coste registradas cada vez que el stock entra o sale.

    Si falta alguno de ellos, el informe puede devolver valores cero o resultados incompletos.

## Parameters

Antes de generar el informe, configura los siguientes filtros:

| Field | Description |
|-------|-------------|
| **Organization** | Filtra el informe por la organización seleccionada. |
| **Currency** | Define la moneda en la que se muestran todos los valores monetarios (Cost, Value). Por defecto, usa la moneda del sistema. |
| **Warehouse** | Restringe el informe a un almacén específico dentro de la organización seleccionada. |

!!! warning
    Debe definirse una **Conversión** a la moneda seleccionada para que el informe funcione correctamente. Verifícalo en `General Setup` > `Aplicación` > `Conversion Rates` antes de ejecutar el informe.

Después de establecer los filtros, elige una de las dos acciones:

- **Search** — Muestra los resultados en la misma ventana.
- **View Results** — Abre el informe en una vista separada, lo que puede ser útil para imprimir o comparar lado a lado.

## Report Output

El informe lista cada producto del almacén seleccionado, ordenado por valor descendente, y asigna a cada producto su categoría ABC.

![Pareto Product Report output](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools/pareto-product-report.png)

### Column Reference

| Column | Description |
|--------|-------------|
| **Search Key** | El código identificador único del producto. |
| **Name** | El nombre descriptivo del producto. |
| **Quantity** | El stock actual (cantidad en mano) del producto en el almacén seleccionado. |
| **Unit** | La unidad de medida del producto. |
| **Cost** | El coste unitario del producto (Value total dividido por Quantity). |
| **Value** | El valor total del inventario del producto, calculado como la suma de todos sus costes de transacción de material. |
| **Percentage** | La proporción entre el Value del producto y el valor total del almacén (la suma de todas las líneas del informe). |
| **Category** | La clasificación ABC asignada al producto (A, B o C). Los productos cuyo valor acumulado alcanza hasta el 80 % del total se clasifican como A, los que están entre el 80 % y el 95 % como B, y el resto como C. |

!!! tip "Reading the results"
    Los productos situados en la parte superior de la lista (Categoría A) tienen el mayor impacto individual en el valor del almacén. Prioriza primero la revisión y el control de estos artículos.

## Update ABC

El botón **Update ABC** situado en la parte inferior de la ventana escribe la clasificación de cada producto en el campo **ABC** de la pestaña **Org. Specific** de la ventana de Producto.

- Si ya existe un registro para esa organización, el valor se **actualiza**.
- Si no existe ningún registro, se **crea un nuevo registro**.

Una vez persistida, la categoría ABC queda disponible para filtrar e informar en otras áreas de la aplicación; por ejemplo, al definir reglas de reposición o al generar informes de compras.

!!! tip "When to update"
    Ejecuta el informe y haz clic en **Update ABC** periódicamente — por ejemplo, después de cada ciclo de valoración de inventario o cuando se hayan producido movimientos de stock significativos. Esto mantiene la clasificación alineada con las condiciones actuales del almacén.

## Using Pre-Aggregated Data

Para un mejor rendimiento en entornos de gran volumen, este informe puede reutilizar datos agregados generados previamente por el [Informe de Valuación de Existencias](valued-stock-report.md).

!!! note
    El Informe Pareto de Productos también puede ejecutarse sin datos agregados. Sin embargo, el uso de datos agregados es especialmente útil en entornos de gran volumen en los que se experimentan problemas de rendimiento al lanzar el informe.

---

Este trabajo es una derivación de [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.