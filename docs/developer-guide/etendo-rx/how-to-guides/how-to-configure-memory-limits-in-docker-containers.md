---
tags:
  - Etendo Rx
  - Docker
  - Memory
  - Tomcat
  - CPU
status: beta
---
# How to Manage Memory Limits for Etendo RX Docker Containers (BETA)

!!! example  "IMPORTANT:THIS IS A BETA VERSION"
    - It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**, especially in production environments.
    - It should be used with **caution**, and you should always **validate backups** before executing any critical operation.

## Overview

This document explains **how users can set memory limits** for each Etendo RX service either by:

1. Defining **per-service properties** in `gradle.properties`, or  
2. using **base properties with multipliers** that auto-calculate the `BASE_*_MEMORY_LIMIT` and  `BASE_*_CPU_LIMIT` variables.

> **How it works from end to end**
>
> - You declare properties in `gradle.properties`.
> - When you run:
>   ```bash
>   ./gradlew resources.up
>   ```
>   Gradle reads those properties and writes the resolved variables to a `.env` file (e.g., `BASE_CONFIG_MEMORY_LIMIT`, `BASE_CONFIG_CPU_LIMIT`, etc.).
> - `docker-compose` then consumes `.env` and applies the limits via:
>   ```yaml
    limits:
        cpus: "${SERVICE_CPU_LIMIT:-${BASE_SERVICE_CPU_LIMIT:-<hard default>}}"
>       memory: ${SERVICE_MEMORY_LIMIT:-${BASE_SERVICE_MEMORY_LIMIT:-<hard default>}}
>   ```

---

## Resolution order (per service)

### Memory Limit
1. **`SERVICE_MEMORY_LIMIT`** — generated from `gradle.properties` (e.g., `config.memory.limit=512M`).  
2. **`BASE_SERVICE_MEMORY_LIMIT`** — calculated from the **base property in MB** (e.g., `rx.base.memory.mb`) × the **service factor**.  
3. **Hard default** — the last fallback defined in the compose file if the above are not present.

> 📏 **Units**  
> - Base properties are **MB** (e.g., `512`).  
> - Generated env vars are written with `M` (e.g., `1024M`). Values equal to `1024MB` are effectively **1G**.

### CPU Limit
1. **`SERVICE_CPU_LIMIT`** — generated from `gradle.properties` (e.g., `config.cpu.limit=2`).  
2. **`BASE_SERVICE_CPU_LIMIT`** — calculated from the **base property** (e.g., `rx.base.cpu`) × the **service factor**.  
3. **Hard default** — the last fallback defined in the compose file if the above are not present.

> 📏 **Units**  
> - Base properties are **logic CPU cores** (e.g., `1.0` → full access to one logical CPU. `0.5` → the container can use at most 50% of a single logical CPU).  
---

## Quick examples

### A) Set a service limit explicitly
In `gradle.properties`:
```properties
config.memory.limit=512M
das.memory.limit=1024M
```

Run:

```bash
./gradlew resources.up
```

.env gets:

```.env
CONFIG_MEMORY_LIMIT=512M
DAS_MEMORY_LIMIT=1024M
```
### B) Set base properties with multipliers

In `gradle.properties`:
```properties
rx.base.memory.mb=512
rx.base.cpu=2.0

```
Run:

```bash
./gradlew resources.up
```

.env gets:

```.env
BASE_CONFIG_MEMORY_LIMIT=512M
BASE_CONFIG_CPU_LIMIT=2.0
BASE_DAS_MEMORY_LIMIT=1024M
BASE_DAS_CPU_LIMIT=2.0
BASE_AUTH_MEMORY_LIMIT=512M
BASE_AUTH_CPU_LIMIT=2.0
BASE_EDGE_MEMORY_LIMIT=512M
BASE_EDGE_CPU_LIMIT=2.0
```

### C) Using default values

If you do not set any variable in `gradle.properties` and run:

```bash
./gradlew resources.up
```
For example, in the `com.etendoerp.etendorx.yml` file:

The Config service will be used:

```com.etendoerp.etendorx.yml
resources:
limits:
    cpus: 1
    memory:256M
```
The Das service will be used:

```com.etendoerp.etendorx.yml
resources:
limits:
    cpus: 1
    memory:512M
```
The Auth service will be used:

```com.etendoerp.etendorx.yml
resources:
limits:
    cpus: 1
    memory:256M
```
The Edge service will be used:

```com.etendoerp.etendorx.yml
resources:
limits:
    cpus: 1
    memory:256M
```

## All properties to manage Docker containers resources:

### Memory Management

