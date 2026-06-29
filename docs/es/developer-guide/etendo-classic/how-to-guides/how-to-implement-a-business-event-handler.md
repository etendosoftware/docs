---
title: Cómo implementar un business event handler
tags:
  - Cómo
  - Event Handler
  - Lógica de negocio
  - Método de evento
  - Client Event Handler
---

# Cómo implementar un business event handler { #how-to-implement-a-business-event-handler }

## Descripción general { #overview }

Un business entity event es un hook que ejecuta automáticamente su código Java cuando un registro — denominado entidad en el modelo de datos de Etendo — se guarda, actualiza o elimina. Esto le permite aplicar reglas de negocio en Java en lugar de escribir triggers en la base de datos.
Los business entity events se corresponden con triggers en la base de datos.
La principal ventaja de implementar lógica usando business entity events en lugar de triggers es que puede programar su lógica en Java usando su IDE.
Esto ayuda a la productividad y a la calidad, ya que puede programar, depurar y probar en un entorno integrado con el resto de su lógica de negocio.

!!! note "Algunas notas sobre los business entity events:"
    * Se disparan cuando una instancia de entidad se actualiza, elimina o inserta. Antes de que la operación real se haya realizado en la base de datos, por lo que puede cambiar o añadir información que persiste junto con la entidad del evento.
    * Su código de gestión de eventos se ejecuta en la misma transacción que el evento de negocio; los cambios que realice en la base de datos persisten junto con el business entity event en una única transacción.
    * Los business entity events solo funcionan cuando se accede a la base de datos a través de la data access layer, por lo que no funcionan para ventanas clásicas o llamadas JDBC directas.
    * Puede hacer uso de toda la funcionalidad de la [data access layer](../concepts/data-access-layer.md) en su código de gestión de eventos: puede consultar, crear nuevos objetos, persistir, etc.


