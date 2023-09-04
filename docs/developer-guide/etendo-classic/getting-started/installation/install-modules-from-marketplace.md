---
title: Install Modules
---
## Install Modules

This section provides a step by step explanation on how to Install modules from Etendo Marketplace.

![](/docs/assets/drive/LWaskO0G5UdmwGWdwZy5nHf4FcCTMBcgObbWv_PSjtMPCOAeqBPNSoLKrqheTLiNqc_aiqbVrJYYJlCQ_o7rGGofcqN0-myRi3u3YpXYNuVt1FYIli0RbiWYD8hYGcDLMpRYVS_dHOGGOLY117nmB2o.png)

1.  First, go to [Etendo Marketplace](http://marketplace.etendo.cloud){target="_blank"}.
2.  Browse or search for the module that you want to install.
3.  Click on the module to see its details, such as the version, description, and compatibility with different platforms and applications.
4.  Check the requirements for the module, such as any dependencies or system configurations needed to run the module.
5.  Select the format for the installation of the module, Source or JAR, and copy the corresponding dependency.
6.  Go to the `build.gradle` file and paste the dependency in the dependencies section.
7. 
    === "**Source Format**"
        To work with sources, you have to expand modules tasks available.  
        
        ``` bash title="Terminal" 
        ./gradlew expandModules
        ```  
        
        This task will try to download and install the added module.   
        A menu will be displayed showing the modules that will be expanded, you have to confirm manually to continue with the expansion.  
        
    === "**JAR Format**"  
        To work with JAR modules, you need to resolve the dependencies running

        ``` bash title="Terminal"  
        ./gradlew dependencies
        ```

    !!! info
        Remember to configure the credentials in `gradle.properties` file

8. Finally, install or update the database with the new modules 
    ``` bash title="Terminal" 
    ./gradlew smartbuild -Dlocal=no
    ```
9. Verify that the module is installed correctly by checking that its functions or features are available in the application or platform where you want to use it.