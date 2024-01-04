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

  

#  XML REST Web Services

##  Contents

  * 1  Overview 
  * 2  Glossary 
  * 3  Why REST? 
  * 4  REST Webservice 
  * 5  Main REST Webservice 
  * 6  DAL REST Web service 
  * 7  Single Request and Response 
  * 8  Query Request and Response 
  * 9  Retrieval of a subset of the entity properties 
  * 10  Update/Create Request and Response 
  * 11  Remove Request and Response 
  * 12  Update multiple business objects Request and Response (Import) 
  * 13  Business Object to XML 
  * 14  DAL REST: Overview of return messages in XML 
  * 15  HTTP Return Codes 
  * 16  Login and Security 
  * 17  Stateless Webservice Requests - HTTP Session 
  * 18  Database Transaction 
  * 19  Non-updatable fields: Client, Organisation etc. 
  * 20  XSD Schema Generation for REST approach 
  * 21  Error Handling 
  * 22  Simple XSLT templates 
  * 23  Test 
  * 24  Tips & tricks and trouble shooting 

  
---  
  
##  Overview

Openbravo ERP REST consists of a framework offering security and exception
services and a data access REST web service implementation. The data access
(DAL) REST web services provide a CRUD-like web service so that external
applications can retrieve, update, create and delete business objects through
standard HTTP requests.

##  Glossary

This document uses the term business object to denote an entity and its
dependent information. A business object can be a simple entity such as a
currency which just has basic primitive fields. On the other hand it can also
be a structure of entities, for example an order header with its order line. A
business object structure always has one business object which is the owner of
all the business objects in that structure, for example for a sales order the
sales order header business object is the owner of the complete structure.
Another way of describing this is that the order lines depend on the order
header, i.e. an order line can not exist without its order header and when an
order header is removed also the order line should be removed.

Some background information related to REST:

The REST concept was first described by Roy Fielding:

  * Fieldings's Dissertation 

An overview article on REST with a lot of links to other material:

  * Wikipedia on REST 

A quick intro into an example REST approach:

  * How to Create a REST Protocol 
  * Building Web Services the REST Way 

Some links related to REST versus SOAP, there is a fair amount of articles on
the web on this topic:

  * REST versus SOAP - the REST story 
  * A RESTful approach to Web services 

##  Why REST?

There are a number of reasons why a REST approach makes sense for a data
centric service: a REST approach

  * favors identifying and addressing resources which fits to the data-centric nature of the provided apis (a resource corresponds to a business object) 
  * has actions (POST, PUT, DELETE, GET) which correspond to standard CRUD actions 
  * allows linking to specific business objects or to sets of business objects. This is a very powerfull feature of a REST approach and it allows for easy navigation between business objects. 
  * is simple to develop and use, and very lightweight from an architectural point of view 

##  REST Webservice

It is important to note that REST is not a standard but more an approach or
architectural style. Openbravo ERP REST adheres to the REST approach:

  * resources (business objects) are identified by specific links which are stable over time 
  * the GET action is side-effect free 
  * all http actions: POST, PUT, DELETE, GET are supported 
  * http response codes are used to specify results of actions 

##  Main REST Webservice

A request is processed by the REST web service servlet
(org.openbravo.service.web.BaseWebServiceServlet). This servlet uses the
request URL to determine the type of request and how to handle it.

The REST web service servlet also handle login and authentication (see below).

A request (GET, POST, PUT) can consist of three parts:

  * the url path 
  * the url parameters 
  * the content of the request 

A GET request will not have content and is completely controlled by the url
path and its parameters.

A POST and PUT request will have content which is assumed to be a valid xml
document.

The response of a REST call will be an XML document, containing the requested
data, a result XML message or an error XML message.

##  DAL REST Web service

The DAL REST web service is an implementation of a REST web service in
Openbravo ERP 2.50. It provides a CRUD-like web service so that external
applications can retrieve, update, create and delete business objects through
standard HTTP requests.

