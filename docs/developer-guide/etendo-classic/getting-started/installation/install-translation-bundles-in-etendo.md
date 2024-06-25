---
title: Install Translation Bundles in Etendo
---

## Overview
This page will explain how to install translation bundles, as their process is different from that of the other bundles. 
These bundles require the correct version of the ones they translate to be installed manually.

## Installation steps

To install a bundle, follow the corresponding section of the documentation on how to [Install Modules in Etendo](../../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md).

!!! warning
    Remember to add both the translation bundle and the correct version of the bundle it translates as dependencies! Otherwise, the environment's compilation will fail. For example:


    === ":material-language-java: JARs"

        ```groovy

        dependencies {
            // Add your dependency here
            implementation ('com.etendo:example.module:1.0.0')
            implementation ('com.etendo:example.module.es_es:1.0.0')
        }
        ```

    === ":octicons-package-16: Sources"

        ```groovy
        dependencies {
            // Add your dependency here
            moduleDeps ('com.etendo:example.module:1.0.0@zip'){ transitive = true }
            moduleDeps ('com.etendo:example.module.es_es:1.0.0@zip'){ transitive = true }
        }
        ```

## Bundle Compatibility

For information on what bundle version is compatible with which translation bundle, the documentation and [Release Notes](../../../../whats-new/overview.md){target="_blank"} for each bundle can be referred to.

## Troubleshooting

- **Access to dependencies not allowed**: check you have your GitHub credentials and their access level correctly configured. Refer to the [Etendo installation guide](../../../../getting-started/installation.md) for more information.
- **Fields, columns, etc. not found**: check you have set the translated bundle version compatible with the version of the translation bundle you want to install. Refer to the translation bundle's [Release Notes](../../../../whats-new/overview.md){target="_blank"} for a list of the compatible bundle versions.