---
title: Cómo crear un Callout
tags:
    - Cómo
    - Creación de Callout
    - Callout simple
    - DAL
---

# Cómo crear un Callout

##  Visión general

El objetivo de este artículo es mostrarle cómo crear un nuevo callout. Un callout es una pieza de código Javascript asociada a un campo concreto en una solapa. Este código se ejecuta cada vez que el campo cambia. Es un tipo de sustituto de Ajax, que cambia partes de una solapa/ventana sin necesidad de refrescarla.

Funciona llamando al FIC cuando se modifica un campo con un callout asociado. El FIC (Form Initialization Component) refresca los campos necesarios en función de la lógica del callout.

Esta sección implementa la siguiente nueva funcionalidad: al introducir un nuevo producto, se tiene la opción de introducir el _Identificador_ del producto, el _Nombre_ y la _Categoría_ a la que pertenece. Pero, ¿qué ocurre si nuestro cliente quiere que el identificador se construya automáticamente tomando el nombre del producto, eliminando todos los espacios, añadiendo el guion bajo (_) y el nombre de la categoría a la que pertenece?

Por ejemplo, el Identificador de un producto que tiene el Nombre _Bon Fountain_ y pertenece a la Categoría del producto _Water_ pasaría a ser _BonFountain_Water_. Veamos cómo podría hacerse usando un callout.

Los pasos implicados en la creación de un nuevo callout son:

  1. Crear el/los archivo(s) fuente del callout (normalmente un archivo java). 
  2. Definir el nuevo callout dentro del diccionario de aplicación (`Menú` > `Diccionario de aplicación` > `Configuración` > `Callout`). 
  3. Asociar este callout con una columna de tabla (`Diccionario de aplicación` > `Tabla y columna: campo Callout dentro de la solapa Columna`). 
  4. Compilar la(s) ventana(s)/solapa(s) donde se utiliza esta columna. 

!!!Important
    Los desarrollos relacionados con los puntos (1) y (2) deben pertenecer a
    un módulo que no sea el módulo _core_. Siga la sección [Cómo crear un módulo](How_To_Create_a_Module.md) para crear un nuevo módulo. Para el desarrollo relacionado
    con el punto (3) sobre la modificación de una columna ubicada en _core_, se
    necesita una nueva plantilla. Puede leer el artículo [Cómo cambiar una ventana existente](How_to_change_an_existing_Window.md) para obtener más información.

!!!Note
    Este artículo asume que ha creado tanto el módulo como la plantilla de acuerdo con los artículos mencionados.  

  
##  Creación del Callout

