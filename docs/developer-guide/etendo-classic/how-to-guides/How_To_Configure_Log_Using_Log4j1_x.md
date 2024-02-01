---
tags: 
  - configuration
  - log
  - rotation
  - file
---


#  How To Configure Log Using Log4j1.x


##  Overview

Logging allows developers to insert messages when code is executed, these
messages can be used to understand different issues in the backend code, such
as errors, performance problems, etc.

!!!note
    Etendo uses  log4j  to log.

##  Configuration

Logging is configured by ` log4j.lcf ` file in Etendo's ` config `
directory.

###  File

Typically log is redirected to a file. This file is determined by
`log4j.appender.*.File` property. The defaults are:

    
    
    log4j.appender.R=org.apache.log4j.RollingFileAppender
    log4j.appender.R.File=${catalina.base}/logs/openbravo.log
    
    
    
    log4j.appender.HB=org.apache.log4j.RollingFileAppender
    log4j.appender.HB.File=${catalina.base}/logs/openbravo_hibernate.log
    

With this configuration, regular log will be placed in ` etendo.log ` file
in tomcat's log directory and log for hibernate will be in the same directory
in ` etendo_hibernate.log ` file.

###  Log Verbosity

Verbosity in the log is defined by the log levels:

ERROR WARN INFO DEBUG

The developer decides which is the level of each of the messages sent to the log.

It is possible to configure the log to display messages starting from any of
these levels. Default configuration shows INFO and above. Log level can be
configured globally and/or per class/package.

This can be modified in 2 ways:

  * In ` log4j.lcf ` , it requires to deploy the changes ( ` ant smartbuild ` ) and restart Tomcat after modifying. 
    * Globally: Change ` log4j.rootCategory= **INFO** ` to the desired level. 
    * Per Java class or package: add lines like ` log4j.category. _your.path.here_ =DEBUG ` where ` _your.path_ ` is the fully qualified class name or pacakage. 
  * At runtime. The change does not require Tomcat to be restarted to be effective, but after restarting its configuration will be read from ` log4j.lcf ` and changes will be lost. To do it, log in the application as System Administrator, open _Session Preferences_ window, click on _Change Logs_ button, select the class you want to modify the log level for, select log level and click on _Process_ button. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Configure_Log_Using_Log4j1_x-1.png){: .legacy-image-style}

##  Rotation

In order to prevent log file to constantly increase, rotation is defined.
Rotation sets up the policy to decide when log file will be archived and how
many archives will be maintained.

It is configured with the following properties:

    
    
     log4j.appender.R.MaxFileSize=10000KB
     log4j.appender.R.MaxBackupIndex=10
    

In this example, log file will have at most 10MB. When this size is reached,
current log is archived and a new log empty file is created, it will also keep
up to 10 files, so when a new archive is created, the oldest existing one will
be deleted.

This work is a derivative of [How To Configure Log Using Log4j1.x](http://wiki.openbravo.com/wiki/How_To_Configure_Log_Using_Log4j1.x){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.



