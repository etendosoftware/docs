---
tags:
  - Docker
  - Management
  - Infrastructure
---

# Docker Management

## Overview

Docker is a platform that enables developers to automate the deployment, scaling, and management of applications. It uses containerization technology, which packages an application and its dependencies into a standardized unit called a "container." Containers can run consistently across different computing environments, making them highly portable and efficient.

The `com.etendoerp.docker` module enables the use of Dockerized containers in Etendo Classic. This allows for the distribution and encapsulation of new functionalities using Etendo's existing module infrastructure. It also provides the capability to Dockerize the database, Tomcat, or any current or future Etendo infrastructure dependencies. Also, the module includes Gradle tasks to manage containers.

!!! Info 
    This module includes the infrastructure for container management and the Postgres database service, as an example. In case you want to run other services, add the corresponding modules that implement the dockerization.  

Additionally, the infrastructure could be extended, and allows other modules to include in it their own specific containers within each module.  This module operates incrementally, and there are additional modules that extend functionality using the same format.

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](https://docs.etendo.software/latest/whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

## Requirements

- [Docker](https://docs.docker.com/get-docker/){target="_blank"}
- [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}

## Using Containers Distributed in Modules

  It is necessary to include at least one configuration variable for each module to be launched, this variable enables all the services related to the module to be started.

  `docker_<javapackage>=true`
  
  
  Example:
  ``` groovy title="gradle.properties"
  docker_com.etendoerp.docker=true
  ```

  Finally, to apply changes, execute 

  ``` bash title="Terminal"
  ./gradlew setup
  ```

## Tasks to Manage Containers

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