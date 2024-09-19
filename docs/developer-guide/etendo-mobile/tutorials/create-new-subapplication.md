---

tags:
    - Etendo Mobile
    - Etendo RX
    - Dynamic App Configuration
    - Subapp
---

# Create New Subapplication

## Overview

This tutorial provides a step-by-step guide to creating a new sub-application within **Etendo Mobile**. By following these instructions, you will learn how to fully utilize the capabilities of **Etendo RX** and leverage the visual components available in the **Etendo UI Library** to build a functional sub-application.

The tutorial will guide you through the creation of the *Product Subapp*, a simple application that enables the addition, deletion, and modification of products, as well as their visualization in a grid. Upon completion, you will have the skills to create and distribute sub-applications as modules, thereby extending the mobile functionality of Etendo.


!!! info
    Before beginning, ensure that your local environment meets all necessary requirements by reviewing the Etendo Mobile [Getting Started](../getting-started.md) section.


## Module Setup 

### Create New Etendo Classic Module

:material-menu: `Application` > `Application Dictionary` > `Module`

1. As a System Administrator role, open the **Module** window and create a new register. This module will be used to develop and distribute the application.

    <figure markdown="span">
    ![modules-creation.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-example-subapplication/modules-creation.png)
    <figcaption>Product Subapp module configuration example</figcaption>
    </figure>

    !!! tip
        - Notice that the name can be anything you want, but the type has to be setted as Module.
        - The _description field_ is free and also _required_.
        - In this case, start from `1.0.0` module version and set the DB Prefix as `ETSAPPP`.


### Dynamic App configuration

:material-menu: `Application` > `General Setup` > `Application` > `Dynamic App`

Configure and export dynamic applications in Etendo Classic, which are displayed dynamically in Etendo Mobile.

In the **Dynamic App** window, specify the paths and versions for each subapplication. These settings determine how subapplications are displayed when users log into Etendo Mobile.

For the example we are following, the Dynamic App in Etendo must be configured with the following form fields and corresponding values:

![](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/dynamic-app-creation.png)

Fields to note:

- **Module**: The module that can export the window configuration, in the example **Product SubApp**.
- **Name**: Name with the application will be shown.
- **Directory Location**: The path where the compiled application bundle is located. In development, the path is empty, but in production, the path is `/<javapackage>/web/`.
- **Active**: To select if this application is active or not.


The **Dynamic App Version** tab allows the application to be versioned, enabling both development and production versions.

Fields to note:

- **Name**: Name of the application version E.g. `dev` or `1.0.0`.
- **File Name**: The bundle name of the compiled application, by default `dist.js`.
- **Default**: This check defines that this version is productive.
- **Is Development**: This check defines that this version is in development and can be deployed locally.
- **Active**: To select if this application version is active or not.


### Role configuration
:material-menu: `Application` > `General Setup` > `Security` > `Role`

Logged in as the **Group Admin** role (which is the default role for accessing Etendo Mobile in our example), the settings are applied as specified below.

![role-configuration.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-example-subapplication/role-configuration.png)

!!! warning "Important"
    Keep this dynamic app as _active_.

!!!info
    At this point, you have done with the Product Subapplication configuration.

### Export the Module

1. After saving all the configuration, you have to export the changes. Open a terminal in the root of your **Etendo Classic** project and execute the following command:
    
    ``` bash title="Terminal"
    ./gradlew export.database --info
    ```

    !!!success "Important"
        The output must be a "BUILD SUCCESSFUL" message.

3. A new module is created in the `/modules` folder, with the following structure

    ```
    modules
    └── com.etendoerp.subapp.product
        └── src-db 
    ```

## Dokerized Services

Before proceeding, it is necessary to start the **Etendo RX** services. These services provide a security layer (Auth Service) and a data access layer (Das Service), which are essential for consuming or writing data in Etendo. Additionally, by selecting the **isReact** checkbox in the previously defined module, React code will be automatically generated, allowing for easier data access.

To launch all the services, it is necessary to define the following configuration variables in the `gradle.properties` file:

```groovy title="gradle.properties"
docker_com.etendoerp.etendorx=true
```

!!!info
    For more information about how to handle Etendo Dockerizations visit [Docker Management](../../etendo-classic/bundles/platform/dependency-manager.md). 

