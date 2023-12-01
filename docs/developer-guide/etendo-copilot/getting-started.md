---
title: Getting Started
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

6. When done using Etendo Copilot, run:

    ```bash
    ./gradlew copilot.stop
    ```

    This command will stop the Docker container running Copilot.

## Translation Tool: XMLTranslatorTool
:octicons-package-16: Javapackage: com.etendoerp.copilot.xmltranslationtool

Translates the content of an XML file from one language to another, as specified within the XML.  

### Functionality


1. Add Copilot Translation Tool dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot.xmltranslationtool:1.0.0')
    ```
2. In `gradle.properties` file you can add some environment variables. If they are not set, the default values will be used.


    ```groovy title="gradle.properties"
    OPENAI_MODEL=gpt-4
    BUSINESS_TOPIC=ERP
    ```

    | **Environment Variable**   | **Options**                                | **Default**| **Info**                                                                                             |
    | ---------------------- | ---------------------------------------------- |----------| ---------------------------------------------------------------------------------------------------- |
    | OPENAI_MODE            | `gpt-4`, `gpt-3.5-turbo-16k` , `gpt-3.5-turbo` |`gpt-3.5-turbo` | Among others that have the same number of requests per minute                                        |
    | BUSINESS_TOPIC         | `ERP` , `Human Resorces`, `Finance`, `Other`  | `ERP` | This parameter indicates the category to which the translations will be focused.                     |
  
3. Restart Docker image using `./gradlew copilot.stop` and `./gradlew copilot.start` tasks

4. The tool will translate the XML files to the language indicated when the XML file to be translated is generated, for example if the first line of the file is:

    ```xml
    <compiereTrl baseLanguage="en_US" language="es_ES" table="AD_ELEMENT" version="">
    ```

    The tool will know that the language to be translated will be Spanish.

4. It goes through each of these XML files and translates what is in the source language to the target language, overwriting them for later use.

### How to use the XML translation tool shown in an example

First of all, we start from the module `com.etendoerp.bankingpool` originally in English and we can see the Financial Type Configuration window:

![](/assets/developer-guide/etendo-copilot/getting-started/banking-pool-en.png)

1. You must generate the `com.etendoerp.bankingpool` translation module, you can see how to do it in [How to Create and Update Translation Modules](/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/){target="_blank"}. <br> Initially all its fields will be in the source language and then it will be translated by the translation tool.
  
    After having created the translation module in the modules folder we will find `com.etendoerp.bankingpool.es_es`

2.  To execute translation tool, in a new terminal, run:
    ``` bash title="Terminal"
    ./gradlew copilot.translate -Parg=com.etendoerp.bankingpool.es_es
    ```

3. In the folder ```modules/com.etendoerp.bankingpool.es_es``` you will find the automatic translations.

4. To apply the translation compile the enviroment
    ``` bash title="Terminal"
    ./gradlew update.database smartbuild --info
    ```

5. Now we can see the *Financial Type Configuration* windows with their respective fields translated into Spanish.
    ![](/assets/developer-guide/etendo-copilot/getting-started/banking-pool-es.png)