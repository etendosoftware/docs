---
tags: 
    - Cambios de API
    - Guía de actualización
    - Migrar a Etendo 25
    - Etendo 25
    - Actualizar Etendo
    - Registro de cambios para desarrolladores
    
---

# Documentación de cambios de API 

## Visión general

Este documento proporciona información detallada sobre los cambios de API y de stack introducidos en las últimas versiones de Etendo.  
Sirve como referencia para desarrolladores y administradores de sistemas para comprender qué componentes se han actualizado, quedado obsoletos o eliminado, y cómo estos cambios pueden afectar a los desarrollos personalizados.  

Si está planificando actualizar su entorno, asegúrese de revisar también la guía oficial de actualización: [Actualizar Etendo a cualquier versión](../getting-started/upgrade/upgrade-etendo-to-any-version.md).
## Marzo 2025

- [Etendo - Versión 25.1.0](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.0)
- [Etendo - Versión 25.1.1](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.1)
- [Etendo - Versión 25.1.2](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.2)

[Actualizar Etendo a cualquier versión](../getting-started/upgrade/upgrade-etendo-to-any-version.md)
### Actualización del stack de la plataforma de Etendo

#### :material-language-java: Java SE

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


    
#### :simple-postgresql: PostgreSQL

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



#### :simple-gradle: Gradle

