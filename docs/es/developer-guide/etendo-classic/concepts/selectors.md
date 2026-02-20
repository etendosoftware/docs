---
tags: 
  - Concepts
  - Selector
  - HQL
  - Reference
---

# Selectores

## Visión general

En esta sección se describe el proceso para definir selectores en el sistema Etendo.

Los selectores combinan un cuadro de sugerencias con una ventana emergente con capacidades de filtrado y ordenación. Tienen una serie de características importantes:

  * Pueden definirse completamente sin codificación manual.
  * La definición del selector (columnas, criterios de búsqueda, cláusula where) puede cambiarse en tiempo de ejecución sin recompilar ni reiniciar el sistema.
  * El selector facilita enormemente mostrar información vinculada de una entidad seleccionada o buscar, ordenar y filtrar por información vinculada.
  * El cuadro de sugerencias del selector, así como el grid emergente, admiten paginación con anticipación (lookahead). Esto los hace adecuados también para conjuntos de datos grandes.

## Concepto de selector

Un selector se define dentro del Diccionario de Aplicación, como parte de la definición de una Referencia (un tipo de dominio) y se utiliza para representar referencias de clave foránea en la interfaz de usuario de Etendo.

Un selector consta de tres partes:

  * La definición de la referencia.
  * La cabecera del selector que define desde qué tabla seleccionar y la cláusula where a utilizar.
  * Los campos del selector que definen en qué columnas se busca y qué columnas se muestran en la ventana emergente.

## Definir un selector

Para definir un nuevo selector, vaya a `Application Dictionary` > ventana `Reference`.
Definir el selector es un procedimiento de tres pasos:

  1. Crear una nueva referencia.
  2. Crear una cabecera de selector.
  3. Crear cero o más campos de selector.

Esta sección le guía a través de los tres pasos.

### Paso 1: Definir una referencia

La referencia se utiliza en la definición de la columna. La definición se muestra a continuación en la captura de pantalla.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-2.png)

Descripción de los campos:

  * Nombre, Descripción y Ayuda deben establecerse con un valor específico para la referencia que está creando.
  * Referencia base **debe** establecerse a false.
  * Referencia padre **debe** establecerse a `OBUISEL_Selector_Reference`.
  * Model, WAD y Runtime UI Implementation pueden dejarse vacíos la mayor parte del tiempo.

### Paso 2: Definir el selector

Después de definir la referencia, puede introducirse la información del selector. Esto también se hace en la ventana de referencia. Asegúrese de que la ventana de referencia muestra la referencia que ha creado en el paso 1; a continuación, haga clic en **Selector Definido** en la parte superior derecha de la ventana y pulse el botón **nuevo**.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-3.png)

Descripción de los campos:

  * **Nombre y Ayuda/Comentario**: establézcalos con valores que describan el selector.
  * **Descripción**: se utiliza como título de la ventana emergente.
  * **Plantilla**: normalmente solo debería haber una opción: Selector Template. Es posible que haya múltiples opciones si se han instalado plantillas adicionales para selectores.
  * **Tabla**: normalmente un selector selecciona desde una tabla; seleccione la tabla relevante de la lista.
  * **Columna**: la columna en la tabla referenciada a la que apunta la columna de clave foránea. Si no se establece nada aquí (valor por defecto), entonces se utiliza la columna de clave primaria.
  * **Fuente de datos**: puede establecerse cuando no se selecciona ninguna tabla. Una fuente de datos puede utilizarse para proporcionar datos que no se leen de la base de datos sino que, por ejemplo, se calculan en tiempo de ejecución. Para más información sobre Fuentes de datos, consulte el Manual del desarrollador de [Fuente de datos](../concepts/datasources.md).
  * **Cláusula HQL 'where'**: esta cláusula where se utiliza para filtrar los datos leídos desde la base de datos.

!!! Note
    Actualmente no es posible utilizar variables de sesión en la cláusula where.

