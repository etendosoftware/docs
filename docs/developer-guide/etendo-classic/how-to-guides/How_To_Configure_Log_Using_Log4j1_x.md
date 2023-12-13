![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  How To Configure Log Using Log4j1.x

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Starting from **PR19Q1** Openbravo uses  log4j2  for logging. If you're using
this version or newer, please refer to  How_To_Configure_Log  to configure log
using log4j 2.x.  
---|---  
  
##  Contents

  * 1  Introduction 
  * 2  Configuration 
    * 2.1  File 
    * 2.2  Log Verbosity 
  * 3  Rotation 

  
---  
  
##  Introduction

Logging allows developers to insert messages when code is executed, these
messages can be used to understand different issues in the backend code, such
as errors, performance problems, etc.

Openbravo uses  log4j  to log.

##  Configuration

Logging is configured by ` log4j.lcf ` file in Openbravo's ` config `
directory.

###  File

Typically log is redirected to a file. This file is determined by
log4j.appender.*.File property. The defaults are:

    
    
    log4j.appender.R=org.apache.log4j.RollingFileAppender
    log4j.appender.R.File=${catalina.base}/logs/openbravo.log
    
    
    
    log4j.appender.HB=org.apache.log4j.RollingFileAppender
    log4j.appender.HB.File=${catalina.base}/logs/openbravo_hibernate.log
    

With this configuration, regular log will be placed in ` openbravo.log ` file
in tomcat's log directory and log for hibernate will be in the same directory
in ` openbravo_hibernate.log ` file.

###  Log Verbosity

Verbosity in the log is defined by the log levels:

ERROR WARN INFO DEBUG

Developer decides which is the level of each of the messages sent to the log.

It is possible to configure the log to display messages starting from any of
these levels. Default configuration shows INFO and above. Log level can be
configured globally and/or per class/package.

This can be modified in 2 ways:

  * In ` log4j.lcf ` , it requires to deploy the changes ( ` ant smartbuild ` ) and restart Tomcat after modifying. 
    * Globally: Change ` log4j.rootCategory= **INFO** ` to the desired level. 
    * Per Java class or package: add lines like ` log4j.category. _your.path.here_ =DEBUG ` where ` _your.path_ ` is the fully qualified class name or pacakage. 
  * At runtime. The change doesn't require Tomcat to be restarted to be effective, but after restarting it configuration will be read from ` log4j.lcf ` and changes will be lost. To do it, log in the application as System Administrator, open _Session Preferences_ window, click on _Change Logs_ button, select the class you want to modify the log level for, select log level and click on _Process_ button. 

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

Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Configure_Log_Using_Log4j1.x  "

This page has been accessed 3,220 times. This page was last modified on 14
November 2018, at 09:44. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

