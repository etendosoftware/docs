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

  

#  How to Create an External Connection Pool

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
use of external connection pools is available from **3.0MP32**  
---|---  
  
##  Introduction

Openbravo uses connection pools to reuse existing connections/prepared
statements, avoiding the cost of initiating a connection, parsing SQL etc. By
default Openbravo uses two different connection pools:

  * Hibernate default connection pool for DAL-related queries 
  * Apache DBCP  for the connections provided by the ConnectionProviderImpl. 

From 3.0MP32 it is possible to specify an external connection provider to
replace these two connection pools. Openbravo provides a free commercial
module that implements the Tomcat JDBC Connection Pool, but it is possible for
developers to publish a module implement their own connection pool.

##  ExternalConnectionPool abstract class

In order to implement an external connection pool, developers must subclass
the ExternalConnectionPool abstract class. This class has three methods:

    
    
    /**
       * 
       * @param externalConnectionPoolClassName
       *          The full class name of the external connection pool
       * @return An instance of the external connection pool
       */
    public final synchronized static ExternalConnectionPool getInstance(
          String externalConnectionPoolClassName) throws InstantiationException,
          IllegalAccessException, ClassNotFoundException;

The getInstance method is in charge of instantiating the external connection
pool. The name of the class that implements the connection pool is passed as a
parameter, its value is taken from the **db.externalPoolClassName** property
of Openbravo.properties.

    
    
    /**
       * @return A Connection from the external connection pool
       */
    public abstract Connection getConnection()

This is the main method that should be overwritten by all external connection
providers. It takes no arguments, and it should return a connection that has
been borrowed from the pool.

    
    
    /**
       * If the external connection pool supports interceptors this method should be overwritten
       * 
       * @param interceptors
       *          List of PoolInterceptorProvider comprised of all the interceptors injected with Weld
       */
    public void loadInterceptors(List<PoolInterceptorProvider> interceptors)

This method should be overwritten if the connection pool supports interceptors
and allows custom interceptors to be instantiated using dependency injection.
A list of PoolInterceptorProvider will be passed as an arguments, containing
the full class name of the interceptors.

##  Design Considerations

  * Include a configuration file so that users can customize the external connection pool to meet their needs. 
  * If the pool needs to execute some initialization code, place it in the getConnection method and make sure that is only executed the first time that method is invoked. 
  * For all connection returned by the pool: 
    * SessionInfo.setDBSessionInfo(Connection conn, String rdbms) must be executed 
    * The sql query included in the **bbdd.sessionConfig** property must be executed using that connection. 
  * Take into account that these two operations must be executed on the returned connection only when the connection is actually created, not every time it is returned from the pool. 

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_Create_an_External_Connection_Pool  "

This page has been accessed 5,823 times. This page was last modified on 14
February 2014, at 15:40. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

