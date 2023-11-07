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
In this section, you can read the [System Requirements](/getting-started/requirements).

### Install Etendo 
=== ":material-language-java: JAR Format"

    ## Steps to Install Etendo in JAR Format

    1.  Clone Etendo Base project in a temporal directory.

        ``` bash
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```
    2.  Copy the sources in `/opt/EtendoERP` folder.

        ```bash
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Modify the `gradle.properties` file with your GitHub Credentials. Create the credentials by following this [guide](/developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo).
       
        ```groovy
        nexusUser=
        nexusPassword=
        githubUser= username
        githubToken=*******

        context.name=etendo

        bbdd.sid=etendo
        bbdd.port=5432
        bbdd.systemUser=postgres
        bbdd.systemPassword=syspass
        bbdd.user=tad
        bbdd.password=tad

        org.gradle.jvmargs=-Xmx2g -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
        ```
    4. Change the build.gradle file, deleting core version section and uncomment the core dependency in the dependencies section 
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

    5. Modify the `gradle.properties` file with your environment variables, if it is necessary:
        
        ```groovy
        nexusUser=
        nexusPassword=
        githubUser= username
        githubToken=*******

        context.name=etendo

        bbdd.sid=etendo
        bbdd.port=5432
        bbdd.systemUser=postgres
        bbdd.systemPassword=syspass
        bbdd.user=tad
        bbdd.password=tad
        ```
    6. Dependencies
        ``` bash
        ./gradlew dependencies
        ```
    7. Setup 
        ```
        ./gradlew setup
        ```
    8. Installation 
        ```
        ./gradlew install smartbuild
        ```
    9.  Start the Tomcat, in case of Linux you can run:
        ```
        sudo /etc/init.d/tomcat start
        ```
        
        !!! note
                If you want to run Etendo locally, go to [Run Etendo Development Environment](/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment/#run-etendo-development-environment).

    10. Open your browser in `https://<Public server IP>/<Context Name>`

=== ":octicons-file-zip-24: Source Format"

    ##Steps to Install Etendo in Sources Format

    1.  Clone Etendo Base project in a temporal directory.

        ``` bash
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```

    2.  Copy the sources in `/opt/EtendoERP` folder.
        ```bash
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```
    3. Modify the `gradle.properties` file with your GitHub Credentials. Create the credentials by following this [guide](/developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo).
        ```groovy
        nexusUser=
        nexusPassword=
        githubUser= username
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

    4. By default, the latest core version available will be expanded but if there is a need to change it, edit the `build.gradle` file changing the `coreVersion = "[<version>,<version>)"`. The following code is an example, you must modify your current file
        
        ``` groovy
        plugins {
            id 'java'
            id 'war'
            id 'groovy'
            id 'maven-publish'
            id 'com.etendoerp.gradleplugin' version 'latest.release'
        }
        
        etendo {
            coreVersion = "<version>"
        }

        dependencies {
            /*
            To use Etendo in JAR format delete the Etendo section and uncomment the following line.
            Then when executing any gradle command the core will be dynamically downloaded as a dep>
            Set up the credentials in gradle.properties file
           
            implementation('com.etendoerp.platform:etendo-core:<version>')
             */
        
            //Add other dependencies bellow

        }
        ```    
    5.  Expand Etendo Base

        ```
        ./gradlew expand 
        ```
    6. Modify the `gradle.properties` file with your environment variables, if it is necessary:

        ```groovy
        context.name=etendo

        bbdd.sid=etendo
        bbdd.port=5432
        bbdd.systemUser=postgres
        bbdd.systemPassword=syspass
        bbdd.user=tad
        bbdd.password=tad
        ```

    7. Setup: to apply or create the initial configurations
        ```
        ./gradlew setup
        ```
    8. Installation: Create the database, compile the sources and deploy to Apache Tomcat
        ```
        ./gradlew install smartbuild
        ```
    9.  Start the Tomcat, in case of Linux you can run:
        ```
        sudo /etc/init.d/tomcat start
        ```

        !!! note
                If you want to run Etendo locally, go to [Run Etendo Development Environment](/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment/#run-etendo-development-environment).
                
    10. Open your browser in `https://<Public server IP>/<Context Name>`










