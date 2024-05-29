---
tags: 
  - JSON
  - Rest
  - Web Services
  - Smartclient
---
# JSON Rest Web Services

##  Overview

This section describes the [Etendo JSON REST](https://github.com/etendosoftware/etendo_core/blob/main/web/js/dojotoolkit/dojox/rpc/JsonRest.js) functionality as it is provided by the  Etendo JSON REST module. The JSON REST functionality consists of 2 main parts: 

1. the JSON REST webservice, and 
2. the underlying classes used to provide this service (mainly business object to JSON converters and back). 

As a developer you can integrate directly with the JSON REST webservice or develop your own webservice making use of the core JSON REST classes.

As a side note the JSON format expected and returned by this webservice follows the format as used by  [Smartclient](https://smartclient.com/){target="\_blank"}. For more information on what the Smartclient json syntax see these links:

  - [Smartclient Client Server Integration](https://smartclient.com/smartclient-release/isomorphic/system/reference/?id=class..clientDataIntegration){target="\_blank"}
  - [Smartclient REST Datasource](https://smartclient.com/smartclient-release/isomorphic/system/reference/?id=class..RestDataSource){target="\_blank"}

This functionality is not provided by Etendo core but by the Etendo JSON REST module which you have to install separately. The module is available through the central repository or can be downloaded from the forge here.

!!!note
    If more information about JSON and REST is necessary, visit [JSON](https://en.wikipedia.org/wiki/JSON){target="\_blank"} and [REST](https://en.wikipedia.org/wiki/REST){target="\_blank"}.

##  Conversion from and to JSON

This section discusses how business objects are converted from and to JSON. The logic is used by the webservice to implement retrieval, update and insert logic.

Etendo webservices will return the JSON compressed, for reading purposes it is expanded and formatted on this wiki.

Compressed JSON(as it is returned by webservices):

    
    
    "language":{"_identifier":"English (USA)","entityName":"ADLanguage","$ref":"ADLanguage\/192","id":"192","active":true}

Formatted JSON(better readability):

    
    
    "language":{
       "_identifier":"English (USA)",
       "entityName":"ADLanguage",
       "$ref":"ADLanguage/192",
       "id":"192",
       "active":true
    }

##  Convert from a Business Object to JSON

To convert a business object to JSON, the logic iterates over all properties (except list/one-to-many properties) of the object and applies the following logic:

* the property name is used as the name of the JSON field/key name 
* a null value is set to `JSONObject.NULL`
* a date or date time property is converted to a string using the xml schema format (e.g. yyyy-MM-dd'T'HH:mm:ss.S) 
* other primitive typed properties (string, numeric) are converted using JSON itself. 
* a reference to another object is 'jsonified' by creating a JSON object with a limited set of properties: the id, _identifier, entityName $ref, active (see the description of special properties above). For example the following JSON-snippet shows a reference for a property called **language**: 

```
    
    "language":{
       "_identifier":"English (USA)",
       "entityName":"ADLanguage",
       "$ref":"ADLanguage/192",
       "id":"192",
       "active":true
    }
```

!!!Note
    List/one-to-many properties are not converted. So for example, when an invoice is converted to JSON then its invoice lines are not present in the JSON string. The invoice lines can be retrieved with a separate JSON request.

Here you can find an example of the Country object (with ID 100) converted to JSON:

    
    
    {
        "_identifier": "United States",
        "_entityName": "Country",
        "$ref": "Country/100",
        "id": "100",
        "client": "0",
        "client$_identifier": "System",
        "organization": "0",
        "organization$_identifier": "*",
        "active": true,
        "creationDate": "2011-02-22T17:06:39+00:00",
        "createdBy": "0",
        "createdBy$_identifier": "System",
        "updated": "2011-02-22T17:06:39+00:00",
        "updatedBy": "0",
        "updatedBy$_identifier": "System",
        "name": "United States",
        "description": "United States of America",
        "iSOCountryCode": "US",
        "hasRegions": true,
        "regionName": "State",
        "phoneNoFormat": "Y",
        "addressPrintFormat": "@C@, @R@ @P@",
        "postalCodeFormat": null,
        "additionalPostalCode": false,
        "additionalPostalFormat": null,
        "default": true,
        "language": "en_US",
        "language$_identifier": "English (USA)",
        "currency": "100",
        "currency$_identifier": "USD",
        "iBANLength": null,
        "iBANCode": null,
        "decimalseparator": null,
        "groupingseparator": null,
        "numericmask": null,
        "dateformat": null,
        "datetimeformat": null,
        "recordTime": 1570171151702,
        "_readOnly": true
    }

##  Convert from JSON to a Business Object (using the database)

The JSON to business object logic is slightly more complex as it tries to take into account that an object may exist in the database and it will try to update that object. In addition references between JSONObjects is supported.

The conversion logic goes through the following steps:

  1. the logic checks if the JSON object contains an ID and _entityName value. If so, it tries to read the object from the database. If not set or not found in the database, a new object is created. The object is stored in memory using the ID found in the JSON object, this allows other JSON objects in the same conversion batch to use/refer to that id. 
  2. then for each property of the object (except list/one-to-many) it is checked if the JSON object contains a value for that property. 

if there is a value then, depending if it is a primitive or a reference property, it is handled differently.

  1. A primitive value is converted by JSON itself except for date values. These are converted using date formatters using the XML Schema format pattern. 
  2. A reference value is treated differently. It is assumed that the value of a reference property in JSON is also a JSON Object. If it has an ID value, then this is used to search in the in-memory map (and found there if the object was already converted earlier). If not found in the in-memory map, then the refered JSON object is converted using this same logic as discussed in the steps here (so first search in the database then create a new one) and the returned BaseOBObject is considered the value set in the property. If found in the database or already converted earlier then that BaseOBObject is used. 

##  Special Properties

The conversion logic in general converts all properties. In addition, the logic above provides and can handle additional special properties:

  * _identifier: contains the (concatenated) content of the identifier properties/columns of an object, can also be used as the sortBy in a query.
  * _entityName: the type name of the object, corresponds to a specific [Entity] in the system 
  * $ref: is the entityName and the ID separated by a forward-slash. It is a 'globally' unique identity of the object, it can be used to create the url to retrieve the details of the object. 

##  GET

A get request can be used to retrieve information in different ways:

  * [https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country](https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country)  : this will return all countries 
  * [https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country/100](https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country/100)  : this will return one country (the one with ID 100) 
  * [https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country/100?_selectedProperties=id,name](https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country/100?_selectedProperties=id,name)  : only the ID and the name properties will be returned for the country with ID 100 
  * [https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country?_startRow=10&_endRow=50&_sortBy=name](https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country?_startRow=10&_endRow=50&_sortBy=name)  : this will return 40 countries (rows 10 to 50) sorted by name 
  * [https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country?_where=currency.iSOCode='USD](https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country?_where=currency.iSOCode='USD')'  : returns all countries which have a currency with the isocode USD. The _where parameter can contain a valid HQL where-clause. 
  * [https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/FinancialMgmtPeriod?_where=_computedColumns.status='P'](https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/FinancialMgmtPeriod?_where=_computedColumns.status='P')  : returns all the periods in _Permanently closed_ status (P). Note that when referencing to a property based on a computed column ( _status_ ), it must be referenced starting from the __computedColumns_ property. 
  * [https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country?_noActiveFilter=true](https://livebuilds.openbravo.com/erp_pi_pgsql/org.openbravo.service.json.jsonrest/Country?_noActiveFilter=true)  : The inactive records will be shown. The parameter "_noActiveFilter" can be set to false for avoiding to show the inactive records. 

Different types of requests will return a slightly different result. The request for a single object (the first one above) returns a single JSON object:

    
    
    {
        "_identifier": "United States",
        "_entityName": "Country",
        "$ref": "Country/100",
        "id": "100",
        "client": "0",
        "client$_identifier": "System",
        "organization": "0",
        "organization$_identifier": "*",
        "active": true,
    ... truncated for clarity ...
        "language": "en_US",
        "language$_identifier": "English (USA)",
        "currency": "100",
        "currency$_identifier": "USD",
        "iBANLength": null,
        "iBANCode": null,
        "decimalseparator": null,
        "groupingseparator": null,
        "numericmask": null,
        "dateformat": null,
        "datetimeformat": null,
        "recordTime": 1570171151702,
        "_readOnly": true
    }

The other requests which request multiple results will return something like this:

    
    
    {
        "response": {
            "data": [
                {
                    "_identifier": "Ukraine",
                    "_entityName": "Country",
                    "$ref": "Country/331",
    ... truncated for clarity ...
                }
                {
                    "_identifier": "Germany",
                    "_entityName": "Country",
                    "$ref": "Country/101",
    ... truncated for clarity
                    "datetimeformat": null,
                    "recordTime": 1570171295463
                },
                {
                    "_identifier": "United States",
                    "_entityName": "Country",
                    "$ref": "Country/100",
                    "id": "100",
                    "client": "0",
                    "client$_identifier": "System",
                    "organization": "0",
    ... truncated for clarity ...
                    "recordTime": 1570171295463
                }
            ],
            "status": 0,
            "totalRows": 241,
            "startRow": 0,
            "endRow": 240
        }
    }

The difference is that the result contains paging information (startRows and endRow). The request which contains paging parameters will also return the total number of rows for the passed filter parameters:

    
    
    "response": {
         "data": [... results truncated for clarity ...]
         "status": 0,
         "totalRows": 241,
         "startRow": 0,
         "endRow": 240
    }

###  Paging Properties

Get requests that fetch multiple results from webservice can have paging properties provided:

  * **totalRows**: Shows the total number of results in the response. If there are more results than the ones fetched, its value will be endRows + 2. 
  * **startRow**: The starting row from where results will be fetch. If startRow is bigger than the number of results in database, then no result will be provided. 
  * **endRow**: The ending row marks the final row to be retrieved and is exclusive. If it is not set, then all rows will be fetched. It can't be less than the startRow property. 

For instance, requesting some object with properties startRow = 0 and endRow = 1 will retrieve only one row. If there are more rows that have not been fetched, totalRows will be 3 (endRow + 2).

##  POST and PUT

The POST and PUT operations perform add and update actions. In case of Etendo, the PUT operation will perform an add also, if an object does not have an ID set.

To do an update operation the following `JSON` has to be PUT to the system:

    
    
    {
        "data": {
            "_identifier": "United States",
            "_entityName": "Country",
            "$ref": "Country/100",
            "id": "100",
            "client": {
                "_identifier": "System",
                "_entityName": "ADClient",
                "$ref": "ADClient/0",
                "id": "0",
                "active": true
            },
            "organization": {
                "_identifier": "*",
                "_entityName": "ADLanguage",
                "$ref": "ADLanguage/192",
                "id": "192",
                "active": true
            },
    ... truncated for clarity ...
            "currency": {
                "_identifier": "USD",
                "_entityName": "Currency",
                "$ref": "Currency/100",
                "id": "100",
                "active": true
            },
            "iBANLength": null,
            "iBANCode": null
        }
    }

The data is contained in the data field, the data maybe a single JSON object or a JSON array with JSON objects. If you update a single object then the ID may be passed in as part of the URL. In general it is better to set the ID in the object. For objects which are updated only the changed fields need to be
passed in.

To do an add operation, the same data format as above should be used without values for the id.

The response of an add or update action contains the updated/added object. In case of an add action, the ID is passed back together with the other properties.

    
    
    {
        "response": {
            "status": 0,
            "data": [
                {
                    "_identifier": "United States3",
                    "_entityName": "Country",
                    "$ref": "Country/FF808181249CF48C01249CF5140E0002",
                    "id": "FF808181249CF48C01249CF5140E0002",
                    "client": {
                        "_identifier": "System",
                        "_entityName": "ADClient",
                        "$ref": "ADClient",
    ... truncated for clarity ...
                        "id": "100",
                        "active": true
                    },
                    "iBANLength": null,
                    "iBANCode": null
                }
            ]
        }
    }

##  DELETE

For the DELETE action, the DELETE HTTP method should be used. The system expects that the ID and entityName are passed in the URL itself. For example;

`https://livebuilds.openbravo.com/erp_pi_pgsql/openbravo/org.openbravo.service.json.jsonrest/Country/FF808181249CF48C01249CF5140E0002`

!!!Note
    In your specific case this country record will probably not exist with the same id.

If this URL is used as the target of the DELETE action, then the Country object
with ID `FF808181249CF48C01249CF5140E0002` is removed. The response will
contain the status code (0 if success) and the complete removed object. For
example:

    
    
    {
        "response": {
            "status": 0,
            "data": [
                {
                    "_identifier": "United States3",
                    "_entityName": "Country",
                    "$ref": "Country/FF808181249CF48C01249CF5140E0002",
                    "id": "FF808181249CF48C01249CF5140E0002",
                    "client": {
                        "_identifier": "System",
                        "_entityName": "ADClient",
                        "$ref": "ADClient",
    ... truncated for clarity ...
                        "id": "100",
                        "active": true
                    },
                    "iBANLength": null,
                    "iBANCode": null
                }
            ]
        }
    }

##  Error Result

The JSON REST service returns errors also as JSON and/or uses standard HTTP error codes.

###  HTTP Error Codes

The following HTTP error codes are used to flag different error situations:

  * 400: the request uri or parameters are incorrect, for example the request uri did not have a valid entity name. 
  * 409: the JSON content is invalid 
  * 404: the object could not be found (applies when a uri points to a single object and that single object can not be found)
  * 401: if a security exception occurs 
  * 500: is used for all other exceptions 

Next to the return response code more error information is returned in the response content (as JSON). See the next section.

!!!Note
    Validation exceptions which occur at an update or insert are not considered as real application errors and are not handled through HTTP error response codes.

###  JSON Error Result

There are two types of situations which will result in an error JSON message:

  * an application error 
  * a validation error on a field/property 

The first error situation will be combined with one of the HTTP error response codes above. The first error result will return a message like this:

    
    
    {
        "response": {
            "status": -1,
            "error": {
                "message": "Invalid url, no entity found with entityName: /openbravo/jsonrest/Count",
                "messageType": "Error",
                "title": ""
            },
            "totalRows": 0
        }
    }

So in this case the response will be a JSON object with the field response which contains two fields a status and as the data the error message. The status codes can be found in the [JsonConstants]() class, all the statics starting with RPCREQUEST_STATUS_.

In case of a validation error the message is different:

    
    
    {
        "response": {
            "status": -4,
            "errors": {
                "creationDate": {
                    "errorMessage": "Cannot format given Object as a Date"
                },
                "updated": {
                    "errorMessage": "Cannot format given Object as a Date"
                },
                "hasRegions": {
                    "errorMessage": "hasRegions: Property Country.hasRegions only allows instances of java.lang.Boolean but the value is an instanceof java.lang.String"
                }
            }
        }
    }

In this case, the response object contains one or more fields with an error message. Each field/message combination relates to one specific property of an object.

##  Login and Security

The JSON webservice provides the same login and security control as the [XML REST](https://wiki.openbravo.com/wiki/XML_REST_Web_Services#Login_and_Security){target="\_blank"} webservice.

The data access authorization is defined through the table and window access in Etendo. See the  [Security and Validation](../concepts/Data_Access_Layer.md#security-and-validation) section in the  DAL developers guide for more details.

Also, the default role for the user who is doing the log in should be enabled to do calls to web services. Search for "Is Web Service Enabled" inside the [Role](../../../user-guide/etendo-classic/basic-features/general-setup/security.md#role) document for more information.

##  JSON Core Classes

This section of the developers manual describes the classes and components used by the JSON REST webservice. These classes can be used as a basis for other modules as well.

All classes discussed here can be found in the modules/org.openbravo.service.json/src folder in the
[org.openbravo.service.json] package.

###  DataToJsonConverter

The  [DataToJsonConverter]()  class converts an Etendo Business Object (a [BaseOBObject]()) to its JSON representation. This class should be instantiated for each conversion action (use the [OBProvider factory] pattern for this).

This class provides two main public methods: toJsonObjects and toJsonObject. The first converts a list of BaseOBObjects to a list of JSONObjects. The latter performs the same action for a single BaseOBObject returning a single JSONObject. The conversion logic is described in the sections above.

###  JsonToDataConverter

The  [JsonToDataConverter]()  class converts JSON back to Etendo business object. This class uses an internal map/cache to synchronize references between JSON objects passed in together. This class can therefore not be shared by multiple threads.

This class provides three conversion methods: toBaseOBObject and 2 toBaseOBObjects methods receiving a JSONArray or a list of JSONObjects.

The logic reads objects from the database using the [DAL](../concepts/Data_Access_Layer.md) and it therefore assumes that it runs in a standard Etendo [transactional](../concepts/Data_Access_Layer.md#transaction-and-session) environment.
Objects read from the database are updated in memory so if at the end of the request the transaction commits then the objects are saved. It is however better to do an explicit flush and commit as it makes it possible to capture any hibernate or database exceptions.

    
    
    try {
    	final List<BaseOBObject> bobs = fromJsonConverter.toBaseOBObjects((JSONArray) jsonContent);
     
    	// error handling removed to get a focused code snippet	
     
    	for (BaseOBObject bob : bobs) {
    		OBDal.getInstance().save(bob);
    	}
    	OBDal.getInstance().flush();
     
    	// almost successfull, now create the response
    	// needs to be done before the close of the session
    	final DataToJsonConverter toJsonConverter = OBProvider.getInstance().get(DataToJsonConverter.class);
    	final List<JSONObject> jsonObjects = toJsonConverter.toJsonObjects(bobs);
     
    	OBDal.getInstance().commitAndClose();
    } catch (Exception e) {
    	// convert the exception to JSON
    	return convertExceptionToJson(e);
    }

The above code snippet also converts back to JSON to create a response string later. The JSON contains all the objects which have been updated/saved. This to pass back any new IDs. Creating such a response needs to be done before closing the session because hibernate may access to database to get extra information.

The  JsonToDataConverter  also collects all errors it encounters. You can check if errors occured (call: hasErrors()) and get the errors (call getErrors()). The error objects contain both the property on which the error occured and the throwable and object itself.

###  JsonDataService

The  JsonDataService  class provides four types of methods: fetch, remove, add and update. The methods expect a combination of a parameter map and the request content.

####  Fetch Operation

The fetch method fetches one or more objects from the database using the query parameters specified in the parameters map. The query parameters can be a filter criteria, paging parameters or a where clause. The parameter names are defined in the  JsonConstants  class, all the statics ending on _PARAMETER.

The JSON string returned contains paging information as well as the actual retrieved data (which can be empty if not found).

Note that the JSON returned from the fetch operation is slightly different from the one returned by the REST service itself. The fetch operation will always return the object as a JSON object wrapped in another JSON object containing metadata. The REST service will for single objects unwrap the JSON object and return that. So the fetch operation will return this:

while the REST webservice will return this JSON:

    
    
    {
        "_identifier": "United States",
        "_entityName": "Country",
        "$ref": "Country/100",
        "id": "100",
        "name": "United States",
        "description": "United States of America",
        "iSOCountryCode": "US",
    ... truncated ...
        "language": "en_US",
        "language$_identifier": "English (USA)",
        "currency": "100",
        "currency$_identifier": "USD",
        "iBANLength": null,
        "iBANCode": null,
    }

the fetch method the JsonDataService will return this (so with paging information):

    
    
    {
        "response": {
            "status": 0,
            "startRows": 10,
            "endRow": 12,
            "totalRows": 240,
            "data": [
                {
                    "_identifier": "Armenia",
                    "_entityName": "Country",
                    "$ref": "Country/120",
                    "id": "120",
                    "client": {
                        "_identifier": "System",
                        "_entityName": "ADClient",
                        "$ref": "ADClient/0",
                        "id": "0",
                        "active": true
                    },
                    "organization": {
                        "_identifier": "*",
                        "_entityName": "Organization",
                        "$ref": "Organization"
                    }
                },
                {
                    "language": {
    ... truncated for clarity ...
                        "_entityName": "ADLanguage",
                        "$ref": "ADLanguage/126",
                        "id": "126",
                        "active": true
                    },
                    "currency": {
                        "_identifier": "AUD",
                        "_entityName": "Currency",
                        "$ref": "Currency/120",
                        "id": "120",
                        "active": true
                    },
                    "iBANLength": null,
                    "iBANCode": null
                }
            ]
        }
    }

!!!Note
    The fetch method will do a count operation and return the startRows value if the parameters which are passed in have values for the paging parameters.

####  Remove Operation

The remove operation expects a parameter map with two parameters and ID and entityName. It removes the object and returns the removed object as a JSON string. See the DELETE method description above. Note that if the object can not be found in the database that an error message is returned.

####  Add and Update Operation

The add and update operation operate in the same way. If an object has an ID and it exists in the database then an update action is done, in all other cases an add is done. The input for both operations is a parameter map and the posted content. For what type of posted content is expected see the above description of the PUT and POST operation. The parameter map may contain an ID and entityName parameter. If so, then they are used to identify the object to update. 

!!!note
    These parameters are only used if only one object is posted.

####  Test Cases

The JSON REST source code contains several testcases which can be found in the [org.openbravo.service.json.test]() package.

!!!note
    Some of the test cases require a running Etendo instance on localhost:8080 and context Etendo. This can be easily changed to another setting in the [JsonRestTest]() class.

---

This work is a derivative of [JSON Rest Web Services](http://wiki.openbravo.com/wiki/JSON_REST_Web_Services){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 