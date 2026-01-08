---
title: Core format migration
tags:
    - Core Migration
    - JAR to Source
    - Etendo Core Dependency
    - Build Gradle Configuration
---

# Core format migration

=== "From Sources to JAR"

    !!! warning
        In JAR format, patchs can not be applied because the Core is resolved dinamically as a dependency.


    1. To migrate from an environment with sources, you need to add to the build.gradle, the Etendo core dependency 
    `implementation('com.etendoerp.platform:etendo-core:<version>')`


    2. You need to remove all the folders and files leaving the ones belonging to attachments,gradle, modules and config directories:

        - gradle/
        - attachments/
        - config/
        - modules/ 
        - build.gradle
        - gradle.properties
        - gradlew
        - gradlew.bat
        - settings.gradle

    3. To update the environment you have to execute the task
        ``` bash title="Terminal" 
        ./gradlew update.database --info
        ```
        and run
        ``` bash title="Terminal" 
        ./gradlew compile.complete smartbuild --info
        ```

=== "From JAR to Sources"

    1. To migrate from an environment with JARs to sources, you have to remove the Etendo core dependency from your build.gradle and run
        ``` bash title="Terminal" 
        ./gradlew clean
        ```

    2. To work with sources, you need to specify the version to use in the Etendo plugin extension block inside the build.gradle

        ``` groovy title="build.gradle"
        etendo {
            coreVersion = "22.1.0"
        }
        ```

         By default, Etendo tries to resolve the artifact `com.etendoerp.platform:etendo-core`


        !!! info
            Notice the `supportJars` flag. This is used to indicate if the current core version support JARs or not. By default is set to `true`.

    3. Finally, to download the sources you need to run the expand core task.

        ``` bash title="Terminal"
        ./gradlew expandCore --info
        ```

    4. Recompile
        ``` bash title="Terminal"
        ./gradlew compile.complete smartbuild --info
        ```

    5. Update the database
        ``` bash title="Terminal"
        ./gradlew update.database
        ```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
