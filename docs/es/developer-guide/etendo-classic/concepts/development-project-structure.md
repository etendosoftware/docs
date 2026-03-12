---
title: Estructura del proyecto de desarrollo
tags:
    - Desarrollo
    - Proyecto
    - Estructura
    - Diccionario de la aplicación

status: beta
---

#  Estructura del proyecto de desarrollo

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

##  Visión general

Esta sección describe la estructura de un proyecto de desarrollo de Etendo. Etendo tiene una estructura de directorios en árbol que divide lógicamente diferentes componentes del núcleo (`XmlEngine`, `SQLC`, `HttpBaseServlet`) y WAD (Wizard for Application Dictionary) del propio Etendo (formularios, informes, call-outs, combos, procesos, etc.).

##  Estructura del proyecto

A continuación se muestra una instantánea de la estructura del proyecto de desarrollo de Etendo.

```
etendo  
    |-build
    |-config
    |-docs
    |-legal
    |-lib
    |-modules
    |-referencedata
    |-src
    |-src-core
    |-src-db
    |-src-gen
    |-src-test
    |-src-trl
    |-src-util
    |-src-wad
    |-srcAD
    |-temp
    |-web
    |-WebContent
```

###  Build

El directorio **build** contiene la subcarpeta `classes`, donde se copian todas las clases Java compiladas después de ejecutar las tareas de compilación de ant. Además, el código fuente Java que se genera a partir de los archivos `.xsql` de la aplicación durante la fase `sqlc` de la build del proyecto se escribe en la subcarpeta `javasqlc`.

```
|-build
    |-classes
    |-org
        ...
    |-javasqlc
    |-src
    |-srcAD
```

###  config

El directorio **config** contiene los archivos de configuración de Etendo. El directorio config es donde se descarga y desde donde se ejecuta el script de instalación. Otros archivos de configuración en el directorio config incluyen el archivo de propiedades de la aplicación, `Openbravo.properties`, que se genera tras ejecutar el proceso `./gradlew setup`, y los archivos de propiedades de logging y planificación (`log4j.lcf` y `quartz.properties`). En esta carpeta hay varios archivos .template (`Openbravo.properties.template`, `Format.xml.template`, `log4j.lcf.template`, etc.), que necesitan tener sus archivos correspondientes (Openbravo.properties, Format.xml, etc.) para que Etendo funcione correctamente.

```
|-config
    |-log4j.lcf
    |-Openbravo.properties
    |-quartz.properties
    |-...
```

###  docs

