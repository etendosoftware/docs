---
title: Tarifa
tags:
  - Master Data Management
  - Etendo Classic
  - Pricing
  - Price List
---

## Tarifa { #price-list }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Tarifas` > `Tarifa`

### Visión general { #overview }

Una tarifa es un listado de precios para diferentes productos o servicios.

!!! info
    Es posible crear tantas tarifas y versiones de tarifa como sea necesario en función de las necesidades de la organización.

El proceso de creación de una tarifa es ligeramente diferente del proceso de creación de una versión de tarifa.

Creación de tarifa:

1.  El nombre y el tipo de tarifa (venta o compra) se detallan en la cabecera de la ventana Tarifa. También es obligatorio definir si el precio incluye impuestos o no.
2.  Existe la posibilidad de una **Lista de precios basado en coste**; para ello, la tarifa debe ser una tarifa de venta.
3.  El **Esquema de tarificación** por defecto sin ninguna configuración, así como la información de la fecha válida desde, deben detallarse en la solapa **Versión de tarifa**.
4.  El precio **Pr. estándar** / **Precio tarifa** de cada producto que debe incluirse en la tarifa se detalla en la subsolapa **Tarifa de Precios**.
5.  La tarifa está lista y puede vincularse a los terceros según sea necesario y utilizarse.

Creación de versión de tarifa:

1.  El nombre y el tipo de tarifa (venta o compra) se detallan en la cabecera de la ventana Tarifa.
2.  Un **Esquema de tarificación** que contiene las nuevas reglas comerciales a aplicar, la fecha válida desde y la tarifa base para la cual se crea la versión de tarifa, deben detallarse en la solapa **Versión de tarifa**.
3.  El proceso **Crear lista de precios** rellena la solapa "Tarifa de Precios" incluyendo:
    1.  cada producto contenido en la tarifa original
    2.  cada producto tendrá un nuevo precio estándar y/o precio tarifa, en función de lo configurado en el esquema de tarificación utilizado.
4.  La versión de tarifa está lista y puede vincularse a los terceros según sea necesario y, por tanto, utilizarse.
5.  Los documentos establecerán automáticamente como valor por defecto la versión más reciente de una tarifa.
6.  No existe fecha de fin en las versiones de tarifa, pero las versiones antiguas pueden desactivarse.

### Tarifa { #price-list_1 }

La ventana Tarifa permite crear tarifas de compra y de venta para asignarlas a los terceros para su uso en transacciones de compra y venta, como pedidos y facturas.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/price-list/price-list-1.png)

Tal y como se muestra en la imagen anterior, se puede crear una tarifa o una versión de tarifa introduciendo la siguiente información relevante:

- Al seleccionar el campo "**Tarifas de venta**" será para transacciones de venta; en caso contrario, será una tarifa de compra.
- El campo **Valor por defecto** permite definir una tarifa determinada como la tarifa por defecto que se utilizará en caso de que un tercero no tenga asignada una tarifa específica.
- **Lista de precios basado en coste**: este campo se muestra si la tarifa es una tarifa de venta. Esta opción permite crear una tarifa basada en el coste más un margen.
  - el coste es el definido en la solapa **Costo** de la ventana Producto.
  - el margen se define en la ventana **Esquema de tarificación**.
  - cuando la tarifa es una lista de precios basada en coste, el esquema de tarificación debe configurarse con coste y un margen.
- **El precio incluye impuestos**. Este indicador es muy importante y, en función de él, se verá afectado el comportamiento de los flujos de venta y aprovisionamiento.
  - Si está marcado, entonces el precio definido es el precio unitario bruto
  - Si no está marcado, entonces el precio definido es el precio unitario neto

**¿Cómo afecta esto a los flujos?**

- Cuando la tarifa incluye impuestos, se rellenan el _precio unitario bruto_ y el _importe bruto de línea_ y el _precio unitario neto_ se calcula en base al _precio unitario bruto_ y al tipo impositivo correspondiente. Lo que no se puede cambiar es el bruto y, debido a ello, puede haber algunos problemas de redondeo que el sistema gestiona automáticamente sumando o restando estas diferencias en el importe del impuesto.

