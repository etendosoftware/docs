---
title: Desarrollo del lado del cliente y API
tags:
  - Desarrollo del lado del cliente
  - API
  - Plataforma
  - Javascript

status: beta
---

# Desarrollo del lado del cliente y API

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
## Herramientas de desarrollo del lado del cliente

El desarrollo del lado del cliente es una combinación de `javascript`, `css` y `html` muy limitado. La programación se realiza en `javascript`, que se carga en el navegador. El navegador es la principal plataforma cliente. Dentro del cliente utilizamos las siguientes herramientas de desarrollo:

- Herramientas para desarrolladores de Chrome
- Firebug

En esta página, mostraremos las **Herramientas para desarrolladores de Chrome**, ya que es la herramienta que utilizamos la mayor parte del tiempo.
## Procesamiento de código javascript en Etendo

Al desarrollar código del lado del cliente, es importante entender cómo Etendo preprocesa el código javascript antes de enviarlo al navegador. Es importante leer la sección de caché y compresión de la guía del desarrollador.

Etendo concatenará todos los recursos estáticos (javascript y css) en un único archivo grande antes de enviarlo al cliente. Si ningún módulo está marcado como en desarrollo, se minimizará/comprimirá (usando jsmin).

El código javascript se genera en un archivo que tiene un nombre basado en un GUID (por ejemplo, `088afd247a8fe06c91a654891a1358a2.js`). Este GUID, a su vez, se basa en el contenido del archivo, por lo que si el javascript cambia, también cambia el nombre del archivo js (y, por tanto, se recarga en el navegador). El archivo js se genera en la carpeta web/js/gen y se sirve desde ahí al cliente.

!!! Note
    El código fuente de Smartclient siempre se entrega minimizado y ofuscado. Consulte la siguiente sección para obtener información sobre cómo conseguir una versión de Smartclient no ofuscada.
## El módulo smartclient.dev, la consola de smartclient y los fuentes

Cuando trabaje con código del lado del cliente de Etendo, puede tener sentido instalar también el módulo con el código fuente de smartclient. Puede encontrarlo aquí. Para instalarlo, vaya al directorio de módulos en su proyecto de desarrollo y, en la consola, escriba lo siguiente:

```
git clone https://bitbucket.org/koodu_software/org.openbravo.userinterface.smartclient.dev
```

y en el directorio raíz del proyecto haga esto:

```
./gradlew smartbuild -Dlocal=no
```

Y actualice Eclipse para que Eclipse detecte el contenido de los módulos. Dentro de Eclipse puede abrir un archivo js de smartclient con la combinación de teclas: shift-ctrl-r; introduzca, por ejemplo, FormItem.js para ver el código fuente de FormItem.

Después de instalar el módulo de fuentes de smartclient, también puede usar la consola de smartclient en el cliente. En la barra de direcciones del navegador (después de cargar Etendo) haga esto:

`javascript:isc.showConsole();`

Dentro del módulo `smartclient.dev` puede encontrar el directorio docs, que contiene el manual de referencia y la guía de inicio rápido.
## Obtener javascript no minimizado y no ofuscado

Tal y como se explicó anteriormente, Etendo intentará automáticamente minimizar el código javascript para obtener el mejor rendimiento de carga. Sin embargo, esto hace que la depuración en el lado del cliente sea muy difícil; por lo tanto, existe una forma sencilla de evitar la minimización del javascript.

### Javascript de Etendo

El javascript de los módulos se minimiza si el módulo no está en desarrollo. Por tanto, para evitar la minimización de su javascript, ponga su módulo en desarrollo. Los módulos más habituales que se tienen en desarrollo para Etendo son:

- `org.openbravo.client.kernel` 
- `org.openbravo.client.application`
- `org.openbravo.userinterface.selector` 

### Código de Smartclient

La librería Smartclient normalmente está minimizada/ofuscada, ya que esto ofrece el mejor rendimiento al cargar las librerías. Sin embargo, para depurar y comprender el código fuente, resulta de gran ayuda tener cargado en el cliente el código no ofuscado. Para usar el código no ofuscado en el navegador, debe instalar el módulo `org.openbravo.userinterface.smartclient.dev` (y ejecutar `ant smartbuild -Dlocal=no` después de instalarlo).

