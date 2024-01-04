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

  

#  How to create a callout that extends from another callout

##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  Defining callouts 
    * 3.1  Defining Parent Callout 
    * 3.2  Defining Child Callout 
  * 4  Working with combos 
  * 5  Using getStringParameter method 

  
---  
  
##  Introduction

This howto discusses how to implement a callout that extends from another
callout. This howto only explain the main important elements needed for the
new feature. More details about callouts can be found in the  How to create a
Callout  howto.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from version **3.0PR16Q4**  
---|---  
  
##  Example Module

This howto is supported by an example module which shows examples of the code
shown and discussed.

The code of the example module can be downloaded from this public mercurial
repository:  org.openbravo.client.application.examples  .

##  Defining callouts

It are going to show two callouts. One of them is the parent callout and the
other one is the child callout.In this example, these two callouts are working
in 'Assets' window.

####  Defining Parent Callout

The following example follows this  guide  to implement the callout. The
example shows a callout that edits value of the 'Name' field.

    
    
     
    package org.openbravo.client.application.examples.callouts;
     
    import javax.servlet.ServletException;
     
    import org.openbravo.erpCommon.ad_callouts.SimpleCallout;
     
    public class OBEXAPP_Assets_Name extends SimpleCallout {
     
      protected static final String MODIFIED_FIELD = "_UPDATED";
     
      @Override
      protected void execute(CalloutInfo info) throws ServletException {
     
        // get value of field name and update value
        final String name = info.getStringParameter("inpname");
        info.addResult("inpname", name + MODIFIED_FIELD);
     
        // Combo example. Added three currencies to currency combo.
        info.addSelect("inpcCurrencyId");
        // USD currency is selected.
        info.addSelectResult("100", "USD", true);
        info.addSelectResult("102", "EUR", false);
        info.addSelectResult("103", "DEM", false);
        info.endSelect();
      }
     
    }

As you can see the callout gets the value of 'Name' field and concatenates the
following string: '_UPDATED'. Besides you can see a code that defines a combo.
This code it will explain in following section.

####  Defining Child Callout

This example callout extends from the parent callout that is defined above.
Combo example is explained in next section.

    
    
     
    package org.openbravo.client.application.examples.callouts;
     
    import javax.servlet.ServletException;
     
    public class OBEXAPP_Assets_Desc extends OBEXAPP_Assets_Name {
     
      @Override
      protected void execute(CalloutInfo info) throws ServletException {
     
        // OBEXAPP_Assets_Name callout is executed
        super.execute(info);
     
        // Combo example. Removed USD currency from combo and select DEM currency.
        info.addSelect("inpcCurrencyId");
        info.removeSelectResult("100");
        info.addSelectResult("103", "DEM", true);
        info.endSelect();
     
        // Checks if name field has been updated by parent callout.
        String name = info.getStringParameter("inpname");
        String message = "Feature 'Extends a Callout' works as expected.";
        if (name.endsWith(MODIFIED_FIELD)) {
          info.addResult("inpdescription", message);
          info.addResult("MESSAGE", message);
        } else {
          message = "Feature 'Extends a Callout' not works as expected.";
          info.addResult("inpdescription", message);
          info.addResult("ERROR", message);
        }
     
        // Now it is possible to update the 'name' field again and the value will be overwritten
        info.addResult("inpname", "UPDATED...");
      }
    }

First of all, OBEXAPP_Assets_Desc callout extends from OBEXAPP_Assets_Name. In
this situation, you should take into account the following sections in this
callout:

  * Run parent callout. 

    
    
     
        // OBEXAPP_Assets_Name callout is executed
        super.execute(info);
     

  * Operations for **combo** field are executed. This code is explained in next section. 

    
    
     
        // Combo example. Removed USD currency from combo and select DEM currency.
        info.addSelect("inpcCurrencyId");
        info.removeSelectResult("100");
        info.addSelectResult("103", "DEM", true);
        info.endSelect();
     

  * Operations **after** parent callout is executed. In this case, child callout checks if name is been modified by parent callout. Then child callout takes two actions. Update the description field with a message and shows an information or failure message. Finally name field is updated again. 

    
    
     
       // Checks if name field has been updated by parent callout.
        String name = info.getStringParameter("inpname");
        String message = "Feature 'Extends a Callout' works as expected.";
        if (name.endsWith(MODIFIED_FIELD)) {
          info.addResult("inpdescription", message);
          info.addResult("MESSAGE", message);
        } else {
          message = "Feature 'Extends a Callout' not works as expected.";
          info.addResult("inpdescription", message);
          info.addResult("ERROR", message);
        }
     
        // Now it is possible to update the 'name' field again and the value will be overwritten
        info.addResult("inpname", "UPDATED...");
     

In the following screenshot you can see how failure message is displayed.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_callout_that_extends_from_another_callout-1.png){: .legacy-image-style}

##  Working with combos

As you can see in above sections, the OBEXAPP_Assets_Name callout builds a
currency combo. This combo is populated with 3 currencies and one of them is
selected.

    
    
        ............
     
        // Combo example. Added three currencies to currency combo.
        info.addSelect("inpcCurrencyId");
        // USD currency is selected.
        info.addSelectResult("100", "USD", true);
        info.addSelectResult("102", "EUR", false);
        info.addSelectResult("103", "DEM", false);
        info.endSelect();
     
        ............

You can see the currency combo with 3 currencies and 'USD' as selected
currency.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_callout_that_extends_from_another_callout-2.png){: .legacy-image-style}

  
Then, child callout (OBEXAPP_Assets_Desc) removes a currency and select
another one. This child callout extends OBEXAPP_Assets_Name and change the
currency combo.

    
    
        ............
     
        // Combo example. Removed USD currency from combo and select DEM currency.
        info.addSelect("inpcCurrencyId");
        info.removeSelectResult("100");
        info.addSelectResult("103", "DEM", true);
        info.endSelect();
     
        ............

In this screenshot you can see how currency combo is displayed when child
callout is executed.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

The DEM currency is selected and USD currency has been removed.  
  
---|---  
  
![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_callout_that_extends_from_another_callout-4.png){: .legacy-image-style}

##  Using getStringParameter method

This method is used in callouts to get values of any field of the window.(e.g.
value of name field in Assets window).

Now, with the inclusion of this project this method takes into account if a
parent callout modified a value. If a value was modified,
"getStringParameter()" method returns value modified by parent callout. If
not, "getStringParameter()" method returns the initial value of the parameter.

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_callout_that_extends_from_another_callout
"

This page has been accessed 6,588 times. This page was last modified on 30
September 2016, at 07:50. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

