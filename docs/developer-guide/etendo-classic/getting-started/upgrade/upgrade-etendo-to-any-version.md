---
title: Upgrade Etendo to Any Version
---

## Overview

This guide explains how to upgrade your Etendo environment to the latest version, or any version you want.

## Upgrade Etendo

!!! warning
    In case of upgrading the Core to 23.1.0 or newer, you must run `./gradlew wrapper --gradle-version 7.3.2` to upgrade the Gradle version.

!!! warning
    In case of upgrading the Core from Etendo 21Q4.X, you must remove the modules `com.smf.securewebservices`, `com.smf.smartclient.boostedui`, `com.smf.smartclient.debugtools`, as they are distributed in the Core.

!!! warning
    From Etendo 22Q1, the Nexus credentials should not be required interactively. You must set them in the `gradle.properties` file, since Gradle resolves and checks dependencies periodically.
    `githubUser=USER` > `githubToken=TOKEN`

### Resolving the Etendo Gradle Plugin

From Etendo 22Q1, Etendo uses a standard gradle plugin to execute all the gradle tasks.
To work with the plugin you need to specify in the root project from where the plugin will be resolved.

1. Update the `settings.gradle` file with the next content.

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

2. Add in the `build.gradle` file the Etendo Gradle Plugin

    ```groovy title="build.gradle"
    plugins {
        id 'com.etendoerp.gradleplugin' version 'latest.release'
    }
    ```

3.  Delete if the old plugin exists removing the "apply from" line:

``` bash title="Terminal"
apply from: 'https://repo.futit.cloud/repository/static-public-releases/com/etendo/etendo/latest/etendo-latest.gradle'

```

=== "JAR Core"

    !!! warning
        If you upgrade from a source Etendo instance, read [Core Format Migration](/docs/developer-guide/etendo-classic/getting-started/upgrade/core-format-migration/), because some directories must be deleted.

    1. Create a backup of your environment, following the [Etendo Backup and Restore Tool](/docs/developer-guide/etendo-classic/developer-tools/etendo-backup-restore-tool/).
    2. Verify the target version inside `build.gradle`

        ```groovy title="build.gradle"
        dependencies {
        implementation('com.etendoerp.platform:etendo-core:<version>')
        }
        ```

    3. Compile your environment:

        ``` bash title="Terminal"
        ./gradlew update.database compile.complete smartbuild
        ```

    4.  Verify any compilation errors that may arise due to incompatible customization or modifications.

        !!! success
            Your Etendo environment is now updated!

=== "Source Core"

    1.  Verify the target version inside `build.gradle`

        ```groovy title="build.gradle"

        // latest.release will download the most recent stable version
        // Any other Gradle/Maven version sintax works, for example : [22.1.0,)
        etendo {
        coreVersion = "latest.release"
        }
        ```

        !!! info
            You can declare a specific version (e.g. '1.0.0') or an interval of versions:<br>
                    - [begin, end] - Both versions are included<br>
                    - (begin, end) - Both versions are not included<br>
                    - [begin, ) - From a base version to the latest one<br>
            And the other possible combinations.


    2.  Create a backup of your environment.
    3.  Run the following command to update the core:

        ``` bash title="Terminal"

        ./gradlew expandCore
        ```

    4.  Compile your environment:

        ``` bash title="Terminal"

        ./gradlew update.database compile.complete smartbuild
        ```

    5.  Verify any compilation errors that may arise due to incompatible customization or modifications.

    !!! success
        Your Etendo environment is now updated!
