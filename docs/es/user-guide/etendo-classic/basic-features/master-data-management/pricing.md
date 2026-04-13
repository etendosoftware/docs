---
title: Tarifas
tags: 
  - Tarifa
  - Descuento
  - Promociones
  - Regla de precios

---

## Esquema de tarificación

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Tarifas` > `Esquema de tarificación`

### Visión general

Un esquema de tarificación es una plantilla utilizada para completar automáticamente una nueva versión de una tarifa.

La gestión de tarifas no es una tarea fácil de manejar, principalmente en mercados competitivos donde los márgenes son muy ajustados.

Hoy en día, las organizaciones tienen que gestionar una enorme variedad de productos, que tienen precios diferentes en función de la temporada y otras variables de tarificación.

Etendo gestiona los precios a través de tres conceptos relacionados con las tarifas:

- la **Tarifa**
- el **Esquema de tarificación**
- y la **Versión de tarifa**

Y permite la creación de:

- Tarifas de venta y/o compra **generales**
- Tarifas **específicas** para un proveedor o cliente concreto, o un grupo de ellos.
- Tarifas **basadas en coste**, basadas en el coste del producto

La forma en que estos conceptos funcionan en Etendo se describe a continuación:

1.  **Creación de tarifa(s)**:
    1.  Se crea por defecto un "Esquema de tarificación por defecto", sin ninguna configuración, después de crear una organización.
    2.  El "Esquema de tarificación por defecto" es el esquema que se utilizará en la creación de las tarifas que NO son una "Versión de tarifa".
    3.  Las tarifas vinculadas al "Esquema de tarificación por defecto" pueden contener tanto el precio tarifa como los precios unitarios netos de los productos.  
        Para saber más, visite Tarifa.
    4.  La(s) tarifa(s) creada(s) puede(n) vincularse a los terceros según sea necesario.  
        Para saber más, visite Terceros
2.  **Creación de esquema(s) de tarificación**:
    1.  Se pueden crear nuevos esquemas de tarificación como una forma de configurar un conjunto de reglas comerciales que se aplicarán a tarifas existentes.  
        Para saber cómo, siga leyendo.
3.  **Creación de versión(es) de tarifa**:
    1.  Se crea una nueva versión de una tarifa existente como una combinación de una tarifa base y un "Esquema de tarificación" determinado.  
        Para saber más, visite Tarifa.
    2.  Las versiones de la(s) tarifa(s) creadas pueden vincularse a los terceros según sea necesario.  
        Para saber más, visite Terceros.

### Cabecera

La ventana de esquema de tarificación permite la creación de tantos esquemas de tarificación como sea necesario con el objetivo de obtener una gestión sencilla de las tarifas y de las versiones de tarifa.

![](../../../../assets/drive/8dm__0RGCoicJS7A0HIQ2wiXDhVxmgxLG0KI3K3QcCW8LIHOvh-QaKXy12rE-WHLQkVlr476bjI-t7tX7Q877O_4-ek18q8CU8MGnz_tTNhFahwOAvn9co79yD-EKha4_NQvAfHwLOmGt0J49g.png)

Como se muestra en la imagen siguiente, la creación de un esquema de tarificación es tan sencilla como crearlo y asignarle un Nombre.

El conjunto de reglas de precio y descuento que podrían aplicarse a un conjunto de categorías de producto o a productos específicos debe configurarse en la solapa "Líneas".

### Líneas

La solapa de líneas del esquema de tarificación permite definir un conjunto de reglas de precios, como aplicar un % de descuento al precio unitario neto de una categoría de producto determinada o de un producto específico.

![](../../../../assets/drive/1xuN1UnuUBcuYhWnHvIFMpKJ-OufSVW9rM0t-Otml29IRjyIQ5gjF3gIHNu1BdwLNikv9n3_5XmZ3rxWMDvg6Ig80WHdzCkEQI2q4cLeQ4Cbl_W3KVnYszYbQHJffZumj85Y1Q1RJjd_bFOp7w.png)

Lo primero que hay que tener en cuenta es que, como se muestra en la imagen anterior, la solapa "Líneas" se divide en dos secciones:

- la primera sección permite al usuario:
  - informar a Etendo sobre:
    - el "Terceros" y/o
    - la "Categoría del producto" y/o
    - el "Producto"  
      a los que se van a aplicar las reglas de precio/descuento que se definirán en la siguiente sección.
- la segunda sección permite al usuario:
  - configurar qué precio de la tarifa existente se tomará como "Base precio tarifa" en la nueva versión de tarifa. Las opciones disponibles son:
    - **Precio tarifa** que es el precio publicado en la tarifa
    - **Precio unitario** que es el precio final utilizado en las líneas de pedido/factura de compra y venta
    - **Precio fijo**, ya que es posible configurar que, para la nueva versión de tarifa, el precio tarifa sea igual a un precio fijo determinado.
    - **Costo**, donde el precio publicado en la tarifa será el coste del producto (solapa Costo en la ventana de producto) y un margen.
    - **Precio fijo o basado en coste** combina las dos opciones anteriores con la siguiente condición:
      - Si el precio fijo es superior al coste, entonces se selecciona el precio fijo definido.
      - Si el precio fijo es inferior al coste, entonces se selecciona el coste (más el margen definido).
    - **Precio fijo o basado en coste más margen** combina las opciones de precio fijo y coste con la siguiente condición:
      - Si el precio tarifa/unitario fijo establecido es superior al coste actual más el margen del precio tarifa/unitario, la tarifa se creará con el precio fijo.
      - Si el precio tarifa/unitario fijo establecido es inferior al coste actual más el margen del precio tarifa/unitario, entonces la tarifa se creará utilizando el coste más el margen.
  - configurar qué precio de la tarifa existente se tomará como "Precio base unitario" en la nueva versión de tarifa. Las opciones disponibles son las mismas que las anteriores:
    - **Precio tarifa**
    - **Precio unitario**
    - **Precio fijo**, ya que es posible configurar que, para la nueva versión de tarifa, el precio unitario neto sea igual a un precio fijo determinado
    - **Costo**
    - **Precio fijo o basado en coste**
    - **Precio fijo o basado en coste más margen**
  - configurar los descuentos, si los hubiera, a aplicar al precio unitario neto y/o al precio tarifa en los campos:
    - **Descuento (%) precio tarifa**
    - **Descuento (%) precio estándar**
  - configurar el margen sobre el coste del producto a aplicar al precio unitario neto y/o al precio tarifa en los campos:
    - **%Margen Precio Neto**
    - **% Margen Precio Unitario**

Lo segundo que hay que tener en cuenta es que el conjunto de reglas de precios y/o descuentos podría configurarse de forma "jerárquica", es decir, línea por línea, o aplicando la última regla de precio válida (forma no jerárquica).

!!! info
    La preferencia Habilitar tarifa jerárquica está disponible para seleccionar el comportamiento deseado al aplicar las reglas de la tarifa.

Imaginemos que las reglas que deben formar parte de un esquema de tarificación son:

- aplicar un descuento del 5% sobre el precio unitario neto a los productos que pertenecen a una Categoría del producto X.
- aplicar un descuento del 10% sobre el precio unitario neto a los productos que pertenecen a la Categoría del producto Y.
- aplicar un descuento del 15% sobre el precio unitario neto al Producto X que pertenece a la Categoría del producto X.

La forma en que esto funciona en Etendo es:

- el esquema de tarificación debe contener 2 líneas, una por cada regla de descuento a aplicar:
  - La primera línea contendrá información como:
    - Secuencia = 10
    - Tipo de rango de conversión = Spot
    - Categoría del producto = Categoría del producto X
    - Precio Base Neto Unitario = Precio unitario
    - Descuento del precio unitario neto = 5.00
  - La segunda línea contendrá información como:
    - Secuencia = 20
    - Tipo de rango de conversión = Spot
    - Categoría del producto = Categoría del producto Y
    - Precio Base Neto Unitario = Precio unitario
    - Descuento del precio unitario neto = 10.00
  - La tercera línea contendrá información como:
    - Secuencia = 30
    - Tipo de rango de conversión = Spot
    - Categoría del producto = Categoría del producto X
    - Producto = Producto X
    - Precio Base Neto Unitario = Precio unitario
    - Descuento del precio unitario neto = 15.00

Usando comportamiento jerárquico:

- se aplica un descuento del 5% sobre el precio unitario a los productos que pertenecen a la Categoría del producto X.
- se aplica un descuento del 10% sobre el precio unitario a los productos que pertenecen a la Categoría del producto Y.
- se aplica un descuento del 15% sobre el precio unitario al Producto X, además del descuento del 5% por pertenecer a la Categoría del producto X.

Usando comportamiento no jerárquico:

- se aplica un descuento del 5% sobre el precio unitario a los productos que pertenecen a la Categoría del producto X, excepto al Producto X.
- se aplica un descuento del 10% sobre el precio unitario a los productos que pertenecen a la Categoría del producto Y.
- se aplica un descuento del 15% sobre el precio unitario al Producto X.
## Tarifa

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Tarifas` > `Tarifa`

