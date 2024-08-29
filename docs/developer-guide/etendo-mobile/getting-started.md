---

tags:
    - Etendo Mobile
    - React-Native
    - Subapp
---

# Etendo Mobile

![cover-getting-started.png](../../assets/getting-started/overview/cover-getting-started.png)

## Overview

*Etendo Mobile* is a subapplication development platform that includes the possibility to log in to an *Etendo Classic* server and configure the available dynamic subapplications there according to role. 

A schematic of the infrastructure is shown here:

![etendo-mobile-infrastructure.png](../../assets/developer-guide/etendo-mobile/getting-started/etendo-mobile-infrastructure.png)

On this page we will explain what are the requirements to create a subapplication and how to install all the necessary tools to develop a new subapplication.

## Environment Setup
### Requirements

- [Etendo Classic](../../developer-guide/etendo-rx/getting-started.md)
- [Etendo Mobile](../../user-guide/etendo-mobile/getting-started.md) latest version available in PlayStore or Appstore.
- [Etendo RX](../etendo-rx/getting-started.md) version `2.0.0` or higher.
- [Dynamic App](../../user-guide/etendo-classic/basic-features/general-setup/application.md#dynamic-app) 

!!! info  
    To include **Etendo RX** and **Dynamic App** modules, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](https://docs.etendo.software/latest/whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

- [Docker](https://docs.docker.com/get-docker/){target="_blank"}: version `26.0.0` or higher.
- [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: version `2.26.0` or higher.
- [Yarn](https://classic.yarnpkg.com/en/docs/install/){target="_blank"} version `1.22.0` or higher
- [NodeJS](https://nodejs.org/en/download/package-manager){target="_blank"} version `16.20` or higher.
- [Java](https://www.oracle.com/ar/java/technologies/downloads/#jdk17){target="_blank"} JDK 17 

Then continue with the [Create New Subappliction](../../developer-guide/etendo-mobile/tutorials/create-new-subapplication.md){target="_blank"} tutorial.