El directorio **docs** contiene la documentación de la API de Etendo, que puede generarse utilizando la herramienta [Javadoc](https://www.oracle.com/java/technologies/){target="\_blank"}. Esta documentación puede generarse ejecutando el comando `ant generate.java.doc`.

###  legal

El directorio **legal** contiene una colección de licencias de las distintas bibliotecas que utiliza Etendo.

###  lib

El directorio **lib** contiene todas las bibliotecas Java jar utilizadas en toda la aplicación. Se divide en build y runtime, siendo **build** el que contiene las bibliotecas utilizadas durante la compilación de Etendo, y **runtime** el que contiene los archivos jar que se utilizan durante la ejecución de la aplicación.

```
|-lib
|-build
|-runtime
```

###  Módulo

El directorio **modules** es donde se ubican los módulos que usted haya instalado o desarrollado. Cada módulo tiene un directorio de nivel superior nombrado según el paquete Java especificado en su descripción del módulo y, por debajo, un diseño similar a la estructura de desarrollo del núcleo, que en sí misma es un módulo. Al desarrollar un módulo en el Diccionario de la aplicación, cuando el módulo se exporta, se exportará aquí, al directorio modules.

A continuación se muestra la estructura de un módulo de ejemplo.

```
|-modules
|-com.etendoerp.examples.helloworld 
    |-src
        ...
    |-src-db
        |-database
            |-model
            |-sourcedata
    |-web
        ...
    |-lib
        |-runtime
        |-build
```

En Etendo, hay varios módulos dentro de la carpeta modules/ que ahora forman parte de la distribución estándar.

### referencedata

El directorio **referencedata** contiene datos de referencia específicos de la implementación, como estructuras contables, informes, listas de productos o listas de precios, etc. Los módulos de datos de referencia son una forma cómoda de cargar datos de referencia en Etendo. Puede encontrar más información sobre esto [aquí](../concepts/datasets.md).

```
referencedata
    |-sampledata
    |-standard
```

###  src

El directorio **src** es el directorio de nivel superior de la base principal de código fuente del proyecto Etendo. Contiene el código fuente de todos los componentes que conforman las ventanas clásicas de la aplicación web de Etendo, así como servicios, incluidos formularios, informes, call-outs, combos, Data Access Layer (DAL), procesos, ventanas manuales, archivos xsql y HTML, informes, etc.

```
|-src
    |-org
    |-etendo
        |-authentication
        |-base
        |-dal
        |-erpCommon
            |-ad_actionButton
            |-ad_callouts
            ...
            |-ad_reports
        |-erpReports
        |-scheduling
        |-services
```
    

El `ad_ prefix` (en carpetas/paquetes erpCommon) denota el Diccionario de la aplicación. Los sufijos de los nombres de directorio son bastante autoexplicativos. La diferencia entre `ad_reports` y erpReports radica en la forma en que accedemos a un informe dentro de la aplicación. Si es accesible directamente a través del menú, entonces debería estar en `ad_reports`. Por otro lado, algunas ventanas (facturas, pedidos, etc.) tienen un icono de Imprimir en la barra de herramientas, que genera un informe. Estos informes deberían almacenarse en erpReports.

###  src-core

El directorio **src-core** contiene el código fuente de los componentes del núcleo: XmlEngine (Vista), [SQLC](../concepts/sqlc.md) (Modelo), HttpBaseServlet (Controlador) y ConnectionPool.   

```
|-src-core
    |-src
    |-org
        |-openbravo
            |-base
                ...
                |-HttpBaseServlet.java
                |-HttpBaseUtils.java
                ...
            |-data
                |-Sqlc.java
            |-database
            |-exception
            |-utils
            |-xmlEngine
```
    

###  src-db

El directorio **src-db** contiene la biblioteca dbsourcemanager. También contiene el directorio **database**, que es donde se encuentran todos los datos del modelo (estructura: tablas, restricciones, procedimientos y triggers), los datos de ejemplo (datos de Etendo como productos, terceros, etc.) y los datos fuente (metadatos de ventanas y pestañas) en archivos *.xml en texto plano.

```
|-src-db
    |-build
    |-database
    |-lib
        |-dbsourcemanager.jar
    |-model
    |-sourcedata
```

###  src-util

La carpeta src-util contiene la herramienta de diagnóstico, las validaciones de build y los scripts de módulo. El directorio **diagnostic** contiene el código/herramienta para ejecutar una prueba de diagnóstico sobre su configuración e informar de cualquier problema o elemento que no haya configurado correctamente. La herramienta de diagnóstico se ejecuta usando la tarea `ant diagnostic` desde el directorio raíz de Etendo. Puede encontrar más información sobre qué son las validaciones de build y los scripts de módulo, y cómo crear uno, [aquí](../how-to-guides/how-to-create-build-validations-and-module-scripts.md).

```
src-util
|-buildvalidation
|-diagnostics
    |-build
    |-config
    |-src
    |-WebContent
|-modulescript
```
    
###  src-gen

El directorio **src-gen** contiene los objetos del modelo DAL generados a partir del modelo de Etendo (tablas, columnas, referencias, etc.) durante la tarea ant generate.entities.

```
src-gen
    |-org
    |-openbravo
        |-model
```
    
###  **src-test**

El directorio **src-test** contiene el código fuente de pruebas, como pruebas y suites de JUnit.

```
src-test
    |-src
    |-com
        |-etendoerp
        |-test
            |-base
            |-dal
            |-expression
            ...
```

###  src-trl

El directorio **src-trl** contiene el código fuente del código que genera entradas en la base de datos para cada cadena traducible en archivos html, jrxml, fo y srpt.

```
|-src-trl
    |-src
    |-org
        |-openbravo
            |-translate
```

###  src-wad

El directorio **src-wad** contiene el código fuente de WAD (Wizard for Application Dictionary), que se utiliza para generar archivos de ventanas clásicas a partir de la información de definición de ventanas del Diccionario de la aplicación.

```
|-src-wad
    |-src
    |-org
        |-openbravo
            |-wad
```

###  srcAD

El directorio **srcAD** contiene todo el código generado automáticamente a partir del Diccionario de la aplicación.

###  temp

Carpeta temporal que contiene archivos que no se confirman en Mercurial. Se crea solo cuando es necesario, por ejemplo, cuando se descargan archivos obx desde el Repositorio Central.

###  web

El directorio **web** contiene todos los recursos web, como hojas de estilo en cascada (`CSS`), código `Javascript`, imágenes y ventanas emergentes.

```
web
|-images
|-js
|-popups
|-skins
```
    
###  WebContent

Es la carpeta de salida web para IntelliJ; la carpeta de salida define la webapp utilizada por la integración de IntelliJ con Tomcat. Contiene WEB-INF (con web.xml y otros archivos importantes) y META-INF.

---

Este trabajo es una obra derivada de [Development Project Structure](http://wiki.openbravo.com/wiki/Development_Project_Structure){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.