A continuación, inicie la aplicación y ponga `org.openbravo.userinterface.smartclient.dev` en desarrollo. Después de eso, reinicie la aplicación.

Entonces, al depurar (consulte la siguiente sección), puede ver/usar el código fuente de Smartclient no minimizado:

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-0.png)
## Depuración de código del lado del cliente

La depuración de código del lado del cliente se realiza mediante las Chrome Developers Tools. Tras abrir Etendo en una ventana del navegador, abra las Chrome Dev Tools. Haga clic en el botón **Scripts** en la parte superior y, en el desplegable justo debajo, busque el archivo que tiene un nombre similar a un GUID.

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-1.png)

Este archivo js contiene el código javascript completo concatenado; algunas observaciones:

- el nombre del archivo es un GUID generado dinámicamente; es diferente en distintas instalaciones y versiones de Etendo
- si el javascript está minimizado, ponga uno de los módulos core, client application o client kernel en modo desarrollo y reinicie la aplicación
- el código javascript de Smartclient no está incluido en este archivo

### Crear un breakpoint

Las herramientas de desarrollo de Chrome ofrecen varias formas de establecer breakpoints. Por ejemplo, pausar en excepción o pausar en excepciones no capturadas.

Para realizar una depuración, introduzca esta cadena `this.messageBar = isc.OBMessageBar.create({` como cadena de búsqueda en el campo de búsqueda de la parte superior.  
A continuación, haga clic a la izquierda, sobre el número de línea, para crear un breakpoint. Ahora, para probar el breakpoint, abra una ventana en Etendo. El breakpoint debería activarse.

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-2.png)

### Búsqueda de componentes globales y de Smartclient

Todos los componentes de Smartclient son accesibles globalmente:

- Las definiciones de clase están todas en el objeto `isc`.
- Las instancias se almacenan en variables globales con esta estructura: `isc_[ClassName]_[SequenceNumber]`, por ejemplo `isc_OBViewGrid_0`, `isc_OBViewForm_0`.

Puede escribir las variables globales y los objetos directamente en la consola:

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-3.png)

### Búsqueda de errores de javascript en su propio código, deteniéndose en excepciones

Cuando se produce una excepción en su código javascript y tiene abiertas las herramientas de desarrollo de Chrome, a menudo las herramientas de desarrollo de Chrome detendrán la ejecución del programa en código ofuscado de Smartclient.

Para que el depurador se detenga en su propio código, permita que Chrome se detenga en excepción. Esto se describe con más detalle aquí: pausar en excepción o pausar en excepciones no capturadas.
## Análisis de solicitudes cliente-servidor

Mientras trabaja con Etendo, el sistema realizará varias solicitudes al sistema. Las solicitudes se realizan para imágenes, datos y definiciones de vistas. Las Chrome Developers Tools proporcionan la pestaña de red para ver qué solicitudes tienen lugar realmente. Las más interesantes son las solicitudes xhr.

La imagen siguiente ilustra las solicitudes realizadas al abrir la ventana de producto:

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-4.png)

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-5.png)

  
Un resumen:

- la solicitud de vista obtiene del servidor el código javascript para la ventana de producto (y todas sus solapas). Esta llamada solo se realiza si la vista no se ha almacenado en caché en la caché del navegador.
- la primera solicitud `org.openbravo.client.kernel` obtiene la información dinámica relacionada con esta ventana; esta llamada nunca se almacena en caché.
- Product y PricingProductPrice son las denominadas solicitudes de datasource; obtienen los registros mostrados en las rejillas y formularios. Solo se recuperan los datos de las solapas visibles.
- las otras solicitudes `org.openbravo.client.kernel` son llamadas al gestor de alertas; comprueba si hay alertas abiertas.

Puede ver el contenido devuelto haciendo clic en la pestaña de contenido.
## Añadir javascript a Etendo

