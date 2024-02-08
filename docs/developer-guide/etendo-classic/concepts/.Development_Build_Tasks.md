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

  

#  Development Build Tasks

##  Contents

  * 1  Introduction 
  * 2  Main Build Tasks 
    * 2.1  Initial installation 
    * 2.2  Build 
    * 2.3  Database export 
    * 2.4  Update database 
    * 2.5  Validate Module 
    * 2.6  Module Consistency Check 
    * 2.7  Test Ant Tasks 
  * 3  Detailed Build Tasks 
    * 3.1  Libraries build tasks 
    * 3.2  Build tasks 
    * 3.3  Database tasks 
    * 3.4  Modules 
    * 3.5  Test Tasks 
    * 3.6  Other Tasks 

  
---  
  
##  Introduction

This document discusses the ant tasks used during the build process of
Openbravo ERP. It explains what the ant tasks are used for and which
properties can be used to control their behavior. Notice that ant is case
sensitive.

##  Main Build Tasks

![](/assets/developer-guide/etendo-
classic/concepts/Development_Build_Tasks-0.png){: .legacy-image-style}

This section explains the main build tasks following the steps as illustrated
in the image.

In most of the cases it is only necessary to use 3 tasks ( _install.source_ ,
_smartbuild_ and _export.database_ ). There are a number of other tasks that
can be used but they are not required for the standard process, they are
explained in the  Detailed Build Tasks  section.

The main task for the standard process is **smartbuild** which performs all
the required processes as explained below. This task accepts an optional
property:

  1. _local_ for local or remote developments which by default is set to **yes** . 

The difference between _local_ and _remote_ development is illustrated in the
diagram on the right. Local development are changes by the developer
him/herself. Remote developments are changes done by other developers. Changes
by remote developments are pulled from the source code revision system.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  _remote_
means that you're bringing changes to your workspace from an external
location, e.g. with a  hg pull  
---|---  
  
###  Initial installation

After downloading the Openbravo ERP source files (for example with an hg clone
from mercurial). It is necessary to install and deploy it.

