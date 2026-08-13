---
title: How to Diagnose Idle in Transaction Connections
tags:
  - Connection Pool
  - Troubleshooting
  - Database
  - PostgreSQL
  - Hibernate
  - DAL
status: beta
---

# How to Diagnose Idle in Transaction Connections

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

## Overview

Etendo serves most requests through `DalFilter`, which opens a Hibernate/DAL session at the start of the request and closes it once the response is sent. Custom servlets, processes, or webservice endpoints that call `OBDal.getInstance()` or open a `SessionHandler` session outside that lifecycle are responsible for closing the session themselves.

A session that is never closed keeps its underlying JDBC connection checked out of the pool with an open transaction. PostgreSQL reports that connection as `idle in transaction`. Left unbounded, this blocks autovacuum on the tables the transaction touched, causes table bloat, and degrades database performance over time. Restarting Tomcat clears the pool and hides the symptom temporarily, which is why the underlying leak can go unnoticed for a while.

## Detecting the Problem

Query PostgreSQL for connections stuck in this state:

```sql
SELECT pid, now() - query_start AS duration, state, LEFT(query, 80) AS query_snippet
FROM pg_stat_activity
WHERE state = 'idle in transaction';
```

A growing number of rows that never clears until Tomcat restarts indicates a session that is not being closed somewhere in the request path.

## Finding the Leak

Review custom code paths that open a DAL or Hibernate session directly instead of relying on `DalFilter`. This is common in servlets that extend `HttpServlet` or `HttpBaseServlet` directly, bypassing the standard filter chain. Each of these paths must close its session explicitly in a `finally` block:

```java
try {
  // ... request processing that uses OBDal.getInstance() ...
} finally {
  OBDal.getInstance().commitAndClose();
}
```

Or, when using `SessionHandler` directly:

```java
try {
  // ... request processing ...
} finally {
  SessionHandler.getInstance().commitAndClose();
}
```

To confirm which code path is responsible before changing anything, enable abandoned-connection logging. This logs the stack trace of where a connection was borrowed once it has been checked out longer than expected, without closing anything:

```properties title="gradle.properties"
db.pool.logAbandoned=true
db.pool.suspectTimeout=<seconds>
```

Apply the change with:

```bash
./gradlew setup
```

!!! warning
    Logging abandoned connections adds overhead to every connection borrow, because a stack trace has to be generated. Use it to diagnose the leak, then disable it once the responsible code path is identified.

## Mitigating at the Pool Level

While the code fix is developed and rolled out, the connection pool can be configured to forcibly reclaim connections that have been checked out too long. Add the following properties to `gradle.properties`:

```properties title="gradle.properties"
db.pool.removeAbandoned=true
db.pool.removeAbandonedTimeout=<seconds>
```

Then apply the change:

```bash
./gradlew setup
```

See [How to Use an External Connection Pool](how-to-use-an-external-connection-pool.md#pool-configuration) for the full reference of pool configuration properties.

!!! warning
    Set `removeAbandonedTimeout` well above the longest legitimate transaction or background process duration in the environment. Any operation still running past that timeout has its connection reclaimed while in use, which corrupts that operation. This setting is a temporary safety net, not a substitute for closing the session in code.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
