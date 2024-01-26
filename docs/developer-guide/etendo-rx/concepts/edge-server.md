## Overview of Etendo RX Edge Service

The Etendo RX Edge Service is designed to simplify API routing and provide essential services like security, monitoring, metrics, and resilience. It is a versatile tool that integrates seamlessly into your API infrastructure.

### Key Features

- **Spring Framework Base**: Utilizes the robustness of Spring Framework and Spring Boot.
- **Flexible Route Matching**: Capable of matching routes based on various request attributes.
- **Customizable Predicates and Filters**: Offers the ability to tailor predicates and filters for specific routes.
- **User-Friendly Configuration**: Predicates and filters are straightforward to configure.
- **Path Rewriting Capability**: Allows for the modification of request paths as needed.

For more advanced configurations and features, consult the [Spring Cloud Gateway Documentation](https://docs.spring.io/spring-cloud-gateway/reference/index.html).

### Operational Dynamics

The Edge Service functions as a gateway, handling client requests. When a request is made to the Edge Server Gateway, the Gateway Handler Mapping assesses whether the request corresponds to an established route. If it does, the Gateway Web Handler processes the request, applying a set of route-specific filters.

### Running the Service

To launch the Edge Service, execute `./gradlew rx:rx` (or `./gradlew :rx` for installations from the source code). The service can be accessed at its default URL: `http://localhost:8096`.

### Configuration Guidelines

Configuration adjustments can be made in the `edge.yaml` file. For further information on configuration settings, please refer to the [Config Server Documentation](/developer-guide/etendo-rx/concepts/config-server/) in the rxconfig directory.

Below is a basic overview of the default edge configuration:

```yaml
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

### Understanding the Configuration

1. **Global Variables**: Define URLs for different services like authentication, classic app, and sub-applications.
2. **Routing Configurations**:
   - **Login Authentication Route**: Routes `/login` requests to the authentication service.
   - **Classic Application Path Route**: Handles various HTTP methods for paths starting with `/etendo/`.
   - **DAS Path Route**: Manages requests to the DAS service with paths starting with `/das/`.

### Adding Custom Services

To integrate a new service, add a routing configuration in `spring.cloud.gateway.routes`. Follow the existing structure:

```yaml
# Example of adding a custom service route
- id: <<custom_service_identifier>>
  uri: <<Internal_url_accessible_by_edge_service>>
  predicates:
    - Method=<<HTTP_Methods>>
    - Path=<<Matching_Path>>
  filters:
    - RewritePath=/<<path_segment_to_remove>>/(?<segment>.*), /$\{segment}
```
