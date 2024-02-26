![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  How to create a new REST webservice

##  Contents

  * 1  Objective 
  * 2  Module 
  * 3  Implementing the webservice logic 
  * 4  Registering the webservice 
  * 5  Installing the webservice 
  * 6  Calling the webservice 
  * 7  Stateless Webservice Requests - HTTP Session 
  * 8  Adding logic to do updates 
  * 9  Relevant Links 
  * 10  Tips & tricks and trouble shooting 

  
---  
  
##  Objective

In this howto article we will create a new webservice which returns all sales
orders for a certain product. The article will focus on reading information
and not updating the database. As the information is needed to be returned in
xml format, we will show how objects read from the database can be converted
to it.

The last section describes how to convert xml (received through a web service
request) to a business object structure and update the database.

Openbravo REST provides a  CRUD-like  interface so that external applications
can retrieve, update, create and delete business objects through standard HTTP
requests.

We will add a webservice here which runs inside of the Openbravo REST
framework. By implementing a new web service within Openbravo REST you can
benefit from standard functionality such as security and exception handling.

An Openbravo REST webservice implementation consists of two parts:

  * A class implementing the desired web service behavior. This class should implement the interface: _org.openbravo.service.web.WebService_ . 
  * A configuration file to register the webservice with Openbravo REST framework. 

Both parts will be discussed.

For an introduction to Openbravo REST, see:

  1. REST Web Services concepts 
  2. This blog post 

##  Module

All new developments must belong to a module that is not the _core_ module.
Please follow the  How to create and package a module  section to create a new
module.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This article will assume such a module has been created accordingly.  
---|---  
  
  

##  Implementing the webservice logic

The webservice shall return all the sales orders for a certain product. Here
is the workflow of the service:

  1. Receive the http request which contains the product ID as a parameter 
  2. Read all sales orders which have this product in any of the order lines 
  3. Convert the sales order(s) to an xml 
  4. Return the xml to the client browser sending the request 

As mentioned above your webservice class should implement the interface
_org.openbravo.service.web.WebService_ . This interface has four methods which
correspond to the HTTP request methods: GET, POST, PUT, DELETE. The four
methods all receive the same three parameters:

  1. path: the part of the path after the context path, 
  2. request: the Http request object, 
  3. response: the Http response object. 

Within our scenario the 'request' object is required in order to retrieve the
'productID' parameter and the 'response' object to return the xml to the
client browser.

Now assume that the webservice will be created in a module with javaPackage:
org.openbravo.howtos. After creating a module (see the  how-to create and
package a module  article) there should be a folder:

    
    
    OpenbravoERP/modules/org.openbravo.howtos
    

Create a _src_ directory in this folder and if you are using Eclipse add it to
the source path (Java Build Path) of the openbravo project (see project
properties in Eclipse). Within this folder, create the full folder structure
according to the full package name we would like our webservice to reside in:
_org.openbravo.howtos.service.getsalesorders_ . Hence, the folder structure
that should be created is:

    
    
    OpenbravoERP/modules/org.openbravo.howtos/src/org/openbravo/howtos/service/getsalesorders/
    

Next create a new Java file in that folder:

    
    
    OpenbravoERP/modules/org.openbravo.howtos/src/org/openbravo/howtos/service/getsalesorders/SalesOrdersByProductWebService.java
    

with the content given below:

    
    
     
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

As you can see only the **doGet** method is implemented here, the update or
delete would normally be handled in the other methods that do not apply to our
requirements.

Here is the workflow of the doGet() method:

  1. first, it queries for the  Product  and then for the  OrderLines 
  2. for each OrderLine the  Order  is added to the result list. 
  3. the result list is then converted to xml using the  org.openbravo.dal.xml.EntityXMLConverter  . This converter has different options as illustrated above. The javadoc of the EntityXMLConverter describes in detail what the meaning of these options is. 

After adding the above Java file you should have something similar to the
following file structure:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_new_REST_webservice-1.png){: .legacy-image-style}

  
If you use Eclipse, make sure you add the
_OpenbravoERP/modules/org.openbravo.howtos/src_ folder as a source path to
your project (right click on the Eclipse development project and select
project properties and then Java Build Path, add the folder here). This way,
Eclipse will know to compile any java sources found within the src folder and
subfolders.

##  Registering the webservice

Once the webservice is written you need to register it so that Openbravo ERP
knows about it. Use an xml configuration file for this. This file needs to be
created in the config folder in the module's folder:

    
    
    OpenbravoERP/modules/org.openbravo.howtos/config
    

As this file is copied to the WEB-INF directory during the build with other
configuration files it needs a unique name, hence:

    
    
    <moduleJavaPackage>-provider-config.xml
    

