---
title: Configuración de productos
---

## Característica de producto

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Característica de producto`

### Visión general

La **Característica de producto** puede definirse para completar la definición de un producto utilizando variantes.

Las _Características de producto_ son atributos que pueden añadirse a la definición del producto para ampliar la descripción de cada producto. Ejemplos de características son _Talla_, _Color_, _Calidad_, _Forma_ o _Peso_. Estas características pueden utilizarse posteriormente para filtrar o buscar productos.

Una vez creada la definición de las características, estas pueden asignarse a un producto y, a continuación, crear otros productos o SKU basados en este **Producto genérico** y sus características. Este es un producto genérico donde se definen atributos comunes como impuestos o precios. Por defecto, los productos heredan todos los atributos del _Producto genérico_ como impuestos, precios, etc. Pueden sobrescribirse en cada producto. Los productos genéricos no pueden comprarse ni venderse ni utilizarse en ningún documento.

Por ejemplo, el producto genérico _Camisas Temporada de Verano 2013 de Mi Proveedor_ implementa las características _Talla_ y _Color_ como variantes. Este _Producto genérico_ tendrá como variante de producto cada combinación de Color y Talla.

### Característica

**Definición de característica**

Campos a tener en cuenta:

- **Variante**: cuando está marcado, explotará/creará combinaciones con sus valores. Si no está marcado, no creará combinaciones con otras características. Por ejemplo:
  - Característica Color: Variante marcada con valor Azul y Blanco
  - Característica Talla: Variante marcada con valor M y L
  - Característica Línea de moda: Variante no marcada con valor Sport, Classic, Vintage
- **Explotar Solapa de Configuración**: indicador disponible en las características de variante. Cuando está marcado, los valores de la característica de variante seleccionada se insertan automáticamente en la solapa _Configuración de características_ cuando la variante se asigna a un producto genérico. Si no está marcado, los valores deben añadirse manualmente.

Estas tres características se asignan al producto de esta forma:

- Color: Azul, Blanco
- Talla: M,L
- Línea de moda: Sport

Se crearán cuatro variantes/productos y todos ellos con la característica Sport. Se puede decir que una característica que no es una variante es como una etiqueta que se añade a cada nuevo producto.

![](../../../../assets/drive/cdjlrR76mBK3wKqB3XQ6bNRK_KDGSQ0EVVtc3t_SAYwPU_JW9f9aTb3RyiWfBiICaOuta8k49CiQN8FZ0--XfpKZ22cROG1FySev_r2sTdzSxoo_aegpn6sseo2efzfQXglibd6WknWTX05Ymg.png)

### Costo

Cada uno de los valores de una característica.

![](../../../../assets/drive/T08VPSpQt04CjFcMqUGY5stqRukgrwkmbvB4vvZkbroD_H2vXSgKGlb5E8R8mFz7PPfOlxRatH0AQeNQ9iF0ciK6puVW5M7dn8PvXC25R8vcSfoxYDilZ3r8n985hnZN3evM1FuRxdMlUQdBpg.png)

Campos a tener en cuenta:

- Nombre: Valor
- Código: para utilizarse posteriormente al crear la variante. Se informará en el campo _Identificador_
- Nivel agrupación: se permite crear una estructura en árbol. Por ejemplo, si la característica es color y para el mismo valor (p. ej., Verde) hay diferentes referencias dependiendo del proveedor:

![](../../../../assets/drive/30qiD3TYly1aHtadA8da6N1on2NsS-24GPTMc4awiD1PJp8YlesaDaIZWxHD6GroXrmmQqlO009SZ21glwlNUwhVU3AWsNKyuyy-D-P0sypHrPr6pbXSI6Tzxn2WAF5dVFffLzWR_KFKSynaSA.png)

#### Botón Añadir Productos

El botón "Añadir Productos" se muestra cuando un valor de característica de producto NO es una "Variante", por lo tanto, puede asignarse a cualquier producto.

![](../../../../assets/drive/IzWGMoCZ3c1nUm2OmvW-MWssK6KzQ1vdmYkLEjwqtOs4aLa_KnRpnZy-kA9YruqEuqstoyo7te-LG9nF3DVjHt7G08DzacTuATqMXW9SeVJ94VywvnPyTEywXyS9h4OaYv2BCAVbb0jy5eCD4Q.png)

No actualiza los valores actuales. Por eso el botón solo muestra productos a los que no se les ha asignado la característica.

- Escenario 1:
  - El producto A tiene la característica Color (definida como variante) con valores Blanco, Rosa, Azul y Negro
  - Después de crear las variantes de producto, el usuario crea la característica no variante Línea de moda: Mujer, Hombre
  - La característica no variante puede asignarse al producto en la ventana Producto utilizando el botón de proceso Actualizar características.
- Escenario 2:
  - Se crea una característica de producto no variante en la ventana Característica de producto como "Variante" = No.
  - Una vez que se ha introducido una característica de producto en la solapa "Costo", se muestra un botón de proceso "Añadir Productos".
  - El botón "Añadir Productos" abre una ventana de selección/ejecución donde cualquier producto o conjunto de productos puede relacionarse con ese valor de característica de producto.

### Subconjunto

Un subconjunto es una colección de valores de una Característica de producto.

La funcionalidad de subconjuntos es una característica potente que permite al usuario compartir las mismas características para diferentes propósitos. Por ejemplo, pueden crearse muchos colores y tallas para diferentes productos:

- Color:
  - Verde
  - Gris
  - Blanco
  - Azul
  - Amarillo
  - Rojo
  - Naranja

Pero finalmente tiene productos diferentes, por ejemplo camisetas y pantalones: subconjuntos:

- Pantalones
  - Verde
  - Blanco
  - Gris
  - Azul
- Camisetas
  - Verde
  - Blanco
  - Naranja
  - Azul

El objetivo de esta funcionalidad es evitar tener valores duplicados (azul, azul, verde, verde) debido a diferentes propósitos. Con este subconjunto, al seleccionar un producto que es un pantalón, por ejemplo, en lugar de seleccionar la característica _Color_ se selecciona el subconjunto _Pantalones_. De este modo, en lugar de recuperar siete valores, recuperará solo cuatro. Otra ventaja de hacer esto es que, al buscar variantes, en lugar de tener azul dos veces (y no sabría si el azul es para pantalones o camisetas), tendrá azul una sola vez. Así, al buscar variantes que tengan la característica _Azul_, el sistema recuperará pantalones y camisetas.

### Valor de subconjunto

Cada uno de los valores de la característica de producto asignados al subconjunto.

![](../../../../assets/drive/8qzF_YI5MuZAL78CRMbdJSNZ8du0swgIEukOgIlHQ_8LTQr1rvbhX2RtOoq9CkprpZaV-Y2nIJQZH40wX_ipyG5uIjKf7bGbA40ZwGQc_U2y1mUFllwYkid1BrbpCRn1ia5FpvwSSqGJCjI5nA.png)

- Número de secuencia: para ordenar la forma de ver los valores
- Nombre: Valor. Tenga en cuenta que solo pueden seleccionarse valores de la característica.
- Código: si se informa, sobrescribirá el código configurado en la característica

### Filtrado

Los campos basados en columnas cuya referencia es Características de producto pueden filtrarse en la cuadrícula con ayuda de un popup donde se muestra el árbol de características disponibles.

![](../../../../assets/drive/c1KyrMrnAS9Ci-UjCi9mCzmMjtHi1layEkYHZWFvgdMoGTGyDW73G28ts-enKErw0xV02TJilqP4GYtWnvWU2VTw1-3CaLmwK_MkXzZd0ECboTr-10RBLFqT4vz4IrFIWZjpvW4kySrV734lkQ.png)

!!! info
    Las características disponibles en este popup se limitan a las aplicables a los datos filtrados en la cuadrícula donde se muestra, con los criterios de filtrado actuales para el resto de campos.

### Configuración

Las Características de producto están listas para usarse de forma estándar.

En cualquier caso, también pueden mostrarse algunas funcionalidades nuevas con opciones de configuración sencillas (estos cambios deben exportarse a la plantilla).

#### Mejorar el selector de producto

Puede seleccionar entre las diferentes características de producto utilizando el selector de producto. Allí tiene una columna que muestra la descripción de las características de producto (ver imagen).

![](../../../../assets/drive/HuSSbpe8wKiBb3z_zy1u3J3Vpade6eOyRQSP28xLwU7-oWoIvIj3RtRDxCG73vVdQMRuN6AaJx51b0AZxqTaO7fJrqFbhd9mdRlXX7W99lFC6ZAVVV6GaRLGesNJZ-6drk9EVJnsd3fqCtsmUQ.png)

Esto no sucede al seleccionar desde el cuadro de sugerencias. Allí solo se utilizan los nombres de producto. Teniendo en cuenta que los productos con características comparten el nombre, se vuelve imposible distinguir uno de otro (ver imagen).

![](../../../../assets/drive/HpBpfokkfU8331lBrHV76V0Jx-n2fECiBH5Fi7-nTB8eghX3S9JBXgt7SNj3xbuJJJQ6pXfZ_k5nHqbcfAos8JUfAIDT-KcidMmxmYXh409vMtUHljjiqgokBwJwBLzJSYR0VposKg3MH2E9Iw.png)

La experiencia de usuario en este caso sería completamente diferente si los productos pudieran identificarse desde el cuadro de sugerencias (ver imagen).

![](../../../../assets/drive/toMnI_Io2di0EJVl4hcg8FejMI1Mji4mE4WwDzzA6F1xQtwVYVnCfXq63Y_irQ-Kd3kL6oBVE9oQ9AYk6OQ3bPgbY3wOivZK6LMsMRCJfpkydJzFTYSvMZt2wLpp-NrFIovQM4NEX0T_T3Ki4Q.png)

Esto puede mejorarse fácilmente habilitando algunas opciones del selector.

Siga estos sencillos pasos para habilitar esta configuración y, por favor, no olvide exportar esos cambios a su plantilla.

- Inicie sesión como Administrador del sistema
- Vaya a Tablas y Columnas y seleccione C_OrderLine
- Vaya a la solapa líneas y seleccione producto (M_Product_ID)
- Navegue al selector (ver imagen)

![](../../../../assets/drive/N1WJZnz1jvs6oMx3ujSTNn9w6CBuKf1fzCFDRc8f8utnUhODwr8DIg8sz4kePzN-GQEClRIVfmV976AfLmAdd4lgmTLnrOt17IsBXRVvUwzw3C8mKGtsK3shjz_WhIhUvDTyJ5nzzTQ9tXpmIQ.png)

- Vaya a la solapa Defined Selector y luego a la solapa de campo Defined Selector y seleccione el campo Descripción de característica.
- Edite y marque las casillas de verificación "Usado en el cuadro de sugerencias" y "Mostrar en la Lista" (ver imagen)

![](../../../../assets/drive/VeWmotz-vCwIybOp0GCuBP7Bix5SLKwHh68bX2NpVZV1R4Co_k8pAfTI9dLENbG2XPf4RJ1RDg3cro74LxzywXIsLN8RkmjNvDXaDYrkXEazCJRZg3mkZt0oxNuBCGluasJb_00MRnN8KP-0ug.png)

- El último punto sería exportar estos cambios a la plantilla. Esto es realmente importante para evitar problemas en futuros procesos de actualización y para mantener estos cambios después de la actualización.
## Actualizar descripción de las características de producto

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Actualizar descripción de las características de producto`

