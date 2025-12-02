---
title: How to Call an Etendo Webservice from Java 
tags:
    - Java class
    - Etendo webservice
    - HTTP connections
    - Authentication
    - xml-processing
status: beta
---

# How to Call an Etendo Webservice from Java 
  
!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

## Overview

This section explains how to prepare and implement a **Java class** capable of invoking Etendo web services and which **Java APIs** are required to establish HTTP connections, authenticate requests, and process responses, especially those returned in XML format by XML REST webservices. Using Etendo's own `BaseWSTest.java` class as a reference, the guide shows how to build and extend methods for different HTTP operations (GET, POST, PUT, DELETE), handle authentication securely, and manage session behavior for high-frequency or stateless integrations.

!!!info
    For more information visit, [XML REST web services](../../../developer-guide/etendo-classic/concepts/.XML_REST_Web_Services.md). 


## Execution Steps

To call an **Etendo Webservice** from a Java class, make use of several classes that provide the proper Java API to create a HTTP connection via the webservice's URL and to use classes of the `java.iopackage` that allow to read the data streams. Furthermore, optionally use some classes that ease processing the results that are returned in **XML format** in case of the **XML REST** type webservices, because they allow to get, parse and validate an XML document.

### Example Code

Etendo has a **test java class** that exemplifies the above. This class is `BaseWSTest.java` and it is located inside the directory `src-test/org/openbravo/test/webservice`. To make a webservice request we have the **createConnection()** method which uses the httpURLConnection class to make a request to a webservice by using the specific command parameter and specifying the credentials (username/password).

``` java
protected HttpURLConnection createConnection(String wsPart, String method) throws Exception {
    Authenticator.setDefault(new Authenticator() {
        @Override
        protected PasswordAuthentication getPasswordAuthentication() {
            return new PasswordAuthentication(LOGIN, PWD.toCharArray());
        }
    });
    log.debug(method + ": " + getOpenbravoURL() + wsPart);
    final URL url = new URL(getOpenbravoURL() + wsPart + "&basicAuthentication=true");
    final HttpURLConnection hc = (HttpURLConnection) url.openConnection();
    hc.setRequestMethod(method);
    hc.setAllowUserInteraction(false);
    hc.setDefaultUseCaches(false);
    hc.setDoOutput(true);
    hc.setDoInput(true);
    hc.setInstanceFollowRedirects(true);
    hc.setUseCaches(false);
    hc.setRequestProperty("Content-Type", "text/xml");
    return hc;
}
```

!!! note
    This sample code uses basic authentication, see below for more details.

Using this function as base will implement other methods for the other `HTTP` comamnds: **POST, PUT, GET and DELETE**. Furthermore, this class uses the `org.xml.sax library` to parse the `XML` results that will be returned after our `HTTP` request. For example, the **GET** request:
    
``` java 
protected String doTestGetRequest(String wsPart, String testContent, int responseCode,boolean validate) {
    try {
        final HttpURLConnection hc = createConnection(wsPart, "GET");
        hc.connect();
        final SAXReader sr = new SAXReader();
        final InputStream is = hc.getInputStream();
        final StringBuilder sb = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line).append("\n");
        }
        try {
            final Document doc = sr.read(new StringReader(sb.toString()));
            final String content = XMLUtil.getInstance().toString(doc);
            if (testContent != null && content.indexOf(testContent) == -1) {
                log.debug(content);
                fail();
            }
            assertEquals(responseCode, hc.getResponseCode());
            is.close();
            // do not validate the xml schema itself, this results in infinite loops
            if (validate) {
                validateXML(content);
            }
            return content;
        } catch (Exception e) {
            log.debug(sb.toString());
            throw e;
            }
    } catch (final Exception e) {
            throw new OBException("Exception when executing ws: " + wsPart, e);
        }
}
```

Thus, it is possible to utilize this class as the base for the development and implement the adaptations that are considered necessary. Using this class, it is possible to implement calls to the webservices of your choice by simply specifying its path, that will be formed with the Etendo URL **getOpenbravoURL()**  plus the webservice part **wsPart**.

### Login and Security

Etendo general webservices provide the same login and security control as the  XML REST webservice.

### Basic Authentication: 

The bellow sample code shows one way of implementing basic authentication:

    
``` java    
Authenticator.setDefault(new Authenticator() {
    @Override
    protected PasswordAuthentication getPasswordAuthentication() {
    return new PasswordAuthentication(getLogin(), getPassword().toCharArray());
    }
});
```

This approach will need two requests: 

- The first one will fail with 401, return to the caller/client and then call the getPasswordAuthentication method above for a second request with credentials. As two requests are needed for this authentication it is less useful for high frequency calls. 

    To make this type of approach work in Etendo code it is required to pass in the parameter `basicAuthentication=true` in the request url.

- Another approach to set credentials in the request header like this, this only requires one request as Etendo will directly find the authentication information and will not throw a 401:

     
    ``` java
    String userpass = getLogin() + ":" + getPassword();
    String basicAuth = "Basic " + new String(new Base64().encode(userpass.getBytes()));
    hc.setRequestProperty("Authorization", basicAuth);
    ```

### High Frequency - Stateless

Client side code which calls webservices will typically **not maintain** the session cookie of the server. This means that every webservice request can create a new http session on the receiving server. This is not adviced for high frequency webservices. The implementor of the webservice within the Etendo system can **force the call** being stateless. But the caller can also achieve this by passing a parameter. 

---
This work is a derivative of [How to Call an Openbravo Webservice from Java](http://wiki.openbravo.com/wiki/How_To_Call_An_Openbravo_Webservice_From_Java){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 

