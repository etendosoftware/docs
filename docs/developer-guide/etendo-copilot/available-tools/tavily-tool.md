---
tags:
    - Copilot
    - Tavily
    - API
    - Search Engine
    - Tool
---

# Tavily Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview 

The **TavilySearchTool** is a custom tool designed to perform searches using the Tavily search engine, which is known for allowing users to search the Internet for various types of information.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Configuration 

### Tavily API key Configuration

1. Visit the [Tavily website](https://tavily.com/){target="_blank"} and sign up for an account.
2. Once logged in, navigate to the API key section of your account.
3. Generate a new API key.
4. It is necessary to add the `gradle.properties` file with the following configuration:

    ``` groovy title="gradle.properties"
    TAVILY_API_KEY=<your_api_key_here>
    ```

5. Restart Copilot service

    ``` bash title="terminal"
    ./gradlew resources.down resources.up
    ```


## Functionality

This tool is used to interface with the Tavily search engine and retrieve search results for a given query.

Everytime this tool is called, the parameter to use is a JSON like:

```json 
{ "query": "What is the capital of Spain?" }
```