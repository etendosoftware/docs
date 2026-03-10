---
title: Cómo crear un informe
tags: 
  - Cómo hacer
  - Informes
  - Jaspersoft Studio
  - Classpath
---
#  Cómo crear un informe
  
##  Visión general

En esta sección, el usuario puede encontrar información sobre los pasos necesarios para crear un nuevo informe en Etendo. El ejemplo explicado es un informe sencillo con una lista de productos.

##  Configuración de Jaspersoft Studio
  
!!!note
    Se recomienda utilizar la última versión de Jaspersoft Studio.  
  
  
Primero, necesita descargar Jaspersoft Studio, una herramienta gráfica que permite crear y modificar plantillas de JasperReports (archivos .jrxml).

  * Descargue [Jaspersoft Studio](https://www.jaspersoft.com/products/jaspersoft-community){target="\_blank"}. 
  * En Linux: simplemente descargue el archivo .tgz y descomprímalo; ejecute el binario _Jaspersoft Studio_ ubicado dentro de la carpeta principal.
  * En Windows: descargue y ejecute el archivo .exe.

###  Configuración de la versión de la librería de Jaspersoft Studio
!!! warning
    Etendo soporta Jasper Reports compatible con JasperReports 6.0.0. Por lo tanto, si está utilizando una versión más reciente de Jaspersoft Studio, necesita asegurarse de que la versión de la librería de JasperReports sea 6.0.0. Es muy importante utilizar la versión correcta de la librería de JasperReports, para que el archivo jrxml tenga la sintaxis compatible con Etendo.

* Vaya a `Settings` > `Jaspersoft Studio` > `Compatibility` > `Source .jrxml Version` y configúrelo en 6.0.0.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-1.png)

###  Configuración de las propiedades de Jaspersoft Studio

Algunas propiedades de Jaspersoft Studio deben modificarse para que funcione correctamente. En resumen, necesita asegurarse de que:

  * Ha modificado la propiedad de JasperReport _net.sf.jasperreports.awt.ignore.missing.font_ y la ha establecido en *true*. Puede cambiarse en `Properties` > `Jaspersoft Studio` > `Properties` 
  * No utilice ninguna clase *Scriptlet* 
  * Utilice *Java* como lenguaje de expresión predeterminado 


  
###  Configuración del Classpath

En Jaspersoft Studio, se supone que cada informe forma parte de un proyecto. Por lo tanto, primero necesita crear un nuevo proyecto (`File` > `New` > `Project`).

El proyecto tiene un classpath, y aquí es donde puede añadir los jars que necesite.

  * Haga clic con el botón derecho en el nombre del proyecto: `Properties` > `Java Build Path`
  * Vaya a la pestaña *Libraries* 
  * Haga clic en el botón *Add External Jars* 
  * Añada la librería deseada. 
  * Haga clic en *OK*

##  Creación de la plantilla

  * Vaya a `File` > `New`
  * Seleccione *Jasper Report*
  * Se abrirá el *Asistente de nuevo informe* 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-2.png)

  * Seleccione una plantilla de informe (_Blank_ siguiendo nuestro ejemplo) 
  * Defina un nombre de informe 
  * Defina la ubicación del archivo en el proyecto. 

Más adelante, copiaremos este archivo .jrxml dentro de nuestro módulo de Etendo, que va a contener nuestro informe y también la configuración requerida en el Diccionario de Aplicación.

  * Defina el origen de datos del informe: haciendo clic en "New", se puede configurar una nueva conexión a base de datos usando el *Asistente de adaptador de datos*
  * Haga clic en *New*
  * Seleccione *Database JDBC Connection* y haga clic en _Next_
  * Rellene todos los campos 
    * *Name:* Etendo (o cualquier nombre que desee, p. ej. pi) 
    * *JDBC Driver:* PostgreSQL (`org.postgresql.Driver`). En este caso, usaremos PostgreSQL 
    * *JDBC URL:* `jdbc:postgresql://localhost:5432/etendo` donde _5432_ es el puerto en el que se está ejecutando PostgresSQL y _etendo_ es el SSID de nuestra base de datos 
    * *Username:* tad (puede comprobar su usuario/contraseña en el archivo de configuración gradle.properties. Para más información sobre gradle.properties, visite [Instalar Etendo](../../../getting-started/installation.md#install-etendo)) 
    * *Password:* tad 
  * Haga clic en el botón Finish para generar la conexión JDBC 
  * Pruebe su conexión 
  * Guarde 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-3.png)

Ahora tenemos que configurar la consulta: vamos a listar los productos presentes en la base de datos.

  * Haga clic con el botón derecho en el menú Report Outline y seleccione *Dataset and Query*. Aquí es donde tenemos que establecer la consulta del informe y también es posible cambiar entre las conexiones de base de datos disponibles en caso de que queramos probar la consulta. 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-4.png)

  * Los productos se almacenan en la tabla `M_Product` 
    
        SELECT m_product_id, value, name FROM m_product

  * Tenemos que añadir los campos basados en su consulta que queremos utilizar en el informe, por lo que vamos a añadir: 
    * `m_product_id` 
    * `value` 
    * `name` 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-5.png)

  * Haga clic en *OK* 
  * Recuerde limpiar la clase Scriptlet y modificar el Language para las expresiones 
  * Haga clic con el botón derecho en el menú Report Outline y seleccione *Show Properties*. 
  * En las propiedades del informe a la derecha, busque lo siguiente: 
    * Limpie la clase Scriptlet 
    * Elija Java como Language 
  * Guarde sus cambios 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-6.png)

