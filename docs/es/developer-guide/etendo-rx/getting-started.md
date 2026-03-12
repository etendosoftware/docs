---
title: Guía del desarrollador - Etendo RX - Primeros pasos
---

## Visión general

Esta guía le ayudará a configurar Etendo, incluyendo tanto las funcionalidades de Etendo Classic como Etendo RX, nuestra plataforma reactiva capaz de ejecutar microservicios con interacción con la base de datos y acciones asíncronas.
## Requisitos

1. Instale Etendo Classic. Para ello, siga la [guía de instalación de Etendo Classic](../../getting-started/installation.md).
2. Instale el [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}.
3. Este proyecto depende de las siguientes herramientas:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: versión `26.0.0` o superior.
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: versión `2.26.0` o superior.

!!! warning
    Evite instalar Docker mediante [Snap](https://snapcraft.io){target="_blank"}, ya que puede estar restringido por este sandbox y puede no tener acceso a directorios del host como `/opt/`, lo que puede impedir que los contenedores Docker de Etendo se inicien correctamente.

    Recomendación: instale Etendo utilizando la [ISO más reciente](../../whats-new/release-notes/etendo-classic/iso.md)(que incluye Docker) o instale Docker siguiendo la guía de instalación oficial de su distribución.
## Servicios dockerizados

En el bundle de plataforma, puede encontrar el módulo **Servicios dockerizados**, que proporciona la arquitectura necesaria para distribuir la infraestructura. En este caso, en este bundle, también se incluye el módulo **Etendo RX** y, para lanzar los servicios distribuidos en él, se necesita una determinada configuración. En el archivo `gradle.properties`, añada la siguiente variable:

``` groovy title="gradle.properties"
docker_com.etendoerp.etendorx=true
```

!!!info
    Para más información sobre cómo gestionar las dockerizaciones de Etendo, visite [Gestión de Docker](../etendo-classic/bundles/platform/docker-management.md). 

??? Note "Tomcat y PostgresSQL dockerizados (opcional)"
    También es posible ejecutar el [servicio PostgreSQL](../platform/docker-management.md#postgres-database-service) y el [servicio Tomcat](../platform/tomcat-dockerized-service.md) dockerizados, añadiendo **opcionalmente** el [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank} y las siguientes variables de configuración:

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    docker_com.etendoerp.docker_db=true
    ```

    Si desea depurar Tomcat localmente con IntelliJ, visite [Servicio dockerizado de Tomcat](../../developer-guide/etendo-classic/bundles/platform/tomcat-dockerized-service.md).
###  Configuraciones de Etendo RX

Antes de iniciar los servicios dockerizados, hay algunas configuraciones que deben realizarse en Etendo Classic.

### Configuración de la Entidad 
:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

Es necesario configurar el token de cifrado para la autenticación en la ventana `Entidad` con el rol `System Administrator`.
Si el tiempo de expiración es igual a `0`, los tokens no caducan.

Genere una clave aleatoria con el botón **Generar Clave**.

![](../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)
### Ventana RX Config
:material-menu: `Aplicación` > `Etendo RX` > `RX Config`

Esta ventana de configuración almacena los datos de acceso para los servicios de Etendo RX, que son cruciales para la interacción entre diferentes servicios. Con el rol `System Administrator`, en esta ventana, ejecute el proceso `Initialize RX Services` en la barra de herramientas. 

![](../../assets/developer-guide/etendo-rx/getting-started/initialize-rx-service.png)

Tras la ejecución de este proceso, se completan las variables de configuración por defecto, en función de la configuración de la instancia y de la infraestructura; incluso se configuran los parámetros por defecto requeridos por cada servicio.

![default-rx-config.png](../../assets/developer-guide/etendo-rx/getting-started/default-rx-config.png)

!!!info
    El campo **URL pública** solo necesita configurarse cuando los servicios estén configurados para producción.
### Lanzar servicios RX

A continuación, para ejecutar eficazmente los servicios, es necesario **ejecutar el comando** en el terminal:

```bash title="Terminal"
./gradlew resources.up
```

Aquí, se pueden ver todos los servicios y sus respectivos logs en ejecución utilizando [lazydocker](https://github.com/jesseduffield/lazydocker#installation){target="_blank"} o [Docker Desktop](https://www.docker.com/products/docker-desktop/){target="_blank"} para una gestión de contenedores sencilla y rápida.

![Servicios Docker](../../assets/developer-guide/etendo-rx/getting-started/rx-services.png)

Por defecto, los siguientes servicios deberían estar en funcionamiento:

- Config
- Auth
- Edge
- Das

!!! success
    Ha configurado correctamente los servicios de Etendo RX. Para más información, visite la página [Projections and Mappings](./concepts/projections.md) y [Creating a New Microservice](../../developer-guide/etendo-rx/tutorials/creating-a-new-microservice.md) en la sección de la guía del desarrollador.

Actualmente, la mayor parte de los servicios de Etendo RX se basan en imágenes Docker denominadas dynamic-das y dynamic-gradle, que sustentan la ejecución de microservicios. Dynamic-das se dedica exclusivamente a ejecutar el microservicio Das y dynamic-gradle, por el contrario, puede lanzar múltiples microservicios, como Config, Edge, Auth, AsyncProcess, ObConnSrv, Worker y otros.
### Dynamic DAS v1.1.0

#### Pila

- **Imagen base:** `amazoncorretto:17.0.14-alpine3.21` ([enlace](https://github.com/corretto/corretto-docker/tree/main/17/jdk/alpine/3.21))
- **Versión de JDK:** 17.0.14
- **Versión de Gradle:** 8.12.1
- **Versión de OpenTelemetry:** v2.18.1 ([versión](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/tag/v2.18.1))  
- **Gestor de paquetes:** `apk` (Alpine Package Keeper)
- **Herramientas adicionales instaladas:** `wget`, `unzip`

---

#### Puertos

| Puerto | Descripción                 |
|--------|-----------------------------|
| `5021` | Puerto del servicio DAS     |
| `8092` | Puerto de depuración remota |

---

#### Variables de entorno

| Name                                                        | Description                                                                                              | Type     | Allowed Values                                                      | Default                                      | Notes                                                                                                                                                        |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DEPENDENCIES`                                              | Coordenadas GAV de Maven para dependencias dinámicas                                                     | string   | Lista separada por comas                                            | *null*                                       | —                                                                                                                                                            |
| `REPO_URL`                                                  | URL del repositorio Maven                                                                                 | URL      | Cualquier URL válida                                                | `https://repo.maven.apache.org/maven2/`     | —                                                                                                                                                            |
| `REPO_USER`                                                 | Nombre de usuario del repositorio Maven                                                                  | string   | —                                                                   | *null*                                       | —                                                                                                                                                            |
| `REPO_PASSWORD`                                             | Contraseña del repositorio Maven                                                                          | string   | —                                                                   | *null*                                       | —                                                                                                                                                            |
| `CONFIG_SERVER_URL`                                         | URL del servidor Spring Cloud Config                                                                     | URL      | Cualquier URL válida                                                | `http://localhost:8888`                     | —                                                                                                                                                            |
| `TASK`                                                      | Tarea a ejecutar                                                                                            | enum     | `downloadJar`, `run`                                                | `downloadJar`                                | —                                                                                                                                                            |
| `DB_HOST`                                                   | Nombre de host de la base de datos                                                                         | string   | —                                                                   | `db`                                         | —                                                                                                                                                            |
| `DB_PORT`                                                   | Puerto para la conexión a la base de datos                                                                | integer  | Cualquier puerto válido                                             | `5432`                                       | —                                                                                                                                                            |
| `DB_SID`                                                    | SID de la base de datos                                                                                   | string   | —                                                                   | `etendo`                                     | —                                                                                                                                                            |
| `DEBUG_PORT`                                                | Puerto de depuración remota                                                                                | integer  | Cualquier puerto válido                                             | `5021`                                       | —                                                                                                                                                            |
| `ENABLE_OPEN_TELEMETRY`                                     | Habilita la instrumentación de OpenTelemetry                                                              | boolean  | `true`, `false`                                                     | `false`                                      | —                                                                                                                                                            |
| `OTEL_SERVICE_NAME`                                         | Nombre del servicio para OpenTelemetry                                                                    | string   | Cualquier cadena                                                    | `das`                                        | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_ENDPOINT`                               | URL base del endpoint OTLP                                                                                 | string   | Cualquier URL                                                      | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
| `OTEL_EXPORTER_OTLP_PROTOCOL`                               | Protocolo de transporte para OTLP                                                                         | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
| `OTEL_METRICS_EXPORTER`                                     | Exportador de métricas                                                                                     | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
| `OTEL_LOGS_EXPORTER`                                        | Exportador de logs                                                                                         | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
| `OTEL_TRACES_EXPORTER`                                      | Exportador de trazas                                                                                       | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_TIMEOUT`                                | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                          | integer  | Cualquier número positivo                                          | `10000`                                      | —                                                                                                                                                            |
| `SPRING_PROFILES_ACTIVE`                                    | Perfiles activos de Spring                                                                                 | string   | Lista separada por comas                                            | *null*                                       | Ejemplo: `prod,dev`                                                                                                                                         |
| `SPRING_CLOUD_CONFIG_SERVER_NATIVE_SEARCHLOCATIONS`         | Rutas de búsqueda nativas para el servidor Spring Config                                                  | string   | Rutas de archivo separadas por comas                                | *null*                                       | Ejemplo: `file:///config,classpath:/defaults`                                                                                                               |
| `DISABLE_DEBUG`                                             | Deshabilitar el agente de depuración de la JVM                                                            | boolean  | `true`, `false`                                                     | `false`                                      | Si `true`, añade `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:${DEBUG_PORT}`. `dt_socket`: el mecanismo de transporte (es decir, un socket TCP) utilizado para la conexión de depuración. `server=y` indica a la JVM que actúe como servidor de depuración (esperando a que un depurador se conecte). `suspend=n` significa “no pausar al inicio”: la aplicación se ejecutará inmediatamente y podrá adjuntar el depurador en cualquier momento. (Si configura `suspend=y`, la JVM se pausará en la primera línea hasta que se adjunte un depurador). |
| `JAVA_OPTS`                                                 | Opciones adicionales de la JVM                                                                             | string   | Cualquier opción válida de la JVM                                  | *null*                                       | Ejemplo: `-Dfile.encoding=UTF-8`                                                                                                                             |
| `GRADLE_FLAGS`                                              | Flags del comando de Gradle                                                                                 | string   | Cualquier flag válido de Gradle                                     | `-no-daemon --info --refresh-dependencies`   | —                                                                                                                                                            |
| `DEBUG_MODE`                                                | Habilitar el modo de depuración para la aplicación                                                        | boolean  | `true`, `false`                                                     | `false`                                      | —                                                                                                                                                            |

---
### Dynamic Gradle v1.1.0

#### Pila

- **Imagen base:** `amazoncorretto:17.0.14-alpine3.21` ([enlace](https://github.com/corretto/corretto-docker/tree/main/17/jdk/alpine/3.21))
- **Versión de JDK:** 17.0.14
- **Versión de Gradle:** 8.12.1
- **Versión de OpenTelemetry:** v2.18.1 ([versión](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/tag/v2.18.1))  
- **Gestor de paquetes:** `apk` (Alpine Package Keeper)
- **Herramientas adicionales instaladas:** `wget`, `unzip`

---

#### Puertos

| Puerto | Descripción                                  |
|--------|----------------------------------------------|
| `8888` | Puerto del servicio de configuración         |
| `5020` | Puerto de depuración remota del servicio de configuración |
| `8094` | Puerto del servicio de autenticación         |
| `5022` | Puerto de depuración remota del servicio de autenticación |
| `8096` | Puerto del servicio Edge                     |
| `5023` | Puerto de depuración remota del servicio Edge |
| `8099` | Puerto del servicio de procesamiento asíncrono |
| `5024` | Puerto de depuración remota del servicio de procesamiento asíncrono |
| `8101` | Puerto del servicio Obconnsrv                |
| `5025` | Puerto de depuración remota del servicio Obconnsrv |
| `8102` | Puerto del servicio Worker                   |
| `5026` | Puerto de depuración remota del servicio Worker |

---

#### Variables de entorno

| Nombre                                                       | Descripción                                                                                              | Tipo     | Valores permitidos                                                | Valor por defecto                             | Notas                                                                                                                                                        |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DEPENDENCIES`                                               | Coordenadas Maven GAV para dependencias dinámicas                                                        | string   | Lista separada por comas                                          | *null*                                        | —                                                                                                                                                            |
| `REPO_URL`                                                   | URL del repositorio Maven                                                                                 | URL      | Cualquier URL válida                                              | `https://repo.maven.apache.org/maven2/`       | —                                                                                                                                                            |
| `REPO_USER`                                                  | Nombre de usuario para el repositorio Maven                                                               | string   | —                                                                 | *null*                                        | —                                                                                                                                                            |
| `REPO_PASSWORD`                                              | Contraseña para el repositorio Maven                                                                       | string   | —                                                                 | *null*                                        | —                                                                                                                                                            |
| `CONFIG_SERVER_URL`                                          | URL del servidor Spring Cloud Config                                                                       | URL      | Cualquier URL válida                                              | `http://localhost:8888`                      | —                                                                                                                                                            |
| `TASK`                                                       | Tarea a ejecutar                                                                                           | enum     | `downloadJar`, `run`                                              | `run`                                         | —                                                                                                                                                            |
| `DEBUG_PORT`                                                 | Puerto de depuración remota                                                                                 | integer  | Cualquier puerto válido                                           | `5005`                                        | —                                                                                                                                                            |
| `ENABLE_OPEN_TELEMETRY`                                      | Habilita la instrumentación de OpenTelemetry                                                               | boolean  | `true`, `false`                                                   | `false`                                       | —                                                                                                                                                            |
| `OTEL_SERVICE_NAME`                                          | Nombre del servicio para OpenTelemetry                                                                      | string   | Cualquier cadena                                                  | `dynamic-gradle`                              | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_ENDPOINT`                                | URL base del endpoint OTLP                                                                                    | string   | Cualquier URL                                                     | `http://jaeger:4318`                          | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
| `OTEL_EXPORTER_OTLP_PROTOCOL`                                | Protocolo de transporte para OTLP                                                                            | enum     | `grpc`, `http/protobuf`, `http/json`                              | `http/protobuf`                               | —                                                                                                                                                            |
| `OTEL_METRICS_EXPORTER`                                      | Exportador de métricas                                                                                        | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                | `none`                                        | —                                                                                                                                                            |
| `OTEL_LOGS_EXPORTER`                                         | Exportador de logs                                                                                           | enum     | `otlp`, `console`, `logging`, `none`                              | `none`                                        | —                                                                                                                                                            |
| `OTEL_TRACES_EXPORTER`                                       | Exportador de trazas                                                                                         | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                    | `otlp`                                        | —                                                                                                                                                            |
| `OTEL_EXPORTER_OTLP_TIMEOUT`                                 | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                            | integer  | Cualquier número positivo                                         | `10000`                                       | —                                                                                                                                                            |
| `SPRING_PROFILES_ACTIVE`                                     | Perfiles Spring activos                                                                                      | string   | Lista separada por comas                                          | *null*                                        | Ejemplo: `prod,dev`                                                                                                                                         |
| `SPRING_CLOUD_CONFIG_SERVER_NATIVE_SEARCHLOCATIONS`          | Rutas de búsqueda nativas para el servidor Spring Config                                                    | string   | Rutas de archivo separadas por comas                              | *null*                                        | Ejemplo: `file:///config,classpath:/defaults`                                                                                                               |
| `DISABLE_DEBUG`                                              | Deshabilitar el agente de depuración de la JVM                                                              | boolean  | `true`, `false`                                                   | `false`                                       | Si es `true`, añade `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:${DEBUG_PORT}`. `dt_socket`: el mecanismo de transporte (es decir, un socket TCP) usado para la conexión de depuración. `server=y` indica a la JVM que actúe como servidor de depuración (esperando a que se conecte un depurador). `suspend=n` significa “no pausar al inicio”: la aplicación se ejecutará inmediatamente y puede adjuntar el depurador en cualquier momento. (Si configura `suspend=y`, la JVM se pausará en la primera línea hasta que se adjunte un depurador). |
| `JAVA_OPTS`                                                  | Opciones adicionales de la JVM                                                                               | string   | Cualquier opción válida de la JVM                                 | *null*                                        | Ejemplo: `-Dfile.encoding=UTF-8`                                                                                                                             |
| `GRADLE_FLAGS`                                               | Flags del comando de Gradle                                                                                  | string   | Cualquier flag válido de Gradle                                   | `-no-daemon --info --refresh-dependencies`    | —                                                                                                                                                            |
| `DEBUG_MODE`                                                 | Habilitar el modo de depuración para la aplicación                                                          | boolean  | `true`, `false`                                                   | `false`                                       | —                                                                                                                                                            |

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.