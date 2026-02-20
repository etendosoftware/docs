---
title: Cómo crear un nuevo servicio web REST
tags: 
    - Servicio web REST
    - Salida XML
    - Configuración del Módulo 
    - Registro del servicio web


status: beta
---

# Cómo crear un nuevo servicio web REST

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.


## Visión general

Esta sección explica cómo crear un **nuevo servicio web** que devuelve todas las partes de venta para un producto específico. El enfoque está en la **lectura de datos** en lugar de actualizar la base de datos. Dado que la respuesta debe proporcionarse en formato XML, el artículo también describe cómo convertir objetos de base de datos a XML.

La sección final explica cómo el XML recibido a través de una solicitud de servicio web puede transformarse en **objetos de negocio** y utilizarse para actualizar la base de datos.

Etendo REST proporciona una interfaz tipo CRUD que permite a aplicaciones externas recuperar, actualizar, crear y eliminar objetos de negocio mediante solicitudes HTTP estándar.

El servicio web descrito aquí se ejecuta dentro del framework de Etendo REST, aprovechando funcionalidades integradas como **seguridad** y **gestión de excepciones**.

Una implementación de servicio web de Etendo REST consta de dos partes:

- Una clase que define el comportamiento del servicio web e implementa la interfaz `org.openbravo.service.web.WebService`.
- Un archivo de configuración que registra el servicio web dentro del framework de **Etendo REST**.

Ambos elementos se tratan en este documento.

!!! info
    Para una introducción a Etendo REST, consulte [Conceptos de servicios web REST](../concepts/)

##  Módulo

Todos los nuevos desarrollos deben pertenecer a un módulo que no sea el módulo **core**.

!!! info
    Lea la sección [Cómo crear un módulo](../how-to-guides/how-to-create-a-module.md) para crear un nuevo módulo.

##  Implementación de la lógica del servicio web

El servicio web devolverá todas las partes de venta para un determinado producto. Este es el flujo de trabajo del servicio:

1. Recibir la solicitud HTTP que contiene el ID del producto como parámetro.
2. Leer todas las partes de venta que tengan este producto en cualquiera de las líneas de la parte. 
3. Convertir la(s) parte(s) de venta a un XML. 
4. Devolver el XML al navegador del cliente que envía la solicitud. 

Como se mencionó anteriormente, la clase del servicio web debe implementar la interfaz `org.openbravo.service.web.WebService`. Esta interfaz tiene cuatro métodos que corresponden a los métodos de solicitud HTTP: **GET, POST, PUT, DELETE**. Los cuatro métodos reciben los mismos tres parámetros:

1. **ruta**: la parte de la ruta después de la ruta de contexto, 
2. **solicitud**: el objeto de solicitud Http, 
3. **respuesta**: el objeto de respuesta Http. 

En este escenario, el objeto **solicitud** es necesario para recuperar el parámetro **productID** y el objeto **respuesta** para devolver el XML al navegador del cliente.

Ahora suponga que el servicio web se creará en un módulo con javaPackage: `org.openbravo.howtos`. Tras crear un módulo, debería existir una carpeta:

```
EtendoERP/modules/org.openbravo.howtos
```

Cree un directorio **src** en esta carpeta. Dentro de esta carpeta, cree la estructura completa de carpetas según el nombre completo del paquete en el que residirá el servicio web: `org.openbravo.howtos.service.getsalesorders` 
 
Por lo tanto, la estructura de carpetas que debe crearse es:

```
EtendoERP/modules/org.openbravo.howtos/src/org/openbravo/howtos/service/getsalesorders/
```

A continuación, cree un nuevo archivo Java en esa carpeta:

```
EtendoERP/modules/org.openbravo.howtos/src/org/openbravo/howtos/service/getsalesorders/SalesOrdersByProductWebService.java
```

con el contenido que se muestra a continuación:

```java
/*
    *************************************************************************
    * The contents of this file are subject to the Openbravo  Public  License
    * Version  1.0  (the  "License"),  being   the  Mozilla   Public  License
    * Version 1.1  with a permitted attribution clause; you may not  use this
    * file except in compliance with the License. You  may  obtain  a copy of
    * the License at http://www.openbravo.com/legal/license.html 
    * Software distributed under the License  is  distributed  on  an "AS IS"
    * basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
    * License for the specific  language  governing  rights  and  limitations
    * under the License. 
    * The Original Code is Openbravo ERP. 
    * The Initial Developer of the Original Code is Openbravo SLU 
    * All portions are Copyright (C) 2001-2009 Openbravo SLU 
    * All Rights Reserved. 
    * Contributor(s):  ______________________________________.
    ************************************************************************
    */
package org.openbravo.howtos.service.getsalesorders;
 
import java.io.StringWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
 
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
 
import org.hibernate.criterion.Restrictions;
import org.openbravo.base.structure.BaseOBObject;
import org.openbravo.dal.service.OBCriteria;
import org.openbravo.dal.service.OBDal;
import org.openbravo.dal.xml.EntityXMLConverter;
import org.openbravo.model.common.order.OrderLine;
import org.openbravo.model.common.plm.Product;
import org.openbravo.service.web.WebService;
 
/**
 * Implementation of example webservice querying for all sales orders on the basis of a product.
 * 
 * @author mtaal
 */
public class SalesOrdersByProductWebService implements WebService {
 
    private static final long serialVersionUID = 1L;
 
    public void doGet(String path, HttpServletRequest request, HttpServletResponse response)
        throws Exception {
    // do some checking of parameters
    final String productID = request.getParameter("product");
    if (productID == null) {
        throw new IllegalArgumentException("The product parameter is mandatory");
    }
    final Product product = OBDal.getInstance().get(Product.class, productID);
    if (product == null) {
        throw new IllegalArgumentException("Product with id: " + productID + " does not exist");
    }
 
    // select lines from C_ORDERLINE table that match the product
    final OBCriteria<OrderLine> orderLineList = OBDal.getInstance().createCriteria(OrderLine.class);
    orderLineList.add(Restrictions.eq(OrderLine.PROPERTY_PRODUCT, product));
    final List<BaseOBObject> orders = new ArrayList<BaseOBObject>();
 
    // iterate through the lines
    for (OrderLine orderLine : orderLineList.list()) {
        // get the order and only add each order once
        if (!orders.contains(orderLine.getSalesOrder())) {
        orders.add(orderLine.getSalesOrder());
        }
    }
 
    // get an xml converter and set some options
    final EntityXMLConverter exc = EntityXMLConverter.newInstance();
    // also export OrderLines
    exc.setOptionIncludeChildren(true);
    // and embed them in the OrderLines
    // element in an Order.
    exc.setOptionEmbedChildren(true);
    // do not read and convert referenced data in the xml
    // so for example a product reference (from orderLine)
    // will be just one tag with the product id and not a
    // complete product xml document
    exc.setOptionIncludeReferenced(false);
 
    // also export the client/organization elements
    exc.setOptionExportClientOrganizationReferences(true);
 
    // write the output to a String writer
    StringWriter sw = new StringWriter();
    exc.setOutput(sw);
 
    // convert
    exc.process(orders);
 
    // and get the result
    final String xml = sw.toString();
 
    // write to the response
    response.setContentType("text/xml");
    response.setCharacterEncoding("utf-8");
    final Writer w = response.getWriter();
    w.write(xml);
    w.close();
    }
 
    public void doDelete(String path, HttpServletRequest request, HttpServletResponse response)
        throws Exception {
    }
 
    public void doPost(String path, HttpServletRequest request, HttpServletResponse response)
        throws Exception {
    }
 
    public void doPut(String path, HttpServletRequest request, HttpServletResponse response)
        throws Exception {
    }
}
```

Como puede verse, aquí solo se implementa el método **doGet**; la actualización o eliminación normalmente se gestionaría en los otros métodos, que no aplican a nuestros requisitos.

Este es el flujo de trabajo del método `doGet()`:

1. primero, consulta el **Producto** y luego las **OrderLines**, 
2. para cada OrderLine, la **Parte** se añade a la lista de resultados,
3. la lista de resultados se convierte a **XML** usando `org.openbravo.dal.xml.EntityXMLConverter`. Este conversor tiene diferentes opciones, como se ilustra arriba. El javadoc de `EntityXMLConverter` describe en detalle el significado de estas opciones. 

