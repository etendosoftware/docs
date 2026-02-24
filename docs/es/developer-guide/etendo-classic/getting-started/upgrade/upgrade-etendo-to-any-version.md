---
title: Actualizar Etendo a cualquier versión
tags:
    - Actualización de Etendo
    - Actualizar Etendo
    - Gestión de versiones
    - Plugin de Gradle
    - Core
---

# Actualizar Etendo a cualquier versión

## Visión general

Esta guía explica cómo actualizar su entorno de Etendo a cualquier versión que desee. 

!!! info
    Solo si está actualizando desde *Etendo 21* es necesario seguir la guía [Actualizar desde Etendo 21 a cualquier versión](#actualizar-desde-etendo-21-a-cualquier-versión). En todos los demás casos, simplemente siga la guía actual. 

**Lista de verificación**

- [X] Crear una copia de seguridad.
- [X] Verificar la pila tecnológica requerida para la versión objetivo (Gradle, Java SE, PostgreSQL, Apache Tomcat).
- [X] Actualizar la versión de Etendo.
- [X] Actualizar la versión del plugin de Gradle de Etendo.
- [X] Revisar y actualizar la versión de los bundles si es necesario.
- [X] Expandir (descargar) el Core o los módulos al usar el formato Source (si aplica).
- [X] Compilar el entorno y resolver cualquier incidencia.


### Copia de seguridad

!!! warning "¡Es esencial crear una copia de seguridad antes de iniciar el proceso de actualización!"  
    
    - Una copia de seguridad completa de su entorno garantiza que pueda restaurar su sistema en caso de cualquier problema durante la actualización.  
    - Puede usar el [Plugin de Gradle de copia de seguridad y restauración de Etendo](../../developer-tools/etendo-backup-restore-tool.md) para crear y restaurar copias de seguridad de forma fácil y segura.

### Actualización de la pila

**Actualización de Gradle**
    
- Si está actualizando a **Etendo 24** o anterior, actualice Gradle ejecutando:
  
    ```bash title="Terminal"
    ./gradlew wrapper --gradle-version 7.3.2
    ```

- Si está actualizando a **Etendo 25**, actualice Gradle ejecutando:
  
    ```bash title="Terminal"
    ./gradlew wrapper --gradle-version 8.12.1
    ```

**Actualización completa de la pila**

La pila tecnológica requerida depende de la versión objetivo.

- Para versiones de Etendo anteriores a **Etendo 25**, la pila inicial permanece sin cambios. Para más información, visite: [Etendo 24 and Earlier - Software Stack](../../../../getting-started/requirements.md#etendo-24-and-earlier)

- Si está migrando a **Etendo 25**, primero debe actualizar **toda la pila tecnológica** (Java SE, PostgreSQL, Apache Tomcat). Para más información, visite: [Etendo 25 - Software Stack](../../../../getting-started/requirements.md#etendo-25)
   
    !!!tip 
        La guía [Developer Changelog](../../developer-changelog/apichanges.md) proporciona detalles sobre la pila requerida y los posibles cambios necesarios en módulos personalizados. 

### Actualización de Etendo

Etendo puede instalarse o actualizarse usando dos formatos: Source o JAR. El formato Source es el más común y permite modificar el código de la aplicación. El formato JAR es más eficiente, ya que utiliza clases precompiladas, pero no permite cambios de código.

#### Etendo en formato Source (más utilizado)
    
1. Verifique la versión del core de **Etendo** dentro de `build.gradle`; se recomienda establecer una versión fija. Puede encontrar la lista de versiones y sus estados en [Etendo - Release Notes](../../../../whats-new/release-notes/etendo-classic/release-notes.md). Se recomienda actualizar siempre a la última versión *Confirmed Stable (CS)* disponible. 

  
    ```groovy title="build.gradle"

    etendo {
        coreVersion = "<version>"
    }
    ```

    !!! info
        Puede declarar una versión específica (p. ej., "25.1.0") o un intervalo de versiones:<br>
                - [begin, end] - Ambas versiones están incluidas<br>
                - (begin, end) - Ambas versiones no están incluidas<br>
                - [begin, ) - Desde una versión base hasta la última<br>
        Y las demás combinaciones posibles.

2. Verifique la versión del **plugin de Gradle de Etendo** y actualícela a la última versión *Confirmed Stable (CS)* disponible para la versión de Etendo a la que está actualizando. Para más información, visite [Etendo Gradle Plugin - Release Notes](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) 

    ```groovy title="build.gradle"
    plugins {
        id 'com.etendoerp.gradleplugin' version '<version>'
    }
    ```

3. Ejecute el siguiente comando para actualizar el core:

    ``` bash title="Terminal"

    ./gradlew expandCore --info
    ```
    !!! warning 
        Puede que necesite forzar la ejecución de esta tarea, ya que por defecto, por motivos de seguridad, no es posible expandir el core si detecta módulos que aún no son compatibles. Para ello, añada lo siguiente al archivo `build.gradle`:

        ``` groovy title="build.gradle"
        etendo {
            forceResolution = true 
        }
        ``` 

        Recuerde eliminar esta configuración después de la actualización para evitar errores futuros.


4. Si hay **dependencias de bundles** declaradas en el archivo `build.gradle`, debe actualizar esas dependencias a la versión compatible con el Etendo actualizado. Puede obtener más información y las versiones de cada bundle compatibles con cada versión de Etendo en [Etendo Marketplace](https://marketplace.etendo.cloud/){target="\_blank"}.

    !!! info 
        Solo si las dependencias están instaladas en **formato Source** debe expandirlas ejecutando:

        ``` bash title="Terminal"

        ./gradlew expandModules --info
        ```

5. Compile el entorno:

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```

6. Compruebe si se producen errores de compilación debido a personalizaciones o modificaciones incompatibles.

    !!! warning
        Recuerde revisar los cambios de la API que puedan afectar a los módulos instalados en **Etendo 25** o posterior. Para más información, visite: [Etendo API Changes](../../developer-changelog/apichanges.md)

    !!! success
        ¡Su entorno de Etendo ya está actualizado!
     


#### Etendo en formato JAR (recomendado para entornos menos personalizados y dinámicos)

1. Verifique la versión objetivo de **Etendo** dentro de `build.gradle`; se recomienda establecer una versión fija. Puede encontrar la lista de versiones y sus estados en [Etendo - Release Notes](../../../../whats-new/release-notes/etendo-classic/release-notes.md). Se recomienda actualizar siempre a la última versión *Confirmed Stable (CS)* disponible. 

    ```groovy title="build.gradle"
    dependencies {
        implementation('com.etendoerp.platform:etendo-core:<version>')
    }
    ```

2. Verifique la versión del **plugin de Gradle de Etendo** y actualícela a la última versión *Confirmed Stable (CS)* disponible para la versión de Etendo a la que está actualizando. Para más información, visite [Etendo Gradle Plugin - Release Notes](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) 

    ```groovy title="build.gradle"
    plugins {
        id 'com.etendoerp.gradleplugin' version '<version>'
    }
    ```

3. Si hay **dependencias de bundles** declaradas en el archivo `build.gradle`, debe actualizar esas dependencias a la versión compatible con el Etendo actualizado. Puede obtener más información y las versiones de cada bundle compatibles con cada versión de Etendo en [Etendo Marketplace](https://marketplace.etendo.cloud/){target="\_blank"}.

    !!! info
        Solo si las dependencias están instaladas en **formato Source** debe expandirlas ejecutando:

        ``` bash title="Terminal"

        ./gradlew expandModules --info
        ```


4. Compile el entorno:

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```

    !!! warning 
        
        Al ejecutar esta tarea, todas las dependencias, incluido Etendo Core, se resolverán dinámicamente. Puede que necesite forzar la ejecución de esta tarea, ya que por defecto, por motivos de seguridad, no es posible expandir el core si detecta módulos que aún no son compatibles. Para ello, añada lo siguiente al archivo `build.gradle`:

        ``` groovy title="build.gradle"
        etendo {
            forceResolution = true 
        }
        ``` 

        Recuerde eliminar esta configuración después de la actualización para evitar errores futuros.
    

5. Verifique cualquier error de compilación que pueda surgir debido a personalizaciones o modificaciones incompatibles.

    
    !!! warning
        Recuerde revisar los cambios de la API que puedan afectar a los módulos instalados en **Etendo 25** o posterior. Para más información, visite: [Etendo API Changes](../../developer-changelog/apichanges.md)


    !!! success
        ¡Su entorno de Etendo ya está actualizado!


## Actualizar desde Etendo 21 a cualquier versión 


- En caso de actualizar el Core de Etendo desde **Etendo 21**, debe comprobar si existen y eliminar los siguientes módulos del directorio `/modules`, ya que se distribuyen dentro del Core de Etendo:

    - `com.smf.securewebservices`
    - `com.smf.smartclient.boostedui`
    - `com.smf.smartclient.debugtools` 

- A partir de **Etendo 22**, las credenciales para acceder a paquetes en los repositorios de Etendo deben configurarse en el archivo `gradle.properties`, ya que Gradle resuelve y comprueba dependencias dinámicamente. Debe establecer `githubUser` y `githubToken`. Para más información, visite: [Uso de repositorios en Etendo](../installation/use-of-repositories-in-etendo.md)


### Resolver el plugin de Gradle de Etendo por primera vez

A partir de **Etendo 22**, Etendo utiliza un plugin estándar de Gradle para ejecutar todas las tareas de Gradle.
Para trabajar con este plugin, necesita especificar en el proyecto raíz desde dónde se resolverá el plugin.

1. Cree o actualice el archivo `settings.gradle` con el siguiente contenido:

    ```groovy title="settings.gradle"
    pluginManagement {
        repositories {
            mavenCentral()
            gradlePluginPortal()
            maven {
                url 'https://maven.pkg.github.com/etendosoftware/com.etendoerp.gradleplugin'
                credentials {
                    username "${githubUser}"
                    password "${githubToken}"
                }
            }
            maven {
                url 'https://repo.futit.cloud/repository/maven-public-snapshots'
            }
        }
    }

    // Add modules subprojects
    new File("${this.rootDir}/modules").listFiles().each {
        if (it.directory && new File(it, 'build.gradle').exists()) {
            include(":modules:${it.name}")
        }
    }

    rootProject.name = "etendo"
    ```

2. Añada en el archivo `build.gradle` la última versión confirmada estable (CS) del **plugin de Gradle de Etendo** compatible con la versión de Etendo a la que está actualizando. Para más información, visite [Etendo Gradle Plugin - Release Notes](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md)
    
    ```groovy title="build.gradle"
    plugins {
        id 'com.etendoerp.gradleplugin' version '<version>'
    }
    ```

3. Elimine el plugin antiguo si existe, quitando la línea "apply from":

    ``` bash title="Terminal"
    apply from: 'https://repo.futit.cloud/repository/static-public-releases/com/etendo/etendo/latest/etendo-latest.gradle'

    ```
4. Continúe con la sección [Actualización de Etendo](#actualización-de-etendo).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.