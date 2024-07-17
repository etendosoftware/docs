---
tags:
    - Copilot
    - IA
    - Tavily
    - API
    - Etendo
---

# Tavily Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview 

The **TavilySearchTool** is a custom tool designed to perform searches using the Tavily search engine, which is known for allowing users to search the Internet for various types of information.

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
    ./gradlew copilot.stop copilot.start
    ```


## Functionality

This tool is used to interface with the Tavily search engine and retrieve search results for a given query.

Everytime this tool is called, the parameter to use is a JSON like:

```json 
{ "query": "What is the capital of Spain?" }
```