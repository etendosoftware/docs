---
title: Cómo crear una Definición del Proceso estándar
tags:
    - Cómo
    - Implementación Java
    - Validación
    - Backend
    - Validación de lado del cliente
    - Migración 
    - JSON
    - Subir archivo
---

# Cómo crear una Definición del Proceso estándar
## Visión general

El **patrón de IU estándar de la Definición del Proceso** permite crear ventanas de Parámetros definidas en el :material-menu: `Diccionario de la Aplicación`; la IU de estas ventanas se genera bajo demanda, por lo que, una vez definidos esos parámetros, el desarrollador solo necesita encargarse de la implementación del proceso.

Esta sección añadirá una nueva **Definición del Proceso estándar** y creará una entrada de menú para invocarla.

La implementación requiere experiencia en desarrollo. Consulte las siguientes páginas de conceptos para obtener información de base sobre los handlers de acción y el desarrollo JavaScript:

- [Handler de acción](../concepts/etendo-architecture.md)
- [Desarrollo del lado del cliente y API](../concepts/client-side-development-and-api.md)
- [Convenciones de codificación JavaScript](../concepts/javascript-coding-conventions.md)
## Módulo de ejemplo
Este procedimiento está respaldado por un módulo de ejemplo que muestra ejemplos del código mostrado y comentado.

El código del módulo de ejemplo puede descargarse desde el repositorio [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="\_blank"}
## Pasos para implementar el Proceso

Los procesos de **Definición del Proceso estándar** aprovechan los mismos conceptos base del *Diccionario de la Aplicación*, lo que permite definir parámetros para el proceso como metadatos que generan la UI cuando se requiere, sin necesidad de generar código, compilar o reiniciar tomcat para aplicar los cambios durante el desarrollo.

Este proceso de ejemplo tendrá los siguientes parámetros:

- Cantidad mín. y máx.: dos campos enteros obligatorios. 
- Parte: una búsqueda que permite seleccionar varias partes al mismo tiempo. 
- Terceros: un selector estándar de terceros. 

Cuando se hace clic en el botón **Hecho**, se ejecuta el proceso:

- Verifica en backend que el campo `max qty` sea mayor que `min qty`. En caso de que no lo sean, se envía un error de validación al cliente solicitando al usuario que corrija los valores antes de continuar. 
- Si se cumple la validación anterior: 
    - Se suma el importe total de todas las partes seleccionadas y se muestra en un mensaje en la ventana de **Parámetro**. 
    - Si se selecciona un tercero, se abre la ventana **Terceros** dentro del seleccionado y se muestra un mensaje en esta ventana. 

### Definir el Proceso

- Abra la ventana **Definición del Proceso** 
- Cree un nuevo registro 
- Defina el patrón de UI: **Estándar (Parámetros definidos en el Diccionario)**
- Establezca el Handler: `org.openbravo.client.application.examples.StandardProcessActionHandler`. Esta es la clase Java que implementa el proceso y que se invocará cuando el usuario haga clic en el botón de acción. 
- Guarde 

### Añadir Parámetros

- Parámetro `Min Qty`: 
    - Vaya a la pestaña **Parámetros** 
    - Cree un nuevo registro 
    - Nombre: `Min Qty`. Este es el nombre que se mostrará en la UI para este parámetro. 
    - Nombre interno: min. Es el nombre interno que se utilizará para recuperar el valor en la clase Java. 
    - Número de secuencia: 10. Define la posición de este campo en la ventana de **Parámetro** en relación con el resto de campos. 
    - Referencia: Entero. Define tanto el tipo de dato que contendrá el parámetro como la forma en que este parámetro se visualiza y se comporta en la UI. 
    - Obligatorio: true. Forzará a que el parámetro tenga un valor antes de permitir enviar la información al proceso. 
    - Valor por defecto: 0. Es el valor que tomará el parámetro por defecto. Es una expresión JavaScript evaluada en el lado servidor, como las Expresiones de filtrado por defecto usadas en los selectores. 
