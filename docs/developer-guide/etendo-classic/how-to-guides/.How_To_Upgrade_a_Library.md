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

  

#  How To Upgrade a Library

##  Contents

  * 1  Overview 
  * 2  Prerequisites 
    * 2.1  JDK version compatibility 
    * 2.2  License compatibility 
  * 3  Process 
    * 3.1  Check for API changes 
      * 3.1.1  Check source compatibility 
      * 3.1.2  Check how these changes affect published modules 
        * 3.1.2.1  Adding a new library 
      * 3.1.3  Publish API changes 
    * 3.2  Update legal folder 
    * 3.3  Update the .classpath file 
    * 3.4  Update wiki 

  
---  
  
##  Overview

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
intended audience of this document is mainly Openbravo staff. It describes the
internal process to be followed whenever a library needs to be upgraded. It
applies both to libraries in Openbravo 3 distribution as well as to libraries
delivered by modules.  
---|---  
  
From time to time, it is necessary to upgrade a Java library (a jar file) to a
newer version. Motivations for this can be diverse:

  * Make use of new capabilities 
  * Get rid of bugs in older version 
  * Keep updated stack 
  * ... 

To upgrade a library the process described bellow needs to be followed.

##  Prerequisites

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Upgrade_a_Library-1.png){: .legacy-image-style} |  If any of the following
prerequisites is not satisfied, it will **not be possible** to upgrade the
library to the newer version!!  
---|---  
  
Note these prerequisites apply also when adding a new library.

###  JDK version compatibility

**All** jars need to be compatible with, at least, the  lowest supported JDK
version  by Openbravo. If the jar is compiled with a higher version, it will
not be usable in instances running an older one (yes in the other way around).

To check the JDK version used to compile this library:

  * Unzip the new jar: ` unzip _new-library.jar_ -d /tmp/new-library `
  * Typically in the ` META-INF/MANIFEST.MF ` file there is information about the JDK used to compile it 
  * It is also posible to check the JDK used to compile ` .class ` files. This is done with the ` javap ` program checking the major version value.  Here  you can find how they correspond with the currently used numbers. The following script list versions of all ` .class ` files, note it can take time in case there are many files in the jar: ` for f in `find -name "*class"`; do javap -verbose $f | grep "major version"; done | sort | uniq `

###  License compatibility

Usually libraries select a license and they stick to it among different
versions. But sometimes, license is changed from a version to another.

When upgrading a library (or including a new one), you need to check the newer
version's license.

  * If it is the same as the older version, there is no problem. 
  * If it is a different one, check in the ` legal/Licensing.txt ` file: 
    * If the new license is already used by any of the included libraries, no problem 
    * If not, lawyer needs to be asked whether the new license allows to distribute this library 

##  Process

Once the prerequisites are satisfied, the upgrade process consists on the
following steps:

###  Check for API changes

A new library version can change its public API. To check these changes:

    
    
     hg clone clone https://code.openbravo.com/erp/devel/api-checks/
     cd api-checks/java/tools
     java -classpath japitools.jar net.wuffies.japi.Japize as /tmp/old-api apis _path_to_old_jar_ $JAVA_HOME/jre/lib/rt.jar $JAVA_HOME/jre/lib/jsse.jar +org # change org with the topmost part of the package in the library
     java -classpath japitools.jar net.wuffies.japi.Japize as /tmp/new-api apis _path_to_new_jar_ $JAVA_HOME/jre/lib/rt.jar $JAVA_HOME/jre/lib/jsse.jar +org # change org with the topmost part of the package in the library
     ./japicompat /tmp/old-api.japi.gz /tmp/new-api.japi.gz | tee /tmp/api-checks.txt
    

These steps will generate a ` /tmp/api-checks.txt ` file detailing all changes
that might exist.

####  Check source compatibility

Even when the api-checks tools do not find any API changes, there may be
source incompatibilities of the new version with the previous ones, see  here
an example. To check this, review the release notes of the library from the
previous to the new version.

####  Check how these changes affect published modules

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This step is only applicable in case of API changes or when including a new
library.  
---|---  
  
Get the code of all published modules in Central Repository. If you have
access to Central Repository server, follow next steps, if not, ask someone
else (ALO, SHU, AMA...) to do it for you.

    
    
    git clone https://github.com/alostale/ob-scripts.git
    ob-scripts/getAllModules/get-modules.sh
    ob-scripts/getAllModules/unzip-modules.sh
    

This will generate a ` src ` directory with sources of all published modules.

Now you can check in the code how the library is used there and whether these
changes can affect them. This will give you an idea of the risk of these
changes, and might, eventually, require to abort the upgrade process.

#####  Adding a new library

When adding a new library, check in published modules whether there are
already modules that deliver it. Pay special attention whether they include a
different version to the one you want to update, because in this case
incompatibility issues could appear when installing that module together with
your library. Depending on how big the impact is a decision on what to do
(proceed and communicate it to owner, abort upgrade...) will be required to be
taken.

####  Publish API changes

In case there are API change publish them in the  wiki  following the defined
process.

###  Update ` legal ` folder

All modules containing third party libraries should have a ` legal `
directory, which lists the licenses of all included libraries. It also has a `
Licensing.txt ` file, listing all library versions and the license they have.

  * Update ` Licensing.txt ` file to reflect new version 
  * In case of a different license: 
    * Include the text if it is not present yet 
    * Check if old license is still used by any other library, if not, remove the not used license file 

###  Update the .classpath file

The library is referenced in the .classpath file. If the name of the jar has
changed, the file must be updated with the new name.

###  Update wiki

When upgrading a library included within Openbravo 3 distribution, update the
wiki page  that list all the libraries included.

Retrieved from "  http://wiki.openbravo.com/wiki/How_To_Upgrade_a_Library  "

This page has been accessed 9,458 times. This page was last modified on 8
April 2019, at 14:45. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

