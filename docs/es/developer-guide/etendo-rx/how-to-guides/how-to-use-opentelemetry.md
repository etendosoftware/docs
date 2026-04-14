---
tags:
  - Etendo Rx
  - Docker
  - OpenTelemetry
  - Tomcat
  - Dynamic Das
  - Dynamic Gradle
status: beta
---
# Cómo usar OpenTelemetry (BETA)

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    - Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**, especialmente en entornos de producción.
    - Debe utilizarse con **precaución**, y siempre debe **validar las copias de seguridad** antes de ejecutar cualquier operación crítica.
## Visión general

OpenTelemetry es un framework de observabilidad de código abierto que define un conjunto de API, SDK y bibliotecas de instrumentación neutrales respecto al proveedor para generar, recopilar y exportar datos de telemetría; concretamente **trazas**, **métricas** y **logs**. Proporciona un modelo de programación coherente entre aplicaciones y servicios, lo que le permite capturar un comportamiento detallado en tiempo de ejecución sin acoplarse a ningún back end específico.

OpenTelemetry y Jaeger, en conjunto, forman una potente pila de observabilidad para los microservicios de Etendo Rx. Al instrumentar sus canalizaciones reactivas con OpenTelemetry, captura spans y trazas detalladas a través de límites asíncronos. Exportar esta telemetría al collector y a la UI de Jaeger le ofrece visibilidad en tiempo real de los flujos de solicitudes, lo que permite identificar rápidamente errores, puntos críticos de latencia y dependencias entre servicios. Como resultado, los desarrolladores pueden acelerar la entrega de funcionalidades, mejorar la fiabilidad del sistema y solucionar de forma proactiva problemas de rendimiento en entornos distribuidos complejos.

### Conceptos clave

- **Span**: Una única unidad de trabajo u operación, como una consulta a base de datos o una solicitud HTTP.
- **Trace**: Un árbol de spans que representa un flujo de solicitud de extremo a extremo a través de múltiples servicios.
- **Propagación de contexto**: El mecanismo mediante el cual el contexto de la traza (ID de traza, ID de span, baggage) se transmite a lo largo de llamadas asíncronas o remotas.

### Envío de trazas al servicio OpenTelemetry

1. **Instrumente su código**
    - Añada el SDK de OpenTelemetry para Java (o el agente de inyección automática) a sus servicios basados en Rx.
    - Cree spans alrededor de operaciones críticas (p. ej., solicitudes upstream, canalizaciones reactivas como `Flux`/`Mono`).

2. **Configure un exportador**
    - Utilice el **exportador de Jaeger** proporcionado por OpenTelemetry para agrupar y enviar spans mediante `UDP` o `HTTP`.
    - Apunte el exportador a la dirección y el puerto del collector de Jaeger.

3. **Propague el contexto**
    - Asegúrese de que cada llamada downstream transporte el contexto de traza actual para que los spans se aniden correctamente.

### Jaeger: back end de trazado distribuido

Jaeger es un sistema de trazado distribuido de código abierto desarrollado originalmente por Uber. Proporciona:

- **Collector**: Recibe spans de las aplicaciones instrumentadas.
- **Almacenamiento**: Persiste los datos de trazas (p. ej., en Elasticsearch o Cassandra).
- **Servicio de consulta y UI**: Permite a desarrolladores y operadores buscar, visualizar y analizar trazas en tiempo real.
## Requisitos previos

