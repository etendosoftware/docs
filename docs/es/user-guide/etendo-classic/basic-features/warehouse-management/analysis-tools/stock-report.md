---
title: Informe Stock
tags:
    - Informe Stock
    - Gestión de Almacén
    - Inventario
    - Niveles de Stock
    - Herramientas de análisis
---

# Informe Stock { #stock-report }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Stock`

## Descripción general { #overview }

El **Informe Stock** muestra los niveles de stock actuales de todos los productos con inventario distinto de cero (incluidas las cantidades disponibles negativas). Los datos se agrupan por categoría de producto, y cada fila muestra el producto, el almacén y la ubicación del hueco. Este informe proporciona una visibilidad rápida de cómo se distribuye el inventario entre almacenes y huecos.

Un hueco es un lugar físico específico dentro de un almacén (por ejemplo, una estantería o un espacio), identificado por una fila, una columna y una altura, de forma similar a una coordenada en un mapa.

Revisar periódicamente el Informe Stock ayuda a mantener la exactitud del inventario y favorece mejores decisiones de compra. Al identificar productos que están bajando de nivel o acumulándose por encima de lo esperado, los usuarios pueden actuar a tiempo para evitar roturas de stock que retrasen las operaciones o situaciones de sobrestock que inmovilicen capital y espacio de almacén. Esto convierte al informe en una herramienta práctica para mantener el inventario alineado con la demanda real del negocio.

## Filtros primarios { #primary-filters }

<figure markdown="span">
  ![Ventana de parámetros del Informe Stock](../../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools/stock-report/stock-report-1.png)
  <figcaption>Ventana de parámetros del Informe Stock</figcaption>
</figure>

El resultado de este informe puede filtrarse utilizando los siguientes parámetros:

-   **Fecha**: Filtra las transacciones hasta la fecha seleccionada.
-   **Categoría de producto**: Limita el informe a una categoría de producto específica.
-   **Producto**: Filtra el informe a un producto específico.
-   **Hueco**: Filtra el informe a un hueco específico seleccionado de la lista.

## Hueco { #storage-bin }

En lugar de seleccionar un hueco de la lista, limite el informe a los huecos de una posición de fila, columna y/o altura específica, las mismas coordenadas que se muestran en la etiqueta del hueco:

-   **Fila (x)**: Posición horizontal del hueco.
-   **Columna (y)**: Posición en profundidad del hueco.
-   **Altura (z)**: Posición vertical del hueco.

## Ver resultados { #view-results }

Tras configurar los filtros deseados, el informe aparece en la sección **Ver resultados**. Expórtelo mediante los botones **Formato HTML**, **Formato PDF** o **Formato Excel**, si es necesario.

<figure markdown="span">
  ![Salida del Informe Stock](../../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools/stock-report/stock-report-2.png)
  <figcaption>Salida del Informe Stock</figcaption>
</figure>

La salida del informe incluye las siguientes columnas:

-   **Artículo**: Nombre o código del producto.
-   **Cantidad**: Cantidad actual disponible.
-   **Unidad**: Unidad de medida del producto.
-   **Atributo**: Características del producto, como tamaño, color o número de lote, si están definidas para el producto.
-   **X**: Posición de fila dentro del hueco (ubicación horizontal).
-   **Y**: Posición de columna dentro del hueco (ubicación en profundidad).
-   **Z**: Posición de altura dentro del hueco (ubicación vertical).
-   **Almacén**: Almacén donde se encuentra el stock.

!!! info
    Las columnas **X**, **Y**, **Z** del informe corresponden a **Fila (x)**, **Columna (y)** y **Altura (z)** del hueco.

---

Este trabajo es una derivación de [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