It provides the following functionality:

  * retrieve a single business object using a url which contains both the type as well as the id of the request business object 
  * retrieve a list of business objects using just the type, for example  http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country  (User Name: Openbravo / Password: openbravo) 
  * querying, filtering, paging and sorting of lists of business objects 
  * updating of an existing business object or multiple business objects through xml and a http POST or PUT operation 
  * creation of new business objects through a POST/PUT operation which submits a xml structure 
  * export and import of data: xml files which contain a mix of different types of business objects and a mix of new and existing business objects 
  * retrieval of a list of id and identifier values, for example to fill a listbox in an external user interface 
  * delete operation using either a url pointing to a specific business object which needs to be removed or a XML document (in the content) which contains business objects (as full xml or as partial xml) which need to be removed. 

The rest of this document will mainly focus on the functionality of the DAL
REST web services.

##  Single Request and Response

A single request is a request which points to one unique business object. For
example the url:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country/106 (User Name: Openbravo / Password: openbravo)
    

will return the xml for an instance of the Country business object with ID =
106 (Spain). The REST Webservice will retrieve this business object from the
database, create XML for it and return the resulting XML. See below for a
description of the XML.

##  Query Request and Response

A query url is used to retrieve a list of business objects. It can handle
filter, sort and paging parameters. An example of a query url: for example:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?where=currency.id='100'&orderBy=name&firstResult=5&maxResult=10 
    

(User Name: Openbravo / Password: openbravo)

This url will return all Country objects which have ID = 100 (USD) as
currency, sorted by the country name, the page starting at object 5 and 10
objects should be returned.

To query on date fields for a specific date it is easiest to use a
larger/smaller than, this because date fields are stored in the database with
a time value (which can include milliseconds):

http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?where=currency.updated%3E'2012-11-20'%20and%20currency.updated%3C'2012-11-21'&orderBy=name&firstResult=5&maxResult=10

(note the %3E is an encoded > and the %3C is an encoded >)

The REST query functionality supports the following parameters in the url:

  * where: a HQL whereclause 
  * orderBy: an orderBy definition 
  * firstResult and maxResult parameters for paging support 

The user has two types of possible operations which can be performed by the
query:

  * default when after the entity name there is no additional segment in the URL: this operation will query for the business objects and return (in XML) the properties of each of the business objects (this depends on security settings also). 
  * count: this will return the number of business objects which are selectable according to the filter. This action is used for support of paged views. 

The default query operation will return the business objects (with their child
objects) as XML. See the  business-object-to-xml  section. If you only want to
have the objects returned without children then you can pass the
includeChildren parameter (as a URL parameter) with the value false.

**Note:** when doing querying with the whereclause any special characters
should be url encoded, for example the % character when doing like has to be
encoded with %25, like this:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?where=name like '%25Fr%25' (User Name: Openbravo / Password: openbravo)
    

**Note:** Notice that in this first example:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?where=currency.id='100'&orderBy=name&firstResult=5&maxResult=10
    

is it also possible to query the server using the currency identifier
returned. Nevertheless, for this case we must use the original name of the
identifier, in the currency table it is ISO_CODE so the query would change to:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?where=currency.iSOCode='USD'&orderBy=name&firstResult=5&maxResult=10
    

**Note** Notice that the where clause can also be used with more than one
condition using the AND clause, e.g.

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?where=currency.id='100'%20and%20hasRegions=true
    

##  Retrieval of a subset of the entity properties

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
functionality is available in 3.0MP27 and later MPs.  
---|---  
  
Using the parameter _selectedProperties it is possible to specify the list of
properties that the webservice should return. This parameter can be used both
in single and query requests.

For instance, to retrieve only the id and name of all countries:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?_selectedProperties=id,name
    

The list of properties can include not only properties of the top level
entity, but also of its child entities. For instance this URL retrieves the id
and name of each country, and the id and identifier of each of its regions:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?_selectedProperties=id,name,regionList
    

