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

  

#  How to create a Pick and Execute Process

##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  Steps to implement the Process 
    * 3.1  Overview 
    * 3.2  Implementation 
      * 3.2.1  Defining the Window 
      * 3.2.2  Defining the Reference 
      * 3.2.3  Defining the Process 
        * 3.2.3.1  Parameters 
      * 3.2.4  Adding a button to Sales Order 
        * 3.2.4.1  Create a Column 
        * 3.2.4.2  Create a Field 
      * 3.2.5  Java Implementation 
  * 4  Testing the Process 
  * 5  Advanced Topics 
    * 5.1  Selecting by default 
    * 5.2  Validation Function 
      * 5.2.1  JavaScript Definition 
    * 5.3  Selection Function 
    * 5.4  Performing Several Actions after Execution 

  
---  
  
##  Introduction

_Pick and Execute (P &E) _ is a case of  _Process Definition_ with _Standard_
UI pattern  .

This how to will add a new Pick and Execute process and associate it with the
Sales Order window.

The implementation requires development experience. See the following concept
pages for background information on action handlers and javascript
development:

  * Action Handler 
  * Client_Side_Development_and_API 
  * JavaScript_Coding_Conventions 

It also makes sense to study the following page:  Openbravo_3_Architecture  .

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
Pick and Execute processes explained in this how to, is available from
**3.0MP6**  
---|---  
  
##  Example Module

This howto is supported by an example module which shows examples of the code
shown and discussed.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), for more information see the  Examples Client
Application  project page.

##  Steps to implement the Process

###  Overview

The P&E processes take advantage of the same foundation concepts in the
Application Dictionary. We'll be using the _Window, Tabs and Fields_ for
defining the editable grid that will be shown, a new _Reference_ for the
parameter of the process; and then implementing an _action handler_ that will
get executed when the user hits the "Done" button.

###  Implementation

####  Defining the Window

  * Create a new window 
  * Fill the required fields 
  * Select **Pick and Execute** as window type 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-1.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-2.png){: .legacy-image-style}

  * Following the same concepts, you require have a **Table** as your data-source. Note: If you need to mix information from several tables, you have different options: 
    * A database view used to create a table in  Application Dictionary  . 
    * A table based on an  HQL query 
    * A table based on a  manual datasource 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-3.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-4.png){: .legacy-image-style}

  * Create the necessary fields that will turn into the columns of the grid. Pick a **Column** and pay attention to some important properties: 
    * **Displayed:** This must be checked in order to generate a field. If Displayed is unchecked no field will be generated. 
    * **Read Only:** Most of the times all the fields will be read-only. If you want a user to be able to modify some data, e.g. quantity leave it unchecked 
    * **Show in Grid View:** Defines if the field will be shown in the grid. You can define a Field as displayed but not shown in grid, so a field will get generated but not shown. This is useful for retrieving data to the grid and send it to the process. 
    * **Grid Position:** Defines the sequence of the fields in the grid 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-5.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-6.png){: .legacy-image-style}

####  Defining the Reference

After defining the window, you need to define a new Reference.

  * Create a new Reference 
  * Select in the Base Reference drop down: Window Reference 
  * Save 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-7.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-8.png){: .legacy-image-style}

  * Move to Window tab 
  * Create a new record 
  * Select your newly created window 
  * Save 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-9.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-10.png){: .legacy-image-style}

####  Defining the Process

There is a new window for processes: **Process Definition**

  * Open the Process Definition window 
  * Create a new record 
  * Define the UI pattern: Standard (Parameters defined in Dictionary) 
  * Set the Handler (Java class implementing the process) 
  * Save 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-11.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-12.png){: .legacy-image-style}

#####  Parameters

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Window Reference is the an implementation of a _rich parameter_  
---|---  
  
  * Move to Parameters tab 
  * Create a new record 
  * Fill the required fields. The name of the parameter will be the name shown in the title of the running process. 
  * Select Window Reference 
  * Pick the Window you defined previously 
  * Save 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-14.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-15.png){: .legacy-image-style}

####  Adding a button to Sales Order

#####  Create a Column

As you know, you required to have a new column to associated it to a button.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  You
can check other how-to if you are not confident with this process, e.g.
How_to_add_a_field_to_a_Window_Tab  
---|---  
  
  * Create a new column in the C_Order table. PostgreSQL syntax: 

    
    
    ALTER TABLE c_order ADD COLUMN em_obexapp_pick1 character(1);
    ALTER TABLE c_order ALTER COLUMN em_obexapp_pick1 SET DEFAULT 'N'::bpchar;

  * Go to: Tables and Columns 
  * Open the C_Order record 
  * Execute: **Create Columns from DB** process 
  * Move to the Columns Tab 
  * Pick the newly created column 
  * Change the reference from: Yes/No to Button 
  * Pick your defined process 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-17.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-18.png){: .legacy-image-style}

#####  Create a Field

  * Go to Windows, Tabs and Fields 
  * Search for Sales Order 
  * Create a new Field associated with your column 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-19.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-20.png){: .legacy-image-style}

####  Java Implementation

As mentioned earlier you should be confident with the concept of an  action
handler  .

