## Overview

This section provides a step-by-step guide on how to create a new sub-application to work with Etendo RX, which involves creating a new module with RX capabilities and building a React-native project to consume commands making use of projections, repository and other resources that we will create in our Etendo Classic.

## Building a New Module for RX Capabilities

!!! info
    Make sure to complete the [Getting Started section in Etendo Mobile](/developer-guide/etendo-mobile/getting-started.md) to set up the Etendo Platform.


### Accessing as Admin User

After setting the local environment up, as described in the [**install etendo development environment**](/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment), we will need to log in to the system with administration permissions to create the new module, projections, repository, etc.

Log in to your account as an administrator. The default login credentials for this administrative account are:

- Username: `admin`
- Password: `admin`

Once you are logged in, switch your role to *System Administrator*, as the image shows:

  ![switch-admin.png](/assets/developer-guide/etendo-mobile/tutorials/system-etendo-mobile-products.png)

### Creating a New Module

Now we will create a new module for the sub-application. To create a new module, go to the Module window, and add a new record by providing the following information:

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

### Creating a New Projection


Creates a projection by adding the name of the module created and the name of the projection.

| Parameter       | Value                                 |
| --------------- | ------------------------------------- |
| Module          |`Products - 1.0.0 - English (USA)`     |
| Name            |`Tutorial`                             |

It should look like this:

  ![new-projection.png](/assets/developer-guide/etendo-mobile/tutorials/projection-etendo-mobile-products.png)



  ![new-projection.png](/assets/developer-guide/etendo-mobile/tutorials/table-and-column-etendo-mobile-product.jpg)
  
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

  