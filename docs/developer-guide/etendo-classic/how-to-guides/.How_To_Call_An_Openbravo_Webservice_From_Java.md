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

  

#  How To Call An Openbravo Webservice From Java

**Languages:** |

** English  ** |  Translate this article...  
  
---|---  
  
##  Contents

  * 1  Objective 
  * 2  Recommended articles 
  * 3  Execution Steps 
    * 3.1  Background 
    * 3.2  Example Code 
  * 4  Other Aspects 
    * 4.1  Login and Security 
    * 4.2  Basic Authentication: two ways to do it 
    * 4.3  High Frequency - stateless 

  
---  
  
##  Objective

The objective of this article it to provide the necessary steps to prepare a
Java class so it is possible to call Openbravo web services from this class.

##  Recommended articles

Before reading this guide, we recommend that you take some time to get further
information about the REST webservice concept:

  * XML REST web services 

##  Execution Steps

###  Background

To call an **Openbravo Webservice** from a Java class we have to make use of
several classes that provide the proper Java API to create a HTTP connection
via the webservice's URL and to use classes of the **java.io package** that
allow to read the data streams. Furthermore we can optionally use some classes
that ease processing the results that are returned in XML format in case of
the **XML REST** type webservices, because they allow to get, parse and
validate an XML document  [1]  .

###  Example Code

Openbravo has a **test** java class that exemplifies the above. This class is
**"BaseWSTest.java"** and it is located inside the directory _**"src-
test/org/openbravo/test/webservice"** _ . To make a webservice request we have
the **"createConnection()"** method which uses the httpURLConnection class to
make a request to a webservice by using the specific command parameter and
specifying the credentials (username/password).

    
    
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

Note: this sample code uses basic authentication, see below for more details.

Using this function as our base, we will implement other methods for the other
HTTP comamnds: **POST, PUT, GET and DELETE** . Furthermore, this class uses
the **org.xml.sax library** to parse the XML results that will be returned
after our HTTP request, which we refered to before. For example, the **GET**
request:

    
    
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

Thus we can utilize this class as the base for our development and implement
the adaptations that we consider necessary. Using this class, we can implement
calls to the webservices of your choice by simply specifying its path, that
will be formed with the Openbravo URL ( **getOpenbravoURL()** ) plus the
webservice part ( **wsPart** ).

##  Other Aspects

###  Login and Security

Openbravo general webservices provides the same login and security control as
the  XML REST  webservice.

###  Basic Authentication: two ways to do it

The above sample code shows one way of implementing basic authentication:

    
    
        Authenticator.setDefault(new Authenticator() {
          @Override
          protected PasswordAuthentication getPasswordAuthentication() {
            return new PasswordAuthentication(getLogin(), getPassword().toCharArray());
          }
        });

This approach will need two requests. The first one will fail with 401, return
to the caller/client and then call the getPasswordAuthentication method above
for a second request with credentials. As two requests are needed for this
authentication it is less useful for high frequency calls. **To make this type
of approach work in Openbravo code it is required to pass in the parameter
'basicAuthentication=true' in the request url.**

Another approach to set credentials in the request header like this, this only
requires one request as Openbravo will directly find the authentication
information and will not throw a 401:

    
    
     
        String userpass = getLogin() + ":" + getPassword();
        String basicAuth = "Basic " + new String(new Base64().encode(userpass.getBytes()));
        hc.setRequestProperty("Authorization", basicAuth);

###  High Frequency - stateless

Client side code which calls webservices will typically not maintain the
session cookie of the server. This means that every webservice request can
create a new http session on the receiving server. This is not adviced for
high frequency webservices. The implementor of the webservice within the
Openbravo system can force the call being stateless. But the caller can also
achieve this by passing a parameter. See  here  for more details.

Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Call_An_Openbravo_Webservice_From_Java
"

This page has been accessed 11,154 times. This page was last modified on 12
June 2017, at 21:50. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

