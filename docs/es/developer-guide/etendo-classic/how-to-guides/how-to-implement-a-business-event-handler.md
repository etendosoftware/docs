---
title: Cómo implementar un manejador de eventos de negocio
tags:
  - Cómo
  - Manejador de eventos
  - Lógica de negocio
  - Método de evento
---
 
# Cómo implementar un manejador de eventos de negocio

## Visión general

El evento de entidad de negocio le permite implementar lógica de negocio que reacciona a eventos específicos que se disparan cuando las entidades se actualizan, eliminan o insertan en la base de datos. 
Los eventos de entidad de negocio se corresponden con triggers en la base de datos. 
La principal ventaja de implementar lógica usando eventos de entidad de negocio en lugar de triggers es que puede programar su lógica en Java usando su IDE. 
Esto ayuda a la productividad y a la calidad, ya que puede programar, depurar y probar en un entorno integrado con el resto de su lógica de negocio.

!!! note "Algunas notas sobre los eventos de entidad de negocio:"
    * Se disparan cuando una instancia de entidad se actualiza, elimina o inserta. Antes de que la operación real se haya realizado en la base de datos, por lo que puede cambiar o añadir información que persiste junto con la entidad del evento. 
    * Su código de gestión de eventos se ejecuta en la misma transacción que el evento de negocio; los cambios que realice en la base de datos persisten junto con el evento de entidad de negocio en una única transacción. 
    * Los eventos de entidad de negocio solo funcionan cuando se accede a la base de datos a través de la capa de acceso a datos, por lo que no funcionan para ventanas clásicas o llamadas JDBC directas.
    * Puede hacer uso de toda la funcionalidad de la [capa de acceso a datos](../concepts/Data_Access_Layer.md) en su código de gestión de eventos: puede consultar, crear nuevos objetos, persistir, etc.
      
      Advertencia: no llame a setters en la propia instancia; esto no funciona porque, cuando el evento se ha difundido, Hibernate ya ha leído el estado del objeto. 
      Por lo tanto, debe cambiar el valor mediante el método especial `setCurrentState`: `event.setCurrentState(greetingTitleProperty, title + ".");`


Los eventos de negocio hacen uso del framework de eventos proporcionado por el framework [Weld](../concepts/Etendo_Architecture.md#Introducing_Weld:_dependency_injection_and_more). Para registrar un manejador de eventos, se utilizan anotaciones. 

!!!note
    Para maximizar el rendimiento, se excluyen ciertas partes del classpath; consulte [esta sección](../concepts/Etendo_Architecture.md#Analyzing_the_classpath) si no se encuentran sus manejadores de eventos.

En esta sección, implementaremos un manejador de eventos sobre la entidad Tratamientos. Cada vez que se guarde un título, se añadirá una traducción al español. Además, imprimiremos algunos mensajes en la consola para otros eventos de negocio.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-0.png)

##  Módulo de ejemplo

Esta sección está respaldada por un módulo de ejemplo que muestra un ejemplo del código mostrado y comentado aquí.

El código del módulo de ejemplo puede descargarse desde este repositorio: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)
  
##  El manejador de eventos: una primera implementación

Un manejador de eventos se implementa como una clase Java normal en su módulo. La clave es crear métodos con una anotación en los parámetros. Aquí tiene un primer ejemplo sencillo de un manejador de eventos que escucha eventos sobre la entidad Tratamientos:

    
```java title="GreetingEventHandler.java"
class GreetingEventHandler extends EntityPersistenceEventObserver {
  private static Entity[] entities = { ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
  private static final Logger logger = LogManager.getLogger();
 
  @Override
  protected Entity[] getObservedEntities() {
    return entities;
  }
 
  public void onUpdate(@Observes EntityUpdateEvent event) {
    if (!isValidEvent(event)) {
      return;
    }
    logger.info("Greeting " + event.getTargetInstance().getId() + " is being updated");
  }
 
  public void onSave(@Observes EntityNewEvent event) {
    if (!isValidEvent(event)) {
      return;
    }
    logger.info("Greeting " + ((Greeting) event.getTargetInstance()).getName()
        + " is being created");
  }
 
  public void onDelete(@Observes EntityDeleteEvent event) {
    if (!isValidEvent(event)) {
      return;
    }
    logger.info("Greeting " + event.getTargetInstance().getId() + " is being deleted");
  }
}
```

!!!note
    * Tiene sentido extender [EntityPersistenceEventObserver](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.kernel/src/org/openbravo/client/kernel/event/EntityPersistenceEventObserver.java){target="\_blank"}, ya que ayuda a filtrar los eventos correctos. 
    * El nombre del método no es relevante; lo relevante es la anotación en el parámetro y el propio parámetro. Weld utiliza esto para detectar y registrar para qué eventos escucha esta clase. 
    * El manejador de eventos se llamará para eventos que ocurran en todas las entidades; por lo tanto, cada método comienza con la sentencia if con isValidEvent, para filtrar eventos no deseados. 
    * Se recomienda el uso de la clase `_org.apache.logging.log4j.Logger_` para el registro (logging), tal y como se muestra arriba. 

