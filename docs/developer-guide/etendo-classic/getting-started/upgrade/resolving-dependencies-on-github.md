---
title: Migrating and Resolving Dependencies of Bundles and Modules on GitHub
---
## 🔄 Migrating and Resolving Dependencies of Bundles and Modules on GitHub

Hello, Etendo Partner 👋. We've moved the bundles and modules from Nexus to GitHub. This allows us to take advantage of the stability of GitHub, and have the packages associated with each bundle and the releases in the same repository. Here we provide a step-by-step guide to help you make the transition.
### 📝 Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/OhiV6ObyGG4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

### 📦 Migrated Bundles

The following bundles have been migrated to GitHub, along with all their versions, check the Etendo Core compatibility, in case that you have a old Etendo version you must update before:
We recommend migrating to Etendo 23.2.0 or grather and the dependencies to the latest supported versions. 

|Bundle|Javapakage|Version|From Core | To core|
|--|--|--|--|--|
|Sales Extensions					|com.etendoerp.sales.extensions							|1.5.0|22.1.0	|23.2.x	|
|Sales Extensions ES			|com.etendoerp.sales.extensions.es_es				|1.4.0|22.1.0	|23.2.x	|
|Financial Extensions			|com.etendoerp.financial.extensions					|1.8.0|23.1.4	|23.2.x	|
|Financial Extensions ES	|com.etendoerp.financial.extensions.es_es		|1.2.0|23.1.4	|23.2.x	|
|Production Extensions		|com.etendoerp.production.extensions.				|1.3.0|22.1.0	|23.2.x	|
|Production Extensions ES	|com.etendoerp.production.extensions.es_es	|1.1.0|22.1.0	|23.2.x	|
|Platform Extensions			|com.etendoerp.platform.extensions					|1.6.0|23.2.0	|23.2.x	|
|Platform Extensions ES		|com.etendoerp.platform.extensions.es_es		|1.2.0|22.1.0	|23.2.x	|
|Warehouse Extensions			|com.etendoerp.warehouse.extensions					|1.3.0|23.1.4	|23.2.x	|
|Warehouse Extensions ES	|com.etendoerp.warehouse.extensions.es_es		|1.2.0|23.1.4	|23.2.x	|
|Essential Extensions			|com.etendoerp.essentials.extensions				|1.1.0|23.1.4	|23.2.x	|
|Essential Extensions ES	|com.etendoerp.essentials.extensions.es_es	|1.0.0|23.1.4	|23.2.x	|
|Localizacion Española		|com.etendoerp.localization.spain.extensions|1.4.0|22.4.3	|23.2.x	|



### 🚀 Migration Process
 
1. **Update `settings.gradle` File**: You'll need to update your `settings.gradle` file to add the new GitHub repository.

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

2. **Update Etendo Gradle Plugin**: You need to update `com.etendoerp.gradleplugin` to version 1.1.0 or later. Alternatively, you can use `latest.release` to always get the latest version, in this case the gradle version should be 7.3.2, to check the gradle version execute './gradlew --version' and to upgrade execute ./gradlew wrapper --gradle-version 7.3.2 

    ```groovy title="build.gradle"
    plugins {
        id 'java'
        id 'war'
        id 'groovy'
        id 'maven-publish'
        id 'com.etendoerp.gradleplugin' version 'latest.release' 
    }
    ```

3. **GitHub Setup**: You need to set up your GitHub username and token to have read access to Etendo packages. You can create the token by following the [Use of Repositories technical guide](/docs/developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo/).

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

4. **Dependency Check**: Review the dependencies in your Etendo `build.gradle` file to make sure there are bundles that can be upgraded to versions published on GitHub. If you are not ready to migrate yet, that's OK, Nexus will be available until March 2024.

5. **Resolve New Dependencies**

### Considerations

One restriction that GitHub has is that published packages must have a lowercase javapackage, so we had to refactor the translation modules, which previously ended with the suffix "_ES", now all packages including bundle translations have their artifact in lowercase.  

!!! warning
    A special consideration are the modules `org.openbravo.module.invoiceTaxReportEnhanced30` and `org.openbravo.module.invoiceTaxReportEnhanced30.en_ES` which belong to the Spain Localisation bundle and were refactored as well.


This affects the current environments, to fix this we have to: 

=== "Dependencies in Sources"

    1. If the environment has the dependencies as "moduleDeps", in sources, we will have to remove from the `/modules` folder all the ones ending in "_ES". 

        We provide a script to delete all modules that could be resolved from Nexus and then re-download them from GitHub. 

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
                Make sure the modules have no customizations, otherwise local changes will be deleted.
        
        
        Copy this code and create a file `deleteNexusDependencies.sh` in the Etendo root project, run `chmod +x deleteNexusDependencies.sh` to give execution permissions and then run `./deleteNexusDependencies.sh` to delete the dependencies. 

    2. Modify the build.gradle of our project and change the dependencies to lowercase. For example:
        ```groovy title="build.gradle"
        moduleDeps('com.etendoerp:financial.extensions.es_ES:latest.release@zip') {transitive = true}
        // Replace by
        moduleDeps('com.etendoerp:financial.extensions.es_es:latest.release@zip') {transitive = true}

        ```
    3. Execute `./gradlew expandModules` task to download the new dependencies. 
    4. Run `./gradlew update.database smartbuild` to recompile the environment. 

=== "Dependencies in JAR"

    If the dependencies are declared as implementation, this means that they are in JAR format, just change the uppercase to lowercase. 
    For example:

    ``` groovy
    implementation('com.etendoerp:financial.extensions.es_ES:latest.release')
    // Replace by
    implementation('com.etendoerp:financial.extensions.es_es:latest.release')

    ```

    Then run `./gradlew update.database smartbuild`, this will dynamically download the dependencies and compile the environment again.

!!! info
    It is also possible that in the build.gradle there is a combination of both types of dependencies, you should follow both steps.

!!! success
    We recommend using the dependencies in JAR format, having a cleaner workspace and a simpler update process.
    This is a good opportunity to migrate. 


!!! failure
    Remember, Nexus will still be available until March 2024, so you have time to make this transition 🕑. We hope you find this guide useful.

If you encounter any issues or need additional help, do not hesitate to reach out to our [support service](http://support.etendo.software){target="_blank"}🚑.

