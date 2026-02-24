---
tags:
  - Cómo hacer
  - Barra de herramientas
  - Botón
  - JavaScript
  - Capa de Acceso a Datos
---

# Cómo añadir un botón a la barra de herramientas

##  Visión general

Esta sección explica cómo se puede añadir un botón a la barra de herramientas principal que se muestra en rejillas y formularios. La barra de herramientas contiene dos tipos de botones: los botones de la aplicación a la izquierda (visualizados mediante un icono) y los botones personalizados a la derecha (mostrados con una etiqueta). 

Esta sección describe cómo añadir un botón a la parte izquierda: los botones de la aplicación.
  
Para seguir esta sección, desarrolle JavaScript así como Java del lado del servidor y comprenda los conceptos de la [Capa de Acceso a Datos](../concepts/Data_Access_Layer.md).

##  Módulo de ejemplo

Esta sección se apoya en un módulo de ejemplo que muestra un ejemplo del código que se presenta y se comenta aquí.

![Header](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_button_to_the_toolbar-0.png)

!!! info
    El módulo de ejemplo también contiene implementaciones de otras secciones.  
 
  
##  Implementación de un botón de la barra de herramientas

!!! info
    Al implementar sus propios componentes, a menudo tiene sentido ampliar componentes existentes. Asegúrese de que su módulo dependa entonces del módulo que proporciona los tipos base. Esto garantiza que el JavaScript se cargue en el orden correcto.  
  
El botón que se va a implementar calculará y mostrará al usuario la suma de un conjunto de pedidos seleccionados. 

Esta sección se divide en 2 partes:

- la primera parte
se centra en visualizar el botón en las ventanas y solapas correctas y en asegurarse de que el botón se habilita/deshabilita adecuadamente. 

- La segunda parte explicará cómo implementar la lógica del backend y cómo llamar a la lógica del lado del servidor cuando se hace clic en el botón y mostrar sus resultados.

La primera parte consta de los siguientes pasos:

  * un icono para la visualización 
  * un estilo `css` y JavaScript que vinculan el icono al botón 
  * JavaScript que implementa el método de clic/acción del botón y registra el botón en el registro global 
  * añadir JavaScript para habilitar/deshabilitar el botón cuando se seleccionan registros en la rejilla 
  * una clase Java `ComponentProvider` para registrar el JavaScript y el `css` en Etendo.

Estos pasos visualizarán el botón, pero todavía no harán nada. Los pasos posteriores añadirán lógica:

  * un action handler del lado del servidor para implementar la lógica del lado del servidor (sumar los pedidos y devolver el resultado al cliente) 
  * JavaScript del lado del cliente para llamar al servidor y procesar el resultado 

Cada uno de estos pasos se describe con más detalle a continuación.

##  Visualización del botón - Pasos de implementación

###  Definición del icono y un css

El icono y su estilo relacionado se definen mediante un archivo de icono. 

!!!info
    Para una visualización estándar usando el estilo de Etendo, el icono debe ser de 24x24 sin un color de fondo.


El icono debe colocarse en un directorio específico de su módulo:
`web/com.etendoerp.userinterface.smartclient/etendo/skins/Default/[modulename]`.

Normalmente, tiene sentido almacenar el icono en una subcarpeta. El módulo de ejemplo tiene el archivo de icono en:

`web/com.etendoerp.userinterface.smartclient/etendo/skins/Default/
com.etendoerp.client.application.examples/images`.

    com.etendoerp.client.application.examples
    ├── reference data
    ├── src
    ├── src-db
    └── web
        ├── com.etendoerp.client.application.examples
        │   └── js
        │       ├── example-toolbar-button.js
        │       └── example-view-component.js
        └── com.etendoerp.userinterface.smartclient
            └── etendo
                └── skins
                    └── Default
                        └── com.etendoerp.client.application.examples
                            ├── images
                            │   └── iconButton-sum.png
                            └── example-styles.css

  
A continuación, añada un `archivo css` que vincule este icono a un estilo `css` específico. El archivo `css` también debe estar ubicado en este directorio de su módulo:
`web/com.etendoerp.userinterface.smartclient/etendo/skins/Default/[modulename]`.

En el módulo de ejemplo, el archivo `css` se encuentra aquí:

