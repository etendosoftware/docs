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

  

#  Authentication

##  Contents

  * 1  Introduction 
  * 2  How authentication works in Openbravo ERP 
  * 3  How to configure the authentication manager in Openbravo ERP 
    * 3.1  Default Authentication Manager 
  * 4  Getting Authentication Manager 
  * 5  Develop your own Authentication Manager 
    * 5.1  Web Services and Connectors 
  * 6  Authentication with an External Authentication Provider 
    * 6.1  OpenID Authentication 
    * 6.2  Login Page 
    * 6.3  Additional Topics 

  
---  
  
##  Introduction

In context of Openbravo _Authentication_ is the act verifying a Users'
identity. This can be done by asking for Username & Password and verify it
against the built-in _AD_User_ table or any other mechanism.

The process of _Authorization_ which is to determine which actions (like
opening a specific window, or launching a process) a user then is allowed to
do is a separate topic and not scope of this article.

##  How authentication works in Openbravo ERP

When a user wants to gain access to an Openbravo ERP resource. Openbravo ERP
asks to the authentication manager the application User Id of the user that
request access to the Openbravo ERP resource. If the user has not been
authenticated before the authentication provider has the responsibility of
authenticating this user.

The following describes the flow of events happening when using the
_DefaultAuthenticationManager_ :

  * Visit any Openbravo URL for the first time, a Cookie is send back to the browser to allow the usual creation of a HTTP-Session to allow to group the users' request together. 
  * The Authentication Manager's authenticate method is called to check if the session has been already authenticated. The DefaultAuthenticationManagers implementation checks for a special attribute in the HTTP-Session object to decide if this session is authenticated or not. As it is not yet it redirects the user to the standard Openbravo Login-Page asking for User & Password. 
  * When the Login Form is submitted the  LoginHandler  class verifies those credentials against the 'AD_User _table and if accepted sets special attribute HttpSession to mark this session as authenticated and to store the userID of the authenticated user._
  * Then a redirect to the previously requested page is done. 
  * For this request the AuthenticationManagers' _authenticate_ Method is called again. As now the attribute is set in the HttpSession corresponding to this request it returns the userID of the authenticated User and the request continues to be handled in the usual way. 
  * The same now happens for any following request while normally using the application. 
  * This session will be invalidated by any of the following three events: 
    * Explicit logout by the user 
    * Session-Timeout (invalidating the HttpSession) 
    * Clear Browser-Cookie by the User 
  * In that case the flow is back to the first step and the same cycle begins again. 

Note that this only described the flow of events when using the
DefaultAuthenticationManager. Any other implementation may implement this
different by i.e. not using the standard Openbravo Login-page at all or using
another mechanism to mark the HTTP-Session as authenticated.

##  How to configure the authentication manager in Openbravo ERP

The authentication manager used in Openbravo ERP is defined in the
configuration file  Openbravo.properties  . In the property
_authentication.class_ you have to write the class name of the authentication
provider that Openbravo will use for this purpose.

Openbravo includes three _AuthenticationManager_ implementations:

###  Default Authentication Manager

This is the default authentication manager provided by Openbravo. It is the
classic authentication method that uses the Openbravo current login page to
authenticate users.

After installing Openbravo ERP you do not need to configure anything if you
want to use this authentication manager that is the classic method Openbravo
authenticates application users.

##  Getting Authentication Manager

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |
Available from **3.0MP7**  
---|---  
  
To obtain an instance of the Authentication Manager defined in the
Openbravo.properties, it is possible to use the
_AuthenticationManager.getAuthenticationManager_ method.

##  Develop your own Authentication Manager

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
implementation is available from **3.0MP7** . From **3.0MP4** to **3.0MP6** ,
the same is valid but web service implementation is not present in
_AuthenticationManager_ . For versions previous to **3.0MP4** ,
_AuthenticationManager_ was an interface, check  here  how it worked.  
---|---  
  
You can also develop your own Authentication manager. To do this you have to
create a new java class that extends the abstract class
org.openbravo.authentication.AuthenticationManager  . This interface has the
following methods:

    
    
     
      public void init(HttpServlet s) throws AuthenticationException;
     
      public final String authenticate(HttpServletRequest request, HttpServletResponse response)
          throws AuthenticationException, ServletException, IOException
     
      public final String webServiceAuthenticate(HttpServletRequest request)
          throws AuthenticationException
     
      public final String webServiceAuthenticate(String user, String password)
          throws AuthenticationException
     
      public final String connectorAuthenticate(HttpServletRequest request)
          throws AuthenticationException
     
      public final String connectorAuthenticate(String user, String password)
          throws AuthenticationException
     
      protected abstract String doAuthenticate(HttpServletRequest request, HttpServletResponse response)
          throws AuthenticationException, ServletException, IOException
     
      protected String doWebServiceAuthenticate(HttpServletRequest request)
     
      protected String doWebServiceAuthenticate(String user, String password)
     
      public final void logout(HttpServletRequest request, HttpServletResponse response)
          throws ServletException, IOException
     
      protected abstract void doLogout(HttpServletRequest request, HttpServletResponse response)
          throws ServletException, IOException

