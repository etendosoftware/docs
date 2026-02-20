---
tags:
    - Cómo hacer
    - Ingresos diferidos
    - Gestión de gastos
    - Procesos contables
    - Gestión de facturas
---

## Visión general

En la mayoría de las situaciones, una empresa querría reconocer los ingresos en cuanto se completa una factura. Por ejemplo, cuando un distribuidor de alimentación y bebidas vende bebidas, el ingreso de la transacción se reconoce en cuanto la mercancía sale del almacén. En Etendo, en esta situación, el ingreso se genera como parte de la contabilización de la factura de venta correspondiente a la transacción.

Sin embargo, en algunas circunstancias, es necesario diferir el reconocimiento de ingresos, ya sea parcial o totalmente, a periodos posteriores. Por ejemplo:

- Una editorial que vende una suscripción anual a una revista querría reconocer los ingresos por el valor de la suscripción a lo largo de 12 meses.
- Una estación de esquí que vende un abono de temporada durante el verano (junio) para la siguiente temporada de esquí necesita esperar hasta el inicio de la temporada (diciembre) antes de reconocer los ingresos y distribuirlos durante la duración de la temporada de esquí (de diciembre a abril).
- Un distribuidor de alimentación y bebidas que vende y factura un producto que solo podrá entregarse a sus clientes dentro de 3 meses necesita diferir el reconocimiento de ingresos hasta la entrega.

De forma similar, en el lado de los gastos, en la mayoría de los casos las empresas reconocerían el gasto (para compras que no son activos y productos no almacenables) en cuanto se realiza la compra. Por ejemplo, si compra material de oficina (un producto consumible que no se capitaliza), el gasto se reconoce en el momento de la compra. En Etendo, en esta situación, el gasto se genera como parte de la contabilización de la factura de compra correspondiente a la transacción.

Sin embargo, en algunas circunstancias, es necesario diferir el reconocimiento del gasto. Por ejemplo:

- Una empresa que compra un seguro empresarial por la duración de un año querría distribuir ese gasto a lo largo de 12 meses.
- Una empresa que paga el alquiler por adelantado de forma trimestral querría distribuir ese gasto a lo largo de 3 meses.

## Visión general

Etendo permite dar soporte a estas situaciones mediante las capacidades de ingresos y gastos diferidos.

En el lado de los ingresos:

- Al crear facturas de venta, a nivel de línea, los usuarios pueden especificar:
    - Si el ingreso de esta línea debe diferirse
    - En ese caso, el número de periodos a lo largo de los cuales debe distribuirse el ingreso
    - El periodo de inicio para el reconocimiento del ingreso
- Los valores anteriores pueden controlarse línea de factura por línea de factura.
- Para productos que habitualmente requieren diferimiento de ingresos, los usuarios pueden especificar a nivel de producto las reglas de reconocimiento de ingresos:
    - Si el producto requiere diferimiento de ingresos
    - La duración del periodo de diferimiento
    - El periodo de inicio más habitual para el reconocimiento del ingreso, que puede definirse como el periodo actual, el siguiente periodo después de la factura de venta, o un periodo especificado manualmente.
- Los valores especificados a nivel de producto se establecen automáticamente como valores por defecto en las líneas de factura de venta cuando se utiliza el producto.
- Estos valores también se utilizan cuando se crea una factura a partir de otro documento (por ejemplo: el proceso Generar facturas que crea facturas a partir de pedidos de venta).

De forma similar, en el lado de los gastos:

- Al crear facturas de compra, a nivel de línea, los usuarios pueden especificar:
    - Si los gastos de esta línea deben diferirse
    - En ese caso, el número de periodos a lo largo de los cuales deben distribuirse los gastos
    - El periodo de inicio para el reconocimiento del gasto
- Los valores anteriores pueden controlarse línea de factura por línea de factura.
- Para productos que habitualmente requieren diferimiento de gastos, los usuarios pueden especificar a nivel de producto las reglas de reconocimiento de gastos:
    - Si el producto requiere diferimiento de gastos
    - La duración del periodo de diferimiento
    - El periodo de inicio más habitual para el reconocimiento del gasto, que puede definirse como el periodo actual, el siguiente periodo después de la factura, o un periodo especificado manualmente.
