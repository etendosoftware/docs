---
tags:
  - Cómo hacer
  - Entidades de negocio
  - Actualizar
  - Etendo Classic
  - JSON REST
  - Servicios web seguros
---

# Cómo crear y actualizar entidades de negocio mediante servicios web

## Visión general

El objetivo de esta sección es mostrar cómo utilizar algunos de los **servicios web disponibles de Etendo** para crear entidades de negocio y/o actualizarlas.

Por lo tanto, estas funcionalidades de servicios web se explicarán en detalle:

  * **JSON REST**
  * **Servicios web seguros**

## Pasos de ejecución

Para añadir o actualizar entidades, utilice comandos `HTTP`. Para ejecutar cualquier `comando HTTP`, se podría crear una [**Clase Java**](../how-to-guides/how-to-call-an-etendo-webservice-from-java.md) y utilizar las clases disponibles relacionadas con el protocolo HTTP.

!!!note
    Podríamos hacer lo mismo para cualquier otro protocolo o lenguaje de scripting como PHP.

Alternativamente, utilice cualquier plugin o aplicación como [**Postman**](https://www.postman.com/downloads/){target="\_blank"}, que permite ejecutar cualquier comando HTTP sobre una URL de su elección. En los siguientes ejemplos haremos uso de este plugin y asumiremos que nuestro entorno de Etendo se está ejecutando en una máquina local mediante `http://localhost:8080/etendo`.

### JSON REST

Estamos a punto de crear una nueva **cabecera de factura**, por lo que la URL para este caso será:

    http://localhost:8080/etendo/org.openbravo.service.json.jsonrest/Invoice

En `Authorization` tenemos que seleccionar el tipo **Basic Auth** y añadir las credenciales que utilizamos para obtener acceso al **Servicio web** (que, por cierto, son las mismas que utilizamos para entrar en la aplicación). Tenga en cuenta que la visibilidad de los datos dentro del servicio web será la misma que si hubiera iniciado sesión en la aplicación con el rol por defecto de este usuario. El `Content-Type` de la solicitud será `application/json` y el contenido del **Cuerpo** de la solicitud será el siguiente, donde los `ID` se sustituirán por los necesarios para que estén presentes en la factura. 

Hemos establecido el atributo `salesTransaction` en `true`, indicando que se trata de una factura de ventas:

```json
    {
      "data":
      {
        "entityName":          "Invoice",
        "active":              true,
        "organization":        { "id": "E443A31992CB4635AFCAEABE7183CE85" },
        "salesTransaction":    true,
        "documentType":        { "id": "7FCD49652E104E6BB06C3A0D787412E3" },
        "transactionDocument": { "id": "7FCD49652E104E6BB06C3A0D787412E3" },
        "documentNo":          "1000050",
        "accountingDate":      "2012-05-29",
        "invoiceDate":         "2012-05-29",
        "currency":            { "id": "102" },
        "priceList":           { "id": "AEE66281A08F42B6BC509B8A80A33C29" },
        "businessPartner":     { "id": "9E6850C866BD4921AD0EB7F7796CE2C7" },
        "partnerAddress":      { "id": "BFE1FB707BA84A6D8AF61A785F3CE1C1" },
        "paymentTerms":        { "id": "66BA1164A7394344BB9CD1A6ECEED05D" },
        "paymentMethod":       { "id": "A97CFD2AFC234B59BB0A72189BD8FC2A" }
      }
    }
```

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-0.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-1.png)

Utilizamos el comando HTTP `POST` con estos datos. Obtendremos una respuesta `200 OK`, lo que indica que todo ha ido bien con los datos de la factura que se acaba de crear.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-2.png)

Para realizar una actualización, utilizaremos el comando `PUT`. Por ejemplo, para actualizar el nombre de un tercero, ejecutaremos ese comando sobre esta URL:

  `http://localhost:8080/etendo/org.openbravo.service.json.jsonrest/BusinessPartner`

con el siguiente contenido:

```json
    {
      "data":
      {
        "entityName": "BusinessPartner",
        "id":         "A6750F0D15334FB890C254369AC750A8",
        "name":       "New Name"
      }
    }
```

### Servicios web seguros

!!!note
    Para saber más sobre cómo Etendo introduce sus propios Servicios web seguros con funcionalidades únicas, visite [Cómo usar servicios web seguros](../how-to-guides/how-to-use-secure-webservices.md).

---

Este trabajo es una obra derivada de [Cómo crear y actualizar entidades de negocio mediante servicios web](https://wiki.openbravo.com/wiki/How_to_Create_And_Update_Business_Entities_Using_Web_Services){target="\_blank"} de [Openbravo Wiki](https://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.