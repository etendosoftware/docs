---
title: Install Translation Bundles in Etendo
tags:
    - Install Translations
    - Translation
    - Translation Bundle
---

# Install Translation Bundles in Etendo Classic

## Overview
This page explains how to install translation bundles in Etendo Classic, which is slightly different from standard module installation.

## Installation steps

Follow the standard [module installation](./install-modules-in-etendo.md) guide, but make sure to include both the original bundle and its corresponding translation bundle, copying the installation line from the [Etendo Marketplace](https://marketplace.etendo.cloud/#/modules?page=1&category=0821B7B067004CD0BAD7A583B2BA9FD2){target="_blank"}, you can filter the **Translation** category to find all available translations.

!!! warning
    Always include both the original module and its translation bundle as dependencies. Missing either will cause compilation to fail.

    === ":material-language-java: JARs"

        ```groovy

        dependencies {
            // Add your dependency here
            implementation ('com.etendo:example.module:[3.0.0,4.0.0)')
            implementation ('com.etendo:example.module.es_es:[1.0.0,)')
        }
        ```

    === ":octicons-package-16: Sources"

        ```groovy
        dependencies {
            // Add your dependency here
            moduleDeps ('com.etendo:example.module:[3.0.0,4.0.0)@zip'){ transitive = true }
            moduleDeps ('com.etendo:example.module.es_es:[1.0.0,)@zip'){ transitive = true }
        }
        ```

## Bundle Compatibility

To check compatibility between a module and its translation bundle. For example, the [Warehouse Extensions ES - Release Notes](../../../../whats-new/release-notes/etendo-classic/translation-bundles/warehouse-extensions-es_es/release-notes.md).


## Troubleshooting

1. By default, translations are applied when you update the database. If they are not, or if you update the module version, run:

    ```bash title="Terminal"

    ./gradlew install.translation -Dmodule=<javapackage>
    ./gradlew update.database smartbuild
    ```

    !!! info
        `install.translation` sets the module status to pending to install. The translations will apply during the next `update.database` run.

2. To force installation of all translation modules, add `forceRefData=true` to `gradle.properties` file,  then run:

    ```bash title="Terminal"
    ./gradlew setup
    ./gradlew update.database smartbuild
    ```