### Visión general

Cada variante tiene su _Descripción de característica_ de producto y este campo se calcula automáticamente cuando:

- Se crean variantes
- Cuando se cambia el valor de una característica, por ejemplo de _Azul_ a _Azul oscuro_

Por ejemplo, si las características de una variante son Color y Talla y los valores son Azul y XL, el resultado de la descripción sería: _Color: Azul, Talla: XL_

Si posteriormente cambia Azul por Azul oscuro, la nueva descripción sería _Color: Azul oscuro, Talla: XL_

En todos estos escenarios, la _Descripción de característica_ se actualiza sin necesidad de ejecutar este proceso.

Este proceso debe utilizarse únicamente en algunos casos especiales:

- Cuando se cambia el nombre de la Característica, por ejemplo de Color a Tono
- Cuando, a través de la base de datos, se modifican características o valores
## Unidad de medida

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Unidad de medida`

### Visión general

Una unidad de medida es una unidad estándar o una combinación de unidades que se utilizará junto con la cantidad de un producto.

Hay muchas unidades de medida que se pueden utilizar para contabilizar la cantidad disponible de un producto, o para comprar o vender un producto.

Las unidades de medida también se pueden utilizar para medir el tiempo. Hay productos como servicios o recursos que deben medirse de esa manera.

A continuación, puede encontrar una lista de las unidades de medida que podría configurar en Etendo:

- **Unidad**
- **Empaquetar**
- **Hora**
- **Kilogramo**
- **KWh** (kilovatio hora)
- **Litro**
- **Palé**
- **Paquete**
- etc.

### Unidad de medida

Los productos de cualquier tipo se gestionan en unidades de medida no monetarias.

![](../../../../assets/drive/Iw-lfQm_nO_kWlUX4lMKyP1PLsGc2gK0pR-gdpvkELwuNVzmGdIs8uFhBLSMbGk9vlooN8WI_HV4cppv96lpvgGE6jy40utYqvHjJZI8RVyNSbAA0USOej4f1ZcyYslRe9mH3rMAwQhd31dvmw.png)

Tal y como se muestra en la imagen anterior, se puede crear una unidad de medida no monetaria en Etendo completando los siguientes datos relevantes:

- el **Código EDI**, si existe.
- el **Nombre de la UOM**
- la **Precisión estándar** que se utilizará al redondear las cantidades calculadas de los productos que tengan esa unidad de medida
- la **Precisión de los  costos** que se utilizará al redondear el coste calculado de los productos que tengan esa unidad de medida.
- y el **Símbolo** o la abreviatura de unidad de medida de uso común

### Traducción

Las Unidades de Medida se pueden traducir a cualquier idioma requerido.

La forma de conseguirlo es tan sencilla como:

- seleccionar primero el idioma requerido
- y luego introducir la unidad de medida traducida a ese idioma.

### Conversión

Edite la tasa de conversión de una unidad de medida a otra.
## Categoría del producto

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Categoría del producto`

