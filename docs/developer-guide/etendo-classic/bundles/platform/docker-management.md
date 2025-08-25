---
tags:
  - Docker
  - Management
  - Infrastructure
---

# Docker Management

:octicons-package-16: Javapackage: `com.etendoerp.docker`

## Overview

[Docker](https://docs.docker.com/){target=_isblank} is a platform that enables developers to automate the deployment, scaling, and management of applications. It uses containerization technology, which packages an application and its dependencies into a standardized unit called a **container**. Containers can run consistently across different computing environments, making them highly portable and efficient.

The `com.etendoerp.docker` module enables the use of Dockerized containers in Etendo Classic. This allows for the distribution and encapsulation of new functionalities using Etendo's existing module infrastructure. It also provides the capability to Dockerize the database, Tomcat, or any current or future Etendo infrastructure dependencies. Also, the module includes Gradle tasks to manage containers.

!!! Info 
    This module includes the infrastructure for container management and the Postgres database service, as an example. In case you want to run other services, add the corresponding modules that implement the dockerization.  

Additionally, the infrastructure could be extended, and allows other modules to include in it their own specific containers.

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](https://docs.etendo.software/latest/whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

## Requirements

This project depends on the following tools:

- [Docker](https://docs.docker.com/get-docker/){target="_blank"}: version `26.0.0` or higher.
- [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: version `2.26.0` or higher.

## Using Containers Distributed in Modules

### Configuration Variables

  - It is necessary to include at least one configuration variable for each module to be launched, this variable enables all the services related to the module to be started.
    
    `docker_<javapackage>=true`
    
    
    Example:
    ``` groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    ```

  - In case you want to configure only one service belonging to a module, it is possible by adding a variable with the format:

    `docker_<javapackage>_<service>=true`

    Example:
    ``` groovy title="gradle.properties"
    docker_com.etendoerp.docker_db=true
    ```
    !!!note
        In this case, only the database service will be taken into account when raising and lowering services related to the `com.etendoerp.docker` module. 
    
  - It is also possible that some services may require configuration variables, in which case they should be added: 

    `docker_<javapackage>_<variable>=<value>`

    Example:
    ``` groovy title="gradle.properties"
    docker_com.etendoerp.tomcat_debug=8009
    ``` 
    !!!note
        In this example, this variable configures the [Dockerized Tomcat Service](./tomcat-dockerized-service.md) module port, although the necessary configurations will be included in the documentation of each module.

  Finally, always to apply changes, execute 

  ``` bash title="Terminal"
  ./gradlew setup
  ```

## Gradle Tasks to Manage Containers
Execute the following command to use the infrastructure:

### Running

``` bash title="Terminal"
./gradlew resources.up
```
This command will search for all configured resources and start the containers.

!!! note 
    If you only have the base `com.etendoerp.docker` module installed and configured, this command will start a PostgreSQL database.

### Stopping
``` bash title="Terminal"
./gradlew resources.stop
```
This command will stop the containers.

### Down

``` bash title="Terminal"
./gradlew resources.down
```
This command will stop and remove the containers.


## Verifying the Status

To verify the status of the resources started by Docker Compose, you can use the following Docker commands:

`docker ps`

This command lists all running Docker containers. You should see the containers related to Etendo

`docker compose logs`

This command shows the logs of all the services defined in your Docker Compose configuration, which can help in troubleshooting and verifying that the services are running correctly.

It is also possible to manage containers with tools such as [Lazydocker](https://github.com/jesseduffield/lazydocker#installation){target=_isblank} or [Docker Desktop](https://www.docker.com/products/docker-desktop/){target=_isblank}.


## Postgres Database Service

In this module a Postgres database service is included, this allows to use the dockerized database in Etendo. To use it the following steps must be followed:

1. Once the `com.etendoerp.docker` module is installed, it is necessary to add a configuration variable in the `gradle.properties` to enable the use of the service:

    ``` groovy title="gradle.properties"
    docker_com.etendoerp.docker_db=true
    ```

2. Then it is necessary to run `./gradlew setup`, to apply the configuration changes.

3. When `./gradlew resources.up` is executed, a new Docker container with the database service will be raised using the configuration variables defined in the `gradle.properties`, such as port, user, password, etc. 

    !!! warning
        In case you have the same service running locally on the same port it should be down. 

4. Finally, using this service it is possible to run `./gradlew install` to install the database from scratch, or it is possible to restore a backup and start using the new dockerized database service. 

