---
title: Cómo crear un módulo
tags: 
  - Cómo
  - Modularidad
  - Crear un módulo
  - Módulo
---

# Cómo crear un módulo

## Visión general

Etendo utiliza el concepto de modularidad. La modularidad proporciona a los desarrolladores los medios para poder desarrollar, publicar y distribuir su trabajo de una manera estructurada y controlada. Para los usuarios de Etendo Classic, la modularidad hace posible descargar, instalar y actualizar desarrollos personalizados.

Esta sección describe cómo crear un módulo nuevo. Es de especial interés, ya que describe los primeros pasos que deben seguirse en todas las demás secciones de esta guía del desarrollador y, en general, en el desarrollo personalizado de Etendo Classic.

## Introducción a la modularidad

Los objetivos de la modularidad son:

  * Facilitar la contribución a Etendo Classic permitiendo un desarrollo y mantenimiento distribuido y desacoplado de funcionalidades opcionales. 
  * Proporcionar a la comunidad un conjunto amplio de extensiones para satisfacer sus requisitos empresariales únicos sin sobrecargar el producto Core. 
  * Acortar los ciclos de implantación permitiendo a los integradores de sistemas desarrollar funcionalidades muy específicas para satisfacer las necesidades particulares de un mercado concreto. 

Un módulo es una pieza de funcionalidad adicional que puede desplegarse de forma opcional e independiente sobre Etendo Classic. Ejemplos de módulos son: informes adicionales, ventanas adicionales, conectores, paquetes de contenido (traducciones, plan contable, lista de códigos de impuestos, categorías de producto, etc.).

!!!info
    Para una descripción detallada del concepto de modularidad de Etendo Classic, consulte la [Guía de modularidad](../concepts/modularity-concepts.md).

Esta sección explica únicamente el tipo de módulo estándar, porque es el más relevante para las demás secciones.

Todo desarrollo nuevo debe realizarse como parte de un módulo. Solo los módulos que estén marcados como _En Desarrollo_ pueden utilizarse en el proceso de desarrollo. Un módulo puede constar de los siguientes artefactos de software:

  * Componentes del diccionario de aplicación: todos los artefactos nuevos del diccionario de aplicación deben estar asociados a un módulo. Las ventanas del diccionario de aplicación tienen un campo que permite vincular un componente del diccionario de aplicación a un módulo. 
  * Recursos de software: son artefactos no definidos en Etendo Classic en sí, sino, por ejemplo, clases Java, librerías, recursos web (imágenes, etc.), archivos de configuración, etc. Para mantener la relación con el módulo, los recursos de software deben ubicarse en el directorio del módulo dentro del proyecto de desarrollo de Etendo Classic. Cada módulo tiene su propio directorio único. 
  * Datos de referencia: los módulos pueden distribuirse con su propio conjunto de datos empresariales de referencia, por ejemplo, categorías de producto, código de impuestos, etc. Los datos de referencia se definen en conjuntos de datos que pueden relacionarse con un módulo. 

El proceso de desarrollo de un módulo tiene tres pasos principales:

  1. Registre su módulo en el Diccionario de aplicación y en su repositorio de github.
  2. Desarrolle los artefactos incluidos en su módulo. Dependiendo de la especificación funcional y del diseño técnico de su módulo, puede incluir solo un tipo de artefactos o una combinación de ellos. En las secciones siguientes, se describe cada tipo de artefacto en detalle. 
  3. Publique el módulo en su repositorio de github.

!!!Important
    Cada pieza de código de Etendo Classic pertenece a un módulo, incluido el propio Core de Etendo Classic. Debe realizar todos sus desarrollos mediante módulos, incluidas las personalizaciones. Puede realizar cambios directamente en otros módulos —incluido el Core de Etendo Classic—, pero se recomienda encarecidamente no hacerlo. Resulta mucho más sencillo mantener Etendo Classic si restringe los cambios de código a módulos.

Un módulo puede distribuirse y descargarse por otros usuarios de Etendo Classic a través del repositorio central. Para más información sobre el repositorio central y la distribución de módulos, visite la [Guía de modularidad](../concepts/modularity-concepts.md).