### Visión general

Los productos similares pueden agruparse en diferentes categorías, que deben crearse con el objetivo de ayudar a su gestión y análisis.

Puede que desee agrupar productos similares dentro de la misma categoría para obtener información de aprovisionamiento y ventas resumida por cada categoría. Esto es posible debido a que el "Grupo de productos" es una de las "Dimensiones" de los informes de compras y ventas.

Para obtener más información, visite Herramientas de análisis de aprovisionamiento y Herramientas de análisis de ventas.

Además, cada categoría del producto permite al usuario configurar un conjunto diferente de cuentas contables que se utilizarán al contabilizar transacciones relacionadas con el producto, como facturas de compra y de venta.

### Categoría del producto

La ventana Categoría del producto permite al usuario crear y configurar cada grupo de productos que su empresa pueda necesitar.

![](../../../../assets/drive/G_gS1HUEVZE4UMppe7SkmQXsZazw9xWDG8mQE-m9fmGzYn_Bwn8DdEE3m1I81RBebq9f7kD2NMrn6QhLMNAMNAu4_SAgrFv5Ag0h2bJLVb0K9ows2xpaDQLz3mtHsAceVkrMhPUcYBmNdZf_wg.png)

Tal y como se muestra en la imagen anterior, la creación de una categoría del producto requiere introducir la siguiente información para cada categoría:

