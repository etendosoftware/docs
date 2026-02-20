---
title: Informes de Almacén
---
## Visión general

Esta sección describe las ventanas relacionadas con los informes de almacén en Etendo. Estas son:


[:material-file-document-outline: Informe Pareto de Productos](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#pareto-product-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe Transacción de Material](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#material-transaction-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe Stock](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#stock-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Historial de stock](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#stock-history){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe de Valuación de Existencias](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#valued-stock-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe Movimiento de Productos](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#product-movements-report){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Operaciones de producto](../../../../user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools.md#product-operations){ .md-button .md-button--primary } <br>

## Informe Pareto de Productos

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Pareto de Productos`

### **Visión general**

**Informe Pareto de Productos** distribuye los productos en tres clases (A, B o C) según el valor de coste que el inventario de cada producto tiene en el almacén. En base a esta clasificación se puede decidir la frecuencia del ciclo de recuento (p. ej., los productos A se cuentan semanalmente, los productos B mensualmente y los productos C anualmente).

Se utiliza la siguiente distribución: los productos A representan el 80% del valor del almacén, los B el 15% y los C el 5%.
> 
!!! info
    La clasificación se basa en el coste del producto. Por eso es necesario tener una Regla de Coste validada y los costes de las transacciones de material del producto calculados y actualizados.

### **Ventana de parámetros**

El campo **Moneda** define la moneda en la que se muestran todos los valores monetarios (como **Costo**, **Costo**) del informe. El campo toma por defecto la moneda del sistema.

!!! warning
    Tenga en cuenta que deben especificarse los **Rangos** a la **Moneda** del informe para que el informe funcione.

El botón **Actualizar ABC** completa el campo **ABC** (actualiza el valor si el registro existe o crea un nuevo registro en caso contrario) de la pestaña específica de organización de la ventana **Producto** para las organizaciones del resultado del informe.

### **Salida de informe de ejemplo**

![Material Transaction Report](../../../../assets/drive/1DpBnQAG8Xyk9rM5xKhQvdKNt8p-bm4tj.png)

Columnas a tener en cuenta:

-   **Cantidad:** es el stock actual del producto (cantidad disponible) en el almacén seleccionado.
-   **Costo:** es la suma de todos los costes de las transacciones de material del producto.
-   **Costo:** este coste se calcula como la relación entre el valor del producto y la cantidad del producto indicada arriba.
-   **Porcentaje:** este porcentaje es la relación entre el valor del producto y el Valor Total del almacén (que es la suma de todas las líneas del informe).

### **Información persistida**

Se puede utilizar la información agregada calculada para el stock valorado. Consulte la documentación del Informe de Valuación de Existencias para obtener más detalles sobre cómo generar la información agregada.

!!! note
    Exactamente igual que para el Informe de Valuación de Existencias, el Informe Pareto de Productos también puede ejecutarse sin datos agregados. Sin embargo, esta funcionalidad es especialmente útil en entornos de alto volumen cuando se experimentan problemas de rendimiento al ejecutar el informe.

## Informe Transacción de Material

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Transacción de Material`

El Informe Transacción de Material lista todos los documentos (albaranes de salida y recepciones de entrada) agrupados por Tercero y documento. Para cada número de documento se muestran los datos, el producto, el almacén, el hueco y la cantidad.

### Parámetros de la ventana

La información de este informe puede filtrarse utilizando la fecha de movimiento, el tercero, el almacén y el proyecto. Los informes pueden generarse en formato HTML y PDF.

![Material Transaction Report](../../../../assets/drive/1B8aETuwl82fGlqe_SQLX3VAFz_2x6Tv2.png)

### Salida de informe de ejemplo

![Material Transaction Report](../../../../assets/drive/1DxL6-LHWr4QxeYT1F1y0SbAT3-szlkGW.png)

## Informe Stock

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Stock`

El Informe Stock muestra el nivel de stock de todos los productos (que tienen cantidad disponible distinta de cero) y su ubicación (almacén y hueco) agrupados por categoría del producto. Para cada fila se muestra producto, cantidad, unidad, atributo, estanterías, columna, altura y almacén.

### **Ventana de parámetros**

El resultado de este informe puede filtrarse utilizando la fecha de movimiento, la categoría del producto, el producto y los localizadores del almacén.

![Material Transaction Report](../../../../assets/drive/1OgkmMsGjuADw-Sbqn1tfJ5WkCbq_AGx5.png)

El resultado de este informe puede visualizarse en formato HTML y PDF.

Los campos **Estanterías (x)**, **Columna (y)**, **Altura (z)** corresponden a **Estantería (X)**, **Columna (Y)** y **Altura (Z)** del Hueco.

**Salida de informe de ejemplo**

![Material Transaction Report](../../../../assets/drive/1jjN-TjQjeY-38odbT6xBRYCpACEmMUxz.png)

## Historial de stock

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Historial de stock`

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).
 

