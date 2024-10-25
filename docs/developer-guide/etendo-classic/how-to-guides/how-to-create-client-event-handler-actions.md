---
tags:
  - client event handler
  - actions
  - Etendo Classic
---

#  How to Create Client Event Handler Actions
  
##  Overview

  This section discusses how to implement client-side functions that are executed before or after an event is fired in a standard window of the User Interface.
  
##  Example Module

  This is supported by an example module which shows examples of the code shown and discussed.

  The code of this module can be downloaded from [this repository](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java).

##  Defining Client Event Handler Actions

  A **Client Event Handler is a component that allows developers to respond to specific events in Etendo**, such as the creation, update or deletion of entities. These handlers are essential for implementing custom business logic that executes when certain changes occur in the database.

##  Defining the Event Handler Class
  In this step, the key methods needed to handle event actions will be implemented:

  * `Method getObservedEntities()` : This method defines the entities that will be observed by the Event Handler. This information is essential for the event handler to know what kind of entities it should react to.

  * `Method onUpdate()` : It is executed when a watched entity is updated.

  * `Method onSave()` : It is executed when a new entity is created.

  * `Method onDelete()` : It is executed when an observed entity is eliminated.

## Examples

### `getObservedEntities()`
This section defines the entities that will be observed by the Event Handler. In this case, the Greeting entity is observed.
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
This method intercepts record updates in the Greeting entity. It validates that thetitle of the entity ends with a dot (“.”) and adds it if necessary.
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
In this method, the creation of a new record in the Greeting entity is intercepted. A validation similar to that of the update event is performed, adding a dot to the title if it does not have one. In addition, a translation record (GreetingTrl) is created for the greeting in a specific language (in this example, the language with ID 171, which is Dutch, is used).
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
The following method is executed when a greeting is deleted and records the deletion in the log.
```java 
public void onDelete(@Observes EntityDeleteEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  logger.info("Greeting {} is being deleted", event.getTargetInstance().getId());
}
```

!!!note
    This Event Handler shows how to intercept creation, update and deletion events in an entity. It allows you to perform automatic validations and actions, such as adding a dot at the end of a title or creating an associated translation automatically when creating a new greeting.
  

!!!info
    This example can be adjusted for other entities or events according to the requirements of your implementation.

---

This work is a derivative of [How to Create Client Event Handler Actions](http://wiki.openbravo.com/wiki/How_to_create_client_event_handler_actions){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.