- un **Identificador** o nombre corto que ayuda a encontrar fácilmente la categoría
- un **Nombre**
- una **Descripción**
- y el indicador **Nivel agrupación**, que ayuda a organizar las categorías del producto en una estructura jerárquica.

Las categorías del producto pueden organizarse en una estructura jerárquica, que posteriormente puede ser explotada por otros informes o procesos. Para obtener más información sobre cómo trabajar con árboles, visite la sección Estructura de árbol.

### Contabilidad

Cada categoría del producto permite al usuario configurar un conjunto diferente de cuentas contables.

![](../../../../assets/drive/Ueek0FRoMRRlbjH2kzHNqRc-x6COVWDiR7oOOvRG3Z5zpeDyPJ1qV_cTafjT_eENf56h-1M7L3L4RkifbsuhC9-MGUexELBuzvaQwZkcpsYVT8sKuJAbcA0z28vzDPj7Lz9JVBFoFNRCLwKe9g.png)

Existe un conjunto de cuentas relacionadas con el producto que debe configurarse correctamente para la configuración del libro mayor de la organización.

El proceso "Copiar cuentas" de la solapa Valores predeterminados de la pantalla Configuración del libro mayor permite completar automáticamente al menos las obligatorias que se muestran en la imagen anterior.

Las cuentas establecidas automáticamente por Etendo siempre pueden modificarse si es necesario.

