---
title: Getting Started
tags:
    - Copilot
    - IA
    - Machine Learning
---
## Overview

Welcome to the getting started guide for the **Copilot** API. This tool allows interaction with a bot that selects the appropriate tool to answer a query.

## Environment Setup

### Requirements
- **Etendo Classic**. If you don't have it, [install it here](/docs/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment/){target="_blank"}.
- **Python** versión ^3.10, [install it here](https://www.python.org/downloads/){target="_blank"}.

### Run copilot locally

1. Add copilot dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation 'com.etendoerp.copilot'
    ```

    ??? warning "Ensure you have the latest version of the plugin:"
        
        ```groovy
        id 'com.etendoerp.gradleplugin' version 'latest.release'
        ```

2. In the terminal, execute:
    ``` bash title="Terminal"
    ./gradlew update.database smartbuild --info
    ```

3. In gradle.properties, add:
    ```groovy title="build.gradle"
    copilotPort=5000
    copilotAPIKey=YOUR_API_KEY_HERE
    ```

    ??? warning "Remember to replace YOUR_API_KEY_HERE with your actual API key."

        You can get it from this link [get it](https://platform.openai.com/account/api-keys){target="_blank"}.

4. To start Copilot:

    ``` bash title="Terminal"
    ./gradlew copilot.start
    ```

## Translation Tool: XMLTranslatorTool

Translates the content of an XML file from one language to another, as specified within the XML.  

### Functionality

1. The tool will translate the XML files to the language indicated when the XML file to be translated is generated, for example if the first line of the file is:

    ```xml
    <compiereTrl baseLanguage="en_US" language="es_ES" table="AD_ELEMENT" version="">
    ```

    The tool will know that the language to be translated will be Spanish.

2. It goes through each of these XML files and translates what is in the source language to the target language, overwriting them for later use.

### How to use the XML translation tool shown in an example

First of all, we start from the module `com.etendoerp.bankingpool` originally in English and we can see the Financial Type Configuration window:

![](/docs/assets/developer-guide/etendo-copilot/getting-started/banking-pool-en.png)

1. You must generate the `com.etendoerp.bankingpool` translation module, you can see how to do it in [How to Create and Update Translation Modules](/docs/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/){target="_blank"}. <br> Initially all its fields will be in the source language and then it will be translated by the translation tool.
  
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

5. Now we can see the "Financial Type Configuration" windows with their respective fields translated into Spanish.
    ![](/docs/assets/developer-guide/etendo-copilot/getting-started/banking-pool-es.png)