---
title: Copilot Installation
tags:
    - Copilot
    - IA
    - Machine Learning
---
## Overview

The getting started guide for the Copilot API is a tool that allows interaction with a bot that selects the appropriate tool to answer a query.

## Etendo Copilot
:octicons-package-16: Javapackage: `com.etendoerp.copilot`

### Requirements
- *Etendo Classic*. If you do not have it, you can install it using the [Etendo Installation Developer Guide](../../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md){target="_blank"}.
- *Python* version ^3.10, to install it follow [The Official Installation Guide](https://www.python.org/downloads/){target="_blank"}.
- *Docker* to install it follow [The Official Installation Guide](https://docs.docker.com/engine/install/)

### Run copilot locally

1. Add copilot dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot:1.2.4')
    ```

    ??? warning "Ensure you have 1.3.2 plugin version or greater:"
        
        ```groovy
        id 'com.etendoerp.gradleplugin' version '1.3.2'
        ```

2. In the terminal, execute:
    ``` bash title="Terminal"
    ./gradlew update.database smartbuild --info
    ```

3. In `gradle.properties` file is necessary to add some environment variables as a mandatory requirement


    ```groovy title="gradle.properties"
    COPILOT_PORT=5000
    OPENAI_API_KEY= ****
    ETENDO_HOST=http://your.etendo.instance/etendo
    ```

    | **Environment Variable**   | **Options**  | **Info** |
    | -------------------------- | -------------| -------- |
    | COPILOT_PORT           | `5000`   | **Required** The copilot port can be defined by the user |
    | OPENAI_API_KEY         | `***********************` | **Required** You can get it from [OpenAI API keys](https://platform.openai.com/account/api-keys){target="_blank"} |
    | ETENDO_HOST            | `http://your.etendo.instance/etendo` | **Required** The URL of the Etendo system, this is where copilot will send the requests to communicate with the Etendo system. |

4. In addition, there are other **optional** variables to configure certain aspects of the copilot. If not specified, default values are used.
    
    | **Environment Variable**    | **Options**  | **Default**  | **Info** |
    | ----------------------------| -------------| -------------| -------- |
    | SYSTEM_PROMPT  | `String` | `"You are a very powerful assistant with a set of tools, which you will try to use for the requests made to you."` | The prompt that will be used to make the request to the agent and that will condition the response and behavior of the copilot.|
    | CONFIGURED_TOOLS_FILENAME | `JSON File name` | `tools_config.json` | The name of the file that contains the configuration of the enabled tools. |
    | DEPENDENCIES_TOOLS_FILENAME | `TOML File name` | `tools_deps.toml` | The name of the file that contains the configuration of the dependencies of the tools. |
    | COPILOT_IMAGE_TAG | `String` | `master` | The tag of the copilot docker image that will be used. |
    | COPILOT_PULL_IMAGE | `Boolean` | `true` | If true, the copilot docker image will be pulled from docker hub. If false, gradle will try to use the local image with the tag specified in COPILOT_IMAGE_TAG, but if it does not exist, it will be pulled from docker hub. |
    | COPILOT_DOCKER_CONTAINER_NAME | `String` | `etendo-default` | The name of the docker container that will be created to run the copilot docker image. |

5. Remember to add this configurations in ```config/Openbravo.properties``` file or do a ```./gradlew setup``` to copy the properties automatically.

5. To download the latest copilot Docker image and run it:

    ``` bash title="Terminal"
    ./gradlew copilot.start
    ```

6. Try Copilot in your Etendo instance. To configure an assistant to use Copilot, follow the [Assistant Configuration Guide](../../user-guide/etendo-copilot/setup.md){target="_blank"}.

