---
title: Etendo Backup and Restore Tool
---

## Resolving the plugin

To use the Etendo Backup and Restore tool, you should add the **plugin id** on the `build.gradle` file, with the selected version.

``` groovy
plugins {
    id 'com.etendoerp.etendobackup' version "1.0.0"
}
```

To resolve the plugin dependiencies, you should add the following lines on top of the `settings.gradle` file

``` groovy
pluginManagement {
    repositories {
        maven {
            url "https://repo.futit.cloud/repository/static-public-releases"
        }
        maven {
            url "https://repo.futit.cloud/repository/static-public-snapshots"
        }
        mavenCentral()
    }
}
```

### Backup task

!!! warning
    The User running the backup must have SUDO access and the `backup.properties` file properly configured.


To run the backup, execute

`./gradlew backup -PbkpMode=<mode>`

Where the mode could be `manual` or `auto`


## Backup properties file

The `backup.properties` file is found inside the `config` folder on the root project.
If it does not exists, run `./gradlew setup` to generate the missing files.

You can also provide a custom location of `backup.properties` adding the next block inside `build.gradle`.
``` groovy
backup {
    configPath = "/path/to/backup.properties"
}
```

`backup.properties` contains most of the properties that you should customize before running the backup.

* USER 
Sets the **user** who will be running the backup.

* GROUP
Sets the **group** related to the user running the backup.

* BACKUPS_DIR
Sets the path where the **backup** will be stored.

* BACKUPS_TMP_DIR
Sets the path where the **temp directory** will be created to store the generated files.

* ATTACH_COPY
Sets a flag (**yes** or **no**) if the **external attachments** (if cointained) should be included in the backup.

* ATTACH_IN_BKP
Sets a flag (**yes** or **no**) if the **source attachments** should be included in the backup.

<br>

### Email properties

These properties are used when the backup is running in `auto` mode.

* EMAIL_FROM
Sets the **address** sending emails.
* EMAIL_USER
Sets the **user address** who sends emails.
* EMAIL_PASSWORD
Sets the email user **password**.

A backup could finalize in 3 **STATES**: `ERROR - WARNING - SUCCESS`

Depending on the finish **STATE**, the next properties are used to specify the email address where to send emails.

* EMAIL_*STATE*_TO
Sets the **email address** where to send emails.

* EMAIL_*STATE*_CC
Sets multiple **email address** (separated with `;`) which will receive the email
`Ex:EMAIL_ERROR_CC=user1@etendo.software;user2@etendo.software`

* EMAIL_*STATE*_SUBJECT
Sets the **subject** of the email.


### Finalized states
* ERROR
Occurs when the creation of the backup fails. An email **must** be sent to the specified properties.

* WARNING
The backup finalizes with **WARNING** messages. If the **SEND_EMAIL_ON_WARNING** flag is set to **yes** an email should be send to the specified properties.

* SUCCESS
The backup finalizes without warning or errors. If the **SEND_EMAIL_ON_SUCCESS** flag is set to **yes** an email should be sent to the specified properties.

<br>

## Restore task

!!! warning
    The user running the **restore** should have SUDO access

To run the restore, execute

`./gradlew restore -PbackupPath=/path/to/backup`

Replace `/path/to/backup/` with the location of the backup to be restored.

A menu will be shown where you can choose multiple options to be performed.

!!! failure
    Make sure all the options selected are correct. The selected **destination directories** and **database** will be **OVERWRITTEN**.


1. **User verification**
You should run the restore with SUDO access **(recommended)**. In case of not having permissions, you will have the option of inserting the SUDO password.
<br>
2. **Sources destination**
You can select the location in which the **sources** will be restored. The default path is set to the root dir from the project where the restore command is being executed.
<br>
3. **Attachments verification**
You can select to keep or ignore the copy of **attachments** (externals or contained inside the sources)
<br>
4. **Properties verification**
You can select which properties to use.

!!! info
    The properties set the options which the database will use on the restore.

- Project properties 
Obtained from the `gradle.properties` file inside the **current project** running the restore. 
You can **change** these properties to select, for example, the name of the database to be restored.
Once the restore is done, the properties inside `config/Openbravo.properties` will be **updated** with the selected ones.
<br>
- Original sources properties
Obtained from the `gradle.properties` file inside the **original sources**.
The database will be restored with the original options (this could **overwrite** an existing database)
The properties inside `config/Openbravo.properties` will **not change**.

5. **Database properties**
In the end, a message will be shown with the properties which the database will use to be restored. These properties depend on the ones selected previously.




