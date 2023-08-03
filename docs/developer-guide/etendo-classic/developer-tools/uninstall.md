---
title: Uninstall modules
---
## Uninstall modules


##### Source modules
To uninstall a Etendo module you need to run the gradle task.

`./gradlew uninstallModule -Ppkg=<modulename>`

This task will try to delete the source module and the source dependencies which depends on.

If the module to uninstall is a dependency of other source module, a exception will be throw. You can force the uninstall providing the flag '**-Pforce=true**'.

##### Jar modules

You can make use of Gradle exclusion rules to prevent the extraction of a JAR dependency.
In the build.gradle of the root project you can specify the dependency to exclude.
``` groovy
configurations.implementation {
	exclude group: 'com.test', module: 'custommodule1'
  exclude group: 'com.test', module: 'custommodule2'
}
```

If the dependency belongs to a build.gradle of a source module, it maybe downloaded when the 'javaCompile' task is executed. You can also can make use of **gradle** exclude rules.

!!! warning
    When you make use of excluded rules in a custom source module, the pom.xml can be affected when you publish a new version.

To prevent downloading dinamic JAR modules, you need to remove the dependency from each **build.gradle**.

The JAR module also could also be a transitive dependency.
You can see the transitive dependencies tree running the gradle task
`./gradlew dependencies --info`
and remove the root parent dependency.

When you declare a dependency you can also exclude custom modules. See [Gradle dependency exclusion](https://docs.gradle.org/current/userguide/dependency_downgrade_and_exclude.html#sec:excluding-transitive-deps)

!!! info
    Etendo JAR modules are dinamically extracted in the root project '**build/etendo/modules**' directory.

!!! warning
    Each **build.gradle** file (from the root project or source modules) can be using the dependency directly or by transitivity and this can lead to resolution of the module.

Finally you need to rebuild the system .
`./gradlew update.database compile.complete`