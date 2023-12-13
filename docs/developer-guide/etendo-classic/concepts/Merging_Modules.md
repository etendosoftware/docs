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

  

#  Merging Modules

##  Contents

  * 1  Overview 
  * 2  What is Merging 
  * 3  When to Merge 
  * 4  Merge Process 
    * 4.1  Merging the Code 
      * 4.1.1  Database 
      * 4.1.2  Java 
    * 4.2  Merge Definition 
    * 4.3  Version 

  
---  
  
##  Overview

The aim of this document is to explain what merges are and how modules can be
merged.

##  What is Merging

A module ( _B_ ) can be merged into another one ( _A_ ). After merging these
two modules, _B_ is no longer available because it is included within _A_ .

In case an instance has an old version of _A_ and tries to install the new
version of _B_ or update to this one. The installation/update process will
uninstall _A_ , after this the only installed module will be _B_ and it will
not be possible to install in that instance any other _A_ version.

![](/assets/developer-guide/etendo-classic/concepts/Merging_Modules-0.png){: .legacy-image-style}

##  When to Merge

Merging modules should be done only in very few cases, it should not become a
common practice.

Two modules are prone to be merged in case one of them does not make sense
without the other one. Initially they could be thought to be separated modules
because of some reason (different functionality, intended to be used
separately, etc.), but within the evolution of both of them you realize they
should have be designed to be a single module.

The first decision to be taken in this situation is which is the module that
will be merged (so it will disappear) and which one will be contain the
functionality of the other.

Take also into account that it will be necessary to publish a new major
version of the module that merges the other one. This will make to extend
dependencies of all modules that depend on this one. Also modules that depend
on the merged module will not be compatible with the new merged one, so these
dependencies should be removed forcing to publish a new major version of them.

##  Merge Process

This section explains which are the steps to be followed in order to merge two
modules within one.

###  Merging the Code

####  Database

The objective here is to reassign all the database artifacts that belong to
merged module ( _B_ ) to the module that is merged into ( _A_ ) without
regenerating all these artifacts.

The simplest way to do this is by directly editing the _database/sourcedata_
files within module _B_ . In all these files it will be needed to replace
module _B's_ UUID with module _A's_ UUID.

After doing that, set both modules in development in the application, execute
ant update.database and then ant export.database. This exportation will move
all database artifacts from _B_ to _A_ .

It is also necessary to change _B_ data package to one inside _A's_ namespace
(starting with _A's_ Java package name). Note that this last change will cause
an API change because all DAL classes generated for _B's_ artifacts will be
repackaged.

####  Java

All Java classes in _B_ must be repackaged to be included within _A's_ Java
package and the .java copied within _A's_ module directory.

Again this repackaging will cause API change for all original _B_ classes.

Because of the change of package for database artifacts, it will also be
necessary to adapt all parts where DAL was used for them to the new package.

###  Merge Definition

Last step is to define the merge and publish a new major version of _B_ .

  
Before setting which is the module merged it is necessary to remove
dependencies of _B_ to _A_ , because it is not allowed to define a module as
merged and as a dependency at the same time.

The merged is defined in _Merges_ tab of _Module_ window, here it is necessary
to insert the Merged Module UUID and its name. As the merged module is not
part of the installed module it is not a foreign key relationship to module
table but it is identified by its UUID as a plain String, the name is used
just to make it human readable.

![](/assets/developer-guide/etendo-classic/concepts/Merging_Modules-1.png){: .legacy-image-style}

###  Version

All these changes will be packaged as a new version of module _A_ . It is
mandatory to be a new major version, this is because this new version includes
major changes in all original _B's_ API. Note that this change of major
version will force all modules that already depend on _A_ to extend their
dependency on _A_ to be compatible with latest major version.

Also modules that depend on _B_ will not be compatible with new _A_ version
(as it is not allowed to have installed a module that merges another module
with a module that depends on the merged one), so they should also publish a
new major version removing this dependency, they might now depend on _A_ as it
includes the old _B's_ functionality.

Retrieved from "  http://wiki.openbravo.com/wiki/Merging_Modules  "

This page has been accessed 4,031 times. This page was last modified on 2 July
2011, at 15:26. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