Después de añadir el archivo Java anterior, debería haber algo similar a la siguiente estructura de archivos:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_new_REST_webservice-1.png)


##  Registro del servicio web

Una vez escrito el servicio web, regístrelo para que Etendo lo conozca. Para ello, utilice un **archivo de configuración XML**. Este archivo debe crearse en la carpeta config dentro de la carpeta del módulo:

```
EtendoERP/modules/org.openbravo.howtos/config
```

Como este archivo se copia al directorio WEB-INF durante la compilación junto con otros
archivos de configuración, necesita un nombre único; por lo tanto:
    
```
<moduleJavaPackage>-provider-config.xml
```

donde `moduleJavaPackage` es el paquete Java del módulo introducido al definir el módulo. En este caso, sería:

    
```
org.openbravo.howtos-provider-config.xml
```

Ahora, el contenido de este archivo:

```XML
    
<?xml version="1.0" encoding="UTF-8"?>
<provider>
<bean>
    <name>doIt</name>
    <class>org.openbravo.howtos.service.getsalesorders.SalesOrdersByProductWebService</class>
    <singleton>true</singleton>
</bean>
</provider>
```


!!! note
    Asegúrese de que la primera línea que define el archivo XML no contenga espacios iniciales o el servicio web no funcionará debido a una sintaxis no bien formada.  
  
  
El contenido del archivo de configuración se utiliza para **mapear la URL del servicio web a la clase** que ejecutará la lógica de ese servicio web. El elemento singleton no se utiliza por el momento.


!!! info
    La URL utilizada para acceder al servicio web viene reflejada por el **Nombre** registrado aquí, precedido por el paquete Java del módulo, separado por un punto. Por lo tanto, la URL se define mediante esta fórmula http://(serveraddress)/etendo/ws/(moduleJavaPackage).(name). 
    
!!! note
    Tenga en cuenta que solo se utiliza `moduleJavaPackage` y no el paquete completo de la clase que implementa el servicio web.   
  

  
##  Instalación del servicio web

El servicio web ya puede **compilarse, desplegarse y probarse**. Para ello, utilice la siguiente tarea estándar usada para compilar código manual:
    
```
 ./gradlew compile.complete smartbuild --info 
```

A continuación, reinicie Tomcat.

Al instalar el servicio web como un módulo, utilice la ventana de la aplicación `Application Dictionary > Application > Module Management` para instalarlo y reconstruir la aplicación.

El archivo `org.openbravo.howtos-provider-config.xml` debería estar ahora presente en el directorio `WEB-INF`.

##  Llamada al servicio web

(Re)inicie Etendo y pruebe el servicio web introduciendo esta URL en el navegador: `http://localhost:8080/etendo/ws/org.openbravo.howtos.doIt?product=1000001&stateless=true`
    

!!! note
    Tenga en cuenta que el `ID` del producto puede ser diferente en su instalación. Observe también que el paquete Java del módulo se antepone al nombre del servicio web definido dentro del archivo de configuración. Recuerde la fórmula: **http://(serveraddress)/etendo/ws/(moduleJavaPackage).(webservicename)**. 
  
  
El sistema probablemente le pedirá iniciar sesión.

!!! info
    El usuario debe tener suficientes privilegios para leer partes de venta y productos. Si está utilizando los datos de demostración estándar de Etendo SmallBazaar y el usuario Etendo, entonces este artículo debería funcionar con el rol **System Administrator**.  
  
!!! note
    El parámetro stateless evitará que el servidor cree una sesión HTTP. Esto es bastante importante para llamadas al servicio web de **alta frecuencia**, que no deberían ocupar recursos innecesariamente en el servidor.  
  
  
Debería ver el XML que muestra una parte de venta:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_new_REST_webservice-7.png)


##  Solicitudes de servicio web sin estado - Sesión HTTP

