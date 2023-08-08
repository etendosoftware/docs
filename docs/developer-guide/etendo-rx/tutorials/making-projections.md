# Creating a New Projection

Ensure you've successfully completed the [Building a New Module for RX Capabilities](/docs/developer-guide/etendo-rx/tutorials/create-new-module) before moving forward.

Start by creating a new projection with the following properties:

| Field       | Value                                |
| ----------- | ------------------------------------ |
| Module      | tutorial - 1.0.0 - English (USA)     |
| Name        | rxtutorial                           |
| Description |  Projections needed for the tutorial |

## Adding Table and Columns

Open the "Tables and Columns" window and look for the "Order" table.

## Adding a Projection

Next, navigate to the "Projections" tab and add a new projection with the following value:

| Field      | Value                                         |
| ---------- | --------------------------------------------- |
| Projection | rxtutorial - tutorial - 1.0.0 - English (USA) |

## Adding Entity Fields

Finally, navigate to the "Entity Field" tab and add the following fields:

|  Field Name         |  Property             |
| ------------------- | --------------------- |
| id                  |  id                   |
| businessPartnerName |  businessPartner.name |
| documentNo          |  documentNo           |
| documentTypeName    |  documentType.name    |
| grandTotalAmount    |  grandTotalAmount     |

Great job! You've successfully created a new projection. Proceed to the [**Tutorials**](/docs/developer-guide/etendo-rx/tutorials) section to continue with the tutorial.
