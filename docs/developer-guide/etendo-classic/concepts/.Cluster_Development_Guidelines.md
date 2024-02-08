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

  

#  Cluster Development Guidelines

##  Contents

  * 1  Introduction 
  * 2  Caches 
    * 2.1  Safe caches 
    * 2.2  Cache implementations 
      * 2.2.1  @ApplicationScoped classes 
      * 2.2.2  Singleton classes 
      * 2.2.3  Static fields 
  * 3  Synchronization at JVM 
  * 4  Files 
  * 5  Session objects 

  
---  
  
##  Introduction

The following guide is intended to describe the basic elements which needs to
be taken into account to ensure developments are supported in a clustered
environment.

For the scope of this document, we consider that a clustered environment is an
Openbravo application distributed on multiple JVMs.

Clustered environments are intended to improve performance allowing to serve
more process concurrently as well as high availability allowing the system to
continue working even if some of the nodes in the cluster are down.

Hereinafter, this document describes the topics that require an special
attention.

##  Caches

A cache is an object intended to store elements that are expensive to create
and are frequently used, in this manner they are created just once and reused
many times, saving their computation for subsequent uses.

The main concern regarding caches in clustered environments is there will be
as many cache instances as nodes in the cluster, this can lead to the
possibility of having nodes with outdated information because of the fact of
changing a value in one node without notifying the rest of the nodes about the
change.

For clustered environments, we have to pay attention on the implementation of
a cache when its life cycle is higher than request and also if it is keeping
instance information.

In that case, it is mandatory to have a mechanism which allows to refresh the
cache contents on every node of the cluster.

For example if we currently have a class extending `
EntityPersistenceEventObserver ` ( ` @ApplicationScoped ` ) which takes care
of updating some kind of cache when it detects a change on the JVM where it is
running, this implementation itself is not enough for a clustered environment
as the rest of the nodes will not be notified about the change.

###  Safe caches

In summary, we do not need to take special care about the caches under the
following scenarios:

  * If the cache life cycle occurs at request scope or lower (for example the life cycle of the cache is within a method). NOTE: If the cache is ` @SessionScoped ` , it can be used safely as long as Openbravo uses the sticky sessions. 
  * If the cache is used internally by an object (it is a private field) which life cycle is not beyond than ` @SessionScoped ` . 
  * If the cache keeps static information, then it is safe to have an instance of the cache per node. Some examples about static information are: 
    * Information based just on the Application Dictionary 
    * Information based on the application configuration: ie. information taken from ` Openbravo.properties ` file. 

###  Cache implementations

Even a class is not designed to be used as a cache, for the purpose of this
discussion, any class that fits in any of the following categories should be
considered as cache, and therefore, be specially reviewed.

####  ` @ApplicationScoped ` classes

` @ApplicationScoped ` is a CDI annotation that allows to define a class whose
is guaranteed to have a single instance per JVM, so for all matters it behaves
as  Singleton classes  .

` @ApplicationScoped ` classes can be considered caches whenever they have
state, this is, they have instance fields, those instance fields are in
practice cached elements.

####  Singleton classes

A  singleton class  , ensures there is a single instance per JVM of that
class.

They can be considered as caches with the same criteria than `
@ApplicationScoped ` classes.

####  Static fields

Any static field can be considered as a cache as its life cycle is application
scoped, this is, there is a single instance of that field for the whole JVM.

Only in the following cases, a static field can be considered safe in this
regards:

  * It is immutable: it is ` final ` and all the fields within it are immutable as well. 
  * It is private and the class containing it, ensures a proper state management. 

##  Synchronization at JVM

Java synchronized blocks  allows to define pieces of code that are guaranteed
not to have parallel executions. But this synchronization occurs at JVM level,
so we cannot ensure with a synchronized block not to have parallel executions
of this block among different nodes in the cluster.

So, on a clustered environment, synchronized blocks must not be used to
synchronize utilities intended to be executed in a synchronized way at system
level.

If we need to synchronize some kind of task at system level, then we have to
use another kind of synchronization mechanism, for example by using the
database tier.

##  Files

We must also take care when handling files in a clustered environment. In
general, we have to:

  * Avoid writing/reading files from the source path: clustered nodes shouldn’t require to have access to source directories. 
  * Avoid writing files on ` WebContent `
  * Unify the usage of temporary files 

##  Session objects

Due to issue  35440  , objects set in session, as well as instances of `
@SessionScoped ` classes, currently cannot be transferred from one node to
another. Once this issues is fixed, it should be possible to do so.
Transferring a session from one node to another implies to serialize it,
transfer over the network and deserialize it the destination one, thus the
bigger the session is, the longer this process will take. The recommendation
is to keep the session as small as possible not storing it in big objects.

Retrieved from "
http://wiki.openbravo.com/wiki/Cluster_Development_Guidelines  "

This page has been accessed 3,077 times. This page was last modified on 1 June
2017, at 09:01. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

