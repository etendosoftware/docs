---
title: Cómo crear un Componente de la barra de navegación
tags:
  - Cómo
  - Barra de navegación
  - Componente
  - Etendo Classic
---

#  Cómo crear un Componente de la barra de navegación
  
##  Visión general

Esta sección explica cómo se puede añadir un componente a la barra de navegación principal de Etendo. Los componentes de la barra de navegación se muestran en la parte superior del diseño de Etendo Classic. Se posicionan de izquierda a derecha.

Algunas características principales de los componentes de la barra de navegación de Etendo Classic:

  * Un componente de la barra de navegación puede ser cualquier canvas de [Smartclient](https://smartclient.com/product/documentation.jsp){target="blank"}. 
  * Los módulos pueden proporcionar nuevos componentes de la barra de navegación. 
  * Se puede controlar la posición de un componente de la barra de navegación. 
  * Los componentes de la barra de navegación se pueden habilitar por rol. 

  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Navigation_Bar_Component-0.png)

##  Módulo de ejemplo

Esto está soportado por un módulo de ejemplo que muestra ejemplos del código mostrado y comentado.

  El código de este módulo se puede descargar desde [este repositorio](https://github.com/etendosoftware/com.etendoerp.client.application.examples/tree/main/src/com/etendoerp/client/application/examples).


##  Flujo principal de la generación de la barra de navegación

La generación de la barra de navegación pasa por una serie de pasos:

  1. El usuario inicia sesión y navega a la página de inicio.
  2. La página de inicio construye el diseño principal que consiste en la barra de navegación y el área de contenido principal (con pestañas).
  3. La barra de navegación se genera en el servidor como JavaScript (que se envía al navegador). 
  4. Esto lo realiza el componente de diseño principal. Este componente crea la estructura general de JavaScript y luego lee los componentes de la barra de navegación desde la tabla de componentes de la barra de navegación (usando información de rol). 
  5. Cada componente de la barra de navegación se instancia, se establece su plantilla y se llama al método generate, que genera el JavaScript de ese componente (usando la plantilla). 
  6. Se asume que el JavaScript de cada componente crea un único canvas o un array de canvases de Smartclient. El JavaScript (es decir, el componente de la barra de navegación) se coloca como un miembro del diseño horizontal, que construye la barra de navegación. 

Este flujo principal ilustra que cada componente de la barra de navegación puede implementar su propia visualización proporcionando/usando una plantilla y un componente personalizados.

##  Implementación de un Componente de la barra de navegación

Para crear un componente que se muestre en la barra de navegación, es necesario implementar las siguientes partes:

  * Crear una clase Java (el componente) que represente el componente de la barra de navegación en el servidor 
  * Crear una plantilla que genere el JavaScript que crea el componente en el cliente 
  * Registrar el componente de la barra de navegación en la tabla de componentes de la barra de navegación

Cada uno de estos pasos se describe con más detalle a continuación.

El módulo de ejemplo contiene un componente **Hola Mundo** con una plantilla. Este ejemplo añade un botón a la barra de navegación que (al hacer clic) saludará al usuario actual.

``` 
modules
└── com.etendoerp.client.application.examples
    ├── referencedata
    └── src
        └── com
            └── etendoerp
                └── client
                    └── application
                        └── examples
                            └── templates
                            │   └── hello_world.js.ftl
                            └── HelloWordlComponent.java
```

###  Creación de un Componente

Un componente es útil cuando desea añadir información en tiempo de ejecución al JavaScript del componente de la barra de navegación cuando se genera. Por ejemplo, el nombre de usuario u otra información de rol o de usuario.


!!!info
    Si no tiene el requisito de usar información dinámica en el JavaScript generado de su componente, entonces no necesita implementar un componente (solo una plantilla). Puede hacer uso del componente de plantilla estándar de Etendo: org.openbravo.client.kernel.BaseTemplateComponent, en la tabla de definición de componentes de la barra de navegación.

El módulo de ejemplo tiene un componente de hola mundo que proporciona el usuario actualmente conectado a la plantilla. El componente se puede encontrar en el directorio src del módulo. Aquí está el código:
    
  ```java title="HelloWorldComponent.java"
  package com.etendoerp.client.application.examples;
   
  import org.openbravo.client.kernel.BaseTemplateComponent;
  import org.openbravo.dal.core.OBContext;

  /**
   * Provides a widget which shows a hello world message when clicked.
   * 
   * @author mtaal
   */
  public class HelloWorldComponent extends BaseTemplateComponent {
   
    public String getUserName() {
      return OBContext.getOBContext().getUser().getName();
    }
  }
  ```

###  Creación de una Plantilla

La plantilla contiene el JavaScript real. Una plantilla consta de dos partes:

  1. Un archivo de plantilla (el origen de la plantilla) que termina en `.FTL` (una extensión de [freemarker](https://freemarker.sourceforge.io/docs/){target="blank"}) y que se encuentra en el árbol de fuentes (en el classpath). 
  2. Un registro en la tabla de plantillas.

La plantilla es un mecanismo potente de Etendo, ya que hace posible combinar información generada dinámicamente y permite la sobrescritura de plantillas por otros módulos.

####  El origen de la plantilla

Para crear la plantilla de su componente de la barra de navegación, cree un archivo `.FTL` en el árbol de fuentes de su módulo. El archivo `.FTL` debe contener JavaScript plano con posibles construcciones de freemarker para leer información del componente. El JavaScript debe crear un canvas de Smartclient o un array de JavaScript con instancias de canvas de Smartclient.

Como ejemplo, la plantilla **Hola Mundo** se puede encontrar en el paquete `com.etendoerp.client.application.examples`; crea un botón en el que se puede hacer clic para saludar. El contenido de la plantilla es este:
    
  ```javascript title="hello_world.js.ftl"
  /* jslint */
  isc.Button.create({
    baseStyle: 'navBarButton',
    title: OB.I18N.getLabel('OBEXAPP_HelloWorld'),
    overflow: "visible",
    width: 100,
    layoutAlign: "center",
    showRollOver: false,
    showFocused: false,
    showDown: false,
    click: function() {
      isc.say(OB.I18N.getLabel('OBEXAPP_SayHello', ['${data.userName?js_string}']));
    }
  })
  ```

Algunos aspectos a tener en cuenta en este código fuente JavaScript:

  * El /*jslint*/ indica a Etendo que realice una comprobación sobre el JavaScript generado. Los errores se imprimen en la consola o en el log de salida. 
  * Como puede ver, las plantillas crean un canvas (el Button). También se permite crear un array de canvases. 
  * El título del botón se obtiene mediante el método `OB.I18N.getLabel`. Esto es para soportar traducción; consulte una sección más abajo en este artículo para más información. 
  * Vea la parte `${data.userName?js_string}'`; esta es una construcción de plantilla de [freemarker](https://freemarker.sourceforge.io/docs/){target="blank"} mediante la cual se recupera información de un objeto Java. En el sistema de plantillas de Etendo, la instancia del componente está disponible como el objeto **Datos**. La `${data.userName?js_string}'` llamará al accesor `getName` en el HelloWorldComponent. 

####  Registro de plantilla

El siguiente paso es informar a Etendo de que la plantilla existe. Esto se hace registrando la plantilla en Etendo en la tabla Template. La función de mantenimiento de plantillas se puede encontrar aquí: `Application Dictionary` > `User Interface` > `Template`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Navigation_Bar_Component-2.png)

###  Registro del Componente como un Componente de la barra de navegación

El último paso es añadir el componente a la barra de navegación. Esto se hace a través de la tabla/ventana de componentes de la barra de navegación. Puede encontrarla mediante el lanzamiento rápido o en el menú aquí: `Application Dictionary` > `User Interface` > `Navigation Bar Components`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Navigation_Bar_Component-3.png)

###  El resultado

Después de ejecutar los pasos anteriores, debería ver un botón **Hola Mundo** en la barra de navegación. Al hacer clic, aparecerá un pequeño mensaje de saludo.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Navigation_Bar_Component-4.png)

###  Componentes estáticos de la barra de navegación
  
Marcando el indicador **Componente Estático** de un componente de la barra de navegación en `Application Dictionary` > `User Interface` > `Navigation Bar Components`, se declara como **Estático**. Este tipo de componentes difiere de sus homólogos en la forma en que se crean. Los **Componentes estáticos de la barra de navegación** se cargan al inicio del contenido **JavaScript** utilizado dentro de la aplicación y no requieren una solicitud adicional para cargarse.

Además, el contenido de la plantilla de un **Componentes estáticos de la barra de navegación** se define de una forma ligeramente diferente:

  ```javascript    
  /* jslint */
  {
    className: 'OBApplicationMenuButton',
    properties: {
      title: 'UINAVBA_APPLICATION_MENU',
      initWidget: function () {
        this.Super('initWidget', arguments);
        this.baseData = isc.clone(OB.Application.menu);
      }
    }
  }
  ```

!!!note
    La plantilla define un objeto JSON con dos propiedades:

      * **className** : el nombre de clase del componente de la barra de navegación. 
      * **properties** : contiene el conjunto de atributos y funciones que se utilizarán para configurar el componente. 

---

Este trabajo es una obra derivada de [Cómo crear un Componente de la barra de navegación](http://wiki.openbravo.com/wiki/How_to_create_a_Navigation_Bar_Component){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.