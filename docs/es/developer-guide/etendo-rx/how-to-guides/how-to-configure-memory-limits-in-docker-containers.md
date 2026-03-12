---
title: Cómo gestionar los límites de memoria para contenedores Docker de Etendo
tags:
  - Etendo
  - Docker
  - Memoria
  - Tomcat
  - CPU
  - Contenedores
---

# Cómo gestionar los límites de memoria para contenedores Docker de Etendo

!!! warning
    Esta guía asume conocimientos prácticos de **entornos de desarrollo Java**, incluidos **comandos de compilación de Gradle**, **despliegue de aplicaciones Java** y **gestión de contenedores Docker**. Está dirigida a desarrolladores con habilidades técnicas intermedias a avanzadas en desarrollo de software y administración de sistemas.

## Visión general

Esta guía explica cómo configurar los límites de memoria y CPU para los servicios de Etendo que se ejecutan en contenedores Docker.
Presenta tres niveles de configuración tanto para el uso de memoria como de CPU:

1. **Límites de servicio**: valores directos establecidos por servicio en el archivo `gradle.properties`.
2. **Límites base de servicio**: un valor base con multiplicadores predefinidos que ajustan los recursos dinámicamente entre servicios.
3. **Lógica del valor por defecto**: mínimos preconfigurados que garantizan que los servicios puedan ejecutarse cuando no se definen límites.

Cada nivel tiene una precedencia definida: los límites directos del servicio prevalecen sobre los límites base, y los límites base prevalecen sobre los valores por defecto.
El documento también proporciona tablas de referencia detalladas que enumeran todas las variables disponibles para los servicios de Etendo en distintos archivos de Docker Compose.

## Gestión de memoria
Etendo permite configurar los límites de memoria en tres niveles diferentes.  
Cada nivel tiene prioridad sobre el anterior:

1. **Límite de memoria del servicio**  
   Se puede establecer un límite directo para cada servicio en `gradle.properties`.  
   Ejemplo:  
   ```properties title="gradle.properties"
   <service>.memory.limit=512M
   ```  
   Los valores pueden expresarse en megabytes (`M`) o gigabytes (`G`). Esta configuración tiene la máxima prioridad.

2. **Límite base de memoria del servicio**  
    En este caso, se define un tamaño de memoria base (solo en `MB`, valor entero) para todos los servicios. Cada servicio en la configuración de Docker Compose incluye un multiplicador predefinido.  

    Ejemplo:  
    ```properties title="gradle.properties"
    <compose>.base.memory.mb=512
    ```  
    Al ejecutar:

    ```bash title="Terminal"
    ./gradlew resources.up
    ```  
    Gradle calcula el límite de memoria efectivo para cada servicio usando el tamaño base multiplicado por el factor del servicio. Estos multiplicadores se determinaron en base a un análisis de rendimiento previo.

    ``` title="archivo .env generado"
        BASE_<SERVICE1>_MEMORY_LIMIT=512M
        BASE_<SERVICE2>_MEMORY_LIMIT=1024M
        BASE_<SERVICE3>_MEMORY_LIMIT=2048M 
    ```

    Este enfoque es útil cuando la memoria del sistema es limitada, ya que permite establecer un tamaño base mínimo para cada servicio mientras los multiplicadores ajustan la distribución de recursos según la demanda del servicio.

3. **Lógica del valor por defecto**  
    Si no se define ninguna variable, cada servicio utiliza valores por defecto preconfigurados.  
    Estos valores por defecto garantizan la memoria mínima requerida para que el servicio funcione.

    !!! info
        Si se definen múltiples variables, el orden de precedencia es:  
        
        1. **Límite de memoria del servicio**  
        2. **Límite base de memoria del servicio**  
        3. **Lógica del valor por defecto**

## Configuración de CPU

La lógica para la asignación de CPU es similar a la de los límites de memoria.  

!!!info 
    Los límites de CPU se expresan como núcleos lógicos de CPU, donde:   

    - `1.0` = 100% de una CPU lógica  
    - `0.5` = hasta el 50% de una CPU lógica  

1. **Límite de CPU del servicio**  
    Se puede establecer un límite directo para cada servicio en `gradle.properties`.  
    Ejemplo:  
    ```properties title="gradle.properties"
    <service>.cpu.limit=1.0
    ```

2. **Límite base de CPU del servicio**  
    En este caso, se define una base de núcleos lógicos de CPU (valor float) para todos los servicios. Cada servicio en la configuración de Docker Compose incluye un multiplicador predefinido.  

    Ejemplo:  
    ```properties title="gradle.properties"
    <compose>.base.cpu=1.0
    ```