Importante para llamadas al servicio web de **alta frecuencia**: por defecto, las solicitudes de servicio web de Etendo son **con estado**, lo que significa que cada llamada al servicio web creará y utilizará una **sesión HTTP** en el servidor Etendo. Dependiendo de cómo configure el cliente para llamar al servicio web, esto incluso puede significar que cada solicitud de servicio web crea una nueva sesión HTTP. Esto no es recomendable para solicitudes de servicio web de alta frecuencia. En caso de llamadas de alto volumen, puede tener sentido pasar a una **implementación sin estado**.

Hay 2 formas de conseguir un manejo sin estado de las solicitudes de servicio web:

- Pasar el parámetro stateless=true en la URL de la solicitud. Por ejemplo: `http://localhost:8080/etendo/ws/org.openbravo.howtos.doIt?product=1000001&stateless=true`
    

- Anotar la clase del servicio web con la anotación `AuthenticationManager.Stateless`: 

``` java
    @AuthenticationManager.Stateless
public class POSTestStatelessWebservice implements WebService {
...
}
```
Al realizar solicitudes sin estado, la implementación del servicio web no debe esperar que exista una sesión HTTP ni crear una nueva sesión HTTP. Por ejemplo, el objeto `VariablesBase` no puede utilizarse en solicitudes de servicio web sin estado. 

Aparte de eso, la mayor parte de la funcionalidad base del framework (como la capa de acceso a datos y el objeto OBContext) está disponible para la lógica.

##  Añadir lógica para realizar actualizaciones

Hasta ahora, aquí se ha tratado la recuperación de información de la base de datos y su devolución como **XML**. La actualización de información debería implementarse oficialmente (según el principio REST) en el **método PUT**, pero es necesario elegir lo que sea práctico.

Para actualizar, un flujo común es el siguiente:

1. **Recibir** la cadena XML desde el objeto de solicitud. 
2. **Convertir** la cadena XML a un conjunto de objetos de negocio. 
3. **Procesar** estos objetos de negocio; por ejemplo, guardarlos en la base de datos. 

A continuación, se muestra un código de ejemplo que sigue este flujo:

``` java
public void doPut(String path, HttpServletRequest request, HttpServletResponse response)
    throws Exception {
    // read the xml from the request inputstream into a Dom4j Document
    final SAXReader reader = new SAXReader();
    final Document document = reader.read(request.getInputStream());
     
    // create a converter from xml to Openbravo business objects
    final XMLEntityConverter xec = XMLEntityConverter.newInstance();
    xec.setClient(OBContext.getOBContext().getCurrentClient());
    xec.setOrganization(OBContext.getOBContext().getCurrentOrganization());
     
    // for a webservice referenced entities should not be created, see the javadoc
    // for more information
    xec.getEntityResolver().setOptionCreateReferencedIfNotFound(false);
     
    // process the dom4j document, does the actual conversion
    xec.process(document);
     
    // list the new objects (which do not yet exist in the db)
    for (BaseOBObject bob : xec.getToInsert()) {
        System.err.println("New business objects: " + bob.getIdentifier());
    }
     
    // list the objects which will be updated
    for (BaseOBObject bob : xec.getToUpdate()) {
        System.err.println("Updated business objects: " + bob.getIdentifier());
    }
     
    // and return something...
    final String returnMessage = WebServiceUtil.getInstance().createResultXMLWithObjectsAndWarning(
        "Action performed successfully", "", xec.getWarningMessages(), xec.getToInsert(),
        xec.getToUpdate(), null);
    try {
        final Writer w = response.getWriter();
        w.write(returnMessage);
        w.close();
    } catch (final Exception e) {
        throw new OBException(e);
    }
     
    // NOTE: as transaction handling is automatic the updated objects are updated automatically
    // in the db at the end of the request, this may fail as the new objects are not inserted in
    // the db, therefore rolling back, this is just for demo.
    OBDal.getInstance().rollbackAndClose();
}
```

!!! info
    Para una descripción más detallada, consulte [Servicios web REST JSON](../concepts/json-rest-web-services.md). 

---
Este trabajo es una obra derivada de [Cómo crear un nuevo servicio web REST](http://wiki.openbravo.com/wiki/How_to_create_a_new_REST_webservice){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.