La lista completa de cuentas relacionadas con el producto es:

- **Inmovilizado del producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar transacciones de inventario tales como:
  - Recuentos de inventario
  - Movimientos de inventario
  - y Recepción de mercancías

Esta cuenta suele ser una cuenta de activo.

- **Gastos del producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar los gastos de compra del producto.  
  Esta cuenta suele ser una cuenta de gastos.
- **Gasto de producto a periodificar**: este campo almacena la cuenta predeterminada que se utilizará para registrar gastos diferidos.  
  Esta cuenta suele ser una cuenta de activo.
- **Ingresos por el producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar los ingresos por ventas del producto.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Ingreso de producto a periodificar**: este campo almacena la cuenta predeterminada que se utilizará para registrar ingresos diferidos.  
  Esta cuenta suele ser una cuenta de pasivo.
- **Costo del producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar el coste de los bienes vendidos.  
  Esta cuenta suele ser una cuenta de gastos.
- **Devolución de Ingresos por el Producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar devoluciones de ventas.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Devolución del Costo del Producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar recepciones de material devuelto.  
  Esta cuenta suele ser una cuenta de gastos.
- **Desviación pr. factura**: este campo almacena la cuenta predeterminada que se utilizará para registrar diferencias de precio entre recepciones de mercancías contabilizadas y facturas de compra registradas.  
  Esta cuenta suele ser una cuenta de activo.

!!! info
    El botón de acción "Copiar cuentas" permite al usuario copiar las cuentas predeterminadas en esta ventana a la solapa Contabilidad del producto.

### Productos asignados

Productos asignados es una vista de todos los productos que pertenecen a una categoría del producto.

Como nota adicional, los productos no reales, como los productos de descuento, deberían pertenecer a un grupo de productos específico, denominado por ejemplo "Otros", como forma de mantenerlos aislados de los reales.

Para obtener más información sobre los productos de descuento, visite Descuento.

### Traducción

Mantiene traducciones de las categorías del producto a diferentes idiomas.
## Atributo

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Atributo`

### Visión general

Los productos pueden tener un atributo o un conjunto de atributos que los hace diferentes del resto.

Un atributo es una característica de un producto, como el color o la talla.

La capacidad de gestionar atributos de producto permite una definición adecuada de los productos y, además, asegura el cumplimiento de los requisitos de trazabilidad impuestos por la mayoría de las industrias.

Etendo permite gestionar los atributos de producto siguiendo los pasos que se indican a continuación:

1.  Creación de cada Atributo de Producto. Un Atributo puede ser un identificador único, como un número de serie, o puede tener una lista predefinida de valores, como los colores azul, blanco y rojo.  
    Para obtener más información, siga leyendo esta sección.
2.  Creación de Conjunto atributos, que puede contener un solo atributo o combinar un conjunto de atributos.  
    Para obtener más información, visite Conjunto atributos
3.  Configurar la relación entre el producto y el conjunto de atributos.  
    Para obtener más información, visite Producto

### Atributo

La ventana Atributo permite al usuario crear y editar atributos como el color o la talla para asignarlos a Conjunto atributos.

![](../../../../assets/drive/KgY7LbRbBSeTKiXl8B-P3rCchmCaJNIgLI3-PCgZZTgJrWVJdtXsYP7yRTR6tYNF3i_T6LtO8PMtzJ8FTiu1P5KtQvQD1SacDNeHwRbNWnGPzOPv9tZ56WT-Fo05Nkxt-unkwXF9BBe0ag8sbw.png)

Tal y como se muestra en la imagen anterior, un atributo puede definirse fácilmente introduciendo los datos relevantes que se indican a continuación:

- el **Nombre** del atributo
- una **Descripción** breve, si es necesario
- Si el atributo es único para cada instancia del producto, por ejemplo un número de lote o un número de serie, seleccione la casilla de verificación **Atributo instancia**.
- El indicador **Lista** permite al usuario indicar que el atributo tiene una lista predefinida de valores que se deben introducir en la solapa "Valor atributo".  
  Para obtener más información, visite Valor atributo.
- El indicador **Obligatorio** define el atributo como obligatorio; por lo tanto, siempre debe especificarse para el producto.

### Valor atributo

Un atributo puede tener varios valores o características individuales que se deben detallar para cada atributo.

Lo anterior aplica a atributos como el color o la talla.

La solapa Valor atributo permite la creación de tantos valores de atributo como sean necesarios para un atributo.
## Conjunto atributos

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Conjunto atributos`

