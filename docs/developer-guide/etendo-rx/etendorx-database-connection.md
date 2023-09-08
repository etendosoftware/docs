---
title: EtendoRX database connection
---
## EtendoRX database connection

When the user needs to deploy EtendoRX on production or there is the need to test on special environments, a wide range of parameters are available to tweak db connections for specific needs. 

### Basic usage



To configure the connection to the database with the [default configuration method](https://en/technical-documentation/etendo-environment/platform/etendorx-config-server) in EtendoRX, it is neccesary to modify the parameters specified in the files as follow: 


#### PostgreSQL database

In gradle.properties file:

```
bbdd.rdbms=POSTGRE
bbdd.driver=org.postgresql.Driver
bbdd.url=jdbc:postgresql://localhost\:5432
bbdd.sid=etendo
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
bbdd.user=tad
bbdd.password=tad
bbdd.sessionConfig=select update_dateFormat('DD-MM-YYYY')
```

In the path /rxconfig, edit das.yaml file:

```
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/etendo
    username: tad
    password: tad
```

#### Oracle database

In gradle.properties file:

```
bbdd.rdbms=ORACLE
bbdd.driver=oracle.jdbc.driver.OracleDriver
bbdd.url=jdbc:oracle:thin:@localhost\:1521\:orclsid
bbdd.sid=orclsid
bbdd.systemUser=sys as sysdba
bbdd.systemPassword=oraclepassword
bbdd.user=C\#\#TAD
bbdd.password=tad
bbdd.sessionConfig=ALTER SESSION SET NLS_DATE_FORMAT='DD-MM-YYYY' NLS_NUMERIC_CHARACTERS='.,'
```

In the path /rxconfig, edit das.yaml file:

```
spring:
  datasource:
    url: jdbc:oracle:thin:@//localhost:1521/orclsid
    username: C##TAD
    password: tad
    driver-class-name: oracle.jdbc.OracleDriver
```

### Advanced configuration

#### Datasource

By default and as recommended, use [HakiriCP](https://github.com/brettwooldridge/HikariCP) as a database connection library in EtendoRX.

> There are several benchmark results available to compare the performance of HikariCP with other connection pooling frameworks, such as c3p0, dbcp2, tomcat, and vibur. For example, the HikariCP team published the below benchmarks:
> 
> HikariCP-bench-2.6.0
> The framework is so fast because the following techniques have been applied:
> 
> Bytecode-level engineering – some extreme bytecode level engineering (including assembly level native coding) has been done
> Micro-optimizations – although barely measurable, these optimizations combined boost the overall performance
> Intelligent use of the Collections framework – the ArrayList<Statement> was replaced with a custom class, FastList, that eliminates range checking and performs removal scans from head to tail
>
!!! info
     Source: https://www.baeldung.com/hikaricp

Connection tweaking can be made by changing the available parameters:

https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#application-properties.data.spring.datasource.hikari

#### Verbose logging
  
If more verbose log output is needed, add to das.yaml file:

```
spring:
  jpa:
    show-sql: true
    properties:
      hibernate:
        format_sql: true
  
logging:
  level:
    org:
      hibernate:
        type:
          descriptor: ## Shows each hibernate SQL query
            sql: WARN

```

This configuration will make log more verbose to easy troubleshoot.
  
  
  
  
