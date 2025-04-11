---
title: Developer Guide - Copilot Installation
tags:
    - Copilot
    - Install
    - IA
    - Infrastructure
    - Assistants
---

## Overview

This guide provides detailed instructions on how to get started with Etendo Copilot, an API that allows interaction with a bot capable of selecting the appropriate tools to respond to user queries. It includes the necessary requirements, instructions for adding dependencies, environment variable configurations, and steps to run Copilot on an Etendo Classic project. Additionally, it covers optional configurations to customize Copilot's behavior and provides links to detailed installation guides for required software.

## Requirements

1. Install Etendo Classic. For this, follow the [Etendo Installation Guide](../../getting-started/installation.md){target="_blank"}.
2. This project depends on the following tools:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: version `26.0.0` or higher.
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: version `2.26.0` or higher.
    - [Python 3](https://www.python.org/downloads/){target="_blank"} version `3.10`or higher.

!!!info
    The [Docker Management](../../developer-guide/etendo-classic/bundles/platform/docker-management.md) module, included as a dependency allows for the distribution of the infrastructure within Etendo modules, which include Docker containers for each service.

## Installation 
Etendo Copilot is distributed within the Copilot Extensions bundle, which in addition to including the Copilot Core functionality and infrastructure, includes default assistants and tools that can be used directly or compose their use in new wizards.  

!!! info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).


## Running Etendo Copilot

