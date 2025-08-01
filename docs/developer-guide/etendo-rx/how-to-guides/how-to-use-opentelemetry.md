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
# How to Use OpenTelemetry (BETA)

!!! warning  "IMPORTANT:THIS IS A BETA VERSION"
    - It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**, especially in production environments.
    - It should be used with **caution**, and you should always **validate backups** before executing any critical operation.

## Overview

OpenTelemetry is an open-source observability framework that defines a set of vendor-neutral APIs, SDKs, and instrumentation libraries for generating, collecting, and exporting telemetry data—namely **traces**, **metrics**, and **logs**. It provides a consistent programming model across applications and services, enabling you to capture detailed runtime behavior without coupling to any specific back end.

## Key Concepts

- **Span**: A single unit of work or operation, such as a database query or an HTTP request.
- **Trace**: A tree of spans representing an end-to-end request flow through multiple services.
- **Context Propagation**: The mechanism by which trace context (trace ID, span ID, baggage) is passed along asynchronous or remote calls.

## Why Use OpenTelemetry

- **Standardization**: Write instrumentation once; switch or combine back-ends at will.
- **End-to-End Visibility**: Correlate distributed operations across microservices, threads, and async boundaries.
- **Performance Analysis**: Identify latency hotspots, error rates, and service dependencies.
- **Extensibility**: Plug in custom exporters, processors, and samplers to fit your needs.

## Sending Traces to a Back End

1. **Instrument Your Code**
   - Add the OpenTelemetry Java SDK (or auto-injection agent) to your Rx-based services.
   - Create spans around critical operations (e.g., upstream requests, reactive pipelines like `Flux`/`Mono`).

2. **Configure an Exporter**
   - Use the **Jaeger exporter** provided by OpenTelemetry to batch and send spans over UDP or HTTP.
   - Point the exporter at your Jaeger collector’s address and port.

3. **Propagate Context**
   - Ensure that each downstream call carries the current trace context so that spans nest correctly.

## Jaeger: Distributed Tracing Back End

Jaeger is an open-source distributed tracing system originally developed by Uber. It provides:

- **Collector**: Receives spans from instrumented applications.
- **Storage**: Persists trace data (e.g., in Elasticsearch or Cassandra).
- **Query Service & UI**: Allows developers and operators to search, visualize, and analyze traces in real time.

## Prerequisites

1. Install Etendo Rx. For this, follow the [Etendo Rx installation guide](../getting-started.md).
2. Install the [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}.
3. This project depends on the following tools:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: version `26.0.0` or higher.
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: version `2.26.0` or higher.

## Step 1: Configure Jaeguer Service

1. **Enable Utils Services**: Enable the necessary util service modules.In the `gradle.properties` file, add the following variable:

``` groovy title="gradle.properties"
docker_com.etendoerp.etendorx_utils=true
```

Once the Rx utils service is enabled, execute the following command in your terminal:

```bash
./gradlew resources.up
```

This will launch the Docker container running Jaeger. To access the Jaeger UI, navigate to `http://localhost:16686`

![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-rx.png)

Initially, there will be no services exporting data to Jaeger. In the next step, we will cover how to enable trace export to Jaeger.

2. **Dynamic Das Services**: Services based on the Dynamic Das Docker image; currently, the only service using this image is `das`.
To enable and configure trace export to Jaeger, edit the `com.etendoerp.etendorx.yml` file in the Rx module’s `compose` directory, updating the following environment variables:

In the das service section, set the environment variables as follows:

   ```com.etendoerp.etendorx.yml
      - ENABLE_OPEN_TELEMETRY=true
      - OTEL_SERVICE_NAME=das
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4318
   ```

   Once enabled opentelemetry in Das service, execute the following command in your terminal:

   ```bash
   ./gradlew resources.up
   ```

   - This configuration enables trace export from the Das service to the Jaeger back end. Now, in the Jaeger UI, this service will be selectable.

   ![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-das.png)

!!! warning
    This functionality is only available starting from the `etendo/dynamic-das:1.1.0` image. For more information, see [Dynamic DAS v1.1.0](../getting-started.md/#dynamic-das-v110).

3. **Dynamic Gradle Services**:Services based on the Dynamic Gradle Docker image currently are `config`, `edge`, `auth`, `asyncprocess`, `obconnsrv` and `worker`.
To enable and configure trace export to Jaeger, edit the `com.etendoerp.etendorx.yml` file in the Rx module’s `compose` directory, updating the following environment variables:

In the config service section, set the environment variables as follows:

   ```com.etendoerp.etendorx.yml
      - ENABLE_OPEN_TELEMETRY=true
      - OTEL_SERVICE_NAME=das
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4318
   ```
In the edge service section, set the environment variables as follows:

   ```com.etendoerp.etendorx.yml
      - ENABLE_OPEN_TELEMETRY=true
      - OTEL_SERVICE_NAME=das
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4318
   ```
In the auth service section, set the environment variables as follows:

   ```com.etendoerp.etendorx.yml
      - ENABLE_OPEN_TELEMETRY=true
      - OTEL_SERVICE_NAME=das
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4318
   ```

To configure the `asyncprocess`, `obconnsrv`, and `worker` services, apply the same environment settings in their respective configuration files:

   - `com.etendoerp.etendorx_async.yml`
   - `com.etendoerp.etendorx_connector.yml`

   Once OpenTelemetry is enabled on any of these services, execute the following command in your terminal:

   ```bash
   ./gradlew resources.up
   ```

   - This configuration enables trace export from these services to the Jaeger back end. Now, in the Jaeger UI, these services will be selectable.

   ![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-edge.png)

!!! warning
    This functionality is only available starting from the `etendo/dynamic-gradle:1.1.0` image. For more information, see [Dynamic Gradle v1.1.0](../getting-started.md/#dynamic-gradle-v110).

3. **Tomcat**:The Tomcat service can be configured to send traces to Jaeger. In the `gradle.properties` file, add the following variable:

   ``` groovy title="gradle.properties"
   otel_com.etendoerp.tomcat=true
   ```

   Once enabled opentelemetry in Tomcat service, execute the following command in your terminal:

   ```bash
   ./gradlew resources.up
   ```

   - This configuration enables trace export from the Das service to the Jaeger back end. Now, in the Jaeger UI, this service will be selectable.

   ![](../../../assets/developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry/jaeger-tomcat.png)

### Conclusion

OpenTelemetry and Jaeger together form a powerful observability stack for Etendo Rx microservices. By instrumenting your reactive pipelines with OpenTelemetry, you capture detailed spans and traces across asynchronous boundaries. Exporting this telemetry to Jaeger’s collector and UI gives you real-time visibility into request flows, enabling rapid identification of errors, latency hotspots, and service dependencies. As a result, developers can accelerate feature delivery, improve system reliability, and proactively troubleshoot performance issues in complex distributed environments.
