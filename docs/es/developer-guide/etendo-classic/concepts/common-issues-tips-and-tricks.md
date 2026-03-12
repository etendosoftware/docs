---
title: Problemas comunes, consejos y trucos
tags:
  - Problemas comunes
  - Consejos
  - Trucos
  - Java
  - Javascript

status: beta
---

#  Problemas comunes, consejos y trucos

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
## Visión general

Esta sección de la guía del desarrollador está dedicada a tratar problemas comunes y a responder preguntas frecuentes. Intenta proporcionar consejos y trucos para los obstáculos habituales que se encuentran al desarrollar y ampliar Etendo.
##  Programación del lado del cliente, JavaScript

Esta sección destaca temas específicos relacionados con la programación del lado del cliente en JavaScript.

###  error de JavaScript en el objeto OB: OB undefined

Esto puede ocurrir si el JavaScript que usted ha creado se carga antes que el código JavaScript general de Etendo. Para solucionarlo, debe asegurarse de que su módulo dependa del módulo User Interface Application. En base a esto, el sistema Etendo cargará su JavaScript después del JavaScript base proporcionado por Etendo.

En general, si su módulo depende de JavaScript proporcionado por otros módulos, debe establecer la dependencia correcta en las dependencias del módulo.

###  Usar un linter de JavaScript

Cuando usted desarrolla su propio JavaScript del lado del cliente, es conveniente usar un linter para detectar posibles errores y malas prácticas en su código. Dependiendo de la versión de Etendo utilizada, se usa un linter diferente.

####  Usar ESLint

Etendo utiliza ESLint para comprobar todo el código JavaScript. Para usar este linter, es necesario instalar npm en su máquina y ejecutar `npm ci` en la carpeta raíz de Etendo para instalar todas las herramientas necesarias.

Esta comprobación puede realizarse tanto para el core como para cualquier módulo ejecutando el siguiente script: `modules/org.openbravo.client.kernel/jslint`

###  Depuración de JavaScript

Todo el código JavaScript estático (de todos los módulos) se concatena en un único archivo JavaScript grande que se almacena en el directorio de la aplicación web (en web/js/gen). El nombre del archivo se basa en un hash del contenido (véase la imagen a continuación). Usted puede revisar el contenido del archivo usando el depurador del navegador. Desde ahí, puede depurar su código. En Etendo, usamos Chromium y su depurador la mayor parte del tiempo.

![](../../../assets/developer-guide/etendo-classic/concepts/Common_Issues_Tips_and_Tricks-1.png){:.legacy-image-style}

!!!info
    Al trabajar con código del lado del cliente, es importante aprender a usar el depurador y la consola de Chromium o Firefox. Revise también las pestañas de red de las herramientas de depuración para analizar las solicitudes realizadas por el sistema.

!!!note
    Para ver código no minimizado en el depurador, necesita tener los módulos core/kernel/application en desarrollo.

###  Convenciones de codificación JavaScript

Visite [Convenciones de codificación JavaScript](../concepts/java-coding-conventions.md) para obtener consejos específicos sobre la codificación en JavaScript.

###  API del lado del cliente

Etendo proporciona e implementa varios componentes del lado del cliente para enviar solicitudes al servidor, internacionalización, etc.

###  Smartclient

Etendo utiliza la librería de interfaz de usuario del lado del cliente Smartclient para implementar componentes. Para trabajar y desarrollar en Etendo y crear nuevos widgets, usted necesita entender Smartclient. Consulte estos recursos:

* demo de Smartclient 
* foro de Smartclient 
* referencia de Smartclient 

