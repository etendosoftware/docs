## Visión general

Esta sección proporciona una guía paso a paso para trabajar con Etendo RX, lo que implica crear un nuevo módulo con capacidades RX y construir un proyecto Spring Boot para consumir pedidos haciendo uso de proyecciones, repositorio y otros recursos JPA que crearemos en nuestro Etendo Classic.

------------------------------------------------------------------

## Creación de un nuevo módulo con capacidades RX

!!!note
    Asegúrese de completar la sección [Getting Started section in the developer guide](../../../developer-guide/etendo-rx/getting-started.md) para configurar la plataforma Etendo.

### Acceso como usuario administrador

Después de configurar el entorno local, tal y como se describe en [**instalar el entorno de desarrollo de Etendo**](../../../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md), necesitaremos iniciar sesión en el sistema con permisos de administración para crear el nuevo módulo, proyecciones, repositorio, etc.

Inicie sesión en su cuenta como administrador. Las credenciales de inicio de sesión por defecto para esta cuenta administrativa son:

- Nombre usuario: `admin`
- Contraseña: `admin`

Una vez haya iniciado sesión, cambie su rol a *System Administrator*, tal y como muestra la imagen:

  ![switch-admin.png](../../../assets/developer-guide/etendo-rx/tutorial/switch-admin.png)

El rol *System Administrator* nos permite acceder a algunas ventanas y otorga permisos para crear y manipular el sistema para satisfacer nuestras necesidades.

### Creación de un nuevo módulo

Ahora crearemos un nuevo módulo. Es una unidad de código autocontenida que realiza una función específica y, en nuestro caso, contiene todos los recursos necesarios en esta guía.
Para crear un nuevo módulo, vaya a la ventana Módulo y añada un nuevo registro proporcionando la siguiente información:

| Parámetro        | Costo                                  |
| --------------- | ------------------------------------- |
| Paquete Java    |`com.tutorial.classictutorial`         |
| Nombre          |`Tutorial`                             |
| Descripción     |`Módulo creado con fines de tutorial`  |
| Versión         |`1.0.0`                                |
| Is RX           |`True`                                 |
| Rx Java Package |`com.tutorial.rxtutorial`              |

Debería verse así:

  ![new-module.png](../../../assets/developer-guide/etendo-rx/tutorial/new-module.png)

Con nuestro nuevo módulo creado, comenzaremos a trabajar con *Proyecciones*.

------------------------------------------------------------------

## Proyección

Al utilizar Spring Data JPA para implementar la capa de persistencia, el repositorio normalmente devuelve una o más instancias de la clase raíz. Sin embargo, en la mayoría de los casos, no necesitamos todas las propiedades de los objetos devueltos.

En esos casos, puede que queramos recuperar los datos como objetos de tipos personalizados. Estos tipos reflejan vistas parciales de la clase raíz, conteniendo solo las propiedades necesarias. Aquí es donde las proyecciones resultan útiles.

Comience abriendo la ventana *Projections* y creando una nueva proyección con las siguientes propiedades:

| Campo       | Costo                                 |
| ----------- | ------------------------------------- |
| Módulo      |`tutorial - 1.0.0 - English (USA)`     |
| Nombre      |`rxtutorial`                           |
| Descripción |`Proyecciones necesarias para el tutorial`  |

  ![new-projection.png](../../../assets/developer-guide/etendo-rx/tutorial/new-projection.png)

### Añadir la proyección a una tabla

A medida que creamos la proyección, ahora necesitamos asignarla a una tabla de la que queramos extraer datos.
Para ello, abra la ventana :material-menu: Tablas y columnas y busque la tabla *Parte* (tal y como se menciona en la introducción, queremos consumir pedidos).

### Añadir una proyección

A continuación, navegue a la solapa *Projections* y añada una nueva proyección con el siguiente valor:

| Campo      | Costo                                          |
| ---------- | ---------------------------------------------- |
| Proyección |`rxtutorial - tutorial - 1.0.0 - English (USA)` |

  ![assign-projection.png](../../../assets/developer-guide/etendo-rx/tutorial/assign-projection.png)

### Añadir campos de entidad

Cuando se crea una proyección, necesitamos definir qué campos queremos recuperar.
En nuestro caso, necesitaremos el ID del registro, el nombre del tercero, el Nº de documento, el nombre del tipo de documento y el total general.
En la solapa Proyección, navegue a la solapa *Entity Field* y añada los siguientes campos:

|  Nombre del campo     |  Propiedad             |
| ------------------- | --------------------- |
| id                  |`id`                   |
| businessPartnerName |`businessPartner.name` |
| documentNo          |`documentNo`           |
| documentTypeName    |`documentType.name`    |
| grandTotalAmount    |`grandTotalAmount`     |

