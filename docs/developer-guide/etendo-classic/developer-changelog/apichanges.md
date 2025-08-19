---
tags: 
    - API Changes
    - Updating Guide
    
---

# API Change Documentation 

## Overview

This document provides detailed information about API and stack changes introduced in the latest Etendo releases.  
It serves as a reference for developers and system administrators to understand which components have been updated, deprecated, or removed, and how these changes may impact custom developments.  

If you are planning to upgrade your environment, make sure to also review the official upgrade guide: [Upgrade Etendo to Any Version](../getting-started/upgrade/upgrade-etendo-to-any-version.md).

## March 2025

- [Etendo - Release 25.1.0](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.0)
- [Etendo - Release 25.1.1](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.1)
- [Etendo - Release 25.1.2](https://github.com/etendosoftware/etendo_core/releases/tag/25.1.2)

[Upgrade Etendo to Any Version](../getting-started/upgrade/upgrade-etendo-to-any-version.md)

### Etendo Platform Stack Upgrade

#### :material-language-java: Java SE

- New Version Supported: `17.0.14`
- Release Notes:
    
    <div class="grid cards" markdown>

    - Java SE 12.x

        - [Java SE 12.0.2](https://www.oracle.com/java/technologies/javase/12-0-2-relnotes.html){target="\_blank"}
        - [All Java 12 Updates](https://www.oracle.com/java/technologies/javase/12all-relnotes.html){target="\_blank"}

    - Java SE 13.x

        - [Java SE 13.0.2](https://www.oracle.com/java/technologies/javase/13-0-2-relnotes.html){target="\_blank"}
        - [All Java 13 Updates](https://www.oracle.com/java/technologies/javase/13all-relnotes.html){target="\_blank"}

    - Java SE 14.x

        - [Java SE 14.0.2](https://www.oracle.com/java/technologies/javase/14-0-2-relnotes.html){target="\_blank"}
        - [All Java 14 Updates](https://www.oracle.com/java/technologies/javase/14all-relnotes.html){target="\_blank"}

    - Java SE 15.x

        - [Java SE 15.0.2](https://www.oracle.com/java/technologies/javase/15-0-2-relnotes.html){target="\_blank"}
        - [All Java 15 Updates](https://www.oracle.com/java/technologies/javase/15all-relnotes.html){target="\_blank"}

    - Java SE 16.x

        - [Java SE 16.0.2](https://www.oracle.com/java/technologies/javase/16-0-2-relnotes.html){target="\_blank"}
        - [All Java 16 Updates](https://www.oracle.com/java/technologies/javase/16all-relnotes.html){target="\_blank"}

    - Java SE 17 (LTS)

        - [Java SE 17.0.14(Oracle)](https://www.oracle.com/java/technologies/javase/17-0-14-relnotes.html){target="\_blank"}
        - [All Java 17 Updates](https://www.oracle.com/java/technologies/javase/17all-relnotes.html){target="\_blank"}

    </div>


    
#### :simple-postgresql: PostgreSQL

- New Version Supported: `16.8.1`
- Release Notes:

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
    To update the Gradle wrapper in an existing environment , you must run:
    
    ``` bash title="Terminal"
        ./gradlew wrapper --gradle-version 8.12.1 
    ```

    For more detailed migration guidelines, refer to [Upgrading Gradle Wrapper](https://docs.gradle.org/8.12.1/userguide/gradle_wrapper.html#sec:upgrading_wrapper){target="\_blank"}

- New Version Supported: `8.12.1`
- Release Notes:

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

- New Version Supported: `9.0.98`
- Release Notes: [Apache Tomcat 9](https://tomcat.apache.org/tomcat-9.0-doc/changelog.html){target="\_blank"}




#### :octicons-file-code-24: Etendo Gradle Plugin

- New Version Supported: `2.0.0` or higher
- Release Notes:

    - [Etendo Gradle Plugin - Release Notes](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md)
    - New Gradle Plugin Task: 

        ``` bash title="Terminal"
        ./gradlew cleanExpandCore
        ```
        This new task deletes directories created by the `expandCore` task.

    - Compatibility Flag

        ``` bash title="Terminal"
        -Pjava.version=11
        ```
        This new flag forces the use of Java 11 with version 25Q1.

#### :octicons-issue-opened-24: Etendo ISO
       
!!!note 
    The **Etendo 25** ISOs are currently based on Ubuntu Live Server `22.04.5` amd64 image. <br>
    For more information, visit [Etendo ISO Release Notes](../../../whats-new/release-notes/etendo-classic/iso.md).



### Third-Party Libraries 

All libraries previously located in `/lib/runtime` as JAR files have been updated to Gradle dependencies now defined in the `artifacts.list.COMPILATION.gradle` file at the root of the project.


#### Updated Libraries

- `dbsourcemanager.jar` -> `com.etendoerp.dbsm` version  `1.1.0`

    - Release Notes:

        - Changes to use new version of Apache Commons Lang 3 library.
        - Changes to use new version of Apache Commons Collections 4 library.
        - Changes in deprecated or removed features used in Java 17.
        - Added support for PostgreSQL 16.
    
 - `commons-collections.commons-collections` `3.2.2` -> `4.4`

    - Release Notes:

        - [Commons Collections 4.0](https://commons.apache.org/proper/commons-collections/release_4_0.html){target="\_blank"}
        - [Commons Collections 4.1](https://commons.apache.org/proper/commons-collections/release_4_1.html){target="\_blank"}
        - [Commons Collections 4.2](https://commons.apache.org/proper/commons-collections/release_4_2.html){target="\_blank"}
        - [Commons Collections 4.3](https://commons.apache.org/proper/commons-collections/release_4_3.html){target="\_blank"}
        - [Commons Collections 4.4](https://commons.apache.org/proper/commons-collections/release_4_4.html){target="\_blank"}

    - API Changes - Migration from Apache Commons Collections `3.2.2` to `4.4`:

        Starting with **Etendo 25.1.0**, Apache Commons Collections has been upgraded from **3.2.2** to **4.4**. This version introduces a new package structure. Classes previously imported from `org.apache.commons.collections` must now be updated to `org.apache.commons.collections4`.

    - Migration Instructions:

        Update all import statements and references to reflect the new package structure:

        ```java
        // Before (Apache Commons Collections 3.2.2)
        import org.apache.commons.collections.CollectionUtils;

        // After (Apache Commons Collections 4.4)
        import org.apache.commons.collections4.CollectionUtils;
        ```

        Additionally, review your code for deprecated, removed, or modified methods to ensure full compatibility with the updated library.

   
    !!! info 
        For detailed migration guidelines, please refer to the [Apache Commons Collections 4.4](https://commons.apache.org/proper/commons-collections/){target="\_blank"} documentation.

- `org.apache.commons:commons-lang3` `2.6` -> `3.17.0`
    - Release Notes:
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

    - API Changes - Migration from Apache Commons Lang `2.6` to `3.17`

        Starting in **Etendo 25.1.0**, Apache Commons Lang has been upgraded from version **2.6** to **3.17**. As part of this upgrade, the package structure has changed. Classes previously imported from `org.apache.commons.lang.*` must now be updated to use `org.apache.commons.lang3.*`.

    - Migration Instructions

        Update your import statements to reflect the new package structure:

        ```java
        // Before (Apache Commons Lang 2.6)
        import org.apache.commons.lang.StringUtils;

        // After (Apache Commons Lang 3.17)
        import org.apache.commons.lang3.StringUtils;
        ```

        Additionally, review your code for deprecated or modified methods and ensure compatibility with the updated library.

    - Additional Notes

        The previous version of the library remains available for backward compatibility but will be removed in future releases.

        !!! warning
            We strongly recommend migrating all custom developments to **Apache Commons Lang 3.17** to ensure long-term support and compatibility.

        !!! info
            For detailed migration guidelines, refer to the [Apache Commons Lang 3 migration notes](https://commons.apache.org/proper/commons-lang/article3_0.html){target="\_blank"}.

- `org.hibernate.common.hibernate-commons-annotations` `5.1.0.Final` -> `5.1.2.Final`
    - Release Notes:
        - [5.1.1.Final](https://in.relation.to/2016/08/12/hibernate-orm-511-final-release/){target="\_blank"}
        - [5.1.2.Final](https://in.relation.to/2016/09/19/hibernate-orm-5011-final-and-512-final-release/){target="\_blank"}

- `org.hibernate:hibernate-core` `5.4.2.Final` -> `5.6.15.Final`
    - Release Notes:
        - [5.4.x](https://github.com/hibernate/hibernate-orm/blob/5.4/changelog.txt){target="\_blank"}
        - [5.5.x](https://github.com/hibernate/hibernate-orm/blob/5.5/changelog.txt){target="\_blank"}

- `net.sf.jasperreports.jasperreports-fonts` `6.0.0` -> `6.17.0`
- `net.sf.jasperreports.jasperreports` `6.0.0` -> `6.17.0`
    - Release Notes:
        - [Releases Page – GitHub](https://github.com/Jaspersoft/jasperreports/releases){target="\_blank"}

- `org.apache.poi.poi` `3.10.1` -> `5.4.0`
    - Release Notes:
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
        
        For older versions, you can check:
        - [Apache POI Release Archive (source & binaries)](https://archive.apache.org/dist/poi/release/){target="\_blank"}
        - [Full changelog overview](https://poi.apache.org/changes.html){target="\_blank"}

- Apache POI 5.x Migration Guide

    This guide outlines the necessary changes to migrate projects using Apache POI 3.x/4.x to version 5.x, including how to replace deprecated classes, methods, and constants removed in recent versions.

    1. Replacing Deprecated Constants (`CellType`)
        
        In POI 5.x, the `Cell.CELL_TYPE_*` constants are replaced by the `CellType` enum.

        Example:

        ```java
        // Before
        cell.getCellType() == Cell.CELL_TYPE_STRING;

        // After
        cell.getCellType() == CellType.STRING;
        ```

        Key Mappings:

        | Old Constant              | New Constant       |
        |---------------------------|--------------------|
        | `Cell.CELL_TYPE_STRING`   | `CellType.STRING`  |
        | `Cell.CELL_TYPE_NUMERIC`  | `CellType.NUMERIC` |
        | `Cell.CELL_TYPE_BOOLEAN`  | `CellType.BOOLEAN` |
        | `Cell.CELL_TYPE_FORMULA`  | `CellType.FORMULA` |
        | `Cell.CELL_TYPE_BLANK`    | `CellType.BLANK`   |

        Required Import:

        ```java
        import org.apache.poi.ss.usermodel.CellType;
        ```

    2. Updating Cell Styles

        Alignment

        | Old Constant             | New Constant                |
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

        Fill Patterns

        ```java
        // Before
        style.setFillPattern(CellStyle.SOLID_FOREGROUND);

        // After
        style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        ```

        ```java
        import org.apache.poi.ss.usermodel.FillPatternType;
        ```

        Borders

        ```java
        // Before
        setBorderBottom((short) 1);

        // After
        setBorderBottom(BorderStyle.THIN);
        ```

        ```java
        import org.apache.poi.ss.usermodel.BorderStyle;
        ```

    3. Fonts API Changes

        The `Font.setBoldweight()` method is deprecated.  
        Now, you should use `Font.setBold(boolean)`.

        Example:

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

    4. Formula Evaluation API Changes:

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

        Evaluating formulas:

        ```java
        FormulaEvaluator evaluator = workbook.getCreationHelper().createFormulaEvaluator();
        CellValue cellValue = evaluator.evaluate(cell);
        ```

        Complete Example:

        ```java
        CellValue cellValue = evaluator.evaluate(cell);
        switch (cellValue.getCellType()) {
            case STRING:
                return cellValue.getStringValue();
            // other cases...
        }
        ```

    5. Additional Best Practices

        Avoid creating new `XSSFWorkbook()` unnecessarily. Instead, reuse:

        ```java
        Workbook workbook = cell.getSheet().getWorkbook();
        ```

        Use modern Map API:

        ```java
        // Instead of containsKey + put
        map.computeIfAbsent(key, k -> new ArrayList<>());
        ```

    6. Full Migration Example

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

    7. **Test your migrated code carefully**. Some subtle behavioral changes may exist in formula evaluation and styling.
    
    
    !!! info "Official Resources"
        - [Apache POI Documentation](https://poi.apache.org/components/spreadsheet/){target="\_blank"}
        - [Migration Guide from Older Versions](https://poi.apache.org/migration.html){target="\_blank"}
    

- `commons-beanutils.commons-beanutils` `1.8.3` -> `1.9.4` 
- `commons-codec.commons-codec` `1.1.1` -> `1.17.1`
- `commons-digester.commons-digester` `1.8.1` -> `2.1`
- `commons-fileupload.commons-fileupload` `1.4` -> `1.5`
- `commons-io.commons-io` `2.4` -> `2.16.1`
- `com.sun.istack.istack-commons-runtime` `3.0.7` -> `4.2.0`    

!!! info
    Refer to each library’s release notes for more detailed information on changes and how they might affect your system.

#### New Libraries

- `org.apache.commons.commons-text` `1.10.0`
    - [Documentation](https://commons.apache.org/proper/commons-text/){target="\_blank"}

- `org.apache.commons.commons-math3` `3.6.1`
    - [Documentation](https://commons.apache.org/proper/commons-math/){target="\_blank"}

- `org.codehaus.castor.castor-core` `1.4.1`
    - [Documentation](https://castor-data-binding.github.io/castor/){target="\_blank"}

- `org.codehaus.castor:castor-xml` `1.4.1`
    - [Documentation](https://castor-data-binding.github.io/castor/){target="\_blank"}

- `com.lowagie:itext` `2.1.7`
    - [Documentation](https://itextpdf.com/resources){target="\_blank"}

#### Removed Libraries

- `itext-pdfa-5.5.0.jar`
- `itextpdf-5.5.0.jar`
- `jcommon-1.0.15.jar`
- `jxl-2.6.10.jar`
