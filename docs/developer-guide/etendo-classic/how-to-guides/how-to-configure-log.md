---
title: How to Configure Log
tags:
  - Logging configuration 
  - Etendo backend debugging 
  - Log rotation
  - Verbosity 

status: beta

---

#  How to Configure Log
 
!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

Logging allows developers  to **insert messages** when code is executed, these messages can be used to understand different issues in the backend code, such as errors, performance problems, etc.

##  Configuration

Logging is configured using 3 log configuration files, depending on the scenario:

  * ` config/log4j2.xml `: Is the configuration for build tasks, both from the command line and the rebuild launched from the **Module Management** Window. 
  * ` config/log4j2-web.xml `: This configuration is used for the Web Application executed from a container such as Tomcat. 
  * ` src-test/src/log4j2-test.xml `: This configuration is used for JUnit tests and suites. 

###  File

Typically log is redirected to a file. This file is determined by the `<RollingFile> ` tag inside the ` <Appenders> ` section. The defaults are:

    
    
    <RollingFile name="RollingFile" fileName="${logDir}/openbravo.log"
                 filePattern="${logDir}/openbravo-%d{yyyyMMdd}-%i.log.gz">
    <PatternLayout pattern="%d [%t] %-5p %c - %m%n"/>
      <Policies>
        <TimeBasedTriggeringPolicy />
        <SizeBasedTriggeringPolicy size="100MB" />
      </Policies>
      <DefaultRolloverStrategy max="30"/>
    </RollingFile>

With this configuration, regular log will be placed in ` openbravo.log ` file in tomcat's log directory. ????

###  Log Verbosity

Verbosity in the log is defined by the log levels:

ALL TRACE DEBUG INFO WARN ERROR FATAL OFF

Developer decides which is the level of each of the messages sent to the log.

It is possible to configure the log to display messages starting from any of these levels. Default configuration shows INFO and above. Log level can be configured **globally** and/or **per class/package**.

This can be modified in 2 ways:

  * In ` log4j2*.xml `, it requires to deploy the changes ( ` ant smartbuild ` ) and restart Tomcat after modifying. 
    * Globally: Change the Root Logger level to the one desired: 

    
    
    <Loggers>
      <!-- Setting default log level as debug -->
      <Root level="debug">
      ...
      </Root>
      ...
    </Loggers>

  *     * Per Java class or package: add lines in the ` <Loggers> ` section like: 

    
    
    <Loggers>
      ...
      <!-- Setting your.path.here logger to debug level -->
      <!-- your.path.here can refer either to a class or a package fully qualified name -->
      <Logger name="your.path.here" level="debug"/>
      ...
    </Loggers>

!!!note
    This logger will inherit the appenders used by the parent logger (Root in most cases). If you want to change this behavior, add the ` additivity ` attribute and set it to false. 

!!!info
    For more information visit, [Log4j2 documentation](https://logging.apache.org/log4j/2.x/manual/configuration.html#Additivity){target="\_blank"}. 
 
  
  * At runtime. The change does not require Tomcat to be restarted to be effective, but after restarting it configuration will be read from ` log4j2-web.xml ` and changes will be lost. To do it, log in the application as **System Administrator**, go to `General Setup > Application > Log Management`. There sort, filter and select one or multiple loggers, select the desired log level and apply the changes by tapping the **Apply** button. 


![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/How-to-configure-log1.png)


##  Rotation

In order to prevent log file to constantly increase, **rotation** is defined. Rotation sets up the policy to decide when log file will be archived and how many archives will be maintained.

It is configured with the following properties in ` <RollingFile> ` section:

    
    
    <Policies>
      <SizeBasedTriggeringPolicy size="100MB" />
      <TimeBasedTriggeringPolicy />
    </Policies>
    <DefaultRolloverStrategy max="30">
      <Delete basePath="${logDir}">
        <IfFileName glob="openbravo-*.log.gz">
          <IfAccumulatedFileCount exceeds="30"/>
        </IfFileName>
      </Delete>
    </DefaultRolloverStrategy>

By default, log file is limited to **100MB size** and will be archived and compressed daily and/or when log exceeds 100MB. The number of log files archived is limited to 30 and when exceeded the older one will be removed.


##  Upgrade from previous versions

In order to fully support **log4j2** when migrating from an older version, the following steps should be taken:

  * Create new config files from the templates provided. There is a **Build Validation** class that creates them automatically, but if no build validation is executed, the following command can be used: 

    
    
    `ant setup -DnonInteractive=yes -DacceptLicense=yes`

  * After this step, the following files should be available: 
    * `config/log4j2.xml` 
    * `config/log4j2-web.xml` 
    * `src-test/src/log4j2-test.xml` 

  * Adjust the new config files according to your needs. 

  * Remove old configuration. Remove `config/log4j.lcf`. 

!!!info
    If using Java 11, add an option to `ANT_OPTS` in order to build Etendo.
 


This work is a derivative of [How to Configure Log](http://wiki.openbravo.com/wiki/How_To_Configure_Log){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 

