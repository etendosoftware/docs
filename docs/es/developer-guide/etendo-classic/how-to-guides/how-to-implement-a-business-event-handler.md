---
title: Cómo implementar un business event handler
tags:
  - Cómo
  - Event Handler
  - Lógica de negocio
  - Método de evento
---
 
# Cómo implementar un business event handler { #how-to-implement-a-business-event-handler }

## Descripción general { #overview }

Un business event handler es un hook que ejecuta automáticamente su código Java cuando un registro — denominado entidad en el modelo de datos de Etendo — se guarda, actualiza o elimina. Esto le permite aplicar reglas de negocio en Java en lugar de escribir triggers en la base de datos.
Los business event handlers se corresponden con triggers en la base de datos. 
La principal ventaja de implementar lógica usando business event handlers en lugar de triggers es que puede programar su lógica en Java usando su IDE. 
Esto ayuda a la productividad y a la calidad, ya que puede programar, depurar y probar en un entorno integrado con el resto de su lógica de negocio.

!!! note "Algunas notas sobre los business event handlers:"
    * Se disparan cuando una instancia de entidad se actualiza, elimina o inserta. Antes de que la operación real se haya realizado en la base de datos, por lo que puede cambiar o añadir información que persiste junto con la entidad del evento. 
    * Su código de gestión de eventos se ejecuta en la misma transacción que el evento de negocio; los cambios que realice en la base de datos persisten junto con el business event handler en una única transacción. 
    * Los business event handlers solo funcionan cuando se accede a la base de datos a través de la Data Access Layer, por lo que no funcionan para ventanas clásicas o llamadas JDBC directas.
    * Puede hacer uso de toda la funcionalidad de la [Data Access Layer](../concepts/data-access-layer.md) en su código de gestión de eventos: puede consultar, crear nuevos objetos, persistir, etc.


