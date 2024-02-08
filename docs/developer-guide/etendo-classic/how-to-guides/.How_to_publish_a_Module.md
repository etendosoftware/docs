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

  

#  How to publish a Module

  

##  Contents

  * 1  Overview 
  * 2  Central Repository 
  * 3  Life Cycle 
    * 3.1  Creation 
      * 3.1.1  Register Module 
      * 3.1.2  Associate with a Forge Project 
        * 3.1.2.1  Register Project 
        * 3.1.2.2  Associate Project with your Module 
        * 3.1.2.3  Unregister Module 
    * 3.2  Support by Author 
    * 3.3  Version Life Cycle 
      * 3.3.1  Publish Version 
      * 3.3.2  Version Life Cycle 
        * 3.3.2.1  Setting Module Version Maturity 
          * 3.3.2.1.1  Initial Status 
          * 3.3.2.1.2  Promotion 
          * 3.3.2.1.3  Cancel 
        * 3.3.2.2  Allowed Maturity Status in Openbravo ERP 
  * 4  Selling modules 

  
---  
  
##  Overview

This document explains how to publish and manage modules in Central Repository
to make them available to any Openbravo ERP instance.

##  Central Repository

The Central Repository is a system embedded in the  Openbravo Forge  to
provide services related to Openbravo ERP _Modules_ for developers and users:

  * For developers: 
    * **Register a module** : a developer registers a new module in the Central Repository to get global unique identifiers to be used for development (it's highly recommended to register a module before starting the module's development). 
    * **Publish a new version** of a module: a module can have different versions in its life cycle. For each of them module owners need to update the information in the Central Repository to make this new version available for users. 
    * **Manage life cycle** of a version: a module version can be in different statuses during its life cycle, each of these statuses makes it available to different kinds of Openbravo ERP instances. 

  * For users: 
    * **Search for modules** : from the MMC users can query the Central Repository to get a list of modules that match with user request. 
    * **Scan for updates** of a list of module versions: from the MMC users can request to the Central Repository if there are available updates (newer versions) for all the modules installed in their instances (or just for one of them). 
    * **Get the code of a module version** (to be installed): for both installing new modules and updating current ones it's needed to get the compressed file (.obx file) that stores module code. 

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-0.png){: .legacy-image-style}

##  Life Cycle

This section explains the complete life cycle of a module starting from its
creation.

###  Creation

####  Register Module

There are two properties in the modules that are very important to be unique
and no other module has the same value for them. They are _Java Package_ and
_DB_Prefix_ . If more than one module with the same _Java Package_ or
_DB_Prefix_ is tried to be installed in the same Openbravo ERP instance there
would be conflicts between them that would prevent the correct installation.
This is why it is very important to guarantee uniqueness for these properties.

The way to guarantee this uniqueness worldwide is to register modules in
Central Repository just after their  creation  . In this way you will notice
in case other registered module is making use of the same _Java Package_ or
_DB_Prefix_ you want to use and in this, case you will be prompted to change
your initial election. It is important to register new modules just after
their creation before starting their development, doing so you will notice
possible conflicts in _Java Package_ or _DB_Prefix_ that would affect your
module's artifacts' names and would require a lot of work to change if it was
registered after they were developed.

You can register your module through the _Register Module_ button in the main
tab of the _Module_ window. It sends your module's information to Central
Repository, checks _Java Package_ and _DB_Prefix_ are not already registered
by any other module and reserves them for yours making not possible other
modules to use them. In case they are already used, an the process is aborted
and an error message is shown you to change them before trying to register
again.

A registered module is not publicly available for download, so even you don't
plan to publish your module it is recommended to register it just to prevent
other registered modules to use the same _Java Package_ or _DB_Prefix_ you
took for yours.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  You
can check out which are modules already registered in Central Repository in
http://forge.openbravo.com/openbravo/moduleslist  
---|---  
  
After registering a module it is possible to unregister it in case it has not
been already associated with any project, see  Unregister Module section  .

####  Associate with a Forge Project

