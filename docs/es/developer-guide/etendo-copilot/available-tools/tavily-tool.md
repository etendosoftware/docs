---
tags:
    - Copilot
    - Tavily
    - API
    - Motor de búsqueda
    - Herramienta
---

# Herramienta Tavily

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general 

La **TavilySearchTool** es una herramienta personalizada diseñada para realizar búsquedas utilizando el motor de búsqueda Tavily, conocido por permitir a los usuarios buscar en Internet diversos tipos de información.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Configuración 

### Configuración de la clave API de Tavily

1. Visite el [sitio web de Tavily](https://tavily.com/){target="_blank"} y regístrese para obtener una cuenta.
2. Una vez haya iniciado sesión, navegue hasta la sección de clave API de su cuenta.
3. Genere una nueva clave API.
4. Es necesario añadir el archivo `gradle.properties` con la siguiente configuración:

    ``` groovy title="gradle.properties"
    TAVILY_API_KEY=<your_api_key_here>
    ```

5. Reinicie el servicio de Copilot

    ``` bash title="terminal"
    ./gradlew resources.down resources.up
    ```


## Funcionalidad

Esta herramienta se utiliza para interactuar con el motor de búsqueda Tavily y recuperar resultados de búsqueda para una consulta determinada.

Cada vez que se llama a esta herramienta, el parámetro a utilizar es un JSON como:

```json 
{ "query": "What is the capital of Spain?" }
```

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.