!!!info
    Las clases que extienden `_EntityPersistenceEventObserver_` se definen como `_@ApplicationScoped_` de forma predeterminada.

###  Resultado

Cuando añada la clase anterior a su módulo, reinicie el sistema y, a continuación, vaya a la ventana de Tratamientos:
[http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)

Y realice algunas acciones; debería ver los siguientes mensajes en la consola:

```bash
Greeting FF8081813097E041013097E805F4000F is being updated
Greeting FF8081813097E041013097E805F4000F is being deleted
Greeting Mr is being created
```

###  Métodos de evento

El código fuente anterior ilustra cómo se implementan los métodos de evento:
     
```java    
public void onUpdate(@Observes EntityUpdateEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  logger.info("Greeting " + event.getTargetInstance().getId() + " is being updated");
}
 
public void onSave(@Observes EntityNewEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  logger.info("Greeting " + ((Greeting) event.getTargetInstance()).getName()
      + " is being created");
}
 
public void onDelete(@Observes EntityDeleteEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  logger.info("Greeting " + event.getTargetInstance().getId() + " is being deleted");
}
```

!!!note 
    * Solo necesita implementar un método para el evento que desea escuchar; por lo tanto, si solo necesita escuchar eventos de actualización, entonces implemente únicamente un método con el parámetro @Observes EntityUpdateEvent. 
    * Cada método comienza con una comprobación de si el evento es válido; esto es necesario para filtrar solo los eventos relevantes; consulte la sección siguiente. 
    * Dentro de los métodos del manejador de eventos, puede usar la API del objeto event para detectar cuál es el evento de entidad y para acceder al estado actual y al estado previo de la entidad. Consulte [aquí](../concepts/Etendo_Architecture.md#Event_Classes_and_API) para más información. 

###  Filtrar solo los eventos relevantes

Como se ha mencionado anteriormente, los métodos de evento se llaman para todas las entidades de todos los tipos. 
En nuestro ejemplo, solo queremos gestionar eventos sobre la entidad Tratamientos.
Hay código específico en el ejemplo anterior que se encarga de esto. 
Comienza en la parte superior de la clase:

```java
private static Entity[] entities = { ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
 
@Override
protected Entity[] getObservedEntities() {
  return entities;
}
```

El método `getObservedEntities` se llama cuando se llama al método `isValidEvent`; `getObservedEntities` devuelve las entidades que desea gestionar en este manejador de eventos. 
Para hacer uso de ello, añada este código al inicio de cada método de gestión de eventos:

```java
if (!isValidEvent(event)) {
  return;
}
```

Esta parte es necesaria porque los métodos de evento se llamarán para entidades de todos los tipos. 
En este ejemplo, solo queremos escuchar cambios en la entidad Tratamientos.

##  Añadir algo de lógica de negocio

En este siguiente paso, añadimos lógica al manejador de eventos:

  * Cada vez que se cree/actualice un tratamiento, añadir un . al título, si no estaba ya ahí. 
  * Cuando se cree un nuevo tratamiento, añadir una traducción para él. 

!!!note
    Para crear una nueva traducción cuando se añade un nuevo tratamiento. 
    Para este ejemplo, añadiremos una traducción al neerlandés.
    

###  Cambiar la entidad en actualización/inserción

En este paso añadiremos una lógica sencilla a los eventos de actualización y guardado para añadir un punto al título si todavía no lo tiene.

```java
public void onUpdate(@Observes EntityUpdateEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final Greeting greeting = (Greeting) event.getTargetInstance();
  final String title = greeting.getTitle();
  if (title != null && !title.endsWith(".")) {
    final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
    final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
    // note use setCurrentState and not setters on the Greeting object directly
    event.setCurrentState(greetingTitleProperty, title + ".");
  }
  logger.info("Greeting " + event.getTargetInstance().getId() + " is being updated");
}
 
public void onSave(@Observes EntityNewEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final Greeting greeting = (Greeting) event.getTargetInstance();
  // now also add the dot to the title
  final String title = greeting.getTitle();
  if (title != null && !title.endsWith(".")) {
    final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
    final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
    // note use setCurrentState and not setters on the Greeting object directly
    event.setCurrentState(greetingTitleProperty, title + ".");
  }
 
  logger.info("Greeting " + ((Greeting) event.getTargetInstance()).getName()
      + " is being created");
}
```

Repasemos el código. En primer lugar, haga el cast de la instancia y obtenga el título:

    
```java
final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
final String title = greeting.getTitle();
```

Si el título no termina en un punto, entonces obtenga la entidad y la propiedad relevante:

```java
if (title != null && !title.endsWith(".")) {
  final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
  final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
```

!!!note
    Usamos las constantes generadas para el nombre de la entidad y los nombres de propiedades; esto proporciona comprobación en tiempo de compilación y es una práctica recomendada.

Y, a continuación, establezca el estado actual.

!!!note
    No llame a setters en la propia instancia de Greeting; esto no funciona porque, cuando el evento se ha difundido, Hibernate ya ha leído el estado del objeto. Por lo tanto, debe cambiar el valor mediante el método especial `setCurrentState`:

```java
event.setCurrentState(greetingTitleProperty, title + ".");
```

La instancia de entidad modificada no necesita guardarse explícitamente; esto lo realiza la [capa de acceso a datos](../concepts/Data_Access_Layer.md) y Hibernate automáticamente.

A continuación, pruebe los cambios: vaya a la ventana ([http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)) e introduzca un nuevo tratamiento sin punto en el título. 
Al guardar, verá que se añade un punto. 
Intente actualizar el registro; tendrá el mismo comportamiento.

###  Añadir una instancia hija

Como siguiente paso, añadiremos lógica al método `onSave` para crear una instancia hija adicional (una nueva traducción). 
Esto es un poco más complejo. Añada el siguiente código al final del método onSave:

```java
final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
// set relevant translation properties
greetingTrl.setGreeting(greeting);
// 171 is dutch, choose any other language..
greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
// note we can call getters on the targetInstance, but not setters!
greetingTrl.setName(greeting.getName());
greetingTrl.setTitle(greeting.getTitle());
greetingTrl.setTranslation(false);
 
// and add the greetingTrl to the greeting
// we don't use event.setCurrentState as we get the list and add to it
// get the trl property for the greeting entity
final Property greetingTrlProperty = greetingEntity
    .getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
@SuppressWarnings("unchecked")
final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
greetingTrls.add(greetingTrl);
 
// don't need to save the greetingTrl, it is saved as the child of the greeting
// OBDal.getInstance().save(greetingTrl);
```


Repasemos el código. Primero se crea el objeto trl y se establecen algunas propiedades. 
Tenga en cuenta que, como el objeto no forma parte del evento, puede llamar a sus setters directamente. 
El idioma se elige de forma arbitraria. 
Consulte el documento [DAL](../concepts/Data_Access_Layer.md) para obtener información sobre las API que puede usar para recuperar objetos de la base de datos.

```java
final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
// set relevant translation properties
greetingTrl.setGreeting(greeting);
// 171 is dutch, choose any other language..
greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
// note we can call getters on the targetInstance, but not setters!
greetingTrl.setName(greeting.getName());
greetingTrl.setTitle(greeting.getTitle());
greetingTrl.setTranslation(false);
```

Después, como siguiente paso, añada el nuevo objeto trl a la entidad del evento. Esto es un poco
especial, ya que necesitamos actualizar una propiedad de tipo List de la entidad del evento. Por lo tanto, en lugar
de llamar a `setCurrentState`, obtenemos la lista y añadimos el elemento. Esta es una forma correcta de hacerlo:

```java
// and add the greetingTrl to the greeting
// we don't use event.setCurrentState as we get the list and add to it
// get the trl property for the greeting entity
final Property greetingTrlProperty = greetingEntity
    .getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
@SuppressWarnings("unchecked")
final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
greetingTrls.add(greetingTrl);
 
// don't need to save the greetingTrl, it is saved as the child of the greeting
// OBDal.getInstance().save(greetingTrl);
```

El objeto trl es hijo de la entidad del evento Tratamientos y persistirá junto con ella, por lo que no es necesario guardarlo explícitamente.
Cuando ahora introduzca una nueva entrada en la ventana, verá que se crea un registro hijo adicional de traducción.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-3.png)