Esta es una ventana de solo lectura en la que el usuario puede consultar el stock diario. Esta funcionalidad actualiza la información diaria recopilada por el proceso en segundo plano que se creó previamente para este propósito.

La ventana Historial de stock se completa únicamente mediante el proceso en segundo plano "Crear Historial de stock". Puede programarse desde la ventana 'Procesamiento de Peticiones', donde se puede asignar para qué rol y organización se ejecuta, y la periodicidad con la que se ejecuta.

!!! info
    Consulte la documentación técnica sobre Historial de stock para ampliar el proceso y calcular los registros del historial de stock diario.

No se mostrará ningún dato en la ventana hasta que se apliquen filtros de búsqueda. Una vez aplicados los filtros, haga clic en el botón de la derecha para completar el proceso.

![](../../../../assets/drive/10C8VIJpu2FJkojmrZ8aKCZMZo0D0OpMJ.png)

La ventana muestra los siguientes campos desde los cuales el usuario puede filtrar y obtener los datos necesarios:
- Fecha de stock
- Producto
- Valor del conjunto de atributos
- Almacén
- Hueco
- Cantidad disponible
- Cantidad reservada
- Cantidad asignada
- Cantidad en transacción en borrador
 
![](../../../../assets/drive/1MhFI0Ii9bhm8EBBK-UalKWK90_-Gkm_G.png)

Esta funcionalidad incluye un proceso para cerrar el stock y guardar la información histórica.

