---
title: Etendo  Gradle  Plugin
---

## Overview

This article explains how to use Gradle, an open-source build automation tool that is designed to be flexible enough to build almost any type of software. (For additional info read: [What is gradle?](https://docs.gradle.org/current/userguide/what_is_gradle.html))

Etendo uses Gradle to define and improve compilation, version management, modules publication, migrations and more tasks.


## How to use Gradle

Etendo project includes an embedded wrapper from Gradle called `gradlew`. Run the `./gradlew <task>` command in the Etendo project directory, and it will execute the mentioned task.

You can use `-P<Parameter Name>` to pass parameters in a task. For example:

```plaintext

./gradlew publishVersion -Ppkg=test.package
```

## Etendo plugin

To work with the plugin you need to specify in the root project from where the plugin will be resolved.

- Create the `settings.gradle` file with the next content.

```groovy
pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
        maven {
            url 'https://repo.futit.cloud/repository/maven-public-releases'
        }
        maven {
            url 'https://repo.futit.cloud/repository/maven-public-snapshots'
        }
    }
}

// Add modules subprojects
new File("${this.rootDir}/modules").listFiles().each {
    if (it.directory && new File(it, 'build.gradle').exists()) {
        include(":modules:${it.name}")
    }
}

rootProject.name = "core"
```

- Add in the `build.gradle` file the plugin version to be used (you could ckeck the latest version available in [Nexus](https://repo.futit.cloud/#browse/browse:maven-public-releases:com%2Fetendoerp%2Fgradleplugin))

```groovy
plugins {
    id 'com.etendoerp.gradleplugin' version <'version'>
}
```

### Plugin flags

The plugin flags needs to be declared in the 'etendo plugin block'.

The etendo plugin block can be specified in the build.gradle

```groovy
etendo {

}
```

For example, to ignore the conflicts between the core versions you can use the 'forceResolution' flag.

```groovy
etendo {
	forceResolution = true
}
```

#### Flags and variables

```groovy
		// Variables used to specify the CORE artifact to resolve.
		String coreVersion = '[21.4.0,)' // default core version
    String coreGroup = "com.etendoerp.platform"
    String coreName = "etendo-core"

    /**
    * Flags used to indicate if the 'default' core dependencies (jar files) should be
    * loaded (This is the case when you are working with sources and the 'default' jar files are missing)
    * This flags should be false.
    */
    boolean loadCompilationDependencies = false
    boolean loadTestDependencies = false

    /**
     * Flag used to ignore loading the source modules to perform resolution conflicts.
     * Default true
     */
    boolean ignoreSourceModulesResolution = true

    /**
     * Flag used to perform or not the resolution of conflicts.
     * Default true
     */
    boolean performResolutionConflicts = true

    /**
     * Flag used to ignore throwing a error if there is conflict resolutions with the Core dependency.
     * Default false
     */
    boolean forceResolution = false

    /**
     * Flag used to apply the subproject dependencies to the main project.
     * Default true
     */
    boolean applyDependenciesToMainProject = true

    /**
     * Flag used to prevent overwriting the transitive source modules when performing the expandModules task.
     * Default true
     */
    boolean overwriteTransitiveExpandModules = true

    /**
     * Flag used to exclude the Core dependency from each subproject to all the configurations.
     * Default true
     */
    boolean excludeCoreDependencyFromSubprojectConfigurations = true

    /**
     *  Flag used to indicate that the current Core version support jars.
     *  Default true.
     * 	When this flag is set to false, the behavior of the 'expandModules' task will change, forcing to expand all the declared modules with 'moduleDeps' to sources.
     */
    boolean supportJars = true

    /**
     * List of Etendo artifacts to always extract and ignore from the version consistency verification.
     */
    List<String> ignoredArtifacts = []

    /**
     * Flag use to prevent throwing error on version inconsistency between modules.
     * Default false
     */
    boolean ignoreConsistencyVerification = false

    /**
     * Flag used to prevent throwing error when an artifact could not be resolved.
     * This includes transitives ones.
     * Default false
     */
    boolean ignoreUnresolvedArtifacts = false

    /**
     * The list of modules that should not be re expanded.
     * Default empty.
     */
    List<String> sourceModulesInDevelopment = []

    /**
     * Flag used to ignore the Etendo CORE jar dependency located in the
     * build.gradle of the root project.
     * Default false.
     */
    boolean ignoreCoreJarDependency = false

```

## Common Gradle tasks in Etendo

- `./gradlew setup --info` Creates the properties and configuration files.

  - Command line parameters.
    - `-PforceDefaultProps=true` recreates the default properties file from the template. **OPTIONAL**
    - `-PforceBackupProps=true` recreates the backup.properties file from the template. **OPTIONAL**
    - `-PforceQuartzProps=true` recreates the quartz.properties file from the template. **OPTIONAL**

- `./gradlew prepareConfig --info` Creates the properties files from the templates, the **setup** tasks depends on this task.
- `./gradlew install --info`
- `./gradlew smartbuild --info`
  - Command line parameters - `-PignoreConsistency=true` Flag used to ignore the consistency verification (verifies the versions between the local modules and the installed ones)
- `./gradlew compile.complete --info`
- `./gradlew update.database --info`
- `./gradlew export.database --info`
- `./gradlew export.config.script --info`
- `./gradlew expandCore --info` Task to download core dependency.
  - Command line parameters - `-PforceExpand=<true>` Flag used to force the sources expansion when the core is in JAR. **OPTIONAL**
- `./gradlew expandModules --info` Task to download the modules dependencies in sources.
  - Command line parameters - `-Ppkg=<package name>` The name of the module to be **re expanded** in case that is already in sources (this will **OVERWRITE** all the changes in the module). **OPTIONAL**

### Submodules

- `./gradlew registerModule --info` Creates the privileges to publish a new module in a specific repository`Command line parameters:
-`-Ppkg=<package name>`The name of the module.
-`-Prepo=<repository name>` The name of the repository.
- `./gradlew createModuleBuild --info` Creates the 'build.gradle' file with all the necessary information to publish.
  Command line parameters - `-Ppkg=<package name>` The name of the module. - `-Prepo=<repository name>` The name of the repository.
- `./gradlew publishVersion --info` Publish the module to a custom repository
  - Command line parameters.
    - `-Ppkg=<package name>` The name of the module. **REQUIRED**
    - `-Precursive=true` This trigger the republication of all the modules which depends on the module being published. **OPTIONAL** - default false.
    - `-PupdateLeaf=true` This updates automatically the version of the project beign published. **OPTIONAL** - default false.
- `./gradlew uninstallModule --info` Uninstall a source module. Refer to the [documentation](https://docs/en/technical-documentation/modules/uninstall)
  - Command line parameters
    - `-Ppkg=<modulename>` The javapackage of the source module to uninstall.

---

### Internal developer tasks

- `./gradlew cloneDependencies --info` Used to clone all the git submodules of a module extension (bundle). The module **build.gradle** should contain the property

```groovy
ext.defaultExtensionModules = [
      'git@bitbucket.org:example1.git',
      'git@bitbucket.org:example2.git'
    ]
```

- Command line parameters.
  - `-Ppkg=<package name>` The name of the bundle. **REQUIRED**
- `./gradlew createModuleBuild`
  - Command line parameters.
    - `-Ppkg=<package name>` The name of the module. **REQUIRED**
      - `-Prepo=<repository name>` The name of the repository. **REQUIRED**
      - `-Pbundle=<bundle package name>` The name of the bundle. **OPTIONAL**
      - `-Ppkg=all` Creates all the build.gradle files for each module, each build.gradle file will contain the dependencies between projects (in the dependencies block).
    - Parameters to override the default core group, name and version.
      - `-PcoreGroup=<core group>` The core group name. **OPTIONAL**
      - `-PcoreName=<core name>` The core name. **OPTIONAL**
      - `-PcoreVersion=<core version>` The core version. **OPTIONAL**
    - Parameters to override the default repository.
      - `-PcommercialRepo=<commercial repo name>` Used when the module is commercial. **OPTIONAL**
      - `-PpublicRepo=<public repo name>` Used when the module is not commercial. **OPTIONAL**
- `./gradlew publishAll --info` Publish all the modules located in the source 'modules' directory.
  - Command line parameters
    - `-PupdateLeaf=true` This updates automatically the version of all the project beign published. **OPTIONAL** - (Default false).
    - `-Pupdate=<mayor, minor, patch>` Used to specify which part of the version will be updated. **OPTIONAL** - (Default patch).
    - `-PpushAndTag=true` Used to specify if the modules published should push the changes and create a tag in the git repository. **OPTIONAL** - (Default false).
    - `-PpushAll=true` Used to specify if all the modules should run the push and tag. **OPTIONAL** - (Default false).
- `./gradlew pushToGit --info` Task used to push and tag the modules changes
  - Command line parameters - `-PpushAll=true` Used to specify if all the modules should run the push and tag. **OPTIONAL** - (Default false).
- `./gradlew updateModuleBuildDependency`. Updates the version of a dependency in each build.gradle submodule.

!!! warning
    If you put a wrong version, you have to revert the changes manually.


  - Command line parameters
    - `-Pdependency=<dependency name>` The name of the module to update in each build.gradle.
      **OPTIONAL**. Default 'com.etendoerp.platform.etendo-core'
    - `-PlowerBound=<version>` The lower version bound.
      **OPTIONAL**. Example: `-PlowerBound=1.0.3`
    - `-PlowerBoundInclusive=<true or false>`
      **OPTIONAL**. (Default false)
    - `-PupperBound=<version>` The upper version bound.
      **OPTIONAL**. Example: `-PupperBound=1.0.3`
    - `-PupperBoundInclusive=<true or false>`
      **OPTIONAL**. (Default false)
    - `-PexactVersion=<version>` Will replace the current version with the specified one. The version should be between quotes.
      **OPTIONAL** Example: `-PexactVersion="[1.0.3]"`

## Common Gradle flags

| Flag                   | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| --offline              | To execute Gradle without internet connection.       |
| --stop                 | To stop all Gradle daemons.                          |
| --no-daemon            | To execute a Gradle task without launching a daemon. |
| --info                 | To give more information in the task execution.      |
| --refresh-dependencies | will force download of dependencies.                 |

## Ant tasks

Most of [ant build tasks](http://wiki.openbravo.com/wiki/Development_Build_Tasks#Detailed_Build_Tasks), previously used in Openbravo, can be run with Gradle (but they do not have support):

```plaintext

./gradlew <ant task> [params]
```

Except some commands:
|Old Command| New Command|
|---|---|
|clean| antClean|
|setup|antSetup|
|init |antInit|
|install.source|antInstall|
|war|antWar|

## Consistency Verification

### Resolution of conflicts
Etendo make uses of the [conflict resolution strategy](https://docs.gradle.org/current/userguide/dependency_resolution.html) offered by GRADLE.

This approach is used to identify conflict between Etendo artifacts published to Nexus.



For example, when you make use of a Etendo module, which depends on the Etendo core.

```groovy
group          = 'com.etendo'
ext.artifact   = "moduleCextract"
version        = '1.0.1'
dependencies {
    // Etendo CORE dependency
    implementation 'com.etendoerp.platform:etendo-core:[22.1.1, 22.1.2]'
}
```

and you are currently working with the Etendo core in `22.1.0`, then a conflict resolution is found.

Depending on the type of conflict, if the problem is with the Etendo Core, then a Exception will be throw.

You can force the resolution using the extension flag

``` groovy
etendo {
	forceResolution = true
}
```

If you want to skip the resolution you can add to the plugin extension the flag
``` groovy
etendo {
	performResolutionConflicts = false
}
```


### Version consistency
The version consistency approach verifies that a extracted Etendo JAR artifact is consistent with the installed one (**Equal** version).

When a new Etendo JAR dependency is added or the version is updated, a `update.database` is need it to run before executing any compilation task (smartbuild, compile.complete, etc).
You can force the compilation tasks adding to the Etendo plugin extension the ignore flag
``` groovy
etendo {
	ignoreConsistencyVerification = true 
}
```
Or run the tasks with the `-PignoreConsistency=true` flag.

By default Etendo not allow you to add a JAR dependency with an old version to the current installed one.
You can ignore this behavior adding the module name to be updated with an old version as a configuration
``` groovy
etendo {
	ignoredArtifacts = ['com.etendoerp.mymodulename']
}
```

## Search Jars Tool

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

## Uninstall modules


### Source modules
To uninstall a Etendo module you need to run the gradle task.

`./gradlew uninstallModule -Ppkg=<modulename>`

This task will try to delete the source module and the source dependencies which depends on.

If the module to uninstall is a dependency of other source module, a exception will be throw. You can force the uninstall providing the flag '**-Pforce=true**'.

#### Jar modules

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





