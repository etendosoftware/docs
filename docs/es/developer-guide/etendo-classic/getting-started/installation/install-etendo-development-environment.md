---
title: Instalar el entorno de desarrollo de Etendo
tags:
    - Primeros pasos
    - Modo de desarrollo
    - Desarrollar
    - Instalar Etendo
---
# Instalar el entorno de desarrollo de Etendo

## Visión general

Esta sección explica cómo instalar y ejecutar un nuevo entorno local de Etendo.


## Instalar Etendo en un entorno local

Para instalar Etendo en un entorno de desarrollo, siga los mismos pasos que se describen en la [Guía de instalación de Etendo](../../../../getting-started/installation.md); la única diferencia es que abrimos el proyecto con IntelliJ y ejecutamos Tomcat localmente.


## Ejecutar el entorno de desarrollo de Etendo

=== "IntelliJ IDEA Community Edition"

    1. Descargue e instale [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/download){target="_blank"}

    2. Abra el directorio fuente de Etendo con IntelliJ:
        ![open-project.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/open-project.png)

    2. Instale el plugin Smart Tomcat:
        Para instalarlo, vaya a `Settings` >> `Plugins` y busque `“Smart Tomcat”`
        ![install-smart-tomcat.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/install-smart-tomcat.png)

    3.  Descargue [Apache Tomcat](https://tomcat.apache.org/download-90.cgi){target="_blank"} y descomprímalo en el directorio del proyecto

    4. Configurar Tomcat
        
        - Vaya a Current File >> Edit configurations.
        ![edit-configurations.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/edit-configurations.png){ align=right }
        - Añada una nueva configuración de Smart Tomcat, haciendo clic en "+"
        - Nombre: Tomcat
        - Tomcat Server: seleccione el directorio de Apache Tomcat descomprimido
        - Deployment directory: seleccione el directorio `WebContent` del proyecto
        - Context path: defina la misma ruta de contexto definida en el archivo gradle.properties (por defecto "/etendo" )
        - Before launch: elimine todas las tareas por defecto

        ![add-new-configuration.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/add-new-configuration.png) 

    5. Inicie Tomcat 

        ![edit-configurations.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/start-tomcat.png)

        !!! success
            Ahora tiene un nuevo entorno de Etendo ejecutándose en [http://localhost:8080/etendo](http://localhost:8080/etendo)

        !!! tip "Credenciales por defecto"
            Usuario: admin  
            Contraseña: admin



=== "IntelliJ IDEA Ultimate"

    1. Descargue e instale [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download){target="_blank"}

    2. Abra el directorio fuente de Etendo con IntelliJ:

        ![open-project-ultimate.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/open project-ultimate.png)

    3. Configurar Tomcat
        
        - Vaya a Current File >> Edit configurations.
            
            ![edit-configurations.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/edit-configurations.png)
        
        - Seleccione la configuración de Tomcat que aparece primero en la lista y compruebe la configuración del servidor Tomcat en su máquina.
            
            ![add-new-configuration-ultimate.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/add-new-configuration-ultimate.png)
        - En la sección Deployment, añada fuentes externas 

            ![add-new-configuration-ultimate.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/add-external-source.png)
        - Seleccione la carpeta `${env.CATALINA_HOME}/webapps/etendo` y, a continuación, haga clic en el botón OK.

            ![config-deployment-folder.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/config-deployment-folder.png)

    4. Inicie Tomcat

        ![edit-configurations.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-etendo-development-environment/start-tomcat.png)

        !!! success
            Ahora tiene un nuevo entorno de Etendo ejecutándose en [http://localhost:8080/etendo](http://localhost:8080/etendo)

        !!! tip "Credenciales por defecto"
            Usuario: admin  
            Contraseña: admin



## Habilitar los logs de Etendo (opcional)

1.  Abra el archivo `config/log4j2-web.xml`, busque la línea `<!-- <AppenderRef ref="Console"/> -->` y descoméntela:

    ``` XML title="config/log4j2-web.xml"
    ...
    <Loggers>
        <Root level="info">
        <AppenderRef ref="RollingFile"/>
        <!-- Add this appender to show log messages in console i.e Eclipse: -->
        <AppenderRef ref="Console"/>  << UNCOMMENT THIS LINE
        </Root>
    ...
    ```
2. Ejecute la tarea smartbuild

    ``` bash title="Terminal"
        ./gradlew smartbuild --info 
    ```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.