En Etendo, una parte significativa de la lógica se implementa en javascript (generado). Los proveedores de soluciones que implementan nueva funcionalidad también pueden añadir nueva funcionalidad en javascript. Etendo se encarga de comprobar, minimizar, cargar y cachear el javascript. Para hacer uso de esta funcionalidad del framework, el javascript debe añadirse a Etendo de la siguiente manera:

- el javascript estático debe ubicarse en archivos en este subdirectorio del módulo: `web/[modulepackage]/js`
- el javascript debe registrarse en Etendo usando java, implementado en un denominado ComponentProvider. Esto se explica con más detalle aquí. A continuación se muestra un fragmento de código que muestra cómo se registra un archivo js:

```
globalResources.add(createStaticResource(
    "web/org.openbravo.client.application.examples/js/example-view-component.js", true));
```

!!!info
    Al implementar sus propios componentes, a menudo tiene sentido ampliar componentes existentes. Asegúrese de que su módulo dependa entonces del módulo que proporciona los tipos base. Esto garantiza que el javascript se cargue en el orden correcto. **Debe** añadir una dependencia desde su módulo al módulo **Openbravo 3.0 Framework** _(org.openbravo.v3.framework)_.
## Pruebas unitarias de código Javascript

Hay disponible una infraestructura para realizar pruebas unitarias de código javascript usando Jest. Para más detalles, consulte [Cómo crear casos de prueba de Jest](../how-to-guides/how-to-create-testcases/how-to-create-jest-testcases.md)
## Implementación de objetos javascript globales *singleton*

Al crear objetos javascript globales *singleton*, es una buena práctica añadir estos objetos a un único objeto global para evitar la contaminación del espacio de nombres global.

La recomendación es utilizar tanto el objeto javascript global existente de Etendo como el prefijo de BD del módulo. Por ejemplo, el módulo Etendo Application Example tiene el prefijo de BD `OBEXAPP`. La forma correcta de crear un *singleton* global es:

```
OB.OBEXAPP = {};
OB.OBEXAPP.OnChangeFunctions = {};
```

Por lo tanto, primero cree/añada un Objeto al objeto global de Etendo; el Objeto añadido debe nombrarse usando el prefijo de BD del módulo. A continuación, las Propiedades específicas de la aplicación pueden añadirse a este objeto global.
## Componentes del lado del cliente de Etendo - API de Javascript

Al añadir nuevas instancias y nuevas clases, Etendo sigue esta convención:

- todos los datos globales se añaden al objeto global Etendo
- todos los nombres de estilo CSS comienzan por Etendo
- todos los nombres de clase de Smartclient comienzan por Etendo

En esta sección, se analiza el contenido del objeto principal de Etendo y las funciones de utilidad disponibles en él.
### Arquitectura de la UI - Publicación del blog

Este blog contiene una imagen útil que muestra la arquitectura de la UI y vincula los componentes de la UI con los tipos/código de javascript.

### OB.Application - información general de la aplicación

El objeto `OB.Application` contiene datos sobre la aplicación del lado del servidor:

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-7.png)
### OB.User - el usuario actual

El objeto `OB.User` contiene información relacionada con el usuario actualmente conectado:

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-8.png)
### OB.Constants - constantes comunes

El objeto `OB.Constants` contiene constantes que se utilizan en toda la aplicación. Incluye nombres de constantes para parámetros que se utilizan en las solicitudes al servidor y para retardos.
### OB.Datasource - obtención de fuentes de datos estándar y personalizadas

El objeto `OB.Datasource` proporciona dos métodos: create y get.

El método get primero comprobará si hay una fuente de datos definida en el cliente para el id solicitado. Si es así, se devuelve directamente; si no, se llama al servidor para generar la definición de la fuente de datos (en javascript) y devolverla. El javascript devuelto se evalúa y la fuente de datos creada se establece en el objeto destino (llamando a su método `setDataSource` o estableciéndola en su propiedad `dsFieldName`).

La persona que llama a la función `OB.Datasource.get` debe tener en cuenta que su comportamiento es asíncrono.

