---
tags:
  - Guía práctica
  - Manejador de eventos del cliente
  - Acciones
  - Etendo Classic
---

#  Cómo crear acciones de Manejador de eventos del cliente
  
##  Visión general

  Esta sección explica cómo implementar funciones del lado del cliente que se ejecutan antes o después de que se dispare un evento en una ventana estándar de la Interfaz de Usuario.
  
##  Módulo de ejemplo

  Esto se respalda con un módulo de ejemplo que muestra ejemplos del código presentado y comentado.

  El código de este módulo se puede descargar desde [este repositorio](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java).

##  Definición de acciones del Manejador de eventos del cliente

  Un **Manejador de eventos del cliente es un componente que permite a los desarrolladores responder a eventos específicos en Etendo**, como la creación, actualización o eliminación de entidades. Estos manejadores son esenciales para implementar lógica de negocio personalizada que se ejecuta cuando se producen determinados cambios en la base de datos.

##  Definición de la clase del Manejador de eventos
  En este paso, se implementarán los métodos clave necesarios para gestionar las acciones de eventos:

  * `Method getObservedEntities()` : Este método define las entidades que serán observadas por el Manejador de eventos. Esta información es esencial para que el manejador de eventos sepa a qué tipo de entidades debe reaccionar.

  * `Method onUpdate()` : Se ejecuta cuando se actualiza una entidad observada.

  * `Method onSave()` : Se ejecuta cuando se crea una nueva entidad.

  * `Method onDelete()` : Se ejecuta cuando se elimina una entidad observada.

## Ejemplos

### `getObservedEntities()`
Esta sección define las entidades que serán observadas por el Manejador de eventos. En este caso, se observa la entidad Greeting.
```java 
class GreetingEventHandler extends EntityPersistenceEventObserver {
  private static Entity[] entities = {
      ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
  private static final Logger logger = LogManager.getLogger();

  @Override
  protected Entity[] getObservedEntities() {
    return entities;
  }
}
```   

### `onUpdate()`
Este método intercepta las actualizaciones de registros en la entidad Greeting. Valida que el título de la entidad termine con un punto (“.”) y lo añade si es necesario.
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
    event.setCurrentState(greetingTitleProperty, title + ".");
  }
  logger.info("Greeting {} is being updated", event.getTargetInstance().getId());
}
```
### `onSave()`
En este método, se intercepta la creación de un nuevo registro en la entidad Greeting. Se realiza una validación similar a la del evento de actualización, añadiendo un punto al título si no lo tiene. Además, se crea un registro de traducción (GreetingTrl) para el saludo en un idioma específico (en este ejemplo, se utiliza el idioma con ID 171, que es neerlandés).
```java 
public void onSave(@Observes EntityNewEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
  final Greeting greeting = (Greeting) event.getTargetInstance();
  final String title = greeting.getTitle();
  if (title != null && !title.endsWith(".")) {
    final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
    event.setCurrentState(greetingTitleProperty, title + ".");
  }

  final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
  greetingTrl.setGreeting(greeting);
  greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
  greetingTrl.setName(greeting.getName());
  greetingTrl.setTitle(greeting.getTitle());
  greetingTrl.setTranslation(false);

  final Property greetingTrlProperty = greetingEntity.getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
  @SuppressWarnings("unchecked")
  final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
  greetingTrls.add(greetingTrl);

  logger.info("Greeting {} is being created", event.getTargetInstance().getId());
}
``` 

### `onDelete()`
El siguiente método se ejecuta cuando se elimina un saludo y registra la eliminación en el log.
```java 
public void onDelete(@Observes EntityDeleteEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  logger.info("Greeting {} is being deleted", event.getTargetInstance().getId());
}
```

!!!note
    Este Manejador de eventos muestra cómo interceptar eventos de creación, actualización y eliminación en una entidad. Le permite realizar validaciones y acciones automáticas, como añadir un punto al final de un título o crear automáticamente una traducción asociada al crear un nuevo saludo.
  

!!!info
    Este ejemplo se puede ajustar para otras entidades o eventos según los requisitos de su implementación.

---

Este trabajo es una obra derivada de [Cómo crear acciones de Manejador de eventos del cliente](http://wiki.openbravo.com/wiki/How_to_create_client_event_handler_actions){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.