Las secciones siguientes tratan el tema principal de esta sección: crear y configurar un módulo, y [publicarlo para su distribución](how-to-publish-modules-to-github-repository.md).

## Creación de un módulo

El primer paso en el proceso de desarrollo es crear un módulo nuevo. En el menú Aplicación, seleccione `Application Dictionary` > `Module`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_To_Create_a_Module-0.png)

Tenga en cuenta los siguientes campos importantes: (para más detalles, consulte la descripción de la tabla `AD_Module`):

  * El formato del campo Versión son tres números separados por dos puntos. 
  * El paquete Java es un identificador único de su módulo y debe cumplir las reglas de nomenclatura de paquetes Java tal como se describe en las convenciones de nomenclatura de Java (nombres y nombres de paquetes). Tenga cuidado al establecer este valor, ya que no se le permite cambiarlo una vez que su módulo esté registrado en el repositorio central. Si su módulo incluye archivos Java, deben empaquetarse dentro del paquete Java de su módulo o en sus subpaquetes. Ejemplos de paquetes Java para un módulo son _org.etendo.howtos_, _com.etendoerp.examples.helloworld_, _com.yourcompany.yourPackage_, _org.yourfoundation.yourPackage.yourSubpackage_, etc. 
  * La opción **En Desarrollo** informa al sistema de que usted está desarrollando el módulo. Solo los módulos en desarrollo son exportados por las herramientas de desarrollo y el sistema generará un error si intenta modificar un componente de un módulo que no esté en desarrollo. 
  * La opción del campo Predeterminado para un módulo marca ese módulo como el que se selecciona por defecto al desarrollar y al editar componentes en el Diccionario de aplicación. Puede estar desarrollando más de un módulo al mismo tiempo, y especificar un valor predeterminado permite que el módulo que desea quede seleccionado por defecto. 
  * Seleccione la opción Requiere traducción si su módulo contiene artefactos de UI (ventana, campo) con elementos traducibles. 

Las solapas en la parte inferior de la ventana le permiten definir el módulo con más detalle:

  * Dependencia: define la dependencia del módulo respecto a otros módulos. 
  * Incluir: se utiliza en plantillas/paquetes de industria. 
  * Prefijo de BD: relaciona los artefactos del esquema de base de datos con los módulos. 
  * Paquete de datos: permite agrupar tablas. Los paquetes de datos se utilizan para determinar el paquete Java del código Java generado (objetos de negocio). 
  * Excepciones de nomenclatura: se utiliza durante las actualizaciones de versiones anteriores de Etendo Classic. No debe utilizarse para ningún otro propósito. 
  * Fusiones: si este módulo A incluye ahora el contenido de otro módulo B publicado previamente de forma independiente (por lo que el módulo B se fusionó en el módulo A). 
  * Traducción: se utiliza para dar soporte a traducciones. 

  
En esta sección, creamos un módulo de ejemplo, llamado _Etendo Howtos_.
Definiremos el módulo utilizando las siguientes tres solapas de la ventana `Application Dictionary` > `Module`:

  * Dependencia
  * Prefijo de BD
  * Paquete de datos

Dependencia: la funcionalidad Core de Etendo Classic es en sí misma un módulo, llamado _Core_. Todos los módulos tienen una dependencia de User Interface Application y, a su vez, este tiene una dependencia del Core de Etendo. En la ventana Dependencia, especifique que el módulo depende de User Interface Application. (consulte también la descripción de `AD_Module_Dependency`):

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_To_Create_a_Module-1.png)

  
Prefijo de BD: se requiere al menos un prefijo de BD cuando un módulo también contiene artefactos de base de datos (tabla, columna, restricciones, etc.). Etendo Classic determina el módulo de un artefacto de base de datos comprobando si su nombre comienza con uno de los db_prefixes definidos. Si se van a añadir artefactos de base de datos al módulo, debe especificarse al menos un Prefijo de BD.