### Visión general

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

### Tarifa

La ventana Tarifa permite crear tarifas de compra y de venta para asignarlas a los terceros para su uso en transacciones de compra y venta, como pedidos y facturas.

![](../../../../assets/drive/bHmRBT-3YqtSLK2PErojCQx8-FE-6UJK0_A3mkisnphxh5R2A7qev8UsVYgo9x7o8xbHuvmIhYY9ijGcJ9tymlAeIUqaNHJCOVNlXTv58MpI1iBTJ3ppDjXB0s_3ZXMro8cp8tS3d4oqD4_hHw.png)

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

### Versión de tarifa

Puede haber tantas versiones de una tarifa existente como sea necesario; versiones que pueden ser válidas para un periodo de tiempo determinado y que pueden definirse según ciertas reglas comerciales.

![](../../../../assets/drive/ix0WIF0unAQdEluAH0VKvAHPQFFb5f6V5DlOMcJlQVi54MtuV41UG8GUHy1aHghfH4CH5Iz100WDv3Q8-fF_rPaNDGuFvqWwnTmVKxdNDFCSXnQFM3TAhlcxHapRGH4a7K2nXQVkk0lkuPJ1NQ.png)

Tal y como se muestra en la imagen anterior, existen dos tipos de "Versiones de tarifa":