Ahora vamos a diseñar el diseño del informe

  * Ponga un texto estático como título del informe: _Lista de productos_
  * Coloque los campos en la banda *Detail* y un título en la banda *Column Header* 
  * Guarde sus cambios 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-7.png)

  * Cambie a la subpestaña *Preview* para obtener una vista previa del informe 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-8.png)

!!!note
    Se recomienda utilizar fuentes Dejavu en informes jasper porque estas
    fuentes soportan la mayoría de los caracteres en casi todos los idiomas. Además,
    la tipografía Dejavu es la familia de fuentes que Etendo incluyó en la librería
    jasperreports-fonts.   
  
###  Entorno de ejecución de Etendo

Los informes estándar en Etendo (`src/org/openbravo/erpReports`) hacen uso de varios métodos que residen dentro del *Entorno de ejecución de Etendo*, que no pueden ejecutarse en tiempo de diseño. Por esta razón, proporcionamos un archivo .jar que encapsula los siguientes métodos adaptados de la clase `org.openbravo.erpCommon.utility.Utility`:

  * `public static BufferedImage showImageLogo`: devuelve una imagen de logotipo que ya está incluida en el archivo JAR 
  * `public static String applyCountryDateFormat`: siempre devuelve la fecha formateada con este patrón dd-MM-yyyy 
  * `public static DecimalFormat getCountryNumberFormat`: simplemente devuelve el mismo DecimalFormat recibido como parámetro 

Para ello, para poder previsualizar los informes estándar de Etendo desde *JasperStudio*, basta con importar el archivo .jar en el classpath del proyecto dentro de JasperStudio.

###  Añadir imágenes y logotipos a un informe usando la API ShowImage

Puede utilizar la referencia Image BLOB para mostrar una imagen para un informe específico, o uno de los logotipos de la Compañía en la aplicación. 

Para hacerlo:

1. Añada un objeto de imagen a su informe

2. establezca la clase de expresión en "java.awt.Image" y la expresión de imagen como una llamada a la función ShowImage de la clase Utility (si quiere que muestre una referencia estándar de imagen ImageBLOB, que corresponde a un campo añadido a una pestaña), o a la función ShowImageLogo si quiere mostrar el logotipo de una Organización o Cliente.

Las imágenes cargadas con este método no deben tener canal alfa. No se soporta una capa de transparencia por la función que carga imágenes en Jasper Reports.

  * Si quiere utilizar la función ShowImage, necesita que la expresión de imagen tenga este aspecto: 
    * `org.openbravo.erpCommon.utility.Utility.showImage("IMAGEID")` 

IMAGEID necesita ser el UUID de la imagen que quiere mostrar. Podría establecer este valor usando un parámetro de Jasper.

  * Si quiere utilizar la función ShowImageLogo para mostrar uno de los logotipos, tiene varias opciones. 
    * Esta mostrará el logotipo de la Compañía a nivel de Sistema: 
        * `org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanylogin")` 
    * Esta mostrará el logotipo de la Compañía a nivel de Cliente (el cliente utilizado será aquel con el que el usuario haya iniciado sesión): 
        * `org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanymenu")` 
    * Esta mostrará el logotipo de la Compañía a nivel de Organización: 
        * `org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanydoc", "ORGANIZATIONID")`

ORGANIZATIONID necesita ser el UUID de la Organización cuyo logotipo quiere mostrar. Podría establecer este valor usando un argumento de Jasper. Un ejemplo podría ser `org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanydoc","4387D62C6486481AB3D148442A6AD34E")̣` siendo `4387D62C6486481AB3D148442A6AD34E` el ID de la organización.

##  Registro del informe en el Diccionario de Aplicación

###  Creación del informe

