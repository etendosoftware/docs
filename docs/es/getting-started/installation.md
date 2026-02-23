---
title: Instalar Etendo

tags:
    - Instalación de Etendo
    - Guía de instalación
    - Gestión de Docker
    - Configuración de PostgreSQL
    - Entorno de Etendo
    - Instalar
    - Instalación de Etendo
---

# Instalar Etendo

## Visión general
Esta sección explica cómo instalar un nuevo entorno de Etendo. Incluye:

- Tutorial sobre la instalación de Etendo.
- Los pasos para instalar Etendo.

## Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/ixNnRuL10xo" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Requisitos 
Esta sección describe los [Requisitos del sistema](../getting-started/requirements.md).

## Configuración de PostgreSQL
Consulta este artículo para configurar PostgreSQL correctamente: [Configuración de PostgreSQL](../developer-guide/etendo-classic/getting-started/installation/postgresql-configuration.md)

## Sistema de configuración interactivo

Etendo ahora incluye un **Sistema de configuración interactivo** que te guía a través del proceso de configuración con un asistente intuitivo. En lugar de editar manualmente `gradle.properties`, puedes usar el modo interactivo para configurar tu proyecto paso a paso.

**Para una guía completa de instalación interactiva paso a paso, consulta: [Guía de instalación interactiva](interactive-installation.md)**

## Cómo instalar Etendo

La instalación de Etendo es muy sencilla...

## Instalar Etendo 
=== ":material-language-java: Formato JAR"

    ### Pasos para instalar Etendo en formato JAR

    1.  Clona el proyecto Etendo Base en un directorio temporal.

        ``` bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```
    2.  Copia los fuentes en la carpeta `/opt/EtendoERP`.

        ``` bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Modifica el archivo `gradle.properties` con tus credenciales de GitHub. Crea las credenciales siguiendo esta [guía](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
       
        ```groovy title="gradle.properties"
        nexusUser=
        nexusPassword=
        githubUser=<username>
        githubToken=<*******>
        ```
    4. Cambia el archivo `build.gradle`, descomenta la dependencia del core en la sección de dependencias:
            
        ```groovy title="build.gradle"
        implementation('com.etendoerp.platform:etendo-core:<version>')
        ```

        !!! info
            Para conocer las versiones disponibles de Etendo Classic, visita la página de [Notas de la versión](../whats-new/release-notes/etendo-classic/release-notes.md).

    5. Modifica el archivo `gradle.properties` con las variables de tu entorno, si es necesario:
        
        ```groovy title="gradle.properties"

        context.name=etendo

        bbdd.sid=etendo
        bbdd.port=5432
        bbdd.systemUser=postgres
        bbdd.systemPassword=syspass
        bbdd.user=tad
        bbdd.password=tad

        org.gradle.jvmargs=-Dfile.encoding=UTF-8
        ```
    6. Dependencias
        
        ``` bash title="Terminal"
        ./gradlew dependencies
        ```
    7. Setup 
        ``` bash title="Terminal"
        ./gradlew setup
        ```
    8. Instalación 
        ``` bash title="Terminal"
        ./gradlew install smartbuild
        ```
    9. Inicia Tomcat; en el caso de Linux puedes ejecutar:
        ``` bash title="Terminal"
        sudo /etc/init.d/tomcat start
        ```
        
        !!! note
            Si quieres ejecutar Etendo en local, ve a [Ejecutar el entorno de desarrollo de Etendo](../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md#run-etendo-development-environment).

    10. Abre tu navegador en `https://<Public server IP>/<Context Name>`