Los eventos de negocio utilizan Weld, el framework de inyección de dependencias de Etendo, para descubrir y registrar automáticamente su clase event handler. No es necesario configurar Weld directamente; las anotaciones en su clase son suficientes. Para más información, consulte [Weld](../concepts/etendo-architecture.md#introducing-weld-dependency-injection-and-more).

!!!note
    Para maximizar el rendimiento, se excluyen ciertas partes del classpath; consulte [esta sección](../concepts/etendo-architecture.md#analyzing-the-classpath) si no se encuentran sus event handlers.

En esta sección, implementaremos un event handler sobre la entidad Tratamientos. Cada vez que se guarde un título, se añadirá una traducción al español. Además, imprimiremos algunos mensajes en la consola para otros eventos de negocio.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-0.png)

!!!note
    Para los event handlers del lado del cliente (JavaScript) que se ejecutan en la interfaz del navegador, consulte [Acciones de Client Event Handler](#client-event-handler-actions) más abajo.

Elija un **event handler del lado del servidor** cuando necesite aplicar reglas de negocio independientemente de cómo se acceda a los datos — a través de la interfaz, una llamada a la API o un proceso en segundo plano. Elija un **event handler del lado del cliente** cuando necesite reaccionar a eventos de la interfaz en el navegador, como mostrar un mensaje después de guardar, bloquear el envío de un formulario con validación del lado del cliente, o actualizar una grilla — sin escribir lógica del lado del servidor.

## Módulo de ejemplo { #example-module }

Esta sección está respaldada por un módulo de ejemplo que muestra un ejemplo del código mostrado y comentado aquí.

El código del módulo de ejemplo puede descargarse desde este repositorio: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

!!!note
    La lista completa de importaciones Java necesarias está disponible en el [archivo fuente de ejemplo](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/GreetingEventHandler.java){target="_blank"}. Copie la declaración del paquete y todas las importaciones del archivo fuente de ejemplo antes de compilar — el fragmento anterior las omite por brevedad.

## El event handler - Primera implementación { #the-event-handler---a-first-implementation }

Un event handler es una clase Java normal en su módulo que extiende `EntityPersistenceEventObserver`. Weld la trata automáticamente como `@ApplicationScoped` — no es necesario añadir esa anotación manualmente. La clase se descubre a partir de las anotaciones en los parámetros del método; no se requiere configuración XML.

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
    * Se recomienda el uso de la clase `org.apache.logging.log4j.Logger` para el registro (logging), tal y como se muestra arriba.

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
    * Solo necesita implementar un método para el evento que desea escuchar; por lo tanto, si solo necesita escuchar eventos de actualización, implemente únicamente un método con el parámetro @Observes EntityUpdateEvent.
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

## Agregar lógica de negocio { #adding-some-business-logic }

En este siguiente paso, añadimos lógica al event handler:

  * Cada vez que se cree o actualice un tratamiento, añadir un `.` al título, si no estaba ya ahí.
  * Cuando se cree un nuevo tratamiento, añadir una traducción para él.

!!!note
    Para crear una nueva traducción cuando se añade un nuevo tratamiento.
    En este ejemplo, añadiremos una traducción al neerlandés.

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

Repasemos el código. En primer lugar, obtenga la instancia con cast y el título:

```java
final Greeting greeting = (Greeting) event.getTargetInstance();
final String title = greeting.getTitle();
```

Si el título no termina en un punto, obtenga la entidad y la propiedad relevante:

```java
if (title != null && !title.endsWith(".")) {
  final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
  final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
```

!!!note
    Usamos las constantes generadas para el nombre de la entidad y los nombres de propiedades; esto proporciona comprobación en tiempo de compilación y es una práctica recomendada.

Y, a continuación, establezca el estado actual.

!!!note
    Utilice `event.setCurrentState(property, newValue)` para modificar la entidad — los setters directos se ignoran (consulte el aviso anterior).

```java
event.setCurrentState(greetingTitleProperty, title + ".");
```

La instancia de entidad modificada no necesita guardarse explícitamente; esto lo realiza la [data access layer](../concepts/data-access-layer.md) y Hibernate automáticamente.

A continuación, pruebe los cambios: vaya a la ventana ([http://localhost:8080/etendo/?tabId=282](http://localhost:8080/etendo/?tabId=282)) e introduzca un nuevo tratamiento sin punto en el título.
Al guardar, verá que se añade un punto.
Intente actualizar el registro; tendrá el mismo comportamiento.

### Añadir una instancia hija { #adding-a-child-instance }

Como siguiente paso, extenderemos el método `onSave` para crear un registro hijo de traducción cada vez que se guarde un nuevo `Greeting`. El método completo que se muestra a continuación reemplaza el `onSave` parcial de la sección anterior:

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

Un objeto `GreetingTrl` es un registro hijo de traducción vinculado a un `Greeting` padre. Etendo utiliza el sufijo `Trl` para denominar las tablas de traducción en todo el modelo de datos.

La propiedad de lista se recupera con `getCurrentState` y se le añaden elementos directamente, en lugar de reemplazarla con `setCurrentState`. Esto se debe a que añadir elementos a una lista existente no requiere reemplazar el valor completo de la propiedad.

El objeto `greetingTrl` es hijo de la entidad del evento `Greeting` y persiste junto con ella, por lo que no es necesario guardarlo explícitamente.

Cuando ahora introduzca una nueva entrada en la ventana, verá que se crea un registro hijo adicional de traducción.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_implement_a_business_event_handler-3.png)

### Interrumpir la acción de guardado { #interrupt-the-save-action }

En ocasiones necesita interrumpir la acción de guardado porque el usuario está realizando algo incorrecto. Esto puede hacerse lanzando una `OBException`. Al hacerlo, Etendo muestra el mensaje de la excepción al usuario como un diálogo de error y revierte la transacción completa, incluidos los cambios que el event handler ya hubiera realizado.

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

Etendo captura la `OBException`, revierte la transacción completa y muestra el mensaje de la excepción al usuario como un diálogo de error.

## Ejemplos de business entity event handlers { #examples-of-business-entity-event-handlers }

Etendo utiliza business entity event handlers para implementar lógica de negocio en varias ubicaciones; aquí tiene algunos ejemplos:

  * [ModuleHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/ModuleHandler.java){target="\_blank"}
  * [SetDocumentNoHandler](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.client.application/src/org/openbravo/client/application/event/SetDocumentNoHandler.java){target="\_blank"}

El código fuente completo del event handler de ejemplo está disponible aquí: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

## Acciones de Client Event Handler { #client-event-handler-actions }

Las acciones de client event handler son funciones JavaScript que se ejecutan en el navegador antes o después de que se dispare un evento de la interfaz en una ventana estándar de Etendo. A diferencia de los business event handlers del lado del servidor — que se ejecutan en Java cuando un registro se persiste en la base de datos — los handlers del lado del cliente reaccionan a eventos del ciclo de vida de la interfaz y pueden interactuar directamente con el formulario, la grilla y la barra de mensajes.

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
    No declare el objeto global con `var`. El código JavaScript incluido en Etendo se ejecuta dentro de un ámbito de función, por lo que una declaración `var` no sería accesible globalmente.

### Registrar el archivo JavaScript { #registering-the-javascript-file }

El archivo JS que cree debe ser servido al navegador por Etendo. Sin este paso, el navegador nunca carga el archivo y `OB.EventHandlerRegistry.register()` nunca se ejecuta.

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

La ruta que se pasa a `createStaticResource()` debe coincidir con la ubicación real del archivo JS bajo el directorio `web/` de su módulo. El segundo argumento (`false`) controla si el recurso también se sirve en el modo de interfaz clásica de Etendo. Pase `false` para incluir el recurso solo en la interfaz moderna; pase `true` para incluirlo en ambos modos.

Reemplace `com.mycompany.mymodule` con el nombre del paquete Java de su módulo — la misma cadena utilizada como directorio del módulo bajo `modules/`. El segmento `js/my-event-handlers.js` es la ruta relativa al directorio `web/<su-modulo>/`; el archivo debe existir en esa ruta para que Etendo lo sirva.

!!!note
    La clase `ComponentProvider` debe residir en el paquete raíz de su módulo — no en un subpaquete. Weld descubre los providers escaneando el classpath, y ubicar la clase en un subpaquete impide su descubrimiento. Para más detalles, consulte [Component Provider](../concepts/etendo-architecture.md#component-provider).

### Registrar la acción { #registering-the-action }

Registre la acción usando `OB.EventHandlerRegistry.register()`. La llamada de registro va en el mismo archivo JS, después de la definición de la función.

Antes de registrar la acción, encuentre el `AD_Tab_ID` de la solapa donde aplica. Abra **Aplicación** > **Diccionario de la Aplicación** > **Ventanas, solapas y campos**, localice la solapa y copie el ID. Alternativamente, consulte la base de datos: `SELECT AD_Tab_ID FROM AD_Tab WHERE Name = 'YourTabName';`

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

Se pueden registrar múltiples acciones para la misma solapa y evento. Se ejecutan ordenadas por una propiedad `sort` en la función de callback (valor predeterminado: `100`). Cuando múltiples acciones comparten el mismo valor de sort, se ejecutan en orden de registro. Para controlar el orden relativo, establezca `yourFunction.sort = <número>` antes de llamar a `register()`. Para sobreescribir una acción definida por otro módulo, registre una nueva acción con el mismo ID único.

---

Este trabajo es una obra derivada de [How to implement a business event handler](https://wiki.openbravo.com/wiki/How_to_implement_a_business_event_handler){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
