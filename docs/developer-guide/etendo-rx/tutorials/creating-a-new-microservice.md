## Overview

This section provides a step-by-step guide for working with Etendo RX, which involves creating a new module with RX capabilities and building a Spring Boot project to consume orders making use of projections, repository and other JPA resources that we will create on our Etendo ERP.

------------------------------------------------------------------

## Building a New Module for RX Capabilities

!!!note
    Make sure to complete the [Getting Started section in the developer guide](/docs/developer-guide/etendo-rx/getting-started) to set up the Etendo Platform.


### Accessing as Admin User

After setting the local environment up, as described in the [**install etendo development environment**](/docs/developer-guide/etendo-classic/getting-started/installation/install-etendo-development-environment), we'll need to log in to the system with administration permissions to create the new module, projections, repository, etc.

Log in to your account as an administrator. The default login credentials for this administrative account are:

- Username: `admin`
- Password: `admin`

Once you're logged in, switch your role to "System Administrator", as the image shows:

  ![switch-sys-admin.png](/docs/assets/developer-guide/etendo-rx/tutorial/switch-sys-admin.png)


The "System Administrator" role allows us to access some windows and permission to create and manipulate the system to fulfill our needs.

### Creating a New Module

Now we'll create a new module. It's a self-contained unit of code that performs a specific function and, in our case, it contains all the resources needed in this guide.
To create a new module, go to the 'Module' window, and add a new record providing the following information:

| Parameter       | Value                                 |
| --------------- | ------------------------------------- |
| Java Package    |`com.tutorial.classictutorial`         |
| Name            |`Tutorial`                             |
| Description     |`Module created for tutorial purposes` |
| Version         |`1.0.0`                                |
| Is RX           |`True`                                 |
| Rx Java Package |`com.tutorial.rxtutorial`              |


It should look like this:

  ![new-module.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-module.png)


With our new module created, we'll start working with 'Projections'

------------------------------------------------------------------

## Projection

When using Spring Data JPA to implement the persistence layer, the repository typically returns one or more instances of the root class. However, more often than not, we don't need all the properties of the returned objects.

In such cases, we might want to retrieve data as objects of customized types. These types reflect partial views of the root class, containing only the necessary properties. This is where projections come in handy.

Start by opening 'Projections' windows and creating a new projection with the following properties:

| Field       | Value                                 |
| ----------- | ------------------------------------- |
| Module      |`tutorial - 1.0.0 - English (USA)`     |
| Name        |`rxtutorial`                           |
| Description |`Projections needed for the tutorial`  |


  ![new-projection.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-projection.png)

### Adding the projection to a table

As we create the projection, now we need to assign it to a table where we want to extract data.
For this, open the "Tables and Columns" window and look for the "Order" table (as mentioned in the introduction, we want to consume orders).

### Adding a Projection

Next, navigate to the "Projections" tab and add a new projection with the following value:

| Field      | Value                                          |
| ---------- | ---------------------------------------------- |
| Projection |`rxtutorial - tutorial - 1.0.0 - English (USA)` |


  ![assign-projection.png](/docs/assets/developer-guide/etendo-rx/tutorial/assign-projection.png)

### Adding Entity Fields

When a projection is created, we need to define which fields we want to retrieve.
In our case, we'll need the record ID, Business Partner name, Document No, Document Type name, and the Grand total.
Under the 'Projection' tab navigate to the "Entity Field" tab and add the following fields:

|  Field Name         |  Property             |
| ------------------- | --------------------- |
| id                  |`id`                   |
| businessPartnerName |`businessPartner.name` |
| documentNo          |`documentNo`           |
| documentTypeName    |`documentType.name`    |
| grandTotalAmount    |`grandTotalAmount`     |

!!!note
    The 'Property' field of this tab is handled with an Entity Mapping, this is like a Hiernate property.
    So, you can navigate the entities related from here, e.g., the Business Partner name, we have it by accessing the entity 'businessPartner' and, then, adding the field that we want, "name" in our case.


  ![new-entity-fields.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-entity-fields.png)

