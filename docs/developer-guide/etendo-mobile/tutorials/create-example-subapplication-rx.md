## Overview

This tutorial provides an extensive, step-by-step guide to help you create a new sub-app from our base project, which can be found on Github as [Subapp Base](https://github.com/etendosoftware/com.etendoerp.subapp.base){target="_blank"}. By following these instructions, you will gain the capability to create a fully functional standalone sub-application, utilizing the power of RX and harnessing the potential of Etendo UI Library components, detailed in our comprehensive guide, installation and usage on the [Storybook](https://develop--649b07373a33e896f7881dd9.chromatic.com/?path=/docs/how-to-install-steps--docs){target="_blank"}. This process not only enables you to develop a unique sub-app but also contributes to the expansion of your application ecosystem by integrating a classic module, thereby enhancing its overall functionality and versatility.

!!! info
    Before starting this tutorial must have done in [Create New Sub-application](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"} tutorial.

## Configuration of Etendo classic

----------
### Module and export database

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

## Download the sub-application

This tutorial is based in our example of a product sub-application, which allows to manage the products of a company. This sub-application will have a list of products, a form to create, edit and a delete product.

!!! tip "Keep in mind"
    All related to the main concepts of a sub-application are explained in the [concepts](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/#concepts){target="_blank"} section in create new sub-application tutorial.
    The following sections are focused on the product sub-application example.

To begin with we must have to download the [ latest version of the project](https://github.com/etendosoftware/subapp-product/releases){target="_blank"} inside the `modules_rx` folder in our Etendo environment. Then unzip the file and the folder must look like this:

![repository-cloned.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/repository-cloned.png)

!!! warning "Important"
    Whole process to run a subapp in _developer mode_ among with etendo classic and etendo mobile is detailed in this link [here](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"}

## Customizing and Programming a Sub-Application

This section explains how to customize and program a sub-application. It uses as an example our [product sub-application](https://github.com/etendosoftware/subapp-product/releases/){target="_blank"} .

### Product subapp example

Here you going to read an overview about the product sub-application example screens and principal parts of the sub-application where covered in [create new sub-application](/developer-guide/etendo-mobile/tutorials/create-new-subapplication/){target="_blank"}.

!!! info "Consideration"
    This sub-application example was developed for both platforms (phone and tablet). 
    When you create a new sub-application, you have to develop it for both platforms (phone and tablet). 
    The provided [base subapplication](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"}  is already configured for both platforms.


#### Home
  - This is the main screen of the sub-application. It will show a list of products. Also, it will allow us to edit and remove a product, find a product by name and navigate to the detail of a product.
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

