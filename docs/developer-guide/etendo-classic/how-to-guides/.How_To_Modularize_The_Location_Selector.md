---
title: "How To Modularize The Location Selector"
tags:
    - location
    - selector
    - modularization
    - module
    - customization
---
  
##  Objective

The objective of this article is to show you how to modify and modularize the
**Location Selector** .

##  Recommended articles

Before reading this guide, it is necessary to have a proper understanding of
Etendo Classic's Modularity concept and how to create and package a module, 
as we take the knowledge from these articles as a given in this guide.

In case you are working with configuration scripts or templates on a regular
basis, the following link to an article might be of interest to you, since it
describes how to create a configuration script .

##  Execution Steps

The steps needed to change and modularize the Location Selector are as
follows:

  1. Define your own **Module** and export it. The module folder will be then be generated, for example: 
    
        modules/ com.etendoerp.locationexample/
    

  2. Create the source folder for the **Module** we just created previously. For our example it should look like this: 
    
        src/ com/etendoerp/locationexample/info/
    

  3. Copy the original files of the Location Selector into the newly created folder. When copying the files, maintain the original file names. The original files are located at: 
    
        src/org/openbravo/erpCommon/info/Location
    

  4. Modify the following files to make them part of your package:   
  
**Location_Search_data.xsql** :

    
        Change the defined package to: " com.etendoerp.locationexample.info"
    

**Location.java** :

    
    Change the package to: " com.etendoerp.locationexample.info"
    
    Change the following mappings to use the new mappings:
    
    org/openbravo/erpCommon/info/Location_FS ->  com/etendoerp/locationexample/info/Location_FS
    org/openbravo/erpCommon/info/Location_F1 ->  com/etendoerp/locationexample/info/Location_F1
    org/openbravo/erpCommon/info/Location_F2 ->  com/etendoerp/locationexample/info/Location_F2
    

After that you can apply all the changes you want to do. In our example we
have just changed the labels for the fields.

!!! note **Note:**
    There is a **Trigger** _c_bpartner_location_trg_ that inserts the location name into the name field of the _c_bpartner_location_ name after any changes. That name is created using the **Function** _c_location_name_.

If you add new fields in the Location Selector and also want to use the
information to compose the name, you will need to do the following:

    * Create your own **Function** based on _c_location_name_ to compose the name that you want to save. 
    * Create your own **Trigger** based on _c_bpartner_location_trg_ to use that new function to save the name. 
    * Deactivate the _c_bpartner_location_trg_ **Trigger** and use your own one instead. 

To deactivate it, you have to delete it and then export the changes into a
**Template** set _In Development_ . At the top of the configScript.xml
template you will see that there is a line that indicates that the trigger was
removed ( _RemoveTriggerChange_ ).  
  

  5. Create a new search reference for the new files for your module and your own name. Define that new reference to use your own Java Class and your own mappings: 


![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Modularize_The_Location_Selector-1.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Modularize_The_Location_Selector-2.png){: .legacy-image-style}



![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Modularize_The_Location_Selector-3.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Modularize_The_Location_Selector-4.png){: .legacy-image-style}

  
  6. Define a new template module and mark it as _In Development_ . You can use the template we used to deactivate the Trigger: In the _**Tables and Columns** _ window, find the column which you want to use with the Locator Selector we have created and change the _**"Reference Searchkey"** _ combo to use this new reference. In the example we have done it in the _C_Bpartner_location_ table, in the _c_location_Id_ column. 
  7. Compile the application with: 
    
        ./gradlew smartbuild

  8. Restart tomcat and use the column to check that the new reference is working with the new changes. 

##  Result

Following screenshot shows the results of our changes:


![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Modularize_The_Location_Selector-5.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Modularize_The_Location_Selector-6.png){: .legacy-image-style}