- Siga pasos similares para crear el campo **Max Qty** 
- Multiselector **Parte** 
    - Cree un selector de múltiples partes 
    - Cree un nuevo parámetro 
    - Referencia: `OBUISEL_Multi Selector Reference` 
    - Referencia clave: Multi Order Selector 
- El parámetro Terceros tiene `OBUISEL_Selector Reference` como Referencia y **Terceros no filtrado por defecto por cliente/proveedor** como Referencia clave 

### Añadirlo al Menú

Añadir un proceso al menú permite abrirlo desde el menú como una nueva pestaña.

- En la ventana **Menú** cree una nueva entrada.
- Acción: `Definición del Proceso`.
- Definición del Proceso: `Example Parameter Process`.

### Implementación Java

En el caso de un handler de acción de Definición del Proceso, extienda de `BaseProcessActionHandler` e implemente el método `doExecute`.
    
```java title="StandardProcessActionHandler.java"
/*
  *************************************************************************
  * The contents of this file are subject to the Openbravo  Public  License
  * Version  1.1  (the  "License"),  being   the  Mozilla   Public  License
  * Version 1.1  with a permitted attribution clause; you may not  use this
  * file except in compliance with the License. You  may  obtain  a copy of
  * the License at http://www.openbravo.com/legal/license.html
  * Software distributed under the License  is  distributed  on  an "AS IS"
  * basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
  * License for the specific  language  governing  rights  and  limitations
  * under the License.
  * The Original Code is Openbravo ERP.
  * The Initial Developer of the Original Code is Openbravo SLU
  * All portions are Copyright (C) 2013 Openbravo SLU
  * All Rights Reserved.
  * Contributor(s):  ______________________________________.
  ************************************************************************
  */
package org.openbravo.client.application.examples;
 
import java.math.BigDecimal;
import java.util.Map;
 
import org.apache.log4j.Logger;
import org.codehaus.jettison.json.JSONArray;
import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;
import org.openbravo.client.application.process.BaseProcessActionHandler;
import org.openbravo.dal.service.OBDal;
import org.openbravo.erpCommon.utility.OBMessageUtils;
import org.openbravo.model.common.order.Order;
 
public class StandardProcessActionHandler extends BaseProcessActionHandler {
  private static final Logger log = Logger.getLogger(StandardProcessActionHandler.class);
 
  @Override
  protected JSONObject doExecute(Map<String, Object> parameters, String content) {
    try {
      JSONObject result = new JSONObject();
 
      JSONObject request = new JSONObject(content);
      JSONObject params = request.getJSONObject("_params");
 
      // Do validations on param values
      double min = params.getDouble("min");
      double max = params.getDouble("max");
 
      if (max < min) {
        // In case validations are not satisfied, show an error message and allow user to fix
        // parameters
        result.put("retryExecution", true);
 
        JSONObject msg = new JSONObject();
        msg.put("severity", "error");
        msg.put(
            "text",
            OBMessageUtils.getI18NMessage("OBEXAPP_MinGtMax", new String[] { Double.toString(min),
                Double.toString(max) }));
        result.put("message", msg);
        return result;
      }
 
      // Execute process and prepare an array with actions to be executed after execution
      JSONArray actions = new JSONArray();
 
      // 1. Sum amounts of all orders and show a message in process view
      JSONArray orders = params.getJSONArray("orders");
      BigDecimal totalAmnt = BigDecimal.ZERO;
      for (int i = 0; i < orders.length(); i++) {
        String orderId = orders.getString(i);
        Order order = OBDal.getInstance().get(Order.class, orderId);
        totalAmnt = totalAmnt.add(order.getGrandTotalAmount());
      }
      JSONObject msgTotal = new JSONObject();
      msgTotal.put("msgType", "info");
      // XXX: these two messages should be translatable, like OBEXAPP_MinGtMax above
      msgTotal.put("msgTitle", "Selected Orders");
      msgTotal.put("msgText", "Total amount: " + totalAmnt.toString());
 
      JSONObject msgTotalAction = new JSONObject();
      msgTotalAction.put("showMsgInProcessView", msgTotal);
 
      actions.put(msgTotalAction);
 
      // 2. If business partner is not null, open it in BP window and show a message in new tab
      if (!params.isNull("bp")) {
        String bpId = params.getString("bp");
        JSONObject recordInfo = new JSONObject();
        recordInfo.put("tabId", "220");
        recordInfo.put("recordId", bpId);
        recordInfo.put("wait", true);
 
        JSONObject openTabAction = new JSONObject();
        openTabAction.put("openDirectTab", recordInfo);
 
        actions.put(openTabAction);
 
        JSONObject msgInBPTab = new JSONObject();
        msgInBPTab.put("msgType", "success");
        msgInBPTab.put("msgTitle", "Process execution");
        msgInBPTab.put("msgText", "This record was opened from process execution");
 
        JSONObject msgInBPTabAction = new JSONObject();
        msgInBPTabAction.put("showMsgInView", msgInBPTab);
 
        actions.put(msgInBPTabAction);
      }
 
      result.put("responseActions", actions);
 
      return result;
    } catch (JSONException e) {
      log.error("Error in process", e);
      return new JSONObject();
    }
  }
}
```

