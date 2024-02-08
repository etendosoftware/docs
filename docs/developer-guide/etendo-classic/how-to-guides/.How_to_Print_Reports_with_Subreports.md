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

  

#  How to Print Reports with Subreports

**Languages:** |

** English  ** |  Translate this article...  
  
---|---  
  
##  Objective

The objective of this article is to show how to print reports that include
subreports.

##  Execution Steps

There are three possible ways to print reports that include subreports:

  1. Using the **$P{SUBREP_report_name}** parameter to automatically look for the subreport that will be shown. This option only works on reports that have been processed by using the **"Print"** button in the **Sales/Purchase Invoice, Sales/Purchase Order, Goods Receipt/Shipment and Payment In/Out** windows. In those cases it is not necessary to include the subreport's .jasper since the .jrxml suffices, because at the time of execution it is being compiled and passed to the main report as a parameter. 
  2. The next possibility is defining the .jrxml for a process (in the **"Report and Process** " window) and then include this process in the menu. In this case, the only possible option is using the precompiled subreport (jasper) and refering to it from the .jrxml using BASE_DESIGN followed by the jasper path. The main disadvantage of using a precompiled subreports in that it is not translated in runtime so that is only possible to have the subreport in one language. 
  3. The last possibility is calling **renderJR** from an own java servlet, compiling the .jrxml and passing it as a parameter like described in the first method. This is done in the **PrintController** class (PrintController.java). 

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_Print_Reports_with_Subreports  "

This page has been accessed 7,442 times. This page was last modified on 21 May
2013, at 10:45. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

