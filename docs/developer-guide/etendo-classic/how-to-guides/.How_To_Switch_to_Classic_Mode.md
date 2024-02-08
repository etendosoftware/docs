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

  

#  How To Switch to Classic Mode

##  Objective

In Openbravo 3 the Application Dictionary (AD) Windows are implemented in a
completely new technology that provides a much better user experience. But
still it is possible to configure the system so it renders the AD Windows
using the 2.50 implementation (we call it 'Classic Mode'). It helps for
backward compatibility and smooth transition between this two major versions.
The objective of this how-to is to explain how you can configure your instance
so it renders AD windows in Classic Mode.

For working and developing in classic mode many parts of the 2.50 developers
guide apply. You can find the 2.50 developers guide  here  .

**Note:**

  * Recent entries in quick launch, quick create and in the Workspace tab store the visualization mode in which they were opened. This means that if you move to classic mode that these 'recent' links are not updated and will open in the previous mode in which they were opened. 
  * There are situations in which Openbravo will automatically fall back to classic mode for specific windows, see  here  for more information 

##  Standard configuration

The standard way to define the way AD windows are rendered is through
Preferences.

Preferences are system properties (attribute-value pairs) that can be defined
at different levels (Global, Client, Organization, Role, User). Preferences
can be overwritten by more specific preferences (eg. a preference at user
level overwrites a global preference). Preferences can also be defined for a a
particular window. You can see the list of preferences defined in your
instance by opening the window 'General Setup > Application > Preference'
logged in as System Administrator.

By default all AD windows in Openbravo 3 are rendered using the new mode. But
you can overwrite this behavior through a preference by setting the property
named 'Use Classic UI mode' to the value 'Y'. As any other preference you can
set this it at different levels:

  * **Globally** : so for all users all windows will be opened in classic mode. In this case all parameters within the visibility section should be null. 
  * **For a particular window:** so only that window is opened in classic mode. In this case you should set the window parameter in the preference. 
  * **At user (or any other) level** : so only that user (or any other level) will open AD windows in classic mode. Set the proper level in the visibility of the preference. It can also be for a particular window. 

Two details you should be aware:

  * After setting the preference you need to logout and login to make the preference available in your session 
  * 'Recent' menu entries links explicitly include the mode in which the window was open. It means that if you open a window in new mode and then change the preference to open that window in classic mode, if you use the 'recent' link the system will ignore the preference and will use the actual mode used (new in this case). 

The image below shows how to set this preference for a particular window.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Switch_to_Classic_Mode-0.png){: .legacy-image-style}

##  URL parameters

In some cases you don't want to change permanently the behavior of the system
but just change it during a session (eg. to test something). In this case,
after being logged in you can 'hack' the system by adding a parameter
_mode=classic_ to the application URL (eg.
http://localhost/openbravo/?mode=classic  ). After this any window you open
will be opened in classic mode during that session.

Finally you can also get a pure 2.50 behaviour including application layout
(menu on the left, application frame on the right, etc.). To get it you have
to use the following url:
http://yourServerAddress/yourOBContext/security/Menu.html?noprefs=true  (eg.
http://localhost/openbravo/security/Menu.html?noprefs=true  ).

Retrieved from "  http://wiki.openbravo.com/wiki/How_To_Switch_to_Classic_Mode
"

This page has been accessed 9,776 times. This page was last modified on 16
June 2011, at 12:21. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