| File                           | Base Memory Property in MB | Service       | Direct Service `gradle.properties` Property        | Multiplier | Generated Base Memory .env Property     | Default Value |
|--------------------------------|----------------------------|---------------|--------------------------------|------------|-----------------------------------|---------------|
| com.etendoerp.etendorx.yml      | rx.base.memory.mb          | Config        | config.memory.limit            | 1.0        | BASE_CONFIG_MEMORY_LIMIT          | 256M          |
|                                |                            | Das           | das.memory.limit               | 8.0        | BASE_DAS_MEMORY_LIMIT             | 2048M          |
|                                |                            | Auth          | auth.memory.limit              | 1.0        | BASE_AUTH_MEMORY_LIMIT            | 256M          |
|                                |                            | Edge          | edge.memory.limit              | 1.0        | BASE_EDGE_MEMORY_LIMIT            | 256M          |
| com.etendoerp.etendorx_connector.yml | connector.base.memory.mb | Obconnsrv     | obconnsrv.memory.limit         | 1.0        | BASE_OBCONNSRV_MEMORY_LIMIT       | 256M          |
|                                |                            | Worker        | worker.memory.limit            | 2.0        | BASE_WORKER_MEMORY_LIMIT          | 512M          |
|                                |                            | Kafka         | kafka.memory.limit             | 4.0        | BASE_KAFKA_MEMORY_LIMIT           | 1024M            |
|                                |                            | Connect       | connect.memory.limit           | 2.0        | BASE_CONNECT_MEMORY_LIMIT         | 512M            |
| com.etendoerp.etendorx_async.yml | async.base.memory.mb       | Asyncprocess  | asyncprocess.memory.limit      | 1.0        | BASE_ASYNCPROCESS_MEMORY_LIMIT    | 256M          |
| com.etendoerp.etendorx_utils.yml | utils.base.memory.mb       | Kafka-ui      | kafka.ui.memory.limit          | 0.5        | BASE_KAFKA_UI_MEMORY_LIMIT        | 128M          |
|                                |                            | Jaeger        | jaeger.memory.limit            | 1.0        | BASE_JAEGER_MEMORY_LIMIT          | 256M          |
|                                |                            | Jaeger-health | jaeger.health.memory.limit     | 0.25       | BASE_JAEGER_HEALTH_MEMORY_LIMIT   | 64M           |
| com.etendoerp.tomcat.yml        | tomcat.base.memory.mb      | Tomcat        | tomcat.memory.limit            | 4.0        | BASE_TOMCAT_MEMORY_LIMIT          | 1024M          |
| com.etendoerp.docker_db.yml     | db.base.memory.mb          | Db            | db.memory.limit                | 1.0        | BASE_DB_MEMORY_LIMIT              | 256M          |

---

### CPU Management

| File                           | Base CPU Property in logic CPU cores| Service       | Direct Service `gradle.properties` Property        | Multiplier | Generated Base CPU .env Property     | Default Value |
|--------------------------------|-------------------|---------------|--------------------------------|------------|-----------------------------------|---------------|
| com.etendoerp.etendorx.yml      | rx.base.cpu       | Config        | config.cpu.limit               | 1.0        | BASE_CONFIG_CPU_LIMIT             | 1.0           |
|                                |                   | Das           | das.cpu.limit                  | 1.0        | BASE_DAS_CPU_LIMIT                | 1.0           |
|                                |                   | Auth          | auth.cpu.limit                 | 1.0        | BASE_AUTH_CPU_LIMIT               | 1.0           |
|                                |                   | Edge          | edge.cpu.limit                 | 1.0        | BASE_EDGE_CPU_LIMIT               | 1.0           |
| com.etendoerp.etendorx_connector.yml | connector.base.cpu | Obconnsrv     | obconnsrv.cpu.limit            | 1.0        | BASE_OBCONNSRV_CPU_LIMIT          | 1.0           |
|                                |                   | Worker        | worker.cpu.limit               | 1.0        | BASE_WORKER_CPU_LIMIT             | 1.0           |
|                                |                   | Kafka         | kafka.cpu.limit                | 1.0        | BASE_KAFKA_CPU_LIMIT              | 1.0           |
|                                |                   | Connect       | connect.cpu.limit              | 1.0        | BASE_CONNECT_CPU_LIMIT            | 1.0           |
| com.etendoerp.etendorx_async.yml | async.base.cpu    | Asyncprocess  | asyncprocess.cpu.limit         | 1.0        | BASE_ASYNCPROCESS_CPU_LIMIT       | 1.0           |
| com.etendoerp.etendorx_utils.yml | utils.base.cpu    | Kafka-ui      | kafka.ui.cpu.limit             | 1.0        | BASE_KAFKA_UI_CPU_LIMIT           | 1.0           |
|                                |                   | Jaeger        | jaeger.cpu.limit               | 1.0        | BASE_JAEGER_CPU_LIMIT             | 1.0           |
|                                |                   | Jaeger-health | jaeger.health.cpu.limit        | 1.0        | BASE_JAEGER_HEALTH_CPU_LIMIT      | 1.0           |
| com.etendoerp.tomcat.yml        | tomcat.base.cpu   | Tomcat        | tomcat.cpu.limit               | 1.0        | BASE_TOMCAT_CPU_LIMIT             | 1.0           |
| com.etendoerp.docker_db.yml     | db.base.cpu       | Db            | db.cpu.limit                   | 1.0        | BASE_DB_CPU_LIMIT                 | 1.0           |



### Disclaimer: Advanced Knowledge Required

This guide assumes a fundamental understanding of Java development environments, including familiarity with Gradle build commands and Java application deployment. It is intended for users with intermediate to advanced technical skills in software development and system administration. New users or those unfamiliar with the concepts discussed may need additional resources or assistance. 

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
