---
title: Unidad logística de stock
tags:
    - Unidad logística
    - Unidad
    - AUOM
    - Stock
    - Etendo Mobile
---
# Unidad logística de stock
:octicons-package-16: Javapackage: `com.etendoerp.stock.logisticunit`

## Visión general

<iframe width="560" height="315" src="https://www.youtube.com/embed/yrP1iPmCk_U?si=Riy5plMo7lVDjVWS" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).


El módulo **Unidad logística de stock** amplía la funcionalidad estándar de Etendo para gestionar unidades logísticas dentro de los procesos de inventario, recepción y reserva de stock. En concreto, este módulo añade las [unidades de medida](../../../basic-features/master-data-management/product-setup.md#unit-of-measure) y los [tipos de inventario referenciado](../../../basic-features/warehouse-management/setup.md#referenced-inventory-type) **Empaquetar** y **Pallet**.

Su objetivo es integrar las **Unidades Alternativas (AUOM)** con el modelo de **Inventario Referenciado (RI)**, de modo que las unidades logísticas se reconozcan, registren y gestionen como entidades trazables en todas las operaciones de almacén.

Además, incorpora una **lógica avanzada de reserva de stock** que prioriza unidades logísticas completas frente a unidades individuales. Esto significa que, al procesar un pedido de venta con reserva automática de cantidad en AUOM, el sistema prioriza esta condición y solo completa la reserva con unidades individuales si no se alcanza la cantidad requerida. Esta regla de prioridad garantiza una gestión de stock más eficiente y asegura que las operaciones respeten la condición original de la venta por AUOM, manteniendo la trazabilidad a nivel de unidad logística. Habilite la preferencia **Habilitar la gestión de UDM** para ver y gestionar UDM alternativas.

En resumen:

- Añade la UDM **Empaquetar** y la UDM **Pallet**. Estas están disponibles en el sistema para configurar AUOM de productos. 
- Agrega los tipos de inventario referenciado **Empaquetar** y **Pallet** con sus secuencias correspondientes.
- Cada AUOM debe estar vinculada a un **tipo de inventario referenciado**, mediante el campo *Tipo de unidad logística*, garantizando que la creación de stock en las ventanas de **Inventario Referenciado** cumpla con la unidad logística definida.
- Introduce reglas inteligentes de reserva que respetan la lógica de las unidades logísticas (p. ej.: cajas) y de las unidades, reduciendo errores de asignación de stock. Con esta lógica, cuando un pedido de venta se reserva automáticamente, el sistema intenta satisfacer la cantidad solicitada en el pedido con unidades logísticas completas si es posible, antes de recurrir a unidades individuales.

## Configuración inicial

Para empezar a utilizar este módulo correctamente, deben completarse los siguientes pasos de instalación y configuración:

- [x] Instalar el bundle [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}.
- [x] Instalar el conjunto de datos **Unidad logística de stock**.
- [x] Configuración de preferencias.

### Instalar el conjunto de datos Unidad logística de stock
:material-menu: `Aplicación`>`Configuración General` > `Organización` > `Gestión del módulo de Empresa`

Abra la ventana **Gestión del módulo de Empresa** e instale los datos de referencia **Unidad logística de stock** incluidos en el módulo; esto creará las unidades de medida y los tipos de inventario referenciado **Empaquetar** y **Pallet**. 

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/dataset.png)

### Preferencias 

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Preferencias`

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/preference.png)

Por defecto, el módulo incluye tres preferencias preconfiguradas. Estas pueden deshabilitarse creando una nueva preferencia con el valor establecido en `N` si fuese necesario:

- **GenerateLogisticsUnitAutomatically**: Controla si el sistema debe crear automáticamente registros de Inventario Referenciado al completar una recepción de mercancías. Si está habilitada (`Y`), se generan automáticamente unidades logísticas como cajas o pallets, garantizando la trazabilidad desde el momento en que los artículos entran en el almacén.

- **Habilitar reservas de stock**: Habilita la lógica de reserva de stock. Cuando está activa, el sistema prioriza satisfacer los pedidos de venta con unidades logísticas completas (cajas, pallets) antes de utilizar unidades individuales. Esto asegura una asignación más eficiente y reduce errores de stock.

- **Habilitar la gestión de UDM**: Activa la gestión de Unidades de Medida (UDM). Cuando está habilitada, los usuarios pueden asignar cajas o pallets como unidades para los productos, configurar conversiones y aplicarlas en los procesos (ventas, compras, logística). Esta preferencia es necesaria para integrar Unidades Alternativas con inventario referenciado (Tipo de unidad logística).

### Unidad de medida

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Unidad de medida`

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/uom.png)