Como ejemplo: si el precio con impuestos incluidos es originalmente 135.50 y el tipo es 4.5 %, entonces el precio redondeado antes de impuestos sería 129.67.

La línea de pedido quedaría:

Cantidad: 1 Precio unitario neto: 129.67 Importe neto de línea: 129.67 Precio unitario bruto: 135.50 Importe bruto de línea: 135.50

Pero el importe bruto total (calculado por el sistema) sería 135.51 (base imponible:129.67 + importe del impuesto:5.84) y lo que debe quedar claro es que el resultado final debe ser 135.50 (el cliente compró 1 unidad cuyo precio es 135.50). Esta diferencia se resolverá ajustando los impuestos:

El sistema ajustará la diferencia sumando o restando dicha diferencia al impuesto que tenga el mayor importe. Así, en este ejemplo, en lugar de tener una línea de impuesto cuyo importe es 5.84 €, el importe será 5.83 € (5.84-0.01).

Finalmente, el importe bruto total para el pedido de venta sería 135.50 (129.67+5.83), que es el importe deseado.

Debido a esto (importe neto vs importe bruto), al utilizar precios que incluyen impuestos se recomienda trabajar con mayor precisión (precisión de precio) para evitar diferencias de redondeo.

- Cuando la tarifa no incluye impuestos, los campos _precio unitario bruto_ e _importe bruto de línea_ no se muestran y no se calculan en absoluto en la línea del documento. El importe bruto final del documento será el resultado de la suma de los importes netos de las líneas más los importes de impuestos.
- La tarifa se define a nivel de documento (cabecera), por lo que no puede haber líneas en las que el precio incluya impuestos y otras en las que no. Esto es claro para los pedidos, pero para las facturas en las que los pedidos pueden agruparse en una única factura, la regla también se aplica. Una factura no puede tener pedidos en los que la tarifa incluya impuestos y pedidos en los que la tarifa no incluya impuestos.

### Versión de tarifa { #price-list-version }

Puede haber tantas versiones de una tarifa existente como sea necesario; versiones que pueden ser válidas para un periodo de tiempo determinado y que pueden definirse según ciertas reglas comerciales.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/price-list/price-list-2.png)

Tal y como se muestra en la imagen anterior, existen dos tipos de "Versiones de tarifa":

- genéricas y originales vinculadas al "Esquema de tarificación por defecto"
- versiones de tarifa adicionales (no basadas en coste) que requieren ambas cosas:
  - un **Esquema de tarificación**
  - y una versión de tarifa base
- las versiones de tarifa basadas en coste requieren un **Esquema de tarificación** con configuración de coste en **Base precio tarifa** y **Precio base unitario**.

El botón de proceso denominado **Crear lista de precios** debe utilizarse únicamente en el caso de crear versiones de tarifa adicionales, ya que requiere una tarifa base si la tarifa no está basada en coste. Si la tarifa está basada en coste, es obligatorio seleccionar el esquema de tarificación y, opcionalmente, la versión base.

- si la versión base está en blanco, la aplicación calcula el precio estándar y el precio tarifa para todos los productos (excluyendo los productos con descuento) más el margen definido.
- si se selecciona un valor de versión base, la aplicación calcula el precio estándar y el precio tarifa para todos los productos definidos en la tarifa base como coste más margen.

### Tarifa de Precios { #product-price }

La solapa **Tarifa de Precios** permite al usuario añadir o editar productos y sus precios para una tarifa seleccionada.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/price-list/price-list-3.png)

En otras palabras:

- Añadir productos en el caso de crear una tarifa
- Editar productos en el caso de modificar una versión de tarifa:
  - ya que los productos requeridos con sus nuevos precios se rellenan automáticamente por Etendo en esta solapa al ejecutar el proceso "Crear lista de precios".

En general, esta solapa incluye dos campos principales:

- el campo '_Precio tarifa_', como el precio utilizado como referencia en una tarifa o versión de tarifa determinada. Este precio puede ser el resultado de un descuento o de cualquier otra regla comercial aplicada por un **Esquema de tarificación**.
- y el campo **Pr. estándar**, como el precio final utilizado en documentos como pedidos y facturas. Este precio puede ser el resultado de un descuento o de cualquier otra regla comercial aplicada por un **Esquema de tarificación**.

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