!!! Note
    Al utilizar propiedades de la entidad en la cláusula where, siempre debe usarse el prefijo `e.`, por ejemplo `e.seqno`

  * **Campo Mostrado**: este campo del selector se muestra en el desplegable del cuadro de sugerencias. Algunos aspectos específicos:
    * Un valor vacío (el valor por defecto) significa que se utilizan las columnas identificadoras de la tabla referenciada para mostrar información en el cuadro de sugerencias. Este valor por defecto suele ser una buena elección.
    * Inicialmente, al crear un selector, no es posible seleccionar aquí un campo ya que aún no se han definido campos de selector (véase la siguiente sección). Después de definir uno o más campos de selector, es posible elegir aquí uno de estos campos.
  * **Campo de Valor**: este campo del selector se establece como valor y se almacena en la base de datos como el campo de clave foránea. Algunos aspectos específicos:
    * Un valor vacío (el valor por defecto) significa que se utiliza la columna de clave primaria de la tabla referenciada. Este es, con diferencia, el caso más común y por tanto una buena elección para la mayoría, si no prácticamente todos, los casos.
    * Inicialmente, al crear un selector, no es posible seleccionar aquí un campo ya que aún no se han definido campos de selector (véase la siguiente sección). Después de definir uno o más campos de selector, es posible elegir aquí uno de estos campos.
  * **Ordenar por campo**: este campo del selector se utiliza para ordenar los registros en el desplegable del cuadro de sugerencias. Algunos aspectos específicos:
    * Un valor vacío (el valor por defecto) significa que los registros se ordenan por los valores del campo mostrado. Y en caso de que el campo mostrado tampoco esté definido, se utilizan las columnas identificadoras de la tabla referenciada para ordenar la información en el cuadro de sugerencias. Este valor por defecto suele ser una buena elección.
    * Inicialmente, al crear un selector, no es posible seleccionar aquí un campo ya que aún no se han definido campos de selector (véase la siguiente sección). Después de definir uno o más campos de selector, es posible elegir aquí uno de estos campos.

### Paso 3: Definir campos del selector

Después de definir la cabecera del selector, el siguiente paso es definir el campo del selector. Un campo del selector se utiliza para lo siguiente:

  * Definir una columna en el grid de búsqueda emergente.
  * Definir una columna de la tabla destino en la que se busca para el cuadro de sugerencias.
  * Definir el campo mostrado del cuadro de sugerencias (lo que se muestra cuando un usuario escribe valores en el campo).
  * Definir el campo de valor, la columna que se utiliza para establecer el valor en la columna de clave foránea.
  * Definir el campo de ordenación del cuadro de sugerencias.

Un selector puede tener cero o más campos de selector. Es posible definir un selector sin campos de selector. El sistema utilizará el valor por defecto, que consiste en mostrar el identificador en el cuadro de sugerencias y usar la clave primaria de la tabla referenciada como valor. El cuadro de sugerencias se muestra en el campo, pero no se muestra ninguna ventana emergente. Por tanto, esta es una definición de selector ligera.

Para definir un campo de selector, haga clic en el enlace **Campo de Selector Definido** que se muestra en la parte superior derecha de la pestaña Selector Definido.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-6.png)

