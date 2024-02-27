---
tags: 
  - callout creation
  - simple callout
  - DAL
  - Etendo Infrastructure
  - Etendo ERP
  - FIC
---

#  How to create a Callout

##  Objective



The objective of this article is to show you how to create a new  callout . A
callout is a piece of Javascript code associated with a particular field on a
tab. This code is executed whenever the field changes. It is a type of Ajax
substitute, changing parts of a tab/window without the need of refreshing it.

It works by calling the FIC when a field with an associated callout is
changed. The FIC (Form Initialization Component) refreshes the needed fields
based on the callout logic.

This section will implement the following new functionality: When entering a
new product, one has the option of entering the _Search Key_ for the product,
the _Name_ and the _Category_ it belongs to. But what if our client wants the
search key to be constructed automatically by taking the product's name,
removing all spaces, appending the underscore (_) and the category name it
belongs to?

For example, the Search Key of a product that has the
Name _Bon Fountain_ and belongs to the _Water_ Product Category would
become _BonFountain_Water_. Let's see how this could be done using a callout.

The steps involved in creating a new callout are:

  1. Create the source file(s) of the callout (usually a java file). 
  2. Define the new  callout  within the application dictionary (menu Application Dictionary > Setup > Callout  ). 
  3. Associate this callout with a table  column  ( Application Dictionary > Table and Column: Callout field withinin Column tab). 
  4. Compile the window/tab(s) where this Column is used. 

!!!Important
    Developments related to points (1) and (2) must belong to
    a module that is not the _core_ module. Please follow the [How to create and package a module](../../../developer-guide/etendo-classic/how-to-guides/How_To_Create_and_Package_a_Module.md)  section to create a new module. For the development related
    to point (3) about modifying a _core_ located column, a new template is
    needed. You can read the [How to change an existing Window](../../../developer-guide/etendo-classic/how-to-guides/How_to_change_an_existing_Window.md) article to obtain more information.

!!!Note
    This article assumes you have created both module and template according to the articles just mentioned.  

  
##  Creating the Callout

Existing callouts are located in _src/org/openbravo/erpCommon/ad_callouts_ .

The right way to create a callout is by extending the SimpleCallout class.
This class simplifies the callout code, hides some of the internals of the
callout and keeps you focused on the operations required. To access database
data, DAL is used.

###  Theory

To develop a new callout based on this class, you only have to create a new
java class that extends SimpleCallout and overwrite the following method:

    
    
     protected void execute(CalloutInfo info) throws ServletException;

With this method, you can develop the logic of the callout and use the info
object of class CalloutInfo to access window fields, database and other
methods. The most important are:

  * public String getStringParameter(String param, RequestFilter filter) : Returns the value of a field named param as an String using the filter to accept values. 
  * public BigDecimal getBigDecimalParameter(String param) throws ServletException : This method returns the value of of a field named param as a BigDecimal. 
  * public void addResult(String param, String value) : This method sets the value of a field named param with the String value indicated. 
  * public void addResult(String param, Object value) : This method sets the value of a field named param with the value indicated. This method is useful to set numbers like BigDecimal objects. 
  * public void addSelect(String param) : Starts the inclusion of values of a field named param of type select. 
  * public void addSelectResult(String name, String value) : Adds an entry to the select field and marks it as unselected. 
  * public void addSelectResult(String name, String value, boolean selected) : Adds an entry to the select field. 
  * public void endSelect() : Finish the inclusion of values to the select field. 
  * protected void showMessage(String value) : Shows a message in the browser with the value indicated. 
  * protected void showError(String value) : Shows an error message in the browser with the value indicated. 
  * protected void showWarning(String value) : Shows a warning message in the browser with the value indicated. 
  * protected void showInformation(String value) : Shows an information message in the browser with the value indicated. 
  * protected void showSuccess(String value) : Shows a success message in the browser with the value indicated. 
  * protected void executeCodeInBrowser(String value) : Executes the javascript code indicated in the value in the browser. 
  * public String getLastFieldChanged() : Returns the name of field that triggered the callout. 
  * public String getTabId() : Returns the Tab Id that triggered the callout. 
  * public String getWindowId() : Returns the Window Id that triggered the callout. 
  * public VariablesSecureApp vars : This instance field contains the VariablesSecureApp associated to the callout servlet. 

It is important to keep coherence with each expected data type (String, BigDecimal, ...)

See the following class as an example of a class that currently uses
SimpleCallout:  [SL_Project_Service](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/erpCommon/ad_callouts/SL_Project_Service.java){target="\_blank"}. This callout simply takes the numeric value of two fields,calculates the sum and writes it into another field. This is the interesting part of the code that performs the logic:

    
     @Override
     protected void execute(CalloutInfo info) throws ServletException { 
     
         BigDecimal serviceSerCost = info.getBigDecimalParameter("inpservsercost");
         BigDecimal serviceOutCost = info.getBigDecimalParameter("inpservoutcost"); 
     
         BigDecimal serviceTotalCost = serviceSerCost.add(serviceOutCost);
     
         info.addResult("inpservcost", serviceTotalCost);
     }

####  Extend a Callout

