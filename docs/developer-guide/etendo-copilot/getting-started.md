---
title: Getting Started
tags:
    - Copilot
    - IA
    - Machine Learning
---
## Overview

The getting started guide for the Copilot API is a tool that allows interaction with a bot that selects the appropriate tool to answer a query.

## Environment Setup

### Requirements
- *Etendo Classic*. If you do not have it, you can install it using the [Etendo Installation Developer Guide](/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment/){target="_blank"}.
- *Python* version ^3.10, to install it follow [The Official Installation Guide](https://www.python.org/downloads/){target="_blank"}.
- *Docker* to install it follow [The Official Installation Guide](https://docs.docker.com/engine/install/)

### Run copilot locally

1. Add copilot dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot:latest.release')
    ```

    ??? warning "Ensure you have 1.1.4 plugin version or greater:"
        
        ```groovy
        id 'com.etendoerp.gradleplugin' version '1.1.4'
        ```

2. In the terminal, execute:
    ``` bash title="Terminal"
    ./gradlew update.database smartbuild --info
    ```

3. In `gradle.properties` file is necessary to add some environment variables as a mandatory requirement


    ```groovy title="gradle.properties"
    COPILOT_PORT=5000
    OPENAI_API_KEY= ****
    OPENAI_MODEL=gpt-4
    BUSINESS_TOPIC=ERP
    ```

    | **Environment Variable**   | **Options**                                | **Info**                                                                                             |
    | ---------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
    | COPILOT_PORT           | `5000`                                         | **Required** The copilot port can be defined by the user                                             |
    | OPENAI_API_KEY         | `***********************`                      | **Required** You can get it from [OpenAI API keys](https://platform.openai.com/account/api-keys){target="_blank"} |
    | OPENAI_MODE            | `gpt-4`, `gpt-3.5-turbo-16k` , `gpt-3.5-turbo` | Among others that have the same number of requests per minute                                        |
    | BUSINESS_TOPIC         | `ERP` , `Human Resorces`, `Finance`, `Other`   | This parameter indicates the category to which the translations will be focused.                     |
  

        

4. To download the latest copilot Docker image and run it:

    ``` bash title="Terminal"
    ./gradlew copilot.start
    ```

5. When done using Etendo Copilot, run:

    ```bash
    ./gradlew copilot.stop
    ```

    This command will stop the Docker container running Copilot.

## Translation Tool: XMLTranslatorTool

Translates the content of an XML file from one language to another, as specified within the XML.  

### Functionality


1. Add Copilot Translation Tool dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot.xmltranslationtool:latest.release')
    ```
2. Restart Doker image using `./gradlew copilot.stop` and `./gradlew copilot start` tasks

3. The tool will translate the XML files to the language indicated when the XML file to be translated is generated, for example if the first line of the file is:

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
    ./gradlew copilot.translate -Ppkg=com.etendoerp.bankingpool.es_es
    ```

3. In the folder ```modules/com.etendoerp.bankingpool.es_es``` you will find the automatic translations.

4. To apply the translation compile the enviroment
    ``` bash title="Terminal"
    ./gradlew update.database smartbuild --info
    ```

5. Now we can see the *Financial Type Configuration* windows with their respective fields translated into Spanish.
    ![](/assets/developer-guide/etendo-copilot/getting-started/banking-pool-es.png)