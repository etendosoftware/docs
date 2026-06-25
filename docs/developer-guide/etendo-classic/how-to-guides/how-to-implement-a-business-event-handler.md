---
title: How to Implement a Business Event Handler
tags:
  - How to
  - Event Handler
  - Business Logic
  - Event Method
---
 
# How to Implement a Business Event Handler

## Overview

A business entity event is a hook that runs your Java code automatically when a record — called an entity in Etendo's data model — is saved, updated, or deleted. This lets you enforce business rules in Java instead of writing database triggers.
Business entity events correspond to triggers in the database. 
The main advantage of implementing logic using business entity events instead of in triggers is that you can code your logic in java using your IDE. 
This helps productivity and quality as you can code, debug and test in an integrated environment with the rest of your business logic.

!!! note "Some notes on business entity events:"
    * They are fired when an entity instance is updated, deleted or inserted. Before the actual operation has been done in the database, so you can change or add information which persists together with the event entity. 
    * Your event handling code runs in the same transaction as the business event, changes you make to the database persist together with the business entity event in one transaction. 
    * Business entity events only work when accessing the database through the data access layer, so they do not work for classic windows or direct jdbc calls.
    * You can make use of the full [data access layer](../concepts/data-access-layer.md) functionality in your event handling code, you can query, create new objects, persist etc.


Business events use Weld, Etendo's dependency injection framework, to discover and register your event handler class automatically. You do not configure Weld directly; the annotations in your class are sufficient. For more information, see [Weld](../concepts/etendo-architecture.md#introducing-weld-dependency-injection-and-more).

!!!note
    In order to maximize performance, certain part of the classpath are excluded, check out [this section](../concepts/etendo-architecture.md#analyzing-the-classpath) if your event handlers are not found.

In this section, we will implement an event handler on the Greeting entity. Whenever a title is saved, a Spanish translation will be added. In addition, we will print some messages to the console for other business events.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-0.png)

!!!note
    For a consolidated implementation reference, see [How to Create Client Event Handler Actions](how-to-create-client-event-handler-actions.md).

##  Example Module

This section is supported by an example module which shows an example of the code shown and discussed here.

The code of the example module can be downloaded from this repository: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

!!!note
    The full list of required Java imports is available in the [example source file](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}.
  
##  The event handler - A first implementation

An event handler is implemented as a normal java class in your module. The key thing is to create methods with an annotation on the parameters. Here is a first simple example of an event handler which listens to events on the Greeting entity:

    
!!!warning
    Do not call setters on the event entity directly. When the event fires, the persistence framework has already captured the object's current field values. Calling a setter updates the Java object in memory, but Hibernate has already captured the property values into its internal state array before firing the event, so the setter's change is silently ignored and will not be persisted. Use `event.setCurrentState(property, newValue)` instead. This is shown in every code example on this page.

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
    * It makes sense to extend the [EntityPersistenceEventObserver](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.kernel/src/org/openbravo/client/kernel/event/EntityPersistenceEventObserver.java){target="\_blank"}, it helps to filter for the correct events. 
    * The name of the method is not relevant, the relevant thing is the annotation on the parameter and the parameter. Weld uses this to detect and register for which events this class listens to 
    * The event handler will be called for events occurring on all entities, therefore each method starts with the if statement with isValidEvent, to filter out unwanted events. 
    * The use of the `_org.apache.logging.log4j.Logger_` class is recommended for logging as shown above.

!!!info
    Classes extending `_EntityPersistenceEventObserver_` are defined as `_@ApplicationScoped_` by default.

###  Result

When you add the above class to your module, restart the system, then go to the greeting window:
[http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)

And do some actions you should see the following messages in the console:

```bash
Greeting FF8081813097E041013097E805F4000F is being updated
Greeting FF8081813097E041013097E805F4000F is being deleted
Greeting FF8081813097E041013097E805F4000F is being created
```

