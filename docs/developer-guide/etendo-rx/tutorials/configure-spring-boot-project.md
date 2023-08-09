# Configuring a Spring Boot Project

Before we start, ensure that you have successfully completed the [Create a new Spring Boot Project](/docs/developer-guide/etendo-rx/tutorials/configure-spring-boot-project) tutorial.

## Updating the application.properties file

Modify your `application.properties` file, under the new spring boot project created on the previous steps, with the following configurations:

```
config.server.url=http://localhost:8888
spring.config.import=configserver:${config.server.url}
spring.application.name=rxtutorial
server.port=8101
token=
```
## Adding the 'token' value

To generate the token value we need to follow theese steps:

  1. As 'System Administartor' role on the ERP, go to 'RX Services' window.
  2. Create a new row with the following values:

    |  Field Name         |  Property                        |
    | ------------------- | -------------------------------- |
    | Searchkey           |  Tutorial                        |
    | Secret              |  123                             |
    | Module              |  Tutorial - 1.0.0 - English (USA)|

  3. Change to 'F&B International Group Admin' role.
  4. Go to 'User' window.
  5. Choose a user, e.g. 'F&B ES User'
  
    !!! info
        Change the password for this record, you'll need it later.
        Also, check that the user is active.

  6. On the tab 'RX Services Access' create a new row and fill it with the following values:
    
    |  Field Name         |  Property                        |
    | ------------------- | -------------------------------- |
    | Organization        |  *                               |
    | RX Services         |  Tutorial                        |
    | Default Role        |  F&B España, S.A - Sales         |
    | Default Org         |  F&B España, S.A                 |

  7. Open Postman and we'll make a authenticate request.
  
    Verbose: POST

    URL: http://localhost:8094/api/authenticate

    Body:
    ```json
          {
            "username":"F&B ES User",
            "password":"EtendoAdmin1", // Password changed before
            "service":"Tutorial",
            "secret":"123"
          }
    ```
  
  8. Take the token under the response and fill in the 'token' property on the application.properties of the tutorial module.

## Adding Component Scan Annotation to the Application Class

To scan your application for annotated components, add the `@ComponentScan` annotation to your Application class with the necessary base packages:

```java
@ComponentScan({
    "com.tutorial.rxtutorial",
    "com.etendorx.clientrest.base",
})
```
!!! warning
    Remember to add the import for ComponentScan annotation: 
    ```java
    ...
    import org.springframework.context.annotation.ComponentScan
    ...
    ```

Hence, your Application class should look like:

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

Congratulations! You have successfully configured a Spring Boot project with RX capabilities. To continue learning and building, proceed to the [**Tutorials**](/docs/developer-guide/etendo-rx/tutorials) section.
