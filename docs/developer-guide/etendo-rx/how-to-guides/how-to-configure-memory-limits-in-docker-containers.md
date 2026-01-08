---
title: How to Manage Memory Limits for Etendo Docker Containers
tags:
  - Etendo
  - Docker
  - Memory
  - Tomcat
  - CPU
  - Containers
---

# How to Manage Memory Limits for Etendo Docker Containers

!!! warning
    This guide assumes a working knowledge of **Java development environments**, including **Gradle build commands**, **Java application deployment**, and **Docker container management**. It is intended for developers with intermediate to advanced technical skills in software development and system administration.

## Overview

This guide explains how to configure memory and CPU limits for Etendo services running in Docker containers.
It introduces three configuration levels for both memory and CPU usage:

1. **Service Limits**: Direct values set per service in `gradle.properties` file.
2. **Base Service Limits**: A base value with predefined multipliers that adjust resources dynamically across services.
3. **Default Values**: Preconfigured minimums that ensure services can run when no limits are defined.

Each level has a defined precedence, with direct service limits overriding base limits, and base limits overriding defaults.
The document also provides detailed reference tables listing all available variables for Etendo services across different Docker Compose files.


## Memory Management
Etendo allows memory limits to be configured at three different levels.  
Each level takes precedence over the previous one:

1. **Service Memory Limit**  
   A direct limit can be set for each service in `gradle.properties`.  
   Example:  
   ```properties title="gradle.properties"
   <service>.memory.limit=512M
   ```  
   Values can be expressed in megabytes (`M`) or gigabytes (`G`). This configuration has the highest precedence.

2. **Base Service Memory Limit**  
    In this case, a base memory size (only in `MB`, integer value) is defined for all services. Each service in the Docker Compose configuration includes a predefined multiplier.  

    Example:  
    ```properties title="gradle.properties"
    <compose>.base.memory.mb=512
    ```  
    When executing:

    ```bash title="Terminal"
    ./gradlew resources.up
    ```  
    Gradle calculates the effective memory limit for each service using the base size multiplied by the service factor. These multipliers were determined based on prior performance analysis.

    ``` title=".env file generated"
        BASE_<SERVICE1>_MEMORY_LIMIT=512M
        BASE_<SERVICE2>_MEMORY_LIMIT=1024M
        BASE_<SERVICE3>_MEMORY_LIMIT=2048M 
    ```

    This approach is useful when system memory is limited, as it allows setting a minimum base size for each service while letting the multipliers adjust resource distribution according to service demand.

3. **Default Values**  
    If no variables are defined, each service uses preconfigured default values.  
    These defaults guarantee the minimum required memory for the service to operate.

    !!! info
        If multiple variables are defined, the order of precedence is:  
        
        1. **Service Memory Limit**  
        2. **Base Service Memory Limit**  
        3. **Default Values**


## CPU Configuration

The logic for CPU allocation is similar to memory limits.  

!!!info 
    CPU limits are expressed as logical CPU cores, where:   

    - `1.0` = 100% of one logical CPU  
    - `0.5` = up to 50% of one logical CPU  

1. **Service CPU Limit**  
    A direct limit can be set for each service in `gradle.properties`.  
    Example:  
    ```properties title="gradle.properties"
    <service>.cpu.limit=1.0
    ```

2. **Base Service CPU Limit**  
    In this case, a base logical CPU cores (float value) is defined for all services. Each service in the Docker Compose configuration includes a predefined multiplier.  

    Example:  
    ```properties title="gradle.properties"
    <compose>.base.cpu=1.0
    ```

3. **Default Values**  
    If no variables are defined, each service uses preconfigured default values.  



## All Services and Variables 

The following tables provide detailed references for all memory and CPU configuration variables.


### Etendo RX Services

:material-docker: Docker Compose File: `com.etendoerp.etendorx.yml`

**Memory**

