---
title: Install Etendo Development Environment
---

## Overview

This section explains how to install a new Etendo environment. It includes:

- The steps to install Etendo on your PC
- A guide for installing Etendo if you are using IntelliJ IDEA Ultimate
- A guide for installing Etendo if you are using IntelliJ Community

## Requirements

!!! info
    You can read the [requirements page](/docs.etendo.software/requirements).

## Install Etendo on PC

!!! warning
    From Etendo 22Q1, the credentials should not be required interactively. You must set them in the `gradle.properties` file, since Gradle resolves and checks dependencies periodically. Create the credentials by following this [guide](/docs.etendo.software/developers/setup/use-of-repositories-in-etendo). <br>
    `githubUser=USER` > `githubToken=TOKEN`

##### Working with JARs

1.  Add to the **build.gradle** file the Etendo core dependency.

```groovy
dependencies {
  implementation('com.etendoerp.platform:etendo-core:22.1.0')
}
```

!!! info
    If you want to migrate from an environment with sources, refer to the [ Environment migration](https://docs.etendo.software/en/technical-documentation/etendo-environment/setup-and-upgrade/installation/22q1/core-format-migration) guide

To resolve the Etendo dependency, run:

```groovy
./gradlew dependencies
```

##### Working with sources

To work with sources, you need to specify the version to use in the Etendo extension block inside the `build.gradle`

```groovy
etendo {
	coreVersion = "<version>"
}
```

By default, Etendo will try to resolve the artifact `com.etendoerp.platform:etendo-core`

If you want to use a different artifact name, you can specify it in the Etendo block.
For example `com.smf.classic.core:ob:21.4.1`

```groovy
etendo {
  coreGroup = "com.smf.classic.core"
  coreName = "ob"
  coreVersion = "21.4.1"
  supportJars = false
}
```

!!! info
    Notice the `supportJars` flag. This is used to indicate if the current core version support JARs or not. By default, it is set to `true`

Finally, to download the sources, you need to run the expand task.

`./gradlew expand --info`

---

2.  Modify the `gradle.properties` file with your environment variables:

!!! warning
    Remember to set up the GitHub user and token since they are used to expand private modules. Create the credentials by following this [guide](/docs.etendo.software/developers/setup/use-of-repositories-in-etendo).

```groovy

githubUser=
githubToken=

context.name=etendo

bbdd.sid=etendo
bbdd.port=5432
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
bbdd.user=tad
bbdd.password=tad
```

3.  Run the following command to download the Etendo source code:

```plaintext
./gradlew setup
```

4.  Run the install task to create a new database:

```plaintext

./gradlew install
```

!!! info
    If you want to use an existing DB, just run `./gradlew setup compile.complete.deploy`. It may be necessary to run a `./gradlew update.database` first in case the database has local changes.

5.  Start Tomcat with this command:

```plaintext

$CATALINA_HOME/bin/catalina.sh start
```

!!! info
    If you do not want to use Tomcat directly, you can configure your IDE following the steps that are in the next section of this page.

6.  Open your browser at http://localhost:8080/etendo

> **Default credentials:**  
> User: admin  
!!! info
    Password: admin

!!! info
    Now you have a new Etendo environment running.

## How to run Etendo Project in IntelliJ IDEA Ultimate

1.  Open source directory with IntelliJ:

![intellij1.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij1.png)

2.  Open the project. This can be done from the welcome view, from `Open & Import` or from `File` >> `Open`

![intellij2.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij2.png)

3.  The project includes Tomcat configuration. Click on “Add configuration...”

![intellij3.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij3.png)

4.  Select the Tomcat configuration that appears first in the list, check the Tomcat server configuration on your machine, and then click the OK button.

![intellij4.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij4.png)

5.  Run Tomcat or run in development mode.

![intellij5.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij5.png)

## How to run Etendo Project in IntelliJ Community

1.  You can use the Smart Tomcat plugin. To install, go to `File` >> `Settings` >> `Plugins` and search for `“Smart Tomcat”`.

![intellij6.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij6.png)

2.  Download Apache-Tomcat and unzip it.
3.  Go to `Add Configuration` >> `+` >> `Smart Tomcat`. In Tomcat Sever, select the Apache-Tomcat folder. In the same window, set “Tomcat” as the name and change the Context path to the context project name.

![intellij7.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij7.png) ![intellij8.jpeg](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij8.png)

## Enable Etendo Logs (optional)

1 - Open the file `config/ log4j2-web.xml`, find the line `<AppenderRef ref = "Console" />` and uncomment it:

```

<Loggers>
    <Root level="info">
      <AppenderRef ref="RollingFile"/>
      <!-- Add this appender to show log messages in console i.e Eclipse: -->
      <AppenderRef ref="Console"/>  << UNCOMMENT THIS LINE
    </Root>
```

2 - Then run `./gradlew smartbuild` and reset the Tomcat.
