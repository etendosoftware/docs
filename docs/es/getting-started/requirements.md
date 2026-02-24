---
title: Requisitos

tags:
    - Requisitos de Etendo
    - Navegadores web
    - Conectividad de red
    - Plataforma Java
    - Pila de software
    - Etendo Classic
    - Requisitos
---
## Visión general

Esta sección explica la pila de herramientas y los requisitos para instalar Etendo.

## Cliente: navegadores web

|     |     |     |     |
| --- | --- | --- | --- |
| **Navegador web** |     | **Mínimo requerido** | **Versión recomendada** |
| ![Chrome logo.png](../assets/drive/mOCl2euDZU8wO2MedNIrplZBmdiqguZm86ab6e3RVnKM4B4uX3s0UMMf0FVPIYLYeHmFy8FHPMNsJ9nOX6rXZAo76IzmQSSPrrN2DgNiD3DrJIG2j25JRJvASy7yiBGzsJBRp2Cg.png) | **Google Chrome** | 95  | **97 o superior** |
| ![Safari icon large.png](../assets/drive/JVloGgFusza-4BFZ30Gjra-m_4Aknv5c3Y5vJEoYZ4B4HiEV09e6bMcnSfyImo7D7TJbgPRsIIUScqqatrJBW8SoMV7HmSe3q12JLmaEp7AIYT2FSuLrjcz2mnT3fQ6NCMWg0zAu.png) | **Apple Safari** | 12  | **14 o superior** |
| ![Firefox logo 2017.png](../assets/drive/p3EzTz7im_NXkvyXHa5aIk29Va-vEN-96NUPsPr1BLqnWL7AA6CuewRnASM9EfEyMxRmaGmq3pNHPbAqNy2ZJL6xAuEUtM5q10QXfcadnvVJwW7-ISmAZ9xNgbOSs3XwSDsppY1P.png) | **Mozilla Firefox ESR** | 78  | **90 o superior** |
| ![Microsoft Edge logo.png](../assets/drive/acUA_bLGo6j1tRenMx_zSRQddDaf2N86N0iL2cT5o5Om5Gc96_YzQ0HOZ_CdZAitgs1m6M24Nbk5cbs1Et2I0MrUPB1a5sapBINQg_4Jzg8C_aoCmS3-CaKmn8BItB4O25SvFpy6.png) | **Microsoft Edge (basado en Chromium)** | 95  | **97 o superior** |

## Cliente: conectividad de red

Aquí se muestran configuraciones de ejemplo, en función del número de usuarios concurrentes que se deban soportar. Estas asumen que el servidor está alojado con una conexión rápida, por lo que su red no es un factor limitante.

| Ancho de banda de bajada | Usuarios concurrentes |
| --- | --- |
| 3Mbit/s | <=10 |
| 10MBit/s | <=20 |
| 100MBit/s | <=100 |

## Servidor: basado en Java = multiplataforma

Etendo se ejecuta allí donde funcione el Java JDK. Actualmente, esto significa:

### Sistema operativo:
:material-microsoft-windows:  Windows <br>
:simple-linux:  Distribución Linux <br>
:simple-freebsd:  FreeBSD <br>
:simple-macos:  Mac OSX <br>
Solaris y más.  <br>

### Arquitecturas:
x86, x86\_64, IA64, Sparc, PowerPC, AIX.  
Además, PostgreSQL también debería estar soportado por su sistema de destino

## Pila de software

### Etendo 25

| Componente de la pila | Versiones soportadas | Versión recomendada | Guía de instalación |
| :--- | :--- | :--- | :--- |
| :fontawesome-brands-java:  Java SE | 17  | Última 17.x | [Guía de instalación de Java](https://www.oracle.com/java/technologies/downloads/#java17){target="_blank"} |
| :simple-postgresql:  PostgreSQL | 14.x, 16.x Amazon RDS | Última 16.x | [Guía de instalación de Postgres ](https://www.postgresql.org/download/){target="_blank"} |
| :simple-apachetomcat:  Apache Tomcat | 9.0.x | Última 9.0.x | [Guía de instalación de Tomcat](https://tomcat.apache.org/download-90.cgi){target="_blank"} |
| :simple-gradle:  Gradle | 8.12.1 | 8.12.1 | [Documentación de Gradle](https://docs.gradle.org/8.12.1){target="_blank"} |
| :material-database:  Oracle | 19c (LTS) | 19c (LTS) |

### Etendo 24 y anteriores

| Componente de la pila | Versiones soportadas | Versión recomendada | Guía de instalación |
| :--- | :--- | :--- | :--- |
| :fontawesome-brands-java:  Java SE | 11  | Última 11.x | [Guía de instalación de Java](https://www.java.com/en/download/manual.jsp){target="_blank"} |
| :simple-postgresql:  PostgreSQL | 10.x, 11.x, 12.x, 13.x, Amazon RDS | Última 14.x | [Guía de instalación de Postgres ](https://www.postgresql.org/download/){target="_blank"} |
| :simple-apachetomcat:  Apache Tomcat | 8.5.x (x >= 24) | Última 8.5.x | [Guía de instalación de Tomcat](https://tomcat.apache.org/download-80.cgi){target="_blank"} |
| :simple-gradle:  Gradle | 7.3.2 | 7.3.2 | [Documentación de Gradle](https://docs.gradle.org/7.3.2){target="_blank"} |
| :material-database:  Oracle | 19c (LTS) | 19c (LTS) | |

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.