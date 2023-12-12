---
title: Installation
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
- *Etendo Classic*. If you do not have it, you can install it using the [Etendo Installation Developer Guide](/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment/){target="_blank"}.
- *Python* version ^3.10, to install it follow [The Official Installation Guide](https://www.python.org/downloads/){target="_blank"}.
- *Docker* to install it follow [The Official Installation Guide](https://docs.docker.com/engine/install/)

### Run copilot locally

1. Add copilot dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot:1.0.1')
    ```

    ??? warning "Ensure you have 1.2.2 plugin version or greater:"
        
        ```groovy
        id 'com.etendoerp.gradleplugin' version '1.2.2'
        ```

2. In the terminal, execute:
    ``` bash title="Terminal"
    ./gradlew update.database smartbuild --info
    ```

3. In `gradle.properties` file is necessary to add some environment variables as a mandatory requirement


    ```groovy title="gradle.properties"
    COPILOT_PORT=5000
    OPENAI_API_KEY= ****
    ```

    | **Environment Variable**   | **Options**  | **Info** |
    | -------------------------- | -------------| -------- |
    | COPILOT_PORT           | `5000`   | **Required** The copilot port can be defined by the user |
    | OPENAI_API_KEY         | `***********************` | **Required** You can get it from [OpenAI API keys](https://platform.openai.com/account/api-keys){target="_blank"} |
  

4. In addition, there are other optional variables to configure certain aspects of the copilot. If not specified, default values are used.
    
    | **Environment Variable**    | **Options**  | **Default**  | **Info** |
    | ----------------------------| -------------| -------------| -------- |
    | SYSTEM_PROMPT  | `String` | `"You are a very powerful assistant with a set of tools, which you will try to use for the requests made to you."` | The prompt that will be used to make the request to the agent and that will condition the response and behavior of the copilot.|
    | CONFIGURED_TOOLS_FILENAME | `JSON File name` | `tools_config.json` | The name of the file that contains the configuration of the enabled tools. |
    | DEPENDENCIES_TOOLS_FILENAME | `TOML File name` | `tools_deps.toml` | The name of the file that contains the configuration of the dependencies of the tools. |
    | COPILOT_IMAGE_TAG | `String` | `master` | The tag of the copilot docker image that will be used. |
    | COPILOT_PULL_IMAGE | `Boolean` | `true` | If true, the copilot docker image will be pulled from docker hub. If false, gradle will try to use the local image with the tag specified in COPILOT_IMAGE_TAG, but if it does not exist, it will be pulled from docker hub. |
    | COPILOT_DOCKER_CONTAINER_NAME | `String` | `etendo-default` | The name of the docker container that will be created to run the copilot docker image. |



5. To download the latest copilot Docker image and run it:

    ``` bash title="Terminal"
    ./gradlew copilot.start
    ```

6. You can now send prompts to the copilot using the following command:

    ``` bash title="Terminal"
    ./gradlew copilot.do -Pprompt="prompt"
    ```

    Where `prompt` is the prompt you want to send to the copilot.

    For example:

    ``` bash title="Terminal"
    ./gradlew copilot.do -Pprompt="I want to say Hello World"
    ```

    The copilot will detect the tool that best suits the prompt and will return the response of the tool.

    In the following example, we can see how the copilot detects that the tool that best suits the prompt is the `HelloWorldTool`(a default tool) and returns the response of the tool:
    ![Alt text](/assets/developer-guide/etendo-copilot/getting-started/helloworld.png)
    
    Another screenshot from the Copilot side, where we can see how the copilot detects that the tool that best suits the prompt is the `HelloWorldTool`:
    ![Alt text](/assets/developer-guide/etendo-copilot/getting-started/helloworld-1.png)

7. When done using Etendo Copilot, run:

    ```bash
    ./gradlew copilot.stop
    ```

    This command will stop the Docker container running Copilot.

