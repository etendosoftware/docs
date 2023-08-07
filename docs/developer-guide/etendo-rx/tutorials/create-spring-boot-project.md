# Creating a New Spring Boot Project

Before you begin, please ensure that you've completed the [Making new searches](/docs/developer-guide/etendo-rx/tutorials/making-new-searches.md) step.

## Project Creation

1. Visit [Spring Initializr](https://start.spring.io/) to start your project setup.
2. Fill in the following details:

   | Field        | Value                            |
   | ------------ | -------------------------------- |
   | Project      | Gradle Project                   |
   | Language     | Java                             |
   | Spring Boot  | 2.7.14 (or latest 2.7.x version) |
   | Packaging    | Jar                              |
   | Java Version | 11                               |

   ### Project Metadata

   | Field        | Value                      |
   | ------------ | -------------------------- |
   | Group        | com.tutorial               |
   | Artifact     | rxtutorial                 |
   | Name         | rxtutorial                 |
   | Description  | Etendo RX tutorial project |
   | Package Name | com.tutorial.rxtutorial    |

3. Add the following dependencies: Spring Web, Lombok, Config Client
4. Click on the 'Generate' button to download your project. The page will generate a file named `rxtutorial.zip`.

Uncompress the zip file to the platform project created in the first step, as: `modules_rx/com.tutorial.rxtutorial`.

## Project Configuration

### Modify `build.gradle` File

Remove version of spring plugins:

```groovy
plugins {
    ...
    id 'org.springframework.boot' version '2.7.14'
    id 'io.spring.dependency-management' version '1.0.15.RELEASE'
}
```

Change it to this:

```groovy
plugins {
    ...
    id 'org.springframework.boot'
    id 'io.spring.dependency-management'
}
```

Gradle will get versions from the Etendo Platform project.

Add the following dependencies in the dependencies section:

```groovy
implementation 'org.springframework.cloud:spring-cloud-starter-openfeign'
implementation 'org.springframework.boot:spring-boot-starter-hateoas'
```

Add the Etendo repository:

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

> Note: `githubUser` and `githubToken` were configured in the first step.

Add custom source set:

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

Etendo compile task will generate java files in the `src-gen` directory.

Great job! You've successfully created a new Spring Boot project. To proceed with the next steps, please navigate to the [next step]().