- genéricas y originales vinculadas al "Esquema de tarificación por defecto"
- versiones de tarifa adicionales (no basadas en coste) que requieren ambas cosas:
  - un **Esquema de tarificación**
  - y una versión de tarifa base
- las versiones de tarifa basadas en coste requieren un **Esquema de tarificación** con configuración de coste en **Base precio tarifa** y **Precio base unitario**.

El botón de proceso denominado **Crear lista de precios** debe utilizarse únicamente en el caso de crear versiones de tarifa adicionales, ya que requiere una tarifa base si la tarifa no está basada en coste. Si la tarifa está basada en coste, es obligatorio seleccionar el esquema de tarificación y, opcionalmente, la versión base.

- si la versión base está en blanco, la aplicación calcula el precio estándar y el precio tarifa para todos los productos (excluyendo los productos con descuento) más el margen definido.
- si se selecciona un valor de versión base, la aplicación calcula el precio estándar y el precio tarifa para todos los productos definidos en la tarifa base como coste más margen.

### Tarifa de Precios

La solapa **Tarifa de Precios** permite al usuario añadir o editar productos y sus precios para una tarifa seleccionada.

![](../../../../assets/drive/rapFdQYs8ZYQ3c9wO_nEZ-tTniv5PDDLmdlXZ03ByVKh6Im-Jwt2KIB1Rj1Hm1agjXK55WcmCR6Xok4iO4s3zlRoP1TK-C6rh6oJSIBNVEdEcBRJB4OHbEtWV-7ZE8slY7CahOj4x7wU9GBuow.png)

En otras palabras:

- Añadir productos en el caso de crear una tarifa
- Editar productos en el caso de modificar una versión de tarifa:
  - ya que los productos requeridos con sus nuevos precios se rellenan automáticamente por Etendo en esta solapa al ejecutar el proceso "Crear lista de precios".

En general, esta solapa incluye dos campos principales:

- el campo '_Precio tarifa_', como el precio utilizado como referencia en una tarifa o versión de tarifa determinada. Este precio puede ser el resultado de un descuento o de cualquier otra regla comercial aplicada por un **Esquema de tarificación**.
- y el campo **Pr. estándar**, como el precio final utilizado en documentos como pedidos y facturas. Este precio puede ser el resultado de un descuento o de cualquier otra regla comercial aplicada por un **Esquema de tarificación**.
## Actualizar tarifas

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Tarifas` > `Actualizar tarifas`

### Visión general

En las ventas diarias, especialmente en el comercio minorista y la distribución, las tarifas son muy importantes. Por lo tanto, Etendo incluye abundante información para gestionar y actualizar las versiones de tarifa por tercero.

Esta funcionalidad incluye diferentes tarifas, versiones de tarifa para cada tarifa y esquemas de tarificación. Revise estos conceptos para comprender mejor la funcionalidad de *Actualizar tarifas*.

Etendo permite una estructura jerárquica de tarifas y esta jerarquía se basa en los esquemas de tarificación.

#### Funcionalidad

Siga este ejemplo sobre para qué se utiliza *Actualizar tarifas*:

Ejemplo 1:

Imagine que usted es propietario de una panadería y vende diferentes tipos de pan a distintos clientes. Puede tener pan francés, bollos, bagels, etc. Y para cada tipo puede tener diferentes tamaños: pequeño, mediano y extra.

Usted utiliza una tarifa principal (con una versión de tarifa) que contiene un precio por pan cuando es de tamaño mediano. En base a esta tarifa, se crean otras 2 tarifas aplicando un esquema de tarificación. Para el pan pequeño, un 5% de descuento y para los panes extra, un 4% más. De este modo, podrá gestionar las actualizaciones de precios fácilmente. Suponga que el precio de la harina sube un 10% y usted quiere incrementar todos los precios de todos los panes. Podría seguir estos pasos:

- Crear un nuevo esquema de tarificación incrementando el precio un 10%.
- Crear una nueva versión para la tarifa principal, basada en el nuevo esquema de tarificación.
- Regenerar automáticamente todas las tarifas basadas en la tarifa principal. Para este tercer paso, puede utilizar la funcionalidad **Actualizar tarifas**.

#### Proceso

**Actualizar tarifas** genera todas las tarifas pendientes a partir de la tarifa seleccionada. El proceso comprueba todas las tarifas hijas y, aplicando el esquema de tarificación definido, genera una nueva versión para cada tarifa.

![](../../../../assets/drive/1gcdIPde692fCVAn9cq0PEXTyJBTBR9vT.png)

![](../../../../assets/drive/1JC58tbBLqjqN5hDZv5Puwp_lAmDafJqd.png)
## Ventana Modificación de precios
:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Tarifas` > `Modificación de precios`

### Visión general

Modificación de precios es una funcionalidad flexible que le permite ajustar automáticamente los precios en las líneas de pedidos y facturas según reglas de negocio configurables. Puede definir cuándo y cómo se aplican las promociones usando filtros (como Terceros, Productos, Tarifas y Características), configurar el tipo de descuento (porcentaje, importe fijo o precio fijo) y controlar la disponibilidad de la promoción por día y hora. Se pueden aplicar múltiples promociones en una cascada priorizada. La configuración también permite traducir los nombres de las promociones y realizar el seguimiento de los descuentos aplicados en documentos procesados mediante una solapa opcional de solo lectura.

### Cabecera
Define la configuración principal y las condiciones para aplicar Modificación de precios a pedidos y facturas.

![alt text](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/discounts-add-promotions.png)

Campos a tener en cuenta:

#### Sección principal

- **Organización**: Organización para la que el descuento o la promoción estará disponible.
- **Tipo de descuento/promoción**: Define el tipo de regla utilizada para ajustar precios. Por defecto, Etendo incluye el tipo _Ajuste de precios_, pero es posible ampliar y añadir tipos personalizados según las necesidades de la organización.
- **Nombre**: Identificador interno de la promoción.
- **Nombre impreso**: Etiqueta mostrada a los usuarios finales y en informes. Si está vacío, toma como valor por defecto el Nombre.
- **Descripción**: Texto corto opcional que describe la promoción (hasta 255 caracteres).
- **Activo**: Habilita la promoción para su uso. Los registros inactivos se conservan para auditoría/informes.

#### Opciones del Filtro