```
    // ** {{{ OB.Datasource.get(dataSourceId, target, dsFieldName) }}} **
    //
    // Retrieves a datasource from the server. The return from the server is a
    // javascript string which is evaluated. This string creates a datasource. The
    // datasource
    // object is set in a field of the target (if the target parameter is set). This
    // is done asynchronously.
    //
    // The method returns the datasourceid.
    //
    // Parameters:
    // * {{{dataSourceId}}}: the id or name of the datasource
    // * {{{target}}}: the target object which needs the datasource
    // * {{{dsFieldName}}}: the field name to set in the target object.
    // * {{{doNew}}}: if set to true then a new datasource is created
    // If not set then setDataSource or optionDataSource are used.
    //
    OB.Datasource.get = function(/* String */dataSourceId, /* Object */
    target, /* String */dsFieldName, /*Boolean*/ doNew) {
    ...
    }
```

El método create no llama al servidor, sino que crea la fuente de datos directamente en el cliente, utilizando las propiedades pasadas. Antes de crear la nueva fuente de datos, realiza una comprobación para ver si la fuente de datos ya se ha creado; si es así, se devuelve.

```
    // ** {{{ OB.Datasource.create}}} **
    // Performs a last check if the datasource was already registered before
    // actually creating it, prevents re-creating datasources when multiple
    // async requests are done for the same datasource.
    // Parameters:
    // * {{{dsProperties}}}: the properties of the datasource which needs to be
    // created.
    OB.Datasource.create = function(/* Object */dsProperties) {
```

El objeto `OB.Datasource` crea fuentes de datos utilizando la clase javascript `isc.OBRestDataSource`, que amplía la clase RestDataSource de Smartclient.
### OB.Format - patrones de formato

El objeto `OB.Format` contiene la configuración global de formato del usuario actual en relación con las fechas y el formato de números. Tenga en cuenta que el formato de campos específicos está controlado por la definición de Format.xml y no por este objeto.

![](../../../assets/developer-guide/etendo-classic/concepts/Client_Side_Development_and_API-9.png)
### OB.I18N - obtención de etiquetas

El objeto `OB.I18N` proporciona un método `getLabel` que puede utilizarse para obtener una etiqueta traducida del sistema. El método `getLabel` tiene 4 parámetros:

- **Key**: la clave en la tabla `AD_Message` para la etiqueta
- **Parámetros**: null, o un array de parámetros; si la etiqueta contiene parámetros (50. %1, etc.), entonces se sustituyen por los valores del array
- **Objeto** y **Propiedad**: cuando se establecen, entonces la etiqueta se asigna en esa propiedad del objeto, o si la propiedad es una función, entonces se invoca sobre el objeto con la etiqueta como parámetro. Consulte también la carga asíncrona a continuación.

El sistema precargará todos los registros de `AD_Message` que no formen parte del módulo core. Esto significa que, si intenta obtener una etiqueta definida en core, la función `getLabel` funcionará de forma asíncrona:

- inicialmente devolverá la clave y llamará al servidor para obtener la etiqueta (de forma asíncrona)
- cuando se devuelve la etiqueta, entonces (tras la sustitución de parámetros) la etiqueta se asigna en el objeto usando la propiedad; si la propiedad es una función, entonces se invoca como función con la etiqueta como parámetro; si no es una función, entonces la etiqueta se asigna en el objeto usando la propiedad.
### OB.PropertyStore - gestión de preferencias

Etendo dispone de una funcionalidad para definir preferencias en distintos niveles (sistema, cliente, organización, rol, usuario, ventana) y establecerlas y obtenerlas desde el sistema. Cuando un usuario carga la aplicación, todas las preferencias relevantes se precargan en el cliente.

La aplicación puede hacer uso de estas preferencias en el cliente e incluso establecerlas. Cuando se establece una preferencia, el cliente llamará al servidor para actualizar el valor en la base de datos.

La obtención y el establecimiento de preferencias se implementa en el cliente mediante el objeto `OB.PropertyStore`. Tiene 2 métodos:

- **get**: function(propertyName, windowId): devuelve el valor de una Propiedad para una determinada ventana

    ``` 
    dataPageSizeaux = OB.PropertyStore.get('dataPageSize',this.view.windowId);
    ```

