---
title: Requirements
---
## Overview

This section explains the stack of tools and requirements to install Etendo.

## Client: web browsers

|     |     |     |     |
| --- | --- | --- | --- |
| **Web browser** |     | **Minimum required** | **Recommended version** |
| ![Chrome logo.png](../assets/drive/mOCl2euDZU8wO2MedNIrplZBmdiqguZm86ab6e3RVnKM4B4uX3s0UMMf0FVPIYLYeHmFy8FHPMNsJ9nOX6rXZAo76IzmQSSPrrN2DgNiD3DrJIG2j25JRJvASy7yiBGzsJBRp2Cg.png) | **Google Chrome** | 95  | **97 or higher** |
| ![Safari icon large.png](../assets/drive/JVloGgFusza-4BFZ30Gjra-m_4Aknv5c3Y5vJEoYZ4B4HiEV09e6bMcnSfyImo7D7TJbgPRsIIUScqqatrJBW8SoMV7HmSe3q12JLmaEp7AIYT2FSuLrjcz2mnT3fQ6NCMWg0zAu.png) | **Apple Safari** | 12  | **14 or higher** |
| ![Firefox logo 2017.png](/assets/drive/p3EzTz7im_NXkvyXHa5aIk29Va-vEN-96NUPsPr1BLqnWL7AA6CuewRnASM9EfEyMxRmaGmq3pNHPbAqNy2ZJL6xAuEUtM5q10QXfcadnvVJwW7-ISmAZ9xNgbOSs3XwSDsppY1P.png) | **Mozilla Firefox ESR** | 78  | **90 or higher** |
| ![Microsoft Edge logo.png](/assets/drive/acUA_bLGo6j1tRenMx_zSRQddDaf2N86N0iL2cT5o5Om5Gc96_YzQ0HOZ_CdZAitgs1m6M24Nbk5cbs1Et2I0MrUPB1a5sapBINQg_4Jzg8C_aoCmS3-CaKmn8BItB4O25SvFpy6.png) | **Microsoft Edge (Chromium based)** | 95  | **97 or higher** |

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

## Server: software stack

| Stack component | Supported versions | Recommended version | Instalation Guide |
| :--- | :--- | :--- | :--- |
| :fontawesome-brands-java:  Java SE | 11  | Latest 11.x | [Java Instalation Guide](https://www.java.com/en/download/manual.jsp){target="_blank"} |
| :simple-postgresql:  PostgreSQL | 10.x, 11.x, 12.x, 13.x, Amazon RDS | Latest 14.x | [Postgres Instalation Guide ](https://www.postgresql.org/download/){target="_blank"} |
| :simple-apachetomcat:  Apache Tomcat | 8.5.x (x >= 24), 9.0.x | Latest 9.0.x | [Tomcat Instalation Guide](https://tomcat.apache.org/download-90.cgi){target="_blank"} |
| :simple-oracle:  Oracle | 19c (LTS) | 19c (LTS) |