Properties of the child entities can also be specified. For instance, to
additionally obtain the name and description of each of the country regions:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country?_selectedProperties=id,name,regionList,regionList.name,regionList.description
    

The use of the _selectedProperties parameter has a benefitial effect on the
performance: the fewer child entities are specified, the better the
performance of the webservice call will be.

##  Update/Create Request and Response

A business object can be updated/created through REST using the http POST or
PUT command. The posted XML should adhere to the  XML Schema generated  by the
REST Webservice. With one exception, for update situations it is allowed to
only include the changed properties in the XML.

The system will automatically check (by querying) if a business object is new
or not. If no id is supplied then it will always be considered as new, if a id
is supplied then a database query is done. If the id exists (for that type) in
the database then the system will assume an update. If the id does not exist
it is an insert, in which case the id (in the xml) is maintained.

If the update was successful a success response is returned (<success/>), if
it fails an error XML response is send back.

##  Remove Request and Response

The DAL REST webservice also supports a delete or remove request. Delete
requests use the http DELETE command. The Delete action can accept two types
or urls:

  * a single URI pointing to the business object which needs to be removed, for example: 

http://localhost:8080/openbravo/ws/dal/Product/1000004

  * a URI with a where parameter: 

http://localhost:8080/openbravo/ws/dal/Product?where=name='C02'

In the second case it is possible to remove multiple objects in one http
DELETE request.

##  Update multiple business objects Request and Response (Import)

The system also supports updating of multiple business objects which are
passed in one file. The following aspects need to be taken into account:

  * the xml file can contain mixes of new and existing (to-be-updated) business objects 
  * there maybe references to new business objects in the same xml file, these references use a unique id which does not need to in the database. This means that the import logic will internally (within the xml file) resolve object references before persisting the total xml file. 
  * the xml file can contain mixes of different types of business objects 

A XML file containing different types can be posted to the generic DAL web
service url:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal (User Name: Openbravo / Password: openbravo)
    

##  Business Object to XML

The XML response to a retrieval request consists of the data of the business
object or business objects. The business object is translated to xml in the
following way:

  * The entity name is used for the tag name of the business object element. The entity tag/element also has attributes for the id and the identifier. 
  * The property name is used for the element name of each property. It depends on the security settings of the user which properties or information is returned (see security section). 

Property values are xml-ised as follows:

  * Date value is exported according to the XML Schema datetime format 
  * String value is exported as is (encoding is required) 
  * Numeric value is exported using decimal point and no grouping 
  * Reference (to another business object) is converted to an xml tag which contains the id, the entity name and the identifier value. This makes it possible for consumers of the XML to easily create hyperlinks to retrieve the data of the reference business object. The identifier can be used to generate a display of the reference. 
  * Child objects (the list/one-to-many associations) are also exported and are embedded in the parent object (this is done recursively through the parent-child structure). You can disable/prevent the return of child objects by setting the (URL) parameter includeChildren to false. 

The element used for the XML version of a reference is also used in case when
lists of references need to be exported.

##  DAL REST: Overview of return messages in XML

The design discusses different functionalities. To summarize this section
lists the set of return types which can be expected for different types of
REST requests:

  * a request for a specific business object will return a XML document with this business object 
  * a request (a query) for a list of business objects will return a XML document with the data of those business objects 
  * a request (a query) for a list of identifiers will return a XML document with the only the id, entity name and the identifier of each business object 
  * a query with a count parameter will only return a simple xml message with a count number (<count>5</count>) 
  * an update/insert request will return a success XML message (<success/>) if it succeeded, the return message will contain the id of the inserted record. 
  * a query with a identifier parameter will return a list of identifier values (one for each business object) 

If the requests fails then an error XML message is returned.

##  HTTP Return Codes

