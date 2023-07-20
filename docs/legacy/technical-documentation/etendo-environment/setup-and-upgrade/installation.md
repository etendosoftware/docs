---
title: Installation
---
## Overview
This section explains how to install a new Etendo environment. It includes:
- Tutorial about the Etendo installation.
- The steps to install Etendo.

## Tutorial

###
<iframe width="560" height="315" src="https://www.youtube.com/embed/ixNnRuL10xo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Etendo Installation

### Requirements 
In this section, you can read the [System Requirements](https://docs.etendo.software/en/technical-documentation/etendo-environment/requirements-and-tools/requirements).


### Install Etendo in Source format
#### Steps
1.  Clone Etendo Base project in a temporal directory.

``` bash
cd /tmp
git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
```

2.  Copy the sources in /opt/EtendoERP folder.
```bash

mv EtendoERP/* /opt/EtendoERP/
cd /opt/EtendoERP
```
3. Modify the `gradle.properties` file with your GitHub Credentials. Create the credentials by following this [guide](https://docs.etendo.software/en/technical-documentation/etendo-environment/requirements-and-tools/developer-tools/use-of-repositories-in-etendo).

```groovy
githubUser=username
githubToken=*******

context.name=etendo

bbdd.sid=etendo
bbdd.port=5432
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
bbdd.user=tad
bbdd.password=tad

org.gradle.jvmargs=-Xmx2g -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encod>

```

4.  Expand Etendo Base

```
./gradlew expand 
```
5. Modify the `gradle.properties` file with your environment variables, if it is necessary:

```
context.name=etendo

bbdd.sid=etendo
bbdd.port=5432
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
bbdd.user=tad
bbdd.password=tad
```

6. Setup: to apply or create the initial configurations
```
./gradlew setup
```
7. Installation: Create the database, compile the sources and deploy to Apache Tomcat
```
./gradlew install smartbuild
```
8.  Start the Tomcat, in case of Linux you can run:
```
sudo /etc/init.d/tomcat start
```
9. Open your browser in `https://<Public server IP>/<Context Name>`


### Install Etendo in JAR format
!!! warning
    From Etendo *22.1.x* Etendo is distributed as Source (Zip) and JAR format. For more information [Etendo JARs](https://docs.etendo.software/en/technical-documentation/etendo-environment/platform/22q1/etendo-jars)

#### Steps 

1.  Clone Etendo Base project in a temporal directory.

``` bash
cd /tmp
git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
```

2.  Copy the sources in /opt/EtendoERP folder.
```bash

mv EtendoERP/* /opt/EtendoERP/
cd /opt/EtendoERP
```
3. Modify the `gradle.properties` file with your GitHub Credentials. Create the credentials by following this [guide](https://docs.etendo.software/en/technical-documentation/etendo-environment/requirements-and-tools/developer-tools/use-of-repositories-in-etendo).

```groovy
githubUser=username
githubToken=*******

context.name=etendo

bbdd.sid=etendo
bbdd.port=5432
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
bbdd.user=tad
bbdd.password=tad

org.gradle.jvmargs=-Xmx2g -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encod>
```
3. Change the build.gradle file, deleting core version section and uncomment the core dependency in the dependencies section 
The following code is an example, you must modify your current file
``` groovy
plugins {
    id 'java'
    id 'war'
    id 'groovy'
    id 'maven-publish'
    id 'com.etendoerp.gradleplugin' version 'latest.release'
}

// Delete this section
// etendo {
//    coreVersion = "[<version>,<version>)"
// }

dependencies {
    /*
    To use Etendo in JAR format delete the Etendo section and uncomment the following line.
    Then when executing any gradle command the core will be dynamically downloaded as a dep>
    Set up the credentials in gradle.properties file
 		*/
    
    implementation('com.etendoerp.platform:etendo-core:<version>')
  
    //Add other dependencies bellow

}
```
4. Modify the `gradle.properties` file with your environment variables, if it is necessary:

```
githubUser= <user>
githubToken= <token>

context.name=etendo

bbdd.sid=etendo
bbdd.port=5432
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
bbdd.user=tad
bbdd.password=tad

```
5. Dependencies
```
./gradlew dependencies
```

5. Setup 
```
./gradlew setup
```
6. Installation
```
./gradlew install smartbuild
```
7.  Start the Tomcat, in case of Linux you can run:
```
sudo /etc/init.d/tomcat start
```
8. Open your browser in `https://<Public server IP>/<Context Name>`







