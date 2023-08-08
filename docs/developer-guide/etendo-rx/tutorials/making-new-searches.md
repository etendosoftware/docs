# Implementing New Searches

Before proceeding, make sure you've successfully completed the steps outlined in the [Create new projection](/docs/developer-guide/etendo-rx/tutorials/making-projections.md) guide.

## Creating a New Repository

The creation of a new repository is a crucial step in the implementation of new searches. If you need assistance with this step, please consult the [Create New Repository](/docs/developer-guide/etendo-rx/tutorials/creating-repositories.md) section of our developer guide.

## Creating a New Search

Next, set up a new search method using the following specifications:

| Field       | Value                                                                                  |
| ----------- | -------------------------------------------------------------------------------------- |
| Method Name |  `findSalesOrder`                                                                      |
|  Query      |  `select o from Order o where o.documentType.id = :documentType order by o.documentNo` |

## Creating a New Search Parameter

After creating a new search, you'll need to set up a corresponding search parameter. Use the following settings:

| Field | Value           |
| ----- | --------------- |
| Line  |  `10`           |
| Name  |  `documentType` |

Excellent work! You've successfully created and implemented new searches. If you're ready to move onto the next stage, please refer to the [**Tutorials**](/docs/developer-guide/etendo-rx/tutorials) section.