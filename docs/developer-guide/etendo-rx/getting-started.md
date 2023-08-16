# Getting Started with Etendo

Welcome! This guide will help you set up the Etendo Platform, including both the Etendo Classic functionalities and Etendo RX, our reactive platform capable of executing microservices with database interaction and asynchronous actions.

Follow these steps for a smooth installation:

## Prerequisites

Ensure you have cloned the Etendo repository before proceeding:

```bash
git clone git@github.com:etendosoftware/etendo.git
```

## Setting Up Configuration Variables

To compile and deploy an Etendo instance, you need to set up the configuration variables. To do this, create a copy of the `gradle.properties.template` file located in the root and `src-rx` folders:

```bash
cp gradle.properties.template gradle.properties
cp src-rx/gradle.properties.template src-rx/gradle.properties
```

Now, you can edit both `gradle.properties` files updating the variables, or simply use their default values.

- gradle.properties

!!! note
    The GitHub credentials are required.
    To configure GitHub credentials read 'Use of Repositories in Etendo' by clicking [**here**](https://docs.etendo.software/en/technical-documentation/etendo-environment/requirements-and-tools/developer-tools/use-of-repositories-in-etendo).

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


## Database Setup

For this tutorial, we'll create a new database named `etendo` on a PostgreSQL server accessible at port `5432`. If you prefer different settings, modify the values in the `gradle.properties` files accordingly.

## Generating Configuration Files

Run the setup tasks to generate the configuration files:

```bash
./gradlew setup
./gradlew rx:setup
```

**Warning:** If you change the default `bbdd.url` and/or `bbdd.sid`, you must update the `src-rx/rxconfig/das.yaml` file with the new values.

## Installing Etendo Classic

1. Execute the `install` task to create the initial database and compile the sources:

```bash
./gradlew install
```

2. Deploy Etendo ERP to Tomcat:

```bash
./gradlew smartbuild
```

This task deploys the `webContent` folder into the `tomcat/webapps` directory. Make sure to set `$CATALINA_HOME` to the correct path.

3. Run Tomcat and navigate to [**http://localhost:8080/etendo**](http://localhost:8080/etendo) to access the Etendo ERP.

## Compiling Etendo RX

1. Execute the `rx:generate.entities` task:

```bash
./gradlew rx:generate.entities
```

2. To launch the RX services, run:

```bash
./gradlew rx:rx
```
!!! info 
    The first time you run the above command, you'll need to provide an access token, for auth service.
    To accomplish it, open src-rx/logs/auth-*currentDate*.log
    There, at the end on the log you will find the value for the token.
    Fill the 'token' property with this value on src-rx/rxconfig/auth.yaml and re-run ./gradlew rx:rx


By default, the following services should be up and running:

- Config
- Auth
- Edge
- Das
- Async

Congratulations! You've successfully set up the Etendo Platform. Continue your learning journey by visiting our [**Tutorials**](/docs/developer-guide/etendo-rx/tutorials) section.