Es posible crear un informe usando una definición de proceso. Para más información, visite [esta sección](How_to_create_a_Report_using_Process_Definition.md).

  * Usando el rol de Administrador del Sistema 
  * Usando el inicio rápido, abra: la ventana *Definición de proceso* 
    * Puede encontrarla en el menú: `Application Dictionary` > `Process Definition` 

  * Cree un nuevo registro 
  * Rellene todos los campos requeridos 
    * *Module:* Seleccione su módulo 
    * *Search Key:* ETPF_ProductList (es una buena práctica comenzar con el [DB_Prefix](../concepts/modularity-concepts.md#DB_prefix) de su módulo) 
    * *Name:* Lista de productos 
    * *UI Pattern:* Informe (usando plantillas JR) 
    * *Data Access Level:* Cliente/Organización 
    * *Handler*: use el valor predeterminado `org.openbravo.client.application.report.BaseReportActionHandler`

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-9.png)

Debemos copiar el archivo de plantilla .jrxml generado con Jaspersoft Studio en nuestro módulo. Al usar Definición de proceso para generar un informe, las plantillas deben almacenarse en la carpeta web del módulo. En nuestro ejemplo, lo ubicamos en la siguiente ruta: `/web/com.etendoerp.platform.features/jasper`

  * Navegue a la pestaña *Report Definition* 
  * Rellene el campo de plantilla PDF con la ubicación del archivo .jrxml 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-10.png)

###  Creación del registro de menú

  * Usando el rol de Administrador del Sistema 
  * Abra la ventana Menú 
  * Cree un nuevo registro 
  * Rellene todos los campos requeridos: 
    * *Module:* Su módulo 
    * *Name:* Nombre de la entrada de menú (Lista de productos) 
    * *Description:* Descripción de la acción relacionada con la entrada de menú 
    * *Action:* Seleccione `Process Definition` 
    * *Process Definition:* Seleccione su Definición de proceso (Lista de productos) 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-11.png)

##  Compilación

Después de haber registrado el informe y la entrada de menú en el Diccionario de Aplicación, necesita compilar para generar el código necesario.

``` bash title="Terminal"
./gradlew smartbuild
```

Una vez completada la compilación, reinicie su servidor Tomcat.

##  Prueba del informe

Si ha completado todos los pasos, debería poder abrir su informe Lista de productos desde el inicio rápido o desde la entrada de menú.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report-12.png)

##  Más detalles

###  Diseño

Para información sobre cómo JasperReports gestiona el diseño, consulte [Creación de informes compatibles con HTML, XLS o CSV](https://community.jaspersoft.com/knowledgebase/tips-n-tricks/making-html-xls-or-csv-friendly-reports/){target="\_blank"}.

Además, puede encontrar [aquí](https://community.jaspersoft.com/knowledgebase/tips-n-tricks/designing-report-jaspersoft-studio/){target="\_blank"} un tutorial con los conceptos básicos sobre cómo diseñar un informe.

###  Configuración del tipo de celda en informes XLS

Por defecto, el motor de informes de Etendo exporta los datos XLS como cadenas. Esto se hace para asegurar que los datos exportados puedan leerse después de abrir el informe con la gran mayoría de aplicaciones de hoja de cálculo.

Si queremos tener un formato particular en una celda de nuestro informe XLS y, por ejemplo, mostrar números dentro de una celda numérica, esta configuración predeterminada puede sobrescribirse a nivel de plantilla.

Para sobrescribir esta configuración, debe hacerse lo siguiente dentro de la plantilla de informe .jrxml:

  1. Añada la propiedad *net.sf.jasperreports.export.xls.detect.cell.type* con true como valor. 
  2. Añada un *patrón* para el campo de texto que se mostrará en la celda XLS. Con la etiqueta `<pattern>`, se puede establecer un patrón fijo y con la etiqueta `<patternExpression>`, es posible definir un patrón dinámico. 

!!!note
    Los *separadores* decimales y de miles utilizados para las celdas numéricas
    exportadas de esta forma serán los definidos dentro del propio programa de hoja de cálculo
    (LibreOffice Calc, Excel, etc.).

###  Creación de un informe usando Informe y Proceso

En [esta sección](how-to-create-a-report-with-ireport.md#registering-the-report-in-application-dictionary), puede encontrar un ejemplo sobre cómo crear un informe de esta manera.

###  Compilación de informes
  
Al imprimir un informe en la aplicación, previamente se compila en tiempo de ejecución. El resultado de esta compilación del informe se almacena en caché si no hay módulos en estado _En Desarrollo_.

Además, es posible gestionar el estado de esta caché mediante una extensión JMX. De este modo, esta extensión permite:

  * Ver si la caché está habilitada. 
  * Habilitar/Deshabilitar la caché. 
  * Ver la lista de informes cuya compilación se almacena en caché. 
  * Limpiar el contenido de la caché. 

###  Código de barras

Es posible generar códigos de barras desde JasperReports, usando las librerías barcode4j o barbecue. Estas librerías están incluidas en el módulo [Generación de código de barras en informes](../../../assets/developer-guide/etendo-classic/how-to-guides/org.openbravo.service.reporting.barcode.zip){target="\_blank"}.

En el módulo Platform Features, hay un ejemplo de un informe que hace uso de diferentes estilos de código de barras; consulte la [plantilla jrxml](../../../assets/developer-guide/etendo-classic/how-to-guides/Barcodes.jrxml){target="\_blank"}.

---

Este trabajo es una obra derivada de [Cómo crear un informe](http://wiki.openbravo.com/wiki/How_to_create_a_Report){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.