Puede ser útil tener el código fuente de Smartclient y el material de referencia en su workspace de IntelliJ; así es muy fácil buscar en el código fuente. El código fuente más reciente de Smartclient está disponible en este repositorio: [https://bitbucket.org/koodu_software/org.openbravo.userinterface.smartclient.dev](https://bitbucket.org/koodu_software/org.openbravo.userinterface.smartclient.dev)

###  Trabajar en WebContent

Cuando trabajamos con archivos JavaScript, es habitual trabajar directamente en la carpeta WebContent para comprobar los cambios inmediatamente en el navegador. Después, copiamos nuestros cambios desde WebContent al código fuente para poder enviarlos al repositorio correspondiente. La tarea smartbuild copia el código fuente js en WebContent. Al trabajar directamente en WebContent, podríamos perder nuestros cambios después de ejecutar smartbuild, por lo que sugerimos hacerlo de esta forma:

####  Visual Studio Code

1. Trabajando con VS Code, en su workspace abra VS Code Quick Open (Ctrl+P), pegue el siguiente comando y pulse Enter: `ext installemeraldwalk.RunOnSave`.
2. Abra Show All Commands (Ctrl+Shift+P) y seleccione: `Run On Save: Enable`.
3. Vaya a Manage (icono de Settings) en la esquina inferior izquierda y seleccione `Settings`.
4. En User Settings, despliegue Extensions, seleccione la configuración del comando `Run On Save` y haga clic en `Edit` en `settings.json`.
5. Por último, ponga esto dentro de `settings.json`:
    
    ```
    "emeraldwalk.runonsave": {
            "commands": [
                {
                    "match": "WebContent/web/(?!org.openbravo.userinterface.smartclient|org.openbravo.userinterface.smartclient.dev|userinterface.skin.250to300Comp)",
                    "cmd": "dir=$( echo ${file} | sed -r 's#.*WebContent/web/([^/]+)/.*#\\1#') && file_mod=$(echo ${file} | sed -r 's#WebContent/web/'$dir'/#modules/'$dir'/web/'$dir'/#' ) && cp ${file} $file_mod"
                }
            ]
        }
    ```

Después de seguir estos pasos, si estamos trabajando en WebContent con VSCode, se copiará el archivo que estamos editando en la carpeta correspondiente cuando lo guardemos. Recuerde que la copia se realizará solo cuando guardemos el archivo.
## Weld

### Mi componente no se encuentra

Si su componente no se encuentra, puede que esté dentro del filtro de exclusión definido en el módulo Weld.

### ¿Puedo ejecutar lógica cuando se inicia la aplicación?

Sí, puede consultar [Arquitectura de Etendo](../concepts/etendo-architecture.md#implement-application-initialization-logic) para más información.
##  Capa de Acceso a Datos

###  Funciones SQL en HQL: error «no data type for node»

Visite [Capa de Acceso a Datos](../concepts/data-access-layer.md#sql-functions-in-hql) para obtener información sobre cómo usar funciones SQL en HQL.

###  Advertencia: llamadas desequilibradas a enableAsAdminContext y resetAsAdminContext

Esta advertencia se muestra (junto con un *stacktrace*) cuando la configuración del modo administrador no se realiza correctamente. Visite [esta página](../concepts/data-access-layer.md#administrator-mode) de la guía del desarrollador.

###  Cómo llamar a un procedimiento almacenado/proceso a través de la DAL

Visite [esta página](../how-to-guides/how-to-call-a-stored-procedure-from-the-dal.md) sobre cómo llamar a un proceso a través de la DAL.

###  Cómo leer datos visibles solo desde una Organización específica

El comportamiento por defecto de la DAL (de `OBQuery` y `OBCriteria`) es leer información de todas las organizaciones legibles. Es decir, todas las organizaciones a las que el rol actual tiene acceso. Sin embargo, en ocasiones puede querer leer información que solo es accesible/visible desde una organización específica. El fragmento de código siguiente muestra cómo se puede conseguir:

```
final OBCriteria<PaymentTerm> obc = OBDal.getInstance().createCriteria(PaymentTerm.class);
obc.add(Expression.in("organization.id", OBContext.getOBContext().getOrganizationStructureProvider().getNaturalTree(orgId)));
obc.setFilterOnReadableOrganization(false);
final List<PaymentTerm> pts = obc.list();
```

Este fragmento de código muestra que debe añadir una expresión `in` al `OBCriteria` y, a continuación, deshabilitar el filtrado estándar por organización. Se puede implementar un enfoque similar para `OBQuery`.

###  Cuando al hacer flush/commit de un trigger se lanza una excepción, pero no puedo ver/mostrar el mensaje real del trigger

Hibernate y JDBC envolverán la excepción lanzada por el trigger en otra excepción (la `java.sql.BatchUpdateException`) y, en ocasiones, esta excepción se vuelve a envolver. Además, `java.sql.BatchUpdateException` almacena la excepción subyacente del trigger en `nextException` y no en la propiedad `cause`. El siguiente método puede ayudarle a obtener el mensaje subyacente del trigger:

```
private String getExceptionMessage(Throwable t) {
    if (t.getCause() instanceof BatchUpdateException
        && ((BatchUpdateException) t.getCause()).getNextException() != null) {
        final BatchUpdateException bue = (BatchUpdateException) t.getCause();
        return bue.getNextException().getMessage();
    }
    return t.getMessage();
}
```

!!!info
    La API de Etendo proporciona un método llamado `getUnderlyingSQLException()` en la clase `DbUtility` que ya realiza estas comprobaciones y también cubre otros casos.

###  Pruebe su HQL: la herramienta de Consulta HQL

Etendo contiene un módulo que ofrece una herramienta de consultas que le permite probar una **Consulta HQL** directamente en la interfaz de Etendo. La [herramienta de Consulta HQL](https://github.com/etendosoftware/org.openbravo.utility.hqlquerytool) también está disponible a través del repositorio de Etendo.

###  ¿Cómo puedo ver qué SQL se ejecuta?

Para ver las consultas SQL lanzadas por Hibernate, debe establecerse la siguiente propiedad de log4j en `WEB-INF/log4j2-web.xml` o en `config/log4j2-web.xml`:

```
<Loggers>
    ...
    <Logger name="org.hibernate.SQL" level="debug"/>
    ...
</Loggers>
```

Para ver el *binding* de valores a los parámetros de la consulta, establezca esta propiedad:

```
<Loggers>
    ...
    <Logger name="org.hibernate.type" level="debug"/>
    ...
</Loggers>
```

Si no le funciona, es posible que el archivo log4j.properties se esté leyendo desde otra ubicación distinta de la que espera. Para ver desde dónde lee log4j sus propiedades, establezca este parámetro de la JVM: `-Dlog4j2.debug=true`

###  Mi consulta no devuelve mi objeto recién creado

Esto puede ocurrir cuando no establece explícitamente la propiedad `active` a `true` en el nuevo objeto de negocio.

Las clases principales de consulta de Etendo (`OBCriteria` y `OBQuery`) añaden automáticamente distintos criterios de filtrado. Uno de los criterios de filtrado es la propiedad `active`. Por defecto, las clases de consulta solo devolverán objetos con `active` a `true` (o 'Y' en la base de datos).

Al crear un objeto de negocio, la propiedad `active` debe establecerse explícitamente a `true` (`setActive(true)`). Esto garantiza que el filtro de activos no lo omita en las consultas.

###  Mi consulta no devuelve nada

Hay casos en los que Hibernate realizará un *inner-join* al ejecutar una consulta. Si no hay datos relacionados en la tabla unida, entonces la consulta completa no devolverá nada.

Como ejemplo, tome la siguiente consulta:

`SELECT p.id, p.image FROM Product AS p`

Esta consulta parece bastante simple. Sin embargo, en realidad la imagen es un objeto persistido por separado y una referencia *any-to-one* desde el producto a la tabla de imágenes. Por tanto, esta consulta da como resultado un *inner-join* con la tabla de imágenes. En este caso, esa tabla estaba vacía y no se devolvió nada.

Para resolver este problema, la imagen debe unirse mediante un *outer join*:

`SELECT p.id, p.image FROM Product AS p LEFT OUTER JOIN p.image`

###  not-null property references a null or transient value: *.creationDate

Esta excepción se lanza cuando intenta guardar un nuevo objeto de negocio con su Id establecido. Tiene sentido establecer un id si quiere controlar la asignación del id (y no dejar que Hibernate cree uno por usted). Sin embargo, si el id está establecido, entonces Hibernate/Etendo pensará que es un objeto existente y no establecerá las propiedades de auditoría.

Para resolverlo, llame también a `setNewOBObject(true)` en el nuevo objeto de negocio. Esto indica a Etendo que el objeto es nuevo aunque su id esté establecido.

###  not-null property references a null or transient value: *.updated

El mismo problema que el anterior.

###  org.hibernate.TransientObjectException: object references an unsaved transient instance - save the transient instance before flushing

Esta excepción ocurre cuando guarda un objeto que hace referencia a otro objeto que todavía no se ha guardado. Se aplica a las denominadas referencias *many-to-one*, por ejemplo de Pedido a Moneda (muchos pedidos usan la misma moneda). Etendo mapea las asociaciones *many-to-one* sin *cascading*. Esto es por motivos de rendimiento.

Para evitar esta excepción, guarde la instancia referenciada antes que la instancia que referencia.

Tenga en cuenta que, en la práctica, esta excepción no ocurre tan a menudo, ya que la mayoría de referencias son desde datos transaccionales a datos maestros, y los datos maestros se configuran tradicionalmente antes de crear datos transaccionales.

Los procesos de importación de datos/servicios web REST se encargan de persistir los objetos en el orden correcto, por lo que esta excepción no se produce al importar datos mediante estos procesos.

###  Rendimiento: obtener el id de un BaseOBObject

Para mejorar el rendimiento de asociaciones de un solo extremo, la DAL hace uso de la funcionalidad de *proxy* de Hibernate. Esta funcionalidad envuelve un objeto dentro de un objeto *proxy* de Hibernate (cglib). El *proxy* de Hibernate se encarga de cargar el objeto de negocio cuando realmente se accede a él y no antes.

En muchos casos, un desarrollador solo quiere acceder al id o al `entityname` de un objeto. Para evitar la carga del objeto de negocio al recuperar solo esta información, la clase `DalUtil` en `org.openbravo.dal.core` ofrece un método `getId` y un método `getEntityName`. Estos métodos trabajan directamente con el objeto `HibernateProxy` y no cargan el objeto de negocio subyacente.

###  Carga de clases

La DAL carga clases al inicializarse. Por defecto, la DAL utiliza el *context class loader* del hilo. En algunos casos esto no funciona correctamente (por ejemplo, al usar la DAL en Ant). La DAL utiliza la clase `OBClassLoader` para hacer configurable el *classloader*. Llamando a `OBClassLoader.setInstance` con su propio `OBClassLoader`, puede controlar el cargador de clases usado por la DAL.

###  NPE al llamar a un getter de un objeto de negocio

Todos los getters de los objetos de negocio de Etendo devuelven un `Object`. Esto también aplica a propiedades de tipo primitivo. De este modo, Etendo puede soportar valores nulos en la base de datos (lo que dará como resultado un valor nulo para la propiedad). Sin embargo, los valores nulos provocan NPE cuando se usan directamente en expresiones. Por ejemplo, tome este código:

```
SystemInformation sys = OBDal.getInstance().get(SystemInformation.class, "0");
return sys.isEnableHeartbeat();
```

Cuando el valor de `enableHeartbeat` es nulo en la base de datos, la llamada a `isEnableHeartbeat` dará como resultado un NPE aunque la variable `sys` esté establecida correctamente.

Lo mismo ocurrirá al usar directamente resultados de llamadas a getters en expresiones numéricas.

###  Las consultas DAL no devuelven o no ven cambios en la base de datos

Esto puede ocurrir en la siguiente situación:

1. su programa lee objetos de la base de datos usando la DAL
2. después actualiza la base de datos directamente sin pasar por la DAL (ya sea mediante SQL directo o mediante un procedimiento almacenado); la base de datos actualiza los objetos/datos que usted leyó a través de la DAL en el paso 1
3. después su programa usa los mismos objetos leídos en el paso 1 o los vuelve a leer desde la base de datos

El problema que encontrará entonces es que los objetos no reflejan el estado de la base de datos (no están actualizados). Esto se debe a lo siguiente:

Cuando Hibernate lee datos de la base de datos, se almacenan en una caché para esa sesión. Esta caché de sesión no se actualiza automáticamente cuando los datos cambian en la base de datos fuera de su sesión de Hibernate. Por tanto, cuando en el último paso vuelve a leer los objetos desde la base de datos, obtiene los objetos desde la caché de sesión y no desde la base de datos.

Hay 2 soluciones:

1. limpiar completamente la caché de sesión

    ```
    OBDal.getInstance().getSession().flush();
    OBDal.getInstance().getSession().clear();
    ```

2. forzar la relectura de objetos específicos

    ```
    OBDal.getInstance().getSession().refresh(myObject);
    ```

El primer enfoque tiene sentido si hay muchas actualizaciones en la base de datos o si no sabe exactamente qué objetos han cambiado. El segundo enfoque tiene sentido si sabe exactamente qué objeto(s) han cambiado y no son demasiados.

En el caso de la primera solución, debe tener en cuenta que los objetos que se hayan leído (a través de la DAL) antes de hacer flush/clear ya no se pueden usar después de flush/clear. Estos objetos deben volver a adjuntarse a la sesión o leerse completamente de nuevo desde la base de datos:

```
    // reattach an object from the database, only if it is not already part of it
    if (OBDal.getInstance().getSession().contains(myObject)) {
          OBDal.getInstance().getSession().lock(myObject.getEntity().getName(), myObject, LockMode.NONE);
    }
    // or reread it again, this example assumes that the object 
    // is a Business Partner
    BusinessPartner businessPartner = OBDal.getInstance().get(BusinessPartner.class, myPreviouslyReadBP.getId());
```

Al elegir la estrategia de **bloqueo** es importante seleccionar el orden de bloqueo correcto. Primero bloquee los objetos que son usados por los otros objetos.

###  ERROR org.hibernate.LazyInitializationException - could not initialize proxy - no Session

Hibernate cargará de forma diferida los objetos a los que se hace referencia desde otros objetos. Por tanto, cuando un objeto A referencia a un objeto B, al leer A desde la base de datos, Hibernate creará un denominado objeto *proxy* B, que es usado por A. El objeto *proxy* B no se inicializa (sus datos no se establecen); esta inicialización se realiza cuando se accede directamente a B (por ejemplo, llamando a un método). Para realizar esta inicialización, Hibernate necesita la sesión original de Hibernate que se usó para leer A y crear el *proxy* B.

La `LazyInitializationException` ocurre cuando esta sesión ya no es válida. Esto sucede, por ejemplo, cuando se llama a `OBDal.getInstance().commitAndClose()`, lo que cerrará y eliminará la sesión. Si se accede a un objeto *proxy* no inicializado después de la llamada a `commitAndClose`, se lanza esta excepción.

Para evitarlo, asegúrese de que todos los objetos que necesita después de `commitAndClose` están inicializados. Esto puede hacerse usando la llamada `Hibernate.initialize(object)` o llamando a un método arbitrario del objeto (por ejemplo, `getIdentifier()`).
##  Servicios web REST

###  Estoy obteniendo: 'Caused by: Object Entity(null) is new but not writable'

El servicio web REST utiliza el **rol, cliente y organización por defecto** del usuario. El error `Caused by: Object Order(null) is new but not writable` se debe a que el rol o la organización del usuario no permiten escribir/crear la entidad que está pasando.

###  Mi servicio web REST no devuelve nada

Si su servicio web REST solo devuelve esto: `<ob:Openbravo/>`

Entonces, la mayoría de las veces el usuario que utilizó para iniciar sesión no está autorizado a ver la información solicitada. Otro motivo para no ver información es que el sistema añadirá automáticamente el filtrado por cliente y organización a la consulta REST y solo mostrará objetos que tengan active==true.

###  Uso del esquema XML de REST para generar código de (de-)serialización

El esquema XML de REST puede utilizarse para generar código Java o C# que puede usarse para (de-)serializar el contenido XML de REST de forma segura en cuanto a tipos. Algo a tener en cuenta es que los elementos de tipo primitivo (como un nombre o una descripción) tienen atributos definidos en el esquema XML. Esto significa que los generadores de código no crearán un miembro/accesor de tipo String (u otro tipo primitivo), sino que en su lugar utilizarán un tipo generado independiente para encapsular el valor del tipo primitivo. Este tipo generado por separado también contiene los otros atributos.

###  Complemento de Firefox: Poster, para probar servicios web

Para facilitar las pruebas de servicios web, Firefox dispone de un buen complemento: Poster. Este complemento le permite hacer POST/PUT de XML a una URL y realizar solicitudes GET y DELETE.

###  Estoy obteniendo: 'message: "OBUIAPP_ActionNotAllowed" type: "user"'

Debe añadir la tabla que está intentando editar al perfil de usuario en `Role Access` > `Table Access`.
##  Modelo de datos del Diccionario de la Aplicación

###  Uso de referencias de Selector para no mostrar un desplegable en campos no editables

Para la referencia completa sobre la referencia Selector, lea la sección Selector en el documento [Modelo de datos](../concepts/data-model.md).

Una referencia **Selector** no muestra una lista desplegable, sino únicamente un cuadro de texto con el valor seleccionado y un botón a su lado para invocar el selector. Cuando el campo no es escribible, el botón no se muestra y solo aparece el cuadro de texto.

Si se sabe que una columna se utiliza siempre en campos no editables y sigue la regla de nomenclatura definida para las referencias **TableDir**, es una buena práctica no configurarla como referencia **TableDir**, sino como **Selector**; en este caso no es necesario configurar el campo **Referencia clave**. Al hacerlo, la página generada será más ligera porque, en lugar de generar una lista desplegable con todos los elementos, solo generará un cuadro de texto.

###  Sintaxis del Diccionario de la Aplicación

El Diccionario de la Aplicación contiene muchos ejemplos de sintaxis de **Lógica del valor por defecto**, **Lógica para mostrar**, **lógicas de solo lectura** y **validaciones**. Simplemente consulte su base de datos para averiguar cómo están definidas (puede ejecutar estas consultas dentro de Etendo, iniciando sesión con un usuario con el rol de **Administrador del sistema** dentro de **Diccionario de la Aplicación** > **Mantenimiento** > **Consulta SQL**). Encuentre más información sobre Expresiones dinámicas [aquí](../concepts/dynamic-expressions.md)

####  Lógica del valor por defecto
    
``` 
SELECT t.name AS table_name, c.name AS column_name, c.defaultvalue AS default_value
FROM ad_table t, ad_column c  
WHERE c.defaultvalue IS NOT NULL
--AND c.defaultvalue like '%+%'
--AND c.defaultvalue like '%SQL%'
AND c.ad_table_id = t.ad_table_id
ORDER BY t.name, c.name;
```

####  Lógica para mostrar
    
```
SELECT w.name AS window, t.name AS tab, f.name AS FIELD, f.displaylogic AS display_logic  
FROM ad_window w, ad_tab t, ad_field f
WHERE f.displaylogic IS NOT NULL
AND w.ad_window_id = t.ad_window_id
AND t.ad_tab_id = f.ad_tab_id
ORDER BY w.name, t.name, f.name;
```

**Ejemplo 1** Si desea restringir el acceso a una solapa hija en función del valor de un campo de su solapa padre, debe:

1. Marcar la columna del campo dentro de la solapa padre como _Atributo sesión_. 
2. Añadir a todos los campos de la solapa hija una lógica para mostrar con el formato @Father_Column_Name@ = 'Value' 

Vea, por ejemplo, cómo se hace en **Gestión de Datos Maestros** > **Configuración de productos** > **Atributo** > **Atributo** > **Valor atributo** al desmarcar la casilla **Lista** en la solapa **Atributo**, consultando:
    
```
SELECT w.name AS window, t.name AS tab, f.name AS FIELD, f.displaylogic AS display_logic 
FROM ad_window w, ad_tab t, ad_field f
WHERE f.displaylogic IS NOT NULL
AND w.ad_window_id = t.ad_window_id
AND t.ad_tab_id = f.ad_tab_id
AND UPPER(t.name) LIKE '%ATTRIBUTE VALUE%'
ORDER BY w.name, t.name, f.name;
```

  
####  Lógicas de solo lectura  
    
```
SELECT t.name AS table_name, c.name AS column_name, c.readonlylogic AS read_only_logic
FROM ad_table t, ad_column c  
WHERE c.readonlylogic IS NOT NULL  
AND c.ad_table_id = t.ad_table_id
ORDER BY t.name, t.name;
```

####  Validación

```
SELECT t.name AS table_name, c.name AS column_name, vr.code AS validation_rule  
FROM ad_val_rule vr, ad_table t, ad_column c  
WHERE c.ad_val_rule_id = vr.ad_val_rule_id  
AND c.ad_table_id = t.ad_table_id
ORDER BY t.name, c.name;
```

---

Este trabajo es una obra derivada de [Problemas comunes, consejos y trucos](http://wiki.openbravo.com/wiki/Common_Issues_Tips_and_Tricks){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.