- **Fecha de inicio**: Fecha en la que la promoción pasa a ser válida.
- **Fecha final**: Fecha hasta la que la promoción permanece válida (inclusive).
- **Prioridad**: Orden de aplicación cuando se aplican varias promociones. Número menor = mayor prioridad.
- **Aplicar próximo descuento/promoción**: Si está marcado, también se aplicarán las promociones posteriores que correspondan.
- **Filtro**:

    Cada uno de los siguientes campos admite dos métodos de filtrado que definen cómo se tratarán los registros relacionados configurados en las solapas durante la evaluación de la promoción. Estas opciones proporcionan flexibilidad para definir el alcance de una promoción en relación con Terceros, Productos, Tarifas y Organizaciones.

    - **Modo selección Grupo Terceros**
    - **Conjunto de Terceros Incluidos**
    - **Modo selección terceros**
    - **Modo selección Categoría de producto**
    - **Modo selección de producto**
    - **Modo selección Tarifas**
    - **Organizaciones incluidas**
    - **Referencias Externas al Tercero Incluídas**

        | Método                    | Descripción                                                                                                   |
        |---------------------------|---------------------------------------------------------------------------------------------------------------|
        | **Todos excepto los definidos** | **(Valor por defecto)** La promoción se aplica a todos los registros **excepto** a los listados en la solapa correspondiente. |
        | **Solo los definidos**    | La promoción se aplica **solo** a los registros listados en la solapa correspondiente.                       |

    Algunos filtros tienen métodos de filtrado diferentes, que se describen a continuación:

    - **Características Incluidas**: Define cómo se filtran las características del producto para aplicar la promoción. Hay tres métodos disponibles:
    
        | Método                        | Descripción                                                                                 |
        |-------------------------------|---------------------------------------------------------------------------------------------|
        | **Todas las características** | **(Valor por defecto)** La promoción se aplica independientemente de las características del producto. |
        | **Todos los valores definidos** | El producto debe coincidir con **todas** las características definidas para que se aplique la promoción. |
        | **Cualquiera de los definidos** | El producto debe coincidir con **cualquiera** de las características definidas para que se aplique la promoción. |

    - **Excluir Características**: Define cómo se filtran las características del producto para excluir la promoción. Hay dos métodos disponibles:

        | Método                        | Descripción                                                                                                   |
        |-------------------------------|---------------------------------------------------------------------------------------------------------------|
        | **Todos los valores definidos** | **(Valor por defecto)** El producto debe coincidir con **todas** las características definidas para que no se aplique la promoción. |
        | **Cualquiera de los definidos** | El producto debe coincidir con **cualquiera** de las características definidas para que no se aplique la promoción. |

#### Definición

- **% de descuento**: Porcentaje de descuento a aplicar al precio.
- **Importe del descuento**: Importe fijo a restar del precio.
- **Fijo precio estándar**: Precio final asignado al producto cuando se aplica la promoción.
- **Cantidad desde**: Cantidad mínima requerida para que se aplique la promoción.
- **Cant. hasta**: Cantidad máxima elegible para la promoción.
- **Es múltiple**: El descuento se aplica solo si la cantidad es múltiplo de un valor definido.
    - **Unidades por paquete**: Esta opción se muestra solo si _Es múltiple_ está habilitado. Define el número de unidades consideradas por paquete.

#### Disponibilidad
Esta sección define los días y horas en los que la promoción está activa. Si no se configura ninguna disponibilidad, la promoción se aplicará siempre.

- **Toda la semana**: Indicador para habilitar la promoción durante toda la semana.
    - **Comienzo**: Hora de inicio diaria de la promoción.
    - **Fin**: Hora de fin diaria de la promoción.
- **Lunes – Domingo**: Indicadores para habilitar la promoción en días concretos de la semana.
    - **Comienzo**: Hora de inicio para el día de la semana especificado.
    - **Fin**: Hora de fin para el día de la semana especificado.

### Solapa

