---
title: Capa de Acceso a Datos
tags:
    - Conceptos
    - Capa de Acceso a Datos
    - Lógica de negocio
    - Hibernate
    - Objeto de negocio
    - Arquitectura de desarrollo
---

# Capa de Acceso a Datos
  
##  Visión general

El objetivo del desarrollo de la Capa de Acceso a Datos (DAL) de Etendo es reforzar la capa intermedia de la aplicación, es decir, implementar la lógica de negocio en Java. La DAL proporciona al desarrollador de la aplicación la siguiente funcionalidad:

- Consultas y recuperación con seguridad de tipos de objetos de negocio desde la base de datos. 
- Una API cómoda para actualizar o crear nuevos datos en la base de datos. 
- Una interfaz con seguridad de tipos para actualizar la información de un objeto de negocio, aumentando la productividad al hacer que las propiedades de un objeto de negocio sean directamente visibles mediante getters y setters (en el IDE). 
- Gestión de transacciones y del contexto. 
- Comprobación de seguridad y validación. 
- Mapea automáticamente nuevas entradas en el Diccionario de Aplicación a tablas y columnas de la base de datos. 
- Genera clases Java de objetos de negocio (y sus asociaciones) sobre la base del modelo del Diccionario de Aplicación. 

La DAL consta de una parte en tiempo de desarrollo y una parte en tiempo de ejecución. La parte en tiempo de desarrollo se encarga de generar las clases Java de objetos de negocio. La parte en tiempo de ejecución se encarga de mapear las clases Java a la base de datos y de proporcionar funcionalidad de soporte como la seguridad y la validación.
## Un ejemplo de 'Hello World'

Como primer ejemplo sencillo, vamos a crear un nuevo grupo de terceros y guardarlo en la base de datos:
``` java
     // create the object through the factory
      final Category bpg = OBProvider.getInstance().get(Category.class); 
     
     // set some values
     bpg.setDefault(true);
     bpg.setDescription("hello world");
     bpg.setName("hello world");
     bpg.setValue("hello world");
     bpg.setActive(true);
     
     // store it in the database
     OBDal.getInstance().save(bpg);
```

Hay varias cosas importantes que conviene tener en cuenta:

- El código anterior no establece un contexto de usuario explícito. El contexto de usuario se establece automáticamente al ejecutar el código anterior en Etendo Classic. Sin embargo, en otros entornos, debe establecerse explícitamente; consulte [aquí](#contexto-de-usuario) para más información.
- Existe una clase BPGroup que modela los datos de la tabla _c_bp_group_. Esta clase tiene getters y setters con tipado seguro para todos los datos de esta tabla.
- Se utiliza una factoría (OBProvider) para crear una instancia de la clase BPGroup.
- El servicio OBDal es el principal punto de entrada a la Data Access Layer; ofrece funcionalidad de guardado, eliminación y consulta. La API de OBDal se trata con más detalle más abajo.

El fragmento de código anterior también muestra que no necesita trabajar con SQL o JDBC para trabajar con los datos de la base de datos. Como desarrollador, trabaja directamente con objetos y los datos disponibles son visibles directamente a través de los getters y setters.

Como siguiente paso, vamos a consultar el grupo de terceros y cambiar su descripción:

```java
     // create an OBCriteria object and add a filter
     final OBCriteria<Category> obCriteria = OBDal.getInstance().createCriteria(Category.class);
     obCriteria.add(Restrictions.eq("name", "hello world"));
     
     // perform the actual query returning a typed list
     final List<Category> categories = obCriteria.list();
     final Category cat = categories.get(0);
     
     // and set a new name
     cat.setName("another hello world");
     OBDal.getInstance().save(cat);
```

Este fragmento de código introdujo varios conceptos nuevos:

- El servicio OBDal se utiliza para crear un objeto OBCriteria.
- El objeto OBCriteria representa la consulta, implementa la interfaz Hibernate Criteria y puede utilizarse como un objeto Hibernate Criteria estándar. El objeto OBCriteria también admite parámetros de ordenación y paginación. La API de OBCriteria se trata con más detalle más abajo.
- El método `list` de OBCriteria ejecuta la consulta; devuelve una lista con tipado seguro de los objetos solicitados.
- Tras cambiar el nombre del grupo de terceros, no necesita realizar un guardado explícito. En el momento del commit, Hibernate detectará automáticamente los objetos _dirty_ y los guardará.

Esta fue una breve introducción que muestra cómo el DAL puede utilizarse para crear, almacenar y recuperar un objeto de negocio (simple). El resto de esta sección describirá la funcionalidad de la Data Access Layer con más detalle.
## Arquitectura DAL

La imagen siguiente muestra la arquitectura prevista para la capa de acceso a datos en
Etendo Classic.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Access_Layer-0.png)
  
Esta arquitectura se implementa:

- Modelo en tiempo de ejecución: el modelo en tiempo de ejecución es el principal impulsor para generar los objetos de negocio y el mapeo de Hibernate. También se utiliza ampliamente en seguridad, exportación/importación y en implementaciones de servicios web. 
- Mapeo de Hibernate: a partir del modelo en tiempo de ejecución, la DAL (durante la inicialización) genera un mapeo de Hibernate. Este mapeo de Hibernate se utiliza para inicializar Hibernate. 
- Esquema de base de datos: el modelo en tiempo de ejecución (en realidad, el diccionario de aplicación) puede utilizarse para actualizar el esquema de base de datos. Esto no está disponible como parte de la DAL, sino como parte del producto DBSourceManager. 
- Capa de acceso a datos: la Capa de acceso a datos (DAL) proporciona una API para almacenar, consultar y eliminar objetos de negocio de la base de datos. 
- Capa de modelo/lógica de negocio: la capa de modelo/lógica de negocio contiene la implementación de los procesos de negocio. 
- Servicios de negocio: la capa de servicios expone la lógica de negocio al mundo exterior. I

La arquitectura completa se ejecuta dentro de un contexto que proporciona seguridad y
gestión de transacciones.
## Objeto de negocio

Este documento utiliza el término objeto de negocio para denotar una entidad y su información dependiente. Un objeto de negocio puede ser una entidad simple, como una divisa, que solo tiene campos primitivos básicos. Por otro lado, también puede ser una estructura de entidades, por ejemplo, una cabecera de pedido con sus líneas de pedido.

Una estructura de objeto de negocio siempre tiene un objeto de negocio que es el propietario de todos los objetos de negocio de esa estructura; por ejemplo, para un pedido de venta, el objeto de negocio de la cabecera del pedido de venta es el propietario de la estructura completa (es decir, de las líneas del pedido de venta). Otra forma de describir esto es que las líneas del pedido de venta dependen de la cabecera del pedido de venta; una línea de pedido de venta no puede existir sin su cabecera del pedido de venta y, cuando se elimina una cabecera del pedido de venta, también deberían eliminarse sus líneas del pedido de venta.

La DAL utiliza las claves foráneas desde el hijo al padre para crear la asociación padre-hijo en Java e Hibernate. Más específicamente: las columnas de clave foránea que tienen el campo isParent establecido en sí (marcado/true) definen las relaciones padre-hijo del objeto de negocio; otras columnas de clave foránea definen asociaciones estándar de muchos a uno. Por ejemplo, el campo de clave foránea _c_order_id_ en _c_order_line_ se utiliza para crear la asociación de uno a muchos (en el modelo de ejecución en memoria) desde _c_order_ a _c_order_line_. Esta asociación de uno a muchos se utiliza después para generar un miembro List<OrderLine> en la clase Java Order y un mapeo de uno a muchos en Hibernate.
  
