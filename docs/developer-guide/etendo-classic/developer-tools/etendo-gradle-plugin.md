---
title: Etendo  Gradle  Plugin
---

## Overview

This article explains how to use Gradle, an open-source build automation tool that is designed to be flexible enough to build almost any type of software. 

!!! note
    For additional info read: [What is gradle?](https://docs.gradle.org/7.3/userguide/what_is_gradle.html){target="_blank"}.


Etendo uses Gradle to define and improve compilation, version management, modules publication, migrations and more tasks.


## How to use Gradle

Etendo project includes an embedded wrapper from Gradle called `gradlew`. Run the following  command in the Etendo project directory, and it will execute the mentioned task.

```bash title="Terminal"
 ./gradlew <task>
```
 

You can use `-P<Parameter Name>` to pass parameters in a task. For example:

```bash title="Terminal"
./gradlew publishVersion -Ppkg=test.package
```

## Etendo plugin


Add in the `build.gradle` file the plugin version to be used (you could check the latest version available in [Latest Releases](/whats-new/release-notes/etendo-classic/etendo-gradle-plugin/){target="_blank"})

```groovy title="build.gradle"
plugins {
    id 'com.etendoerp.gradleplugin' version <'lastest.release'>
}
```

### Plugin flags

The plugin flags need to be declared in the *etendo block*. <br>
In the following sections, you can find all the flags or variables available to set up and a brief description of each one.

```groovy title="build.gradle"
etendo {
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
}

```

## Common Gradle tasks in Etendo

- Creates the properties and configuration files.
  
    ``` bash title="Terminal"
    ./gradlew setup 
    
    ```
  
    | Command line parameters                  | Description                                               |                       
    |  -------------------       | ------------------------------------                      |
    | `-PforceDefaultProps=true` | Recreates the default properties file from the template.  |
    | `-PforceBackupProps=true`  | Recreates the backup.properties file from the template.   |
    | `-PforceQuartzProps=true`  | Recreates the quartz.properties file from the template.   |





- Creates the properties files from the templates in `/config` folder. The *setup* tasks depend on this task.
    ``` bash title="Terminal"
    ./gradlew prepareConfig
      
    ```

- Creates the database and installs reference data. 
    ``` bash title="Terminal"
    ./gradlew install
        
    ```

-  Compiles the Java classes that were modified and deploys them to Tomcat.

    ``` bash title="Terminal"
    ./gradlew smartbuild
        
    ``` 
    
    | Command line parameter         | Description                                                                                                            |          
    |  -------------------           | ------------------------------------                                                                                     |
    | `PignoreConsistency=true`      | Flag used to ignore the consistency verification (verifies the versions between the local modules and the installed ones)|
    

- Deletes all the Java Classes and recompiles them. 
    ``` bash title="Terminal"
    ./gradlew compile.complete
          
    ``` 
       
- Updates the database applying the changes in XML files.
    ``` bash title="Terminal"
    ./gradlew update.database
            
    ``` 

- Exports the database changes to XML files
    ``` bash title="Terminal"
    ./gradlew export.database
              
    ``` 
      
- The first one exports the module Application Dictionary data and the second one exports the configuration script. 
  ``` bash title="Terminal"
  ./gradlew export.database
  ./gradlew export.config.script
                
  ``` 
   

- Task to download core dependency.
    ``` bash title="Terminal"
    ./gradlew expandCore
                      
    ``` 
      

    | Command line parameter    | Description                                                        |                       
    |  -------------------       | ------------------------------------                               |
    | `-PforceExpand=<true>`     | Flag used to force the sources expansion when the core is in JAR.  |



- Task to download the modules dependencies in sources.
    ``` bash title="Terminal"
    ./gradlew expandModules
                      
    ``` 


    | Command line parameter    | Description                                                        |  
    |  -------------------       | ------------------------------------                                                                                                  |
    | `-Ppkg=<package name>`     | The name of the module to be *re expanded* in case that it is already in sources. This will *OVERWRITE* all the changes in the module.|


### Submodules

- Creates the `build.gradle` file with all the necessary information to publish.
    ``` bash title="Terminal"
    ./gradlew createModuleBuild
                      
    ```  

    | Comand line parameters                  | Description                                               |                       
    |  -------------------       | ------------------------------------                      |
    | `-Ppkg=<package name>`     | The name of the module.                                   |
    | `-Prepo=<repository name>` | The name of the repository.                               |




- Publish the module to a custom repository.
    
    ``` bash title="Terminal"
    ./gradlew publishVersion
                            
    ``` 

    |   Command Line Parameters         | Description| 
    |  :------------------------------- | :--- |
    | `-Ppkg=<packagename>`     | **Required** The name of the module.                                                |
    | `-Precursive=true    `     | This trigger the republication of all the modules which depends on the module being published. By default false.|
    | `-PupdateLeaf=true   `     | This updates automatically the version of the project beign published.By default false.|

  
  
- Uninstalls a source module.
    ``` bash title="Terminal"
    ./gradlew uninstallModule
                              
    ``` 
    
    | Comand line parameter                  | Description                                                                         |                       
    |  -------------------       | ------------------------------------                                                |
    | `-Ppkg=<modulename>`       | The javapackage of the source module to uninstall.                                  |



### Internal developer tasks

- Used to clone all the git submodules of a module extension (bundle). The module *build.gradle* should contain the property
      ``` bash title="Terminal"
      ./gradlew cloneDependencies
                                    
      ```
    


      ```groovy  title="build.gradle"
      ext.defaultExtensionModules = [
          'git@bitbucket.org:example1.git',
          'git@bitbucket.org:example2.git'
        ]
      ```



      | Comand line parameter                  | Description                                                  |                       
      |  -------------------                   | ------------------------------------                         |
      | `-Ppkg=<package name>`                 | **Required** The name of the bundle                          |



- Creates modules
    ``` bash title="Terminal"
    ./gradlew createModuleBuild
                                          
    ```

    | Comand line parameter                  | Description                                                  |                       
    |  -------------------                   | ------------------------------------                         |
    | `-Ppkg=<package name>`                 | **Required** The name of the bundle                          |
    | `-Prepo=<repository name>`             | **Required** The name of the repository                      |
    | `-Pbundle=<bundle package name>`       | The name of the bundle                                       |
  
      
    
      - `-Ppkg=all` Creates all the `build.gradle` files for each module, each `build.gradle` file will contain the dependencies between projects (in the dependencies block).

- Parameters to override the default core group, name and version.

    | Comand line parameters                  | Description                                                  |                       
    |  -------------------                   | ------------------------------------                         |
    | `-PcoreGroup=<core group>`             | The core group name                                          |
    | `-PcoreName=<core name>`               | The core name                                                |
    | `-PcoreVersion=<core version>`         | The core version                                             |


     
- Parameters to override the default repository. Publish all the modules located in the source modules directory.
    ``` bash title="Terminal"
    ./gradlew publishAll
                                              
    ```

    | Comand line parameters                  | Description                                                  |                       
    |  -------------------                    | ------------------------------------                         |
    | `-PupdateLeaf=true`                     | This updates automatically the version of all the project beign published. By defaul false.|
    | `-Pupdate=<mayor, minor, patch>`        | Used to specify which part of the version will be updated. By default patch.               |
    | `-PpushAndTag=true`                     | Used to specify if the modules published should push the changes and create a tag in the git repository. By default false.|
    | `-PpushAll=true`                        | Used to specify if all the modules should run the push and tag. By default false.|
        

- Task used to push and tag the modules' changes.
    ``` bash title="Terminal"
    ./gradlew pushToGit
                                                          
    ```

    | Comand line parameters                  | Description                                                  |                       
    |  -------------------                    | ------------------------------------                         |
    | `-PpushAll=true`                        | Used to specify if all the modules should run the push and tag. By defaul false.|
        
 

- Updates the version of a dependency in each `build.gradle` submodule.
    ``` bash title="Terminal"
    ./gradlew updateModuleBuildDependency
                                                              
    ```


!!! warning
    If you put a wrong version, you have to revert the changes manually.



| Comand line parameters                      | Description                                                  |                       
|  -------------------                    | ------------------------------------                         |
| `-Pdependency=<dependency name>`        | The name of the module to update in each `build.gradle`. Default `com.etendoerp.platform.etendo-core`|
| `-PlowerBound=<version>`                | The lower version bound. Example: `-PlowerBound=1.0.3`|
| `-PlowerBoundInclusive=<true or false>` | (Default false)|
| `-PupperBound=<version>`                | The upper version bound. Example: `-PupperBound=1.0.3`|
| `-PupperBoundInclusive=<true or false>` |(Default false)|
| `-PexactVersion=<version>`             |Will replace the current version with the specified one. The version should be between quotes. Example: `-PexactVersion="[1.0.3]"`|

  

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

```bash title="Terminal"

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
Etendo make uses of the [conflict resolution strategy](https://docs.gradle.org/current/userguide/dependency_resolution.html){target="_blank"} offered by GRADLE.

This approach is used to identify conflict between Etendo artifacts published to Nexus.

For example, when you make use of an Etendo module, which depends on the Etendo core.

```groovy title="build.gradle"
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
The version consistency approach verifies that an extracted Etendo JAR artifact is consistent with the installed one (**Equal** version).

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

This tool is used to filter all the JAR files in a specified directory.

A lookup is performed in the Maven Central Repository or a specified Nexus repository to verify if the JAR file already exists. The search is based on sha1 checksums.

Depending if the JAR file is found or not, two build files are generated.

For the resolved JAR files, the build file contains the block of code that you can use to import the JARs from the cloud.

For the unresolved JAR files, the build file contains all the necessary configuration and tasks to publish the JARs to a custom repository.

To execute the tool, run:

``` bash title="Terminal"
./gradlew searchJarDependency -Prepo=customrepo  -Plocation=customlocation -Pdestination=customdestination
```

Where

* -Prepo: Specifies the Nexus repository used to resolve JAR files or where uploading the unresolved ones.

* -Plocation: Specifies the location used to search JAR files locally in the project. The default location is the root project.

* -Pdestination: Specifies the location where the build files will be created. The default location is the root project.

---

#### JAR Scopes

This tool supports two scopes, Test and Compilation.

For each scope, two build files will be created.

* The Test scope filters all the JAR files located under a 'test' named directory (using the  **/test/\*\* pattern).

!!! info
    The files created will be resolved.TEST.artifacts.gradle and unresolved.TEST.artifacts.gradle

* The Compilation scope filter all the JAR files excluding those in a 'test' named directory.

!!! info
    The files created will be resolved.COMPILATION.artifacts.gradle and unresolved.COMPILATION.artifacts.gradle


Once the build files are created, you can use the [apply from](https://docs.gradle.org/current/userguide/plugins.html#sec:script_plugins){target="_blank"} Gradle clause to import the build file, or copy the content in your custom Gradle project (build.gradle).

The unresolved build file generated contains a custom task to publish the JAR files depending on the scope:

* Test: To publish, you need to run 

``` bash title="Terminal"
./gradlew publishUnresolvedTestJars
```

* Compilation: To publish, you need to run 

``` bash title="Terminal"
./gradlew publishUnresolvedCompilationJars
```

!!! warning
    The JARs will be published in the repository declared in the `searchJarDependency` task. 

## Uninstall modules


### Source modules
To uninstall an Etendo module you need to run the gradle task.

``` bash title="Terminal"
./gradlew uninstallModule -Ppkg=<modulename>
```

This task will try to delete the source module and the source dependencies which depends on.

If the module to uninstall is a dependency of other source module, an exception is thrown. You can force the uninstall providing the flag '-Pforce=true'.

#### Jar modules

You can make use of Gradle exclusion rules to prevent the extraction of a JAR dependency.
In the build.gradle of the root project you can specify the dependency to exclude.

``` groovy title="build.gradle"
configurations.implementation {
	exclude group: 'com.test', module: 'custommodule1'
  exclude group: 'com.test', module: 'custommodule2'
}
```

If the dependency belongs to a build.gradle of a source module, it may be downloaded when the 'javaCompile' task is executed. You can also make use of gradle exclude rules.

!!! warning
    When you make use of exclude rules in a custom source module, the pom.xml can be affected when you publish a new version.

To prevent downloading dinamic JAR modules, you need to remove the dependency from each build.gradle.

The JAR module also could also be a transitive dependency.
You can see the transitive dependencies tree running the gradle task
`./gradlew dependencies --info`
and remove the root parent dependency.

When you declare a dependency you can also exclude custom modules. See [Gradle dependency exclusion](https://docs.gradle.org/current/userguide/dependency_downgrade_and_exclude.html#sec:excluding-transitive-deps){target="_blank"}.

!!! info
    Etendo JAR modules are dinamically extracted in the root project 'build/etendo/modules' directory.

!!! warning
    Each build.gradle file (from the root project or source modules) can be using the dependency directly or by transitivity and this can lead to resolution of the module.

Finally you need to rebuild the system:

``` bash title="Terminal"
./gradlew update.database compile.complete
```

## Recompile CSS files

The `cssCompile` task in the Etendo Gradle configuration is specifically designed to convert `.scss` files into `.css` files. To customize the Etendo skin, you'll need to work with .scss files. When making changes to the .scss files, in order to modify the ERP skin, it is necessary to run the `cssCompile` task and restart Tomcat to generate the new .css files.

### Set-Up

!!! warning "Requirements"
    - **Node.js**: Version 16 or higher.
    - **npm**: Node Package Manager.
    - **Sass**: Must have a Sass compiler installed.

??? info "How to install Node.js, npm and Sass"

    === ":simple-linux: Linux"
        
        **Node.js & npm:**
        
        1. Update the package repository:
        ```bash
        sudo apt update
        ```
        
        2. Install Node.js and npm:
        ```bash
        sudo apt install nodejs npm
        ```

        3. Verify the installation:
        ```bash
        node -v
        npm -v
        ```

    === ":simple-macos: Mac OS"

        **Homebrew Installation:**

        - Install Homebrew by running the following command in the terminal:

        ```bash
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```

        - Once Homebrew is installed, verify it by checking its version:

        ```bash
        brew --version
        ```

        **Node.js & npm Installation using Homebrew:**
            
        1. Update Homebrew (ensuring you have the latest package definitions):
        ```bash
        brew update
        ```

        2. Install Node.js and npm:
        ```bash
        brew install node
        ```

        3. Verify the installation of Node.js and npm:
        ```bash
        node -v
        npm -v
        ```


    === ":material-microsoft-windows: Windows"
        
        **Node.js & npm:**
        
        1. Download the Node.js Windows Installer from the [official website](https://nodejs.org/){target="_blank"}.
        
        2. Run the installer and follow the instructions.
        
        3. After installation, open a command prompt or PowerShell and verify the installation:
        ```powershell
        node -v
        npm -v
        ```

    **Installing npm (Node Package Manager)**

    If you don't have npm installed on your system, follow these steps:

    - Install npm globally using the following command:

    ```bash
    npm install -g npm
    ```

    - Confirm the installation by checking the versions of node and npm:

    ```bash
    node -v
    npm -v
    ```

    **Installing Sass (Syntactically Awesome Style Sheets)**
    
    If you have npm installed and need the Sass compiler, follow these instructions:

    - Use npm to install Sass globally on your system:

    ```bash
    npm install -g sass
    ```

    - Confirm the Sass installation by running:

    ```bash
    sass --version
    ```

    Seeing the Sass version number means that Sass has been installed correctly.

### Execution

1. Ensure your terminal or command-line tool is open.
2. Navigate to the root directory of the Etendo project
3. Run the following command

```bash
./gradlew cssCompile smartbuild --info
```

After executing the task, look for the following output to indicate a successful build:
!!! success "Successful Execution"
    After executing the task, the following output indicates a successful build:

    ```
    > Task :cssCompile
    > BUILD SUCCESSFUL
    ```

    This confirms the successful processing of the files.

Finally, Restart Tomcat to apply the changes and ensure the updated .css files are properly served.