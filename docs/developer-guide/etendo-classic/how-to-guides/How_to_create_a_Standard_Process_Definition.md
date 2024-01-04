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

  

#  How to create a Standard Process Definition

##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  Steps to implement the Process 
    * 3.1  Overview 
    * 3.2  Implementation 
      * 3.2.1  Defining the Process 
      * 3.2.2  Adding Parameters 
      * 3.2.3  Adding it to the Menu 
      * 3.2.4  Java Implementation 
        * 3.2.4.1  Response 
          * 3.2.4.1.1  Validations 
          * 3.2.4.1.2  Returning Several Actions 
  * 4  Testing the Process 
  * 5  Advanced Topics 
    * 5.1  Invoke the Process from a Tab 
    * 5.2  Read Only and Display Logic 
    * 5.3  Subordinated Combos 
    * 5.4  Parameter Grouping 
    * 5.5  Showing results in the process window itself 
    * 5.6  Placing a parameter in a particular column 
    * 5.7  Invoking a client side validation before calling the action handler 
    * 5.8  Invoking a function when a non-grid parameter is changed 
    * 5.9  How to set the value of non-grid parameters programmatically 
    * 5.10  Invoking a function when all the non-grid parameters have been initialized 
    * 5.11  Invoking a function when the process needs to be refreshed 
    * 5.12  Invoking when a grid parameter is loaded for the first time 
    * 5.13  Specifying the number of rows displayed in a grid parameter 
    * 5.14  Defining a display logic for the fields of a grid parameter 
    * 5.15  Specifying a default value for the filter of a parameter grid field 
    * 5.16  Hiding the parameter name of a grid parameter 
    * 5.17  Adding new buttons 
    * 5.18  Multi Record Process 
    * 5.19  Uploading files 
    * 5.20  Downloading files 
  * 6  Limitations 
    * 6.1  References 
    * 6.2  UI Logic 
  * 7  Migrating old Processes 

  
---  
  
##  Introduction

_Standard_ UI pattern of _Process Definition_ allows to create Parameter
Windows defined in Application Dictionary, the UI for this windows is
generated on demand so once defined those parameters, developer only needs to
take care about process implementation.

This how to will add a new Standard Process Definition and create a menu entry
to invoke it.

The implementation requires development experience. See the following concept
pages for background information on action handlers and javascript
development:

  * Action Handler 
  * Client_Side_Development_and_API 
  * JavaScript_Coding_Conventions 

It also makes sense to study the following page:  Openbravo_3_Architecture  .

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **3.0MP20**  
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

_Standard Process Definition_ processes take advantage of the same foundation
concepts in the Application Dictionary, allowing to define parameters for the
process as meta data that generates the UI when it is required without need of
generate code, compile nor restart tomcat to apply the changes when
developing.

This example process will have the following parameters:

  * Min and Max Qty: two mandatory integer fields. 
  * Orders: a search that allows to select several orders at the same time. 
  * Business Partner: a regular business partner selector. 

When _Done_ button is clicked the process is executed:

  * It verifies in backend max qty field is greater than min qty. In case they are not, a validation error is sent back to the client asking the user to fix the values before continuing. 
  * If previous validation is satisfied: 
    * Total amount of all selected orders is summed and displayed in a message in the parameter window. 
    * If a business partner is selected, Business Partner window is opened within the selected one and a message is shown in this window. 

###  Implementation

####  Defining the Process

  * Open _Process Definition_ window 
  * Create a new record 
  * Define the UI pattern: _Standard (Parameters defined in Dictionary)_
  * Set the Handler: ` org.openbravo.client.application.examples.StandardProcessActionHandler ` . This is the Java class implementing the process that will be invoked when user clicks on the action button. 
  * Save 

####  Adding Parameters

  * _Min Qty_ parameter 
    * Move to Parameters tab 
    * Create a new record 
    * Name: Min Qty. This is the name that will be shown in UI for this parameter. 
    * Internal Name: min. It is the internal name that will be used to retrieve the value in the java class. 
    * Sequence Number: 10. Defines the position of this field in the Parameter window in relation with the rest of fields. 
    * Reference: Integer. Defines both the data type the parameter will hold and how this parameter is visualized and behaves in the UI. 
    * Mandatory: true. Will force the parameter to have a value before allowing to submit the info to the process. 
    * Default value: 0. It is the value that will take the parameter by default. It is a javascript expression evaluated in the server side, like  Default Filter Expressions  used in selectors. 
  * Follow similar steps to create _Max Qty_ field 
  * _Orders_ multi selector 
    * Create a  Multi Order  selector 
    * Create a new parameter 
    * Reference: OBUISEL_Multi Selector Reference 
    * Reference Search Key: Multi Order Selector 
  * Business Partner parameter has _OBUISEL_Selector Reference_ as Reference and _Business Partner not filtered by default by customer/vendor_ as Reference Search Key 