En la ventana Unidad de medida, el módulo añade las unidades de medida **Empaquetar** y **Pallets** para facilitar la gestión de unidades logísticas dentro del sistema.
Estas UDM sirven como base para configurar productos con unidades alternativas, mientras que el usuario puede crear tantas variantes adicionales como necesite en función del diferente formato de caja utilizado.


### Tipo de Inventario Referenciado

:material-menu: `Aplicación` > `Gestión de Almacén` > `Configuración` > `Tipo de Inventario Referenciado`

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/referenced-inventory-type.png)

En la ventana Tipo de Inventario Referenciado, el módulo añade los tipos de inventario referenciado **Empaquetar** y **Pallet**, cada uno con su secuencia correspondiente. De este modo, el inventario referenciado mantiene la trazabilidad a nivel de unidad logística, garantizando la consistencia entre las AUOM definidas y los registros de stock. Las reservas se actualizan utilizando una lógica que permite tener en cuenta las unidades alternativas de medida.

### Producto - Unidad Alternativa

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Producto`

En la solapa [Unidad Alternativa](../../../basic-features/master-data-management/master-data.md#alternate-uom-tab) de la **ventana Producto**, al habilitar la preferencia **Habilitar la gestión de UDM** se permite a los usuarios asignar *Empaquetar* o *Pallet* como **unidades alternativas de medida**

!!! warning
    Solo se admite un nivel de unidades logísticas. Por ejemplo, los productos pueden gestionarse en pallets o en cajas, pero todavía no se admiten pallets que contengan cajas de productos.

Los usuarios pueden definir tasas de conversión y especificar en qué procesos (ventas, compras, logística) se aplican estas conversiones. En base a esta configuración, las reglas de reserva de stock priorizan automáticamente pallets y cajas completos antes de utilizar unidades individuales, optimizando la gestión de inventario.

Una funcionalidad adicional introducida es una mayor granularidad mediante la posibilidad de seleccionar un **Tipo de unidad logística**. Por ejemplo, si la unidad alternativa es *Empaquetar*, el sistema permite especificar si se trata de una caja grande, mediana o pequeña. Esto proporciona un mayor nivel de control y precisión en la gestión de inventario.


![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/alternate-uom.png)

**Campos a tener en cuenta:**

- **Tipo de unidad logística**: Desplegable vinculado a [Tipo de Inventario Referenciado](../../../basic-features/warehouse-management/setup.md#referenced-inventory-type), utilizado al registrar entradas y salidas de mercancía.

### Producto - Stock por unidad logística

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Producto`

Permite visualizar el stock por unidades logísticas (inventario referenciado) de una forma más clara y organizada. Los usuarios pueden aplicar filtros por producto, ubicación o tipo de unidad logística, proporcionándoles una vista simplificada y enfocada del stock. Por ejemplo, es posible filtrar por una ubicación específica y un tipo específico de unidad logística para ver cuántas unidades logísticas hay y qué productos contienen. Además, desde esta solapa, los usuarios pueden navegar directamente a la ventana Unidad logística (Inventario Referenciado), accediendo a todos los detalles de su contenido.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/product-stock-by-logistic-unit-tab-1.png)

Campos a tener en cuenta:

- Unidad logística: este campo muestra el Inventario Referenciado más el tipo de Inventario Referenciado.
- Tipo de unidad logística: este campo muestra el tipo de Inventario Referenciado.
- Ubicación: espacio donde se encuentra el producto.
- Cantidad disponible: cantidad disponible.
- Cantidad reservada: cantidad reservada.

## Flujo de trabajo

El módulo Unidad logística de stock interviene de forma transversal en los procesos de recepción, reserva, venta y entrega de productos, proporcionando una gestión integral basada en unidades alternativas de medida (AUOM) y referencias de inventario (RI).
Su funcionalidad se potencia cuando se utiliza junto con otros componentes del Warehouse Extensions Bundle.

### Recepción (Recepción de mercancías)

El flujo de recepción comienza en la ventana Recepción de mercancías, donde se registran las entradas de producto. Al introducir mercancía que utiliza unidades alternativas (como **cajas** o **pallets**), el módulo Unidad logística de stock identifica estas condiciones gracias a su integración con AUOM y los tipos de Inventario Referenciado que define.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/goods-receipt.png)

Cuando se completa el documento de recepción, utilizando el botón *Finalización masiva*, el sistema **genera automáticamente los registros de inventario referenciado** (RI) asociados a esas unidades logísticas.

!!! info
    Para utilizar la creación **automática de RI**, debe disponer del módulo **Finalización masiva**. Para más detalles, consulte [Finalización masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/essentials-extensions/bulk-completion.md)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/reference-inventory-1.png)

Las cajas recibidas pueden verse en el stock.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/stock-1.png)

