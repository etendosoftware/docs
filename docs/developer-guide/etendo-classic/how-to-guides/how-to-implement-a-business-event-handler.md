---
title: How to Implement a Business Event Handler
tags:
  - How to
  - Event Handler
  - Business Logic
  - Event Method
  - Client Event Handler
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
    For client-side (JavaScript) event handlers that run in the browser UI, see [Client Event Handler Actions](#client-event-handler-actions) below.

Choose a **server-side event handler** when you need to enforce business rules regardless of how the data is accessed — through the UI, an API call, or a background process. Choose a **client-side event handler** when you need to react to UI events in the browser, such as showing a message after a save, blocking a form submission with client-side validation, or refreshing a grid — without writing server-side logic.

##  Example Module

This section is supported by an example module which shows an example of the code shown and discussed here.

The code of the example module can be downloaded from this repository: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

!!!note
    The full list of required Java imports is available in the [example source file](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}. Copy the package declaration and all imports from the example source file before compiling — the snippet above omits them for brevity.

##  The event handler - A first implementation

An event handler is a normal Java class in your module that extends `EntityPersistenceEventObserver`. Weld automatically treats it as `@ApplicationScoped` — you do not need to add that annotation manually. The class is discovered from the annotations on the method parameters; no XML configuration is required.

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
    * The use of the `org.apache.logging.log4j.Logger` class is recommended for logging as shown above.

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

Let's walk through the code. First, cast the instance and get the title:

```java
final Greeting greeting = (Greeting) event.getTargetInstance();
final String title = greeting.getTitle();
```

If the title does not end on a dot then get the entity and the relevant property:

```java
if (title != null && !title.endsWith(".")) {
  final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
  final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
```

!!!note
    We use the generated constants to the entity name and property
    names, this gives compile time checking and is a recommended practice.

And then set the current state.

!!!note
    Use `event.setCurrentState(property, newValue)` to modify the entity — direct setters are ignored (see the warning above).

```java
event.setCurrentState(greetingTitleProperty, title + ".");
```

The changed entity instance does not need to be saved explicitly, this is done by the [data access layer](../concepts/data-access-layer.md) and hibernate automatically.

Then test the changes, go to the window ([http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)), enter a new greeting without a dot in the title.
When saving you will see a dot getting added.
Try updating the record, you will have the same behavior.

###  Adding a child instance

As the next step we will extend the `onSave` method to create a translation child record whenever a new `Greeting` is saved. The complete method below replaces the partial `onSave` shown in the previous section:

```java
public void onSave(@Observes EntityNewEvent event) {
  if (!isValidEvent(event)) {
    return;
  }

  final Greeting greeting = (Greeting) event.getTargetInstance();

  // Add a dot to the title if it does not already end with one
  final String title = greeting.getTitle();
  final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
  if (title != null && !title.endsWith(".")) {
    final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
    // note: use setCurrentState and not setters on the Greeting object directly
    event.setCurrentState(greetingTitleProperty, title + ".");
  }

  logger.info("Greeting {} is being created", event.getTargetInstance().getId());

  // Create a translation child record for this new Greeting
  final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
  greetingTrl.setGreeting(greeting);
  // 171 is Dutch — replace with any other Language ID as needed
  greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
  // note: getters on the targetInstance are safe; setters are not
  greetingTrl.setName(greeting.getName());
  greetingTrl.setTitle(greeting.getTitle());
  greetingTrl.setTranslation(false);

  // Retrieve the translation list property and append the new record.
  // We do not use event.setCurrentState here because we are appending to an
  // existing list, not replacing the whole property value.
  final Property greetingTrlProperty = greetingEntity
      .getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
  @SuppressWarnings("unchecked")
  final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
  greetingTrls.add(greetingTrl);

  // greetingTrl is a child of the Greeting entity and persists with it —
  // OBDal.getInstance().save(greetingTrl) is not needed
}
```

A `GreetingTrl` object is a translation child record linked to a parent `Greeting`. Etendo uses the `Trl` suffix to denote translation tables throughout the data model.

The list property is retrieved with `getCurrentState` and appended to directly, rather than replaced with `setCurrentState`. This is because adding to an existing list does not require replacing the whole property value.

The `greetingTrl` object is a child of the `Greeting` event entity and persists together with it, so it is not necessary to save it explicitly.

When you now enter a new entry in the window, you will see an additional translation child record being created.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-3.png)

###  Interrupt the Save Action

Sometimes you need to interrupt the save action because the user is doing something wrong. This can be done by throwing an `OBException`. When you do, Etendo displays the exception message to the user as an error dialog and rolls back the entire transaction, including any changes the event handler had already made.

The minimum import required is `org.openbravo.base.exception.OBException`.

```java
public void onSave(@Observes EntityNewEvent event) {
  if (!isValidEvent(event)) {
    return;
  }
  final Greeting greeting = (Greeting) event.getTargetInstance();
  if (greeting.getTitle() == null || greeting.getTitle().trim().isEmpty()) {
    throw new OBException("Greeting title must not be empty.");
  }
}
```

Etendo catches the `OBException`, rolls back the entire transaction, and displays the exception message to the user as an error dialog.

##  Examples of Business Entity Event Handlers

Etendo uses business entity event handlers to implement business logic in various locations, here are some examples:

  * [ModuleHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/ModuleHandler.java){target="\_blank"}
  * [SetDocumentNoHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/SetDocumentNoHandler.java){target="\_blank"}