!!! warning
    Para actualizar el wrapper de Gradle en un entorno existente, debe ejecutar:
    
    ``` bash title="Terminal"
        ./gradlew wrapper --gradle-version 8.12.1 
    ```

    Para obtener directrices de migración más detalladas, consulte [Actualización del wrapper de Gradle](https://docs.gradle.org/8.12.1/userguide/gradle_wrapper.html#sec:upgrading_wrapper){target="\_blank"}

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
    
#### :simple-apachetomcat: Apache Tomcat

- Nueva versión compatible: `9.0.98`
- Notas de la versión: [Apache Tomcat 9](https://tomcat.apache.org/tomcat-9.0-doc/changelog.html){target="\_blank"}




#### :octicons-file-code-24: Etendo Gradle Plugin

- Nueva versión compatible: `2.0.0` o superior
- Notas de la versión:

    - [Etendo Gradle Plugin - Notas de la versión](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md)
    - Nueva tarea del plugin de Gradle: 

        ``` bash title="Terminal"
        ./gradlew cleanExpandCore
        ```
        Esta nueva tarea elimina los directorios creados por la tarea `expandCore`.

    - Indicador de compatibilidad

        ``` bash title="Terminal"
        -Pjava.version=11
        ```
        Este nuevo indicador fuerza el uso de Java 11 con la versión 25Q1.

#### :octicons-issue-opened-24: Etendo ISO
       
!!!note 
    Las ISO de **Etendo 25** actualmente se basan en la imagen amd64 de Ubuntu Live Server `22.04.5`. <br>
    Para obtener más información, visite [Notas de la versión de Etendo ISO](../../../whats-new/release-notes/etendo-classic/iso.md).
### Bibliotecas de terceros 

Todas las bibliotecas que anteriormente se encontraban en `/lib/runtime` como archivos JAR se han actualizado a dependencias de Gradle, ahora definidas en el archivo `artifacts.list.COMPILATION.gradle` en la raíz del proyecto.


#### Bibliotecas actualizadas

- `dbsourcemanager.jar` -> `com.etendoerp.dbsm` versión `1.1.0`

    - Notas de la versión:

        - Cambios para usar la nueva versión de la biblioteca Apache Commons Lang 3.
        - Cambios para usar la nueva versión de la biblioteca Apache Commons Collections 4.
        - Cambios en funcionalidades obsoletas o eliminadas utilizadas en Java 17.
        - Se añadió soporte para PostgreSQL 16.
    
 - `commons-collections.commons-collections` `3.2.2` -> `4.4`

    - Notas de la versión:

        - [Commons Collections 4.0](https://commons.apache.org/proper/commons-collections/release_4_0.html){target="\_blank"}
        - [Commons Collections 4.1](https://commons.apache.org/proper/commons-collections/release_4_1.html){target="\_blank"}
        - [Commons Collections 4.2](https://commons.apache.org/proper/commons-collections/release_4_2.html){target="\_blank"}
        - [Commons Collections 4.3](https://commons.apache.org/proper/commons-collections/release_4_3.html){target="\_blank"}
        - [Commons Collections 4.4](https://commons.apache.org/proper/commons-collections/release_4_4.html){target="\_blank"}

    - Cambios en la API - Migración de Apache Commons Collections `3.2.2` a `4.4`:

        A partir de **Etendo 25.1.0**, Apache Commons Collections se ha actualizado de **3.2.2** a **4.4**. Esta versión introduce una nueva estructura de paquetes. Las clases que anteriormente se importaban desde `org.apache.commons.collections` ahora deben actualizarse a `org.apache.commons.collections4`.

    - Instrucciones de migración:

        Actualice todas las sentencias de importación y referencias para reflejar la nueva estructura de paquetes:

        ```java
        // Before (Apache Commons Collections 3.2.2)
        import org.apache.commons.collections.CollectionUtils;

        // After (Apache Commons Collections 4.4)
        import org.apache.commons.collections4.CollectionUtils;
        ```

        Además, revise su código en busca de métodos obsoletos, eliminados o modificados para garantizar la compatibilidad total con la biblioteca actualizada.

   
    !!! info 
        Para directrices de migración detalladas, consulte la documentación de [Apache Commons Collections 4.4](https://commons.apache.org/proper/commons-collections/){target="\_blank"}.

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

    - Cambios en la API - Migración de Apache Commons Lang `2.6` a `3.17`

        A partir de **Etendo 25.1.0**, Apache Commons Lang se ha actualizado de la versión **2.6** a **3.17**. Como parte de esta actualización, la estructura de paquetes ha cambiado. Las clases que anteriormente se importaban desde `org.apache.commons.lang.*` ahora deben actualizarse para usar `org.apache.commons.lang3.*`.

    - Instrucciones de migración

        Actualice sus sentencias de importación para reflejar la nueva estructura de paquetes:

        ```java
        // Before (Apache Commons Lang 2.6)
        import org.apache.commons.lang.StringUtils;

        // After (Apache Commons Lang 3.17)
        import org.apache.commons.lang3.StringUtils;
        ```

        Además, revise su código en busca de métodos obsoletos o modificados y asegure la compatibilidad con la biblioteca actualizada.

    - Notas adicionales

        La versión anterior de la biblioteca sigue disponible por compatibilidad hacia atrás, pero se eliminará en futuras versiones.

        !!! warning
            Recomendamos encarecidamente migrar todos los desarrollos personalizados a **Apache Commons Lang 3.17** para garantizar soporte y compatibilidad a largo plazo.

        !!! info
            Para directrices de migración detalladas, consulte las [Apache Commons Lang 3 migration notes](https://commons.apache.org/proper/commons-lang/article3_0.html){target="\_blank"}.

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
        
        Para versiones anteriores, puede consultar:
        - [Apache POI Release Archive (source & binaries)](https://archive.apache.org/dist/poi/release/){target="\_blank"}
        - [Resumen completo del registro de cambios](https://poi.apache.org/changes.html){target="\_blank"}

- Guía de migración de Apache POI 5.x

    Esta guía describe los cambios necesarios para migrar proyectos que usan Apache POI 3.x/4.x a la versión 5.x, incluyendo cómo reemplazar clases, métodos y constantes obsoletos eliminados en versiones recientes.

    1. Sustitución de constantes obsoletas (`CellType`)
        
        En POI 5.x, las constantes `Cell.CELL_TYPE_*` se sustituyen por el enum `CellType`.

        Ejemplo:

        ```java
        // Before
        cell.getCellType() == Cell.CELL_TYPE_STRING;

        // After
        cell.getCellType() == CellType.STRING;
        ```

        Correspondencias clave:

        | Constante antigua         | Constante nueva    |
        |---------------------------|--------------------|
        | `Cell.CELL_TYPE_STRING`   | `CellType.STRING`  |
        | `Cell.CELL_TYPE_NUMERIC`  | `CellType.NUMERIC` |
        | `Cell.CELL_TYPE_BOOLEAN`  | `CellType.BOOLEAN` |
        | `Cell.CELL_TYPE_FORMULA`  | `CellType.FORMULA` |
        | `Cell.CELL_TYPE_BLANK`    | `CellType.BLANK`   |

        Importación requerida:

        ```java
        import org.apache.poi.ss.usermodel.CellType;
        ```

    2. Actualización de estilos de celda

        Alineación

        | Constante antigua         | Constante nueva             |
        |--------------------------|-----------------------------|
        | `CellStyle.ALIGN_LEFT`   | `HorizontalAlignment.LEFT`  |
        | `CellStyle.ALIGN_CENTER` | `HorizontalAlignment.CENTER`|
        | `CellStyle.ALIGN_RIGHT`  | `HorizontalAlignment.RIGHT` |
        
               
                - CellStyle.ALIGN_CENTER → 
                -  → 

        ```java
        // Before
        style.setAlignment(CellStyle.ALIGN_CENTER);

        // After
        style.setAlignment(HorizontalAlignment.CENTER);
        ```

        ```java
        import org.apache.poi.ss.usermodel.HorizontalAlignment;
        ```

        Patrones de relleno

        ```java
        // Before
        style.setFillPattern(CellStyle.SOLID_FOREGROUND);

        // After
        style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        ```

        ```java
        import org.apache.poi.ss.usermodel.FillPatternType;
        ```

        Bordes

        ```java
        // Before
        setBorderBottom((short) 1);

        // After
        setBorderBottom(BorderStyle.THIN);
        ```

        ```java
        import org.apache.poi.ss.usermodel.BorderStyle;
        ```

    3. Cambios en la API de fuentes

        El método `Font.setBoldweight()` está obsoleto.  
        Ahora debe usar `Font.setBold(boolean)`.

        Ejemplo:

        ```java
        // Before
        font.setBoldweight(Font.BOLDWEIGHT_BOLD);

        // After
        font.setBold(true);
        ```

        ```java
        // Before
        font.setBoldweight(Font.BOLDWEIGHT_NORMAL);

        // After
        font.setBold(false);
        ```

    4. Cambios en la API de evaluación de fórmulas:

        ```java
        // Before
        switch (cellValue.getCellType()) {
            case Cell.CELL_TYPE_NUMERIC:
        }

        // After
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
            // other cases...
        }
        ```

    5. Buenas prácticas adicionales

        Evite crear `XSSFWorkbook()` nuevos innecesariamente. En su lugar, reutilice:

        ```java
        Workbook workbook = cell.getSheet().getWorkbook();
        ```

        Use la API moderna de Map:

        ```java
        // Instead of containsKey + put
        map.computeIfAbsent(key, k -> new ArrayList<>());
        ```

    6. Ejemplo completo de migración

        ```java
        // Before
        cellFont.setBoldweight(HSSFFont.BOLDWEIGHT_BOLD);
        style.setAlignment(CellStyle.ALIGN_RIGHT);
        style.setFillPattern(CellStyle.SOLID_FOREGROUND);

        // After
        cellFont.setBold(true);
        style.setAlignment(HorizontalAlignment.RIGHT);
        style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        ```

    7. **Pruebe cuidadosamente su código migrado**. Pueden existir algunos cambios sutiles de comportamiento en la evaluación de fórmulas y el estilo.
    
    
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
    Consulte las notas de la versión de cada biblioteca para obtener información más detallada sobre los cambios y cómo podrían afectar a su sistema.

#### Bibliotecas nuevas

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

#### Bibliotecas eliminadas

- `itext-pdfa-5.5.0.jar`
- `itextpdf-5.5.0.jar`
- `jcommon-1.0.15.jar`
- `jxl-2.6.10.jar`



---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.