Los eventos de negocio utilizan Weld, el framework de inyección de dependencias de Etendo, para descubrir y registrar automáticamente su clase event handler. No es necesario configurar Weld directamente; las anotaciones en su clase son suficientes. Para más información, consulte [Weld](../concepts/etendo-architecture.md#introducing-weld-dependency-injection-and-more).

!!!note
    Para maximizar el rendimiento, se excluyen ciertas partes del classpath; consulte [esta sección](../concepts/etendo-architecture.md#analyzing-the-classpath) si no se encuentran sus event handlers.

En esta sección, implementaremos un event handler sobre la entidad Tratamientos. Cada vez que se guarde un título, se añadirá una traducción al español. Además, imprimiremos algunos mensajes en la consola para otros eventos de negocio.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-0.png)

!!!note
    Para una referencia de implementación consolidada, consulte [Cómo crear acciones de client event handler](how-to-create-client-event-handler-actions.md).

## Módulo de ejemplo { #example-module }

Esta sección está respaldada por un módulo de ejemplo que muestra un ejemplo del código mostrado y comentado aquí.

El código del módulo de ejemplo puede descargarse desde este repositorio: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

!!!note
    La lista completa de importaciones Java necesarias está disponible en el [archivo fuente de ejemplo](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}.
  
## El event handler: una primera implementación { #the-event-handler---a-first-implementation }

Un event handler se implementa como una clase Java normal en su módulo. La clave es crear métodos con una anotación en los parámetros. Aquí tiene un primer ejemplo sencillo de un event handler que escucha eventos sobre la entidad Tratamientos:

    
!!!warning
    No llame a setters directamente en la entidad del evento. Cuando el evento se dispara, el framework de persistencia ya ha capturado los valores actuales de los campos del objeto. Llamar a un setter actualiza el objeto Java en memoria, pero Hibernate ya ha capturado los valores de las propiedades en su array de estado interno antes de disparar el evento, por lo que el cambio realizado por el setter se ignora silenciosamente y no se persistirá. Utilice `event.setCurrentState(property, newValue)` en su lugar. Esto se muestra en cada ejemplo de código de esta página.

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
    logger.info("Greeting {} is being updated", event.getTargetInstance().getId());
  }
 
  public void onSave(@Observes EntityNewEvent event) {
    if (!isValidEvent(event)) {
      return;
    }
    logger.info("Greeting {} is being created", event.getTargetInstance().getId());
  }
 
  public void onDelete(@Observes EntityDeleteEvent event) {
    if (!isValidEvent(event)) {
      return;
    }
    logger.info("Greeting {} is being deleted", event.getTargetInstance().getId());
  }
}
```

!!!note
    * Tiene sentido extender [EntityPersistenceEventObserver](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.kernel/src/org/openbravo/client/kernel/event/EntityPersistenceEventObserver.java){target="\_blank"}, ya que ayuda a filtrar los eventos correctos. 
    * El nombre del método no es relevante; lo relevante es la anotación en el parámetro y el propio parámetro. Weld utiliza esto para detectar y registrar para qué eventos escucha esta clase. 
    * El event handler se llamará para eventos que ocurran en todas las entidades; por lo tanto, cada método comienza con la sentencia if con isValidEvent, para filtrar eventos no deseados. 
    * Se recomienda el uso de la clase `_org.apache.logging.log4j.Logger_` para el registro (logging), tal y como se muestra arriba. 

!!!info
    Las clases que extienden `_EntityPersistenceEventObserver_` se definen como `_@ApplicationScoped_` de forma predeterminada.

### Resultado { #result }

Cuando añada la clase anterior a su módulo, reinicie el sistema y, a continuación, vaya a la ventana de Tratamientos:
[http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)

Y realice algunas acciones; debería ver los siguientes mensajes en la consola:

```bash
Greeting FF8081813097E041013097E805F4000F is being updated
Greeting FF8081813097E041013097E805F4000F is being deleted
Greeting FF8081813097E041013097E805F4000F is being created
```

!!!note 
    * Solo necesita implementar un método para el evento que desea escuchar; por lo tanto, si solo necesita escuchar eventos de actualización, entonces implemente únicamente un método con el parámetro @Observes EntityUpdateEvent. 
    * Cada método comienza con una comprobación de si el evento es válido; esto es necesario para filtrar solo los eventos relevantes; consulte la sección siguiente. 
    * Dentro de los métodos event handler, puede usar la API del objeto event para detectar cuál es el evento de entidad y para acceder al estado actual y al estado previo de la entidad. Consulte [aquí](../concepts/etendo-architecture.md#event-classes-and-api) para más información. 

### Filtrar solo los eventos relevantes { #filtering-only-relevant-events }

Todos los event handlers del sistema reciben eventos de todas las entidades, no solo de aquellas para las que fue escrito. Si omite el filtro, su código se ejecutará en cada inserción, actualización y eliminación en toda la aplicación. La comprobación `isValidEvent` restringe la ejecución a las entidades listadas en `getObservedEntities`.

```java
private static Entity[] entities = { ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
 
@Override
protected Entity[] getObservedEntities() {
  return entities;
}
```

El método `getObservedEntities` se llama cuando se llama al método `isValidEvent`; `getObservedEntities` devuelve las entidades que desea gestionar en este event handler. 
Para hacer uso de ello, añada este código al inicio de cada método event handler:

```java
if (!isValidEvent(event)) {
  return;
}
```

Esta parte es necesaria porque los métodos de evento se llamarán para entidades de todos los tipos. 
En este ejemplo, solo queremos escuchar cambios en la entidad Tratamientos.

!!!note
    `isValidEvent` también devuelve `false` durante las operaciones de importación de datos. Esto es intencional — evita que la lógica de negocio se ejecute sobre datos importados. Si su event handler no se está disparando, compruebe si la operación se está realizando a través de un proceso de importación.

## Añadir algo de lógica de negocio { #adding-some-business-logic }

En este siguiente paso, añadimos lógica al event handler:

  * Cada vez que se cree/actualice un tratamiento, añadir un . al título, si no estaba ya ahí. 
  * Cuando se cree un nuevo tratamiento, añadir una traducción para él. 

!!!note
    En el siguiente paso se crea automáticamente una traducción al neerlandés cada vez que se inserta un nuevo tratamiento.
    

### Cambiar la entidad en actualización/inserción { #changing-the-entity-on-updateinsert }

En este paso añadiremos una lógica sencilla a los eventos de actualización y guardado para añadir un punto al título si todavía no lo tiene.

```java
public void onUpdate(@Observes EntityUpdateEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final Greeting greeting = (Greeting) event.getTargetInstance();
  final String title = greeting.getTitle();
  if (title != null && !title.endsWith(".")) {
    final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
    final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
    // note use setCurrentState and not setters on the Greeting object directly
    event.setCurrentState(greetingTitleProperty, title + ".");
  }
  logger.info("Greeting {} is being updated", event.getTargetInstance().getId());
}
 
public void onSave(@Observes EntityNewEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final Greeting greeting = (Greeting) event.getTargetInstance();
  // now also add the dot to the title
  final String title = greeting.getTitle();
  if (title != null && !title.endsWith(".")) {
    final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
    final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
    // note use setCurrentState and not setters on the Greeting object directly
    event.setCurrentState(greetingTitleProperty, title + ".");
  }
 
  logger.info("Greeting {} is being created", event.getTargetInstance().getId());
}
```

Repasemos el código. En primer lugar, obtenga la entidad y el título:

    
```java
final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
final String title = greeting.getTitle();
```

Si el título no termina en un punto, entonces obtenga la entidad y la propiedad relevante:

```java
if (title != null && !title.endsWith(".")) {
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

La instancia de entidad modificada no necesita guardarse explícitamente; esto lo realiza la [Data Access Layer](../concepts/data-access-layer.md) y Hibernate automáticamente.

A continuación, pruebe los cambios: vaya a la ventana ([http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)) e introduzca un nuevo tratamiento sin punto en el título. 
Al guardar, verá que se añade un punto. 
Intente actualizar el registro; tendrá el mismo comportamiento.

### Añadir una instancia hija { #adding-a-child-instance }

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

Un objeto `GreetingTrl` es un registro hijo de traducción vinculado a un `Greeting` padre. Etendo utiliza el sufijo `Trl` para denominar las tablas de traducción en todo el modelo de datos.

Tenga en cuenta que la propiedad de lista se recupera con `getCurrentState` y se le añaden elementos directamente, en lugar de reemplazarla con `setCurrentState`. Esto se debe a que añadir elementos a una lista existente no requiere reemplazar el valor completo de la propiedad.

El objeto trl es hijo de la entidad del evento Tratamientos y persistirá junto con ella, por lo que no es necesario guardarlo explícitamente.
Cuando ahora introduzca una nueva entrada en la ventana, verá que se crea un registro hijo adicional de traducción.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-3.png)

### Interrumpir la acción de guardado { #interrupt-the-save-action }

A veces necesita interrumpir la acción de guardado porque el usuario está haciendo algo incorrecto. Esto puede hacerse lanzando una `OBException`. Al hacerlo, Etendo muestra el mensaje de la excepción al usuario como un diálogo de error y revierte la transacción completa, incluidos los cambios que el event handler ya hubiera realizado.

```java
public void onUpdate(@Observes
EntityUpdateEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final OBSA_Orderline_Assign olineAssign = (OBSA_Orderline_Assign) event.getTargetInstance();
  if (olineAssign.getProductWithStorage().getProduct() != olineAssign.getSalesOrderLine()
      .getProduct()) {
    String language = OBContext.getOBContext().getLanguage().getLanguage();
    ConnectionProvider conn = new DalConnectionProvider(false);
    throw new OBException(Utility.messageBD(conn, "OBSA_ErrorProduct", language));
  }
}
```

## Ejemplos de business entity event handlers { #examples-of-business-entity-event-handlers }

Etendo utiliza business entity event handlers para implementar lógica de negocio en varias ubicaciones; aquí tiene algunos ejemplos:

  * [ModuleHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/ModuleHandler.java){target="\_blank"}
  * [SetDocumentNoHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/SetDocumentNoHandler.java){target="\_blank"}

El código fuente completo del event handler de ejemplo está disponible aquí: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

---

Este trabajo es una obra derivada de [How to implement a business event handler](https://wiki.openbravo.com/wiki/How_to_implement_a_business_event_handler){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
