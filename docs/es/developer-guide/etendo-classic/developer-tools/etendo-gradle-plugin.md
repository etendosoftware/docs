---
title: Plugin de Gradle de Etendo 
tags: 
  - Gradle
  - Mantenimientos
  - Plugin
  - Parámetros
  - Compilación
  - Desarrollo
---

## Visión general

Este artículo explica cómo usar Gradle, una herramienta de automatización de compilación de código abierto que está diseñada para ser lo suficientemente flexible como para compilar casi cualquier tipo de software. 

!!! note
    Para obtener información adicional, lea: [¿Qué es gradle?](https://docs.gradle.org/7.3/userguide/what_is_gradle.html){target="_blank"}.


Etendo usa Gradle para definir y mejorar la compilación, la gestión de versiones, la publicación de módulos, las migraciones y más mantenimientos.
## Cómo usar Gradle

El proyecto de Etendo incluye un wrapper embebido de Gradle llamado `gradlew`. Ejecute el siguiente comando en el directorio del proyecto de Etendo y se ejecutará el mantenimiento mencionado.

```bash title="Terminal"
 ./gradlew <task>
```
 

Puede usar `-P<Nombre del parámetro>` para pasar parámetros en un mantenimiento. Por ejemplo:

```bash title="Terminal"
./gradlew publishVersion -Ppkg=test.package
```
## Flags comunes de Gradle

| Flag                     | Descripción                                                   |
| ------------------------ | ------------------------------------------------------------- |
| `--offline`              | Para ejecutar Gradle sin conexión a internet.                 |
| `--stop`                 | Para detener todos los daemons de Gradle.                     |
| `--no-daemon`            | Para ejecutar una tarea de Gradle sin iniciar un daemon.      |
| `--info`                 | Para proporcionar más información en la ejecución de la tarea. |
| `--refresh-dependencies` | Forzará la descarga de dependencias.                          |
## Plugin de Etendo

Añada en el archivo `build.gradle` la versión del plugin disponible en [Notas de la versión del plugin de Gradle](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md).

```groovy title="build.gradle"
plugins {
    id 'com.etendoerp.gradleplugin' version '<version>'
}
```

### Configuración del plugin

La configuración del plugin debe declararse en el archivo `build.gradle` en el *bloque etendo*. <br>
En las siguientes secciones, puede encontrar todos los flags o variables disponibles para configurar y una breve descripción de cada uno.

```groovy title="build.gradle"
etendo {
  /**
  * Flags utilizados para indicar si las dependencias del Core 'por defecto' (archivos jar) deben
  * cargarse (este es el caso cuando está trabajando con fuentes y faltan los archivos jar 'por defecto')
  * Estos flags deben ser false.
  */
  boolean loadCompilationDependencies = false
  boolean loadTestDependencies = false

  /**
  * Flag utilizado para ignorar la carga de los módulos fuente para realizar la resolución de conflictos.
  * Por defecto true
  */
  boolean ignoreSourceModulesResolution = true

  /**
  * Flag utilizado para realizar o no la resolución de conflictos.
  * Por defecto true
  */
  boolean performResolutionConflicts = true

  /**
  * Flag utilizado para ignorar el lanzamiento de un error si hay resoluciones de conflictos con la dependencia del Core.
  * Por defecto false
  */
  boolean forceResolution = false

  /**
  * Flag utilizado para aplicar las dependencias de los subproyectos al proyecto principal.
  * Por defecto true
  */
  boolean applyDependenciesToMainProject = true

  /**
  * Flag utilizado para evitar sobrescribir los módulos fuente transitivos al ejecutar la tarea expandModules.
  * Por defecto true
  */
  boolean overwriteTransitiveExpandModules = true

  /**
  * Flag utilizado para excluir la dependencia del Core de cada subproyecto en todas las configuraciones.
  * Por defecto true
  */
  boolean excludeCoreDependencyFromSubprojectConfigurations = true

  /**
  *  Flag utilizado para indicar que la versión actual del Core soporta jars.
  *  Por defecto true.
  * 	Cuando este flag se establece en false, el comportamiento de la tarea 'expandModules' cambiará, forzando a expandir a fuentes todos los módulos declarados con 'moduleDeps'.
  */
  boolean supportJars = true

  /**
  * Lista de artefactos de Etendo que siempre se deben extraer e ignorar en la verificación de consistencia de versiones.
  */
  List<String> ignoredArtifacts = []

  /**
  * Flag utilizado para evitar lanzar un error por inconsistencia de versiones entre módulos.
  * Por defecto false
  */
  boolean ignoreConsistencyVerification = false

  /**
  * Flag utilizado para evitar lanzar un error cuando no se pudo resolver un artefacto.
  * Esto incluye los transitivos.
  * Por defecto false
  */
  boolean ignoreUnresolvedArtifacts = false

  /**
  * La lista de módulos que no deben volver a expandirse.
  * Por defecto vacío.
  */
  List<String> sourceModulesInDevelopment = []

  /**
  * Flag utilizado para ignorar la dependencia del jar del CORE de Etendo ubicada en el
  * build.gradle del proyecto raíz.
  * Por defecto false.
  */
  boolean ignoreCoreJarDependency = false
}

```
## Tareas principales de compilación

Esta sección explica las tareas principales de compilación siguiendo los pasos tal y como se ilustran en la imagen.

![](../../../assets/developer-guide/etendo-classic/concepts/Development_Build_Tasks-0.png)

En la mayoría de los casos, solo es necesario usar 3 tareas (`install`, `smartbuild` y `export.database`). Hay otras tareas que se pueden usar, pero no son necesarias para el proceso estándar.

!!!info
    Para más información, consulte la sección [Tareas de compilación detalladas](#tareas-de-compilación-detalladas).

La tarea principal para el proceso estándar es `smartbuild`, que ejecuta todos los procesos requeridos tal y como se explica a continuación. Esta tarea acepta una propiedad opcional:

  * `local` para desarrollos locales o remotos, que por defecto está configurada en **yes**.

La diferencia entre el desarrollo `local` y `remote` se ilustra en el diagrama. El desarrollo local son cambios realizados por el/la propio/a desarrollador/a. Los desarrollos remotos son cambios realizados por otros desarrolladores. Los cambios de desarrollos remotos se obtienen del sistema de control de versiones del código fuente.

!!!info
    `remote` significa que el usuario está trayendo cambios al espacio de trabajo desde una ubicación externa, por ejemplo, con un `git pull` o `./gradlew expandModules`.

### Instalación inicial

Después de descargar los archivos fuente de Etendo ERP, es necesario instalarlo y desplegarlo. Consulte nuestra guía sobre [Etendo Install](../../../getting-started/installation.md#install-etendo)

### Exportación de base de datos

En la mayoría de los casos, los desarrollos incluyen modificaciones en la base de datos. Estas modificaciones pueden persistirse en archivos `xml` usando la herramienta **DBSourceManager**. **DBSourceManager** exporta a archivos `xml` únicamente los módulos (incluyendo el core) que estén configurados como `In Development`. Para exportar la base de datos, ejecute:

``` bash title="Terminal"
./gradlew export.database
```

Después de este paso, los archivos `xml` del modelo modificado pueden subirse (push)/confirmarse (commit) al sistema de control de versiones del código fuente, de modo que otros desarrolladores puedan obtenerlos y continuar trabajando sobre ellos.

Cuando se exporta un módulo usando la tarea `export.database`, primero se valida para comprobar errores comunes. Si la validación falla, entonces la tarea `export.database` también fallará y no será posible exportar.

Actualmente se realizan las siguientes comprobaciones:

  * Una tabla definida en el Diccionario de Aplicación debe estar presente en la base de datos y viceversa.
  * Se comparan las definiciones de columnas en la base de datos y en el Diccionario de Aplicación; se informa de cualquier discrepancia. Se comprueban el tipo de dato de la columna, el valor por defecto y la longitud.
  * Las tablas deben tener una clave primaria.
  * Los campos de clave foránea deben formar parte de una restricción de clave foránea.
  * Se comprueba la longitud de los nombres de tablas, columnas y restricciones (Oracle y PostgreSQL tienen ahí un límite de 30 caracteres).

### Actualizar base de datos

Los cambios del **modelo de base de datos** se distribuyen confirmando (commit) el esquema de base de datos como `xml` en `SCM`. Otros desarrolladores obtienen (pull) los cambios desde `SCM` y pueden aplicarlos para actualizar su propia base de datos. Tras actualizar la base de datos, el proceso es exactamente el mismo que el local: compilar y desplegar los elementos que se hayan modificado desde la última compilación.

``` bash title="Terminal"
./gradlew update.database
./gradlew smartbuild
```

Todas las acciones requeridas (actualizar base de datos, compilar las últimas modificaciones y desplegarlas) se pueden realizar únicamente con el comando `smartbuild`:

``` bash title="Terminal"
./gradlew smartbuild -Dlocal=no -Dforce=yes
```

La única diferencia con el desarrollo local está en el parámetro `local`, que hace que el proceso actualice la base de datos en caso de que los archivos `xml` hayan cambiado.
## Tareas de compilación detalladas

Esta sección contiene un listado detallado de todas las tareas de compilación disponibles.

### Tareas de compilación de librerías

|  Mantenimiento      |  Descripción  |  Notas  |
|------------|---------------|---------|
|  `core.lib`  |  Compila y genera un archivo `.jar` a partir del proyecto `src-core`. Es necesario para `wad.lib` y el resto de tareas de compilación.  |  **Requerido por**: wad.lib  |
|  `wad.lib`   |  Compila y genera un archivo `.jar` a partir del proyecto `src-wad`. Es necesario para las tareas de compilación. Este proyecto contiene el WAD, el generador automático de ventanas.  |  **Requiere**: `core.lib`, base de datos creada **Requerido por**: compile.*  |
|  `trl.lib`   |  Compila y genera un archivo `.jar` a partir del proyecto `src-trl`. Es necesario para la tarea de traducción. Este proyecto permite traducir a diferentes idiomas las ventanas manuales.  | **Requiere**: core.lib  |
  
### Tareas de compilación

|  Mantenimiento                 |  Descripción   |  Notas  |
|-----------------------|----------------|---------|
|  `install`            |  Instala la aplicación completa: crea la base de datos, compila y genera un archivo war para desplegarlo o copia las clases al directorio de Tomcat (dependiendo de la propiedad `deploy.mode` configurada en Openbravo.properties).  |  **Llama a**: `create.database`, `core.lib`, `wad.lib`, `trl.lib`, `compile.complete.deploy`, `applyModule`.
|  `smartbuild`         |  Realiza una compilación incremental de la aplicación. Incluye: <br> `update.database` <br> compile <br> deploy <br> Todas estas tareas se realizan solo si es necesario.  |  **Requiere**: la base de datos debe estar creada y cargada con datos **Propiedades**: <br> `local`: (`sí/no` por defecto `sí`) cuando esta propiedad se establece en no, se ejecuta la tarea `update.database`; en caso contrario, no se ejecuta. <br> `tr`: (`sí/no` por defecto `sí`) si se establece en no, no se ejecuta el proceso de traducción. <br> `force`: (`sí/no` por defecto `no`) se usa con `local=no`. Si se establece en sí, sobrescribirá los cambios en la base de datos con la información XML. Nota: se perderán todos los cambios no exportados.
|  `compile.complete`  |  Compila todas las clases modificadas (incluidas las generadas), pero antes elimina todos los archivos generados y compilados, por lo que se compila la aplicación completa.  |  **Requiere**: `wad.lib`, `trl.lib`, base de datos creada y cargada. **Llama a**: translate <br> **Propiedades**: <br> **Solapa**: especifica el/los nombre(s) de ventana a generar; para especificar más de una ventana, añádalas como una lista de valores separados por comas. Tenga en cuenta que, aunque se especifique una ventana mediante esta propiedad, su código 2.50 no se generará a menos que sea requerido o forzado. <br>  **tr**: si se establece en "no", no llamará al proceso de traducción. <br>  **módulo**: una lista de javapackages de módulos separados por comas para generar únicamente las ventanas que contengan objetos de esos módulos. <br>
|  `generate.entities`  |  Genera los archivos Java para el directorio `src-gen` y los compila. DAL los utiliza para acceder a la información de la base de datos.  |   **Requiere**: la base de datos debe estar creada y cargada con datos.
|  `translate`          |  Comprueba en los archivos de interfaz de usuario de las ventanas manuales los elementos traducibles que aún no se han registrado y los registra; esto es necesario para poder traducir esas interfaces a diferentes idiomas.  |  **Requiere**: `trl.lib` **Llamado por:** esta tarea es llamada por las tareas compile.* en caso de que la propiedad tr no esté establecida en "no". 
|  `antWar`                |  Genera un archivo war a partir del código ya compilado. En realidad, solo comprime la aplicación en un único archivo war.  |  **Requiere:** compile.*: la aplicación debe estar compilada antes de llamar a esta tarea.
|  `deploy.context`     |  Despliega el archivo war existente en el contexto de Tomcat utilizando el gestor de Tomcat.  |  **Requiere:** <br> el archivo war debe estar creado <br> el gestor de Tomcat debe estar en ejecución <br> estas propiedades deben estar correctamente configuradas en el archivo `Openbravo.properties`: <br> `tomcat.manager. url` <br> `tomcat.manager.username` <br> `tomcat.manager.password` 

### Tareas de base de datos

|  Mantenimiento               |  Descripción  |  Notas  |  Subtareas  |
|---------------------|---------------|---------|-------------|
|  `create.database`  |  Crea la base de datos a partir de los archivos `xml`; tenga en cuenta que primero se elimina la base de datos. Si se establece la propiedad `apply.on.create`, se insertarán masterdata y sampledata en la base de datos. En caso contrario, solo se insertará sourcedata.  |  **Propiedades:** <br> `apply.on.create`: si se establece en **true** y hay módulos, se aplicarán; en caso contrario, se establecerán en estado **En proceso**.  |  `create.database.script`: igual que `create.database.structure`, pero no afecta a la base de datos; solo genera el archivo `sql script` con todas las sentencias que ejecutarían las otras tareas. 
|  `update.database`  |  Sincroniza la base de datos con los archivos xml actuales de la base de datos. Por defecto, comprueba que no se hayan realizado cambios en el diccionario de aplicación en la base de datos; si los hay, el proceso se detiene.  |  **Propiedades:**  <br>  `force`: (`sí/no` por defecto `no`) no comprueba modificaciones en la base de datos y actualiza directamente. Esto puede provocar pérdida de datos en la base de datos.  |   `update.database.script`: es igual que `update.database.structure`, pero no modifica la base de datos. Solo genera un archivo de script `sql` con las sentencias que ejecutarían las otras tareas.
|  `export.database`  |  Sincroniza los archivos xml con el contenido actual de la base de datos. Por defecto, solo se exportan en caso de que haya modificaciones en la base de datos. Además, realiza validaciones de base de datos para los módulos que se exportan.  |  **Propiedades:** <br> `force`: (`sí/no` por defecto `no`) fuerza la exportación omitiendo la comprobación de qué archivos se han modificado desde el último `update.database`. <br> `validate.model`: (`sí/no` por defecto `sí`) comprueba que el modelo que se está exportando cumple una serie de reglas relacionadas con la modularidad, la compatibilidad `oracle-postgreSQL`, etc. En caso de que alguna de estas reglas no se cumpla, no se realizará la exportación y se mostrará un mensaje de error.

!!!info

    ` update.database ` y ` export.database ` admiten ejecución paralela multihilo para algunas de sus acciones, como la creación de índices o la estandarización de funciones. Por defecto, el número de hilos utilizados se calcula como la mitad del número de núcleos disponibles en la máquina donde se ejecuta la tarea. Este valor puede configurarse añadiendo el parámetro `-Dmax.threads=numOfThreads`. 

### Tareas de prueba

|  Mantenimiento     |  Descripción  |  
|-----------|---------------|
|  `test`  |  Por defecto, se ejecutan todas las pruebas de Etendo. Puede usar `--tests "<package>"` para especificar qué pruebas desea ejecutar.

!!!info
    Para más información sobre la ejecución de pruebas en Gradle, visite [Filtrado de pruebas en Gradle](https://docs.gradle.org/current/userguide/java_testing.html#test_filtering)

### Otras tareas

|  Mantenimiento                   |  Descripción  |
|-------------------------|---------------|
|  `migrate.attachments`  |  Migra los adjuntos al nuevo modelo de adjuntos.
## Tareas comunes de Gradle

!!!danger
    Desde Etendo Classic 25Q1, todas las tareas de Gradle requieren Java 17 o superior. Para añadir compatibilidad con versiones anteriores, se ha añadido el nuevo flag `java.version`.

    ``` bash title="Terminal"
    ./gradlew <task> -Pjava.version=11
    ```

    Este nuevo flag fuerza el uso de Java 11.

- Crea los archivos de propiedades y de configuración.
  
    ``` bash title="Terminal"
    ./gradlew setup 
    
    ```
  
    | Parámetros de línea de comandos | Descripción                                                   |                       
    | ------------------------------- | ------------------------------------------------------------- |
    | `-PforceDefaultProps=true`      | Recrea el archivo de propiedades por defecto desde la plantilla. |
    | `-PforceBackupProps=true`       | Recrea el archivo `backup.properties` desde la plantilla.     |
    | `-PforceQuartzProps=true`       | Recrea el archivo `quartz.properties` desde la plantilla.     |

- Crea los archivos de propiedades a partir de las plantillas de la carpeta `/config`. Las tareas de *configuración* dependen de esta tarea.
    ``` bash title="Terminal"
    ./gradlew prepareConfig
      
    ```

- Crea la base de datos e instala los datos de referencia. 
    ``` bash title="Terminal"
    ./gradlew install
        
    ```

- Compila las clases Java que se modificaron y las despliega en Tomcat.

    ``` bash title="Terminal"
    ./gradlew smartbuild
        
    ``` 
    
    | Parámetro de línea de comandos | Descripción                                                                                                                                |          
    | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
    | `PignoreConsistency=true`      | Flag utilizado para ignorar la verificación de consistencia (verifica las versiones entre los módulos locales y los instalados)          |
    

- Elimina todas las clases Java y las recompila. 
    ``` bash title="Terminal"
    ./gradlew compile.complete
          
    ``` 
       
- Actualiza la base de datos aplicando los cambios en los archivos XML.
    ``` bash title="Terminal"
    ./gradlew update.database
            
    ``` 

- Exporta los cambios de la base de datos a archivos XML
    ``` bash title="Terminal"
    ./gradlew export.database
              
    ``` 
      
- Exporta los datos del Diccionario de Aplicación del módulo.
    ``` bash title="Terminal"
    ./gradlew export.database
                  
    ``` 

- Exporta el script de configuración. 
    ``` bash title="Terminal"
    ./gradlew export.config.script 
                  
    ``` 
   

- Tarea para descargar la dependencia del core.
    ``` bash title="Terminal"
    ./gradlew expandCore
                      
    ``` 
      

    | Parámetro de línea de comandos | Descripción                                                                 |                       
    | ------------------------------ | --------------------------------------------------------------------------- |
    | `-PforceExpand=<true>`         | Flag utilizado para forzar la expansión de fuentes cuando el core está en JAR. |



- Tarea para descargar las dependencias de los módulos en fuentes.
    ``` bash title="Terminal"
    ./gradlew expandModules
                      
    ``` 


    | Parámetro de línea de comandos | Descripción                                                                                                                                    |  
    | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
    | `-Ppkg=<package name>`         | El nombre del módulo que se va a *re expanded* en caso de que ya esté en fuentes. Esto *OVERWRITE* todos los cambios en el módulo.            |

- Tarea para eliminar los directorios creados por la tarea expandCore.
    ``` bash title="Terminal"
    ./gradlew cleanExpandCore
    ```

### Módulo

- Crea el archivo `build.gradle` con toda la información necesaria para publicar.
    ``` bash title="Terminal"
    ./gradlew createModuleBuild
                      
    ```  

    | Parámetros de línea de comandos | Descripción                     |                       
    | ------------------------------- | ------------------------------- |
    | `-Ppkg=<package name>`          | El nombre del módulo.           |
    | `-Prepo=<repository name>`      | El nombre del repositorio.      |




- Publica el módulo en un repositorio personalizado.
    
    ``` bash title="Terminal"
    ./gradlew publishVersion
                            
    ``` 

    | Parámetros de línea de comandos | Descripción                                                                                         | 
    | :------------------------------ | :-------------------------------------------------------------------------------------------------- |
    | `-Ppkg=<packagename>`           | **Obligatorio** El nombre del módulo.                                                               |
    | `-PupdateLeaf=true   `          | Actualiza automáticamente la versión del proyecto que se está publicando. Por defecto `false`.      |


### Desinstalar módulos (uninstallModule) 

**:octicons-package-16: Módulos fuente**

Para desinstalar un módulo de Etendo, necesita ejecutar la tarea de Gradle.

``` bash title="Terminal"
./gradlew uninstallModule -Ppkg=<modulename>
```

Esta tarea intentará eliminar el módulo fuente y las dependencias fuente que dependen de él.

Si el módulo a desinstalar es una dependencia de otro módulo fuente, se lanza una excepción. Puede forzar la desinstalación proporcionando el flag `-Pforce=true`.

**:material-language-java: Módulos JAR**

1. Para desinstalar una dependencia en formato `JAR`, simplemente elimine la dependencia del archivo `build.gradle` y recompile.

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild
    ```

2. Si desea desinstalar una dependencia transitiva, puede utilizar las **Reglas de exclusión de Gradle** (excluir dependencias) para evitar la extracción de una dependencia `JAR`. En el `build.gradle` del proyecto raíz puede especificar la dependencia a excluir: 

    - Excluir dependencias globalmente: 

        ``` groovy title="build.gradle"
        configurations.implementation {
            exclude group: 'com.etendoerp', module: 'test1'
            exclude group: 'com.etendoerp', module: 'test2'
        }
        ```

    - Excluir dependencias transitivas:

        ``` groovy title="build.gradle"
        dependencies {
            implementation("com.etendoerp:test:1.0.0") {
                exclude group: "com.etendoerp", module: "test2"
            }
        }
        ```

    !!! info
        - [Exclusión global de dependencias en Gradle](https://docs.gradle.org/current/userguide/dependency_downgrade_and_exclude.html#sec:excluding-transitive-deps){target="_blank"}
        - [Exclusión de dependencias transitivas en Gradle](https://docs.gradle.org/current/userguide/how_to_exclude_transitive_dependencies.html){target="_blank"}


    !!! tip 
        - También puede utilizar las **Reglas de exclusión de Gradle** si la dependencia pertenece a un módulo fuente, aplicando las reglas en el archivo `build.gradle` del módulo.
        - Un módulo `JAR` también podría ser una dependencia transitiva. Puede ver el árbol de dependencias transitivas ejecutando la tarea de Gradle: `./gradlew dependencies --info` y excluir la dependencia padre raíz.
        - Los módulos `JAR` de Etendo se extraen dinámicamente en el directorio `build/etendo/modules` del proyecto raíz.

    Finalmente, necesita reconstruir el sistema:

    ``` bash title="Terminal"
    ./gradlew update.database compile.complete smartbuild
    ```

### Tareas internas de desarrollo

- Se utiliza para clonar todos los submódulos git de una extensión de módulo (bundle). El `build.gradle` del módulo debe contener la propiedad
      ``` bash title="Terminal"
      ./gradlew cloneDependencies
                                    
      ```

      ```groovy  title="build.gradle"
      ext.defaultExtensionModules = [
          'git@github.com:example1.git',
          'git@github.com:example2.git'
        ]
      ```


      | Parámetro de línea de comandos | Descripción                         |                       
      | ------------------------------ | ----------------------------------- |
      | `-Ppkg=<package name>`         | **Obligatorio** El nombre del bundle |



- Crea todos los archivos `build.gradle` para cada módulo usando la base de datos de `AD_MODULE.xml`.
    ``` bash title="Terminal"
    ./gradlew createModuleBuild
                                          
    ```

    | Parámetro de línea de comandos      | Descripción                                                                                                                                                 |                       
    | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `-Ppkg=<package name>`              | **Obligatorio** El nombre del módulo                                                                                                                        |
    | `-Prepo=<repository name>`          | **Obligatorio** El nombre del repositorio                                                                                                                   |
    | `-Pbundle=<bundle package name>`    | El nombre del bundle                                                                                                                                       |
    | `-Ppkg=all`                         | Crea todos los archivos `build.gradle` para cada módulo; cada `build.gradle` contendrá las dependencias entre proyectos (en el bloque de dependencias).     |
  
      

- Parámetros para sobrescribir el grupo, nombre y versión del core por defecto.

    | Parámetros de línea de comandos     | Descripción                 |                       
    | ----------------------------------- | --------------------------- |
    | `-PcoreGroup=<core group>`          | El nombre del grupo del core |
    | `-PcoreName=<core name>`            | El nombre del core          |
    | `-PcoreVersion=<core version>`      | La versión del core         |


     
- Parámetros para sobrescribir el repositorio por defecto. Publica todos los módulos de un bundle en el directorio de módulos fuente.
    ``` bash title="Terminal"
    ./gradlew publishAll
                                              
    ```

    | Parámetros de línea de comandos     | Descripción                                                                                                                                    |
    | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
    | `-Ppkg=<bundle package name>`      | **Obligatorio** El paquete del bundle                                                                                                          |
    | `-PupdateLeaf=true`                | Actualiza automáticamente la versión de todos los proyectos que se están publicando. Por defecto `false`.                                      |
    | `-Pupdate=<major, minor, patch>`   | Se utiliza para especificar qué parte de la versión se actualizará. Por defecto `patch`.                                                       |
    | `-PpushAndTag=true`                | Se utiliza para especificar si los módulos publicados deben hacer push de los cambios y crear un tag en el repositorio git. Por defecto `false`. |
    | `-PpushAll=true`                   | Se utiliza para especificar si todos los módulos deben ejecutar el push y el tag. Por defecto `false`.                                         |
        

- Tarea utilizada para hacer push y tag de los cambios de los módulos.
    ``` bash title="Terminal"
    ./gradlew pushToGit
                                                          
    ```

    | Parámetros de línea de comandos | Descripción                                                                                  |
    | ------------------------------- | -------------------------------------------------------------------------------------------- |
    | `-PpushAll=true`                | Se utiliza para especificar si todos los módulos deben ejecutar el push y el tag. Por defecto `false`. |
        
 

- Actualiza la versión de una dependencia en cada submódulo `build.gradle`.
    ``` bash title="Terminal"
    ./gradlew updateModuleBuildDependency
                                                              
    ```

    !!! warning
        Si introduce una versión incorrecta, debe revertir los cambios manualmente.


    | Parámetros de línea de comandos            | Descripción                                                                                                                                 |
    | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
    | `-Pdependency=<dependency name>`           | El nombre del módulo a actualizar en cada `build.gradle`. Por defecto `com.etendoerp.platform.etendo-core`                                  |
    | `-PlowerBound=<version>`                   | El límite inferior de versión. Ejemplo: `-PlowerBound=1.0.3`                                                                                |
    | `-PlowerBoundInclusive=<true or false>`    | Por defecto `false`.                                                                                                                        |
    | `-PupperBound=<version>`                   | El límite superior de versión. Ejemplo: `-PupperBound=1.0.3`                                                                                |
    | `-PupperBoundInclusive=<true or false>`    | Por defecto `false`.                                                                                                                        |
    | `-PexactVersion=<version>`                 | Sustituirá la versión actual por la especificada. La versión debe ir entre comillas. Ejemplo: `-PexactVersion="[1.0.3]"`                    |



### Tareas de Ant

La mayoría de las [tareas de compilación de ant](#detailed-build-tasks) utilizadas anteriormente se pueden ejecutar con Gradle:

```bash title="Terminal"
./gradlew <ant task> [params]
```

Excepto algunos comandos:

| Comando antiguo   | Comando nuevo | 
| ----------------- | ------------- | 
| `clean`           | `antClean`    |
| `setup`           | `antSetup`    |
| `init`            | `antInit`     |
| `install.source`  | `antInstall`  |
| `war`             | `antWar`      |
## Resolución de conflictos

!!!note
    Etendo hace uso de la [Estrategia de resolución de conflictos](https://docs.gradle.org/current/userguide/dependency_resolution.html){target="_blank"} ofrecida por Gradle.

Este enfoque se utiliza para identificar conflictos entre artefactos de Etendo publicados en un repositorio.

Por ejemplo, cuando hace uso de un módulo de Etendo, que depende del core de Etendo

```groovy title="build.gradle"
group          = 'com.etendoerp'
ext.artifact   = "moduleCextract"
version        = '1.0.1'
dependencies {
    // Etendo CORE dependency
    implementation 'com.etendoerp.platform:etendo-core:[22.1.1, 22.1.2]'
}
```

y actualmente está trabajando con el core de Etendo en `22.1.0`, entonces se encuentra una resolución de conflictos.

Dependiendo del tipo de conflicto, si el problema es con el core de Etendo, entonces se lanzará una excepción.

!!!danger "Para forzar la resolución de dependencias, este debe ser el último paso a seguir"
    Puede forzar la resolución usando el flag de la extensión
    ``` groovy
    etendo {
      forceResolution = true
    }
    ```

    Si desea omitir la resolución, puede añadir el flag a la extensión del plugin.
    ``` groovy
    etendo {
      performResolutionConflicts = false
    }
    ```
## Consistencia de versiones

El enfoque de consistencia de versiones verifica que un artefacto JAR de Etendo extraído sea consistente con el instalado (misma versión).

Cuando se añade una nueva dependencia JAR de Etendo o se actualiza la versión, es necesario ejecutar `update.database` antes de ejecutar cualquier tarea de compilación (smartbuild, compile.complete, etc.).
Puede forzar las tareas de compilación añadiendo en la extensión del plugin de Etendo el flag de ignorar.

!!!warning "Esta sección explica cómo ignorar la verificación de consistencia. Utilice este enfoque solo si no hay conflictos entre versiones."
    ``` groovy
    etendo {
      ignoreConsistencyVerification = true 
    }
    ```
    o ejecute las tareas con el flag `-PignoreConsistency=true`.

    De forma predeterminada, Etendo no le permite añadir una dependencia JAR con una versión antigua respecto a la instalada actualmente.
    Puede ignorar este comportamiento añadiendo como configuración el nombre del módulo que se va a actualizar con una versión antigua.
    ``` groovy
    etendo {
      ignoredArtifacts = ['com.etendoerp.mymodulename']
    }
    ```
## Recompilar archivos CSS

**Requisitos**

  - *Node.js*: Versión 16 o superior.
  - *npm*: Gestor de paquetes de Node.
  - *Sass*: Debe tener instalado un compilador de Sass.


??? info "Cómo instalar Node.js, npm y Sass"

    === ":simple-linux: Linux"
        
        **Node.js 16.10.0 usando NVM:**
        
        1. Instale NVM (Node Version Manager):
        ```bash
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
        ```
        Cierre y vuelva a abrir su terminal para empezar a usar NVM, o ejecute los siguientes comandos:
        ```bash
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
        ```
        
        2. Instale la versión 16.10.0 de Node.js:
        ```bash
        nvm install 16.10.0
        ```

            **Nota:** Si encuentra errores durante la instalación de Node.js con el comando `nvm install 16.10.0`, puede deberse a que `curl` no está instalado o está mal configurado en su sistema. En esos casos, puede intentar ejecutar los siguientes comandos:

            ```bash
            sudo snap remove curl
            sudo apt install curl
            ```

            Después de configurar correctamente `curl` mediante este método, vuelva a esta guía y ejecute los pasos anteriores para instalar NVM y configurar Node.js.
        
        3. Establezca la versión 16.10.0 de Node.js como versión predeterminada:
        ```bash
        nvm use 16.10.0
        nvm alias default 16.10.0
        ```
        
        4. Verifique la instalación:
        ```bash
        node -v
        npm -v
        ```


    === ":simple-macos: Mac OS"

        **Instalación de Homebrew:**

        - Instale Homebrew ejecutando el siguiente comando en la terminal:

        ```bash
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```

        - Una vez instalado Homebrew, verifíquelo comprobando su versión:

        ```bash
        brew --version
        ```

        **Instalación de Node.js y npm usando Homebrew:**
            
        1. Actualice Homebrew (asegurándose de tener las definiciones de paquetes más recientes):
        ```bash
        brew update
        ```

        2. Instale Node.js y npm:
        ```bash
        brew install node
        ```

        3. Verifique la instalación de Node.js y npm:
        ```bash
        node -v
        npm -v
        ```


    === ":material-microsoft-windows: Windows"
        
        **Node.js y npm:**
        
        1. Descargue el instalador de Node.js para Windows desde el [sitio web oficial](https://nodejs.org/){target="_blank"}.
        
        2. Ejecute el instalador y siga las instrucciones.
        
        3. Después de la instalación, abra un símbolo del sistema o PowerShell y verifique la instalación:
        ```powershell
        node -v
        npm -v
        ```

    **Instalar npm (Node Package Manager)**

    Si no tiene npm instalado en su sistema, siga estos pasos:

    - Instale npm globalmente usando el siguiente comando:

    ```bash
    npm install -g npm
    ```

    - Confirme la instalación comprobando las versiones de node y npm:

    ```bash
    node -v
    npm -v
    ```

    **Instalar Sass (Syntactically Awesome Style Sheets)**
    
    Si tiene npm instalado y necesita el compilador de Sass, siga estas instrucciones:

    - Use npm para instalar Sass globalmente en su sistema:

    ```bash
    npm install -g sass
    ```

    - Confirme la instalación de Sass ejecutando:

    ```bash
    sass --version
    ```

    Ver el número de versión de Sass significa que Sass se ha instalado correctamente.

**Ejecución**

La tarea `cssCompile` en la configuración de Etendo Gradle está diseñada específicamente para convertir archivos `.scss` en archivos `.css`. Para personalizar el skin de Etendo, deberá trabajar con archivos `.scss`. 

``` bash title="Terminal"
./gradlew cssCompile smartbuild
```


Después de ejecutar la tarea, busque la siguiente salida para indicar una compilación correcta:
!!! success "Ejecución correcta"
    Después de ejecutar la tarea, la siguiente salida indica una compilación correcta:

    ```
    > Task :cssCompile
    > BUILD SUCCESSFUL
    ```

    Esto confirma el procesamiento correcto de los archivos.

Por último, reinicie Tomcat para aplicar los cambios y asegurarse de que los archivos `.css` actualizados se despliegan correctamente.
## Proceso de eliminación de cliente

La tarea `delete.client` permite ejecutar el Proceso de eliminación de cliente directamente desde gradlew. Esta tarea también permite ejecutar este proceso con el servicio Tomcat detenido para evitar bloqueos en la base de datos.

``` bash title="Terminal"
./gradlew delete.client

```

| Parámetros de línea de comandos           | Descripción                                                                                                              |
|  -------------------                      | ------------------------------------                                                                                     |
| `-DclientId=<AD_Client_ID>`               | `AD_Client_ID` de la tabla `AD_Client` que se utilizará en este proceso para eliminar toda la información de este cliente. |

!!!danger "Proceso peligroso"
    Esta tarea ejecuta el mismo proceso heredado que puede ejecutar en la aplicación con el rol de Administrador del sistema. Es una tarea muy sensible; debe tener mucho cuidado, ya que esto puede provocar fallos en el sistema si se utiliza incorrectamente.
    <br>**Se recomienda realizar una copia de seguridad antes de ejecutar el mantenimiento.**



---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.