1. Instale Etendo Rx. Para ello, siga la [guía de instalación de Etendo Rx](../getting-started.md).
2. Instale el [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}.
3. Este proyecto depende de las siguientes herramientas:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: versión `26.0.0` o superior.
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: versión `2.26.0` o superior.

    !!! warning
        Evite instalar Docker mediante [Snap](https://snapcraft.io){target="_blank"}, ya que puede estar restringido por este sandbox y no tener acceso a directorios del host como `/opt/`, lo que puede impedir que los contenedores Docker de Etendo se inicien correctamente.
    
        Recomendación: instale Etendo utilizando la [última ISO](../../../whats-new/release-notes/etendo-classic/iso.md) (que incluye Docker) o instale Docker siguiendo la guía de instalación oficial de su distribución.
## Configurar el servicio Jaeger

1. **Habilitar servicios Utils**: habilite los módulos de servicios util necesarios. En el archivo `gradle.properties`, añada la siguiente variable:

    ``` groovy title="gradle.properties"
    docker_com.etendoerp.etendorx_utils=true
    ```

    Una vez habilitado el servicio de utilidades de Rx, ejecute el siguiente comando en su terminal:

    ```bash
    ./gradlew resources.up
    ```

    Esto iniciará el contenedor Docker que ejecuta Jaeger. Para acceder a la **UI de Jaeger**, navegue a [http://localhost:16686](http://localhost:16686)

    ![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-rx.png)

    Inicialmente, no habrá servicios exportando datos a Jaeger. En el siguiente paso, se explicará cómo habilitar la exportación de trazas a Jaeger.

2. **Servicios Dynamic Das**: servicios basados en la imagen Docker de Dynamic Das; actualmente, el único servicio que utiliza esta imagen es `das`. Para habilitar y configurar la exportación de trazas a Jaeger, edite el archivo `gradle.properties` añadiendo la siguiente variable:

    ``` groovy title="gradle.properties"
    otel.das.enable=true
    ```

    Opcionalmente, puede añadir propiedades adicionales al archivo `gradle.properties` para configurar con más detalle el agente de OpenTelemetry en el servicio DAS.

    | Nombre | Descripción | Tipo | Valores permitidos | Valor por defecto | Notas |
    |-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `otel.das.name`                                              | Nombre del servicio Das                                                           | string   |                                                  | *das*                                       |                                                                                                                                                             |
    | `otel.das.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.das.otlp.protocol`                                              | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.das.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.das.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.das.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.das.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |


    Una vez que OpenTelemetry esté habilitado en el servicio Das, ejecute el siguiente comando en su terminal:

    ```bash
    ./gradlew resources.up
    ```

    Esta configuración habilita la exportación de trazas desde el servicio Das al back end de Jaeger. Ahora, en la UI de Jaeger, este servicio se podrá seleccionar.

    ![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-das.png)

    !!! warning
        Esta funcionalidad solo está disponible a partir de la imagen `etendo/dynamic-das:1.1.0`. Para más información, consulte [Dynamic DAS v1.1.0](../getting-started.md/#dynamic-das-v110).

3. **Servicios Dynamic Gradle**: los servicios basados en la imagen Docker de Dynamic Gradle actualmente son `config`, `edge`, `auth`, `asyncprocess`, `obconnsrv` y `worker`.
    Para habilitar y configurar la exportación de trazas a Jaeger, añada las variables que considere necesarias al archivo `gradle.properties`:

    ``` groovy title="gradle.properties"
    otel.config.enable=true
    otel.edge.enable=true
    otel.auth.enable=true
    otel.asyncprocess.enable=true
    otel.obconnsrv.enable=true
    otel.worker.enable=true
    ```

    Opcionalmente, puede añadir propiedades adicionales al archivo `gradle.properties` para configurar con más detalle el agente de OpenTelemetry en cada servicio.

    | Nombre | Descripción | Tipo | Valores permitidos | Valor por defecto | Notas |
    |-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `otel.config.name`                                              | Nombre del servicio Config                                                           | string   |                                                  | *config*                                       |                                                                                                                                                             |
    | `otel.config.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.config.otlp.protocol`                                           | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.config.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.config.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.config.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.config.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
    | `otel.edge.name`                                              | Nombre del servicio Edge                                                           | string   |                                                  | *edge*                                       |                                                                                                                                                             |
    | `otel.edge.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.edge.otlp.protocol`                                           | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.edge.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.edge.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.edge.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.edge.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
    | `otel.auth.name`                                              | Nombre del servicio Auth                                                           | string   |                                                  | *auth*                                       |                                                                                                                                                             |
    | `otel.auth.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.auth.otlp.protocol`                                           | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.auth.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.auth.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.auth.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.auth.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
    | `otel.asyncprocess.name`                                              | Nombre del servicio Asyncprocess                                                           | string   |                                                  | *asyncprocess*                                       |                                                                                                                                                             |
    | `otel.asyncprocess.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.asyncprocess.otlp.protocol`                                           | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.asyncprocess.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.asyncprocess.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.asyncprocess.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.asyncprocess.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
    | `otel.obconnsrv.name`                                              | Nombre del servicio Obconnsrv                                                           | string   |                                                  | *obconnsrv*                                       |                                                                                                                                                             |
    | `otel.obconnsrv.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.obconnsrv.otlp.protocol`                                           | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.obconnsrv.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.obconnsrv.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.obconnsrv.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.obconnsrv.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |
    | `otel.worker.name`                                              | Nombre del servicio Worker                                                           | string   |                                                  | *worker*                                       |                                                                                                                                                             |
    | `otel.worker.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.worker.otlp.protocol`                                           | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.worker.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.worker.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.worker.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.worker.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |

    Una vez que OpenTelemetry esté habilitado en cualquiera de estos servicios, ejecute el siguiente comando en su terminal:

    ```bash
    ./gradlew resources.up
    ```

    Esta configuración habilita la exportación de trazas desde estos servicios al back end de Jaeger. Ahora, en la UI de Jaeger, estos servicios se podrán seleccionar.

    ![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-edge.png)

    !!! warning
        Esta funcionalidad solo está disponible a partir de la imagen `etendo/dynamic-gradle:1.1.0`. Para más información, consulte [Dynamic Gradle v1.1.0](../getting-started.md/#dynamic-gradle-v110).

4. **Tomcat**: el servicio Tomcat se puede configurar para enviar trazas a Jaeger. En el archivo `gradle.properties`, añada la siguiente variable:

    ``` groovy title="gradle.properties"
    otel.tomcat.enable=true
    ```

    Opcionalmente, puede añadir propiedades adicionales al archivo `gradle.properties` para configurar con más detalle el agente de OpenTelemetry en el servicio Tomcat.

    | Nombre | Descripción | Tipo | Valores permitidos | Valor por defecto | Notas |
    |-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `otel.tomcat.name`                                              | Nombre del servicio Tomcat                                                           | string   |                                                  | *tomcat*                                       |                                                                                                                                                             |
    | `otel.tomcat.otlp.endpoint`                                              | string   | Cualquier URL                                                             | `http://jaeger:4318`                         | Añade automáticamente `/v1/traces\|metrics\|logs}` en función del tipo de señal                                                                             |
    | `otel.tomcat.otlp.protocol`                                              | Protocolo de transporte para OTLP                                                                              | enum     | `grpc`, `http/protobuf`, `http/json`                                | `http/protobuf`                              | —                                                                                                                                                            |
    | `otel.tomcat.otlp.timeout`                                              | Tiempo de espera (ms) para la exportación de datos OTLP (trazas, métricas, logs)                                                | integer  | Cualquier número positivo                                                 | `10000`                                      | —                                                                                                                                                            |
    | `otel.tomcat.metrics.exporter`                                              | Exportador de métricas                                                                                         | enum     | `otlp`, `prometheus`, `console`, `logging`, `none`                  | `none`                                       | —                                                                                                                                                            |
    | `otel.tomcat.logs.exporter`                                              | Exportador de logs                                                                                            | enum     | `otlp`, `console`, `logging`, `none`                                | `none`                                       | —                                                                                                                                                            |
    | `otel.tomcat.traces.exporter`                                              | Exportador de trazas                                                                                          | enum     | `otlp`, `zipkin`, `console`, `logging`, `none`                      | `otlp`                                       | —                                                                                                                                                            |

    Una vez que OpenTelemetry esté habilitado en el servicio Tomcat, ejecute el siguiente comando en su terminal:

    ```bash
    ./gradlew resources.up
    ```

    Esta configuración habilita la exportación de trazas desde el servicio Tomcat al back end de Jaeger. Ahora, en la UI de Jaeger, este servicio se podrá seleccionar.

    ![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-tomcat.png)

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.