`web/com.etendoerp.userinterface.smartclient/etendo/skins/Default/
com.etendoerp.client.application.examples/example-styles`



Dentro del archivo `css` añada un estilo definido así:

    
    
    .ETToolbarIconButton_icon_etexapp_sum {
      background-repeat: no-repeat;
      background-position: center center;
      background-image: url(./images/iconButton-sum.png);
    }

!!!note
    El nombre de la clase `css` es importante, debe comenzar con
    `ETToolbarIconButton_icon_`; la parte posterior (etexapp_sum) se utiliza más adelante en este tutorial. Tiene sentido usar el dbprefix del módulo en esta última parte para evitar colisiones de nombres con otros módulos.

###  El JavaScript para crear y registrar el botón

El siguiente paso es implementar el JavaScript que define el botón y lo registra para que se muestre en las solapas. Comience creando un archivo JavaScript en esta ubicación: `web/com.etendoerp.client.application.examples/js/example-toolbar-button.js`.

Este es el JavaScript completo para `toolbar-button`:


```js title="example-toolbar-button.js"
    
    (function () {
      var buttonProps = {
          action: function(){
            alert('You clicked me!');
          },
          buttonType: 'etexapp_sum',
          prompt: OB.I18N.getLabel('ETEXAPP_SumData'),
          updateState: function(){
              var view = this.view, form = view.viewForm, grid = view.viewGrid, selectedRecords = grid.getSelectedRecords();
              if (view.isShowingForm && form.isNew) {
                this.setDisabled(true);
              } else if (view.isEditingGrid && grid.getEditForm().isNew) {
                this.setDisabled(true);
              } else {
                this.setDisabled(selectedRecords.length === 0);
              }
          }
        };
      
      // register the button for the sales order tab
      // the first parameter is a unique identification so that one button can not be registered multiple times.
      ET.ToolbarRegistry.registerButton(buttonProps.buttonType, isc.ETToolbarIconButton, buttonProps, 100, '186');
    }());
```
Veamos las distintas partes. El JavaScript comienza y termina con esta parte:

``` javascript
    
    (function () {
    ...
    }());
```

Esto se hace para evitar que las variables locales estén disponibles globalmente. Crea una función y la ejecuta inmediatamente.

A continuación, la primera parte de buttonprops"

``` javascript
          action: function(){
            alert('You clicked me!');
          },
          buttonType: 'etexapp_sum',
          prompt: OB.I18N.getLabel('ETEXAPP_SumData'),
```


  * Establece el método de acción que se llama cuando el usuario hace clic en el botón. 
  * El buttonType se corresponde con el nombre usado en el estilo css; controla el icono y el estilo y también se utiliza como identificador 
  * El prompt se muestra cuando el usuario pasa el ratón por encima del botón; la etiqueta se obtiene mediante el método OB.I18N.getLabel para soportar traducción. Añada una etiqueta en la tabla Messages para visualizarla correctamente: 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_button_to_the_toolbar-4.png)

La función updateState se llama para habilitar y deshabilitar el botón cuando el
usuario navega por el sistema.

```javascript   
    
         updateState: function(){
              var view = this.view, form = view.viewForm, grid = view.viewGrid, selectedRecords = grid.getSelectedRecords();
              if (view.isShowingForm && form.isNew) {
                this.setDisabled(true);
              } else if (view.isEditingGrid && grid.getEditForm().isNew) {
                this.setDisabled(true);
              } else {
                this.setDisabled(selectedRecords.length === 0);
              }
          }
```
La función habilita/deshabilita el botón si el formulario o la rejilla son nuevos y si no hay registros seleccionados.

A continuación, este código registra el botón para la solapa con id '186':


``` javascript
      OB.ToolbarRegistry.registerButton(buttonProps.buttonType, isc.OBToolbarIconButton, buttonProps, 100, '186');
```

Nota:

  * el primer parámetro es una identificación única para que un botón no pueda registrarse varias veces. 
  * como segundo parámetro se pasa la clase JavaScript del botón; como valor por defecto use siempre `isc.ETToolbarIcon`Button 
  * buttonProps define las características del botón 
  * el tercer parámetro define el orden en la barra de herramientas; los botones estándar se colocan con un intervalo de 10, por lo que puede colocar su botón entre otros botones. 
  * El último parámetro es el tabId (un String); puede pasar null para registrar un botón para todas las solapas. También es posible pasar un array de tabIds (strings) para registrar un botón para varias solapas. 
  * Para registrar un botón para varias solapas, llame a registerButton varias veces para distintas solapas 


