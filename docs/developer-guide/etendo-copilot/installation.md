---
title: Copilot Installation
tags:
    - Etendo Copilot
    - Copilot Core
    - IA
    - Infrastructure
    - Chat
    - Assistants
---
## Overview

This guide provides detailed instructions on how to get started with Etendo Copilot, an API that allows interaction with a bot capable of selecting the appropriate tools to respond to user queries. It includes the necessary requirements, instructions for adding dependencies, environment variable configurations, and steps to run Copilot on an Etendo Classic project. Additionally, it covers optional configurations to customize Copilot's behavior and provides links to detailed installation guides for required software.

## Etendo Copilot
:octicons-package-16: Javapackage: `com.etendoerp.copilot`

### Requirements
- *Etendo Classic*. If you do not have it, you can install it using the [Etendo Installation Developer Guide](../../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md){target="_blank"}.
- *Python* version ^3.10, to install it follow [The Official Installation Guide](https://www.python.org/downloads/){target="_blank"}.
- *Docker* to install it follow [The Official Installation Guide](https://docs.docker.com/get-docker/){target="_blank"}.
- *Docker Management module.* you can install it by following the guide on [Docker Management](../../developer-guide/etendo-classic/bundles/platform/docker-management.md)

!!!info
    The [Docker Management](../../developer-guide/etendo-classic/bundles/platform/docker-management.md) module allows for the distribution of the infrastructure needed to configure Etendo Classic within Etendo modules, which include Docker containers for each service. Specifically, the Docker Management module includes the [PostgreSQL Database Service](../../developer-guide/etendo-classic/bundles/platform/docker-management.md#postgres-database-service) and the [Dockerized Tomcat Service](../../developer-guide/etendo-classic/bundles/platform/dockerized-tomcat-service.md) module.

### Installation 

This module is included in the Copilot Extensions bundle

!!! info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).


In addition, you can install only the module containing the **Etendo Copilot** by following the guide on [How to install modules in Etendo](../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md), looking for the GitHub Package `com.etendoerp.copilot`.

!!! warning "Ensure you have 1.3.2 plugin version or greater:"        
    ```groovy title="build.gradle"
    id 'com.etendoerp.gradleplugin' version '1.3.2'
    ```

### Run Etendo Copilot

1. In `gradle.properties` file is necessary to add some environment variables as a mandatory requirement


    ```groovy title="gradle.properties"
    COPILOT_HOST=localhost
    COPILOT_PORT=5005
    OPENAI_API_KEY= ****
    ETENDO_HOST=http://your.etendo.instance/etendo
    ```

    | **Environment Variable**   | **Default**  | **Info** |
    | -------------------------- | -------------| -------- |
    | COPILOT_HOST           | `localhost` | **Required** The copilot port can be defined by the user. |
    | COPILOT_PORT           | `5005` | **Required** The copilot port can be defined by the user. |
    | OPENAI_API_KEY         | `***********************` | **Required** You can use an [OPEN AI API Key](https://platform.openai.com/account/api-keys){target="_blank"} of your own, or you can contact the Etendo support team to obtain one.|
    | ETENDO_HOST            | `http://your.etendo.instance/etendo` | **Required** The URL of the Etendo system, this is where copilot will send the requests to communicate with the Etendo system. |
    | ETENDO_HOST_DOCKER     |  | **Optional** The URL of the Etendo system, this is where copilot will send the requests to communicate with the Etendo system. This variable is used when the copilot is running in a docker container and the Etendo Instance is not accessible from a domain. |
    !!! info
        The `ETENDO_HOST_DOCKER` variable is used when the copilot is running in a docker container and the Etendo Instance is not accessible from a domain. This is important because the copilot needs to communicate with the Etendo system to perform the necessary actions. For example, if Copilot is running into a docker container and the Etendo Instance is running locally, the `ETENDO_HOST` variable should be `http://localhost:8080/etendo` and the `ETENDO_HOST_DOCKER` variable should be `http://host.docker.internal:8080/etendo`. Its recommended to access to the Docker Container shell and check the network configuration to get the correct IP address.

    2. In addition, there are other **optional** variables to configure certain aspects of the copilot. If not specified, default values are used.
    
    | **Environment Variable**    | **Options**  | **Default**  | **Info** |
    | ----------------------------| -------------| -------------| -------- |
    | SYSTEM_PROMPT  | `String` | `"You are a very powerful assistant with a set of tools, which you will try to use for the requests made to you."` | The prompt that will be used to make the request to the agent and that will condition the response and behavior of the copilot.|
    | CONFIGURED_TOOLS_FILENAME | `JSON File name` | `tools_config.json` | The name of the file that contains the configuration of the enabled tools. |
    | DEPENDENCIES_TOOLS_FILENAME | `TOML File name` | `tools_deps.toml` | The name of the file that contains the configuration of the dependencies of the tools. |
    | COPILOT_PULL_IMAGE | `Boolean` | `true` | If true, the copilot docker image will be pulled from docker hub. If false, gradle will try to use the local image with the tag specified in COPILOT_IMAGE_TAG, but if it does not exist, it will be pulled from docker hub. |
    | COPILOT_IMAGE_TAG | `String` | `master` | The tag of the copilot docker image that will be used. |
    | COPILOT_DEBUG | `Boolean` | `false` | If true, copilot will log additional messages in the console. |
    | COPILOT_PORT_DEBUG | `String` | `5100` | The copilot debug port can be defined by the user. |

3.  Once the Copilot dependency was added and the variables configurated, in the terminal execute:
    
    ``` bash title="Terminal"
    ./gradlew setup
    ``` 
    To apply changes 

    ``` bash title="Terminal"
    ./gradlew smartbuild --info
    ```
    To complile the environment 

4. To download and run the latest copilot Docker image, execute:

    ``` bash title="Terminal"
    ./gradlew resources.up
    ```

    To stop the Copilot container you can run: 
    ``` bash title="Terminal"
    ./gradlew resources.stop
    ```

    !!! warning 
        Be aware that if you are running other services, it will stop all of them

5. Try Copilot in your Etendo instance. To configure an assistant to use Etendo Copilot, follow the [Copilot Setup and Usage](../../user-guide/etendo-copilot/setup-and-usage.md){target="_blank"}.

