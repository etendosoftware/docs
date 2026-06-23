---
title: Producto
tags:
  - Gestión de datos maestros
  - Etendo
  - Producto
  - Inventario
  - Costes
---

## Producto { #product }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Producto`

### Descripción general { #overview }

La ventana Producto es donde se crea y gestiona el catálogo de todo lo que la organización compra, vende o fabrica: bienes físicos, servicios y materias primas. Para cada producto, puede definir su precio, las cuentas utilizadas para la contabilización, los niveles de stock, los proveedores y los datos de fabricación. Cada uno de estos aspectos se gestiona en una solapa independiente dentro de la ventana.

La ventana Producto está organizada en las siguientes solapas:

- **Producto**: Campos de la cabecera principal: tipo de producto, unidad de medida, categoría, indicadores de precio, atributos y configuración de ingresos/gastos diferidos.

    - **Precio**: Asignaciones de tarifa y reglas de precio.
    - **Contabilidad**: Cuentas del libro mayor para las transacciones.
    - **Lista de Materiales**: Componentes para productos de tipo paquete.
    - **Regla de Coste**: Método de cálculo de costes por rango de fechas.
    - **Coste**: Historial de costes e introducción manual de costes.
    - **Operaciones**: Registro de solo lectura de movimientos de inventario.
    - **Compras**: Datos de proveedor y de compras.
    - **Producción**: Datos del plan de producción.
    - **Traducción**: Traducciones del nombre del producto.
    - **Características**: Características de variante del producto.
    - **Coste Unitario**: Coste unitario calculado.
    - **Stock**: Stock disponible por hueco.
    - **UOM Alternativa**: Unidades de medida alternativas.

## Cabecera { #header }

La ventana **Producto** permite la creación de artículos tales como productos, materias primas, recursos, servicios, etc.

La información requerida para crear un **Producto** en Etendo viene determinada por la naturaleza del **Producto**, su tipo de producto.

Hay cuatro tipos de producto disponibles:

- **Artículo**. El tipo de producto más utilizado es *Artículo*. El inventario mantenido para reventa, los materiales que se incorporan a un proceso de producción y los productos semielaborados o terminados creados mediante producción son ejemplos de productos definidos usando el tipo de producto *Artículo*.
    - Un artículo debe marcarse como **Almacenado** si se requiere el seguimiento de cantidades del artículo; en caso contrario, no es necesario marcarlo como **Almacenado**.
    - Un artículo debe marcarse como **Producción** si el artículo se utiliza en fabricación.
    - Si un artículo es un producto intermedio o terminado, su lista de materiales (BOM) debe detallarse en la solapa **Lista de Materiales**.
- **Servicio**. Este tipo de producto se utiliza para identificar prestaciones como servicios profesionales, transporte, telefonía y otros artículos que no se corresponden con bienes materiales.
    - Por lo tanto, un servicio no es almacenable, pero puede comprarse o venderse.
    - Un servicio puede tener una lista de materiales que se definirá en la solapa **Lista de Materiales**.
- **Recurso** y **Gasto**. Estos tipos de producto pueden utilizarse para distinguir entre diferentes tipos de productos que pueden comprarse o venderse, pero no pueden almacenarse.
    - El tipo Recurso puede utilizarse para configurar recursos como recursos financieros, legales o naturales utilizados por la organización.
    - El tipo Gasto puede utilizarse para configurar gastos como gastos de viaje que se usarán al informar los gastos de empleados.

!!! info
    Los tipos de producto no afectan al modo en que las transacciones se contabilizan en el libro mayor. Todos los tipos de producto se contabilizan de la misma manera al comprarse, almacenarse o venderse, utilizando las cuentas del libro mayor definidas en la solapa **Contabilidad**.

![Campos del formulario de encabezado de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-1.png)

Los datos clave adicionales a completar son:

- **Unidad**, es decir, la unidad de medida que se utilizará al comprar, almacenar y vender un producto, por ejemplo *Unidades*.  
    Un producto también puede tener unidades alternativas además de la unidad del producto.
- **Categoría del producto**, es obligatorio seleccionar una categoría del producto a la que pertenecerá el producto.  
    Para saber más, visite [Categoría de producto](../product-setup/product-category.md).
- **Categoría de Impuesto**, esta categoría es clave para gestionar los impuestos relacionados con el producto. Impuestos como el IVA dependen del tipo de producto.  
    Para saber más, visite [Categoría de Impuesto](../../financial-management/accounting/setup/tax-category.md).
- La casilla **Compra** puede seleccionarse para indicar que el producto puede comprarse a un proveedor externo. Esta casilla es principalmente informativa, ya que no añade lógica de negocio por sí misma, salvo en lo relativo a MRP.  
    En ese caso, si está seleccionada, MRP comprará el producto si es necesario; en caso contrario, lo producirá.
- La casilla **Ventas** puede seleccionarse para indicar que el producto se vende o puede venderse a terceros o clientes externos. Esta casilla es informativa, ya que no añade lógica de negocio por sí misma.
- La casilla **Almacenado** se selecciona si el producto forma parte del inventario; por lo tanto, se registran en Etendo las transacciones de movimientos de inventario correspondientes.  
    Este indicador ya no puede modificarse para un producto si dicho producto forma parte de cualquier documento relacionado con ventas, compras, inventario o producción, independientemente del estado del documento.
