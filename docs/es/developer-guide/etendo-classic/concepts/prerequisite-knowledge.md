---
title: Conocimientos previos
tags:
    - Prerrequisito
    - Conocimiento
    - Conceptos
    - Base de datos
---

# Conocimientos previos

## Visión general

Esta sección enumera las principales áreas de conocimiento que son relevantes al desarrollar en/con Etendo. El nivel exacto de conocimiento requerido depende en gran medida de la tarea que se necesite realizar. Algunas tareas de desarrollo consistirán principalmente en cambios a través de la interfaz de usuario de Etendo, que requieren muy poco conocimiento técnico profundo. Otras tareas pueden ser más complejas y requerir cambiar o ampliar Etendo. En este último caso, también se requiere una comprensión técnica del producto Etendo.

## Conocimientos generales

Para desarrollar en/con Etendo, se requiere como mínimo tener una comprensión básica de la siguiente tecnología:

* [Java](https://dev.java/){target="\_blank"}: El lenguaje de programación utilizado en todos los componentes del lado del servidor de Etendo. Se utiliza en todos los niveles, desde los componentes del núcleo hasta la lógica de negocio del ERP. 
* [J2EE](https://www.oracle.com/java/technologies/){target="\_blank"}: La plataforma utilizada para la programación del servidor en el lenguaje Java; añade bibliotecas para proporcionar capacidades empresariales a aplicaciones Java que se ejecutan en un servidor de aplicaciones. 
* [Gradle](https://gradle.org/){target="\_blank"}: La herramienta utilizada para ejecutar las tareas de compilación relacionadas con Etendo, como compilar, desplegar en un servidor de aplicaciones, exportar e importar el esquema de la base de datos, etc. 
* [IntelliJ IDEA](https://www.jetbrains.com/idea/){target="\_blank"}: Un entorno de desarrollo integrado que ayuda en todas las tareas de desarrollo relacionadas con Etendo, como editar archivos fuente, depurar, ejecutar tareas de compilación, etc. 
* [SQL](https://en.wikipedia.org/wiki/SQL){target="\_blank"}: Un lenguaje declarativo informático de base de datos. Se utiliza en todos los componentes del lado del servidor de Etendo para acceder a los datos almacenados en los sistemas de gestión de bases de datos relacionales utilizados: PosgreSQL y Oracle. 
* [HTML](https://en.wikipedia.org/wiki/HTML){target="\_blank"}: El lenguaje de marcado utilizado para renderizar la interfaz de usuario de Etendo en el navegador web utilizado por los usuarios de Etendo. 
* [XML](https://en.wikipedia.org/wiki/XML){target="\_blank"}: El lenguaje de marcado utilizado para describir distintos documentos en Etendo, como servicios web REST, informes Jasper, archivos de configuración, archivos de plantilla, etc. 

## Base de datos

Si las tareas de desarrollo se centran principalmente en el área de base de datos, entonces un desarrollador también necesitará tener experiencia con:

* [PostgreSQL](https://www.postgresql.org/){target="\_blank"} o [Oracle](https://www.oracle.com/database/){target="\_blank"}: La base de datos de destino utilizada. 
* Conceptos de esquema de base de datos como restricciones, clave foránea, triggers, índices... 
* [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL){target="\_blank"}: El lenguaje utilizado para desarrollar lógica de negocio del lado de la base de datos. 

## UI / Código del lado del cliente

Etendo requiere un navegador web como Internet Explorer, Firefox, Chrome o Safari para renderizar la interfaz de usuario. Para desarrollos centrados en la interfaz de usuario, se requerirá experiencia con:

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript){target="\_blank"}: Un lenguaje de scripting utilizado por los navegadores web para proporcionar acceso a las páginas de la interfaz de usuario. Los desarrolladores deben ser capaces de leer, escribir y depurar código JavaScript utilizando las herramientas de desarrollo proporcionadas por los navegadores web. 
* [SmartClient](https://smartclient.com/){target="\_blank"}: El framework RIA en el que se basa Etendo; está basado en JavaScript e incluye una amplia colección de widgets y otras utilidades para el lado del cliente. 

## Capa de acceso a datos

Para desarrollos del lado del servidor en el lenguaje de programación Java que acceden a la base de datos, se utilizan las siguientes tecnologías:

* [Capa de acceso a datos](../concepts/data-access-layer.md): El componente de Etendo utilizado para reforzar el desarrollo de lógica de negocio en Java. 
* [Hibernate](https://hibernate.org/){target="\_blank"}: La biblioteca en la que se basa la Capa de acceso a datos, que proporciona mapeo objeto/relacional y permite a los desarrolladores utilizar un modelo de objetos para acceder a bases de datos relacionales. Para aprovechar al máximo la Capa de acceso a datos, es importante comprender sus conceptos principales para saber cómo crear consultas más avanzadas, especialmente el lenguaje de consultas de Hibernate ([HQL](https://docs.hibernate.org/core/3.6/reference/en-US/html/queryhql.html){target="\_blank"}) y la API de criterios de Hibernate. 

## Servicios web

Para consumir y ampliar los servicios web de Etendo, un desarrollador necesita tener conocimientos en las siguientes áreas:

* [REST](https://en.wikipedia.org/wiki/REST){target="\_blank"}: El estilo de arquitectura de software utilizado para proporcionar servicios web en Etendo. 
* [XML Schema](https://www.w3.org/TR/xmlschema-0/){target="\_blank"} para servicios web XML, para representar el tipo de medio XML proporcionado por este tipo de servicios web. 
* [JSON](https://en.wikipedia.org/wiki/JSON){target="\_blank"}: Un estándar basado en texto diseñado para el intercambio de datos; tiene una estrecha relación con JavaScript y se utiliza para servicios web JSON en Etendo. 

---

Este trabajo es una obra derivada de [Conocimientos previos](http://wiki.openbravo.com/wiki/Prerequisite_Knowledge){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.