The first step is to properly configure all the required configuration files
(Openbravo.properties, log4j.lcf, Eclipse's .classpath, etc). All properties
are stored in the _ Openbravo.properties  _ file. This file is not in the base
source but it can be easily generated from the _Openbravo.properties.template_
. Another way to set up it is to execute the setup tool for the current
platform. (run ant setup).

**Note:** More about the properties and setup ant task can be found at
Openbravo.properties  .

After all the properties are configured the following step is to build the
application from scratch and to deploy it. All this is done by the
**install.source** task. This task creates the database, inserts sample data
on it and compiles and deploys the application accordingly with the chosen
deployment mode  . To execute it just type in the Openbravo ERP source
directory:

    
    
    ant install.source

Once Openbravo ERP is up and running it is possible to develop on it.
Generally, new developments should be done through modules, further
explanations about how to develop modules can be found in the  Modularity
article  .

###  Build

Once the developments are ready to be tested it is necessary to build the
application. It is not necessary to do a complete build, but just incremental
builds, that is building only what has been modified. This is done with the
**smartbuild** command:

    
    
    ant smartbuild

This task generates and compiles the sources for the modified elements, and,
depending on the deploy mode, it also deploys them.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |
Available from **3.0PR17Q1**  
---|---  
  
To build Openbravo to be deployed on Wildfly,  **application.server** property
needs to be set with value ` wildfly ` .

###  Database export

In most cases developments include modifications on the database. This
modifications can be persisted in xml files using the  DBSourceManager  tool.
DBSourceManager exports to xml files only the modules (including core) that
are set as _In Development_ . To export the database execute:

    
    
    ant export.database

After this step the changed model xml files can be pushed/committed to the
source code revision system, so that other developers can pick them up and
continue working on top of it.

When a module is exported using the _export.database_ task it is first
validated to check for common errors. If the validation fails then the
_export.database_ task will also fail and export is not possible.

The following checks are currently done:

  * A table defined in the Application Dictionary should be present in the database and vice versa. 
  * Column definitions in the database and the Application Dictionary are compared, any mismatch is reported. The column datatype, default value and length are checked. 
  * Tables should have a primary key. 
  * Foreign key fields should be part of a foreign key constraint. 
  * Names of tables, columns and constraints are checked for their length (Oracle has a 30 character limit there). 

  

###  Update database

Database model changes are distributed by committing the database schema as
xml to SCM. Other developers pull the changes from SCM and can apply them to
update their own database. After updating the database the process is exactly
the same as the local one, that is compile and deploy the elements that have
been modified since last build. All the required actions (update database,
compile last modifications and deploy them) can be done with only the
**smartbuild** command:

    
    
    ant smartbuild -Dlocal=no # note the -Dlocal=no 

The only difference with the local development is in the _local_ parameter
which makes the process to update the database in case the xml files were
changed.

###  Validate Module

When a module is packaged with the _package.module_ ant task, then first it is
checked for some common errors. If an error is detected then the
_package.module_ task will fail.

Specifically the following checks are done:

  * A module should depend on the Core module, or depend on a module which depends on the Core module (recursively). 
  * The path in side the _modules/.../src_ directory must correspond to the javapackage defined for the module. 
  * The javapackages of the DataPackages which are part of the module must be in line with the Java package defined for the module. So if the module has the javapackage org.example, then all Data Packages should have a Java package which starts with org.example. 
  * The license type and text must be set. 
  * If the module is an Industry Template then it must depend on core and the dependency must be set to 'Included'. 
  * If the module adds UI artifacts such as a window or tab then its 'translation required' field must be set to yes. 

###  Module Consistency Check

An instance is consistent in case the dependencies all the modules it has
installed are satisfied. Development instances can define inconsistencies (for
example by creating a dependency on a module version which is not installed)
whereas production instances where all the modules are installed through obx
or Central Repository shouldn't be inconsistent because it is guaranteed by
the installation process.

Inconsistent instances can be in a situation where it is not possible to
update any of the modules (including core) they have installed. This is due
the fact that Central Repository only proposes updates to consistent sets of
versions and it is possible the inconsistency cannot be resolved by any.

This ant task helps to detect which are the modules that cause this
inconsitency and which are the dependencies that are not satisfied, in this
way it makes easier to solve the problem.

    
    
    ant check.module.consistency

###  Test Ant Tasks

Openbravo has a number of ant tasks for running Junit test cases. The main one
is run.tests:

    
    
    ant run.tests

It will run the tests which are side effect free. The test ant tasks assume
that the Small Bazaar and Accounting Test clients have been installed.

##  Detailed Build Tasks

This section contains a detailed listing of all available build tasks.

###  Libraries build tasks

Task  |  Description  |  Notes

  
  
  
---|---|---  
core.lib  |  Compiles and generates a .jar file from the src-core project.
Which is needed by wad.lib and the rest of build tasks.  |  **Required by** :
wad.lib

  
  
  
wad.lib  |  Compiles and generates a .jar file from the src-wad project. Which
is needed by the build tasks. This project contains the WAD, the automatic
window generator.  |  **Requires** : core.lib, database created

**Required by** : compile.*  
  
trl.lib  |  Compiles and generates a .jar file from the src-trl project. Which
is needed by the translate task. This project allows to translate to different
languages manual windows.  |  **Requires** : core.lib  
  
###  Build tasks

Task  |  Description  |  Notes  |  Sub Tasks  
---|---|---|---  
smartbuild  |  Makes an incremental build of the application. Including:

  * update.database 
  * compile 
  * deploy 

All these tasks are done only if needed.

|  **Requires** :

Database must be created and populated with data.

**Properties** :

  * **local:** (default to yes) when this property is set to no _update.database_ task is executed, otherwise it is not executed. 
  * **tr:** (default to yes) if set to no, translation process is not executed. 
  * **force:** (default to no) used with local=no. If set to yes it will overwrite the changes in the database with the XML information. Note: All un-exported changes will be lost. 
  * **wad.generateAllClassic250Windows:** (default to false) when it is true, it forces WAD to generate code for all 2.50 style windows. 

|  
generate.entities  |  Generates the Java files for src-gen directory, and
compiles them. They are used by DAL to access to the database information.  |
**Requires** :

Database must be created and populated with data.

|  
install.source  |  Installs the whole application: creates the database,
compiles it and generates a war file to be deployed or copies the classes to
Tomcat's directory (depending on the deploy.mode property set in
Openbravo.properties).  |  **Calls** :

create.database, core.lib, wad.lib, trl.lib, compile.complete.deploy,
applyModule

|  
compile  |  Generates Java classes for the WAD windows that are required, this
is, the ones that contain processes with standard UI implemented within 2.50
windows or windows compatible only with 2.50 but not with 3.0; the rest of
windows are not generated unless they are forced through `
wad.generateAllClassic250Windows ` property.Generates Java classes from
modified xsql files, compiles all modified classes (including the generated
ones), makes insertions in translation tables for non-existing entries for the
manual UI files and copies everything to WebContent directory.  |
**Requires** :

wad.lib, trl.lib, database created and populated.

**Calls** : translate

**Properties** :

  * **tab** : specifies the window name(s) to be generated, to specify more than one window add them as a list of comma separated values. Note that even window is specified by this property, its 2.50 code will not be generated unless it is required or forced. 
  * **tr** : if set to "no" it will not call the translation process. 
  * **module** : a list of comma separated javapackages of modules to generate just the windows containing objects for those modules. 
  * **wad.generateAllClassic250Windows:** (default to false) when it is true, it forces WAD to generate code for all 2.50 style windows. 

|

  * compile.src: it does the same as compile but without generating WAD windows. 
  * compile.development: it also copies the files to the tomcat's context. 
  * compile.complete: It does the same as compile but before removes all the generated and built files, so the whole application is built. Note do not use tab or module properties because the application will be partially rebuilt. 
  * compile.complete.development: The same as compile.complete but after the process copies all the generated classes to the tomcat's context. 
  * compile.deploy: The same as compile or compile.development, depending on how the deploy.mode property in the Openbravo.properties file is set. 
  * compile.complete.deploy: The same as a compile.complete or compile.complete.development, depending on how the deploy.mode property in the Openbravo.properties file is set. 

  
