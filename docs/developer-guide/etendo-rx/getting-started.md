---
title: Developer Guide - Etendo RX - Getting Started
---

## Overview

This guide will help you set up Etendo, including both the Etendo Classic functionalities and Etendo RX, our reactive platform capable of executing microservices with database interaction and asynchronous actions.

## Requirements

1. Install Etendo Classic. For this, follow the [Etendo Classic installation guide](../../getting-started/installation.md).
2. Install the [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}.
3. This project depends on the following tools:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: version `26.0.0` or higher.
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: version `2.26.0` or higher.


## Dockerized Services

In the platform bundle, you can find the Dockerized Services module, which provides the necessary architecture to distribute infrastructure. In this case, in this bundle, the module Etendo RX is also included and, to launch the Services distributed in it, a certain configuration is needed. In the `gradle.properties` file, add the following variable:

``` groovy title="gradle.properties"
docker_com.etendoerp.etendorx=true
```

!!!info
    For more information about how to handle Etendo Dockerizations, visit [Docker Management](../etendo-classic/bundles/platform/docker-management.md). 

??? Note "Tomcat and PostgresSQL Dockerized (Optional)"
    It is also possible to run the dockerized [PostgreSQL service](../platform/docker-management.md#postgres-database-service) and [Tomcat service](../platform/tomcat-dockerized-service.md), **optionally** adding the [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank} and the following configuration variables:

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    docker_com.etendoerp.docker_db=true
    ```

    If you want to debug Tomcat locally with IntelliJ, visit [Tomcat Dockerized Service](../../developer-guide/etendo-classic/bundles/platform/tomcat-dockerized-service.md).


###  Etendo RX Configurations

Before starting the dockerized services, there are some configurations that need to be done in Etendo Classic

### Client Setup 
:material-menu: `Application` > `General Setup` > `Client` > `Client`

It is necessary to configure the encryption token for the authentication in the `Client` window with the `System Administrator` role.
If the expiration time is equal to `0` the tokens do not expire.

Generate a random key with the **Generate key** button.

![](../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)


### RX Config window
:material-menu: `Application` > `Etendo RX` > `RX Config`

This configuration window stores the access data for Etendo RX services, which are crucial for the interaction between different services. As `System Administrator` role, in this window, run the `Initialize RX Services` process in the toolbar. 

![](../../assets/developer-guide/etendo-rx/getting-started/initialize-rx-service.png)

After the execution of this process the default configuration variables are completed, depending on the configuration of the instance and the infrastructure, even the default parameters required by each service are configured.

![default-rx-config.png](../../assets/developer-guide/etendo-rx/getting-started/default-rx-config.png)

!!!info
    The **Public URL** field only needs to be configured when the services is set to production.


### Launch RX services

Then, to effectively run the services, it is necessary to **execute the command** in the terminal: 

```bash title="Terminal"
./gradlew resources.up
```

Here, all the services and their respective logs can be seen running using [lazydocker](https://github.com/jesseduffield/lazydocker#installation){target="_blank"} or [Docker Desktop](https://www.docker.com/products/docker-desktop/){target="_blank"} for a simple and fast container management. 

![Docker Services](../../assets/developer-guide/etendo-rx/getting-started/rx-services.png)

By default, the following services should be up and running:

- Config
- Auth
- Edge
- Das

!!! success
    You have successfully set up the Etendo RX services. For more information, visit [Projections and Mappings](./concepts/projections.md) and [Creating a New Microservice](../../developer-guide/etendo-rx/tutorials/creating-a-new-microservice.md) page in the developer guide section.

Currently, the bulk of Etendo RX services rely on Docker images named dynamic‑das and dynamic‑gradle, which underpin microservice execution. Dynamic‑das is dedicated solely to running the Das microservice and dynamic‑gradle, by contrast, can launch multiple microservices—such as Config, Edge, Auth, AsyncProcess, ObConnSrv, Worker, and others.

### Dynamic DAS v1.1.0

#### Stack

- **Image base:** `amazoncorretto:17.0.14-alpine3.21` ([link](https://github.com/corretto/corretto-docker/tree/main/17/jdk/alpine/3.21))
- **JDK Version:** 17.0.14
- **Gradle Version:** 8.12.1
- **OpenTelemetry Version:** v2.18.1 ([release](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/tag/v2.18.1))  
- **Package manager:** `apk` (Alpine Package Keeper)
- **Additional tools installed:** `wget`, `unzip`

---

#### Ports

| Port   | Description               |
|--------|---------------------------|
| `5021` | DAS service port          |
| `8092` | Remote debug port         |

---

#### Environment Variables

| Name                                                        | Description                                                                                              | Type     | Allowed Values                                                      | Default                                      | Notes                                                                                                                                                        |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DEPENDENCIES`                                              | Maven GAV coordinates for dynamic dependencies                                                           | string   | Comma-separated list                                                | *null*                                       | —                                                                                                                                                            |
| `REPO_URL`                                                  | Maven repository URL                                                                                     | URL      | Any valid URL                                                       | `https://repo.maven.apache.org/maven2/`     | —                                                                                                                                                            |
| `REPO_USER`                                                 | Username for Maven repository                                                                            | string   | —                                                                   | *null*                                       | —                                                                                                                                                            |
| `REPO_PASSWORD`                                             | Password for Maven repository                                                                            | string   | —                                                                   | *null*                                       | —                                                                                                                                                            |
| `CONFIG_SERVER_URL`                                         | Spring Cloud Config Server URL                                                                           | URL      | Any valid URL                                                       | `http://localhost:8888`                     | —                                                                                                                                                            |
| `TASK`                                                      | Task to execute                                                                                          | enum     | `downloadJar`, `run`                                                | `downloadJar`                                | —                                                                                                                                                            |
| `DB_HOST`                                                   | Hostname for the database                                                                                | string   | —                                                                   | `db`                                         | —                                                                                                                                                            |
| `DB_PORT`                                                   | Port for the database connection                                                                         | integer  | Any valid port                                                      | `5432`                                       | —                                                                                                                                                            |
| `DB_SID`                                                    | Database SID                                                                                             | string   | —                                                                   | `etendo`                                     | —                                                                                                                                                            |
| `DEBUG_PORT`                                                | Remote debug port                                                                                        | integer  | Any valid port                                                      | `5021`                                       | —                                                                                                                                                            |
| `ENABLE_OPEN_TELEMETRY`                                     | Enables OpenTelemetry instrumentation                                                                    | boolean  | `true`, `false`                                                     | `false`                                      | —                                                                                                                                                            |
| `OTEL_SERVICE_NAME`                                         | Service name for OpenTelemetry                                                                           | string   | Any string                                                          | `das`                                        | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_ENDPOINT`                               | Base OTLP endpoint URL                                                                                   | string   | Any URL                                                             | `http://jaeger:4318`                         | Automatically appends `/v1/traces\|metrics\|logs}` depending on the signal type                                                                             |
| `OTEL_EXPORTER_OTLP_PROTOCOL`                               | Transport protocol for OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
| `OTEL_METRICS_EXPORTER`                                     | Metrics exporter                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
| `OTEL_LOGS_EXPORTER`                                        | Logs exporter                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
| `OTEL_TRACES_EXPORTER`                                      | Traces exporter                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_TIMEOUT`                                | Timeout (ms) for OTLP data export (traces, metrics, logs)                                                | integer  | Any positive number                                                 | `10000`                                      | —                                                                                                                                                            |
| `SPRING_PROFILES_ACTIVE`                                    | Active Spring profiles                                                                                   | string   | Comma-separated list                                                | *null*                                       | Example: `prod,dev`                                                                                                                                         |
| `SPRING_CLOUD_CONFIG_SERVER_NATIVE_SEARCHLOCATIONS`         | Native search paths for Spring Config Server                                                             | string   | Comma-separated file paths                                          | *null*                                       | Example: `file:///config,classpath:/defaults`                                                                                                               |
| `DISABLE_DEBUG`                                             | Disable JVM debug agent                                                                                  | boolean  | `true`, `false`                                                     | `false`                                      | If `true`, adds `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:${DEBUG_PORT}`. `dt_socket`: The transport mechanism—i.e., a TCP socket—used for the debug connection. `server=y` tells the JVM to act as the debug server (waiting for a debugger to connect). `suspend=n` means “don’t pause at startup”—the app will run immediately, and you can attach the debugger at any time. (If you set suspend=y, the JVM will pause on the first line until a debugger attaches.)                                                                |
| `JAVA_OPTS`                                                 | Additional JVM options                                                                                   | string   | Any valid JVM option                                                | *null*                                       | Example: `-Dfile.encoding=UTF-8`                                                                                                                             |
| `GRADLE_FLAGS`                                              | Gradle command flags                                                                                     | string   | Any valid Gradle flags                                              | `-no-daemon --info --refresh-dependencies`   | —                                                                                                                                                            |

---

### Dynamic Gradle v1.1.0

#### Stack

- **Image base:** `amazoncorretto:17.0.14-alpine3.21` ([link](https://github.com/corretto/corretto-docker/tree/main/17/jdk/alpine/3.21))
- **JDK Version:** 17.0.14
- **Gradle Version:** 8.12.1
- **OpenTelemetry Version:** v2.18.1 ([release](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/tag/v2.18.1))  
- **Package manager:** `apk` (Alpine Package Keeper)
- **Additional tools installed:** `wget`, `unzip`

---

#### Ports

| Port   | Description                              |
|--------|------------------------------------------|
| `8888` | Config service port                      |
| `5020` | Config service remote debug port         |
| `8094` | Auth service port                        |
| `5022` | Auth service remote debug port           |
| `8096` | Edge service port                        |
| `5023` | Edge service remote debug port           |
| `8099` | Asyncprocess service port                |
| `5024` | Asyncprocess service remote debug port   |
| `8101` | Obconnsrv service port                   |
| `5025` | Obconnsrv service remote debug port      |
| `8102` | Worker service port                      |
| `5026` | Worker service remote debug port         |

---

#### Environment Variables

| Name                                                        | Description                                                                                              | Type     | Allowed Values                                                      | Default                                      | Notes                                                                                                                                                        |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DEPENDENCIES`                                              | Maven GAV coordinates for dynamic dependencies                                                           | string   | Comma-separated list                                                | *null*                                       | —                                                                                                                                                            |
| `REPO_URL`                                                  | Maven repository URL                                                                                     | URL      | Any valid URL                                                       | `https://repo.maven.apache.org/maven2/`     | —                                                                                                                                                            |
| `REPO_USER`                                                 | Username for Maven repository                                                                            | string   | —                                                                   | *null*                                       | —                                                                                                                                                            |
| `REPO_PASSWORD`                                             | Password for Maven repository                                                                            | string   | —                                                                   | *null*                                       | —                                                                                                                                                            |
| `CONFIG_SERVER_URL`                                         | Spring Cloud Config Server URL                                                                           | URL      | Any valid URL                                                       | `http://localhost:8888`                     | —                                                                                                                                                            |
| `TASK`                                                      | Task to execute                                                                                          | enum     | `downloadJar`, `run`                                                | `run`                                | —                                                                                                                                                            |
| `DEBUG_PORT`                                                | Remote debug port                                                                                        | integer  | Any valid port                                                      | `5005`                                       | —                                                                                                                                                            |
| `ENABLE_OPEN_TELEMETRY`                                     | Enables OpenTelemetry instrumentation                                                                    | boolean  | `true`, `false`                                                     | `false`                                      | —                                                                                                                                                            |
| `OTEL_SERVICE_NAME`                                         | Service name for OpenTelemetry                                                                           | string   | Any string                                                          | `dynamic-gradle`                                        | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_ENDPOINT`                               | Base OTLP endpoint URL                                                                                   | string   | Any URL                                                             | `http://jaeger:4318`                         | Automatically appends `/v1/traces\|metrics\|logs}` depending on the signal type                                                                             |
| `OTEL_EXPORTER_OTLP_PROTOCOL`                               | Transport protocol for OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
| `OTEL_METRICS_EXPORTER`                                     | Metrics exporter                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
| `OTEL_LOGS_EXPORTER`                                        | Logs exporter                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
| `OTEL_TRACES_EXPORTER`                                      | Traces exporter                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_TIMEOUT`                                | Timeout (ms) for OTLP data export (traces, metrics, logs)                                                | integer  | Any positive number                                                 | `10000`                                      | —                                                                                                                                                            |
| `SPRING_PROFILES_ACTIVE`                                    | Active Spring profiles                                                                                   | string   | Comma-separated list                                                | *null*                                       | Example: `prod,dev`                                                                                                                                         |
| `SPRING_CLOUD_CONFIG_SERVER_NATIVE_SEARCHLOCATIONS`         | Native search paths for Spring Config Server                                                             | string   | Comma-separated file paths                                          | *null*                                       | Example: `file:///config,classpath:/defaults`                                                                                                               |
| `DISABLE_DEBUG`                                             | Disable JVM debug agent                                                                                  | boolean  | `true`, `false`                                                     | `false`                                      | If `true`, adds `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:${DEBUG_PORT}`. `dt_socket`: The transport mechanism—i.e., a TCP socket—used for the debug connection. `server=y` tells the JVM to act as the debug server (waiting for a debugger to connect). `suspend=n` means “don’t pause at startup”—the app will run immediately, and you can attach the debugger at any time. (If you set suspend=y, the JVM will pause on the first line until a debugger attaches.)                                                                |
| `JAVA_OPTS`                                                 | Additional JVM options                                                                                   | string   | Any valid JVM option                                                | *null*                                       | Example: `-Dfile.encoding=UTF-8`                                                                                                                             |
| `GRADLE_FLAGS`                                              | Gradle command flags                                                                                     | string   | Any valid Gradle flags                                              | `-no-daemon --info --refresh-dependencies`   | —                                                                                                                                                            |

---