- **Traducción**: Permite definir el idioma, así como el **Nombre** y el **Nombre impreso** traducidos correspondientes para cada idioma.
- **Grupos de Terceros**: Permite incluir o excluir Grupos de Terceros de una promoción o descuento.
- **Terceros**: Permite incluir o excluir Terceros específicos de una promoción o descuento.
- **Conjunto de Terceros**: Permite definir Conjuntos de Terceros a los que se aplicará una promoción o descuento.
- **Categoría del producto**: Permite incluir o excluir Categorías del producto de una promoción o descuento.
- **Productos**: Permite incluir o excluir Productos individuales de una promoción o descuento.
- **Tarifa**: Permite seleccionar Tarifas para incluir o excluir de una promoción o descuento.
- **Organización**: Permite seleccionar Organizaciones para incluir o excluir de una promoción o descuento.
- **Características**: Permite seleccionar Características del producto a incluir en una promoción o descuento.
- **Excluir Características**: Permite seleccionar Características del producto a excluir de una promoción o descuento.
- **Tercero Externo** Permite seleccionar Tercero Externo para incluir o excluir de una promoción o descuento.

### Botones

- **Añadir Organizaciones**: Añade registros de Organización en la solapa *Organización* para incluirlos o excluirlos de la promoción.
    ![alt text](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/add-organizations.png)
- **Añadir Categorías de Productos**: Añade registros de Categoría del producto en la solapa *Categoría del producto* para incluirlos o excluirlos de la promoción.
    ![alt text](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/add-product-categories.png)
- **Añadir Productos**: Añade registros de Producto en la solapa *Productos* para incluirlos o excluirlos de la promoción.
    ![alt text](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/add-products.png)

### ¿Cómo se definen las promociones?

El proceso para configurar una promoción es sencillo:

1. **Identificar la promoción**: Use los campos **Nombre** y **Nombre impreso** para identificar la promoción. _Nombre impreso_ se mostrará al usuario final, mientras que _Nombre_ se usa internamente.

2. **Definir el periodo activo**: Configure **Fecha de inicio** y **Fecha final** para definir cuándo será válida la promoción.

3. **Controlar la prioridad y la cascada de la promoción**: Use **Prioridad** para determinar el orden en el que se aplicarán las promociones si hay más de una válida. Habilite **Aplicar próximo descuento/promoción** si desea que se apliquen promociones posteriores después de esta.

4. **Configurar filtros**: Use la sección **Opciones del Filtro** para determinar dónde se aplica la promoción:
    - Seleccione el **método de inclusión** para cada filtro (Terceros, Productos, Tarifas, Características y Organizaciones).
    - Defina los valores reales del filtro en las sub-solapas correspondientes o use los botones disponibles.

    !!! tip
        La configuración de filtros es clave para garantizar que la promoción se aplique solo en los escenarios previstos.

5. **Definir la lógica del descuento**: En la sección **Definición**, configure el descuento:
    - **Importe del descuento** y/o **% de descuento** para ajustar el precio.
    - **Fijo precio estándar** para sobrescribir el precio final.
    - **Cantidades mínima y máxima** para aplicar la promoción solo para determinadas cantidades.

    !!! tip
        Use **Fijo precio estándar** para promociones que deban forzar un precio específico, y **Cantidades mínima/máxima** para promociones basadas en volumen.

6. **Establecer la disponibilidad de la promoción (opcional)**: En la sección **Disponibilidad**, configure cuándo estará activa la promoción; si no se configura ninguna disponibilidad, la promoción se aplicará siempre:

    - Use **Toda la semana** para aplicar la promoción todos los días.
    - Opcionalmente, habilite días individuales (**Lunes** a **Domingo**) para ajustar con precisión cuándo está activa la promoción.
    - Para cada día (o Toda la semana), configure **Comienzo** y **Fin** para definir el rango horario válido.

    !!! tip
        Configurar la disponibilidad garantiza que las promociones se apliquen correctamente según el horario comercial, días especiales o estrategias de marketing basadas en el tiempo.

### ¿Cómo se aplican las promociones?