translate  |  Checks in the manual windows User Interface files the
translateable elements that have not been yet registered and registers them,
this is necessary to be able to translate those interfaces to different
languages.  |  **Requires** :

trl.lib

**Called by:** This task is called by the compile.* tasks in case the tr
property is not set to "no"

|  
war  |  Generates a war file from the existing built code. In fact it only
zips the application in a single war file.  |  **Requires:**

compile.*: the application must be built before calling this task.

|  
deploy.context  |  Deploy the existing war file in the tomcat context using
the tomcat manager.  |  **Requires:**

  * war file must be created. 
  * Tomcat manager must be running 
  * These properties must be properly set in the Openbravo.properties file: 
    * tomcat.manager.url 
    * tomcat.manager.username 
    * tomcat.manager.password 

|  
  
###  Database tasks

Task  |  Description  |  Notes  |  Sub Tasks  
---|---|---|---  
update.database  |  Synchronizes database with the current database xml files.
By default it checks that no changes in application dictionary in database are
done, if so the process stops.  |  **Properties:**

  * force: (default as false) Do not check for database modification and update directly. This can cause lose of database data. 

|

  * update.database.script: It is the same as _update.database.structure_ but does not modify the database. It only generates a sql script file with the statements that would be executed by the other tasks. 

  
create.database  |  Creates the database from the xml files, note that the
database is first removed.

If the _apply.on.create_ property is set, masterdata and sampledata will be
inserted in the database. If not, only sourcedata will be inserted.

|  **Properties:**

  * apply.on.create: If is set to "true" and there are modules they will be applied, otherwise they will be set as "In process" status. 

|

  * create.database.script: The same as _create.database.structure_ but does not affect the database it only generates the sql script file with all the statements that would be executed by the other tasks. 

  
export.database  |  Synchronizes xml files with the database current contents.
By default they are only exported in case there are modifications in the
database. In addition performs database validations for the modules which are
exported.  |  **Properties:**

  * force: (default to false) Forces the export skipping the check of which files had been modified since last update.database 
  * validate.model: (default to true) Checks the model that is being exported fulfills a series of rules related to modularity, oracle-postgreSQL compatibility, etc. In case any of these rules is not complied, export will not be done and an error message will be raisen. 

|  
  
![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR17Q2  ** .  
---|---  
  
` update.database ` and ` export.database ` tasks support multi-thread
parallel execution for some of their actions such as index creation or
function standardization. By default, the number of threads used is calculated
as the half of the available number of cores in the machine where the task is
executed. This value can be set by adding the ` -Dmax.threads= _numOfThreads_
` parameter

###  Modules

Task  |  Description  |  Notes  
---|---|---  
package.module  |  Validates the module and if no errors are found generates
the obx file for the module.  |  **Properties**

  * module: Java package for the module to extract. 
  * obx.export.RD: If set to true the reference data is exported for the modules (if it has), by default is false. 
  * obx.export.DB: If set to true the database is exported for the modules, by default is false. 
  * obx.export.CS: If set to true the configuration script is exported (in case there is an active template), by default is false. 
  * obx.export.validate: (from 3.0MP20) Validates module before exporting, by default is true. 
  * obx.export.allDeps: (from 3.0MP20) Includes in the obx all dependencies (recursively) of the module being exported (not only inclusions), in this way it is possible to create an umbrella module on top of all installed modules in the instance, that when it is exported, contains all the sources in the instance, being in this way much simpler to promote this code from testing to production environments. By default it is false. 

  
export.config.script  |  Generates the configuration script for the current
active template (if any). More information about Industry Templates and
configuration scripts can be found  here  |  **Note:** export.database must be
executed before running this process  
check.module.consistency  |  Checks the locally installed modules satisfy all
their dependencies, this is, the instance is consistent. In case there are
modules that define dependencies that are not installed a message is shown
indicating which is the module and which dependency is not satisfied.  |  
  
###  Test Tasks

Task  |  Description  
---|---  
run.tests  |  The default, it runs the suite:
_org.openbravo.test.AntTaskTests_ . These tests are side effect free and can
be run multiple times, after the run the database should be in the same state
as before.  
run.quick.tests  |  This task runs test cases which are fast and which test
the most important parts of the system. It runs the test suite:
_org.openbravo.test.AllQuickAntTaskTests_ .  
run.all.tests  |  Runs the suite _org.openbravo.test.AllAntTaskTests_ . This
suite contains all the test cases, also tests which can change the database.  
  
###  Other Tasks

Task  |  Description  
---|---  
migrate.attachments  |  Migrates the attachments to the new attachment model.
For more information on the new attachment model refer  here  .  
host.name  |  Prints local host name, to be used to create an instance `
Openbravo.properties ` to  override common properties  .  
  
Retrieved from "  http://wiki.openbravo.com/wiki/Development_Build_Tasks  "

This page has been accessed 34,132 times. This page was last modified on 5
February 2021, at 06:43. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

