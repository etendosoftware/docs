---
title: Arquitectura de Etendo
tags:
    - Etendo
    - Arquitectura
    - Componentes
    - Weld

status: beta
---

# Arquitectura de Etendo

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
## Visión general

En Etendo, el sistema se aleja de una arquitectura clásica de servlets para pasar a una arquitectura de **Rich Internet Application (RIA)**. Se trata de un cambio de paradigma radical que da como resultado una interfaz de usuario mucho más dinámica y versátil. En una arquitectura RIA, las solicitudes de datos y las solicitudes de la página/interfaz de usuario están separadas. La página/interfaz de usuario se carga en el cliente una vez y luego se reutiliza mientras el usuario trabaja en la aplicación. En cambio, las solicitudes de datos y acciones se ejecutan de forma continua.

![](../../../assets/developer-guide/etendo-classic/concepts/etendo-architecture/etendo-architecture.png)

La arquitectura de Etendo se implementa utilizando Etendo Core y varios módulos relacionados:

- El módulo JSON proporciona el [servicio web JSON REST](../concepts/json-rest-web-services.md); se utiliza para la comunicación de datos cliente-servidor.
- El módulo [Weld](#introducing-weld-dependency-injection-and-more) proporciona inyección de dependencias y gestión de componentes.
- El módulo Kernel se encarga de tareas de infraestructura como el procesamiento de solicitudes, la gestión de eventos y la [compresión y caché](#etags-caching-and-compressing).
- El módulo DataSource utiliza el módulo JSON y proporciona funcionalidad de solicitud de datos de nivel superior para consultas y acciones relacionadas con los datos.
- El módulo Smartclient proporciona la biblioteca de interfaz de usuario [Smartclient](https://smartclient.com/){target="\_blank"}.
- El módulo de aplicación contiene la implementación de la barra de navegación, rejillas y formularios, y otro código del lado del cliente y del servidor orientado a la aplicación.

![](../../../assets/developer-guide/etendo-classic/concepts/etendo-architecture-1.png)
  
Esta sección explica los conceptos implementados por estos módulos.
##  Conceptos principales: Componente y Proveedor de componentes

Esta sección presenta conceptos centrales de la interfaz de usuario de Etendo. La interfaz de usuario de Etendo se implementa mediante los llamados **componentes**. Un **componente** es una parte específica de la interfaz de usuario. Puede ser un selector, un campo en un formulario, pero también un diseño completo, o un formulario o una cuadrícula.

Los componentes se implementan en módulos. Un módulo tiene total libertad sobre cómo implementar componentes (si existe una tabla de ventana, una tabla de cuadrícula o una tabla de vista genérica, etc.). Los componentes dentro de un módulo son gestionados por un **Proveedor de componentes**, que es responsable de crear un componente y proporcionarlo al kernel de Etendo. Un proveedor de componentes también es responsable de registrar el contenido estático en Etendo; esto se explica con más detalle a continuación.

Un componente puede recuperarse mediante una URL (una **solicitud de componente**). Por ejemplo, esta URL recuperará el javascript de la ventana de factura de ventas:

`http://localhost:8080/etendo/org.openbravo.client.kernel/OBUIAPP_MainLayout/View?viewId=_167`

Para explicar la estructura de esta URL, OBUIAPP_MainLayout identifica el módulo de la aplicación cliente. El `ComponentProvider` de ese módulo sabe cómo gestionar la última parte de la URL: View?viewId=_167. Creará un `StandardWindowComponent` que obtiene el `viewId` (el id de `ADWindow`) para generar el javascript. El javascript generado se posprocesa (compresión, comprobación de sintaxis) antes de enviarse al cliente.

La siguiente imagen ilustra el procesamiento del flujo de solicitudes con más detalle:

![](../../../assets/developer-guide/etendo-classic/concepts/etendo-architecture-2.png)

El flujo general de solicitud y generación funciona de la siguiente manera:

1. el módulo Client Kernel recibe una solicitud de componente (con un tipo de componente y un ID) (en el KernelServlet).
2. en función del tipo de componente, el módulo kernel encuentra el módulo responsable de gestionar el componente solicitado; a continuación, se llama a ese módulo para crear el componente usando el ID del componente.
3. el módulo lee la definición del componente desde tablas u otras fuentes e instancia la instancia de Component.
4. se llama al componente para generar su representación del lado del cliente.
5. si es un componente basado en plantilla (es decir, tiene una plantilla específica), entonces el componente llama a un procesador de plantillas para la plantilla.
6. la vista se genera usando la plantilla o ejecutando código Java que genera un String (javascript).
7. el Resultado (a menudo una cadena javascript) se devuelve al módulo Client Kernel.
8. el módulo Client Kernel comprime el Resultado usando [jsmin](https://www.crockford.com/jsmin.html){target="\_blank"}.

!!!note
    El módulo Client Kernel también se encarga del almacenamiento en caché de componentes y de las solicitudes de componente. Esto se trata con más detalle en una sección posterior de esta documentación.
## Introducción a Weld: inyección de dependencias y más

Weld implementa la [JSR-299](https://jcp.org/en/jsr/detail?id=299){target="\_blank"}: Contextos e Inyección de Dependencias de Java para la plataforma Java EE (CDI). CDI es el estándar de Java para la inyección de dependencias y la gestión contextual del ciclo de vida. Para información general sobre los conceptos de inyección de dependencias, visite [esta página](https://en.wikipedia.org/wiki/Dependency_injection){target="\_blank"}.

Para más información, visite [Weld](https://weld.cdi-spec.org/documentation/){target="\_blank"}.

Las partes principales de la arquitectura de Etendo usan Weld para la inyección de dependencias, la definición de componentes y los eventos de entidades de negocio. El punto de partida es definir los componentes y el ámbito en el que viven. El siguiente paso es usar estos componentes inyectándolos en otros componentes. Tenga en cuenta que, para hacer uso de la inyección de dependencias de Weld, no es posible crear objetos usando la palabra clave clásica `new` de Java. Consulte una sección posterior más abajo sobre este tema.

!!!note
    Etendo soporta **CDI 2.0** ya que Weld se actualizó a la versión **3.1.0**. CDI 2.0 es la especificación [JSR-365](https://jcp.org/en/jsr/detail?id=365){target="\_blank"}.
  

### Definición de ámbito

Con Weld es posible definir componentes que están disponibles en distintos niveles: `ApplicationScoped`, `SessionScoped` y `RequestScoped`. Para cada uno de estos ámbitos se pueden encontrar ejemplos en el código fuente de Etendo. El ámbito se define usando una anotación:
    
    @ApplicationScoped
    @ComponentProvider.Qualifier(ExampleComponentProvider.EXAMPLE_VIEW_COMPONENT_TYPE)
    public class ExampleComponentProvider extends BaseComponentProvider {
    ...
    }
     
    @SessionScoped
    public class MenuManager implements Serializable {
    ....
    }

!!!note
    La anotación anterior para `ComponentProvider` es una anotación específica de Etendo utilizada para registrar `ComponentProvider` globalmente usando una cadena única. Consulte la sección sobre `ComponentProviders` para más información.

### Herencia de ámbito

En lo relativo a la herencia de anotaciones de ámbito, Weld sigue el comportamiento esperado descrito en la [especificación de CDI 2.0](https://docs.jboss.org/cdi/spec/2.0/cdi-spec.html#inheritance){target="\_blank"}.

Suponga que una clase **X** es extendida directa o indirectamente por otra clase **Y**. Si X está anotada con un tipo de ámbito **Z**, entonces Y hereda la anotación si y solo si Z declara la meta-anotación **` @Inherited `** y ni Y ni ninguna clase intermedia que sea una subclase de X y una superclase de Y declara un tipo de ámbito. Tenga en cuenta que este comportamiento es diferente de lo definido en la Especificación del Lenguaje Java.

Por lo tanto, como todas las anotaciones **`@ApplicationScoped`**, **`@SessionScoped`** y **`@RequestScoped`** declaran la meta-anotación `@Inherited`, una subclase hereda el ámbito de su clase padre si ni la subclase ni ninguna clase intermedia declara otro ámbito.

Este comportamiento no se aplica a aquellas clases que implementan una interfaz con un ámbito particular: si una interfaz declara un ámbito, no es heredado por las clases que implementan esa interfaz.

### Inyección

Los componentes definidos pueden inyectarse automáticamente en otros componentes usando **puntos de inyección**, que se definen mediante la anotación `@Inject`:

```
@Inject
private MenuManager menuManager;
```

**Reglas de asignabilidad**
  
CDI 2.0 define en qué circunstancias funciona la asignabilidad de tipos sin parametrizar y parametrizados dentro de un punto de inyección. Esto se especifica con un conjunto de reglas definidas [aquí](https://docs.jboss.org/cdi/spec/2.0/cdi-spec.html#assignable_parameters){target="\_blank"}.

A partir de cualquier versión de Etendo, necesitamos usar [comodines](https://docs.oracle.com/javase/tutorial/extra/generics/wildcards.html){target="\_blank"} para definir el punto de inyección con el fin de cumplir las reglas de asignabilidad:

```
public class BaseGenerator {
 
    @Inject
    @Any
    private Instance<DocGenerator<? extends BaseOBObject>> docGenerators;
 
    ...
}
```

### Instanciación de objetos habilitados para Weld

Weld necesita poder inyectar componentes en objetos recién instanciados. Esto significa que no es posible crear objetos usando la palabra clave `new` de Java. A menudo no necesita crear objetos directamente; deberían inyectarse. Pero, en algunos casos específicos, no es posible usar inyección porque su propio objeto se crea de una forma ajena a Weld. Para estos casos, Etendo dispone de un método de utilidad para ayudarle:

```
org.openbravo.base.weld.WeldUtils.getInstanceFromStaticBeanManager(Class<T> type);
```

La instancia creada se integrará con Weld y podrá hacer uso de sus capacidades de inyección de dependencias; además, se tiene en cuenta el ámbito definido para el componente. Por tanto, al invocar el método anterior para un componente `ApplicationScoped`, siempre se devuelve la misma instancia única.

### Análisis del classpath

Weld analizará el classpath para encontrar componentes que tengan anotaciones específicas.

De forma predeterminada, Weld busca en todos los archivos de clase en `WEB-INF/classes`, pero, por defecto, los archivos jar en `WEB-INF/lib` se excluyen de esta búsqueda. Consulte [aquí](https://docs.jboss.org/weld/reference/latest/en-US/html/ee.html#packaging-and-deployment){target="\_blank"} (capítulo Packaging and Deployment de la documentación de Weld) cómo crear un archivo jar que sea buscado por Weld.

Etendo Weld también excluirá clases específicas de `WEB-INF/classes`. Para evitar buscar en todas las clases, se han especificado filtros de exclusión concretos. Se pueden encontrar en el archivo `config/beans.xml` del módulo Weld. Las clases capturadas por el filtro de exclusión no se considerarán componentes y no serán encontradas por Etendo/Weld.

### Módulo Weld para desarrolladores
  
El [**Modo de desarrollo de Weld**](https://docs.jboss.org/weld/reference/3.1.7.SP1/en-US/html_single/#devmode){target="\_blank"} es un modo especial que proporciona varias herramientas integradas adecuadas para fines de desarrollo y pruebas. De forma predeterminada, este modo está deshabilitado. [Probe](https://docs.jboss.org/weld/reference/3.1.7.SP1/en-US/html_single/#probe){target="\_blank"} de Weld es una de estas herramientas.

El módulo `org.openbravo.base.weld.dev` puede utilizarse para habilitar el Modo de desarrollo. Este módulo **nunca** debe utilizarse en **entornos productivos** porque puede tener un impacto negativo en el rendimiento.
##  ETags, caché y compresión

Para mejorar la experiencia de usuario y el rendimiento, es importante hacer uso de la funcionalidad de caché en el navegador, así como en el servidor. Para el uso de caché, se puede distinguir entre componentes y archivos js estáticos. Los componentes se generan en base a definiciones en la base de datos y pueden contener cadenas específicas de idioma. Los archivos js estáticos definen widgets de JavaScript que son reutilizados por los componentes.

Etendo implementa varios tipos de caché en diferentes capas de la aplicación para optimizar la experiencia de usuario. Aprovecha la funcionalidad de modularidad, lo que significa que Etendo distingue entre una situación en la que un módulo está en desarrollo o no. Para un módulo en desarrollo, tiene sentido evitar la caché, ya que un consultor que cambia la interfaz de usuario quiere obtener feedback inmediato. Para un módulo que no está en desarrollo, tiene sentido maximizar la caché, ya que esto mejora la experiencia de usuario. Cuando un módulo no está en desarrollo, entonces se utiliza la versión del módulo para refrescar automáticamente la caché del cliente.

###  Caché y refresco de archivos js estáticos

Un archivo js estático contiene una librería o un widget estándar que es utilizado por los componentes. El enlace a un archivo js estático se crea cuando la aplicación se inicia y se genera en la parte superior de la página.

Los archivos js estáticos normalmente se almacenan en caché en el navegador. Sin embargo, los archivos js estáticos pueden cambiar durante actualizaciones de módulos o durante el desarrollo.

Esto se implementa de la siguiente manera. Los archivos js estáticos (es decir, recursos globales) son proporcionados por los módulos. Un módulo publica sus recursos estáticos a través de un `ComponentProvider`. La API de un `ComponentProvider` contiene un método `getGlobalResources`. Etendo concatena todos los recursos estáticos en un único archivo js grande. El orden de concatenación se basa en las relaciones de dependencia entre los módulos. El nombre del archivo js se basa en un guid (por ejemplo: `088afd247a8fe06c91a654891a1358a2.js`). Este guid, a su vez, se basa en el contenido del archivo, de modo que si el JavaScript cambia, entonces también cambia el nombre del archivo js (y por tanto se vuelve a cargar en el navegador). El archivo js se genera en la carpeta web/js/gen y se sirve desde ahí al cliente.

!!!note
    El archivo JavaScript concatenado no se comprimirá si los módulos core, `client.kernel` y `client.application` están en desarrollo. Esto facilita la depuración del lado del cliente.

###  Caché y refresco de componentes

Los componentes se consideran dinámicos y contienen datos de ejecución leídos de bases de datos. Los componentes se generan bajo demanda y se almacenan en caché en el servidor. El lado servidor puede validar si un componente ha cambiado desde la última solicitud. Esta validación no es posible en el cliente, ya que los datos en el servidor pueden haber cambiado.

Para soportar el concepto de caducidad de la caché del lado servidor, el Client Kernel hace uso del concepto de ETag. Un [ETag](https://www.infoq.com/articles/etags/){target="\_blank"} es como un código hash que se utiliza para determinar si el contenido ha cambiado desde la última vez que el navegador lo solicitó. La implementación de `BaseComponent` genera ETags de dos maneras:

* si el módulo del componente no está en desarrollo, entonces el ETag es: la concatenación del idioma del usuario y la versión del módulo
* si el módulo del componente está en desarrollo, entonces el ETag es: la concatenación del idioma del usuario y una marca de tiempo en milisegundos

Esto da el mismo resultado que con el contenido estático: si un módulo no está en desarrollo, el código del lado cliente solo se refresca cuando se actualiza un módulo; cuando un módulo está en desarrollo, el código del lado cliente no se almacena en caché. Este último comportamiento es muy deseable al cambiar definiciones de componentes (añadir columnas, renombrar campos, etc.), ya que el sistema no necesita reiniciarse ni vaciar la caché del navegador para ver los resultados.

La lógica de generación de ETag se puede sobrescribir en una implementación específica de Component.

!!!note
    Un Component puede contener otros componentes proporcionados por otros módulos. La generación del ETag solo tiene en cuenta el estado de en desarrollo del módulo del Component raíz.

###  Compresión y comprobación de sintaxis
  
La salida generada por un módulo se puede comprimir y comprobar sintácticamente. Para la compresión, se utiliza [jsmin](https://www.crockford.com/jsmin.html){target="\_blank"}. Para la comprobación de sintaxis, Etendo hace uso de [JSLint](https://www.jslint.com/){target="\_blank"} y [JSLint4Java](https://code.google.com/archive/p/jslint4java/){target="\_blank"}. La compresión/comprobación de sintaxis se realiza en función del estado en desarrollo de un módulo:

* Si un módulo está en desarrollo, entonces la salida de sus componentes se comprueba sintácticamente, pero no se comprime (para mejorar la legibilidad para un desarrollador en el navegador).
* Si un módulo no está en desarrollo, entonces la salida no se comprueba sintácticamente, pero sí se comprime (para mejorar el rendimiento para los usuarios finales).

###  Información sobre la caché HTTP y los ETags

* [http://www.infoq.com/articles/etags](http://www.infoq.com/articles/etags){target="\_blank"} 
* [http://www.oreillynet.com/onjava/blog/2004/07/optimizing_http_downloads_in_j.html](http://www.oreillynet.com/onjava/blog/2004/07/optimizing_http_downloads_in_j.html){target="\_blank"} 
* [http://www.xml.com/pub/a/2006/02/01/doing-http-caching-right-introducing-httplib2.html ](http://www.xml.com/pub/a/2006/02/01/doing-http-caching-right-introducing-httplib2.html ){target="\_blank"}
* [http://bitworking.org/news/150/REST-Tip-Deep-etags-give-you-more-benefits](http://bitworking.org/news/150/REST-Tip-Deep-etags-give-you-more-benefits){target="\_blank"} 
* [http://blogs.atlassian.com/developer/2007/12/cachecontrol_nostore_considere.html](http://blogs.atlassian.com/developer/2007/12/cachecontrol_nostore_considere.html){target="\_blank"}
* [http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13](http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13){target="\_blank"}
## Estructura estándar de un módulo

Un módulo que implemente funcionalidad en la arquitectura de Etendo debe seguir una estructura fija. La imagen siguiente refleja la estructura estándar:

* el código fuente Java y las plantillas se encuentran en el directorio `src`
* el JavaScript estático debe ubicarse en este subdirectorio: `web/<modulepackage>/js`
* los artefactos de estilo (imágenes, CSS y JavaScript) deben ubicarse en este subdirectorio: `web/org.openbravo.userinterface.smartclient/3.00/<modulepackage>`
* las pruebas unitarias de JavaScript deben ubicarse en el directorio `web-test`.

Siguiendo esta estructura, los archivos se copiarán en la ubicación correcta durante los pasos principales de compilación.

![](../../../assets/developer-guide/etendo-classic/concepts/etendo-architecture-7.png)
##  Proveedor de componentes

Cada módulo necesita implementar un proveedor de componentes. Un proveedor de componentes se encarga de las siguientes tareas:

* Crea los componentes del módulo bajo petición del kernel de Etendo. 
* Registra los recursos estáticos del módulo en el kernel de Etendo. 

Un `ComponentProvider` es un componente de Weld y tiene una estructura estándar que se explica aquí.

La clase Java `ComponentProvider` debe tener 2 anotaciones:

* `@ApplicationScoped` indicando este componente como un singleton 
* `@ComponentProvider.Qualifier` registra el nombre identificativo de este componente; debe ser único, por lo que preferiblemente use el dbprefix del módulo. 

```
@ApplicationScoped
@ComponentProvider.Qualifier(ExampleComponentProvider.EXAMPLE_VIEW_COMPONENT_TYPE)
public class ExampleComponentProvider extends BaseComponentProvider {
    public static final String EXAMPLE_VIEW_COMPONENT_TYPE = "OBEXAPP_ExampleViewType";
```

!!!note
    El proveedor de componentes debe estar siempre en el mismo paquete raíz que el paquete del módulo en el que se encuentra. El desarrollador NO debe colocarlo en un subpaquete del paquete principal del módulo.
  
  
Lo siguiente para un proveedor de componentes es instanciar componentes bajo petición:

```
public Component getComponent(String componentId, Map<String, Object> parameters) {
    if (componentId.equals(ExampleViewComponent.EXAMPLE_VIEW_COMPONENT_ID)) {
    final ExampleViewComponent component = new ExampleViewComponent();
    component.setId(ExampleViewComponent.EXAMPLE_VIEW_COMPONENT_ID);
    component.setParameters(parameters);
    return component;
    }
    throw new IllegalArgumentException("Component id " + componentId + " not supported.");
}
```

!!!Note
    Implementar este método solo es necesario si tiene contenido dinámico; si el módulo solo tiene archivos js/css estáticos, entonces este método puede permanecer vacío (o simplemente lanzar una excepción).

Un componente puede ser muy simple; solo necesita implementar el método generate si extiende la clase `BaseComponent` de Etendo. Un ejemplo muy simple de la implementación del método generate:

```
public String generate() {
    return "alert('Hello world!')";
}
```

Una tarea muy importante del proveedor de componentes es registrar recursos estáticos: javascript y css. Estos recursos estáticos son concatenados/comprimidos por el kernel de Etendo:

```
public List<ComponentResource> getGlobalComponentResources() {
    final List<ComponentResource> globalResources = new ArrayList<ComponentResource>();
    globalResources.add(createStaticResource(
        "web/org.openbravo.client.application.examples/js/example-view-component.js", true));
    globalResources
        .add(createDynamicResource("org.openbravo.client.kernel/"
            + ExampleViewComponent.EXAMPLE_VIEW_COMPONENT_ID + "/"
            + ExampleViewComponent.EXAMPLE_VIEW_COMPONENT_ID));
    globalResources.add(createStyleSheetResource(
        "web/org.openbravo.userinterface.smartclient/openbravo/skins/"
            + KernelConstants.SKIN_VERSION_PARAMETER
            + "/org.openbravo.client.application.examples/my-styles.css", false));
    return globalResources;
}
```

El código anterior muestra cómo registrar recursos javascript y css. También se muestra un ejemplo de un recurso dinámico; esto llamará al componente para generar javascript.

**Búsqueda de todos los proveedores de componentes**

Etendo puede encontrar todos los `ComponentProviders` porque Weld analizará el classpath y recopilará todas las clases que tengan una anotación `@ComponentProvider`. Consulte la sección de Weld sobre el análisis del classpath indicada anteriormente.
## Implementación de acciones del lado del servidor invocables desde el cliente

Etendo proporciona una solución práctica para ejecutar acciones en el servidor desde el cliente. Este es el denominado concepto `ActionHandler`. El concepto `ActionHandler` tiene una parte del lado del servidor y otra del lado del cliente.

**ActionHandler: lado del servidor, invocación desde el cliente**

!!!note
    Por defecto, los `ActionHandlers` no pueden ser ejecutados por usuarios del Portal. Para hacerlos accesibles para usuarios del Portal, deben implementar la interfaz `org.openbravo.portal.PortalAccessible `.  
  
En el servidor, la lógica debe implementarse en una clase que implemente la interfaz `ActionHandler`.

Para la mayoría de los casos, tiene sentido sobrescribir/extender la clase `BaseActionHandler`:

```
package org.openbravo.client.application.examples;

...
 
public class MyActionHandler extends BaseActionHandler {
    /**
    * Needs to be implemented by a subclass.
    * 
    * @param parameters
    *          the parameters obtained from the request. Note that the request object and the session
    *          object are also present in this map, resp. as the constants
    *          {@link KernelConstants#HTTP_REQUEST} and {@link KernelConstants#HTTP_SESSION}.
    * @param content
    *          the request content (if any)
    * @return the return should be a JSONObject, this is passed back to the caller on the client.
    */
    protected JSONObject execute(Map<String, Object> parameters, String content) {
    try {
        // create the result
        JSONObject json = new JSONObject();
        json.put("result", "success");
 
        // and return it
        return json;
        } catch (Exception e) {
        throw new OBException(e);
        }
    }
}
```

Este lado del servidor puede invocarse desde el cliente usando este javascript:

```
// define the callback function which shows the result to the user
var callback = function(rpcResponse, data, rpcRequest) {
    isc.say('The result is : ' + data.result);
};
        
// and call the server
OB.RemoteCallManager.call('org.openbravo.client.application.examples.MyActionHandler', {}, {}, callback);
```

!!! info
    Para más información, visite [Cómo añadir un botón a la barra de herramientas](../how-to-guides/how-to-add-a-button-to-the-toolbar.md#adding-server-side-logic---implementation-steps). Contiene un ejemplo de un `ActionHandler` del lado del servidor que se invoca desde el cliente.
## Implementar lógica de inicialización de la aplicación

En los módulos, a veces tiene sentido inicializar algo cuando se inicia la aplicación. Etendo proporciona un mecanismo para implementar lógica de inicialización de la aplicación. Debe hacer lo siguiente:

  * crear una clase que implemente la interfaz `org.openbravo.client.kernel.ApplicationInitializer` 
  * anotar su clase con `@ApplicationScoped` 
    
    `@ApplicationScoped`
    public class KernelApplicationInitializer implements ApplicationInitializer {
     
      public void initialize() {
        // ponga aquí sus tareas de inicialización
      }
    }

  
Weld encontrará automáticamente su clase y Etendo la llamará al inicializar la capa de acceso a datos. 

!!!info
    Tiene acceso a la `SessionFactory` a través de `SessionFactoryController`, pero no a una sesión de Hibernate. Por lo tanto, para acceder a la base de datos, debe crear una sesión de Hibernate a partir de la SessionFactory.

!!!note
    Si no se está llamando a su código de aplicación, entonces consulte este [consejo](../concepts/common-issues-tips-and-tricks.md#my-component-is-not-found).
##  Eventos de entidad de negocio

La arquitectura de Etendo permite añadir fácilmente componentes que escuchan eventos de entidad de negocio. Los eventos de entidad de negocio son la creación, actualización y eliminación de entidades y los eventos de transacción. Etendo utiliza el framework de eventos de negocio para implementar lógica de negocio específica (por ejemplo, para generar/establecer números de documento en pedidos de venta).

Los eventos de entidad de negocio se emiten en el evento, es decir, antes de que el evento se ejecute en la base de datos. Es posible modificar la instancia de entidad relevante o realizar otras acciones en la base de datos. Los manejadores de eventos se ejecutan en la misma transacción que el propio evento de negocio.

!!!note
    Los eventos de entidad de negocio **solo** funcionan al acceder a la base de datos a través de la capa de acceso a datos, por lo que **no** funcionan para ventanas clásicas ni para llamadas directas a jdbc.

!!! info
    Para más información, visite [cómo implementar un manejador de eventos de negocio](../how-to-guides/how-to-implement-a-business-event-handler.md). Ofrece una descripción detallada de cómo implementar su propio manejador de eventos que escuche eventos de entidad de negocio.

###  Clases de eventos y API

Los eventos se implementan como clases Java; cuando se dispara un evento, se emite una instancia de esta clase y es recibida por los manejadores de eventos. Todas las instancias de evento heredan de la clase base `EntityPersistenceEvent`:

- `EntityNewEvent` 
- `EntityUpdateEvent`  
- `EntityDeleteEvent` 
- `TransactionBeginEvent.java` 
- `TransactionCompletedEvent.java` 

Las clases de eventos tienen `javadoc`, que proporciona más detalles.

Las API más relevantes se tratan aquí:

- `getTargetInstance` (disponible para todos los eventos): devuelve el objeto de negocio que es el objetivo del evento,
    
    !!!note
        No llame directamente a métodos set sobre este objeto; los nuevos valores no se persisten, ya que Hibernate ya ha leído los valores del objeto.

- `setCurrentState`(Property property, Object value) (disponible para todos los eventos, pero solo relevante para eventos de actualización/nuevo): establece un nuevo valor para la propiedad en la instancia objetivo; el nuevo valor se persistirá y, a continuación, se actualiza la instancia objetivo. La Property puede recuperarse desde la entidad de `targetInstance` (llame a `getEntity` en la instancia objetivo y luego a `getProperties` o `getProperty`). 
- Object `getPreviousState`(Property property) (solo disponible en el evento de actualización): devuelve el valor anterior (actualmente establecido en la base de datos) para la propiedad en la entidad.
## Implementación de una nueva vista

Una vista corresponde al contenido de una solapa principal en la interfaz de usuario de Etendo; por ejemplo, la ventana de pedido de compra es una vista. La arquitectura de Etendo permite crear su propia vista completamente personalizada desde cero. Al crear una entrada de menú para su vista, puede integrar su vista personalizada en el menú de la aplicación, el inicio rápido y en las vistas recientes de su espacio de trabajo. La implementación de una nueva vista se explica en detalle en este [Cómo](../how-to-guides/how-to-implement-a-new-main-view.md).
##  Programación del lado del cliente

El uso de la tecnología Rich Internet Application (RIA) significa que parte de la programación se realiza del lado del cliente y en JavaScript. La programación y depuración en JavaScript es muy diferente de la programación y el desarrollo en Java del lado del servidor. Puede ser vital consultar los consejos de [programación del lado del cliente](../concepts/common-issues-tips-and-tricks.md#client-side-coding-javascript).

Etendo proporciona e implementa varios componentes del lado del cliente para enviar solicitudes al servidor, internacionalización, etc. Visite [Desarrollo del lado del cliente y API](../concepts/client-side-development-and-api.md) para más información.
## Smartclient

Etendo utiliza la biblioteca de interfaz de usuario del lado del cliente [Smartclient](https://smartclient.com/){target="\_blank"} para implementar componentes. Para trabajar y desarrollar en Etendo y crear nuevos widgets, necesita comprender Smartclient. Consulte estos recursos:

* [Demo de Smartclient](https://smartclient.com/smartclient/showcase/?id=_Welcome){target="\_blank"} 
* [Foro de Smartclient](https://forums.smartclient.com/){target="\_blank"}  

Puede ser útil tener el código fuente de Smartclient y el material de referencia en su espacio de trabajo de IntelliJ; así es muy fácil buscar en el código fuente. El código fuente más reciente de Smartclient está disponible en este [repositorio correspondiente](https://bitbucket.org/koodu_software/org.openbravo.userinterface.smartclient.dev)

---

Este trabajo es una obra derivada de [Arquitectura de Openbravo 3](https://wiki.openbravo.com/wiki/Openbravo_3_Architecture){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.