Descripción de los campos de Campo de Selector Definido:

  * **Nombre**: utilice aquí un nombre descriptivo.
  * **Propiedad**: es una columna/propiedad de la tabla establecida en la cabecera del selector. Este campo está implementado utilizando el propio selector. Esto facilita que un usuario seleccione la propiedad de modelo correcta. Es posible introducir una ruta de propiedad. Para la tabla de tercero, es posible, por ejemplo, especificar `name`, lo que mostrará el nombre del banco de la cuenta bancaria del tercero. Consulte la [siguiente sección](#rutas-de-propiedad-mostrar-información-vinculada) sobre Rutas de propiedad para más información.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-7.png)

  * **Descripción y Ayuda/Comentario**: establézcalos con valores significativos para su caso específico (consulte también el campo **Centralizado** a continuación). El campo descripción es para uso futuro.
  * **Mostrar en grid**: si está marcado, entonces el campo es visible en el grid emergente. Si no está marcado, entonces el campo no se muestra en el grid emergente. Aun así puede utilizarse como campo de valor, campo mostrado, campo de ordenación o como campo de búsqueda para el cuadro de sugerencias.
  * **Orden de las columnas en el grid**: el orden en el que se muestran las columnas en el grid emergente. Solo es relevante si **Mostrar en grid** está marcado.
  * **Permitir ordenar**: determina si el usuario puede ordenar por esta columna en el grid emergente. Solo es relevante si **Mostrar en grid** está marcado.
  * **Filtrable**: determina si el usuario puede filtrar por esta columna en el grid emergente. Solo es relevante si **Mostrar en grid** está marcado.
  * **Centralizado**: si está marcado, entonces el nombre, la descripción y la ayuda/comentario se copian/usan desde la columna. Esto se gestiona mediante el proceso [Sincronizar términos](../concepts/Element_and_Synchronize_Terminology.md).
  * **Usado en el cuadro de sugerencias**: por defecto, el cuadro de sugerencias utilizará la cadena introducida por el usuario para buscar en el campo mostrado (establecido en la cabecera del selector) o en el identificador. Puede seleccionar campos adicionales en los que buscar estableciendo este campo (Usado en el cuadro de sugerencias) a sí/marcándolo. Para hacer invisible el campo de búsqueda, simplemente desmarque el campo **Mostrar en grid**; entonces el campo solo se utiliza para buscar y no se muestra en el grid emergente.

!!! note
    * Si ninguno de los campos del selector tiene **Mostrar en grid** marcado/establecido a sí, entonces no hay grid emergente disponible y no se muestra el icono de la lupa; el usuario solo puede seleccionar datos a través del cuadro de sugerencias.
    * Al establecer una columna como filtrable o permitir ordenar, es posible que se encuentre una disminución del rendimiento en una tabla con muchos miles de registros. Si esto ocurre, contacte con el administrador de la base de datos para optimizar la tabla añadiendo índices. Tenga en cuenta que estos nuevos índices deben exportarse a los metadatos de Etendo usando los procedimientos estándar `export.database`.

### Rutas de propiedad, mostrar información vinculada

El selector tiene una funcionalidad muy potente que facilita mostrar información vinculada en el cuadro de sugerencias y en las ventanas emergentes.

Para dar un ejemplo de información vinculada: para un selector de tercero, es bastante fácil mostrar el identificador de la categoría del tercero. Esta información vinculada puede requerir múltiples pasos, por lo que es posible mostrar el nombre del banco de la cuenta bancaria del tercero. Estos dos ejemplos se introducen así en el campo propiedad de Campo de Selector Definido:

  * `businessPartnerCategory._identifier`
  * `name`

Al usar el punto (.), la ruta da el siguiente paso en el modelo. El cuadro de sugerencias en la ventana Campo de Selector Definido ayuda a introducir la ruta correcta.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-8.png)

Esto se muestra así:

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-9.png)

### Tabla y Fuente de datos

Un selector puede obtener su contenido de una tabla o de una Fuente de datos. Cuando en la definición del selector se define una tabla, entonces en el servidor Etendo creará una fuente de datos para esta tabla. Por tanto, internamente para Etendo no hay una diferencia real entre una tabla o una fuente de datos para el selector.

Hay varios casos de uso para los que tiene sentido usar una fuente de datos:

  * Cuando los datos de un selector requieren preprocesamiento después de recuperarlos de la base de datos.
  * Cuando los datos de un selector ni siquiera se leen de la base de datos, sino que el sistema los calcula en memoria.

