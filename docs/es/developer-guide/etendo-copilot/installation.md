---
title: Guía del desarrollador - Instalación de Copilot
tags:
    - Copilot
    - Instalación
    - IA
    - Infraestructura
    - Agentes
---

## Visión general

Esta guía proporciona instrucciones detalladas sobre cómo empezar con Etendo Copilot, una API que permite la interacción con un bot capaz de seleccionar las herramientas adecuadas para responder a las consultas de los usuarios. Incluye los requisitos necesarios, instrucciones para añadir dependencias, configuraciones de variables de entorno y los pasos para ejecutar Copilot en un proyecto de Etendo. Además, cubre configuraciones opcionales para personalizar el comportamiento de Copilot y proporciona enlaces a guías de instalación detalladas del software requerido.

## Requisitos

1. Instale Etendo. Para ello, siga la [Guía de instalación de Etendo](../../getting-started/installation.md){target="_blank"}.
2. Este proyecto depende de las siguientes herramientas:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: versión `26.0.0` o superior.
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: versión `2.26.0` o superior.

    !!! warning
        Evite instalar Docker mediante [Snap](https://snapcraft.io){target="_blank"}, ya que puede quedar restringido por este sandbox y puede no tener acceso a directorios del host como `/opt/`, lo que puede impedir que los contenedores Docker de Etendo se inicien correctamente.
    
        Recomendación: instale Etendo usando la [última ISO](../../../../whats-new/release-notes/etendo-classic/iso.md)(que incluye Docker) o instale Docker siguiendo la guía de instalación oficial de su distribución.

!!!info
    El módulo [Docker Management](../../developer-guide/etendo-classic/bundles/platform/docker-management.md), incluido como dependencia, permite la distribución de la infraestructura dentro de los módulos de Etendo, que incluyen contenedores Docker para cada servicio.

## Instalación 
Etendo Copilot se distribuye dentro del bundle [Copilot Extensions](./bundles/overview.md), que además de incluir la **Infraestructura de Copilot**, incluye **agentes predeterminados** y **herramientas** que pueden utilizarse directamente o componer su uso en nuevos agentes.  

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el bundle **Copilot Extensions**. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Ejecución de Etendo Copilot

La configuración más sencilla que vamos a seguir como ejemplo es montar **Copilot** dockerizado y **Tomcat** ejecutándose como un servicio local. Otras configuraciones se detallan en la sección [Configuraciones avanzadas](#configuraciones-avanzadas).

### Copilot en Etendo 25 (recomendado)
Las últimas actualizaciones de Copilot siempre se desarrollan para la versión más reciente disponible de Etendo. Recomendamos mantener su entorno actualizado.

1. Ejecute la [configuración interactiva](../../getting-started/interactive-installation.md): este comando le guiará a través de la configuración de Copilot. Hay dos opciones principales:

    - **Copilot** la versión simple utilizada por la mayoría de usuarios.
    - **Copilot (Advanced)** proporciona más personalización e incluye todas las variables de configuración disponibles.

    ```bash title="Terminal"
    ./gradlew setup -Pinteractive=true --console=plain
    ```

    Una vez en el menú, seleccione **Copilot** y siga las indicaciones paso a paso; la configuración se completará con todas las variables requeridas.
    
    ![alt text](../../assets/developer-guide/etendo-copilot/getting-started/interactive-setup.png)

2. El archivo `gradle.properties` debería verse ahora así:

    ```groovy title="gradle.properties"
    docker_com.etendoerp.copilot=true
    OPENAI_API_KEY= ****
    ETENDO_HOST=http://localhost:8080/etendo
    ETENDO_HOST_DOCKER=http://host.docker.internal:8080/etendo
    COPILOT_HOST=copilot
    COPILOT_PORT=5005
    ```

3.  A continuación, debe crearse/recrearse el contenedor de Copilot:
    
    ``` bash title="Terminal"
    ./gradlew resources.up
    ```

4.  A continuación, recompile el entorno para asegurarse de que los cambios se aplican y se instalan correctamente:
    
    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```
5.  Inicie el servicio **Tomcat** y ¡pruebe Copilot en Etendo!
    
    !!!info
        Para configurar un nuevo agente o utilizar uno predefinido, siga la guía [Configuración y uso de Copilot](../../user-guide/etendo-copilot/setup-and-usage.md){target="_blank"}.
        

### Copilot en Etendo 24

1. Añada en `gradle.properties` la variable `docker_com.etendoerp.copilot=true` para habilitar el contenedor Docker de Copilot y al menos una `API_KEY`, dependiendo del proveedor de modelos que utilice.
    
    Recuerde que, debido a limitaciones de acceso a nivel de API, se requieren versiones de pago. Estas variables son obligatorias para ejecutar el contenedor de Copilot y acceder a los modelos utilizados.

    ```groovy title="gradle.properties"
        docker_com.etendoerp.copilot=true
        OPENAI_API_KEY= ****    // If you are using OpenAI
        ANTHROPIC_API_KEY= **** // If you are using Anthropic
        DEEPSEEK_API_KEY= ****  // If you are using DeepSeek
        GOOGLE_API_KEY= ****    // If you are using Gemini
    ```

2. Las variables de `gradle.properties` `ETENDO_HOST`, `ETENDO_HOST_DOCKER`, `COPILOT_HOST` y `COPILOT_PORT` se utilizan para configurar la conexión entre el servicio **Copilot** y **Etendo**.
    
    Etendo Copilot proporciona una **tarea de Gradle** para recuperar automáticamente estas variables en función de la configuración de su instancia de Etendo. Para ello, ejecute el siguiente comando en el terminal:

    ``` bash title="Terminal"
    ./gradlew copilot.variables.setup  --console=plain
    ```

    ![copilot.setup.variables](../../assets/developer-guide/etendo-copilot/getting-started/copilot-setup-variables.png)
    
    Este comando solicita características de su instancia de Etendo. Y, en función de sus respuestas, imprimirá los valores.
    
    **Copie** los valores impresos y **péguelos** en su archivo `gradle.properties`.

3. El archivo `gradle.properties` debería verse ahora así:

    ```groovy title="gradle.properties"
    docker_com.etendoerp.copilot=true
    OPENAI_API_KEY= ****    // If you are using OpenAI
    ANTHROPIC_API_KEY= **** // If you are using Anthropic
    DEEPSEEK_API_KEY= ****  // If you are using DeepSeek
    ETENDO_HOST=http://localhost:8080/etendo
    ETENDO_HOST_DOCKER=http://host.docker.internal:8080/etendo
    COPILOT_HOST=copilot
    COPILOT_PORT=5005
    ```
4. Una vez añadida la dependencia [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"} y configuradas las variables, ejecute en el terminal el siguiente comando para aplicar los cambios:
    
    ``` bash title="Terminal"
    ./gradlew setup
    ```

5.  A continuación, debe crearse/recrearse el contenedor de Copilot:
    
    ``` bash title="Terminal"
    ./gradlew resources.up
    ```

6.  A continuación, recompile el entorno para asegurarse de que los cambios se aplican y se instalan correctamente:
    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```
7.  Inicie el servicio **Tomcat** y ¡pruebe Copilot en Etendo!
    
    !!!info
        Para configurar un nuevo agente o utilizar uno predefinido, siga la guía [Configuración y uso de Copilot](../../user-guide/etendo-copilot/setup-and-usage.md){target="_blank"}.
        
### Variables de configuración

A continuación se enumeran todas las variables de configuración disponibles, que pueden configurarse manualmente.

| **Variable de entorno**          | **Predeterminado** | **Obligatorio**        | **Información**                                                                                                   |
| -------------------------------- | ------------------ | ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `docker_com.etendoerp.copilot`   | `true`             | ✅ (Obligatorio)       | Habilita el contenedor Docker de Etendo Copilot.                                                                  |
| `OPENAI_API_KEY`                 | `none`             | ✅ Si usa OpenAI       | Clave API para [OpenAI](https://platform.openai.com/account/api-keys){target="_blank"}. Contacte con Etendo o use la suya propia. |
| `GOOGLE_API_KEY`                 | `none`             | ✅ Si usa Gemini       | Clave API para [Gemini](https://aistudio.google.com/app/api-keys){target="_blank"}. Solo necesaria si usa modelos Gemini. |
| `ANTHROPIC_API_KEY`              | `none`             | ✅ Si usa Anthropic    | Clave API para [Anthropic](https://docs.anthropic.com/en/api/getting-started){target="_blank"}. Solo necesaria si usa modelos Anthropic. |
| `DEEPSEEK_API_KEY`               | `none`             | ✅ Si usa DeepSeek     | Clave API para [DeepSeek](https://deepseek.ai/){target="_blank"}. Solo necesaria si usa modelos DeepSeek.        |
| `ETENDO_HOST`                    | `none`             | ✅ (Obligatorio)       | URL a la que Copilot envía solicitudes para comunicarse con el sistema Etendo.                                    |
| `ETENDO_HOST_DOCKER`             | `none`             | ✅ (Obligatorio)       | Se utiliza cuando Copilot se ejecuta en Docker y Etendo no es accesible desde un dominio.                         |
| `COPILOT_HOST`                   | `none`             | ✅ (Obligatorio)       | Host del servicio Copilot.                                                                                        |
| `COPILOT_PORT`                   | `5005`             | ✅ (Obligatorio)       | Puerto utilizado por el servicio Copilot.                                                                         |
| `COPILOT_DEBUG`                  | `false`            | ❌ (Opcional)          | Habilita logs detallados de Copilot en la consola.                                                                |
| `COPILOT_MAX_ITERATIONS`         | `100`              | ❌ (Opcional)          | Número máximo de pasos de interacción del agente.                                                                 |
| `COPILOT_EXECUTION_TIMEOUT`      | `0`                | ❌ (Opcional)          | Tiempo de espera en segundos para la ejecución del agente (`0` = ilimitado).                                      |
| `COPILOT_STREAM_DEBUG`           | `false`            | ❌ (Opcional)          | Habilita el log de respuesta en tiempo real en el pop-up de Copilot.                                              |
| `CONFIGURED_TOOLS_FILENAME`      | `tools_config.json`| ❌ (Opcional)          | Archivo que define qué herramientas están habilitadas.                                                            |
| `DEPENDENCIES_TOOLS_FILENAME`    | `tools_deps.toml`  | ❌ (Opcional)          | Archivo que define dependencias entre herramientas.                                                               |
| `COPILOT_PULL_IMAGE`             | `true`             | ❌ (Opcional)          | Si es true, descarga la imagen Docker desde Docker Hub; si es false, usa la imagen local.                        |
| `COPILOT_IMAGE_TAG`              | `master`           | ❌ (Opcional)          | Tag de la imagen Docker a utilizar.                                                                               |
| `COPILOT_PORT_DEBUG`             | `5100`             | ❌ (Opcional)          | Puerto para depurar Copilot (si está habilitado).                                                                 |

### Gestión del contenedor del servicio Copilot

- Para iniciar la imagen Docker de Copilot, ejecute:

    ``` bash title="Terminal"
    ./gradlew resources.up
    ```

- Para detener el contenedor de Copilot, puede ejecutar: 
    ``` bash title="Terminal"
    ./gradlew resources.stop
    ```

- Cada vez que se añade una nueva herramienta o cambian las variables de entorno, es necesario eliminar y crear de nuevo el contenedor de Copilot. Ejecute el siguiente comando para eliminar el contenedor: 
    
    ``` bash title="Terminal"
    ./gradlew resources.down
    ```

!!! warning 
    Tenga en cuenta que resources.stop y resources.down también afectarán a otros servicios configurados en el contenedor de Etendo.

!!! warning
    En versiones del bundle Copilot Extensions inferiores a [3.3.0](../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md), si sufre errores relacionados con la falta de la dependencia `poetry`, puede usar la imagen Docker heredada, con el tag `poetry`. Para ello, debe añadir la siguiente variable en el archivo `gradle.properties`:
    
    ```groovy title="gradle.properties"
    COPILOT_IMAGE_TAG=poetry
    ```
    Esto utilizará la imagen Docker heredada con la dependencia `poetry` instalada, en lugar de la nueva con `uv` como gestor de paquetes instalado.

## Configuraciones avanzadas 

### Ejecutar Copilot localmente (solo para desarrollar Copilot)

**Requisitos**

- [Python 3](https://www.python.org/downloads/){target="_blank"} versión `3.10` o superior.
- [uv](https://docs.astral.sh/uv/){target="_blank"} gestor de paquetes.

Recomendamos usar **PyCharm** para ejecutar Copilot localmente. Descárguelo e instálelo aquí: [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/){target="_blank"}

1. Abra PyCharm, busque el módulo de Copilot y ábralo.

    ![](../../assets/developer-guide/etendo-copilot/getting-started/copilot-local-1.png)

2. Abra el archivo `Run.py` y, a continuación, añada un nuevo intérprete.

    ![](../../assets/developer-guide/etendo-copilot/getting-started/copilot-local-2.png)
    ![](../../assets/developer-guide/etendo-copilot/getting-started/copilot-local-3.png)

3. Añada un nuevo archivo de configuración y seleccione Python.

    ![](../../assets/developer-guide/etendo-copilot/getting-started/copilot-local-4.png)
    ![](../../assets/developer-guide/etendo-copilot/getting-started/copilot-local-5.png)

4. Seleccione el intérprete creado anteriormente. En el campo script, seleccione el archivo `run.py` y, en el campo .env, seleccione el archivo `gradle.properties`.

    ![](../../assets/developer-guide/etendo-copilot/getting-started/copilot-local-6.png)

5. Una vez hecho, abra el terminal de PyCharm y ejecute los siguientes comandos:

    ``` bash title="terminal"
    source venv/bin/activate
    uv sync
    ```
    !!! warning
        En versiones anteriores a 3.3.0, el gestor de paquetes utilizado por Copilot era `poetry`, por lo que el comando a ejecutar es `poetry install` en lugar de `uv sync`.

6. Ejecute `Run.py` desde PyCharm

### ¿Cómo depurar Etendo Copilot?

Hay dos formas principales de depurar Etendo Copilot, dependiendo de su configuración.

- **Usando PyCharm (modo local)**  

    Si está ejecutando Copilot localmente, puede usar el depurador integrado de PyCharm. Simplemente establezca puntos de interrupción en el código y ejecute el depurador para inspeccionar el flujo de ejecución paso a paso.

- **Usando VSCode (Copilot dockerizado)**
    
    Si Copilot se está ejecutando en un contenedor Docker, puede depurarlo con VSCode usando la configuración `launch.json` proporcionada:  

    1. Asegúrese de que **VSCode** y la **extensión de Python** estén instaladas y habilitadas.  
    2. Abra el directorio `build/copilot` dentro del *proyecto Etendo*.
        
        !!! note Important
            Este es el directorio que contiene el código de las herramientas, lo cual es necesario para que el depurador pueda localizar los archivos fuente.
        
        ![alt text](../../assets/developer-guide/etendo-copilot/getting-started/how-to-debug-when-dockerized.png)  
    3. Vaya a la sección **Run and Debug** en VSCode. Verá una configuración llamada **Copilot Remote Debug**. Haga clic en el botón verde de reproducción para iniciar la depuración.
        
        ![alt text](../../assets/developer-guide/etendo-copilot/getting-started/how-to-debug-when-dockerized-1.png)  
    4. Una vez que el depurador esté en ejecución, establezca puntos de interrupción según sea necesario y ejecute Copilot. El depurador se detendrá en sus puntos de interrupción, permitiéndole inspeccionar variables y analizar el flujo de ejecución.
        
        ![alt text](../../assets/developer-guide/etendo-copilot/getting-started/how-to-debug-when-dockerized-2.png)
    
---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.