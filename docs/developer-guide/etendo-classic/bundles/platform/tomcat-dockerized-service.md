---
tags:
  - Docker
  - Tomcat
  - Service
  - Infrastructure
---

# Dockerized Tomcat Service
:octicons-package-16: Javapackage: `com.etendoerp.tomcat`

## Overview

The `com.etendoerp.tomcat` module enables the Dockerization of Tomcat within Etendo Classic. This module modifies Gradle tasks to automatically deploy the WAR file into the container when executing the `smartbuild` task.

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](https://docs.etendo.software/latest/whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

## Configuration Variables

To enable and configure the Tomcat service, the following configuration variables are available:

- **Enable the Service**

  ```groovy title="gradle.properties"
  docker_com.etendoerp.tomcat=true
  ```
  This variable enables the Tomcat service.


- **Configure Tomcat Port** (Optional)
    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat_port=<port>
    ```
    This variable sets the port for the Tomcat service. The default port is `8080`

- **Configure Debug Port** (Optional)

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat_debug=<debug_port>
    ```
    This variable sets the debug port for the Tomcat service. The default debug port is `8009`

    !!! info
            For debugging in IntelliJ, create a new configuration of type **Remote JVM Debug** and set the port to listen on.

            ![Debug-Mode.png](../../../../assets/developer-guide/etendo-classic/bundles/platform/tomcat-dockeridez-service/debug-mode.png)


Execute the following command to apply the configuration changes:

```groovy title="Terminal"
./gradlew setup
```

## Compile the Environment

- The first time Tomcat is used within a Docker environment, the setup must be compiled by executing:
    
    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild
    ```

    This command will update the database and recompile the java classes and deploy the `WAR` to the dockerized Tomcat service. 

      !!! info
       This module modifies **Gradle tasks**. Executing the `update.database` command will automatically stop the Tomcat service. The `smartbuild` task will then ensure that the WAR file is correctly deployed in the container. After the smartbuild execution, the service will automatically restart, enabling an automated compilation from the command line.
         


- Finally, the container should be launched, following the commands documented in [Gradle Tasks to Manage Containers](./docker-management.md#gradle-tasks-to-manage-containers) section in Docker Management page.