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

### Setting up the Development Environment

Before diving into the customization and programming of your sub-application, ensure your development environment is correctly set up:

1. **Create a Java Package:** 
   In the `modules_rx` directory of your Etendo environment, create a Java package specific to your sub-application. For instance, in the case of a product sub-application, you might create a package named `com.etendorx.subapp.product`. This package will house the custom codes and functionalities specific to your sub-application.

2. **Generate Entities Using RX:**
   After setting up your Java package, you need to generate entities which will form the foundation of your sub-application's data structure. Run the following command in the root of your Etendo environment:

   ```bash
   ./gradlew rx:generate.entities
   ```

   This command will initiate the Etendo RX's entity generation process. It will create essential directories and files such as `lib`, `src-db`, and `src-gen` within your Java package. These directories contain the libraries, database scripts, and generated source code crucial for your sub-application's operation.

   ![generate-entities.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/modules-rx.png)

   Ensure that this process completes successfully and that all necessary files and directories are correctly generated. Then, with your Java package set up and entities generated, you can now proceed to customize and program your sub-application as detailed in the subsequent sections.

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
|  Query      |`select e from Product e where e.active = true and e.name like :name or e.uPCEAN like :barcode`   |


  ![search.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/search.png)

### Creating a New Search Parameter

  To define the parameters we defined in the previous query we need to create a new row in the Search Parameter tab and add the following records:

| Field | Value         |
| ----- | ------------- |
| Line  |`20`           |
| Name  |`barcode`      |
| Type  |`String`       |

| Field | Value         |
| ----- | ------------- |
| Line  |`10`           |
| Name  |`name`         |
| Type  |`String`       |


  ![search-parameters.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/search-parameters.png)


  Finally, launch this command in the root of the environment to generate the entities: 

  ``` bash title="Terminal"
  ./gradlew rx:generate.entities
  ```

  It should generate the following files:

  ![search-parameters.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/generate-entities.png)

# Integrating RX with Etendo Sub-Application

This section outlines the integration of RX-generated TypeScript entities with the Etendo Sub-Application, focusing on backend-frontend interactions.

### Custom Hooks in React Native

Custom hooks are a fundamental aspect of React Native, offering a modular approach to managing logic in applications. These hooks allow for creating, updating, and deleting functionalities, and are instrumental in abstracting complex interactions with the backend, thereby enhancing code maintainability and readability.

#### Overview of Custom Hooks

Custom hooks, such as `useProduct`, exemplify the integration between frontend components and backend services. These hooks simplify complex data operations like fetching, creating, and updating information. They effectively manage the application's state, ensuring dynamic interaction with backend systems.

### Implementing Custom Hooks

Here's an example of how custom hooks are utilized:

```typescript
// Example usage of a custom hook in a React Native component
const [products, setProducts] = useProduct();

// Fetching data
useEffect(() => {
  const fetchData = async () => {
    const data = await getFilteredProducts();
    setProducts(data);
  };
  fetchData();
}, []);

// Function to handle product creation
const handleCreateProduct = async (product) => {
  await createProduct(product);
  // Update state accordingly
};

// Function to handle product update
const handleUpdateProduct = async (product) => {
  await updateProduct(product);
  // Update state accordingly
};
```

### Launching Your Sub-App into Action with RX Integration

Integrating RX with your Etendo Sub-Application involves leveraging custom hooks for efficient backend communication and user-centric component design. These practices ensure a dynamic, responsive, and well-structured application, aligning with modern development standards.