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

  

#  Application Menu

##  Contents

  * 1  Introduction 
    * 1.1  Managing the menu 
    * 1.2  Security 
    * 1.3  Information folder 

  
---  
  
##  Introduction

Application  Menu  is shown in the window's left side. It is used to make
accessible to the user all the application elements.

  

![](/assets/developer-guide/etendo-classic/concepts/Application_Menu-0.png){: .legacy-image-style}

  

###  Managing the menu

Menu is managed from **General Setup || Application || Menu** window. To
create a new menu entry:

  * Create a new record in this window 
  * Select the element type for the entry, this is done setting the _Action_ field, the elements callable from menu are _Window_ , _Report_ , _Process_ , _Form_ , _Workflow_ , _Internal/External link_ and _Task_ . 
  * Depending on the selected action a different drop down list will be shown to selected one element of the selected type. 
  * Note that name and description will be overwritten when synchronize process is executed. 
  * Place the new menu entry in the correct position, this is done by: 
    * Selecting a record in the grid 
    * Opening the tree pop up clicking in tree menu icon  ![](/assets/developer-guide/etendo-classic/concepts/Application_Menu-1.png){: .legacy-image-style}
    * Select the entry to relocate and drag and drop it to the new position. 

  

![](/assets/developer-guide/etendo-classic/concepts/Application_Menu-2.png){: .legacy-image-style}

  
Folders are created checking the _Summary Level_ field.

###  Security

Although a menu entry is defined it will not be displayed in case the role
that has log in the application has not granted permission for that element.

###  Information folder

In the bottom of the menu there is a _Information Folder_ , it contains links
to the _Searchs_ . The elements displayed in this folder are the ones that are
used in at least one accessible window for the current role.

Retrieved from "  http://wiki.openbravo.com/wiki/Application_Menu  "

This page has been accessed 12,430 times. This page was last modified on 23
December 2011, at 09:05. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

