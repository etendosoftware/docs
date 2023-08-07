# Configuring a Spring Boot Project

Before we start, ensure that you have successfully completed the [Create a new Spring Boot Project](/docs/developer-guide/etendo-rx/tutorials/configure-spring-boot-project.md) tutorial.

## Updating the `application.properties` file

Modify your `application.properties` file with the following configurations:

```
config.server.url=http://localhost:8888
spring.config.import=configserver:${config.server.url}
spring.application.name=rxtutorial
server.port=8101
token=
```

## Adding Component Scan Annotation to the Application Class

To scan your application for annotated components, add the `@ComponentScan` annotation to your Application class with the necessary base packages:

```java
@ComponentScan({
    "com.tutorial.rxtutorial",
    "com.etendorx.clientrest.base",
})
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

Congratulations! You have successfully configured a Spring Boot project with RX capabilities. To continue learning and building, proceed to the [next step]().
