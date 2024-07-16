---
title: Getting Started
---

## Overview

This guide will help you set up the Etendo Platform, including both the Etendo Classic functionalities and Etendo RX, our reactive platform capable of executing microservices with database interaction and asynchronous actions.

Follow these steps for a smooth installation:

## Installing Etendo

### Prerequisites

Ensure you have cloned the Etendo repository before proceeding:

```bash
git clone git@github.com:etendosoftware/etendo.git
```

### Setting Up Configuration Variables

To compile and deploy an Etendo instance, you need to set up the configuration variables. To do this, create a copy of the `gradle.properties.template` file located in the root and `src-rx` folders:

```bash title="Terminal"
cp gradle.properties.template gradle.properties
cp src-rx/gradle.properties.template src-rx/gradle.properties
```

Now, you can edit both `gradle.properties` files updating the variables, or simply use their default values.

- gradle.properties

!!! note
    The GitHub credentials are required.
    To configure GitHub credentials read the [Use of Repositories technical guide](../../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md) in Etendo.

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

- src-rx/gradle.properties

| Variable      | Description                          | Default Value      |
| ------------- | ------------------------------------ | ------------------ |
| `bbdd.rdbms`| Database manager system  | POSTGRE |
| `bbdd.driver`       | Environment name | org.postgresql.Driver |
| `bbdd.url`    |  Database name | jdbc:postgresql://localhost:5432 |
| `bbdd.sid`    |  Database port | etendo |
| `bbdd.systemUser`    |  Database system user | postgres |
| `bbdd.systemPassword`    |  Database system password | syspass |
| `bbdd.user`    |  Database user | tad |
| `bbdd.password`    |  Database password | tad |
| `bbdd.sessionConfig	`    |  Database session preferences	 | select update_dateFormat('DD-MM-YYYY') |

!!! warning
    Variables appearing in both files must have identical values. To gain more insight into what's happening, run the Gradle tasks with the `--info` or `--debug` flag.


### Database Setup

For this tutorial, we will create a new database named `etendo` on a PostgreSQL server accessible at port `5432`. If you prefer different settings, modify the values in the `gradle.properties` files accordingly.

### Generating Configuration Files

Now we need to generate the configuration files, for this, run:

```bash title="Terminal"
./gradlew setup
./gradlew rx:setup
```

!!!warning
    If you change the default `bbdd.url` and/or `bbdd.sid`, you must update the `src-rx/rxconfig/das.yaml` file with the new values.

### Installing Etendo Classic

At this point, we have all the source code needed to create the arquitecture of Etendo.
To do so, run the `install` task to create the initial database

``` bash title="Terminal"
./gradlew install
```

After the database creation, compile the project and deploy Etendo Classic to Tomcat with the following command:

``` bash title="Terminal"
./gradlew smartbuild
```

This task deploys the `webContent` folder into the `tomcat/webapps` directory. Make sure to set `$CATALINA_HOME` to the correct path.

Run Tomcat and navigate to [**http://localhost:8080/etendo**](http://localhost:8080/etendo) to access the Etendo Classic.

!!!note
    If you want to set up Tomcat locally with IntelliJ, follow the [Install Etendo Development Environment developer guide](../../developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment.md).

### Compiling Etendo RX

Execute the `rx:generate.entities` task to create the needed jars to start working with Etendo RX:

``` bash title="Terminal"
./gradlew rx:generate.entities
```

To launch the RX services, run:

``` bash title="Terminal"
./gradlew rx:rx
```

The first time you run the command above, you need to provide an access token for auth service, so now, we proceed to configure the auth project.

### Configure auth project

After executing the rx:rx task, it starts setting up the services.
It starts with the configuration service and when it starts to try with the auth service, it will fail because of the missing token.
To extract the token check Auth log file in `src-rx/logs/auth.log`

You will find something similar to:

```
Populate the auth.yaml file with the following property:
token: eyJhbGciOiJSUzI1NiJ9... (truncated)
```

Copy the value of token line and replace the token value in the file `src-rx/rxconfig/auth.yaml`

Replace default empty token value with log content

```
 token: eyJhbGciOiJSUzI1NiJ9... (truncated)
```

Now that you fill the token value, run rx:rx task again and all the microservices will be up and running.

By default, the following services should be up and running:

- Config
- Auth
- Edge
- Das
- Async

!!! success
    You have successfully set up the Etendo Platform. Continue your learning journey by visiting our [Creating a New Microservice section in the developer guide](../../developer-guide/etendo-rx/tutorials/creating-a-new-microservice.md).