In the case of a Pick and Execute action handler, you must extend from
**BaseProcessActionHandler** and implement the **doExecute** method.

    
    
    /*
     *************************************************************************
     * The contents of this file are subject to the Openbravo  Public  License
     * Version  1.1  (the  "License"),  being   the  Mozilla   Public  License
     * Version 1.1  with a permitted attribution clause; you may not  use this
     * file except in compliance with the License. You  may  obtain  a copy of
     * the License at http://www.openbravo.com/legal/license.html
     * Software distributed under the License  is  distributed  on  an "AS IS"
     * basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
     * License for the specific  language  governing  rights  and  limitations
     * under the License.
     * The Original Code is Openbravo ERP.
     * The Initial Developer of the Original Code is Openbravo SLU
     * All portions are Copyright (C) 2011 Openbravo SLU
     * All Rights Reserved.
     * Contributor(s):  ______________________________________.
     ************************************************************************
     */
    package org.openbravo.client.application.examples;
     
    import java.util.Map;
     
    import org.apache.log4j.Logger;
    import org.codehaus.jettison.json.JSONArray;
    import org.codehaus.jettison.json.JSONObject;
    import org.openbravo.client.application.ApplicationConstants;
    import org.openbravo.client.application.process.BaseProcessActionHandler;
     
    /**
     * @author iperdomo
     * 
     */
    public class PickExampleActionHandler extends BaseProcessActionHandler {
     
      private static final Logger log = Logger.getLogger(PickExampleActionHandler.class);
     
      @Override
      protected JSONObject doExecute(Map<String, Object> parameters, String content) {
        try {
          JSONObject request = new JSONObject(content);
     
          log.info(">> parameters: " + parameters);
          // log.info(">> content:" + content);
     
          // _selection contains the rows that the user selected.
          JSONArray selection = new JSONArray(
              request.getString(ApplicationConstants.SELECTION_PROPERTY));
     
          log.info(">> selected: " + selection);
     
          // _allRows contains all the rows available in the grid
          JSONArray allRows = new JSONArray(request.getString(ApplicationConstants.ALL_ROWS_PARAM));
     
          log.info(">> allRows: " + allRows);
     
          // A Pick and Execute process can have several buttons (buttonList)
          // You can know which button was clicked getting the value of _buttonValue
          log.info(">> clicked button: " + request.getString(ApplicationConstants.BUTTON_VALUE));
     
          return request;
        } catch (Exception e) {
          log.error("Error processing request: " + e.getMessage(), e);
        }
        return new JSONObject();
      }
    }

##  Testing the Process

Since you have changed the structure of some Entity by adding a new column,
you need to restart the tomcat server.

  * After restarting, you should be able to go to the Sales Order window and see a new button. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-21.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-22.png){: .legacy-image-style}

  * When clicking the button, a new process window shows up. The user can pick, filter, modify according to the window definition, and click "Done" 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-23.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-24.png){: .legacy-image-style}

##  Advanced Topics

###  Selecting by default

Your data-source (table or view) defined in the Tab, can set which rows will
be selected by default when the user launches the process. You just need to
create a column c_ob_selected, this will turn into a _obSelected_ property in
the generated entity. When the value of this column is ' **Y'** , the row will
be selected by default. Here you have an working example:
M_RM_RECEIPT_PICK_EDIT.xml  .

Note that when registering the column in the Application Dictionary the
**Yes/No** reference must be used.

###  Validation Function

You can define at Field level a JavaScript validation function. In an editable
field when the user enters a value, this function will get executed.

  * Go to Window, Tabs and Fields 
  * Pick your window and the tab 
  * Go to the Quantity field 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-25.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-26.png){: .legacy-image-style}

####  JavaScript Definition

  * Your Component Provider needs to register a new global resource. If you are not familiar with this, check:  Openbravo_3_Architecture#Component_Provider 
  * If your function returns false, the cell will be marked with an error 
  * In your JavaScript define a validation function, e.g. 

    
    
    OB.OBEXAPP.PNE = {};
     
    OB.OBEXAPP.PNE.validate = function (item, validator, value, record) {
      // item has access to grid: item.grid
      // from the grid you can get all selected records and edited values, e.g.
      //   * item.grid.getSelection()
      //   * item.grid.getEditedRecord()
      // grid has access to view: grid.view
      // view has access to parentWindow: view.parentWindow (the window running the process)
      // parentWindow has access to currentView
      // currentView has getContextInfo
      // debugger;
      if(window.console) {
        console.log('validation function!', value);
      }
      return true;
    };

  * More info on the capabilities of the grid in the SmartClient API documentation:  ListGrid 

###  Selection Function

You could also define a selection function, at Tab level. This function will
get called when the user select/unselect a row.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-27.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Pick_and_Execute_Process-28.png){: .legacy-image-style}

And define a JavaScript function in your loaded static .js file:

    
    
    OB.OBEXAPP.PNE.selectionChanged = function (grid, record, recordList) {
      if (window.console) {
        console.log('selection function!');
        console.log(grid, record, recordList);
      }
    };

If you want to change any value of the selected record, you have to use the
following instruction:

    
    
    grid.setEditValue(grid.getRecordIndex(record), columnName, newColumnValue)

###  Performing Several Actions after Execution

After the process is executed, a series of actions can be taken. How to do it
is explained  here  .

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Pick_and_Execute_Process  "

This page has been accessed 26,982 times. This page was last modified on 27
June 2018, at 06:14. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

