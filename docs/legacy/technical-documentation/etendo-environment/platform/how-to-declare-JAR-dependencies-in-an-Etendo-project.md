---
title: How to Declare JAR Dependencies in an Etendo Project
---
In an Etendo project, we can declare JAR dependencies in the main `build.gradle` file and in each module too.

1.  Modify `build.gradle`in the dependencies area. E.g.

```plaintext

dependencies {
    // Add your dependency here
    compile 'group:artifact:version'
}
```

In case of adding dependencies of a new repository, this must also be declared in the `build.gradle`. E.g.

```plaintext

repositories{
    maven{
        url "https://repo.futit.cloud/repository/partner-jars"
    }
}
```

> `jcenter()` and `maven-releases`, `maven-public-releases`, `maven-public-jars` from `repo.futit.cloud` repository are not necessary to define. They are automatically added.

2.  You must delete the Jar files if they were being used from the disk. If this is the first time using the dependency, this is not needed.

```plaintext

rm -r /opt/EtendoERP/<jarPath>/<JarName>
```

3.  After declaring dependencies and repositories, it only remains to run `expandModules` or `expand` task to download Jars.

```plaintext

./gradlew expandModules or ./gradlew expand
```