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

  

#  How To Define Display Logic For Tabs

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Contents in this article are available from **3.0MP19**  
---|---  
  
##  Objective

The objective of this how-to is to show how you can define display logic for
tabs, so its visibility will depend on the value of the fields of its ancestor
tabs, of preferences and of system variables. The display logic will only be
applicable for tabs that are not header tabs.

For that purpose a new field called Display Logic has been added to the Tab
tab in the Windows, Tabs and Fields:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Define_Display_Logic_For_Tabs-1.png){: .legacy-image-style}

##  How to define the tab display logic

The syntax of the tab display logic is the same as the field display logic.
Boolean values (true, false) can be entered, and also expressions that
evaluate into a boolean value.

If there is a reference the a field of a tab of a higher level, the name of
the field should be placed between '@'. I.e., if we only want to show the
Query tab of the Widget window when the selected widget is a Query widget, the
Query tab display logic can be defined as:
@Widget_Superclass_ID@='2A32CF26F3F64FE39C7F94E9D82497D1'.

If there is a reference to a preference, the preference name must also be
placed between '@'. I.e. if a tab must be shown only if the StockReservations
property is set, this display logic can be used: @StockReservations@!''

And if inside the display logic there is a reference to a system variable, its
name must be placed between '@#' and '@', i.e. @#ShowAcct@='Y'.

Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Define_Display_Logic_For_Tabs  "

This page has been accessed 14,454 times. This page was last modified on 1
September 2016, at 08:03. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

