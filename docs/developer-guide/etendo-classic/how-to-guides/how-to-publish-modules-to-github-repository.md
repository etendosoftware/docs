---
title: How to Publish Modules to a GitHub Repository
tags:
    - How to
    - GitHub
    - Module Deployment
    - Gradle
    - Publish Modules
---
## Overview

This article explains how to publish a module to GitHub Repositories.

Now, modules will be published in ZIP and JAR format.

A published module can be declared as a Gradle dependency, which makes installing or updating modules easier.

Using dependencies alongside with Gradle in an Etendo environment can remove the need to transfer the modules from a local machine to the server using FTP, SSH etc. The module is hosted as a package in the repository and  Gradle is in charge of downloading the correct version, and its dependencies.

Partners will have access to Etendo’s public and commercial repositories to download standard modules, in addition to this, it is possible to use their own repositories where they can privately store their modules for internal or commercial usage.

!!! info "Requirements"
    
    - GitHub user and token, with access to read and write packages.
    - A module to be distributed.

!!! success
    It is recommended to use [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow){target="_blank"} to manage work flow, versions and tags.

## Deployment

!!! info
    
    The module version, group and artifact that will deploy are those declared in the file `src-db/database/sourcedata/AD_MODULE.xml` file


#### 1.  Create build.gradle file:

To generate the `build.gradle` with all the necessary information to publish, execute the following task:

``` bash title="Terminal"
./gradlew createModuleBuild -Ppkg=<javapackage> -Prepo=<repositoryURL> --info
```
Example:
``` bash title="Terminal"
./gradlew createModuleBuild -Ppkg=com.myrepo.test -Prepo=https://maven.pkg.github.com/myrepo/com.myrepo.test --info
```

!!! warning "Important"
    - If the module depends on other modules or libraries, they need to be specified in the build.gradle file using the implementation configuration.
    Before adding an Etendo module dependency, they have to be published in the repository.
    - You need to make sure those dependencies are also published.
    - Add the dependencies manually in `build.gradle` file.
    - Add Core dependency to define the range of versions the module is compatible with.

!!! info
    To make use of the dependencies resolution approach, you should declare in the modules dependencies which version of the core your module depends on.
    If the Etendo Core dependency is omitted, the module can be installed on any version of Etendo, even if there are inconsistencies in the compilation.



Modules Dependencies example:

```groovy title="build.gradle"
/**
*   This file was generated automatically by the 'createModuleBuild' task.
*   Created at: 2022-12-16T15:41:21.426339Z.
*
*   WARNING: Do not put your credentials directly in this file.
*
*/

group          = "com.etendoerp"
version        = "1.0.0"
description    = "Test module to publish"
ext.artifact   = "test"
ext.repository = "https://maven.pkg.github.com/myrepo/com.myrepo.test"

configurations {
    moduleDependencyContainer
}

publishing {
    publications {
        "com.myrepo.test"(MavenPublication) {
            from components.java
            groupId    = group
            artifactId = artifact
            version    = version
        }
    }
    repositories {
        maven {
            url "https://maven.pkg.github.com/myrepo/com.myrepo.test"
        }
    }
}

repositories {
    mavenCentral()
    maven {
        url "https://maven.pkg.github.com/myrepo/com.myrepo.test"
    }
}

/**
* Declare Java dependencies using 'implementation'
* Ex: implementation "com.sun.mail:javax.mail:1.6.2"
*/
dependencies {

    implementation('com.myrepo:dependency.test:1.0.0')
    
   	implementation('com.etendoerp.platform:etendo-core:[22.1.0, x.y.z)')
}

```

#### 2.  In case of adding dependencies of a new repository, declare it in `build.gradle`

```groovy title="build.gradle"
repositories {
    mavenCentral()
    maven {
        url "https://maven.pkg.github.com/myrepo/com.myrepo.test"
    }
     maven {
        url "https://maven.pkg.github.com/myrepo2/com.myrepo2.test"
    }
}
```



#### 3. If your module makes use of dependency injection, you need to specify the location of the **'beans.xml'** file

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
!!! info
    Before publishing a module, it will be compiled and packaged to a JAR format.

``` bash title="Terminal"
./gradlew update.database smartbuild
```
``` bash title="Terminal"
./gradlew publishVersion -Ppkg=<javapackage>
```


!!! success
    Once Gradle finishes the deployment, your module is ready to be used as a dependency.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