=== ":octicons-file-zip-24: Formato fuentes"

    ### Pasos para instalar Etendo en formato fuentes

    1.  Clona el proyecto Etendo Base en un directorio temporal.

        ``` bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```

    2.  Copia los fuentes en la carpeta `/opt/EtendoERP`.
        
        ``` bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```
    3. Modifica el archivo `gradle.properties` con tus credenciales de GitHub. Crea las credenciales siguiendo esta [guía](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
        
        ```groovy title="gradle.properties"
        nexusUser=
        nexusPassword=
        githubUser=<username>
        githubToken=<*******>
        ```

    4. De forma predeterminada, se expandirá la última versión del core disponible, pero si es necesario cambiarla, edita el archivo `build.gradle` cambiando `coreVersion = "(<version>,<version>)"`.
        
        ```groovy title="build.gradle"
        etendo {
            coreVersion = "<version>"
        }
        ```

        !!! info
            Para conocer las versiones disponibles de Etendo Classic, visita la página de [Notas de la versión](../whats-new/release-notes/etendo-classic/release-notes.md).

    5.  Expandir Etendo Base

        ``` bash title="Terminal"
        ./gradlew expand 
        ```
    6. Modifica el archivo `gradle.properties` con las variables de tu entorno, si es necesario:

        ```groovy title="gradle.properties"
        
        context.name=etendo

        bbdd.sid=etendo
        bbdd.port=5432
        bbdd.systemUser=postgres
        bbdd.systemPassword=syspass
        bbdd.user=tad
        bbdd.password=tad

        org.gradle.jvmargs=-Dfile.encoding=UTF-8
        ```

    7. Setup: para aplicar o crear las configuraciones iniciales
        
        ``` bash title="Terminal"
        ./gradlew setup
        ```

    8. Instalación: crear la base de datos, compilar los fuentes y desplegar en Apache Tomcat
        
        ``` bash title="Terminal"
        ./gradlew install smartbuild
        ```

    9. Asegúrate de tener la siguiente configuración de PostgreSQL en tu `postgresql.conf`; este archivo se encuentra donde tengas instalado PostgreSQL
        
        ``` bash title="Terminal"
        lc_numeric = 'en_US.UTF-8'
        max_locks_per_transaction = 128
        ```        

        !!! note
            Después de modificar el archivo, reinicia el servicio de PostgreSQL
           
    10.  Inicia Tomcat; en el caso de Linux puedes ejecutar:
        
        ``` bash title="Terminal"
        sudo /etc/init.d/tomcat start
        ```

        !!! note
            Si quieres ejecutar Etendo en local, ve a [Ejecutar el entorno de desarrollo de Etendo](../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md#run-etendo-development-environment).
                
    11. Abre tu navegador en `https://<Public server IP>/<Context Name>`

=== ":octicons-issue-opened-24: Etendo ISO"

    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/FqG4uM4PpbA?si=wKhH34wvQKY_7r4e" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    
    ### Pasos para instalar la ISO de Etendo

    1. Descarga la ISO de Etendo desde la página [Etendo ISO - Notas de la versión](../whats-new/release-notes/etendo-classic/iso.md).

    2. Graba la imagen ISO de Etendo en una memoria USB. Se recomienda usar [balenaEtcher](https://etcher.balena.io/#download-etcher){target="_blank"} en Linux o MacOS y [Rufus](https://rufus.ie/en/){target="_blank"} en Windows.

        !!! tip
            Si estás instalando la ISO de Etendo en una máquina virtual, se recomienda usar [Qemu](https://www.qemu.org/download/){target="_blank"} junto con una interfaz gráfica como [Virt-Manager (Linux)](https://virt-manager.org/download.html){target="_blank"} o [UTM (MacOS)](https://mac.getutm.app/){target="_blank"} para gestionar fácilmente tus entornos virtuales. 

    3. Inicia el sistema usando la imagen ISO de Etendo. Se te solicitará:

        - **Conexiones de red**: verifica que estás en una red con conexión a internet y que se ha asignado correctamente una dirección IP a tu servidor.
        
        - **Guía de configuración de almacenamiento**: selecciona el disco donde quieres ejecutar la instalación. Si solo tienes un disco, continúa con el siguiente paso.
        
        - **Configuración de almacenamiento**: igual que el paso anterior.
        
        - **Configuración del perfil**: introduce tu nombre, el nombre del servidor y el usuario *etendo* con la contraseña que elijas.

    4. Espera a que se realice la instalación del **Sistema operativo** y la actualización del servidor. Cuando se te solicite, selecciona **reboot now**.

    5. Tras el reinicio, comenzará la configuración final del servidor. Espera a que finalice y el servidor estará listo.

    **Pasos para instalar la ISO de Etendo sin conexión a internet**

    Si no tienes conexión a internet durante la instalación, sigue estos pasos adicionales:

    1. Sigue el mismo procedimiento descrito en la sección anterior, *Pasos para instalar la ISO de Etendo con conexión a internet*, hasta la etapa de configuración de red.

        - **Configuración de red**: en esta sección, si no tienes conexión a internet, selecciona **Continue without internet**.

    2. Una vez completada la instalación del sistema operativo, reinicia el servidor cuando se te solicite.

    3. Inicia sesión en el servidor usando el nombre de usuario y la contraseña que configuraste durante la instalación.

    4. Configura los ajustes de red como desees para establecer una conexión a internet.

    5. Una vez conectado a internet, inicia sesión como superusuario: `sudo su`.

    6. Inicia el proceso de instalación ejecutando el comando: `etendo-install`.

    7. Cuando finalice la instalación, el servidor estará listo para su uso.


=== ":material-docker:  Base de datos y Tomcat dockerizados"

    ### Pasos para instalar Etendo con base de datos Postgres y Tomcat dockerizados

    El módulo [Gestión de Docker](../developer-guide/etendo-classic/bundles/platform/docker-management.md) permite distribuir la infraestructura necesaria para configurar Etendo Classic dentro de los módulos de Etendo, que incluyen contenedores Docker para cada servicio. En concreto, el módulo Docker Management incluye el [Servicio de base de datos PostgreSQL](../developer-guide/etendo-classic/bundles/platform/docker-management.md#postgres-database-service) y el módulo [Servicio de Tomcat dockerizado](../developer-guide/etendo-classic/bundles/platform/tomcat-dockerized-service.md) que, como su nombre indica, proporciona el servicio de Tomcat.
    Estos módulos forman parte del bundle [Extensiones de plataforma](../user-guide/etendo-classic/optional-features/bundles/platform-extensions/overview.md), que se tratará en esta guía paso a paso sobre cómo instalarlos.
    
    !!! info
        En esta guía asumiremos la instalación de Etendo Classic en formato fuentes; en caso de que quieras instalarlo en formato JAR, debes consultar los cambios en la pestaña correspondiente.

    1.  Clona el proyecto Etendo Base en un directorio temporal.

        ```bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```
    2.  Copia los fuentes en la carpeta `/opt/EtendoERP`.

        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Modifica el archivo `gradle.properties` con tus credenciales de GitHub. Crea las credenciales siguiendo esta [guía](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
       
        ```groovy title="gradle.properties"
        nexusUser=
        nexusPassword=
        githubUser=<username>
        githubToken=<*******>
        ```
    4. De forma predeterminada, se expandirá la última versión del core disponible, pero si es necesario cambiarla, edita el archivo `build.gradle` cambiando `coreVersion = "<version>"`.
        
        ```groovy title="build.gradle"
        etendo {
            coreVersion = "<version>"
        }
        ```

        !!! info
            Para conocer las versiones disponibles, visita la página de Notas de la versión de Etendo Classic [Notas de la versión](../whats-new/release-notes/etendo-classic/release-notes.md).

    5.  Expandir Etendo Classic

        ``` bash title="Terminal"
        ./gradlew expand 
        ```

    6.  Añade la dependencia del bundle Extensiones de plataforma, para incluir las funcionalidades de plataforma dockerizadas

        ```groovy title="build.gradle"
        dependencies {
            //Add other dependencies bellow
            implementation ('com.etendoerp:platform.extensions:2.6.0') // version 2.6.0 or later
        }
        ```
    7. Modifica el archivo `gradle.properties` con las variables de tu entorno

        ```groovy title="gradle.properties"
        
        context.name=etendo

        bbdd.sid=etendo
        bbdd.port=5434
        bbdd.systemUser=postgres
        bbdd.systemPassword=syspass
        bbdd.user=tad
        bbdd.password=tad

        org.gradle.jvmargs=-Dfile.encoding=UTF-8

        docker_com.etendoerp.tomcat=true
        docker_com.etendoerp.docker_db=true
        ```
        
        !!! info
            El servicio de base de datos dockerizado se ejecutará en el puerto definido en la variable `bbdd.port`; sugerimos usar el puerto `5434` para evitar conflictos si tienes una instancia local de Postgres usando el puerto por defecto.

            Por defecto, el servicio de Tomcat se levantará en el puerto `8080`; en caso de que ese puerto esté ocupado, puedes usar la variable `tomcat.port=<port>`.


    8. Lanzar los servicios dockerizados de Tomcat y base de datos

        ``` bash title="Terminal"
        ./gradlew resources.up
        ```
        <figure markdown="span">
        ![tomcat-database-dockerized](../assets/getting-started/installation/tomcat-database-dockerized.png)
        <figcaption> Base de datos Postgres y servicio Tomcat ejecutándose dockerizados; si es necesario, puedes acceder al log de cada servicio. </figcaption>
        </figure>
        

    9. Setup: para aplicar o crear las configuraciones iniciales
    
        ``` bash title="Terminal"
        ./gradlew setup
        ```

    10. Instalación: crear la base de datos, compilar los fuentes y desplegar en Apache Tomcat
        
        ``` bash title="Terminal"
        ./gradlew install smartbuild
        ```
           
    11. Después de que finalice la tarea smartbuild, el servicio Tomacat se reiniciará automáticamente; abre tu navegador en: 
    
        `https://<Public server IP>/<context.name>` o, en caso de que lo ejecutes en un entorno local, [`http://localhost:8080/etendo`](http://localhost:8080/etendo){target="_blank"}


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.