3. **Lógica del valor por defecto**  
    Si no se define ninguna variable, cada servicio utiliza valores por defecto preconfigurados.  

## Todos los servicios y variables 

Las siguientes tablas proporcionan referencias detalladas para todas las variables de configuración de memoria y CPU.

### Servicios Etendo RX

:material-docker: Archivo Docker Compose: `com.etendoerp.etendorx.yml`

**Memoria**

| Servicios | Variable directa     | Propiedad de memoria base en MB | Multiplicador | Propiedad de memoria base `.env` generada | Lógica del valor por defecto |
|----------|-----------------------|----------------------------------|--------------|------------------------------------------|------------------------------|
|          |                       | rx.base.memory.mb                |              |                                          |                              |
| Config   | config.memory.limit   |                                  | 1.0          | BASE_CONFIG_MEMORY_LIMIT                 | 256M                         |
| Das      | das.memory.limit      |                                  | 8.0          | BASE_DAS_MEMORY_LIMIT                    | 2048M                        |
| Auth     | auth.memory.limit     |                                  | 1.0          | BASE_AUTH_MEMORY_LIMIT                   | 256M                         |
| Edge     | edge.memory.limit     |                                  | 1.0          | BASE_EDGE_MEMORY_LIMIT                   | 256M                         |

**CPU**

| Servicios | Variable directa  | Propiedad de CPU base en CPU lógica | Multiplicador | Propiedad de CPU base `.env` generada | Lógica del valor por defecto |
|----------|--------------------|-------------------------------------|--------------|---------------------------------------|------------------------------|
|          |                    | rx.base.cpu                         |              |                                       |                              |
| Config   | config.cpu.limit   |                                     | 1.0          | BASE_CONFIG_CPU_LIMIT                 | 1.0                          |
| Das      | das.cpu.limit      |                                     | 1.0          | BASE_DAS_CPU_LIMIT                    | 1.0                          |
| Auth     | auth.cpu.limit     |                                     | 1.0          | BASE_AUTH_CPU_LIMIT                   | 1.0                          |
| Edge     | edge.cpu.limit     |                                     | 1.0          | BASE_EDGE_CPU_LIMIT                   | 1.0                          |

### Servicios de conectores

**Memoria**

:material-docker: Archivo Docker Compose: `com.etendoerp.etendorx_connector.yml`

| Servicios  | Variable directa         | Propiedad de memoria base en MB | Multiplicador | Propiedad de memoria base `.env` generada | Lógica del valor por defecto |
|------------|--------------------------|----------------------------------|--------------|------------------------------------------|------------------------------|
|            |                          | connector.base.memory.mb         |              |                                          |                              |
| Obconnsrv  | obconnsrv.memory.limit   |                                  | 1.0          | BASE_OBCONNSRV_MEMORY_LIMIT              | 256M                         |
| Responsable | worker.memory.limit     |                                  | 2.0          | BASE_WORKER_MEMORY_LIMIT                 | 512M                         |
| Kafka      | kafka.memory.limit       |                                  | 4.0          | BASE_KAFKA_MEMORY_LIMIT                  | 1024M                        |
| Connect    | connect.memory.limit     |                                  | 2.0          | BASE_CONNECT_MEMORY_LIMIT                | 512M                         |

**CPU**

| Servicios  | Variable directa       | Propiedad de CPU base en CPU lógica | Multiplicador | Propiedad de CPU base `.env` generada | Lógica del valor por defecto |
|------------|------------------------|-------------------------------------|--------------|---------------------------------------|------------------------------|
|            |                        | connector.base.cpu                  |              |                                       |                              |
| Obconnsrv  | obconnsrv.cpu.limit    |                                     | 1.0          | BASE_OBCONNSRV_CPU_LIMIT              | 1.0                          |
| Responsable | worker.cpu.limit      |                                     | 1.0          | BASE_WORKER_CPU_LIMIT                 | 1.0                          |
| Kafka      | kafka.cpu.limit        |                                     | 1.0          | BASE_KAFKA_CPU_LIMIT                  | 1.0                          |
| Connect    | connect.cpu.limit      |                                     | 1.0          | BASE_CONNECT_CPU_LIMIT                | 1.0                          |

### Servicios de utilidades

:material-docker: Archivo Docker Compose: `com.etendoerp.etendorx_utils.yml`

**Memoria**

