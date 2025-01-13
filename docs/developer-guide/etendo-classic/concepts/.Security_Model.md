---
search:
  exclude: true
---

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

  

#  Security Model

##  Contents

  * 1  Introduction 
  * 2  Openbravo Security Concepts 
  * 3  Security concepts and Openbravo Servlets 
  * 4  Security concepts and XSQL and Manual Code 
  * 5  Security concepts and the Data Access Layer 
  * 6  Application Administrators 
    * 6.1  Upgrading from previous MPs 
    * 6.2  Roles created by the Initial Client and Organization setup 
  * 7  CSRF Protection 

  
---  
  
##  Introduction

This section discusses how different Openbravo security concepts influence
development in Openbravo.

Openbravo's security concept consists of three main parts:

  * Multi-Client/Multi-organization: defines which client/organizations are visible to a user and referenceable from other client/organizations. 
  * Data access level (of a table): defines the client/organization which is allowed for data stored in a specific table. See the  access level  field of AD_Table. 
  * Access definition: Openbravo has several access definitions, allowing for fine-grained access control, see the tables in the  org.openbravo.model.ad.access  package. 

This section will discuss security and access definitions from the perspective
of a developer. Where necessary references to functional documentation is
used.

The developer can work in two modes in Openbravo: 1) traditional: using sqlc
etc., 2) data access layer: using the new data access layer. Both approaches
are discussed separately.

##  Openbravo Security Concepts

The following functional documents give a good introduction in Openbravo
security concepts:

  * Security Setup 
  * Security Multi-Organization 
  * How to define user, roles, privileges and menus 
  * Configuration Manual, configuring roles and users 

##  Security concepts and Openbravo Servlets

The tables in the  org.openbravo.model.ad.access  package define access
control for windows/tabs, processes, workflow etc.

The security checks using this table are implemented by the
HttpSecureAppServlet  servlet. Any servlet extending this class will
automatically inherit this security implementation.

##  Security concepts and XSQL and Manual Code

Openbravo provides a standard way to extend sql queries with filters for
accessible clients and organizations. This is discussed in detail in this
section of the developers guide:

  * XSQL Definition 
  * XSQL Java Usage 

##  Security concepts and the Data Access Layer

For the developer the  Data Access Layer  provides several interfaces (
OBCriteria  and  OBQuery  ) that take automatic care of specific security
aspects:

  * filter for readable clients/organizations 
  * filter for readable tables (based on  AD_Window_Access  ) 

In addition checks are done when retrieving a value of a property. The data
access layer makes a distinction between the following two read-modes (on
object level):

  * direct readable: all properties of the object are readable, this readability is defined by the  AD_Window_Access  table 
  * derived readable: only the id and identifier properties are readable, derived readable entities are the entities which are not directly readable but are refered to by directly readable entities. 

The DAL also checks write access when changing properties of a business
object. Write access is also checked when an object is saved to the database.
The following checks are done:

  * the user has write access to the client/organization 
  * the user has write access to the table of the object (defined in the  AD_Window_Access  table) 
  * the client/organization of the object fit to the  access level  of the table 
  * the object only refers to other objects which are in the natural tree of organizations of the object itself 

The data access layer also performs specific authorization checks when an
object is deleted: the user must have access to the object and it must be
deletable  .

For much more information on how the Data Access Layer implements security see
this link  .

For more information on the Data Access Layer and multi-client/multi-
organization see  this link  .

##  Application Administrators

There is an administrator flag on the _Role_ window that enables users to make
configurations at different levels depending on their role.

There are 4 different levels on Openbravo:

**System level**

     There is no flag for _System_ level. 
     Users logged as _System Administrator_ are able to configure settings at _System_ level. 
     These settings will be available to everyone. 
**Client level**

     There is a new _Client Administrator_ flag on the _Role_ tab. 
     Users are able to configure settings at Client level if the logged role has the flag enabled. 
     These settings are available to all the users on the role's client. 
**Organization level**

     There is a new _Organization Administrator_ flag on the _Org Access_ tab. 
     Users are able to configure settings at Organization level on all the organizations of the logged role that have the flag enabled. 
     These settings are available to all the users logged on that Organization. 
**Role level**

     There is a new _Role Administrator_ flag on the _User Assignement_ tab. 
     Users are able to configure setting at _Role_ level on all the roles it is assigned to with the flag enabled. 
     These settings are available to all the users logged with that role. 

###  Upgrading from previous MPs

When a role is created manually all the flags are set to false by default.
There is a module script defined to set as true the flags based on the
following rules:

**Client Administrator**

     All roles with access to _*_ organization and to the _Initial Organization Setup_ form. 
**Organization Administrator**

     All the assigned organizations of a role with access to the _Initial Organization Setup_ form. 
**Role Administrator**

     All the roles assigned to a user if at least one of the roles has access to the _Role_ window. 

Notice that this module script only populates the flags the first time these
flags are added. On the following core updates the flags won't be updated and
the configuration has to be done manually.

###  Roles created by the Initial Client and Organization setup

The _Initial Client and Organization setup_ forms automatically create some
users and roles. These ones have the flag initialized to true.

**Initial Client Setup**

     The role created has the _Client Administrator_ flag set to true. 
     The user created has the new role assigned with the _Role Administrator_ set to true. 

**Initial Organization Setup**

     The role and the organization created has the _Organization Administrator_ flag set to true. 
     The user created has the new role assigned with the _Role Administrator_ set to true. 

##  CSRF Protection

Openbravo is protected against CSRF (Cross-Site Request Forgery) attacks, both
in the backoffice and in the POS.

For a more detailed discussion about this attack and how this protection is
implemented see  this page  .

Retrieved from "  http://wiki.openbravo.com/wiki/Security_Model  "

This page has been accessed 5,911 times. This page was last modified on 19
October 2018, at 08:19. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

