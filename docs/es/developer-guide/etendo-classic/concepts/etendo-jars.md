---
title: JAR de Etendo
tags:
    - JAR de Etendo
    - Bibliotecas Java
    - Configuración de Gradle
    - Publicación de Módulos
---
## Visión general

La nueva versión de Etendo incluye un nuevo plugin que está enfocado en los JAR.

Un [JAR](https://docs.oracle.com/javase/8/technotes/guides/jar/jarGuide.html){target="_blank"} (Java ARchive) es un formato de archivo empaquetado que contiene clases compiladas, información de metadatos y recursos para una aplicación Java en un único archivo. 

Un archivo JAR proporciona múltiples beneficios:

-   Seguridad
-   Portabilidad
-   Compresión
-   Empaquetado
-   Distribución


Un caso común de uso de los JAR son las bibliotecas.

Con [Gradle](https://gradle.org/){target="_blank"} puede hacer uso de bibliotecas para incorporar nueva funcionalidad a su aplicación.

Usando la configuración 'implementation' proporcionada por gradle, puede definir múltiples dependencias:

`implementation 'groupId:artifactId:version'`

Por ejemplo, para hacer uso de la [biblioteca de correo Javax](https://mvnrepository.com/artifact/javax.mail/mail/1.4.7){target="_blank"} necesita definir el siguiente bloque de código en el archivo de compilación de gradle.
``` groovy
dependencies {
	// https://mvnrepository.com/artifact/javax.mail/mail
	implementation group: 'javax.mail', name: 'mail', version: '1.4.7'
}
```


El plugin de Etendo intenta utilizar este enfoque, gestionando todas las bibliotecas y dependencias que necesita para ejecutar su entorno de Etendo.

---

### Módulos JAR de Etendo

Los Módulos son un aspecto importante de Etendo, le permiten crear e introducir nueva funcionalidad en su aplicación.

Para obtener todos los beneficios de un archivo JAR, el nuevo plugin permite al usuario crear una versión JAR de un módulo con toda la configuración necesaria para ser publicada y distribuida.


#### Permisos
Para obtener permisos para publicar una nueva versión de un módulo necesita ejecutar:

`./gradlew registerModule -Ppkg=<package name> -Prepo=<repository rame>`

Esta tarea le otorga privilegios para publicar en el repositorio especificado. También ejecuta internamente la tarea **createModuleBuild** para generar el archivo **build.gradle**.

!!! warning
    Si ya tiene permisos para publicar y el archivo **build.gradle** ya existe, no tiene que ejecutar esta tarea.

El **build.gradle** es un archivo que contiene toda la configuración e información utilizada cuando el módulo se publica.

Los Módulos que contienen un archivo **build.gradle** ahora se reconocen como subproyectos de Gradle, creando una [compilación multiproyecto](https://docs.gradle.org/current/userguide/multi_project_builds.html){target="_blank"}.


!!! info
    Si solo quiere generar el archivo **build.gradle** puede ejecutar
    `./gradlew createModuleBuild -Ppkg=<package name> -Prepo=<repository rame>`
    Este comando **sobrescribirá** el archivo build.gradle si ya está presente.

#### Publicación

Para publicar una nueva versión de un módulo necesita ejecutar

`./gradlew publishVersion -Ppkg=<package name> -Prepo=<repository rame>`


Esta tarea crea la versión JAR y ZIP del módulo, e intenta publicarla en el repositorio especificado.

!!! info
    El módulo necesita compilarse antes de publicarse. Tiene que estar trabajando en un entorno compilado con todas las entidades autogeneradas creadas.

!!! info
    Para más información, consulte la [guía How to Publish Modules to a GitHub Repository](../../../developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository.md)


<br>

#### Estructura del archivo JAR
Los **Módulo** JAR de Etendo contienen una estructura especial. Todo el contenido del directorio ***src*** se incluirá en la raíz del JAR, junto con las clases Java compiladas. 
Otros directorios como ***src-db***, ***src-util***, etc., se almacenarán en la ubicación '***META-INF/etendo***'.


#### Uso de un Módulo JAR de Etendo
Para usar una versión publicada de un módulo en su entorno de Etendo, necesita definir la dependencia en el archivo '**build.gradle**' del proyecto raíz.

Al igual que una biblioteca, usando la configuración implementation:

`implementation 'moduleGroupId:moduleArtifactId:moduleVersion'`

El plugin de Etendo intentará resolver automáticamente el artefacto. Si la dependencia es un módulo de Etendo, se ubicará en el directorio '**build/etendo/modules**'.

El directorio '**build/etendo/modules**' es una nueva ubicación especial. Las tareas de desarrollo de Etendo ahora utilizarán este lugar como una nueva ubicación de módulos para buscar.

### JAR del núcleo de Etendo

Con la nueva versión de Etendo, todavía puede trabajar con el código en fuentes o con el nuevo formato **JAR**.

El nuevo JAR del núcleo de Etendo contiene una estructura similar a la de los módulos JAR.

Para hacer uso del JAR del núcleo de Etendo, al igual que una biblioteca, necesita definir la dependencia en el **build.gradle** del proyecto raíz

``` groovy
dependencies {
  implementation group: 'com.etendoerp.platform', name: 'etendo-core', version: '22.1.0'
}
```

Una vez que el artefacto se resuelve, el plugin de Etendo identificará que la dependencia es el núcleo de Etendo, y se ubicará en el directorio '**build/etendo**'.

Se creará un directorio de configuración en el proyecto raíz. Este directorio contiene las plantillas de configuración utilizadas por Etendo para ejecutar la aplicación.

Necesita establecer sus propias configuraciones usando un archivo **gradle.properties** y ejecutar:

`./gradlew setup`

Una vez creados los archivos de configuración, puede instalar la aplicación.

`./gradlew install`

Todas las tareas de desarrollo de Etendo utilizadas con el núcleo en fuentes deberían seguir funcionando con JAR.


!!! info
    El núcleo de Etendo, (**Fuentes** y **Jar**), permite al usuario trabajar con Módulos en ambos formatos.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.