!!!note
    El campo *Propiedad* de esta solapa se gestiona con un mapeo de entidad; esto es similar a una propiedad de Hibernate.
    Por lo tanto, puede navegar por las entidades relacionadas desde aquí. Por ejemplo, para obtener el nombre del tercero, puede hacerlo accediendo a la entidad *businessPartner* y, a continuación, añadiendo el campo que desea recuperar, *name* en este caso.

  ![new-entity-fields.png](../../../assets/developer-guide/etendo-rx/tutorial/new-entity-fields.png)

------------------------------------------------------------------

## Repositorio

En Spring Data, un repositorio es una abstracción que proporciona las operaciones relativas a una clase de dominio para interactuar con un almacén de datos.
Para crear el repositorio para nuestro propósito, y del mismo modo que hicimos con las proyecciones, necesitamos ir a Tablas y columnas y buscar la tabla `C_Order`.

### Creación de un nuevo repositorio

Después de seleccionar una tabla, en este caso `C_Order`, necesitamos ir a la solapa *Repository* y crear un nuevo registro con los siguientes valores:

| Campo       | Costo                                |
| ----------- | ------------------------------------ |
| Módulo      |`tutorial - 1.0.0 - English (USA)`    |

 ![new-repository.png](../../../assets/developer-guide/etendo-rx/tutorial/new-repository.png)

------------------------------------------------------------------

## Selector

### Creación de un nuevo selector

A continuación, definiremos un método de búsqueda para usarlo más adelante cuando queramos consumir los pedidos. Esta consulta se toma como un filtro para recuperar los pedidos.
Para crear este nuevo método de filtro/búsqueda, en la solapa Repository de la tabla `C_Order`, cree un nuevo registro con los siguientes datos:

| Campo         | Costo                                                                                  |
| ----------- | -------------------------------------------------------------------------------------- |
| Method Name |`findSalesOrder`                                                                        |
|  Consulta   |`select o from Order o where o.documentType.id = :documentType order by o.documentNo`   |

  ![new-search.png](../../../assets/developer-guide/etendo-rx/tutorial/new-search.png)

### Creación de un parámetro de búsqueda

Como puede ver en la consulta anterior, utilizamos un parámetro llamado `:documentType`. 
Podemos añadir este tipo de parámetro para utilizarlo más adelante añadiéndole un valor correspondiente y filtrando en función de las necesidades actuales.
Para definir el parámetro, necesitamos crear una nueva fila en la solapa *Search Parameter* de la solapa *Search*. Rellénela con la siguiente configuración:

| Campo | Costo         |
| ----- | ------------- |
| Línea |`10`           |
| Nombre |`documentType` |
| Tipo  |`String`       |

En nuestro caso, filtraremos en función del tipo de documento de los pedidos.

  ![new-search-parameter.png](../../../assets/developer-guide/etendo-rx/tutorial/new-search-parameter.png)

------------------------------------------------------------------

## Creación de un nuevo proyecto Spring Boot

Ahora que hemos declarado la proyección, los campos, el repositorio y las búsquedas en Etendo Classic, necesitaremos crear un nuevo proyecto Spring para hacer uso de estos recursos JPA que acabamos de crear.
A continuación, encontrará los pasos para crear el proyecto Spring Boot y añadirlo como un módulo en Etendo RX.

### Creación del proyecto

