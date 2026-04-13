---
title: Cómo configurar Etendo Copilot para usar un proxy
tags:
    - Guía práctica
    - Etendo Copilot
    - Proxy
    - Red
status: beta
---

# Cómo configurar Etendo Copilot para usar un proxy

## Visión general

**Etendo Copilot** puede configurarse para enrutar su tráfico de la API de LLM a través de un proxy por varios motivos operativos:

- Aislamiento de red (servidores sin acceso directo a internet)
- Enrutamiento centralizado o balanceo de carga, cumplimiento e inspección del tráfico.
- Consolidar las credenciales de los proveedores detrás de un endpoint controlado.

Un proxy delante de los **proveedores de LLM** actúa como intermediario que reenvía las solicitudes desde Copilot a proveedores como *OpenAI*, *Anthropic* o *Google*.

Esta guía muestra una configuración habitual usando [LiteLLM Proxy](https://docs.litellm.ai/docs/simple_proxy){target="_blank"} y explica cómo apuntar **Etendo Copilot** a ese proxy. El caso de *sin acceso directo a internet* es un escenario típico, pero la misma configuración aplica cuando necesita enrutamiento centralizado, aplicación de políticas o una mejor observabilidad de las solicitudes a LLM.

## Configurar el servidor proxy

Una opción conveniente es **LiteLLM Proxy**, que simplifica la gestión de distintos proveedores de LLM detrás de un único endpoint. El siguiente ejemplo muestra una configuración básica con Docker:

1.  **Crear el archivo `litellm_config.yaml`**: Este archivo indica al proxy qué modelos y comportamiento del proveedor exponer. Para un passthrough simple, use:

    ```yaml
    model_list:
      # Works for ALL Providers and needs the default provider credentials in .env
      - model_name: "*"
        litellm_params:
          model: "*"
    ```

2.  **Crear el archivo `.env`**: Almacene de forma segura en este archivo las claves API del proveedor. Sustituya los placeholders por sus claves reales:

    ```bash
    OPENAI_API_KEY=sk-proj-XXXXXXX
    ANTHROPIC_API_KEY=sk-ant-XXXXXXXXXX
    GOOGLE_API_KEY=
    ```

3.  **Ejecutar el proxy con Docker**: Coloque `litellm_config.yaml` y `.env` en el mismo directorio y ejecute:

    ```sh
    docker run \
        --env-file .env \
        -v $(pwd)/litellm_config.yaml:/app/config.yaml \
        -p 4000:4000 \
        ghcr.io/berriai/litellm:main-stable \
        --config /app/config.yaml --detailed_debug
    ```

    Este comando inicia un contenedor que expone el proxy en el puerto `4000` del servidor host.

    !!!info
        El ejemplo anterior muestra una configuración de passthrough simple. Para un uso avanzado (caché, control de acceso, limitación de tasa, etc.) consulte la [documentación de LiteLLM Proxy](https://docs.litellm.ai/docs/simple_proxy){target="_blank"}

## Configurar Etendo Copilot

Una vez que el proxy esté en ejecución, configure Etendo Copilot para enviar sus **solicitudes a LLM** a través de la URL del proxy.

1.  **Editar `gradle.properties`**: Abra el archivo `gradle.properties` en la raíz de su instalación de Etendo.

2.  **Añadir la propiedad `COPILOT_PROXY_URL`**: Añada la siguiente línea, sustituyendo `my.server.with.the.proxy` y `<PORT>` por el host y el puerto de su proxy (para el ejemplo anterior el puerto es `4000`):

    ```properties
    COPILOT_PROXY_URL=http://my.server.with.the.proxy:4000
    ```

## Aplicar los cambios y reiniciar el servicio

Para que la configuración sea efectiva, debe recompilar, desplegar la configuración en Etendo y reiniciar los servicios relevantes. Realice los pasos en el orden indicado a continuación:

1.  **Reiniciar el servicio de Copilot**: Desde la raíz del proyecto ejecute:

    ```sh
    ./gradlew resources.up
    ```

    Este target actualiza y reinicia el servicio de Copilot en su empaquetado de desarrollo/despliegue. Úselo después de cambiar propiedades de ejecución para que la aplicación de Copilot recargue los nuevos valores de propiedades.

2.  **Desplegar la configuración en Etendo**: Ejecute las tareas de setup y smartbuild para aplicar y construir la configuración para Etendo:

    ```sh
    ./gradlew setup smartbuild
    ```

    Estas tareas preparan y despliegan la configuración y los recursos actualizados en el runtime de Etendo para que la plataforma use el nuevo `COPILOT_PROXY_URL` a nivel de aplicación.

3.  **Reiniciar Tomcat**: Reinicie su servidor de aplicaciones Tomcat para que Etendo Classic recoja la nueva configuración. El método exacto de reinicio depende de su sistema operativo y de la instalación de Tomcat.

Tras completar estos pasos, Etendo Copilot enviará las solicitudes a LLM a través del proxy configurado. Esto resulta útil para el aislamiento de red, el enrutamiento centralizado o el balanceo de carga, la aplicación de políticas y la auditoría.

---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.