!!!note 
    * You only need to implement a method for the event you want to listen to, so if you only need to listen to update events, then only implement a method with the @Observes EntityUpdateEvent parameter. 
    * Each method starts with a check if the event is valid, this is needed to filter for relevant events only, see the section below. 
    * Within the event handler methods, you can use the api on the event object to detect which is the entity event and to get access to the current and previous state of the entity. See [here](../concepts/etendo-architecture.md#event-classes-and-api) for more information. 

###  Filtering Only Relevant Events

Every event handler in the system receives events from every entity, not just the ones it was written for. If you omit the filter, your code will run on every insert, update, and delete across the entire application. The `isValidEvent` check restricts execution to the entities listed in `getObservedEntities`.

```java
private static Entity[] entities = { ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
 
@Override
protected Entity[] getObservedEntities() {
  return entities;
}
```

The `getObservedEntities` method is called when you call the `isValidEvent` method, `getObservedEntities` returns the entities you want to handle in this event handler. 
To make use of it add this code to each event handling method in the beginning:

```java
if (!isValidEvent(event)) {
  return;
}
```

This part is needed because the event methods will be called for entities of all types. 
In this example we only want to listen to changes on the Greeting entity.

!!!note
    `isValidEvent` also returns `false` during data import operations. This is intentional — it prevents business logic from running on imported data. If your event handler is not firing, check whether the operation is being performed through an import process.

##  Adding some business logic

In this next step, we add logic to the event handler:

  * Whenever a greeting gets created/updated, add a . to the title, if it was not already there 
  * When a new greeting gets created, add a translation for it. 

!!!note
    To create a new translation for when a new greeting is added. 
    For this example, we will be adding a dutch translation.
    

###  Changing the entity on update/insert

In this step we will be adding some simple logic to the update and save event to add a dot to the title if it not already has one.

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
  logger.info("Greeting {} is being updated", event.getTargetInstance().getId());
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
 
  logger.info("Greeting {} is being created", event.getTargetInstance().getId());
}
```

Let's walk through the code. First, cast the instance and get the title:

    
```java
final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
final String title = greeting.getTitle();
```

If the title does not end on a dot then get the entity and the relevant property:

```java
if (title != null && !title.endsWith(".")) {
  final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
  final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
```

!!!note
    We use the generated constants to the entity name and property
    names, this gives compile time checking and is a recommended practice.

And then set the current state.

!!!note
    Don't call setters on the Greeting instance itself. Calling a setter updates the Java object in memory, but Hibernate has already captured the property values into its internal state array before firing the event, so the setter's change is silently ignored and will not be persisted. Use `event.setCurrentState(property, newValue)` instead:

```java
event.setCurrentState(greetingTitleProperty, title + ".");
```

The changed entity instance does not need to be saved explicitly, this is done by the [data access layer](../concepts/data-access-layer.md) and hibernate automatically.

Then test the changes, go to the window ([http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)), enter a new greeting without a dot in the title. 
When saving you will see a dot getting added. 
Try updating the record, you will have the same behavior.

###  Adding a child instance

As the next step we will be adding logic to the `onSave` method to create an extra child instance (a new translation). 
This is a bit more complex. Add the following code to the onSave method at the end:

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

A `GreetingTrl` object is a translation child record linked to a parent `Greeting`. Etendo uses the `Trl` suffix to denote translation tables throughout the data model.

Note that the list property is retrieved with `getCurrentState` and appended to directly, rather than replaced with `setCurrentState`. This is because adding to an existing list does not require replacing the whole property value.

The trl object is a child of the Greeting event entity and will persist together with it, so it is not necessary to explicitly save it.
When you now enter a new entry in the window, you will see an additional translation child record being created.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-3.png)

###  Interrupt the Save Action

Sometimes you need to interrupt the save action because the user is doing something wrong. This can be done by throwing an `OBException`. When you do, Etendo displays the exception message to the user as an error dialog and rolls back the entire transaction, including any changes the event handler had already made.

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

##  Examples of Business Entity Event Handlers

Etendo uses business entity event handlers to implement business logic in various locations, here are some examples:

  * [ModuleHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/ModuleHandler.java){target="\_blank"}
  * [SetDocumentNoHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/SetDocumentNoHandler.java){target="\_blank"}

The complete source code of the example event handler is available here [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

---

This work is a derivative of [How to implement a business event handler](https://wiki.openbravo.com/wiki/How_to_implement_a_business_event_handler){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
