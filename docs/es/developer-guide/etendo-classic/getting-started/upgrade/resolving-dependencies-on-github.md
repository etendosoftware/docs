---
title: Migración y resolución de dependencias de bundles y módulos en GitHub
tags:
    - Migración a GitHub
    - Actualización de dependencias
    - Módulos de Etendo
    - Guía de transición
---
## 🔄 Migración y resolución de dependencias de bundles y módulos en GitHub

Hola, Partner de Etendo 👋. Hemos migrado los bundles y módulos desde Nexus a GitHub. Esto nos permite aprovechar la estabilidad de GitHub y tener los paquetes asociados a cada bundle y las versiones en el mismo repositorio. Aquí le proporcionamos una guía paso a paso para ayudarle a realizar la transición.
### 📝 Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/OhiV6ObyGG4" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

### 📦 Bundles migrados

Los siguientes bundles se han migrado a GitHub, junto con todas sus versiones. Compruebe la compatibilidad con Etendo Core; en caso de que tenga una versión antigua de Etendo, debe actualizar antes.
Recomendamos migrar a Etendo 23.2.0 o superior y las dependencias a las últimas versiones soportadas.

|Bundle|Javapakage|Versión|Desde Core | A core|
|--|--|--|--|--|
|Sales Extensions						|com.etendoerp.sales.extensions							|1.5.0|22.1.0	|23.2.x	|
|Sales Extensions ES		|com.etendoerp.sales.extensions.es_es				|1.4.0|22.1.0	|23.2.x	|
|Financial Extensions			|com.etendoerp.financial.extensions					|1.8.0|23.1.4	|23.2.x	|
|Financial Extensions ES	|com.etendoerp.financial.extensions.es_es		|1.2.0|23.1.4	|23.2.x	|
|Production Extensions		|com.etendoerp.production.extensions.				|1.3.0|22.1.0	|23.2.x	|
|Production Extensions ES	|com.etendoerp.production.extensions.es_es	|1.1.0|22.1.0	|23.2.x	|
|Platform Extensions			|com.etendoerp.platform.extensions					|1.6.0|23.2.0	|23.2.x	|
|Platform Extensions ES		|com.etendoerp.platform.extensions.es_es	|1.2.0|22.1.0	|23.2.x	|
|Warehouse Extensions			|com.etendoerp.warehouse.extensions					|1.3.0|23.1.4	|23.2.x	|
|Warehouse Extensions ES	|com.etendoerp.warehouse.extensions.es_es		|1.2.0|23.1.4	|23.2.x	|
|Essential Extensions			|com.etendoerp.essentials.extensions				|1.1.0|23.1.4	|23.2.x	|
|Essential Extensions ES	|com.etendoerp.essentials.extensions.es_es		|1.0.0|23.1.4	|23.2.x	|
|Localizacion Española		|com.etendoerp.localization.spain.extensions|1.4.0|22.4.3	|23.2.x	|

### 🚀 Proceso de migración
 
1. **Actualizar el archivo `settings.gradle`**: deberá actualizar su archivo `settings.gradle` para añadir el nuevo repositorio de GitHub.

    ```groovy title="settings.gradle"
    pluginManagement {
        repositories {
            mavenCentral()
            gradlePluginPortal()
            maven {
                url 'https://maven.pkg.github.com/etendosoftware/com.etendoerp.gradleplugin'
                credentials {
                    username "${githubUser}"
                    password "${githubToken}"
                }
            }
            maven {
                url 'https://repo.futit.cloud/repository/maven-public-snapshots'
            }
        }
    }

    // Add modules subprojects
    new File("${this.rootDir}/modules").listFiles().each {
        if (it.directory && new File(it, 'build.gradle').exists()) {
            include(":modules:${it.name}")
        }
    }

    rootProject.name = "etendo"
    ```

