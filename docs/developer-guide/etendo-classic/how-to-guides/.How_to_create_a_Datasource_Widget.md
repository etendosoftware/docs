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

  

#  How to create a Datasource Widget

##  Contents

  * 1  Introduction 
  * 2  Developing the datasource 
    * 2.1  Implementing the Java datasource 
    * 2.2  Defining the datasource in the application dictionary 
  * 3  Developing the widget 
    * 3.1  Create the widget 
    * 3.2  Select the datasource 
    * 3.3  Create the columns 
  * 4  Adding the widget to your workspace 

  
---  
  
##  Introduction

This How To article describes how to create a new widget that fetches its data
from an user-defined datasource. The generic documentation about widgets can
be found  here  .

A related How to article explaining how to embed a widget into a generated
Window/Tab can be found in this  link  .

##  Developing the datasource

The new datasource like all developments must belong to a module.  Create a
new one  if you still don't have it.

###  Implementing the Java datasource

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  By
default Datasources cannot be executed by Portal users. To make them
accessible for portal users they must implement `
org.openbravo.portal.PortalAccessible ` interface.  
---|---  
  
This test datasource is going to return the following Data:

Row 1 - 1

Row 2 - 2

The first column is a String, and the second column is a Number.

    
    
     
    package org.openbravo.datasourceWidget;
     
    import java.util.ArrayList;
    import java.util.LinkedHashMap;
    import java.util.List;
    import java.util.Map;
     
    import org.openbravo.service.datasource.ReadOnlyDataSourceService;
     
    public class TestDatasourceForWidget extends ReadOnlyDataSourceService {
     
      /**
       * Returns the count of objects based on the passed parameters.
       * 
       * @param parameters
       *          the parameters passed in from the request
       * @return the total number of objects
       */
      @Override
      protected int getCount(Map<String, String> parameters) {
        return 2;
      }
     
      @Override
      protected List<Map<String, Object>> getData(Map<String, String> parameters, int startRow,
          int endRow) {
        List<Map<String, Object>> result = new ArrayList<Map<String, Object>>();
     
        Map<String, Object> firstRow = new LinkedHashMap<String, Object>();
        firstRow.put("column1", "Row 1");
        firstRow.put("column2", 1);
        result.add(firstRow);
     
        Map<String, Object> secondRow = new LinkedHashMap<String, Object>();
        secondRow.put("column1", "Row 2");
        secondRow.put("column2", 2);
        result.add(secondRow);
     
        return result;
      }
     
    }

###  Defining the datasource in the application dictionary

Select the module where your developments belong, give a name to the
datasource, and specify its java class name.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-1.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-2.png){: .legacy-image-style}

Datasource definition in the application dictionary.

##  Developing the widget

The new widget like all developments must belong to a module.  Create a new
one  if you still don't have it.

####  Create the widget

All the widget definition is done in the _Widget_ window.

Create a new _widget class_ :

Widget title

     is the title that appear on the widget header. Put here a short sentence that describes the widget. 
Superclass & Widget superclass

     leave the flag unchecked and select the _Query/List_ superclass widget from the drop/down menu. 
Height

     set up any value, the Query/List override this value setting up the height based on the number of rows. 
Enable for all users

     Check it if the widget has to be available to all roles. Otherwise leave unchecked and give access to the desired roles on the _Widget Access_ tab. 

As the widget is implementing a superclass widget some parameters might have
been created to the new widget. On the _Query/List_ case the _Number of Rows_
parameter is created automatically. This sets the number of rows visible on
the grid.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-3.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-4.png){: .legacy-image-style}

Widget definition

####  Select the datasource

The datasource is selected on the _Query_ tab. Select the Datasource option in
the Type field, and then select the previously defined selector in the
Datasource combo.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-5.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-6.png){: .legacy-image-style}

Setting the datasource of the widget.

####  Create the columns

Once the query is defined and the necessary parameters created is time to
define the columns that will be available on the grid on the _Column_ tab.

In this example two column have the be defined. The first one is a string
named column1 and the second one is a number named column2 (see Java
datasource definition).

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-7.png){: .legacy-image-style}

##  Adding the widget to your workspace

Once the widget is done if you have access to it you are able to add it to
your workspace. It is not needed to compile anything.

On the _Add widget_ menu select your new widget. If all the parameters have a
default value or are fixed you will see the widget added on the workspace.
Otherwise you will be prompted to fill the parameters.

This is the final result:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Datasource_Widget-8.png){: .legacy-image-style}

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Datasource_Widget  "

This page has been accessed 8,274 times. This page was last modified on 7
March 2014, at 08:06. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

