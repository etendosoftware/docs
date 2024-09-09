---
title: Getting Started
---

## Overview

This guide will help you set up Etendo, including both the Etendo Classic functionalities and Etendo RX, our reactive platform capable of executing microservices with database interaction and asynchronous actions.

Follow these steps for a smooth installation:

## Installing Etendo

### Prerequisites

Ensure you have cloned the Etendo repository before proceeding:

```bash
git clone git@github.com:etendosoftware/etendo_base.git
```

### Setting Up Configuration Variables

To compile and deploy an Etendo instance, you need to set up the configuration variables. To do this, create a copy of the `gradle.properties.template` file located in the root.

```bash title="Terminal"
cp gradle.properties.template gradle.properties
```

Now, you can edit the `gradle.properties` file updating the variables, or simply use its default values.

- gradle.properties

!!! note
    The GitHub credentials are required.
    To configure GitHub credentials read the [Use of Repositories technical guide](../../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md) in Etendo.

#### Adding the Configuration Variables for the Services to Dockerize

We need to add some variables to define which services will be dockerized. The options are Tomcat, the database and Etendo RX.

- Tomcat: `docker_com.etendoerp.tomcat=true`
- DB: `docker_com.etendoerp.docker_db=true`
- RX: `docker_com.etendoerp.etendorx=true`

!!!warning
    To be able to run this process, remember Docker must be installed.

| Variable                | Description                                                      | Default Value      |
| ----------------------- | ---------------------------------------------------------------- | ------------------ |
| `githubUser githubToken`| GitHub repository credentials, for access to commercial modules  |                    |
| `context.name`          | Environment name                                                 | etendo             |
| `bbdd.sid`              | Database name                                                    | etendo             |
| `bbdd.port`             | Database port                                                    | 5432               |
| `bbdd.systemUser`       | Database system user                                             | postgres           |
| `bbdd.systemPassword`   | Database system password                                         | syspass            |
| `bbdd.user`             | Database user                                                    | tad                |
| `bbdd.password`         | Database password                                                | tad                |
| `docker_com.etendoerp.tomcat` | Dockerized Tomcat                                          | false              |
| `docker_com.etendoerp.docker_db` | Dockerized Database                                     | false              |
| `docker_com.etendoerp.etendorx` | Dockerized Etendo RX                                     | false              |

### Adding Dependencies for Etendo RX and Tomcat

To be able to add RX and Tomcat dependencies, it is necessary to modify the `dependecies` block from `build.gradle` file.

The needed dependencies are:

```bash title="build.gradle"
dependencies {
    implementation('com.etendoerp.platform:etendo-core:[22.1.0,24.3.0)')
    implementation('com.etendoerp:platform.extensions:2.0.0')
    implementation('com.etendoerp:tomcat:latest.release')
}
```

### Database Setup

For this tutorial, we will create a new database named `etendo` on a PostgreSQL server accessible at port `5432`. If you prefer different settings, modify the values in the `gradle.properties` files accordingly.

### Generating Configuration Files

Now we need to generate the configuration files, for this, run:

```bash title="Terminal"
./gradlew setup
```

### Setting Up RX Docker Container

Before installing Etendo Classic, it is necessary to create the containers where Tomcat, the database, and the RX services will be located.

Using the `resources.up` task, Gradle will generate the required containers.

```bash title="Terminal"
./gradlew resources.up
```

### Installing Etendo Classic

At this point, we have all the source code and the architecture needed to install Etendo with Etendo RX.
To do so, run the `install` task to create the initial database.

``` bash title="Terminal"
./gradlew install
```

After the database creation, compile the project and deploy Etendo Classic to Tomcat with the following command:

``` bash title="Terminal"
./gradlew smartbuild
```

This task deploys the `webContent` folder into the Tomcat container.

Once the `smartbuild` task has finished, navigate to [**http://localhost:8080/etendo**](http://localhost:8080/etendo) to access Etendo Classic.

!!!note
    If you want to debug Tomcat locally with IntelliJ, visit [Tomcat Dockerized Service](../../developer-guide/etendo-classic/bundles/platform/tomcat-dockerized-service.md).

By default, the following services should be up and running:

- Config
- Auth
- Edge
- Das

!!! success
    You have successfully set up the Etendo Platform. Continue your learning journey by visiting our [Creating a New Microservice section in the developer guide](../../developer-guide/etendo-rx/tutorials/creating-a-new-microservice.md).