Es posible no generar esas asociaciones de uno a muchos en la entidad padre. Esto puede evitarse estableciendo el campo *Propiedad Hija en Entidad Padre* en false en la solapa Column. 

!!!note
    Las propiedades de uno a muchos generadas en la entidad padre cargan todos los hijos en memoria cuando se invocan, por lo que solo deberían generarse cuando la cantidad esperada de registros hijo sea baja; de lo contrario, podría provocar un `OutOfMemoryError`.

Para mantener una API compatible con versiones anteriores, puede configurarse la preferencia `hb.generate.all.parent.child.properties=true` en etendo.propeties; de este modo, todas las columnas de clave foránea generarán una propiedad de uno a muchos en la entidad padre.
##  Interfaces principales de DAL

La DAL ofrece tres servicios principales para instanciar, crear y consultar objetos de negocio de Etendo Classic: OBDal, OBCriteria y OBProvider. Las clases de servicio se pueden encontrar en el paquete _org.openbravo.dal.service_.

###  OBDal

La instancia de [OBDal](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/service/OBDal.java){target="\_blank"} (disponible a través de _OBDal.getInstance()_) es el principal punto de entrada para recuperar y almacenar objetos de negocio en la base de datos de forma validada y segura. Proporciona las siguientes funciones:

- save: almacena un nuevo objeto de negocio en la base de datos o actualiza un objeto de negocio existente. Para objetos de negocio existentes, no es necesario llamar a este método, ya que Hibernate realiza automáticamente la comprobación _dirty_. 
- get: recupera un único objeto de negocio usando su ID. Hay dos versiones: una usando el nombre de la clase (del objeto de negocio generado) y otra usando el nombre de la entidad. 
- remove: elimina un objeto de negocio de la base de datos; la eliminación real en base de datos se realiza en el momento del commit. 
- create OBCriteria: los objetos [OBCriteria](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/service/OBCriteria.java){target="\_blank"} se utilizan para realizar consultas. 
- commitAndClose y rollbackAndClose: estos métodos se pueden usar para implementar una gestión de transacciones personalizada. Normalmente, esto lo gestiona el entorno (contenedor web de Etendo o test de Etendo). 

La API de OBDal hace un uso extensivo de las clases [OBCriteria](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/service/OBCriteria.java){target="\_blank"} y [OBQuery](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/service/OBQuery.java){target="\_blank"} para dar soporte a las consultas.
  
La clase OBDal permite acceder al pool de base de datos de solo lectura. En este caso, la instancia debe recuperarse con el método _OBDal.getReadOnlyInstance()_. Es importante tener en cuenta que, si el pool de solo lectura no está configurado, este método utilizará el pool estándar para obtener las conexiones a la base de datos.
  
Una vez configurado el pool de solo lectura, hay dos formas de sobrescribir el comportamiento de _OBDal.getReadOnlyInstance()_:

- Creando un registro en _Selección de Pool de Datos_, que asocia un pool de base de datos con un informe concreto. 
- Usando la Preferencia _Pool de BD por defecto usado por informes_, que define el pool por defecto devuelto por _OBDal.getReadOnlyInstance()_ si no se realiza ninguna entrada en Selección de Pool de Datos para el Proceso actual. 

###  OBCriteria