------------------------------------------------------------------

## Repository

In Spring Data, a repository is an abstraction that provides the operations relative to a domain class to interact with a data store.
To create the repository for our purpose, and the same as we did for projections, we need to go to Tables and Columns and look for 'C_Order' table

### Creating a New Repository

After selecting a table, in this case 'C_Order', we need to go to 'Repository' tab and create a new record with the following values:

| Field       | Value                                |
| ----------- | ------------------------------------ |
| Module      |`tutorial - 1.0.0 - English (USA)`    |


 ![new-repository.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-repository.png)

------------------------------------------------------------------

## Search

### Creating a New Search

Next, we'll define a search method to use later when we want to consume the orders. This query is taken as a filter for retrieving the orders.
To create this new filter/search method, under "Repository" tab of the C_Order table, create a new record with the following data:

| Field       | Value                                                                                  |
| ----------- | -------------------------------------------------------------------------------------- |
| Method Name |`findSalesOrder`                                                                        |
|  Query      |`select o from Order o where o.documentType.id = :documentType order by o.documentNo`   |


  ![new-search.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-search.png)

### Creating a New Search Parameter

As you can see in the query above, we use a parameter called `:documentType`. 
We can add this type of parameter to use it later by adding a corresponding value to it and filtering depending on the current needs.
To define the parameter, we need to create a new row on the 'Search Parameter' tab of the 'Search' tab. Fill it with the following settings:

| Field | Value         |
| ----- | ------------- |
| Line  |`10`           |
| Name  |`documentType` |
| Type  |`String`       |

In our case, we'll filter depending on the Document Type of the orders

  ![new-search-parameter.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-search-parameter.png)

------------------------------------------------------------------


## Creating a New Spring Boot Project

Now that we have declared the projection, fields, repository, and searches on Etendo ERP, we'll need to create a new spring project to make use of these JPA resources that we have created just before.
Next, you'll find the steps to create the Spring Boot project and add it as a module on Etendo RX.

### Project Creation

