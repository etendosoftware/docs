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

  

#  Model Object Mapping

##  Contents

  * 1  Introduction 
  * 2  Model - Implementation concept 
    * 2.1  Servlets 
      * 2.1.1  Application Dictionary Objects 
      * 2.1.2  Other Servlets 
    * 2.2  Filters 
    * 2.3  Listeners 
    * 2.4  Resources 
    * 2.5  Error Pages 
      * 2.5.1  Default error page 
      * 2.5.2  Exception type 
      * 2.5.3  Error code 
  * 3  Modularity and the Model Object Definition 

  
---  
  
##  Introduction

Web Applications (as Openbravo ERP) have a _Deployment Descriptor_ . It is
actually a xml file ( _web.xml_ ) which defines everything about the
application the server needs to know (servlets, mappings and other
components).

Openbravo ERP generates this file in compilation time with the information
stored in _ AD_Model_Object  _ and _ AD_Model_Object_Mapping  _ tables. This
document explains these two tables.

##  Model - Implementation concept

_AD_Model_Object_ is a table in Openbravo Application Dictionary to link
Application Dictionary components and the class (servlet) that implement that
object. So this table is a mapping between the logical side (AD components)
and the physical side (classes). It is useful for two main reasons:

  1. It allows to implement in a generic way rules that apply to all AD components like security, navigation and others. 
  2. It is the mechanism to automatically populate the web.xml file where classes (servlets) are declared. The AD_Model_Object_Mapping is an utility to create the mapping entries in the web.xml file. 

There is a few number of exceptions to this description: some servlets that
are deployed in Openbravo context but are not linked to any AD component, such
us the DataGrid or the AuditInfo servlets. They are invoked from manual or
standard components (windows, forms, etc.) through http requests by hardcoding
its url-mapping in the request. It can be interpreted still as a mapping of
actual classes that implement a functionality that is not described in current
Openbravo model, although it may be in the future.

The following sections explain how different elements are defined.

###  Servlets

####  Application Dictionary Objects

In previous versions of Openbravo, when a tab was created, new Model Objets
were created for it. This no longer happens, as the web.xml entries for tabs
are automatically added to the web.xml file directly when the compilation is
done, without reading any info from the Model Object tables.

####  Other Servlets

As explained in  Model - Implementation concept section  there are some
situations where it is necessary to define a Servlet which does not implements
an Application Dictionary Object. These cases are defined in **Application
Dictionary || AD Implementation Mapping** window. Selecting in **Object** tab
the _Servlet_ Object Type  , setting the  Java class  with the Servlet
implementation and adding in the **Mapping** tab the mapping to access the
Servlet.

###  Filters

Filters can also be defined in **Application Dictionary || AD Implementation
Mapping** window. Select _Filter_ object type, and set the Java class that
implements the filter. In **Mapping** tab add the url patterns for the object
to be filtered, and in case the filter receives any parameter set them in the
**Parameters** tab with the values they will have. To retrieve the parameters
values in the implementation use implement _init_ method like follows:

    
    
     
      public void init(FilterConfig config) throws ServletException {
        encoding = config.getInitParameter("requestEncoding");
        if (encoding == null)
          encoding = "UTF-8";
      }

###  Listeners

Listeners are defined in **Application Dictionary || AD Implementation
Mapping** window with type _Listener_ . In this case it is not necessary to
define _Mapping_ nor _Parameters_ , just the java class implementing it. Take
into account that listeners must be executed in certain order, this order is
defined by the _Sequence number_ field.

###  Resources

Resources are defined in **Application Dictionary || AD Implementation
Mapping** window with type _Resource_ .

Let's see the following example in web.xml:

    
    
     
      <resource-ref>
        <description>Oracle Datasource example</description>
        <res-ref-name>jdbc/openbravo</res-ref-name>
        <res-type>javax.sql.DataSource</res-type>
        <res-auth>Container</res-auth>
      </resource-ref>

This resource is defined by assigning the following values to the following
fields:

  * _Object.Name_ : jdbc/openbravo 
  * _Object.Java Class Name_ : javax.sql.DataSource 
  * _Parameters.Name_ : auth 
  * _Parameters.Search Key_ : Container 

###  Error Pages

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR18Q2  ** .  
---|---  
  
Error pages can be defined in **Application Dictionary || AD Implementation
Mapping** window using the type _Error page_ .

If multiple pages of the same kind (e.g. multiple 404 pages) are found, the
last one in web.xml is the one that will be used to handle the error. This
order is determined by the Error code object's sequence number.

Core module implements a default error page with sequence number 10. To
override this page, the created page must have a sequence number higher than
10 or be either an error code or an exception type page.

Examples of usages for this feature can be found in the  Platform Features
module  .

_Error page_ objects accepts the following parameters:

  * _location_ : The location of the error html page relative to the default design path. 
  * _error-code_ : The HTTP error code associated to the error page. e.g. 404. 
  * _exception-type_ : The Java exception type the error page will handle. e.g. java.lang.RuntimeException 

Depending on the parameters defined, the following kind of error pages will be
generated:

####  Default error page

Parameters:

  * _location_ : org/openbravo/erpCommon/security/Error.html 

    
    
      <error-page>
        <location>/src-loc/design/org/openbravo/erpCommon/security/Error.html</location>
      </error-page>

  

####  Exception type

Parameters:

  * _location_ : org/openbravo/erpCommon/security/Exception.html 
  * _exception-type_ : javax.servlet.ServletException 

    
    
      <error-page>
        <exception-type>javax.servlet.ServletException</exception-type>
        <location>/src-loc/design/org/openbravo/erpCommon/security/Exception.html</location>
      </error-page>

  

####  Error code

Parameters:

  * _location_ : org/openbravo/erpCommon/security/Error404.html 
  * _error-code_ : 404 

    
    
      <error-page>
        <error-code>404</error-code>
        <location>/src-loc/design/org/openbravo/erpCommon/security/Error404.html</location>
      </error-page>

##  Modularity and the Model Object Definition

Openbravo Modularity aims to allow through modules the deployment of any type
of optional content in an Openbravo instance, including additional entries in
the web.xml file of openbravo context. This is done through the
AD_Model_Object table. Developers can create entries in this window not linked
to any AD component. To support any type of web.xml content (servlet,
listeners, filters, etc.) a new column is added to the AD_Model_Object to
represent the type of web.xml entry that the developer is adding. They can
also declare a set of mappings for the entry and a set of parameters if
needed.

The module of a AD_Model_Object entry is calculated with the following rule:
if it is linked to any AD component then the module is the one assigned to
that AD component, otherwise the module is the one assigned to the
AD_Model_Object record itself. Note that the module for the AD_Model_Object
child tables (AD_Model_Object_Mapping and AD_Model_Object_Para) is the same as
their parent record.

With this extension the web.xml file in the openbravo context is fully
extensible through modules.

In previous releases AD_Model_Object table defined just Servlets, other
objects in web.xml file were added directly to its template. In r2.50 model
was extended to allow definition of other objects (filters, listeners,
resources and Servlets not linked to AD elements) adding the
AD_Model_Object_Para  table and the **Application Dictionary || AD
Implementation Mapping** window to manage it.

Retrieved from "  http://wiki.openbravo.com/wiki/Model_Object_Mapping  "

This page has been accessed 6,354 times. This page was last modified on 21
February 2018, at 11:56. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