The complete source code of the example event handler is available here [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

## Client Event Handler Actions

Client event handler actions are JavaScript functions that execute in the browser before or after a UI event fires on a standard Etendo window. Unlike server-side business event handlers — which run in Java when a record is persisted to the database — client handlers react to UI lifecycle events and can interact with the form, grid, and message bar directly.

**Available events**

| Event | When it fires |
| :--- | :--- |
| `OB.EventHandlerRegistry.POSTSAVE` | After a record is successfully saved |
| `OB.EventHandlerRegistry.PRESAVE` | Before the save request is sent to the server |
| `OB.EventHandlerRegistry.PREDELETE` | Before the delete request is sent to the server |

### Defining the Action

A client event handler action is a JavaScript function placed in a JS file within your module. Place it inside a global object using your module's DB prefix to avoid naming collisions.

Every action function must call `OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions)` before returning. If it does not, subsequent actions registered for the same event will not execute.

The function receives five parameters:

| Parameter | Description |
| :--- | :--- |
| `view` | `OBStandardView` — access to the complete window and tab structure |
| `form` | `OBViewForm` — the form containing the record fields |
| `grid` | `OBViewGrid` — the grid listing records for the tab |
| `extraParameters` | Event-specific data, e.g. `isNewRecord`, `data` |
| `actions` | The chain of actions to execute — do not modify this value |

**Example — show a message after save**

```javascript title="YourModule.js"
OB.MYMODULE = {};
OB.MYMODULE.ClientSideEventHandlers = {};

OB.MYMODULE.ClientSideEventHandlers.showMessage = function(view, form, grid, extraParameters, actions) {
  var data = extraParameters.data;

  view.messageBar.keepOnAutomaticRefresh = true;
  if (extraParameters.isNewRecord) {
    view.messageBar.setMessage(isc.OBMessageBar.TYPE_SUCCESS, 'New Record', 'Created: ' + data.name);
  } else {
    view.messageBar.setMessage(isc.OBMessageBar.TYPE_INFO, 'Updated Record', 'Updated: ' + data.name);
  }
  OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions); // Required: lets the next registered action execute
};
```

!!! warning
    Do not declare the global object with `var`. JavaScript code included in Etendo runs inside a function scope, so a `var` declaration would not be globally accessible.

### Registering the JavaScript File

The JS file you create must be served to the browser by Etendo. Without this step, the browser never loads the file and `OB.EventHandlerRegistry.register()` never executes.

Create a `ComponentProvider` class in your module that extends `BaseComponentProvider` and overrides `getGlobalComponentResources()`. This method returns the list of static files Etendo includes on every page load.

```java title="MyModuleComponentProvider.java"
import org.openbravo.client.kernel.BaseComponentProvider;
import org.openbravo.client.kernel.Component;
import org.openbravo.client.kernel.ComponentProvider;

import javax.enterprise.context.ApplicationScoped;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@ApplicationScoped
@ComponentProvider.Qualifier(MyModuleComponentProvider.MY_MODULE_VIEW_COMPONENT_TYPE)
public class MyModuleComponentProvider extends BaseComponentProvider {
    public static final String MY_MODULE_VIEW_COMPONENT_TYPE = "MYMOD_ViewType";

    @Override
    public Component getComponent(String componentId, Map<String, Object> parameters) {
        throw new IllegalArgumentException("Component id " + componentId + " not supported.");
    }

    @Override
    public List<ComponentResource> getGlobalComponentResources() {
        final List<ComponentResource> globalResources = new ArrayList<ComponentResource>();
        globalResources.add(createStaticResource(
                "web/com.mycompany.mymodule/js/my-event-handlers.js", false));
        return globalResources;
    }
}
```

The path passed to `createStaticResource()` must match the actual location of the JS file under the `web/` directory of your module. The second argument (`false`) controls whether the resource is also served in Etendo's classic UI mode. Pass `false` to include the resource only in the modern UI; pass `true` to include it in both modes.

Replace `com.mycompany.mymodule` with your module's Java package name — the same string used as the module's directory under `modules/`. The `js/my-event-handlers.js` segment is the path relative to the `web/<your-module>/` directory; the file must exist at that path for Etendo to serve it.

!!!note
    The `ComponentProvider` class must reside in the root package of your module — not in a sub-package. Weld discovers providers by scanning the classpath, and placing the class in a sub-package prevents discovery. For full details, see [Component Provider](../concepts/etendo-architecture.md#component-provider).

### Registering the Action

Register the action using `OB.EventHandlerRegistry.register()`. The registration call goes in the same JS file, after the function definition.

Before registering the action, find the `AD_Tab_ID` of the tab where it applies. Open **Application** > **Application Dictionary** > **Windows, Tabs and Fields**, locate the tab, and copy the ID. Alternatively, query the database: `SELECT AD_Tab_ID FROM AD_Tab WHERE Name = 'YourTabName';`

```javascript
OB.EventHandlerRegistry.register(
  TAB_ID,                                                    // the AD_Tab.AD_Tab_ID value
  OB.EventHandlerRegistry.POSTSAVE,                          // event type
  OB.MYMODULE.ClientSideEventHandlers.showMessage,           // action function
  'MYMODULE_ShowMessage'                                     // unique ID — use your module's DB prefix
);
```

The unique ID prevents conflicts with actions from other modules and allows overriding them.

### Multiple Actions and Execution Order

Multiple actions can be registered for the same tab and event. They execute sorted by a `sort` property on the callback function (default: `100`). When multiple actions share the same sort value, they execute in registration order. To control relative ordering, set `yourFunction.sort = <number>` before calling `register()`. To override an action defined by another module, register a new action with the same unique ID.

---

This work is a derivative of [How to implement a business event handler](https://wiki.openbravo.com/wiki/How_to_implement_a_business_event_handler){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
