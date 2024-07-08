---
tags: 
  - connection pool
  - DAL
  - Etendo Classic
---

#  How to Create an External Connection Pool

##  Overview

Etendo uses connection pools to reuse existing connections/prepared statements, avoiding the cost of initiating a connection, parsing SQL etc. By default, Etendo uses two different connection pools:

  * Hibernate default connection pool for DAL-related queries 
  * [Apache DBCP](https://commons.apache.org/proper/commons-dbcp/){target="\_blank"} for the connections provided by the `ConnectionProviderImpl`. 

It is possible to specify an external connection provider to replace these two connection pools. Etendo provides a free commercial module that implements the Tomcat JDBC Connection Pool, but it is possible for developers to publish a module to implement their own connection pool.

##  ExternalConnectionPool Abstract Class

In order to implement an external connection pool, developers must subclass the `ExternalConnectionPool` abstract class. This class has three methods:

    
    
    /**
       * 
       * @param externalConnectionPoolClassName
       *          The full class name of the external connection pool
       * @return An instance of the external connection pool
       */
    public final synchronized static ExternalConnectionPool getInstance(
          String externalConnectionPoolClassName) throws InstantiationException,
          IllegalAccessException, ClassNotFoundException;

The `getInstance` method is in charge of instantiating the external connection pool. The name of the class that implements the connection pool is passed as a parameter, its value is taken from the `db.externalPoolClassName` property of `Etendo.properties`.

    
    
    /**
       * @return A Connection from the external connection pool
       */
    public abstract Connection getConnection()

This is the main method that should be overwritten by all external connection providers. It takes no arguments, and it should return a connection that has been borrowed from the pool.

    
    
    /**
       * If the external connection pool supports interceptors this method should be overwritten
       * 
       * @param interceptors
       *          List of PoolInterceptorProvider comprised of all the interceptors injected with Weld
       */
    public void loadInterceptors(List<PoolInterceptorProvider> interceptors)

This method should be overwritten if the connection pool supports interceptors and allows custom interceptors to be instantiated using dependency injection. A list of `PoolInterceptorProvider` will be passed as arguments, containing the full class name of the interceptors.

##  Design Considerations

  * Include a configuration file so that users can customize the external connection pool to meet their needs. 
  * If the pool needs to execute some initialization code, place it in the `getConnection` method and make sure that is only executed the first time that method is invoked. 
  * For all connections returned by the pool: 
    * `SessionInfo.setDBSessionInfo`(Connection conn, String rdbms) must be executed 
    * The SQL query included in the `bbdd.sessionConfig` property must be executed using that connection. 
  * Take into account that these two operations must be executed on the returned connection only when the connection is actually created, not every time it is returned from the pool. 

---

This work is a derivative of [How to Create an External Connection Pool](http://wiki.openbravo.com/wiki/How_to_Create_an_External_Connection_Pool){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.