### Visión general

Un conjunto de atributos puede definirse mediante un único atributo o mediante un conjunto de atributos para aplicar a productos específicos.

Si **un conjunto de atributos** incluye, entre otros, **un atributo que es único para cada instancia del producto**, por ejemplo, un número de lote o un número de serie, esta ventana es el lugar para definir qué **Control lote** o **Control nº serie** debe aplicarse para obtener ese atributo único.

Los pasos a seguir son:

- **Creación de la(s) secuencia(s) de número de lote**. Para saber cómo, visite Control lote
- **Creación de la(s) secuencia(s) de número de serie**. Para saber cómo, visite Control nº serie
- **Configurar la relación entre** la(s) **secuencia(s) de número de lote/serie** creada(s) previamente y el **Conjunto atributos**, en la ventana Conjunto atributos.  
  Para saber cómo, siga leyendo esta sección.

### Conjunto atributos

La ventana Conjunto atributos permite crear tantas combinaciones de atributos como sea necesario para definir productos con pocas o múltiples características.

![](../../../../assets/drive/eFfHmZoippBAg2UAyKfVODqUewZCKUFQwC-0lr71L_P1uTZIN8khQzaIzN7cPdDoP7ZrlW7RkGUjq24Y2SB3vwd4_zYLHPYxEDxttakbcdEVhUm_oIMyzQeLAByyByHFmOZYit4L2GHp0fHJgg.png)

Tal y como se muestra en la imagen anterior, un conjunto de atributos que se va a asignar a un(os) producto(s) específico(s) puede contener:

- un **Nombre** del conjunto de atributos
- una breve **Descripción** si es necesario
- un **Lote** o identificador único asignado a una cantidad determinada de ese producto.  
  Si **la marca Lote está seleccionada**, se muestra un nuevo campo denominado "**Control lote**" para que seleccione la secuencia de número de lote que deben seguir los productos vinculados a ese conjunto de atributos.
- un **Nº de serie** o un identificador único asignado a cada unidad del producto.  
  Si **la marca Nº de serie está seleccionada**, se muestra un nuevo campo denominado "**Control del número de serie**" para que seleccione la secuencia de número de serie que deben seguir los productos vinculados a ese conjunto de atributos.
- una **F. caducidad** o fecha hasta la cual se garantiza la calidad del producto.  
  Si **la marca F. caducidad está seleccionada**, se muestra un nuevo campo denominado "**Días de garantía**" para que introduzca el número de días durante los cuales se puede garantizar un producto.
- por último, la marca "**Se requiere por lo menos un valor**" implica que se requerirá al menos un valor del conjunto de atributos en las transacciones relacionadas con el producto.

### Atributos asignados

Un conjunto de atributos puede tener asignado un único atributo o un conjunto de atributos.

![](../../../../assets/drive/JKPixcSV3hgLjW-UlwcYfpGHyrKD1pT39o4XAyHeltD26-0fx1Kn5wXESm5DPoJtrVMistsa0OaXEZKaYLcxAfOG--fJgVgcXZzDWVGvU5xemPX_SiOMMirw-aIuq17LxKfgKlQ0Q3w4q7N3nA.png)

Tal y como se muestra en la imagen anterior, un conjunto de atributos puede tener solo un atributo, por ejemplo Color, o tantos atributos como sea necesario, por ejemplo Talla, número de lote y número de serie.