#### Respuesta

El `ActionHandler` devuelve un `JSONObject` con las acciones que se deben realizar tras la ejecución.

##### Validaciones

Es posible realizar validaciones en el backend antes de ejecutar el proceso real; cuando estas validaciones no se satisfacen, se puede mostrar un mensaje en la UI para permitir que el usuario corrija los valores problemáticos.

Cuando las validaciones no se satisfacen, se incluye la propiedad `"retryExecution": true` en la respuesta. Esto permite al usuario corregir los datos y reenviar de nuevo.
Adicionalmente, se puede añadir un mensaje para mostrar más información sobre el problema.

La respuesta tendría un aspecto similar a este:

```json 
{
  "retryExecution": true,
  "message": {
    "severity": "error",
    "text": "Min value (80.0) cannot be greater than Max value (10.0)"
  }
}
```

##### Devolver varias acciones

Tras ejecutar el proceso, es posible realizar una serie de acciones.

!!!info
    Para más información, consulte [extensión de proceso Pick & Execute](how-to-create-a-pick-and-execute-process.md). 

La respuesta debería ser similar a:

```json
{
  "responseActions": [{
    "showMsgInProcessView": {
      "msgType": "info",
      "msgTitle": "Selected Orders",
      "msgText": "Total amount: 3020482.63"
    }
  }, {
    "openDirectTab": {
      "tabId": "220",
      "recordId": "A6750F0D15334FB890C254369AC750A8",
      "wait": true
    }
  }, {
    "showMsgInView": {
      "msgType": "success",
      "msgTitle": "Process execution",
      "msgText": "This record was opened from process execution"
    }
  }, {
    "refreshGrid": {
    }
  }, {
    "refreshGridParameter": {
      "gridName": "gridParameterName"
    }
  }]
}
```

