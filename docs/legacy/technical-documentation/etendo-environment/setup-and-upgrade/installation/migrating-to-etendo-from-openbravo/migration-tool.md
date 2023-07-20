---
title: Migration Tool
---
## Migration Tool

!!! warning
     **Important**: 
    This tool is not compatible with Windows operating system and the Oracle.

These are the steps to follow for the automatic migration from OpenbravoERP to EtendoERP: 


1. Configure Nexus Repository credentials. Create a file in `~/.gradle/gradle.properties`  with the following content:

!!! warning
    If the `.gradle` directory not exist you could create it with `mkdir ~/.gradle`

```plaintext
mavenUser=USER
mavenPassword=PASS
```

!!! warning
    Make sure to replace USER and PASS with your Nexus credentials.

2. Download the [latest version of migration tool](https://repo.futit.cloud/repository/static-public-releases/migration/cli/migration-cli/latest/migration-cli-latest.jar):

```plaintext

sudo wget https://repo.futit.cloud/repository/static-public-releases/migration/cli/migration-cli/latest/migration-cli-latest.jar -O migration-cli-latest.jar
```

3. Create installation folder

```
sudo mkdir -p /opt/EtendoERP/
```

4. Change directory to that folder:

```plaintext

cd /opt/EtendoERP
```

5. Execute migration tool:

!!! warning
    Replace `/path/to/migration/tool/` with the path where you downloaded the migration tool

```plaintext

java -jar /path/to/migration/tool/migration-cli-latest.jar run
```

6. Follow the tool steps:

> The migration tool will ask you to enter some information like the current folder where the Openbravo instance is located. Make sure to enter them correctly.  
!!! info
    After the data is entered and verified, the tool will automatically migrate your instance.


```plaintext

______ _                 _       ______ _____  _____
|  ____| |               | |     |  ____|  __ \|  __ \
| |__  | |_ ___ _ __   __| | ___ | |__  | |__) | |__) |
|  __| | __/ _ \ '_ \ / _` |/ _ \|  __| |  _  /|  ___/
| |____| ||  __/ | | | (_| | (_) | |____| | \ \| |
|______|\__\___|_| |_|\__,_|\___/|______|_|  \_\_|

Starting wizard ...
Requirements checklist

OpenbravoERP source folder [/opt/OpenbravoERP]:
...
```

7.  When this message appears, verify the tool has completed successfully:

```plaintext

The migration ends successfully.
Welcome to Etendo team !
```

!!! info
        The migration tool moves the following modules to `modules_core` folder:
        com.etendoerp.legacy.advpaymentmngt
        com.smf.jobs
        com.smf.jobs.defaults
        com.smf.mobile.utils
        com.smf.userinterface.skin.legacy
        com.smf.securewebservices
        com.smf.smartclient.boostedui
        com.smf.smartclient.debugtools
        org.openbravo.advpaymentmngt
        org.openbravo.apachejdbcconnectionpool
        org.openbravo.base.weld
        org.openbravo.client.application
        org.openbravo.client.htmlwidget
        org.openbravo.client.kernel
        org.openbravo.client.myob
        org.openbravo.client.querylist
        org.openbravo.client.widgets
        org.openbravo.financial.paymentreport
        org.openbravo.reports.ordersawaitingdelivery
        org.openbravo.service.datasource
        org.openbravo.service.integration.google
        org.openbravo.service.integration.openid
        org.openbravo.service.json
        org.openbravo.userinterface.selector
        org.openbravo.userinterface.skin.250to300Comp
        org.openbravo.userinterface.smartclient
        org.openbravo.utility.cleanup.log
        org.openbravo.v3
        org.openbravo.v3.datasets
        org.openbravo.v3.framework


### Migration Tool configuration flags

|Flag |  Description |
| --- | --- |
| --auto | Automagically run migration |
|-c --context-name=<contextName> | Name of the EtendoERP context name|
|--db-host=<dbHost>|    db host|
|--db-pass=<dbPass> |   db password|
|--db-port=<dbPort> |   db port|
|--db-system-pass=<dbSystemPass> |db password|
|--db-system-user=<dbSystemUser>| db user|
|--db-user=<dbUser>|    db user|
|-f  --openbravo-source-folder=<openbravoSourceFolder>| Path to Openbravo source code folder|
|-nd  --new-database=<newDatabaseName> |Name of the new database|
|-nl  --no-send-logs  | Do not send logs to the server|
|-np  --nexus-password=<nexusPassword> |Nexus password|
|-nu  --nexus-username=<nexusUsername> |Nexus username|
|-od  --openbravo-database=<oldDatabaseName> |Name of the existing OpenbravoERP database|
|-rb  --no-rollback   | Do not rollback|
|--server-url=<serverUrl> |Server URL|
|-st --stack trace |   Stack trace|
|-stc --skip-tomcat-check | Skip tomcat check in requirments check list|

  
!!! info
    Go back to the main migration page to continue with the [Post Migration Configuration](https://docs.etendo.software/en/technical-documentation/etendo-environment/setup-and-upgrade/installation/migrating-to-etendo-from-openbravo#post-migration-configuration) process.


