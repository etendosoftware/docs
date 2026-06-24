---
title: Cómo crear acciones de manejador de eventos del cliente
tags:
  - Guía práctica
  - Manejador de eventos del cliente
  - Acciones
  - Etendo Classic
---

# Cómo crear acciones de manejador de eventos del cliente { #how-to-create-client-event-handler-actions }

## Descripción general { #overview }

Esta página es una referencia de implementación práctica para la clase `GreetingEventHandler`. Cubre los cuatro métodos clave y proporciona un ejemplo de código consolidado. Para el contexto conceptual — incluyendo el framework Weld, la configuración del classpath, el alcance de la transacción y el filtrado — consulte [Cómo implementar un manejador de eventos de negocio](how-to-implement-a-business-event-handler.md).

## Módulo de ejemplo { #example-module }

Esto se respalda con un módulo de ejemplo que muestra ejemplos del código presentado y comentado.

El código de este módulo se puede descargar desde [este repositorio](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}.

## Referencia de métodos { #methods-reference }

| Método | Descripción |
| :--- | :--- |
| `getObservedEntities()` | Devuelve el array de entidades que este manejador observa; llamado internamente por `isValidEvent`. |
| `onUpdate()` | Se ejecuta cuando se actualiza un registro de una entidad observada. |
| `onSave()` | Se ejecuta cuando se crea un nuevo registro de una entidad observada. |
| `onDelete()` | Se ejecuta cuando se elimina un registro de una entidad observada. |

## Ejemplo de implementación completo { #complete-implementation-example }

La siguiente clase implementa los cuatro métodos para la entidad `Greeting`. El método `onSave` añade un punto al título cuando éste está ausente y, a continuación, crea un registro hijo `GreetingTrl` para el idioma 171 (neerlandés).

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

Este trabajo es una obra derivada de [How to Create Client Event Handler Actions](http://wiki.openbravo.com/wiki/How_to_create_client_event_handler_actions){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
