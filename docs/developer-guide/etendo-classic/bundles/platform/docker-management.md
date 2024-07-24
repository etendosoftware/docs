---
tags:
  - Docker
  - Management
  - Module
  - Compose
---

# Docker Management

## Overview

Docker is a platform that enables developers to automate the deployment, scaling, and management of applications. It uses containerization technology, which packages an application and its dependencies into a standardized unit called a "container." Containers can run consistently across different computing environments, making them highly portable and efficient.

The `com.etendoerp.docker` module introduces new tasks to Etendo Classic and the infrastructure needed to launch all the necessary containers. This module operates incrementally, and there are additional modules that extend functionality using the same format. For instance, by using the `com.etendoerp.tomcat` module, you can add the functionality of using Tomcat within Docker. There are several similar modules available that extend various functionalities.

## Prerequisites

Docker and Docker Compose must be installed on your system.

## Installation and Setup

1. Adding the Module

    To add the `com.etendoerp.docker` module as a dependency to your ERP, include it in your project's build configuration and add `docker_com.etendoerp.docker_db=true` in **gradle.properties** file

2. Installing Additional Modules

    You can enhance the functionality by installing related modules. For example:

    com.etendoerp.tomcat: Adds the capability to use Tomcat within Docker

    And docker_com.etendoerp.tomcat=true in gradle.properties file.

    Then, run ./gradlew deploy to compile and deploy etendo classic on tomcat container

3. Executing the Tasks

Once the `com.etendoerp.docker` module and any other related modules are installed and configured, execute the following command to initiate the derived infrastructure:

Running

./gradlew resources.up
If you only have the base `com.etendoerp.docker` module installed, this command will start a PostgreSQL database.

Stopping
Execute:

./gradlew resources.stop
This command will stop all containers.

Down
Execute:

./gradlew resources.down
This command will stop and remove all containers.

## Verifying the Status

To verify the status of the resources started by Docker Compose, you can use the following Docker commands:

`docker ps`

This command lists all running Docker containers. You should see the containers related to your ERP system.

`docker compose logs`

This command shows the logs of all the services defined in your Docker Compose configuration, which can help in troubleshooting and verifying that the services are running correctly.

---

How to extend
On a module level, create a new folder called compose and add a <>.yml file with the configuration of the new service.

Example:

module/com.etendoerp.busybox/compose/com.etendoerp.busybox.yml

services:
  busybox:
    image: busybox:latest
    command: [ "/bin/busybox", "watch", "ls", "-l" ]
