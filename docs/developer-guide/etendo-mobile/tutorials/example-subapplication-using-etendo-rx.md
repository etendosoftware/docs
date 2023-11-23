## Overview

This tutorial provides an extensive, step-by-step guide to help you create a new sub-app from our base project, which can be found on Github as [Subapp Base](https://github.com/etendosoftware/com.etendoerp.subapp.base){target="_blank"}. By following these instructions, you will gain the capability to create a fully functional standalone subapplication, utilizing the power of RX and harnessing the potential of Etendo UI Library components, detailed in our comprehensive guide, installation and usage on the [Storybook](https://develop--649b07373a33e896f7881dd9.chromatic.com/?path=/docs/how-to-install-steps--docs){target="_blank"}. This process not only enables you to develop a unique sub-app but also contributes to the expansion of your application ecosystem by integrating a classic module, thereby enhancing its overall functionality and versatility.

!!! info
    Before starting this tutorial, visit the [Create New Subapplication](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"} tutorial.

## Setup

----------
### Create new Module

Following the documentation about [how to create a new etendo classic module](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/#create-a-new-etendo-classic-module){target="_blank"}, you have to create a new module in the Etendo Classic.

Below is a succinct representation of the required fields and expected values for the module configuration:

| Field                | Value                           |
|----------------------|---------------------------------|
| Java Package         | `com.etendoerp.subapp.product`  |
| Name                 | `Product Subapplication`        |
| Type                 | `Module`                        |
| Description          | `Subapplication to manage products using Etendo RX` |
| Version              | `1.0.0`                         |
| In Development       | `true`                          |
| Is RX                | `true`                          |
| Is React             | `true`                          |
| RX Java Package      | `com.etendoerx.subapp.product`  |
| Translation Required | `true`                          |
| License Type         | `Etendo Commercial License`     |
| Commercial            | `true`                          |

![modules-creation.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/modules-creation.png)

!!! tip
    - Notice that the name can be anything you want, but the type have to be setted as Module.
    - The _description field_ is free and also _required_.

### Dynamic app and role configuration

As the same as the previos section, the dynamic app and role have to be configured following the documentation about the [dynamic app window](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/#dynamic-app-window){target="_blank"}.

#### Dynamic app

The dynamic app in Etendo must contain the following form fields and corresponding values:

| Field               | Value                             |
|---------------------|-----------------------------------|
| Module              | `Product Subapplication - 1.0.0 - English (USA)` |
| Name                | `Product Subapplication`          |
| Directory Location  | `/`                               |
| Name                | `1.0.0`                           |
| File Name           | `productSubapp.js`                |
| Active              | `true`                            |
| Is Development      | `true`                            |

![dynamic-app-creation.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/dynamic-app-creation.png)

#### Role configuration

The next table reflect the settings to be configured for the role in relation to the dynamic app within the Etendo system.

| Field                 | Value                           |
|-----------------------|---------------------------------|
| Organization          | `*`       |
| App                   | `Product Subapplication`        |
| Version               | `1.0.0`                         |
| Active                | `true`                          |

![role-configuration.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/role-configuration.png)

!!! warning "Important"
    Keep this dynamic app as _active_.

At this point you have _done_ with the etendo classic configuration.

## Download the subapplication

This tutorial is based in our example of a product subapplication, which allows to manage products in a list of products (create, edit and delete) using Etendo RX.

!!! tip "Keep in mind"
    All related to the main concepts of a subapplication are explained in the [concepts](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/#concepts){target="_blank"} section in create new subapplication tutorial.
    The following sections are focused on the product subapplication example.

To begin with we must have to download the [ latest version of the project](https://github.com/etendosoftware/subapp-product/releases){target="_blank"} inside the `modules/<javapackage>` folder in the Etendo environment. Then unzip the file and the folder must look like this:

![repository-cloned.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/repository-cloned.png)

!!! warning "Important"
    Whole process to run a subapp in _developer mode_ among with etendo classic and etendo mobile is detailed in [Create New Subapplication](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"}

## Customizing and Programming a Sub-Application

This section explains how to customize and program a subapplication. It uses as an example the [Product Subapplication](https://github.com/etendosoftware/subapp-product/releases/){target="_blank"} .

### Product subapp example

This section covers an overview about the product subapplication example screens and principal parts of the subapplication where covered in [Create New Subapplication](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/){target="_blank"}.

!!! info "Consideration"
    This subapplication example was developed for both platforms (phone and tablet). 
    When you create a new subapplication, you have to do the same. 
    The provided [base subapplication](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"}  is already configured for both platforms.

#### Home
  - This is the main screen of the subapplication. It will show a list of products. Also, it will allow us to edit and remove a product, find a product by name and navigate to the detail of a product.
  - The route to this screen is `src/screens/home/index.tsx`.
    <figure markdown>
      ![home-screen.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/home-screen.png){ width="300", align=left } 
      ![remove-product.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/remove-product.png){ width="300", align=right}
    </figure>
    _Tablet version_
    ![home-screen-tablet.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/home-screen-tablet.png)

#### ProductDetail
  - This screen will show the detail of a product. Also, it will allow us to edit the product.
  - It's the same screen used to create a new product. there is a flag to know if the product is new or not (productItem).
  - The route to this screen is `src/screens/productDetail/index.tsx`.
    <figure markdown>
      ![add-product.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/add-product.png){ width="300", align=left } 
      ![edit-product.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/edit-product.png){ width="300", align=right}
    </figure>
    _Tablet version_
    ![add-product-tablet.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/add-product-tablet.png)

# Projections, Repository and Search
!!! info
    In this section we will explain how to configure the projections, repository and search needed in this example. For more info visit [Projections, Repository And Search](/developer-guide/etendo-rx/concepts/projections){target="_blank"}  official documentation. 

## Create a projection

It is required to create projections that reflect partial views of the root class and contain only the necessary properties.
To do this we will go to the `Projections` window and create a projection with the following properties:


  | Field       | Value                                               |
  | ----------- | ----------------------------------------------------|
  | Module      |`Subapp Product Module - 1.0.0 - English (USA)`      |
  | Name        |`ProdSubApp`                                         |
  | Description |`-`                                                  |


  ![projection.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/projection.png)


### Adding the projection to a table

As we have created the projection, we now have to assign it to a table from which we want to extract data. To do this, we open the Tables and Columns window and look for the `M_Product` table.

Next, navigate to the *Projections* tab and add a new projection with the following value:

  | Field      | Value                                          |
  | ---------- | ---------------------------------------------- |
  | Projection |`ProdSubApp - Subapp Product Module - 1.0.0` |


  ![assign-projection.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/assign-projection.png)



### Adding entity fields

Once we have the projection, we must define which fields we want to retrieve.
For it in the Tables and columns window we look for the table M_Product and in the Projection tab navigate to the Entity Field tab and add the following fields:

| Name                |  Property             |
| ------------------- | --------------------- |
| id                  |`id`                   |
| name                |`name`                 |
| productCategory     |`productCategory`      |
| uPCEAN              |`uPCEAN`               |

  ![entity-fields.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/entity-field.png)


## Create a New Repository

Now to interact with a data warehouse we have to create a repository in the Tables and Columns window select the table `M_Product`, go to the `Repository` tab and create a new record with the following values:

| Field       | Value                                             |
| ----------- | --------------------------------------------------|
| Module      |`Subapp Product Module - 1.0.0 - English (USA)`    |


  ![repository.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/repository.png)

## Create a New Search

Next we will define a search method to be used later when we want to consume the products. To create this new filter/search method, in the Repository tab of the `M_Product` table, create a new record with the following data:

| Field       | Value                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------ |
| Method Name |`getFilteredProducts`                                                                             |
|  Query      |`SELECT e FROM Product e WHERE (e.active = true) AND (lower(e.name) LIKE lower('%' || :name || '%') OR lower(e.uPCEAN) LIKE lower('%' || :name || '%')) order by e.updated desc`   |


  ![search.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/search.png)

### Creating a New Search Parameter

  To define the parameter we defined in the previous query we need to create a new row in the Search Parameter tab and add the following record:

| Field | Value         |
| ----- | ------------- |
| Line  |`10`           |
| Name  |`name`         |
| Type  |`String`       |


  ![search-parameters.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/search-parameters.png)


### Setting up the Development Environment

Before customizing and programming your sub-application, ensure your development environment is properly set up. The following steps detail how to do this:

1. **Create a Java Package:** 
   Create a Java package in the `modules_rx` directory of your Etendo environment. This package should match the Etendo RX Java package created in Etendo Classic for your sub-application. For instance, if you're developing a product sub-application, you could create a package like `com.etendorx.subapp.product`.

2. **Generate Entities Using Etendo RX:**
   Use Etendo RX to generate entities for your sub-application's data structure. Run the command `./gradlew rx:generate.entities` in the root of your Etendo environment. This generates essential directories and files like `lib`, `src-db`, and `src-gen` in your Java package.
   
    Run the following command in the root of your Etendo environment:

    ```bash title="Terminal"
    ./gradlew rx:generate.entities
    ```

    In turn, this command will initiate the Etendo RX's entity generation process.
    
    ![generate-entities.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/modules-rx.png)

    Verify the completion of this process and the accurate creation of all essential files and directories.

3. **Migrate the 'lib' Directory:**
    Move the `lib` directory from `modules_rx/<RXJavapackage>/lib` to `modules/<javapakage>/<subapp-name>/lib`. In our particular example, from the root of your Etendo environment, execute the following command to move the `lib` folder:

    ```bash title="Terminal"
    mv modules_rx/com.etendorx.subapp.product/lib/ modules/com.etendoerp.subapp.product/subapp-product/
    ```

    ![generate-entities.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/lib-inside-modules.png)

    Completing this step ensures that the libraries are correctly placed in the project, promoting efficient integration of your sub-application.

    !!! warning "Important"
        Consider moving the generated files and directories to the location described in the previous step after each execution of `./gradlew rx:generate.entities`. Otherwise, your sub-application may work incorrectly. It is strongly recommended to check and confirm the location of these files after each entity generation.

  4. **Restart the Etendo RX Service:**
    After successfully migrating the `lib` directory, restart the Etendo RX service to recognize the new changes. To do this, first stop the currently running Etendo RX service, and then restart it using the following command from the root of your Etendo environment:

    ```bash title="Terminal"
    ./gradlew rx:rx
    ```

    Executing this command will relaunch the Etendo RX service with the newly integrated libraries and configurations.

# Integrating Etendo RX with Etendo Sub-Application

This section details the integration of Etendo RX generated TypeScript entities with the Etendo Sub-Application, focusing on backend-frontend interactions.

### Custom Hooks in React Native

Custom hooks are a fundamental aspect of React Native, offering a modular approach to managing logic in applications. These hooks allow for creating, updating, and deleting functionalities, and are instrumental in abstracting complex interactions with the backend, thereby enhancing code maintainability and readability.

#### Overview of Custom Hooks

Custom hooks, such as `useProduct`, exemplify the integration between frontend components and backend services.

### Implementing Custom Hooks

Here's an example of how custom hooks are utilized:

```typescript title="useProduct.ts"
import { useState, useEffect } from 'react';
import { Product } from '../../lib/data_gen/product.types';
import ProductService from '../../lib/data_gen/productservice';

// Custom hook for managing products
export const useProduct = () => {
  const [products, setProducts] = useState<Product[]>([]);

  // Fetching data
  useEffect(() => {
    const fetchData = async () => {
      const data = await ProductService.BACK.getFilteredProducts();
      setProducts(data);
    };
    fetchData();
  }, []);

  // Function to handle product update
  const handleUpdateProduct = async (updatedProduct: Product) => {
    await ProductService.BACK.updateProduct(updatedProduct);
    // Optionally, update the products state to reflect the changes
  };

  // Function to get filtered products (if needed)
  const getFilteredProducts = async (filterCriteria: any) => {
    const filteredProducts = await ProductService.BACK.getFilteredProducts(filterCriteria);
    setFilteredProducts(filtered);
    return filteredProducts; // This line is optional, allowing the function to return the filtered products
  };

  return {
    products,
    handleUpdateProduct,
    getFilteredProducts,
  };
};
```

## Implementing `useProduct` Hook in `Home` Component

The `Home` component serves as the central hub for product management within our React Native application. It leverages the `useProduct` hook to interact with product data. This custom hook provides functions to retrieve and update products, which the `Home` component uses to maintain its state and UI.

The `Home` component serves as a central hub for product management within our React Native application, which allows interacting with product data. The `useProduct` custom hook provides functions for retrieving and updating products, which the `Home` component uses to maintain its state and user interface.

### Structure of `Home.tsx`

- **Imports and State Initialization**: The component begins by importing necessary React hooks and the custom hook `useProduct`. It initializes the `products` state to an empty array to hold the product data.

- **Data Fetching with useEffect**: Upon mounting, the `useEffect` hook calls `getFilteredProducts` to fetch product data from the backend and populate the `products` state.

- **Product Update Function**: `handleProductUpdate` is an asynchronous function provided to update an existing product using `updateProduct` from the `useProduct` hook.

- **User interface composition**: The component returns the user interface built using the `Etendo UI library`, which includes the `Table` component that displays the list of products.

### Example Usage

```typescript title="Home.tsx"
import React, { useEffect, useState } from 'react';
import { View } from 'react-native';
import useProduct from '../../hooks/useProduct';
import Table from '../../components/Table';

const Home = () => {
  const { getFilteredProducts, updateProduct } = useProduct();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    (async () => {
      const fetchedProducts = await getFilteredProducts();
      setProducts(fetchedProducts);
    })();
  }, []);

  return (
    <View>
      <Table data={products} />
    </View>
  );
};

export default Home;
```

Based on this, the `Home` component is presented as an efficient product data manager, highlighting the main actions of obtaining and visualizing products, presenting a sub-application design and allowing real-time updates and fluid interactions with the user.

### Conclusion

The integration of Etendo RX with Etendo Sub-Applications using custom hooks like `useProduct` enhances the development process and the user experience. It provides a seamless connection between backend services and a React Native frontend

In the `Home.tsx` component, we observed the practical application of these hooks, which resulted in a dynamic, responsive, and user-friendly interface. This approach not only streamlines the development process but also ensures that the code remains maintainable and readable.

While the example focused on listing products using a table, it's important to note that the distributed code includes additional functionalities. These include **editing**, **adding**, and **deleting** products, further demonstrating the versatility and comprehensive nature of the `useProduct` hook within the application.

Attached below is an example of **F&B International Group's products**, obtained through Etendo RX, demonstrating the efficiency between backend and frontend operations in a practical sub-application context.

![generate-entities.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/home-subapp-product.png)

In essence, this integration is a significant stride in creating robust, scalable, and intuitive mobile applications within the Etendo ecosystem.