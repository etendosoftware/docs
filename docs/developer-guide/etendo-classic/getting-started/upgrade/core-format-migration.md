---
title: Core format migration
---
## Core format migration

#### From Sources to JAR

!!! warning
    In JAR format patchs can not be applied beacause the Core is resolved dinamicaly as a dependency.


1. To migrate from a environment with sources, you need to add to the build.gradle, the Etendo core dependency

    ``` groovy
    dependencies {
      implementation group: 'com.etendoerp.platform', name: 'etendo-core', version: '22.1.0'
    }
    ```

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

3. To update the environment you have to execute the `./gradlew update.database --info` task, and run `./gradlew compile.complete smartbuild --info`

#### From JAR to Sources

To migrate from a environment with JARs to sources, you have to remove the Etendo core dependency from your build.gradle and run a `./gradlew clean`

To work with sources, you need to specify the version to use in the Etendo plugin extension block inside the build.gradle

``` groovy
etendo {
	coreVersion = "22.1.0"
}
```

By default, Etendo will try to resolve the artifact `com.etendoerp.platform:etendo-core`


!!! info
    Notice the `supportJars` flag. This is used to indicate if the current core version support JARs or not. By default is set to `true`

Finally, to download the sources you need to run the expand core task.

`./gradlew expandCore --info`

Recompile

`./gradlew compile.complete smartbuild --info`

Update the database

`./gradlew update.database`