####  Adding it to the Menu

Adding a process to the menu allows to open it from menu as a new tab.

  * In _Menu_ window create a new entry 
  * Action: Process Definition 
  * Process Definition: Example Parameter Process 

####  Java Implementation

As mentioned earlier you should be confident with the concept of an  action
handler  .

In the case of a Process Definition action handler, you must extend from
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
     * All portions are Copyright (C) 2013 Openbravo SLU
     * All Rights Reserved.
     * Contributor(s):  ______________________________________.
     ************************************************************************
     */
    package org.openbravo.client.application.examples;
     
    import java.math.BigDecimal;
    import java.util.Map;
     
    import org.apache.log4j.Logger;
    import org.codehaus.jettison.json.JSONArray;
    import org.codehaus.jettison.json.JSONException;
    import org.codehaus.jettison.json.JSONObject;
    import org.openbravo.client.application.process.BaseProcessActionHandler;
    import org.openbravo.dal.service.OBDal;
    import org.openbravo.erpCommon.utility.OBMessageUtils;
    import org.openbravo.model.common.order.Order;
     
    public class StandardProcessActionHandler extends BaseProcessActionHandler {
      private static final Logger log = Logger.getLogger(StandardProcessActionHandler.class);
     
      @Override
      protected JSONObject doExecute(Map<String, Object> parameters, String content) {
        try {
          JSONObject result = new JSONObject();
     
          JSONObject request = new JSONObject(content);
          JSONObject params = request.getJSONObject("_params");
     
          // Do validations on param values
          double min = params.getDouble("min");
          double max = params.getDouble("max");
     
          if (max < min) {
            // In case validations are not satisfied, show an error message and allow user to fix
            // parameters
            result.put("retryExecution", true);
     
            JSONObject msg = new JSONObject();
            msg.put("severity", "error");
            msg.put(
                "text",
                OBMessageUtils.getI18NMessage("OBEXAPP_MinGtMax", new String[] { Double.toString(min),
                    Double.toString(max) }));
            result.put("message", msg);
            return result;
          }
     
          // Execute process and prepare an array with actions to be executed after execution
          JSONArray actions = new JSONArray();
     
          // 1. Sum amounts of all orders and show a message in process view
          JSONArray orders = params.getJSONArray("orders");
          BigDecimal totalAmnt = BigDecimal.ZERO;
          for (int i = 0; i < orders.length(); i++) {
            String orderId = orders.getString(i);
            Order order = OBDal.getInstance().get(Order.class, orderId);
            totalAmnt = totalAmnt.add(order.getGrandTotalAmount());
          }
          JSONObject msgTotal = new JSONObject();
          msgTotal.put("msgType", "info");
          // XXX: these two messages should be translatable, like OBEXAPP_MinGtMax above
          msgTotal.put("msgTitle", "Selected Orders");
          msgTotal.put("msgText", "Total amount: " + totalAmnt.toString());
     
          JSONObject msgTotalAction = new JSONObject();
          msgTotalAction.put("showMsgInProcessView", msgTotal);
     
          actions.put(msgTotalAction);
     
          // 2. If business partner is not null, open it in BP window and show a message in new tab
          if (!params.isNull("bp")) {
            String bpId = params.getString("bp");
            JSONObject recordInfo = new JSONObject();
            recordInfo.put("tabId", "220");
            recordInfo.put("recordId", bpId);
            recordInfo.put("wait", true);
     
            JSONObject openTabAction = new JSONObject();
            openTabAction.put("openDirectTab", recordInfo);
     
            actions.put(openTabAction);
     
            JSONObject msgInBPTab = new JSONObject();
            msgInBPTab.put("msgType", "success");
            msgInBPTab.put("msgTitle", "Process execution");
            msgInBPTab.put("msgText", "This record was opened from process execution");
     
            JSONObject msgInBPTabAction = new JSONObject();
            msgInBPTabAction.put("showMsgInView", msgInBPTab);
     
            actions.put(msgInBPTabAction);
          }
     
          result.put("responseActions", actions);
     
          return result;
        } catch (JSONException e) {
          log.error("Error in process", e);
          return new JSONObject();
        }
      }
    }