- La casilla **Producción** se selecciona si el producto forma parte de un proceso de producción. Una vez seleccionada, aparece un campo adicional para seleccionar un *Plan de Producción*.  
    Para saber más, visite [Plan de Producción](../../production-management/setup.md#process-plan).
- **Conjunto atributos**, un producto puede tener un grupo de características o un conjunto de atributos, como **Color y talla**, a tener en cuenta al pedir o almacenar el producto.

    - Si aquí se selecciona un **Conjunto atributos**, Etendo muestra un nuevo campo llamado **Valor atributos**. Para saber más, visite [Conjunto atributos](../product-setup/attribute-set.md).

- **Valor atributos**, si se selecciona un valor del conjunto de atributos como *Azul y grande*, Etendo muestra un nuevo campo llamado **Valor del Conjunto de Atributos como**.
- **Valor del Conjunto de Atributos como**, una vez seleccionado un conjunto de atributos, este puede utilizarse como se describe a continuación según el criterio seleccionado en este campo:

    - **Por defecto**: el sistema rellena previamente el valor del atributo (por ejemplo, Talla = *Mediana*), pero el usuario puede cambiarlo en cada transacción.
    - **Sobrescribir Especificación**: el valor del atributo define completamente el producto (por ejemplo, *Cerveza sin alcohol* = 0% de graduación alcohólica), pero puede modificarse para registrar excepciones (por ejemplo, una desviación en producción).
    - **Especificación**: el valor del atributo es fijo y no puede modificarse en ninguna transacción (por ejemplo, *Vaqueros grandes azules* siempre tiene Talla *L* y Color *Azul*).

    !!! info
        Para saber más sobre atributos, visite los artículos [Atributo](../product-setup/attribute.md) y [Conjunto de atributos](../product-setup/attribute-set.md).
- **UPC/EAN**, utilizado para almacenar información de código de barras
- La casilla **Lista de materiales** se selecciona cuando el producto es un paquete de otros productos, tal como se lista en la solapa **Lista de Materiales**.

- **Ingresos diferidos** aplica cuando un producto se vende pero el ingreso debe registrarse a lo largo del tiempo en lugar de todo de una vez — por ejemplo, una suscripción anual a un software. Cuando se habilita este indicador, se define durante cuántos meses deben distribuirse los ingresos y cuándo comienza dicha distribución.

    Este indicador solo es visible para productos con la casilla **Ventas** habilitada. Cuando está marcado, el grupo de campos **Plan de ingresos** se hace visible con los siguientes campos:

    - **Tipo de plan de ingresos**: este campo especifica la frecuencia por defecto de la distribución de ingresos. Actualmente, solo se admiten planes de ingresos mensuales.
    - **Número de periodo**: este campo especifica la duración por defecto de un plan de ingresos. Por ejemplo, una suscripción anual a una revista se definirá con un plan de ingresos de 12 periodos mensuales, mientras que un abono de esquí de temporada tendrá un plan de ingresos de 5 periodos mensuales.
    - **Periodo por defecto**: este campo especifica el primer periodo en el que se reconocerán los ingresos. Las opciones disponibles son:

        - _Mes actual_. Esta opción establecerá el Periodo de inicio del plan de ingresos en el mismo periodo que el periodo contable de la factura.
        - _Mes siguiente_. Esta opción establecerá el Periodo de inicio del plan de ingresos en el siguiente periodo contable de la factura.
        - _Manual_. Esta opción no establecerá ningún periodo de inicio del plan de ingresos; por lo tanto, se podrá seleccionar un periodo de inicio al crear la línea de la factura de cliente.

- **Gastos diferidos** aplica cuando un producto se compra pero el coste debe registrarse a lo largo del tiempo — por ejemplo, un servicio prepagado. Cuando se habilita este indicador, se define el periodo de distribución y el mes de inicio.

    Este indicador solo es visible para productos con la casilla **Compra** habilitada. Cuando está marcado, el grupo de campos **Plan de gastos** se hace visible con los siguientes campos:

    - **Tipo de plan de gastos**: este campo especifica la frecuencia por defecto de la distribución de gastos. Actualmente, solo se admiten planes de gastos mensuales.
    - **Número de periodo**: este campo especifica la duración por defecto de un plan de gastos.
    - **Periodo por defecto**: este campo especifica el primer periodo en el que se reconocerá el gasto. Las opciones disponibles son:

        - _Mes actual_. Esta opción establecerá el Periodo de inicio del plan de gastos en el mismo periodo que el periodo contable de la factura.
        - _Mes siguiente_. Esta opción establecerá el Periodo de inicio del plan de gastos en el siguiente periodo contable de la factura.
        - _Manual_. Esta opción no establecerá ningún periodo de inicio del plan de gastos; por lo tanto, se podrá seleccionar un periodo de inicio al crear la línea de la factura de proveedor.

Estos valores se utilizan cuando se crea una factura para un producto que tiene un plan de gastos y/o un plan de ingresos.

Del mismo modo, estos valores también se utilizan cuando se crea una factura a partir de otro documento (por ejemplo: el proceso Facturar que crea facturas a partir de pedidos de venta). Del mismo modo, estos valores pueden modificarse transacción por transacción.

Para saber más, visite el artículo [Cómo gestionar ingresos y gastos diferidos](../../../how-to-guides/how-to-manage-deferred-revenue-and-expenses.md).

- **Registrar con precio de compra**: este indicador se utiliza al contabilizar un documento de **Albarán (Proveedor)** o una **Factura (Proveedor)** conciliada en el libro mayor.  
    Normalmente, se utiliza el coste del producto al contabilizar esas transacciones; sin embargo, esta casilla permite usar el precio de compra del producto en su lugar.  
    Esta funcionalidad solo funciona para el tipo de producto *Gasto* que no tenga seleccionada la casilla **Ventas**.

!!! info
    Tenga en cuenta que, en este caso, es necesario que un **Pedido de compra** esté relacionado con el **Albarán (Proveedor)**; de lo contrario, se mostrará un mensaje de error, ya que se requiere el precio de compra del producto.

- **Retornable**: seleccione esta casilla para indicar que el producto puede ser devuelto por un cliente. Cuando se selecciona esta casilla, el campo **Días de Retraso en Devolución** queda disponible. Si intenta devolver un producto no retornable desde la ventana Devolución de cliente, Etendo mostrará un mensaje de error.

![Campo Retornable en la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-2.png)

- **Días de Retraso en Devolución**: en este campo, es posible configurar la cantidad máxima de días antes de que un producto ya no pueda devolverse. Si el campo se deja en blanco, el producto puede devolverse sin limitaciones de tiempo. Al intentar devolver un producto cuyo periodo ha expirado, aparecerá un mensaje de advertencia.

![Mensaje de advertencia de Días de Retraso en Devolución](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-3.png)

!!! info
    Si la casilla **Almacenado** no está marcada y la casilla **Lista de materiales** está marcada, el precio del producto debe establecerse en 0. En este caso, el precio total se calcula automáticamente a partir de los precios de los componentes individuales listados en la solapa **Lista de materiales**. Para aplicar promociones o descuentos, use la funcionalidad Descuentos y promociones.

### Variantes { #variants }

El producto puede marcarse como **Es genérico**. Esto significa que se crearán variantes de este producto basadas en algunas características como color, talla, etc. La definición de estas características tiene lugar en el producto genérico, por lo que puede decirse que un producto genérico es como una plantilla en la que las nuevas variantes heredarán todos los atributos (impuestos, precios, imagen) de este producto. Debido a esto, un producto genérico no puede utilizarse en transacciones, sino sus variantes.

!!! info
    Los productos marcados como genéricos no pueden utilizarse en operaciones de transacción como pedidos de venta, pedidos de compra, albaranes, etc.

Cuando se marca este indicador, se muestran dos botones:

- El botón **Gestionar variantes** muestra todas las combinaciones de variantes posibles para el producto genérico, tanto las ya creadas como las que aún no se han creado. Es muy útil en dos situaciones:

    ![Botones Gestionar variantes y Crear variantes en un producto genérico](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-4.png)

    - El usuario quiere crear solo algunas combinaciones, no todas. El botón permite revisar y seleccionar combinaciones específicas antes de crearlas.
    - El usuario añade un nuevo valor de característica (por ejemplo, Rojo, cuando ya existían Azul y Blanco) y quiere ver qué nuevas combinaciones están ahora disponibles.

    Por ejemplo, imagine que el producto genérico *Camiseta Modelo A* tiene las características:

    - Color: Azul, Blanco
    - Talla: S, M, L

    Pero todavía no se han creado variantes. Si pulsa el botón, puede ver todas las combinaciones posibles:

    ![Todas las combinaciones de variantes posibles para un producto genérico](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-5.png)

    Entonces pueden seleccionarse todas las combinaciones o elegir solo algunas. Una vez que se pulsa **Hecho**, las combinaciones seleccionadas se crean como registros de producto individuales. Cada nuevo producto queda vinculado al producto genérico original mediante el campo **Producto genérico** — este vínculo significa que la variante hereda precios, impuestos e imágenes del producto genérico.


- El botón **Crear variantes** crea todas las variantes de producto, es decir, todas las combinaciones basadas en las características definidas.

    ![Variantes de producto creadas listadas en la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-6.png)

- Otro botón que puede aparecer es **Actualizar característica**. Solo aparece cuando el producto genérico o la nueva variante de producto tiene relacionada una característica no variante. Dos escenarios:

    ![Botón Actualizar característica](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-7.png)

    1.  **Producto genérico**: este botón permite introducir el valor de esa característica.  
    Imagine que la característica es *Línea de moda*, que tiene tres valores: *Sport*, *Vintage*, *Classic*.  
    A diferencia de las características que son variantes, los usuarios no pueden introducir el valor mediante la solapa **Configuración de características**.

    2.  **Producto variante**: este botón permite al usuario introducir/actualizar la característica que no es variante.


Una vez creada una variante, sus características y valores pueden visualizarse en la vista de grilla o en la vista de formulario:

- Vista de grilla: hay una nueva columna **Descripción de característica**. Esta columna se calcula y no es editable. Muestra las características con sus valores como texto. Esta columna tiene un nuevo selector de búsqueda para encontrar variantes de producto en función de sus características.

    ![Columna Descripción de característica en la vista de grilla del producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-8.png)

- Vista de formulario: las variantes de producto tienen una nueva sección llamada **Descripción de característica**. Esta sección contiene tantos campos como características diferentes tenga el producto.

La preferencia **Mostrar Características de Producto padres** controla cuántos niveles de la jerarquía de una característica se muestran en la vista de formulario de la ventana **Producto**. Establézcala en un número (1, 2, 3, etc.) para controlar cuántos niveles superiores aparecen por encima de un valor. Por ejemplo, si la jerarquía es `Color` > `Verde` > `Verde claro` > `0034` y la preferencia está establecida en `2`, el formulario mostrará *Verde claro* y su padre *Verde*, pero no el nivel superior *Color* ni el código `0034`. Esta preferencia se establece en la ventana **Preferencias**. Contacte con su administrador del sistema si necesita cambiarla.

Se pueden añadir nuevos valores de una característica existente. Por ejemplo, el color *Rojo* cuando ya se dispone de *Azul* y *Blanco*. Cuando esto ocurre, este nuevo valor se añade automáticamente a todos los productos genéricos que ya tienen la característica *Color*. Este nuevo valor estará presente en la solapa de configuración, pero desactivado. Si el usuario quiere utilizarlo en un producto específico para crear nuevas variantes, puede simplemente activar el valor y usar el botón **Gestionar características**.

### Modificar Impuesto { #modify-tax }

**Modificar Impuesto** permite que un producto de tipo servicio (como la instalación) cambie automáticamente el tipo impositivo aplicado a los bienes que acompaña — por ejemplo, los muebles vendidos con instalación pueden tener un tipo impositivo diferente que los muebles vendidos sin ella. Esta funcionalidad aplica únicamente a los Pedidos; los documentos creados posteriormente toman la información fiscal del Pedido. Esta funcionalidad es configurada por un administrador.

Esta modificación de impuestos se implementa mediante un servicio vinculado al producto. Este servicio debe marcarse como capaz de modificar los impuestos de los productos vinculados y también debe especificarse la configuración de los productos a los que se modificarán los impuestos y la nueva categoría de impuesto a aplicar.

Para configurarlo, vaya a la ventana **Producto** y cree un nuevo servicio. Un servicio es simplemente un producto con el campo **Tipo de producto** establecido en *Servicios*. También deben activarse el campo **Vinculado a producto** y el campo **Modificar Impuesto**. Cuando este campo se activa, se hace visible una nueva solapa llamada **Modificar Categorías de Impuestos**. En esta solapa se define la configuración de las categorías de impuestos de los productos que este servicio modificará cuando esté vinculado y la nueva categoría de impuesto a aplicar.

![Configuración de la solapa Modificar Categorías de Impuestos](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-11.png)

Para facilitar el proceso de configuración, se han añadido dos componentes:

1. **Modificar Impuesto para Categoría del producto** (Botón): ventana **Seleccionar y ejecutar** para asignar las categorías del producto y las categorías de impuestos en la misma acción.

![Botón Modificar Impuesto para Categoría del producto — ventana Seleccionar y ejecutar](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-12.png)

2. **Copiar configuración de Modificar Impuesto del servicio** (Botón): ventana **Seleccionar y ejecutar** donde se muestran los servicios que modifican impuestos. El usuario puede seleccionar uno o varios servicios, y la configuración actual se asignará a los servicios seleccionados. Una vez ejecutado el proceso, la configuración antigua (si existe) se eliminará y se añadirá una nueva. Este proceso ayuda a desplegar la misma configuración en múltiples servicios.

![Botón Copiar configuración de Modificar Impuesto del servicio — ventana Seleccionar y ejecutar](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-13.png)

## Solapas y subsolapas { #tabs-and-subtabs }

La ventana Producto está organizada en las siguientes solapas, cada una de las cuales cubre un aspecto específico del registro del producto:

### Precio { #price }

Un producto puede formar parte de muchas Versiones de tarifa que son válidas para un periodo de tiempo determinado.


Hay dos formas en las que el usuario puede hacer que un producto forme parte de una Tarifa:

1.  **seleccionando la/s Tarifa/s** e introduciendo los valores de *Precio unitario* y *Precio tarifa* en la solapa Tarifa, mientras se crea el producto.  
    Como consecuencia, el producto que se está creando también formará parte de la Tarifa seleccionada.
2.  **seleccionando el producto** e introduciendo los valores de *Precio unitario* y *Precio tarifa*, mientras se crea la *Tarifa*.  
    Como consecuencia, la Tarifa, así como los valores de *Precio unitario* y *Precio tarifa*, se mostrarán automáticamente en la solapa *Tarifa* del producto.  
    Para obtener más información, visite [Tarifa](../pricing/price-list.md).

#### Versión de Regla de Precio { #price-rule-version }

Esta solapa solo estará disponible cuando se seleccione el campo **Is Price Rule Based**. Esta solapa ofrece la posibilidad de añadir Reglas de Precio de Servicios al Servicio a partir de una fecha determinada.

![Solapa Versión de Regla de Precio](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-15.png)

En esta ventana también es posible definir importes máximos y mínimos que se tendrán en cuenta al mostrar servicios.

Estos importes definen un intervalo entre precios de producto, de manera que el servicio solo estará disponible para añadirse en caso de que la suma de los productos seleccionados esté dentro del intervalo.

Para servicios con regla de cantidad: Cantidad única, la cantidad de la línea es relevante, ya que solo se añadirá un servicio.

Para servicios con regla de cantidad: Según producto, la cantidad de la línea no es relevante; solo importa el precio del producto, ya que se añadirán tantos servicios como productos se seleccionen. Solo si los precios de todos los productos están dentro del tramo, se mostrará el servicio.

Además, si una vez que se ha añadido un servicio (aún no entregado) al albarán, cambia el precio del producto relacionado, se activará una validación y, en caso de que el servicio ya no cumpla las reglas del tramo, se eliminará del albarán actual y se mostrará un pop-up indicándolo.

### Contabilidad { #accounting }

La solapa Contabilidad permite al usuario configurar las cuentas contables que se utilizarán al contabilizar transacciones relacionadas con el producto, como la compra o la venta del producto, en el libro mayor.

![Solapa Contabilidad de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-16.png)

Tal y como se muestra en la pantalla anterior, puede configurar para cada producto y libro mayor algunas cuentas que se utilizarán en las transacciones que se listan a continuación:

- **Inmovilizado del producto**: este campo almacena la cuenta por defecto que se utilizará para registrar transacciones de inventario tales como:
  - Recuentos de inventario
  - Movimientos de inventario
  - y Albarán (Proveedor)

Esta cuenta suele ser una cuenta de activo.

- **Gastos del producto**: este campo almacena la cuenta por defecto que se utilizará para registrar las compras del producto:
  - Normalmente, esta cuenta puede configurarse como un tipo de cuenta de *Gasto* en caso de no gestionar *Inventario perpetuo*.  
    En ese caso, el gasto se contabiliza en el momento en que se compran los bienes, al precio de compra.  
    El ingreso se contabiliza en el momento en que se venden los bienes, al precio de venta.  
    No gestionar *Inventario perpetuo* implica la necesidad de ajustar manualmente el valor del inventario al final del año.  
    Ese ajuste de inventario implica calcular la diferencia entre el *Valor final del inventario* y el *Valor inicial del inventario*.
  - Sin embargo, esta cuenta también puede configurarse como una cuenta de *Activo* en caso de gestionar *Inventario perpetuo*.  
    En ese caso, el gasto debe contabilizarse cuando el producto se vende al cliente como *Coste de los bienes vendidos* al coste del producto.  
    En Etendo, el ingreso se contabiliza en el momento en que se venden los bienes al precio de venta y el coste de los bienes vendidos se contabiliza en el momento del envío de los bienes al coste del producto.  
    Gestionar *Inventario perpetuo* no implica la necesidad de ajustar el valor del inventario al final del año.
- **Gasto de producto a periodificar**: este campo almacena la cuenta por defecto que se utilizará para registrar gastos diferidos.  
  Esta cuenta suele ser una cuenta de activo.
- **Ingresos por el producto**: este campo almacena la cuenta por defecto que se utilizará para registrar los ingresos por ventas del producto.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Ingreso de producto a periodificar**: este campo almacena la cuenta por defecto que se utilizará para registrar ingresos diferidos.  
  Esta cuenta suele ser una cuenta de pasivo.
- **Costo del producto**: este campo almacena la cuenta por defecto que se utilizará para registrar el coste de los bienes vendidos.  
  Esta cuenta suele ser una cuenta de gasto.
- **Devolución de Ingresos por el Producto**: este campo almacena la cuenta por defecto que se utilizará para registrar devoluciones de ventas.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Devolución del Costo del Producto**: este campo almacena la cuenta por defecto que se utilizará para registrar el coste de los bienes vendidos en devoluciones de ventas.  
  Esta cuenta suele ser una cuenta de gasto.
- **Desviación pr. factura**: este campo almacena la cuenta por defecto que se utilizará para registrar diferencias de precio entre Albaranes (Proveedor) contabilizados y Facturas (Proveedor) registradas.  
  Esta cuenta suele ser una cuenta de activo.

Inicialmente, estas cuentas se heredan de las cuentas por defecto de la configuración del libro mayor de la organización para la cual se está creando el producto. El usuario final siempre puede modificarlas.

!!! info
    Además, es importante remarcar que es posible configurar la creación de nuevas cuentas correlativas para los productos, tal y como se describe en la solapa **Libros mayores** de la ventana **Organización**.

### Lista de materiales { #bill-of-materials }

Esta solapa permite editar los componentes de la lista de materiales de los que consta el producto seleccionado.

La Lista de materiales aplica a productos marcados como **Lista de materiales**.

Esta solapa proporciona información de la lista de productos contenidos y su cantidad para la producción de la Lista de materiales.

Si la Categoría de Impuesto del producto está marcada como `As per BOM`, esta solapa también proporciona información del precio de cada producto en la lista de la Lista de materiales. El precio y la cantidad de esta lista se utilizan para realizar la división del importe base para calcular los impuestos en función de los impuestos configurados para cada producto de la lista.

![Solapa Lista de materiales de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-17.png)

Tras añadir todos los componentes, haga clic en el botón **Comprobar LDM** en el registro del producto. Esto valida la estructura de la Lista de materiales — confirmando que todos los componentes y cantidades requeridos están correctamente introducidos — y marca el producto como listo para su uso en [Producción LDM](../../../warehouse-management/transactions/bill-of-materials-production.md).

### Regla de cálculo de costes { #costing-rule }

La solapa **Regla de cálculo de costes** permite al usuario revisar las reglas de cálculo de costes que se aplican al producto dentro de un rango de fechas determinado.

Las reglas de cálculo de costes se aplican a los productos configurados como tipo *Artículo* y marcados como **Almacenado**.

Esta solapa proporciona información sobre la(s) regla(s) de cálculo de costes validada(s) que se aplica(n) al producto en un rango de fechas determinado, así como el **Algoritmo de cálculo de costes** definido para esa regla.

Las reglas de cálculo de costes se pueden crear y validar en la ventana **Regla de cálculo de costes**, relacionada con la entidad legal / organización correspondiente.

La moneda utilizada por la regla de cálculo de costes es la moneda configurada para la organización.

![Solapa Regla de cálculo de costes de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-18.png)

### Costo { #costing }

La solapa **Costo** muestra el historial de costes del producto y permite introducir un coste inicial cuando se incorpora por primera vez al sistema. Esta sección es gestionada habitualmente por el equipo de contabilidad. Si necesita ajustar el coste de un producto, contacte con su administrador del sistema o su contable.

La solapa **Costo** recopila y resume la información relacionada con el coste del producto como resultado de cada transacción del producto. Los costes del producto son válidos durante un rango de fechas fijo y pueden calcularse utilizando un algoritmo de cálculo de costes *Average* o *Standard*.

Una de las primeras cosas que debe hacer al crear o importar un producto en Etendo es informar a Etendo sobre:

1.  el **Costo** inicial de los productos, si lo hubiera, introduciéndolo en esta solapa.  
    Siga leyendo para aprender cómo hacerlo.
2.  y el **Stock** inicial de los productos, si lo hubiera, creando y contabilizando un Inventario físico.

En general, esta solapa permite:

- **definir el Coste** de los productos almacenables; ese coste puede ser un coste estándar o un coste medio.
- **definir el Coste** de los productos no almacenables; en este caso debe ser un coste estándar.

Del mismo modo, también debe definirse para la **Organización** una Regla de cálculo de costes *Standard* o *Average* como forma de calcular el coste de las transacciones de los productos dentro de esa organización.

- **revisar el coste medio** calculado por el Servidor de Costes cuando se utiliza un Algoritmo de cálculo de costes *Average*.

Tenga en cuenta que, al utilizar un algoritmo de cálculo de costes *Standard*, el coste de cada transacción del producto es el *coste estándar por defecto* introducido en esta solapa.  
!!! info
    El *coste estándar por defecto* puede ser utilizado por el método de Coste por defecto siempre que no sea posible obtener el precio de una transacción para la cual sea necesario calcular su coste.

Los algoritmos *Average* sobrescriben el comportamiento del método de *Coste por defecto*, priorizando el uso del *Coste medio* actual, si existe.

- y, por último, disponer de una vista de todas las transacciones de entrada del producto que han impactado en el cálculo del coste del producto.
  - Las transacciones de entrada, como los albaranes de proveedor, son las que impactan en el cálculo del coste del producto; por lo tanto, el campo *Operaciones de almacén* las refleja claramente una a una.
  - De forma similar, un ajuste manual de coste *permanente* ejecutado en una transacción de salida, como un *Movimiento de mercancías desde* (M-), impacta en el cálculo del coste del producto; por lo tanto, el campo *Operaciones de almacén* refleja claramente este tipo de transacciones de salida.
  - La última transacción informa sobre:
    - el último coste, válido hasta una fecha final determinada
    - y la cantidad total de unidades de ese producto que están valoradas a ese coste.

Aquí también son visibles los costes calculados por el motor *legacy*.

Es posible reconocerlos por su tipo de coste:

- **Legacy Average**
- y **Legacy Standard**.

![Solapa Costo de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-19.png)

La forma de definir el **Costo** de un producto implica introducir la siguiente información detallada:

- La **Organización** para la cual aplican los costes calculados. Tenga en cuenta que la organización debe ser de tipo *Entidad Legal*.
- El **Tipo de costo**. Hay dos tipos de coste disponibles: _Standard_ y _Average_.
- El **Costo** del producto; ese coste puede ser el coste unitario estándar del producto o el coste unitario medio del producto.
- Una **Fecha de inicio** desde la cual es válido el coste inicial del producto introducido.
- Una **Fecha final**, hasta la cual es válido el coste inicial del producto introducido; por ejemplo, 31-12-9999.  
  Esto equivale a decir que el coste introducido es válido hasta que un nuevo movimiento de ese producto tenga fecha en un día anterior a 31-12-9999. Obviamente, ese nuevo movimiento de entrada cambiará el coste del producto.

Además:

- el **indicador Manual** permite al usuario diferenciar las transacciones de coste introducidas manualmente de las creadas automáticamente por Etendo.
  - las creadas manualmente por usted al introducir la información de coste por defecto del producto deben marcarse como Manual.
  - las automáticas relacionadas con la contabilización de Transacciones de material no se marcarán como Manual.
- el **indicador Permanente** bloquea la posibilidad de eliminar el coste manualmente. Todos los costes deben establecerse como Permanente.
- el **Almacén** permite disponer de un coste diferente por almacén cuando se desee y siempre que la Regla de cálculo de costes definida permita hacerlo.

!!! warning
    Tenga en cuenta que no debe completar este campo si la Regla de cálculo de costes no tiene marcado el campo Dimensión de Almacén.

### Operaciones { #transactions }

La solapa **Operaciones** es una vista resumida de todas las transacciones de un producto.

No existe una forma para que el usuario cree directamente nuevas transacciones de producto en la solapa de operaciones.

Las transacciones de producto de cualquier tipo se guardan automáticamente y se listan en esta solapa a medida que se contabilizan en Etendo.

![Solapa Operaciones de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-20.png)

Tal y como se muestra en la imagen anterior, Etendo guarda y nos informa de los siguientes datos relevantes para cada tipo de transacción de producto:

- **Hueco** donde el producto ha sido almacenado o del que se ha retirado
- **Cant. movida**, como el número de unidades de producto movidas internamente o bien de entrada o de salida
- **Fecha del movimiento**, como la fecha de la transacción del producto
- **Tipo de Movimiento**, como por ejemplo:
  - **Albarán (Cliente)**, este tipo puede tener:
    - una cantidad movida negativa cuando un producto se envía a un cliente en un documento de **Albarán (Cliente)**.
    - una cantidad movida positiva cuando un producto se devuelve desde un cliente en una recepción de devolución de material.
  - Consumo interno, como las unidades consumidas en actividades internas tales como proyectos, reparaciones. Este tipo puede ser:
    - **Positivo** si las unidades del producto reducen el stock del almacén
    - o **Negativo** si se cancela una transacción de consumo interno; esto funciona como cuando se cancela un envío.
  - Entrada de inventario, esto se relaciona con un recuento de inventario físico superior al stock contabilizado para un producto en Etendo.
  - Salida de inventario, esto se relaciona con un recuento de inventario físico inferior al stock contabilizado para un producto en Etendo.
  - Movimiento desde, esto se relaciona con movimientos de mercancía desde un almacén y hueco
  - Movimiento a, esto se relaciona con movimientos de mercancía hacia un almacén y hueco
  - **Producción**, como las unidades de un producto incluidas en un esfuerzo de trabajo. Este tipo puede ser:
    - **Positivo**, para P+ cuando los productos se añaden al almacén
    - o **Negativo**, para P- cuando los productos se consumen
  - Recepciones de proveedor, este tipo puede tener:
    - una cantidad movida positiva cuando un producto se recibe de un proveedor en un documento de **Albarán (Proveedor)**.
    - una cantidad movida negativa cuando un producto se devuelve a un proveedor en un envío de devolución a proveedor.

Etendo también nos informa sobre la información específica de:

- **Línea Albarán/Albarán (Proveedor)**
- **Línea de almacén**
- **Línea de movimiento**
- **Línea de producción**
- o **Asunto proyecto**

de la transacción del producto, según corresponda.

También es posible revisar:

1\. El **Costing Status** de una transacción.

El estado de cálculo de costes de una transacción puede ser cualquiera de los que se listan a continuación y tiene mucho que ver con el **Proceso en segundo plano de cálculo de costes**:

- **Not Calculated**. Este estado significa que el **Proceso en segundo plano de cálculo de costes** todavía no ha tomado la transacción para calcular su coste.
- **Cost Calculated**. Este estado significa que el **Proceso en segundo plano de cálculo de costes** ya ha tomado la transacción y su coste ha sido calculado.
- **Pendiente**. Este estado se ha implementado para evitar que el **Proceso en segundo plano de cálculo de costes** lance un error cuando no es posible calcular el coste de una transacción.  
  Este estado no es utilizado por los algoritmos de cálculo de costes implementados actualmente en Etendo, pero puede ser utilizado por otros algoritmos de cálculo de costes como FIFO para aquellos casos en los que se contabiliza una transacción de salida de producto sin contabilizar su correspondiente transacción de entrada de producto.
- **Omitir**. Este estado se ha implementado para que el **Proceso en segundo plano de cálculo de costes** no tenga en cuenta las transacciones establecidas como *Omitir* al calcular costes.  
  Este estado no es utilizado por los algoritmos de cálculo de costes implementados actualmente en Etendo, pero podría ser utilizado por otros algoritmos de cálculo de costes.

2\. y si el coste de una transacción ha sido calculado o no.

En cuanto una transacción de producto tiene su coste calculado por el **Proceso en segundo plano de cálculo de costes**, el campo **Es coste calculado** toma el valor *Sí*.

Una vez calculado el coste de una transacción, también puede ver:

- **Coste Original Trx**, que es el coste original de la transacción
- **Coste Total**, que es la suma del coste original de la transacción y todos los costes de ajuste de cualquier tipo.
- **Coste Unitario**, que es la suma del coste original y todos los ajustes de tipo *coste unitario*.
- **Moneda** utilizada para los cálculos.

Adicionalmente, el campo **Coste Permanente** informa de si el coste de una transacción es permanente o no. En caso de ser permanente, ya no se modificará.

Por último, es importante remarcar que, en el caso del algoritmo de coste *Promedio*, el coste *promedio* de un producto se calcula como *Promedio móvil*.

El coste promedio de un producto se calcula en base al flujo de transacciones del producto; por lo tanto, es la suma o resta del *Coste Total* de las transacciones listadas para el producto, dividido entre la suma de la *Cantidad acumulada* de las transacciones.

Por ejemplo, el coste promedio de un producto cuyas transacciones se listan a continuación es igual a 23.33 = (2000.00-1000.00+2500.00)/(100-50+100):

- albarán de proveedor para una cantidad movida 100 con un coste total de 2000
- albarán de cliente para una cantidad movida -50 con un coste total de 1000
- albarán de proveedor para una cantidad movida 100 con un coste total de 2500

#### Ajuste manual de coste { #manual-cost-adjustment }

Adicionalmente, el coste de una transacción puede modificarse haciendo clic en el botón de proceso **Corrección Manual del Coste**. Tras hacer clic en este botón, se abre un nuevo popup:

![Popup de Corrección Manual del Coste](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-21.png)

Este pop-up permite introducir los siguientes datos detallados:

- **Importe de coste total**: es el nuevo coste total de la transacción de producto
- **Fecha contable**: es la fecha en la que este cambio manual, que implicará un ajuste de coste, se contabilizará en el libro mayor
- **Incremental**:
  - si no está marcado, el importe introducido en el campo de importe de coste total es el nuevo coste total de la transacción que, además, se establecerá como un coste *Permanente* que ya no podrá ajustarse.
  - si está marcado, el importe introducido en el campo de importe de coste total se añadirá al coste total actual; además, se muestra la casilla **Coste Unitario**.
- **Coste Unitario**: esta casilla solo se muestra si se selecciona la casilla **Incremental**.
  - si no está marcada, el importe incremental introducido en el campo de importe de coste total no se considerará parte del coste unitario de la transacción, sino del coste total. Esto es como introducir un coste *extra* como *Landed Cost*, que no cambia el coste unitario de esa transacción, pero sí el coste total.
  - si está marcada, el importe incremental introducido en el campo de importe de coste total se considerará parte del coste unitario de la transacción.

Para información adicional sobre qué ajuste de coste es, o no es, coste unitario, revise la sección Ajustes de coste - Descripción general.

Una vez hecho, se creará un ajuste de coste de *corrección manual de coste*.

Este ajuste de coste puede revisarse y contabilizarse en el libro mayor en la ventana **Ajuste de coste**.

Del mismo modo, este ajuste de coste también puede revisarse en la solapa **Costes Transacción**.

#### Costes Transacción { #transaction-costs }

Los registros de **Costes Transacción** se crean automáticamente mediante el **Proceso en segundo plano de cálculo de costes** y luego se listan para el producto en esta solapa.

En cuanto una transacción de producto tiene su coste calculado, se crea un nuevo registro en esta solapa.

En cuanto una transacción de producto tiene su coste ajustado, se crea un nuevo registro en esta solapa haciendo referencia a una **Línea de Ajuste de Coste**.


Algunos campos relevantes a tener en cuenta son:

- **Fecha de coste**: es la fecha en la que el coste ha sido calculado (p. ej., la fecha contable de un albarán de proveedor)
- **Costo**: es el coste total calculado por el **Proceso en segundo plano de cálculo de costes**
- **Moneda**: es la moneda utilizada para calcular el coste.  
  La moneda del coste es la moneda de la entidad legal; por lo tanto, una transacción de producto que tenga una moneda diferente (una tarifa en moneda USD, por ejemplo) tendrá su coste calculado en la moneda heredada (p. ej., EUR)
- **Línea de Ajuste de Coste**: si un coste calculado proviene de un ajuste de coste, este campo rellena la línea de ajuste de coste que provoca ese coste.  
  En última instancia, el coste total de una transacción de producto es la suma de todos los costes listados en esta solapa, tanto los originales como los ajustados, que pueden formar parte del coste unitario o no (p. ej., landed costs).
- **Coste Unitario**: este campo detalla si el coste calculado forma parte del coste unitario del producto o no.
- **Fecha contable**: es la fecha contable en la que el coste ha sido calculado y contabilizado en el libro mayor (p. ej., la fecha contable de un albarán de proveedor contabilizado en el libro mayor)

### Compras { #purchasing }

La solapa **Compras** almacena datos de proveedor y planificación para los productos gestionados a través del Plan de Compras. Complete esta solapa cuando desee que Etendo sugiera o cree automáticamente Pedidos de compra para este producto.

Además, el proceso de solicitud utiliza la información de **Terceros** para la creación automática de **Pedidos de compra**.

![Solapa Compras de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-23.png)

- **Terceros**, el proveedor que aparecerá en el **Pedido de compra** cuando se cree automáticamente desde la solicitud o desde el plan de compras.
- **Valoración calidad**: valoración de calidad del proveedor. Campo solo informativo que no es utilizado por el proceso MRP.
- **Casilla Proveedor actual**: indicación del proveedor por defecto que será tenido en cuenta por el proceso MRP.
- **UPC/EAN**: Universal Product Code/European Article Number (código de barras) del producto tal y como lo utiliza el proveedor seleccionado. Solo informativo; esta información no aparece en un **Pedido de compra** creado.
- **Moneda**: moneda del pedido de compra.
- **Precio tarifa**: campo solo informativo del precio neto de tarifa que debe actualizarse manualmente en el **Pedido de compra** creado automáticamente desde el plan de compras.
- **Precio vigente desde**: la fecha a partir de la cual los precios introducidos son válidos. Solo informativo; no se utiliza en el proceso MRP.
- **Precio de compra**: campo solo informativo del **Precio unitario** que debe actualizarse manualmente en el **Pedido de compra** creado automáticamente desde el plan de compras.
- **Último precio de pedido de compra**: el **Precio unitario** del **Pedido de compra** añadido más recientemente.
- **Pr. última factura**: el **Precio unitario** de la **Factura (Proveedor)** añadida más recientemente.
- **Unidad**: la unidad de medida del producto.
- **Cantidad mínima de pedido**: una cantidad mínima de pedido para el proveedor. En el plan de compras, la cantidad de los pedidos de compra sugeridos será este valor o superior.
- **Cant. paquetes pedido**: campo solo informativo sobre el empaquetado del producto. Esta información no se tiene en cuenta para la creación de la información en el plan de compras ni para la creación de **Pedidos de compra**.
- **Tiempo de entrega esperado**: tiempo en días naturales entre el momento en que el producto se pide al proveedor y el momento en que se recibe en stock. En el plan de compras, esta información se utiliza para calcular cuándo deben realizarse los pedidos de compra, dando como resultado la fecha de pedido planificada para el pedido de compra sugerido.
- **Costo por pedido**: campo solo informativo de un importe fijo que debe añadirse manualmente al **Pedido de compra** creado automáticamente desde el plan de compras.
- **Nº de producto del proveedor**: la referencia del proveedor para el producto.
- **Categoría proveedor**: campo solo informativo para añadir información de la categoría del proveedor.
- **Descatalogado**: campo solo informativo para indicar que este producto ya no se utiliza. El plan de compras no tiene en cuenta esta configuración al generar el plan ni al crear **Pedidos de compra**. Al seleccionarlo, aparece el campo **Descatalogado por fecha** para indicar cuándo se descataloga el producto. Solo con fines informativos.
- **Tipo Cantidad**:
    - **Exacto**: cada pedido de compra sugerido es por la cantidad exacta requerida. Por ejemplo, si la demanda es de 85 unidades, la cantidad del pedido de compra sugerido es 85 unidades.
    - **Múltiple**: la cantidad que aparece como cantidad del pedido de compra sugerido es un múltiplo de la cantidad estándar (tal y como se define en esta pantalla). Por ejemplo, si la cantidad estándar es 20 unidades y la demanda es de 85 unidades, la cantidad del pedido de compra sugerido es 100.
- **Fabricante**: campo solo informativo para indicar el fabricante del producto.
- **Cantidad Std.**: cantidad que se tiene en cuenta en combinación con el **Tipo Cantidad** para el valor de cantidad del pedido de compra sugerido.
- **Capacidad**: cantidad por día que el proveedor puede suministrar. En base a este campo y al tiempo de entrega, se calcula la fecha del pedido de compra. El número de días se calcula como el valor máximo entre el tiempo de entrega y la cantidad requerida / capacidad.

### Producción { #manufacturing }

La solapa Producción se utiliza para productos que se planifican mediante el plan de producción.

La información de esta solapa es utilizada principalmente por el MRP para procesar el Plan de Producción y el Plan de Compras. El campo Hueco se completa para los productos en producción para indicar el hueco por defecto en el que se almacenará el producto cuando salga de producción.

- **Hueco**: ubicación por defecto del producto en el almacén.
- **Método de planificación**: definición de los elementos de suministro y demanda que se tienen en cuenta y con qué porcentaje para la creación del Plan de Producción y del Plan de Compras. Para más detalles, consulte la sección [Método de planificación](../../material-requirement-planning/setup.md#planning-method).
- **Planificador**: la persona responsable de la ejecución del plan de MRP del producto. Para más detalles, consulte la sección [Planificador](../../material-requirement-planning/setup.md#planner).
- **Capacidad**: capacidad de producción por día para el producto.
- **Cantidad desde:** cantidad mínima que debe introducirse en un requerimiento de trabajo.
- **Tipo Cantidad**:
    - **Exacto**: cada requerimiento de trabajo sugerido es para la cantidad estándar (según se define en esta pantalla). Aparecen múltiples requerimientos de trabajo sugeridos para cubrir la demanda total. Por ejemplo, si la cantidad estándar es de 20 unidades y la demanda es de 85 unidades, aparecen 5 líneas de requerimientos de trabajo sugeridos con cantidad 20.
    - **Múltiple**: la cantidad que aparece como cantidad del requerimiento de trabajo sugerido es un múltiplo de la cantidad estándar (según se define en esta pantalla). Por ejemplo, si la cantidad estándar es de 20 unidades y la demanda es de 85 unidades, la cantidad del requerimiento de trabajo sugerido es 100.
- **Cantidad Std.**: cantidad que se tiene en cuenta en combinación con el Tipo Cantidad para el valor de cantidad del requerimiento de trabajo sugerido.
- **Retraso Mínimo**: plazo de fabricación del producto.
- **Stock Mín.**: el nivel mínimo de stock que siempre debe existir en el almacén. Por ejemplo, si existe un stock mínimo de 1000 unidades y el stock es de 900 unidades, se sugiere un requerimiento de trabajo (Plan de Producción) o un pedido de compra (Plan de Compras) por 100 unidades. Normalmente, los productos de bajo coste o los productos con un plazo de entrega muy largo se configuran con un nivel de stock mínimo.
- **Máximo stock no reservado**: stock máximo sin tener en cuenta el stock pre-reservado. Este campo solo es visible cuando la funcionalidad de reserva de stock está habilitada. Consulte el siguiente ejemplo para entender cómo funciona:

1.  _Stock Mín._ y _Máximo stock no reservado_ son 200 y 1000 unidades, respectivamente
2.  Existen varios pedidos de venta que deben entregarse por un total de 3000 unidades
3.  Estos pedidos de venta generarán los pedidos de compra correspondientes (pre-reservados) al lanzar el MRP
4.  Actualmente hay 80 unidades en stock
5.  Cuando se lanza el MRP, creará los correspondientes pre-reservados y, al estar por debajo del stock mínimo, creará otro pedido de compra:
    1.  Como el _Máximo stock no reservado_ está definido, el sistema creará un pedido de compra de 920 unidades (1000-80)
    2.  Si este parámetro no estuviera definido, funcionaría como de costumbre y crearía un pedido de compra de 120 unidades (200-80)

- **ABC**: valor utilizado en la gestión de almacén para indicar una combinación del nivel de stock y el coste de una pieza. El valor se calcula ejecutando el Informe de Producto Pareto.

### Traducción { #translation }

Los nombres de los productos se pueden traducir a cualquier idioma.

La forma de hacerlo es tan sencilla como:

- seleccionar primero el idioma requerido
- y luego introducir el nombre del producto traducido a ese idioma.

### Características { #characteristics }

Relación de características asignadas al **Producto**.

Campos:

- **Secuencia**: Orden de las características
- **Característica**: Lista todas las características definidas en la ventana **Característica de producto**
- **Variante**: Cuando está marcada, explotará/creará combinaciones con sus valores. Si no está marcada, no creará combinaciones con otras características. Por ejemplo:
  - Característica Color: Variante marcada con valor *Azul* y *Blanco*
  - Característica Talla: Variante marcada con valor *M* y *L*
  - Característica Línea de moda: Variante no marcada con valor *Sport*
  - Creará cuatro variantes/productos y en todos ellos con la característica *Sport*
- **Explotar Solapa de Configuración**: Indicador disponible en Productos genéricos y Características de variante. Cuando está marcado, los valores de la característica de variante seleccionada se insertan automáticamente en la solapa **Configuración de características**. Si no está marcado, los valores deben añadirse manualmente.
- **Define precio**: Cada valor de esa característica definirá el precio del nuevo producto. Sobrescribirá el precio definido para el producto genérico. Este precio se define en la solapa **Configuración de características**.
- **Tipo de tarifa**: Se muestra cuando **Define precio** está marcado. Permite al usuario seleccionar en qué tipo de tarifa desea sobrescribir el precio. Por ejemplo:
  - El producto genérico tiene dos tarifas: una es para ventas y la otra para compra
  - Usted selecciona el valor *Tarifas de venta*. Entonces, al crear las variantes de producto, solo sobrescribirá el precio en las tarifas definidas como Ventas
  - Lo contrario si el valor seleccionado es *Tarifa de compra*
- **Define imagen**: Cada valor de esa característica definirá la imagen del nuevo producto. Sobrescribirá la imagen del producto genérico. Esta imagen se define en la solapa **Configuración de características**.
- **Subconjunto de característica**: Lista todos los subconjuntos incluidos para la Característica seleccionada (p. ej., *Pantalones*)

Una vez guardado el registro, todos los valores de la característica se rellenan en la solapa **Configuración de características**.

**Configuración de características**

La solapa Configuración de características contiene los valores disponibles para cada característica asignada al producto genérico. En esta solapa también se definen los modificadores de precio para crear las variantes.

Campos a tener en cuenta:

- **Valor de característica**: No puede ser editable, ya que se rellena automáticamente al seleccionar la característica
- **Código**: Código del valor. Hereda lo que se ha definido en la ventana de característica de producto
- **Pr. estándar**: Este campo se muestra cuando la característica está marcada como **Define precio**. El objetivo de este campo es disponer de precios diferentes por valor. Por ejemplo, en función de las tallas
- **Imagen**: Este campo se muestra cuando la característica está marcada como **Define imagen**. El objetivo de este campo es disponer de imágenes diferentes por valor. Por ejemplo, en función del color.

### Stock { #stock }

Esta solapa muestra el Stock disponible para este Producto en la Aplicación. Solo muestra los Huecos para los que la cantidad disponible del Producto no es 0.

Para cada hueco no vacío, también muestra información sobre:

- la cantidad reservada
- y la cantidad asignada

### Coste Unitario { #unit-cost }

La solapa **Coste Unitario** muestra información sobre el *Coste Unitario* real del producto.

El *Coste Unitario* de un Producto es el valor de cada unidad almacenada del producto, independientemente del algoritmo de cálculo de costes utilizado para calcular el coste de ese producto.

Este coste se calcula utilizando el *Stock Total* de un producto y el *Valor Total* del stock del producto, según la fórmula siguiente:

- Coste Unitario = Valor total del stock / Stock Total

De este modo, el coste unitario calculado es independiente del *Algoritmo de cálculo de costes* utilizado para calcular el coste de cada transacción y producto; por lo tanto, este coste unitario es compatible con todos los *Algoritmos de cálculo de costes* (Promedio, Estándar, FIFO, ...)

En esta solapa, va a existir un registro para:

- cada Organización que sea una Entidad Legal y que tenga definida una Regla de cálculo de costes
- o para cada Organización y Almacén, siempre que la Dimensión de Almacén esté definida como una dimensión de coste de la Regla de cálculo de costes actual definida para la *Entidad Legal*.


### Categorías de Productos { #product-categories }

El usuario puede definir si un producto de una determinada categoría de producto puede relacionarse con un producto de tipo *Servicios* creando una relación entre una Línea de pedido del producto de Servicios y otra Línea de Pedido de venta del producto perteneciente a las categorías de producto incluidas/excluidas.

Esta solapa solo estará disponible cuando el campo **Categorías de producto incluidas** del Servicio tenga un valor. Contiene todas las categorías de producto relacionadas con el servicio.

![Solapa Categorías de Productos de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-25.png)

En la solapa está disponible la siguiente información sobre los productos relacionados:

- **Identificador**: Identificador de la Categoría del producto.
- **Nombre**: Nombre de la Categoría del producto.
- **Descripción**: Descripción de la Categoría del producto.

Esta solapa no es editable; no es posible añadir registros manualmente ni editarlos. Solo permite eliminar registros. Para añadir nuevos registros, es necesario hacer clic en el botón **Relacionar categorías de producto** (visible solo cuando el campo **Categorías de producto incluidas** tiene un valor). Este botón abrirá un Pick & Edit mostrando todas las categorías de producto no relacionadas con el servicio.

![Ventana Pick and Edit de Relacionar categorías de producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-26.png)

### Versión de Regla de Precio de Categoría { #category-price-rule-version }

Esta solapa solo estará disponible cuando el campo **Is Price Rule Based** esté seleccionado. Permite definir versiones de regla de precio que se aplican cuando el servicio está vinculado a productos pertenecientes a categorías de producto específicas.

### Productos { #products }

El usuario puede definir si un producto puede relacionarse con un producto de tipo *Servicios* creando una relación entre una Línea de pedido del producto de Servicios y otra Línea de Pedido de venta del producto incluido/excluido.

Esta solapa solo estará disponible cuando el campo **Productos incluidos** del Servicio tenga un valor. Contiene todos los productos relacionados con el servicio.

![Solapa Productos de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-27.png)

En la solapa está disponible la siguiente información sobre los productos relacionados:

- **Identificador**: Identificador del Producto.
- **Nombre**: Nombre del Producto.
- **Marca**: Identificador de la Marca del Producto.
- **Categoría del producto**: Categoría del producto a la que pertenece el producto.
- **Producto genérico**: Producto genérico del Producto, si tiene.
- **Descripción de característica**: Características del Producto, si tiene.

Esta solapa no es editable; no es posible añadir registros manualmente ni editarlos. Solo permite eliminar registros. Para añadir nuevos registros, es necesario hacer clic en el botón **Relacionar productos** (visible solo cuando el campo **Productos incluidos** tiene un valor). Este botón abrirá un Pick & Edit mostrando todos los productos no relacionados con el servicio.


#### Versión de Regla de Precio de Producto { #product-price-rule-version }

Esta solapa solo estará disponible cuando el campo **Is Price Rule Based** esté seleccionado. Permite definir versiones de regla de precio que se aplican cuando el servicio está vinculado a productos individuales específicos.

### UOM Alternativa { #alternate-uom }

!!! info
    Para habilitar esta solapa, vaya a `Configuración General` > `Aplicación` > `Preferencias`, cree una nueva preferencia con la propiedad **Habilitar la gestión de UOM** y establezca su valor en Y. Si no dispone de acceso, contacte con su administrador del sistema.

![Solapa Unidad Alternativa de la ventana Producto](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/product/product-29.png)

Campos a tener en cuenta:

- **Unidad**, es la unidad de medida alternativa del producto, por ejemplo *Palet*. Es importante remarcar que cualquier unidad de medida debe crearse y configurarse en la ventana [Unidad de medida](../product-setup/unit-of-measure.md).
- **Ratio de conversión**, es la conversión entre la unidad de medida alternativa del producto (AUM) y la unidad de medida del producto. Por ejemplo, si la conversión de la AUM del producto a la UOM del producto es 50, significa que 1 Palet representa 50 Unidades.
- **Gtin**, es el *Global Trade Item Number* del producto definido en la AUM correspondiente.
- **Ventas**, **Compra** y **Logística**, estos campos permiten definir el uso de la AUM del producto dentro de los flujos de Ventas, Compra e Inventario.  
  Los valores permitidos son:
  
    - **Primario**: la AUM del producto definida en esta solapa se utiliza como unidad de medida por defecto en el flujo seleccionado (Ventas o Compra), al crear un documento de venta o compra como un pedido o un albarán/recepción.  
    Solo se puede definir una AUM Primaria por Producto y flujo.  
    Por ejemplo, si *Palet* es la AUM primaria definida para un producto dentro del flujo de Compra, significa que cada vez que se cree un documento de compra, *Palet* será la unidad de medida por defecto que se mostrará.
    - **Secundario**: la AUM del producto definida en esta solapa se puede seleccionar para el flujo seleccionado al crear un Documento.  
    Por ejemplo, si *Palet* es la AUM secundaria definida para un producto dentro del flujo de Ventas, mientras que *Paquete* es la primaria, significa que cada vez que se cree un documento de venta, *Paquete* será la unidad de medida por defecto que se mostrará, pero el usuario final puede cambiarla a *Palet*.
    - **No aplicable**: la AUM definida en esta solapa para el producto no estará disponible para su selección al crear Documentos para el flujo seleccionado.  
    Esta es la opción a seleccionar para **Logística**, ya que el uso de unidades de medida alternativas actualmente está implementado solo para ventas y compras. Las transacciones/documentos de inventario siempre hacen referencia a la unidad de medida del producto.

#### Modificar Categorías de Impuestos { #modify-taxes-categories }

Define la modificación de impuestos para productos vinculados a servicios. Los productos vinculados a este servicio que pertenezcan a la categoría configurada cambiarán la categoría de impuesto cuando se vinculen a este servicio.

### Stock por unidad logística { #stock-by-logistic-unit }


!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo **Unidad logística de stock**, parte de Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Permite visualizar el stock por unidades logísticas (inventario referenciado) de una forma más clara y organizada.

!!! info
    Para más información, visite [Unidad logística de stock](../../../optional-features/bundles/warehouse-extensions/stock-logistic-unit.md#product-stock-by-logistic-unit).

*[AUM]: Unidad de Medida Alternativa
*[BOM]: Lista de Materiales
*[COGS]: Coste de los Bienes Vendidos
*[EAN]: Número de Artículo Europeo
*[FIFO]: Primero en Entrar, Primero en Salir
*[GTIN]: Número Global de Artículo Comercial
*[MRP]: Planificación de Necesidades de Material
*[UOM]: Unidad de Medida
*[UPC]: Código Universal de Producto
*[VAT]: Impuesto sobre el Valor Añadido

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
