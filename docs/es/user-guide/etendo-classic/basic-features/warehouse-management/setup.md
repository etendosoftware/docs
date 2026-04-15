---
title: Configuración de Gestión de Almacén
---
## Visión general

Esta sección describe los pasos que deben realizarse para configurar las secciones de gestión de almacén en Etendo. Las ventanas correspondientes son:

[:material-file-document-outline:Procesar Ajuste de Diferencias de Precio](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#process-price-difference-adjustment){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Almacén y huecos](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#warehouse-and-storage-bins){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Transportista](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#shipping-company){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Categoría portes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#freight-category){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Reglas de cálculo de costes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#costing-rules){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Algoritmo de cálculo de costes](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#costing-algorithm){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Tipo de Landed Cost](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#landed-cost-type){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Reglas de almacén](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#warehouse-rules){ .md-button .md-button--primary } <br>

[:material-file-document-outline:Tipo de Inventario Referenciado](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#referenced-inventory-type){ .md-button .md-button--primary } <br>

[:material-file-document-outline:Tipo EAN 128](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#ean-128-type){ .md-button .md-button--primary } <br>
## Procesar Ajuste de Diferencias de Precio

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Procesar Ajuste de Diferencias de Precio`

Los ajustes de diferencias de precio se pueden realizar de forma "automática" programando el "Proceso en segundo plano de corrección de precios" o manualmente para un producto determinado o un conjunto de productos ejecutando este proceso.
## Almacén y huecos

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Almacén y huecos`

### Visión general

El usuario puede crear almacenes y organizarlos mediante huecos.

**Almacén** representa la ubicación física del stock en la aplicación, y se divide en **Hueco** para definir una ubicación más exacta de los bienes dentro del almacén.

Esta ventana permite al usuario crear y configurar almacenes y obtener información sobre los bienes disponibles en el almacén, así como información relacionada con las transacciones.

### Almacén

El usuario puede crear almacenes para sus organizaciones.

Es importante tener una visión general previa antes de crear almacenes. La solapa **Almacén** contiene los detalles esenciales del almacén; los más relevantes son **Nombre** y **Dirección**.

![Warehouse](../../../../assets/drive/1vxTgfKhjgIIhpZbIFp7FC8y1X9mJOcrE.png)

Campos a tener en cuenta:

-   **Identificador:** es importante definir un identificador adecuado para los almacenes, de modo que puedan identificarse fácilmente más adelante desde otras ventanas e informes.
-   **Hueco de devoluciones:** valor por defecto para el campo **Hueco** de las líneas de recibo de devolución de material, al que se colocan los productos devueltos por el cliente.
-   **Regla de almacén:** definición de una regla de almacén que se aplicará al obtener stock del almacén.

### Hueco

El usuario puede crear huecos para un almacén seleccionado.

Define la posición del **Hueco** en el almacén: los campos **Estantería (X)**, **Columna (Y)** y **Altura (Z)**, y otros parámetros.

![Storage Bin](../../../../assets/drive/1AN5LR3kYTm3OhGshk_DUgJD75I1S5AxT.png)

Otros campos a tener en cuenta:

-   **Prioridad relativa:** en términos de recuperación y retirada de stock. La secuencia normal de salida de productos del almacén es **primero en entrar, primero en salir** (FIFO), pero en este campo se indica una prioridad relacionada con los huecos que contienen el mismo producto (0 = prioridad más alta). El campo lo utilizan procesos automáticos que necesitan determinar qué hueco usar, por ejemplo, Crear envíos desde pedidos. También define la ordenación de los huecos en el selector de localizador (Hueco).
-   **Valor por defecto:** cuando se selecciona, este hueco aparece por defecto en los documentos.
-   **Código de barras:** no hay lógica detrás de este campo. Se ha creado para ser utilizado/implementado por otros módulos como **Etendo Mobile Application**.
-   **Estado de Inventario:** es el Estado de Inventario actual del Hueco seleccionado. Puede cambiarse haciendo clic en el botón *Cambiar estado*.  
Para más información, visite [Estado de Inventario](../../../../developer-guide/etendo-classic/concepts/inventory-status.md).

### Operaciones de producto

El usuario puede ver todas las operaciones de producto relacionadas con el almacén seleccionado y el historial de transacciones (recepción de materiales, envío, uso en producción, etc.) que influyen en el hueco seleccionado.

El contenido de esta solapa es el mismo que el de la ventana de transacciones de mercancías.

### Inventario

El usuario puede ver los productos almacenados de un hueco seleccionado.

La solapa de solo lectura **Inventario** lista los productos almacenados en un hueco concreto.

![Bin Contents](../../../../assets/drive/1g3JvIz3nAMp_BxJLc13QyIFIRRRLfG_x.png)

Campos a tener en cuenta:

-   **Valor atributos:** este campo se muestra si el producto de la línea tiene atributos (color, talla, número de serie o varios de ellos a la vez, etc.).
-   **F.último inventario**: la última fecha en la que este producto se comprobó durante el proceso de recuento de inventario físico.
-   **Cantidad disponible:** stock actual del producto.
-   **Cant. en curso:** cantidad de producto que está en transacciones de almacén (como recepción de mercancías, envío de mercancías, inventario físico, movimientos de mercancías) en estado Borrador.

### Contabilidad

El usuario puede crear y editar cuentas de mayor (G/L) que se utilizarán en transacciones que incluyan un almacén seleccionado.

Esta solapa especifica la cuenta de diferencias de almacén para la configuración del libro mayor de cada organización.

Se completa automáticamente cuando se crea un nuevo almacén, ya que se toma de la cuenta correspondiente de la solapa Valor por defecto de la configuración del libro mayor correspondiente.
## Transportista

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Transportista`

El usuario puede crear transportistas y definir costes de portes que se utilizarán en la logística de productos.

También se pueden crear transportistas para ser utilizados en otras transacciones de la aplicación.

### Porte

El usuario puede definir portes que se utilizarán para un transportista especificado.
## Categoría portes

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Categoría portes`

El usuario puede definir y crear categorías de portes para que sean utilizadas por los transportistas.

## Reglas de cálculo de costes

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Reglas de cálculo de costes`

### Visión general

Una regla de cálculo de costes se puede aplicar durante el cálculo de costes. Cada regla de cálculo de costes requiere un algoritmo de cálculo de costes y una fecha válida desde para calcular correctamente el coste de las operaciones de material. El "Almacén" se puede configurar como una dimensión que se tendrá en cuenta al calcular los costes.

Las reglas de cálculo de costes solo se pueden crear para entidades legales, es decir, organizaciones "legal con contabilidad" u organizaciones "legal sin contabilidad".

Los costes de las operaciones de producto se pueden calcular para ambos tipos de entidades legales; sin embargo, solo las organizaciones "legal con contabilidad" admiten la contabilización de inventario "perpetua", ya que las organizaciones "legal sin contabilidad" no admiten ningún tipo de contabilización.

!!! note
    Una regla de cálculo de costes se puede validar si hay una "Moneda" configurada para la entidad legal en la ventana de organización; por lo tanto, los costes se calculan en esa moneda.

Una regla de cálculo de costes válida, una vez creada y validada para una organización de entidad legal, se asignará automáticamente a los productos de esa organización; por lo tanto, se puede revisar en la solapa Regla de cálculo de costes de la ventana "Producto".

Las reglas de cálculo de costes permiten al usuario definir si las transacciones retroactivas registradas para productos en una fecha posterior deben ajustarse; por lo tanto, también se crean y contabilizan los ajustes de coste de la "transacción retroactiva" correspondiente para obtener el coste correcto de esos productos.

!!! warning
    "Reglas de cálculo de costes" es una funcionalidad implementada por el nuevo Motor de Costes; por lo tanto, una regla de cálculo de costes se puede crear y validar dentro de una instancia de Etendo que gestione costes solo si se ha migrado al nuevo "Motor de Costes".

Etendo recomienda migrar las instancias que utilizan el motor de costes "heredado" al nuevo motor de costes.

Para crear y validar una "Regla de cálculo de costes", el usuario debe tener en cuenta que:

-   La primera regla de cálculo de costes creada no permite introducir ninguna fecha en el campo "Fecha de inicio", lo que significa que se calculará el coste de todas las operaciones de producto existentes.
    -   Una fecha en blanco en el campo "Fecha de inicio" implica también una fecha en blanco en el campo "Ajuste Retroactivo de Transacciones Desde", a menos que se introduzca una fecha diferente en este campo. La fecha "Ajuste Retroactivo de Transacciones Desde" puede ser igual o posterior a la "Fecha de inicio".
    -   Etendo mostrará un error en caso de que existan operaciones de producto cuyos costes deban calcularse con una fecha de movimiento en un periodo "Cerrado". En esos casos, no será posible contabilizar ninguna transacción de coste en el libro mayor a menos que el periodo correspondiente esté abierto para entidades legales con contabilidad.
-   La primera regla de cálculo de costes creada también permite especificar una fecha en el campo "Fecha de inicio", p. ej. 01-01-2022:
    -   En ese caso, todas las transacciones con una fecha de proceso de transacción anterior a esa fecha también se calcularán a coste cero.
    -   Todas las transacciones con una fecha de proceso de transacción el 1 de enero de 2022 y posteriores se calcularán al coste correspondiente.
-   La segunda regla de cálculo de costes no permite introducir una "Fecha de inicio", ya que se toma la fecha "actual" por defecto; por lo tanto, la primera regla de cálculo de costes finaliza cuando comienza la segunda, y así sucesivamente.
    -   Lo mismo aplica a la fecha "Ajuste Retroactivo de Transacciones Desde", que por defecto toma la fecha actual, a menos que se introduzca una fecha específica posterior a la fecha "actual".

#### **Regla de cálculo de costes**

La ventana de regla de cálculo de costes permite al usuario definir y validar reglas de cálculo de costes.

![Regla de cálculo de costes](../../../../assets/drive/1MxTiOhHzaaxhZQlKOMkF9jA6DKEbD-b5.png)

Tal y como se muestra en la imagen anterior, se puede definir una "Regla de cálculo de costes" y asignarla a una organización para la cual sea necesario calcular el coste de las transacciones.

Solo puede haber una regla válida a la vez para una organización, que además debe ser de tipo organización "Entidad Legal". El periodo de validez de la regla de cálculo de costes se establece mediante la "Fecha de inicio" introducida.

!!! note
    Una vez asignada, la regla de cálculo de costes se aplica a cada operación de producto registrada en la *Entidad Legal* y en todas sus organizaciones hijas.

La propiedad principal que se debe establecer en una regla de cálculo de costes es el Algoritmo de cálculo de costes que se utilizará al calcular los costes.

Los algoritmos Estándar y Promedio están disponibles por defecto. Algoritmos adicionales como FIFO, LIFO se pueden implementar mediante módulos de extensión.

Además, los costes se calculan a nivel de organización por defecto; sin embargo, también es posible que los costes se calculen para cada organización de Almacén.

Esto se puede lograr utilizando el indicador de Dimensión de Almacén de la regla de cálculo de costes.

Las reglas de cálculo de costes deben validarse para empezar a utilizarlas. Esto se realiza mediante el botón "Process_Rule".

!!! warning
    Una vez que una Regla de cálculo de costes se valida, no es posible modificarla ni eliminarla.

Si es necesario cambiar una regla de cálculo de costes, el usuario debe crear una nueva regla de cálculo de costes con la nueva configuración requerida.

Imaginemos que una organización requiere un nuevo algoritmo de cálculo de costes para el cálculo de costes. En ese caso, es necesario crear una nueva regla de cálculo de costes.

La nueva regla sobrescribe la existente, a partir de una nueva "Fecha de inicio" posterior.

En este caso:

-   es necesario cerrar la regla de cálculo de costes existente; esto significa cerrar el inventario valorado con la regla "antigua"
-   y realizar la inicialización del inventario que se valorará con la regla de cálculo de costes "nueva" a partir de una fecha determinada

Los saldos de inventario de **cierre** e **inicialización** se gestionan como inventarios físicos en el nuevo motor de costes.

Se crean dos inventarios físicos para cada organización y almacén a los que se aplica la regla de cálculo de costes:

-   el inventario físico de **cierre** vacía el stock de productos; por lo tanto, el recuento de cantidad se establece en 0.  
    El coste de los productos es el calculado utilizando la regla de cálculo de costes configurada hasta ese momento, aunque no se muestre en el inventario físico.
-   El inventario de **apertura** vuelve a rellenar el stock; por lo tanto, el recuento de cantidad se vuelve a establecer en la cantidad disponible.  
    El coste de los productos se muestra y es el calculado utilizando la regla de cálculo de costes configurada hasta ese momento.  
    Tenga en cuenta que el coste de las nuevas transacciones de esos productos se calculará utilizando la nueva regla de cálculo de costes.

El proceso de **validación de la regla de cálculo de costes** realiza varias comprobaciones:

-   las instancias que gestionan costes y que no se han migrado al nuevo motor de costes no podrán validar reglas de cálculo de costes
-   las instancias que no gestionan costes no necesitan migrar; por lo tanto, podrán crear y validar reglas de cálculo de costes
-   y, por último, para instancias que ya gestionan costes bajo la infraestructura del nuevo motor de costes:
    -   en el caso de productos incluidos en transacciones cuyo coste se calculó utilizando una regla, si se configura una nueva regla, primero es necesario calcular todas sus transacciones de acuerdo con esa regla anterior.
    -   en el caso de productos incluidos en transacciones cuyo coste no se calculó mediante ninguna regla, si se configura una nueva regla, no se debe calcular el coste de ninguna de sus transacciones.

##### **Ajuste Retroactivo de Transacciones**

Tal y como ya se ha descrito, una regla de cálculo de costes también puede definir si las transacciones retroactivas registradas para un producto deben ajustarse; por lo tanto, se crean y contabilizan los ajustes de coste de la transacción retroactiva correspondiente para ese producto con el fin de obtener el coste correcto del producto.

Para que esto funcione, se puede realizar una de las dos acciones siguientes:

1.  utilizar una Regla de cálculo de costes existente y validada.  
    De este modo, la funcionalidad de ajuste retroactivo de transacciones se activa utilizando el botón de proceso "Ajuste Retroactivo de Transacciones".  
    Esta opción permite introducir una fecha "Ajuste Retroactivo de Transacciones Desde" como fecha de inicio, antes de ejecutar el proceso.

![Ajuste Retroactivo de Transacciones](../../../../assets/drive/1dSn2VWGuwWybweNlYEgdtUImlXA8UihG.png)
 

2\. crear y validar una nueva Regla de cálculo de costes.  
De este modo, la funcionalidad de ajuste retroactivo de transacciones se activa marcando la casilla de verificación de transacciones retroactivas ajustadas y completando una fecha Ajuste Retroactivo de Transacciones Desde antes de validar la regla de cálculo de costes.

En ambos casos:

-   la "Fecha de inicio" de la regla de cálculo de costes se establecerá como la fecha "Ajuste Retroactivo de Transacciones Desde" siempre que el usuario final no introduzca una fecha "Ajuste Retroactivo de Transacciones Desde".
-   la fecha "Ajuste Retroactivo de Transacciones Desde" debe ser una fecha válida dentro de un periodo abierto.

#### **Inicialización**

La solapa Inicialización es una solapa de solo lectura que permite revisar el inventario físico de "Cierre" / "Apertura" creado para validar una regla de cálculo de costes. Cada vez que se valida una regla de cálculo de costes, se crea un nuevo registro para cada Organización y Almacén. Este registro contiene enlaces a los inventarios físicos creados.
## Algoritmo de cálculo de costes

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Algoritmo de cálculo de costes`

### Visión general

Un algoritmo de cálculo de costes define el método que se va a utilizar para calcular el coste de las transacciones.

Etendo entrega los algoritmos de cálculo de costes Estándar y Promedio como parte del nuevo Motor de cálculo de costes.

Cada algoritmo de cálculo de costes debe contener e implementar todo lo necesario para calcular los costes y almacenarlos.

### Cabecera 

La principal característica de un algoritmo de cálculo de costes es la clase Java que incluye todo lo necesario para implementarlo.

Los algoritmos de cálculo de costes deben cargarse mediante un conjunto de datos de "Sistema", por lo que pueden estar disponibles para cada Entidad de la instancia de Etendo.

Los algoritmos de cálculo de costes pueden listarse en esta ventana una vez que se haya aplicado el conjunto de datos de sistema correspondiente.

Se recomienda aplicar este tipo de conjuntos de datos de sistema a la organización (\*) para que estén disponibles para cada organización de la Entidad.

Si no se muestra ningún registro en esta ventana, póngase en contacto con su "Administrador del sistema" para asegurarse de que los conjuntos de datos de "Sistema" se han aplicado correctamente utilizando el siguiente comando de "ant": *ant apply.module -DforceRefData=true*
## Tipo de Landed Cost

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Tipo de Landed Cost`

### Visión general

La ventana Tipo de Landed Cost permite al usuario definir diferentes tipos de Landed Cost que pueden asignarse a las recepciones de mercancía y, por tanto, distribuirse a los productos incluidos en las recepciones.

El Landed Cost es el coste total de un envío recibido, incluyendo el precio de compra, el porte, el seguro, los aranceles aduaneros y otros costes hasta el puerto de destino.

Etendo gestiona los landed costs no como parte del "coste unitario" de un producto, sino como parte de su coste total.

### Cabecera

Los Tipos de Landed Cost pueden definirse como un "Producto" o como una "Cuenta" (apunte de mayor / elemento de G/L). Además, puede definirse un algoritmo de distribución para configurar la forma en que los landed costs se van a distribuir a los productos.

Algunos campos a tener en cuenta son:

-   **Nombre**: es el nombre del tipo de landed cost, por ejemplo "Seguro", "Porte", "Aranceles" o "Impuestos".
-   **Algoritmo de Distribución de Landed Cost**: es el algoritmo que se utilizará para distribuir o asignar los Landed Costs entre todas las Líneas de la recepción relacionadas con esos landed costs.

Etendo proporciona un "Algoritmo de Distribución de Landed Cost" que es "Distribución por importe" como parte de la funcionalidad de ajuste de costes.

Este algoritmo distribuye los landed costs a las líneas de recepción de forma proporcional al importe de la línea de recepción.

La característica principal de un algoritmo de distribución de landed cost es la clase Java, que incluye todo lo necesario para implementarlo.

El algoritmo de distribución de landed cost debe cargarse mediante un conjunto de datos "Sistema", por lo que puede estar disponible para cada Entidad de la instancia de Etendo.

Una vez aplicado, el algoritmo de cálculo de costes "Distribución por importe" se lista en esta ventana.

Se recomienda aplicar este tipo de conjuntos de datos de sistema a la organización (\*), por lo que están disponibles para cada organización de la Entidad.

Si no se muestra ningún registro en esta ventana, contacte con su "Administrador del sistema" para asegurarse de que los conjuntos de datos "Sistema" se han aplicado correctamente utilizando el siguiente comando "ant": ant apply.module -DforceRefData=true

Un tipo de landed cost puede crearse como una "**Cuenta**" o como un "**Producto**".

-   Los tipos de landed cost de "**Cuenta**" requieren que se cree un elemento de G/L, por ejemplo "Aranceles".
    -   El elemento de G/L debe configurarse como "Habilitado en facturas financieras" y relacionado con una categoría de impuestos; de este modo, este tipo de landed costs puede contabilizarse mediante una factura financiera de compra.
    -   La cuenta contable de tipo "Gasto" utilizada al contabilizar una factura financiera de compra que incluya un landed cost de este tipo es la configurada en la solapa Contabilidad del elemento de G/L.
-   Los tipos de landed cost de "**Producto**" requieren que se cree un Producto, por ejemplo "Porte"; de este modo, este tipo de landed costs puede contabilizarse mediante una factura de compra.
    -   La cuenta contable de tipo "Gasto" utilizada al contabilizar una factura de compra que incluya un landed cost de este tipo es la configurada en la solapa Contabilidad del Producto.

![Tipo de Landed Cost](../../../../assets/drive/1RtueiqPAlE2jmnhvOF5o4nkkwutJL1e6.png)
## Reglas de almacén

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Reglas de almacén`

### Visión general

La ventana de reglas de almacén permite al usuario revisar las reglas de almacén disponibles.

Las reglas de almacén se utilizan para restringir el stock disponible en el almacén.

Las reglas se aplican cuando el stock se recupera automáticamente mediante procesos como la generación de albaranes.

### Regla

Las nuevas reglas de almacén solo pueden aplicarse mediante módulos de extensión, que deben incluir un conjunto de datos con la definición de la regla y un procedimiento que la implemente.

Etendo incluye tres reglas diferentes por defecto:

-   **Atributo único**: todo el stock propuesto para su uso debe ser del mismo valor de atributos. Devuelve el primer valor de atributos que se encuentre con cantidad suficiente para cumplir el requisito. Si no existe ningún valor de atributos con stock suficiente, no se propone ningún stock. Esta es una regla de exclusión.
-   **Hueco único**: todo el stock propuesto debe proceder del mismo hueco. Devuelve el stock del primer hueco encontrado con cantidad suficiente. Si no existe ningún hueco con cantidad suficiente, entonces el stock se obtiene de cualquier hueco. Esta es una regla de preferencia y no una regla de exclusión.
-   y **Regla de almacén por defecto**: la regla por defecto no restringe nada y se devuelve todo el stock disponible de los almacenes con cantidad disponible. Esta regla puede utilizarse en los pedidos de venta siempre que se desee sobrescribir una regla definida en el almacén para no aplicar ninguna regla.
## Tipo de Inventario Referenciado

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Tipo de Inventario Referenciado`

Esta sección define diferentes tipos de contenedores o cajas, que incluyen cualquier tipo de objeto que pueda contener mercancías.

Campos de la ventana **Tipo de Inventario Referenciado**

-   **Organización** : Entidad organizativa dentro de la entidad.
-   **Nombre** : Un identificador no único para un registro/documento, a menudo utilizado como herramienta de búsqueda.
-   **Compartido** : Referencias compartidas o únicas.
-   **Secuencia** : El orden de los registros en un documento especificado.
-   **Descripción** : Un espacio para escribir información adicional relacionada.
-   **Activo** : Un indicador que señala si este registro está disponible para su uso o está desactivado.
-   **Tipo de Inventario Referenciado**
-   **Entidad** : Entidad para esta instalación.
## Ventana Tipo EAN 128

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Tipo EAN 128`

En esta ventana puede añadir diferentes tipos de códigos de barras. Estos almacenan información sobre el producto en este código, como por ejemplo: Fecha, Producto, Línea de almacén, y cuando lo escanee, puede obtener esta información desde el código de barras.

![Ventana Tipo EAN 128](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/EAN128Type.png)

### Cabecera

![](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/EAN128Header.png)

- Campos de cabecera de **Tipo EAN 128**:

- **Módulo** : Módulo para exportar los datos.

- **Organización** : Entidad organizativa dentro de la entidad.

- **Nombre** : Un identificador no único para un registro/documento, a menudo utilizado como herramienta de búsqueda.

- **Descripción** : Aquí se introduce una descripción que indique la utilidad de este nuevo tipo.

- **Valor por defecto** : Cuando se selecciona, este Tipo EAN 128 aparecerá por defecto.

- **Activo** : Un indicador que señala si este registro está disponible para su uso o está desactivado.

### Líneas

En las líneas puede añadir un registro que haga referencia al padre ya creado. Aquí creará un dato que se recibirá al escanear un código de barras.

![](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/EAN128Lines.png)

- Campos de líneas de **Tipo EAN 128**:

- **Módulo** : Módulo para exportar los datos.

- **Organización** : Entidad organizativa dentro de la entidad.

- **Activo** : Un indicador que señala si este registro está disponible para su uso o está desactivado.

- **Contenido** : Nombre del contenido de la línea.

- **AI** : Identificador de aplicación, que hace referencia a los números adicionales del código.

- **Longitud del contenido** : Longitud del contenido del tipo EAN.

- **Tipo de datos** : Tipo de datos del Tipo EAN 128.

- **Longitud fija** : Esta casilla se marca si el código solo contiene el dato o no.

- **Lote** : Indicador que determina si el código EAN corresponde a un "lote" o "número de lote".

- **N.º de serie** : Un número único de productos.

- **F. caducidad** : Determina si es una fecha de caducidad.

- **Secuencia** : El orden de los registros en un documento especificado. La secuencia indica el orden de los registros.

- **Atributo**: Un atributo para definir un elemento.

- **Entidad**: El grupo al que hace referencia el elemento escaneado.

- **Campo de entidad** : Propiedad de la entidad de la que se obtiene el valor. Hace referencia al campo HQL de la entidad.

### Ejemplo

Por ejemplo, veremos un registro creado aquí:

![](../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/EANLineExample.png)

- **Contenido** : Aquí se añadirá el nombre de este nuevo tipo que se está creando.

- **AI** : El AI proporciona un número de posiciones decimales en el valor siguiente. El valor representado es el entero siguiente dividido por 10X. Por ejemplo, un peso neto de 22,7 kg podría codificarse como 3101 000227, 3102 002270, 3103 022700 o 3104 227000. El AI registrado debería ser 310X.

- **Longitud del contenido** : Esta será la longitud del código; en función de para qué se utilice, puede ser más larga o más corta.

- **Tipo de datos** : Esto hace referencia al tipo de dato que se almacenará en el código de barras. Puede ser: Fecha, Cadena, Entero o Decimal.

- **Longitud fija** : Esta casilla deja únicamente la información relevante en el código escaneado.

- **Lote** : El atributo de lote parece ser un indicador que determina si el contenido actual extraído del código EAN corresponde a un "lote" o "número de lote".

- **N.º de serie** : Un número único; representa un número de serie.

- **F. caducidad** : Este campo define que el valor del código de barras es una fecha de caducidad.

- **Secuencia** : Este campo ayuda a realizar el seguimiento del número de secuencia de cada entrada. Si hay varias entradas con el mismo nombre de campo de entidad, el código utiliza el número de secuencia para determinar cuál tiene el número más reciente y, en base a ello, decide si actualiza o no el contenido almacenado en el objeto.

- **Entidad**: en este campo puede asignar la entidad a la que corresponde este valor. Tiene 5 opciones:

- **Atributo**: cuando se selecciona esta opción, el campo "Atributo" aparecerá en la pantalla. Si no tiene ninguno creado, puede ir a esta ventana y crearlo. Un atributo es una característica que se puede añadir al valor escaneado, para tener una mejor referencia del mismo.
    * **Línea de pedido**.
    * **Línea de almacén.**
    * **Línea de producto.**
    * **Línea de envío/recepción.**

Estas últimas 4 opciones muestran el Campo de entidad; por lo tanto, al seleccionar una de estas 4 opciones.

- **Campo de entidad**: En este selector puede elegir el campo específico de la entidad a la que hace referencia.

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.