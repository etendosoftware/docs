---
title: Getting Started
---

## Overview

This guide will help you set up Etendo, including both the Etendo Classic functionalities and Etendo RX, our reactive platform capable of executing microservices with database interaction and asynchronous actions.

Follow these steps for a smooth installation:

## Requirements

1. Install Etendo Classic. For this, follow the [Etendo Classic installation guide](../../getting-started/installation.md).

2. Install the [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}.

## Dockerized Services

We need to add some variables to define which services will be dockerized. The options are Tomcat, the database and Etendo RX.

- RX: `docker_com.etendoerp.etendorx=true`

!!!warning
    To be able to run this process, remember Docker must be installed.

```groovy title="gradle.properties"
docker_com.etendoerp.etendorx=true
docker_com.etendorx.psd2.bank.integration=true
```

!!!info
    For more information about how to handle Etendo Dockerizations, visit [Docker Management](../platform/dependency-manager.md). 

??? Note "Tomcat and PostgresSQL Dockerized (Optional)"
    It is also possible to run the dockerized [PostgreSQL service](../platform/docker-management.md#postgres-database-service) and [Tomcat service](../platform/tomcat-dockerized-service.md), **optionally** adding the [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank} and the following configuration variables:

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    docker_com.etendoerp.docker_db=true
    ```

    If you want to debug Tomcat locally with IntelliJ, visit [Tomcat Dockerized Service](../../developer-guide/etendo-classic/bundles/platform/tomcat-dockerized-service.md).

Then, to effectively run the services is necessary to **execute the command** in the terminal: 

```bash title="Terminal"
./gradlew resources.up
```

Here, all the services and their respective logs can be seen running using [LazyDocker tool](https://github.com/jesseduffield/lazydocker){target=_isblank}.

![Docker Services](../../../../assets/developer-guide/etendo-classic/bundles/financial/psd2-integration/tech-doc-psd2-integration-9.png)



By default, the following services should be up and running:

- Config
- Auth
- Edge
- Das

!!! success
    You have successfully set up the Etendo RX services. Continue your learning journey by visiting our [Creating a New Microservice section in the developer guide](../../developer-guide/etendo-rx/tutorials/creating-a-new-microservice.md).