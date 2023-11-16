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

## Integrating RX with Etendo Sub-Application

After setting up the environment and generating entities with RX, an essential step is integrating these entities with the Etendo Sub-Application. This process involves using the generated TypeScript entities to facilitate interactions between the backend and the frontend of your sub-application.

### Connecting RX with the Sub-App Through Custom Hooks

Custom hooks in **React Native** are powerful tools for encapsulating complex logic. In the context of integrating RX with your sub-application, custom hooks like `useProduct` play a pivotal role. These hooks abstract the complexities of backend interactions, making the frontend code more readable and maintainable.

#### Custom Hook Example: `useProduct`

### Detailed Overview of the `useProduct` Custom Hook

**Description:**
The `useProduct` custom hook epitomizes the integration of frontend React Native components with the backend services in your Etendo Sub-Application. It's meticulously crafted to streamline the process of fetching, creating, and updating product data, while efficiently managing the state of these data within the app. This hook stands as a cornerstone of your application, enabling a seamless and dynamic interaction with the backend.

**Core Functionalities:**

- **Fetching Data with `getFilteredProducts`:** This function is the gateway to retrieving product information from the backend. It executes asynchronous calls, adeptly utilizing `ProductService.BACK.getFilteredProducts` — a method generated by RX. This function is pivotal for obtaining real-time product data, ensuring the app's content is consistently up-to-date.

- **Creating Products:** The `createProduct` function in the hook is specifically tailored for adding new product records to the database. It interfaces directly with the backend, sending requisite data to register new products, thus expanding the app's inventory.

- **Updating Products:** Similarly, the `updateProduct` function is responsible for modifying existing product records. This feature is vital for maintaining the accuracy and relevance of product information in the ever-evolving business landscape.

- **State Management with React's `useState`:** A key aspect of `useProduct` is its state management capability. By leveraging React's `useState`, the hook maintains and updates the product data state within the app. This ensures that any changes in the product data — be it additions, deletions, or modifications — are immediately reflected in the app's user interface, providing a dynamic and responsive user experience.

This comprehensive hook, `useProduct`, encapsulates complex backend interactions and data management strategies, making it an indispensable part of your Etendo Sub-Application's architecture. By abstracting these functionalities, `useProduct` allows for a more streamlined and focused development of the frontend components, aligning closely with modern best practices in app development.

To visually demonstrate the structure and key functions of the `useProduct` hook, the following screenshot is provided. It showcases the carefully organized code that underpins the dynamic data interactions in your application, highlighting the elegance and efficiency of the custom hook implementation.

![search-parameters.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/useProduct-ts.png)

This visual representation offers a clear insight into how the `useProduct` hook is structured and operates, illustrating its role in managing data fetching, creation, updates, and state within the app. It serves as a practical example of how complex backend processes are seamlessly integrated and managed within a React Native application, using custom hooks for optimal performance and maintainability.

### Implementing Frontend Components with RX Entities

#### A Gateway to Product Interaction

**Description:**  
The `Home` component acts as the central interface for users to engage with the product list in your application. It is meticulously designed to not only display products but also to enhance user experience with features like search and navigation. This component is a testament to the effective application of the `useProduct` hook, showcasing how frontend components can seamlessly interact with backend services.

**Key Features:**

  - **Dynamic Data Retrieval:** Employs the `getFilteredProducts` function from the `useProduct` hook to fetch product data, ensuring the displayed list is always current and comprehensive.

  - **Interactive User Experience:** Integrates search and navigation capabilities, allowing users to effortlessly explore and interact with the product list.

#### Streamlining Product Management

**Description:**  
The `ProductDetail` component is a cornerstone of your application, expertly handling the intricacies of product management. This component is where the core functionality of adding new products and editing existing ones comes to life. Through the adept utilization of `createProduct` and `updateProduct` functions from the `useProduct` hook, it bridges the user interface with the backend services efficiently.

**Functionality Highlights:**

  - **Product Creation and Editing:** Facilitates the addition of new product details and the modification of existing ones, thereby playing a vital role in keeping the product catalog relevant and up-to-date.
  
  - **Backend Integration:** Leverages the custom hook `useProduct` for direct and seamless interaction with the backend, ensuring data integrity and consistency.

### Launching Your Sub-App into Action with RX Integration 🚀

With the comprehensive exploration of custom hooks like `useProduct`, and their application in crucial components such as the `Home` and `ProductDetail`, we have navigated through the essential steps of integrating RX with your Etendo Sub-Application. This journey has not only involved understanding the intricate mechanics of data fetching, creation, updating, and state management but also visualizing these processes through practical examples and screenshots.

- **Seamless Backend Communication:** The custom hooks have enabled a fluid and efficient interaction with the backend, abstracting complex processes and making them more accessible and manageable within the React Native framework.
- **User-Centric Component Design:** The `Home` and `ProductDetail` components stand as testaments to a design philosophy that prioritizes user experience, ensuring that navigating and managing products is intuitive and responsive.
- **Visual Clarity:** The inclusion of screenshots has provided a tangible glimpse into the actual implementation, further solidifying the understanding of these concepts.

By adhering to these practices and utilizing the power of custom hooks, your Sub-Application is now well-equipped to handle the demands of a dynamic and data-driven environment. The integration of RX not only propels the application's functionality but also aligns it with best practices in modern app development.