??? Note "Tomcat and PostgresSQL Dockerized (Optional)"
    It is also possible to run the dockerized [PostgreSQL service](../platform/docker-management.md#postgres-database-service) and [Tomcat service](../platform/tomcat-dockerized-service.md), **optionally** adding the [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank} and the following configuration variables:

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    docker_com.etendoerp.docker_db=true
    ```

Then, to effectively run the services, it is necessary to **execute the command** in the terminal: 

```bash title="Terminal"
./gradlew resourses.up
```

Here, all the services and their respective logs can be seen running using [Docker Desktop](https://www.docker.com/products/docker-desktop/){target=_isblank} tool.

![Docker RX Services](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/rx-services.png)

### RX Config window
:material-menu: `Application` > `Etendo RX` > `RX Config`

This configuration window stores the access data for Etendo RX services, which are crucial for the interaction between different services. In this case, two records need to be created: one for the **RX Config** service, responsible for distributing the dynamic configurations of other available services, and another for the **Auth** service, which provides security utilities. The Auth service must be accessible by the sub-application to obtain the authentication token for requests.

As `System Administrator` role, in this window, it is necessary to add two entries, one for each service to be used. The following fields should be included:

- **Service Name**: The name of each service.
- **Service URL**: The internal URL of the Docker service.
- **Updatable Configs**: Check this checkbox.
- **Public URL**: Configure the publicly accessible URL for the service.

See the configuration examples bellow and replicate them. 

!!!info
    The **Public URL** field only needs to be configured when the sub-application is set to production.

![alt text](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/rx-config-config.png)

![alt text](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/rx-config-auth.png)

!!!info 
    If using Dockerized Tomcat, the URLs within the container's network are `http://config:8888` and `http://auth:8096`.



## Projections and Search

This section covers the creation of projections, mappings, and searches, which enable the generation of a dynamic REST API in the RX DAS service. These configurations allow for reading, writing, and filtering data. Projections are applied to Etendo Classic tables, creating a subset of data that can be interacted with through the API.


### Create a Projection
:material-menu: `Application` > `Etendo RX` > `Projections and Mappings`

1.  As a `System Administrator` role, it is required to create a projection that reflect partial views of the Product class and contain only the necessary properties.

2. To do this we will go to the `Projections and Mappings` window and create a new projection, select the module under development `Product SubApplication - 1.0.0 - English (USA)`, where these configurations will be exported and in the name field we define `ProductSubApp`.

3. Now, with the selected projection we add in the tab `Projected Entities` two projections, one for reading data, selecting the table `M_Product` and in the Mapping Type field we select `Etendo to external system` and another projection for writing data, selecting again the table `M_Product` and in the Mapping Type field `External system to Etendo`.  The other fields are auto-completed with respect to these values 

<figure markdown="span">
 	![projection.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/projections-mappings.png)
	<figcaption>Projection and Projected Entities configuration example</figcaption>
</figure>

### Creating Entity Fields

Now, we define which fields we want to retrieve. To do this we start by selecting the data reading projection `PRODSUBAPP - Product - Read` and run the `Create Projection Fields` process, in the pop-up we will select the fields to project. In our example case: 

- active
- id
- name
- productCategory
- searchkey
- taxCategory
- UOM
- UPCEAN

!!! note
	While not all of these fields will be displayed in the application, as record editing is allowed, we are also selecting all the mandatory fields to create a product.

<figure markdown="span">
	![create-projection-fields.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/create-projection-fields.png)
	<figcaption>Create Projection Fields proccess excecution example</figcaption>
</figure>


This is the M_Product - Write fields.

=== "id"
=== "name"
=== "uPCEAN"
=== "searchKey"
=== "active"

- active
- id
- name
- productCategory
- searchkey
- taxCategory
- UOM
- UPCEAN


  ![entity-fields-read.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-example-subapplication/projected-entity-field-read.png)


### Create a Search in Projected Data

Now, when reading data, it is possible to create filters, for this we have to associate these filters to a table and it is possible to export this filter in the module under development. 
To do this, we open the `Tables and Columns` window, in our example select the `M_Product` table, go to the `Repository` tab and create a new record with the development module.  Then we create a new record in the `Search` tab

<figure markdown="span">
    ![repository.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/repository.png)
    <figcaption>Repository Creation Example</figcaption>
</figure>

### Create a New Search and Search Parameter

Next we will define a search method to be used when we want to consume the products. To create this new filter/search method, in the Repository tab of the `M_Product` table, create a new record with the  method name `getFilteredProducts` and the hql query filter 

```
SELECT e FROM Product e WHERE (e.active = true) AND (lower(e.name) LIKE lower('%' || :name || '%') OR lower(e.uPCEAN) LIKE lower('%' || :name || '%')) order by e.updated desc
```
This query filters active products by name or bar code. 

As we can see in the query it receives the`:name` parameter of String type that we define in the `Search Parameter` tab.

<figure markdown="span">
    ![search-parameters.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/search-parameters.png)
    <figcaption>Search and Search Parameter creation example</figcaption>
</figure>



### Restart the Etendo RX Service

Restart the Das RX service to recognize the  projections and mappings.

```bash title="Terminal"
./gradlew rx.das.restart
```

Executing this command will relaunch the Etendo RX service with the newly integrated libraries and configurations.



## Creating the Sub-application

1. Now, create the sub-application based on a template published in NPM. Execute a Gradle command to automatically create the sub-application within the module under development.

    ``` bash title="Terminal"
    ./gradlew subapp.create -Ppkg=<javapackage> --info
    ```
    In the example we are working on, use the following command:

    ```bash title="Terminal"
    ./gradlew subapp.create -Ppkg=com.etendoerp.subapp.product --info
    ```
    
    A new subapplication will be created within the module, with the following structure:

    ```
    modules
    └── com.etendoerp.subapp.product
      ├── src-db 
      └── subapp
          ├── .bundle
          ├── _tests_
          ├── android
          ├── ios
          ├── lib
          ├── node_modules
          └── src
    ```

2. In a terminal on path `modules/<javapackage>/subapp` install the depedencies declared in the `package.json` the following command: 

    ``` bash title="Terminal"
    yarn install 
    ```

3. Finally, to run in development mode run

    ``` bash title="Terminal"
    yarn dev 
    ```
    !!! note
        By default, the application run in development mode on `localhost` at port `3000`. Additionally, changes in the `/src` directory are automatically scanned, enabling dynamic updates to the application during development. This ensures that any modifications are reflected in real-time without restarting the application.

## Product Sub-application Example

This section covers an overview about the product sub-application example screens and principal parts of the subapplication.

!!! info "Consideration"
    - The applications must be developed for both platforms (phone and tablet). 
   
### Home
 
- This is the main screen of the subapplication. It will show a list of products. Also, it will allow us to edit and remove a product, find a product by name and navigate to the detail of a product.

**Phone View**
<figure markdown>
	![home-screen.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-example-subapplication/home-screen.png){ width="300", align=left } 
	![remove-product.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-example-subapplication/remove-product.png){ width="300", align=right}
</figure>
**Tablet View**
![home-screen-tablet.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-example-subapplication/home-screen-tablet.png)


- The route to this screen is `src/screens/home/index.tsx` and the content:

``` javascript title="src/screens/home/index.tsx"
import React from 'react';
import TableList from '../../components/table/list';
import { NavigationProp } from '@react-navigation/native';
import { INavigationContainerProps } from '../../interfaces';
import locale from '../../localization/locale';
import useProduct from '../../lib/data_gen/useProduct';
import { Product } from '../../lib/data_gen/product.types';

interface TableListProps {
navigation: NavigationProp<any>;
route: any;
navigationContainer: INavigationContainerProps;
}

const Home = (props: TableListProps) => {
const { getFilteredProducts, updateProduct } = useProduct();
return (
	<TableList
	deleteDataItem={async (item: Product) => {
		item.active = false;
		await updateProduct(item);
	}}
	{...props}
	columns={[
		{
		key: 'id',
		primary: true,
		visible: false,
		},
		{
		key: 'name',
		label: locale.t('Table.products'),
		visible: true,
		width: '50%',
		},
		{
		key: 'productCategoryName',
		label: locale.t('Table.products'),
		visible: true,
		width: '30%',
		},
	]}
	getData={getFilteredProducts}
	labels={{
		dataName: 'Product',
		navbarTitle: locale.t('Home.welcome'),
		containerTitle: locale.t('Home.productList'),
		buttonNew: locale.t('Home.newProduct'),
		searchPlaceholder: locale.t('Home.typeProduct'),
		successfulDelete: locale.t('Success.deleteProduct'),
		errorDelete: locale.t('Error.deleteProduct'),
	}}
	/>
);
};

export default Home;

```

Key Components: ???

1. **Navbar**: Positioned at the top, it displays the application's title and user's name, offering navigation controls.

2. **ButtonUI**: A customizable UI button from Etendo UI Library, used for actions like navigating to product details. It can be styled in terms of size, style, and includes icons.

3. **SearchContainer**: Enables product search by name, allowing the product list to be updated based on the query using the component from Etendo UI Library.

4. **TableUI**: Displays products in a table format, allowing interactions such as editing, deleting or viewing product details. Available in the tablet or web version.

5. **Cards**: Used to display product details in a card format, providing a more detailed view of the product. Only available in the mobile version.

6. **Layout and Style**: The screen is designed to be responsive for both mobile and tablet formats, with a layout comprising the navbar, button, search bar, and table. Styles are defined in the `styles` object for consistency.


### ProductDetail

- This screen will show the detail of a product. Also, it will allow us to edit the product.
- It's the same screen used to create a new product. there is a flag to know if the product is new or not (productItem).
- The route to this screen is `src/screens/productDetail.txt` , and the content:

``` javascript title="src/screens/productDetail.txt"
import React, { useState } from 'react';
import TableDetail from '../../components/table/detail';
import { NavigationProp } from '@react-navigation/native';
import locale from '../../localization/locale';
import useProduct from '../../lib/data_gen/useProduct';

interface TableDetailProps {
  navigation: NavigationProp<any>;
  route: any;
}

const ProductDetail = (props: TableDetailProps) => {
  const { createProduct, updateProduct } = useProduct();
  const [id, setId] = useState<string>('');
  const [searchKey, setSearchKey] = useState<string>('');
  const [name, setName] = useState<string>('');
  const [uPCEAN, setUPCEAN] = useState<string>('');
  return (
    <TableDetail
      {...props}
      createData={async () => {
        await createProduct({ searchKey, name, uPCEAN });
      }}
      updateData={async () => {
        await updateProduct({ id, searchKey, name, uPCEAN });
      }}
      fields={[
        {
          key: 'id',
          visible: false,
          setValue: setId,
          getValue: id,
          labels: {
            title: '',
            placeholder: '',
          },
        },
        {
          key: 'searchKey',
          setValue: setSearchKey,
          getValue: searchKey,
          labels: {
            title: locale.t('ProductDetail.searchKey'),
            placeholder: locale.t('ProductDetail.searchKeyExample'),
          },
        },
        {
          key: 'name',
          setValue: setName,
          getValue: name,
          labels: {
            title: locale.t('ProductDetail.products'),
            placeholder: locale.t('ProductDetail.nameExample'),
          },
        },
        {
          key: 'barcode',
          setValue: setUPCEAN,
          getValue: uPCEAN,
          labels: {
            title: locale.t('ProductDetail.barcode'),
            placeholder: locale.t('ProductDetail.barcodePlaceholder'),
          },
        },
      ]}
      labels={{
        editTitle: locale.t('ProductDetail.editProduct'),
        newTitle: locale.t('ProductDetail.newProduct'),
        errorTitle: locale.t('Error.product'),
        successUpdateTitle: locale.t('Success.updateProduct'),
        successCreateTitle: locale.t('Success.saveProduct'),
        connectionError: locale.t('Error.connection'),
        navbarTitle: locale.t('Home.welcome'),
        cancel: locale.t('Common.cancel'),
        save: locale.t('Common.save'),
        successTitle: id
          ? locale.t('Success.updateProduct')
          : locale.t('Success.createProduct'),
      }}
    />
  );
};

export default ProductDetail;

```
    
### Navegation 

In addition, it is necessary to add the navigation configuration in the app.tsx file, in the return statement.  This configuration provides the infrastructure to navigate between the different screens of the application.

``` javascript title="App.tsx"
<Stack.Navigator initialRouteName="Home">
      <Stack.Screen
        options={{ headerShown: false }}
        name="Home"
        initialParams={{ dataUser }}>
        {props => <Home {...props} navigationContainer={navigationContainer} />}
      </Stack.Screen>
      <Stack.Screen
        options={{ headerShown: false }}
        name="ProductDetail"
        initialParams={{ dataUser }}>
        {props => <ProductDetail {...props} />}
      </Stack.Screen>
</Stack.Navigator>
```

## Integrating Etendo RX with Etendo Sub-Application


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

The `Home` component serves as a central hub for product management within our React Native application, which allows interacting with product data. The `useProduct` custom hook provides functions for retrieving and updating products, which the `Home` component uses to maintain its state and user interface.

### Example Usage

Using the Table component from [Etendo UI Library](https://www.npmjs.com/package/etendo-ui-library){target="_blank"}, the `Home` component lists the products, displaying a loading spinner while the data is being fetched. The `useProduct` hook is used to manage the data and loading state, ensuring that the component remains responsive and user-friendly.

```typescript title="Home.tsx"
import React, { useEffect, useState } from 'react';
import { View } from 'react-native';
import useProduct from '../../hooks/useProduct';
import { Table } from 'etendo-ui-library';

const Home = () => {
  // data is the list of products, as a result of a RX consult in useProduct
  // loading is a boolean that indicates if the data is being loaded
  const { data, loading } = useProduct();
  ...
  return (
    <View>
    ...
      <TableUI
        columns={dataColumns}
        data={data} // here is used to list the products
        isLoading={loading} // here is used to show a loading spinner
        onLoadMoreData={onLoadMoreData}
        commentEmptyTable={locale.t('Table.textEmptyTable')}
        textEmptyTable={locale.t('Table.commentEmptyTable')}
        pageSize={PAGE_SIZE}
      />
      ...
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

![generate-entities.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-example-subapplication/home-subapp-product.png)

In essence, this integration is a significant stride in creating robust, scalable, and intuitive mobile applications within the Etendo ecosystem.