- `responseActions`. Es el nombre del `JSONArray` que indica que se realizará una serie de acciones tras la ejecución. Cada uno de los elementos del array es una acción; se pueden ejecutar distintos tipos de acciones. También es posible ampliar mediante módulos las acciones posibles a realizar: 
- `showMsgInProcessView`. Muestra un mensaje en la misma pestaña desde la que se invocó el proceso. En caso de que el proceso se abra desde el menú, este mensaje se verá en la ventana donde se proporcionan los valores de los parámetros; si el proceso se invoca desde un botón en una pestaña, el mensaje se mostrará en esa pestaña. 
- `openDirectTab`. Abre una nueva pestaña. Con `tabId`, es posible indicar el registro a abrir en esa pestaña (`recordId`). La propiedad `wait: true` indica que la siguiente acción no se iniciará hasta que esta finalice. Opcionalmente, también puede incluir un objeto de criterios para añadir automáticamente un filtro eliminable a la pestaña abierta. Un criterio es un objeto que describe un filtro en un grid. 

    !!!info
        Para más información, visite [Smartclient](https://smartclient.com/smartgwt/javadoc/com/smartgwt/client/data/AdvancedCriteria.html){target="\_blank"}.

- `showMsgInView`. Muestra un mensaje en la pestaña abierta recientemente. 
- `refreshGrid`. Actualiza el grid donde está definido el botón del proceso. Los grids no se actualizan automáticamente tras invocar un proceso estándar; solo se actualiza el registro seleccionado. Si el proceso añade o elimina registros de ese grid, entonces debe añadir `refreshGrid` a la lista de acciones de respuesta para ver los datos actualizados en el grid. 
- `refreshGridParameter`. Actualiza el **parámetro de grid** con nombre `gridName` presente en la ventana de parámetros del proceso estándar. Este tipo de respuesta es especialmente útil para aquellas ventanas de parámetros que no se cierran tras la ejecución del **handler de acción** (los parámetros permanecen visibles tras la ejecución del proceso), por ejemplo, aquellas definiciones de proceso que se abren directamente desde el menú. 
- El método `getResponseBuilder()` está disponible para las clases que extienden `BaseProcessActionHandler`. Este método devuelve un asistente que puede utilizarse para construir el resultado del proceso con las acciones de respuesta estándar deseadas de forma sencilla. Por ejemplo:
    
```java
@Override
protected JSONObject doExecute(Map<String, Object> parameters, String content) {
  ...
  ...
  return getResponseBuilder()
      .showMsgInProcessView(MessageType.INFO, "Message Title", "This is a sample message")
      .openDirectTab("220", false).build();
}
```
## Prueba del Proceso

Ahora es necesario compilar y desplegar (porque se ha añadido una nueva clase Java; tenga en cuenta que esto no es necesario en caso de solo editar/añadir parámetros).

Después de compilar y desplegar, habrá una nueva entrada en el menú: **Proceso de ejemplo de parámetros**. Esta entrada abre la ventana de parámetros donde se muestran todos los parámetros definidos y se presenta un botón **Hecho** para enviar los valores establecidos para ellos. Cuando se ejecuta el proceso:

- Si `Cantidad máx.` es mayor que `Cantidad mín.`, se muestra un mensaje y el proceso puede enviarse de nuevo.
- Se muestra un mensaje en la ventana de parámetros sumando los importes de todas las partes seleccionadas.
- Si se selecciona un tercero, se abre en una nueva pestaña mostrando un mensaje en ella.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-standard-process-definition/standard-process-definition-1.png)
## Temas avanzados

### Invocar el proceso desde una solapa

Los procesos de **Definición del Proceso** estándar pueden abrirse como una solapa desde el menú o como un popup modal desde un botón en una solapa. Esta segunda opción puede lograrse añadiendo una columna adicional a la tabla utilizada en la solapa. 

!!!info
    Para más detalles sobre este proceso, visite [Cómo crear un proceso Pick and Execute](how-to-create-a-pick-and-execute-process.md). 

### Solo lectura y lógica de visualización

Los parámetros en **Definición del Proceso** soportan lógica de visualización y de solo lectura. Esto permite mostrar u ocultar, y hacer editables o de solo lectura, los parámetros en función de los valores introducidos en otros parámetros.

### Combos subordinados
  
Los datos que pueden seleccionarse dentro de un combo (selector) pueden restringirse en función de los valores que tomen otros parámetros usando **Reglas de validación**. La lógica de estas validaciones es un HQL que se añade a su datasource. Esto se escribe en JavaScript, siendo posible usar `OBBindings`, del mismo modo que se escribe el valor por defecto.

### Agrupación de parámetros
  
Es posible agrupar parámetros en la UI usando la propiedad **Grupo de campos** al definir el parámetro.

### Mostrar resultados en la propia ventana del proceso

Es posible mostrar el resultado de un proceso directamente en la propia ventana del proceso. Esto tiene sentido si la sección de parámetros es pequeña y desea mostrar el resultado directamente.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-standard-process-definition/standard-process-definition-2.png)

Para conseguirlo, el objeto data/json devuelto por el handler del servidor debe establecer el parámetro `showResultsInProcessView` a true. También tiene sentido establecer el parámetro `retryExecution` a true:

```json
{
  "retryExecution": true,
  "showResultsInProcessView": true
}
```

