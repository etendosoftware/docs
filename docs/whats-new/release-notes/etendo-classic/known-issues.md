---
Title: Known Issues
tags:
    - Known Issues
---


### [EPL-858](https://github.com/etendosoftware/etendo_core/issues/221){target="\_blank"} Etendo does not compile with latest version of gradle plugin in JAR format.
??? example "Workaround"


    Before execute setup tasks in a etendo project in JAR format you must follow the next steps:

    On the source path, open `build.gradle` and locate the 'etendo' block in the file. Inside of it, add the following propertie:

    ``` groovy title="build.gradlew" 
    etendo {
        ignoreCoreJarDependency = true
    }
    ```

    This configuration will allow you to download the source of the project on your local environment. It will be needed for following steps. 

    Now we need to execute the command that will download the source code:

    ```bash title='terminal'
    ./gradlew clean
    ./gradlew expandCore 
    ```
    If you don't want to change the `build.gradle`, you can execute the command `./gradlew expandCore` and add the flag `-PforceExpand=true` at the end of it
  
