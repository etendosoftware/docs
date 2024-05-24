---
title: Migrating to Etendo (from Openbravo)
---
## Overview

This guide provides the necessary information to migrate an existing Openbravo instance to a new Etendo instance (in its latest release). 

### Requirements

Before the migration process begins, either if it is done on Linux or on Windows, make sure to have the following items:

!!! info
    - Current Openbravo instance updated to 21Q3.2 ([How to upgrade?](../../../../developer-guide/etendo-classic/getting-started/migration-from-openbravo/upgrading-to-openbravo-21q3-2.md))
    - If previous installation had custom patches applied, they must be ready to be applied in an 21Q3.2 updated environment.
    - Database should not have local changes.
    - Enough disk space for new installation.
    - Environment license and GitHub name and token (Create the credentials by following this [guide](../../../../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md)).

!!! warning
    - The server where the database is hosted needs to have enough free space to hold a copy of the current database.  
    - The server where the sources are hosted also needs to be able to hold a copy of the current sources.  
    - Attachments are kept in the same place as they were before.



## Instructions for the Migration Process

### Before starting the migration
It is necessary to ensure following the next steps:

1.  Stop the Tomcat Server.

    ``` bash title="Terminal" 

    sudo /etc/init.d/tomcat stop
    ```

    !!! info
        Depending on your server, this command may need to be changed.


2. Create a backup of your instance.


### Manual Migration Process

These are the steps to follow for the manual migration from OpenbravoERP to Etendo Classic:

1. Create and enter the folder Etendo Classic.