1. Visit [**Spring Initializr**](https://start.spring.io/){target="_blank"} to start your project setup.
2. Fill in the following details:

    | Field        | Value                           |
    | ------------ | ------------------------------- |
    | Project      |Gradle Project                   |
    | Language     |Java                             |
    | Spring Boot  |2.7.15 (or latest 2.7.x version) |


    Project Metadata

    | Field        | Value                     |
    | ------------ | ------------------------- |
    | Group        |com.tutorial               |
    | Artifact     |rxtutorial                 |
    | Name         |rxtutorial                 |
    | Description  |Etendo RX tutorial project |
    | Package Name |com.tutorial.rxtutorial    |
    | Packaging    |Jar                        |
    | Java Version |11                         |

3. Add the following dependencies: Spring Web, Lombok, Config Client
4. Click on the 'Generate' button to download your project. The page will generate a file named `rxtutorial.zip`.

    ![spring-initializr.png](/docs/assets/developer-guide/etendo-rx/tutorial/spring-initializr.png)

5. Uncompress the zip file to the platform project created in the first step, as: `modules_rx/com.tutorial.rxtutorial`.

!!!info
    Remember to create the `com.tutorial.rxtutorial` folder, inside of `modules_rx` before extract it.


### Project Configuration

After creating the project, we need to add some configuration in order to work with our ERP.

### Modify build.gradle File

Remove version of spring plugins:

```groovy
plugins {
    ...
    id 'org.springframework.boot' version '2.7.14'
    id 'io.spring.dependency-management' version '1.0.15.RELEASE'
}
```

Change it to this:

```groovy
plugins {
    ...
    id 'org.springframework.boot'
    id 'io.spring.dependency-management'
}
```

Gradle will get versions from the Etendo Platform project.

Add the following dependencies in the dependencies section:

```groovy
implementation 'org.springframework.cloud:spring-cloud-starter-openfeign'
implementation 'org.springframework.boot:spring-boot-starter-hateoas'
implementation 'com.etendorx:clientrest_core:latest.integration'
```

Add the Etendo repository:

```groovy
repositories {
    mavenCentral()
    maven {
        url = "https://maven.pkg.github.com/etendosoftware/etendo_rx"
        credentials {
            username = "${githubUser}"
            password = "${githubToken}"
        }
    }
}
```

!!! note
    `githubUser` and `githubToken` were configured in the first step.

Add custom source set:

```groovy
sourceSets {
    main {
        java {
            srcDirs = [
                'src/main/java',
                'src-gen/main/java',
            ]
        }
    }
}
```
After configuring the project, we'll need to generate the proper files for RX.
RX generate.entities task will generate java files in the `src-gen` directory.
Execute `rx:generate.entities` task to do so.

``` bash title="Terminal"
./gradlew rx:generate.entities
```

------------------------------------------------------------------

## Configuring a Spring Boot Project

Now we'll configure the new spring boot project to define how it will run.

### Updating the application.properties file

Modify your `application.properties` file, under the new spring boot project created on the previous steps, with the following configurations:

```properties
config.server.url=http://localhost:8888
spring.config.import=configserver:${config.server.url}
spring.application.name=rxtutorial
server.port=8101
token=
```

The token is empty, but now we'll generate a new one
### Adding the 'token' value

To generate the token value we need to follow these steps:

  1. As 'System Administrator' role on the ERP, go to 'RX Services' window.
  2. Create a new row with the following values:

    |  Field Name         |  Property                      |
    | ------------------- | ------------------------------ |
    | Searchkey           |Tutorial                        |
    | Secret              |123                             |
    | Module              |Tutorial - 1.0.0 - English (USA)|

    ![new-rx-service.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-rx-service.png)

  3. Change to 'F&B International Group Admin' role.
  4. Go to 'User' window.
  5. Choose a user, e.g. 'F&B ES User'
  
    !!! info
        Change the password for this record, you'll need it later.
        Also, check that the user is active.

  6. In the tab 'RX Services Access' create a new row and fill it with the following values:
    
    | Field Name           |  Property                     |
    | ------------------- | ------------------------------ |
    | Organization        |*                               |
    | RX Services         |Tutorial                        |
    | Default Role        |F&B España, S.A - Sales         |
    | Default Org         |F&B España, S.A                 |

    ![new-rx-service-access.png](/docs/assets/developer-guide/etendo-rx/tutorial/new-rx-service-access.png)

  7. Let's run RX so we can make the request to the Auth service:

    ``` bash title="Terminal"
    ./gradlew rx:rx
    ```

  8. Open Postman and we'll make an authenticate request.
  
    Verbose: POST

    URL: http://localhost:8094/api/authenticate

    Body:
    ```json
    {
      "username":"F&BESUser",
      "password":"EtendoAdmin1",
      "service":"Tutorial",
      "secret":"123"
    }
    ```
    !!!warning
        Remember the password changed before.

    ![postman-request.png](/docs/assets/developer-guide/etendo-rx/tutorial/postman-request.png)
  
  9. Take the token under the response and fill in the 'token' property on the application.properties of the tutorial module.

### Adding Component Scan Annotation to the Application Class

To scan your application for annotated components, add the `@ComponentScan` annotation to your Application class with the necessary base packages:

!!!info
    The path to the application class, in this case, is: `modules_rx/com.tutorial.rxtutorial/src/main/java/com/tutorial/rxtutorial/RxtutorialApplication.java`

```java
@ComponentScan({
    "com.tutorial.rxtutorial",
    "com.etendorx.clientrest.base",
})
```
!!! warning
    Remember to add the import for ComponentScan annotation: 
    ```java
    ...
    import org.springframework.context.annotation.ComponentScan;
    ...
    ```

Hence, your Application class should look like:

```java
package com.tutorial.rxtutorial;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan({
    "com.tutorial.rxtutorial",
    "com.etendorx.clientrest.base",
})
public class RxtutorialApplication {

  public static void main(String[] args) {
    SpringApplication.run(RxtutorialApplication.class, args);
  }

}
```

------------------------------------------------------------------

## Creating a New Spring Boot Service

In this last step before launching the microservice, we'll create the logic to consume the orders using the projection and all the JPA resources that we defined in the previous steps. 
Follow the instructions below to create a new service:

1. Create a new file at the following path:

    ```java
    modules_rx/com.tutorial.rxtutorial/src/main/java/com/tutorial/rxtutorial/RxtutorialService.java
    ```

2. Then, copy and paste the following code into the file:

    ```java
    package com.tutorial.rxtutorial;

    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;

    import com.etendorx.clientrest.base.RestUtils;
    import com.etendorx.clientrest.base.RestUtilsException;
    import com.tutorial.rxtutorial.entities.org.openbravo.model.common.order.OrderRxtutorialModel;

    @RestController
    @RequestMapping(path = "/api")
    public class RxtutorialService {
      @Autowired
      RestUtils restUtils;

      @GetMapping(path = "/")
      public String get() throws RestUtilsException {
        String url = "/Order/search/findSalesOrder?documentType=AB22CE8FFA5E4AF29F2AC90FCDD400D8&projection=rxtutorial";
        var orders = restUtils.getList(url, OrderRxtutorialModel.class);
        StringBuilder html = new StringBuilder("<html>");
        html.append("<head>");
        html.append("<style type=\"text/css\">html {font-family: sans-serif;}</style>");
        html.append("</head>");
        html.append("<title>Orders</title></head>");
        html.append("<body>");
        html.append("<h2>Orders</h2>");
        html.append("<table>");
        for (OrderRxtutorialModel o : orders) {
          html.append(
              "<tr>" +
                  "<td>" + o.getDocumentNo() + "</td>" +
                  "<td>" + o.getBusinessPartnerName() + "</td>" +
                  "<td>" + o.getDocumentTypeName() + "</td>" +
                  "<td>" + o.getGrandTotalAmount() + "</td>" +
                  "</tr>"
          );
        }
        html.append("</table></body></html>");
        return html.toString();
      }
    }
    ```

    This file will display a simple HTML page with the retrieved orders.
    But first, we'll take a look at the class that we just created.

      ```java
      String url = "/Order/search/findSalesOrder?documentType=AB22CE8FFA5E4AF29F2AC90FCDD400D8&projection=rxtutorial";
      ```
      This URL is the one that the process will use to consume the service, as you can see, we add here the 'Search' filter that we created before and give it the document type parameter, with one document type id of the order that we'll filter. Also, we're adding the projection to use too, same as before, it's the one created before.

      
      ```java
      var orders = restUtils.getList(url, OrderRxtutorialModel.class);
      ```

      The orders variable will store all the orders that will be filtered with our request, as you can see, the method `getList` receives two parameters, the first one is the URL that we'll use to make the request, and the second one is the model class of the retrieved object.

3. Then, we simply create a StringBuilder as an HTML page that will be shown on the browser.

------------------------------------------------------------------

## Run RX Services

To simplify RX executions you have a simplified run task:

``` bash title="Terminal"
./gradlew rx:rx
```

!!!warning
    Remember to configure the Auth service as described on the [Getting Started](/docs/developer-guide/etendo-rx/getting-started/#configure-auth-project) page

## Run tutorial project

Now we're able to run our new microservice. For that, execute the following task:

``` bash title="Terminal"
./gradlew :com.tutorial.rxtutorial:bootRun
```

Open your browser and you can view the generated page with the following URL: [**http://localhost:8101/api/**](http://localhost:8101/api/)

!!! success
    You've successfully created a fully working RX service.