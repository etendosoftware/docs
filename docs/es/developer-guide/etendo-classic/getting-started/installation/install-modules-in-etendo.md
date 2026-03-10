---
title: Instalar módulos en Etendo Classic
tags:
    - Primeros pasos
    - Instalar
    - Módulos
    - Bundles
    - Dependencias
    - Gestor de dependencias
---

# Instalar módulos en Etendo Classic
## Visión general
Esta guía explica dos formas diferentes de instalar módulos en Etendo Classic:

- **Instalación estándar con Gradle**: este método implica definir manualmente las dependencias en el archivo `build.gradle` del proyecto, especificando los módulos que se incluirán en formato JAR o en formato código fuente.

- **Uso del gestor de dependencias**: un módulo preinstalado en las instancias de Etendo que permite gestionar e instalar dependencias directamente desde la interfaz de usuario de Etendo Classic, sin necesidad de editar manualmente archivos de configuración.

![alt text](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/overview.png)

!!! warning "Aviso importante"
    Se recomienda encarecidamente elegir **un único método** para gestionar dependencias: **Instalación estándar con Gradle** o el **gestor de dependencias**. Una vez que empiece a utilizar el **gestor de dependencias**, este tiene prioridad sobre el archivo `build.gradle`, y la información de dependencias se gestionará a través de la base de datos. No se admite combinar ambos métodos y puede dar lugar a comportamientos inesperados o incoherencias durante la instalación o la actualización de módulos.
##  Autenticación

Es importante mencionar que las dependencias se resuelven desde GitHub, por lo que debe tener las credenciales configuradas correctamente tal y como se explica en el documento [Uso de repositorios en Etendo](../../../etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md). 
Dependiendo del nivel de acceso que tenga su usuario de GitHub, tendrá acceso a paquetes públicos o privados (comerciales).

!!! success "Info"
    Junto con su licencia, tiene acceso a todos los paquetes distribuidos por Etendo.
## Instalación estándar de Gradle

<iframe width="560" height="315" src="https://www.youtube.com/embed/gY0kLINlyq0?si=fGXiZ9wJsw-Bhs2B" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Lista de verificación

:octicons-check-circle-16: **Configurar credenciales**.<br>
:octicons-check-circle-16: **Buscar módulos o bundles para instalar**.<br>
:octicons-check-circle-16: **Elegir el formato del módulo (código fuente o JAR)**.<br>
:octicons-check-circle-16: **Configurar las dependencias en el archivo `build.gradle`**.<br>
:octicons-check-circle-16: **Expandir el código fuente o resolver dependencias dinámicas (JAR)**.<br>
:octicons-check-circle-16: **Instalar módulos**.<br>
:octicons-check-circle-16: **Reiniciar el servicio de Tomcat y verificar la instalación**.<br>


### Buscar dependencias
Existen dos opciones para buscar e instalar módulos en Etendo Classic. Seleccione una de las siguientes:

=== ":material-store: Marketplace"

    Puede instalar módulos desde **Etendo Marketplace**, que contiene paquetes agrupados por funcionalidad.

    ![](../../../../assets/drive/LWaskO0G5UdmwGWdwZy5nHf4FcCTMBcgObbWv_PSjtMPCOAeqBPNSoLKrqheTLiNqc_aiqbVrJYYJlCQ_o7rGGofcqN0-myRi3u3YpXYNuVt1FYIli0RbiWYD8hYGcDLMpRYVS_dHOGGOLY117nmB2o.png)

    Pasos a seguir:

    1. Abra [Etendo Marketplace](http://marketplace.etendo.cloud){target="_blank"}.
    2. **Selector** del módulo o bundle que desea instalar.
    3. **Selecciónelo** para ver detalles e instrucciones.
    4. Elija la **Versión de Etendo Classic**, para determinar el rango de compatibilidad de la dependencia.
    5. **Copie** la línea de instalación en el formato que prefiera: **Código fuente** (permite personalizaciones) o **JAR** (precompilado).

    ![alt text](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/install-marketplace.png)

    !!! info 
        Al seleccionar la **Versión de Etendo Classic**, se determina el rango de compatibilidad, lo que garantiza que siempre se resuelva a la última versión disponible para esa versión de Etendo.
    
    !!! tip 
        Además, en cada bundle encontrará un enlace a las notas de la versión con más información sobre cada versión, compatibilidades y más.   

    !!! tip
        Si su instancia de Etendo Classic es anterior a las versiones soportadas, debe seleccionar la versión 24.x
    
    !!! danger "No recomendado"
        Evite usar la versión `latest.release`, ya que puede no ser compatible con su versión actual de Etendo.

=== ":simple-github: GitHub Packages"

    Si desea instalar módulos específicos directamente desde GitHub:

    Pasos a seguir:

    1. Visite la sección de paquetes en [Etendo Software GitHub](https://github.com/orgs/etendosoftware/packages){target="_blank"} o busque dentro de su propio repositorio.
    2. Seleccione el módulo requerido para obtener la información necesaria.
    3. Copie la información del módulo para incluirla en su archivo `build.gradle`.

    Por ejemplo, para instalar el módulo [Banking Pool](/user-guide/etendo-classic/optional-features/bundles/financial-extensions/overview/#banking-pool), copie allí la información proporcionada.

    ![search-packages.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/search-packages.png)
    ![package.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/package.png)

### Configurar dependencias en Etendo Classic 

En función del formato de los módulos con el que quiera trabajar:

- En el proyecto de Etendo, abra el archivo `build.gradle`.
- En el área de dependencias, pegue los módulos o el bundle a instalar.

=== ":octicons-package-16: Formato de fuentes"

    Si quiere trabajar con módulos en código fuente, declare sus dependencias usando la configuración **moduleDeps** (observe la extensión @zip).

    ```groovy title="Plantilla de ModuleDeps"
        moduleDeps('<groupId>:<artifactId>:<version>@zip'){ transitive = true }
    ```

    P. ej.:

    ```groovy title="build.gradle"
    dependencies {
        // Add your dependency here
        moduleDeps('com.etendoerp:production.extensions:[3.0.0,4.0.0)@zip'){ transitive = true }    
    }
    ```

===  ":material-language-java: Formato JAR"

    Si quiere trabajar con módulos JAR, declare sus dependencias usando la configuración **implementation**.

    ```groovy title="Plantilla de Implementation"
        implementation('<groupId>:<artifactId>:<version>')
    ```
    P. ej.:

    ```groovy title="build.gradle"
    dependencies {
    // Add your dependency here
        implementation('com.etendoerp:production.extensions:[3.0.0,4.0.0)')
    }
    ```


!!! info
    - Puede declarar una versión específica (p. ej. '1.0.0') o un intervalo de versiones: <br>
    - \[begin, end\] Ambas versiones están incluidas <br>
    - (begin, end)  Ambas versiones no están incluidas <br>
    - \[begin, )  Desde una versión base hasta la última <br>
    - Y cualquier otra combinación posible.

!!! tip "Reglas de exclusión de Gradle - Excluir dependencias"
    Puede utilizar reglas de exclusión de Gradle para evitar descargar un módulo transitivo específico. Consulte la [Documentación de Gradle](https://docs.gradle.org/current/userguide/how_to_exclude_transitive_dependencies.html){target="_blank"}


### Resolver dependencias


=== ":octicons-package-16: Formato de fuentes"

    Para trabajar con código fuente, debe expandir manualmente los módulos usando una tarea de **Gradle**.

    ``` bash title="Terminal" 
    ./gradlew expandModules
    ```  
    
    Esta tarea intentará descargar o actualizar los módulos declarados como **moduleDeps** en el archivo `build.gradle`.  
    Se muestra un menú con los módulos que se van a expandir; debe confirmar manualmente para continuar con la expansión.

    ![expand.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/expand.png)

    !!! tip
        Solo se expandirá la dependencia principal definida en formato **Código fuente** (moduleDeps). Si quiere que todas las dependencias transitivas también se resuelvan en este formato, configure la propiedad `supportJars` a `false` en el archivo `build.gradle`:

        ```groovy title="build.gradle"
        etendo {
            supportJars = false
        }
        ```
        Esto garantiza que todas las dependencias se expandan como código fuente en lugar de usar archivos JAR.

    !!! tip 
        Para expandir solo un módulo específico, puede usar el flag `-Ppkg` y tener definido el módulo en la configuración **moduleDeps**.

        ```bash title="Terminal"
        ./gradlew expandModules -Ppkg=com.etendoerp.custommodule
        ```

===  ":material-language-java: Formato JAR"

    Para trabajar con módulos JAR, necesita resolver las dependencias explícitamente ejecutando la tarea `dependencies`, que muestra el árbol de dependencias resuelto:

    ```bash title="Terminal"
    ./gradlew dependencies
    ```

    No obstante, tenga en cuenta que, al ejecutar cualquier tarea de Gradle, las dependencias JAR (declaradas con `implementation`) se resuelven dinámicamente de antemano. 

    Cuando se añade una nueva dependencia **JAR** de Etendo o se actualiza su versión, es necesario ejecutar **update.database** antes de ejecutar cualquier tarea de **compilación** (p. ej., `smartbuild`, `compile.complete`, etc.).
    
    !!! tip
        Puede forzar las tareas de compilación añadiendo a la extensión de Etendo el flag de ignorar

        ```groovy title="build.gradle"
        etendo {
            ignoreConsistencyVerification = true
        }
        ```

        O ejecutar las tareas con el flag `-PignoreConsistency=true`.

    
    !!! warning
        Por defecto, Etendo no le permite añadir una *dependencia JAR* con una versión anterior a la actualmente instalada.
        
        Puede ignorar este comportamiento añadiendo el nombre del módulo que se va a actualizar con una versión anterior en el

        ```groovy
        etendo {
            ignoredArtifacts = ['com.etendoerp.mymodulename']
        }
        ```

### Instalar dependencias

Por último, actualice la base de datos y compile los nuevos módulos.

```bash title="Terminal"
./gradlew update.database smartbuild 
```

!!! success ":simple-apachetomcat: Reiniciar Tomcat"
    Reinicie el servidor Tomcat y compruebe la instalación. <br>
    El módulo está listo para usarse en Etendo!
## Gestor de dependencias
:octicons-package-16: Paquete Java: `com.etendoerp.dependencymanager`

<iframe width="560" height="315" src="https://www.youtube.com/embed/du8EYoSsZ68?si=HDmwg-JxPg7gJ2sT" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- Con este módulo, el usuario puede acceder desde la interfaz de Etendo Classic a todos los paquetes de Etendo publicados en los repositorios de Etendo Software.
- Además, desde la ventana Gestión de módulos puede consultar paquetes, versiones disponibles, dependencias e instalar nuevos paquetes.
- A continuación, desde la ventana Gestión de dependencias puede actualizar, eliminar y cambiar el formato de los módulos ya instalados.

### Instalación

El **Gestor de dependencias** se distribuye por defecto en las versiones actuales de Etendo Classic; en caso de que no esté instalado en su instancia, puede hacerlo siguiendo la sección [Instalación estándar de Gradle](#instalación-estándar-de-gradle) descrita anteriormente.

!!! tip
    Puede encontrar el módulo en Etendo Marketplace en el siguiente enlace: [Gestor de dependencias - Marketplace](https://marketplace.etendo.cloud/#/product-details?module=CBD09C84BFB2469096758C3297F1C7A9)

!!! warning
    Debe asegurarse de utilizar Etendo Gradle Plugin en la versión `1.5.1` o superior; compruebe la sección de plugins en el archivo `build.gradle`. Para más información sobre las versiones del plugin, consulte [Etendo Gradle Plugin - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md)

### Ventanas de gestión de módulos
:material-menu: `Aplicación` > `Gestión de dependencias de Etendo` > `Gestión de módulos`
    
Con la sesión iniciada con el rol de Administrador del sistema, en la ventana `Gestión de módulos`, el usuario puede ver todos los módulos que se van a añadir y seleccionar la versión correspondiente en la pestaña **Versión**. Una vez seleccionada una de las versiones, las dependencias de dicha versión pueden encontrarse en la subpestaña **dependencias**.

![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager1.png)

!!!info
    Los campos de esta ventana son de solo lectura.

Campos a tener en cuenta:

- **Activo**: casilla de verificación para seleccionar si este módulo está activo o no.
- **Grupo**: el identificador del artefacto.
- **Artefacto**: la unidad de despliegue obtenida y utilizada.
- **Versión instalada**: la versión del módulo si está instalado.
- **Es bundle**: campo para filtrar si este módulo es un bundle o no.

Esta ventana presenta dos botones que pueden utilizarse: **Añadir dependencia** y **Actualizar paquetes**.

#### Botones
##### Botón Añadir dependencia

Este botón permite añadir las dependencias asociadas a una versión específica del módulo seleccionado. Al hacer clic, una ventana emergente mostrará todas las dependencias y módulos que se instalarán.

- **Si se selecciona un bundle de paquetes**: tendrá la opción de añadir todos los módulos dentro del bundle o seleccionar solo los que necesite. A continuación, aparecerá una nueva cuadrícula de solo lectura, mostrando las dependencias de los módulos seleccionados. Esta cuadrícula es informativa y le permite ver qué dependencias se añadirán.

- **Si se selecciona un paquete que no es bundle**: la cuadrícula será de solo lectura y mostrará únicamente las dependencias necesarias para que el módulo funcione correctamente. Si no se muestran dependencias, significa que el módulo no tiene dependencias adicionales.

!!! warning
    Se muestra una notificación de advertencia para informar al usuario sobre la compatibilidad de versiones antes de instalar las dependencias mostradas.

!!!info
    Tenga en cuenta que, por defecto, todas las dependencias se añaden en formato Source.

![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager2.png)

Una vez finalizado el proceso, se abre la ventana **Gestión de dependencias** y se muestran todas las dependencias instaladas.

**Reglas de gestión de versiones de dependencias**

1. **Si la versión de la dependencia es mayor que la versión instalada:**:

    - No hay módulo instalado y no hay registro en la ventana `Gestión de dependencias`: se añade un nuevo registro de dependencia.
    - No hay módulo instalado pero existe un registro en la ventana `Gestión de dependencias`: se actualiza la versión del registro existente.
    - Hay módulo instalado y existe el registro de dependencia en la ventana `Gestión de dependencias`: se actualiza la versión del registro existente.
    - Hay módulo instalado pero no existe registro de dependencia en la ventana `Gestión de dependencias`: se elimina la dependencia local y se añade un nuevo registro en `Gestión de dependencias`.

2. **Si la versión de la dependencia es menor que la versión instalada:**

    - Se muestra un error y se deshabilita el proceso, evitando la instalación de una versión anterior para prevenir problemas de compatibilidad. Este enfoque garantiza que las dependencias se gestionen correctamente, manteniendo la compatibilidad y minimizando el riesgo de pérdida de funcionalidad. En caso de que necesite instalar igualmente esa versión de la dependencia, debe degradar la versión desde la ventana `Gestión de dependencias` con el botón [cambiar versión](#cambiar-versión).

##### Botón Actualizar paquetes

Este botón se utiliza para ejecutar el proceso Actualizar paquetes, que actualiza la lista de paquetes disponibles con la información más reciente.

### Ventanas de gestión de dependencias
:material-menu: `Aplicación` > `Gestión de dependencias de Etendo` > `Gestión de dependencias`

Con la sesión iniciada con el rol de Administrador del sistema, en la ventana `Gestión de dependencias`, el usuario puede encontrar todas las dependencias instaladas en el paso anterior.

![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager3.png)

Campos a tener en cuenta:

- **Activo**: casilla de verificación para seleccionar si esta dependencia está activa o no.
- **Grupo**: el identificador del artefacto.
- **Artefacto**: la unidad de despliegue obtenida y utilizada.
- **Versión**: versión del módulo.
- **Formato**: describe el formato de la dependencia. Puede ser `Source`, `JAR` o `local`.
    - `Source`: en este caso, el código fuente está disponible; para descargar las dependencias el usuario debe ejecutar la tarea de Gradle `./gradlew expandModules` y después es necesaria la compilación.
    - `JAR`: en este caso, un formato estándar para la distribución de paquetes Java; incluye las clases Java compiladas y la resolución de dependencias es dinámica.
    - `Local`: el formato local implica que el módulo está instalado, pero no está declarado como una dependencia de repositorio.
- **Estado de instalación**: describe el estado actual de la dependencia.
    - Pendiente de descarga: este es el estado por defecto cuando se añade o actualiza una nueva dependencia. Para instalarla, es necesario compilar el entorno y, en ese caso, la dependencia está en formato `source`.
    - Instalado: se utiliza cuando la dependencia ya está instalada.
- **Módulo**: una referencia que aparece al módulo cuando está instalado.
- **Estado de versión**: describe el estado de la versión de la dependencia.
    - Sin seguimiento: solo para dependencias externas y locales.
    - Actualización disponible: en caso de que existan nuevas versiones disponibles.
    - Actualizado: está instalada la última versión disponible.
- **Dependencia externa** (solo disponible para dependencias `JAR`): casilla de verificación que identifica una librería externa o módulo requerido por el proyecto, gestionado por Gradle. Estas dependencias se recuperan desde repositorios remotos durante el proceso de build.

#### Botones

##### Cambiar versión

![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager4.png)

Este botón se utiliza para actualizar o degradar versiones.

Cuando se modifica la versión de un módulo, sus dependencias relacionadas también podrían modificarse. En este caso, es posible añadir nuevas versiones, actualizar o eliminar versiones.

!!! warning
    Se muestra una notificación de advertencia para informar al usuario sobre la compatibilidad de versiones antes de ejecutar el proceso.

##### Cambiar formato

![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager6.png)

Este botón se utiliza para cambiar el formato del módulo. Este proceso debe ejecutarse cuando sea necesario migrar desde un formato local a una dependencia de Gradle, manteniendo los módulos actualizados. Las opciones son `source`, `JAR` o `local`.

- En caso de que el módulo esté originalmente en formato `local`, las opciones en la ventana emergente **Cambiar formato** son `JAR` o `source`.

- En caso de que el módulo esté originalmente en formato `source`, la única opción en la ventana emergente **Cambiar formato** es `JAR`.

- En caso de que el módulo esté originalmente en formato `JAR`, la única opción en la ventana emergente **Cambiar formato** es `source`. En este caso, la ventana muestra una notificación de advertencia para recordar al usuario que el directorio original se elimina una vez finalizado el proceso.

##### Eliminar dependencia

Este botón se utiliza para eliminar dependencias.

- **Dependencia en formato JAR**: en caso de que necesite eliminar una dependencia, para completar realmente la acción es necesario compilar el entorno.

    ![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager7.png)

- **Dependencia en formato local o Source**: en caso de que necesite eliminar una dependencia, para completar realmente la acción es necesario compilar el entorno. Además, tenga en cuenta que tanto las dependencias `Source` como `Local` deben eliminarse manualmente de la carpeta `/modules` antes de la compilación.

    ![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager8.png)

    !!! warning
        Se muestra una notificación de advertencia para informar al usuario de los pasos para eliminarla.

### Proceso Añadir dependencias locales
:material-menu: `Aplicación` > `Gestión de dependencias de Etendo` > `Añadir dependencias locales`

![](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/install-modules-in-etendo/dependencymanager5.png)

Este proceso, en la ventana `Añadir dependencias locales`, que también forma parte de la **Gestión de dependencias**, se encarga de identificar todos los módulos instalados localmente sin dependencias relacionadas y añadirlos a la ventana Gestión de dependencias con el formato `local`.

!!! note
    El objetivo principal de este proceso es añadir las dependencias en formato `local`, de modo que, en caso de distribuirse como un módulo de Etendo, pueda migrarse fácilmente a formato `Sources` o `Jar`.

### Proceso Actualizar información de paquetes
:material-menu: `Aplicación` > `Gestión de dependencias de Etendo` > `Actualizar información de paquetes`

Dado que la información sobre los paquetes se actualiza diariamente, el usuario puede ejecutar manualmente el proceso desde la ventana `Actualizar información de paquetes` para actualizar la lista de paquetes con la información más reciente.

!!!info
    El mismo proceso puede ejecutarse desde la ventana **Gestión de módulos**, seleccionando un registro y haciendo clic en el botón **Actualizar paquetes**.

!!!note
    Cada vez que se reinicia el servidor, el proceso de actualización se ejecuta automáticamente.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.