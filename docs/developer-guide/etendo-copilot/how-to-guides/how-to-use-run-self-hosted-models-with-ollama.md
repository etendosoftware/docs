---
tags:
    - How to
    - Model
    - Copilot
    - Ollama
---

# How to Run Self-Hosted Models with Ollama

## Overview

This article explains how to run and use self-hosted models with Ollama in Copilot. Copilot uses by default LLM models hosted from cloud providers. However, you can use your own models by hosting them on your own servers. This can be useful for privacy reasons or to use models that are not available in OpenAI. Ollama allows to run self-hosted models in a Docker container.

### Running Ollama as a Docker Container.
Copilot includes a Docker Compose file that allows to run Ollama with the Docker module gradle tasks. To see more information about the Docker module, visit [Docker Management](../../etendo-classic/bundles/platform/docker-management.md) documentation.

To enable the compose file for Ollama, its necessary to add the following line in the `gradle.properties` file:

```groovy title="gradle.properties"
docker_com.etendoerp.copilot.ollama=true
```
After that, you can run the following command to start the Ollama container:

```bash title="Terminal"
./gradlew resources.up --info
```

### Installing a Model

The [models available in Ollama](https://ollama.com/search){target=_isblank} need to be installed in order to be used. This is done only once because the container configuration allows the models to be persisted, so restarting the container will not affect the availability of the models once installed.

To install the models, it is necessary to enter the Ollama container and run the following command:

```bash title="Terminal"
docker exec -it etendo-ollama-1 bash
```
This will open a shell inside the container. Once inside the container, you can install the model using the following command(for example, to install the model llama3.2:3b):

```bash title="Docker Terminal"
ollama run llama3.2:3b
```

After the model is installed, you must create a record in the [AI Model](../../../user-guide/etendo-copilot/setup-and-usage.md#ai-models-window) window in Copilot, with the following information:

- Provider: "ollama"
- Model: "llama3.2:3b"

### Using the Model in Copilot
- Finally you can use the model in Copilot by selecting the record created in the model selector in the [Assistant](../../../user-guide/etendo-copilot/setup-and-usage.md#assistant-window) window.