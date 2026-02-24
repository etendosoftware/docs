---
title: Cómo crear un callout que extiende de otro callout
tags:
  - Cómo hacer
  - Callout
  - Extender callout
  - Etendo Classic
---

#  Cómo crear un callout que extiende de otro callout
  
##  Visión general

Esta sección explica cómo implementar un callout que extiende de otro callout. Se explican los principales elementos importantes necesarios para la nueva funcionalidad. Puede encontrar más detalles sobre los callouts en [Cómo crear un Callout](How_to_create_a_Callout.md).
  
##  Módulo de ejemplo

Esta sección se apoya en un módulo de ejemplo que muestra ejemplos del código mostrado y comentado.

El código del módulo de ejemplo se puede descargar desde este repositorio público de GitHub: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="_blank"}.

##  Definición de callouts

Se mostrarán dos callouts. Uno de ellos es el callout padre y el otro es el callout hijo. En este ejemplo, estos dos callouts funcionan en la ventana **Activos**.

####  Definición del callout padre

El siguiente ejemplo sigue [esta guía](How_to_create_a_Callout.md) para implementar el callout. El ejemplo muestra un callout que edita el valor del campo **Nombre**.

```java
  package com.etendoerp.client.application.examples.callouts;
  
  import javax.servlet.ServletException;
   
  import org.openbravo.erpCommon.ad_callouts.SimpleCallout;
   
  public class OBEXAPP_Assets_Name extends SimpleCallout {
   
    protected static final String MODIFIED_FIELD = "_UPDATED";
   
    @Override
    protected void execute(CalloutInfo info) throws ServletException {
   
      // get value of field name and update value
      final String name = info.getStringParameter("inpname");
      info.addResult("inpname", name + MODIFIED_FIELD);
   
      // Combo example. Added three currencies to currency combo.
      info.addSelect("inpcCurrencyId");
      // USD currency is selected.
      info.addSelectResult("100", "USD", true);
      info.addSelectResult("102", "EUR", false);
      info.addSelectResult("103", "DEM", false);
      info.endSelect();
    }
   
  }
```

Como puede ver, el callout obtiene el valor del campo **Nombre** y concatena la siguiente cadena: `_UPDATED`. Además, puede ver un código que define un desplegable. Este código se explicará en la siguiente sección.

####  Definición del callout hijo

Este callout de ejemplo extiende del callout padre definido anteriormente. El ejemplo del desplegable se explica en la siguiente sección.

```java
  package com.etendoerp.client.application.examples.callouts;
  
  import javax.servlet.ServletException;
   
  public class OBEXAPP_Assets_Desc extends OBEXAPP_Assets_Name {
   
    @Override
    protected void execute(CalloutInfo info) throws ServletException {
   
      // OBEXAPP_Assets_Name callout is executed
      super.execute(info);
   
      // Combo example. Removed USD currency from combo and select DEM currency.
      info.addSelect("inpcCurrencyId");
      info.removeSelectResult("100");
      info.addSelectResult("103", "DEM", true);
      info.endSelect();
   
      // Checks if name field has been updated by parent callout.
      String name = info.getStringParameter("inpname");
      String message = "Feature 'Extends a Callout' works as expected.";
      if (name.endsWith(MODIFIED_FIELD)) {
        info.addResult("inpdescription", message);
        info.addResult("MESSAGE", message);
      } else {
        message = "Feature 'Extends a Callout' not works as expected.";
        info.addResult("inpdescription", message);
        info.addResult("ERROR", message);
      }
   
      // Now it is possible to update the 'name' field again and the value will be overwritten
      info.addResult("inpname", "UPDATED...");
    }
  }
```

En primer lugar, el callout `OBEXAPP_Assets_Desc` extiende de `OBEXAPP_Assets_Name`. En esta situación, debe tener en cuenta las siguientes secciones en este callout:

  * Ejecutar el callout padre. 
  
  ```java
      // OBEXAPP_Assets_Name callout is executed
      super.execute(info);
  ```

  * Se ejecutan operaciones para el campo de **desplegable**. Este código se explica en la siguiente sección. 
  
  ```java
      // Combo example. Removed USD currency from combo and select DEM currency.
      info.addSelect("inpcCurrencyId");
      info.removeSelectResult("100");
      info.addSelectResult("103", "DEM", true);
      info.endSelect();
  ```
  
  * Operaciones **después** de ejecutar el callout padre. En este caso, el callout hijo comprueba si el nombre ha sido modificado por el callout padre. A continuación, el callout hijo realiza dos acciones: actualiza el campo de descripción con un mensaje y muestra un mensaje informativo o de fallo. Por último, el campo de nombre se actualiza de nuevo. 

  ```java
      // Checks if name field has been updated by parent callout.
      String name = info.getStringParameter("inpname");
      String message = "Feature 'Extends a Callout' works as expected.";
      if (name.endsWith(MODIFIED_FIELD)) {
        info.addResult("inpdescription", message);
        info.addResult("MESSAGE", message);
      } else {
        message = "Feature 'Extends a Callout' not works as expected.";
        info.addResult("inpdescription", message);
        info.addResult("ERROR", message);
      } 
        
      // Now it is possible to update the 'name' field again and the value will be overwritten
      info.addResult("inpname", "UPDATED...");
  ```

En la siguiente captura de pantalla, puede ver cómo se muestra un mensaje de fallo.

!!!note
    Para el propósito de este ejemplo, se creó una nueva columna llamada 'EM_Obexapp_Callout' para disparar el callout.  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_callout_that_extends_from_another_callout-1.png)

##  Trabajo con desplegables

Como puede ver en las secciones anteriores, el callout `OBEXAPP_Assets_Name` construye un desplegable de moneda. Este desplegable se rellena con 3 monedas y una de ellas queda seleccionada.
  ```java
      // Combo example. Added three currencies to currency combo.
      info.addSelect("inpcCurrencyId");
      // USD currency is selected.
      info.addSelectResult("100", "USD", true);
      info.addSelectResult("102", "EUR", false);
      info.addSelectResult("103", "DEM", false);
      info.endSelect();
  ```

Puede ver el desplegable de moneda con 3 monedas y **USD** como moneda seleccionada.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_callout_that_extends_from_another_callout-2.png)

  
A continuación, el callout hijo `OBEXAPP_Assets_Desc` elimina una moneda y selecciona otra. Este callout hijo extiende `OBEXAPP_Assets_Name` y cambia el desplegable de moneda.
  ```java
      // Combo example. Removed USD currency from combo and select DEM currency.
      info.addSelect("inpcCurrencyId");
      info.removeSelectResult("100");
      info.addSelectResult("103", "DEM", true);
      info.endSelect();
  ```
En esta captura de pantalla, puede ver cómo se muestra el desplegable de moneda cuando se ejecuta el callout hijo.

!!!note
    La moneda DEM está seleccionada y la moneda USD se ha eliminado.    
  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_callout_that_extends_from_another_callout-3.png)

##  Uso del método getStringParameter

Este método se utiliza en los callouts para obtener valores de cualquier campo de la ventana (p. ej., el valor del campo nombre en la ventana Activos).

Ahora, con la inclusión de este proyecto, este método tiene en cuenta si un callout padre modificó un valor. Si un valor fue modificado, el método
`getStringParameter()` devuelve el valor modificado por el callout padre. Si no, el método `getStringParameter()` devuelve el valor inicial del parámetro. 

---

Este trabajo es una obra derivada de [Cómo crear un callout que extiende de otro callout](http://wiki.openbravo.com/wiki/How_to_create_a_callout_that_extends_from_another_callout){target="blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.