#####  Response

` ActionHandler ` s return a ` JSONObject ` with the actions to be performed
after execution.

######  Validations

It is possible to do validations in the backend before executing the actual
process, when these validations are not satisfied, a message can be shown in
the UI to allow the user to fix the problematic values.

When validations are not satisfied ` retryExecution: true ` property is
included in the response. This allows the user to fix data and resubmit again.
Additionally, a message can be added to show more information about the issue.
The response would look similar to this:

    
    
     
    {
      "retryExecution": true,
      "message": {
        "severity": "error",
        "text": "Min value (80.0) cannot be greater than Max value (10.0)"
      }
    }

######  Returning Several Actions

After executing the process, it is possible to perform a series of actions.
Additional information can be found  here  . The response should look like:

    
    
     
    {
      "responseActions": [{
        "showMsgInProcessView": {
          "msgType": "info",
          "msgTitle": "Selected Orders",
          "msgText": "Total amount: 3020482.63"
        }
      }, {
        "openDirectTab": {
          "tabId": "220",
          "recordId": "A6750F0D15334FB890C254369AC750A8",
          "wait": true
        }
      }, {
        "showMsgInView": {
          "msgType": "success",
          "msgTitle": "Process execution",
          "msgText": "This record was opened from process execution"
        }
      }, {
        "refreshGrid": {
        }
      }, {
        "refreshGridParameter": {
          "gridName": "gridParameterName"
        }
      }]
    }

  * **` responseActions ` ** . It is the name of the ` JSONArray ` that indicates a series of actions will be performed after execution. Each of the items in the array is one action, different kinds of actions can be executed. It is also possible to  extend through modules  the possible actions to be performed: 
    * **` showMsgInProcessView ` ** . Shows a message in the same tab the process was invoked from. In case the process is opened from menu, this message will be seen in the window where the values for the parameters are provided; if the process is invoked from a button in a tab, the message will be shown in that tab. 
    * **` openDirectTab ` ** . Opens a new tab ( ` tabId ` , it is possible to indicate the record to open in that tab ( ` recordId ` ). The ` wait: true ` property indicates next action will not be started till this one finishes. Optionally, you can also include a criteria object to automatically add a removable filter to the open tab (a criteria is an object which describes a filter in a grid. You can find more information about them  here  . 
    * **` showMsgInView ` ** . Shows a message in the recently opened tab. 
    * **` refreshGrid ` ** . Refreshes the grid where the process button is defined. From PR15Q1 on, grids are not automatically refreshed after invoking a standard process, only the selected record is refreshed. If the process adds or removes records from that grid, then it must add the refreshGrid to the list of response actions to see the updated data in the grid. 
    * **` refreshGridParameter ` ** . Refreshes the **grid parameter** with name ` gridName ` present in the standard process parameter window. This kind of response is specially useful for those parameter windows which are not closed after the execution of the **action handler** (the parameters are visible after the process execution), for example those process definitions which are directly opened from the menu. This response action is available from **PR17Q1** . 

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q2  ** .  
---|---  
  
The _getResponseBuilder()_ method is available for classes extending
_BaseProcessActionHandler_ . This method returns a helper that can be used to
build the result of the process with the desired standard response actions in
an easy way. For example:

    
    
     
      @Override
      protected JSONObject doExecute(Map<String, Object> parameters, String content) {
        ...
        ...
        return getResponseBuilder()
            .showMsgInProcessView(MessageType.INFO, "Message Title", "This is a sample message")
            .openDirectTab("220", false).build();
      }

##  Testing the Process

After compiling and deploying (because a new java class is added, note this is
not needed in case of just editing/adding paramters).

There is a new entry in the menu: _Example Param Process_ , this entry opens
the parameter window where all defined parameters are shown and a _Done_
button is presented to submit values set for them. When the process is
executed:

  * If Max Qty is greater the Min Qty, a message is shown and the process can be submited again. 
  * A message in the parameter window is shown summing the amounts of all selected orders. 
  * If a business partner is selected, it is opened in a new tab displaying a message on it. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Standard_Process_Definition-2.png){: .legacy-image-style}

##  Advanced Topics

###  Invoke the Process from a Tab

Standard Process Definition processes can be opened as a tab from the menu or
as a modal popup from a button in a tab. This second option can be achieved by
adding an extra column to the table used in the tab. More details on how to do
it can be found  here  .

###  Read Only and Display Logic

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Read Only logic is available from **3.0MP25**  
---|---  
  
Parameters in Process Definition support display and read only logic. This
allows to show or hide and to make editable or read only parameters based on
values entered for other parameters.

###  Subordinated Combos

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Subordinated Combos are available from **3.0MP25**  
---|---  
  
The data that can be selected within a combo (selector) can be restricted
based on values other parameters take using "Validation Rules". Logic of these
validations is a HQL that is appended to its datasource. This is written in
javascript being posible to use OBBindings, in the same way default value is
written.

###  Parameter Grouping

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Parameter Grouping logic is available from **3.0MP25**  
---|---  
  
It is possible to do groups of parameters in the UI, by using the _Field
Group_ property when defining the paramter.

###  Showing results in the process window itself

It is possible to show the result of a process directly in the process window
itself. This makes sense if the parameter section is small and you want to
display directly.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Standard_Process_Definition-6.png){: .legacy-image-style}

  
To accomplish this the data/json object returned from the server handler
should set this parameter 'showResultsInProcessView' to true. It also makes
sense to 'retryExecution' parameter to true:

    
    
    {
      "retryExecution": true,
      "showResultsInProcessView": true
    }

