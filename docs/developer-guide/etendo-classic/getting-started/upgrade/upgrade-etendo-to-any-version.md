---
title: Upgrade Etendo to Any Version
tags:
    - Etendo Upgrade
    - Update Etendo
    - Version Management
    - Gradle Plugin
    - Core
---

# Upgrade Etendo to Any Version

## Overview

This guide explains how to upgrade your Etendo environment to any version you want. 

!!! info
    Only if you are upgrading from *Etendo 21* is it necessary to follow the guide [Upgrading from Etendo 21 to Any Version](#upgrading-from-etendo-21-to-any-version). In all other cases simply follow the current guide. 

**Checklist**

- [X] Create a backup.
- [X] Verify the technology stack required for the target version (Gradle, Java SE, PostgreSQL, Apache Tomcat).
- [X] Update the Etendo version.
- [X] Update the Etendo Gradle Plugin version.
- [X] Review and update bundles version if necessary.
- [X] Expand (download) the Core or modules when using the Source format (if applicable).
- [X] Compile the environment and resolve any issues.


### Backup

!!! warning "It is essential to create a backup before starting the upgrade process!"  
    
    - A complete backup of your environment ensures you can restore your system in case of any issues during the upgrade.  
    - You can use the [Etendo Backup and Restore Gradle Plugin](../../developer-tools/etendo-backup-restore-tool.md) to easily and safely create and restore backups.

### Stack Upgrade

**Gradle Upgrade**
    
- If you are upgrading to **Etendo 24** or prior, update Gradle by running:
  
    ```bash title="Terminal"
    ./gradlew wrapper --gradle-version 7.3.2
    ```

- If you are upgrading to **Etendo 25**, update Gradle by running:
  
    ```bash title="Terminal"
    ./gradlew wrapper --gradle-version 8.12.1
    ```

**Full Stack Upgrade**

The required technology stack depends on the target version.

- For Etendo versions prior to **Etendo 25**, the initial stack remains unchanged, For more information, visit: [Etendo 24 and Earlier - Software Stack](../../../../getting-started/requirements.md#etendo-24-and-earlier)

- If you are migrating to **Etendo 25**, you must first update the **entire technology stack** (Java SE, PostgreSQL, Apache Tomcat). For more information, visit: [Etendo 25 - Software Stack](../../../../getting-started/requirements.md#etendo-25)
   
    !!!tip 
        The [Developer Changelog](../../developer-changelog/apichanges.md) guide provides details about the required stack and possible changes needed in custom modules. 

### Etendo Upgrade

Etendo can be installed or upgraded using two formats: Source or JAR. The Source format is the most common and allows you to modify the application code. The JAR format is more efficient, as it uses precompiled classes, but does not allow code changes.

#### Etendo in Source Format (Most Used)
    
1. Verify the **Etendo** core version inside `build.gradle`, it is recommended to set a fixed version. You can find the list of versions and their statuses in the [Etendo - Release Notes](../../../../whats-new/release-notes/etendo-classic/release-notes.md). It is recommended always updating to the latest *Confirmed Stable (CS)* version available. 

  
    ```groovy title="build.gradle"

    etendo {
        coreVersion = "<version>"
    }
    ```

    !!! info
        You can declare a specific version (e.g. "25.1.0") or an interval of versions:<br>
                - [begin, end] - Both versions are included<br>
                - (begin, end) - Both versions are not included<br>
                - [begin, ) - From a base version to the latest one<br>
        And the other possible combinations.

2. Verify the **Etendo Gradle Plugin** version and update it to the latest *Confirmed Stable (CS)* version available for the Etendo version you are upgrading to. For more information visit [Etendo Gradle Plugin - Release Notes](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) 

    ```groovy title="build.gradle"
    plugins {
        id 'com.etendoerp.gradleplugin' version '<version>'
    }
    ```

3.  Run the following command to upgrade the core:

    ``` bash title="Terminal"

    ./gradlew expandCore --info
    ```
    !!! warning 
        You may need to force the execution of this task, since by default for security reasons it is not possible to expand the core if it detects modules that are not yet compatible. To do this, add the following to the `build.gradle` file:

        ``` groovy title="build.gradle"
        etendo {
            forceResolution = true 
        }
        ``` 

        Remember to remove this configuration after the update to avoid future errors.


4. If there are **bundle dependencies** declared in the `build.gradle` file, you must upgrade those dependencies to the compatible version with the updated Etendo. You can get more information and the versions of each bundle compatible with each Etendo version at [Etendo Marketplace](https://marketplace.etendo.cloud/){target="\_blank"}.

    !!! info 
        Only if the dependencies are installed in **Source format** you must expand them by running:

        ``` bash title="Terminal"

        ./gradlew expandModules --info
        ```

5.  Compile the environment:

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```

6.  Check for any compilation errors that may occur due to incompatible customizations or modifications.

    !!! warning
        Remember to review the API Changes that may affect modules installed in **Etendo 25** or later. For more information, visit: [Etendo API Changes](../../developer-changelog/apichanges.md)

    !!! success
        Your Etendo environment is now updated!
     


#### Etendo in JAR format (Recommended for Less Customized and Dynamic Environments)

1. Verify the **Etendo** target version inside `build.gradle`, it is recommended to set a fixed version. You can find the list of versions and their statuses in the [Etendo - Release Notes](../../../../whats-new/release-notes/etendo-classic/release-notes.md). It is recommended always updating to the latest *Confirmed Stable (CS)* version available. 

    ```groovy title="build.gradle"
    dependencies {
        implementation('com.etendoerp.platform:etendo-core:<version>')
    }
    ```

2. Verify the **Etendo Gradle Plugin** version and update it to the latest *Confirmed Stable (CS)* version available for the Etendo version you are upgrading to. For more information visit [Etendo Gradle Plugin - Release Notes](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) 

    ```groovy title="build.gradle"
    plugins {
        id 'com.etendoerp.gradleplugin' version '<version>'
    }
    ```

3. If there are **bundle dependencies** declared in the `build.gradle` file, you must upgrade those dependencies to the compatible version with the updated Etendo. You can get more information and the versions of each bundle compatible with each Etendo version at [Etendo Marketplace](https://marketplace.etendo.cloud/){target="\_blank"}.

    !!! info
        Only if the dependencies are installed in **Source format** you must expand them by running:

        ``` bash title="Terminal"

        ./gradlew expandModules --info
        ```


4. Compile the environment:

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild --info
    ```

    !!! warning 
        
        When running this task, all dependencies including Etendo Core will be resolved dynamically. You may need to force the execution of this task, since by default for security reasons it is not possible to expand the core if it detects modules that are not yet compatible. To do this, add the following to the `build.gradle` file:

        ``` groovy title="build.gradle"
        etendo {
            forceResolution = true 
        }
        ``` 

        Remember to remove this configuration after the update to avoid future errors.
    

5.  Verify any compilation errors that may arise due to incompatible customization or modifications.

    
    !!! warning
        Remember to review the API Changes that may affect modules installed in **Etendo 25** or later. For more information, visit: [Etendo API Changes](../../developer-changelog/apichanges.md)


    !!! success
        Your Etendo environment is now updated!


## Upgrading from Etendo 21 to Any Version 


- In case of upgrading the Etendo Core from **Etendo 21**, you must check if exist and remove the following modules from the `/modules` directory, as they are distributed into the Etendo Core:

    - `com.smf.securewebservices`
    - `com.smf.smartclient.boostedui`
    - `com.smf.smartclient.debugtools` 

- From **Etendo 22**, credentials for accessing packages in Etendo repositories must be configured in the `gradle.properties` file, as Gradle resolves and checks dependencies dynamically. You must set `githubUser`  and  `githubToken`. For more information, visit: [Use of Repositories in Etendo](../installation/use-of-repositories-in-etendo.md)


### Resolving the Etendo Gradle Plugin for First Time

From **Etendo 22**, Etendo uses a standard Gradle plugin to execute all the Gradle tasks.
To work with this plugin you need to specify in the root project from where the plugin will be resolved.

1. Create or update the `settings.gradle` file with the next content:

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

2. Add in the `build.gradle` file the latest confirmed stable (CS) **Etendo Gradle Plugin** version compatible with the  Etendo version you are upgrading to. For more information visit [Etendo Gradle Plugin - Release Notes](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md)
    
    ```groovy title="build.gradle"
    plugins {
        id 'com.etendoerp.gradleplugin' version '<version>'
    }
    ```

3.  Delete if the old plugin exists removing the "apply from" line:

    ``` bash title="Terminal"
    apply from: 'https://repo.futit.cloud/repository/static-public-releases/com/etendo/etendo/latest/etendo-latest.gradle'

    ```
4.  Continue with the [Etendo Upgrade](#etendo-upgrade) section.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
