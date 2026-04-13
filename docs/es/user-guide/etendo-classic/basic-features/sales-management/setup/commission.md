---
title: Comisión
tags:
    - Comisión
    - Importe neto
    - Margen
    - Cantidad base
    - Agente comercial
---

# Comisión

:material-menu: `Aplicación` > `Gestión de Ventas` > `Configuración` > `Comisión`

<iframe width="560" height="315" src="https://www.youtube.com/embed/vQGzo7cbCYQ?si=1CLcSz5b4iY_J4hy" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Visión general

La funcionalidad de Comisión en Etendo comienza con la **ventana Comisión**, donde los usuarios configuran los ajustes generales para el cálculo de comisiones, lo que permite definir **cómo y cuándo se van a calcular las comisiones** y **a quién se le van a pagar**. Las comisiones pueden calcularse en base a las ventas definidas en dos documentos: **Pedidos de venta y Facturas de venta**. 

Desde la ventana Comisión, se definen criterios más detallados, incluyendo filtros por tercero, producto o región, junto con la estructura real de la comisión. Una funcionalidad clave es la posibilidad de asignar un **agente comercial** directamente al crear documentos de venta (pedidos y/o facturas), lo que permite a Etendo vincular esas transacciones al plan de comisiones correspondiente y garantiza un filtrado preciso. 

