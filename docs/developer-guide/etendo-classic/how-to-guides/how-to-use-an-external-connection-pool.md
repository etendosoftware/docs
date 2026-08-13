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

Etendo ships with the [Apache JDBC Connection Pool](https://github.com/etendosoftware/etendo_core/tree/main/modules_core/org.openbravo.apachejdbcconnectionpool){target="\_blank"} enabled by default, through the `org.openbravo.apachejdbcconnectionpool` core module. This module implements Etendo's `ExternalConnectionPool` abstraction on top of the [Apache Tomcat JDBC Connection Pool](https://tomcat.apache.org/tomcat-9.0-doc/jdbc-pool.html){target="\_blank"}. No installation step is required: `Openbravo.properties` already sets

```properties title="Openbravo.properties"
db.externalPoolClassName=org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool
```

Because the pool is already active on every installation, the work described on this page is tuning its properties — see [Pool Configuration](#pool-configuration) below. Changing `db.externalPoolClassName` to a different class only becomes necessary to plug in a **custom** external connection pool implementation instead of the bundled one; see [How to Create an External Connection Pool](how-to-create-an-external-connection-pool.md) for that scenario.

Pool properties are set in `gradle.properties`. After adding or changing any of them, apply the change with:

```bash
./gradlew setup
```

This regenerates `Openbravo.properties`, which `JdbcExternalConnectionPool` reads at runtime to build the pool.

## Pool Configuration

A fresh Etendo installation ships with the following properties already set:

```properties title="Openbravo.properties (generated)"
db.pool.initialSize=1
db.pool.minIdle=5
db.pool.maxActive=10000
db.pool.timeBetweenEvictionRunsMillis=60000
db.pool.minEvictableIdleTimeMillis=120000
db.pool.removeAbandoned=false
db.pool.testOnBorrow=true
db.pool.testWhileIdle=false
db.pool.testOnReturn=false
db.pool.validationQuery=SELECT 1 FROM DUAL
db.pool.validationInterval=30000
db.pool.jmxEnabled=false
```

Override any of them by setting the corresponding property in `gradle.properties`:

| Property | Description | Default |
| --- | --- | --- |
| `db.pool.initialSize` | Connections established when the pool starts. Lowered automatically if it exceeds `db.pool.maxActive`. | `1` |
| `db.pool.minIdle` | Minimum established connections kept in the pool at all times. The idle pool does not shrink below this value during an eviction run, but it can still drop lower if `db.pool.validationQuery` fails and connections are closed. | `5` |
| `db.pool.maxActive` | Maximum active connections the pool can hand out at the same time. Kept high by default because capacity planning is delegated to the database; it should be at least as high as the database's own maximum connections. If lowered below that, `db.pool.maxWait` becomes relevant. | `10000` |
| `db.pool.timeBetweenEvictionRunsMillis` | How often (ms) the sweeper thread checks idle and abandoned connections. See [How does the sweeper thread work?](#how-does-the-sweeper-thread-work). Should not be set below `1000`. | `60000` |
| `db.pool.minEvictableIdleTimeMillis` | Minimum time (ms) a connection may sit idle before the sweeper evicts it. | `120000` |
| `db.pool.removeAbandoned` | If `true`, connections held longer than `db.pool.removeAbandonedTimeout` are forcibly reclaimed. | `false` |
| `db.pool.testOnBorrow` | Validates a connection before handing it out; drops and retries if invalid. Requires `db.pool.validationQuery` to be set. | `true` |
| `db.pool.testOnReturn` | Validates a connection when it is returned to the pool. | `false` |
| `db.pool.testWhileIdle` | Validates idle connections periodically. | `false` |
| `db.pool.validationQuery` | SQL used to validate a connection. Must not throw an exception. Required for `testOnBorrow`, `testOnReturn`, and `testWhileIdle` to have any effect. Etendo's database creation scripts provision a `DUAL` compatibility table on PostgreSQL installations, so this query runs unmodified on both PostgreSQL and Oracle. | `SELECT 1 FROM DUAL` |
| `db.pool.validationInterval` | Minimum milliseconds between validations of the same connection, to avoid redundant checks. | `30000` |
| `db.pool.jmxEnabled` | Exposes pool metrics through JMX. | `false` |

The pool also supports the properties below. Etendo does not set a default for any of them — when a property is not set in `gradle.properties`, the underlying [Apache Tomcat JDBC Connection Pool](https://tomcat.apache.org/tomcat-9.0-doc/jdbc-pool.html#Common_Attributes){target="\_blank"} default applies instead:

| Property | Description |
| --- | --- |
| `db.pool.maxIdle` | Maximum idle connections kept in the pool when the sweeper is disabled. |
| `db.pool.maxWait` | Milliseconds the pool waits for a connection to be returned before throwing an exception, once `db.pool.maxActive` has been reached. |
| `db.pool.numTestsPerEvictionRun` | Number of connections examined in each sweeper run. |
| `db.pool.removeAbandonedTimeout` | Seconds a connection can be checked out before it is considered abandoned. Only relevant when `db.pool.removeAbandoned=true`. |
| `db.pool.testOnConnect` | Validates a connection right after it is physically created. |
| `db.pool.validatorClassName` | Custom validator class used instead of `db.pool.validationQuery`. |
| `db.pool.initSQL` | SQL executed once, right after a physical connection is created. |
| `db.pool.defaultAutoCommit` | Default auto-commit state of connections returned by the pool. |
| `db.pool.defaultReadOnly` | Default read-only state of connections returned by the pool. |
| `db.pool.defaultTransactionIsolation` | Default transaction isolation level of connections returned by the pool. |
| `db.pool.defaultCatalog` | Default catalog of connections returned by the pool. |
| `db.pool.connectionProperties` | Extra driver-specific connection properties, as a semicolon-separated list of `name=value` pairs. |
| `db.pool.accessToUnderlyingConnectionAllowed` | Allows retrieving the underlying physical connection through the pooled connection wrapper. |
| `db.pool.logAbandoned` | Logs the stack trace of where a connection was borrowed once it has been checked out longer than `db.pool.suspectTimeout`. Adds overhead to every borrow, since a stack trace has to be generated. |
| `db.pool.suspectTimeout` | Seconds a connection can be checked out before it is logged as suspect. Only relevant when `db.pool.logAbandoned=true`. Independent from `db.pool.removeAbandoned` — a suspect connection is only logged, not reclaimed. |
| `db.pool.name` | Name assigned to the pool, useful to tell pools apart when several are configured. |

!!!info
    Any of these properties can be scoped to a specific named pool — for example the read-only pool — by inserting the pool name after `db.`, e.g. `db.readonly.pool.maxActive`. A pool-specific value takes precedence over the default `db.pool.*` value for that pool; a pool that does not define its own value falls back to the default.

### How does the sweeper thread work?

The sweeper is the background thread that runs every `db.pool.timeBetweenEvictionRunsMillis` milliseconds to validate idle connections and check for abandoned ones. Whether it is enabled changes how the idle pool behaves:

- **Sweeper disabled**: if the idle pool grows larger than `db.pool.maxIdle`, a connection is closed as soon as it is returned to the pool instead of being kept idle.
- **Sweeper enabled**: the number of idle connections can grow beyond `db.pool.maxIdle`, but shrinks back down to `db.pool.minIdle` once a connection has been idle longer than `db.pool.minEvictableIdleTimeMillis`.

The full list of configurable Tomcat JDBC Connection Pool attributes is available in the [Apache Tomcat documentation](https://tomcat.apache.org/tomcat-9.0-doc/jdbc-pool.html#Common_Attributes){target="\_blank"}, along with [guidance on tuning the pool for high-concurrency environments](https://www.tomcatexpert.com/blog/2010/04/01/configuring-jdbc-pool-high-concurrency){target="\_blank"}.

---
This work is a derivative of [How to Use an External Connection Pool](http://wiki.openbravo.com/wiki/How_to_Use_an_External_Connection_Pool){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
