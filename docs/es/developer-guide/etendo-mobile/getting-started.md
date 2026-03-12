---
title: Guía del desarrollador - Primeros pasos - Etendo Mobile
tags:
    - Etendo Mobile
    - React-Native
    - Desarrollo de subaplicaciones
    - Configuración del entorno
    - Infraestructura
---

# Guía del desarrollador - Primeros pasos - Etendo Mobile

![cover-getting-started.png](../../assets/getting-started/overview/cover-getting-started.png)

## Visión general

*Etendo Mobile* es una plataforma de desarrollo de subaplicaciones que incluye la posibilidad de iniciar sesión en un servidor de *Etendo Classic* y configurar allí las subaplicaciones dinámicas disponibles según el rol.

A continuación se muestra un esquema de la infraestructura:

![etendo-mobile-infrastructure.png](../../assets/developer-guide/etendo-mobile/getting-started/etendo-mobile-infrastructure.png)

En esta página, primero explicaremos el paso a paso para instalar y configurar por primera vez subaplicaciones en un cliente y, a continuación, cuáles son los requisitos para crear una subaplicación y las herramientas necesarias para desarrollar una nueva subaplicación.

## Instalar subaplicaciones distribuidas en Etendo Classic

Puede encontrar las subaplicaciones distribuidas por Etendo, disponibles para su instalación, y su documentación en la sección [Subaplicaciones disponibles para instalar](../../user-guide/etendo-mobile/getting-started.md#install-subapps-in-etendo-classic).

Para instalar estos bundles, puede seguir la siguiente guía [Instalar módulos en Etendo Classic](../etendo-classic/getting-started/installation/install-modules-in-etendo.md)

## Configuración del entorno de desarrollo
### Requisitos

- [Etendo Classic](../../developer-guide/etendo-rx/getting-started.md)
- [Etendo Mobile](../../user-guide/etendo-mobile/getting-started.md) última versión disponible en PlayStore o Appstore.
- [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank}.
- [Docker](https://docs.docker.com/get-docker/){target="_blank"}: versión `26.0.0` o superior.
- [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: versión `2.26.0` o superior.
- [Yarn](https://classic.yarnpkg.com/en/docs/install/){target="_blank"} versión `1.22.0` o superior
- [NodeJS](https://nodejs.org/en/download/package-manager){target="_blank"} versión `16.20` o superior.
- [Java](https://www.oracle.com/ar/java/technologies/downloads/#jdk17){target="_blank"} JDK 17

A continuación, continúe con el tutorial [Crear nueva subaplicación](../../developer-guide/etendo-mobile/tutorials/create-new-subapplication.md){target="_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.