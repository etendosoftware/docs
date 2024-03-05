## Etendo RX Config Server

The Etendo RX Config Server is a crucial component in a distributed system, providing both server-side and client-side support for managing externalized configurations. This centralized solution allows for efficient and consistent management of application properties across various environments, from development to production. Seamlessly integrating with the Spring Environment and PropertySource abstractions, the Config Server is not only compatible with RX applications but also adaptable to a wide range of applications in different programming languages. This flexibility ensures that as applications progress through deployment stages, they consistently receive the necessary configurations to function optimally.

!!!info
      For detailed guidance on advanced usage, visit the [Spring Cloud Config Documentation](https://docs.spring.io/spring-cloud-config/docs/current/reference/html/){target="\_blank"}.

### Default configuration

The Config Server, by default, sources its configuration from the `./src-rc/rxconfig` directory. For those utilizing Etendo via source code, the configurations are located in the `./rxconfig` directory. To set up the basic configuration, run the command `./gradlew setup`. This will create the following files in the specified directory:

* `application.yaml`
* `das.yaml`
* `auth.yaml`
* `edge.yaml`

Each of these YAML files is structured to include the necessary properties for various applications.

### YAML structure

YAML files are used to define properties required by different applications in a simple, readable format. The syntax of YAML is based on key-value pairs, where indentation (spaces, not tabs) is used to show hierarchy. Here's an example:

```yaml title="YAML example"
classic:
  url: http://localhost:8080/etendo

das:
  url: http://localhost:8092
  label: Example text
```

In this example, properties like `classic.url`, `das.url`, and `das.label` are defined. Applications will refer to these properties using their respective keys.

### Properties access

Applications within Etendo RX, such as das, auth, edge, etc., each have a dedicated YAML file for their specific configurations. The application.yaml file is reserved for configurations that are shared across all services. For instance, by setting `das.url` in `application.yaml`, all applications can access this data. Properties defined in a service-specific file are exclusive to that service.

### Running config service

To launch the Config Service, execute the command `./gradlew rx:rx` (or `./gradlew rx` for source code installations). This action enables each service to access its configuration. For example, accessing `http://localhost:8888/das/default` yields a JSON response like the following:

For example, if you access `http://localhost:8888/das/default`
You will have something similar to:

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

This response indicates the configuration for the das service. The propertySources key lists the properties in priority order; if a property is defined in multiple files, the first definition is used.

### How to config a property

To modify a property, locate and edit the corresponding service configuration file. The Config Server dynamically updates to reflect the latest file content. However, client services load configurations at startup. Therefore, to apply new configurations, stop the running service using the rx command and then restart it.
