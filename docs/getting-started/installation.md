---
title: Installation

tags:
    - Etendo Installation
    - Installation Guide
    - Docker Management
    - PostgreSQL Setup
    - Etendo Environment
---
## Overview
This section explains how to install a new Etendo environment. It includes:

- Tutorial about the Etendo installation.
- The steps to install Etendo.

## Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/ixNnRuL10xo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Requirements 
This section outlines the [System Requirements](../getting-started/requirements.md).

!!!info
    The [Docker Management](../developer-guide/etendo-classic/bundles/platform/docker-management.md) module allows for the distribution of the infrastructure needed to configure Etendo Classic within Etendo modules, which include Docker containers for each service. Specifically, the Docker Management module includes the [PostgreSQL Database Service](../developer-guide/etendo-classic/bundles/platform/docker-management.md#postgres-database-service) and the [Dockerized Tomcat Service](../developer-guide/etendo-classic/bundles/platform/tomcat-dockerized-service.md) module. If these containers are used, the **services must be launched**, and then follow with the installation guide.

## PostgreSQL Configuration
Check this article to configure PostgreSQL correctly: [PostgreSQL Configuration](../developer-guide/etendo-classic/getting-started/installation/postgresql-configuration.md)

## Install Etendo 
=== ":material-language-java: JAR Format"

    ### Steps to Install Etendo in JAR Format

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

    3. Modify the `gradle.properties` file with your GitHub Credentials. Create the credentials by following this [guide](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
       
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

        org.gradle.jvmargs=-Dfile.encoding=UTF-8
        ```
    4. Change the `build.gradle` file, uncomment the core dependency in the dependencies section:
            
        ```
        implementation('com.etendoerp.platform:etendo-core:<version>')
        ```

        !!! info
            To know the available versions of Etendo Classic, please visit the [Release Notes](../whats-new/release-notes/etendo-classic/release-notes.md) page.

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
    9. Start the Tomcat, in case of Linux you can run:
        ```
        sudo /etc/init.d/tomcat start
        ```
        
        !!! note
            If you want to run Etendo locally, go to [Run Etendo Development Environment](../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md#run-etendo-development-environment).

    10. Open your browser in `https://<Public server IP>/<Context Name>`

=== ":octicons-file-zip-24: Source Format"

    ### Steps to Install Etendo in Sources Format

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
    3. Modify the `gradle.properties` file with your GitHub Credentials. Create the credentials by following this [guide](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
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

        org.gradle.jvmargs=-Dfile.encoding=UTF-8
        ```

    4. By default, the latest core version available will be expanded but if there is a need to change it, edit the `build.gradle` file changing the `coreVersion = "(<version>,<version>)"`.
        
        ```groovy
        etendo {
            coreVersion = "<version>"
        }
        ```

        !!! info
            To know the available versions of Etendo Classic, please visit the [Release Notes](../whats-new/release-notes/etendo-classic/release-notes.md) page.

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
    9. Make sure you have the following PostgreSQL configuration in your `postgresql.conf`, this file is located wherever you have postgresql installed
        ```
        lc_numeric = 'en_US.UTF-8'
        max_locks_per_transaction = 128
        ```        

        !!! note
            After modifying the file restart postgresql
           
    10.  Start the Tomcat, in case of Linux you can run:
        ```
        sudo /etc/init.d/tomcat start
        ```

        !!! note
            If you want to run Etendo locally, go to [Run Etendo Development Environment](../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md#run-etendo-development-environment).
                
    11. Open your browser in `https://<Public server IP>/<Context Name>`

=== ":octicons-issue-opened-24: ISO"

    ### Steps to Install the ISO with Internet Connection

    1. Download the ISO from the [release notes](../whats-new/release-notes/etendo-classic/iso.md) page.

    2. Burn the ISO image into a USB stick. It is recommended to use balenaEtcher on Linux and Rufus on Windows. Alternatively, you can begin with your preferred virtualizer.

    3. Start the system using the ISO image. You will be prompted:

        - **Network Connections**: Verify that you are on a network with an internet connection and that an IP address is correctly assigned to your server.
        
        - **Guide Storage Configuration**: Select the disk where you want to run the installation. If you only have one disk, proceed to the next step.
        
        - **Storage Configuration**: Same as the previous step.
        
        - **Profile Setup**: Enter your name, the server's name, and the user *etendo* with the password of your choice.

    4. Wait for the **operating system** installation and server upgrade to take place. When prompted, select **reboot now**.

    5. After the restart, the final server configuration will begin. Wait for it to finish, and the server will be ready.

    ### Steps to Install the ISO without Internet Connection

    If you do not have an internet connection during installation, follow these additional steps:

    1. Follow the same procedure outlined in the previous section, *Steps to Install the ISO with Internet Connection* up to the network configuration stage.

        - **Network Configuration**: In this section, if you do not have an internet connection, select **Continue without internet**.

    2. After the operating system installation is complete, restart the server as prompted.

    3. Log in to the server using the username and password you configured during installation.

    4. Configure the network settings as desired to establish an internet connection.

    5. Once connected to the internet, log in as the superuser: `sudo su`.

    6. Begin the installation process by running the command: `etendo-install`.

    7. After the installation is finished, the server will be ready for use.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/FqG4uM4PpbA?si=wKhH34wvQKY_7r4e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