###  El ComponentProvider

Los pasos anteriores añadieron recursos estáticos (JavaScript y css) al sistema.

Ahora Etendo debe saber dónde encontrar estos recursos al inicializar y generar la interfaz de usuario. Para ello, el `css`, el JavaScript y los recursos deben registrarse. Esto se hace mediante un ComponentProvider. 

!!!info
    Para información más detallada, visite [ComponentProvider](../concepts/Etendo_Architecture#component-provider.md).


```javascript
     
    @ApplicationScoped
    @ComponentProvider.Qualifier(ExampleComponentProvider.EXAMPLE_VIEW_COMPONENT_TYPE)
    public class ExampleComponentProvider extends BaseComponentProvider {
      public static final String EXAMPLE_VIEW_COMPONENT_TYPE = "ETEXAPP_ExampleViewType";
     
      /*
       * (non-Javadoc)
       * 
       * @see com.etendoerp.client.kernel.ComponentProvider#getComponent(java.lang.String,
       * java.util.Map)
       */
      @Override
      public Component getComponent(String componentId, Map<String, Object> parameters) {
        throw new IllegalArgumentException("Component id " + componentId + " not supported."); 
        /* in this howto we only need to return static resources so there is no need to return anything here */
      }
     
      @Override
      public List<ComponentResource> getGlobalComponentResources() {
        final List<ComponentResource> globalResources = new ArrayList<ComponentResource>();
        globalResources.add(createStaticResource(
            "web/com.etendoerp.client.application.examples/js/example-toolbar-button.js", false));
        globalResources.add(createStyleSheetResource(
            "web/com.etendoerp.userinterface.smartclient/etendo/skins/"
                + KernelConstants.SKIN_VERSION_PARAMETER
                + "/com.etendoerp.client.application.examples/example-styles.css", false));
     
        return globalResources;
      }
     
      @Override
      public List<String> getTestResources() {
        return Collections.emptyList();
      }
    }
```
Una breve explicación:

  * Las anotaciones en la parte superior de la clase están relacionadas con [Weld](../concepts/Etendo_Architecture.md#introducing-weld-dependency-injection-and-more.md).
  
  Las anotaciones definen que solo se crea una instancia de esta clase (un singleton) y definen un identificador para esta instancia. 

  * getGlobalResources es importante aquí; muestra cómo registrar los recursos globales definidos en el módulo de ejemplo. 
  
!!!note
      Para su propio módulo, siga la misma estructura de rutas y el mismo enfoque. 

!!!info
    Para explicar cómo Etendo puede encontrar el ComponentProvider: Etendo/Weld analizará el classpath y encontrará todas las clases que tengan una anotación @ComponentProvider.


###  El resultado

Para ver el resultado, reinicie Tomcat, borre la caché del navegador (a veces los estilos `css` no se recogen) y vuelva a la aplicación y, en concreto, a la ventana de pedido de venta. 

Debería ver esto:

!!!note
    El botón no se visualiza en otras ventanas/solapas porque está
    registrado solo para la solapa de cabecera del pedido de venta.

  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_button_to_the_toolbar-5.png)

  

##  Añadir lógica del lado del servidor - Pasos de implementación

El siguiente paso en este procedimiento es añadir la lógica del lado del servidor y llamar a esta lógica desde el cliente. La lógica del lado del servidor se implementa usando el concepto de action handler. 
El concepto de action handler le permite crear clases en
el servidor que pueden ser llamadas desde el cliente. 

###  Implementar el action handler del lado del servidor

El action handler del lado del servidor (`SumOrderActionHandler.java`) recibe un array de números de pedido de los pedidos seleccionados. Sumará los importes de los pedidos y luego devolverá el total como una cadena JSON.

Esta es la implementación del lado del servidor:

```java title="SumOrderActionHandler.java"
     */
package org.openbravo.client.application.examples;

import java.math.BigDecimal;
import java.util.Map;

import org.codehaus.jettison.json.JSONArray;
import org.codehaus.jettison.json.JSONObject;
import org.openbravo.base.exception.OBException;
import org.openbravo.client.kernel.BaseActionHandler;
import org.openbravo.dal.service.OBDal;
import org.openbravo.model.common.order.Order;

/**
 * Sums the orders passed in through a json array and returns the result.
 */
    public class SumOrderActionHandler extends BaseActionHandler {
     
      protected JSONObject execute(Map<String, Object> parameters, String data) {
        try {
     
          // get the data as json
          final JSONObject jsonData = new JSONObject(data);
          final JSONArray orderIds = jsonData.getJSONArray("orders");
     
          // start with zero
          BigDecimal total = new BigDecimal("0");
     
          // iterate over the orderids
          for (int i = 0; i < orderIds.length(); i++) {
            final String orderId = orderIds.getString(i);
     
            // get the order
            final Order order = OBDal.getInstance().get(Order.class, orderId);
     
            // and add its grand total
            total = total.add(order.getGrandTotalAmount());
          }
     
          // create the result
          JSONObject json = new JSONObject();
          json.put("total", total.doubleValue());
     
          // and return it
          return json;
        } catch (Exception e) {
          throw new OBException(e);
        }
      }
    }
```
Notas:

  * Se amplía BaseActionHandler; a menudo este es el mejor enfoque al implementar un ActionHandler. En este caso, solo es necesario implementar el método execute. 
  * Los datos se pueden enviar al servidor de 2 formas: como parámetros y como parte del cuerpo de la solicitud. Por ello, el método execute tiene 2 parámetros. En este ejemplo se utiliza el cuerpo de la solicitud.
  * Use BigDecimal para números, ya que es mucho más preciso que double; desafortunadamente JSON solo soporta doubles. En el sistema core de Etendo, por tanto, los números se envían de cliente-servidor (y viceversa) como cadenas. 
  * la lógica itera sobre los ids de pedido y recupera el pedido usando la [Capa de Acceso a Datos](../concepts/Data_Access_Layer.md). 
  * el resultado se devuelve de nuevo como JSON.

###  Llamar al lado del servidor desde el cliente, mostrando el resultado

A continuación, en el cliente, debe implementarse el método action del botón para llamar al servidor. Aquí está la implementación. 

```javascript
    
          action: function(){
            var callback, orders = [], i, view = this.view, grid = view.viewGrid, selectedRecords = grid.getSelectedRecords();
            // collect the order ids
            for (i = 0; i < selectedRecords.length; i++) {
              orders.push(selectedRecords[i].id);
            }
            
            // define the callback function which shows the result to the user
            callback = function(rpcResponse, data, rpcRequest) {
              isc.say(OB.I18N.getLabel('ETEXAPP_SumResult', [data.total]));
            }
            
            // and call the server
            OB.RemoteCallManager.call('com.etendoerp.client.application.examples.SumOrderActionHandler', {orders: orders}, {}, callback);
```

Nota:

  * selectedRecords contiene la información completa del registro del pedido (businessPartner, etc.); en este caso solo usamos el id 
  * la llamada al servidor es asíncrona; por tanto, se utiliza un callback, que se llama cuando el servidor devuelve el resultado. El callback recibe 3 parámetros; el parámetro data contiene el JSONObject devuelto por el método execute del servidor. 
  * la llamada a RemoteCallManager tiene estos parámetros: 
    * el nombre de clase del action handler 
    * los datos enviados como cuerpo de la solicitud 
    * parámetros de la solicitud (en este caso no hay nada) 
    * y el callback 


Luego, cuando el servidor devuelve la respuesta, se llama al callback, que mostrará un mensaje. 

!!!note
    La etiqueta utilizada en el callback usa sustitución de parámetros.
    Los parámetros se especifican usando %0, %1, etc.:

  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_button_to_the_toolbar-6.png)

###  El resultado

El resultado muestra la suma de las 2 cabeceras de pedido seleccionadas:


![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_button_to_the_toolbar-7.png)

---

Este trabajo es una obra derivada de [Cómo añadir un botón a la barra de herramientas](https://wiki.openbravo.com/wiki/How_to_add_a_button_to_the_toolbar){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.