2. **Actualizar el plugin de Gradle de Etendo**: necesita actualizar `com.etendoerp.gradleplugin` a la versión 1.1.0 o posterior.

    ```groovy title="build.gradle"
    plugins {
        id 'java'
        id 'war'
        id 'groovy'
        id 'maven-publish'
        id 'com.etendoerp.gradleplugin' version '<version>' 
    }
    ```

3. **Configuración de GitHub**: necesita configurar su usuario y token de GitHub para tener acceso de lectura a los paquetes de Etendo. Puede crear el token siguiendo la [guía técnica de uso de repositorios](../../../../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).

    ```groovy title="gradle.properties"
    nexusUser=
    nexusPassword=
    githubUser=<User>
    githubToken=<Token>

    context.name=etendo

    bbdd.sid=etendo
    bbdd.port=5432
    bbdd.systemUser=postgres
    bbdd.systemPassword=syspass
    bbdd.user=tad
    bbdd.password=tad
    ```

4. **Comprobación de dependencias**: revise las dependencias en su archivo `build.gradle` de Etendo para asegurarse de que hay bundles que pueden actualizarse a versiones publicadas en GitHub. Si todavía no está listo para migrar, no hay problema: Nexus estará disponible hasta marzo de 2024.

5. **Resolver nuevas dependencias**

### Consideraciones

Una restricción que tiene GitHub es que los paquetes publicados deben tener el `javapackage` en minúsculas, por lo que tuvimos que refactorizar los módulos de traducción, que anteriormente terminaban con el sufijo "_ES". Ahora, todos los paquetes, incluidas las traducciones de bundles, tienen su artefacto en minúsculas.

!!! warning
    Una consideración especial son los módulos `org.openbravo.module.invoiceTaxReportEnhanced30` y `org.openbravo.module.invoiceTaxReportEnhanced30.en_ES`, que pertenecen al bundle Spain Localisation y también fueron refactorizados.

Esto afecta a los entornos actuales. Para corregirlo, debemos:

