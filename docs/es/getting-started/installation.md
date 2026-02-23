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
Consulte este artículo para configurar PostgreSQL correctamente: [Configuración de PostgreSQL](../developer-guide/etendo-classic/getting-started/installation/postgresql-configuration.md)

## Sistema de configuración interactivo

Etendo ahora incluye un **Sistema de configuración interactivo** que le guía a través del proceso de configuración con un asistente intuitivo. En lugar de editar manualmente `gradle.properties`, puede utilizar el modo interactivo para configurar su proyecto paso a paso.

**Para una guía completa de instalación interactiva paso a paso, consulte: [Guía de instalación interactiva](interactive-installation.md)**

## Cómo instalar Etendo

La instalación de Etendo es muy sencilla...

## Instalar Etendo 
=== ":material-language-java: Formato JAR"

    ### Pasos para instalar Etendo en formato JAR

    1.  Clone el proyecto Etendo Base en un directorio temporal.

        ``` bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```
    2.  Copie las fuentes en la carpeta `/opt/EtendoERP`.

        ``` bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Modifique el archivo `gradle.properties` con sus credenciales de GitHub. Cree las credenciales siguiendo esta [guía](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
       
        ```groovy title="gradle.properties"
        nexusUser=
        nexusPassword=
        githubUser=<username>
        githubToken=<*******>
        ```
    4. Cambie el archivo `build.gradle`, descomente la dependencia del core en la sección de dependencias:
            
        ```groovy title="build.gradle"
        implementation('com.etendoerp.platform:etendo-core:<version>')
        ```

        !!! info
            Para conocer las versiones disponibles de Etendo Classic, visite la página de [Notas de la versión](../whats-new/release-notes/etendo-classic/release-notes.md).

    5. Modifique el archivo `gradle.properties` con las variables de su entorno, si es necesario:
        
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
    7. Configuración 
        ``` bash title="Terminal"
        ./gradlew setup
        ```
    8. Instalación 
        ``` bash title="Terminal"
        ./gradlew install smartbuild
        ```
    9. Inicie Tomcat; en el caso de Linux puede ejecutar:
        ``` bash title="Terminal"
        sudo /etc/init.d/tomcat start
        ```
        
        !!! note
            Si desea ejecutar Etendo en local, vaya a [Ejecutar el entorno de desarrollo de Etendo](../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md#run-etendo-development-environment).

    10. Abra su navegador en `https://<Public server IP>/<Context Name>`