To be able to publish a module to the Central Repository so they are
accessible through the  Module Manager Console  , it is necessary to associate
it with a Forge Project.

#####  Register Project

Registering a project is your first step to get involved in the Openbravo
ecosystem. Follow this short guide to learn how to register a project in
Openbravo Forge  .

It is a simple 2 step wizard which asks the minimum information to create the
project. Note that you will be able to change the configuration afterwards
using the administration panel.

First go to the register form:

  * On the **Project Directory** box (left column) there's an option at the bottom. 

     ![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_publish_a_Module-2.png){: .legacy-image-style}

Then you only need to fill the form:

  1. **Fill the basic project information:**
    * _Name:_ The project name. Can have spaces and should be enough to understand the project's aim. 
    * _Short name:_ A short version of the project's name without spaces. It will be used in project's URL. 
    * _Description:_ A brief description of the project. What it is about, its goals, its target market. 
    * _License:_ Choose one of the different licenses for your project. You can choose (if needed) _other open source_ if non of the combo-box licenses is the one you have chosen for your project. If that's the case, please specify it on the Description field. 
    * _Project type:_ Whether the project is a translation project or any other kind of project. 
    * _Category:_ Choose if your project targets Openbravo ERP or Openbravo POS. 
    * _Subcategory:_ Choose one of the subcategories for the category previously selected. 

     **Note:** later you will be able to add your project to two more categories in your admin interface. 
    * _Visibility:_
  2. **Fill the links to the services associated to the project** .   
You can add here the links to your **own system services** if any, otherwise
Openbravo recommends the usage of  bitbucket  as free source code hosting.

    * _Forums Link:_
    * _Downloads link:_
    * _Bugtracking Link:_
    * _Code Link:_
    * _Wiki Link:_

     Please note that in the case you are a "Professional" localizer registering a "Localization" module or pack the "Forge Project Tools" listed below need to point to Openbravo tools, such as: 

  * **Wiki Link** to the corresponding wiki page which needs to be tagged at the very end of the document as  Category:Mexico  , for instance.   
Please contact the Openbravo Localization Lead at
(patricia.sanjuan@openbravo.com), before creating your country "Category".

  * **Bugtracking Link** to the  Openbravo Issues system - Project: Professional Localizations - Category: Professional Localization Mexico  , for instance   
If you do not find the specific Professional Localization "Category" for your
country please contact the Openbravo Localization Lead at
(patricia.sanjuan@openbravo.com).  
Either you want to report an issue or monitor the issues entered, you need to
create an account "username" here:  login Openbravo  .

    * if you are the owner of the "Professional" localization for your country,please contact the Openbravo Localization Lead to inform her about the username who will monitor the issues of any kind reported for your localization project. 
  * and a **Code Link** to the corresponding (to be defined). 

     If you have any question related to any "localization" project tools link please contact the Openbravo Localization Lead at (patricia.sanjuan@openbravo.com). 

And that's all you have to do to create a new project in Openbravo Forge.

Now you can go to your recently created project homepage:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-3.png){: .legacy-image-style}

#####  Associate Project with your Module

Once there is a project registered in the forge, the next step is to associate
the module just registered with it.

It is important to remark that the just registered module does not have a
published version yet, therefore you will be able to find it if you select the
checkbox "Show modules without published version".

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-4.png){: .legacy-image-style}

You can find this checkbox while browsing Modules by pressing the process
button "Show advanced filters".

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-5.png){: .legacy-image-style}

Then click on the My Modules link in the left menu. Then a window will be
opened where all the modules you are admin for are listed. Among them, you'll
find the one you just registered.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-6.png){: .legacy-image-style}

If you click in the module name, a new window will be open where you can pick
the project you want to associate your module with.

A module can only be associated with one project, but projects can be
associated with several modules.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-7.png){: .legacy-image-style}

#####  Unregister Module

Right now it is not possible to unregister a module.

Unregistering a module will release the _Java Package_ and _DB_Prefix_ that
module has making them available again.

###  Support by Author

Module's author can decide, at any point in time, which is the support type
for each of the modules owned by him.

