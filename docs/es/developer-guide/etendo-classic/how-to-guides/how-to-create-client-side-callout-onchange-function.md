---
tags:
  - Cómo hacer
  - Desarrollo
  - Funciones JavaScript
  - Gestión de eventos OnChange
  - Interacciones de la interfaz de usuario
---

# Cómo crear una función OnChange de Callout del lado del cliente

## Visión general

Esta sección explica cómo implementar **funciones del lado del cliente (javascript)** que se ejecutan cuando cambia el valor de un campo en la interfaz de usuario. El concepto de onChange se corresponde con el [Callout](How_to_create_a_Callout.md) tradicional; la principal diferencia es que la **funcionalidad onChange se implementa en el cliente**. Esto ofrece las siguientes ventajas:

- mejor rendimiento, ya que para muchas acciones no es necesario llamar al servidor
- acceso directo a componentes de la interfaz de usuario como el campo, el formulario y la cuadrícula

Además, la función onChange tiene todas las ventajas del Callout clásico: aún puede **llamar al servidor** para ejecutar acciones más intensivas en rendimiento o realizar consultas.

## Módulo de ejemplo

Esta sección se apoya en un módulo de ejemplo que muestra ejemplos del código mostrado y comentado.

El código del módulo de ejemplo puede descargarse desde este repositorio: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

El módulo de ejemplo está disponible a través del Repositorio Central (consulte "Client Application Examples"); para más información, consulte la página del proyecto Examples Client Application.

## Definición de funciones OnChange

Una función `OnChange` es una función en javascript disponible a través de un ID global.

!!!note
    El ID global debe ser único; se recomienda encarecidamente usar el prefijo de BD del módulo.

La función `OnChange` debe definirse en un archivo javascript ubicado en el módulo.

!!!info
    Para más información, lea [cómo añadir código javascript](../concepts/client-side-development-and-api.md#adding-javascript-to-etendo) a Etendo.

A continuación se muestra un ejemplo de una función `OnChange` definida en el módulo de ejemplo:

```javascript
OB.OBEXAPP = {};
OB.OBEXAPP.OnChangeFunctions = {};
 
OB.OBEXAPP.OnChangeFunctions.Note_Name = function(item, view, form, grid) {
  // set a message
  view.messageBar.setMessage(
    isc.OBMessageBar.TYPE_INFO,
    'Changed!',
    'You changed the name to ' + item.getValue()
  );

  // set the value for the description and make sure that the
  // onchange handlers are called
  form.setItemValue('description', 'Description ' + item.getValue());
};
```

Como puede ver, la función `OnChange` se coloca en un objeto global; en este caso se utiliza el prefijo de BD del módulo para ello.

!!!note
    Es importante tener en cuenta que no debe usar var antes de la definición del objeto global; de lo contrario, su var no será global.

Esto se debe a que el código javascript global incluido en Etendo se ejecuta, de hecho, dentro de una función.

Una función onchange recibe cuatro argumentos:

- item: el FormItem que cambia.
- view: la vista estándar ( OBStandardView ) que proporciona acceso a la estructura completa de ventana y solapas en una ventana cargada.
- form: el OBViewForm que contiene los campos; el formulario también puede ser el formulario usado en la edición en línea de la cuadrícula.
- grid: el OBViewGrid que contiene la lista de registros cargados para la solapa.

Este ejemplo de onchange establece un mensaje en la barra de mensajes y establece el valor de otro campo.

!!!note
    Tenga en cuenta que se utiliza el método setItemValue del formulario para disparar otras funciones onchange. El formulario también tiene un método setValue, pero ese no disparará un evento onchange.

!!!info
    Si su función onchange no funciona o no se llama, o si su ventana deja de cargar después de definir un onchange, entonces revise la consola.

## Registro y configuración de un OnChange para un campo específico

Hay dos formas de vincular una función `OnChange` a un campo específico:

- A través del diccionario de aplicación
- Mediante programación usando código javascript

El primer enfoque le permite definir el `OnChange` directamente en la definición del campo. Para el segundo enfoque necesita usar javascript, pero ofrece flexibilidad adicional.

### Configurar una función OnChange a través del AD

El Diccionario de Aplicación le permite configurar el `OnChange` para un campo específico; consulte el campo de función `OnChange` en la ventana `Window, Tabs and Fields`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_client_side_callout_onchange_function-0.png)

El valor debe ser el ID global único mencionado anteriormente.