!!!important
    El Prefijo de BD solo puede contener mayúsculas [A-Z0-9] y se requiere que la primera letra sea únicamente de [A-Z].  

  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_To_Create_a_Module-2.png)

!!!info
    Para más información, consulte la descripción de la tabla `AD_Module_Dbprefix`.

  
Paquete de datos: las tablas se vinculan a un módulo a través del Paquete de datos. El objeto de negocio generado para la nueva tabla utilizará el paquete Java definido en el Paquete de datos. Si se van a añadir tablas nuevas al módulo, debe especificarse un paquete de datos como se ilustra en la imagen siguiente.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_To_Create_a_Module-3.png)


## Desarrolle sus artefactos de software

Ahora, veamos cómo desarrollar los artefactos de software necesarios para la funcionalidad del módulo. Durante el desarrollo, la relación con el módulo se mantiene de diferentes maneras:

  * Directa: por ejemplo, una ventana está relacionada directamente con un módulo específico. 
  * Indirecta: una tabla pertenece a un paquete de datos que, a su vez, pertenece a un módulo. 
  * Por nombre: un nuevo procedimiento almacenado se vincula a un módulo anteponiendo el _Prefijo de BD_ del módulo. 

Cuando el desarrollo personalizado esté listo, el siguiente paso es exportar el módulo.

## Exportación de un módulo

La exportación de un módulo crea un directorio para su módulo bajo el directorio raíz de Etendo Classic y los archivos XML correspondientes para su inclusión en el módulo finalizado. Los módulos que no estén marcados como en desarrollo no se exportan.

!!!note
    Recuerde que debe seleccionar la casilla **En Desarrollo** cuando defina un módulo nuevo; de lo contrario, no se exportará.

Cuando el desarrollo del módulo haya finalizado (o para entregar resultados intermedios), abra una ventana de comandos/shell y navegue hasta el proyecto de desarrollo de Etendo Classic; ejecute el comando `./gradlew export.database`.

!!!important
    La tarea de exportación de base de datos exportará todos y solo los módulos configurados como En Desarrollo  
    `./gradlew export.database`
    
Dado que todavía no tenemos desarrollos adicionales, en este punto solo se han creado la estructura de carpetas correspondiente y los archivos XML del descriptor del módulo.

```
modules
    └── org.etendo.howtos
        └── src-db 
            database
               └── sourcedata
                   ├── AD_MODULE_DBPREFIX.xml
                   ├── AD_MODULE_DEPENDENCY.xml
                   ├── AD_MODULE.xml
                   └── AD_PACKAGE.xml
```

  
Etendo Classic valida la base de datos y los artefactos del módulo cuando el módulo se exporta y se crea su archivo de compilación. Consulte más información sobre el [paso de validación de base de datos](../developer-tools/etendo-gradle-plugin.md#build-tasks).

!!!info
    Para una descripción detallada de esta tarea `export.database` y otras tareas de gradle relacionadas con módulos, consulte las [tareas de gradle de base de datos](../developer-tools/etendo-gradle-plugin.md#build-tasks)


## Creación de un directorio de código fuente

Para desarrollar código Java manual necesita un directorio _src_ dentro de su módulo específico:

```
modules
    └── org.etendo.howtos
        ├── src 
        │   └── org
        │       └── etendo
        │           └── howtos
        │                └── 
        └── src-db
            └──[...]
```
  
El paquete Java en el directorio de código fuente debe comenzar con el paquete Java del módulo.

## Publicación de un módulo

Una vez que el módulo esté creado y documentado, el siguiente paso es publicarlo para que esté disponible.

Para información detallada sobre este proceso, visite la [guía Cómo publicar módulos en un repositorio de Github](how-to-publish-modules-to-github-repository.md)

## El resultado

El resultado de esta sección es un módulo configurado correctamente, que puede instalarse en una instancia de Etendo Classic que cumpla los requisitos del módulo.

---

Este trabajo es una obra derivada de [Cómo crear y empaquetar un módulo](http://wiki.openbravo.com/wiki/How_To_Create_and_Package_a_Module){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.