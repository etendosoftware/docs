---
tags:
    - Copilot
    - Translation Tool
    - Module Translation
    - Language
    - Localization
---

#  XML Translation Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.xmltranslationtool`

## Overview

The XMLTranslationTool directly translates XML files’ content based on the specified language attribute within the XML, allowing for effective and accurate localization across different languages. 

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

The XMLTranslationTool allows agents to translate the content of XML files from one language to another, as specified within the XML itself. This is particularly useful in scenarios where localized versions of XML content are required for different regions or languages.

This tool is ideal for automated workflows that need to handle XML translations efficiently, enabling seamless adaptation of content for various languages. By directly translating XML content based on specified language attributes, it ensures accurate localization of text without manually editing individual files.

Using this tool consists of the following actions:

- **Receiving Parameters** 
    The tool receives an input object that contains the following key:

    - relative_path 

        (str): The relative path to the XML files directory where translation is required.

- **Processing**

    1. Validation: The tool first verifies if the provided relative_path points to an existing directory. If the directory does not exist, it returns an error message indicating the issue.

    2. Path Calculation: It calculates the absolute path of the XML directory based on the relative path provided.

    3. XML File Iteration: For each XML file in the directory:

        - Skip Condition: If a file is already translated, it skips the translation process.

        - Translation Process:
            
            - The tool uses OpenAI's API to translate each XML file's text content according to the target language specified within the XML's attributes.

            - Each unlocalized element is marked as "translated" after processing.

            - If all files are already translated, a message indicating this is returned.

    4. Collecting Results: Paths to the successfully translated XML files are collected in a list, which is returned as the final output.

- **Returning the Result**

    Once the translation process is completed, the tool returns a list of file paths, each pointing to a successfully translated XML file.

## Usage Example

If you have XML files located at `/modules/com.etendoerp.webhookevents.es_es` that need translation, you would use the tool as follows:

- **Input**:

```
{
  "relative_path": "/modules/com.etendoerp.webhookevents.es_es"
}
```

- **Output**:

```
{
  "translated_files_paths": [
    "Successfully translated file /modules/com.etendoerp.webhookevents.es_es/AD_REF_LIST_TRL_es_ES.xml",
    "Successfully translated file /modules/com.etendoerp.webhookevents.es_es/AD_ELEMENT_TRL_es_ES.xml"
  ]
}
```