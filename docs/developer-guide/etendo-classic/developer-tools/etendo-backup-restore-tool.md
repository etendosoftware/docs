---
title: Etendo Backup and Restore Tool
tags: 
  - Etendo Classic
  - Plugin
  - Gradle
  - Backup
  - Restore
---

## Overview

This article explains how to use the Etendo Backup and Restore plugin in Etendo Classic. This plugin allows you to easily generate and restore Etendo backups.

## Install plugin

To use the Etendo Backup and Restore tool, you should add the plugin id on the `build.gradle` file, with the selected version.

``` groovy  title="build.gradle"
plugins {
    id 'com.etendoerp.etendobackup' version "<version>"
}
```

!!! info
    To know the available versions of the plugin, please visit [Etendo Backup and Restore Plugin | Release Notes](../../../whats-new/release-notes/etendo-classic/plugins/etendo-backup-restore-plugin/release-notes.md).

To resolve the plugin dependiencies, you should add the following lines on top of the `settings.gradle` file

``` groovy  title="settings.gradle"
pluginManagement {
    repositories {
        maven {
            url 'https://maven.pkg.github.com/etendosoftware/com.etendoerp.etendobackup'
            credentials {
                username "${githubUser}"
                password "${githubToken}"
            }
        }
        maven {
            url "https://repo.futit.cloud/repository/static-public-snapshots"
        }
        mavenCentral()
    }
}
```

!!! warning
    Make sure you have your Github credentials (`githubUser` and `githubToken`) set in the `gradle.properties` file.

## Backup task

!!! warning
    The User running the backup must have `SUDO` access and the `backup.properties` file properly configured.


To run the backup, execute

``` bash title="Terminal"
./gradlew backup -PbkpMode=<mode>
```

Where the mode could be `manual` or `auto`

### Backup properties file

The `backup.properties` file is found inside the `config` folder on the root project.
If it does not exists, run `./gradlew setup` to generate the missing files.

You can also provide a custom location of `backup.properties` adding the next block inside `build.gradle`.
``` groovy title="build.gradle"
backup {
    configPath = "/path/to/backup.properties"
}
```

`backup.properties` contains most of the properties that you should customize before running the backup.

* `USER`
Sets the user who will be running the backup.

* `GROUP`
Sets the group related to the user running the backup.

* `BACKUPS_DIR`
Sets the path where the backup will be stored.

* `BACKUPS_TMP_DIR`
Sets the path where the temp directory will be created to store the generated files.

* `ATTACH_COPY`
Sets a flag (`yes` or `no`) if the external attachments (if cointained) should be included in the backup.

* `ATTACH_IN_BKP`
Sets a flag (`yes` or `no`) if the source attachments should be included in the backup.

#### Email properties

These properties are used when the backup is running in `auto` mode.

* `EMAIL_FROM`
Sets the address sending emails.
* `EMAIL_SERVER`
Sets the email server address.
* `EMAIL_PORT`
Sets the port for the email server..
* `EMAIL_USER`
Sets the user address who sends emails.
* `EMAIL_PASSWORD`
Sets the email user password.
* `EMAIL_ENVIRONMENT`
Specifies the environment for sending emails.

Depending on the end `STATE`, the following properties are used to specify the email address where to send emails.

!!! failure "Error" 
    * `EMAIL_ERROR_TO`
      Sets the email address where error emails will be sent.
    * `EMAIL_ERROR_CC`
      Sets the email address to which copies (CC) will be sent in case of error.
    * `EMAIL_ERROR_SUBJECT`
      Sets the subject of the error email.

!!! warning 
    * `SEND_EMAIL_ON_WARNING`
      Specifies whether to send an email notification in case of warning during the backup process. Accepted values are `yes` or `no`.
    * `EMAIL_WARNING_TO`
      Sets the email address where warning emails will be sent.
    * `EMAIL_WARNING_CC`
      Sets the email address to which copies (CC) will be sent in case of warning.
    * `EMAIL_WARNING_SUBJECT`
      Sets the subject of the warning email.

!!! success 
    * `SEND_EMAIL_ON_SUCCESS`
      Specifies whether to send an email notification in case of success during the backup process. Accepted values are `yes` or `no`.
    * `EMAIL_WARNING_TO`
      Sets the email address where success emails will be sent.
    * `EMAIL_WARNING_CC`
      Sets the email address to which copies (CC) will be sent in case of success.
    * `EMAIL_WARNING_SUBJECT`
      Sets the subject of the success email.

!!! note
    In order to send the email to multiple accounts, separate addresses with `;`.<br>
    For example: `EMAIL_ERROR_CC=user1@smfconsulting.es;user2@smfconsulting.es`

### End states
The following are the possible states at the end of the `backup` task:

!!! failure "Error" 
    Occurs when the creation of the backup fails. An email must be sent to the specified properties.

!!! warning
    The backup ends with warning messages. If the `SEND_EMAIL_ON_WARNING` flag is set to yes, an email should be sent to the specified properties.

!!! success
    The backup ends without warning or errors. If the `SEND_EMAIL_ON_SUCCESS` flag is set to yes, an email should be sent to the specified properties.

## Restore task

!!! warning
    The user running the restore should have `SUDO` access.

To run the restore, execute

``` bash title="Terminal"
./gradlew restore -PbackupPath=/path/to/backup
```

Replace `/path/to/backup/` with the location of the backup to be restored.

A menu will be shown where you can choose multiple options to be performed.

!!! warning
    Make sure all the options selected are correct. The selected destination directories and database will be OVERWRITTEN.

1. *User verification*<br>
  You should run the restore with `SUDO` access (recommended). In case of not having permissions, you will have the option of inserting the `SUDO` password.

2. *Sources destination*<br>
  You can select the location in which the sources will be restored. The default path is set to the root dir from the project where the restore command is being executed.

3. *Attachments verification*<br>
  You can select to keep or ignore the copy of attachments (externals or contained inside the sources).

4. *Properties verification*<br>
  You can select which properties to use.

    !!! info
        The properties set the options which the database will use on the restore.

    - *Project properties*<br>
      Obtained from the `gradle.properties` file inside the current project running the restore. 
      You can change these properties to select, for example, the name of the database to be restored.
      Once the restore is done, the properties inside `config/Openbravo.properties` will be updated with the selected ones.

    - *Original sources properties*<br>
      Obtained from the `gradle.properties` file inside the original sources.
      The database will be restored with the original options (this could overwrite an existing database)
      The properties inside `config/Openbravo.properties` will not change.

5. *Database properties*<br>
  In the end, a message will be shown with the properties which the database will use to be restored. These properties depend on the ones selected previously.