The simplest configuration we are going to follow as an example is to mount Copilot Dockerized and Tomcat running as a local service. Other configurations are detailed in the section, [Advanced Configurations](#advanced-configurations).

1. In `gradle.properties` file is necessary to add some environment variables as a mandatory requirement

    !!!info
        From Etendo Classic version [24.4.0](../../whats-new/release-notes/etendo-classic/release-notes.md) onwards the variables `ETENDO_HOST`, `COPILOT_HOST` and `ETENDO_HOST_DOCKER` are optional, in case they are defined they will overwrite the automatically generated variables.

    ```groovy title="gradle.properties"
    OPENAI_API_KEY= ****
    ETENDO_HOST=https://<Etendo URL>/<Context Path>
    ETENDO_HOST_DOCKER=http://host.docker.internal:<Tomcat Port>/<Context Path>
    COPILOT_HOST=<Copilot URL>
    COPILOT_PORT=<Copilot Port>

    docker_com.etendoerp.copilot=true
    ```

    | **Environment Variable**   | **Default**  | **Info** |
    | -------------------------- | -------------| -------- |
    | OPENAI_API_KEY         | `***********************` | **Required** You can use an [OPEN AI API Key](https://platform.openai.com/account/api-keys){target="_blank"} of your own, or you can contact the Etendo support team to obtain one.|
    | ETENDO_HOST            |  | **Optional** The URL of the Etendo system, this is where copilot will send the requests to communicate with the Etendo system. E.g: https://demo.etendo.cloud/etendo or http://localhost:8080/etendo |
    | ETENDO_HOST_DOCKER     |  | **Optional** The URL of the Etendo system, this is where copilot will send the requests to communicate with the Etendo system. This variable is used when the copilot is running in a docker container and the Etendo Instance is not accessible from a domain. |
    | COPILOT_HOST           | `localhost` | **Optional** The copilot host can be defined by the user. By default use `localhost` |
    | COPILOT_PORT           | `5005` | **Required** The copilot port can be defined by the user. By default use `5005` |
    | docker_com.etendoerp.copilot | `true` | **Required** Configuration variable for the Etendo Copilot container to be launched. |
    |ANTHROPIC_API_KEY      | `***********************` | **Optional** You can use an [ANTHROPIC API Key](https://docs.anthropic.com/en/api/getting-started){target="_blank"} of your own, or you can contact the Etendo support team to obtain one. Remember, its only necessary if you want to use Anthropic AI Models. |
    |DEEPSEEK_API_KEY      | `***********************` | **Optional** You can use an [DEEPSEEK API Key](https://deepseek.ai/){target="_blank"} of your own, or you can contact the Etendo support team to obtain one. Remember, its only necessary if you want to use DeepSeek AI Models. |

    !!! info
        The `ETENDO_HOST_DOCKER` variable is used when the copilot is running in a docker container and the Etendo Instance is not accessible from a domain. This is important because the copilot needs to communicate with the Etendo system to perform the necessary actions. For example, if Copilot is running into a docker container and the Etendo Instance is running locally, the `ETENDO_HOST` variable should be `http://localhost:8080/etendo` and the `ETENDO_HOST_DOCKER` variable should be `http://host.docker.internal:8080/etendo` if you are using Docker Desktop.
    
    !!! warning 
        If you are using docker via console, the `ETENDO_HOST_DOCKER` variable should be `http://172.17.0.1:8080/etendo`
   

2.  Once the Copilot Extensions Bundle dependency was added and the variables configurated, in the terminal execute the following command to apply the changes:

    ``` bash title="Terminal"
    ./gradlew setup
    ```

    Then, the copilot container needs to be created:
    ``` bash title="Terminal"
    ./gradlew resources.up
    ```

    And then recomplile the environment: 

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```
    
3. To start the copilot Docker image, execute:

    ``` bash title="Terminal"
    ./gradlew resources.up
    ```

    To stop the Copilot container you can run: 
    ``` bash title="Terminal"
    ./gradlew resources.stop
    ```

    Everytime a new tool is added or the enviorement variables change, it's necessary to delete and create the Copilot container again. Execute the following command to delete the container: 
    ``` bash title="Terminal"
    ./gradlew resources.down
    ```

    !!! warning 
        Be aware that resources.stop and resources.down will also affect other services configured in the etendo container

4. Try Copilot in your Etendo instance. To configure an assistant to use Etendo Copilot, follow the [Copilot Setup and Usage](../../user-guide/etendo-copilot/setup-and-usage.md){target="_blank"} guide.


## Advanced Configurations 

=== "Copilot & Tomcat Dockerized"

    The `com.etendoerp.tomcat` module enables the Dockerization of Tomcat within Etendo Classic. This module modifies Gradle tasks to automatically deploy the `WAR` file into the container when executing the `smartbuild` task.
    Follow the [Dockerized Tomcat Service](../../developer-guide/etendo-classic/bundles/platform/dockerized-tomcat-service.md) documentation to learn how to configure it.

    When using both services in docker, the enviorement variables should look like this:

    ```groovy title="gradle.properties"
    OPENAI_API_KEY= ****
    ETENDO_HOST=http://tomcat:<Docker Tomcat Port>/<Context Path>
    ETENDO_HOST_DOCKER=http://host.docker.internal:<Docker Tomcat Port>/<Context Path>
    COPILOT_HOST=copilot
    COPILOT_PORT=<Docker Copilot Port>

    docker_com.etendoerp.copilot=true
    docker_com.etendoerp.tomcat=true
    docker_com.etendoerp.tomcat_port=<Docker Tomcat Port>
    ```

=== "Copilot locally (for developing copilot only)"

    Requirements:
    
    - [Python](https://www.python.org/downloads/){target="_blank"} 3.10 or 3.11
    
    - [Poetry](https://pypi.org/project/poetry/){target="_blank"}

    We recommend usign PyCharm to run copilot locally. Download and install here [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/){target="_blank"}

    1. Open PyCharm, search for the copilot module and open it.
    ![](../../../assets/developer-guide/etendo-copilot/getting-started/Copilot_Local_1.png)


    2. Open the `Run.py` file, then add a new interpreter.
    ![](../../../assets/developer-guide/etendo-copilot/getting-started/Copilot_Local_2.png)
    ![](../../../assets/developer-guide/etendo-copilot/getting-started/Copilot_Local_3.png)


    3. Add a new configuration file and select Python
    ![](../../../assets/developer-guide/etendo-copilot/getting-started/Copilot_Local_4.png)
    ![](../../../assets/developer-guide/etendo-copilot/getting-started/Copilot_Local_5.png)


    4. Select the interpreter created before, in the script field select the `run.py` file and .env field select the `gradle.properties`
    ![](../../../assets/developer-guide/etendo-copilot/getting-started/Copilot_Local_6.png)
    
    
    5. Once done, open the PyCharm terminal and execute the following commands:
    ``` bash title="terminal"
    source venv/bin/activate
    poetry install
    ```

    6. Execute `Run.py` from PyCharm
    
### Developer Environment Variables

In addition, there are other **optional** variables to configure certain aspects of the copilot. If not specified, default values are used.
    
| **Environment Variable**    | **Options**  | **Default**  | **Info** |
| ----------------------------| -------------| -------------| -------- |
| COPILOT_DEBUG | `Boolean` | `false` | **Optional** If true, copilot will log additional messages in the console. |
| COPILOT_MAX_ITERATIONS | `Integer` | `100` | **Optional** Maximum number of interactions of agents. |
| COPILOT_EXECUTION_TIMEOUT | `Integer` | `0` | **Optional** Defines a timeout in the execution of an agent in seconds, by default 0 represents unlimited time. |
| COPILOT_STREAM_DEBUG | `Boolean` | `false` | **Optional** Enable debug mode in the copilot pop-up, to see the log while the response is being generated. |
| CONFIGURED_TOOLS_FILENAME | `JSON File name` | `tools_config.json` | **Optional** The name of the file that contains the configuration of the enabled tools. |
| DEPENDENCIES_TOOLS_FILENAME | `TOML File name` | `tools_deps.toml` | **Optional** The name of the file that contains the configuration of the dependencies of the tools. |
| COPILOT_PULL_IMAGE | `Boolean` | `true` | **Optional** If true, the copilot docker image will be pulled from docker hub. If false, gradle will try to use the local image with the tag specified in COPILOT_IMAGE_TAG, but if it does not exist, it will be pulled from docker hub. |
| COPILOT_IMAGE_TAG | `String` | `master` | **Optional** The tag of the copilot docker image that will be used. |
| COPILOT_PORT_DEBUG | `String` | `5100` | **Optional** The copilot debug port can be defined by the user. |