where <moduleJavaPackage> is the module's Java package you entered when
defining the module. In our case, it would be:

    
    
    org.openbravo.howtos-provider-config.xml
    

Now, to the contents of this file:

    
    
     <?xml version="1.0" encoding="UTF-8"?>
     <provider>
       <bean>
           <name>doIt</name>
           <class>org.openbravo.howtos.service.getsalesorders.SalesOrdersByProductWebService</class>
           <singleton>true</singleton>
       </bean>
     </provider>

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

**IMPORTANT** : Make sure the first line defining the xml file contains no
leading spaces or the webservice will not work due to the non well-formed
syntax!  
  
---|---  
  
The content of the **configuration file is used in order to map the URL of the
webservice to the class** which will execute the logic of that webservice. The
singleton element is not used at the moment.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

**IMPORTANT** : the URL used to access the webservice is reflected by the
<name> registered here, prefixed by the module's java package, separated by a
dot. Hence, the URL is defined by this formula: ** http://
<serveraddress>/openbravo/ws/<moduleJavaPackage>.<name> ** . Note that only
the <moduleJavaPackage> is used and not the entire package of the class that
implements the webservice! More information on this will be given below.  
  
---|---  
  
##  Installing the webservice

The webservice can now be compiled, deployed and tested. To do so, use the
following standard task used to compile manual code:

    
    
    ant compile.development -Dtab=xxx
    

(note the xxx is used to execute a minimal compile step)

**Restart Tomcat.**

When installing the web service as a module, use the application's window
_Application Dictionary || Application || Module Management_ to install it and
rebuild the application.

The _org.openbravo.howtos-provider-config.xml_ file should now be present in
the WEB-INF directory.

##  Calling the webservice

(Re-)Start Openbravo ERP and try out the webservice by entering this URL into
the browser:

    
    
    http://localhost:8080/openbravo/ws/org.openbravo.howtos.doIt?product=1000001&stateless=true
    

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

Note that the product ID may be different with your installation. Also see
that the java package of the module is prefixed to the webservice's name
defined inside the config file. Remember the formula: ** http://
<serveraddress>/openbravo/ws/<moduleJavaPackage>.<webservicename> **  
  
---|---  
  
You will probably be asked to login.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

**Note** : The user should have enough privileges to read sales orders and
products. If you are using the standard Openbravo SmallBazaar demo data and
the Openbravo user, then this article should work with the role _Openbravo
Admin_ .  
  
---|---  
  
![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

**Note** : the stateless parameter will prevent the server to create a http
session. This is quite important for high frequency webservice calls which
should not unnecessarily occupy resources on the server.  
  
---|---  
  
You should see the xml showing a sales order:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_new_REST_webservice-7.png){: .legacy-image-style}

##  Stateless Webservice Requests - HTTP Session

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q1  ** .  
---|---  
  
![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

**Note:** important for high frequency webservice calls.  
  
---|---  
  
By default OB webservice requests are statefull. Meaning that each webservice
call will create and use a http session in the OB server. Depending on how you
setup the client to call the webservice this can even mean that each
webservice request creates a new http session. This is not advisable for high-
frequency webservice requests. In case of high volume calls it can make sense
to move to a stateless implementation.

There are 2 ways in which you can achieve a stateless handling of a webservice
requests:

  * passing the parameter stateless=true in the request url. For example: 

    
    
    http://localhost:8080/openbravo/ws/org.openbravo.howtos.doIt?product=1000001&stateless=true
    

  * annotating the webservice class with the AuthenticationManager.Stateless annotation: 

    
    
    @AuthenticationManager.Stateless
    public class POSTestStatelessWebservice implements WebService {
    ...
    }

When doing stateless requests the implementation of the webservice should not
expect a http session to be present or create a new http session. For example
the VariablesBase object can not be used in stateless webservice requests.
Other than that most base framework functionality (like the data-access-layer
and the OBContext object) is available for the logic.

##  Adding logic to do updates

So far we only discussed retrieving information from the database and
returning it as xml. Updating information should officially (according to the
REST principle) be implemented in the PUT method, but you need to choose what
is practical. For updating, a common flow is the following:

  1. Receive the XML string from the request object. 
  2. Convert the XML string to a set of Business Objects. 
  3. Process these Business Objects, for example save them in the database. 

Below you will find some sample code which follows this flow:

    
    
     
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

##  Relevant Links

For a more detailed description take a look at  Openbravo REST and other links
.

##  Tips & tricks and trouble shooting

For trouble shooting and tips and tricks please see this link  here  . The
tips and tricks section for example discuss a firefox plugin to make it easy
to test REST webservices.

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_new_REST_webservice  "

This page has been accessed 40,334 times. This page was last modified on 16
February 2017, at 09:44. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

