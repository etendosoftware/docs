---
title: Cómo implementar un business event handler
tags:
  - Cómo hacerlo
  - Event Handler
  - Lógica de negocio
  - Método de evento
  - Client Event Handler
---

# Cómo implementar un business event handler { #how-to-implement-a-business-event-handler }

## Descripción general { #overview }

Un business entity event es un hook que ejecuta código Java automáticamente cuando un registro se guarda, actualiza o elimina. Los registros en el modelo de datos de Etendo se denominan entidades. Utilice los business entity events para aplicar reglas de negocio en Java en lugar de escribir triggers en la base de datos.

Los business entity events se ejecutan en la misma transacción que la operación que los origina. Cualquier cambio que realice en la entidad persiste junto con el cambio original. La [data access layer](../concepts/data-access-layer.md) completa está disponible dentro del código del event handler: puede consultar, crear y persistir objetos libremente.

!!! note "Comportamiento de los business entity events"
    - Los eventos se disparan antes de que la operación en la base de datos se complete, por lo que todavía puede modificar la entidad.
    - Los eventos solo se disparan cuando se accede a los datos a través de la data access layer. Las ventanas clásicas y las llamadas JDBC directas no los activan.

Los business events utilizan Weld, el framework de inyección de dependencias de Etendo, para descubrir y registrar automáticamente las clases event handler. Las anotaciones en los parámetros del método son suficientes; no se requiere configuración XML. Para más información, consulte [Weld](../concepts/etendo-architecture.md#introducing-weld-dependency-injection-and-more).

!!! note
    Ciertas partes del classpath se excluyen para maximizar el rendimiento. Si sus event handlers no se encuentran, consulte [esta sección](../concepts/etendo-architecture.md#analyzing-the-classpath).

El ejemplo de esta guía implementa un event handler sobre la entidad Greeting. Cada vez que se guarda un título, el handler añade una traducción al español. También registra mensajes en la consola para otros business events.

![Resultado del business event handler mostrando la ventana Greeting](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-0.png)
/// caption
La ventana Greeting utilizada a lo largo de este ejemplo.
///

!!! note
    Para los event handlers del lado del cliente (JavaScript) que se ejecutan en la interfaz del navegador, consulte [Acciones de Client Event Handler](#client-event-handler-actions) más abajo.

Elija un **event handler del lado del servidor** cuando necesite aplicar reglas de negocio independientemente de cómo se acceda a los datos — a través de la interfaz, una llamada a la API o un proceso en segundo plano. Elija un **event handler del lado del cliente** cuando necesite reaccionar a eventos de la interfaz en el navegador, como mostrar un mensaje después de guardar, bloquear el envío de un formulario o actualizar una grilla.

## Módulo de ejemplo { #example-module }

El código mostrado en esta guía está disponible en el siguiente módulo de ejemplo: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

!!! note
    La lista completa de importaciones Java necesarias está disponible en el [archivo fuente de ejemplo](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}. Copie la declaración del paquete y todas las importaciones de ese archivo antes de compilar — los fragmentos a continuación las omiten por brevedad.

## El event handler - Primera implementación { #the-event-handler---a-first-implementation }

Un event handler es una clase Java en su módulo que extiende `EntityPersistenceEventObserver`. Weld la trata automáticamente como `@ApplicationScoped` — no es necesario añadir esa anotación manualmente. Weld descubre la clase a partir de las anotaciones en los parámetros del método; no se requiere configuración XML.

!!! warning
    No llame a setters directamente en la entidad del evento. Cuando el evento se dispara, el framework de persistencia ya ha capturado los valores actuales de los campos del objeto. Llamar a un setter actualiza el objeto Java en memoria, pero Hibernate ya ha capturado los valores de las propiedades en su array de estado interno, por lo que el cambio se ignora silenciosamente y no se persistirá. Utilice `event.setCurrentState(property, newValue)` en su lugar. Esto se muestra en cada ejemplo de código de esta página.

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

!!! note
    - Extienda [EntityPersistenceEventObserver](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.kernel/src/org/openbravo/client/kernel/event/EntityPersistenceEventObserver.java){target="_blank"} para filtrar los eventos correctamente.
    - El nombre del método no es relevante. Weld detecta y registra el handler a partir de la anotación y el tipo del parámetro.
    - Utilice la clase `org.apache.logging.log4j.Logger` para el registro (logging).

### Resultado { #result }

Añada la clase a su módulo y reinicie el sistema. Abra la ventana de saludos en [http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282) y realice algunas acciones. La consola muestra mensajes como:

```bash
Greeting FF8081813097E041013097E805F4000F is being updated
Greeting FF8081813097E041013097E805F4000F is being deleted
Greeting FF8081813097E041013097E805F4000F is being created
```

!!! note
    - Implemente solo los métodos para los eventos que desea gestionar. Si solo necesita eventos de actualización, implemente únicamente el método con `@Observes EntityUpdateEvent`.
    - Cada método comienza con `isValidEvent` para filtrar solo los eventos relevantes. Consulte [Filtrar solo los eventos relevantes](#filtering-only-relevant-events) más abajo.
    - Utilice la API del objeto event para identificar el tipo de evento y acceder al estado actual y al estado previo de la entidad. Consulte [aquí](../concepts/etendo-architecture.md#event-classes-and-api) para más información.

### Filtrar solo los eventos relevantes { #filtering-only-relevant-events }

Todos los event handlers reciben eventos de todas las entidades del sistema, no solo de aquellas para las que fueron escritos. Si omite el filtro, su código se ejecutará en cada inserción, actualización y eliminación en toda la aplicación. La comprobación `isValidEvent` restringe la ejecución a las entidades listadas en `getObservedEntities`.

```java
private static Entity[] entities = { ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };

@Override
protected Entity[] getObservedEntities() {
  return entities;
}
```

`isValidEvent` llama a `getObservedEntities` internamente para determinar qué entidades son relevantes. Añada esta comprobación al inicio de cada método de gestión de eventos:

```java
if (!isValidEvent(event)) {
  return;
}
```

En este ejemplo, solo se gestionan los cambios en la entidad Greeting. Todos los demás eventos de entidad se filtran.

!!! note
    `isValidEvent` también devuelve `false` durante las operaciones de importación de datos. Esto es intencional — evita que la lógica de negocio se ejecute sobre datos importados. Si su event handler no se está disparando, compruebe si la operación se está realizando a través de un proceso de importación.

## Agregar lógica de negocio { #adding-business-logic }

Los siguientes ejemplos extienden el event handler con dos comportamientos:

- Añadir un punto al título del saludo en la creación o actualización, si no está ya presente.
- Crear un registro hijo de traducción cuando se guarda un nuevo saludo.

### Modificar la entidad en actualización o inserción { #changing-the-entity-on-update-or-insert }

Los métodos `onUpdate` y `onSave` actualizados a continuación añaden un punto al título si no termina ya con uno.

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

public void onSave(@Observes EntityNewEvent event) {
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

  logger.info("Greeting {} is being created", event.getTargetInstance().getId());
}
```

Obtenga la instancia con cast y lea el título:

```java
final Greeting greeting = (Greeting) event.getTargetInstance();
final String title = greeting.getTitle();
```

Si el título no termina en un punto, resuelva la entidad y la propiedad de destino:

```java
if (title != null && !title.endsWith(".")) {
  final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
  final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
```

!!! note
    Utilice las constantes generadas para los nombres de entidad y propiedad (`Greeting.ENTITY_NAME`, `Greeting.PROPERTY_TITLE`). Esto proporciona comprobación en tiempo de compilación y es la práctica recomendada.

Establezca el nuevo valor usando `event.setCurrentState`:

```java
event.setCurrentState(greetingTitleProperty, title + ".");
```

La entidad modificada no necesita guardarse explícitamente. La [data access layer](../concepts/data-access-layer.md) y Hibernate gestionan la persistencia automáticamente.

Abra la ventana de saludos en [http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282). Introduzca un nuevo saludo sin punto al final. Se añade un punto al guardar. El mismo comportamiento se aplica en la actualización.

### Agregar una instancia hija { #adding-a-child-instance }

El método `onSave` completo a continuación reemplaza la versión parcial de la sección anterior. Añade tanto la lógica del punto como un registro hijo de traducción al neerlandés cada vez que se guarda un nuevo saludo.

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
    event.setCurrentState(greetingTitleProperty, title + ".");
  }

  logger.info("Greeting {} is being created", event.getTargetInstance().getId());

  // Create a translation child record for this new Greeting
  final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
  greetingTrl.setGreeting(greeting);
  // 171 is Dutch — replace with any other Language ID as needed
  greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
  greetingTrl.setName(greeting.getName());
  greetingTrl.setTitle(greeting.getTitle());
  greetingTrl.setTranslation(false);

  // Retrieve the translation list property and append the new record.
  // Use getCurrentState here because the list already exists — appending does not replace the whole property.
  final Property greetingTrlProperty = greetingEntity
      .getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
  @SuppressWarnings("unchecked")
  final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
  greetingTrls.add(greetingTrl);

  // greetingTrl is a child of the Greeting entity and persists with it automatically
}
```

`GreetingTrl` es un registro hijo de traducción vinculado a un `Greeting` padre. Etendo utiliza el sufijo `Trl` para denominar las tablas de traducción en todo el modelo de datos.

La propiedad de lista se recupera con `getCurrentState` y el nuevo registro se añade directamente. Esto es correcto porque añadir a una lista existente no requiere reemplazar el valor completo de la propiedad con `setCurrentState`.

El objeto `greetingTrl` persiste junto con la entidad `Greeting` padre — no se necesita ninguna llamada explícita a save.

Introduzca un nuevo registro en la ventana de saludos. Se crea automáticamente un registro hijo de traducción adicional.

![Registro hijo de traducción creado por el event handler](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-3.png)
/// caption
Un registro hijo de traducción al neerlandés creado automáticamente al guardar.
///

### Interrumpir la acción de guardado { #interrupt-the-save-action }

Lance una `OBException` para cancelar un guardado cuando la entrada del usuario no es válida. Etendo captura la excepción, revierte la transacción completa — incluidos los cambios que el event handler ya hubiera realizado — y muestra el mensaje de la excepción al usuario como un diálogo de error.

La importación mínima requerida es `org.openbravo.base.exception.OBException`.

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

## Ejemplos de Business Entity Event Handlers { #examples-of-business-entity-event-handlers }

Etendo utiliza business entity event handlers para implementar lógica de negocio en varias ubicaciones. Ejemplos:

- [ModuleHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/ModuleHandler.java){target="_blank"}
- [SetDocumentNoHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/SetDocumentNoHandler.java){target="_blank"}

El código fuente completo del event handler de ejemplo está en [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples).

---

## Acciones de Client Event Handler { #client-event-handler-actions }

Los business event handlers del lado del servidor se ejecutan en Java cuando un registro se persiste. Las acciones de client event handler son diferentes: son funciones JavaScript que se ejecutan en el navegador antes o después de que se dispare un evento de la interfaz en una ventana estándar de Etendo. Los handlers del lado del cliente interactúan directamente con el formulario, la grilla y la barra de mensajes — no se requiere un viaje al servidor.

**Eventos disponibles**

| Evento | Cuándo se dispara |
| :--- | :--- |
| `OB.EventHandlerRegistry.POSTSAVE` | Después de que un registro se guarda correctamente |
| `OB.EventHandlerRegistry.PRESAVE` | Antes de que la solicitud de guardado se envíe al servidor |
| `OB.EventHandlerRegistry.PREDELETE` | Antes de que la solicitud de eliminación se envíe al servidor |

### Definir la acción { #defining-the-action }

Una acción de client event handler es una función JavaScript ubicada en un archivo JS dentro de su módulo. Colóquela dentro de un objeto global usando el prefijo de base de datos de su módulo para evitar colisiones de nombres.

Toda función de acción debe llamar a `OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions)` antes de retornar. Si no lo hace, las acciones subsiguientes registradas para el mismo evento no se ejecutarán.

La función recibe cinco parámetros:

| Parámetro | Descripción |
| :--- | :--- |
| `view` | `OBStandardView` — acceso a la estructura completa de ventana y solapa |
| `form` | `OBViewForm` — el formulario que contiene los campos del registro |
| `grid` | `OBViewGrid` — la grilla que lista los registros de la solapa |
| `extraParameters` | Datos específicos del evento, p. ej. `isNewRecord`, `data` |
| `actions` | La cadena de acciones a ejecutar — no modifique este valor |

**Ejemplo — mostrar un mensaje después de guardar**

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
    No declare el objeto global con `var`. El código JavaScript incluido en Etendo se ejecuta dentro de un ámbito de función, por lo que una declaración `var` no es accesible globalmente.

### Registrar el archivo JavaScript { #registering-the-javascript-file }

El archivo JS debe ser servido al navegador por Etendo. Sin este paso, el navegador nunca carga el archivo y `OB.EventHandlerRegistry.register()` nunca se ejecuta.

Cree una clase `ComponentProvider` en su módulo que extienda `BaseComponentProvider` y sobreescriba `getGlobalComponentResources()`. Este método devuelve la lista de archivos estáticos que Etendo incluye en cada carga de página.

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

La ruta que se pasa a `createStaticResource()` debe coincidir con la ubicación real del archivo JS bajo el directorio `web/` de su módulo. El segundo argumento (`false`) controla si el recurso se sirve en el modo de interfaz clásica de Etendo. Pase `false` para incluir el recurso solo en la interfaz moderna; pase `true` para incluirlo en ambas.

Reemplace `com.mycompany.mymodule` con el nombre del paquete Java de su módulo — la misma cadena utilizada como directorio del módulo bajo `modules/`. El segmento `js/my-event-handlers.js` es la ruta relativa al directorio `web/<su-modulo>/`; el archivo debe existir en esa ruta para que Etendo lo sirva.

!!! note
    La clase `ComponentProvider` debe residir en el paquete raíz de su módulo — no en un subpaquete. Weld descubre los providers escaneando el classpath, y ubicar la clase en un subpaquete impide su descubrimiento. Para más detalles, consulte [Component Provider](../concepts/etendo-architecture.md#component-provider).

### Registrar la acción { #registering-the-action }

Registre la acción usando `OB.EventHandlerRegistry.register()`. La llamada de registro va en el mismo archivo JS, después de la definición de la función.

Antes de registrar, encuentre el `AD_Tab_ID` de la solapa donde aplica la acción. Abra **Aplicación** > **Diccionario de la Aplicación** > **Ventanas, solapas y campos**, localice la solapa y copie el ID. Alternativamente, consulte la base de datos: `SELECT AD_Tab_ID FROM AD_Tab WHERE Name = 'YourTabName';`

```javascript
OB.EventHandlerRegistry.register(
  TAB_ID,                                                    // the AD_Tab.AD_Tab_ID value
  OB.EventHandlerRegistry.POSTSAVE,                          // event type
  OB.MYMODULE.ClientSideEventHandlers.showMessage,           // action function
  'MYMODULE_ShowMessage'                                     // unique ID — use your module's DB prefix
);
```

El ID único previene conflictos con acciones de otros módulos y permite sobreescribirlas.

### Múltiples acciones y orden de ejecución { #multiple-actions-and-execution-order }

Se pueden registrar múltiples acciones para la misma solapa y evento. Se ejecutan ordenadas por una propiedad `sort` en la función de callback (valor predeterminado: `100`). Cuando múltiples acciones comparten el mismo valor de sort, se ejecutan en orden de registro. Establezca `yourFunction.sort = <número>` antes de llamar a `register()` para controlar el orden relativo. Para sobreescribir una acción definida por otro módulo, registre una nueva acción con el mismo ID único.

---

Este trabajo es una obra derivada de [How to implement a business event handler](https://wiki.openbravo.com/wiki/How_to_implement_a_business_event_handler){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.
