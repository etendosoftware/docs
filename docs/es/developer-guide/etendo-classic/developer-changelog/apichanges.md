---
tags:
    - API Changes
    - Etendo 26
    - Etendo 25
    - Migrate to Etendo 25
    - Update Etendo
    - Updating Guide
    - Developer Changelog
---

# Documentación de cambios de API

## Resumen

Este documento proporciona información detallada sobre los cambios de API y de stack introducidos en las últimas versiones de Etendo.
Sirve como referencia para desarrolladores y administradores de sistemas para entender qué componentes se han actualizado, quedado obsoletos o eliminado, y cómo estos cambios pueden afectar a los desarrollos personalizados.

Si estás planificando actualizar tu entorno, asegúrate de revisar también la guía oficial de actualización: [Actualizar Etendo a cualquier versión](../getting-started/upgrade/upgrade-etendo-to-any-version.md).

## Etendo 26

- [Etendo - Release 26.1.0](https://github.com/etendosoftware/etendo_core/releases/tag/26.1.0){target="\_blank"}

[Actualizar Etendo a cualquier versión](../getting-started/upgrade/upgrade-etendo-to-any-version.md)

### Actualización de la pila de plataforma

**:material-language-java: Java SE**

- Versión mínima requerida: `17.0.14` — [Notas de la versión](https://www.oracle.com/java/technologies/javase/17all-relnotes.html){target="\_blank"}

    !!! danger "Cambio incompatible: Java 17 es ahora obligatorio"
    
        A partir de **Etendo 26.1.0**, Java 17 es la **única versión compatible** de Java. El indicador de compatibilidad `-Pjava.version=11` introducido en Etendo 25 ha sido **completamente eliminado**.

        Cualquier entorno que siga ejecutando Java 11 quedará **bloqueado al compilar**. Debes instalar y configurar **Java 17 o superior** antes de actualizar a Etendo 26.

    !!! warning "Acción requerida para desarrollos personalizados"
        Si tienes módulos personalizados con clases `BuildValidation` o `ModuleScript`, recompílalos con Java 17 antes de actualizar. Estas clases se ejecutan durante `update.database` y fallan en tiempo de ejecución si se compilan con Java 11 debido a incompatibilidades de bytecode.

        ```bash title="Terminal"
        ./gradlew compile.modulescript -Dmodule=<javapackage>
        ./gradlew compile.buildvalidation -Dmodule=<javapackage>
        ```

        Esto solo aplica a módulos **personalizados**. Los módulos núcleo de Etendo ya están compilados con Java 17.

---

**:simple-postgresql: PostgreSQL**

- Nueva versión compatible: `17`
- Controlador JDBC: `42.5.4` -> `42.7.8` — [Registro de cambios](https://jdbc.postgresql.org/changelogs/){target="\_blank"}

PostgreSQL 17 es compatible a partir de esta versión. No es necesaria ninguna acción si te mantienes en una versión actualmente compatible. Si actualizas el motor de base de datos, revisa las [notas de la versión de PostgreSQL 17](https://www.postgresql.org/docs/release/17.0/){target="\_blank"} para ver los cambios incompatibles.

---

**:octicons-file-code-24: Etendo Gradle Plugin**

- Nueva versión requerida: `2.3.0` o superior — [Notas de la versión](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md)
- El indicador `-Pjava.version=11` ha sido eliminado. Java 17 ahora se aplica sin posibilidad de omisión.

---

**:octicons-file-code-24: DBSourceManager**

- Nueva versión: `1.1.0` -> `1.2.0`
- Cambios:
    - El wrapper de Gradle se ha actualizado de `7.3.2` a `8.12.1`.
    - Se ha añadido compatibilidad con la plataforma PostgreSQL 16 (`PostgreSql16Platform`).
    - Nuevo sistema `ExcludedConstraint` para gestionar tablas particionadas y esquemas de base de datos complejos.
    - Mejora en el manejo de tablas particionadas durante la exportación de la base de datos.
    - Se han eliminado todos los JAR incluidos en `lib/`; ahora las dependencias se resuelven desde el classpath del proyecto.

### Bibliotecas de terceros

**Actualizado**

- `org.postgresql:postgresql` `42.5.4` -> `42.7.8` — actualización compatible. Revisa el [registro de cambios](https://jdbc.postgresql.org/changelogs/){target="\_blank"} si utilizas funciones específicas del controlador.

- `org.mozilla:rhino` `1.7.13` -> `1.8.0`
- `org.mozilla:rhino-engine` `1.7.13` -> `1.8.0` — [Versiones de Rhino](https://github.com/mozilla/rhino/releases){target="\_blank"}

    !!! warning
        Si tienes JavaScript personalizado ejecutado a través del motor Rhino, pruébalo para comprobar su compatibilidad con la versión 1.8.0. Esta actualización incluye cambios en la compatibilidad con ECMAScript y en las API internas.

- `org.antlr:antlr` `2.7.7` -> `org.antlr:antlr-complete` `3.5.3` — [Documentación de ANTLR 3](https://www.antlr3.org/){target="\_blank"}

    !!! warning
        Esta es una **actualización de versión mayor** (ANTLR 2 a ANTLR 3). Si utilizas las API de ANTLR directamente en código personalizado, debes migrar. La estructura de paquetes y la API han cambiado significativamente.

- `org.codehaus.woodstox:wstx-asl` `3.0.2` -> `4.0.6` — [Versiones de Woodstox](https://github.com/FasterXML/woodstox/releases){target="\_blank"} — actualización de versión mayor para la biblioteca de procesamiento de flujos XML. Revísalo si utilizas las API de Woodstox directamente.

- `com.etendoerp:dbsm` `1.1.0` -> `1.2.0` — ver arriba [DBSourceManager (DBSM)](#dbsourcemanager-dbsm).

---

**Coordenadas de artefactos migradas al upstream**

Varias bibliotecas anteriormente reempaquetadas bajo `com.etendoerp` ahora se resuelven desde sus coordenadas oficiales de Maven Central upstream. Si tus módulos declaran alguna de estas como dependencias explícitas, actualiza las coordenadas del artefacto. Sin cambios funcionales.

| Anterior | Nuevo | Versión |
|---|---|---|
| `com.etendoerp:yuiant` `1.0` | `com.etendoerp:YUIAnt` `1.0.0` | Cambio de mayúsculas/minúsculas en el ID del artefacto |
| `com.etendoerp:jettison` `1.3` | `org.codehaus.jettison:jettison` `1.3` | Misma versión |
| `com.etendoerp:wstx-asl` `3.0.2` | `org.codehaus.woodstox:wstx-asl` `4.0.6` | Versión actualizada |
| `com.etendoerp:slf4j-api` `1.7.25` | `org.slf4j:slf4j-api` `1.7.25` | Misma versión |
| `com.etendoerp:antlr` `2.7.7` | `org.antlr:antlr-complete` `3.5.3` | Versión actualizada |
| `com.etendoerp:rhino-engine` `1.7.13` | `org.mozilla:rhino-engine` `1.8.0` | Versión actualizada |

---

**Nuevas**

Las siguientes bibliotecas son nuevas incorporaciones al classpath de la plataforma. No es necesaria ninguna acción salvo que tus módulos personalizados declaren versiones en conflicto.

- `org.apache.poi:ooxml-schemas` `1.4` — [Documentación](https://poi.apache.org/components/oxml4j/){target="\_blank"}
- `org.hamcrest:hamcrest-all` `1.3` — [Documentación](http://hamcrest.org/JavaHamcrest/){target="\_blank"}
- `junit:junit` `4.12` — [Documentación](https://junit.org/junit4/){target="\_blank"}

---

**Eliminadas**

- `org.apache.commons:commons-compress` `1.27.1`

    !!! warning
        Si tus módulos personalizados dependen de `commons-compress`, añádelo como dependencia explícita en el `build.gradle` de tu módulo.

- `org.eclipse.jdt:ecj` `3.23.0` (Eclipse Compiler for Java)
- `com.etendoerp:ant-nodeps` `1.0.0`
- `com.etendoerp:catalina-ant` `1.0.0`
- `org.apache.poi:ooxml-schemas` `1.4`   

### Cambios en el esquema de base de datos

Los siguientes cambios se aplican automáticamente durante `update.database`:

| Tabla | Cambio | Detalles |
|---|---|---|
| `AD_HEARTBEAT_LOG` | Columnas eliminadas | `ACTIVITY_RATE`, `COMPLEXITY_RATE`, `ANT_VERSION` |
| `AD_HEARTBEAT_LOG` | Columna añadida | `STATUS` |
| `AD_SYSTEM_INFO` | Columnas añadidas | `License_Edition`, `Subscription_Type`, `Subscription_Start_Date`, `Subscription_End_Date`, `Concurrent_Global_System_Users`, `Instance_Number`, `WEB_Service_Access`, `Customer_Name` |

### Otros cambios

- **Generación de claves de Secure Web Services**: el objetivo de Ant `generate.sws.keys` ahora se ejecuta automáticamente durante `install.source`, reduciendo los pasos de configuración manual para los servicios web seguros.

---
## Etendo 25

- [Etendo - Versión 25.1.0](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.0)
- [Etendo - Versión 25.1.1](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.1)
- [Etendo - Versión 25.1.2](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.2)

[Actualizar Etendo a cualquier versión](../getting-started/upgrade/upgrade-etendo-to-any-version.md)

### Actualización de la pila de plataforma

**:material-language-java: Java SE**

- Nueva versión compatible: `17.0.14`
- Notas de la versión:
    
    <div class="grid cards" markdown>

    - Java SE 12.x

        - [Java SE 12.0.2](https://www.oracle.com/java/technologies/javase/12-0-2-relnotes.html){target="\_blank"}
        - [Todas las actualizaciones de Java 12](https://www.oracle.com/java/technologies/javase/12all-relnotes.html){target="\_blank"}

    - Java SE 13.x

        - [Java SE 13.0.2](https://www.oracle.com/java/technologies/javase/13-0-2-relnotes.html){target="\_blank"}
        - [Todas las actualizaciones de Java 13](https://www.oracle.com/java/technologies/javase/13all-relnotes.html){target="\_blank"}

    - Java SE 14.x

        - [Java SE 14.0.2](https://www.oracle.com/java/technologies/javase/14-0-2-relnotes.html){target="\_blank"}
        - [Todas las actualizaciones de Java 14](https://www.oracle.com/java/technologies/javase/14all-relnotes.html){target="\_blank"}

    - Java SE 15.x

        - [Java SE 15.0.2](https://www.oracle.com/java/technologies/javase/15-0-2-relnotes.html){target="\_blank"}
        - [Todas las actualizaciones de Java 15](https://www.oracle.com/java/technologies/javase/15all-relnotes.html){target="\_blank"}

    - Java SE 16.x

        - [Java SE 16.0.2](https://www.oracle.com/java/technologies/javase/16-0-2-relnotes.html){target="\_blank"}
        - [Todas las actualizaciones de Java 16](https://www.oracle.com/java/technologies/javase/16all-relnotes.html){target="\_blank"}

    - Java SE 17 (LTS)

        - [Java SE 17.0.14(Oracle)](https://www.oracle.com/java/technologies/javase/17-0-14-relnotes.html){target="\_blank"}
        - [Todas las actualizaciones de Java 17](https://www.oracle.com/java/technologies/javase/17all-relnotes.html){target="\_blank"}

    </div>

---

**:simple-postgresql: PostgreSQL**

- Nueva versión compatible: `16.8.1`
- Notas de la versión:

    <div class="grid cards" markdown>

    - PostgreSQL 16.x
        - [PostgreSQL 16.8](https://www.postgresql.org/docs/release/16.8/){target="\_blank"}
        - [PostgreSQL 16.7](https://www.postgresql.org/docs/release/16.7/){target="\_blank"}
        - [PostgreSQL 16.6](https://www.postgresql.org/docs/release/16.6/){target="\_blank"}
        - [PostgreSQL 16.5](https://www.postgresql.org/docs/release/16.5/){target="\_blank"}
        - [PostgreSQL 16.4](https://www.postgresql.org/docs/release/16.4/){target="\_blank"}
        - [PostgreSQL 16.3](https://www.postgresql.org/docs/release/16.3/){target="\_blank"}
        - [PostgreSQL 16.2](https://www.postgresql.org/docs/release/16.2/){target="\_blank"}
        - [PostgreSQL 16.1](https://www.postgresql.org/docs/release/16.1/){target="\_blank"}
        - [PostgreSQL 16.0](https://www.postgresql.org/docs/release/16.0/){target="\_blank"}

    - PostgreSQL 15.x
        - [PostgreSQL 15.10](https://www.postgresql.org/docs/release/15.10/){target="\_blank"}
        - [PostgreSQL 15.9](https://www.postgresql.org/docs/release/15.9/){target="\_blank"}
        - [PostgreSQL 15.8](https://www.postgresql.org/docs/release/15.8/){target="\_blank"}
        - [PostgreSQL 15.7](https://www.postgresql.org/docs/release/15.7/){target="\_blank"}
        - [PostgreSQL 15.6](https://www.postgresql.org/docs/release/15.6/){target="\_blank"}
        - [PostgreSQL 15.5](https://www.postgresql.org/docs/release/15.5/){target="\_blank"}
        - [PostgreSQL 15.4](https://www.postgresql.org/docs/release/15.4/){target="\_blank"}
        - [PostgreSQL 15.3](https://www.postgresql.org/docs/release/15.3/){target="\_blank"}
        - [PostgreSQL 15.2](https://www.postgresql.org/docs/release/15.2/){target="\_blank"}
        - [PostgreSQL 15.1](https://www.postgresql.org/docs/release/15.1/){target="\_blank"}
        - [PostgreSQL 15.0](https://www.postgresql.org/docs/release/15.0/){target="\_blank"}

        </div>

---

**:simple-gradle: Gradle**

!!! warning
    Para actualizar el wrapper de Gradle en un entorno existente, debes ejecutar:
    
    ``` bash title="Terminal"
        ./gradlew wrapper --gradle-version 8.12.1 
    ```

    Para obtener directrices de migración más detalladas, consulta [Actualización del wrapper de Gradle](https://docs.gradle.org/8.12.1/userguide/gradle_wrapper.html#sec:upgrading_wrapper){target="\_blank"}

- Nueva versión compatible: `8.12.1`
- Notas de la versión:

    <div class="grid cards" markdown>
    
    - Gradle 8.x
        - [Gradle 8.12.1](https://docs.gradle.org/8.12.1/release-notes.html){target="\_blank"}
        - [Gradle 8.12](https://docs.gradle.org/8.12/release-notes.html){target="\_blank"}
        - [Gradle 8.11](https://docs.gradle.org/8.11/release-notes.html){target="\_blank"}
        - [Gradle 8.10](https://docs.gradle.org/8.10/release-notes.html){target="\_blank"}
        - [Gradle 8.9](https://docs.gradle.org/8.9/release-notes.html){target="\_blank"}
        - [Gradle 8.8](https://docs.gradle.org/8.8/release-notes.html){target="\_blank"}
        - [Gradle 8.7](https://docs.gradle.org/8.7/release-notes.html){target="\_blank"}
        - [Gradle 8.6](https://docs.gradle.org/8.6/release-notes.html){target="\_blank"}
        - [Gradle 8.5](https://docs.gradle.org/8.5/release-notes.html){target="\_blank"}
        - [Gradle 8.4](https://docs.gradle.org/8.4/release-notes.html){target="\_blank"}
        - [Gradle 8.3](https://docs.gradle.org/8.3/release-notes.html){target="\_blank"}
        - [Gradle 8.2](https://docs.gradle.org/8.2/release-notes.html){target="\_blank"}
        - [Gradle 8.1](https://docs.gradle.org/8.1/release-notes.html){target="\_blank"}
        - [Gradle 8.0](https://docs.gradle.org/8.0/release-notes.html){target="\_blank"}

    - Gradle 7.x
        - [Gradle 7.6](https://docs.gradle.org/7.6/release-notes.html){target="\_blank"}
        - [Gradle 7.5.1](https://docs.gradle.org/7.5.1/release-notes.html){target="\_blank"}
        - [Gradle 7.5](https://docs.gradle.org/7.5/release-notes.html){target="\_blank"}
        - [Gradle 7.4.2](https://docs.gradle.org/7.4.2/release-notes.html){target="\_blank"}
        - [Gradle 7.4.1](https://docs.gradle.org/7.4.1/release-notes.html){target="\_blank"}
        - [Gradle 7.4](https://docs.gradle.org/7.4/release-notes.html){target="\_blank"}
        - [Gradle 7.3.3](https://docs.gradle.org/7.3.3/release-notes.html){target="\_blank"}

        </div>

---

**:simple-apachetomcat: Apache Tomcat**

- Nueva versión compatible: `9.0.98`
- Notas de la versión: [Apache Tomcat 9](https://tomcat.apache.org/tomcat-9.0-doc/changelog.html){target="\_blank"}

---

**:octicons-file-code-24: Etendo Gradle Plugin**

- Nueva versión compatible: `2.0.0` o superior
- Notas de la versión:

    - [Notas de la versión de Etendo Gradle Plugin](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md)
    - Nueva tarea del plugin de Gradle: 

        ``` bash title="Terminal"
        ./gradlew cleanExpandCore
        ```
        Esta nueva tarea elimina los directorios creados por la tarea `expandCore`.

    - Marca de compatibilidad

        ``` bash title="Terminal"
        -Pjava.version=11
        ```
        Esta nueva marca fuerza el uso de Java 11 con la versión 25Q1.

---

**:octicons-issue-opened-24: Etendo ISO**
       
!!!note 
    Las ISO de **Etendo 25** se basan actualmente en la imagen amd64 de Ubuntu Live Server `22.04.5`. <br>
    Para más información, visita [Notas de la versión de Etendo ISO](../../../whats-new/release-notes/etendo-classic/iso.md).



### Bibliotecas de terceros

Todas las bibliotecas ubicadas anteriormente en `/lib/runtime` como archivos JAR se han actualizado a dependencias de Gradle, ahora definidas en el archivo `artifacts.list.COMPILATION.gradle` en la raíz del proyecto.

**Actualizado**

- `dbsourcemanager.jar` -> `com.etendoerp.dbsm` versión `1.1.0`

    - Notas de la versión:

        - Cambios para usar la nueva versión de la biblioteca Apache Commons Lang 3.
        - Cambios para usar la nueva versión de la biblioteca Apache Commons Collections 4.
        - Cambios en características obsoletas o eliminadas usadas en Java 17.
        - Se añadió compatibilidad con PostgreSQL 16.
    
 - `commons-collections.commons-collections` `3.2.2` -> `4.4`

    - Notas de la versión:

        - [Commons Collections 4.0](https://commons.apache.org/proper/commons-collections/release_4_0.html){target="\_blank"}
        - [Commons Collections 4.1](https://commons.apache.org/proper/commons-collections/release_4_1.html){target="\_blank"}
        - [Commons Collections 4.2](https://commons.apache.org/proper/commons-collections/release_4_2.html){target="\_blank"}
        - [Commons Collections 4.3](https://commons.apache.org/proper/commons-collections/release_4_3.html){target="\_blank"}
        - [Commons Collections 4.4](https://commons.apache.org/proper/commons-collections/release_4_4.html){target="\_blank"}

    - Cambios de API - Migración de Apache Commons Collections `3.2.2` a `4.4`:

        A partir de **Etendo 25.1.0**, Apache Commons Collections se ha actualizado de **3.2.2** a **4.4**. Esta versión introduce una nueva estructura de paquetes. Las clases importadas anteriormente desde `org.apache.commons.collections` ahora deben actualizarse a `org.apache.commons.collections4`.

    - Instrucciones de migración:

        Actualiza todas las sentencias de importación y referencias para reflejar la nueva estructura de paquetes:

        ```java
        // Antes (Apache Commons Collections 3.2.2)
        import org.apache.commons.collections.CollectionUtils;

        // Después (Apache Commons Collections 4.4)
        import org.apache.commons.collections4.CollectionUtils;
        ```

        Además, revisa tu código en busca de métodos obsoletos, eliminados o modificados para garantizar la compatibilidad total con la biblioteca actualizada.

   
    !!! info 
        Para obtener directrices de migración detalladas, consulta la documentación de [Apache Commons Collections 4.4](https://commons.apache.org/proper/commons-collections/){target="\_blank"}.

- `org.apache.commons:commons-lang3` `2.6` -> `3.17.0`
    - Notas de la versión:
        - [Commons Lang 3.0](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.0){target="\_blank"}
        - [Commons Lang 3.1](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.1){target="\_blank"}
        - [Commons Lang 3.2](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.2){target="\_blank"}
        - [Commons Lang 3.3](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.3){target="\_blank"}
        - [Commons Lang 3.4](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.4){target="\_blank"}
        - [Commons Lang 3.5](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.5){target="\_blank"}
        - [Commons Lang 3.6](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.6){target="\_blank"}
        - [Commons Lang 3.7](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.7){target="\_blank"}
        - [Commons Lang 3.8](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.8){target="\_blank"}
        - [Commons Lang 3.8.1](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.8.1){target="\_blank"}
        - [Commons Lang 3.9](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.9){target="\_blank"}
        - [Commons Lang 3.10](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.10){target="\_blank"}
        - [Commons Lang 3.11](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.11){target="\_blank"}
        - [Commons Lang 3.12.0](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.12.0){target="\_blank"}
        - [Commons Lang 3.13.0](https://commons.apache.org/proper/commons-lang/changes-report.html#a3.13.0){target="\_blank"}

    - Cambios de API - Migración de Apache Commons Lang `2.6` a `3.17`

        A partir de **Etendo 25.1.0**, Apache Commons Lang se ha actualizado de la versión **2.6** a **3.17**. Como parte de esta actualización, la estructura de paquetes ha cambiado. Las clases importadas anteriormente desde `org.apache.commons.lang.*` ahora deben actualizarse para usar `org.apache.commons.lang3.*`.

    - Instrucciones de migración

        Actualiza tus sentencias de importación para reflejar la nueva estructura de paquetes:

        ```java
        // Antes (Apache Commons Lang 2.6)
        import org.apache.commons.lang.StringUtils;

        // Después (Apache Commons Lang 3.17)
        import org.apache.commons.lang3.StringUtils;
        ```

        Además, revisa tu código en busca de métodos obsoletos o modificados y asegúrate de que sea compatible con la biblioteca actualizada.

    - Notas adicionales

        La versión anterior de la biblioteca sigue disponible por compatibilidad hacia atrás, pero se eliminará en futuras versiones.

        !!! warning
            Recomendamos encarecidamente migrar todos los desarrollos personalizados a **Apache Commons Lang 3.17** para garantizar soporte y compatibilidad a largo plazo.

        !!! info
            Para obtener directrices de migración detalladas, consulta las [notas de migración de Apache Commons Lang 3](https://commons.apache.org/proper/commons-lang/article3_0.html){target="\_blank"}.

- `org.hibernate.common.hibernate-commons-annotations` `5.1.0.Final` -> `5.1.2.Final`
    - Notas de la versión:
        - [5.1.1.Final](https://in.relation.to/2016/08/12/hibernate-orm-511-final-release/){target="\_blank"}
        - [5.1.2.Final](https://in.relation.to/2016/09/19/hibernate-orm-5011-final-and-512-final-release/){target="\_blank"}

- `org.hibernate:hibernate-core` `5.4.2.Final` -> `5.6.15.Final`
    - Notas de la versión:
        - [5.4.x](https://github.com/hibernate/hibernate-orm/blob/5.4/changelog.txt){target="\_blank"}
        - [5.5.x](https://github.com/hibernate/hibernate-orm/blob/5.5/changelog.txt){target="\_blank"}

- `net.sf.jasperreports.jasperreports-fonts` `6.0.0` -> `6.17.0`
- `net.sf.jasperreports.jasperreports` `6.0.0` -> `6.17.0`
    - Notas de la versión:
        - [Página de versiones – GitHub](https://github.com/Jaspersoft/jasperreports/releases){target="\_blank"}

- `org.apache.poi.poi` `3.10.1` -> `5.4.0`
    - Notas de la versión:
        - [Apache POI 5.4.0 (2025-01-08)](https://poi.apache.org/changes.html#version-5.4.0-2025-01-08){target="\_blank"}
        - [Apache POI 5.3.0 (2024-07-02)](https://poi.apache.org/changes.html#version-5.3.0-2024-07-02){target="\_blank"}
        - [Apache POI 5.2.5 (2023-11-25)](https://poi.apache.org/changes.html#version-5.2.5-2023-11-25){target="\_blank"}
        - [Apache POI 5.2.4 (2023-09-28)](https://poi.apache.org/changes.html#version-5.2.4-2023-09-28){target="\_blank"}
        - [Apache POI 5.2.3 (2023-05-22)](https://poi.apache.org/changes.html#version-5.2.3-2023-05-22){target="\_blank"}
        - [Apache POI 5.2.2 (2023-01-19)](https://poi.apache.org/changes.html#version-5.2.2-2023-01-19){target="\_blank"}
        - [Apache POI 5.2.1 (2022-09-09)](https://poi.apache.org/changes.html#version-5.2.1-2022-09-09){target="\_blank"}
        - [Apache POI 5.2.0 (2022-01-14)](https://poi.apache.org/changes.html#version-5.2.0-2022-01-14){target="\_blank"}
        - [Apache POI 5.1.0 (2021-08-07)](https://poi.apache.org/changes.html#version-5.1.0-2021-08-07){target="\_blank"}
        - [Apache POI 5.0.0 (2021-02-08)](https://poi.apache.org/changes.html#version-5.0.0-2021-02-08){target="\_blank"}
        - [Apache POI 4.1.2 (2019-12-16)](https://poi.apache.org/changes.html#version-4.1.2-2019-12-16){target="\_blank"}
        - [Apache POI 4.1.1 (2019-07-20)](https://poi.apache.org/changes.html#version-4.1.1-2019-07-20){target="\_blank"}
        - [Apache POI 4.1.0 (2019-04-22)](https://poi.apache.org/changes.html#version-4.1.0-2019-04-22){target="\_blank"}
        - [Apache POI 4.0.1 (2018-11-24)](https://poi.apache.org/changes.html#version-4.0.1-2018-11-24){target="\_blank"}
        - [Apache POI 4.0.0 (2018-09-07)](https://poi.apache.org/changes.html#version-4.0.0-2018-09-07){target="\_blank"}
        
        Para versiones anteriores, puedes consultar:
        - [Archivo de versiones de Apache POI (código fuente y binarios)](https://archive.apache.org/dist/poi/release/){target="\_blank"}
        - [Resumen completo del historial de cambios](https://poi.apache.org/changes.html){target="\_blank"}

- Guía de migración de Apache POI 5.x

    Esta guía describe los cambios necesarios para migrar proyectos que usan Apache POI 3.x/4.x a la versión 5.x, incluida la sustitución de clases, métodos y constantes obsoletos eliminados en versiones recientes.

    1. Sustitución de constantes obsoletas (`CellType`)
        
        En POI 5.x, las constantes `Cell.CELL_TYPE_*` se sustituyen por la enumeración `CellType`.

        Ejemplo:

        ```java
        // Antes
        cell.getCellType() == Cell.CELL_TYPE_STRING;

        // Después
        cell.getCellType() == CellType.STRING;
        ```

        Correspondencias clave:

        | Constante antigua         | Nueva constante       |
        |---------------------------|-----------------------|
        | `Cell.CELL_TYPE_STRING`   | `CellType.STRING`     |
        | `Cell.CELL_TYPE_NUMERIC`  | `CellType.NUMERIC`    |
        | `Cell.CELL_TYPE_BOOLEAN`  | `CellType.BOOLEAN`    |
        | `Cell.CELL_TYPE_FORMULA`  | `CellType.FORMULA`    |
        | `Cell.CELL_TYPE_BLANK`    | `CellType.BLANK`      |

        Importación requerida:

        ```java
        import org.apache.poi.ss.usermodel.CellType;
        ```

    2. Actualización de estilos de celda

        Alineación

        | Constante antigua          | Nueva constante                 |
        |---------------------------|----------------------------------|
        | `CellStyle.ALIGN_LEFT`    | `HorizontalAlignment.LEFT`       |
        | `CellStyle.ALIGN_CENTER`  | `HorizontalAlignment.CENTER`     |
        | `CellStyle.ALIGN_RIGHT`   | `HorizontalAlignment.RIGHT`      |

        ```java
        // Antes
        style.setAlignment(CellStyle.ALIGN_CENTER);

        // Después
        style.setAlignment(HorizontalAlignment.CENTER);
        ```

        ```java
        import org.apache.poi.ss.usermodel.HorizontalAlignment;
        ```

        Patrones de relleno

        ```java
        // Antes
        style.setFillPattern(CellStyle.SOLID_FOREGROUND);

        // Después
        style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        ```

        ```java
        import org.apache.poi.ss.usermodel.FillPatternType;
        ```

        Bordes

        ```java
        // Antes
        setBorderBottom((short) 1);

        // Después
        setBorderBottom(BorderStyle.THIN);
        ```

        ```java
        import org.apache.poi.ss.usermodel.BorderStyle;
        ```

    3. Cambios en la API de fuentes

        El método `Font.setBoldweight()` está obsoleto.  
        Ahora debes usar `Font.setBold(boolean)`.

        Ejemplo:

        ```java
        // Antes
        font.setBoldweight(Font.BOLDWEIGHT_BOLD);

        // Después
        font.setBold(true);
        ```

        ```java
        // Antes
        font.setBoldweight(Font.BOLDWEIGHT_NORMAL);

        // Después
        font.setBold(false);
        ```

    4. Cambios en la API de evaluación de fórmulas:

        ```java
        // Antes
        switch (cellValue.getCellType()) {
            case Cell.CELL_TYPE_NUMERIC:
        }

        // Después
        switch (cellValue.getCellType()) {
            case NUMERIC:
        }
        ```

        Evaluación de fórmulas:

        ```java
        FormulaEvaluator evaluator = workbook.getCreationHelper().createFormulaEvaluator();
        CellValue cellValue = evaluator.evaluate(cell);
        ```

        Ejemplo completo:

        ```java
        CellValue cellValue = evaluator.evaluate(cell);
        switch (cellValue.getCellType()) {
            case STRING:
                return cellValue.getStringValue();
            // otros casos...
        }
        ```

    5. Buenas prácticas adicionales

        Evita crear `XSSFWorkbook()` innecesariamente. En su lugar, reutiliza:

        ```java
        Workbook workbook = cell.getSheet().getWorkbook();
        ```

        Usa la API moderna de Map:

        ```java
        // En lugar de containsKey + put
        map.computeIfAbsent(key, k -> new ArrayList<>());
        ```

    6. Ejemplo completo de migración

        ```java
        // Antes
        cellFont.setBoldweight(HSSFFont.BOLDWEIGHT_BOLD);
        style.setAlignment(CellStyle.ALIGN_RIGHT);
        style.setFillPattern(CellStyle.SOLID_FOREGROUND);

        // Después
        cellFont.setBold(true);
        style.setAlignment(HorizontalAlignment.RIGHT);
        style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        ```

    7. **Prueba cuidadosamente el código migrado**. Pueden existir cambios sutiles de comportamiento en la evaluación de fórmulas y el estilo.
    
    
    !!! info "Recursos oficiales"
        - [Documentación de Apache POI](https://poi.apache.org/components/spreadsheet/){target="\_blank"}
        - [Guía de migración desde versiones anteriores](https://poi.apache.org/migration.html){target="\_blank"}
    

- `commons-beanutils.commons-beanutils` `1.8.3` -> `1.9.4` 
- `commons-codec.commons-codec` `1.1.1` -> `1.17.1`
- `commons-digester.commons-digester` `1.8.1` -> `2.1`
- `commons-fileupload.commons-fileupload` `1.4` -> `1.5`
- `commons-io.commons-io` `2.4` -> `2.16.1`
- `com.sun.istack.istack-commons-runtime` `3.0.7` -> `4.2.0`    

!!! info
    Consulta las notas de la versión de cada biblioteca para obtener información más detallada sobre los cambios y cómo pueden afectar a tu sistema.

---

**Nuevo**

- `org.apache.commons.commons-text` `1.10.0`
    - [Documentación](https://commons.apache.org/proper/commons-text/){target="\_blank"}

- `org.apache.commons.commons-math3` `3.6.1`
    - [Documentación](https://commons.apache.org/proper/commons-math/){target="\_blank"}

- `org.codehaus.castor.castor-core` `1.4.1`
    - [Documentación](https://castor-data-binding.github.io/castor/){target="\_blank"}

- `org.codehaus.castor:castor-xml` `1.4.1`
    - [Documentación](https://castor-data-binding.github.io/castor/){target="\_blank"}

- `com.lowagie:itext` `2.1.7`
    - [Documentación](https://itextpdf.com/resources){target="\_blank"}

---

**Eliminado**

- `itext-pdfa-5.5.0.jar`
- `itextpdf-5.5.0.jar`
- `jcommon-1.0.15.jar`
- `jxl-2.6.10.jar`



---
Este trabajo está bajo licencia :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.