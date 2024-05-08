---
Title: Known Issues
tags:
    - Known Issues
    - Solved Issues
    - Pending Issues
---

## Overview
This page displays the known issues reported by the support team.

## Know Issues

??? success "EPL-1449 Solved"

    ### [EPL-1449](https://github.com/etendosoftware/etendo_backups_script/issues/1){target="\_blank"} Gradle loses execution permissions when doing an etendo-restore.

    #### Workaround

    Apply the following change in the etendo-restore file to ensure that the gradlew file is excluded from the permission change with chmod:

    ``` bash title="etendo-restore"
    - find /opt/EtendoERP -type f -exec chmod 644 '{}' \+
    + find /opt/EtendoERP -type f ! -name gradlew -exec chmod 644 '{}' \+
    ```

    This workaround is applicable if you have deployed Etendo from the ISO in versions prior to [24.1.4](https://etendo-appliances.s3.eu-west-1.amazonaws.com/etendo/iso/etendo-24Q1.4.iso). Starting from that version, the issue of permission changes on the gradlew file is no longer observed.

??? success "EE-758 Solved"

    ### [EE-758](https://github.com/etendosoftware/com.etendoerp.financial.extensions/issues/17){target="\_blank"} Incorrect BP Settlement Module Functionality with Payment (In/Out) Combination and Credit Usage.

    #### Attention

    The combination of Payments (In/Out) with credit usage in the Business Partner Settlement module is currently experiencing issues. Incorrect values for amount and credit used may result in financial account discrepancies. We advise against combining credit usage with settlement until this issue is resolved.

??? success "EPL-858 Solved"

    ### [EPL-858](https://github.com/etendosoftware/com.etendoerp.gradleplugin/issues/34){target="\_blank"} Etendo does not compile with latest version of gradle plugin in JAR format.

    #### Workaround

    Before execute setup tasks in a etendo project in JAR format you must follow the next steps:

    On the source path, open `build.gradle` and locate the 'etendo' block in the file. Inside of it, add the following propertie:

    ``` groovy title="build.gradle" 
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
