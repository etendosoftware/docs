---
title: Getting Started
tags:
    - Copilot
    - IA
    - Machine Learning
---
## 🚀 Overview

Welcome to the getting started guide for the **Copilot** API. This tool allows interaction with a bot that selects the appropriate tool to answer a query.

## 📚 Environment Setup

### 🔍 Requirements:
- **Etendo Classic**. If you don't have it, [install it here](/docs/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment/).
- **Python** versión "^3.10", [install it here](https://www.python.org/downloads/)

### 🛠 Run copilot locally:

1. Add copilot dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation 'com.etendoerp.copilot'
    ```

    ??? warning "IMPORTANT: Ensure you have the latest version of the plugin:"
        
        ```groovy
        id 'com.etendoerp.gradleplugin' version 'latest.release'
        ```

2. In the terminal, execute:
    ```bash
    ./gradlew update.database smartbuild --info
    ```

3. In gradle.properties, add:
    ```
    copilotPort=5000
    copilotAPIKey=YOUR_API_KEY_HERE
    ```

    ??? warning "IMPORTANT: Remember to replace YOUR_API_KEY_HERE with your actual API key."

        you can get it from this link [get it](https://platform.openai.com/account/api-keys)

4. To start Copilot:

    ```bash
    ./gradlew copilot.start
    ```

## 🛠 Translation Tool: XMLTranslatorTool

Translates the content of an XML file from one language to another, as specified within the XML.  

### Functionality:
1. You should generate the translation module to translate before passing the folder to the tool. You can see how to do it from this link:
    [How to Create and Update Translation Modules](/docs/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/)
2. The tool will translate the XML files to the language indicated when the XML file to be translated is generated, for example if the first line of the file is:
    <compiereTrl baseLanguage="en_US" language="es_ES" table="AD_ELEMENT" version="">
    The tool will know that the language to be translated will be Spanish
3. What it will do is go through each of these XML files and translate what is in the source language to the target language, overwriting them for later use.

### How to use the XML translation tool shown in an example:
we want to translate the following module:
    ![](/docs/assets/developer-guide/etendo-copilot/getting-started/banking-pool-en.png)

1. In a new terminal, run:
    ```bash
    ./gradlew copilot.translate -Ppkg=com.etendoerp.bankingpool.es_es
    ```
2. In the folder ```modules/com.etendoerp.bankingpool.es_es``` you will find the automatic translations

3. Compile the enviroment
    ```bash
    ./gradlew update.database smartbuild --info
    ```

4. Now we can see the module translated into Spanish, in this case
    ![](/docs/assets/developer-guide/etendo-copilot/getting-started/banking-pool-es.png)