The REST Webservice uses the following error codes:

  * 200 (OK): for successfull requests 
  * 400 (Bad Request): in case the uri could not be parsed or in case of invalid xml 
  * 401 (Unauthorized): is returned when a security exception occurs 
  * 404 (Not found): if the entityname does not exist or the if an individual business object is addressed, if the business object does not exist. Note that a 410 (Gone) response could also be applicable here but it is less know therefore the 404 is used. 
  * 409 (Conflict): is returned for a POST or PUT action, specifies that the data which was posted is out-of-date or invalid. 
  * 500 (Internal Server Error): if an unrecoverable application error occured. 

##  Login and Security

The REST Webservice provides two methods for logging in:

  * login with login/password passed as request parameters (the parameters names are resp. l and p) 
  * basic http authentication. Basic http authentication can be prevented with the request parameter auth=false. In this case only the status code 401 (Unauthorized) is returned. The request parameter auth=false is available from Openbravo 3.0 MP9. 

The following aspects are of importance for security:

  * The login and context are stored in a session for performance reasons 
  * If the caller/client is session-less (does not support cookies) then it is also possible to include login information in every request. **It then also makes sense to make the webservice request stateless.** See the next section for more information on that. 

Also, the default role for the user who is doing the log in should be enabled
to do calls to web services. Search for "Is Web Service Enabled" inside the
Role  document for more information.

After a successfull login the REST web service action is run within the
context of the user. The REST webservice uses the  DAL security control
mechanism to control read and write access.

##  Stateless Webservice Requests - HTTP Session

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR17Q1  ** .  
---|---  
  
![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |

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

##  Database Transaction

A REST web service request is basically the same as a normal HTTP request.
This means that transaction handling is the same as for standard HTTP
requests. If no exception occured then the transaction is committed at the end
of the web service request (on the Openbravo server).

##  Non-updatable fields: Client, Organisation etc.

There are a number of properties for each business object which are not always
changeable through the REST webservice:

  * Client and Organisation: a webservice update of a business object may not change the Client and Organisation information. In creation mode the client may not be set, the organisation may be specified, if not specified then it is set from the user information. 
  * Update and Created audit fields: the update and created audit fields are not updatable/changeable through the webservice api. 

##  XSD Schema Generation for REST approach

The DAL webservice generates a XSD schema on the basis of the runtime model.
This XSD schema defines the xml which is generated by the REST web service.
This definition is also used for the XML used to update Openbravo through REST
web services.

For an Openbravo ERP instance running on
http://livebuilds.openbravo.com/erp_pi_pgsql  the XSD can be retrieved through
this request:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/schema (User Name: Openbravo / Password: openbravo)
    

##  Error Handling

When a request can not be processed and an error occurs then an error XML
document and the relevant HTTP response code is returned. The error XML
document contains the exception message.

The stacktrace and other more detailed information is not sent out on purpose
(because of security reasons).

##  Simple XSLT templates

Openbravo ERP 2.50 has some simple XSLT templates to show how the XML can be
processed and demonstrate that REST is a good approach for allowing navigation
through data sets. The following URL shows the start URL for a DAL web service
call using the XSLT templates:

    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/?template=types.xslt (User Name: Openbravo / Password: openbravo)
    
    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Country/106?template=bo.xslt (User Name: Openbravo / Password: openbravo)
    
    
    
    http://livebuilds.openbravo.com/erp_pi_pgsql/ws/dal/Currency/100?template=bo.xslt (User Name: Openbravo / Password: openbravo)
    

The XSLT templates can be found in the org.openbravo.service.rest package.

##  Test

The REST Webservice functionality is tested using junit testcases. REST test
cases can be found in the openbravo development project in the src-test folder
and then in the org.openbravo.test.webservice package. The REST test cases
give a first impression on how to do REST requests directly from Java incl.
basic authentication.

##  Tips & tricks and trouble shooting

For trouble shooting and tips and tricks please see this link  here  . The
tips and tricks section for example discuss a firefox plugin to make it easy
to test REST webservices.

Retrieved from "  http://wiki.openbravo.com/wiki/XML_REST_Web_Services  "

This page has been accessed 35,223 times. This page was last modified on 21
February 2017, at 12:38. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