### Registro programático de funciones OnChange

También es posible registrar una **función OnChange mediante javascript**. Esto ofrece más flexibilidad que definirlo a través del Diccionario de Aplicación:

- puede añadir funciones `OnChange` a campos existentes sin cambiar la información en la tabla
- puede añadir más de una función `OnChange` a un campo
- puede sobrescribir la función `OnChange` definida en el Diccionario de Aplicación

Una función `OnChange` se registra mediante el método `OB.OnChangeRegistry.register`. Espera 4 parámetros:

- id de solapa
- field: el nombre del campo para el que se registra el onchange
- callback function: la propia función onchange
- id: puede usarse para sobrescribir una función `OnChange` existente registrada usando el mismo id

Un ejemplo de registro:

```javascript
OB.OnChangeRegistry.register('FF8081813290114F0132901EB0A2001A', 'value', OB.OBEXAPP.OnChangeFunctions.Note_Value, 'OBEXAPP_Value');
```

#### Múltiples funciones OnChange por campo, orden de llamada

La función `OnChange` puede tener una propiedad sort para controlar el orden de llamada si hay múltiples funciones `OnChange` para un mismo campo.

Por ejemplo, se configura así:

```javascript
OB.OBEXAPP.OnChangeFunctions.Note_Value.sort = 20;
```

Algunas notas sobre la ordenación:

- el `OnChange` definido en el Diccionario de Aplicación tiene sort 50 e id: Valor por defecto
- si un `OnChange` no tiene un sort definido, obtiene el sort 100

#### Sobrescribir/reemplazar un OnChange

Un `OnChange` puede registrarse usando un id. Si ya existe un `OnChange` con el mismo id, entonces se reemplaza por el nuevo registro.

El `OnChange` definido a través del Diccionario de Aplicación tiene el id **Valor por defecto**. Por lo tanto, al registrar un nuevo `OnChange` usando ese id, sobrescribirá el `OnChange` definido a través del Diccionario de Aplicación.

## Ejemplo: OnChange llamando a una acción del lado del servidor

Esta sección muestra un ejemplo de un `OnChange` que llama a una acción del lado del servidor:

```javascript
OB.OBEXAPP.OnChangeFunctions.Note_Value = function(item, view, form, grid) {
  // the callback called after the server side call returns
  var callback = function(response, data, request) {
    form.setItemValue(item, data.upperCased);
    view.messageBar.setMessage(
      isc.OBMessageBar.TYPE_WARNING,
      'Uppercased!',
      'The value has been uppercased'
    );
  };

  // do a server side call and on return call the callback
  OB.RemoteCallManager.call(
    'com.etendoerp.client.application.examples.OnchangeExampleActionHandler',
    {
      value: item.getValue()
    },
    {},
    callback
  );
};
OB.OBEXAPP.OnChangeFunctions.Note_Value.sort = 20;
```

El ejemplo anterior llama a una clase ActionHandler: OnchangeExampleActionHandler. El resultado se devuelve y se establece en un campo, y se muestra un mensaje en la barra de mensajes.

!!!info
    Es posible deshabilitar el formulario durante la acción del lado del servidor; llame al método setDisabled en el formulario con el valor true como parámetro.

## OnChange y el Callout clásico

Si un campo tiene definidos tanto un `OnChange` como un Callout clásico, entonces se aplica lo siguiente:

- en la UI de Openbravo 3 se utilizará la función `OnChange` y el Callout quedará deshabilitado
- en la UI clásica se utiliza el Callout y se ignoran las funciones `OnChange`

## Módulo de ejemplo: ventana de ejemplo

El Módulo de ejemplo tiene una ventana de ejemplo con varios ejemplos de una función de Callout/onchange. Puede encontrar la ventana de ejemplo en `Application Examples` >`Callout/OnChange Function`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_client_side_callout_onchange_function-1.png)

Para probar el onchange, cree un nuevo registro y establezca algunos valores en los campos. Debería ver un comportamiento automático.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_client_side_callout_onchange_function-2.png)

Puede **habilitar/deshabilitar** diferentes funciones onchange yendo al archivo web/com.etendoerp.client.application.examples/js/example-onchange.js y descomentando algunas de las líneas comentadas.

---

Este trabajo es una obra derivada de [Cómo crear una función onchange de Callout del lado del cliente](http://wiki.openbravo.com/wiki/How_to_create_client_side_callout_onchange_function){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.