---
title: Conceptos principales de desarrollo
tags:
    - Desarrollo 
    - Conceptos
    - Open Source
    - Modularidad

status: beta
---

#  Conceptos principales de desarrollo

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

##  Principios de diseño

Etendo es una aplicación de software que se está desarrollando teniendo en cuenta los siguientes principios de diseño:

- Open Source
- Framework de aplicación ERP 
- [Desarrollo dirigido por modelos](https://en.wikipedia.org/wiki/Model-driven_engineering){target="\_blank"}
- [Modularidad](../concepts/modularity-concepts.md) 
- [Aplicación de Internet enriquecida (RIA)](../concepts/etendo-architecture.md#smartclient) 
- Java - J2EE ligero 
- Soporte para múltiples bases de datos

El objetivo de Etendo es, siguiendo estos principios, ofrecer una aplicación que sea de vanguardia tanto desde el punto de vista tecnológico como funcional.

### Open Source

Etendo es un proyecto open source construido sobre tecnologías open source. Nuestro objetivo es aprovechar los excelentes componentes de infraestructura desarrollados por la comunidad open source para garantizar que nuestra plataforma se beneficie de las ventajas y la estabilidad de componentes respaldados por una gran comunidad. Siempre que sea necesario, contribuimos con nuestros desarrollos de vuelta a la comunidad.

### Framework de aplicación ERP

Etendo es una aplicación desarrollada mediante un framework de desarrollo integrado incluido en la distribución de Etendo. Este framework de desarrollo integrado se encarga de una amplia gama de aspectos en todas las áreas implicadas durante el proceso de desarrollo. Los más relevantes, de nivel bajo a nivel alto:

- Integración con [IntelliJ IDEA](../getting-started/installation/install-etendo-development-environment.md) 
- Integración con SCM (GitHub) 
- [Proceso de compilación automatizado](../developer-tools/etendo-gradle-plugin.md#build-tasks) 
- Proceso de actualización automatizado 
- Proceso de despliegue automatizado 
- Infraestructura integrada para varias necesidades comunes de desarrollo: 
    - Framework MVC (xmlEngine, httpBaseServlet, sqlc) 
    - [Capa de acceso a datos](../concepts/data-access-layer.md) (basada en [Hibernate](https://hibernate.org/){target="\_blank"}) 
    - Servidor web y contenedor de servlets (integración con [Apache-Tomcat](https://tomcat.apache.org/){target="\_blank"} y soporte para otras implementaciones J2EE) 
    - [Informes](../how-to-guides/how-to-create-a-report.md)(integración con el motor [JasperReports](https://community.jaspersoft.com/download-jaspersoft/){target="\_blank"}) 
    - [XML](../concepts/xml-rest-web-services) y [Servicios web JSON REST](./json-rest-web-services.md) 
    - Envío de correos electrónicos 
    - Planificación de procesos (integración con Quartz) 
- Framework de desarrollo MDD (Diccionario de la Aplicación de Etendo [Diccionario de la Aplicación](../concepts/data-model.md#application-dictionary)) 
- Soporte de interfaz de usuario multilingüe.
- Modelo de seguridad integrado.
- Modelo empresarial integrado. 
- Soporte multimoneda.
- Soporte multilibro mayor. 

###  Desarrollo dirigido por modelos

Etendo sigue un enfoque de [Desarrollo dirigido por modelos](../concepts/development-model.md#development-process) (MDD). Esto significa que Etendo utiliza un modelo agnóstico a la tecnología para definir componentes de la aplicación, como ventanas y procesos. Basándose en este modelo de aplicación, se generan código y otros artefactos de software.

La información del [modelo de datos de Etendo](../concepts/development-model.md) —la denominada metainformación (metadata)— se almacena en el Diccionario de la Aplicación de Etendo.

El Desarrollo dirigido por modelos tiene como objetivo aumentar la productividad y la reutilización mediante la separación de responsabilidades y la abstracción. El modelo es una definición abstracta de los componentes del sistema que contiene información suficiente para impulsar la generación de una (o más) implementaciones del sistema en una tecnología concreta.

Esta separación de responsabilidades —descripción funcional abstracta en el modelo e implementación de los componentes del modelo en una tecnología concreta— oculta las complejidades tecnológicas a los expertos del dominio ERP en su proceso de definir e implementar nueva funcionalidad ERP y simplifica la evolución de la tecnología de implementación.

En algunos casos es necesario codificar una solución externamente al modelo. Esto está totalmente soportado por Etendo. Los desarrolladores pueden desarrollar libremente sus propias soluciones sobre el stack tecnológico de Etendo.

###  Modularidad

La modularidad es una capacidad que permite definir y empaquetar funcionalidad adicional y configuraciones como módulos de extensión, de forma independiente del producto core.

La modularidad cambia la forma en que Etendo puede adaptarse a las necesidades del usuario. En lugar de personalizar el código para ajustarlo a los requisitos del usuario, es posible ampliar la funcionalidad y configurarla externamente —desde un módulo independiente—.

Este nuevo enfoque tiene varias ventajas. Las más importantes:

- **Permite un desarrollo distribuido puro** : la nueva funcionalidad puede desarrollarse mediante módulos de forma puramente distribuida. El equipo que desarrolla el módulo puede trabajar aislado de otros equipos —solo necesita una API estable de los otros módulos que utiliza— y el ciclo de vida de este módulo —incluidas las versiones— es independiente de otros módulos. 
- **Mejora enormemente el mantenimiento del código** : desarrollar mediante módulos implica empaquetar de forma independiente. Con una definición adecuada de las dependencias del módulo y manteniendo estables las API, el proceso de actualización de una instancia es directo y puede realizarse con un solo clic del usuario. 
- **Fomenta el intercambio y la reutilización de nueva funcionalidad** : desarrollar mediante módulos hace que sea bastante sencillo compartir esta nueva funcionalidad con otras personas. Si los desarrolladores quieren compartir sus módulos, todo lo que necesitan es empaquetarlos y publicarlos en Etendo Forge (Repositorio central). Después, estos módulos estarán disponibles públicamente y otros usuarios podrán buscarlos e instalarlos mediante un proceso sencillo. 

###  Aplicación web pura - Cliente enriquecido

Etendo es, por su propia naturaleza, una aplicación web pura. La ubicuidad de los navegadores web proporciona un punto de acceso universal. Etendo entiende la red como una plataforma, ofreciendo y permitiendo a los usuarios utilizar aplicaciones completamente a través de un navegador.

Los requisitos son mínimos: un navegador web está disponible prácticamente en todos los sistemas informáticos. Además, al estar basado en web, el producto puede entregarse a través de Internet, lo que permite actualizar la aplicación sin distribuir e instalar software en potencialmente cientos de ordenadores cliente.

Tradicionalmente, las aplicaciones web tenían grandes limitaciones en lo relativo a la interfaz de usuario. Esto ha cambiado con la introducción de nuevas tecnologías web como AJAX. Con AJAX y frameworks similares, es posible desarrollar una interfaz enriquecida, interactiva y fácil de usar.

###  Java - J2EE ligero

Etendo utiliza Java como su lenguaje de programación de backend. Hay muchas razones para elegir Java como lenguaje del lado del servidor:

- Naturaleza open source 
- Amplio soporte para desarrollo a nivel empresarial 
- Arquitectura madura para aplicaciones web 

Etendo sigue la arquitectura Java 2 Enterprise Edition (J2EE) sin hacer uso del contenedor EJB. En su lugar, Etendo utiliza una infraestructura ligera para implementar el acceso a datos y la lógica de negocio. Etendo ha proporcionado una nueva Capa de acceso a datos [(DAL)](../concepts/data-access-layer.md) basada en Hibernate que ofrece un mecanismo de persistencia potente pero aun así ligero.

###  Soporte para múltiples bases de datos

Etendo está comprometido a evitar el bloqueo por proveedor en cualquier tecnología que utilice, incluida la base de datos. Etendo funciona sobre PostgreSQL (8.3.5+) y Oracle SE (10g-11g).

En versiones futuras, Etendo pretende ser independiente de la base de datos. La Capa de acceso a datos (DAL) basada en Hibernate es un primer paso en esa transición.

##  Conceptos principales de Etendo

###  Requisitos del sistema

Etendo se ejecuta sobre un grupo de aplicaciones de terceros bien conocidas:

- Apache-Tomcat. Usamos Apache Tomcat como contenedor de servlets, pero pueden utilizarse otros 
- Gradle 
- Base de datos PostgreSQL u Oracle SE 

Todas estas aplicaciones pueden instalarse tanto en Linux como en Windows.

###  Entorno de desarrollo

Los desarrolladores de Etendo tienen tres formas diferentes de desarrollar su código. Siguiendo el enfoque MDD, lo más común es editar el Diccionario de la Aplicación de Etendo a través de un navegador web conectado a Etendo. Basándose en la nueva definición del modelo, los artefactos de software pueden generarse automáticamente. Un desarrollador también puede conectarse directamente a la base de datos de Etendo mediante un cliente SQL (p. ej., `pgAdmin`, `sqlDeveloper`) para gestionar objetos del esquema de base de datos (tablas, procedimientos, etc.). Por último, los desarrolladores pueden desarrollar su propio código mediante un entorno de desarrollo integrado como Eclipse.

![](../../../assets/developer-guide/etendo-classic/concepts/main-development-concepts-0.png){: .legacy-image-style}

Todos los artefactos de software de Etendo se almacenan en archivos de texto dentro del proyecto de desarrollo. Esto incluye la definición y el contenido de la base de datos. La gran ventaja de utilizar archivos de texto para almacenar todos los artefactos de software es que resulta mucho más fácil compartir y comparar cambios realizados por desarrolladores en un entorno distribuido.

Etendo utiliza una herramienta llamada [DBSourceManager](../concepts/dbsourcemanager.md) para gestionar el código fuente de la base de datos. DBSourceManager es capaz de leer los objetos del esquema de base de datos y los datos del diccionario de aplicación y exportarlos a archivos xml. También puede crear o actualizar una base de datos de Etendo a partir de esos archivos xml.

El proceso para construir el sistema a partir del código fuente de Etendo incluye una serie de pasos para generar el código en diferentes niveles (DAL, WAD y otros) y ensamblar ese código con otro código escrito directamente por los desarrolladores. Etendo ha automatizado este proceso mediante una tarea ant.

![](../../../assets/developer-guide/etendo-classic/concepts/main-development-concepts-1.png){: .legacy-image-style}

###  Arquitectura

La nueva arquitectura se explica en el artículo [Arquitectura de Etendo](../concepts/etendo-architecture.md).

---

Este trabajo es una obra derivada de [Conceptos principales de desarrollo](http://wiki.openbravo.com/wiki/Main_Development_Concepts){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.