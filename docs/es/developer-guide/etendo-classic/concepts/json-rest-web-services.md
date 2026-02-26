---
title: Servicios web JSON REST
tags:
    - JSON 
    - REST
    - Servicios web
    - Smartclient

status: beta
---

#  Servicios web JSON REST

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
##  Visión general

Esta sección describe la funcionalidad JSON REST de Etendo tal y como la proporciona el [módulo Etendo JSON REST](https://github.com/etendosoftware/etendo_core/tree/main/modules_core/org.openbravo.service.json){target="\_blank"} incluido en Etendo Core. La funcionalidad **JSON REST** consta de 2 partes principales:

1. el *servicio web JSON REST*, y    
2. las clases subyacentes utilizadas para proporcionar este servicio (principalmente convertidores de objetos de negocio a `JSON` y viceversa).

    Como desarrollador, puede integrarse directamente con el servicio web JSON REST o desarrollar su propio servicio web haciendo uso de las clases principales de JSON REST.
    Como nota adicional, el formato `JSON` esperado y devuelto por este servicio web sigue el formato utilizado por [Smartclient](https://smartclient.com/){target="\_blank"}. 

    !!!info
        Para más información sobre la sintaxis JSON de Smartclient, consulte estos enlaces:

        - [Integración cliente-servidor de Smartclient](https://smartclient.com/smartclient-release/isomorphic/system/reference/?id=class..clientDataIntegration){target="\_blank"} 
        - [Fuente de datos REST de Smartclient](https://smartclient.com/smartclient-release/isomorphic/system/reference/?id=class..RestDataSource){target="\_blank"} 

    Esta funcionalidad no la proporciona Etendo Core
## Glosario y enlaces

Este manual asume que usted está familiarizado con los conceptos de `JSON` y `REST`. Los siguientes enlaces proporcionan información de referencia sobre estos temas.

- [json.org](https://www.json.org/json-en.html){target="\_blank"} 
- [Wikipedia de JSON](https://en.wikipedia.org/wiki/JSON){target="\_blank"}  
- [Wikipedia de REST](https://en.wikipedia.org/wiki/REST){target="\_blank"}
##  Conversión desde y hacia JSON

Esta sección analiza cómo se convierten los objetos de negocio desde y hacia `JSON`. La lógica es utilizada por el servicio web para implementar la lógica de recuperación, actualización e inserción. Los servicios web de Etendo devolverán el `JSON` comprimido. `JSON` comprimido (tal y como lo devuelven los servicios web):

```
"language":{"_identifier":"English (USA)","entityName":"ADLanguage","$ref":"ADLanguage\/192","id":"192","active":true}
```

JSON formateado (mejor legibilidad):

```
"language":{
    "_identifier":"English (USA)",
    "entityName":"ADLanguage",
    "$ref":"ADLanguage/192",
    "id":"192",
    "active":true
}
```

###  Convertir de un objeto de negocio a JSON

Para convertir un objeto de negocio a `JSON`, la lógica itera sobre todas las propiedades (excepto las propiedades de lista/uno-a-muchos) del objeto y aplica la siguiente lógica:

- el nombre de la propiedad se utiliza como el nombre del campo/clave `JSON`
- a un valor nulo se le asigna `JSONObject.NULL `
- una propiedad de fecha o fecha y hora se convierte a una `string` usando el formato de esquema `XML` (p. ej. `yyyy-MM-dd'T'HH\:mm:ss.S`)
- otras propiedades de tipo primitivo (`string`, `numeric`) se convierten usando el propio `JSON`.
- una referencia a otro objeto se `jsonifica` creando un objeto `JSON` con un conjunto limitado de propiedades: el `id`, `_identifier`, `entityName $ref`, active (consulte la descripción de las propiedades especiales más arriba). Por ejemplo, el siguiente fragmento JSON muestra una referencia para una propiedad llamada `language`:

```
"language":{
    "_identifier":"English (USA)",
    "entityName":"ADLanguage",
    "$ref":"ADLanguage/192",
    "id":"192",
    "active":true
}
```

!!! Note 
    Las propiedades de lista/uno-a-muchos no se convierten. Por ejemplo, cuando una factura se convierte a `JSON`, sus líneas de factura no estarán presentes en la cadena `JSON`. Las líneas de factura se pueden recuperar con una solicitud `JSON` independiente.

Aquí puede encontrar un ejemplo del objeto País (con id 100) convertido a `JSON`:

```
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
```

###  Convertir de JSON a un objeto de negocio (usando la base de datos)

La lógica de `JSON` a objeto de negocio es ligeramente más compleja, ya que intenta tener en cuenta que un objeto puede existir en la base de datos e intentará actualizar dicho objeto. Además, se admiten referencias entre objetos `JSON`.

La lógica de conversión recorre los siguientes pasos:

1. la lógica comprueba si el objeto `JSON` contiene un valor id y _entityName. Si es así, intenta leer el objeto desde la base de datos. Si no está establecido o no se encuentra en la base de datos, se crea un objeto nuevo. El objeto se almacena en memoria usando el id encontrado en el objeto `JSON`; esto permite que otros objetos `JSON` en el mismo lote de conversión utilicen/hagan referencia a ese id.
2. a continuación, para cada propiedad del objeto (excepto lista/uno-a-muchos) se comprueba si el objeto `JSON` contiene un valor para esa propiedad.  
    Si existe un valor, entonces, dependiendo de si es una propiedad primitiva o una propiedad de referencia, se gestiona de forma diferente.
3. un valor primitivo se convierte mediante el propio `JSON`, excepto los valores de fecha. Estos se convierten usando formateadores de fecha con el patrón de formato de XML Schema.
4. un valor de referencia se trata de forma diferente. Se asume que el valor de una propiedad de referencia en `JSON` también es un objeto `JSON`. Si tiene un valor ID, entonces este se utiliza para buscar en el mapa en memoria (y se encuentra allí si el objeto ya se convirtió anteriormente). Si no se encuentra en el mapa en memoria, entonces el objeto `JSON` referido se convierte usando esta misma lógica, tal y como se describe en estos pasos (por lo tanto, primero se busca en la base de datos y luego se crea uno nuevo) y el BaseOBObject devuelto se considera el valor establecido en la propiedad. Si se encuentra en la base de datos o ya se convirtió anteriormente, entonces se utiliza ese BaseOBObject.

**Propiedades especiales**

La lógica de conversión, en general, convierte todas las propiedades. Además, la lógica anterior proporciona y puede gestionar propiedades especiales adicionales:

- `_identifier`: contiene el contenido (concatenado) de las propiedades/columnas identificadoras de un objeto; también se puede usar como `sortBy` en una consulta.
- `_entityName`: el nombre del tipo del objeto; corresponde a una [Entidad](./data-access-layer.md#etendo-business-objects) específica en el sistema
- `$ref`: es el entityName y el id separados por una barra `/`. Es una identidad 'globalmente' única del objeto; se puede usar para crear la URL para recuperar los detalles del objeto.
##  GET

Una solicitud `get` se puede utilizar para recuperar información de diferentes maneras:

- [https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country](https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country): esto devolverá todos los países 
- [https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country/100](https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country/100)  : esto devolverá un país (el que tiene id 100) 
- [https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country/100?_selectedProperties=id,name](https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country/100?_selectedProperties=id,name)  : solo se devolverán las propiedades id y nombre para el país con id 100 
- [https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country?_startRow=10&_endRow=50&_sortBy=name](https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country?_startRow=10&_endRow=50&_sortBy=name)  : esto devolverá 40 países (filas 10 a 50) ordenados por nombre 
- [https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country?_where=currency.iSOCode='USD'](https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country?_where=currency.iSOCode='USD')  : devuelve todos los países que tienen una moneda con el código ISO USD. El parámetro _where puede contener una cláusula where de HQL válida. 
- [https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/FinancialMgmtPeriod?_where=_computedColumns.status='P'](https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/FinancialMgmtPeriod?_where=_computedColumns.status='P')  : devuelve todos los periodos en estado _Cerrado permanentemente_ (P). Tenga en cuenta que, al referenciar una propiedad basada en una columna calculada (_status_), debe referenciarse comenzando desde la propiedad _computedColumns_. 
- [https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country?_noActiveFilter=true](https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country?_noActiveFilter=true)  : se mostrarán los registros inactivos. El parámetro "_noActiveFilter" se puede establecer en false para evitar mostrar los registros inactivos. 

Diferentes tipos de solicitudes devolverán un resultado ligeramente distinto. La solicitud de un único objeto (la primera de arriba) devuelve un único objeto `JSON`:

```
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
```

Las otras solicitudes que piden múltiples resultados devolverán algo como esto:

```
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
```

La diferencia es que el resultado contiene información de paginación (`startRows` y `endRow`). La solicitud que contiene parámetros de paginación también devolverá el número total de filas para los parámetros de filtro pasados:

```
"response": {
        "data": [... results truncated for clarity ...]
        "status": 0,
        "totalRows": 241,
        "startRow": 0,
        "endRow": 240
}
```

**Propiedades de paginación**

Las solicitudes GET que obtienen múltiples resultados del servicio web pueden incluir propiedades de paginación:

- `totalRows`: muestra el número total de resultados en la respuesta. Si hay más resultados que los obtenidos, su valor será endRows + 2. 
- `startRow`: la fila inicial desde la que se obtendrán los resultados. Si `startRow` es mayor que el número de resultados en la base de datos, no se devolverá ningún resultado. 
- `endRow`: la fila final marca la última fila que se va a recuperar y es exclusiva. Si no se establece, se obtendrán todas las filas. No puede ser menor que la propiedad `startRow`. 

Por ejemplo, solicitar algún objeto con las propiedades startRow = 0 y endRow = 1 recuperará solo una fila. Si hay más filas que no se han obtenido, totalRows será 3 (endRow + 2).
## POST y PUT

Las operaciones POST y PUT realizan acciones de alta y actualización. En el caso de Etendo, la operación PUT también realizará un alta si un objeto no tiene establecido un ID.

Para realizar una operación de actualización, el siguiente `JSON` debe enviarse mediante PUT al sistema:

```
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
```

Los datos se incluyen en el campo `data`; los datos pueden ser un único objeto `JSON` o un array `JSON` con objetos `JSON`. Si actualiza un único objeto, entonces el id puede pasarse como parte de la URL. En general, es mejor establecer el id en el objeto. Para los objetos que se actualizan, solo es necesario enviar los campos modificados.

Para realizar una operación de alta, debe utilizarse el mismo formato de datos que el anterior, pero sin valores para el id.

La respuesta de una acción de alta o actualización contiene el objeto actualizado/añadido. En el caso de una acción de alta, el ID se devuelve junto con el resto de propiedades.

```
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
```
## DELETE

Para la acción DELETE, se debe utilizar el método `HTTP` DELETE. El sistema espera que el ID y el entityName se pasen en la propia URL. Por ejemplo:

https://demo.etendo.cloud/etendo/org.openbravo.service.json.jsonrest/Country/FF808181249CF48C01249CF5140E0002

!!!note
    En su caso específico, es probable que este registro de país no exista con el mismo ID.

Si esta URL se utiliza como destino de la acción DELETE, entonces se elimina el objeto País con ID `FF808181249CF48C01249CF5140E0002`. La respuesta contendrá el código de estado (0 si es correcto) y el objeto completo eliminado. Por ejemplo:

```
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
```
## Resultado de error

El servicio REST `JSON` devuelve los errores también como `JSON` y/o utiliza códigos de error estándar `HTTP`.

**Códigos de error HTTP**

Los siguientes códigos de error `HTTP` se utilizan para indicar diferentes situaciones de error:

- 400: el URI de la solicitud o los parámetros son incorrectos; por ejemplo, el URI de la solicitud no tenía un nombre de entidad válido.
- 409: el contenido `JSON` no es válido
- 404: no se ha podido encontrar el objeto (se aplica cuando un URI apunta a un único objeto y ese único objeto no se puede encontrar)
- 401: si se produce una excepción de seguridad
- 500: se utiliza para todas las demás excepciones

Además del código de respuesta devuelto, se devuelve más información del error en el contenido de la respuesta (como `JSON`). Consulte la siguiente sección.

!!!note
    Las excepciones de validación que se producen en una actualización o inserción no se consideran errores reales de la aplicación y no se gestionan mediante códigos de respuesta de error `HTTP`.

**Resultado de error JSON**

Hay dos tipos de situaciones que darán como resultado un mensaje de error JSON:

- un error de la aplicación
- un error de validación en un campo/propiedad

La primera situación de error se combinará con uno de los códigos de respuesta de error `HTTP` anteriores. El primer resultado de error devolverá un mensaje como este:

```
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
```

Por tanto, en este caso, la respuesta será un objeto `JSON` con el campo `response`, que contiene dos campos: un `status` y, como datos, el mensaje de error. Los códigos de estado se pueden encontrar en la clase `JsonConstants`, todos los estáticos que comienzan por `RPCREQUEST_STATUS_`.

En caso de un error de validación, el mensaje es diferente:

```
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
```

En este caso, el objeto de respuesta contiene uno o más campos con un mensaje de error. Cada combinación campo/mensaje se relaciona con una propiedad específica de un objeto.
##  Inicio de sesión y seguridad

El servicio web `JSON` proporciona el mismo control de inicio de sesión y seguridad que el servicio web [XML REST](../concepts/xml-rest-web-services.md).

La autorización de acceso a los datos se define a través del acceso a tablas y ventanas en Etendo. Consulte la sección [Seguridad y validación](../concepts/data-access-layer.md#security-and-validation) en la guía del desarrollador de [DAL](../concepts/data-access-layer.md) para obtener más detalles.

Además, el rol por defecto del usuario que está realizando el inicio de sesión debe estar habilitado para realizar llamadas a servicios web. Busque "Está habilitado el servicio web" dentro del documento [Rol](../../../user-guide/etendo-classic/basic-features/general-setup/security/role.md#role) para obtener más información.
##  Clases principales de JSON

Esta sección describe las clases y componentes utilizados por el servicio web JSON REST. Estas clases también pueden utilizarse como base para otros módulos.

Todas las clases tratadas aquí se pueden encontrar en la carpeta `modules_core/org.openbravo.service.json/src` en el paquete [org.openbravo.service.json].

### DataToJsonConverter

La clase DataToJsonConverter convierte un objeto de negocio de Etendo (un `BaseOBObject`) a su representación `JSON`. Esta clase debe instanciarse para cada acción de conversión (utilice para ello el patrón de la [factoría OBProvider]).

Esta clase proporciona dos métodos públicos principales: toJsonObjects y toJsonObject. El primero convierte una lista de BaseOBObjects en una lista de JSONObjects. El segundo realiza la misma acción para un único BaseOBObject devolviendo un único JSONObject. La lógica de conversión se describe en las secciones anteriores.

### JsonToDataConverter

La clase JsonToDataConverter convierte `JSON` de vuelta a un objeto de negocio de Etendo. Esta clase utiliza un mapa/caché interno para sincronizar referencias entre `JSONObjects` pasados conjuntamente. Por lo tanto, esta clase no puede compartirse entre múltiples hilos.

Esta clase proporciona tres métodos de conversión: toBaseOBObject y 2 métodos toBaseOBObjects que reciben un JSONArray o una lista de JSONObjects.

La lógica lee objetos de la base de datos utilizando el [DAL](../concepts/data-access-layer.md) y, por lo tanto, asume que se ejecuta en un entorno estándar [transaccional](../concepts/data-access-layer.md#transaction-and-session) de Etendo. Los objetos leídos de la base de datos se actualizan en memoria, de modo que, si al final de la solicitud la transacción confirma, entonces los objetos se guardan. Sin embargo, es mejor realizar un flush y commit explícitos, ya que permite capturar cualquier excepción de Hibernate o de base de datos.

```
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
    // convert the exception to `JSON`
    return convertExceptionToJson(e);
}
```

El fragmento de código anterior también convierte de nuevo a JSON para crear posteriormente una cadena de respuesta. El `JSON` contiene todos los objetos que se han actualizado/guardado. Esto permite devolver cualquier nuevo ID. La creación de dicha respuesta debe realizarse antes de cerrar la sesión porque Hibernate puede acceder a la base de datos para obtener información adicional.

La clase JsonToDataConverter también recopila todos los errores que encuentra. Puede comprobar si se han producido errores (llamada: hasErrors()) y obtener los errores (llamada: getErrors()). Los objetos de error contienen tanto la propiedad en la que se produjo el error como el throwable y el propio objeto.

### JsonDataService

La clase JsonDataService proporciona cuatro tipos de métodos: fetch, remove, add y update. Los métodos esperan una combinación de un mapa de parámetros y el contenido de la solicitud.

#### Operación de obtención

El método fetch obtiene uno o más objetos de la base de datos utilizando los parámetros de consulta especificados en el mapa de parámetros. Los parámetros de consulta pueden ser un criterio de filtro, parámetros de paginación o una cláusula where. Los nombres de los parámetros se definen en la clase JsonConstants, todos los estáticos que terminan en _PARAMETER. La cadena `JSON` devuelta contiene información de paginación, así como los datos realmente recuperados (que pueden estar vacíos si no se encuentran).

!!! Note
    El `JSON` devuelto por la operación de obtención es ligeramente diferente del devuelto por el propio servicio REST. La operación de obtención siempre devolverá el objeto como un objeto `JSON` envuelto en otro objeto `JSON` que contiene metadatos. El servicio REST, para objetos individuales, desempaquetará el objeto `JSON` y devolverá eso. Por lo tanto, la operación de obtención devolverá esto:

mientras que el servicio web REST devolverá este `JSON`:

```
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
```

el método fetch de JsonDataService devolverá esto (por tanto, con información de paginación):

```
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
```

!!!note
    El método fetch realizará una operación de recuento y devolverá el valor `startRows` si los parámetros que se pasan tienen valores para los parámetros de paginación.

#### Operación de eliminación

La operación de eliminación espera un mapa de parámetros con dos parámetros: ID y `entityName`. Elimina el objeto y devuelve el objeto eliminado como una cadena `JSON`. Consulte la descripción del método DELETE anterior.

!!!note
    Si el objeto no se puede encontrar en la base de datos, se devuelve un mensaje de error.

#### Operación de alta y actualización

La operación de alta y actualización funciona del mismo modo. Si un objeto tiene un ID y existe en la base de datos, entonces se realiza una acción de actualización; en todos los demás casos se realiza un alta. La entrada para ambas operaciones es un mapa de parámetros y el contenido publicado. Para saber qué tipo de contenido publicado se espera, consulte la descripción anterior de la operación PUT y POST. El mapa de parámetros puede contener un parámetro ID y `entityName`. Si es así, entonces se utilizan para identificar el objeto a actualizar. Estos parámetros solo se utilizan si se publica un único objeto.

#### Casos de prueba

El código fuente de JSON REST contiene varios casos de prueba que se pueden encontrar en el paquete `org.openbravo.service.json.test`. Tenga en cuenta que algunos de los casos de prueba requieren una instancia de Etendo en ejecución en localhost:8080 y el contexto Etendo. Esto se puede cambiar fácilmente a otra configuración en la clase JsonRestTest.

---

Este trabajo es una obra derivada de [JSON REST Web Services](http://wiki.openbravo.com/wiki/JSON_REST_Web_Services){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.