Los callouts existentes se encuentran en [src/org/openbravo/erpCommon/ad_callouts](https://github.com/etendosoftware/etendo_core/tree/main/src/org/openbravo/erpCommon/ad_callouts){target="_blank"}.

La forma correcta de crear un callout es extendiendo la clase SimpleCallout.
Esta clase simplifica el código del callout, oculta parte de los detalles internos del
callout y le mantiene centrado en las operaciones requeridas. Para acceder a datos de base de datos
se utiliza DAL.

###  Teoría

Para desarrollar un nuevo callout basado en esta clase, solo tiene que crear una nueva
clase java que extienda SimpleCallout y sobrescribir el siguiente método:
```java
  protected void execute(CalloutInfo info) throws ServletException;
```
En este método puede desarrollar la lógica del callout y usar el objeto info
de la clase CalloutInfo para acceder a campos de la ventana, base de datos y otros
métodos. Los más importantes son:

  * public String `getStringParameter(String param, RequestFilter filter)` : Devuelve el valor de un campo llamado param como un String usando el filtro para aceptar valores. 
  * public BigDecimal `getBigDecimalParameter(String param) throws ServletException` : Este método devuelve el valor de un campo llamado param como un BigDecimal. 
  * public void `addResult(String param, String value)` : Este método establece el valor de un campo llamado param con el valor String indicado. 
  * public void `addResult(String param, Object value)` : Este método establece el valor de un campo llamado param con el valor indicado. Este método es útil para establecer números como objetos BigDecimal. 
  * public void `addSelect(String param)` : Inicia la inclusión de valores de un campo llamado param de tipo select. 
  * public void `addSelectResult(String name, String value)` : Añade una entrada al campo select y la marca como no seleccionada. 
  * public void `addSelectResult(String name, String value, boolean selected)` : Añade una entrada al campo select. 
  * public void `endSelect()` : Finaliza la inclusión de valores en el campo select. 
  * protected void `showMessage(String value)` : Muestra un mensaje en el navegador con el valor indicado. 
  * protected void `showError(String value)` : Muestra un mensaje de error en el navegador con el valor indicado. 
  * protected void `showWarning(String value)` : Muestra un mensaje de advertencia en el navegador con el valor indicado. 
  * protected void `showInformation(String value)` : Muestra un mensaje informativo en el navegador con el valor indicado. 
  * protected void `showSuccess(String value)` : Muestra un mensaje de éxito en el navegador con el valor indicado. 
  * protected void `executeCodeInBrowser(String value)` : Ejecuta en el navegador el código javascript indicado en el valor. 
  * public String `getLastFieldChanged()` : Devuelve el nombre del campo que disparó el callout. 
  * public String `getTabId()` : Devuelve el Id de la solapa que disparó el callout. 
  * public String `getWindowId()` : Devuelve el Id de la ventana que disparó el callout. 
  * public `VariablesSecureApp vars` : Este campo de instancia contiene el VariablesSecureApp asociado al servlet del callout. 

Es importante mantener la coherencia con cada tipo de dato esperado (String, BigDecimal, ...)

Vea la siguiente clase como ejemplo de una clase que actualmente utiliza
SimpleCallout: [SL_Project_Service](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/erpCommon/ad_callouts/SL_Project_Service.java){target="_blank"}. Este callout simplemente toma el valor numérico de dos campos, calcula la suma y la escribe en otro campo. Esta
es la parte interesante del código que realiza la lógica:
```java
  @Override
  protected void execute(CalloutInfo info) throws ServletException { 
    BigDecimal serviceSerCost = info.getBigDecimalParameter("inpservsercost");
    BigDecimal serviceOutCost = info.getBigDecimalParameter("inpservoutcost"); 
    BigDecimal serviceTotalCost = serviceSerCost.add(serviceOutCost);
    info.addResult("inpservcost", serviceTotalCost);
  }
```
###  Ampliar un Callout

Es posible implementar un callout que extienda de otro callout. Para
más información, visite este tutorial [Cómo crear un callout que extiende de otro callout](How_to_create_a_callout_that_extends_from_another_callout.md).

  
###  Cálculo del Identificador del producto usando SimpleCallout

Definamos las tareas que deben ser realizadas por el callout:

  1. Recuperar el nombre del producto tal y como lo introdujo el usuario 
  2. Recuperar el ID de la categoría seleccionada por el usuario desde un desplegable 
  3. Obtener el nombre de la categoría del producto en la base de datos usando el ID de categoría del producto recuperado 
  4. Eliminar los espacios de los nombres del producto y de la categoría 
  5. Construir el Identificador 
```java
    // the package name corresponds to the module's manual code folder 
    // created above
    package com.etendoerp.customer.example.ad_callouts;
     
    import javax.servlet.ServletException;
     
    import org.openbravo.utils.FormatUtilities;
    import org.openbravo.erpCommon.ad_callouts.SimpleCallout;
    import org.openbravo.base.secureApp.VariablesSecureApp;
    // classes required to retrieve product category data from the 
    // database using the DAL
    import org.openbravo.dal.service.OBDal;
    import org.openbravo.model.common.plm.ProductCategory;
     
    // the name of the class corresponds to the filename that holds it 
    // hence, modules/modules/org.openbravo.howtos/src/org/openbravo/howtos/ad_callouts/ProductConstructSearchKey.java.
    // The class must extend SimpleCallout
    public class ProductConstructSearchKey extends SimpleCallout {
     
      private static final long serialVersionUID = 1L;
     
      @Override
      protected void execute(CalloutInfo info) throws ServletException {
     
        // parse input parameters here; the names derive from the column
        // names of the table prepended by inp and stripped of all
        // underscore characters; letters following the underscore character
        // are capitalized; this way a database column named
        // M_PRODUCT_CATEGORY_ID that is shown on a tab will become
        // inpmProductCategoryId html field
        String strProductName = info.getStringParameter("inpname", null);
        String strProductCategoryId = info
                        .getStringParameter("inpmProductCategoryId", null);
     
        // inject the result into the response
        info.addResult("inpvalue", getConstructedKey(info.vars, strProductName, strProductCategoryId));
      }
     
      protected String getConstructedKey(VariablesSecureApp vars,
            String strProductName, String strProductCategoryId) {
     
        // Retrieve the product category name
        final ProductCategory productCategory = OBDal.getInstance().get(ProductCategory.class,
                strProductCategoryId);
        String strProductCategoryName = productCategory.getName();
     
        // construct full key
        String generatedSearchKey = FormatUtilities.replaceJS(strProductName
                    .replaceAll(" ", ""))
                    + "_" + strProductCategoryName.replaceAll(" ", "");
     
        // return generated key
        return generatedSearchKey;
      }
    }
``` 

## Definición del Callout dentro del diccionario de aplicación

!!!note
    En esta fase, solo necesita tener su módulo como "En desarrollo".

Usando el rol _System Administrator_, navegue a `Diccionario de aplicación` > `Configuración` > `Callout`. Cree un nuevo registro tal y como se indica en la captura de pantalla siguiente:

!!!warning
    El nombre del callout no debe tener espacios ni caracteres javascript ilegales.  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Callout-3.png)

  
