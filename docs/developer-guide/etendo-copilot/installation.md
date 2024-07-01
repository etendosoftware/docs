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


### Instalation 

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
    COPILOT_PORT=5000
    OPENAI_API_KEY= ****
    ETENDO_HOST=http://your.etendo.instance/etendo
    ```

    | **Environment Variable**   | **Options**  | **Info** |
    | -------------------------- | -------------| -------- |
    | COPILOT_PORT           | `5000`   | **Required** The copilot port can be defined by the user |
    | OPENAI_API_KEY         | `***********************` | **Required** You can get it from [OpenAI API keys](https://platform.openai.com/account/api-keys){target="_blank"} if you use an own API key or get in touch with Etendo support team |
    | ETENDO_HOST            | `http://your.etendo.instance/etendo` | **Required** The URL of the Etendo system, this is where copilot will send the requests to communicate with the Etendo system. |


2. In addition, there are other **optional** variables to configure certain aspects of the copilot. If not specified, default values are used.
    
    | **Environment Variable**    | **Options**  | **Default**  | **Info** |
    | ----------------------------| -------------| -------------| -------- |
    | SYSTEM_PROMPT  | `String` | `"You are a very powerful assistant with a set of tools, which you will try to use for the requests made to you."` | The prompt that will be used to make the request to the agent and that will condition the response and behavior of the copilot.|
    | CONFIGURED_TOOLS_FILENAME | `JSON File name` | `tools_config.json` | The name of the file that contains the configuration of the enabled tools. |
    | DEPENDENCIES_TOOLS_FILENAME | `TOML File name` | `tools_deps.toml` | The name of the file that contains the configuration of the dependencies of the tools. |
    | COPILOT_IMAGE_TAG | `String` | `master` | The tag of the copilot docker image that will be used. |
    | COPILOT_PULL_IMAGE | `Boolean` | `true` | If true, the copilot docker image will be pulled from docker hub. If false, gradle will try to use the local image with the tag specified in COPILOT_IMAGE_TAG, but if it does not exist, it will be pulled from docker hub. |
    | COPILOT_DOCKER_CONTAINER_NAME | `String` | `etendo-default` | The name of the docker container that will be created to run the copilot docker image. |

3.  Onece the Copilot dependency was added and the variables configurated, in the terminal execute:
    
    ``` bash title="Terminal"
    ./gradlew setup
    ``` 
    To apply changes 

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```
    To complile the environment 

4. To download and run the latest copilot Docker image, execute:

    ``` bash title="Terminal"
    ./gradlew copilot.start
    ```

    !!! info 
        In the terminal Etendo Copilot will be running, and you can see the corresponding log, in case you want to return to the terminal you can exit with Ctrl + C, although the docker container will continue running. We recommend using [lazydocker](https://github.com/jesseduffield/lazydocker#installation){target="_blank"} or [Docker Desktop](https://www.docker.com/products/docker-desktop/){target="_blank"} for a simple and fast container management. 

    To stop the Copilot container you can run: 
    ``` bash title="Terminal"
    ./gradlew copilot.stop
    ```

6. Try Copilot in your Etendo instance. To configure an assistant to use Etendo Copilot, follow the [Assistant Configuration Guide](../../user-guide/etendo-copilot/setup.md){target="_blank"}.

