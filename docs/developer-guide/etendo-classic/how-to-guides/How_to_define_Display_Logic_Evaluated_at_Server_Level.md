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

  

#  How to define Display Logic Evaluated at Server Level

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q1  ** .  
---|---  
  
###  Overview

With the introduction of this functionality, it is possible to define in
Openbravo Display Logic that are going to be evaluated at Server Level.

This means that the expression for this particular Display Logic is going to
be evaluated while generating the code for the final Window instead of being
evaluated when the Window is loaded.

By doing so, it is possible to avoid blank fields when the field should not be
shown. Instead, the fields are rearranged and the Window looks more clean.

###  Usage

In the Windows, Tabs & Fields Window, there is a new field named _Display
Logic Evaluated in the Server_ .

In this field, it is possible to define an expression that will be evaluated
to decide whether that particular field must be shown or not.

This expression must follow the same syntactic rules that are used in the
normal Display Logic. The expression can evaluate Preferences, but only those
defined at System Level.

An example of an expression would be: @uomManagement@ = 'Y' &
@enableNegativeStockCorrections@ = 'Y'

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_define_Display_Logic_Evaluated_at_Server_Level-1.png){: .legacy-image-style}

###  Limitations

Since this functionality is going to be evaluated at a System Level (the
visibility of the fields is going to be the same for all the Clients,
Organizations and Users), it is possible to use Preferences, but only those
ones that have been defined at System Level.

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_define_Display_Logic_Evaluated_at_Server_Level
"

This page has been accessed 4,471 times. This page was last modified on 11
November 2016, at 07:18. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