Guarde y navegue a la solapa _Callout class_ de la misma ventana. Verá
que el nombre de la clase Java se generó automáticamente,
sin embargo, no de forma correcta ya que el nombre no pudo coincidir con el nombre de _Callout_ que
ha proporcionado. Corríjalo en línea con el nombre de su paquete/clase del callout. Vea la
captura de pantalla siguiente:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Callout-4.png)

  
Ahora Etendo Classic sabe que existe un callout y que está implementado por la clase que
acaba de especificar.

!!!warning 
    Recuerde ejecutar
    ```./gradlew export.database```
    para persistir sus cambios en su módulo.  
 
  
##  Asociación del Callout con una columna

!!!note
    En esta fase, necesita tener SOLO su plantilla como "En desarrollo".

Usando el rol _System Administrator_ navegue a `Diccionario de aplicación` > `Tablas y columnas` > y busque la tabla de BD _M_Product_. Esta es la tabla subyacente de la solapa principal de la ventana _Producto_.

Vaya a la solapa Columna, busque el registro _Nombre_ y edítelo. Busque el desplegable Callout
que en este punto debería estar vacío. Seleccione nuestro
callout _Product_Construct_SearchKey_ y guarde el registro:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Callout-6.png)

  
Haga lo mismo para el registro _Categoría del producto_ ya que un cambio en cualquiera de ellos
también debería regenerar el Identificador.

!!! warning
    Recuerde ejecutar
    ```./gradlew export.database```

    y

    ```./gradlew export.config.script```

    para persistir sus cambios en su plantilla.  
  
  
##  Compilación de la ventana

Por último, para que el callout tenga efecto, la ventana que lo utiliza necesita ser
recompilada y desplegada en Tomcat. Ejecute:
  ``` bash
    ./gradlew smartbuild 
  ```

!!!info
    Una vez finalizada la compilación, reinicie el servidor Apache Tomcat.  
  

##  El resultado

Usando el rol _Group Admin_ (o su rol de 'administrador' definido),
navegue a la ventana `Gestión de datos maestros` > `Producto`. Introduzca un nuevo
producto con Nombre = _Bon Fountain_ y salga del campo Nombre. Observe
cómo cambia el Identificador. Después, cambie la Categoría del producto a otra
y vea cómo el cambio se refleja dentro del campo Identificador.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Callout-8.png)

Por último, guarde los cambios.

---

Este trabajo es una obra derivada de [Cómo crear un Callout](http://wiki.openbravo.com/wiki/How_to_create_a_Callout){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.