---
title: Fuentes de datos
tags: 
  - fuentes de datos
  - API
  - Etendo
  - Fuente de datos de Etendo
  - Etendo Classic
  - Selector
  - JSON REST Web Services
---

#  Fuentes de datos

##  Visión general

Esta sección describe cómo definir e implementar fuentes de datos basándose en la funcionalidad de Fuente de datos de Etendo. Una fuente de datos es el principal proveedor de datos en la interfaz de usuario de Etendo. La API de la fuente de datos contiene métodos para obtener datos, actualizar datos y para crear y eliminar datos en el servidor. Una fuente de datos tiene una representación tanto del lado del cliente como del lado del servidor.

Esta sección describe cómo implementar una fuente de datos personalizada. Una fuente de datos personalizada puede utilizarse en componentes de la interfaz de usuario de Etendo Classic como el [Selector](/developer-guide/etendo-classic/concepts/Selectors).

##  Información relacionada

Las funciones de Fuente de datos de Etendo hacen uso de y amplían la funcionalidad de [JSON_REST_Web_Services](/developer-guide/etendo-classic/concepts/JSON_REST_Web_Services).

La Fuente de datos de Etendo implementa y amplía el RESTDatasource de Smartclient de dos maneras:

  * en el cliente, genera una instancia de RESTDatasource de Smartclient (en javascript) 
  * en el servidor, proporciona un servicio web JSON REST que soporta la misma API que la definida por Smartclient 

La implementación de la fuente de datos consta de dos partes:

  * la implementación del lado del servidor de la fuente de datos en java 
  * la definición de la fuente de datos en el Diccionario de Aplicación 

##  API de la fuente de datos

La API de la fuente de datos está definida por la interfaz [DataSourceService](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.service.datasource/src/org/openbravo/service/datasource/DataSourceService.java){target="\_blank"}. Esta interfaz define métodos que son necesarios para un funcionamiento correcto del lado del servidor. Es recomendable ampliar la clase [BaseDataSourceService](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.service.datasource/src/org/openbravo/service/datasource/BaseDataSourceService.java){target="\_blank"}, que se encarga de implementar la mayoría de los métodos.

Tras ampliar la clase BaseDataSourceService, es necesario implementar los siguientes métodos:

    
    
      /**
       * Execute a query request and return the result as a json string. For a query request, the content
       * ({@link #getContent()}) is normally empty, the query parameters can be found in the parameters
       * map ({@link #getParameters()}).
       * 
       * @param parameters
       *          the parameters often coming from the HTTP request
       * @return the json result string
       */
      public String fetch(Map<String, String> parameters);
     
      /**
       * Execute a delete action. The ID of the deleted record is present in the parameters.
       * 
       * @param parameters
       *          the parameters often coming from the HTTP request
       * @return the result message as a json string
       */
      public String remove(Map<String, String> parameters);
     
      /**
       * Execute an insert action. There can be parameters in the parameter map (
       * {@link #getParameters()}) but often the data to insert is present in the content (
       * {@link #getContent()}).
       * 
       * @param parameters
       *          the parameters often coming from the HTTP request
       * @param content
       *          , the request content, is assumed to be a json string
       * @return the result message as a json string
       */
      public String add(Map<String, String> parameters, String content);
     
      /**
       * Execute an update action. There can be parameters in the parameter map (
       * {@link #getParameters()}) but often the data to insert is present in the content (
       * {@link #getContent()}).
       * 
       * @param parameters
       *          the parameters often coming from the HTTP request
       * @param content
       *          , the request content, is assumed to be a json string
       * @return the result message as a json string
       */
      public String update(Map<String, String> parameters, String content);

El contenido y las cadenas devueltas son cadenas JSON que deben ajustarse al mismo formato que el definido en el RESTDatasource de Smartclient.

