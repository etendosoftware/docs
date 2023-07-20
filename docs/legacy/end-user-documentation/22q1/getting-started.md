---
title: What is Etendo?
---
**Etendo** is a composable and scalable ERP software. **Etendo** is focused on non-retail and it is adapted for different companies. To present a flexible and modern product, **Etendo** combines a web platform with a user-friendly skin and a mobile application. We are always keeping our product dynamic and we look for surpassing technologies.

![Etendo desktop](https://drive.google.com/uc?export=view&id=1JKekHpGBzHi9kVLw4rBxHnUbtAiqSfCa)

## Functional characteristics

### Massive record actions

**Etendo** supports massive record cloning and allows users to make actions for multiple invoices and orders. By selecting all the needed records, the documents’ status can be changed with a click.

### Grid summary functions update on selection

In **Etendo** the user can get summary functions of a subset of records of a window. It is possible to filter the records that are on a grid, and the calculation changes based on the selected entities.

### Alert emails

The name of the alert and other relevant data, such as the host and instance purpose (e.g. development, production, test) are included in the subject of the emails sent from the **Etendo** ERP. 

### Quotations management

**Etendo** supports a [Sales Quotations module](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/modules/sales-quotation) which allows the user to edit a quotation's customer, rate or currency, while keeping the lines already created. The changes generate a new quotation and cancel the previous one, requiring a reject reason that must be completed in the ERP. Each time the quotations’ conditions change, they can be recorded in a History tab.

### Updated localization modules

Required localization modules (taxes, billing processes, locations) are available and have continuous maintenance.

## Technical characteristics

### Tools standarization

The **Etendo** development team uses tools that are standard in the industry such as Git flow, Sonar, Docker, Jenkings, JUnit, Gradle, Nexus, Flex, Elastic, React, among others.

[Gradle is used](https://docs.etendo.software/en/technical-documentation/etendo-environment/requirements-and-tools/developer-tools/use-of-gradle-in-etendo) to build, publish and for dependency handling automation, to define and improve compilation, version management, modules publication, migrations and much more. This tool offers flexibility and allows the developer to create any type of task.

Git Flow tool is used to speed up and simplify the development process as well as the versioning of releases, hotfixes, features, etc.

Spock is available for testing. This framework has JUnit runner, which makes it compatible with most IDEs, build tools, and continuous integration servers. It allows the developer to get insightful reports when the testing is done.

The tool for testing modules’ compatibility uses Docker to mount an image of **Etendo** in a specific version and installs the modules to test. This allows us to verify the compilation process and the compatibility of modules in the specified version of **Etendo**.

### Integrations

**Etendo** has flexible architecture, structured in layers and with a low-level communication interface that allows the implementation of integrations in a generic way with other platforms.

**Etendo** supports an integration with Redis to handle sessions. The ERP introduces some special classes, so the developer can cache values in the classes transparently.

### Jobs and Actions

**Etendo** introduces [the concept of Jobs](https://docs.etendo.software/en/technical-documentation/etendo-environment/platform/create-jobs-and-actions), which are one or more Actions executed in sequence. These Actions are standard processes, and developers are able to create and store Jobs for later usage. It is possible to cancel/kill currently executing jobs.

### Kubernetes Ready

**Etendo** is an allocable and horizontally scalable software. Kubernetes provides the infrastructure which allows us to scale the system on demand. The ERP has a helper tool that facilitates doing everyday tasks with Etendo K8s. It includes the most common actions used by developers in the K8s environment.

### Ongoing Maintenance

Through **Etendo**'s repository, which is mounted on [a Nexus server](https://docs.etendo.software/en/technical-documentation/etendo-environment/requirements-and-tools/developer-tools/use-of-nexus-in-etendo), it is possible to store and distribute the software and modules.

### Core's code in JAR

The module management in **Etendo** is standard, since [it supports the JAR format](https://docs.etendo.software/en/technical-documentation/etendo-environment/platform/how-to-declare-JAR-dependencies-in-an-Etendo-project) and enables the distribution of compiled code.

[JAR](https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jarGuide.html) is defined as a file format that is similar to the ZIP format. It allows data compression, reducing the size of the files and improving download time.