| Servicios      | Variable directa             | Propiedad de memoria base en MB | Multiplicador | Propiedad de memoria base `.env` generada | Lógica del valor por defecto |
|----------------|------------------------------|----------------------------------|--------------|------------------------------------------|------------------------------|
|                |                              | utils.base.memory.mb             |              |                                          |                              |
| Kafka-ui       | kafka.ui.memory.limit        |                                  | 0.5          | BASE_KAFKA_UI_MEMORY_LIMIT               | 128M                         |
| Jaeger         | jaeger.memory.limit          |                                  | 1.0          | BASE_JAEGER_MEMORY_LIMIT                 | 256M                         |
| Jaeger-health  | jaeger.health.memory.limit   |                                  | 0.25         | BASE_JAEGER_HEALTH_MEMORY_LIMIT          | 64M                          |

**CPU**

| Servicios      | Variable directa          | Propiedad de CPU base en CPU lógica | Multiplicador | Propiedad de CPU base `.env` generada | Lógica del valor por defecto |
|----------------|---------------------------|-------------------------------------|--------------|---------------------------------------|------------------------------|
|                |                           | utils.base.cpu                      |              |                                       |                              |
| Kafka-ui       | kafka.ui.cpu.limit        |                                     | 1.0          | BASE_KAFKA_UI_CPU_LIMIT               | 1.0                          |
| Jaeger         | jaeger.cpu.limit          |                                     | 1.0          | BASE_JAEGER_CPU_LIMIT                 | 1.0                          |
| Jaeger-health  | jaeger.health.cpu.limit   |                                     | 1.0          | BASE_JAEGER_HEALTH_CPU_LIMIT          | 1.0                          |

### Servicios de conectores
:material-docker: Archivo Docker Compose: `com.etendoerp.etendorx_async.yml`

**Memoria**

| Servicios      | Variable directa             | Propiedad de memoria base en MB | Multiplicador | Propiedad de memoria base `.env` generada | Lógica del valor por defecto |
|----------------|------------------------------|----------------------------------|--------------|------------------------------------------|------------------------------|
|                |                              | async.base.memory.mb             |              |                                          |                              |
| Asyncprocess   | asyncprocess.memory.limit    |                                  | 1.0          | BASE_ASYNCPROCESS_MEMORY_LIMIT           | 256M                         |

**CPU**

| Servicios      | Variable directa          | Propiedad de CPU base en CPU lógica | Multiplicador | Propiedad de CPU base `.env` generada | Lógica del valor por defecto |
|----------------|---------------------------|-------------------------------------|--------------|---------------------------------------|------------------------------|
|                |                           | async.base.cpu                      |              |                                       |                              |
| Asyncprocess   | asyncprocess.cpu.limit    |                                     | 1.0          | BASE_ASYNCPROCESS_CPU_LIMIT           | 1.0                          |

### Servicios Tomcat
:material-docker: Archivo Docker Compose: `com.etendoerp.tomcat.yml`

**Memoria**

| Servicios | Variable directa      | Propiedad de memoria base en MB | Multiplicador | Propiedad de memoria base `.env` generada | Lógica del valor por defecto |
|----------|------------------------|----------------------------------|--------------|------------------------------------------|------------------------------|
|          |                        | tomcat.base.memory.mb            |              |                                          |                              |
| Tomcat   | tomcat.memory.limit    |                                  | 4.0          | BASE_TOMCAT_MEMORY_LIMIT                 | 1024M                        |

**CPU**

| Servicios | Variable directa   | Propiedad de CPU base en CPU lógica | Multiplicador | Propiedad de CPU base `.env` generada | Lógica del valor por defecto |
|----------|---------------------|-------------------------------------|--------------|---------------------------------------|------------------------------|
|          |                     | tomcat.base.cpu                     |              |                                       |                              |
| Tomcat   | tomcat.cpu.limit    |                                     | 1.0          | BASE_TOMCAT_CPU_LIMIT                 | 1.0                          |

### Servicios de base de datos
:material-docker: Archivo Docker Compose: `com.etendoerp.docker_db.yml`  

**Memoria**

| Servicios | Variable directa | Propiedad de memoria base en MB | Multiplicador | Propiedad de memoria base `.env` generada | Lógica del valor por defecto |
|----------|-------------------|----------------------------------|--------------|------------------------------------------|------------------------------|
|          |                   | db.base.memory.mb                |              |                                          |                              |
| Db       | db.memory.limit   |                                  | 1.0          | BASE_DB_MEMORY_LIMIT                     | 256M                         |

**CPU**

| Servicios | Variable directa | Propiedad de CPU base en CPU lógica | Multiplicador | Propiedad de CPU base `.env` generada | Lógica del valor por defecto |
|----------|-------------------|-------------------------------------|--------------|---------------------------------------|------------------------------|
|          |                   | db.base.cpu                         |              |                                       |                              |
| Db       | db.cpu.limit      |                                     | 1.0          | BASE_DB_CPU_LIMIT                      | 1.0                          |

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.