- **set**: function(propertyName, value, windowId, noSetInServer, setAsSystem): establece el valor de una Propiedad, para una determinada ventana. El llamador puede evitar el establecimiento en el servidor pasando `noSetInServer` como `true` y, si se establece en el servidor, puede controlar en qué nivel se realiza estableciendo `setAsSystem` como `true`

    ```
    OB.PropertyStore.set('OBUIAPP_GridConfiguration', result, this.windowId);
    ```

El `OB.PropertyStore` dispone del concepto de **listener**, que permite registrar un listener que recibe notificaciones cuando cambia el valor de una Propiedad. Esto se utiliza para actualizar la lista de vistas recientes en la solapa Etendo Workspace. Para registrar un listener, llame al método `addListener` en el `OB.PropertyStore`; tiene un parámetro, el listener, que debe ser una función. Para cada cambio de Propiedad, se llama al listener con estos parámetros:

- **identificador de Propiedad**: concatenación del nombre de la Propiedad y el id de la ventana, separados por un guion bajo.
- **valor anterior**: el valor anterior de la Propiedad.
- **Nuevo valor**: el nuevo valor de la Propiedad.
### OB.RemoteCallManager - Llamar al servidor desde el cliente

El `RemoteCallManager` se utiliza para llamar a ActionHandlers en el servidor. Los ActionHandlers son clases Java que implementan la interfaz ActionHandler. Consulte el concepto de ActionHandler.

El `OB.RemoteCallManager` ofrece un método: **llamar** que tiene los siguientes parámetros:

- `actionName`: el nombre de la clase (classname) de la clase ActionHandler
- `data`: un objeto JavaScript que se pasa como cuerpo de la solicitud, serializado como JSON
- `requestParams`: un objeto JavaScript; sus propiedades se traducen en parámetros de la solicitud:
- `callback`: una función que se llama cuando la solicitud devuelve respuesta; al llamarse se pasan 3 parámetros: response, data y request:

    - response: el objeto de respuesta de Smartclient
    - data: contiene el objeto JavaScript que crea el servidor
    - request: el objeto de solicitud original

- `callerContext`: se devuelve en `request.clientContext` (consulte el tercer parámetro del callback)
### OB.ViewManager - Apertura de vistas

El `OB.ViewManager` es el punto central para gestionar qué vistas están abiertas en la interfaz principal de tipo Multi-Document-Interface (MDI). También lo utiliza el gestor de historial para dar soporte al botón Atrás y a la actualización de la página completa de la aplicación, manteniendo aun así parte del estado.

El `OB.ViewManager` tiene un método principal de interés: `openView(viewName, params)`. Esta función tiene 2 parámetros:

- `viewName`: el nombre de la clase de la instancia de vista que se va a crear; debe ser una clase de Smartclient que admita el método estático `create`.
- `params`: un objeto javascript que contiene los **Parámetros** que se pasan al crear la vista.

El ViewManager comprobará si `viewName` existe como clase en el cliente. Si no existe, se llama al servidor para recuperar la definición de la clase; si está presente, se crea una instancia de la vista.

Si la vista tiene una **Propiedad** `showsItSelf` establecida en `true`, entonces el `ViewManager` no abrirá la instancia de vista en una solapa del MDI, sino que en su lugar realizará una llamada a la función `show` de la instancia. Esto permite abrir ventanas emergentes a través del ViewManager.

Si la instancia no tiene una **Propiedad** `showsItSelf`, o es `false`, entonces la instancia de vista se abre en una solapa del MDI.
### OB.Utilities.Action - utilidades relacionadas con la ejecución de acciones

Permite definir algunas acciones que se pueden llamar de forma secuencial. Ya existen algunas acciones definidas de serie en el core.

### Cómo configurar/definir una acción

Se pueden definir nuevas acciones mediante código javascript (por lo que pueden definirse, gracias a la modularidad, dentro de un módulo simplemente con un nuevo archivo javascript para configurar la acción y un proveedor de componentes para cargar este nuevo archivo). La forma de definir una acción es la siguiente:

```    
OB.Utilities.Action.set('myDefinedAction', function (paramObj) {
    ...
});
```

