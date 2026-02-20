## Visión general del servicio Etendo RX Edge

El servicio Etendo RX Edge está diseñado para simplificar el enrutamiento de API y proporcionar servicios esenciales como seguridad, monitorización, métricas y resiliencia. Es una herramienta versátil que se integra sin problemas en su infraestructura de API.

### Funcionalidades clave

- Base de Spring Framework: Utiliza la robustez de Spring Framework y Spring Boot.
- Coincidencia flexible de rutas: Capaz de hacer coincidir rutas en función de varios atributos de la solicitud.
- Predicados y filtros personalizables: Ofrece la posibilidad de adaptar predicados y filtros para rutas específicas.
- Configuración fácil de usar: Los predicados y filtros son sencillos de configurar.
- Capacidad de reescritura de rutas: Permite modificar las rutas de las solicitudes según sea necesario.

!!!info
    Para configuraciones y funcionalidades más avanzadas, visite la [Documentación de Spring Cloud Gateway](https://docs.spring.io/spring-cloud-gateway/reference/index.html){target="\_blank"}.

### Dinámica operativa

El servicio Edge funciona como una pasarela, gestionando las solicitudes del cliente. Cuando se realiza una solicitud al Edge Server Gateway, el Gateway Handler Mapping evalúa si la solicitud corresponde a una ruta establecida. Si es así, el Gateway Web Handler procesa la solicitud, aplicando un conjunto de filtros específicos de la ruta.

### Ejecución del servicio

Para iniciar el servicio Edge, ejecute `./gradlew rx:rx` (o `./gradlew :rx` para instalaciones desde el código fuente). Se puede acceder al servicio en su URL predeterminada: `http://localhost:8096`.

### Directrices de configuración

Los ajustes de configuración se pueden realizar en el archivo `edge.yaml`. Para más información sobre los parámetros de configuración, consulte la [Documentación de Config Server](config-server.md) en el directorio rxconfig.

A continuación se muestra una visión general básica de la configuración edge predeterminada:

```yaml title="edge.yaml"
# Global settings
etendorx:
  auth:
    url: http://localhost:8094
classic:
  url: http://localhost:8080
subapp:
  url: http://localhost:3000

# Spring Cloud Gateway routing configurations
spring:
  cloud:
    gateway:
      routes:
        # Login Authentication Route
        - id: login_auth_route
          uri: ${etendorx.auth.url}
          predicates:
            - Method=GET,POST
            - Path=/login
          filters:
            - RewritePath=/login, /api/authenticate

        # Classic Application Path Route
        - id: classic_path_route
          uri: ${classic.url}
          predicates:
            - Method=GET, POST, DELETE, HEAD, PATCH
            - Path=/etendo/**
          filters:
            - RewritePath=/etendo/(?<segment>.*), /etendo/$\{segment}
            - RemoveResponseHeader=Location

        # DAS Path Route
        - id: das_path_route
          uri: ${das.url}
          predicates:
            - Method=GET, POST, DELETE, HEAD, PATCH
            - Path=/das/**
          filters:
            - RewritePath=/das/(?<segment>.*), /$\{segment}
```

### Comprender la configuración

1. Variables globales: Definen las URL para diferentes servicios como autenticación, aplicación clásica y subaplicaciones.
2. Configuraciones de enrutamiento:
   - Ruta de autenticación de inicio de sesión: Enruta las solicitudes `/login` al servicio de autenticación.
   - Ruta de la aplicación clásica: Gestiona varios métodos HTTP para rutas que comienzan por `/etendo/`.
   - Ruta DAS: Gestiona las solicitudes al servicio DAS con rutas que comienzan por `/das/`.

### Añadir servicios personalizados

Para integrar un nuevo servicio, añada una configuración de enrutamiento en `spring.cloud.gateway.routes`. Siga la estructura existente:

```yaml title="YAML example"
  #Example of adding a custom service route
  - id: <<custom_service_identifier>>
    uri: <<Internal_url_accessible_by_edge_service>>
    predicates:
      - Method=<<HTTP_Methods>>
      - Path=<<Matching_Path>> 
    filters:
      - RewritePath=/<<path_segment_to_remove>>/(?<segment>.*), /$\{segment}
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.