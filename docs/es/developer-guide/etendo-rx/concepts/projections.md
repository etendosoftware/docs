---
tags:
    - Etendo RX
    - Servicio DAS
    - Proyecciones
    - Mapeos
    - Conector
    - Búsqueda
    - API
---

# Proyecciones y mapeos

## Visión general

Al utilizar Spring Data JPA para implementar la capa de persistencia, el repositorio normalmente devuelve una o más instancias de la clase raíz. Sin embargo, en la mayoría de los casos, no necesitamos todas las propiedades de los objetos devueltos.

En estos casos, puede que queramos recuperar los datos como objetos de tipos personalizados. Estos tipos reflejan vistas parciales de la clase raíz, conteniendo solo las propiedades necesarias. Aquí es donde las proyecciones son útiles.

## Ventana Proyecciones y mapeos

:material-menu: `Aplicación` > `Etendo RX` > `Proyecciones y mapeos`

Una **proyección** es un conjunto de campos específicos de una entidad o campos combinados de múltiples entidades. Las proyecciones son útiles cuando necesitamos recuperar solo un subconjunto de datos, ya que reduce la cantidad de datos que necesitamos recuperar de la base de datos, lo que conlleva una mejora del rendimiento.

Esta ventana permite la creación de endpoints de lectura y escritura de datos en Etendo, utilizando el servicio DAS. Este servicio, en base a las configuraciones de esta ventana, genera dinámicamente los endpoints al iniciarse.

Para crear una nueva proyección en Etendo, es necesario completar los campos en la cabecera de la ventana **Proyecciones y mapeos**.

![](../../../assets/developer-guide/etendo-rx/concepts/projections/projection-and-mappings.png)

- Organización: Entidad organizativa dentro del cliente.
- Nombre: Describe el nombre de la proyección. La cantidad máxima de caracteres para este campo es 10.
- Módulo: Indica el módulo del que forma parte el elemento. Este es el módulo en el que se exporta la configuración.
- Descripción: Descripción de la proyección.
- Activo: Un check para indicar si esta proyección está disponible o deshabilitada.

### Solapa Entidades proyectadas

En esta solapa, se pueden definir las entidades a proyectar. Pueden tener dos tipos de proyecciones: Lectura y Escritura. Esto significa que, al interactuar con un sistema externo, es posible leer la información en la base de datos de Etendo Classic para exponerla al otro sistema. La otra opción es escribir información en la base de datos de Etendo Classic, es decir, extraer información del sistema externo para utilizarla en Etendo.

Al referirse a una entidad a proyectar, esta entidad está relacionada con una tabla específica.

!!!warning
    Recuerde que siempre es necesario crear ambos registros, uno de tipo escritura y otro de tipo lectura, para que los endpoints generados funcionen correctamente.

![](../../../assets/developer-guide/etendo-rx/concepts/projections/projected-entities.png)

Campos a tener en cuenta:

- Organización: La organización correspondiente de la entidad.
- Nombre: Este campo se completa automáticamente según las opciones seleccionadas en los campos Tabla y Tipo de mapeo, añadiendo _Lectura_ o _Escritura_ según corresponda.
- Tabla: Es el identificador que conecta la entidad de Etendo a proyectar con la tabla de base de datos, responsable de almacenar la información de la entidad.
- Tipo de mapeo: En este caso, hay dos opciones: Etendo a sistema externo y Sistema externo a Etendo. En el caso del tipo Lectura, la opción a seleccionar es Etendo a sistema externo. En el caso del tipo Escritura, la opción a seleccionar es Sistema externo a Etendo.
- Es endpoint REST: Casilla de verificación para permitir que el servicio genere el endpoint o no.
    
    !!!info
        Esta casilla no debería marcarse, por ejemplo, cuando no es necesario exponer un endpoint de subentidad.
- External_Name: parámetro para llamar a la API. Debe ser único, pero es posible tener más de un nombre para cada entidad. Por defecto, se autogenera con el nombre de la entidad, pero en caso de generar más de uno, deben tener nombres diferentes.
- Activo: Un check para indicar si este registro está disponible o no.

