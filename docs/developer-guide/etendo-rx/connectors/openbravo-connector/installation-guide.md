---
title: Connecting Openbravo and Etendo with Etendo RX Middleware
tags:
    - Connector
    - Openbravo
    - POS Terminal
    - Etendo Classic
    - Etendo RX 
    - Environment Synk
    - Demo
---


# Connecting Openbravo and Etendo with Etendo RX Middleware

## Overview
This guide provides step-by-step instructions to install and configure the integration between Openbravo and Etendo environments. This setup allows you to generate documents in Openbravo POS Terminal, store them in the Openbravo environment and synchronize them with Etendo using Etendo RX as middleware.

In this guide we will start from two clean environments using test data, which facilitates the configuration and demonstrates the potential of this integration.

!!! info 
    Esta guia esta definida utilizando Openbravo 24Q4 y Etendo 24.4.0

## Required Software and Tools
- [Openbravo 24Q4](https://gitlab.com/orisha-group/bu-commerce/openbravo/product/openbravo) or later
- [Etendo Environment 24.3.0](../../../../whats-new/release-notes/etendo-classic/release-notes.md) or later
- [Platform Extensions Bundle ](../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) latest version installed in Etendo
- [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community or Ultimate Edition)
- [Eclipse](https://eclipseide.org/){target="_blank"}
- [Apache Tomcat](https://tomcat.apache.org/){target="_blank"}
- [Docker Desktop](https://www.docker.com/products/docker-desktop/){target="_blank"}

## Openbravo

First, follow the [Openbravo Custom Installation Guide](https://wiki.openbravo.com/wiki/Installation/Custom){target="_blank"} and install in a local environment following [How to setup Eclipse IDE](https://wiki.openbravo.com/wiki/How_to_setup_Eclipse_IDE){target="_blank"}.  

### Modules to Install on Openbravo
In the Openbravo environment we need to install the Retail POS, EDL and Business API modules.

To get these modules, you must have an active Openbravo License, and access to the Openbravo Forge.
Ensure the following modules are installed in the versions compatible with the chosen Openbravo Core version:

!!! info
  This guide is based on [Openbravo 24Q4](https://wiki.openbravo.com/wiki/Release_Notes/24Q4). 

- `org.openbravo.retail.sampledata`
- `org.openbravo.retail.returns`
- `org.openbravo.retail.posterminal`
- `org.openbravo.retail.poshwmanager`
- `org.openbravo.retail.pack`
- `org.openbravo.retail.discounts`
- `org.openbravo.retail.config`
- `org.openbravo.mobile.core`
- `org.openbravo.events.core`
- `org.openbravo.api`
- `org.openbravo.service.openapi`
- `org.openbravo.service.external.integration`
- `org.openbravo.externaldata.integration`

Also is necesary to apply a change in the `modules/org.openbravo.api/src/org/openbravo/api/util/ApiUtils.java` file  in line 38 reeplace by: 

```java

Matcher m = Pattern.compile("(^|[^\\\\]{2}):{1}([a-zA-Z0-9_]+)").matcher(hqlWhereClause);

```

###  Clone Required Repositories

Clone the Openbravo-Etendo connector modules:

```bash
git clone git@github.com:etendosoftware/com.etendoerp.integration.openbravo.git --branch 1.0.0
git clone git@github.com:etendosoftware/com.etendoerp.integration.openbravo.template.git --branch 1.0.0
```

### Set Up the Openbravo Environment
Run the following commands to set up the Openbravo environment:

```bash
ant setup
ant install.sources
ant import.sample.data -Dmodule=org.openbravo.retail.sampledata
ant smartbuild
```

Configurar tomcat para correr en el 8081, reiniciar tomcat y configurar el POS.
https://wiki.openbravo.com/wiki/Retail:Configuration_Guide

Entrar a Openbravo y Configurar el POS

!!! info 
    http://localhost:8081/openbravo/
    user: Openbravo
    password: openbravo


Entar al POS con la URL:
http://localhost:8081/openbravo/web/org.openbravo.retail.posterminal/?terminal=VBS-1#login
Usuario vallblanca
Password: openbravo




## Etendo 

### Configure Etendo Environment

Follow the steps in the [Install Etendo Development Environment Guide](../../../etendo-classic/getting-started/installation/install-etendo-development-environment.md) for development setup in JAR format.

Ahora debemos crear un dump de la base de datos de Openbravo para restaurar en Etendo y conservar todos los datos maestros en una terminal en el proyecto etendo Etjecutamos: 

```bash title="Terminal"
pg_dump -U tad -p 5432 -F c -b -v -f ./openbravo.dump  openbravo
```
Una vez que tenemos el Entorno levantado instalamos el Bundle de Plataforma, 

```groovy title=build.gradle
implementation ('com.etendoerp:financial.extensions:latest.release')
implementation ('com.etendoerp:financial.extensions:latest.release')
```

Ademas en el archivo gradle.properties se deben agregar las siguientes variables de configuracion, para ejecutar todos los servicios necesarios dockerizados:

``` groovy title=gradle.properties

docker_com.etendoerp.docker_db=true
docker_com.etendoerp.etendorx=true
docker_com.etendoerp.etendorx_async=true
docker_com.etendoerp.etendorx_connector=true
docker_com.etendoerp.tomcat=true
docker_com.etendoerp.integration.to_openbravo=true

etendorx.dependencies=com.etendorx.integration.to_openbravo:mapping:1.0.0, com.etendorx.integration.to_openbravo:worker:1.0.0
etendorx.basepackage=com.etendorx.integration.to_openbravo.mapping

```

!!! warning
Como el servicio de base de datos correra dockerizado y se asume que Openbravo esta intalado en un Postgres local en el puerto 5432, cambiaremos el puerto de la base de datos de Etendo a `ddbb.port=5434` para que al levantarse el servicio de Postgres dockerizado lo haga en ese puerto.

./gradlew setup  // Para aplicar los cambios en las configuraciones del gradle.properties
./gradlew resources.up // Para levantar todos los servicios dockerizados

Ahora restauraremos la base de datos de Openbravo, cambiando el nombre por defecto a etendo, o el nombre que se defina en el ddbb.sid 

PGPASSWORD=syspass psql -U postgres -d postgres -h localhost -p 5434
CREATE ROLE tad LOGIN PASSWORD 'tad' SUPERUSER CREATEDB CREATEROLE VALID UNTIL 'infinity';
CREATE DATABASE etendojar WITH ENCODING='UTF8' OWNER=tad;
pg_restore -v -U tad -d etendojar -h localhost -p 5434 -v -O openbravo.dump
pasword:tad

Luego debemos borrar el contenido de algunas tablas

PGPASSWORD=tad psql -U tad -d etendojar -h localhost -p 5434
TRUNCATE TABLE m_offer, obuiapp_gc_tab, obuiapp_gc_field CASCADE;


Ahora vamos a compilar el entorno, forzando el update.database ya que los modulos de retail no estan en Etendo pero queremos conservar los datos maestros. 
```bash title="Terminal"
./gradlew update.database -Dforce=yes compile.complete smartbuild
````
Una vez compilado el entorno, se levanta el Tomcat y veremos 
!!! info 
    Access Etendo at: [http://localhost:8080/etendo](http://localhost:8080/etendo)
    User:admin
    Password: admin

### Aplicar Configuraciones

cd modules/com.etendoerp.integration.to_openbravo/utils
make set_wal
make insert
make setupconnector


### 5. Verify Middleware Configuration
Ensure Etendo RX middleware is configured to handle synchronization between Openbravo and Etendo. Update any required endpoints and authorization tokens.

### 6. Testing the Integration
#### Generating Documents in Openbravo POS
1. Log in to the Openbravo POS terminal.
2. Perform a sales transaction or any activity that generates a document.
3. Confirm that the document is synchronized to the Etendo environment.

#### Verifying Synchronization
1. Check the Etendo environment for the synchronized document.
2. Review logs in Etendo RX middleware to ensure smooth data flow.

## Additional Notes
- Logs can be enabled in Etendo by modifying the `config/log4j2-web.xml` file:

  ```xml
  <AppenderRef ref="Console"/>
  ```

- Run the `smartbuild` task after updating configurations:

  ```bash
  ./gradlew smartbuild --info
  ```

## Troubleshooting
- Ensure all services (Openbravo, Etendo RX, and Etendo) are running correctly.
- Verify database connections and network configurations.

## Default Credentials
- **Openbravo POS**: Default credentials vary based on setup.
- **Etendo**:
  - Username: `admin`
  - Password: `admin`

## References
- Openbravo Documentation
- Etendo Installation Guide
- PostgreSQL Official Documentation