1. Visite [**Spring Initializr**](https://start.spring.io/){target="_blank"} para iniciar la configuración de su proyecto.
2. Rellene los siguientes detalles:

    | Campo        | Costo                           |
    | ------------ | ------------------------------- |
    | Proyecto     |Gradle Project                   |
    | Idioma       |Java                             |
    | Spring Boot  |2.7.15 (o la última versión 2.7.x) |

    Metadatos del proyecto

    | Campo        | Costo                     |
    | ------------ | ------------------------- |
    | Grupo        |com.tutorial               |
    | Artifact     |rxtutorial                 |
    | Nombre       |rxtutorial                 |
    | Descripción  |Proyecto tutorial de Etendo RX |
    | Package Name |com.tutorial.rxtutorial    |
    | Packaging    |Jar                        |
    | Versión de Java |11                      |

3. Añada las siguientes dependencias: Spring Web, Lombok, Config Client
4. Haga clic en el botón *Generate* para descargar su proyecto. La página generará un archivo llamado `rxtutorial.zip`.

    ![spring-initializr.png](../../../assets/developer-guide/etendo-rx/tutorial/spring-initializr.png)

5. Descomprima el archivo zip en el proyecto de plataforma creado en el primer paso, como: `modules_rx/com.tutorial.rxtutorial`.

!!!info
    Recuerde crear la carpeta `com.tutorial.rxtutorial`, dentro de `modules_rx` antes de extraerlo.

### Configuración del proyecto

Después de crear el proyecto, necesitamos añadir cierta configuración para poder trabajar con Etendo Classic.

### Modificar el archivo build.gradle

Elimine la versión de los plugins de Spring:

```groovy
plugins {
    ...
    id 'org.springframework.boot' version '2.7.14'
    id 'io.spring.dependency-management' version '1.0.15.RELEASE'
}
```

Cámbielo por esto:

```groovy
plugins {
    ...
    id 'org.springframework.boot'
    id 'io.spring.dependency-management'
}
```

Gradle obtendrá las versiones del proyecto de la plataforma Etendo.

Añada las siguientes dependencias en la sección de dependencias:

```groovy
implementation 'org.springframework.cloud:spring-cloud-starter-openfeign'
implementation 'org.springframework.boot:spring-boot-starter-hateoas'
implementation 'com.etendorx:clientrest_core:latest.integration'
```

Añada el repositorio de Etendo:

```groovy
repositories {
    mavenCentral()
    maven {
        url = "https://maven.pkg.github.com/etendosoftware/etendo_rx"
        credentials {
            username = "${githubUser}"
            password = "${githubToken}"
        }
    }
}
```

!!! note
    `githubUser` y `githubToken` se configuraron en el primer paso.

Añada un conjunto de fuentes personalizado:

```groovy
sourceSets {
    main {
        java {
            srcDirs = [
                'src/main/java',
                'src-gen/main/java',
            ]
        }
    }
}
```

Después de configurar el proyecto, necesitaremos generar los archivos adecuados para RX.
La tarea RX generate.entities generará archivos Java en el directorio `src-gen`.
Ejecute la tarea `rx:generate.entities` para hacerlo.

``` bash title="Terminal"
./gradlew rx:generate.entities
```

------------------------------------------------------------------

## Configuración de un proyecto Spring Boot

Ahora configuraremos el nuevo proyecto Spring Boot para definir cómo se ejecutará.

### Actualización del archivo application.properties

Modifique su archivo `application.properties`, dentro del nuevo proyecto Spring Boot creado en los pasos anteriores, con las siguientes configuraciones:

```groovy title="application.properties"
config.server.url=http://localhost:8888
spring.config.import=configserver:${config.server.url}
spring.application.name=rxtutorial
server.port=8101
token=
```

El token está vacío, pero ahora generaremos uno nuevo.

### Añadir el valor del token

Para generar el valor del token necesitamos seguir estos pasos:

  1. Con el rol *System Administrator* en Etendo Classic, vaya a la ventana *RX Services*.
  2. Cree una nueva fila con los siguientes valores:

    |  Nombre del campo     |  Propiedad                      |
    | ------------------- | ------------------------------ |
    | Searchkey           |Tutorial                        |
    | Secret              |123                             |
    | Módulo              |Tutorial - 1.0.0 - English (USA)|

    ![new-rx-service.png](../../../assets/developer-guide/etendo-rx/tutorial/new-rx-service.png)

  3. Cambie al rol *F&B International Group Admin*.
  4. Vaya a la ventana :material-menu: Usuario.
  5. Elija un usuario, por ejemplo, F&B ES User

    !!! info
        Cambie la contraseña de este registro; la necesitará más adelante.
        Además, compruebe que el usuario está activo.

  6. En la solapa *RX Services Access* cree una nueva fila y rellénela con los siguientes valores:

    | Nombre del campo      |  Propiedad                     |
    | ------------------- | ------------------------------ |
    | Organización        |*                               |
    | RX Services         |Tutorial                        |
    | Rol por Defecto     |F&B España, S.A - Sales         |
    | Default Org         |F&B España, S.A                 |

    ![new-rx-service-access.png](../../../assets/developer-guide/etendo-rx/tutorial/new-rx-service-access.png)

  7. Ejecutemos RX para poder realizar la solicitud al servicio de Auth:

    ``` bash title="Terminal"
    ./gradlew rx:rx
    ```

  8. Abra Postman y realizaremos una solicitud de autenticación.

    ```json
    Verbose: POST
    URL: http://localhost:8094/api/authenticate
    Body:
    {
      "username":"F&BESUser",
      "password":"EtendoAdmin1",
      "service":"Tutorial",
      "secret":"123"
    }
    ```

    !!!warning
        Recuerde la contraseña cambiada anteriormente.

    ![postman-request.png](../../../assets/developer-guide/etendo-rx/tutorial/postman-request.png)

  9. Tome el token de la respuesta y rellene la propiedad *token* en el `application.properties` del módulo del tutorial.

### Añadir la anotación Component Scan a la clase Application

Para escanear su aplicación en busca de componentes anotados, añada la anotación `@ComponentScan` a su clase Application con los paquetes base necesarios:

!!!info
    La ruta a la clase de la aplicación, en este caso, es: `modules_rx/com.tutorial.rxtutorial/src/main/java/com/tutorial/rxtutorial/RxtutorialApplication.java`

```java
@ComponentScan({
    "com.tutorial.rxtutorial",
    "com.etendorx.clientrest.base",
})
```

!!! warning
    Recuerde añadir el import para la anotación ComponentScan:
    ```java
    ...
    import org.springframework.context.annotation.ComponentScan;
    ...
    ```

Por lo tanto, su clase Application debería verse así:

```java
package com.tutorial.rxtutorial;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan({
    "com.tutorial.rxtutorial",
    "com.etendorx.clientrest.base",
})
public class RxtutorialApplication {

  public static void main(String[] args) {
    SpringApplication.run(RxtutorialApplication.class, args);
  }

}
```

------------------------------------------------------------------

## Creación de un nuevo servicio Spring Boot

En este último paso antes de lanzar el microservicio, crearemos la lógica para consumir los pedidos utilizando la proyección y todos los recursos JPA que definimos en los pasos anteriores.
Siga las instrucciones a continuación para crear un nuevo servicio:

1. Cree un nuevo archivo en la siguiente ruta:

    ```java
    modules_rx/com.tutorial.rxtutorial/src/main/java/com/tutorial/rxtutorial/RxtutorialService.java
    ```

2. A continuación, copie y pegue el siguiente código en el archivo:

    ```java
    package com.tutorial.rxtutorial;

    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;

    import com.etendorx.clientrest.base.RestUtils;
    import com.etendorx.clientrest.base.RestUtilsException;
    import com.tutorial.rxtutorial.entities.org.openbravo.model.common.order.OrderRxtutorialModel;

    @RestController
    @RequestMapping(path = "/api")
    public class RxtutorialService {
      @Autowired
      RestUtils restUtils;

      @GetMapping(path = "/")
      public String get() throws RestUtilsException {
        String url = "/Order/search/findSalesOrder?documentType=AB22CE8FFA5E4AF29F2AC90FCDD400D8&projection=rxtutorial";
        var orders = restUtils.getList(url, OrderRxtutorialModel.class);
        StringBuilder html = new StringBuilder("<html>");
        html.append("<head>");
        html.append("<style type=\"text/css\">html {font-family: sans-serif;}</style>");
        html.append("</head>");
        html.append("<title>Orders</title></head>");
        html.append("<body>");
        html.append("<h2>Orders</h2>");
        html.append("<table>");
        for (OrderRxtutorialModel o : orders) {
          html.append(
              "<tr>" +
                  "<td>" + o.getDocumentNo() + "</td>" +
                  "<td>" + o.getBusinessPartnerName() + "</td>" +
                  "<td>" + o.getDocumentTypeName() + "</td>" +
                  "<td>" + o.getGrandTotalAmount() + "</td>" +
                  "</tr>"
          );
        }
        html.append("</table></body></html>");
        return html.toString();
      }
    }
    ```

    Este archivo mostrará una página HTML sencilla con los pedidos recuperados.
    Pero primero, echaremos un vistazo a la clase que acabamos de crear.

      ```java
      String url = "/Order/search/findSalesOrder?documentType=AB22CE8FFA5E4AF29F2AC90FCDD400D8&projection=rxtutorial";
      ```
      Esta URL es la que el proceso utilizará para consumir el servicio; como puede ver, aquí añadimos el filtro de *Selector* que creamos antes y le damos el parámetro de tipo de documento, con un ID de tipo de documento del pedido por el que filtraremos. Además, también estamos añadiendo la proyección a utilizar; al igual que antes, es la creada previamente.

      ```java
      var orders = restUtils.getList(url, OrderRxtutorialModel.class);
      ```

      La variable orders almacenará todos los pedidos que se filtrarán con nuestra solicitud; como puede ver, el método `getList` recibe dos parámetros: el primero es la URL que utilizaremos para realizar la solicitud y el segundo es la clase modelo del objeto recuperado.

3. A continuación, simplemente creamos un StringBuilder como una página HTML que se mostrará en el navegador.

------------------------------------------------------------------

## Ejecutar servicios RX

Para simplificar las ejecuciones de RX, dispone de una tarea de ejecución simplificada:

``` bash title="Terminal"
./gradlew rx:rx
```

!!!warning
    Recuerde configurar el servicio de Auth tal y como se describe en la página [Getting Started](../../../developer-guide/etendo-rx/getting-started.md#configure-auth-project).

## Ejecutar el proyecto del tutorial

Ahora podemos ejecutar nuestro nuevo microservicio. Para ello, ejecute la siguiente tarea:

``` bash title="Terminal"
./gradlew :com.tutorial.rxtutorial:bootRun
```

Abra su navegador y podrá ver la página generada con la siguiente URL: [**http://localhost:8101/api/**](http://localhost:8101/api/)

!!! success
    Ha creado correctamente un servicio RX totalmente funcional.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.