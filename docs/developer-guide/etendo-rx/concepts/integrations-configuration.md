---
tags:
    - Etendo RX
    - Mappings
    - Connector
    - Integrations
    - Configuration
    - Entity
---

# Integrations Configuration

## Overview

In this section, the different windows included in the [Etendo connector](#connector) configuration are explained. In this configuration, the windows [Entity Mapping](#entity-mapping) and [External ID Mappings](#external-id-mappings) are also used.

!!! info
    For more information about Etendo RX services, visit [Etendo RX Getting Started](../getting-started.md)


### Connector

:material-menu: `Application` > `Etendo RX` > `Integrations Configuration` > `Connector`

A connector is a mechanism or intermediary component that enables communication and data exchange between two different systems, applications, or modules. It acts as a bridge, allowing these systems, which may use different protocols, data formats, or technologies, to interact with each other in a seamless and standardized way.

In the Connector window, you can define one connector for each external system with which Etendo will be synchronized.

By default, the Etendo standard connector has 5 layers 
- Communication layer: With services such as Debezium, Kafka and DAS. These are in charge of CHECK VIDEO?
- Model layer: For each object required to synchronize, it is necessary to define a converter. For this, the Projection and mappings window is used to generate the REST API, which models data in Etendo.
- Synchronization layer: This layer is functional, but must be extendable and overridable to allow a new integration that has other logic. it gives Unidirectional and Bidirectional synchronization functionality
- ...
-

LAYERS

VA

Fields to note:

- Organization: The corresponding organization of the connector.
- Name: Corresponding name of the connector.
- Module: It indicates the module the element forms part of. This is the module in which the configuration is exported.
- Active: A check to indicate whether this connector is available or disabled.

#### Instance Connector Tab

In this tab, the user can define the instances to use the connector. The same connector can have multiple instances. For example, Etendo could be connected with two different instances of an external system, and take different information from each instance at the same time.

VA

Fields to note:

- Organization: The corresponding organization of the Instance connector.
- Name: Corresponding name of the Instance connector.
- URL: The exposed API's URL of the external system to be synchronized
- Authorization Type: It is the API's authorization method. In the dropdown list, you can find the available options.
- Username: The necessary username to log in the external system. This field is only available if the option Basic Auth is selected in the Authorization Type field.
- Password: The necessary password to log in the external system. This field is only available if the option Basic Auth is selected in the Authorization Type field.
- oAuth Token: The necessary token to log in the external system. This field is only available if the option X Token is selected in the Authorization Type field.
- Active: A check to indicate whether this instance connector is available or disabled.
- Etendo to External Endpoint:
- External to Etendo Endpoint:

#### Instance Connector Mapping Subtab

In this subtab, it is possible to define entities to map for each connected instance.

VA

Fields to note:

- Entity Mapping: A dropdown list with the available [entities mappings](#entity-mapping) in the currect instance connector. 
- Filter: It is possible to filter the records to synchronize using [JAXB](to complete) language. This is an advanced feature to be used to synchronize records following a specific logic.
- Active: A check to indicate whether this mapping is available or disabled.

### Entity Mapping

:material-menu: `Application` > `Etendo RX` > `Integrations Configuration` > `Entity Mapping`

Entity mapping is crucial in ensuring that the logical representation of data in the application aligns with the physical structure of the data in the database.

In this window, the entity mapping is configured, from an external system (the exposed API entities) to Etendo entities. In this configuration, the external API is represented. 

There are two types of entity mappings: 

- Default entity mapping: used for [standard endpoints](doc link)
- Custom entity mapping: customized endpoint paths

VA

Fields to note:

- Organization: The corresponding organization of the entity.
- Module: It indicates the module the element forms part of. This is the module in which the configuration is exported.
- External Entity: Name of the API's external entity to be mapped.
- Etendo Entity: Name of the Etendo entity to be mapped, available in the DAS Service Swagger.
- Integration Direction: Two options: From Etendo to External System and From External System to Etendo. This options filter the possible options shown in the field Projection Entity.
- Projection Entity: Entity that is projected...
- Active: A check to indicate whether this record is available or disabled.
- Disable Triggers: If this option is selected, when an external system request is received in this entity mapping, the database triggers are not executed. This is useful so as not to have duplicated information?

JSONpath? (Mentioned in the video, Mati's doing it, minute 38)

#### Post Process Action

...???

### External ID Mappings

:material-menu: `Application` > `Etendo RX` > `Integrations Configuration` > `External ID Mappings`

Definition of External ID Mappings

VA

Fields to note:

- Organization: The corresponding organization of the ?.
- Instance Connector:
- Record ID:
- External ID:
- Table:
- Active: A check to indicate whether this record is available or disabled.

