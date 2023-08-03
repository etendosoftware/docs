---
title: Zapier Integration
---

## Overview

This page explains the Zapier integration architecture developed in EtendoRx platform and how to set up and run the service.

!!! info
    You could try the Etendo Zapier Integration using a demo environment following the functional documentation [Setup an Etendo Zap](/docs/legacy/end-user-documentation/integrations/zapier).

## Zapier Integration

### Infrastructure

<img src="/technicaldocumentation/platform/gra%CC%81fico_wik-05.png" alt="drawing" width="500"/>

Infraestructura

### Etendo Rx

Etendo Rx is the development platform, where the Zapier Integration service is developed. This platform provides some services which simplify the comunication, security and access layers.  
For more information read [EtendoRX](/docs/legacy/technical-documentation/etendo-environment/platform/EtendoRx)

This connector uses the following services:

- Edge: Ingress service.
- Auth: Service encharged on security layer.
- DAS: Communication service to read, write and update the Database.
- Debezium: Service that listens database changes and enqueues these changes reactively in a queuing system [Debezium Docs](https://debezium.io/documentation/reference/1.9/).
- Kafka: Queue managenment service [Kafka Docs](https://kafka.apache.org/30/documentation.html)

### Docker deployment

#### Requirements

!!! info
    You need [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) latest 1.29.x version or grather

#### Run dockerization

Etendo distributes a Docker Compose with all the services that need to execute the Zapier Connector.

1.  Clone the main and default configuration repositories

```plaintext
git clone https://github.com/etendosoftware/etendo_rx_compose.git etendo_rx_compose
cd etendo_rx_compose
git clone https://github.com/etendosoftware/etendorx_default_config main/rxconfig
```

!!! failure
    The public and private keys needed to autenticate the connections are distributed by default in the `etendorx_default_config` reporitory, this credentials are only to **demo porpouse**, in other case you have to generate a new one keys following the guide [Setup Etendo Rx autentication keys](/docs/legacy/end-user-documentation/integrations/zapier/setup-etendorx-autentication-keys)

3.  To run the dockerization execute:

```
docker-compose -p rx -f main/docker-compose.yaml --profile zapier up -d
```

| Profile | Services                                                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| NONE    | **zookeeper** <br> **kafka** <br> **debezium** <br> **postgres**                                                                            |
| base    | zookeeper <br> kafka <br>debezium <br>postgres <br> **config** <br>**das** <br> **auth** <br> **edge**                                      |
| zapier  | zookeeper <br> kafka <br> debezium <br> postgres <br> config <br> das <br> auth <br> edge <br> **zapier**                                   |
| all     | zookeeper <br> kafka <br> debezium <br> postgres <br> config <br> das <br> auth <br> edge <br> zapier <br> **debezium-ui** <br> **kafdrop** |

4. Wait until `das` service are running (healthy), to check that:

```
watch 'docker ps --format "table {{.Names}}\t {{.Status}}" --filter name=rx-das-1'
```

4. Execute `create-connector.sh` to create the default configuration of debezium

```
./main/create-connector.sh
```

### Etendo Classic

1. An Etendo instance with the Zapier Integration `com.etendoerp.integration.zapier` module in its latest version is necessary.
   Follow the guide [Install Etendo in JAR format](/docs/legacy/technical-documentation/etendo-environment/setup-and-upgrade/installation#install-etendo-in-jar-format) and include the following in the step where the build.gradle is changed:

```plaintext
plugins {
  id 'java'
  id 'war'
  id 'maven-publish'
  id 'com.etendoerp.gradleplugin' version '1.0.2'
}

dependencies {
  implementation group: 'com.etendoerp.platform', name: 'etendo-core', version: '22.1.2'
  implementation 'com.etendoerp:integration.zapier:1.0.3'
}
```

2. In the step to modify the `gradle.properties` file you have change the `ddbb.port` to `5470`, because the database used will be working in Docker.

```
...
bbdd.sid=etendo
bbdd.port=5470
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
...
```

3. Start the tomcat and setup the default organization and default client to the user who will sinchoronize with Zapier.
   You can set deafault configuration in the top navegation checking the check "set as default" or navegate to user -> select a user -> and edit the role, default organization and default client.

<img src="/technicaldocumentation/integrations/zapier/defaultorgclient.png" alt="drawing" width="300"/>

## Setup a new Zap

Set up a Zap connecting Etendo with other Zapier application like Google Contacts following the guide [Setup an Etendo Zap](/docs/legacy/end-user-documentation/integrations/zapier)
