---
title: Prerequisite Knowledge
tags:
    - Prerequisite
    - Knowledge
    - Concepts
    - Database

status: beta
---

#  Prerequisite Knowledge

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.
  
##  Overview

This section lists the main knowledge areas which are relevant when developing in/with Etendo. The exact required knowledge level depends very much on the task one needs to under take. Some development tasks will consist primarily of changes through the Etendo UI which require very little deep technical knowledge. Other tasks can be more involving and require changing or extending Etendo. In this last case, a technical understanding of the Etendo product is also required.

##  General Knowledge

To develop in/with Etendo, it is at least required to have a basic understanding of the following technology:

* [Java](https://dev.java/){target="\_blank"}: The programming language used in all the server side components of Etendo. It is used in all levels from the core components to ERP business logic. 
* [J2EE](https://www.oracle.com/java/technologies/){target="\_blank"}: The platform used for server programming in the Java language it adds libraries to provide enterprise capabilities to java applications running on an application server. 
* [Apache Ant](https://ant.apache.org/){target="\_blank"}: The tool used to execute the build tasks related to Etendo like compiling, deployment to an application server, exporting and importing the database schema, etc. 
* [Eclipse IDE](../how-to-guides/how-to-set-up-eclipse-ide.md): An integrated development environment that helps in all the development tasks related to Etendo like editing source files, debugging, executing build tasks, etc. 
* [SQL](https://en.wikipedia.org/wiki/SQL){target="\_blank"}: A database computer declarative language. It is used across all the Etendo server side components to access data stored in the relational database management systems used: PosgreSQL and Oracle. 
* [HTML](https://en.wikipedia.org/wiki/HTML){target="\_blank"}: The markup language used to render the Etendo user interface in the web browser used by Etendo users. 
* [XML](https://en.wikipedia.org/wiki/XML){target="\_blank"}: The markup language used to describe different documents in Etendo like REST Web Services, Jasper Reports, configuration files, template files, etc. 

##  Database

If the development tasks are primarily in the database area, then a developer would also need to have experience with:

* [PostgreSQL](https://www.postgresql.org/){target="\_blank"} or [Oracle](https://www.oracle.com/database/){target="\_blank"}: The target database used. 
* Database schema concepts like constraints, foreign key, triggers, indexes... 
* [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL){target="\_blank"}: The language used to develop business logic in the database side. 

##  UI / Client-Side Code

Etendo requires a web browser like Internet Explorer, Firefox, Chrome or Safari to render the user interface. For developments focused on the user interface there will be required experience with:

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript){target="\_blank"}: An scripting language used by web browsers to provide access to the user interface pages. Developers should be able to read, write and debug JavaScript code using the development tools provided by web browsers. 
* [SmartClient](https://smartclient.com/){target="\_blank"}: The RIA Framework Etendo is based on, it is based on JavaScript it includes a large collection of widgets and other utilities for the client side. 

##  Data Access Layer

For server side developments in the Java programming language that access the database, the following technologies are used:

* [Data Access Layer](../concepts/data-access-layer.md): The Etendo component used to strengthen the development of business logic in Java. 
* [Hibernate](https://hibernate.org/){target="\_blank"}: The library Data Access Layer is based on that provides Object/Relational mapping and enables developers to use an object model to access relational databases. To make the best use of the Data Access Layer, its main concepts are important to understand how to create more advanced queries, especially the Hibernate Query Language ([HQL](https://docs.hibernate.org/core/3.6/reference/en-US/html/queryhql.html){target="\_blank"}) and the Hibernate Criteria API. 

##  Web Services

To consume and extend Etendo web services, a developer needs to have knowledge in the following areas:

* [REST](https://en.wikipedia.org/wiki/REST){target="\_blank"}: The style of software architecture used to provide web services in Etendo. 
* [XML Schema](https://www.w3.org/TR/xmlschema-0/){target="\_blank"}  for XML Web Services, to represent the XML media type provided by this type web services. 
* [JSON](https://en.wikipedia.org/wiki/JSON){target="\_blank"}: A text based standard designed for data interchange, it has a close relation with Javascript and it is used for JSON Web Services in Etendo. 

---

This work is a derivative of [Prerequisite Knowledge](http://wiki.openbravo.com/wiki/Prerequisite_Knowledge){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.