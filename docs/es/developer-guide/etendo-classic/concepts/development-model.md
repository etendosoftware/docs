---
title: Modelo de desarrollo
tags:
    - Desarrollo
    - Modelo
    - Diccionario de la Aplicación
    - Modelo XML

status: beta
---
#  Modelo de desarrollo

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
## Visión general

El **Entorno de Desarrollo de Etendo** (abreviado como **ODE**) es un framework de herramientas, metodologías y procesos para facilitar el proceso de desarrollo de Etendo y ayudar a los desarrolladores a ser más eficientes en tareas como editar el código fuente, depurar, probar, desplegar y gestionar repositorios de código. ODE es compatible con entornos basados en **Oracle** y **PostgreSQL**. ODE está diseñado para dar soporte al proceso de desarrollo independientemente del objetivo (contribuciones al core de Etendo, módulos y código personalizado) y del alcance (desde pequeñas correcciones de errores hasta nuevos módulos funcionales completos).
##  Conceptos

Antes de comenzar con el proceso de desarrollo, expliquemos algunos conceptos generales básicos.

###  Modelo de Base de datos

Contiene la estructura de todos los elementos de base de datos utilizados en Etendo: tablas, triggers, vistas, secuencias y funciones. El Modelo de Base de datos forma parte del modelo `XML`.

###  Diccionario de la Aplicación

El Diccionario de la Aplicación es la parte del código fuente de Etendo almacenada en la base de datos. Es un conjunto de definiciones declarativas de elementos y lógica de negocio que se utilizan para construir y renderizar la aplicación. Por ejemplo, contiene la definición de ventanas, tablas, formularios, informes, procesos, etc. Se almacena en tablas `AD` como `AD_Window` o `AD_Column` y forma parte del modelo `XML`.

###  Modelo XML

El modelo XML contiene el esquema de la base de datos y el Modelo de Base de datos y el Diccionario de la Aplicación. Para facilitar los desarrollos concurrentes, esta información puede exportarse desde la base de datos a archivos XML de texto plano. Estos archivos mantienen toda la información necesaria para generar la base de datos y poblarla con todos los datos del Diccionario de la Aplicación. Se almacena en un lenguaje neutral compatible con los dos motores de base de datos soportados por Etendo: PostgreSQL y Oracle.

La sincronización desde la base de datos al modelo XML y viceversa se gestiona mediante el [DBSourceManager](../concepts/dbsourcemanager.md).

###  Código fuente

Es donde se encuentra toda la información necesaria para construir el sistema completo de Etendo. Incluye el Modelo de Base de datos, el Diccionario de la Aplicación, clases de entidad generadas, clases del core para gestionar el sistema, así como código Java, código JavaScript, HTML, informes y otros archivos para implementar funcionalidad que complementa al Diccionario de la Aplicación.

###  Binarios

Durante el proceso de build, todas las clases `Java` del sistema se compilan y se transforman en archivos binarios. Estos archivos binarios pueden empaquetarse y desplegarse en un servidor de aplicaciones `J2EE` como Tomcat.

###  Base de datos

La Base de datos es donde se almacenan el Diccionario de la Aplicación y los datos del usuario.

###  Gradle