donde `myDefinedAction` es el nombre de la acción y `paramObj` es el único argumento de la función. Este `paramObj` se utilizará dentro de la lógica de la función.

**Ejemplo:**
        
``` 
OB.Utilities.Action.set('showAlert', function (paramObj) {
    alert(paramObj.text);
});
```
### Cómo llamar/ejecutar una acción

Hay dos formas de llamar/ejecutar una acción:

- Usando la función `execute`: esta forma ejecuta solo una acción 
    
    ``` 
    OB.Utilities.Action.execute('myDefinedAction', myParamObj);
    ````

    donde `myDefinedAction` es el nombre de la acción y `myParamObj` es un objeto con los parámetros necesarios como miembros del objeto.

    Esta función **execute** también tiene un tercer argumento opcional "delay", que se utiliza para realizar una llamada diferida de la ejecución.

    **Ejemplos:**
        

    ```
    OB.Utilities.Action.execute('showAlert', {'text': 'This is just an example'});
    ```

- Usando la función `executeJSON`: esta forma puede ejecutar varias acciones de forma secuencial 

    ```
    OB.Utilities.Action.executeJSON({'myDefinedAction': { myParamObj }});
    ```
    o 

    ```
    OB.Utilities.Action.executeJSON([{'myDefinedActionA': { myParamObjA }}, {'myDefinedActionB': { myParamObjB }}]);
    ```

    donde 'myDefinedAction' es el nombre de la acción y 'myParamObj' es un objeto con los parámetros necesarios como miembros del objeto. Como puede ver, puede llamar a executeJSON solo con un objeto (una acción) o con un array de objetos (varias acciones de forma secuencial).

    **Ejemplo:**
        
    ```
    OB.Utilities.Action.executeJSON({'showAlert': {'text': 'This is just an example'}});
    ```

    o

    ``` 
    OB.Utilities.Action.executeJSON([{'showAlert': {'text': 'This is the first alert'}}, {'showAlert': {'text': 'This is the second alert'}}]);
    ````

**Hilos**

Si se llama a la función `executeJSON` con varias acciones que se deben ejecutar de forma secuencial (llamada con un array de objetos), se genera un hilo para esta llamada. Para ello, existe un segundo argumento en la función `executeJSON`: `threadId`. Si no se proporciona este `threadId`, se generará uno aleatorio.

Este argumento `threadId` también se añadirá automáticamente a cada objeto de parámetros de cada llamada de acción, de modo que cada acción tenga una referencia del hilo que la ha invocado.

Hay tres acciones que se pueden realizar sobre un hilo:

  - cancelThread 
  - pauseThread 
  - resumeThread 

**Ejemplo completo:**

```
OB.Utilities.Action.set('confirmDialog', function(paramObj) {
    var text = 'Hello ' + paramObj.name + ', do you want to continue with the thread?';
    if (!confirm(text)) {
    OB.Utilities.Action.cancelThread(paramObj.threadId);
    }
});
 
OB.Utilities.Action.set('promptDialog', function(paramObj) {
    var text = '';
    if (paramObj.value) {
    text += 'You have introduced: ' + paramObj.value + '\n';
    }
    text += 'Please, introduce here a 0 in order to continue'
    paramObj.value = prompt(text);
    if (paramObj.value === '0') {
    OB.Utilities.Action.resumeThread(paramObj.threadId);
    } else {
    OB.Utilities.Action.pauseThread(paramObj.threadId);
    OB.Utilities.Action.execute('promptDialog', paramObj, 100);
    }
});
 
OB.Utilities.Action.set('alertDialog', function(paramObj) {
    var text = 'You have finished the thread!\nBye ' + paramObj.name;
    alert(text);
});
 
OB.Utilities.Action.executeJSON([
    {
    'confirmDialog': {
        name: 'John Smith'
    }
    },{
    'promptDialog': {
    }
    },{
    'alertDialog': {
        name: 'John Smith'
    }
    }
]);
```
  
En este ejemplo, hay un hilo con tres acciones:

1. **Diálogo de confirmación:** pregunta si desea continuar el hilo; si acepta, el hilo continúa; si no, el hilo se cancela (`OB.Utilities.Action.cancelThread`).

2. **Diálogo de solicitud:** si introduce 0, el hilo continúa (`OB.Utilities.Action.resumeThread`), pero si introduce cualquier otra cosa, el hilo se pausa (`OB.Utilities.Action.pauseThread`) y se muestra el valor introducido previamente. Observe cómo la función se llama de forma recursiva hasta que se cumple una condición usando el parámetro 'delay' de la función 'execute' (100 en este caso). Esto es para evitar el bloqueo del navegador debido a una iteración constante en el tiempo.

3. **Diálogo de alerta:** este es el último paso del hilo; simplemente se lo notifica.
### OB.Utilities.Number - utilidades relacionadas con números

El objeto `OB.Utilities.Number` contiene varios métodos relacionados con el formato y el redondeo de números que se utilizan dentro de la aplicación:

- `OB.Utilities.Number.roundJSNumber(num, dec)`: redondea un número a un número de decimales
- `OB.Utilities.Number.OBMaskedToJS(numberStr, decSeparator, groupSeparator)`: convierte una cadena numérica que sigue el patrón numérico de OB a un número de javascript
- `OB.Utilities.Number.JSToOBMasked(number, maskNumeric, decSeparator, groupSeparator, groupInterval)`: da formato a un número de javascript utilizando la máscara numérica de Etendo (definida en `format.xml`), el separador decimal, el separador de miles y el tamaño del intervalo de agrupación (normalmente 3)
### OB.Utilities.Date - utilidades relacionadas con fechas

El objeto `OB.Utilities.Date` contiene varios métodos de análisis y formateo de fechas:

- `OB.Utilities.Date.OBToJS(OBDate, dateFormat)`: analiza una cadena de fecha con formato de Etendo y la convierte en una fecha de javascript
- `OB.Utilities.Date.JSToOB(SDate, dateFormat)`: formatea una fecha de javascript en una cadena de fecha siguiendo el patrón de Etendo
### OBGrid

El `OBGrid` es la clase principal de rejilla, utilizada por Etendo. Si desea implementar su propia rejilla, tiene sentido extender `OBGrid`, ya que esto garantizará que su rejilla siga los mismos ajustes de estilo que las demás rejillas.
###  Componentes de ventana de Etendo

Una ventana de Etendo consta de una jerarquía de solapas; cada solapa tiene una vista de cuadrícula y una vista de formulario. Además, cada solapa tiene una barra de herramientas y una barra de mensajes. Esta interfaz de usuario está representada por una estructura interna de objetos javascript. Esta sección explica la estructura interna y las principales propiedades y métodos.

####  OBStandardWindow

Una ventana de Etendo se crea en el cliente usando una instancia de `OBStandardWindow`. Para cada solapa de la ventana, se crea una instancia de `OBStandardView`. Las instancias de `OBStandardView` están estructuradas jerárquicamente; cada `OBStandardView` tiene un conjunto de vistas hijas. Un `OBStandardView` tiene una instancia de `OBViewGrid` para representar la cuadrícula y una instancia de `OBViewForm` para representar el formulario.

El OBStandardWindow tiene las siguientes propiedades importantes:

- windowId: el id de base de datos de la ventana 
- view: la `OBStandardView` raíz 
- views: una lista completa/aplanada de todas las vistas contenidas en esta ventana 

Para más propiedades y otras, consulte el código fuente de `OBStandardWindow`.

####  OBStandardView

El `OBStandardView` tiene los siguientes componentes:

- un formulario 
- una cuadrícula 
- un conjunto de solapas con solapas, donde cada solapa de Smartclient representa una solapa hija de Etendo 
- una barra de mensajes 
- una barra de herramientas 

Cada uno de estos componentes se trata con más detalle a continuación.

El OBStandardView tiene las siguientes propiedades:

- tabId: el id de la solapa representada por esta vista 
- tabTitle: el título de la solapa 
- standardWindow: un enlace de vuelta a la instancia de ventana estándar 
- childTabSet: el TabSet de Smartclient que contiene las vistas hijas; cada solapa del TabSet tiene un panel, y el panel es una instancia de `OBStandardView`. 
- parentView: un enlace de vuelta al padre, si esta vista es hija 
- parentTabSet: el enlace al parentTabSet (parentView.childTabSet === parentTabSet) 
- toolBar: la instancia de `OBToolbar` para esta vista 
- messageBar: el `OBMessageBar` que se muestra cuando se visualiza un mensaje 
- viewForm: el `OBViewForm` de esta solapa 
- viewGrid: el `OBViewGrid` de esta solapa 
- dataSource: el origen de datos que proporciona registros a la cuadrícula y al formulario. El datasource es una instancia de `OBViewDataSource`, que es una subclase del `DataSource` de Smartclient. 
- isActiveView: (una función), devuelve true si la vista está activa (tiene el foco y una barra naranja) 

####  OBViewGrid

El `OBViewGrid` es una subclase del `ListGrid` de Smartclient. Además de las propiedades estándar de Smartclient, las siguientes propiedades son importantes:

- view: referencia al `OBStandardView` que posee esta cuadrícula

    - setItemValue: function(item, value), establece el valor del elemento y dispara las funciones `OnChange`

- Algunos métodos/propiedades de Smartclient que pueden ser útiles:

    - `getSelectedRecord`: obtiene el registro seleccionado actualmente 
    - `getSelectedRecords`: en caso de que se hayan seleccionado varios registros, devuelve todos los registros seleccionados 
    - `getEditForm`: cuando está en modo de edición de cuadrícula, contiene el formulario de edición actual para esa fila 
    - `getEditRow`: la fila que se está editando 
    - `setValue`: function(item, value), establece el valor sin disparar las funciones onchange 

####  OBViewForm

El `OBViewForm` es una subclase del `DynamicForm` de Smartclient. Además de las propiedades estándar de Smartclient, las siguientes propiedades son importantes:

- view: una referencia al `OBStandardView` que contiene este formulario 
- grid: se establece cuando el formulario se usa en edición en línea de la cuadrícula 
- hasChanged: es true si el usuario ha cambiado un campo del formulario 
- isNew: si el formulario está editando un registro nuevo 

####  OBMessageBar

La barra de mensajes muestra mensajes informativos, de error y de advertencia al usuario. Puede ser útil utilizar la barra de mensajes al reaccionar a la entrada del usuario. Por ejemplo, al implementar una función onchange del lado del cliente.

La barra de mensajes se implementa usando el tipo `OBMessageBar`.

Los siguientes métodos pueden ser relevantes:

- `setType`: function(type), establece el tipo de la barra de mensajes; controla el color y el icono. El tipo puede ser una de las siguientes constantes: 

    - `isc.OBMessageBar.TYPE_SUCCESS` 
    - `isc.OBMessageBar.TYPE_ERROR`
    - `isc.OBMessageBar.TYPE_WARNING` 
    - `isc.OBMessageBar.TYPE_INFO`

- `setText`: function(title, text), establece el contenido de la barra de mensajes; si no se establece el título, entonces se muestra un título por defecto. 
- `setLabel`: function(type, title, label, params), se puede usar para establecer una etiqueta parametrizada; consulte la sección `OB18N`. 
- `setMessage`: function(type, title, text), combinación de los 2 métodos anteriores; además muestra la barra de mensajes. 
- `hide/show`: llame a hide o show para ocultar o mostrar la barra de mensajes 

####  OBToolbar

Cada `OBStandardView` tiene su propia instancia de barra de herramientas (`OBToolbar`); sin embargo, en la interfaz de usuario solo se muestra una: la barra de herramientas perteneciente a la vista activa. Las otras barras de herramientas están ocultas.

Normalmente un desarrollador no necesita *hablar* directamente con la barra de herramientas `OBToolbar`. El enfoque estándar es [añadir un botón a la barra de herramientas](../how-to-guides/how-to-add-a-button-to-the-toolbar.md).

---

Este trabajo es una obra derivada de [Desarrollo del lado del cliente y API](http://wiki.openbravo.com/wiki/Client_Side_Development_and_API){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.