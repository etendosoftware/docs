## Etendo RX Config Server

El Etendo RX Config Server es un componente crucial en un sistema distribuido, ya que proporciona soporte tanto del lado del servidor como del lado del cliente para gestionar configuraciones externalizadas. Esta solución centralizada permite una gestión eficiente y coherente de las propiedades de las aplicaciones en distintos entornos, desde desarrollo hasta producción. Al integrarse de forma transparente con las abstracciones Spring Environment y PropertySource, el Config Server no solo es compatible con aplicaciones RX, sino que también es adaptable a una amplia variedad de aplicaciones en distintos lenguajes de programación. Esta flexibilidad garantiza que, a medida que las aplicaciones avanzan por las etapas de despliegue, reciban de forma consistente las configuraciones necesarias para funcionar de manera óptima.

!!!info
      Para obtener una guía detallada sobre el uso avanzado, visite la [Documentación de Spring Cloud Config](https://docs.spring.io/spring-cloud-config/docs/current/reference/html/){target="\_blank"}.

### Configuración por defecto

El Config Server, por defecto, obtiene su configuración del directorio `./src-rc/rxconfig`. Para quienes utilicen Etendo mediante código fuente, las configuraciones se encuentran en el directorio `./rxconfig`. Para configurar la configuración básica, ejecute el comando `./gradlew setup`. Esto creará los siguientes archivos en el directorio especificado:

* `application.yaml`
* `das.yaml`
* `auth.yaml`
* `edge.yaml`

Cada uno de estos archivos YAML está estructurado para incluir las propiedades necesarias para distintas aplicaciones.

### Estructura YAML

Los archivos YAML se utilizan para definir propiedades requeridas por distintas aplicaciones en un formato simple y legible. La sintaxis de YAML se basa en pares clave-valor, donde la indentación (espacios, no tabulaciones) se utiliza para mostrar la jerarquía. A continuación se muestra un ejemplo:

```yaml title="YAML example"
classic:
  url: http://localhost:8080/etendo

das:
  url: http://localhost:8092
  label: Example text
```

En este ejemplo, se definen propiedades como `classic.url`, `das.url` y `das.label`. Las aplicaciones harán referencia a estas propiedades utilizando sus respectivas claves.

### Acceso a propiedades

Las aplicaciones dentro de Etendo RX, como das, auth, edge, etc., tienen cada una un archivo YAML dedicado para sus configuraciones específicas. El archivo application.yaml está reservado para configuraciones que se comparten entre todos los servicios. Por ejemplo, al establecer `das.url` en `application.yaml`, todas las aplicaciones pueden acceder a estos datos. Las propiedades definidas en un archivo específico de un servicio son exclusivas de ese servicio.

### Ejecución del servicio de configuración

Para iniciar el Config Service, ejecute el comando `./gradlew rx:rx` (o `./gradlew rx` para instalaciones mediante código fuente). Esta acción permite que cada servicio acceda a su configuración. Por ejemplo, al acceder a `http://localhost:8888/das/default` se obtiene una respuesta JSON como la siguiente:

Por ejemplo, si accede a `http://localhost:8888/das/default`
Tendrá algo similar a:

```json title="Query response"
{
   "name":"das",
   "profiles":[
      "default"
   ],
   "label":null,
   "version":null,
   "state":null,
   "propertySources":[
      {
         "name":"file:<...>/rxconfig/das.yaml",
         "source":{
            "server.port":8092,
            "spring.datasource.url":"jdbc:postgresql://localhost:5432/etendo",
            "spring.datasource.username":"tad",
            "spring.datasource.password":"tad",
            "spring.jackson.serialization.FAIL_ON_EMPTY_BEANS":false,
         }
      },
      {
         "name":"file:/<...>/rxconfig/application.yaml",
         "source":{
            "classic.url":"http://localhost:8080/etendo",
            "das.url":"http://localhost:8092",
            "management.endpoints.web.exposure.include":"*",
            "spring.output.ansi.enabled":"ALWAYS",
            "public-key":"<...>"
         }
      }
   ]
}
```

Esta respuesta indica la configuración del servicio das. La clave propertySources enumera las propiedades en orden de prioridad; si una propiedad está definida en varios archivos, se utiliza la primera definición.

### Cómo configurar una propiedad

Para modificar una propiedad, localice y edite el archivo de configuración del servicio correspondiente. El Config Server se actualiza dinámicamente para reflejar el contenido más reciente del archivo. Sin embargo, los servicios cliente cargan las configuraciones al iniciarse. Por lo tanto, para aplicar nuevas configuraciones, detenga el servicio en ejecución usando el comando rx y, a continuación, reinícielo.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.