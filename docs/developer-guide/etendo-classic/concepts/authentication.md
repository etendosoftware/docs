---
title: Authentication
tags:
  - Authentication
  - Identity
  - Username
  - Password

status: beta
---
#  Authentication
  
##  Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.
    
**Authentication** is the act verifying a user's identity. This can be done by asking for Username & Password and verify it against the built-in `AD_User` table or any other mechanism.

##  How Authentication Works in Etendo

When a user wants to have access to an Etendo resource. Etendo asks to the authentication manager the application User Id of the user that request access to the Etendo resource. If the user has not been authenticated before, the authentication provider has the responsibility of authenticating this user.

The following describes the flow of events happening when using the `DefaultAuthenticationManager`:

1. Visit any Etendo URL for the first time, a cookie is send back to the browser to allow the usual creation of a HTTP-Session to allow to group the users' request together. 
2. The Authentication Manager's authenticate method is called to check if the session has been already authenticated. The DefaultAuthenticationManagers implementation checks for a special attribute in the HTTP-Session object to decide if this session is authenticated or not. As it is not yet it redirects the user to the standard Etendo Login-Page asking for User & Password. 
3. When the Login Form is submitted the `LoginHandler` class verifies those credentials against the `AD_User` table and if accepted sets special attribute HttpSession to mark this session as authenticated and to store the userID of the authenticated user.
4. Then a redirect to the previously requested page is done. 
5. For this request the AuthenticationManagers' `authenticate` Method is called again. As now the attribute is set in the HttpSession corresponding to this request it returns the userID of the authenticated User and the request continues to be handled in the usual way. 
6. The same now happens for any following request while normally using the application. 
7. This session will be invalidated by any of the following three events: 
    * Explicit logout by the user 
    * Session-Timeout (invalidating the HttpSession) 
    * Clear Browser-Cookie by the User 
8. In that case, the flow is back to the first step and the same cycle begins again. 

!!!Note
    This only described the flow of events when using the `DefaultAuthenticationManager`. Any other implementation may implement this different by i.e. not using the standard Etendo Login-page at all or using another mechanism to mark the HTTP-Session as authenticated.

##  How to Configure the Authentication Manager in Etendo

The authentication manager used in Etendo is defined in the configuration file `gradle.properties`. In the property `authentication.class` you have to write the class name of the authentication provider that Etendo will use for this purpose.

Etendo includes three `AuthenticationManager` implementations:

###  Default Authentication Manager

This is the default authentication manager provided by Etendo. It is the classic authentication method that uses the Etendo current login page to authenticate users.

After installing Etendo, you do not need to configure anything if you want to use this authentication manager that is the classic method Etendo authenticates application users.

##  Getting Authentication Manager

!!!info
    To obtain an instance of the Authentication Manager defined in the `gradle.properties`, it is possible to use the `AuthenticationManager.getAuthenticationManager` method.

##  Develop your own Authentication Manager
  
You can also develop your own Authentication manager. To do this, you have to create a new java class that extends the abstract class `org.openbravo.authentication.AuthenticationManager`. This interface has the following methods:

    ```
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
    ```

The method `init` is called after the class is instantiated. It can be used to read the configuration parameters of the authentication manager if needed.

The method `authenticate` is called for each single request done which requires authentication. It invokes the abstract `doAuthenticate` method which if this request is authenticated, must the return the userid of the authenticated user. This id must be a valid ad_user_id of a existing entry in the `AD_User` table.

Otherwise the method must perform the needed steps to acquire some authentication and then return null' as return-value for the function. Usually this consists of redirecting the user to some kind of Login-Page and asking for credentials. After these have been verified the **authenticate** method will be called again for the next request an now will succeed and return the userId as described above.

The method **logout** is called when the user requests to close the current session. This method invokes the abstract `doLogout`. The work expected to be done by the authentication manager is to invalidate the existing session and redirect the user to a page where a new login page be done.

!!!info
    `AuthenticationManager` is where authentication page is served outside Etendo code, for example from a Single Sign On service, must override `useExternalLoginPage` method, returning `true`.  
  
!!!Note
    For implementation: The **authenticate** method is always called with DAL adminMode being active, so code inside it does not need to manage the adminMode on its own.  
  
###  Web Services and Connectors

!!!info
    All external authenticated services **must** make use of `webServiceAuthenticate` authentication. Authorized **Connectors** can use `connectorAuthenticate`.  
  
Web Service authentication invokes `webServiceAuthenticate` and connectors invoke `connectorAuthenticate`, both of them call `doWebServiceAuthenticate`. This method is implemented to do standard authentication, it first looks whether user **l** and password **p** are sent as request parameters, if not basic authentication is performed. `doWebServiceAuthenticate` method can be implemented by authentication managers in case different authentication is needed.

`webServiceAuthenticate` and `connectorAuthenticate` are overloaded to accept both `HttpServletRequest` parameter (default one) or `String, String` parameters. This second one should be used by other services where the default one is not suitable, this one receives user and password parameters.


---

This work is a derivative of [Authentication](http://wiki.openbravo.com/wiki/Authentication){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 