De este modo, el stock recibido no se interpreta como unidades individuales, sino como una entidad logística trazable (una caja o un pallet), garantizando la consistencia entre las cantidades físicas y el inventario del sistema, sentando las bases para que los procesos posteriores —como reservas, ventas o entregas— respeten siempre la estructura logística en la que el producto fue registrado originalmente.

### Inventario Referenciado

Al instalar este módulo, el **Inventario Referenciado** permite crear unidades logísticas anidadas, lo que significa que un inventario referenciado (p. ej., un pallet) puede contener otros inventarios referenciados (p. ej., cajas). 

Esta mejora permite crear estructuras logísticas jerárquicas, como *cajas dentro de pallets*, manteniendo plena compatibilidad con los procesos estándar **Empaquetar** y **Desempaquetar**. De este modo, cuando se ejecuta la acción *Desempaquetar* sobre un pallet, se obtienen las cajas que contiene. A su vez, puede ejecutarse la acción *Desempaquetar* sobre esas cajas para obtener las unidades individuales incluidas en cada una.

!!! important
    Restricciones para la gestión de pallets y cajas: 

    - Los pallets pueden contener cajas y unidades básicas.
    - Los pallets no pueden contener pallets.
    - Las cajas pueden contener cajas y unidades básicas.
    - Cada unidad logística solo puede estar en una agrupación a la vez.
    - Las cajas no pueden moverse entre pallets. Una vez que una caja está en un pallet, debe permanecer allí hasta que se realice un Desempaquetar para liberarla.
    - El proceso Desempaquetar aplica la Ubicación asignada a esa agrupación para los productos que contiene, sustituyendo la ubicación original.

El usuario accede a la ventana **Inventario Referenciado** y crea un nuevo registro seleccionando el tipo **Pallet**. Una vez creado, el pallet queda disponible como unidad logística contenedora.

A continuación, mediante el botón *Empaquetar*, el usuario puede seleccionar una o varias cajas existentes (de tipo CAJA) a través del selector de stock o unidades básicas de uno o varios productos. El sistema **solo mostrará aquellas cajas y unidades** que no estén asignadas a otra agrupación. Tras la confirmación, la selección queda vinculada al pallet y su información se actualiza automáticamente.

En cualquier momento, el usuario puede consultar la solapa Contenido del pallet para ver las cajas que contiene o utilizar el botón *Desempaquetar* para liberarlas, devolviéndolas a su estado original.

<figure markdown="span">
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/box-box-units-1.png)
    <figcaption>Ejemplo: Caja que contiene *Cajas* y *Unidades básicas*</figcaption>
</figure>

<figure markdown="span">
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/pallet-box-units-1.png)
    <figcaption>Ejemplo: Pallets que contienen *Cajas* y *Unidades básicas*</figcaption>
</figure>


!!! example
    Se recibe un pallet con cajas de zumo de piña. La recepción se realiza desde la ventana Recepción de mercancías.
    Una vez completada la recepción, el usuario debe entrar manualmente en la ventana **Inventario Referenciado** para crear una **caja** por cada **caja** recibida.
    A continuación, debe crearse un nuevo Inventario Referenciado de tipo **Pallet** y asociar a este las cajas creadas previamente.
    De este modo, el stock del producto muestra un Pallet cuyo contenido está compuesto por cajas, en lugar de unidades individuales del producto.

### Ventas

El flujo de ventas se combina con la lógica de reserva de stock, garantizando que las unidades logísticas permanezcan consistentes y trazables durante todo el proceso.

En el Pedido de venta, el usuario puede seleccionar el producto y definir la unidad alternativa (AUOM) en la que desea realizar la venta, como una **caja** o un **pallet**. Aquí es donde entra en juego la **lógica de reserva del módulo**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/sales-order-1.png)

Las reglas inteligentes de reserva **priorizan la unidad definida en el pedido de venta** y, en el caso de unidades logísticas, el sistema intentará primero asignar unidades alternativas completas (cajas o pallets) antes de recurrir a unidades individuales, optimizando el uso del stock y manteniendo la trazabilidad de cada unidad logística.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit/reserved-1.png)

Cuando se genera una reserva automática desde el pedido de venta, el sistema compara el producto, la AUOM y la cantidad solicitada, seleccionando las unidades referenciadas que mejor satisfacen la demanda.

Esta lógica garantiza que, si la venta se realizó por una unidad alternativa, el proceso de reserva mantenga esa condición y respete la composición original del producto.

Como resultado, la venta se gestiona y ejecuta en la unidad alternativa de medida definida, transfiriéndose automáticamente a los procesos logísticos posteriores como entrega, empaquetado y otras operaciones de almacén.

La trazabilidad de las Unidades Alternativas y de los Inventarios Referenciados se mantiene en todas las etapas de la gestión de inventario, garantizando que las unidades logísticas utilizadas permanezcan correctamente identificadas desde la venta hasta que el producto sale del almacén.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.