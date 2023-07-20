---
title: Search Jars Tool
---
## Etendo JAR Resolver Tool

This tool is used to filter all the **JAR** files in a specified directory.

A lookup is performed in the **Maven Central Repository** or a specified **Nexus** repository to verify if the **JAR** file already exists. The search is based on **sha1** checksums.

Depending if the **JAR** file is found or not, two **build files** are generated.

For the **resolved JAR** files, the build file contains the block of code that you can use to import the JARs from the cloud.

For the **unresolved JAR** files, the build file contains all the necessary configuration and tasks to publish the JARs to a custom repository.

To execute the tool, run:

`./gradlew searchJarDependency -Prepo=customrepo  -Plocation=customlocation -Pdestination=customdestination`

Where 
* **-Prepo:** Specifies the **Nexus** repository used to resolve **JAR** files or where uploading the unresolved ones.

* **-Plocation:** Specifies the location used to search **JAR** files locally in the project. The **default** location is the root project.

* **-Pdestination:** Specifies the location where the **build files** will be created. The **default** location is the root project.

---

#### JAR Scopes

This tool supports two scopes, **Test** and **Compilation**.

For each scope, **two build** files will be created.

* The **Test** scope filters all the **JAR** files located under a **'test'** named directory (using the  ****/test/\*\*** pattern).

!!! info
   The files created will be **resolved.TEST.artifacts.gradle** and **unresolved.TEST.artifacts.gradle**

* The **Compilation** scope filter all the **JAR** files excluding those in a **'test'** named directory.
!!! info
    The files created will be **resolved.COMPILATION.artifacts.gradle** and **unresolved.COMPILATION.artifacts.gradle**


Once the build files are created, you can use the [apply from](https://docs.gradle.org/current/userguide/plugins.html#sec:script_plugins) Gradle clause to import the build file, or copy the content in your custom Gradle project (**build.gradle**).

The **unresolved** build file generated contains a custom task to publish the JAR files depending on the scope:

* **Test:** To publish, you need to run `./gradlew publishUnresolvedTestJars`

* **Compilation:** To publish, you need to run `./gradlew publishUnresolvedCompilationJars`

!!! warning
   The JARs will be published in the repository declared in the `searchJarDependency` task. 


