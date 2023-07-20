---
title: Publish Modules to a Nexus Repository
---


## Overview
!!! warning
   The publication of modules changed from Etendo 22Q1, to review the previous documentation see the following  link [Publish modules to a Nexus repository | 21Q4](https://docs.etendo.software/e/en/technical-documentation/etendo-environment/platform/publish-modules-to-a-nexus-repository)  

This article explains how to publish a module to Etendo’s Nexus Repositories.

Now, modules will be JAR files.

A published module can be declared as a Gradle dependency, which makes installing or updating modules easier.

Using Nexus alongside with Gradle in an Etendo environment can remove the need to transfer the modules from a local machine to the server using FTP, SSH etc. The module hosted in Nexus and Gradle is in charge of downloading the correct version, and its dependencies.

Partners will have access to Etendo’s public and commercial repositories to download standard modules, in addition to their own Nexus repository where they can privately store their modules for internal or commercial usage.

> **Requirements**
> 
> -Nexus Access: distributed alongside your license (includes username, password and repository).
!!! info
    -A module to be distributed. It must be compatible with any of Etendo's core version. In Openbravo terms, it needs to be at least compatible with 21Q3.2.

!!! success
    It is recommended to use [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) to manage work flow, versions and tags.

## Deployment    

!!! warning
    **Important:**
    Before following the steps in this section, remember that, to publish following versions, it is only necessary to run the `publishVersion` command, since the module will be already registered. To deploy the next version, export the new version and remember to change it in `build.gradle`

!!! info
    The module version, group and artifact that will deploy are those declared in the file `ad_module.xml` file

> **Note:** 
If you only need to generate the `build.gradle` with all the necessary information to publish, execute the following task:
> `./gradlew createModuleBuild --info`
> Command line parameters:
>   	 `-Ppkg=<package name>` The name of the module.
!!! info
         `-Prepo=<repository name>` The name of the repository.


#### 1.  Register the module in the Nexus repository:

Create the privileges to publish a new module in a specific repository and generate the `build.gradle` file.

- `./gradlew registerModule --info` 
Command line parameters:
	 `-Ppkg=<package name>` The name of the module.
	 `-Prepo=<repository name>` The name of the repository.

!!! success
    When user and password are asked, use your Nexus Access distributed alongside your license.


> **Important:**
> 
> -If the module depends on others Etendo modules or libraries, they need to be specified in the **build.gradle** file using the **implementation** configuration.
Before adding an Etendo module dependency, they have to be published in Nexus.
> -You need to make sure those dependencies are also deployed in Nexus.
> -Add the JARs dependencies manually in build.gradle file.
!!! warning
    -Add Core dependency to define the range of versions the module is compatible with.

!!! info
    To make use of the dependencies **resolution** approach, you should declare in the modules dependencies which version of the core your module depends on.



Modules Dependencies example: `build.gradle`

```groovy
/**
*   This file was generated automatically by the 'createModuleBuild' task.
*   Created at: 2022-03-18T19:12:16.265001Z.
*
*   WARNING: Do not put your credentials directly in this file.
*
*/

group          = "com.etendoerp"
version        = "1.0.0"
description    = "test"
ext.artifact   = "test"
ext.repository = "https://repo.futit.cloud/repository/maven-snapshot"

configurations {
    moduleDependencyContainer
}

publishing {
    publications {
        "com.etendo.test"(MavenPublication) {
            from components.java
            groupId    = group
            artifactId = artifact
            version    = version
        }
    }
    repositories {
        maven {
            url "https://repo.futit.cloud/repository/maven-snapshot"
        }
    }
}

repositories {
    mavenCentral()
    maven {
        url "https://repo.futit.cloud/repository/maven-snapshot"
    }
    maven {
        url "https://repo.futit.cloud/repository/maven-releases"
    }
    maven {
        url "https://repo.futit.cloud/repository/maven-public-jars"
    }
}

/**
* Declare Java dependencies using 'implementation'
* Ex: implementation "com.sun.mail:javax.mail:1.6.2"
*/
dependencies {
    // Etendo dependency
   	implementation 'com.etendoerp:etendo-module:1.0.0'
    
    // Library dependency
   	implementation 'javax.mail:mail:1.4'
    
    // Etendo CORE dependency
    implementation 'com.etendoerp.platform:etendo-core:[22.1.0, 22.1.1]'

}

```

#### 2.  In case of adding dependencies of a new repository, declare it in `build.gradle`

!!! info
   `maven-releases`, `maven-public-releases` and `maven-public-jars` repositories are not necessary to define.


#### 3. If your module makes use of **dependency injection**, you need to specify the location of the **'beans.xml'** file

Add to the build.gradle the location of the beans.xml
``` groovy
sourceSets {
    main {
        resources {
            srcDirs("etendo-resources")
        }
    }
}
```

Create the following structure in the root of your module
``` 
com.test.yourmodule
	|--- etendo-resources
  			| --- META-INF
        			| --- beans.xml
```

Add to the **beans.xml**

``` xml
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/beans_2_0.xsd" bean-discovery-mode="all" version="2.0">
</beans>
```

#### 4.  Deploy the new module, running the commands :


```plaintext
./gradlew update.database smartbuild
```
```plaintext
./gradlew publishVersion -Ppkg=<javapackage>
```
!!! info
    Before publishing a module, it will be compiled and packaged to a JAR format.

!!! success
    Once Gradle finishes the deployment, your module will be ready to be used as a dependency.



