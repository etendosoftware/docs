---
title: Publish Modules to a Nexus Repository (deprecated)
---
## Overview

This article explains how to publish a module to Etendo’s Nexus Repositories.

A published module can be declared as a Gradle dependency, which makes installing or updating modules easier.

Using Nexus alongside with Gradle in an Etendo environment can remove the need to transfer the modules from a local machine to the server using FTP, SSH etc. The module hosted in Nexus and Gradle is in charge of downloading the correct version, and its dependencies.

Partners will have access to Etendo’s public and commercial repositories to download standard modules, in addition to their own Nexus repository where they can privately store their modules for internal or commercial usage.

> **Requirements**
> 
>   Nexus Access: distributed alongside your license (includes username, password and repository).
!!! info
      A module to be distributed. It must be compatible with any of Etendo's core version. In Openbravo terms, it needs to be at least compatible with 20Q2.2.

!!! success
    It is recommended to use [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) to manage work flow, versions and tags.

## Deployment

!!! info
    The module version, group and artifact that will deploy are those declared in the file `ad_module.xml`

1.  Register the module in the Nexus repository:

```plaintext

./gradlew registerModule -Prepo=<repositoryName> -Ppkg=<javapackage>
```

!!! info
    When user and password are asked, use your Nexus Access distributed alongside your license

> **Important:**
> 
>    -Manually add the modules dependencies declared in the ad\_module\_dependency.xml to the deploy.gradle generated in the module directory (registerModuletask create automatically deploy.gradle file in source).
>   -Make sure those dependencies are also deployed in Nexus.
>   -Manually add the JARS dependencies in build.gradle file.
!!! warning
      -Some dependencies are from modules that are already distributed with the Core. These dependencies do not need to be added, only add the dependency to the Core package (the core package includes the core itself, and all its modules).

Modules Dependencies example: `deploy.gradle`

```plaintext

group = 'com.etendo'
version = '3.8.200'
dependencies{
    compile 'com.smf.classic.core:ob:[20.2.1,20.2.2)@zip'
    //compile 'group:artifact:version@zip'
}
```

2.  In case of adding dependencies of a new repository, declare it in `deploy.gradle`

!!! info
    `jcenter()`, `maven-releases`, `maven-public-releases` and `maven-public-jars` repositories are not necessary to define.

Repository example:

!!! warning
    JAR dependencies should be defined in the same way, but in `build.gradle` file, and after expand you have to run build task to download the JARS declared.

3.  Deploy the new module, running the command :

```plaintext
./gradlew publishVersion -Ppkg=<javapackage>
```

!!! success
    Once Gradle finishes the deployment, your module will be ready to be used as a dependency. To publish next versions you only need to run the `publishVersion` command, since the module will be already registered.

!!! warning
    To deploy a next version, remember change it in `build.gradle` and `ad_module.xml`, otherwise it won’t be possible to deploy it.