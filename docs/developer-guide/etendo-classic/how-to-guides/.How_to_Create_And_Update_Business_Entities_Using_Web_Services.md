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

  

#  How to Create And Update Business Entities Using Web Services

**Languages:** |

** English  ** |  Translate this article...  
  
---|---  
  
##  Contents

  * 1  Objective 
  * 2  Recommended articles 
  * 3  Execution Steps 
    * 3.1  JSON REST 
    * 3.2  XML REST 

  
---  
  
##  Objective

The objective of this article is to show you how to use some of Openbravo's
available web services to create business entities and/or to update them.

Therefore, we will exemplary show it for these two sets of web services:

  * **JSON REST**
  * **XML REST**

##  Recommended articles

Before reading this guide, we recommend that you take some time to get further
information about these two web service concepts being used to achieve the
goal of this article:

  * JSON REST web services 
  * XML REST web services 
  * How to call an Openbravo Webservice from Java 

##  Execution Steps

To add or update entities, we use **HTTP** commands. To execute any HTTP
commands, we could create a  **Java class** and use the available classes
related to the HTTP protocol.  
(Note: We could do the same for any other protocol or scripting language like
PHP).

Alternatively, we could use a plugin like **Poster** (for Firefox; downoad
here  ) which allows us to execute any HTTP command on an URL of your choice.  
In the examples we will show, we will make use of this plugin and we will be
assuming that our Openbravo environment is running on a local machine via

    
    
    http://localhost:8080/openbravo
    

###  JSON REST

We are about to create a new **invoice header** , so that the URL for this
case will be

    
    
    http://localhost:8080/openbravo/org.openbravo.service.json.jsonrest/Invoice
    

Into **"User Auth"** we have to insert the credentials which we use to get
access to the web service (which are by the way the same that we use to get
into the application). You have to take into account that the visibility of
the data within the web service will be the same as if you logged into the
application with the default role of this user. The **"Content-Type"** of the
Request will be _**"text/xml"** _ and the least content will be as follows,
where the **"id"** s will be replaced by those that we want to be present in
the invoice. Note that we have set the attribute **"salesTransaction"** to
_**"true"** _ , indicating that this is a sales invoice:

    
    
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

View larger

|  |

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-2.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-3.png){: .legacy-image-style}

View larger

|  
---|---|---|---|---  
We use the **HTTP POST** command with this data. We will get a _**"200 OK"** _
response back, indicating that everything went well with the invoice data we
have just created.

To make an update, we will use the **PUT** command. For instance, to update a
Business Partner's name, we will execute that command on this URL:

    
    
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

Now we will create a new invoice header using **XML REST** . In the case of
REST, the process is **analog** to the method explained above, except of the
URL on which we have to execute the **HTTP POST** command:

    
    
    http://localhost:8080/openbravo/ws/dal/Invoice
    

, and obviously the invoice data, since we have to convert it into the **xml
format** :

    
    
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

|

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-4.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-5.png){: .legacy-image-style}

View larger

|  |

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-6.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_And_Update_Business_Entities_Using_Web_Services-7.png){: .legacy-image-style}

View larger

|  
---|---|---|---|---  
And for our example of updating the Business Partner's name, we will need the
following content:

    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <ob:Openbravo xmlns:ob="http://www.openbravo.com">
    <BusinessPartner id="A6750F0D15334FB890C254369AC750A8">
    <name>New Name</name>
    </BusinessPartner>
    </ob:Openbravo>

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_Create_And_Update_Business_Entities_Using_Web_Services
"

This page has been accessed 15,768 times. This page was last modified on 27
August 2013, at 10:48. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

