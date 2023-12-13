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

  

#  How To Enable Customization Of The Login Page

**Languages:** |

** English  ** |  Translate this article...  
  
---|---  
  
##  Contents

  * 1  Objective 
  * 2  Recommended Articles 
  * 3  Execution Steps 
    * 3.1  Installing Required Module 
    * 3.2  Configuring the Environment 

  
---  
  
##  Objective

The objective of this article it to provide the necessary steps to enable
customization of the Openbravo login page.

##  Recommended Articles

Please read this article about  Authentication  in Openbravo ERP. It explains
the the way the authentication and the authentication manager work and how
they are being configured.

##  Execution Steps

A couple of modiffications are necessary to change the look of the login page.
To start off with a base we will be working on, we will be using the
**Openbravo 3 Demo Login Page** module.

###  Installing Required Module

  * Log in as System Adminisrator 
  * Go to General Setup -> Application -> Module Management -> Add Modules 
  * Search and install the following module: 
    * **Openbravo 3 Demo Login Page**

###  Configuring the Environment

As already mentioned, a few more steps are needed:

  * **In openbravo.properties:**

    
    
    authentication.class=org.openbravo.demo.loginpage.authentication.DemoAuthenticationManager
    

  * **In modules/org.openbravo.demo.loginpage/src/org/openbravo/demo/loginpage/security:**

    
    
    Exchange the revision number _**"revisionControl('14275')"**_ with the number set in the **getCurrentRevision()** method in utils.js
    

Once done, you will see that the login page has changed. You can use this
module as the base for your development and customize the **Login.html** as
you want.

Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Enable_Customization_Of_The_Login_Page
"

This page has been accessed 10,067 times. This page was last modified on 22
May 2013, at 08:22. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