=== "Dependencias en fuentes"

    1. Si el entorno tiene las dependencias como "moduleDeps", en fuentes, tendremos que eliminar de la carpeta `/modules` todas las que terminen en "_ES".

        Proporcionamos un script para eliminar todos los módulos que podrían resolverse desde Nexus y, a continuación, volver a descargarlos desde GitHub.

        ```bash
        #!/bin/bash

        ## Define the list of modules to be deleted
        modules=("com.etendoerp.accounting.templates"
        "com.etendoerp.accounting.templates.es_ES"
        "com.etendoerp.advanced.financial.docs.processing"
        "com.etendoerp.advanced.financial.docs.processing.es_ES"
        "com.etendoerp.advanced.financial.docs.processing.template"
        "com.etendoerp.advanced.intercompany"
        "com.etendoerp.advanced.intercompany.es_ES"
        "com.etendoerp.advanced.work.effort"
        "com.etendoerp.advanced.work.effort.es_ES"
        "com.etendoerp.asyncprocess"
        "com.etendoerp.bankingpool"
        "com.etendoerp.bankingpool.es_ES"
        "com.etendoerp.bulk.posting"
        "com.etendoerp.bulk.posting.es_ES"
        "com.etendoerp.etendorx"
        "com.etendoerp.financial.extensions"
        "com.etendoerp.financial.extensions.es_ES"
        "com.etendoerp.financial.reports.advanced"
        "com.etendoerp.financial.reports.advanced.es_ES"
        "com.etendoerp.gljournal.advanced"
        "com.etendoerp.gljournal.advanced.es_ES"
        "com.etendoerp.localization.spain.extensions"
        "com.etendoerp.payment.removal"
        "com.etendoerp.payment.removal.es_ES"
        "com.etendoerp.payment.removal.template"
        "com.etendoerp.platform.extensions"
        "com.etendoerp.platform.extensions.es_ES"
        "com.etendoerp.printdocumentws"
        "com.etendoerp.production.extensions"
        "com.etendoerp.production.extensions.es_ES"
        "com.etendoerp.quotation"
        "com.etendoerp.quotation.es_ES"
        "com.etendoerp.quotation.template"
        "com.etendoerp.reactivate.warehouse.documents"
        "com.etendoerp.reactivate.warehouse.documents.es_ES"
        "com.etendoerp.reactivate.warehouse.documents.template"
        "com.etendoerp.reactor"
        "com.etendoerp.sales.extensions"
        "com.etendoerp.sales.extensions.es_ES"
        "com.etendoerp.stock.history"
        "com.etendoerp.stock.history.es_ES"
        "com.etendoerp.warehouse.extensions"
        "com.etendoerp.warehouse.extensions.es_ES"
        "com.etendoerp.webhookevents"
        "com.exos.erp.reportcachemanagement"
        "com.smf.asset.amortization.report"
        "com.smf.currency.apiconfig"
        "com.smf.currency.apiconfig.es_ES"
        "com.smf.currency.conversionrate"
        "com.smf.currency.conversionrate.es_ES"
        "com.smf.gljournal.reverse"
        "com.smf.gljournal.reverse.template"
        "com.smf.jobs.defaults.es_ES"
        "com.smf.ws.printdocument"
        "org.openbravo.advpaymentmngt.es_ES"
        "org.openbravo.alerts.accounting30"
        "org.openbravo.alerts.accounting30.es_ES"
        "org.openbravo.client.application.es_ES"
        "org.openbravo.client.htmlwidget.es_ES"
        "org.openbravo.client.kernel.es_ES"
        "org.openbravo.client.myob.es_ES"
        "org.openbravo.client.querylist.es_ES"
        "org.openbravo.client.widgets.es_ES"
        "org.openbravo.finance.checkprinting"
        "org.openbravo.finance.checkprinting.es_ES"
        "org.openbravo.financial.bpsettlement"
        "org.openbravo.financial.bpsettlement.es_ES"
        "org.openbravo.financial.paymentreport.es_ES"
        "org.openbravo.localization.spain30"
        "org.openbravo.localization.spain.referencedata.accounts"
        "org.openbravo.localization.spain.referencedata.accounts.pymes"
        "org.openbravo.localization.spain.referencedata.taxes"
        "org.openbravo.localization.spain.referencedata.translation.esES"
        "org.openbravo.module.aeat190.es"
        "org.openbravo.module.aeat303.es"
        "org.openbravo.module.aeat347apr.es"
        "org.openbravo.module.aeat347apr.es.es_ES"
        "org.openbravo.module.aeat349.es"
        "org.openbravo.module.aeat390.es"
        "org.openbravo.module.bptaxidkey"
        "org.openbravo.module.cifnifvalidator"
        "org.openbravo.module.cifnifvalidator.es_ES"
        "org.openbravo.module.countryisocode"
        "org.openbravo.module.cuaderno43.es"
        "org.openbravo.module.epigrafes.iae.es"
        "org.openbravo.module.eucountries"
        "org.openbravo.module.finactvalidator.es"
        "org.openbravo.module.incoterms"
        "org.openbravo.module.intrastat"
        "org.openbravo.module.intrastat.es_ES"
        "org.openbravo.module.intrastat.spain"
        "org.openbravo.module.invoicesregisterbook"
        "org.openbravo.module.invoicesregisterbook.es_ES"
        "org.openbravo.module.invoicesregisterbook.estaxes"
        "org.openbravo.module.invoiceTaxReportEnhanced30"
        "org.openbravo.module.invoiceTaxReportEnhanced30.es_ES"
        "org.openbravo.module.organization.representative.es"
        "org.openbravo.module.paymentmethod.type"
        "org.openbravo.module.remittance"
        "org.openbravo.module.remittance.es_ES"
        "org.openbravo.module.sii"
        "org.openbravo.module.sii.es_ES"
        "org.openbravo.module.sii.template"
        "org.openbravo.module.taximprovements.ES"
        "org.openbravo.module.taximprovements.es_ES"
        "org.openbravo.module.taxreportlauncher"
        "org.openbravo.module.taxreportlauncher.es"
        "org.openbravo.numbertoword"
        "org.openbravo.numbertoword_en"
        "org.openbravo.numbertoword_es"
        "org.openbravo.numbertoword.es_ES"
        "org.openbravo.proflocalization.spain.dataset"
        "org.openbravo.reports.ordersawaitingdelivery.es_ES"
        "org.openbravo.service.datasource.es_ES"
        "org.openbravo.service.integration.google.es_ES"
        "org.openbravo.service.integration.openid.es_ES"
        "org.openbravo.spain.regions"
        "org.openbravo.spanishdefaultdata.paymentmethods"
        "org.openbravo.spanishdefaultdata.paymentterms"
        "org.openbravo.userinterface.selector.es_ES"
        "org.openbravo.userinterface.smartclient.es_ES"
        "org.openbravo.utility.multiplebpselector"
        "org.openbravo.utility.multiplebpselector.es_ES"
        "org.openbravo.util.javax.xml.soap"
        "org.openbravo.util.saaj.impl"
        "org.openbravo.v3.translation.pack.es_ES")

        ## Define the modules directory
        module_directory="./modules"

        ## Iterate over each module and delete it
        for module in "${modules[@]}"; do
        if [ -d "${module_directory}/${module}" ]; then
            echo "Deleting ${module_directory}/${module}..."
            rm -rf "${module_directory}/${module}"
        else
            echo "Directory ${module_directory}/${module} does not exist"
        fi
        done

        echo "Modules deletion has been completed."

        ```


        !!! warning
                Asegúrese de que los módulos no tienen personalizaciones; de lo contrario, se eliminarán los cambios locales.
        
        
        Copie este código y cree un archivo `deleteNexusDependencies.sh` en el proyecto raíz de Etendo; ejecute `chmod +x deleteNexusDependencies.sh` para dar permisos de ejecución y, a continuación, ejecute `./deleteNexusDependencies.sh` para eliminar las dependencias.

    2. Modifique el `build.gradle` de su proyecto y cambie las dependencias a minúsculas. Por ejemplo:
        ```groovy title="build.gradle"
        moduleDeps('com.etendoerp:financial.extensions.es_ES:<version>@zip') {transitive = true}
        // Replace by
        moduleDeps('com.etendoerp:financial.extensions.es_es:<version>@zip') {transitive = true}

        ```
    3. Ejecute la tarea `./gradlew expandModules` para descargar las nuevas dependencias.
    4. Ejecute `./gradlew update.database smartbuild` para recompilar el entorno.

=== "Dependencias en JAR"

    Si las dependencias se declaran como `implementation`, esto significa que están en formato JAR; simplemente cambie las mayúsculas a minúsculas.
    Por ejemplo:

    ``` groovy
    implementation('com.etendoerp:financial.extensions.es_ES:<version>')
    // Replace by
    implementation('com.etendoerp:financial.extensions.es_es:<version>')

    ```

    A continuación, ejecute `./gradlew update.database smartbuild`; esto descargará dinámicamente las dependencias y compilará el entorno de nuevo.

!!! info
    También es posible que en el `build.gradle` haya una combinación de ambos tipos de dependencias; debe seguir ambos pasos.

!!! success
    Recomendamos utilizar las dependencias en formato JAR, manteniendo un espacio de trabajo más limpio y un proceso de actualización más sencillo.
    Esta es una buena oportunidad para migrar.

!!! failure
    Recuerde: Nexus seguirá estando disponible hasta marzo de 2024, por lo que tiene tiempo para realizar esta transición 🕑. Esperamos que esta guía le resulte útil.

Si encuentra cualquier incidencia o necesita ayuda adicional, no dude en ponerse en contacto con nuestro [servicio de soporte](http://support.etendo.software){target="_blank"}🚑.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.