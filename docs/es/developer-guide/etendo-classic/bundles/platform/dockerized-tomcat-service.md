---
tags:
  - Docker
  - Tomcat
  - Servicio
  - Infraestructura
---

# Servicio Tomcat dockerizado

:octicons-package-16: Javapackage: `com.etendoerp.tomcat`

## Visión general

El módulo `com.etendoerp.tomcat` permite la dockerización de Tomcat dentro de Etendo Classic. Este módulo modifica las tareas de Gradle para desplegar automáticamente el archivo `WAR` en el contenedor al ejecutar la tarea `smartbuild`.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Platform Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Platform Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

## Variables de configuración

Para habilitar y configurar el servicio de Tomcat, están disponibles las siguientes variables de configuración:

- **Habilitar el servicio**

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    ```
    Esta variable habilita el servicio de Tomcat.

- **Configurar el puerto de Tomcat** (Opcional)
    ```groovy title="gradle.properties"
    tomcat.port=<port>
    ```
    Esta variable establece el puerto para el servicio de Tomcat. El puerto por defecto es `8080`

- **Configurar el puerto de depuración** (Opcional)

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat_debug=<debug_port>
    ```
    Esta variable establece el puerto de depuración para el servicio de Tomcat. El puerto de depuración por defecto es `8009`

    !!! info
        Para depurar en IntelliJ, cree una nueva configuración de tipo **Depuración remota de JVM** y establezca el puerto en el que se escuchará.

        ![Debug-Mode.png](../../../../assets/developer-guide/etendo-classic/bundles/platform/tomcat-dockeridez-service/debug-mode.png)

Ejecute el siguiente comando para aplicar los cambios de configuración:

```groovy title="Terminal"
./gradlew setup
```

## Compilar el entorno

- La primera vez que se utiliza Tomcat dentro de un entorno Docker, debe compilarse la configuración ejecutando:
    
    ``` bash title="Terminal"
    ./gradlew resources.up
    ```

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild
    ```

    Este comando actualizará la base de datos, recompilará las clases Java y desplegará el `WAR` en el *servicio Tomcat dockerizado*. 

    !!! info
        Este módulo modifica las **tareas de Gradle**. Al ejecutar el comando `update.database`, el servicio de Tomcat se detendrá automáticamente. A continuación, la tarea `smartbuild` garantizará que el archivo `WAR` se despliegue correctamente en el contenedor. Tras la ejecución de smartbuild, el servicio se reiniciará automáticamente, habilitando una compilación automatizada desde la línea de comandos.
         


- Consulte la página [Gestión de Docker](./docker-management.md) para más información sobre la gestión de contenedores.


## Configuración adicional para usar Tomcat (dockerizado) con una base de datos del host en entornos Linux

1. Escuchar en la red de Docker

    Cree el archivo `etendo.conf` en la ubicación `/etc/postgresql/<your_pg_version>/main/conf.d/etendo.conf` con el siguiente contenido:

    ``` title="etendo.conf"
    listen_addresses = 'localhost,172.17.0.1'
    ```

    !!! note
        La dirección IP `172.17.0.1` es la interfaz que conecta el host con el servicio de Docker. Esta es la dirección por defecto utilizada para esta conexión.

2. Permitir acceso desde la subred de Docker

    Añada la siguiente línea al archivo `/etc/postgresql/<your_pg_version>/main/pg_hba.conf`:
    
    ``` title="pg_hba.conf"
    host all all 172.0.0.0/8 scram-sha-256
    ```
    !!! note
        La subred `172.0.0.0/8` se utiliza para habilitar el acceso desde Docker Tomcat al host. Por defecto, Docker asigna una subred dentro del rango de `172.1.0.0/8` a `172.254.0.0/8`.
3. Reiniciar el servicio de PostgreSQL

    Por último, reinicie el servicio de PostgreSQL ejecutando el siguiente comando en el terminal:

    ``` bash title="Terminal"
    sudo systemctl restart postgresql
    ```



---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.