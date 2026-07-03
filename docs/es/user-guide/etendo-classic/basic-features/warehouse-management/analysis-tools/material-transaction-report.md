---
title: Informe Transacción de Material
tags:
    - Informe Transacción de Material
    - Gestión de Almacén
    - Inventario
    - Transacciones
    - Herramientas de análisis
---

# Informe Transacción de Material { #material-transaction-report }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Transacción de Material`

## Descripción general { #overview }

El **Informe Transacción de Material** proporciona una vista consolidada de todos los movimientos de material registrados en el sistema, incluidas las expediciones salientes y las recepciones entrantes. Las transacciones se agrupan por Tercero —el cliente o proveedor involucrado en la transacción— y por documento, lo que facilita identificar qué productos se enviaron o recibieron, en qué cantidades y a través de qué almacén.

Este informe es útil para:

- Realizar el seguimiento de los movimientos de material entrantes y salientes durante un período específico.
- Auditar las transacciones de inventario para verificar que las expediciones y recepciones coincidan con las cantidades esperadas.
- Conciliar documentos por Tercero para garantizar la integridad y exactitud de las transacciones registradas.

Para generar el informe:

1. Configure los filtros deseados en la sección **Filtro**.
2. El informe aparece en la sección **Ver resultados**.
3. Exporte el informe mediante los botones **Formato HTML** o **Formato PDF**, si es necesario.

## Filtro { #filter }

Los siguientes parámetros permiten filtrar los datos incluidos en el informe:

-   **Fecha desde** / **Fecha hasta**: Define el rango de fechas del informe. Solo aparecen las transacciones que se hayan producido dentro de este rango.
-   **Tercero**: Filtra las transacciones por un proveedor o cliente específico. Déjelo vacío para incluir las transacciones de todos los terceros.
-   **Almacén**: Restringe el informe a las transacciones que se hayan producido en el almacén seleccionado.
-   **Proyecto**: Filtra las transacciones asociadas a un código de proyecto específico, utilizado cuando la organización realiza el seguimiento de costos o transacciones por proyecto, por ejemplo una obra de construcción o un contrato de servicio. Déjelo vacío para incluir todos los proyectos.

Tras configurar los filtros deseados, el informe aparece en la sección **Ver resultados**. Expórtelo mediante los botones **Formato HTML** o **Formato PDF**, si es necesario.

<figure markdown="span">
  ![Ventana de parámetros del Informe Transacción de Material](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools/material-transaction-report/material-transaction-report-1.png)
  <figcaption>Ventana de parámetros del Informe Transacción de Material</figcaption>
</figure>

### Ver resultados { #view-results }

La salida del informe se organiza por **Tercero** y, dentro de cada tercero, por número de documento, que aparece como encabezado de sección, por ejemplo *Albarán (Cliente) 1000425*. Para cada línea de transacción, se muestran las siguientes columnas:

-   **Fecha del movimiento**: La fecha en que se registró la transacción.
-   **Producto**: El nombre del producto involucrado en la transacción.
-   **Almacén**: El almacén donde tuvo lugar la transacción.
-   **Hueco**: La ubicación específica (estante, rack o sección) dentro del almacén donde se almacenó o retiró el producto.
-   **Cantidad**: La cantidad del producto movida en la transacción, junto con su unidad de medida.

<figure markdown="span">
  ![Salida del Informe Transacción de Material](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools/material-transaction-report/material-transaction-report-2.png)
  <figcaption>Salida del Informe Transacción de Material</figcaption>
</figure>

---

Este trabajo es una derivación de [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
