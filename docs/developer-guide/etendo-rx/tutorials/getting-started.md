# Getting Started with Etendo

Welcome! This guide will help you set up the Etendo Platform, including both the Etendo Classic functionalities and Etendo RX, our reactive platform capable of executing microservices with database interaction and asynchronous actions.

For more details, visit the [Etendo Platform repository](/docs/developer-guide/etendo-platform/concepts/what-is-etendo-platform.md).

Follow these steps for a smooth installation:

## Prerequisites

Ensure you have cloned the Etendo repository before proceeding:

```bash
git clone git@github.com:etendosoftware/etendo.git
```

## Add com.etendoerp.etendorx

dependencies {
implementation('com.etendoerp:etendorx:latest.release')
}

## Setting Up Configuration Variables

To compile and deploy an Etendo instance, you need to set up the configuration variables. To do this, create a copy of the `gradle.properties.template` file located in the root and `src-rx` folders:

```bash
cp gradle.properties.template gradle.properties
cp src-rx/gradle.properties.template src-rx/gradle.properties
```

Now, you can edit both `gradle.properties` files updating the variables, or simply use their default values.

- ### [gradle.properties](/docs/developer-guide/etendo-classic/reference/file-gradle-properties.md)
- ### [src-rx/gradle.properties](/docs/developer-guide/etendo-rx/reference/file-gradle-properties.md)

**Note:** Variables appearing in both files must have identical values. To gain more insight into what's happening, run the Gradle tasks with the `--info` or `--debug` flag.

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

3. Run Tomcat and navigate to [http://localhost:8080/etendo](http://localhost:8080/etendo) to access the Etendo ERP.

## Compiling Etendo RX

1. Execute the `rx:generate.entities` task:

```bash
./gradlew rx:generate.entities
```

2. To launch the RX services, run:

```bash
./gradlew rx:rx
```

By default, the following services should be up and running:

- Config
- Auth
- Edge
- Das
- Async

Congratulations! You've successfully set up the Etendo Platform. Continue your learning journey by visiting our [Tutorials](/docs/developer-guide/etendo-rx/tutorials/index.md) section.
