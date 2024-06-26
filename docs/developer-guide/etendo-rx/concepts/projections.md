## Projection

When using Spring Data JPA to implement the persistence layer, the repository typically returns one or more instances of the root class. However, more often than not, we do not need all the properties of the returned objects.

In such cases, we might want to retrieve data as objects of customized types. These types reflect partial views of the root class, containing only the necessary properties. This is where projections come in handy.

Start by opening *Projections* windows and creating a new projection with the following properties:

| Field       | Value                                 |
| ----------- | ------------------------------------- |
| Module      |`tutorial - 1.0.0 - English (USA)`     |
| Name        |`rxtutorial`                           |
| Description |`Projections needed for the tutorial`  |


  ![new-projection.png](../../../assets/developer-guide/etendo-rx/tutorial/new-projection.png)

### Adding the projection to a table

As we create the projection, now we need to assign it to a table where we want to extract data.
For this, open the *Tables and Columns* window and look for the *Order* table (as mentioned in the introduction, we want to consume orders).

### Adding a Projection

Next, navigate to the *Projections* tab and add a new projection with the following value:

| Field      | Value                                          |
| ---------- | ---------------------------------------------- |
| Projection |`rxtutorial - tutorial - 1.0.0 - English (USA)` |


  ![assign-projection.png](../../../assets/developer-guide/etendo-rx/tutorial/assign-projection.png)

### Adding Entity Fields

When a projection is created, we need to define which fields we want to retrieve.
In our case, we will need the record ID, Business Partner name, Document No, Document Type name, and the Grand total.
Under the Projection tab navigate to the *Entity Field* tab and add the following fields:

|  Field Name         |  Property             |
| ------------------- | --------------------- |
| id                  |`id`                   |
| businessPartnerName |`businessPartner.name` |
| documentNo          |`documentNo`           |
| documentTypeName    |`documentType.name`    |
| grandTotalAmount    |`grandTotalAmount`     |

!!!note
    The *Property* field of this tab is handled with an Entity Mapping, this is like a Hibernate property.
    So, you can navigate the entities related from here. E.g. To get the Business Partner name, you can have it by accessing the entity *businessPartner* and then, adding the field that you want to filter, *name* in this case.


  ![new-entity-fields.png](../../../assets/developer-guide/etendo-rx/tutorial/new-entity-fields.png)

------------------------------------------------------------------

## Repository

In Spring Data, a repository is an abstraction that provides the operations relative to a domain class to interact with a data store.
To create the repository for our purpose, and the same as we did for projections, we need to go to Tables and Columns and look for `C_Order` table.

### Creating a New Repository

After selecting a table, in this case `C_Order`, we need to go to *Repository* tab and create a new record with the following values:

| Field       | Value                                |
| ----------- | ------------------------------------ |
| Module      |`tutorial - 1.0.0 - English (USA)`    |


 ![new-repository.png](../../../assets/developer-guide/etendo-rx/tutorial/new-repository.png)

------------------------------------------------------------------

## Search

### Creating a New Search

Next, we will define a search method to use later when we want to consume the orders. This query is taken as a filter for retrieving the orders.
To create this new filter/search method, under Repository tab of the `C_Order` table, create a new record with the following data:

| Field       | Value                                                                                  |
| ----------- | -------------------------------------------------------------------------------------- |
| Method Name |`findSalesOrder`                                                                        |
|  Query      |`select o from Order o where o.documentType.id = :documentType order by o.documentNo`   |


  ![new-search.png](../../../assets/developer-guide/etendo-rx/tutorial/new-search.png)

### Creating a New Search Parameter

As you can see in the query above, we use a parameter called `:documentType`. 
We can add this type of parameter to use it later by adding a corresponding value to it and filtering depending on the current needs.
To define the parameter, we need to create a new row on the *Search Parameter* tab of the *Search* tab. Fill it with the following settings:

| Field | Value         |
| ----- | ------------- |
| Line  |`10`           |
| Name  |`documentType` |
| Type  |`String`       |

In our case, we will filter depending on the Document Type of the orders.

  ![new-search-parameter.png](../../../assets/developer-guide/etendo-rx/tutorial/new-search-parameter.png)

------------------------------------------------------------------