| Service | Direct Variable     | Base Memory Property in MB | Multiplier | Base Memory `.env` Property Generated | Default Value |
|---------|---------------------|----------------------------|------------|---------------------------------------|---------------|
|         |                     | rx.base.memory.mb          |            |                                       |               |
| Config  | config.memory.limit |                            | 1.0        | BASE_CONFIG_MEMORY_LIMIT              | 256M          |
| Das     | das.memory.limit    |                            | 8.0        | BASE_DAS_MEMORY_LIMIT                 | 2048M         |
| Auth    | auth.memory.limit   |                            | 1.0        | BASE_AUTH_MEMORY_LIMIT                | 256M          |
| Edge    | edge.memory.limit   |                            | 1.0        | BASE_EDGE_MEMORY_LIMIT                | 256M          |

**CPU**

| Service | Direct Variable  | Base CPU Property in logic CPU | Multiplier | Base CPU `.env` Property Generated | Default Value |
|---------|------------------|------------------------------- |------------|---------------------------------------|------------|
|         |                  | rx.base.cpu                    |            |                                       |            |
| Config  | config.cpu.limit |                                | 1.0        | BASE_CONFIG_CPU_LIMIT                 | 1.0        |
| Das     | das.cpu.limit    |                                | 1.0        | BASE_DAS_CPU_LIMIT                 | 1.0        |
| Auth    | auth.cpu.limit   |                                | 1.0        | BASE_AUTH_CPU_LIMIT                | 1.0        |
| Edge    | edge.cpu.limit   |                                | 1.0        | BASE_EDGE_CPU_LIMIT                | 1.0        |


### Connector Services

**Memory**

:material-docker: Docker compose File: `com.etendoerp.etendorx_connector.yml`

| Service   | Direct Variable        | Base Memory Property in MB | Multiplier | Base Memory `.env` Property Generated | Default Value |
|-----------|------------------------|----------------------------|------------|---------------------------------------|---------------|
|           |                        | connector.base.memory.mb   |            |                                       |               |
| Obconnsrv | obconnsrv.memory.limit |                            | 1.0        | BASE_OBCONNSRV_MEMORY_LIMIT           | 256M          |
| Worker    | worker.memory.limit    |                            | 2.0        | BASE_WORKER_MEMORY_LIMIT              | 512M          |
| Kafka     | kafka.memory.limit     |                            | 4.0        | BASE_KAFKA_MEMORY_LIMIT               | 1024M         |
| Connect   | connect.memory.limit   |                            | 2.0        | BASE_CONNECT_MEMORY_LIMIT             | 512M          |

**CPU**

| Service   | Direct Variable      | Base CPU Property in logic CPU | Multiplier | Base CPU `.env` Property Generated | Default Value |
|-----------|----------------------|--------------------------------|------------|------------------------------------|---------------|
|           |                      | connector.base.cpu             |            |                                    |               |
| Obconnsrv | obconnsrv.cpu.limit  |                                | 1.0        | BASE_OBCONNSRV_CPU_LIMIT           | 1.0           |
| Worker    | worker.cpu.limit     |                                | 1.0        | BASE_WORKER_CPU_LIMIT              | 1.0           |
| Kafka     | kafka.cpu.limit      |                                | 1.0        | BASE_KAFKA_CPU_LIMIT               | 1.0           |
| Connect   | connect.cpu.limit    |                                | 1.0        | BASE_CONNECT_CPU_LIMIT             | 1.0           |


### Utils Services

:material-docker: Docker compose File: `com.etendoerp.etendorx_utils.yml`

**Memory**

| Service       | Direct Variable            | Base Memory Property in MB | Multiplier | Base Memory `.env` Property Generated | Default Value |
|---------------|----------------------------|----------------------------|------------|---------------------------------------|---------------|
|               |                            | utils.base.memory.mb       |            |                                       |               |
| Kafka-ui      | kafka.ui.memory.limit      |                            | 0.5        | BASE_KAFKA_UI_MEMORY_LIMIT            | 128M          |
| Jaeger        | jaeger.memory.limit        |                            | 1.0        | BASE_JAEGER_MEMORY_LIMIT              | 256M          |
| Jaeger-health | jaeger.health.memory.limit |                            | 0.25       | BASE_JAEGER_HEALTH_MEMORY_LIMIT       | 64M           |

