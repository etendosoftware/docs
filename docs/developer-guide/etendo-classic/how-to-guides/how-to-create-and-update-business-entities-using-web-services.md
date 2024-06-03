---
tags:
  - web services
  - business entities
  - update
  - Etendo Classic
  - JSON REST
  - XML REST
---

#  How to Create And Update Business Entities Using Web Services  
  
##  Overview

The point of this section is to show you how to use some of Etendo's available web services to create business entities and/or to update them.

Therefore, we will exemplary show it for these two sets of web services:

  * **JSON REST**
  * **XML REST**

##  Execution Steps

To add or update entities, we use **HTTP** commands. To execute any HTTP commands, we could create a  [**Java class**](../how-to-guides/how-to-call-an-etendo-webservice-from-java.md) and use the available classes related to the HTTP protocol.  

!!!note
    We could do the same for any other protocol or scripting language like PHP.

Alternatively, we could use a plugin like **Poster** which allows us to execute any HTTP command on an URL of your choice.  
In the examples we will show, we will make use of this plugin and we will assume that our Etendo environment is running on a local machine via
    
    http://localhost:8080/etendo
    

###  JSON REST

We are about to create a new **invoice header**, so that the URL for this case will be
    
    http://localhost:8080/openbravo/org.openbravo.service.json.jsonrest/Invoice
    

In **User Auth** we have to insert the credentials which we use to get access to the web service (which are by the way the same that we use to get into the application). You have to take into account that the visibility of the data within the web service will be the same as if you logged into the application with the default role of this user. The **Content-Type** of the Request will be **text/xml** and the least content will be as follows, where the **ID**s will be replaced by those that we want to be present in the invoice. Note that we have set the attribute **salesTransaction** to **true**, indicating that this is a sales invoice:

    
    
    {
      data: 
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

|

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-0.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-1.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-2.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-3.png){: .legacy-image-style}

We use the **HTTP POST** command with this data. We will get a **200 OK** response back, indicating that everything went well with the invoice data we have just created.

To make an update, we will use the **PUT** command. For instance, to update a Business Partner's name, we will execute that command on this URL:

    
    http://localhost:8080/openbravo/org.openbravo.service.json.jsonrest/BusinessPartner
    

with the following content:

    
    
    {
      data: 
      {
        "entityName": "BusinessPartner",
        "id":         "A6750F0D15334FB890C254369AC750A8",
        "name":       "New Name"
      }
    }

###  XML REST

Now we will create a new invoice header using **XML REST**. In the case of REST, the process is **analog** to the method explained above, except for the URL on which we have to execute the **HTTP POST** command:
    
    
    http://localhost:8080/openbravo/ws/dal/Invoice
    

and obviously the invoice data, since we have to convert it into the **xml format**:

    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <ob:Openbravo xmlns:ob="http://www.openbravo.com">
      <Invoice>
        <active>true</active>
        <organization id="E443A31992CB4635AFCAEABE7183CE85"/>
        <salesTransaction>true</salesTransaction>
        <documentType id ="7FCD49652E104E6BB06C3A0D787412E3"/>
        <transactionDocument id ="7FCD49652E104E6BB06C3A0D787412E3"/>
        <documentNo>1000050</documentNo>
        <accountingDate>2012-05-29</accountingDate>
        <invoiceDate>2012-05-29</invoiceDate>
        <currency id="102"/>
        <priceList id="AEE66281A08F42B6BC509B8A80A33C29"/>
        <businessPartner id="9E6850C866BD4921AD0EB7F7796CE2C7"/>
        <partnerAddress id="BFE1FB707BA84A6D8AF61A785F3CE1C1"/>
        <paymentTerms id="66BA1164A7394344BB9CD1A6ECEED05D"/>
        <paymentMethod id="A97CFD2AFC234B59BB0A72189BD8FC2A"/>
      </Invoice>
    </ob:Openbravo>


![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-4.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-5.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-6.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-7.png){: .legacy-image-style}

And for our example of updating the Business Partner's name, we will need the following content:

    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <ob:Openbravo xmlns:ob="http://www.openbravo.com">
    <BusinessPartner id="A6750F0D15334FB890C254369AC750A8">
    <name>New Name</name>
    </BusinessPartner>
    </ob:Openbravo>

---

This work is a derivative of [How to Create and Update Business Entities using Web Services](http://wiki.openbravo.com/wiki/How_to_Create_And_Update_Business_Entities_Using_Web_Services){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.