###  Interrumpir la acción de guardado

A veces necesita interrumpir la acción de guardado porque el usuario está haciendo algo incorrecto; esto puede hacerse lanzando una excepción.

```java
public void onUpdate(@Observes
EntityUpdateEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final OBSA_Orderline_Assign olineAssign = (OBSA_Orderline_Assign) event.getTargetInstance();
  if (olineAssign.getProductWithStorage().getProduct() != olineAssign.getSalesOrderLine()
      .getProduct()) {
    String language = OBContext.getOBContext().getLanguage().getLanguage();
    ConnectionProvider conn = new DalConnectionProvider(false);
    throw new OBException(Utility.messageBD(conn, "OBSA_ErrorProduct", language));
  }
}
```

##  Ejemplos de manejadores de eventos de entidad de negocio

Etendo Classic utiliza manejadores de eventos de entidad de negocio para implementar lógica de negocio en
varias ubicaciones; aquí tiene algunos ejemplos:

  * [ModuleHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/ModuleHandler.java){target="\_blank"}
  * [SetDocumentNoHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/SetDocumentNoHandler.java){target="\_blank"}

El código fuente completo del manejador de eventos de ejemplo está disponible aquí: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

---

Este trabajo es una obra derivada de [How to implement a business event handler](https://wiki.openbravo.com/wiki/How_to_implement_a_business_event_handler){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.