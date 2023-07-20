---
title: Use of gradle in Etendo
---
## Overview

This article explains how to use Gradle, an open-source build automation tool that is designed to be flexible enough to build almost any type of software. (For additional info read: [What is gradle?](https://docs.gradle.org/current/userguide/what_is_gradle.html))

Etendo uses Gradle to define and improve compilation, version management, modules publication, migrations and more tasks.

## How to use Gradle

Etendo project includes an embedded wrapper from Gradle called `gradlew`. Run the `./gradlew <task>` command in the Etendo project directory, and it will execute the mentioned task.

You can use `-P<Parameter Name>` to pass parameters in a task. For example:

```plaintext

./gradlew publishVersion -Ppkg=test.package
```

### Common Gradle tasks

-   `smartbuild`
-   `update.database`
-   `export.database`
-   `compile.complete`
-   `expand`: Task to resolve and download all declared dependencies.
-   `expandCore`: Task to download core dependency.
-   `expandModules`: Task to resolve and download all dependencies declared in each module.
-   `registerModule`: Task to request permission to publish a module in a repository.
-   `publishVersion`: Task to publish in Nexus a specific module.
-   `normalize`: Task to change automatically all local modules by dependencies available in Nexus.
-   `normalizeModule`: Task to normalize a specified module.
-   `createModuleBuild`: Task to create build.gradle file (used to publish a new module in Nexus, declare dependencies and repositories).

### Ant tasks
Most of [ant build tasks](http://wiki.openbravo.com/wiki/Development_Build_Tasks#Detailed_Build_Tasks), previously used in Openbravo, can be run with Gradle (but they do not have support):

```plaintext
./gradlew <ant task> [params] 
```
 Except some commands:
|Old Command| New Command|
|---|---|
|clean| antClean|
|setup|antSetup|
|init |antInit|
|install.source|antInstall|
|war|antWar|



### Common Gradle flags
|Flag| Description|
|---|---|
|--offline| To execute Gradle without internet connection. |
|--stop|To stop all Gradle daemons.|
|--no-daemon|To execute a Gradle task without launching a daemon. |
|--info|To give more information in the task execution.|
|--refresh-dependencies|will force download of dependencies.|