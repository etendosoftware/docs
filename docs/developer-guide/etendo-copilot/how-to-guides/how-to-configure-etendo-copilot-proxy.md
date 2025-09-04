---
tags:
    - How to
    - Etendo Copilot
    - Proxy
    - Network
---

# How to Configure Etendo Copilot to Use a Proxy

## Overview

Etendo Copilot can be configured to route its LLM API traffic through a proxy for several operational reasons: network isolation (servers without direct internet access), centralized routing or load balancing, compliance and traffic inspection, or to consolidate provider credentials behind a controlled endpoint. A proxy in front of the LLM providers acts as an intermediary that forwards requests from Copilot to providers such as OpenAI, Anthropic or Google.

This guide shows a common setup using LiteLLM Proxy and explains how to point Etendo Copilot to that proxy. The “no direct internet access” case is one typical scenario, but the same configuration applies when you need centralized routing, policy enforcement, or better observability of LLM requests.

---

## 1. Set up the proxy server

A convenient option is LiteLLM Proxy, which simplifies handling different LLM providers behind a single endpoint. The following example shows a basic Docker setup:

1.  **Create the `litellm_config.yaml` file**: This file tells the proxy which models and provider behavior to expose. For a simple passthrough, use:

    ```yaml
    model_list:
      # Works for ALL Providers and needs the default provider credentials in .env
      - model_name: "*"
        litellm_params:
          model: "*"
    ```

2.  **Create the `.env` file**: Store provider API keys securely in this file. Replace placeholders with your real keys:

    ```bash
    OPENAI_API_KEY=sk-proj-XXXXXXX
    ANTHROPIC_API_KEY=sk-ant-XXXXXXXXXX
    GOOGLE_API_KEY=
    ```

3.  **Run the proxy with Docker**: Place `litellm_config.yaml` and `.env` in the same directory and run:

    ```sh
    docker run \
        --env-file .env \
        -v $(pwd)/litellm_config.yaml:/app/config.yaml \
        -p 4000:4000 \
        ghcr.io/berriai/litellm:main-stable \
        --config /app/config.yaml --detailed_debug
    ```

    This command starts a container that exposes the proxy on port `4000` of the host server.

> **Note:** The example above shows a simple passthrough configuration. For advanced usage (caching, access control, rate limiting, etc.) consult the LiteLLM Proxy documentation: https://docs.litellm.ai/docs/simple_proxy

---

## 2. Configure Etendo Copilot 🤝

After the proxy is running, configure Etendo Copilot to send its LLM requests through the proxy URL.

1.  **Edit `gradle.properties`**: Open the `gradle.properties` file at the root of your Etendo installation.

2.  **Add the `COPILOT_PROXY_URL` property**: Add the following line, replacing `my.server.with.the.proxy` and `<PORT>` with your proxy host and port (for the example above the port is `4000`):

    ```properties
    COPILOT_PROXY_URL=http://my.server.with.the.proxy:4000
    ```

---


## 3. Apply the changes and restart the service 🚀

To make the configuration effective you must rebuild, deploy the configuration to Etendo Classic and restart the relevant services. Perform the steps in the order below:

1.  **Restart the Copilot service (resources)**: From the project root run:

    ```sh
    ./gradlew resources.up
    ```

    This target refreshes and restarts the Copilot service in your development/deployment packaging. Use this after changing runtime properties so the Copilot application reloads the new property values.

2.  **Deploy configuration to Etendo Classic**: Run the setup and smartbuild tasks to apply and build the configuration for Etendo Classic:

    ```sh
    ./gradlew setup smartbuild
    ```

    These tasks prepare and deploy the updated configuration and resources into the Etendo Classic runtime so the platform uses the new `COPILOT_PROXY_URL` at the application level.

3.  **Move the configuration**: Copy the `COPILOT_PROXY_URL` property from `gradle.properties` into the `config` folder so the setting persists in the deployed configuration.

4.  **Restart Tomcat**: Restart your Tomcat application server so  Etendo Classic pick up the new configuration. The exact restart method depends on your OS and Tomcat installation.

That’s it! 🎉 After completing these steps Etendo Copilot will send LLM requests through the configured proxy (useful for network isolation, centralized routing/load balancing, policy enforcement, or auditing).