La forma de conseguirlo es simplemente seleccionar en esta solapa los atributos creados previamente.

Debe tener en cuenta que:

- si uno de los atributos seleccionados es un atributo de tipo "Lote" o de tipo "Nº de serie", la secuencia de numeración correspondiente debe haberse configurado correctamente en la ventana Conjunto atributos.
## Control lote

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Control lote`

### Visión general

Un atributo de producto puede ser un número de lote.

Algunos productos requieren numeración de lotes para asegurar el cumplimiento con los requisitos de trazabilidad impuestos por la mayoría de las industrias, lo cual implica que una cantidad determinada de un producto siempre debe estar vinculada a un número de lote único.

### Control lote

Un número de lote es un número único asignado a una cantidad concreta de un producto, que puede definirse con un prefijo o un sufijo, entre otras características.

![](../../../../assets/drive/zxXMUjr6dqf-ED398clHXDSahfNlz0oql8RmrUh4LopzsnqQ-wFiN-dP8Ss4YSbnYNA5k8UA1wdTE8uYU0SflUrJjuxkcBqgLrjxAb2yVTvglixLgh4gLQpu4gu9dASMfFCVavnkQldZGOvGGQ.png)

Una secuencia de números de lote puede configurarse:

- definiendo el primer número o **Número inicial** que se utilizará como número de lote
- especificando el valor por el cual el número de lote se **incrementará en**
- definiendo cuál es el **Valor actual** que se utilizará. Etendo actualiza el valor del número asignado siguiente a medida que se asignan los números de lote.
- introduciendo un **Prefijo** como **Lote N?/**, que ayuda a entender fácilmente que el número en cuestión es un número de lote.
- introduciendo un **Sufijo** como **/2011**, que ayuda a proporcionar información adicional si es necesario.
## Control nº serie

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Control nº serie`

### Visión general

Un atributo de producto puede ser un número de serie.

Algunos productos requieren numeración de serie para asegurar el cumplimiento con los requisitos de trazabilidad impuestos por la mayoría de las industrias, lo cual implica que:

- cada unidad de un producto siempre debe estar vinculada a un número de serie único.

### Nº serie

Un número de serie es un número único asignado a cada unidad de un producto/artículo, que puede definirse con un prefijo o un sufijo, entre otras características.

![](../../../../assets/drive/_I2P7xT_wcIiLPx2GnSTR3Ne4sqAemn-eWLFVQ1NKaTt_qHVVuQwKso1kczmCmlG6a3AyZeKI8iwolANuoRbYSd3RE0Fg5lmAIWc0kdvdjvPtgtD7cokdzHpLZ2yn3vrm9JM4nRAxYppGdOm8w.png)

Una secuencia de números de serie puede configurarse:

- definiendo el primer número o **Número inicial** que se utilizará como número de serie
- especificando el valor en el que el número de serie se **incrementará en**.  
  En el caso de los números de serie, siempre será "1".
- definiendo cuál es el **Valor actual** que se utilizará. Etendo actualiza el valor del siguiente número asignado a medida que se asignan los números de serie.
- introduciendo un **Prefijo** como **Nº serie?/**, que ayuda a entender fácilmente que el número en cuestión es un número de serie.
- introduciendo un **Sufijo** como **/2011**, que ayuda a proporcionar información adicional si fuese necesario.
## Marca

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Marca`

### Visión general

Esta ventana permite al usuario introducir marcas asociadas a un producto.
Las marcas son fabricantes o nombres comerciales utilizados por los fabricantes para identificar una línea de producto.

### Cabecera

Para utilizar esta funcionalidad, seleccione una organización y añada una nueva marca en los campos correspondientes. También es posible introducir una descripción cuando sea necesario.

![](../../../../assets/drive/aZfc6Qanmv-C8prh4FgF0KT-ykE3xADBzz57qx01JIBzwouPawsewFcMRjpJ5sN5_kT2VTxnNlwcTCnEYDNswMyijThPC8K634MtikPrLKcmBqYSQ08OH6ZYPedFBlir-8rueg7FQgv1ykKgekY.png)

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.