[Gradle](https://http://gradle.org/){target="\_blank"} es una herramienta de build basada en Groovy. Etendo automatiza la mayoría de sus tareas de desarrollo y compilación utilizando Gradle.

###  IntelliJ IDEA

El código fuente de Etendo está preparado para IntelliJ IDEA. Esto significa que la configuración del código fuente de Etendo dentro de IntelliJ IDEA está optimizada para realizarse en muy pocos pasos.

###  GitHub

GitHub es un SCM distribuido que facilita que varios desarrolladores trabajen sobre el mismo código gestionando revisiones para cada archivo de código fuente. El código fuente y los paquetes de Etendo se mantienen y están disponibles libremente en los **repositorios de Etendo Software**. 

###  Modos de despliegue

Etendo es una aplicación web que se ejecuta en un contenedor de servlets. Esto significa que, para construir el sistema, necesita generar los binarios a partir del código fuente y desplegar los binarios en un contenedor de servlets, normalmente Apache-Tomcat. Las tareas de build de Etendo pueden configurarse para gestionar el despliegue en tres modos diferentes:

- **class**

    El modo de despliegue **class** copia las clases Java compiladas y todos los archivos necesarios a la carpeta de contexto de Etendo dentro del contenedor de servlets desde donde se sirve la aplicación. Usando este modo de despliegue, la aplicación se despliega automáticamente cuando se construye el sistema.

- **war**

    El modo de despliegue **war** genera un archivo war con la aplicación completa. Este archivo puede desplegarse posteriormente en el servidor. Tenga en cuenta que, usando este modo de despliegue, la aplicación no se despliega automáticamente cuando se construye el sistema, sino que el archivo war debe desplegarse manualmente.

- **none**

    Cuando Etendo se compila, todos los archivos necesarios para ejecutarse en el servidor se copian al directorio `WebContent`. Es posible configurar el servidor para servir desde este directorio, que es la forma estándar de trabajar desde Eclipse IDE. En este caso, Eclipse gestionará el despliegue.

El modo de despliegue se establece en el archivo `gradle.properties`, mediante la propiedad `deploy.mode`.
##  Estructura del código fuente

El código fuente de Etendo está estructurado en diferentes carpetas:

- **config** : Aquí se encuentran todos los archivos de configuración de Etendo. El archivo más importante es **gradle.properties** y **Openbravo.properties**, que contiene todas las opciones de despliegue y las propiedades de conexión a la base de datos. 
- **legal** : Aquí se encuentran la licencia de Etendo y los archivos de licencia de todos los componentes de terceros utilizados por Etendo. 
- **lib** : Todos los archivos de librerías se encuentran en esta carpeta. Las librerías se separan entre **lib/build** , librerías necesarias solo para ejecutar tareas de compilación, y **lib/runtime** librerías necesarias en tiempo de ejecución y durante la ejecución de tareas de compilación. 
- **Módulo** : Todos los módulos instalados o en desarrollo, con todos sus artefactos, se encuentran en su propia subcarpeta dentro de **modules** . 
- **modules_core** : Todos los módulos distribuidos con el núcleo de Etendo. 
- **referencedata** : Los datos estándar y de ejemplo almacenados en archivos XML se encuentran en esta carpeta. 
- **src** : Esta es la carpeta principal para todos los archivos y recursos del código fuente del núcleo. 
- **src-core** : Aquí se encuentran los archivos fuente y recursos de la librería **openbravo-core.jar**. 
- **src-trl** : Aquí se encuentran los archivos fuente y recursos de la librería **openbravo-trl.jar**. 
- **src-wad** : Aquí se encuentran los archivos fuente y recursos de la librería **openbravo-wad.jar**. 
- **src-util** : Esta carpeta se utiliza para la validación de compilación, scripts de módulo y componentes de diagnóstico necesarios para ejecutar tareas de mantenimiento para Etendo y módulos. 
- **src-db** : Aquí se encuentran los archivos fuente y recursos de la herramienta DBSourceManager, así como los archivos del modelo de base de datos y del Diccionario de la Aplicación. 
- **src-gen** : En esta carpeta se encuentran todas las clases Java de entidad DAL generadas. 
- **src-test** : En esta carpeta se encuentran todos los archivos fuente y recursos de las pruebas. 
- **web** : Aquí es donde se encuentran todos los archivos web estáticos, como archivos JavaScript, imágenes, skins, ... 
- **WebContent** : Aquí es donde se copian todos los archivos necesarios para desplegar Etendo al ejecutar las tareas de compilación. Un servidor de aplicaciones puede servir la aplicación Etendo directamente desde aquí o se puede construir un archivo de paquete desde aquí para ser desplegado.
##  Gestión del código de base de datos

###  Visión general

El código fuente de Etendo está compuesto por dos **Tipo** diferentes de código: **código fuente** (archivos `Java`, `JavaScript`, `CSS`, `HTML`) y **código de base de datos**. El código de base de datos puede separarse en sentencias DDL del **Modelo de Base de datos** (tablas, triggers, vistas, secuencias y funciones) y el **Diccionario de la Aplicación**.

Cuando se instala Etendo, se crea una base de datos (Oracle o PostgreSQL) ejecutando las sentencias DDL, se insertan los datos del diccionario de la aplicación y se genera código. Una vez creada la base de datos, se añaden a la base de datos datos ERP personalizados (productos, terceros, pedidos, facturas, etc.). Esos datos se almacenan en la base de datos en archivos binarios mezclados con el Modelo de Base de datos y el Diccionario de la Aplicación.

Los nuevos desarrollos (correcciones de errores o nuevas funcionalidades) normalmente incluyen cambios tanto en el código fuente como en el código de base de datos. Existen **dos problemas principales** con el volcado genérico exportado de la base de datos, especialmente cuando se desea incluirlo en un repositorio de código fuente:

1. **No es fácil obtener una descripción detallada y limpia de sus cambios de desarrollo** ya que el archivo `dump` (`*.dmp`) es un archivo binario y no de texto. Por lo tanto, la sentencia `diff` no funciona bien con archivos binarios.

2. **No es posible actualizar un entorno de producción desplegando los cambios en el código fuente**. En su lugar, es necesario preparar un script de base de datos que realice las sentencias `alter` y `update` requeridas para conservar los datos del cliente que ya están en la base de datos.

###  DBSourceManager

DBSourceManager se basa en [DdlUtils](https://db.apache.org/ddlutils/){target="\_blank"}, un componente pequeño y fácil de usar de la Apache Foundation para trabajar con archivos de Definición de Base de Datos (DDL). Estos son **archivos XML** que contienen la definición del esquema de la base de datos (p. ej., tablas y columnas). Estos archivos pueden alimentarse a DBSourceManager mediante su correspondiente **tarea Ant** para crear o modificar la base de datos. Del mismo modo, DBSourceManager puede generar un archivo DDL a partir de una base de datos existente. **Etendo ha ampliado varias capacidades de DdlUtils** (por ejemplo, soporte para restricciones check, procedimientos y vistas; traducción PL/SQL de Oracle a PostgreSQL; soporte para más tipos de base de datos, etc.) y ha ajustado otras (por ejemplo, exportar objetos del esquema de base de datos, etc.) para dar soporte completo a los requisitos de ODE.

###  Cómo funciona

Cada sistema Etendo (copia de trabajo) tiene una carpeta llamada [`database`](../concepts/development-project-structure.md#src-db) donde se almacena todo el **código de base de datos** (Modelo de Base de datos y Diccionario de la Aplicación) en **archivos de texto XML sin formato**. El código fuente en archivos XML sin formato dentro de la carpeta `src/database` se divide en:

* **model** Modelo de base de datos.
* **sourcedata** Diccionario de la aplicación.

**Los cambios en la base de datos pueden producirse en 2 lugares**:

1. **Dentro de la carpeta `src-db/database`** (copia de trabajo):
    1. Mediante actualizaciones procedentes del repositorio de GitHub. Cuando los cambios provienen de una actualización de GitHub, no sobrescriben los cambios realizados en la copia de trabajo, ya que estos cambios se fusionan dentro de los archivos XML sin formato.
2. **Dentro de la base de datos**:
    1. Editando el Diccionario de la Aplicación usando las ventanas y procesos del Diccionario de la Aplicación de Etendo.
    2. Realizando cambios en el modelo de base de datos (tablas, procedimientos, etc.) usando su herramienta de gestión de base de datos favorita (PGAdmin, SQL Developer, TOAD, etc.).

ODE proporciona las siguientes **tareas para sincronizar los archivos XML de la base de datos con la propia base de datos**:

* Tarea [**create.database**](../developer-tools/etendo-gradle-plugin.md#database-tasks): primero lee los archivos XML del Modelo de Base de datos dentro de la carpeta `src-db/database/model` y crea los objetos del esquema en la base de datos Oracle o PostgreSQL. Después, esta tarea rellena la base de datos con el Diccionario de la Aplicación tomado de la carpeta `src-db/database/sourcedata`.

    !!!warning
        Tenga en cuenta que esta tarea vuelve a crear la base de datos desde cero, lo que significa que primero se eliminará la base de datos existente.

* Tarea [**update.database**](../developer-tools/etendo-gradle-plugin.md#update-database): compara el Modelo de Base de datos y el Diccionario de la Aplicación almacenados en la base de datos con los archivos XML dentro de las carpetas `src-db/database/model` y `src-db/database/sourcedata`. Las diferencias se aplican a la base de datos, manteniendo intactos los datos ERP personalizados (productos, terceros, pedidos, facturas, etc.) de la base de datos.

* Tarea [**export.database**](../developer-tools/etendo-gradle-plugin.md#database-export): toma el Modelo de Base de datos y el Diccionario de la Aplicación almacenados en la base de datos y sobrescribe los archivos XML dentro de las carpetas `src-db/database/model` y `src-db/database/sourcedata`.

Como puede imaginar, siempre que se ejecuta cualquiera de estas tareas, **se fuerza a que ambos modelos (el que está dentro de la carpeta `src-db/database` y la propia base de datos) sean idénticos**. Las dos primeras tareas modifican la base de datos para que sea igual al contenido de la carpeta `src-db/database` y la tercera sobrescribe el contenido de la carpeta `src-db/database` para igualarlo al de la base de datos.

En resumen, la carpeta `src-db/database` contiene el código fuente de base de datos de Etendo (archivos XML sin formato) claramente separado de los datos ERP personalizados (productos, terceros, pedidos, facturas, etc.). De este modo, la base de datos ya no se distribuye como un archivo binario de volcado.

!!! important
    Dado que los cambios en la base de datos pueden producirse dentro de los archivos de texto o en la propia base de datos, es extremadamente **importante garantizar que estos cambios no se produzcan simultáneamente en ambos lados**, ya que esta situación conduciría a inconsistencias del sistema y pérdida de datos. Esto se garantiza mediante una comprobación basada en el **número de revisión de GitHub**. Cada vez que se lanzan las tareas `create.database` o `update.database`, el número de revisión de la copia de trabajo se guarda en la base de datos. La tarea `export.database` comprueba que el número de revisión de la copia de trabajo coincide con el número de revisión de la base de datos.
    Si coincide, existe una garantía de que los cambios en nuestra base de datos no sobrescribirán los cambios realizados por otros desarrolladores en los archivos XML de base de datos. Si no coincide, el desarrollador obtendrá un error y se verá obligado a cambiar la copia de trabajo al número de revisión actual de la base de datos.

###  Diferentes tipos de datos

La instalación por defecto de Etendo instalará diferentes conjuntos de datos, dando como resultado un sistema completo y operativo. Dentro de Etendo, distinguimos la siguiente información:

* sourcedata: esta es la información del Diccionario de la Aplicación. Aquí van los datos de las tablas `ad_tables`, `ad_columns`, `ad_windows`. Esto puede ampliarse mediante módulos (los módulos pueden añadir información aquí) y se actualiza en cada actualización del Core (mediante `update.database`). Los datos del Diccionario de la Aplicación pueden encontrarse en la carpeta `src-db/database/sourcedata`.
* referenceddata: esta es información referenciada por sourcedata, datos de las tablas `ad_client`, `ad_org`, `ad_user`, `ad_language` o `ad_role`. La base de datos de Etendo no puede crearse sin esta información (la integridad referencial de la base de datos se vería comprometida sin ella), y esto explica por qué se trata de una manera especial. No se actualiza en cada actualización del Core. Estos datos se encuentran en la carpeta `src-db/database/sourcedata/referenceddata`.
* standard: esta es información que no es necesaria para crear la base de datos, pero es realmente conveniente para cada usuario, como tipos de documento, plantillas de documento, etc. Esto tampoco se actualiza en cada actualización del Core. Estos datos se encuentran en la carpeta `referencedata/standard`.
* sampledata (): esta es información de ejemplo que proporcionamos para que los usuarios prueben Etendo, y contiene un nuevo cliente, con su correspondiente información de negocio. Estos datos se encuentran en la carpeta `referencedata/sampledata`.

Estos datos se instalan/cargan en la base de datos al instalar Etendo.
##  Proceso de desarrollo

![](../../../assets/developer-guide/etendo-classic/concepts/Development_Model-1.png)

Esta sección explica la forma más común de desarrollar en Etendo y qué tareas de build deben utilizarse para cada caso. En la mayoría de los casos solo es necesario usar 3 tareas (`install.source`, `smartbuild` y `export.database`). Hay otras tareas que pueden utilizarse, pero no son necesarias para el proceso estándar. Se explican en el artículo [Tareas de build de desarrollo](../developer-tools/etendo-gradle-plugin.md#build-tasks).

La tarea principal del proceso estándar es **smartbuild**, que realiza un build incremental del sistema (solo se reconstruyen los componentes modificados), tal y como se explica a continuación. Esta tarea acepta dos propiedades opcionales: `local` para desarrollos locales o remotos, que por defecto está establecida en `yes`, y `restart`, que indica si tras el proceso de build debe reiniciarse Tomcat, con `no` como valor por defecto.

`local` se utiliza como una indicación para la tarea de build, para que sepa si ha habido cambios en la base de datos procedentes de otros desarrolladores a través de un pull del repositorio de GitHub, por lo que es necesario aplicar esos cambios a la base de datos en la instancia local. Un desarrollador que trabaja localmente en sus instancias realiza todos los cambios de base de datos directamente en la base de datos, por lo que no es necesario actualizar la base de datos para hacer el build del sistema. Pero si el desarrollador acaba de hacer un pull de GitHub, entonces es probable que otros desarrolladores hayan realizado cambios en los archivos XML de base de datos, por lo que es necesario actualizar la base de datos con esos cambios.

Smartbuild es un proceso incremental y evita cualquier tarea que no sea necesaria. Cuando el desarrollo es local, smartbuild puede omitir la actualización de la base de datos. En cualquier caso, los desarrolladores pueden actualizar su base de datos desde archivos XML en cualquier momento.

###  Instalación inicial

Después de descargar los archivos fuente de Etendo (por ejemplo, desde un repositorio clonado usando GitHub), el siguiente paso es instalar y desplegar el sistema.

En primer lugar, debe configurar correctamente todas las propiedades requeridas. Todas ellas se almacenan en el archivo `gradle.properties`, que **debe configurar correctamente antes de continuar**.

Una vez configuradas todas las propiedades, el siguiente paso es construir la aplicación a partir del código fuente y desplegarla. Todo esto se realiza con la tarea **install.source**. Esta tarea crea la base de datos, inserta datos de ejemplo en ella y compila y despliega la aplicación de acuerdo con el modo de despliegue elegido. Para ejecutarla, escriba en el directorio raíz de Etendo:
    
```
./gradlew install.source
```

###  Desarrollos locales

Una vez que Etendo está en funcionamiento, es posible desarrollar sobre él. Generalmente, los nuevos desarrollos deben realizarse mediante módulos.

La forma estándar de desarrollar localmente consiste en:

* Desarrollar/modificar ventanas, solapas, etc. a través del Diccionario de la Aplicación. 
* Crear/modificar objetos de base de datos directamente en la base de datos. 
* Desarrollar/modificar ventanas editando archivos html, xml, javascript y java. 

####  Build

Una vez realizados sus cambios y antes de probarlos, es necesario hacer el build de la aplicación. Puede hacer un build incremental ejecutando (desde la línea de comandos):

```
./gradlew  smartbuild
```

!!!note
    Recuerde que, por defecto, smartbuild considera solo cambios locales, por lo que no sincroniza la base de datos desde los archivos XML (se omite `update database`).

Esta tarea genera y compila las fuentes de los elementos modificados y, dependiendo del modo de despliegue, también los despliega. Es posible reiniciar Tomcat desde la misma tarea estableciendo la propiedad restart a yes; sería:

```
./gradlew smartbuild -Dlocal=yes -Drestart=yes # Note the -Drestart=yes 
```

####  Exportación de base de datos

En la mayoría de los casos, los desarrollos incluyen modificaciones en la base de datos. Estas modificaciones pueden persistirse en los archivos XML de base de datos usando la herramienta [DBSourceManager](../concepts/dbsourcemanager.md). DBSourceManager exporta a archivos XML únicamente los cambios de base de datos de los módulos (incluyendo el core) que estén establecidos como `In Development`. Para exportar los cambios de base de datos, ejecute:
    
```
./gradlew export.database
```

###  Desarrollos remotos

Los desarrollos remotos los realizan otros desarrolladores de forma remota y luego se fusionan con las fuentes locales. La principal diferencia con los desarrollos locales es que los desarrollos remotos no modifican la base de datos directamente. La forma en que un desarrollo remoto puede cambiar objetos en la base de datos es usando archivos XML, por lo que, tras actualizar (fusionar) los archivos XML, también es necesario actualizar la base de datos. Después de actualizar la base de datos, el proceso es exactamente el mismo que el local; es decir, compilar y desplegar los elementos que se hayan modificado desde el último build. Todo esto (actualizar la base de datos, compilar las últimas modificaciones y desplegarlas) puede hacerse al mismo tiempo con el comando **smartbuild**:
    
```
./gradlew smartbuild -Dlocal=no # Note the -Dlocal=no 
```

La única diferencia con el desarrollo local está en el parámetro `local`, que hace que el proceso actualice la base de datos en caso de que los archivos XML hayan cambiado.

###  Validar base de datos

Cuando un módulo se exporta usando la tarea `export.database`, primero se valida para comprobar errores comunes. Si la validación falla, entonces la tarea `export.database` también fallará y no será posible exportar.

Actualmente se realizan las siguientes comprobaciones:

* Una tabla definida en el Diccionario de la Aplicación debe estar presente en la base de datos y viceversa. 
* Se comparan las definiciones de columnas en la base de datos y en el Diccionario de la Aplicación; se informa de cualquier discrepancia. Se comprueban el tipo de dato de la columna, el valor por defecto y la longitud. 
* Las tablas deben tener una clave primaria. 
* Los campos de clave foránea deben formar parte de una restricción de clave foránea. 
* Se comprueba la longitud de los nombres de tablas, columnas y restricciones (Oracle tiene un límite de 30 caracteres). 

###  Tareas de test de Gradle

Etendo dispone de varias tareas de Gradle para ejecutar casos de prueba JUnit.

``` bash title="Terminal"
./gradlew test`
```
``` bash title="Terminal"
./gradlew test --tests <package>
```

Estas tareas ejecutarán todos los tests definidos en Etendo y en los módulos instalados.
##  Core, módulos y personalizaciones

Etendo está diseñado para satisfacer todos los requisitos del cliente, sean cuales sean. Esto se realiza en diferentes niveles, cada uno más específico para el cliente que el anterior:

* **Etendo core**: funcionalidad común **sin ningún detalle específico de la industria** que se utiliza para la mayoría de los clientes. 
* **Módulos** divididos en tres tipos diferentes: 
    * **Módulos funcionales y plugins**: funcionalidad ampliada (como un módulo de RR. HH.) y herramientas o componentes específicos (como una conexión a un sistema bancario remoto). Se podría aplicar más de un módulo/plugin a una instalación de cliente. 
    * **Paquetes de localización**: adaptación de Etendo Core y módulos a operaciones específicas de un país (traducción y reglas específicas como el plan contable e impuestos). 
    * **Plantillas de industria**: adaptación de Etendo Core y los módulos relacionados a operaciones específicas de una industria (por ejemplo, una vertical para organizaciones sin ánimo de lucro). Solo se puede aplicar una `plantilla de industria` por instalación de cliente. 
* **Código personalizado**: personalización de Etendo Core y los módulos relacionados para satisfacer completamente los requisitos del cliente. 

Por lo tanto, independientemente del alcance de un proyecto (solo una pequeña corrección de error o un gran módulo funcional nuevo), el desarrollo usando ODE se puede dividir en una de las siguientes categorías:

1. **Core**: una modificación del código fuente proporcionado por la distribución de Etendo.
2. **Módulo**: un módulo conectable que se puede empaquetar de forma independiente del core de Etendo, distribuir y desplegar en otras instalaciones de Etendo.  
3. **Personalización**: para **ajustarse a algunos requisitos del cliente**, a veces es necesario actualizar el código fuente del core de Etendo que no se puede empaquetar en un módulo.

El **despliegue en producción del cliente** puede, por tanto, consistir en **varios elementos** enumerados anteriormente, como correcciones de errores, plugins de módulos, nuevas funcionalidades, etc.

Independientemente del objetivo, la base del proceso de desarrollo es un **repositorio de código fuente** actualizado desde diferentes fuentes. ODE realizará el seguimiento del origen de cada cambio, pero todos se gestionarán de la misma manera estándar.

![](../../../assets/developer-guide/etendo-classic/concepts/Development_Model-3.png)

Esta figura también explica el árbol de dependencias en Etendo. **Etendo core** es completamente **independiente de los módulos y del código personalizado**. Un módulo depende de Etendo core y de otros módulos en los que pueda basarse. El código personalizado depende de Etendo core y de todos los módulos que el cliente tenga instalados.

El [proceso de desarrollo](#proceso-de-desarrollo) es idéntico para todas las categorías descritas anteriormente.

---

Este trabajo es una obra derivada de [Modelo de desarrollo](http://wiki.openbravo.com/wiki/Development_Model){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.