The called java script method gets an object with a _processView property
which refers back to the overall process view. From the process view you can
get to the resultLayout to show the result. The resultLayout is a Smartclient
HLayout.

For example, a return action:

    
    
    OB.Utilities.Action.set('openSaikuReport', function(paramObj) {
      var i, queries = paramObj.queries,
          processView = paramObj._processView,
          mainLayout = processView.resultLayout, reportView;
     
      reportView = isc.OBANALY_ShowSaikuReport.create({
        parameters: paramObj,
        queries: queries
      });
      mainLayout.addMember(reportView);

###  Placing a parameter in a particular column

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
The _Column Number_ field of the Parameter tab allows you to specify the
column where the parameter should be placed. Grid parameters use always the
four columns of the form, so this field does not apply to them.

###  Invoking a client side validation before calling the action handler

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
The _Client Side Validation_ field of the Process Definition tab allows you to
define a function that will be executed before the request to the action
handler is done. You can use this function to do client side validations.

This function must accept 3 parameters:

  * the parameter window object. I.e., if you name this parameter 'view', then the form of the parameter window will be accessible via 'view.theForm'. You can retrieve the value of a particular parameter using 'view.theForm.getItem(parameter_name).getValue()' 
  * a validation success callback. If the current values of the form passes the validation, you must invoke this callback 
  * a validation failure callback (from **PR15Q1.3** ). If form values don't satisfy the validation, you must invoke this callback. 

For instance:

    
    
    OB.Utilities.TestClientSideValidation = function (view, actionHandlerCall, failureCallback) {
      var minNumber, maxNumber;
      minNumber = view.theForm.getItem('min_number').getValue();
      maxNumber = view.theForm.getItem('max_number').getValue();
      if (maxNumber >= minNumber) {
        // only execute the callback if the form values pass the validation
        actionHandlerCall();
      } else {
        failureCallback();
      }

In addition, starting from version **PR17Q3** client side validation functions
support a fourth parameter that contains additional information, like the
pressed button:

    
    
    OB.Utilities.TestClientSideValidation = function (view, actionHandlerCall, failureCallback, additionalInfo) {
      if (additionalInfo.buttonValue === 'OK') {
        // execute validations related to the 'OK' button
      } else {
        // do another validations
      }

To learn how to define new buttons in a standard process definition window,
see  here  .

From **PR20Q3** additional information can be added to the payload the process
will receive. For example this code would add a new parameter named myParam:

    
    
     
      view.externalParams = { myParam:'value' };

###  Invoking a function when a non-grid parameter is changed

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
The _On Change Function_ field of the Parameter tab allows you to define a
function that will be executed when a non-grid parameter is updated, after the
parameter loses its focus. This function can be used to do validations or to
implement client side callouts, among other things.

The function must accept four parameters:

  * item: the item that has been modified 
  * view: the parameter window object 
  * form: the form that contains the item 

###  How to set the value of non-grid parameters programmatically

It is possible to execute an _On Change Function_ , besides when the parameter
loses its focus, when setting the parameter value programmatically.

When setting the value of a parameter from code, it is recommended to use the
**setValueProgrammatically()** function. This way, if the parameter has an _On
Change Function_ , it will be executed after setting the parameter value.

    
    
     
      var issotrx = form.getItem('issotrx');
      // Set the value for the item
      // If the 'issotrx' parameter has an 'On Change Function' it will be executed also
      issotrx.setValueProgrammatically('Y');

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
_setValueProgrammatically()_ method is available from **PR16Q1**  
---|---  
  
###  Invoking a function when all the non-grid parameters have been
initialized

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
The _On Load Function_ field of the Process Definition tab allows you to
define a function that will be executed once the parameters have been
initialized.

###  Invoking a function when the process needs to be refreshed

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q4**  
---|---  
  
The _On Refresh Function_ field of the Process Definition tab allows you to
define a function that will be executed when the parameter window refresh
action be invoked.

For example, if the process has a child-process, once the child-process
finishes, it will invoke a refresh of the parent process.

Since each process has its particularities, a custom refresh function should
be defined in case the process be susceptible of being refreshed/reloaded.

The function must accept, at least, one parameter:

  * view: the parameter window object 

###  Invoking when a grid parameter is loaded for the first time

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
The initialization of the grid parameters is done asynchronously, so when the
general onLoadFunction is invoked, it is not certain whether all the grid
parameters have been loaded with their initial data. If you need to execute
some code right after a grid is loaded for the first time, you should use the
_On Grid Load Function_ field. The function used here must accept one
parameter, the grid itself.

For example:

    
    
    OB.Utilities.TestOnGridLoad = function (grid) {
      var nRecordsReceived = grid.getData().getLength(),
          messageBar = grid.view.messageBar;
      messageBar.setMessage('info', 'The grid has been loaded with ' + nRecordsReceived + ' records');
    }

###  Specifying the number of rows displayed in a grid parameter

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
You can set the number of rows that should be shown at the first time in a
grid parameter using the _Number of Displayed Rows_ field. This field is used
just for setting the height of the grid, if the grid has actually more rows
than the Number of Displayed Rows, a scrollbar will be shown. The default
value for this field is 5.

It is not possible to define the colspan of the grid parameters, because they
always use the four available columns of the form.

###  Defining a display logic for the fields of a grid parameter

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
The _Display Logic for Grid Column_ field in the Field tab allows to define a
display logic for the fields of grid parameters.

For instance, suppose that you have defined a parameter window with two
parameters:

  * a boolean called Show Advanced Columns (column name showAdvancedColumns 
  * a grid. 

Let's suppose the grid has some fields that should be displayed only if the
Show Advanced Column flag is checked. The Display Logic for Grid Column field
of these fields should be set to:

    
    
    @showAdvancedColumns@='Y'

  

###  Specifying a default value for the filter of a parameter grid field

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
The _Default Filter Expression_ field of the Field tab allows to define a
default value for the filter of a field. This default value can be a constant,
depend from another parameter or use OBBindings.

###  Hiding the parameter name of a grid parameter

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **PR14Q3**  
---|---  
  
Although it is possible to define several grid parameters in a parameter
window, it is likely that most of the times there will be at most one (for
instance in pick and execute windows). In those cases, you might consider not
showing the name of the grid parameter. You can do this by unckecking the flag
'Show Title' in the Parameter tab.

###  Adding new buttons

By default, process definitions have a single "Done" button (and a "Cancel"
one in case they are shown in a popup from a standard window). It is possible
to change that button or to add new ones.

To do it you can:

  1. Create a new _Reference_ with _Button List_ as _Parent Reference_ . In the _List Reference_ add as many records as buttons to be displayed in the process. The name of these elements will be seen in the button's label whereas the _Search Key_ is the value that will be sent to the _Handler_ in the backend within the ` _buttonValue ` field. 
  2. Add a new parameter to the process with _Button List_ as reference and the new reference just created as _Reference Search Key_ . Note there should be, at most, only one parameter of _Button List_ type. 

###  Multi Record Process

A standard process can be defined as multi record process to be able to
execute it for more than one record.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q2  ** .  
---|---  
  
###  Uploading files

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR22Q2  ** .  
---|---  
  
Process definitions can receive files as parameters. To do that, add a
'Process File upload' Reference as a process parameter. This parameter will
show a file upload element in the process form where you can upload a single
file.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Standard_Process_Definition-20.png){: .legacy-image-style}

By default, files uploaded using this component are limited to be 10MB at
most. To override this configuration, you can set the Preference **Maximum
Process File Upload size (MB)** and change this value. File size validation
will be performed both client-side and server-side.

Once uploaded a file, file contents and additional data will be available as a
parameter entry in the **doExecute(parameters, content)** function in the
Process Event Handler. The entry corresponding to the file upload will contain
a Map with the following information:

    
    
    Map<String, Object> params = (Map<String, Object>) parameters.get(paramName);
     
    String fileName = params.get(PARAM_FILE_NAME); // The file name
    InputStream content = params.get(PARAM_FILE_CONTENT); // The content of the file as an Stream
    Long size = params.get(PARAM_FILE_SIZE); // The file size in bytes

  

###  Downloading files

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR23Q3  ** .  
---|---  
  
Process definition has the ability to generate and download a file.

In this case of Process Definition, you must extend from
FileExportActionHandler and implement the generateFileToDownload and
getDownloadFileName methods.

    
    
     
     
    /**
     * Action handler example to export a file from a process definition
     */
    public class ExportFileExample extends FileExportActionHandler {
      private static final String FILE_PREFIX = "Test";
      private static final String FILE_EXTENSION = ".txt";
     
      @Override
      protected Path generateFileToDownload(Map<String, Object> parameters, JSONObject data)
          throws IOException, JSONException {
        String tmpFileName = UUID.randomUUID().toString() + FILE_EXTENSION;
        File file = new File(ReportingUtils.getTempFolder(), tmpFileName);
        try (FileWriter outputfile = new FileWriter(file)) {
          outputfile.write("Hello World!");
        }
        return file.toPath();
      }
     
      @Override
      protected String getDownloadFileName(Map<String, Object> parameters, JSONObject data) {
        return FILE_PREFIX + FILE_EXTENSION;
      }
    }

If the process definition is launched from a button in a standard window with
a header and lines and it is not configured as multi-record, the generated
file will be attached to the header by default.

This behavior can be modified overriding the method uploadAttachment.

    
    
     
     
     @Override
      protected void uploadAttachment(Path originalFile, Map<String, Object> parameters,
          JSONObject data) throws IOException, JSONException {
     
      }
     

See example:  ExportFileExample

##  Limitations

###  References

Currently, not all references available in Standard windows are available in
Process Definition. The following ones cannot be used as parameters:

  * Button: the mechanism to add new buttons is described  here  . 
  * Image 
  * Masked String 
  * Table 
  * TableDir 
  * Tree 
  * 2.50 based components, like the  Location  selector 

Some other ones are supported starting from an older release:

  * List, starting from 3.0PR14Q2 

###  UI Logic

Callouts are not implemented for parameters.

  

##  Migrating old Processes

Starting from  3.0PR14Q3  Process Definitions support several parameters.
Previous to this release, they supported either no parameter or a single grid
parameter. In order to implement this support, the way grid parameter value is
sent to backend was changed and a new _Compatibility with Legacy Grids_ flag
was added, all processes defined before 3.0PR14Q3 were defaulted to be
compatible and processes defined afterwards are not by default.

To migrate grid legacy compatible processes to new format, set _Compatibility
with Legacy Grids_ to false and depending on the case:

  * If the process' _UI Pattern_ is _Manual_ , no other change is needed. 
  * If the process has no parameter, no other change is needed. 
  * If the process has a (grid) parameter, the JSON that ` doExecute ` method receives changes these are the required modifications: 

Old code  |  New code  
---|---  
      
    
         
      JSONObject gridInfo = new JSONObject(content);
     
     
     
     
      JSONArray gridSelection = gridInfo.getJSONArray("_selection");
      JSONArray gridAllRows = gridInfo.getJSONArray("_allRows");

|

    
    
      
      JSONObject params = new JSONObject(content).getJSONObject("_params");
     
      // Replace here gridColumnName with the actual DB Column Name for your grid parameter
      JSONObject gridInfo = params.getJSONObject("gridColumnName");
     
      JSONArray gridSelection = gridInfo.getJSONArray("_selection");
      JSONArray gridAllRows = gridInfo.getJSONArray("_allRows");  
  
Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Standard_Process_Definition  "

This page has been accessed 42,381 times. This page was last modified on 31
May 2023, at 11:07. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