The method _init_ is called after the class is instantiated. It can be used to
read the configuration parameters of the authentication manager if needed.

The method _authenticate_ is called for each single request done which
requires authentication. It invokes the abstract _doAuthenticate_ method which
if this request is authenticated, must the return the userid of the
authenticated user. This id must be a valid ad_user_id of a existing entry in
the _AD_User_ table.

Otherwise the method must perform the needed steps to acquire some
authentication and then return _null' as return-value for the function.
Usually this consists of redirecting the user to some kind of_ Login-Page _and
asking for credentials._ After these have been verified the _authenticate_
method will be called again for the next request an now will succeed and
return the userId as described above.

The method _logout_ is called when the user requests to close the current
session. This method invokes the abstract _doLogout_ . The work expected to be
done by the authentication manager is to invalidate the existing session and
redirect the user to a page where a new login page be done.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Starting
from  3.0PR18Q1.4  ` AuthenticationManager ` s where authentication page is
served outside Openbravo code, for example from a Single Sign On service, must
override ` useExternalLoginPage ` method, returning ` true ` .  
---|---  
  
![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Note for
implementation: The _authenticate_ method is always called with DAL adminMode
being active, so code inside it does not need to manage the adminMode on its
own.  
---|---  
  
###  Web Services and Connectors

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  All
external authenticated services **must** make use of _webServiceAuthenticate_
authentication. Authorized _Connectors_ can use _connectorAuthenticate_ .  
---|---  
  
Web Service authentication invokes _webServiceAuthenticate_ and connectors
invoke _connectorAuthenticate_ , both of them call _doWebServiceAuthenticate_
. This method is implemented to do standard authenitcation, it first looks
whether user ( _l_ ) and password ( _p_ ) are sent as request parameters, if
not basic authentication is performed. _doWebServiceAuthenticate_ method can
be implemented by authentication managers in case different authentication is
needed.

_webServiceAuthenticate_ and _connectorAuthenticate_ are overloaded to accept
both _HttpServletRequest_ parameter (default one) or _String, String_
parameters. This second one, should be used by other services where the
default one is not suitable, this ones receives user and password parameters.

##  Authentication with an External Authentication Provider

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 23Q4  ** .  
---|---  
  
To authenticate with an external authentication provider, the provider
configuration must be created, as system administrator, in the
**Authentication Provider Configuration** window. In the header the following
fields should be populated:

  * Name: a descriptive name for the authentication provider 
  * Type: the type or authentication protocol used by the provider 
  * Sequence Number: determines the position in the login page of the button linked to this configuration. Lower values appears first 
  * Icon: the image show in the button that is rendered in the login page linked to this configuration 
  * Description: an optional text to include additional information about the configuration 

![](/assets/developer-guide/etendo-classic/concepts/Authentication-6.png){: .legacy-image-style}

###  OpenID Authentication

If the selected type in the header is _OpenID_ then the **OpenID** subtab is
displayed, allowing to configure the specific  OpenID  settings required by
the external authentication provider:

  * Client ID: identifies the client application making a request to the authorization server. The client identifier is typically assigned by the authorization server when the client application is registered and is unique to the authorization server 
  * Client Secret: a confidential identifier known only to the client application and the authorization server. It is used to authenticate the client application when making requests to the authorization server to obtain an access token 
  * Authorization URL: the URL of the server to request for the authentication 
  * Access Token URL: the URL to request the OAuth 2.0 access token 
  * Certificate URL: the URL where the certificates required for the ID token verification can be requested. The supported certificate types that can be retrieved through this URL are: 
    * X.509 in ASCII PEM format 
    * JSON Web Key (JWK) 

![](/assets/developer-guide/etendo-classic/concepts/Authentication-7.png){: .legacy-image-style}

Note there can only be one active record in the OpenID subtab per
configuration.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  For the
OpenID authentication it is expected that the **e-mail** is used to identify
the user in the external authentication provider, so the e-mail provided in
the authentication must be the e-mail of the  Openbravo User  that is
accessing into the application.  
---|---  
  
###  Login Page

Once configured the login page will display one button per active
configuration.

![](/assets/developer-guide/etendo-classic/concepts/Authentication-9.png){: .legacy-image-style}

###  Additional Topics

  * The  Google Sign In  module is deprecated in favor of using this External Authentication Provider configuration. 

Retrieved from "  http://wiki.openbravo.com/wiki/Authentication  "

This page has been accessed 15,815 times. This page was last modified on 26
July 2023, at 15:01. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