Al utilizar la fuente de datos en una ventana/formulario clásico de Etendo (como en el caso del [Selector](/developer-guide/etendo-classic/concepts/Selectors/#property-paths-showing-linked-information)), entonces los parámetros contendrán todos los campos del formulario presentes en el formulario HTML.

Para su comportamiento en tiempo de ejecución, la fuente de datos hace un uso extensivo de [JSON_REST_Web_Services](/developer-guide/etendo-classic/concepts/JSON_REST_Web_Services). Por tanto, la fuente de datos en tiempo de ejecución opera de forma muy similar al servicio web JSON. Sin embargo, existen algunas diferencias menores:

  * Cuando solo se [solicita](/developer-guide/etendo-classic/concepts/JSON_REST_Web_Services#get) un único objeto, entonces JSON REST devolverá únicamente una cadena JSON con este objeto. La fuente de datos envolverá esta única cadena JSON y añadirá los metadatos requeridos para la fuente de datos del lado del cliente. 
  * La definición de la fuente de datos en el Diccionario de Aplicación permite especificar una cláusula where. La fuente de datos añadirá esta cláusula where a la consulta antes de llamar a JSON Rest para ejecutar la consulta y devolver la cadena JSON. 

Al desarrollar su propia fuente de datos, tiene sentido estudiar y utilizar las [clases del núcleo](/developer-guide/etendo-classic/concepts/JSON_REST_Web_Services#JSON_Core_Classes) de la funcionalidad JSON REST.

##  Definición de la fuente de datos

Tras la implementación del lado del servidor de la fuente de datos, el siguiente paso es definirla en el diccionario de aplicación. Esto hace posible utilizar la fuente de datos en componentes de la interfaz de usuario definidos en el diccionario de aplicación.

La definición de la fuente de datos consta de dos partes:

  * la «cabecera» de la fuente de datos, que define la clase que implementa la fuente de datos. 
  * los campos de la fuente de datos, que definen los campos de la fuente de datos. 

Para definir la fuente de datos en el diccionario de aplicación, vaya a: Diccionario de Aplicación > Interfaz de usuario > Fuente de datos. A continuación, haga clic en el botón de insertar.

  

![](/assets/developer-guide/etendo-classic/concepts/Datasource1.png)

  
Descripción de los campos en la definición de la fuente de datos:

  * Módulo: seleccione el módulo que entrega esta fuente de datos 
  * Nombre/Descripción: un nombre y una descripción relevantes y descriptivos 
  * Tabla y cláusula where: pueden utilizarse para definir una fuente de datos leyendo directamente de una tabla. 
  * Nombre de clase Java: el nombre de la clase que implementa la fuente de datos. Este campo puede estar vacío. En ese caso, el campo tabla debe estar informado. Si no se especifica un nombre de clase Java, entonces se utiliza la clase [DefaultDataSourceService](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.service.datasource/src/org/openbravo/service/datasource/DefaultDataSourceService.java){target="\_blank"}. Esta clase implementa completamente la interfaz de fuente de datos (soporte CRUD completo mediante servicios web y representación del lado del cliente de la fuente de datos). 
  * Plantilla: la plantilla es responsable de generar la fuente de datos del lado del cliente en javascript. Consulte la siguiente sección sobre cómo implementar una fuente de datos personalizada del lado del cliente para obtener más información sobre el significado de este campo. En general, la única opción a seleccionar es plantilla (la predeterminada). 

Si se especifica una tabla y se utiliza DefaultDataSourceService (por ejemplo, el nombre de clase Java está vacío), entonces no es necesario especificar campos de la fuente de datos. Todas las columnas de la tabla están disponibles automáticamente como campos de la fuente de datos.

Sin embargo, si dispone de una clase de fuente de datos personalizada o desea añadir campos adicionales (calculados) a una fuente de datos, entonces deben definirse como Campos de fuente de datos.

Para añadir campos a una fuente de datos, haga clic en el enlace Campo de fuente de datos en la parte superior de la ventana de fuente de datos.

  

![](/assets/developer-guide/etendo-classic/concepts/Datasource2.png)

  
Descripción de los campos en la definición del campo de la fuente de datos:

  * Nombre: un nombre único que también debe ser un nombre válido de javascript. 
  * Descripción: un campo descriptivo de formato libre. 
  * Referencia: la referencia define el tipo del campo. 
  * Tabla: si la referencia es una referencia de clave externa, entonces este campo puede utilizarse para especificar la tabla a la que se hace referencia. 

##  Implementación de su propia fuente de datos del lado del cliente (Avanzado)

La definición de la fuente de datos se convierte a código javascript utilizando una plantilla. La plantilla se selecciona en la definición de la fuente de datos (véase el paso anterior). Es posible que un módulo añada una nueva plantilla que pueda utilizarse para crear fuentes de datos del lado del cliente.

La creación de una nueva plantilla debe realizarla un desarrollador con un buen conocimiento de Etendo. Para implementar una nueva plantilla, es necesario comprender el procesamiento de plantillas y la funcionalidad de gestión de plantillas utilizada por Etendo. La página [Arquitectura de Etendo](/developer-guide/etendo-classic/concepts/Etendo_Architecture) proporciona información detallada. En ella se tratan tanto el procesamiento de plantillas, el almacenamiento en caché, i18n, como también se dan indicaciones sobre cómo implementar una plantilla personalizada.

La plantilla utilizada para la fuente de datos puede encontrarse en el árbol de fuentes del paquete org.openbravo.service.datasource dentro del paquete org.openbravo.service.datasource.templates en el archivo datasource.ftl. La plantilla hace uso del lenguaje de plantillas freemarker.

Una plantilla personalizada debe crearse dentro de un módulo independiente. Para utilizarla, defínala en Diccionario de Aplicación > Interfaz de usuario > Plantilla.

  

![](/assets/developer-guide/etendo-classic/concepts/Datasource3.png)

  
Los principales campos a configurar:

  * TemplateClasspathLocation debe apuntar a la ubicación en el árbol de fuentes de la plantilla personalizada, incluyendo su nombre de archivo. 
  * ComponentType debe establecerse en datasource. ComponentType determina si la plantilla puede seleccionarse en la ventana de definición de la fuente de datos. 

  

![](/assets/developer-guide/etendo-classic/concepts/Datasource4.png)

  
A continuación, al definir fuentes de datos, se podrá seleccionar la plantilla personalizada.

##  Ejemplos de fuentes de datos

El código fuente de la fuente de datos contiene 2 ejemplos de implementación de una fuente de datos:

  * [DefaultDataSourceService](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.service.datasource/src/org/openbravo/service/datasource/DefaultDataSourceService.java){target="\_blank"}: esta es una implementación completa de la interfaz [DataSourceService](https://github.com/etendosoftware/etendo_core/blob/main/modules_core/org.openbravo.service.datasource/src/org/openbravo/service/datasource/DataSourceService.java){target="\_blank"}. Soporta la obtención con consulta y paginación, así como operaciones de actualización, alta y eliminación. Esta fuente de datos se utiliza ampliamente en la interfaz de usuario de Etendo Classic. 
  * ModelDataSourceService: es una fuente de datos en memoria que proporciona acceso a las propiedades de un modelo utilizando una sintaxis de ruta por puntos. Solo implementa el método fetch. Se utiliza en el [Selector](/developer-guide/etendo-classic/concepts/Selectors/#property-paths-showing-linked-information) para proporcionar acceso al modelo. 

  

![](/assets/developer-guide/etendo-classic/concepts/Datasources-4.png){: .legacy-image-style}

  
Las definiciones de fuentes de datos pueden encontrarse en la aplicación en Diccionario de Aplicación > Interfaz de usuario > Fuente de datos.

  

![](/assets/developer-guide/etendo-classic/concepts/Datasource6.png)
  
!!!note
    DefaultDataSourceService no tiene una definición explícita, ya que se instancia bajo demanda en el servidor. Esto facilita el uso de la fuente de datos directamente para cualquier tabla dentro de Etendo Classic sin requerir una definición explícita para cada tabla.

---

Este trabajo es una obra derivada de [Fuentes de datos](http://wiki.openbravo.com/wiki/Datasources){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.