## Informe de Valuación de Existencias

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe de Valuación de Existencias`

### **Visión general**

El Informe de Valuación de Existencias muestra el stock de un almacén en particular así como el valor del stock.

El coste se calcula como la suma del coste de cada transacción de material del producto en el almacén. El coste de las transacciones del producto se calcula mediante el proceso Costing Server.

### **Ventana de parámetros**

![Material Transaction Report](../../../../assets/drive/1HGDsUBdSrfe3_Nzk_ojKq3Ck-aGvIAdx.png)

-   **Organización**: Este campo permite al usuario seleccionar entre organizaciones de tipo "Legal con contabilidad" y "Genérica".
-   **Almacén**: Si la organización seleccionada es "Genérica", entonces lista todos los almacenes que pertenecen a ella; en cambio, si la organización es "Legal con contabilidad", entonces no se muestra ningún almacén para seleccionar.
-   **Fecha**: El informe mostrará información hasta la fecha seleccionada.
-   **Almacén consolidado**: Si está marcado, la información del stock se consolidará a nivel de organización; en caso contrario, la información se desglosará por almacén.
-   **Categoría del producto**: Permite mostrar información solo de la categoría del producto seleccionada.
-   **Moneda**: Define la moneda en la que se muestran todos los valores monetarios (como coste, **Valoración**) del informe.

!!! warning
    Tenga en cuenta que deben especificarse los Rangos a la Moneda del informe para que el informe funcione.

### **Ventana de salida** 

![Material Transaction Report](../../../../assets/drive/1btCDeLvHaczMWt9lE05E0J8RFjePTZFM.png)

-   **Producto**: Nombre del producto.
-   **Cantidad**: Stock del producto en la fecha seleccionada.
-   **Unidad**: Unidad en la que se mide el stock.
-   **Coste Unitario**: Coste de cada unidad en particular. Es el resultado de dividir la **Valoración** entre el stock.
-   **Valoración**: Valoración del stock. Se calcula sumando todas las valoraciones de cada transacción que ha ocurrido en el almacén.
-   **Coste del algoritmo actual promedio/estándar**: Coste promedio/estándar actual, el último cálculo de su valor.
-   **Valoración del algoritmo actual promedio/estándar**: Valoración del stock basada en el coste actual promedio/estándar. Es el resultado de multiplicar el stock por el coste actual.

### **Información persistida**

Este paso no es necesario para ejecutar el informe. Sin embargo, si existen problemas de rendimiento, esto puede ayudar a mejorar considerablemente el rendimiento del informe.

Es posible agregar información que permita consultas más rápidas. Esta información se agrega para cada período contable cerrado, lo que significa que deben definirse períodos contables y, al menos algunos de ellos, deben estar en estado *Cerrado* o *Cerrado permanentemente*.

La información persistirá hasta el primer período no cerrado. De este modo, es posible evitar recorrer muchos registros. Sin embargo, no se agregará información después del primer período cerrado y esto puede dar como resultado un rendimiento no óptimo del informe si necesita recuperar mucha información.

!!! info
    Para utilizar esta funcionalidad es necesario programar el proceso en segundo plano denominado *Generate Aggregated Data Background*. Esto puede hacerse a través de la ventana *Procesamiento de Peticiones*.

![Material Transaction Report](../../../../assets/drive/1_mjP-Y6k-QGbCLm8FeIQI08YLJghMAfM.png)

!!! info
    Se recomienda programarlo diariamente, en un momento en el que el sistema no tenga mucha actividad. Solo agregará datos cuando un nuevo período se cierre o se cierre permanentemente.

### **Limitaciones**

Al agregar la información por cada período cerrado, no es posible conservar la fecha de cada transacción. Por lo tanto, cuando el informe se ejecuta para una moneda diferente, toda esa información se convertirá a la fecha de cierre del período. Esto puede dar lugar a discrepancias menores con la versión anterior debido a conversiones entre monedas en fechas diferentes.

## Informe Movimiento de Productos

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Informe Movimiento de Productos`

El Informe Movimiento de Productos muestra todas las recepciones, envíos, movimientos e inventarios físicos agrupados por tipo de transacción y tercero. Para cada fila se muestran el número de documento, la fecha, la descripción, los localizadores y la cantidad.

### Ventana de parámetros

El resultado de este informe puede filtrarse utilizando la fecha de movimiento, el producto, el atributo y el tercero.

Adicionalmente, el usuario puede incluir o excluir estos documentos:

-   Envío/Recepción
-   Inventario físico
-   Movimientos de inventario
-   y Producción.

![Product Movements Report](../../../../assets/drive/1KCTc1ueZ2Z-w-saDYnPVYx-BUDlYq4Gl.png)

### Salida de informe de ejemplo

![Product Movements Report](../../../../assets/drive/1Vc4maTIIThjJpROn9ES_qlzWXXupl7DU.png)

## Operaciones de producto

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Operaciones de producto`

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Esta funcionalidad **centraliza todas las transacciones** asociadas con el producto seleccionado, permitiendo la visualización de cada movimiento y acciones tales como línea de envío/recepción de mercancías, coste original del impuesto, coste unitario, hueco y muchas otras acciones relacionadas con los productos.

Esta centralización facilita el análisis y una comprensión completa del rendimiento de las operaciones del producto.

![alt text](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/product-operations-0.png)

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.