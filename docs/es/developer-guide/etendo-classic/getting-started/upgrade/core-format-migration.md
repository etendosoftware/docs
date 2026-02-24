---
title: Migración del formato Core
tags:
    - Migración del Core
    - De JAR a código fuente
    - Dependencia del Core de Etendo
    - Configuración de Build Gradle
---

# Migración del formato Core

=== "De código fuente a JAR"

    !!! warning
        En formato JAR, no se pueden aplicar parches porque el Core se resuelve dinámicamente como una dependencia.


    1. Para migrar desde un entorno con código fuente, necesita añadir en el build.gradle la dependencia del core de Etendo 
    `implementation('com.etendoerp.platform:etendo-core:<version>')`


    2. Necesita eliminar todas las carpetas y archivos, dejando únicamente los que pertenecen a los directorios de adjuntos, gradle, módulos y configuración:

        - gradle/
        - attachments/
        - config/
        - modules/ 
        - build.gradle
        - gradle.properties
        - gradlew
        - gradlew.bat
        - settings.gradle

    3. Para actualizar el entorno tiene que ejecutar la tarea
        ``` bash title="Terminal" 
        ./gradlew update.database --info
        ```
        y ejecutar
        ``` bash title="Terminal" 
        ./gradlew compile.complete smartbuild --info
        ```

=== "De JAR a código fuente"

    1. Para migrar desde un entorno con JAR a código fuente, tiene que eliminar la dependencia del core de Etendo de su build.gradle y ejecutar
        ``` bash title="Terminal" 
        ./gradlew clean
        ```

    2. Para trabajar con código fuente, necesita especificar la versión a utilizar en el bloque de extensión del plugin de Etendo dentro del build.gradle

        ``` groovy title="build.gradle"
        etendo {
            coreVersion = "22.1.0"
        }
        ```

         Por defecto, Etendo intenta resolver el artefacto `com.etendoerp.platform:etendo-core`


        !!! info
            Tenga en cuenta el flag `supportJars`. Se utiliza para indicar si la versión actual del core soporta JAR o no. Por defecto está configurado a `true`.

    3. Por último, para descargar el código fuente necesita ejecutar la tarea de expansión del core.

        ``` bash title="Terminal"
        ./gradlew expandCore --info
        ```

    4. Recompilar
        ``` bash title="Terminal"
        ./gradlew compile.complete smartbuild --info
        ```

    5. Actualizar la base de datos
        ``` bash title="Terminal"
        ./gradlew update.database
        ```

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.