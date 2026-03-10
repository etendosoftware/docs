---
title: Instalar bundles de traducción en Etendo
tags:
    - Instalar traducciones
    - Traducción
    - Bundle de traducción
---

# Instalar bundles de traducción en Etendo Classic

## Visión general
Esta página explica cómo instalar bundles de traducción en Etendo Classic, lo cual es ligeramente diferente de la instalación estándar de módulos.

## Pasos de instalación

Siga la guía estándar de [instalación de módulos](./install-modules-in-etendo.md), pero asegúrese de incluir tanto el bundle original como su bundle de traducción correspondiente, copiando la línea de instalación desde [Etendo Marketplace](https://marketplace.etendo.cloud/#/modules?page=1&category=0821B7B067004CD0BAD7A583B2BA9FD2){target="_blank"}; puede filtrar la categoría **Traducción** para encontrar todas las traducciones disponibles.

!!! warning
    Incluya siempre tanto el módulo original como su bundle de traducción como dependencias. Si falta cualquiera de los dos, la compilación fallará.

    === ":material-language-java: JARs"

        ```groovy

        dependencies {
            // Add your dependency here
            implementation ('com.etendo:example.module:[3.0.0,4.0.0)')
            implementation ('com.etendo:example.module.es_es:[1.0.0,)')
        }
        ```

    === ":octicons-package-16: Fuentes"

        ```groovy
        dependencies {
            // Add your dependency here
            moduleDeps ('com.etendo:example.module:[3.0.0,4.0.0)@zip'){ transitive = true }
            moduleDeps ('com.etendo:example.module.es_es:[1.0.0,)@zip'){ transitive = true }
        }
        ```

## Compatibilidad de bundles

Para comprobar la compatibilidad entre un módulo y su bundle de traducción. Por ejemplo, las [Warehouse Extensions ES - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/translation-bundles/warehouse-extensions-es_es/release-notes.md).

## Resolución de problemas

1. De forma predeterminada, las traducciones se aplican cuando actualiza la base de datos. Si no se aplican, o si actualiza la versión del módulo, ejecute:

    ```bash title="Terminal"

    ./gradlew install.translation -Dmodule=<javapackage>
    ./gradlew update.database smartbuild
    ```

    !!! info
        `install.translation` establece el estado del módulo como pendiente de instalar. Las traducciones se aplicarán durante la siguiente ejecución de `update.database`.

2. Para forzar la instalación de todos los módulos de traducción, añada `forceRefData=true` al archivo `gradle.properties` y, a continuación, ejecute:

    ```bash title="Terminal"
    ./gradlew setup
    ./gradlew update.database smartbuild
    ```

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.