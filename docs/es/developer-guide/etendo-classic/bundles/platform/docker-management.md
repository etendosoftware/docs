---
tags:
  - Docker
  - Gestión
  - Infraestructura
---

# Gestión de Docker

:octicons-package-16: Paquete Java: `com.etendoerp.docker`

## Visión general

[Docker](https://docs.docker.com/){target=_isblank} es una plataforma que permite a los desarrolladores automatizar el despliegue, el escalado y la gestión de aplicaciones. Utiliza tecnología de contenedorización, que empaqueta una aplicación y sus dependencias en una unidad estandarizada llamada **contenedor**. Los contenedores pueden ejecutarse de forma consistente en distintos entornos de computación, lo que los hace altamente portables y eficientes.

El módulo `com.etendoerp.docker` permite el uso de contenedores Dockerizados en Etendo Classic. Esto permite la distribución y encapsulación de nuevas funcionalidades utilizando la infraestructura de módulos existente de Etendo. También proporciona la capacidad de Dockerizar la base de datos, Tomcat o cualquier dependencia de infraestructura actual o futura de Etendo. Además, el módulo incluye tareas de Gradle para gestionar contenedores.

!!! Info 
    Este módulo incluye la infraestructura para la gestión de contenedores y el servicio de base de datos Postgres, como ejemplo. En caso de que quiera ejecutar otros servicios, añada los módulos correspondientes que implementen la dockerización.  

Adicionalmente, la infraestructura podría ampliarse y permite que otros módulos incluyan en ella sus propios contenedores específicos.

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Platform Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Platform Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

## Requisitos

Este proyecto depende de las siguientes herramientas:

- [Docker](https://docs.docker.com/get-docker/){target="_blank"}: versión `26.0.0` o superior.
- [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: versión `2.26.0` o superior.

!!! warning
    Evite instalar Docker mediante [Snap](https://snapcraft.io){target="_blank"}, puede quedar confinado por este sandbox y no tener acceso a directorios del host como `/opt/`, lo que puede impedir que los contenedores Docker de Etendo se inicien correctamente.

    Recomendación: instale Etendo usando la [última ISO](../../../../whats-new/release-notes/etendo-classic/iso.md)(que incluye Docker) o instale Docker siguiendo la guía de instalación oficial de su distribución.

## Uso de contenedores distribuidos en módulos

**Variables de configuración**

- Es necesario incluir al menos una variable de configuración para cada módulo que se vaya a lanzar; esta variable permite que se inicien todos los servicios relacionados con el módulo.

    `docker_<javapackage>=true`


    Ejemplo:
    ``` groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    ```

- En caso de que quiera configurar solo un servicio perteneciente a un módulo, es posible añadiendo una variable con el formato:

    `docker_<javapackage>_<service>=true`

    Ejemplo:
    ``` groovy title="gradle.properties"
    docker_com.etendoerp.docker_db=true
    ```
    !!! note
        En este caso, solo se tendrá en cuenta el servicio de base de datos al levantar y bajar servicios relacionados con el módulo `com.etendoerp.docker`. 

- También es posible que algunos servicios requieran variables de configuración; en ese caso, deben añadirse: 

    `docker_<javapackage>_<variable>=<value>`

    Ejemplo:
    ``` groovy title="gradle.properties"
    docker_com.etendoerp.tomcat_debug=8009
    ``` 
    !!! note
        En este ejemplo, esta variable configura el puerto del módulo [Servicio de Tomcat Dockerizado](./tomcat-dockerized-service.md), aunque las configuraciones necesarias se incluirán en la documentación de cada módulo.

- **Excluir servicios**

    Si la configuración de Compose incluye múltiples servicios, puede excluir o personalizar qué servicios se inician listando sus nombres en la siguiente propiedad:

    `docker.exclude=<service1>,<service2>`

    Ejemplo:
    ``` groovy title="gradle.properties"
    docker.exclude=das,auth
    ```

Finalmente, para aplicar siempre los cambios, ejecute 

``` bash title="Terminal"
./gradlew setup
```

## Tareas de Gradle para gestionar contenedores
Ejecute el siguiente comando para usar la infraestructura:

### Ejecución

``` bash title="Terminal"
./gradlew resources.up
```
Este comando buscará todos los recursos configurados e iniciará los contenedores.

!!! info 
    Antes de ejecutar las tareas de compilación de Gradle `./gradlew update.database compile.complete smartbuild`, necesita ejecutar `./gradlew resources.up` para crear e iniciar realmente los contenedores Docker. 

!!! note 
    Si solo tiene instalado y configurado el módulo base `com.etendoerp.docker`, este comando iniciará una base de datos PostgreSQL.

### Detención

``` bash title="Terminal"
./gradlew resources.stop
```
Este comando detendrá los contenedores.

### Baja

``` bash title="Terminal"
./gradlew resources.down
```
Este comando detendrá y eliminará los contenedores.

### Construcción

``` bash title="Terminal"
./gradlew resources.build
```
Este comando fuerza a los servicios que usan un Dockerfile a reconstruir su propia imagen Docker.

!!! info
    Este comando debe ejecutarse cuando la proyección o el mapeo se hayan modificado debido a cambios del usuario o a actualizaciones de la gestión de módulos en estas tablas. El comando fuerza al servicio DAS a recompilar y generar nuevas clases antes de iniciar el servicio.

### Verificación del estado

Para verificar el estado de los recursos iniciados por Docker Compose, puede usar los siguientes comandos de Docker:

`docker ps`

Este comando lista todos los contenedores Docker en ejecución. Debería ver los contenedores relacionados con Etendo

`docker compose logs`

Este comando muestra los logs de todos los servicios definidos en su configuración de Docker Compose, lo que puede ayudar en la resolución de problemas y en verificar que los servicios se están ejecutando correctamente.

!!! info 
    También es posible gestionar contenedores con herramientas como [Lazydocker](https://github.com/jesseduffield/lazydocker#installation){target=_isblank} o [Docker Desktop](https://www.docker.com/products/docker-desktop/){target=_isblank}.


## Servicio de base de datos Postgres

En este módulo se incluye un servicio de base de datos Postgres; esto permite usar la base de datos dockerizada en Etendo. Para utilizarlo, deben seguirse los siguientes pasos:

1. Una vez instalado el módulo `com.etendoerp.docker`, es necesario añadir una variable de configuración en el `gradle.properties` para habilitar el uso del servicio:

    ``` groovy title="gradle.properties"
    docker_com.etendoerp.docker_db=true
    ```

2. Luego es necesario ejecutar `./gradlew setup`, para aplicar los cambios de configuración.

3. Cuando se ejecuta `./gradlew resources.up`, se levantará un nuevo contenedor Docker con el servicio de base de datos usando las variables de configuración definidas en el `gradle.properties`, como puerto, usuario, contraseña, etc. 

    !!! warning
        En caso de que tenga el mismo servicio ejecutándose localmente en el mismo puerto, debería estar dado de baja. 

4. Finalmente, usando este servicio es posible ejecutar `./gradlew install` para instalar la base de datos desde cero, o es posible restaurar un backup y comenzar a usar el nuevo servicio de base de datos dockerizado. 



---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.