La clase OBCriteria implementa la interfaz [Hibernate Criteria](https://docs.jboss.org/hibernate/core/3.5/reference/en/html/querycriteria.html){target="\_blank"}. Amplía la funcionalidad estándar de Hibernate Criteria para filtrar por activo, cliente y organización. Además, ofrece métodos de conveniencia para establecer el orderby y para realizar acciones de recuento.

En resumen, el objeto OBCriteria soporta todas las funcionalidades de Hibernate Criteria:

- Establecer la cláusula where de un filtro usando el concepto Hibernate Criterion. 
- Establecer parámetros de paginación como la primera fila y el número máximo de resultados. 
- Establecer el order by en la consulta. 
- Especificar joins por motivos de rendimiento. 
- Realizar recuentos, medias, etc. 

Para más información, consulte [Hibernate Criteria](https://docs.jboss.org/hibernate/core/3.5/reference/en/html/querycriteria.html){target="\_blank"} sobre consultas Criteria.

La funcionalidad de OBCriteria se ilustra con varios fragmentos de código:

Una instancia de OBCriteria se crea de la siguiente manera:

``` java
final OBCriteria obc = OBDal.getInstance().createCriteria(Currency.class);
```

Consulta sobre la propiedad name:

```java
obc.add(Restrictions.eq("name", "testname"));
```

Restrictions.eq es una instancia de la clase Hibernate Criterion. El concepto Hibernate Criterion es un lenguaje de expresiones codificado en Java que soporta las expresiones más utilizadas (and, or, equal, not-equal, in, between, etc.).

Establecer un orden descendente por la propiedad name:

``` java
obc.addOrderBy("name", false);
```

U otro: ordenar por la propiedad name de un objeto de negocio referenciado product:

``` java
obc.addOrderBy("product.name", false);
```

Establecer algunos parámetros de paginación, devolver 10 objetos, comenzando por el 100º:

``` java
     obc.setFirstResult(100);
     obc.setMaxResults(10);
```

Devolver también objetos inactivos (por defecto solo se devuelven objetos activos):

``` java
obc.setFilterOnActive(false);
```

Contar el número de objetos Currency en la base de datos:

``` java
final int bpGroupCount = obc.count();
```

Recuperar la lista de objetos de negocio:

``` java
     final List<BPGroup> bpgs = obc.list();
```

Obtener una moneda específica:

``` java
     final OBCriteria<Currency> obc = OBDal.getInstance().createCriteria(Currency.class);
     obc.add(Restrictions.eq("isoCode", "USD"));
     final List<Currency> cs = obc.list();
     final Currency c = cs.get(0);
```

###  OBQuery

La clase [OBQuery](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/service/OBQuery.java){target="\_blank"} es una extensión del objeto [Hibernate Query](https://docs.jboss.org/hibernate/orm/3.5/reference/en/html/queryhql.html){target="\_blank"}. Amplía la funcionalidad estándar de Hibernate Query para filtrar por activo, cliente y organización.

El objeto OBQuery se crea mediante el método _OBDal.createQuery_. El primer argumento de createQuery es una clase o un nombre de entidad; el segundo argumento es la cláusula where. La cláusula where puede ser una simple:
``` sql
    name='test'
```

o una que también declara un alias:
``` sql 
    as ol where ol.order.id='abc'
```

En código:
``` java
final OBQuery<Category> obQuery = OBDal.getInstance().createQuery(Category.class,"name='testname' or searchKey='testvalue'");
final List<Category> bpgs = obQuery.list();
```

###  OBProvider

Los objetos de negocio de Etendo no deben instanciarse directamente usando el operador new. En su lugar, debe usarse la clase [OBProvider](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/provider/OBProvider.java){target="\_blank"} para crear una instancia del objeto de negocio requerido. OBProvider se encuentra en el paquete _org.openbravo.base.provider_ y se puede recuperar usando el método OBProvider.getInstance(). OBProvider ofrece métodos para instanciar usando un nombre de clase o usando un nombre de entidad. Algunos ejemplos de código:
``` java
      final Category bpg = OBProvider.getInstance().get(Category.class); 
     
     // The ENTITYNAME constant is created by the business object generation logic
     final BPGroup bpg = (BPGroup)OBProvider.getInstance().get(BPGroup.ENTITYNAME);
```
##  Objetos de negocio de Etendo

La DAL genera, instancia y utiliza objetos de negocio de Etendo. Esta parte del manual de desarrollo describe su estructura y sus interfaces principales.

###  BaseOBObject

Todos los objetos de negocio de Etendo Classic heredan de la clase [BaseOBObject](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/structure/BaseOBObject.java){target="\_blank"}. Esta clase se encuentra en el paquete _org.openbravo.base.structure_.

La clase BaseOBObject ofrece la siguiente funcionalidad:

- Acceso directo (denominado la API dinámica) a todas las propiedades y valores de los datos dentro del objeto de negocio mediante los métodos get(String propertyName) y set((String propertyName, Object value). Estos métodos son especialmente útiles cuando se trabaja con funciones genéricas como la seguridad y el registro. 
- Acceso a la Entidad que describe el tipo y las propiedades del objeto de negocio. 
- Comprobaciones de seguridad y validación al obtener y establecer valores. 
- Acceso al ID del objeto mediante el método getId. 
- Acceso al identificador del objeto: el método getIdentifier de BaseOBObject utiliza las propiedades identificadoras del objeto para crear un título visible para ese objeto. 

La sección sobre el modelo en tiempo de ejecución y la API dinámica a continuación ofrece un ejemplo de cómo se pueden utilizar la API dinámica y el modelo en tiempo de ejecución.

Como todos los objetos de negocio de Etendo Classic deben extender esta clase, es seguro convertir un objeto a esta clase cuando sea necesario.

###  Clases de objetos de negocio generadas

En tiempo de desarrollo, la DAL generará clases de objetos de negocio para cada tabla definida en el diccionario de aplicación. Esto se realiza como parte de las tareas ant compile.complete o puede hacerse por separado mediante la tarea ant generate.entities. Estas clases generadas son las que normalmente utiliza un desarrollador porque ofrecen acceso tipado a propiedades comprobado en tiempo de compilación. Las clases generadas se crean en la carpeta _src-gen_ del proyecto de desarrollo de Etendo Classic y forman parte del paquete _org.openbravo.base.model_ y sus subpaquetes.

Las clases generadas extienden BaseOBObject y ofrecen getters y setters envoltorio tipados alrededor de los métodos genéricos set y get de la clase padre BaseOBObject:
``` java
     public String getRecord() {
      return (String) get("record");
     }
     
     public void setRecord(String record) {
      set("record", record);
     }
```
Además, las clases Java generadas establecen valores por defecto (en el constructor) y tienen una variable estática ENTITYNAME que debe utilizarse cuando sea necesario referirse directamente al nombre de una entidad.

###  Nomenclatura de Entidad, Propiedad y Columna

La Data Access Layer utiliza los nombres definidos en el Diccionario de Aplicación para diferentes propósitos:

- nombres de etiquetas xml en servicios web REST e importación/exportación 
- nombres de clase de las clases de Entidad generadas 
- nombres de miembro de los miembros de las clases de Entidad generadas 
- para detectar que una determinada Entidad implementa/soporta una determinada interfaz (consulte [aquí](#interfaces-importantes)) 

Históricamente, el diccionario de aplicación permite muchos tipos diferentes de nombres (también algunos que son ilegales para xml/java). Por lo tanto, la Data Access Layer aplica una lógica de conversión específica para garantizar siempre que los nombres sean válidos y únicos para xml/Java.

Para un listado completo de todos los nombres de entidad y propiedad, consulte la sección [Referencia del modelo de datos](/developer-guide/etendo-classic/concepts/data-model).

####  Nomenclatura de Entidad

Una entidad (corresponde a una tabla en Etendo Classic) tiene diferentes nombres, relevantes para distintas situaciones:

- Un nombre de tabla (almacenado en _AD_Table.tablename_) que es el nombre de la tabla de base de datos en la base de datos física. 
-  Un nombre de entidad (presente en _AD_Table.name_) que es un nombre globalmente único. Corresponde al nombre de la etiqueta XML utilizada para esa entidad. Se utiliza, por ejemplo, en [servicios web REST](../../../developer-guide/etendo-classic/concepts/xml-rest-web-services.md) y en exportación/importación de cliente. 
- Un nombre de clase Java (almacenado en _AD_Table.classname_), el nombre de clase se utiliza al generar el objeto de negocio Java. Es único dentro del paquete de datos de la tabla. 

Cada tabla (es decir, entidad) en Etendo Classic pertenece a un paquete de datos. Un paquete de datos tiene un campo de paquete Java que define el paquete Java en el que se genera la clase Java de la entidad.

!!!warning
   `AD_Table.name` no debería contener espacios en blanco. Si el nombre de la tabla contiene espacios, el proceso de construcción del nombre de la entidad eliminará esos espacios; por ejemplo, `My Table` se convertirá en `MyTable`.  
  
####  Nomenclatura de Propiedad

Para la nomenclatura de propiedades, la lógica es ligeramente diferente. La lógica de nomenclatura de propiedades tiene dos pasos diferenciados: 

1. Primero determinar un nombre de propiedad inicial, y

2. corregir/convertir este nombre de propiedad.

    El nombre de propiedad inicial se determina de la siguiente manera:

    Propiedades para tipo primitivo estándar (varchar, numeric, etc.) y columnas de clave foránea: para estas propiedades se utiliza el valor en _AD_Column.name_ como punto de partida del cálculo del nombre de la propiedad.
     
    - Propiedades que modelan una lista de entidades hijas: las denominadas propiedades one-to-many o de lista. Por ejemplo, la clase Order tiene una propiedad _OrderLineList_. El nombre inicial de esta propiedad se establece de la siguiente manera:
    
        - (caso común) si el nombre de la columna en el otro lado (del hijo al padre) es el mismo que el nombre de la columna de clave primaria del padre, entonces se utiliza el nombre de entidad del hijo más el sufijo 'List'. Por ejemplo, la tabla c_orderline tiene una clave foránea c_order_id hacia la tabla c_order. Esto da como resultado una propiedad orderLineList en la entidad Order.
        - (caso no común) si el nombre de la columna, que apunta del hijo al padre, es diferente del nombre de la columna de clave primaria del padre, entonces se utiliza la siguiente regla de nomenclatura: nombre de entidad destino + "_" + nombre de propiedad referenciada + "List". Por ejemplo, si la tabla c_orderLine tiene una columna: c_orderheader_id con nombre de propiedad orderHeader, entonces la propiedad de lista resultante en Order sería: OrderLine_orderHeaderList. 

    A continuación, la generación del nombre de propiedad realiza los siguientes pasos:

    - Se eliminan los espacios y se usan para camelcase; por ejemplo, el nombre 'Enable in Cash' se convierte en: EnableInCash (observe la I en mayúscula). 
    - Se eliminan los guiones bajos y se usan para camelcase: por ejemplo, el nombre 'C_Poc_email_ID' se traduce a CPocEmailID. 
    - Se eliminan los caracteres 'ilegales': solo se mantienen caracteres de la a a la z y de la A a la Z y números (no como prefijo), por lo que 'G/L Item' se traducirá a 'GLItem'. 
    - El primer carácter se pasa a minúscula: AccountingFact se convierte en accountingFact. 

####  Nomenclatura de Propiedad e interfaces soportadas

La Data Access Layer detecta automáticamente que una entidad soporta una determinada interfaz analizando el nombre de las propiedades de esa entidad. Por lo tanto, es muy importante ser preciso en la nomenclatura de propiedades. La nomenclatura de propiedades y las interfaces soportadas por propiedades específicas se tratan en la siguiente sección.

###  Interfaces importantes

Las clases generadas implementan un conjunto de interfaces que pueden utilizarse para comprobar si una determinada instancia de una clase tiene disponible una funcionalidad específica:

- [ClientEnabled](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/structure/ClientEnabled.java){target="\_blank"} : marca un objeto como que tiene un método getClient/setClient y como un objeto que es almacenado por Cliente.

    !!! note 
        Etendo detecta automáticamente que una tabla (==Entidad) implementa esta interfaz si tiene una columna con el nombre: client (definido en el campo ad_column.name). Cuando esta interfaz se implementa/detecta, entonces la propiedad client se utiliza para filtrar automáticamente objetos (en los clientes legibles) al consultar y para realizar comprobaciones de seguridad al persistir un objeto.


- [OrganizationEnabled](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/structure/OrganizationEnabled.java){target="\_blank"}: un objeto que implementa esta interfaz tiene métodos getOrganization/setOrganization. 

    !!! note
        Etendo detecta automáticamente que una tabla (==Entidad) implementa esta interfaz si tiene una columna con el nombre: organization (definido en el campo ad_column.name). Cuando esta interfaz se implementa/detecta, entonces la propiedad organization se utiliza para filtrar automáticamente objetos (en las organizaciones legibles) al consultar y para realizar comprobaciones de seguridad al persistir un objeto. 

- [ActiveEnabled](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/structure/ActiveEnabled.java){target="\_blank"}: un objeto que implementa esta interfaz tiene un indicador active (boolean) al que se puede acceder mediante los métodos isActive/setActive. 

    !!! note
        Etendo detecta automáticamente que una tabla (==Entidad) implementa esta interfaz si tiene una columna con el nombre: active (definido en el campo ad_column.name). Cuando esta interfaz se detecta/implementa, entonces el campo active se utiliza en el filtrado automático de objetos al consultar a través de la Data Access Layer. 

- [Traceable](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/structure/Traceable.java){target="\_blank"}: un objeto Traceable tiene información de auditoría: created y updated (campos de fecha), y createdby y updatedby (contienen un Usuario). Esta información de auditoría es accesible mediante los accesores correspondientes. 

    !!! note
        Etendo detecta automáticamente que una tabla (==Entidad) implementa esta interfaz si tiene las siguientes columnas (todas son obligatorias): creationDate, created, updated, updatedBy (establecidas en el campo ad_column.name). Observe específicamente el nombre de la propiedad de fecha de creación: debería ser: creationDate. Cuando esta interfaz se implementa/detecta, entonces la Data Access Layer establecerá automáticamente los campos de auditoría cuando un objeto se persista. 

###  Cliente, organización e información de auditoría

Las interfaces anteriores son utilizadas por la DAL cuando un objeto se guarda por primera vez o se actualiza en la base de datos:

- un objeto ClientEnabled para el cual no se ha establecido el Cliente obtendrá el Cliente actual del usuario (presente en el contexto de usuario). 
- un objeto OrganizationEnabled para el cual no se ha establecido la Organización obtendrá la Organización actual del usuario (presente en el contexto de usuario). 
- un objeto Traceable: cuando se guarda por primera vez, se establecen created, createdby, updated y updatedby. Cuando un objeto se actualiza, se establecen updated y updatedby. 

Por lo tanto, un desarrollador no necesita establecer explícitamente esta información en un objeto nuevo o existente. 

!!!note 
    Para que la Data Access Layer detecte que una tabla soporta las interfaces anteriores, los nombres de columna (AD_Column.name) deben ajustarse a estándares específicos; consulte [aquí](../../../developer-guide/etendo-classic/concepts/Data_Access_Layer.md#property-naming-and-supported-interfaces) para más información.

###  Creación de una nueva instancia de un objeto de negocio

Un objeto de negocio nunca debe crearse utilizando el operador new de Java. Todos los objetos de negocio deben crearse utilizando la clase factoría [OBProvider](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/provider/OBProvider.java){target="\_blank"}:

``` java
     // create the object through the factory
      final Category bpg = OBProvider.getInstance().get(Category.class);
```
Hibernate detectará que un objeto de negocio es nuevo cuando:

- el ID del objeto de negocio no está establecido 
- cuando el indicador newOBObject se establece explícitamente a true 

Por lo tanto, si desea crear un nuevo objeto de negocio con un ID específico (llamando a setId(...)), entonces necesita llamar explícitamente a businessObject.setNewOBObject(true). De lo contrario, Hibernate lanzará una excepción ('count of batch update operation....').
##  Contexto de usuario

La DAL opera dentro de un contexto de usuario. El contexto de usuario se implementa en la clase [OBContext](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/core/OBContext.java){target="\_blank"} en _org.openbravo.dal.core_. El OBContext se inicializa usando un userId. En base a este userId, el OBContext calcula el rol, los clientes, las organizaciones y las entidades accesibles. Esta información es utilizada por la DAL para la comprobación de seguridad y el filtrado automático por cliente y organización.

El OBContext se almacena como una variable ThreadLocal y la DAL siempre asume que hay una disponible. El OBContext puede recuperarse usando la llamada _OBContext.getOBContext()_.

Normalmente, un desarrollador puede asumir que siempre hay un contexto de usuario disponible. Las siguientes secciones lo tratan en detalle.

###  Contexto de usuario en una instancia de Etendo Classic en ejecución

Cuando el código se ejecuta dentro de una aplicación Etendo Classic, entonces el contexto de usuario siempre está establecido. Esto se realiza mediante un filtro de petición (el _DalRequestFilter_ en el paquete _org.openbravo.dal.core_). Este filtro de petición garantiza que el ThreadLocal de OBContext se establezca para el usuario actual (de Etendo), coloca el OBContext en la sesión http y limpia el OBContext cuando el hilo finaliza (ya que el hilo puede reutilizarse por otro usuario).

###  Contexto de usuario en un entorno de pruebas

La DAL utiliza una clase base para sus casos de prueba (consulte el tema Pruebas más abajo). Esta clase base se encarga de establecer el contexto de usuario al ejecutar pruebas.

###  Contexto de usuario en una situación independiente

El contexto de usuario también puede establecerse llamando a _OBContext.setOBContext(userId)_ con un userId que exista en la tabla ad_user. Esto configurará un contexto de usuario y lo colocará en el miembro ThreadLocal de OBContext para que lo utilice la DAL.

###  Modo administrador

Como se acaba de mencionar, la DAL opera dentro de un contexto de usuario y proporciona mecanismos automáticos de comprobación de seguridad para evitar que el usuario acceda a datos a los que, según el Modelo de Seguridad de Etendo, no debería acceder.

Sin embargo, en la mayoría de los casos, el fragmento de código desarrollado está contenido dentro de un objeto que, por sí mismo, proporciona automáticamente parte de la comprobación de seguridad, en particular el acceso a la entidad. Por ejemplo, si el fragmento de código forma parte de un proceso que se llama desde un botón, el usuario solo podrá hacer clic en ese botón si ya está en la ventana (y, por lo tanto, tiene acceso a esa entidad). Lo mismo ocurre cuando el código forma parte de un callout (el callout solo se disparará si el usuario ya está en la ventana).

El OBContext proporciona un Modo administrador que puede utilizarse para realizar acciones administrativas incluso si el usuario no tiene suficientes privilegios. Este modo omite la comprobación de Acceso a Entidad y no filtra por Cliente u Organización.

Se proporciona un Modo administrador adicional, que omite la comprobación de Acceso a Entidad, pero sí filtra por Cliente y Organización. Se recomienda utilizar este Modo administrador restringido, ya que filtra convenientemente por Cliente y Organización, algo que normalmente se necesita en el código de lógica de negocio.

La sintaxis para activar el Modo administrador restringido:
``` java
    try {
      OBContext.setAdminMode(true);
     
      // do administrative things here
     
    } finally {
      OBContext.restorePreviousMode();
    }
```

En algunos casos, sin embargo, también es necesario evitar la comprobación de cliente/organización; esto puede hacerse usando ` OBContext.setAdminMode(false) ` .

!!!note 
    Las llamadas a setAdminMode/restorePreviousMode están balanceadas, lo que significa
    que por cada llamada a setAdminMode también hay exactamente una llamada a
    restorePreviousMode. Si en una petición el número de llamadas a setAdminMode es
    desigual al número de llamadas a restorePreviousMode, entonces se muestra una advertencia:
    _Unbalanced calls to enableAsAdminContext and resetAsAdminContext_.

####  Modo administrador de referencia cruzada de organización
  
La validación de la organización del objeto referenciado en columnas [que lo soportan](../../../developer-guide/etendo-classic/concepts/Data_Access_Layer.md#cross-organization-references) puede
omitirse usando un modo Administrador especial: `
setCrossOrgReferenceAdminMode ` . La restauración del modo anterior se realiza mediante `
restorePreviousCrossOrgReferenceMode ` . De forma similar al modo administrador estándar,
las llamadas deben estar balanceadas para este modo, independientemente del modo administrador estándar.

``` java
      OBContext.setCrossOrgReferenceAdminMode();
      try {
     
        // cross organization references are allowed here
     
      } finally {
        OBContext.restorePreviousCrossOrgReferenceMode();
      }
```
## Transacción y sesión

La DAL implementa el patrón denominado open-session-view [https://developer.jboss.org/docs/DOC-13954]. Con una ligera variación: la DAL creará automáticamente una sesión de Hibernate e iniciará una transacción cuando se produzca el primer acceso a datos (si no existía ninguna). Por tanto, no cuando comienza la solicitud HTTP. La sesión y la transacción se almacenan en un `ThreadLocal` y se reutilizan para acciones posteriores de acceso a datos en el mismo hilo.

Un aspecto importante a tener en cuenta es que, normalmente, todas las acciones de base de datos se vuelcan (flush) a la base de datos cuando se confirma (commit) la sesión. En un entorno web, esto ocurre al final de la solicitud HTTP. Para realizar el flush bajo demanda, llame al método _OBDal.getInstance().flush()_.

Normalmente, un desarrollador no necesita confirmar (commit) o revertir (rollback) explícitamente una sesión o transacción:

- Dentro de Etendo Classic: se utiliza el patrón open-session-view [https://developer.jboss.org/docs/DOC-13954]; al ejecutar el código en la aplicación Etendo Classic, la confirmación de la transacción y el cierre de la sesión tienen lugar al final de la solicitud HTTP (consulte el [DalRequestFilter](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/core/DalRequestFilter.java){target="\_blank"}). Si se produce una excepción, entonces se realiza un rollback.
- En el entorno de pruebas de Etendo Classic: la clase base de pruebas de la DAL ([OBBaseTest](https://github.com/etendosoftware/etendo_core/blob/main/src-test/src/org/openbravo/test/base/OBBaseTest.java){target="\_blank"}) se encarga de confirmar o hacer rollback de las transacciones.
- Standalone: si el código se ejecuta en modo standalone, entonces es necesario realizar un commit o rollback explícito. Esto puede hacerse mediante los métodos de OBDal: _OBDal.getInstance().commitAndClose()_ o _OBDal.getInstance().rollbackAndClose())_.

!!!warning
    SQLC y DAL: el acceso estándar a la base de datos de Etendo Classic (a través de ventanas) funciona fuera de la DAL. Esto significa que el acceso a la base de datos utiliza una conexión diferente a la de la DAL. Si ambas conexiones actualizan la base de datos, entonces es posible que se produzca una situación de interbloqueo (deadlock). Por tanto, al trabajar/actualizar tanto mediante la DAL como mediante SQLC, siempre se debe primero confirmar/cerrar explícitamente la conexión de la DAL antes de continuar con SQLC, o viceversa.
##  Seguridad y Validación

La DAL realiza muchas comprobaciones diferentes de seguridad y validación, tanto en modo lectura como en modo escritura. Una violación de seguridad da como resultado una  [_SecurityException_](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/exception/OBSecurityException.java){target="\_blank"} , y un error de validación una  [_ValidationException_](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/validation/ValidationException.java){target="\_blank"}. Se lanzan diferentes excepciones en distintos puntos: algunas excepciones de seguridad se lanzan al leer un objeto de negocio (p. ej., violaciones de seguridad de lectura), otras se lanzan cuando la sesión hace commit o flush (violaciones de seguridad de escritura) o cuando se llama a un setter (ValidationException).

Si necesita trabajar sin estas comprobaciones de seguridad, debe utilizar el Modo Administrador o el Modo Administrador restringido.
Puede encontrar más información sobre ellos en [Modo Administrador](#modo-administrador).

###  Acceso de escritura

Las comprobaciones de acceso de escritura se realizan cuando se llaman los métodos save o remove de OBDal o cuando un objeto de negocio es guardado por Hibernate (en flush/commit). Para el acceso de escritura, se realizan las siguientes comprobaciones:

- El usuario debe tener acceso a una ventana/solapa que muestre la entidad. Consulte la tabla AD_Window_Access. 
- La organización del objeto de negocio debe estar en la lista de organizaciones con permiso de escritura de ese usuario. Las organizaciones con permiso de escritura son organizaciones vinculadas directamente al rol del usuario. 
- El cliente del objeto de negocio debe estar en la lista de clientes con permiso de escritura de ese usuario. 

Si falla cualquiera de las comprobaciones anteriores, se lanza una _SecurityException_.

###  Acceso de lectura

Un usuario solo puede ver información de sus propios clientes y de las organizaciones accesibles. Esto lo garantiza la DAL añadiendo automáticamente criterios de filtro en el objeto OBCriteria.

El acceso de lectura se comprueba tanto para el acceso de lectura directo como para el acceso de lectura derivado.
El acceso de lectura directo permite a un usuario ver toda la información de una determinada entidad. Con el acceso de lectura derivado, un usuario solo puede leer la propiedad activa, la información de auditoría y el ID y el identificador.

El acceso de lectura directo se basa en las tablas de acceso a ventanas; es decir, un usuario puede leer toda la información de una determinada entidad si el usuario tiene acceso a una ventana que muestre esa entidad. El acceso de lectura para una determinada tabla/entidad puede sobrescribirse usando la tabla ad_table_access. El conjunto de entidades directamente legibles lo calcula el  [EntityAccessChecker](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/security/EntityAccessChecker.java){target="\_blank"}  en el paquete `org.openbravo.dal.security`.

El acceso de lectura derivado se calcula de la siguiente manera: para cada entidad directamente legible se determina a qué otras entidades hace referencia. Estas otras entidades pasan a ser accesibles mediante lectura derivada. Por ejemplo, si un usuario puede leer directamente una entidad de factura, y una factura hace referencia a una divisa, entonces el usuario tiene acceso de lectura derivado a una divisa. Las entidades legibles derivadas también se calculan en el EntityAccessChecker.

El acceso de lectura directo y derivado se comprueba en distintos puntos:

- El acceso de lectura directo se comprueba cuando se llama a un método en la instancia de OBDal. 
- El acceso de lectura derivado se comprueba cuando se invoca un getter o se llama al método genérico get. 

###  Comprobación de borrado

Un usuario puede eliminar un objeto de negocio si:

- Tiene acceso de escritura a la entidad del objeto de negocio. 
- La entidad no está configurada como no eliminable; esto se define en _ad_table_ . 

Ambas comprobaciones de seguridad se realizan cuando la sesión hace commit o flush. Consulte la clase  [OBInterceptor](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/core/OBInterceptor.java){target="\_blank"} para más detalles.

###  Validación de acceso a tabla

Diferentes tablas en Etendo Classic tienen distintos niveles de acceso. Algunas tablas solo permiten información del cliente 0 y la organización *. Otras tablas permiten objetos de cualquier organización.

Cuando se guarda un objeto de negocio, se realiza una comprobación para verificar si el cliente y la organización de ese objeto de negocio son válidos para el nivel de acceso a tabla de la tabla. La comprobación se ha implementado en el AccessLevelChecker en `org.openbravo.base.validation`. Esta comprobación se realiza cuando la sesión hace commit o se hace flush.

###  Validación

Los valores de las propiedades se validan cuando se llama al setter o cuando se llama al método genérico set en el BaseOBObject. Se realizan las siguientes comprobaciones:

- se comprueba si la instancia del valor es válida para esa Propiedad 
- para valores String, se comprueba la longitud o los valores String permitidos (valores de lista/enumeración) 
- para valores numéricos, se comprueban el mínimo y el máximo 
- para valores obligatorios, se comprueba si el valor es distinto de null 

La validación de propiedades la realizan las clases en `org.openbravo.base.validation`. La estructura de validación se inicializa cuando se crea el modelo en tiempo de ejecución. Para cada Propiedad se crea un PropertyValidator correspondiente. Diferentes tipos de propiedades tienen diferentes tipos de PropertyValidators.

###  Validación de organización de entidad

Un objeto de negocio solo puede referirse a otros objetos de negocio que pertenezcan al árbol natural de la organización del objeto de negocio. Esta validación se realiza cuando se guarda un objeto de negocio (es decir, cuando la sesión hace commit/flush).

####  Referencias entre organizaciones
  
La validación de organización de entidad puede omitirse si se cumplen todas las condiciones siguientes:

- La columna de clave externa que referencia al otro objeto está marcada como _Permitir Referencia de Organización Cruzada_ . Esto puede configurarse en Tablas y Columnas > solapa Columna. 
- El contexto está en [Modo Administrador de Referencia entre Organizaciones](#modo-administrador-de-referencia-entre-organizaciones). 

#####  Referencias entre organizaciones en la UI

Las columnas que permiten referencias entre organizaciones permiten a los usuarios seleccionar registros de organizaciones no incluidas en el árbol del registro desde el que se referencian.
## Soporte de DAL para Vistas de Base de Datos

La DAL soporta las vistas prácticamente de la misma manera que las tablas normales definidas en el diccionario de aplicación. Esto significa que:

- las vistas de base de datos se consideran objetos de negocio normales
- se generan entidades para las vistas de base de datos
- las vistas de base de datos se pueden consultar usando HQL y las APIs de consulta de la DAL
- se puede acceder a las vistas de base de datos a través de las APIs de servicios web REST [XML](../../../developer-guide/etendo-classic/concepts/xml-rest-web-services.md) y [JSON](../../../developer-guide/etendo-classic/concepts/json-rest-web-services.md)

Hay una diferencia entre una vista de base de datos y una tabla de base de datos: la DAL no soporta actualizaciones sobre vistas; los objetos de negocio de vista se pueden leer y consultar, pero no insertar ni actualizar.

!!!note
    Para que la DAL considere una vista como un objeto de negocio, necesita tener una columna de clave primaria definida en el diccionario de aplicación. Esta columna no necesita ser una clave primaria real en la base de datos, pero debe contener valores únicos para cada registro de la vista.
## Funciones SQL en HQL

Para usar funciones SQL en HQL, primero debe asegurarse de que Hibernate conozca su función. Por lo tanto, en su código Java tiene que registrar la función. Esto se hace creando una clase que implemente la interfaz **SQLFunctionRegister** y esté anotada como _@ApplicationScoped_.

``` java
    @ApplicationScoped
    public class ExampleSQLFunctionRegister implements SQLFunctionRegister {
      @Override
      public Map<String, SQLFunction> getSQLFunctions() {
        Map<String, SQLFunction> sqlFunctions = new HashMap<>();
        sqlFunctions.put("ad_column_identifier_std", new StandardSQLFunction("ad_column_identifier_std",
            StandardBasicTypes.STRING));
        sqlFunctions.put("now", new StandardSQLFunction("now", StandardBasicTypes.DATE));
        return sqlFunctions;
      }
    }
```

El método _getSQLFunctions()_ debe implementarse proporcionando un mapa con las funciones SQL que se van a registrar. Este mapa se recuperará durante la inicialización de la capa DAL para realizar el registro automáticamente.

Tenga en cuenta que ya hay varias funciones SQL registradas por defecto en el core. Consulte [aquí](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.kernel/src/org/openbravo/client/kernel/KernelSQLFunctionRegister.java){target="\_blank"} y [aquí](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.advpaymentmngt/src/org/openbravo/advpaymentmngt/utility/APRMSQLFunctionRegister.java){target="\_blank"}.
  
Después de registrar la función, puede usarla directamente en un HQL como este:

``` java
    final Session session = OBDal.getInstance().getSession();
    final String qryStr = "select bc.id, ad_column_identifier_std('C_BP_Group', bc.id) from " + Category.ENTITY_NAME + " bc";
    final Query qry = session.createQuery(qryStr);
```
## Ejecutar consultas SQL nativas

La DAL también permite la ejecución de consultas SQL nativas:

``` java
      String documentNo = (String) OBDal.getInstance().getSession()
            .createNativeQuery("SELECT documentNo FROM c_order WHERE c_order_id = :id")
            .setParameter("id", orderId)
            .uniqueResult();
    
    
     
      // retrieving several records with multiple columns
      @SuppressWarnings("unchecked")
      List<Object[]> warehouseInfo = OBDal.getInstance().getSession()
            .createNativeQuery("SELECT name, value FROM m_warehouse WHERE ad_org_id = :id")
            .setParameter("id", orgId)
            .list();
```
!!!note
    El método _createNativeQuery_ acepta un segundo argumento donde se puede especificar el tipo de resultado devuelto. Pero esto NO está soportado debido a un error en Hibernate.
## Modelo en tiempo de ejecución y la API dinámica

La DAL hace que el modelo (definido en el Diccionario de Aplicación) esté disponible en tiempo de ejecución. El modelo en tiempo de ejecución es especialmente útil en funcionalidades genéricas como la importación y exportación y la seguridad y validación.

El modelo en tiempo de ejecución consta de dos conceptos principales:

- [Entidad](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/model/Entity.java){target="\_blank"}: una entidad modela una tabla de base de datos y sus asociaciones hacia y desde otras tablas (es decir, entidades). Una entidad tiene un _Entityname_ que es globalmente único. Además, una entidad tiene una clase Java en tiempo de ejecución que se utiliza para la representación Java en tiempo de ejecución. La clase de entidad tiene métodos para recuperar la lista completa de propiedades, las propiedades ID o las propiedades identificadoras.
- [Propiedad](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/model/Property.java){target="\_blank"}: una propiedad corresponde a una columna en la base de datos. Algunas particularidades de las propiedades:

    - Una propiedad puede ser una propiedad primitiva (String, Date, numérica) o una referencia a otra entidad (que puede recuperarse mediante el método _getTargetEntity_).
    - Una propiedad puede formar parte de la clave primaria ( _isId() == true_ ).
    - Una propiedad puede formar parte del identificador de una entidad ( _isIdentifier() == true_ ).

El modelo en tiempo de ejecución está disponible a través de la clase [ModelProvider](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/base/model/ModelProvider.java){target="\_blank"} (en _org.openbravo.base.model_ ), que puede obtenerse llamando a _ModelProvider.getInstance()_. El ModelProvider ofrece varios métodos para recuperar Entidades del modelo en memoria (la lista completa, por nombre de entidad o por clase Java).

El modelo en tiempo de ejecución hace posible utilizar técnicas de desarrollo guiadas por el modelo también en tiempo de ejecución. Por ejemplo, el modelo en tiempo de ejecución junto con la API dinámica ofrecida por BaseOBObject hace posible iterar por todas las propiedades (y sus valores) de un objeto de negocio sin conocer el tipo exacto de los objetos de negocio.

El ejemplo siguiente ilustra cómo hacerlo. Este método traducirá cualquier entidad de negocio de Etendo Classic a un documento XML simple utilizando el modelo en tiempo de ejecución y la API dinámica:

``` java
      private void printXML(BaseOBObject bob) {
        // used to print a bit nicer xml
        final String indent = "\t ";
        
        // get the entity from the runtime model using the entity name of the object
        final String entityName = bob.getEntityName();
        final Entity e = ModelProvider.getInstance().getEntity(entityName);
        // Note: bob.getEntity() also gives the entity of the object
     
        
        // print the opening tag
        System.err.println("<" + e.getName() + ">");
        
        // iterate through the properties of the entity
        for (Property p : e.getProperties()) {
          
          // and get the value through the dynamic api offered by the BaseOBObject
          final Object value = bob.get(p.getName());
          
          // handle null, just create an empty tag for that
          if (value == null) {
            System.err.println(indent + "<" + p.getName() + "/>");
            continue;
          }
          
          // make a difference between a primitive and a reference type
          if (p.isPrimitive()) {
            // in reality some form of xml conversion/encoding should take place...
            System.err.println(indent + "<" + p.getName() + ">" + value + "</" + p.getName() + ">");
          } else {
            // cast to the parent of all openbravo objects
            final BaseOBObject referencedObject = (BaseOBObject) value;
            // assumes that the id is always a primitive type
            System.err.println(indent + "<" + p.getName() + ">" + referencedObject.getId() + 
    		"</" + p.getName() + ">");
          }
        }
        
        // and the closing tag
        System.err.println("</" + e.getName() + ">");
      }
```

Este ejemplo ejecuta los siguientes pasos:

- Obtener el _entityname_ del objeto y recuperar la Entidad del modelo en tiempo de ejecución a través de la instancia de ModelProvider.
- Crear una etiqueta de apertura e iterar por todas las propiedades de la entidad (es decir, todas las columnas de la tabla).
- Para cada propiedad, hacer lo siguiente:

    1. Obtener el valor de la propiedad desde el objeto de negocio a través de la API dinámica.
    2. Gestionar valores nulos y comprobar si la propiedad es de tipo primitivo o no.
    3. Para un tipo primitivo, simplemente imprimir el valor.
    4. Para un tipo de referencia, convertir el valor a BaseOBObject e imprimir el id del objeto referenciado.

El método anterior imprimirá la siguiente salida para un grupo de terceros como el almacenado en el ejemplo de hello world anterior:

``` xml
    <CoreBPGroup>
    	 <deflt>true</deflt>
    	 <description>hello world</description>
    	 <name>hello world</name>
    	 <value>hello world</value>
    	 <updatedby>1000001</updatedby>
    	 <updated>Sat Oct 04 12:31:57 CEST 2008</updated>
    	 <createdby>1000001</createdby>
    	 <created>Sat Oct 04 12:31:57 CEST 2008</created>
    	 <active>true</active>
    	 <org>1000000</org>
    	 <client>1000000</client>
    	 <id>ff8081811cc769b4011cc769e49b0002</id>
    </CoreBPGroup>
```

En general, cuando esté trabajando con código muy genérico (preocupaciones transversales) que se aplica a todos los objetos de negocio, entonces puede considerarse el uso del modelo en tiempo de ejecución.
##  Testing

Es de vital importancia seguir un enfoque de desarrollo guiado por pruebas para cada proyecto de desarrollo. Esto se aplica especialmente al desarrollo de procesos de backend (algo menos al desarrollo de UI, que es más difícil de probar automáticamente). La Data Access Layer se prueba utilizando muchos casos de prueba JUnit. Estos se pueden encontrar en la carpeta _src-test_ del proyecto Etendo Classic.

Como desarrollador, puede hacer uso de la misma infraestructura de pruebas que los casos de prueba de la Data Access Layer. Lo único que necesita hacer es que su clase de prueba herede de la clase [OBBaseTest](https://github.com/etendosoftware/etendo_core/blob/main/src-test/src/org/openbravo/test/base/OBBaseTest.java){target="\_blank"}. La clase OBBaseTest se encarga de gestionar las transacciones, el contexto y de inicializar la DAL.

Puede elegir ejecutar los casos de prueba para usuarios específicos; consulte los métodos de la clase OBBaseTest para obtener más información.

``` java
      public void testMyStuff() {
       setTestUserContext();
     
        // do your test here
      }
```

Para más información, visite [Cómo desarrollar casos de prueba](../../../developer-guide/etendo-classic/how-to-guides/How_to_create_testcases.md).
##  Pruebe su HQL: la herramienta de consulta HQL

Existe una herramienta de consulta HQL de Etendo que le permite probar una consulta HQL directamente en la interfaz de Etendo Classic. El módulo se puede encontrar en el [repositorio de Github](https://github.com/etendosoftware/org.openbravo.utility.hqlquerytool){target="\_blank"}. 

Este módulo crea una ventana de Administrador del Sistema en la que puede introducir una consulta HQL y ver el resultado. Esta ventana incluye una lista de todas las entidades y sus propiedades. La herramienta de consulta HQL es una herramienta muy útil para probar consultas HQL y para ver el resultado de la consulta.
## Llamada a procesos/procedimientos almacenados desde la DAL

En ocasiones, tiene sentido llamar a un procedimiento almacenado desde la DAL utilizando la misma conexión a la base de datos que está usando la DAL. Para este propósito, la DAL incluye dos clases de utilidad que facilitan la llamada a procesos y procedimientos almacenados a través de la DAL:

- [CallProcess](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/service/db/CallProcess.java){target="\_blank"} 
- [Llamar a procedimiento almacenado](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/service/db/CallStoredProcedure.java){target="\_blank"}

Estas clases utilizan la misma conexión a la base de datos que la DAL; además, en lugar de trabajar con parámetros de tipo `String`, puede trabajar directamente con objetos (primitivos) de Java.

Ambas clases contienen javadoc con una descripción detallada de cómo utilizar la clase.

Otra parte interesante al trabajar con actualizaciones directas en la base de datos (fuera de Hibernate) es la siguiente sección en la guía de troubleshooting: [cambios no visibles en la DAL después de llamar a un procedimiento almacenado](../concepts/common-issues-tips-and-tricks.md#dal-queries-do-not-return-or-do-not-see-changes-in-the-database).
## El DalConnectionProvider

Para acceder y hacer uso del código clásico de Etendo, a menudo es necesario disponer de un objeto `ConnectionProvider`. Al combinar acciones del DAL con operaciones clásicas de Etendo, tiene sentido utilizar una única conexión global a la base de datos y confirmar todas las acciones en un solo paso.

Para dar soporte a esto, el DAL proporciona una implementación especial de `ConnectionProvider` que hace uso de la conexión a base de datos del DAL: el [DalConnectionProvider](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/service/db/DalConnectionProvider.java){target="\_blank"}.
Esta clase es sencilla de usar; consulte el javadoc para más información. La clase puede utilizarse simplemente instanciándola:

``` java
    ConnectionProvider cp = DalConnectionProvider();
```

No se necesita información adicional para que funcione correctamente.
  
Para aquellas consultas que quieran utilizar el pool de solo lectura, el proveedor de conexión debe definirse de la siguiente manera:

``` java 
    ConnectionProvider cp = DalConnectionProvider.getReadOnlyConnectionProvider();
```
## Uso de la Data Access Layer en una tarea Ant

Para facilitar el uso de la DAL en Ant, la DAL ofrece una clase base de tarea Ant: la DalInitializingTask en el paquete _org.openbravo.dal.core_. Esta clase se encarga de inicializar la capa DAL y otros detalles (p. ej., usar el classloader correcto).

Para utilizar esta clase, es necesario realizar los siguientes cambios en la tarea Ant y en la implementación personalizada de la tarea Ant en Java:

- La clase Java de la tarea Ant personalizada debe heredar de _DalInitializatingTask_. 
- La clase Java de la tarea Ant personalizada debe implementar un método _doExecute_ en lugar del método execute en la clase Ant Java personalizada (es suficiente con renombrar el método execute a _doExecute_). 
- Se requieren dos propiedades adicionales en la definición de la tarea ant (en el build.xml):

    - propertiesFile= `${base.config}/Openbravo.properties`. 
    - userId="100". 

La primera propiedad configura la ubicación donde se puede encontrar el archivo _Openbravo.properties_. La segunda propiedad establece el usuario bajo el cual se ejecuta la tarea.
##  Información importante

###  Proxies de Hibernate

Para mejorar el rendimiento de las asociaciones de un solo extremo, la DAL hace uso de la funcionalidad de proxies de Hibernate. La funcionalidad de proxies de Hibernate envuelve un objeto dentro de un objeto proxy de Hibernate. Esto se realiza en tiempo de ejecución usando cglib. El objeto proxy de Hibernate se encarga de cargar el objeto de negocio cuando realmente se accede a él. La ventaja de este enfoque es que, si nunca se accede a un objeto, entonces no se carga, ahorrando rendimiento.

Sin embargo, el proxy de Hibernate es muy visible cuando un desarrollador depura una aplicación, porque la instancia de un objeto en tiempo de ejecución no será la clase exacta (por ejemplo, BPGroup), sino una instancia de una clase proxy de Hibernate.

Para entender cuál es la consecuencia de usar proxies de Hibernate, es esencial que un desarrollador que use la DAL lea [esta parte](https://docs.jboss.org/hibernate/core/3.6/reference/en-US/html/performance.html#performance-fetching-proxies){target="\_blank"} del manual de Hibernate.

###  Rendimiento: obtener el ID de un BaseOBObject

La sección anterior trató el concepto de proxy de Hibernate. Un proxy de Hibernate cargará su objeto de negocio envuelto cuando se llame a uno de los métodos del objeto de negocio. En muchos casos, un desarrollador solo quiere acceder al ID o al nombre de entidad de un objeto. Para evitar la carga del objeto de negocio al recuperar únicamente esta información, la clase DalUtil en _org.openbravo.dal.core_ ofrece un método _getId_ y un método _getEntityName_. Estos métodos trabajan directamente con el objeto HibernateProxy y no cargan el objeto de negocio subyacente.

###  Funcionamiento interno de Hibernate

Para entender cómo opera Hibernate internamente, se recomienda encarecidamente leer el capítulo 21 del manual de Hibernate: [Mejorar el rendimiento](https://docs.jboss.org/hibernate/core/3.6/reference/en-US/html/performance.html){target="\_blank"}.

###  Carga de clases

La DAL carga clases al inicializar la DAL. La DAL, de forma predeterminada, utiliza el cargador de clases de contexto del hilo. En algunos casos, esto no funciona correctamente (por ejemplo, cuando se usa la DAL en Ant). La DAL utiliza la clase OBClassLoader para hacer que el cargador de clases sea configurable. Llamando a _OBClassLoader.setInstance_ con su propio OBClassLoader, puede controlar el cargador de clases utilizado por la DAL.

###  Crear un nuevo objeto de negocio con un ID específico

Hibernate detectará que un objeto de negocio es nuevo cuando:

- el ID del objeto de negocio no está establecido 
- cuando el indicador newOBObject se establece explícitamente en true 

Por lo tanto, si quiere crear un nuevo objeto de negocio con un ID específico (llamando a _setId(...)_), entonces necesita llamar explícitamente a _businessObject.setNewOBObject(true)_. De lo contrario, Hibernate no detectará el objeto de negocio como nuevo y lanzará una excepción ('count of batch update operation....').
##  Prácticas de codificación al usar/ampliar la DAL

Esta sección analiza una serie de prácticas de codificación esenciales que deben seguirse al usar o ampliar la DAL.

###  Estructura de excepciones

Todas las excepciones lanzadas por la DAL extienden la clase base OBException. La OBException es una _RuntimeException_, por lo que no se requieren sentencias explícitas de `catch` y `throw`.

La clase OBException se encarga de registrar la excepción de la forma correcta.

Al crear su propia clase de excepción, es recomendable extender OBException para poder hacer uso de las capacidades estándar de registro en OBException (las capacidades de registro se ampliarán con el tiempo).

###  Invariantes en tiempo de ejecución: la clase Check

La Data Access Layer, en varias ubicaciones, realiza aserciones o comprobaciones de invariantes en tiempo de ejecución. Por ejemplo, para comprobar si los argumentos no son nulos o si se cumple una determinada condición. Implementar este tipo de comprobaciones ayuda a que su sistema sea mucho más robusto. Para que la implementación de este tipo de comprobaciones sea más conveniente, la Data Access Layer utiliza la clase Check, que se encuentra en el paquete _org.openbravo.base.util_. La clase Check ofrece métodos para comprobar _instanceof_, _isNull_, _isNotNull_, etc.

El uso de una clase común para aserciones en todo su código hace que su código sea más legible y más fácil de entender (en comparación con implementar su propia comprobación de aserciones).

###  Formato de código

El código fuente, que forma parte de la Data Access Layer, está formateado utilizando una plantilla de formato. Es esencial que, al desarrollar código en la Data Access Layer o al utilizarla, se use esta misma plantilla de formato de código.

Un formato de código común tiene los siguientes beneficios:

- Todo el código de Etendo Classic obtiene un aspecto uniforme, se ve más limpio/ordenado y, por lo tanto, es más profesional.
- El código será más fácil de entender y se cometerán menos errores.
- Es posible hacer diff de diferentes versiones del código en mercurial (a través de su IDE), y es más fácil entender los cambios a lo largo del tiempo.
- Resolver conflictos de mercurial es más sencillo.

La plantilla de formato de código y su configuración se pueden encontrar en el siguiente artículo: [Formato de código de IntelliJ](../../etendo-classic/getting-started/installation/intellij-code-formatting.md).
## Consejos y trucos y solución de problemas

!!!info
    Para consultar consejos y trucos e incidencias comunes (y sus soluciones) que puede encontrar, visite la sección de [solución de problemas](../../../developer-guide/etendo-classic/concepts/Common_Issues_Tips_and_Tricks.md#data-access-layer).

---

Este trabajo es una obra derivada de [Capa de Acceso a Datos](http://wiki.openbravo.com/wiki/Data_Access_Layer){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.