It is possible to implement a callout that extends from another callout. For
more information visit this [How to create a callout that extends from another callout](../../../developer-guide/etendo-classic/how-to-guides/How_to_create_a_callout_that_extends_from_another_callout.md) tutorial.
  
###  Product Search Key Calculation using SimpleCallout

Let's define the tasks that need to be performed by the callout:

  1. Retrieve the name of the product as entered by the user 
  2. Retrieve the ID of the category selected from a dropdown by the user 
  3. Get the name of the product category inside the database using the product category ID retrieved 
  4. Strip spaces out of the product and category names 
  5. Construct the Search Key 

```
    
    // the package name corresponds to the module's manual code folder 
    // created above
    package org.openbravo.howtos.ad_callouts;
     
    import javax.servlet.ServletException;
     
    import org.openbravo.utils.FormatUtilities;
    import org.openbravo.erpCommon.ad_callouts.SimpleCallout;
    import org.openbravo.base.secureApp.VariablesSecureApp;
    // classes required to retrieve product category data from the 
    // database using the DAL
    import org.openbravo.dal.service.OBDal;
    import org.openbravo.model.common.plm.ProductCategory;
     
    // the name of the class corresponds to the filename that holds it 
    // hence, modules/modules/org.openbravo.howtos/src/org/openbravo/howtos/ad_callouts/ProductConstructSearchKey.java.
    // The class must extend SimpleCallout
    public class ProductConstructSearchKey extends SimpleCallout {
     
      private static final long serialVersionUID = 1L;
     
      @Override
      protected void execute(CalloutInfo info) throws ServletException {
     
        // parse input parameters here; the names derive from the column
        // names of the table prepended by inp and stripped of all
        // underscore characters; letters following the underscore character
        // are capitalized; this way a database column named
        // M_PRODUCT_CATEGORY_ID that is shown on a tab will become
        // inpmProductCategoryId html field
        String strProductName = info.getStringParameter("inpname", null);
        String strProductCategoryId = info
                        .getStringParameter("inpmProductCategoryId", null);
     
        // inject the result into the response
        info.addResult("inpvalue", getConstructedKey(info.vars, strProductName, strProductCategoryId));
      }
     
      protected String getConstructedKey(VariablesSecureApp vars,
            String strProductName, String strProductCategoryId) {
     
        // Retrieve the product category name
        final ProductCategory productCategory = OBDal.getInstance().get(ProductCategory.class,
                strProductCategoryId);
        String strProductCategoryName = productCategory.getName();
     
        // construct full key
        String generatedSearchKey = FormatUtilities.replaceJS(strProductName
                    .replaceAll(" ", ""))
                    + "_" + strProductCategoryName.replaceAll(" ", "");
     
        // return generated key
        return generatedSearchKey;
      }
    }
``` 

## Defining the Callout within the Application Dictionary

!!!note
    You need to have only your module as "In Development" at this stage.

Using the role _System Administrator_, navigate to _Application
Dictionary > Setup > Callout_. Create a new  record as indicated by the
screenshot below:

!!!info
    The name of the callout should not have spaces or illegal javascript
    characters.  
  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Callout-3.png){: .legacy-image-style}
  
Save and navigate to the _Callout Class_ tab of the same window. You will
notice that the Java Class Name was automatically generated for you,
however, not correctly since the name could not match the _Callout_ name you
have provided. Correct it in line with your callout package/class name. See
screenshot below:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Callout-4.png){: .legacy-image-style}

  
Now Etendo knows that a callout exists and is implemented by the class you
have just specified.

Remember to perform
   
    ant export.database
    

in order for your changes to persist in your module.  
  
  
##  Associating the Callout with a Column

!!!note
    You need to have ONLY your template as "In Development" at this stage.

Using the role _System Administrator_ navigate to _Application
Dictionary_ > _Tables and Columns_ > and find the _M_Product_ DB Table. This
is the underlying table of the main tab of the _Product_ window.

Go to Column tab, find the _Name_ record and edit it. Find the  Callout
dropdown  that should at this point be empty. Select our
_Product_Construct_SearchKey_ callout and save the record:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Callout-6.png){: .legacy-image-style}

  
Do the same for the _Product Category_ record since a change in any of them
should also regenerate the Search Key.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

Remember to perform  
    
    ant export.database
    

and
    
    ant export.config.script
    

in order for your changes to persist in your template.  
  
##  Compiling the Window

Finally, for the callout to take effect, the window that uses it needs to be
recompiled and deployed to Tomcat. If using Eclipse, use the
eclipse.compile ant task and enter _Product_ into the dialog that pops up.
If manually compiling Etendo, use the
    
    ant smartbuild 
    

or  
    
    ant compile.development -Dtab=Product
    

!!!Important
    Once the compilation has finished, restart Apache Tomcat server.  

##  The Result

Using the role _System Admin_ (or your defined 'administrator' role),
navigate to the _Master Data Management_ > _Product_ window. Enter a new
product with Name = _Bon Fountain_ and leave the Name field. Notice
how the Search Key changes. Then, modify the Product Category and see how the change is reflected inside the Search Key field.


![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Callout-8.png){: .legacy-image-style}

Last, save changes.

---

This work is a derivative of [How to Create a Callout](http://wiki.openbravo.com/wiki/How_to_create_a_Callout){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
