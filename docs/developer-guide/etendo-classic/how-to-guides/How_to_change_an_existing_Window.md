---
tags: 
  - Application Dictionary (AD)
  - UI Customization
  - Physical Inventory
  - Module Development
---

#  How to change an existing Window

  
##  Overview

Application elements (windows, tabs and fields) are liable to change
repeatedly during the development or maintenance phases of a project.
Etendo is able to cope with these changes because its architecture is
suited to iterative development. The definitions of all generated Windows,
tabs and fields are stored as metadata in the Application Dictionary (AD).

Changing the window of an existing application is a simple process of changing
the AD definition.

When using the Etendo UI this is all that is needed, the changes can be
seem immediately when switching role and then by opening the changed window
again.

When using classic Window additionally a compile step is needed as it was
during the Openbravo 2.50 cycle.

This How-To explains how to modify existing elements of a window. If only new
elements (like new fields) should be added to a window the use of a Template
(as explained here) is not needed. Instead, those new elements can just be
added using a normal module as explained in the other How-To on
[How to add a field to a window Tab](/developer-guide/etendo-classic/how-to-guides/How_to_change_an_existing_Window/). 
 


##  Objective

The objective of this how-to is to illustrate how to make changes to existing
generated windows in terms of appearance and behavior. The window used in the
example is the Physical Inventory window and the changes illustrated will be:

  * Hide a field 
  * Re-sequence the layout 

Physical Inventory is a window that belongs to Etendo Classic.
It comprises of:

  * 1 Window - Physical Inventory. 
  * 2 Tabs - Header and Lines. 
  * A Header Tab has 19 Fields 10 of which are displayed (A few are displayed conditionally).

Before any changes the header tab has the following appearance:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_change_an_existing_Window-0.png){: .legacy-image-style}

  
To customize these window in a Modularity Context a new module of Type
*Template* / *Industry Template* is needed.

If these changes are just planned as local customization then there is an easy
way of creating such a module. Navigating to General Setup || Application ||
System Info _and marking the_  _Customization Allowed_ CheckBox
automatically creates a new module of type Template which can be used
directly.

If the changes are planned to be published then a new module needs to be
created and its _Type_ set to _Template_ . This new template needs to have
dependency added to it on all other modules which contain elements which are
to be customized. In this How-To this is only a dependency on the _Core_ module
as the _Physical Inventory_ window is defined there.

##  Changing the window

Navigate to the _Application Dictionary || Windows, Tabs and Fields_ window
and select the record for _Physical Inventory_ .

In the _Fields_ tab we can now make the changes needed to adapt the layout as
wanted:

  * _Description_ field, unmark the _Displayed_ checkbox to hide the field from the tab. 
  * _Organization_ field, change sequence number to _45_ and mark the _Start in new line_ checkbox. This moves the field below all other normally displayed. 

  
For testing the changed layout, switch away from the _System Administrator_
role to i.e. the _F &B International Group Admin _ role and open the _Physical
Inventory_ window again. As the instance contains our module marked as
_InDevelopment_ the window layout is reloaded each time the window is opened, so
we can see the changed layout immediate as seen below:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_change_an_existing_Window-1.png){: .legacy-image-style}

  
To apply the same layout changes to the window in _classic UI mode_, the
windows need to be recompiled, the changes deployed to tomcat and tomcat
restarted. The compile & deploy step can be done by using _ant smartbuild_
which will recompile all changed windows and deploy the changes.

  

##  Exporting the changes

The final step is to export the changes into the module so they are persisted.

!!!note
    When exporting changes into a template, it is important that only
    the *template is in development* and the module which contains the changed
    object (i.e. window) is not.

After ensuring that the export of the changes consists of the following two
steps:

  1. _ant export.database_ , same steps as for any other module 
  2. _ant export.config.script_ , analyses the changes done and creates a special file _configScript.xml_ in the module to contain them. 



This work is a derivative of ["How to change an existing window"](http://wiki.openbravo.com/wiki/How_to_change_an_existing_Window){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.   


