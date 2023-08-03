---
title: How to Declare JAR Dependencies in an Etendo Project
---
In an Etendo project, we can declare JAR dependencies in the main `build.gradle` file and in each module too.

1.  Modify `build.gradle`in the dependencies area. E.g.

```groovy

dependencies {
    // Add your dependency here
   	implementation 'group:artifact:version'
}
```

In case of adding dependencies of a new repository, this must also be declared in the `build.gradle`. E.g.

``` groovy

repositories{
    maven{
        url "https://repo.futit.cloud/repository/partner-jars"
    }
}
```

!!! info
    `maven-releases`, `maven-public-releases`, `maven-public-jars` from `repo.futit.cloud` repository are not necessary to define. They are automatically added.



2.  You must delete the Jar files if they were being used from the disk. If this is the first time using the dependency, this is not needed.

```plaintext

rm -r /opt/EtendoERP/<jarPath>/<JarName>
```

3.  After declaring dependencies and repositories, you can run

`./gradlew dependencies`

This task will list all the graph of declared dependencies.

## Consistency
When a new Etendo JAR dependency is added or the version is updated, a `update.database` is need it to run before executing any compilation task (smartbuild, compile.complete, etc).
You can force the compilation tasks adding to the Etendo plugin extension the ignore flag
``` groovy
etendo {
	ignoreConsistencyVerification = true 
}
```
Or run the tasks with the `-PignoreConsistency=true` flag.

By default the plugin will not allow you to add a JAR dependency with an old version to the current installed one.
You can ignore this behavior adding to the plugin extension the module name to be updated with an old version
``` groovy
etendo {
	ignoredArtifacts = ['com.etendoerp.mymodulename']
}
```