- Los valores especificados a nivel de producto se establecen automáticamente como valores por defecto en las líneas de factura de compra cuando se utiliza el producto.
- Estos valores también se utilizan cuando se crea una factura a partir de otro documento.

## Ejemplo

Considere la siguiente situación.

La empresa F&B Publishing vende una suscripción de 1 año a F&B Magazine a Healthy Foods Supermarkets el 17 de octubre de 2022. El valor de la suscripción es de 120 $ y la suscripción cubre el periodo desde noviembre de 2022 hasta octubre de 2023.

El 17 de octubre, se registra una factura en el sistema con una línea para la suscripción. La línea se marca como que requiere diferimiento de ingresos, con un periodo de diferimiento de 12 meses a partir de noviembre de 2023.

Se crean los siguientes asientos contables en base a esta factura:

| Fecha        | Cuenta               | Débito contabilizado | Crédito |
|--------------|----------------------|----------------------|--------|
| 17-OCT-2022  | Cuentas a cobrar     | 120.00               |        |
|              | Ingresos no devengados |                      | 120.00 |
| 30-NOV-2022  | Ingresos no devengados | 10.00               |        |
|              | Ingresos             |                      | 10.00  |
| 31-DEC-2022  | Ingresos no devengados | 10.00               |        |
|              | Ingresos             |                      | 10.00  |
| ...          | ...                  | ...                  | ...    |
| 31-OCT-2023  | Ingresos no devengados | 10.00               |        |
|              | Ingresos             |                      | 10.00  |


## Configuración de Contabilidad

#### Esquema contable

Para poder utilizar diferimientos de ingresos y gastos, primero necesita definir correctamente las cuentas por defecto que se utilizarán para contabilizar ingresos diferidos y gastos diferidos.

Esta configuración se realiza en la ventana Esquema contable.

En esta ventana, en la pestaña Por defecto, puede encontrar dos campos relevantes:

- Gasto diferido de producto: este campo almacena la cuenta por defecto que se utilizará para registrar gastos diferidos. Esta cuenta suele ser una cuenta de activo.
- Ingreso diferido de producto: este campo almacena la cuenta por defecto que se utilizará para registrar ingresos diferidos. Esta cuenta suele ser una cuenta de pasivo.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses/glconfiguration.png)

### Categoría del producto

Las cuentas seleccionadas en la ventana Esquema contable se establecen como valores por defecto para cada Categoría del producto. Los usuarios pueden sobrescribir estos valores por defecto a nivel de categoría del producto, permitiendo que los ingresos y gastos diferidos de diferentes grupos de productos se contabilicen en cuentas distintas y aparezcan como asientos separados en el balance de la empresa.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses/productcategory.png)

## Pasos de ejecución - Ingresos

### Configuración de productos para el diferimiento de ingresos

Para diferir ingresos, necesita configurar correctamente los productos que generarán el diferimiento cuando se vendan. En Etendo, los productos se crean y mantienen en la ventana Producto.

Ventana Producto: en esta ventana, la configuración relacionada con el diferimiento de ingresos se encuentra en la pestaña Cabecera y en la pestaña Contabilidad de la [ventana Producto](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product).

Pestaña Cabecera:

- Ingreso diferido: este indicador solo es visible para productos que tienen marcada la casilla Venta e indica que, por defecto, los ingresos por ventas de este producto deben diferirse. Cuando este indicador está marcado, se hace visible el grupo de campos Plan de ingresos, permitiendo a los usuarios configurar los dos campos siguientes.
- Tipo de plan de ingresos: este campo especifica la frecuencia por defecto de la distribución de ingresos. En este momento, solo se admiten planes de ingresos mensuales y se prevén frecuencias adicionales como trimestral o anual para versiones futuras.
- Número de periodos: este campo especifica la duración por defecto de un plan de ingresos. Por ejemplo, una suscripción anual a una revista se definirá con un plan de ingresos de 12 periodos mensuales, mientras que un abono de esquí de temporada tendrá un plan de ingresos de 5 periodos mensuales.

Es importante tener en cuenta que los valores del plan de ingresos que defina a nivel de producto son el plan de ingresos por defecto y pueden modificarse transacción por transacción.

Pestaña Contabilidad:

- Ingreso diferido de producto: esta es la cuenta utilizada para contabilizar ingresos diferidos por ventas de este producto. Se hereda de la categoría del producto y puede definirse adicionalmente a nivel de producto.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses/product.png)

