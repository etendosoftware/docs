---
tags:
  - client event handler
  - actions
  - Etendo Classic
---

#  How to Create Client Event Handler Actions
  
##  Overview

  This section discusses how to implement client-side functions (JavaScript) that are executed before or after an event is fired in a standard window of the User Interface.
  
##  Example Module

  This is supported by an example module which shows examples of the code shown and discussed.

  The code of the example module can be downloaded from this repository:
  [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java).

##  Defining Client Event Handler Actions

  A **Client Event Handler is a component that allows developers to respond to specific events in Etendo**, such as the creation, update or deletion of entities. These handlers are essential for implementing custom business logic that executes when certain changes occur in the database.

### Step 1: Creating an Action

  * Navigate to the **Process Definition** window.
  * Create a new record and define the **UI pattern** as **Action**.
  * Mark the process as **Multi Record**.

!!!info
    Check the box to indicate that the process is **Multi Record** (if it is necessary to handle multiple registrations at the same time).

![createjobs1.png](https://docs.etendo.software/latest/assets/legacy/technicaldocumentation/platform/createjobs1.png)

### Step 2: Create a Button to Execute the Action

  * Create Column: Adds a column in the corresponding table.
  * Create Field: Create a field in the window where you want the button to appear.
  * Set the field to execute the action.
  * Implementing the Java Class for Action.

##  Define the Event Handler Class
  In this step, the key methods needed to handle event actions will be implemented:

  * Method getObservedEntities() : This method defines the entities that will be observed by the Event Handler. This information is essential for the event handler to know what kind of entities it should react to.

  * Method onUpdate() : This method is executed when a watched entity is updated.

  * Method onSave() : This method is executed when a new entity is created.

  * Method onDelete() : This method is executed when an observed entity is eliminated.

## Examples

### getObservedEntities()
In the following code, getObservedEntities returns the entities to be observed.
```java 
@Override
protected Entity[] getObservedEntities() {
  return entities;
}
```   

### onUpdate()
The following method listens for update events and adds a dot to the title if it is not present.
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
### onSave()
In the following code, onSave adjusts the title and adds a translation when a new greeting is created.
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

### onDelete()
The following method is executed when a greeting is deleted and records the deletion in the log.
```java 
public void onDelete(@Observes EntityDeleteEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  logger.info("Greeting {} is being deleted", event.getTargetInstance().getId());
}
```

---

This work is a derivative of [How to Create Client Event Handler Actions](http://wiki.openbravo.com/wiki/How_to_create_client_event_handler_actions){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.