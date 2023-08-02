---
title: Install Modules in Etendo
---

## Overview

- Search for dependencies
- Set dependencies
- Expand (download) and install dependencies

## Search for dependencies

1.  Search for the module that you want to install [here](https://repo.futit.cloud/).

!!! info
    To log in, use your Nexus Access distributed alongside your license.

2.  Go to “Browse” and see all the repositories:

![installmodules1.jpeg](/docs/assets/legacy/technicaldocumentation/setupandupgrade/installmodules1.jpeg)

3.  Inside a repository, you can see all the modules and information (Group, Name and versions):

![installmodules2.jpeg](/docs/assets/legacy/technicaldocumentation/setupandupgrade/installmodules2.jpeg)

## Set dependencies

1.  In your Etendo project, open the `build.gradle` file.
2.  In the dependencies area, declare the modules. In order to do that, change group, name and version.

![installmodules3.jpeg](/docs/assets/legacy/technicaldocumentation/setupandupgrade/installmodules3.jpeg)

Declaration examples:

```plaintext

dependencies {
    // Add your dependency here
    moduleDeps ('com.etendo:example.module:1.0.0@zip'){trasitive = true }
    moduleDeps group: 'com.etendo', name: 'example.module', version:'[1.0.0,)', ext:'zip', transitive: true
}
```

> You can declare a specific version (e.g. '1.0.0') or an interval of versions:
> \[begin, end\] - Both versions are included
> (begin, end) - Both versions are not included
> \[begin, ) - From a base version to the latest one
!!! info
    And the other possible combinations

## Expand (download) and install dependencies

Once all modules are declared, run the following commands:

```plaintext

./gradlew expandModules
./gradlew smartbuild -Dlocal=no
```

!!! info
    Restart the Tomcat server and check the installation.

!!! success
    The module is ready to use in Etendo!

## Installing translation modules

If you want to install translation modules, you have to follow some more steps. The translation modules are installed automatically when you compile the code for first time. E.g. after running `./gradlew install` command to create a new client's instance.  
But if you want to update a translation module version you can execute:

```plaintext

./gradlew install.translation -Dmodule=javapackage
./gradlew smartbuild -Dlocal=no
```

!!! info
    install.translation task change the module status to be installed in the next smartbuild.

Another option to force the installation of all the translation modules is to add the `forceRefData=true` property in the `Openbravo.properties` file and then run:

```plaintext

./gradlew smartbuild -Dlocal=no
```
