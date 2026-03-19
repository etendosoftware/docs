---
tags:
  - Primeros pasos
  - Desarrollo
  - Instalación
  - Desarrollo local
  - IntelliJ
---

# Instalar Etendo - Entorno de Desarrollo Local

## Visión general

Esta guía cubre la configuración de un entorno local de desarrollo de Etendo. Utiliza IntelliJ IDEA con una instancia local de Tomcat para ejecutar Etendo, y Docker para ejecutar Copilot y la UI principal como servicios en contenedores.

## Requisitos previos

Antes de empezar, asegúrate de que lo siguiente está listo:

- [Requisitos del sistema](requirements.md)
- [PostgreSQL configurado](postgresql-configuration.md)
- [Credenciales de GitHub](use-of-repositories-in-etendo.md)
- [Docker](https://docs.docker.com/get-docker/){target="_blank"} versión `26.0.0` o superior
- [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"} versión `2.26.0` o superior
- **Clave de API de OpenAI** — requerida para Copilot. Usa tu propia clave de [OpenAI](https://platform.openai.com/account/api-keys){target="_blank"} o contacta con [Etendo](https://etendo.software){target="_blank"} para obtener una. Para más detalles sobre proveedores compatibles, consulta la [guía de instalación de Copilot](../../../etendo-copilot/installation.md#configuration-variables).

!!! warning
    Evita instalar Docker mediante [Snap](https://snapcraft.io){target="_blank"} — sus restricciones de sandbox pueden impedir que los contenedores Docker de Etendo accedan correctamente a los directorios del host. Instala Docker siguiendo la guía oficial para tu distribución.

## Instalación

### 1. Clonar el proyecto

```bash title="Terminal"
cd /path/to/workspace
git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
cd EtendoERP
```

### 2. Añadir credenciales de GitHub

Edita `gradle.properties` y añade tus credenciales de GitHub. Para generarlas, sigue la guía [Uso de repositorios en Etendo](use-of-repositories-in-etendo.md).

```groovy title="gradle.properties"
githubUser=<username>
githubToken=<*******>
```

### 3. Expandir el proyecto

=== ":octicons-file-zip-24: Source Format"

    Se recomienda el formato fuente para desarrollo local, ya que proporciona acceso completo a la base de código.

    ```bash title="Terminal"
    ./gradlew expand
    ```

=== ":material-language-java: JAR Format"

    Descomenta la dependencia del core en `build.gradle`:

    ```groovy title="build.gradle"
    implementation('com.etendoerp.platform:etendo-core:<version>')
    ```

    !!! info
        Para conocer las versiones disponibles, visita las [Notas de versión de Etendo](../../../../whats-new/release-notes/etendo-classic/release-notes.md).

### 4. Aplicar la plantilla local

Ejecuta la siguiente tarea para configurar todas las variables necesarias para Etendo, Copilot y la UI principal:

```bash title="Terminal"
./gradlew setup.applyTemplates --template=local
```

Cuando se te solicite, introduce tu **Clave de API de OpenAI**.

La plantilla configura `gradle.properties` automáticamente con todos los ajustes necesarios para un entorno local, incluyendo los servicios Docker de Copilot y la UI principal.

!!! info "Availability"
    `setup.applyTemplates` está disponible a partir de **Etendo 26**, o en versiones anteriores con el [Etendo Gradle Plugin 3.0.0](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) o superior.

!!! info
    Para más detalles sobre las plantillas disponibles, opciones y uso avanzado, consulta la guía [Cómo usar Setup Apply Templates](../../how-to-guides/how-to-use-setup-apply-templates.md).

!!! tip "Alternativa: configuración manual"
    Configura las variables directamente en `gradle.properties` y aplícalas ejecutando:
    ```bash
    ./gradlew setup --info
    ```

!!! tip "Alternativa: configuración interactiva"
    Para una configuración totalmente guiada, propiedad por propiedad, ejecuta la configuración interactiva:
    ```bash
    ./gradlew setup -Pinteractive=true --console=plain
    ```
    Para más detalles, consulta la guía [Cómo usar la configuración interactiva](../../how-to-guides/how-to-use-interactive-setup.md).

### 5. Instalar Etendo

```bash title="Terminal"
./gradlew install smartbuild --info
```

Esto crea la base de datos, compila las fuentes y despliega en el directorio local de Tomcat.

### 6. Iniciar servicios Docker

```bash title="Terminal"
./gradlew resources.up --info
```

Esto inicia los contenedores de **Copilot** y la **UI principal**. Ambos están incluidos en la instalación base.

## Ejecutar en IntelliJ

=== "IntelliJ IDEA Community Edition"

    1. Descarga e instala [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/download){target="_blank"}.

    2. Abre el directorio fuente de Etendo con IntelliJ:

        ![open-project.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/open-project.png)

    3. Instala el plugin **Smart Tomcat**: ve a `Settings` > `Plugins` y busca `Smart Tomcat`.

        ![install-smart-tomcat.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/install-smart-tomcat.png)

    4. Descarga [Apache Tomcat](https://tomcat.apache.org/download-90.cgi){target="_blank"} y descomprímelo dentro del directorio del proyecto.

    5. Configura la ejecución de Tomcat:

        - Ve a `Current File` > `Edit Configurations`.

            ![edit-configurations.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/edit-configurations.png)

        - Haz clic en `+` y añade una nueva configuración de **Smart Tomcat** con los siguientes valores:
            - **Name**: `Tomcat`
            - **Tomcat Server**: selecciona el directorio de Apache Tomcat descomprimido
            - **Deployment directory**: selecciona el directorio `WebContent` del proyecto
            - **Context path**: usa el mismo valor definido en `gradle.properties` (por defecto: `/etendo`)
            - **Before launch**: elimina todas las tareas por defecto

            ![add-new-configuration.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/add-new-configuration.png)

    6. Inicia Tomcat desde la configuración de ejecución:

        ![start-tomcat.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/start-tomcat.png)

=== "IntelliJ IDEA Ultimate"

    1. Descarga e instala [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download){target="_blank"}.

    2. Abre el directorio fuente de Etendo con IntelliJ.

    3. Configura la ejecución de Tomcat:

        - Ve a `Current File` > `Edit Configurations`.

            ![edit-configurations.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/edit-configurations.png)

        - Selecciona la configuración de Tomcat de la lista y verifica los ajustes del servidor Tomcat.

            ![add-new-configuration-ultimate.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/add-new-configuration-ultimate.png)

        - En la sección **Deployment**, añade fuentes externas y selecciona la carpeta `${env.CATALINA_HOME}/webapps/etendo`.

            ![add-external-source.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/add-external-source.png)

            ![config-deployment-folder.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/config-deployment-folder.png)

    4. Inicia Tomcat desde la configuración de ejecución.

## Acceder a la instalación

Una vez que Tomcat y los servicios Docker estén en ejecución:

| Interfaz | URL |
|---|---|
| **UI principal** | [http://localhost:3000](http://localhost:3000){target="_blank"} |
| **UI clásica** | [http://localhost:8080/etendo](http://localhost:8080/etendo){target="_blank"} |

!!! tip "Credenciales por defecto"
    Usuario: `admin`
    Contraseña: `admin`

## Opcional

### Habilitar logs de Etendo

1. Abre `config/log4j2-web.xml` y descomenta la referencia al appender `Console`:

    ```xml title="config/log4j2-web.xml"
    <Loggers>
        <Root level="info">
            <AppenderRef ref="RollingFile"/>
            <AppenderRef ref="Console"/>  <!-- uncomment this line -->
        </Root>
    ```

2. Ejecuta `smartbuild` para aplicar el cambio:

    ```bash title="Terminal"
    ./gradlew smartbuild --info
    ```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.