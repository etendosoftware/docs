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

## Configuring build.gradle

On the source path, open `build.gradle` and locate the 'etendo' block in the file. Inside of it, add the following propertie:

```gradle
etendo {
    ignoreCoreJarDependency = true
}
```

This configuration will allow you to download the source of the project on your local environment. It will be needed for following steps. 

Now we need to execute the command that will download the source code:

```bash
./gradlew expandCore 
```

!!!info
    If you don't want to change the `build.gradle`, you can execute the command `./gradlew expandCore` and add the flag `-PforceExpand=true` at the end of it 

## Generating Configuration Files

Now we need to generate the configuration files, for this, run:

```bash
./gradlew setup
./gradlew rx:setup
```

!!!warning
    If you change the default `bbdd.url` and/or `bbdd.sid`, you must update the `src-rx/rxconfig/das.yaml` file with the new values.

## Installing Etendo Classic

At this point we have all the source code needed to create the arquitecture of Etendo.
To do so, run the `install` task to create the initial database

```bash
./gradlew install
```

After the database creation, we'll need to compile the project and deploy Etendo ERP to Tomcat with the followin command:

```bash
./gradlew smartbuild
```

This task deploys the `webContent` folder into the `tomcat/webapps` directory. Make sure to set `$CATALINA_HOME` to the correct path.

Run Tomcat and navigate to [**http://localhost:8080/etendo**](http://localhost:8080/etendo) to access the Etendo ERP.

!!!note
    If you want to set up Tomcat locally with IntelliJ, you can the following [**link**](/docs/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment) where it's explain how to do it.

## Compiling Etendo RX

Execute the `rx:generate.entities` task to create the needed jars to start working with Etendo RX:

```bash
./gradlew rx:generate.entities
```

To launch the RX services, run:

```bash
./gradlew rx:rx
```

The first time you run the above command, you'll need to provide an access token, for auth service, so noew, we'll proceed to configure the auth project.

## Configure auth project

After executing the rx:rx task it will start to setting up the services.
It will start with the config service and when it start to try with the auth service, it will fail because of the missing token.
To extract the token check Auth log file in `src-rx/logs/auth.log`

You will find something like this:

```
Populate the auth.yaml file with the following property:
token: eyJhbGciOiJSUzI1NiJ9... (truncated)
```

Copy the value of token line and replace the token value in the file `src-rx/rxconfig/auth.yaml`

Replace default empty token value with log content

```
 token: eyJhbGciOiJSUzI1NiJ9... (truncated)
```

Now that you fill the token value, run rx:rx task again, all the microservices, now, will be up and running.

By default, the following services should be up and running:

- Config
- Auth
- Edge
- Das
- Async

Congratulations! You've successfully set up the Etendo Platform. Continue your learning journey by visiting our [**First Steps**](/docs/developer-guide/etendo-rx/tutorials/first-steps) section.
