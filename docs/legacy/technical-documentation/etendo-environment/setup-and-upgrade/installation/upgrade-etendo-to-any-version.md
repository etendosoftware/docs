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

> From Etendo 22Q1, the Nexus credentials should not be required interactively. You must set them in the `gradle.properties` file, since Gradle resolves and checks dependencies periodically.
!!! warning
    `githubUser=USER` > `githubToken=TOKEN`

### Resolving the Etendo Gradle Plugin

From Etendo 22Q1, Etendo uses a standard gradle plugin to execute all the gradle tasks.
To work with the plugin you need to specify in the root project from where the plugin will be resolved.

1. Update the `settings.gradle` file with the next content.

`settings.gradle`

```groovy
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

```groovy
plugins {
    id 'com.etendoerp.gradleplugin' version 'latest.release'
}
```

3.  **Delete** if exist the old plugin removing the "apply from" line:

```
apply from: 'https://repo.futit.cloud/repository/static-public-releases/com/etendo/etendo/latest/etendo-latest.gradle'

```

### JAR Core

!!! warning
    If you upgrade from a source Etendo instance, read [Core Format Migration](/docs.etendo.software/legacy/technical-documentation/etendo-environment/setup-and-upgrade/installation/22q1/core-format-migration), because some directories must be deleted.

1. Create a backup of your environment, following the [Etendo Backup and Restore Tool](/docs.etendo.software/legacy/technical-documentation/etendo-environment/setup-and-upgrade/etendo-backup-restore-tool).
2. Verify the target version inside `build.gradle`

```groovy
dependencies {
  implementation('com.etendoerp.platform:etendo-core:<version>')
}
```

3. Compile your environment:

```plaintext

./gradlew update.database compile.complete smartbuild
```

5.  Verify any compilation errors that may arise due to incompatible customization or modifications.

!!! success
    Your Etendo environment is now updated!

### Source Core

1.  Verify the target version inside `build.gradle`

```groovy

// latest.release will download the most recent stable version
// Any other Gradle/Maven version sintax works, for example : [22.1.0,)
etendo {
   coreVersion = "latest.release"
}
```

> You can declare a specific version (e.g. '1.0.0') or an interval of versions:
> \[begin, end\] - Both versions are included
> (begin, end) - Both versions are not included
> \[begin, ) - From a base version to the latest one
!!! info
    And the other possible combinations

By default, the plugin will try to resolve the artifact `com.etendoerp.platform:etendo-core`

If you want to use a different artifact name, you can specify it in the plugin block.
For example `com.smf.classic.core:ob:21.4.1`

```groovy
etendo {
  coreGroup = "com.smf.classic.core"
	coreName = "ob"
  coreVersion = "21.4.1"
	supportJars = false
}
```

2.  Create a backup of your environment.
3.  Run the following command to update the core:

```plaintext

./gradlew expandCore
```

4.  Compile your environment:

```plaintext

./gradlew update.database compile.complete smartbuild
```

5.  Verify any compilation errors that may arise due to incompatible customization or modifications.

!!! success
    Your Etendo environment is now updated!
