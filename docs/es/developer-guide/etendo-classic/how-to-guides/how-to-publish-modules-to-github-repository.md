---
title: Cómo publicar módulos en un repositorio de GitHub
tags:
    - How to
    - GitHub
    - Despliegue de módulos
    - Gradle
    - Publicar módulos
---
## Visión general

Este artículo explica cómo publicar un módulo en GitHub Repositories.

Ahora, los módulos se publicarán en formato ZIP y JAR.

Un módulo publicado puede declararse como una dependencia de Gradle, lo que facilita la instalación o actualización de módulos.

El uso de dependencias junto con Gradle en un entorno Etendo puede eliminar la necesidad de transferir los módulos desde una máquina local al servidor mediante FTP, SSH, etc. El módulo se aloja como un paquete en el repositorio y Gradle se encarga de descargar la versión correcta y sus dependencias.

Los partners tendrán acceso a los repositorios públicos y comerciales de Etendo para descargar módulos estándar; además, es posible utilizar sus propios repositorios donde pueden almacenar sus módulos de forma privada para uso interno o comercial.

!!! info "Requisitos"
    
    - Usuario y token de GitHub, con acceso para leer y escribir paquetes.
    - Un módulo para distribuir.

!!! success
    Se recomienda utilizar [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow){target="_blank"} para gestionar el flujo de trabajo, las versiones y las etiquetas.

## Despliegue

!!! info
    
    La versión del módulo, el grupo y el artefacto que se desplegarán son los declarados en el archivo `src-db/database/sourcedata/AD_MODULE.xml`


#### 1.  Crear el archivo build.gradle:

Para generar el `build.gradle` con toda la información necesaria para publicar, ejecute la siguiente tarea:

``` bash title="Terminal"
./gradlew createModuleBuild -Ppkg=<javapackage> -Prepo=<repositoryURL> --info
```
Ejemplo:
``` bash title="Terminal"
./gradlew createModuleBuild -Ppkg=com.myrepo.test -Prepo=https://maven.pkg.github.com/myrepo/com.myrepo.test --info
```

!!! warning "Importante"
    - Si el módulo depende de otros módulos o librerías, deben especificarse en el archivo build.gradle usando la configuración implementation.
    Antes de añadir una dependencia de un módulo de Etendo, deben haberse publicado en el repositorio.
    - Debe asegurarse de que esas dependencias también estén publicadas.
    - Añada las dependencias manualmente en el archivo `build.gradle`.
    - Añada la dependencia de Core para definir el rango de versiones con el que el módulo es compatible.

!!! info
    Para hacer uso del enfoque de resolución de dependencias, debe declarar en las dependencias del módulo de qué versión del core depende su módulo.
    Si se omite la dependencia de Etendo Core, el módulo puede instalarse en cualquier versión de Etendo, incluso si existen inconsistencias en la compilación.



Ejemplo de dependencias de módulos:

```groovy title="build.gradle"
/**
*   This file was generated automatically by the 'createModuleBuild' task.
*   Created at: 2022-12-16T15:41:21.426339Z.
*
*   WARNING: Do not put your credentials directly in this file.
*
*/

group          = "com.etendoerp"
version        = "1.0.0"
description    = "Test module to publish"
ext.artifact   = "test"
ext.repository = "https://maven.pkg.github.com/myrepo/com.myrepo.test"

configurations {
    moduleDependencyContainer
}

publishing {
    publications {
        "com.myrepo.test"(MavenPublication) {
            from components.java
            groupId    = group
            artifactId = artifact
            version    = version
        }
    }
    repositories {
        maven {
            url "https://maven.pkg.github.com/myrepo/com.myrepo.test"
        }
    }
}

repositories {
    mavenCentral()
    maven {
        url "https://maven.pkg.github.com/myrepo/com.myrepo.test"
    }
}

/**
* Declare Java dependencies using 'implementation'
* Ex: implementation "com.sun.mail:javax.mail:1.6.2"
*/
dependencies {

    implementation('com.myrepo:dependency.test:1.0.0')
    
   	implementation('com.etendoerp.platform:etendo-core:[22.1.0, x.y.z)')
}

```

#### 2.  En caso de añadir dependencias de un nuevo repositorio, declárelo en `build.gradle`

```groovy title="build.gradle"
repositories {
    mavenCentral()
    maven {
        url "https://maven.pkg.github.com/myrepo/com.myrepo.test"
    }
     maven {
        url "https://maven.pkg.github.com/myrepo2/com.myrepo2.test"
    }
}
```



#### 3. Si su módulo hace uso de inyección de dependencias, debe especificar la ubicación del archivo **'beans.xml'**

Añada en el build.gradle la ubicación del beans.xml
``` groovy
sourceSets {
    main {
        resources {
            srcDirs("etendo-resources")
        }
    }
}
```

Cree la siguiente estructura en la raíz de su módulo
```
com.test.yourmodule
	|--- etendo-resources
  			| --- META-INF
        			| --- beans.xml
```

Añada en el **beans.xml**

``` xml
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/beans_2_0.xsd" bean-discovery-mode="all" version="2.0">
</beans>
```

#### 4.  Desplegar el nuevo módulo, ejecutando los comandos :
!!! info
    Antes de publicar un módulo, se compilará y se empaquetará en formato JAR.

``` bash title="Terminal"
./gradlew update.database smartbuild
```
``` bash title="Terminal"
./gradlew publishVersion -Ppkg=<javapackage>
```


!!! success
    Una vez que Gradle finalice el despliegue, su módulo estará listo para utilizarse como una dependencia.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.