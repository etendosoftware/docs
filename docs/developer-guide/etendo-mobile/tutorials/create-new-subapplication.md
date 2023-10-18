## Overview

This section provides a step-by-step guide on how to run a sub-app in developer mode to work with Etendo. This requires that your project has dependencies installed so that you can generate a bundle of it, be able to set it as developer mode and start incorporating this sub-app into Etendo Mobile. 

!!! info
    Before starting this tutorial you must have Etendo, Etendo Mobile and Node.js in your environment. For more information check the [Getting Started in the Etendo Mobile section](/developer-guide/etendo-mobile/getting-started/)

## Fork the dummy application

To begin with we must make a fork of our dummy application com.etendoerp.subapp.base https://github.com/etendosoftware/com.etendoerp.subapp.base and clone it inside the modules folder in our Etendo environment.

![modules.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/modules.png)

## Configuring the Etendo

Log in to your account as an administrator. The default login credentials for this administrative account are:

    Username: admin
    Password: admin

Once you are logged in, switch your role to Admin, as the image shows:

![admin.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/admin.png)


Enter the Dynamic App tab, find the name Subapp Example, select it and in the lower tab under DYNAMIC APP VERSION add a record with the version name, the application bundle name and set Is Development to true.

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Name`                  | Version name                                                     | dev                                    | 
| `File Name`             | Bundle name                                                      | subappexample.js                       |
| `Version`               | Version number                                                   | 1.0.0                                  |
| `Active`                | If active                                                        | true                                   |
| `Is Development`        | Is the development mode                                          | true                                   |

![admin.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/dynamicapp-version.png)

Enter the Role tab, filter by the name F&B International Group Admin, select it and at the bottom select the DYNAMIC APPS - Subapp tab in which you must add the example record Subapp Example with version 1.0.0.  

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Organization`          | Name of organization                                             | *                                      | 
| `App`                   | Name of application                                              | Subapp Example                         |
| `Version`               | Version number                                                   | 1.0.0                                  |
| `Active`                | If active                                                        | true                                   |

![admin.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/role-dynamicapp.png)

Finally open in a terminal in modules/com.etendoerp.subapp.base/resources and execute the following command

1. Install the dependencies 
    ``` bash title="Terminal"
    yarn install 
    ```
2. Run in development mode
    ``` bash title="Terminal"
    yarn dev 
    ```