Una fuente de datos la implementa un desarrollador y luego se define en el Diccionario de Aplicación. Después de esto, puede utilizarse para definir selectores.

!!!note
    Para más información sobre cómo implementar una fuente de datos, consulte su página de [Fuentes de datos](../concepts/datasources.md).

### Información traducida

El Selector y los Campos del selector también le permiten especificar versiones traducidas de los nombres y títulos mostrados en la interfaz de usuario. Para usar nombres y títulos traducidos, vaya a las pestañas **Traducción del Selector Definido** y **Traducción de campo de selector definido**. Estas pestañas están disponibles en la parte superior de la ventana al editar un Selector o un Campo del selector.

## Usar un selector

El siguiente paso es hacer uso del selector en el modelo de datos. El selector es igual que cualquier otra Referencia en Etendo. La Referencia se utiliza en la definición de una Columna. Para usar el selector definido y establecerlo en una columna, vaya a `Application Dictionary` > `Tables and Columns`. A continuación, seleccione la tabla y la columna para la que desea establecer la referencia.

Luego, en el campo de referencia, elija la referencia `OBUISEL_Selector`. Después, en el siguiente desplegable **Referencia clave**, seleccione el selector específico. En la captura de pantalla siguiente se elige un Selector de tercero.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-11.png)

La columna puede utilizarse para definir un campo en la ventana de Etendo de forma estándar. Por tanto, en la definición de Ventana/Solapa/Campo de Etendo no se requiere ninguna configuración o tratamiento especial para el selector.

Después de establecer la referencia en la columna y usarla en una ventana específica, necesita reiniciar Etendo para verlo en funcionamiento.

## Cambiar un selector en tiempo de ejecución

La propia definición del selector puede cambiarse en tiempo de ejecución sin recompilar el sistema. No hay límites reales sobre qué parte de la definición del selector puede cambiarse en tiempo de ejecución; una lista no exhaustiva:

  * Añadir/eliminar columnas del grid emergente.
  * Cambiar la cláusula where.
  * Cambiar los campos en los que se busca como parte de la visualización del cuadro de sugerencias.

!!! note
    Para cambiar un selector, el módulo al que pertenece debe estar en desarrollo.
    Si no, es posible que el javascript del lado cliente (que representa el selector) no se actualice automáticamente.

## Definir campos de salida

Los valores de retorno habituales de un Selector son el registro **id** y el **identificador**. En algunos casos el desarrollador quiere devolver más campos y no solo estos dos. Puede marcar un Campo del selector como **Campo de salida** y formará parte del objeto devuelto en JavaScript.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-13.png)

!!! note
    Por defecto, los campos **id** e **identifier** forman parte del objeto devuelto.

### Usar campos de salida en código manual (avanzado)

Puede usar los nuevos selectores en código manual (no generado por WAD). Debe incluir todas las importaciones JS necesarias. Hay una función gancho vacía `onValueChanged` que puede sobrescribir en su ventana manual para realizar cualquier acción personalizada. Cuando el usuario selecciona una fila, esta función se ejecuta. Por defecto no hace nada.

#### Ejemplo de función

!!! note
    Para probar este código, debe tener un navegador con la consola habilitada, por ejemplo Firefox con Firebug.

```javascript
    isc.OBSelectorLinkWidget.addProperties({
      onValueChanged: function(selected) {
        // selected is an object with members id and _identifier
        // plus all Out Fields
        window.console.log("%o", selected); 
      }
    });
```

En este caso, todas las instancias de OBSelectorLinkWidget ejecutarán la misma función; esta función de ejemplo simplemente imprime el objeto pasado como parámetro.

También puede sobrescribir la función solo en una instancia concreta.

```javascript
    // sc_C_Bpartner_One_ID is an instance of OBSelectorWidget or OBSelectorLinkWidget
    sc_C_Bpartner_One_ID.onValueChanged = function(selected) {
      window.console.log("%o", selected);
    };
```