El método `javascript` llamado obtiene un objeto con una propiedad `processView` que hace referencia a la vista general del proceso. Desde la vista del proceso puede acceder al resultLayout para mostrar el resultado. El resultLayout es un `SmartclientHLayout`.

Por ejemplo, una acción de retorno:

```javascript
OB.Utilities.Action.set('openSaikuReport', function(paramObj) {
  var i, queries = paramObj.queries,
      processView = paramObj._processView,
      mainLayout = processView.resultLayout, reportView;
 
  reportView = isc.OBANALY_ShowSaikuReport.create({
    parameters: paramObj,
    queries: queries
  });
  mainLayout.addMember(reportView);

```

### Colocar un parámetro en una columna concreta
  
El campo **Número de columna** de la solapa **Parámetro** permite especificar la columna donde debe colocarse el parámetro. Los parámetros de grid usan siempre las cuatro columnas del formulario, por lo que este campo no aplica a ellos.

### Invocar una validación de lado del cliente antes de llamar al handler de acción

El campo **Validación de lado del cliente** de la solapa **Definición del Proceso** permite definir una función que se ejecutará antes de que se realice la petición al handler de acción. Esta función puede usarse para realizar **Validación de lado del cliente**.

Esta función debe aceptar 3 parámetros:

- el objeto de la ventana de parámetros. Es decir, si nombra este parámetro **vista**, entonces el formulario de la ventana de parámetros será accesible mediante `view.theForm`. El valor de un parámetro concreto puede recuperarse usando `view.theForm.getItem(parameter_name).getValue() `
- un callback de éxito de validación. Si los valores actuales del formulario pasan la validación, debe invocarse este callback
- un callback de fallo de validación. Si los valores del formulario no satisfacen la validación, invoque este callback. 

Por ejemplo:

```javascript
OB.Utilities.TestClientSideValidation = function (view, actionHandlerCall, failureCallback) {
  var minNumber, maxNumber;
  minNumber = view.theForm.getItem('min_number').getValue();
  maxNumber = view.theForm.getItem('max_number').getValue();
  if (maxNumber >= minNumber) {
    // only execute the callback if the form values pass the validation
    actionHandlerCall();
  } else {
    failureCallback();
  }
```

Además, las funciones de validación de lado del cliente soportan un cuarto parámetro que contiene información adicional, como el botón pulsado:  

```javascript
OB.Utilities.TestClientSideValidation = function (view, actionHandlerCall, failureCallback, additionalInfo) {
  if (additionalInfo.buttonValue === 'OK') {
    // execute validations related to the 'OK' button
  } else {
    // do another validations
  }
```

