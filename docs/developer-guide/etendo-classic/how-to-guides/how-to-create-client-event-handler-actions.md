---
title: How to Create Client Event Handler Actions
tags:
  - How to
  - Client Event Handler
  - Actions
  - Etendo Classic
---

# How to Create Client Event Handler Actions

## Overview

This page shows the complete, ready-to-use `GreetingEventHandler` class and a summary of each method. Use it as a starting point when writing your own event handler. For the concepts behind how events work — including transaction scope, classpath setup, and entity filtering — see [How to Implement a Business Event Handler](how-to-implement-a-business-event-handler.md).

## Example Module

This is supported by an example module which shows examples of the code shown and discussed.

The code of this module can be downloaded from [this repository](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}.

!!!note
    The full list of required Java imports is available in the [example source file](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}.

## Methods Reference

| Method | Description |
| :--- | :--- |
| `getObservedEntities()` | Returns the array of entities this handler observes; called internally by `isValidEvent`. |
| `onUpdate()` | Executes when an observed entity record is updated. |
| `onSave()` | Executes when a new observed entity record is created. |
| `onDelete()` | Executes when an observed entity record is deleted. |

## Complete Implementation Example

The following class implements all four methods for the `Greeting` entity. The `onSave` method appends a dot to the title when one is absent, then creates a `GreetingTrl` child record for language 171 (Dutch).

```java title="GreetingEventHandler.java"
class GreetingEventHandler extends EntityPersistenceEventObserver {

  private static Entity[] entities = {
      ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
  private static final Logger logger = LogManager.getLogger();

  @Override
  protected Entity[] getObservedEntities() {
    return entities;
  }

  public void onUpdate(@Observes EntityUpdateEvent event) {
    if (!isValidEvent(event)) {
      return;
    }
    final Greeting greeting = (Greeting) event.getTargetInstance();
    final String title = greeting.getTitle();
    if (title != null && !title.endsWith(".")) {
      final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
      final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
      // use setCurrentState, not a setter on the instance
      event.setCurrentState(greetingTitleProperty, title + ".");
    }
    logger.info("Greeting {} is being updated", event.getTargetInstance().getId());
  }

  public void onSave(@Observes EntityNewEvent event) {
    if (!isValidEvent(event)) {
      return;
    }
    final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
    final Greeting greeting = (Greeting) event.getTargetInstance();
    final String title = greeting.getTitle();
    if (title != null && !title.endsWith(".")) {
      final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
      // use setCurrentState, not a setter on the instance
      event.setCurrentState(greetingTitleProperty, title + ".");
    }

    // create a translation child record for the new greeting
    final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
    greetingTrl.setGreeting(greeting);
    greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
    greetingTrl.setName(greeting.getName());
    greetingTrl.setTitle(greeting.getTitle());
    greetingTrl.setTranslation(false);

    // get the list property and add the child — no explicit save needed
    final Property greetingTrlProperty = greetingEntity.getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
    @SuppressWarnings("unchecked")
    final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
    greetingTrls.add(greetingTrl);

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

---

This work is a derivative of [How to Create Client Event Handler Actions](http://wiki.openbravo.com/wiki/How_to_create_client_event_handler_actions){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
