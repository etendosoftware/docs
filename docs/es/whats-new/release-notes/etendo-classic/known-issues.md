---
Title: Incidencias conocidas
tags:
    - Incidencias conocidas
    - Incidencias resueltas
    - Incidencias pendientes
---

## Visión general
Esta página muestra las incidencias conocidas reportadas por el equipo de soporte.

## Incidencias conocidas

??? success "EPL-1449 Resuelto"

    ### [EPL-1449](https://github.com/etendosoftware/etendo_backups_script/issues/1){target="\_blank"} Gradle pierde permisos de ejecución al realizar un etendo-restore.

    #### Solución alternativa

    Aplique el siguiente cambio en el archivo etendo-restore para asegurar que el archivo gradlew quede excluido del cambio de permisos con chmod:

    ``` bash title="etendo-restore"
    - find /opt/EtendoERP -type f -exec chmod 644 '{}' \+
    + find /opt/EtendoERP -type f ! -name gradlew -exec chmod 644 '{}' \+
    ```

    Esta solución alternativa es aplicable si ha desplegado Etendo desde la ISO en versiones anteriores a [24.1.4](https://etendo-appliances.s3.eu-west-1.amazonaws.com/etendo/iso/etendo-24Q1.4.iso). A partir de esa versión, ya no se observa el problema de cambios de permisos en el archivo gradlew.

??? success "EE-856 Resuelto"

    ### [EE-856](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/34){target="\_blank"} El conjunto de datos del Modelo 390 duplica datos para 2022 cuando se aplica en un servidor migrado de OB a Etendo después de 01-2023.

    #### Solución alternativa

    **Advertencia:** La siguiente solución alternativa puede variar dependiendo de diversos factores, tales como:

    - Impuestos creados manualmente
    - Categorías de impuestos creadas manualmente
    - Conjunto de datos de impuestos aplicado en una organización distinta de \*
    - Intentos de aplicar los conjuntos de datos antes de realizar las soluciones alternativas
    - etc.

    Si tiene alguna de estas características en su entorno, contacte con el equipo de soporte para una solución personalizada.

    ---

    Existen dos formas de resolver el problema, dependiendo de cómo se hayan aplicado previamente los conjuntos de datos de impuestos y de impuestos temporales:

    1. **Conjunto de datos de impuestos temporales en organizaciones "individuales" y conjunto de datos de impuestos a nivel \*:**

        1. Ejecute este script SQL, que realizará lo siguiente:

            1. Mover los impuestos desde una de las organizaciones (la primera en la que se aplicó el conjunto de datos de impuestos temporales) a \*.

            2. Actualizar los impuestos de la organización \* y cambiar sus IDs de historial de aplicación (un ID para saber qué impuesto se aplicó), para convertirlos de los de Openbravo a los de Etendo.

            3. Actualizar los IDs de historial de aplicación para aquellos impuestos temporales que se hayan creado en organizaciones individuales, de modo que el proceso de importación del conjunto de datos no los detecte y no inserte datos en ellos.

            [Corrección de impuestos en distintas organizaciones](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_different_orgs.sql)

        2. Instale el conjunto de datos de impuestos a nivel \*. Se actualizarán los impuestos de la organización \*.

        3. Ejecute el script de corrección donde se resuelve el problema de duplicación del Modelo 390.

            [Corrección del Modelo 390 de informes fiscales 2022](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_localization_spain_390_2022_ids.sql)

        4. Aplique la actualización del conjunto de datos para el modelo fiscal 390.

    2. **Conjuntos de datos de impuestos e impuestos temporales aplicados ambos a nivel \*:**

        1. Ejecute el script de impuestos diseñado en la incidencia [EE-808](#ee-808-problema-al-intentar-importar-el-conjunto-de-datos-impuestos-configuración-para-españa-si-el-entorno-ya-ha-importado-el-conjunto-de-datos-relacionado-con-los-impuestos-temporales-303-de-openbravo).

            [Corrección de impuestos para la misma organización](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_same_org.sql)

        2. Ejecute el script de corrección donde se resuelve el problema de duplicación del Modelo 390.

            [Corrección del Modelo 390 de informes fiscales 2022](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_localization_spain_390_2022_ids.sql)

        3. Aplique la actualización del conjunto de datos de impuestos para la organización correspondiente.

        4. Aplique la actualización del conjunto de datos para el modelo fiscal 390.

??? success "EE-808 Resuelto"

    ### [EE-808](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/33){target="\_blank"} Problema al intentar importar el conjunto de datos 'impuestos: configuración para España' si el entorno ya ha importado el conjunto de datos relacionado con los impuestos temporales 303 de Openbravo.

    #### Solución alternativa

    **Advertencia:** La siguiente solución alternativa puede variar dependiendo de diversos factores, tales como:

    - Impuestos creados manualmente
    - Categorías de impuestos creadas manualmente
    - Conjunto de datos de impuestos aplicado en una organización distinta de \*
    - Intentos de aplicar los conjuntos de datos antes de realizar las soluciones alternativas
    - etc.

    Si tiene alguna de estas características en su entorno, contacte con el equipo de soporte para una solución personalizada.

    ---

    Existen dos formas de resolver el problema, dependiendo de cómo se hayan aplicado previamente los conjuntos de datos de impuestos y de impuestos temporales:

    1. **Conjunto de datos de impuestos temporales en organizaciones "individuales" y conjunto de datos de impuestos a nivel \*:**

        1. Ejecute este script SQL, que realizará lo siguiente:

            1. Mover los impuestos desde una de las organizaciones (la primera en la que se aplicó el conjunto de datos de impuestos temporales) a \*.

            2. Actualizar los impuestos de la organización \* y cambiar sus IDs de historial de aplicación (un ID para saber qué impuesto se aplicó), para convertirlos de los de Openbravo a los de Etendo.

            3. Actualizar los IDs de historial de aplicación para aquellos impuestos temporales que se hayan creado en organizaciones individuales, de modo que el proceso de importación del conjunto de datos no los detecte y no inserte datos en ellos.

            [Corrección de impuestos en distintas organizaciones](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_different_orgs.sql)

        2. Instale el conjunto de datos de impuestos a nivel \*. Se actualizarán los impuestos de la organización \*.

    2. **Conjuntos de datos de impuestos e impuestos temporales aplicados ambos a nivel \*:**
        1. Ejecute el siguiente script, que actualizará los impuestos de la organización \* y cambiará sus IDs de historial de aplicación (un ID para saber qué impuesto se aplicó), para convertirlos de los de Openbravo a los de Etendo:

            [Corrección de impuestos para la misma organización](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_same_org.sql)

        2. Instale el conjunto de datos de impuestos a nivel \*. Se actualizarán los impuestos de la organización \*.

    Los siguientes pasos son los mismos para ambos casos:

    1. Ejecute el siguiente script, que actualizará el modelo 303, cambiando sus IDs de Openbravo a IDs de Etendo.

        [Corrección del Modelo 303 de informes fiscales 2023](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_localization_spain_303_2023_ids.sql)

    2. Instale el conjunto de datos del modelo 303 a nivel de organizaciones individuales. Los parámetros correspondientes se insertarán en los impuestos de la organización \*, cada uno asociado a su organización individual específica.

??? success "EE-758 Resuelto"

    ### [EE-758](https://github.com/etendosoftware/com.etendoerp.financial.extensions/issues/17){target="\_blank"} Funcionalidad incorrecta del módulo de liquidación de tercero con la combinación de pago (entrada/salida) y uso de crédito.

    #### Atención

    La combinación de pagos (entrada/salida) con el uso de crédito en el módulo de liquidación de tercero presenta actualmente incidencias. Valores incorrectos del importe y del crédito utilizado pueden provocar descuadres en la cuenta financiera. Se recomienda no combinar el uso de crédito con la liquidación hasta que esta incidencia se resuelva.

??? success "EPL-858 Resuelto"

    ### [EPL-858](https://github.com/etendosoftware/com.etendoerp.gradleplugin/issues/34){target="\_blank"} Etendo no compila con la última versión del plugin de Gradle en formato JAR.

    #### Solución alternativa

    Antes de ejecutar las tareas de configuración en un proyecto de Etendo en formato JAR, debe seguir los siguientes pasos:

    En la ruta del código fuente, abra `build.gradle` y localice el bloque 'etendo' en el archivo. Dentro de este, añada la siguiente propiedad:

    ``` groovy title="build.gradle" 
    etendo {
        ignoreCoreJarDependency = true
    }
    ```

    Esta configuración le permitirá descargar el código fuente del proyecto en su entorno local. Será necesario para los siguientes pasos.

    Ahora debe ejecutar el comando que descargará el código fuente:

    ```bash title='terminal'
    ./gradlew clean
    ./gradlew expandCore 
    ```
    Si no desea cambiar el `build.gradle`, puede ejecutar el comando `./gradlew expandCore` y añadir el flag `-PforceExpand=true` al final del mismo.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.