=== ":octicons-file-zip-24: Formato de fuentes"

    ### Pasos para instalar Etendo en formato de fuentes

    1.  Clone el proyecto Etendo Base en un directorio temporal.

        ``` bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```

    2.  Copie las fuentes en la carpeta `/opt/EtendoERP`.
        
        ``` bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```
    3. Modifique el archivo `gradle.properties` con sus credenciales de GitHub. Cree las credenciales siguiendo esta [guía](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
        
        ```groovy title="gradle.properties"
        nexusUser=
        nexusPassword=
        githubUser=<username>
        githubToken=<*******>
        ```

    4. De forma predeterminada, se expandirá la última versión del core disponible, pero si es necesario cambiarla, edite el archivo `build.gradle` cambiando `coreVersion = "(<version>,<version>)"`.
        
        ```groovy title="build.gradle"
        etendo {
            coreVersion = "<version>"
        }
        ```

        !!! info
            Para conocer las versiones disponibles de Etendo Classic, visite la página de [Notas de la versión](../whats-new/release-notes/etendo-classic/release-notes.md).

    5.  Expandir Etendo Base

        ``` bash title="Terminal"
        ./gradlew expand 
        ```
    6. Modifique el archivo `gradle.properties` con las variables de su entorno, si es necesario:

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

    7. Configuración: para aplicar o crear las configuraciones iniciales
        
        ``` bash title="Terminal"
        ./gradlew setup
        ```

    8. Instalación: crear la base de datos, compilar las fuentes y desplegar en Apache Tomcat
        
        ``` bash title="Terminal"
        ./gradlew install smartbuild
        ```

    9. Asegúrese de tener la siguiente configuración de PostgreSQL en su `postgresql.conf`; este archivo se encuentra donde tenga instalado postgresql
        
        ``` bash title="Terminal"
        lc_numeric = 'en_US.UTF-8'
        max_locks_per_transaction = 128
        ```        

        !!! note
            Después de modificar el archivo, reinicie el servicio de postgresql
           
    10.  Inicie Tomcat; en el caso de Linux puede ejecutar:
        
        ``` bash title="Terminal"
        sudo /etc/init.d/tomcat start
        ```

        !!! note
            Si desea ejecutar Etendo en local, vaya a [Ejecutar el entorno de desarrollo de Etendo](../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md#run-etendo-development-environment).
                
    11. Abra su navegador en `https://<Public server IP>/<Context Name>`

=== ":octicons-issue-opened-24: Etendo ISO"

    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/FqG4uM4PpbA?si=wKhH34wvQKY_7r4e" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    
    ### Pasos para instalar la ISO de Etendo

    1. Descargue la ISO de Etendo desde la página de [Etendo ISO - Notas de la versión](../whats-new/release-notes/etendo-classic/iso.md).

    2. Grabe la imagen ISO de Etendo en una memoria USB. Se recomienda utilizar [balenaEtcher](https://etcher.balena.io/#download-etcher){target="_blank"} en Linux o MacOS y [Rufus](https://rufus.ie/en/){target="_blank"} en Windows.

        !!! tip
            Si está instalando la ISO de Etendo en una máquina virtual, se recomienda utilizar [Qemu](https://www.qemu.org/download/){target="_blank"} junto con una interfaz gráfica como [Virt-Manager (Linux)](https://virt-manager.org/download.html){target="_blank"} o [UTM (MacOS)](https://mac.getutm.app/){target="_blank"} para gestionar fácilmente sus entornos virtuales. 

    3. Inicie el sistema utilizando la imagen ISO de Etendo. Se le solicitará:

        - **Conexiones de red**: Verifique que está en una red con conexión a internet y que se asigna correctamente una dirección IP a su servidor.
        
        - **Configuración guiada del almacenamiento**: Seleccione el disco donde desea ejecutar la instalación. Si solo tiene un disco, continúe con el siguiente paso.
        
        - **Configuración del almacenamiento**: Igual que en el paso anterior.
        
        - **Configuración del perfil**: Introduzca su nombre, el nombre del servidor y el usuario *etendo* con la contraseña que elija.

    4. Espere a que se realice la instalación del **Sistema operativo** y la actualización del servidor. Cuando se le solicite, seleccione **reiniciar ahora**.

    5. Tras el reinicio, comenzará la configuración final del servidor. Espere a que finalice y el servidor estará listo.

    **Pasos para instalar la ISO de Etendo sin conexión a internet**

    Si no dispone de conexión a internet durante la instalación, siga estos pasos adicionales:

    1. Siga el mismo procedimiento descrito en la sección anterior, *Pasos para instalar la ISO de Etendo con conexión a internet* hasta la etapa de configuración de red.

        - **Configuración de red**: En esta sección, si no dispone de conexión a internet, seleccione **Continuar sin internet**.

    2. Una vez completada la instalación del sistema operativo, reinicie el servidor cuando se le solicite.

    3. Inicie sesión en el servidor utilizando el nombre de usuario y la contraseña que configuró durante la instalación.

    4. Configure los ajustes de red según desee para establecer una conexión a internet.

    5. Una vez conectado a internet, inicie sesión como superusuario: `sudo su`.

    6. Inicie el proceso de instalación ejecutando el comando: `etendo-install`.

    7. Una vez finalizada la instalación, el servidor estará listo para su uso.


=== ":material-docker:  Base de datos y Tomcat dockerizados"

    ### Pasos para instalar Etendo con base de datos Postgres y Tomcat dockerizados

    El módulo [Gestión de Docker](../developer-guide/etendo-classic/bundles/platform/docker-management.md) permite distribuir la infraestructura necesaria para configurar Etendo Classic dentro de módulos de Etendo, que incluyen contenedores Docker para cada servicio. En concreto, el módulo Gestión de Docker incluye el módulo [Servicio de base de datos PostgreSQL](../developer-guide/etendo-classic/bundles/platform/docker-management.md#postgres-database-service) y el módulo [Servicio de Tomcat dockerizado](../developer-guide/etendo-classic/bundles/platform/tomcat-dockerized-service.md) que, como su nombre indica, proporciona el servicio de Tomcat.
    Estos módulos forman parte del bundle [Platform Extensions](../user-guide/etendo-classic/optional-features/bundles/platform-extensions/overview.md), que se tratará en esta guía paso a paso sobre cómo instalarlos.
    
    !!! info
        En esta guía se asumirá la instalación de Etendo Classic en formato de fuentes; en caso de que desee instalarlo en formato JAR, debe consultar los cambios en la pestaña correspondiente.

    1.  Clone el proyecto Etendo Base en un directorio temporal.

        ```bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP 
        ```
    2.  Copie las fuentes en la carpeta `/opt/EtendoERP`.

        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Modifique el archivo `gradle.properties` con sus credenciales de GitHub. Cree las credenciales siguiendo esta [guía](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
       
        ```groovy title="gradle.properties"
        nexusUser=
        nexusPassword=
        githubUser=<username>
        githubToken=<*******>
        ```
    4. De forma predeterminada, se expandirá la última versión del core disponible, pero si es necesario cambiarla, edite el archivo `build.gradle` cambiando `coreVersion = "<version>"`.
        
        ```groovy title="build.gradle"
        etendo {
            coreVersion = "<version>"
        }
        ```

        !!! info
            Para conocer las versiones disponibles, visite la página de Notas de la versión de Etendo Classic [Notas de la versión](../whats-new/release-notes/etendo-classic/release-notes.md).

    5.  Expandir Etendo Classic

        ``` bash title="Terminal"
        ./gradlew expand 
        ```

    6.  Añada la dependencia del bundle Platform Extensions para incluir las funcionalidades de plataforma dockerizadas

        ```groovy title="build.gradle"
        dependencies {
            //Add other dependencies bellow
            implementation ('com.etendoerp:platform.extensions:2.6.0') // version 2.6.0 or later
        }
        ```
    7. Modifique el archivo `gradle.properties` con las variables de su entorno

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
            El servicio de base de datos dockerizado se ejecutará en el puerto definido en la variable `bbdd.port`; se sugiere utilizar el puerto `5434` para evitar conflictos si tiene una instancia local de Postgres usando el puerto predeterminado.

            De forma predeterminada, el servicio de Tomcat estará disponible en el puerto `8080`; en caso de que ese puerto esté ocupado, puede utilizar la variable `tomcat.port=<port>`.


    8. Iniciar los servicios dockerizados de Tomcat y base de datos

        ``` bash title="Terminal"
        ./gradlew resources.up
        ```
        <figure markdown="span">
        ![tomcat-database-dockerized](../assets/getting-started/installation/tomcat-database-dockerized.png)
        <figcaption> Base de datos Postgres y servicio Tomcat ejecutándose dockerizados; si es necesario, puede acceder al log de cada servicio. </figcaption>
        </figure>
        

    9. Configuración: para aplicar o crear las configuraciones iniciales
    
        ``` bash title="Terminal"
        ./gradlew setup
        ```

    10. Instalación: crear la base de datos, compilar las fuentes y desplegar en Apache Tomcat
        
        ``` bash title="Terminal"
        ./gradlew install smartbuild
        ```
           
    11. Después de que finalice la tarea smartbuild, el servicio Tomcat se reiniciará automáticamente; abra su navegador en: 
    
        `https://<Public server IP>/<context.name>` o, en caso de que lo ejecute en un entorno local, [`http://localhost:8080/etendo`](http://localhost:8080/etendo){target="_blank"}


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

---