#### Botón Crear campos de proyección

Con este botón, se muestra una ventana emergente donde puede encontrar una lista de todos los campos a proyectar y seleccionar los necesarios. Este proceso no incluye proyecciones de tipo **Lista** ni de tipo Identidad.

![](../../../assets/developer-guide/etendo-rx/concepts/projections/create-projections-fields.png)

!!!info
    Los campos obligatorios a proyectar pueden filtrarse con la columna _Es obligatorio_.

#### Subsolapa Campo de entidad

En esta subsolapa, el desarrollador puede definir cada campo de entidad que se incluirá en la proyección.

![](../../../assets/developer-guide/etendo-rx/concepts/projections/entity-field.png)

=== "Tipo Lectura"

    Campos a tener en cuenta:

    - Módulo: Indica el módulo del que forma parte el elemento. Este es el módulo en el que se exporta la configuración.
    - Organización: La organización correspondiente de la entidad.
    - Propiedad: Este campo tiene 3 tipos de opciones:
        - `_identifier`: Esta opción permite proyectar el/los campo/s definidos como identificador en la ventana Tablas y columnas. Esta opción siempre proyecta una cadena.
        - Estándar: En este caso, es posible seleccionar todos los campos estándar de la entidad proyectada. Ej.: tipos cadena, número, fecha, etc. Además, es posible navegar por las diferentes entidades. Ej.: product.name, businessPartner.name, etc.
        - `*List`: Las propiedades que terminan en "List" permiten proyectar una lista de entidades relacionadas. Estas listas se autogeneran a partir de las columnas con la casilla Link to Parent Column seleccionada. Ej.: la propiedad `OrderLineList` de la entidad Order se genera ya que la columna `C_Order_ID` de la tabla `C_OrderLine` está relacionada con la tabla `C_Order`.
    - Nombre: Clave JSON de salida. Debe ser única, pero es posible tener más de un nombre para cada propiedad. Por defecto, se autogenera con el nombre de la propiedad, pero en caso de generar más de uno, deben tener nombres diferentes.
    - Identifica el registro de forma unívoca: Casilla de verificación para usar este registro como identificador. Si ningún campo tiene este check seleccionado, se utilizará el ID de base de datos de la tabla.

    Configuración de mapeo

    - Mapeo de campo:
      - Mapeo directo: cada propiedad se muestra tal cual.
      - Mapeo Java: es un mapeo personalizable y puede configurarse a través de la ventana Mapeos Java. Si se elige esta opción, permite definir mapeos más complejos o implementar una lógica específica. El resultado del mapeo será de tipo JSON.
      - Mapeo de entidad: esta opción se utiliza cuando es necesario relacionar dos proyecciones diferentes. En este caso, se habilita el campo Entidad de proyección relacionada para seleccionar la entidad proyectada. En caso de proyectar una lista de elementos, la entidad seleccionada se asigna a cada ítem de la lista.
      - Mapeo constante: si elige esta opción, se proyecta el valor constante definido en el campo correspondiente.
    - Entidad de proyección relacionada: Campo adicional que se muestra cuando se selecciona la opción Mapeo de entidad anterior. Aquí puede seleccionar la propiedad a proyectar para cada entidad en el mapeo.
    - Valor constante: Solo disponible cuando se selecciona Mapeo constante como tipo de mapeo. Aquí define el valor constante a utilizar en el mapeo.
    - Identificadores de proyección relacionados: Campo adicional que se muestra cuando se selecciona la opción Mapeo de entidad anterior. Es un campo informativo para revisar el identificador de la entidad mapeada.
    - Activo: Un check para indicar si este registro está disponible o deshabilitado.