### Creación manual de facturas

Cuando crea una línea de factura de venta, puede definir a nivel de línea si la línea va a provocar que el ingreso se difiera.

Los campos relevantes son:

- Ingreso diferido: cuando este indicador está marcado, se hace visible el grupo de campos Plan de ingresos, permitiendo a los usuarios configurar los tres campos siguientes.
- Tipo de plan de ingresos: este campo especifica la frecuencia de la distribución de ingresos.
- Número de periodos: este campo especifica la duración de un plan de ingresos.
- Periodo de inicio: el primer periodo en el que se va a reconocer el ingreso.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses/salesinvoice.png)

### Generación automática de facturas

Si la factura se crea automáticamente, ya sea a partir de un pedido de venta o de cualquier otro documento, se tiene en cuenta la configuración del producto y, si procede, el plan de ingresos se define para las líneas de factura en base a los valores por defecto de la configuración del producto.

### Resultados contables

Independientemente de cómo se cree la factura (manual o automáticamente), cuando se completa y se contabiliza, se crean una serie de asientos contables:

- El primer asiento contable, con fecha de la fecha contable de la factura, carga cuentas a cobrar y abona ingresos no devengados.
- Para cada periodo, se crea un asiento contable adicional cargando ingresos no devengados y abonando ingresos.

## Pasos de ejecución - Gastos

### Configuración de productos para el diferimiento de gastos

Para diferir gastos, necesita configurar correctamente los productos que generarán el diferimiento cuando se compren. En Etendo, los productos se crean y mantienen en la ventana Producto.

Ventana Producto: en esta ventana, la configuración relacionada con el diferimiento de gastos se encuentra en la pestaña Cabecera y en la pestaña Contabilidad de la [ventana Producto](../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product).

Pestaña Cabecera:

- Gasto diferido: este indicador solo es visible para productos que tienen marcada la casilla Compra e indica que, por defecto, los gastos de compras de este producto deben diferirse. Cuando este indicador está marcado, se hace visible el grupo de campos Plan de gastos, permitiendo a los usuarios configurar los dos campos siguientes.
- Tipo de plan de gastos: este campo especifica la frecuencia por defecto de la distribución del gasto.
- Número de periodos: este campo especifica la duración por defecto de un plan de gastos.

Es importante tener en cuenta que los valores del plan de gastos que defina a nivel de producto son el plan de gastos por defecto y pueden modificarse transacción por transacción.

Pestaña Contabilidad:

- Gasto diferido de producto: esta es la cuenta utilizada para contabilizar gastos diferidos o pagados por anticipado por compras de este producto. Se hereda de la categoría del producto y puede definirse adicionalmente a nivel de producto.

![](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-manage-deferred-revenue-and-expenses/product2.png)

### Creación manual de facturas

Cuando crea una línea de factura de compra, puede definir a nivel de línea si la línea va a provocar que el gasto se difiera.

Los campos relevantes son:

- Gasto diferido: cuando este indicador está marcado, se hace visible el grupo de campos Plan de gastos, permitiendo a los usuarios configurar los tres campos siguientes.
- Tipo de plan de gastos: este campo especifica la frecuencia de la distribución del gasto.
- Número de periodos: este campo especifica la duración de un plan de gastos.
- Periodo de inicio: el primer periodo en el que se va a reconocer el gasto.

Estos campos se establecen por defecto en base a la configuración del producto, excepto el campo Fecha de inicio.

### Generación automática de facturas

Si la factura se crea automáticamente, ya sea a partir de un pedido de compra o de cualquier otro documento, se tiene en cuenta la configuración del producto y, si procede, el plan de gastos se define para las líneas de factura en base a los valores por defecto de la configuración del producto.

### Resultados contables

Independientemente de cómo se cree la factura (manual o automáticamente), cuando se completa y se contabiliza, se crean una serie de asientos contables:

- El primer asiento contable, con fecha de la fecha contable de la factura, carga gastos diferidos y abona cuentas a pagar.
- Para cada periodo, se crea un asiento contable adicional cargando la cuenta de gasto del producto y abonando la cuenta de gasto diferido.

---

Este trabajo es una obra derivada de [Guías prácticas](https://wiki.openbravo.com/wiki/How_To){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.