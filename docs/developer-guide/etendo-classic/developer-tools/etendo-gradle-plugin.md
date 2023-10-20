---
title: Etendo  Gradle  Plugin 
tags: 
  - Gradle
  - Tasks
  - Plugin
  - Parameters
---

## Overview

This article explains how to use Gradle, an open-source build automation tool that is designed to be flexible enough to build almost any type of software. 

!!! note
    For additional information read: [What is gradle?](https://docs.gradle.org/7.3/userguide/what_is_gradle.html){target="_blank"}.


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

## Common Gradle flags

| Flag                   | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| --offline              | To execute Gradle without internet connection.       |
| --stop                 | To stop all Gradle daemons.                          |
| --no-daemon            | To execute a Gradle task without launching a daemon. |
| --info                 | To give more information in the task execution.      |
| --refresh-dependencies | Will force download of dependencies.                 |


## Etendo plugin


Add in the `build.gradle` file the plugin version available in [Gradle Plugin Release Notes](/whats-new/release-notes/etendo-classic/etendo-gradle-plugin/) or use `lastest.release` to resolve the latest version.

```groovy title="build.gradle"
plugins {
    id 'com.etendoerp.gradleplugin' version '1.2.2'
}
```

## Plugin configuration

The plugin configuration need to be declared in the *etendo block*. <br>
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

## Common Gradle tasks

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
      
- Exports the module Application Dictionary data.
    ``` bash title="Terminal"
    ./gradlew export.database
                  
    ``` 

- Exports the configuration script. 
    ``` bash title="Terminal"
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


## Submodules

- Creates the `build.gradle` file with all the necessary information to publish.
    ``` bash title="Terminal"
    ./gradlew createModuleBuild
                      
    ```  

    | Command line parameters                  | Description                                               |                       
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
    
    | Command line parameter                  | Description                                                                         |                       
    |  -------------------       | ------------------------------------                                                |
    | `-Ppkg=<modulename>`       | The javapackage of the source module to uninstall.                                  |



## Internal developer tasks

- Used to clone all the git submodules of a module extension (bundle). The module `build.gradle` should contain the property
      ``` bash title="Terminal"
      ./gradlew cloneDependencies
                                    
      ```
    


      ```groovy  title="build.gradle"
      ext.defaultExtensionModules = [
          'git@bitbucket.org:example1.git',
          'git@bitbucket.org:example2.git'
        ]
      ```



      | Command line parameter                  | Description                                                  |                       
      |  -------------------                   | ------------------------------------                         |
      | `-Ppkg=<package name>`                 | **Required** The name of the bundle                          |



- Creates all the `build.gradle` files for each module using the database from AD_MODULExml.
    ``` bash title="Terminal"
    ./gradlew createModuleBuild
                                          
    ```

    | Command line parameter                  | Description                                                  |                       
    |  -------------------                   | ------------------------------------                         |
    | `-Ppkg=<package name>`                 | **Required** The name of the bundle                          |
    | `-Prepo=<repository name>`             | **Required** The name of the repository                      |
    | `-Pbundle=<bundle package name>`       | The name of the bundle                                       |
    | `--Ppkg=all`                           |Creates all the `build.gradle` files for each module, each `build.gradle` file will contain the dependencies between projects (in the dependencies block).                |
  
      

- Parameters to override the default core group, name and version.

    | Command line parameters                  | Description                                                  |                       
    |  -------------------                   | ------------------------------------                         |
    | `-PcoreGroup=<core group>`             | The core group name                                          |
    | `-PcoreName=<core name>`               | The core name                                                |
    | `-PcoreVersion=<core version>`         | The core version                                             |


     
- Parameters to override the default repository. Publish all the modules located in the source modules directory.
    ``` bash title="Terminal"
    ./gradlew publishAll
                                              
    ```

    | Command line parameters                  | Description                                                  |                       
    |  -------------------                    | ------------------------------------                         |
    | `-PupdateLeaf=true`                     | This updates automatically the version of all the project beign published. By defaul false.|
    | `-Pupdate=<mayor, minor, patch>`        | Used to specify which part of the version will be updated. By default patch.               |
    | `-PpushAndTag=true`                     | Used to specify if the modules published should push the changes and create a tag in the git repository. By default false.|
    | `-PpushAll=true`                        | Used to specify if all the modules should run the push and tag. By default false.|
        

- Task used to push and tag the modules' changes.
    ``` bash title="Terminal"
    ./gradlew pushToGit
                                                          
    ```

    | Command line parameters                  | Description                                                  |                       
    |  -------------------                    | ------------------------------------                         |
    | `-PpushAll=true`                        | Used to specify if all the modules should run the push and tag. By defaul false.|
        
 

- Updates the version of a dependency in each `build.gradle` submodule.
    ``` bash title="Terminal"
    ./gradlew updateModuleBuildDependency
                                                              
    ```

    !!! warning
        If you put a wrong version, you have to revert the changes manually.


    | Command line parameters                  | Description                                                  |                       
    |  -------------------                    | ------------------------------------                         |
    | `-Pdependency=<dependency name>`        | The name of the module to update in each `build.gradle`. Default `com.etendoerp.platform.etendo-core`|
    | `-PlowerBound=<version>`                | The lower version bound. Example: `-PlowerBound=1.0.3`|
    | `-PlowerBoundInclusive=<true or false>` | (Default false)|
    | `-PupperBound=<version>`                | The upper version bound. Example: `-PupperBound=1.0.3`|
    | `-PupperBoundInclusive=<true or false>` |(Default false)|
    | `-PexactVersion=<version>`             |Will replace the current version with the specified one. The version should be between quotes. Example: `-PexactVersion="[1.0.3]"`|



## Ant tasks

Most of [ant build tasks](http://wiki.openbravo.com/wiki/Development_Build_Tasks#Detailed_Build_Tasks){target="_blank"} previously used can be run with Gradle:

```bash title="Terminal"

./gradlew <ant task> [params]
```

Except for some commands:

|Old Command| New Command| 
|---|---| 
|clean| antClean|
|setup|antSetup|
|init |antInit|
|install.source|antInstall|
|war|antWar|


## Conflict resolution

!!!note
    Etendo makes use of the [Conflict Resolution Strategy](https://docs.gradle.org/current/userguide/dependency_resolution.html){target="_blank"} offered by GRADLE.

This approach is used to identify conflict between Etendo artifacts published in a repository.

For example, when you make use of an Etendo module, which depends on the Etendo core

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

Depending on the type of conflict, if the problem is with the Etendo Core, then a Exception will be thrown.


!!!danger "To force the dependencies' resolution must be the last step to follow"
    You can force the resolution using the extension flag
    ``` groovy
    etendo {
      forceResolution = true
    }
    ```

    If you want to skip the resolution you can add to the plugin extension the flag.
    ``` groovy
    etendo {
      performResolutionConflicts = false
    }
    ```


## Version consistency
The version consistency approach verifies that an extracted Etendo JAR artifact is consistent with the installed one (Equal version).

When a new Etendo JAR dependency is added or the version is updated, a `update.database` is needed to run before executing any compilation task (smartbuild, compile.complete, etc).
You can force the compilation tasks by adding to the Etendo plugin extension the ignore flag

!!!warning "These section explains how to ingore the consistency verification. Use this approach only if there are no conflicts between versions. "
    ``` groovy
    etendo {
      ignoreConsistencyVerification = true 
    }
    ```
    or run the tasks with the `-PignoreConsistency=true` flag.

    By default Etendo does not allow you to add a JAR dependency with an old version to the current installed one.
    You can ignore this behavior adding the module name to be updated with an old version as a configuration.
    ``` groovy
    etendo {
      ignoredArtifacts = ['com.etendoerp.mymodulename']
    }
    ```



## Uninstall modules

=== ":octicons-package-16: Source Modules"

    To uninstall an Etendo module you need to run the gradle task.

    ``` bash title="Terminal"
    ./gradlew uninstallModule -Ppkg=<modulename>
    ```

    This task will try to delete the source module and the source dependencies which depends on it.

    If the module to uninstall is a dependency of other source module, an exception is thrown. You can force the uninstall providing the flag `-Pforce=true`.


=== ":material-language-java: Jar Modules"

    You can make use of Gradle exclusion rules to prevent the extraction of a JAR dependency.
    In the `build.gradle` of the root project you can specify the dependency to exclude.

    ``` groovy title="build.gradle"
    configurations.implementation {
      exclude group: 'com.test', module: 'custommodule1'
      exclude group: 'com.test', module: 'custommodule2'
    }
    ```

    If the dependency belongs to a `build.gradl` of a source module, it may be downloaded when the `javaCompile` task is executed. You can also make use of gradle exclude rules.

    !!! warning
        When you make use of exclude rules in a custom source module, the `pom.xml` can be affected when you publish a new version.

    To prevent downloading dinamic JAR modules, you need to remove the dependency from each `build.gradle`.

    The JAR module could also be a transitive dependency.
    You can see the transitive dependencies tree running the gradle task
    `./gradlew dependencies --info`
    and remove the root parent dependency.

    When you declare a dependency you can also exclude custom modules. See [Gradle dependency exclusion](https://docs.gradle.org/current/userguide/dependency_downgrade_and_exclude.html#sec:excluding-transitive-deps){target="_blank"}.

    !!! info
        Etendo JAR modules are dinamically extracted in the root project `build/etendo/modules` directory.

    !!! warning
        Each `build.gradle` file (from the root project or source modules) can be using the dependency directly or by transitivity and this can lead to resolution of the module.

    Finally you need to rebuild the system:

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete
    ```

## Recompile CSS files

### Requirements

  - *Node.js*: Version 16 or higher.
  - *npm*: Node Package Manager.
  - *Sass*: Must have a Sass compiler installed.


??? info "How to install Node.js, npm and Sass"

    === ":simple-linux: Linux"
        
        **Node.js 16.10.0 using NVM:**
        
        1. Install NVM (Node Version Manager):
        ```bash
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
        ```
        Close and reopen your terminal to start using NVM, or execute the following commands:
        ```bash
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
        ```
        
        2. Install Node.js version 16.10.0:
        ```bash
        nvm install 16.10.0
        ```
        
        3. Set Node.js version 16.10.0 as the default version:
        ```bash
        nvm use 16.10.0
        nvm alias default 16.10.0
        ```
        
        4. Verify the installation:
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

The `cssCompile` task in the Etendo Gradle configuration is specifically designed to convert `.scss` files into `.css` files. To customize the Etendo skin, you will need to work with `.scss` files. 

``` bash title="Terminal"
./gradlew cssCompile smartbuild
```


After executing the task, look for the following output to indicate a successful build:
!!! success "Successful Execution"
    After executing the task, the following output indicates a successful build:

    ```
    > Task :cssCompile
    > BUILD SUCCESSFUL
    ```

    This confirms the successful processing of the files.

Finally, restart Tomcat to apply the changes and ensure the updated `.css` files are properly deployed.

## Copilot

- Running the Copilot docker image locally.
    
    ``` bash title="Terminal"
    ./gradlew copilot.start
                                          
    ```

- Stop the Copilot docker image.
    
    ``` bash title="Terminal"
    ./gradlew copilot.stop
                                            
    ```

- Execute Copilot translation Tool with Gradle.

    ``` bash title="Terminal"
    ./gradlew copilot.translate
                                            
    ```

    | Command line parameter                  | Description                                                 |                       
    |  -------------------                   | ------------------------------------                         |
    | `-Parg=<package name>`                 | **Required** Module Javapackage to be translated             |