=== "Tipo Escritura"

    Campos a tener en cuenta:

    - Módulo: Indica el módulo del que forma parte el elemento. Este es el módulo en el que se exporta la configuración.
    - Organización: La organización correspondiente de la entidad.
    - Propiedad: Este campo tiene 3 tipos de opciones:
        - `_identifier`: Esta opción permite proyectar el/los campo/s definidos como identificador en la ventana Tablas y columnas. Esta opción siempre proyecta una cadena.
        - Estándar: En este caso, es posible seleccionar todos los campos estándar de la entidad proyectada. Ej.: tipos cadena, número, fecha, etc. Además, es posible navegar por las diferentes entidades. Ej.: product.name, businessPartner.name, etc.
        - `*List`: Las propiedades que terminan en "List" permiten proyectar una lista de entidades relacionadas. Estas listas se autogeneran a partir de las columnas con la casilla Link to Parent Column seleccionada. Ej.: la propiedad `OrderLineList` de la entidad Order se genera ya que la columna `C_Order_ID` de la tabla `C_OrderLine` está relacionada con la tabla `C_Order`.
    - Nombre: Clave JSON de salida. Debe ser única, pero es posible tener más de un nombre para cada propiedad. Por defecto, se autogenera con el nombre de la propiedad, pero en caso de generar más de uno, deben tener nombres diferentes.
    - Es obligatorio: Casilla de verificación solo disponible para proyecciones de "Escritura". Esto indica que la propiedad proyectada es obligatoria cuando se crea un nuevo ítem.
    - Identifica el registro de forma unívoca: Casilla de verificación para usar este registro como identificador. Si ningún campo tiene este check seleccionado, se utilizará el ID de base de datos.

    Configuración de mapeo

    - Mapeo de campo:
      - Mapeo directo: cada propiedad se muestra tal cual.
      - Mapeo Java: es un mapeo personalizable y puede configurarse a través de la ventana Mapeos Java. Si se elige esta opción, permite definir mapeos más complejos o implementar una lógica específica. El resultado del mapeo será de tipo JSON.
      - Mapeo de entidad: esta opción se utiliza cuando es necesario relacionar dos proyecciones diferentes. En este caso, se habilita el campo Entidad de proyección relacionada para seleccionar la entidad proyectada. En caso de proyectar una lista de elementos, la entidad seleccionada se asigna a cada ítem de la lista.
      - Mapeo constante: si elige esta opción, se proyecta el valor constante definido en el campo correspondiente.
    - Crear relacionado: Habilita la creación de elementos relacionados a partir de una entidad seleccionada. Solo disponible para mapeos de tipo Escritura.
    - Entidad de proyección relacionada: Campo adicional que se muestra cuando se selecciona la opción Mapeo de entidad anterior. Aquí puede seleccionar la propiedad a proyectar para cada entidad en el mapeo.
    - Jsonpath: lenguaje para extraer propiedades de objetos JSON. Para más información, visite [JSON](https://en.wikipedia.org/wiki/JSONPath){target="_blank"}.
    - Valor constante: Solo disponible cuando se selecciona Mapeo constante como tipo de mapeo. Aquí define el valor constante a utilizar en el mapeo.
    - Identificadores de proyección relacionados: Campo adicional que se muestra cuando se selecciona la opción Mapeo de entidad anterior. Es un campo informativo para revisar el identificador de la entidad mapeada.
    - Activo: Un check para indicar si este registro está disponible o deshabilitado.

    **Mapear campos a hijo**

    Esta subsolapa se muestra si se selecciona el check Crear relacionado en la subsolapa Campo de entidad. Permite proporcionar información desde los campos del padre a los registros hijo. Los registros creados en esta subsolapa son útiles para conectar los campos de entidad proyectados con propiedades que pertenecen a entidades padre.

    Campos a tener en cuenta:

    - Módulo: Indica el módulo del que forma parte el elemento. Este es el módulo en el que se exporta la configuración.
    - Organización: La organización correspondiente de la entidad.
    - Campo relacionado: Muestra opciones de campos de la entidad de proyección relacionada ya definida.
    - Propiedad: Si es necesario crear un nuevo campo, esta es la propiedad a utilizar para crearlo.
    - Activo: Un check para indicar si este registro está disponible o deshabilitado.

    **Ejemplo:**

 	![](../../../assets/developer-guide/etendo-rx/concepts/projections/map-fields-to-child.png)
    ![](../../../assets/developer-guide/etendo-rx/concepts/projections/map-fields-to-child1.png)

    En este ejemplo, al escribir una proyección sobre la tabla C_OrderLine y proyectar la orderLineTaxList (con la lista de impuestos aplicables para cada línea), es necesario seleccionar primero la casilla Crear relacionado. Esta opción creará los elementos relacionados en la lista de entrada. Sin embargo, las líneas de impuestos requieren una referencia obligatoria a la cabecera, concretamente el Pedido.
    
    Para ello, la información debe transmitirse desde la entidad origen a la entidad mapeada. Esto puede hacerse añadiendo un nuevo registro en la solapa Mapear campos a hijo. En el Campo relacionado, seleccione el campo de entidad hijo correspondiente a la entidad proyectada (p. ej., el campo Pedido de venta en la entidad OrderLineTax). En el campo Propiedad, seleccione el campo de la entidad origen (p. ej., Pedido de venta de la entidad OrderLine).
    
    Esta configuración garantiza que, cuando se crean nuevas líneas de pedido, los impuestos relacionados referencien el pedido original. Esta configuración solo es necesaria si la columna mapeada no tiene seleccionada la casilla Link to Parent Column. En este ejemplo, esto se refiere a la columna Pedido de venta en la tabla C_OrderLineTax.

## Ventana Tablas y columnas

:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Tablas y columnas`

En esta ventana, es posible definir búsquedas asociadas a tablas. Estas son filtros personalizados con consultas HQL.

Esta ventana también permite la creación de endpoints de búsqueda, utilizando el servicio DAS. Este servicio, en base a las configuraciones de esta ventana, genera dinámicamente los endpoints al iniciarse.

### Solapa Repositorio

En Spring Data, un repositorio es una abstracción que proporciona las operaciones relativas a una clase de dominio para interactuar con un almacén de datos.
Para crear el repositorio para nuestro propósito, necesitamos ir a Tablas y columnas, seleccionar una tabla y, en la solapa *Repositorio*, crear un nuevo registro definiendo el módulo en desarrollo donde se exportan las configuraciones.

![](../../../assets/developer-guide/etendo-rx/concepts/projections/repository-tab.png)

#### Subsolapa Búsqueda

A continuación, podemos definir búsquedas para obtener datos filtrados de la tabla seleccionada.

<figure markdown="span">
 	![new-search.png](../../../assets/developer-guide/etendo-rx/tutorial/new-search.png)
	<figcaption>Ejemplo de búsqueda en la tabla C_Order</figcaption>
</figure>

Campos a tener en cuenta:

- Nombre del método: el nombre de la búsqueda que se utiliza en la generación del endpoint.
- Consulta: consulta HQL para filtrar los elementos de la tabla.

##### Subsolapa Parámetro de búsqueda

En esta subsolapa, es posible definir parámetros a utilizar en la búsqueda.

<figure markdown="span">
 	![new-search-parameter.png](../../../assets/developer-guide/etendo-rx/tutorial/new-search-parameter.png)
	<figcaption>Ejemplo de parámetro utilizado en la búsqueda de la sección anterior</figcaption>
</figure>

Campos a tener en cuenta:

- Nombre: Nombre del parámetro.
- Tipo: Tipo de parámetro. Es un desplegable con los tipos base disponibles.

## Ventana Valores constantes

:material-menu: `Aplicación` > `Etendo RX` > `Valores constantes`

En esta ventana, es posible definir valores constantes para ser utilizados en los [campos de entidad](#subsolapa-campo-de-entidad) en los que la información no debe modificarse. Esta configuración se realiza en la ventana [Proyecciones y mapeos](#proyecciones-y-mapeos).

![](../../../assets/developer-guide/etendo-rx/concepts/projections/constantvalues.png)

Campos a tener en cuenta:

- Módulo: Indica el módulo del que forma parte el valor. Este es el módulo en el que se exporta la configuración.
- Organización: Entidad organizativa dentro del cliente.
- Nombre: Describe el nombre identificador del valor.
- Valor constante: Describe el valor a establecer, por ejemplo, un ID de entidad.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.