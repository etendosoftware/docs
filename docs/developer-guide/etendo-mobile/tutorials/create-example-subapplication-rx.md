## Overview

This tutorial provides an extensive, step-by-step guide to help you create a new sub-app from our base project, which can be found on Github as [Subapp Base](https://github.com/etendosoftware/com.etendoerp.subapp.base){target="_blank"}. By following these instructions, you will gain the capability to create a fully functional standalone subapplication, utilizing the power of RX and harnessing the potential of Etendo UI Library components, detailed in our comprehensive guide, installation and usage on the [Storybook](https://develop--649b07373a33e896f7881dd9.chromatic.com/?path=/docs/how-to-install-steps--docs){target="_blank"}. This process not only enables you to develop a unique sub-app but also contributes to the expansion of your application ecosystem by integrating a classic module, thereby enhancing its overall functionality and versatility.

!!! info
    Before starting this tutorial must have done in [Create New Subapplication](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"} tutorial.

## Setup

----------
### Create new Module

Following the documentation about [how to create a new etendo classic module](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/#create-a-new-etendo-classic-module){target="_blank"}, you have to create a new module in the etendo classic and it have to look like this:

![modules-creation.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/modules-creation.png)

!!! tip
    - Notice that the name can be anything you want, but the type have to be setted as Module.
    - The _description field_ is free and also _required_.

### Dynamic app and role configuration

As the same as the previos section, the dynamic app and role have to be configured following the documentation about the [dynamic app window](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/#dynamic-app-window){target="_blank"}.

#### Dynamic app

The dynamic app in Etendo must be like this:

![dynamic-app-creation.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/dynamic-app-creation.png)

#### Role configuration

The role configured in Etendo must be like this:

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
  | Projection |`rxtutorial - tutorial - 1.0.0 - English (USA)` |


  ![assign-projection.png](/assets/developer-guide/etendo-rx/tutorial/assign-projection.png)



### Adding entity fields

Once we have the projection, we must define which fields we want to retrieve.
For it in the Tables and columns window we look for the table M_Product and in the Projection tab navigate to the Entity Field tab and add the following fields:

|  Field Name         |  Property             |
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

Before diving into the customization and programming of your sub-application, ensure your development environment is correctly set up:

1. **Create a Java Package:** 
   Within the `modules_rx` directory of your Etendo environment, establish a Java package tailored to your sub-application. This package should correspond to the Etendo RX Java package generated in the Etendo Classic for your specific sub-application. For example, if you're working on a product sub-application, you might create a package named `com.etendorx.subapp.product`. This package will be the repository for all the custom code and unique functionalities of your sub-application.

2. **Generate Entities Using Etendo RX:**
   After setting up your Java package, you need to generate entities which will form the foundation of your sub-application's data structure. When we generate the entities, Etendo RX embarks on a comprehensive entity generation process. During this process, it produces React code, which is then utilized as a library. This library acts as a crucial link between the application's frontend and backend, facilitating seamless data exchange and interaction among various system components.
   
    Run the following command in the root of your Etendo environment:

    ```bash title="Terminal"
    ./gradlew rx:generate.entities
    ```

    In turn, this command will initiate the Etendo RX's entity generation process. It will create essential directories and files such as `lib`, `src-db`, and `src-gen` within your Java package. These directories contain the libraries, database scripts, and generated source code crucial for your sub-application's operation.

    ![generate-entities.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/modules-rx.png)

    Verify the completion of this process and the accurate creation of all essential files and directories.

3. **Migrate the 'lib' Directory:**
    After generating entities, it is crucial to relocate the `lib` directory inside the directory of the created sub-application. Move the `lib` folder from `modules_rx/<RXJavapackage>/lib` to `modules/<javapackage>`. In our particular example, from the root of your Etendo environment, execute the following command to move the `lib` folder:

    ```bash title="Terminal"
    mv modules_rx/com.etendorx.subapp.product/lib modules/com.etendoerp.subapp.product/subapp-product
    ```

    ![generate-entities.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/lib-inside-modules.png)

    Completing this step ensures that the libraries are correctly placed in the project, promoting efficient integration of your sub-application.

  4. **Restart the Etendo RX Service:**
    After successfully migrating the `lib` directory, the next crucial step is to restart the Etendo RX service to recognize the new changes. To do this, first stop the currently running Etendo RX service, and then restart it using the following command from the root of your Etendo environment:

    ```bash title="Terminal"
    ./gradlew rx:rx --info
    ```

    Executing this command will relaunch the Etendo RX service with the newly integrated libraries and configurations.

# Integrating Etendo RX with Etendo Sub-Application

This section outlines the integration of Etendo RX generated TypeScript entities with the Etendo Sub-Application, focusing on backend-frontend interactions.

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

  // Function to handle product creation with default values
  const handleCreateProduct = async (product?: Partial<Product>) => {
    const defaultValues: Product = {
      active: true,
      description: 'default',
      name: body.name,
      organization: '/B843C30461EA4501935CB1D125C9C25A',
      productCategory: '/DC7F246D248B4C54BFC5744D5C27704F',
      productType: 'I',
      productValue: 'default',
      searchKey: `ES/00${generateRandomNumber()}`,
      uPCEAN: body.uPCEAN,
      taxCategory: '/E020A69A1E784DC39BE57C41D6D5DB4E',
      uOM: '/100',
    };

    await ProductService.BACK.createProduct(defaultValues);
    // Optionally, update the products state to include the new product
  };

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
    handleCreateProduct,
    handleUpdateProduct,
    getFilteredProducts,
  };
};
```

Now, to demonstrate the use of the `useProduct` custom hook in a React Native component like `home.tsx`, let's expand on the example with a practical implementation. This implementation will illustrate how the custom hook can be integrated into a component to manage product data effectively.

```typescript title="Home.tsx"
import React, { useEffect, useState } from 'react';
import { View, Text } from 'react-native';
import useProduct from '../../hooks/useProduct';

const Home = () => {
  // Use the custom hook to manage product data
  const { getFilteredProducts, createProduct, updateProduct } = useProduct();
  const [products, setProducts] = useState([]);

  // Fetch products when the component mounts
  useEffect(() => {
    const fetchProducts = async () => {
      const fetchedProducts = await getFilteredProducts();
      setProducts(fetchedProducts);
    };

    fetchProducts();
  }, []);

  // Function to add a new product
  const handleAddProduct = async (newProduct) => {
    await createProduct(newProduct);
    // Optionally refetch or update products list
  };

  // Function to update an existing product
  const handleProductUpdate = async (updatedProduct) => {
    await updateProduct(updatedProduct);
    // Optionally refetch or update products list
  };

  // Render the component
  return (
    <View>
      {/* Render Table with products */}
      <Table navigation={navigation} data={products} />
      {/* Additional UI components for adding/updating products */}
    </View>
  );
};

export default Home;
```

### Conclusion

The integration of Etendo RX with Etendo Sub-Applications, leveraging custom hooks like `useProduct`, exemplifies the efficiency and power of modern application development. It showcases the seamless connection between backend services and a React Native frontend, significantly enhancing both the development process and the end-user experience.

In the `Home.tsx` component, we observed the practical application of these hooks, which resulted in a dynamic, responsive, and user-friendly interface. This approach not only streamlines the development process but also ensures that the code remains maintainable and readable.

While the example focused on listing products using a table, it's important to note that the distributed code includes additional functionalities. These include **editing**, **adding**, and **deleting** products, further demonstrating the versatility and comprehensive nature of the `useProduct` hook within the application.

A visual representation, such as a screenshot of the Home screen displaying products from F&B International Group fetched via Etendo RX, would vividly illustrate this successful integration. This would highlight the effective and seamless connection between backend and frontend operations in a real-world application scenario.

![generate-entities.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/home-subapp-product.png)

In essence, this integration is a significant stride in creating robust, scalable, and intuitive mobile applications within the Etendo ecosystem.