**CPU**

| Service       | Direct Variable         | Base CPU Property in logic CPU | Multiplier | Base CPU `.env` Property Generated | Default Value |
|-------------- |------------------------ |--------------------------------|------------|------------------------------------|---------------|
|               |                         | utils.base.cpu                 |            |                                    |               |
| Kafka-ui      | kafka.ui.cpu.limit      |                                | 1.0        | BASE_KAFKA_UI_CPU_LIMIT            | 1.0           |
| Jaeger        | jaeger.cpu.limit        |                                | 1.0        | BASE_JAEGER_CPU_LIMIT              | 1.0           |
| Jaeger-health | jaeger.health.cpu.limit |                                | 1.0        | BASE_JAEGER_HEALTH_CPU_LIMIT       | 1.0           |




### Connector Services
:material-docker: Docker compose File: `com.etendoerp.etendorx_async.yml`

**Memory**

| Service       | Direct Variable            | Base Memory Property in MB | Multiplier | Base Memory `.env` Property Generated | Default Value |
|---------------|----------------------------|----------------------------|------------|---------------------------------------|---------------|
|               |                            | async.base.memory.mb       |            |                                       |               |
| Asyncprocess  | asyncprocess.memory.limit  |                            | 1.0        | BASE_ASYNCPROCESS_MEMORY_LIMIT        | 256M          |


**CPU**

| Service       | Direct Variable         | Base CPU Property in logic CPU | Multiplier | Base CPU `.env` Property Generated | Default Value |
|-------------- |------------------------ |--------------------------------|------------|------------------------------------|---------------|
|               |                         | async.base.cpu                 |            |                                    |               |
| Asyncprocess  | asyncprocess.cpu.limit  |                                | 1.0        | BASE_ASYNCPROCESS_CPU_LIMIT        | 1.0           |



### Tomcat Services
:material-docker: Docker compose File: `com.etendoerp.tomcat.yml`

**Memory**

| Service | Direct Variable     | Base Memory Property in MB | Multiplier | Base Memory `.env` Property Generated | Default Value |
|---------|---------------------|----------------------------|------------|---------------------------------------|---------------|
|         |                     | tomcat.base.memory.mb      |            |                                       |               |
| Tomcat  | tomcat.memory.limit |                            | 4.0        | BASE_TOMCAT_MEMORY_LIMIT              | 1024M         |

**CPU**

| Service | Direct Variable  | Base CPU Property in logic CPU | Multiplier | Base CPU `.env` Property Generated | Default Value |
|---------|------------------|--------------------------------|------------|------------------------------------|---------------|
|         |                  | tomcat.base.cpu                |            |                                    |               |
| Tomcat  | tomcat.cpu.limit |                                | 1.0        | BASE_TOMCAT_CPU_LIMIT              | 1.0           |

### Database Services
:material-docker: Docker compose File: `com.etendoerp.docker_db.yml`  

**Memory**

| Service | Direct Variable | Base Memory Property in MB | Multiplier | Base Memory `.env` Property Generated | Default Value |
|---------|-----------------|----------------------------|------------|---------------------------------------|---------------|
|         |                 | db.base.memory.mb          |            |                                       |               |
| Db      | db.memory.limit |                            | 1.0        | BASE_DB_MEMORY_LIMIT                  | 256M          |

**CPU**

| Service | Direct Variable | Base CPU Property in logic CPU | Multiplier | Base CPU `.env` Property Generated | Default Value |
|---------|-----------------|--------------------------------|------------|------------------------------------|---------------|
|         |                 | db.base.cpu                    |            |                                    |               |
| Db      | db.cpu.limit    |                                | 1.0        | BASE_DB_CPU_LIMIT                  | 1.0           |

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
