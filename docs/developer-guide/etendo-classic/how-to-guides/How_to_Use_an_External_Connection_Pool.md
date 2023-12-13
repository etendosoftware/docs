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

  

#  How to Use an External Connection Pool

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
use of external connection pools is available from **3.0PR14Q2**  
---|---  
  
##  Introduction

By default Openbravo uses two connection pools:

  * Hibernate default connection pool for DAL-related queries 
  * Apache DBCP  for the connections provided by the ConnectionProviderImpl. 

From 3.0MP32 it is possible to specify an external connection provider that
Openbravo will use to obtain the JDBC connections. For that, a module
containing a subclass of ExternalConnectionPool needs to be installed, and the
db.externalPoolClassName property has to be set in Openbravo.properties.

##  Example: Using the Apache JDBC Connection Pool

The  Apache JDBC Connection Pool  Openbravo modules provides an implementation
of the Apache JDBC Connection Pool.

Once the module has been installed, the db.externalPoolClassName property has
to be set in Openbravo.properties. This module implements the external
connection pool class in the
org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool class, so
this line should be added to Openbravo.properties:

**db.externalPoolClassName=org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool**

This module contains a configuration file template:
modules/org.openbravo.apachejdbcconnectionpool/config/connectionPool.properties.template.
In order to customize the JDBC connection pool properties this file has to be
copied to
modules/org.openbravo.apachejdbcconnectionpool/config/connectionPool.properties.
The user can then configure the pool properties according to his needs. Hints
about how to configure this properties can be found  here  .

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_Use_an_External_Connection_Pool  "

This page has been accessed 6,905 times. This page was last modified on 6 May
2014, at 06:03. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