!!!info
    Para aprender a definir nuevos botones en una ventana de definición de proceso estándar, consulte [Añadir nuevos botones](how-to-create-a-standard-process-definition.md#adding-new-buttons).


Se puede añadir información adicional al payload que recibirá el proceso. Por ejemplo, este código añadiría un nuevo parámetro llamado `myParam`:

```javascript
view.externalParams = { myParam:'value' };
```

### Invocar una función cuando se cambia un parámetro que no es de grid

El campo **Función 'On Change'** de la solapa **Parámetro** permite definir una función que se ejecutará cuando se actualice un parámetro que no es de grid, después de que el parámetro pierda el foco. Esta función puede usarse para realizar validaciones o para implementar **callouts del lado del cliente**, entre otras cosas.

La función debe aceptar cuatro parámetros:

- item: el elemento que se ha modificado 
- view: el objeto de la ventana de parámetros 
- form: el formulario que contiene el elemento 

### Cómo establecer el valor de parámetros que no son de grid de forma programática

Es posible ejecutar una **Función 'On Change'**, además de cuando el parámetro pierde el foco, al establecer el valor del parámetro de forma programática.

Al establecer el valor de un parámetro desde código, se recomienda usar la función **setValueProgrammatically()**. De este modo, si el parámetro tiene una **Función 'On Change'**, se ejecutará después de establecer el valor del parámetro.

```javascript
var issotrx = form.getItem('issotrx');
// Set the value for the item
// If the 'issotrx' parameter has an 'On Change Function' it will be executed also
issotrx.setValueProgrammatically('Y');
```

### Invocar una función cuando se han inicializado todos los parámetros que no son de grid

El campo **Función 'On Load'** de la solapa **Definición del Proceso** permite definir una función que se ejecutará una vez que los parámetros se hayan inicializado.

### Invocar una función cuando el proceso necesita refrescarse

El campo **Función On Refresh** de la solapa **Definición del Proceso** permite definir una función que se ejecutará cuando se invoque la acción de refresco de la ventana de parámetros.

Por ejemplo, si el proceso tiene un proceso hijo, una vez que el proceso hijo finaliza, invocará un refresco del proceso padre.

!!!note
    Dado que cada proceso tiene sus particularidades, debe definirse una función de refresco personalizada en caso de que el proceso sea susceptible de ser refrescado/recargado.

La función debe aceptar, al menos, un parámetro:

- view: el objeto de la ventana de parámetros 

### Invocar cuando un parámetro de grid se carga por primera vez

La inicialización de los parámetros de grid se realiza de forma asíncrona, por lo que cuando se invoca la **onLoadFunction** general, no es seguro que todos los parámetros de grid se hayan cargado con sus datos iniciales. Si necesita ejecutar código justo después de que un grid se cargue por primera vez, use el campo **Función 'On Grid Load'**. La función usada aquí debe aceptar un parámetro: el propio grid.

Por ejemplo:

```javascript
OB.Utilities.TestOnGridLoad = function (grid) {
  var nRecordsReceived = grid.getData().getLength(),
      messageBar = grid.view.messageBar;
  messageBar.setMessage('info', 'The grid has been loaded with ' + nRecordsReceived + ' records');
    }
```

### Especificar el número de filas mostradas en un parámetro de grid

Puede establecer el número de filas que deben mostrarse la primera vez en un parámetro de grid usando el campo **Número de filas mostradas**. Este campo se usa únicamente para establecer la altura del grid; si el grid tiene realmente más filas que el **Número de filas mostradas**, se mostrará una barra de desplazamiento. El valor por defecto de este campo es 5.

!!!note
    No es posible definir el colspan de los parámetros de grid, porque siempre usan las cuatro columnas disponibles del formulario.

### Definir una lógica para mostrar para columna de grid para los campos de un parámetro de grid

El campo **Lógica para mostrar para columna de grid** en la solapa Campo permite definir una lógica de visualización para los campos de los parámetros de grid.

Por ejemplo, suponga que ha definido una ventana de parámetros con dos parámetros:

- un booleano llamado Mostrar columnas avanzadas, nombre de columna `showAdvancedColumns` 
- un grid. 

Supongamos que el grid tiene algunos campos que solo deben mostrarse si está marcada la opción **Mostrar columna avanzada**. El campo **Lógica para mostrar para columna de grid** de esos campos debería establecerse a:

``` java
@showAdvancedColumns@='Y'
```

### Especificar un valor por defecto para el filtro de un campo de grid de parámetros

El campo **Expresión de filtrado por defecto** de la solapa Campo permite definir un valor por defecto para el filtro de un campo. Este valor por defecto puede ser una constante, depender de otro parámetro o usar `OBBindings`.

### Ocultar el nombre del parámetro de un parámetro de grid

Aunque es posible definir varios parámetros de grid en una ventana de parámetros, es probable que la mayoría de las veces haya como máximo uno (por ejemplo, en ventanas de pick and execute). En esos casos, considere no mostrar el nombre del parámetro de grid. Hágalo desmarcando el indicador **Mostrar título** en la solapa **Parámetro**.

### Añadir nuevos botones

Por defecto, las definiciones de proceso tienen un único botón **Hecho** (y uno de **Cancelar** en caso de que se muestren en un popup desde una ventana estándar). Es posible cambiar ese botón o añadir nuevos.

Para hacerlo:

1. Cree una nueva **Referencia con Lista de Botones** como **Referencia padre**. En la solapa **Lista valores** añada tantos registros como botones deban mostrarse en el proceso. El nombre de estos elementos se verá en la etiqueta del botón, mientras que el **Identificador** es el valor que se enviará al **Handler** en el backend dentro del campo `buttonValue`. 
2. Añada un nuevo parámetro al proceso con **Lista de Botones** como referencia y la nueva referencia recién creada como **Referencia clave**. 
  
!!!note
    Debe haber, como máximo, un único parámetro de tipo **Lista de Botones**. 


### Proceso multi-registro

Un proceso estándar puede definirse como proceso multi-registro para poder ejecutarlo para más de un registro.

### Subida de archivos

La **referencia de archivo** mejora las capacidades de Etendo habilitando la subida de archivos directamente dentro de las definiciones de proceso. 

Esta funcionalidad puede usarse en **Definición del Proceso**, introduciendo un **elemento de subida de archivos intuitivo** en el formulario del proceso. Los usuarios pueden subir un **único archivo** para su procesamiento, que luego es gestionado por la lógica del proceso según se especifique en la definición del proceso.

!!!info
    - El tamaño máximo de archivo que los usuarios pueden subir está limitado por defecto a 10MB. Esto se configura en la preferencia `Maximum file upload size (MB)`. Esta comprobación de tamaño de archivo se realiza tanto en el lado del cliente como en el lado del servidor.
    - Para más información sobre preferencias, visite la [sección de Preferencias en la Guía de usuario](../../../user-guide/etendo-classic/basic-features/general-setup/application/preference.md).

#### Módulo de ejemplo

Este procedimiento está soportado por un módulo de ejemplo que demuestra cómo usar la referencia **Subir archivo** en un proceso basado en Java.

El código del módulo de ejemplo puede descargarse desde el repositorio [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="_blank"}


#### Referencia Subir archivo en Definición del Proceso

Para habilitar la subida de archivos en una definición de proceso, puede definirse una referencia **Subir archivo** como parámetro del proceso.

La referencia **Subir archivo** ya está proporcionada por el core de Etendo y no necesita ser creada ni extendida por el desarrollador.

Está implementada en Etendo con una Definición de Interfaz de Usuario que renderiza la entrada de archivo y envía la petición como un formulario multipart: `org.openbravo.client.kernel.reference.ProcessFileUploadUIDefinition`

El archivo subido queda disponible durante la ejecución del proceso a través del **handler de Definición del Proceso** (una clase Java que extiende `BaseProcessActionHandler`).

![Definición de la referencia Subir archivo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-standard-process-definition/upload-file-1.png)

!!!info
    La imagen anterior muestra la referencia **Subir archivo** tal y como está definida en el core. Se incluye únicamente con fines de identificación y no requiere ninguna configuración o personalización adicional.

    Puede seleccionarse cualquier archivo, ya que esta funcionalidad fue diseñada como una base para que los programadores la adapten a sus necesidades específicas.

#### Definición del Proceso

Este ejemplo se proporciona como parte del módulo **User Interface Application Examples**.

La **Definición del Proceso** ya está creada e incluida en el módulo y se muestra aquí para explicar cómo se configura la referencia **Subir archivo**.

![Definición del Proceso con parámetro Subir archivo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-standard-process-definition/upload-file-2.png)

En la ventana **Definición del Proceso**, pueden observarse los siguientes elementos:

- **Módulo**: *User Interface Application Examples* indica que este proceso pertenece al módulo de ejemplo.
- **Identificador / Nombre**: Identifica el proceso en la aplicación.
- **Handler**: [`com.etendoerp.client.application.examples.ExampleUploadFile`](https://github.com/etendosoftware/com.etendoerp.client.application.examples/blob/main/src/com/etendoerp/client/application/examples/ExampleUploadFile.java) clase Java que implementa la lógica del proceso y extiende `BaseProcessActionHandler`.
- **Patrón de la Interfaz de Usuario**: Estándar (Parámetros definidos en el Diccionario)
- **Acceso datos**: Configurado según las necesidades del ejemplo.

#### Parámetro Subir archivo

La **Definición del Proceso** incluye un único parámetro configurado con la referencia **Subir archivo**.

- **Referencia**: Subir archivo. Renderiza una entrada de archivo en la ventana de ejecución del proceso.
- **Nombre columna BD**: Este valor se usa para recuperar el archivo subido desde el mapa de parámetros en el handler de acción del proceso.

Este parámetro permite al usuario subir un **único archivo**, que está disponible únicamente durante la ejecución del proceso.

#### Ejecutar el proceso

Para ejecutar el ejemplo, se define una entrada de **Menú** que apunta a la **Definición del Proceso**.

Esto permite buscar y ejecutar el proceso desde el menú de la aplicación usando el nombre **Ejemplo de Subir archivo**.

Cuando se abre el proceso, se muestra una ventana de ejecución simple con el parámetro **Subir archivo** renderizado como un selector de archivo.

![Ventana de ejecución de Subir archivo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-standard-process-definition/upload-file-3.png)

!!!info
    En este ejemplo, el proceso espera que se suba un archivo `.txt`. La restricción del tipo de archivo forma parte de la lógica del ejemplo y no se aplica por la propia referencia Subir archivo.

Durante la ejecución:

- La lógica del proceso solo acepta archivos de texto.
- El contenido del archivo subido se lee durante la ejecución.
- El texto contenido en el archivo se muestra de vuelta al usuario como resultado del proceso.

#### Procesar el archivo subido

Tras seleccionar un archivo `.txt` válido y ejecutar el proceso, el archivo se procesa mediante el handler de acción Java.

En este ejemplo, el proceso:

- Valida que el archivo subido tenga una extensión `.txt`.
- Lee el contenido del archivo desde el input stream.
- Muestra el contenido del archivo como un mensaje de éxito en la interfaz de usuario.

![Mensaje de resultado de Subir archivo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-standard-process-definition/upload-file-4.png)

El mensaje mostrado al usuario contiene el texto completo leído del archivo subido, confirmando que el archivo se recibió y procesó correctamente.

Este ejemplo demuestra cómo se puede acceder a los archivos subidos, validarlos y procesarlos en una **Definición del Proceso** basada en Java usando la referencia **Subir archivo**.
## Limitaciones

### Referencias

Actualmente, no todas las referencias disponibles en las **ventanas estándar** están disponibles en **Definición del Proceso**. Las siguientes no se pueden usar como parámetros:

- Botón: el mecanismo para añadir nuevos botones se describe en [Añadir nuevos botones](how-to-create-a-standard-process-definition.md#adding-new-buttons). 
- Imagen 
- Cadena enmascarada 
- Tabla 
- TableDir 
- Árbol
- PAttribute

### Lógica de la UI

Los callouts no están implementados para los parámetros.
## Migración de procesos antiguos

Las Definiciones del Proceso admiten varios parámetros. Para implementar este soporte, se cambió la forma en que el valor del parámetro de grid se envía al backend y se añadió un nuevo indicador **Compatibilidad con parámetros de grid antiguos**.  

Para migrar procesos compatibles con grids antiguos al nuevo formato, establezca **Compatibilidad con parámetros de grid antiguos** en false y, dependiendo del caso:

- Si el **Patrón de la Interfaz de Usuario** del proceso es **Manual**, no se necesita ningún otro cambio. 
- Si el proceso no tiene ningún parámetro, no se necesita ningún otro cambio. 
- Si el proceso tiene un parámetro (de grid), el `JSON` que recibe el método `doExecute` cambia; estas son las modificaciones necesarias:

Ejemplo:

```java title="Código antiguo"
JSONObject gridInfo = new JSONObject(content);
JSONArray gridSelection = gridInfo.getJSONArray("_selection");
JSONArray gridAllRows = gridInfo.getJSONArray("_allRows");
```
```java title="Código nuevo"
JSONObject params = new JSONObject(content).getJSONObject("_params");
// Sustituya aquí gridColumnName por el Nombre columna BD real de su parámetro de grid
JSONObject gridInfo = params.getJSONObject("gridColumnName");
JSONArray gridSelection = gridInfo.getJSONArray("_selection");
JSONArray gridAllRows = gridInfo.getJSONArray("_allRows");  
```
---
Este trabajo es una obra derivada de [Cómo crear una Definición del Proceso estándar](http://wiki.openbravo.com/wiki/How_to_create_a_Standard_Process_Definition){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.