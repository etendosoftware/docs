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

  

#  Datasources

##  Contents

  * 1  Introduction 
  * 2  Related Information 
  * 3  Datasource API 
  * 4  Datasource definition 
  * 5  Implementing your own client-side datasource (advanced) 
  * 6  Datasource examples 

  
---  
  
##  Introduction

This manual describes how to define and implement data sources on the basis of
the Openbravo Datasource functionality. A datasource is the main provider of
data in the Openbravo Rich Internet User Interface. The datasource api
contains methods to fetch data, update data and to create and delete data on
the server. A datasource has a client-side as well as a server side
representation.

This manual describes how to implement a custom datasource. A custom
datasource can be used in Openbravo user interface components such as the
Selectors  .

##  Related Information

The Openbravo Datasource functions makes use of and extends the
JSON_REST_Web_Services  functionality.

The Openbravo Datasource implements and extends the  Smartclient
RESTDatasource  in two ways:

  * on the client it generates a Smartclient RESTDatasource instance (in javascript) 
  * on the server it provides a JSON REST web service which supports the same api as defined by Smartclient 

The Datasource implementation consists of two parts:

  * the server side implementation of the datasource in java 
  * the definition of the datasource in the Application Dictionary 

##  Datasource API

The Datasource api is defined by the  DataSourceService  interface. This
interface defines methods which are required for correct server side
operation. It is best to extend the  BaseDataSourceService  class which takes
care of implementing most methods.

After extending the BaseDataSourceService class the following methods need to
be implemented:

    
    
      /**
       * Execute a query request and return the result as a json string. For a query request the content
       * ({@link #getContent()}) is normally empty, the query parameters can be found in the parameters
       * map ({@link #getParameters()}).
       * 
       * @param parameters
       *          the parameters often coming from the HTTP request
       * @return the json result string
       */
      public String fetch(Map<String, String> parameters);
     
      /**
       * Execute a delete action. The id of the deleted record is present in the parameters.
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

The content and return Strings are JSON Strings which need to adhere to the
same format as defined in the  Smartclient RESTDatasource  .

When using the datasource in a classic Openbravo window/form (such as in the
case of the  Selector  ) then the parameters will contain all form fields
present in the HTML form.

For its runtime behavior the datasource makes extensive use of the
JSON_REST_Web_Services  . So the datasource at runtime operates very much like
the JSON webservice. There are however some minor differences:

  * When only a single object is  requested  then JSON REST will return only a JSON string with this object. The datasource will wrap this single JSON string and add metadata required for the client-side datasource. 
  * The datasource definition in the Application Dictionary allows specifying a where clause. The datasource will add this where clause to the query before calling JSON Rest to execute the query and return the JSON string. 

When developing your own datasource it makes sense to study and use the  core
classes  of the JSON REST functionality.

##  Datasource definition

After the server side implementation of the datasource the next step is to
define it in the application dictionary. This makes it possible to use the
datasource in (user interface) components defined in the application
dictionary.

The datasource definition consists of two parts:

  * the datasource 'header' defining the class implementing the datasource. 
  * datasource fields defining the fields of the datasource. 

To define the datasource in the application dictionary go to: _Application
Dictionary > Datasource _ . Then click the insert button.

  

![](/assets/developer-guide/etendo-classic/concepts/Datasources-0.png){: .legacy-image-style}

  
A description of the fields in the datasource definition:

  * Module: choose the module which delivers this datasource 
  * Name/Description: a relevant and describing name and description 
  * Table and Whereclause: these can be used to define a datasource, reading directly from a table. 
  * Java class name: the class name of the class implementing the datasource. This field can be empty. In which case the table field must be set. If no java class name is specified then the  DefaultDataSourceService  class is used. This class fully implements the Datasource interface (full CRUD support through webservices and client-side representation of the datasource). 
  * Template: the template is responsible for generating the client-side datasource in javascript. See the next section on how to implement a custom client-side datasource for more information on the meaning of this field. Most of the time there will be only template to select (the default). 

If a table is specified and the DefaultDataSourceService is used (java class
name is for example empty) then it is not needed to specify datasource fields.
All the columns from the table are automatically available as datasource
fields.

If however, you have a custom datasource class or want to add additional
(computed) fields to a datasource then they need to be defined as Datasource
Fields.

To add fields to a datasource click on the Datasource Field link in the top of
the datasource window.

  

![](/assets/developer-guide/etendo-classic/concepts/Datasources-1.png){: .legacy-image-style}

  
A description of the fields in the datasource field definition:

  * Name: a unique name which should be a valid javascript name also. 
  * Description: a free-format descriptive field. 
  * Reference: the reference defines the type of the field. 
  * Table: if the reference is a foreign key reference then this field can be used to specify the table which is being referenced. 

##  Implementing your own client-side datasource (advanced)

The datasource definition is converted to javascript code using a template.
The template is selected in the datasource definition (see step above). It is
possible for a module to add a new template which can be used for creating
client-side datasources.

Creating a new template needs to be done by a developer with a good
understanding of Openbravo. To implement a new template it is necessary to
understand the template processing and template handling functionality used by
Openbravo. The  Openbravo_3_Architecture  page provides detailed information.
It discusses both template processing, caching, i18n and also gives pointers
on how to implement a custom template.

The template used for the datasource can be found in the source tree of the
org.openbravo.service.datasource package inside the
org.openbravo.service.datasource.templates package in the datasource.ftl file.
The template makes use of the freemarker templating language.

A custom template should be created inside a separate module. To make use of
it define it inside the Application Dictionary > Templates.

  

![](/assets/developer-guide/etendo-classic/concepts/Datasources-2.png){: .legacy-image-style}

  
The main fields to set:

  * The TemplateClasspathLocation should point to the location in the source tree of the custom template, incl. its filename. 
  * The ComponentType **must** be set to datasource. The ComponentType determines if the template can be selected in the datasource definition window. 

  

![](/assets/developer-guide/etendo-classic/concepts/Datasources-3.png){: .legacy-image-style}

  
Then when defining datasources the custom template can be selected.

##  Datasource examples

The datasource source code contains 2 examples of a datasource implementation:

  * DefaultDataSourceService  : this is a complete implementation of the  DataSourceService  interface. It supports fetching with querying and paging and update, add and delete operations. This datasource is used extensively in the Openbravo rich user interface. 
  * ModelDataSourceService  : is an in-memory datasource which provides access to the properties of a model using a dot-path syntax. It only implements the fetch method. It is used in the  Selector  to provide access to the model. 

  

![](/assets/developer-guide/etendo-classic/concepts/Datasources-4.png){: .legacy-image-style}

  
The datasource definitions can be found in the application in _Application
Dictionary > Datasource _

  

![](/assets/developer-guide/etendo-classic/concepts/Datasources-5.png){: .legacy-image-style}

  
**Note** that the DefaultDataSourceService does not have an explicit
definition as it is instantiated on request on the server. This facilitates
using the datasource directly for any table within Openbravo without requiring
an explicit definition for each table.

Retrieved from "  http://wiki.openbravo.com/wiki/Datasources  "

This page has been accessed 14,004 times. This page was last modified on 11
August 2011, at 21:10. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

