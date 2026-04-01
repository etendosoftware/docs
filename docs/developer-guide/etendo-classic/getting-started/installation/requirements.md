---
title: Requirements

tags:
    - Etendo Requirements
    - Web Browsers
    - Network Connectivity
    - Java Platform
    - Software Stack
    - Etendo Classic
    - Requirements
    - Etendo 26
    - Migrate to Etendo 26
---
## Overview

This section explains the stack of tools and requirements to install Etendo.

## Client: web browsers

|     |     |     |     |
| --- | --- | --- | --- |
| **Web browser** |     | **Minimum required** | **Recommended version** |
| ![Chrome logo.png](../../../../assets/drive/mOCl2euDZU8wO2MedNIrplZBmdiqguZm86ab6e3RVnKM4B4uX3s0UMMf0FVPIYLYeHmFy8FHPMNsJ9nOX6rXZAo76IzmQSSPrrN2DgNiD3DrJIG2j25JRJvASy7yiBGzsJBRp2Cg.png) | **Google Chrome** | 95  | **97 or higher** |
| ![Safari icon large.png](../../../../assets/drive/JVloGgFusza-4BFZ30Gjra-m_4Aknv5c3Y5vJEoYZ4B4HiEV09e6bMcnSfyImo7D7TJbgPRsIIUScqqatrJBW8SoMV7HmSe3q12JLmaEp7AIYT2FSuLrjcz2mnT3fQ6NCMWg0zAu.png) | **Apple Safari** | 12  | **14 or higher** |
| ![Firefox logo 2017.png](../../../../assets/drive/p3EzTz7im_NXkvyXHa5aIk29Va-vEN-96NUPsPr1BLqnWL7AA6CuewRnASM9EfEyMxRmaGmq3pNHPbAqNy2ZJL6xAuEUtM5q10QXfcadnvVJwW7-ISmAZ9xNgbOSs3XwSDsppY1P.png) | **Mozilla Firefox ESR** | 78  | **90 or higher** |
| ![Microsoft Edge logo.png](../../../../assets/drive/acUA_bLGo6j1tRenMx_zSRQddDaf2N86N0iL2cT5o5Om5Gc96_YzQ0HOZ_CdZAitgs1m6M24Nbk5cbs1Et2I0MrUPB1a5sapBINQg_4Jzg8C_aoCmS3-CaKmn8BItB4O25SvFpy6.png) | **Microsoft Edge (Chromium based)** | 95  | **97 or higher** |

## Client: network connectivity

Here, there are example configurations, depending on the number of concurrent users to be supported. These assume the server is hosted with a fast connection, so it's network is not a limiting factor.

| Downstream bandwidth | Concurrent users |
| --- | --- |
| 3Mbit/s | <=10 |
| 10MBit/s | <=20 |
| 100MBit/s | <=100 |

## Server: Java based = multiplatform

Etendo runs wherever the Java JDK works. This currently means:

### Operating systems:
:material-microsoft-windows:  Windows <br>
:simple-linux:  Linux distribution <br>
:simple-freebsd:  FreeBSD <br>
:simple-macos:  Mac OSX <br>
Solaris and more.  <br>

### Architectures:
x86, x86\_64, IA64, Sparc, PowerPC, AIX.  
Either PostgreSQL should also be supported by your target system

## Software Stack

### Etendo 26

!!! warning "Breaking Change: Java 17 is Now Mandatory"
    Starting with **Etendo 26**, Java 11 is no longer supported. Java 17 or higher is required to build and run Etendo 26. See [API Changes - Etendo 26](../../developer-changelog/apichanges.md#etendo-26) for migration details.

| Stack component | Supported versions | Recommended version | Installation Guide |
| :--- | :--- | :--- | :--- |
| :fontawesome-brands-java:  Java SE | 17 | 17.0.14 or higher | [Java Installation Guide](https://www.oracle.com/java/technologies/downloads/#java17){target="_blank"} |
| :simple-postgresql:  PostgreSQL | 16.x, 17.x, Amazon RDS | Latest 17.x | [Postgres Installation Guide](https://www.postgresql.org/download/){target="_blank"} |
| :simple-apachetomcat:  Apache Tomcat | 9.0.x | Latest 9.0.x | [Tomcat Installation Guide](https://tomcat.apache.org/download-90.cgi){target="_blank"} |
| :simple-gradle:  Gradle | 8.12.1 | 8.12.1 | [Gradle Docs](https://docs.gradle.org/8.12.1){target="_blank"} |
| :material-database:  Oracle | 19c (LTS) | 19c (LTS) | |

### Etendo 25

| Stack component | Supported versions | Recommended version | Installation Guide |
| :--- | :--- | :--- | :--- |
| :fontawesome-brands-java:  Java SE | 17  | Latest 17.x | [Java Installation Guide](https://www.oracle.com/java/technologies/downloads/#java17){target="_blank"} |
| :simple-postgresql:  PostgreSQL | 14.x, 16.x, Amazon RDS | Latest 16.x | [Postgres Installation Guide ](https://www.postgresql.org/download/){target="_blank"} |
| :simple-apachetomcat:  Apache Tomcat | 9.0.x | Latest 9.0.x | [Tomcat Installation Guide](https://tomcat.apache.org/download-90.cgi){target="_blank"} |
| :simple-gradle:  Gradle | 8.12.1 | 8.12.1 | [Gradle Docs](https://docs.gradle.org/8.12.1){target="_blank"} |
| :material-database:  Oracle | 19c (LTS) | 19c (LTS) | |

### Etendo 24 and earlier (Deprecated)

!!!failure "Deprecated"
    Etendo 24 and earlier are no longer supported. Upgrade to Etendo 25 or higher. See the [Upgrade Guide](../upgrade/upgrade-etendo-to-any-version.md) for instructions.

| Stack component | Supported versions | Recommended version | Installation Guide |
| :--- | :--- | :--- | :--- |
| :fontawesome-brands-java:  Java SE | 11  | Latest 11.x | [Java Installation Guide](https://www.java.com/en/download/manual.jsp){target="_blank"} |
| :simple-postgresql:  PostgreSQL | 10.x, 11.x, 12.x, 13.x, Amazon RDS | Latest 14.x | [Postgres Installation Guide ](https://www.postgresql.org/download/){target="_blank"} |
| :simple-apachetomcat:  Apache Tomcat | 8.5.x (x >= 24) | Latest 8.5.x | [Tomcat Installation Guide](https://tomcat.apache.org/download-80.cgi){target="_blank"} |
| :simple-gradle:  Gradle | 7.3.2 | 7.3.2 | [Gradle Docs](https://docs.gradle.org/7.3.2){target="_blank"} |
| :material-database:  Oracle | 19c (LTS) | 19c (LTS) | |

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

