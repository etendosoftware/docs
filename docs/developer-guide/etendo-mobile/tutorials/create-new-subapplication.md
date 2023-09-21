
## Requirements

To start with this tutorial you should have *Etendo Classic* up locally, our Etendo Mobile container application, Node in version 16.10.0 and a package manager for JavaScript code such as Yarn.

Also our Platform Extensions Bundle which includes enhancements for platform functionality in Etendo.

!!!note
    If you do not have these requirements you can follow the [Getting Started section in the Etendo Mobile](/developer-guide/etendo-mobile/getting-started/) and [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614) (For more information see [Platform Extensions Bundle section in the Bunldes](/developer-guide/etendo-classic/bundles/platform-extensions-bundle/)) to continue with this tutorial.
    
## Overview

This section provides a step-by-step guide on how to create a new sub-application to work with Etendo RX, which involves creating a new module with RX capabilities and building a React-native project to consume commands making use of projections, repository and other resources that we will create in our Etendo Classic.

## Building a New Module for RX Capabilities

!!!note
    Make sure to complete the [Getting Started section in the developer guide](/developer-guide/etendo-rx/getting-started) to set up the Etendo Platform.


### Accessing as Admin User

After setting the local environment up, as described in the [**install etendo development environment**](/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment), we will need to log in to the system with administration permissions to create the new module, projections, repository, etc.

Log in to your account as an administrator. The default login credentials for this administrative account are:

- Username: `admin`
- Password: `admin`

Once you are logged in, switch your role to *System Administrator*, as the image shows:

  ![switch-admin.png](/assets/developer-guide/etendo-rx/tutorial/switch-admin.png)


The *System Administrator* role allows us to access some windows and permission to create and manipulate the system to fulfill our needs.

### Creating a New Module

Now we will create a new module. It is a self-contained unit of code that performs a specific function and, in our case, it contains all the resources needed in this guide.
To create a new module, go to the Module window, and add a new record providing the following information:

| Parameter       | Value                                 |
| --------------- | ------------------------------------- |
| Java Package    |`com.etendomobile.products`            |
| Name            |`Tutorial`                             |
| Description     |`example sub-application to read, filter,crate, edit or delete products` |
| Version         |`1.0.0`                                |
| Is RX           |`True`                                 |
| Is React        |`True`                                 |
| Rx Java Package |`com.etendomobilerx.products`          |
| Author          |`Etendo Software`                      |

It should look like this:

  ![new-module.png](/assets/developer-guide/etendo-mobile/tutorials/module-etendo-mobile-products.png)


With our new module created, we will start working by exporting the database and generating the entities as follows.

------------------------------------------------------------------

1. Export the database to *Etendo Classic*..

  ``` bash title="Terminal"
  ./gradlew export.database
  ```

2. Generate the entities in our subapplication.

``` bash title="Terminal"
./gradlew rx:generate.entities --info
```

  