2. Insert the **etendo_base** sources in the Etendo Classic folder. They can be extracted after downloading Etendo from [Resources](https://etendo.software/es/recursos){target="_blank"}. To do this, use your gitHub user and token.

3. The `gradle.properties` file has default params but if needed this can be changed.  

    ???+Note
        Remember to set up the GitHub user and token since they are used to expand private modules. Create the credentials by following the [Use of Repositories technical guide](../../../../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
        

    ``` groovy title="gradle.properties"
    githubUser=
    githubToken=

    context.name=etendo

    bbdd.sid=etendo
    bbdd.port=5432
    bbdd.systemUser=postgres
    bbdd.systemPassword=syspass
    bbdd.user=tad
    bbdd.password=tad
    ```

    !!! info
        Check if it is necessary to keep the Openbravo database or create a new one for Etendo. In case of creating a new one, use the previous Openbravo one as a base.



4. In a new terminal opened in `EtendoERP` folder, run in the 
    ``` bash title="Terminal" 
    ./gradlew expandCore
    ```
5. Run in the terminal 
    ``` bash title="Terminal"
    ./gradlew setup
    ```
6. Move the existing modules from `Openbravo/modules` folder to the `EtendoERP/modules` folder, except for the following ones:

    !!! warning
        com.smf.securewebservices<br>
        com.smf.smartclient.boostedui<br>
        com.smf.smartclient.debugtools<br>
        org.openbravo.advpaymentmngt<br>
        org.openbravo.apachejdbcconnectionpool<br>
        org.openbravo.base.weld<br>
        org.openbravo.client.application<br>
        org.openbravo.client.htmlwidget<br>
        org.openbravo.client.kernel<br>
        org.openbravo.client.myob<br>
        org.openbravo.client.querylist<br>
        org.openbravo.client.widgets<br>
        org.openbravo.financial.paymentreport<br>
        org.openbravo.reports.ordersawaitingdelivery<br>
        org.openbravo.service.datasource<br>
        org.openbravo.service.integration.google<br>
        org.openbravo.service.integration.openid<br>
        org.openbravo.service.json<br>
        org.openbravo.userinterface.selector<br>
        org.openbravo.userinterface.skin.250to300Comp<br>
        org.openbravo.userinterface.smartclient<br>
        org.openbravo.utility.cleanup.log<br>
        org.openbravo.v3<br>
        org.openbravo.v3.datasets<br>
        org.openbravo.v3.framework<br>

        
        These modules will already be in the `EtendoERP/modules_core` folder since they are core modules in Etendo. 

7. Run
    ``` bash title="Terminal" 
    ./gradlew update.database compile.complete.deploy --info
    ```
!!! info
    Compilation errors associated with API changes may occur due to the version change in custom modules. If this happens, make sure to fix them by using the [documented GitHub issues](https://github.com/etendosoftware/etendo_core/issues?q=is%3Aissue+){target="_blank"}. 



## Post Migration Configuration

### Remove previous instance deployed context

``` bash title="Terminal"
rm -r /var/lib/tomcat/webapps/openbravo
```
!!! warning
    Make sure this step is done before starting Tomcat, otherwise you will risk having two environments running at the same time, which can cause problems (especially when background processes are involved).


### Start Tomcat

!!! info
    Depending on your server, this command may need to be changed.

  
``` bash title="Terminal" 

sudo /etc/init.d/tomcat start
```



### Attachments Configuration

!!! warning
    Before removing your previous instance, make sure you migrate your attachment files.


In the migration process, the attachments directory configuration is not changed. To move them to a new folder (for example `/opt/EtendoERP/attachments`), you must edit the `Openbravo.properties` file:

``` bash title="Terminal" 
vi /opt/EtendoERP/config/Openbravo.properties
## Change the attach.path property like this (do not include the #):
## attach.path=/opt/EtendoERP/attachments
```

 and move the attachments manually: 

``` bash title="Terminal" 
mv /opt/OpenbravoERP/attachments /opt/EtendoERP/attachments
## Deploy changes to tomcat
./gradlew smartbuild
```
!!! info
    Special consideration may have to be taken into account if your attachment folder is in a network drive, or a different partition (with or without a symbolic link in place).  
    Be careful when changing the attachment configuration, and make sure you have a recent backup available.


### Customizations to Core

Reapply patches to core if necessary, and compile.

!!! info
    Compilation tasks now can be made with the Gradle Wrapper.


``` bash title="Terminal" 

patch -p1 < customPatchToCore.patch
## Apply other patches as needed
./gradlew smartbuild
sudo /etc/init.d/tomcat restart
```

### Apache Configuration

1.  If necessary, change apache configuration to use jkmount in the correct context ("openbravo" by default in old installation).  
    Configuration file should be in `/etc/apache2/conf-enabled/openbravo.conf`, `/etc/apache2/conf-available/openbravo.conf`or `/etc/apache2/sites-available/000-default.conf` / `/etc/apache2/sites-available/000-default-le-ssl.conf`<br>
    Replace `jkMount /openbravo* ajp13_worker` by `jkMount /etendo* ajp13_worker`
    
2.  Change apache configuration to redirect to new context ("openbravo" by default in old installation).  
        Configuration file should be in `/var/www/html/index.html`.  
        Replace `<META HTTP-EQUIV="Refresh" CONTENT="0; URL=openbravo">` by `<META HTTP-EQUIV="Refresh" CONTENT="0; URL=etendo"> `  
        
    !!! warning
        Make sure to replace  by the context you chose when in the `gradle.properties`file.


3.  Restart apache:
    

``` bash title="Terminal" 

sudo service apache2 restart
```

### Activate your instance

1.  Login as System Administrator and use the Instance Activation window to activate your instance.
2.  Use Refresh Online
3.  Enter your instance purpose and your activation key.

!!! success
    Your instance is activated!


### Change backup and restore script

1.  Make sure that the backup script now obtains its data from the correct `Openbravo.properties`, for example in folder `/opt/EtendoERP/`  
        The backup script is usually located in `/usr/share/openbravo/backup/backup`. You should change the lines to point to the actual `Openbravo.properties` file. For example:
        

    ```bash title="Terminal"

    db_login=$(awk -F = '/^bbdd.user/ {print $2}' /opt/OpenbravoERP/config/Openbravo.properties)
    ```

    Should be changed for something like this:

    ```bash title="Terminal"

    db_login=$(awk -F = '/^bbdd.user/ {print $2}' /opt/EtendoERP/config/Openbravo.properties)
    ```

    This will vary depending on the path that has been selected for the migration.

    !!! warning
        Remember that in the current state `Openbravo.properties` does not change its name. This should not be changed until further notice from the development team. Also, you must not change the Openbravo name anywhere else. Do it only in the paths for the properties file.


    !!! info
        A dedicated backup tool is in development.


2.  The same should be done for `/usr/bin/openbravo-restore`. Given that the scripts are highly hardcoded, you have to change some lines manually.

The database to be dropped should be the Etendo database, but the script will drop the openbravo db. This should be changed to drop the Etendo database. 

- Change:

    ```bash

    su - postgres -c "psql -U postgres -c "drop database openbravo"" || true
    ```

    for:
    ```bash

    su - postgres -c "psql -U postgres -c "drop database etendo"" || true

    ```

- Change the line that creates the database:

    ```bash

    su - postgres -c "psql -U postgres -c "create database openbravo WITH ENCODING='UTF8' OWNER=TAD;""

    ```

    for

    ```bash

    su - postgres -c "psql -U postgres -c "create database etendo WITH ENCODING='UTF8' OWNER=TAD;""

    ```

- Change the target database on the lines that the pg\_restore is done, for example:

    ```bash

    PGPASSWORD=tad pg_restore -U tad -h localhost -d openbravo -O $TEMP_FOLDER/db_backup.dmp || true

    ```

    for

    ```bash

    PGPASSWORD=tad pg_restore -U tad -h localhost -d etendo -O $TEMP_FOLDER/db_backup.dmp || true

    ```

- Change the line which erases the tomcat files:

    ```bash

    rm -rf /var/lib/tomcat/webapps/openbravo || true

    ```

    for

    ```bash

    rm -rf /var/lib/tomcat/webapps/etendo || true

    ```

- Change the path of the sources for the new path created for Etendo, for example:

    ```bash

    sudo chown openbravo:openbravo /opt/OpenbravoERP/

    ```

    for

    ```bash

    sudo chown openbravo:openbravo /opt/EtendoERP/

    ```
!!! warning
    The same warning for the backups applies here. Be careful with what you rename. If you see an error, please ask for support.


### Change initial directory on login

Inside `~/.bashrc` you may have a command that lets you log in directly to the `/opt/OpenbravoERP` folder. Change it so it points to your new instance folder:

``` bash title=".bashrc" 

## Change
cd /opt/Openbravo
## To
cd /opt/EtendoERP
```

### Change server user

You may change the current user from Openbravo to Etendo, if you want. This guide does not cover how to do so.

### Remove previous installation

1.  Remove Openbravo context from Tomcat folder:

    ``` bash title="Terminal"

    rm -r /var/lib/tomcat/webapps/openbravo
    ```

2.  Remove Openbravo installation:

    ``` bash title="Terminal"

    rm -r /opt/OpenbravoERP
    ```

3.  Remove Openbravo database:

    ``` bash title="Terminal"

    psql -h localhost -U postgres -d etendo -c "DROP DATABASE openbravo;"
    ```
!!! warning
    Make sure above commands are pointing to the correct databases, user and host, and that you have done a backup before executing the command.

### Apply 303 Taxes and Tax Report Fixes

This step is only necessary if the following conditions happen in your environment:

* The `org.openbravo.module.aeat303.temporal.taxes.es`, `org.openbravo.module.aeat303.temporal.taxparameters.es`, `org.openbravo.localization.spain.referencedata.taxes.es` and `org.openbravo.module.aeat303.es` modules are installed and their datasets applied in the ERP
* You want to update the `Spain Localization Extensions` bundle to version `1.8.0` or higher, otherwise, you want to update the afforementioned modules to these versions:
    * `org.openbravo.localization.spain.referencedata.taxes.es`: version `1.8.0` or higher
    * `org.openbravo.module.aeat303.es`: version `1.14.0` or higher

To solve issues with taxes arising from these modules being migrated from Openbravo to Etendo, refer to the related [Known Issue](../../../../whats-new/release-notes/etendo-classic/known-issues.md/#ee-808-problem-when-trying-to-import-the-taxes-configuration-for-spain-dataset-if-the-environment-already-has-imported-the-dataset-related-to-the-303-temporary-taxes-of-openbravo) 

### Apply 390 Taxes and Tax Report Fixes

This step is only necessary if the following conditions happen in your environment:

* The `org.openbravo.module.aeat303.temporal.taxes.es`, `org.openbravo.module.aeat303.temporal.taxparameters.es`, `org.openbravo.localization.spain.referencedata.taxes.es` and `org.openbravo.module.aeat390.es` modules are installed and their datasets applied in the ERP
* You want to update the `Spain Localization Extensions` bundle to version `1.8.0` or higher, otherwise, you want to update the afforementioned modules to these versions:
    * `org.openbravo.localization.spain.referencedata.taxes.es`: version `1.8.0` or higher
    * `org.openbravo.module.aeat390.es`: version `3.9.0` or higher

To solve issues with taxes arising from these modules being migrated from Openbravo to Etendo, refer to the related [Known Issue](../../../../whats-new/release-notes/etendo-classic/known-issues.md/#ee-856-390-tax-report-dataset-duplicates-data-for-2022-when-applied-on-a-server-migrated-from-ob-to-etendo-after-01-2023) 

## Conclusion

!!! info
    With these steps, you should have successfully migrated your Openbravo data to Etendo either on a Linux system or on a Windows system. If you encounter any problems during the process, please reach out to the [Etendo support team](https://etendoproject.atlassian.net/servicedesk/customer/portals){target="_blank"} for assistance.