The possible values are:

  * Included in Openbravo Subscription 
  * Included in Module Subscription 
  * Available as Extra Service 
  * No Commercial Support 
  * No Information 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-8.png){: .legacy-image-style}

###  Version Life Cycle

####  Publish Version

When a module version is completed and  packaged  it can be published in
Central Repository.

  1. Access to the module you want to publish the version for. 
  2. Click on _Upload new version_ button. 
  3. Select the obx file with the version to publish. 
  4. Select the initial maturity status for that version. Maturity statuses are detailed in  Version Life Cycle  section. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-9.png){: .legacy-image-style}

####  Version Life Cycle

During the life of a module, it can be at different maturity statuses in
Central Repository. The maturity status for a version should be promoted after
passing some tests and/or being used for some time in a real production
instance. Setting the maturity for a version is up to the module
administrator.

The possible values version maturity status can have are:

  * **Test** : This status is intended to be used for versions that have not been completely tested. A version published with this status should be installed only in instances which desire to test it, generally to provide feedback to the module administrator/owner. Versions with this maturity shouldn't be installed in production environments. _Not recommended for production purposes_ . 
  * **QA** . During this stage the module must pass all the test defined by the Quality Assurance to confirm it as _QA Approved_ . 
  * **QA Approved** : At this stage the version has been deeply tested and it is ready for production. The module owner feels confident with it, but he wants to have some maturity period before he tags it as _Confirmed Stable_ . It will become available for all the Community instances and the Professional and Basic ones that want to install it at this stage and can be safely installed for production.. _Recommended for production purposes to early adopters_ . 
  * **Confirmed Stable** : It is the final stage for a version. It is supposed to have passed the three previous ones, so it is tested and it has been working during some time in production instances. It is available for every instance. _Recommended for production purposes to all users_ . 
  * **Canceled** : Canceled versions are not available to be installed in any instance. 

#####  Setting Module Version Maturity

Maturity level for a version is set by the module owner and by the
administrators of the project the module is associated with. They should
define and follow some rules to decide which is the correct status for each
version of his modules, but finally is up to him to set it.

######  Initial Status

When  publishing a new version  in Central Repository, the module
administrator will be prompted to select the initial maturity status for that
new version. Being _Test_ the default value.

Note that the status for a version can always be upgraded but it cannot be
downgraded.

######  Promotion

At any point of time, the module administrator can promote the maturity of a
version.

The steps to do it are:

  1. Select in the  forge  the module that contains the version to promote. 
  2. All the versions of the module are listed below the module details. 
  3. Change the maturity status of the version you want to promoto, and click on the Update button. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_publish_a_Module-10.png){: .legacy-image-style}

######  Cancel

In case in a published version a critical issue is found and the module owner
wants to prevent this version to be installed in more instances, he can cancel
it.

Once a version is canceled it will not appear to be installed or upgraded in
any instance. Note that instances that have already installed it, this version
will still be usable.

To cancel a version, you have to click on the version number in the module
details window. Then the version details is open, and you can click on the
Cancel version button on the top right corner.

#####  Allowed Maturity Status in Openbravo ERP

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Professional and Basic instances are defaulted to just accept versions in
**Confirmed Stable** maturity status.

Community instances are defaulted to accept versions in at least **QA
Approved** maturity status.  
  
---|---  
  
Minimum maturity status accepted in Openbravo ERP instances can be configured.
Detailed explanation about how to do that can be found in  Modules Management
Configuration Manual  .

##  Selling modules

Module versions can be defined as **commercial** , which means they may only
be installed and used in an Openbravo instance that has been activated with a
license key that includes the commercial module (normally added after
purchase).

To increase the accessibility of your commercial module, we strongly recommend
that you identify it as **Available for Trial License** , which means that
users who opt for a free 30 Trial license of Openbravo Professional Edition
will be able to install and try out your commercial module for 30 days.

More information about selling modules can be found in this  article  .

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_publish_a_Module  "

This page has been accessed 29,349 times. This page was last modified on 22
May 2019, at 14:37. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