## Proporcionar una nueva plantilla de selector (avanzado)

La definición del selector se convierte a código javascript usando una plantilla. La plantilla se selecciona en el selector (véase el paso 2 anterior). Es posible que un módulo añada una nueva plantilla que pueda utilizarse para crear selectores.
La creación de una nueva plantilla debe realizarla un desarrollador con un buen conocimiento de Etendo.

Además, para implementar una nueva plantilla es necesario entender el procesamiento de plantillas y la funcionalidad de gestión de plantillas utilizada por Etendo. La página [Arquitectura de Etendo](../concepts/etendo-architecture.md) proporciona información detallada. Trata tanto el procesamiento de plantillas, el caché, i18n, como también ofrece indicaciones sobre cómo implementar una plantilla personalizada.

La plantilla utilizada para el selector puede encontrarse en el árbol de código fuente del módulo `org.openbravo.userinterface.selector`, dentro del paquete `org.openbravo.userinterface.selector.templates`, en el archivo `selector.ftl`.

Una plantilla personalizada debe crearse dentro de un módulo separado. Para usarla, defínala en `Application Dictionary` > `Templates`.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-15.png)

Los principales campos a establecer:

  * The TemplateClasspathLocation debe apuntar a la ubicación en el árbol de código fuente de la plantilla personalizada.
  * The ComponentType **debe** establecerse a selector. The ComponentType determina si la plantilla puede seleccionarse en la definición del selector.

![](../../../assets/developer-guide/etendo-classic/concepts/Selectors-16.png)

Al definir selectores, el usuario puede seleccionar la plantilla personalizada.

## Personalizar el aspecto del selector

El estilo del selector se deriva en su mayor parte automáticamente del estilo de otros componentes. Solo es necesario aplicar estilo al icono a la derecha del campo; consulte [esta página](../concepts/skins.md#selector) para más información.

## Resolución de problemas

### El cuadro de sugerencias no filtra

**Síntoma** : Al escribir valores en el cuadro de selección, no filtra; se muestran todos los registros.

**Causa** : Esto puede ocurrir cuando ha añadido accidentalmente campos booleanos/sí-no para que se **usen en el cuadro de sugerencias**.

**Solución** : desmarque los campos **usados en el cuadro de sugerencias** para los campos booleanos/sí-no; la búsqueda en estos campos no está soportada por el selector en el cuadro de sugerencias.

### El cuadro de sugerencias siempre está vacío

**Síntoma** : Al escribir valores en el campo de selección, el cuadro de sugerencias está vacío o muestra muchos menos resultados de los esperados; además, al seleccionar el desplegable directo se obtiene una lista vacía/más pequeña de lo esperado.

**Causa** : esto ocurre porque hay campos **usados en el cuadro de sugerencias** que requieren un join a una tabla mientras que la clave foránea no siempre está establecida. Solo se muestran los registros que tienen un valor en la clave foránea.

**Solución** : si el campo de selección de clave foránea es el único sobre el que se filtra, esto está bien; sin embargo, si hay múltiples campos de búsqueda, entonces la búsqueda sobre campos de clave foránea no obligatorios no está soportada por el selector.

## Temas avanzados

### Transformadores HQL

Es posible modificar completamente una consulta HQL mediante Java e inyección de dependencias usando transformadores. Para implementar la nueva funcionalidad, visite [Transformadores HQL](../how-to-guides/How_to_create_a_HQL_Based_Table.md#HQL_Transformers).

### Usar claves foráneas en consultas HQL personalizadas

Para hacerlo, la cláusula select de HQL para esa propiedad debe apuntar a una entidad (es decir, `e.organization`, en lugar de `e.organization.name`). Luego, en la definición del campo del selector, tenemos que seleccionar una referencia de Tabla que apunte a la entidad destino.

---
Este trabajo es una obra derivada de [Selectores](http://wiki.openbravo.com/wiki/Selectors){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.