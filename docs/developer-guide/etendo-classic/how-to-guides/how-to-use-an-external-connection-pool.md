---
title: How to Use an External Connection Pool
tags: 
    - Use
    - External
    - Connection
    - Pool 
    - Howto

status: beta
---

# How to Use an External Connection Pool

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

## Overview

By default, Etendo uses two connection pools:

- Hibernate default connection pool for DAL-related queries 
- [Apache DBCP](https://commons.apache.org/proper/commons-dbcp/){target="\_blank"} for the connections provided by the `ConnectionProviderImpl`. 

!!!info
    It is possible to specify an external connection provider that Etendo will use to obtain the *JDBC connections*. For that, a module containing a subclass of `ExternalConnectionPool` needs to be installed, and the `db.externalPoolClassName` property has to be set in `gradle.properties` file.

## Example: Using the Apache JDBC Connection Pool

The [Apache JDBC Connection Pool](https://github.com/etendosoftware/etendo_core/tree/main/modules_core/org.openbravo.apachejdbcconnectionpool){target="\_blank"} module core provides an implementation of the Apache JDBC Connection Pool.

The `db.externalPoolClassName` property has to be set in `gradle.properties`. This module implements the external connection pool class in the `org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool` class, so this line should be added to `gralde.properties`:

``` title="Gradle.properties"
db.externalPoolClassName=org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool
```

This module contains a configuration file template: `modules_core/org.openbravo.apachejdbcconnectionpool/config/connectionPool.properties.template`. In order to customize the JDBC connection pool properties this file has to be copied to `modules_core/org.openbravo.apachejdbcconnectionpool/config/connectionPool.properties`. The user can then configure the pool properties according to his needs. Hints about how to configure this properties can be found [here](https://tomcat.apache.org/){target="\_blank"}.

---
This work is a derivative of [How to Use an External Connection Pool](http://wiki.openbravo.com/wiki/How_to_Use_an_External_Connection_Pool){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.