Una vez establecidas todas las condiciones, el sistema genera la comisión correspondiente, que se muestra en la ventana [**Procesar comisión**](../../../../etendo-classic/basic-features/sales-management/transactions.md#commission-payment), donde los usuarios pueden revisar un desglose detallado del cálculo e incluso generar una [**Factura (Proveedor)**](../../../../etendo-classic/basic-features/procurement-management/transactions.md#purchase-invoice) para procesar el pago de la comisión al agente comercial.

En resumen, el flujo general es:

-   Definir la comisión en la **ventana Comisión**.
-   Crear los Pedidos de venta y las Facturas de venta vinculados a un agente comercial.
-   Generar la comisión en la ventana Comisión para un agente comercial determinado utilizando el botón de proceso **Generar comisión**.
-   y, a continuación, desde la ventana [Procesar comisión](../../../../etendo-classic/basic-features/sales-management/transactions.md#commission-payment), crear una factura si es necesario utilizando el botón de proceso **Crear factura**. 

Antes de utilizar comisiones, es necesario realizar algunas **configuraciones**:

-   Crear un agente comercial. La forma de hacerlo es:
    -   En primer lugar, es posible crear un [usuario de Etendo](../../../../etendo-classic/basic-features/general-setup/security/user.md), ya que el agente comercial puede ser un usuario de Etendo que inicia sesión en Etendo y emite pedidos/facturas de venta.
    -   A continuación, crear un [Terceros](../../../../etendo-classic/basic-features/master-data-management/master-data.md#business-partner). Es obligatorio crear un tercero porque el agente comercial podría ser alguien que vaya a emitir una factura para que se le paguen las comisiones.  Si ese es el caso,  ese tercero debe marcarse como *Proveedor* en la **solapa Proveedor** y tener definidos un *Método de pago PO*, un *Proveedor C.P* y una *Tarifa de compra*. Además, es necesario marcar el Terceros como Agente comercial en la **solapa Empleado**.
    -   Y, por último, si se creó el usuario, vincular ambos. La forma de hacerlo es seleccionar el tercero recién creado en el campo **Terceros** de la ventana **Usuario**. 
    - Crear un [Producto](../../../../etendo-classic/basic-features/master-data-management/master-data.md#product) e incluirlo en una **Tarifa** sin información de precios como parte del concepto requerido cuando se crea la factura de compra de la comisión. 


## Cabecera 

El usuario puede definir una comisión de ventas para ser utilizada en el proceso de ventas. La cabecera lista los términos principales que se utilizarán para calcular la comisión:

![Cabecera de la comisión](../../../../../assets/user-guide/etendo-classic/basic-features/sales-management/setup/commission-1.png)

-   **Terceros / Agente comercial**: Se utiliza para crear una factura de compra o para calcular la comisión
-   **Moneda**: La moneda en la que se calculará y pagará la comisión. Esto no es un filtro para facturas/pedidos: las transacciones en cualquier moneda se convertirán a esta moneda a efectos del cálculo de la comisión.
-   **Tipo de frecuencia**: El proceso toma los pedidos/facturas que encajan en el periodo correspondiente.
-   **Producto de facturación**: Si se requiere una factura, la nueva factura tendrá este producto.
-   **Base de cálculo**: Si la comisión se calcula en base a facturas o pedidos.
-   **Fecha del último proceso**: Última fecha en la que se ejecutó el proceso Generar comisión.
-   **Estado base**: Si la comisión se calcula en base a todos los documentos o a documentos totalmente pagados.
-   **Cantidad base**: Si la comisión se calcula en base al **importe neto** o al **margen**. Etendo admite dos métodos principales de cálculo de comisiones: Importe neto (comisiones basadas en los ingresos totales por ventas) y Margen (comisiones basadas en márgenes de beneficio: precio de venta menos coste). Esta es una configuración clave que determina el método de cálculo (consulte [Opciones de Cantidad base](#opciones-de-cantidad-base) para obtener información detallada).
-   **Lista de detalles**: Ver el resultado de la comisión agrupado o línea a línea. Cuando la comisión se calcula en base al margen, la lista de detalles siempre está marcada.
-   **En cascada**: Permite gestionar comisiones complejas (excluir algunas líneas de factura/pedido, aplicar diferentes multiplicadores de cantidad/importe para algunas líneas de factura/pedido, excluir productos de categorías de producto ya definidas). Cuando este campo está marcado, el resultado de la comisión se agrupa línea a línea.

### Opciones de Cantidad base

Etendo admite dos métodos distintos de cálculo de comisiones mediante el campo **Cantidad base**, cada uno diseñado para diferentes escenarios de negocio:

**Comisión por Importe neto**

Las comisiones por Importe neto se calculan en base al **importe neto total de ventas** de las transacciones. Este es el tipo de comisión más sencillo y es adecuado cuando la comisión debe ser directamente proporcional a los ingresos generados.

Características clave:

- La comisión se calcula como un porcentaje o un importe fijo del importe neto de ventas
- Basada en el importe facturado después de descuentos pero antes de impuestos
- Ideal para escenarios de venta estándar donde la comisión se correlaciona directamente con los ingresos
- Permite cálculos tanto basados en porcentaje como en importe fijo

**Comisión por Margen**

Las comisiones por Margen se calculan en base al **margen de beneficio** de cada transacción. Este método tiene en cuenta el coste de los bienes vendidos para determinar el beneficio real generado por la venta, por lo que es ideal para empresas que desean incentivar la rentabilidad por encima del volumen puro de ventas.

!!! warning
    El método de cálculo por Margen **solo está disponible para Facturas**. No puede utilizarse cuando la **Base de cálculo** está configurada como Pedidos.

Características clave:

- La comisión se calcula sobre el beneficio (precio de venta menos coste) en lugar de sobre las ventas brutas
- Requiere información de costes precisa para los productos en el sistema
- Anima a los agentes comerciales a centrarse en productos y precios rentables
- Cuando se selecciona margen, la opción **Lista de detalles** se habilita automáticamente para mostrar cálculos línea a línea
- Cálculo más complejo, pero proporciona una mejor alineación con la rentabilidad del negocio
- Solo aplicable cuando las comisiones se basan en facturas, no en pedidos

!!! note "Consideraciones importantes"
    - **Importe neto**: Más sencillo de implementar y entender, basado en ingresos
    - **Margen**: Requiere un cálculo de costes de producto preciso, promueve la rentabilidad
    - La elección entre estos métodos debe alinearse con su estrategia de ventas y objetivos de negocio

## Líneas

El usuario puede editar el importe de comisión seleccionado.

La solapa Líneas permite al usuario definir en profundidad las condiciones de la comisión:

![Ventana emergente de la comisión](../../../../../assets/user-guide/etendo-classic/basic-features/sales-management/setup/commission-2.png)

-   **Excluir**: las líneas de pedido/factura que cumplan las condiciones establecidas en la línea de comisión no se tendrán en cuenta para calcular la comisión. Este indicador solo será visible cuando el campo En cascada esté marcado en la cabecera.
-   **Basado en agente comercial**: Si el indicador está marcado, solo se tienen en cuenta para calcular la comisión los pedidos/facturas que tengan el mismo agente comercial que en la cabecera.
-   **Grupos de Terceros**: Solo se tienen en cuenta para calcular la comisión los pedidos/facturas con terceros que pertenezcan a esa categoría.
-   **Terceros**: Solo se tienen en cuenta para calcular la comisión los pedidos/facturas con ese tercero.
-   **Categoría del producto**: Solo se tienen en cuenta para calcular la comisión los pedidos/facturas con productos que pertenezcan a esa categoría.
-   **Producto**: Solo se tienen en cuenta para calcular la comisión los pedidos/facturas con ese producto.
-   **Cant.restada**: La cantidad total calculada en base a los criterios anteriores se reduce en esta cantidad; por lo tanto, a partir de este número Etendo comienza a calcular la comisión.
-   **Multiplicador de cant.**: Precio que multiplica el resultado de la cantidad anterior.
-   **Imp.restado**: El importe neto total calculado en base a los criterios anteriores se reduce en este importe; por lo tanto, a partir de este número Etendo comienza a calcular la comisión.
-   **Coeficiente**: coeficiente (porcentaje) que multiplica el resultado del importe anterior. 

## Botones

-   **Copiar líneas**: Permite copiar la configuración de otras comisiones.
-   **Generar comisión**: En base a la cabecera y las líneas, se genera la comisión. Por ejemplo, si se define una frecuencia mensual y la fecha de inicio es 14/12/2025, solo se tendrán en cuenta los pedidos/facturas de marzo. <br><br>
    ![Ventana emergente de la comisión](../../../../../assets/user-guide/etendo-classic/basic-features/sales-management/setup/commission-3.png)

## Ejemplos

### Ejemplos de Comisión por Importe neto

Los siguientes ejemplos muestran cálculos de comisión basados en el **importe neto de ventas**:

*Ejemplo 1: Importe fijo por unidad por encima del umbral*

Quiero pagar a mi agente comercial 10 € por cada unidad de *Ale Beer* vendida por encima de 3000 unidades.

**Configuración:**

- En la cabecera: Establecer **Cantidad base** en "Importe neto"
- Línea 1: 
    - **Producto**: Ale Beer
    - **Cant.restada**: 3000
    - **Multiplicador de cant.**: 10
- **Resultado**: Comisión = (Unidades vendidas - 3000) × 10 €

*Ejemplo 2: Porcentaje del importe por encima del umbral*

Quiero pagar a mi agente comercial una comisión del 15% sobre las ventas al tercero *Healthy Food Supermarkets, Co.* para importes superiores a 25.000 €.

**Configuración:**

- En la cabecera: Establecer **Cantidad base** en "Importe neto"
- Línea 1:
    - **Terceros**: Healthy Food Supermarkets, Co.
    - **Imp.restado**: 25000
    - **Coeficiente**: 0.15
- **Resultado**: Comisión = (Importe neto total - 25.000 €) × 15%
- **Nota**: Si el resultado de (Importe total - Imp.restado) es inferior a cero, no se tiene en cuenta para la comisión.

*Ejemplo 3: Comisión por tramos por categoría de producto*

Quiero pagar diferentes tasas de comisión en función de las categorías de producto: 10% para *Alcoholic* y 5% para *Fruit juice*.

**Configuración:**

- En la cabecera: Establecer **Cantidad base** en "Importe neto" y marcar **En cascada**
- Línea 1:
    - **Categoría del producto**: Alcoholic
    - **Coeficiente**: 0.10
- Línea 2:
    - **Categoría del producto**: Fruit juice
    - **Coeficiente**: 0.05
- **Resultado**: Las ventas de Alcoholic generan una comisión del 10%, las ventas de Fruit juice generan un 5%

### Ejemplos de Comisión por Margen

Cuando **Cantidad base** se establece en "Margen", las comisiones se calculan en base a los márgenes de beneficio. Recuerde que esta opción solo está disponible cuando **Base de cálculo** se establece en *Factura*.

!!! info
    Para este tipo de comisión, la información de costes debe mantenerse con precisión en el sistema para garantizar cálculos correctos del margen de beneficio.

*Ejemplo 1: Porcentaje del margen de beneficio*

Quiero pagar a mi agente comercial el 20% del margen de beneficio en todas las ventas de *Lemonade*.

**Configuración:**

- En la cabecera: 
    - Establecer **Base de cálculo** en "Factura"
    - Establecer **Cantidad base** en "Margen"
- Línea 1:
    - **Producto**: Lemonade
    - **Coeficiente**: 0.20
- **Resultado**: Comisión = (Precio de venta - Precio de coste) × 20%

*Ejemplo 2: Comisión basada en margen para un segmento específico de clientes*

Quiero pagar una comisión del 18% sobre los márgenes de beneficio para todas las ventas a terceros del grupo *Customer - Tier 2*, pero solo para facturas que estén totalmente pagadas.

**Configuración:**

- En la cabecera:
    - Establecer **Base de cálculo** en "Factura"
    - Establecer **Estado base** en "Totalmente pagado"
    - Establecer **Cantidad base** en "Margen"
- Línea 1:
    - **Grupos de Terceros**: Customer - Tier 2
    - **Coeficiente**: 0.18
- **Resultado**: Comisión = (Precio de venta - Precio de coste) × 18% para facturas totalmente pagadas a clientes Customer - Tier 2

!!! info
    Tenga en cuenta que los campos de cantidad e importe pueden utilizarse en combinación para ambas opciones de Cantidad base.

### Ejemplo de comisión compleja (Importe neto con En cascada)

Un ejemplo de comisión compleja utilizando la base **Importe neto** con la funcionalidad en cascada:

Quiero calcular una comisión del 5% para el tercero *Healthy Food Supermarkets, Co.*.

Para 'Cola 0.5L' quiero que la comisión sea del 10%. No el 10% más el 5% calculado en la primera línea. Por lo tanto, esta línea eliminará lo que se calculó previamente para 'Cola 0.5L'.

**Configuración:**

- En la cabecera: Marcar **En cascada** y establecer **Cantidad base** en "Importe neto"
- Línea 1: Tercero *Healthy Food Supermarkets, Co.* y **Coeficiente**: 0.05
- Línea 2: **Excluir** marcado y **Producto**: 'Cola 0.5L'
- Línea 3: **Producto**: 'Cola 0.5L' y **Coeficiente**: 0.10

Finalmente, el resultado de la comisión será la combinación de estas tres líneas, calculada sobre los importes netos de ventas.

---

Este trabajo es una obra derivada de [Comisión](https://wiki.openbravo.com/wiki/Commission){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.