Las reglas de descuento y promoción se aplican automáticamente a las [Línea pedido de venta](../sales-management/transactions.md#lines-1) y a las [líneas de factura de venta](../sales-management/transactions.md#lines-5) en función de los filtros que configure. Por ejemplo, orientando la promoción a determinados Grupos de Terceros o a productos específicos durante un periodo de tiempo definido.

Etendo calcula el precio final en tres pasos:

- **Tarifa**: El precio base definido en la tarifa de precios del producto.
- **Precio estándar**: El primer nivel de descuento. Puede provenir de la tarifa o ajustarse manualmente en la línea.
- **Precio real**: El precio final que aparecerá en el documento tras aplicar las promociones.

Si se aplican varias promociones, se aplicarán por orden de prioridad. Cada nueva promoción se aplica sobre el precio resultante de la anterior (cascada).

Los ajustes de precio son visibles inmediatamente al editar la línea; verá el precio final antes de procesar el documento.

!!! info
    Aunque el descuento se muestra al instante, el registro de **Modificación de precios** solo se crea una vez que el documento se procesa. Consulte la sección [Configuración opcional](#configuración-opcional) para saber cómo mostrar esta información en la ventana del documento.

### Configuración opcional

La solapa de solo lectura **Modificación de precios** puede añadirse a las siguientes ventanas para mostrar los descuentos aplicados a cada precio:

- Pedido de compra
- Pedido de venta
- Factura de compra
- Factura de venta
- Presupuesto de venta

!!! tip
    Para mostrar esta solapa en las ventanas mencionadas, simplemente marque la casilla **Activo** en la solapa correspondiente en la ventana **ventanas, solapas y campos**. 
    Esta acción debe ser realizada por un desarrollador, con rol de administrador del sistema, y usando una **Plantilla** de desarrollo para exportar la configuración y evitar que se pierdan los cambios.
## Regla de Precio de Servicio

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Tarifas` > `Regla de Precio de Servicio`

### Visión general

En esta ventana se configurarán las Reglas de Precio asignadas a servicios basados en Regla de Precio. En lugar de tener un precio fijo, habrá reglas que determinarán el precio del Servicio.

### Regla de Precio de Servicio

![](../../../../assets/drive/X9LCI62xbhWb8fv-Kd56CnOQGzy2Bw1KXj1frgulzwbMa3UkXVFW2GtKdR1a0-BIXVVRePT4wgfzFCFI8LpQAZv66zLqQTzVV_5LuiBKK8wZecnNvki6Pu3rJ-4OBccqbSfCm45H2zJ4eX4xgw.png)

Campos de configuración:

- **Nombre**: Nombre de la Regla de Precio de Servicio.
- **Descripción**: Descripción de la Regla de Precio de Servicio.
- **Tipo de Regla**: Hay dos valores para seleccionar en el desplegable
  - Porcentaje: Si se selecciona, se mostrará un campo Porcentaje que permitirá establecer un Porcentaje. Para determinar el precio del servicio, este importe se aplicará al importe de las líneas relacionadas con el servicio.
    - **Porcentaje**: Porcentaje a aplicar.
    - **Después de Descuentos**: Si se selecciona, el porcentaje se aplicará después de añadir los descuentos al ticket.
  - **Rangos**: Si se selecciona, se mostrará una nueva solapa Rangos que permitirá crear diferentes Rangos en función del importe de las líneas relacionadas.

### Rangos

![](../../../../assets/drive/QwjLn0C5fh2kKYl7P1q381tMurECKsFm_xLVCviWtFqf48yaxSa0PfpjwM80ji2kQQmDQC3VQVL6YQYyRu9y39AgLl19QBGYO4E2iAXV7cC1qINdvHtHTYAQGmQCDrVeqBr-Jnhd_TVcKDDWcw.png)

En esta solapa, se pueden crear diferentes Rangos en función del importe de las líneas de pedido relacionadas. Campos de configuración:

- **Importe Hasta**: Si el importe sumado de las líneas de pedido relacionadas es igual o inferior a este importe, se tendrá en cuenta la configuración de este rango.
- **Tipo de Regla**: Hay dos valores para seleccionar en el desplegable
  - Porcentaje: Si se selecciona, se mostrará un campo Porcentaje que permitirá establecer un Porcentaje. Para determinar el precio del servicio, este importe se aplicará al importe de las líneas relacionadas con el servicio.
    - **Porcentaje**: Porcentaje a aplicar.
    - **Después de Descuentos**: Si se selecciona, el porcentaje se aplicará después de añadir los descuentos al ticket.
  - **Precio fijo**: Si se selecciona, se mostrará un campo ‘Tarifa’.
    - **Tarifa**: Tarifa de la que se obtendrá el precio del servicio.

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.