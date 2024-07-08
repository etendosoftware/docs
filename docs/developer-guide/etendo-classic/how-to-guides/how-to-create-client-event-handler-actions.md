---
tags:
  - client event handler
  - actions
  - Etendo Classic
---

#  How to Create Client Event Handler Actions
  
##  Overview

This section discusses how to implement client side (javascript) functions which are executed before or after an event fired on a standard window of the User Interface.
  
##  Example Module

This is supported by an example module which shows examples of the code shown and discussed.

The code of the example module can be downloaded from this mercurial repository:  https://code.openbravo.com/erp/mods/org.openbravo.platform.ci/

##  Defining Client Event Handler Actions

A client event handler action is a function in javascript available through a global ID. **The global ID should be unique, it is strongly adviced to use the module's db prefix.** The action has to be defined in a javascript file
located in the module, see here for information on how to add javascript code to Etendo.

The following is an example of this kind of actions: it shows a message **after** saving a record. The message type and content depends on if we are creating or updating the record.
  
    
     
    OB.OBPFCI = {};
    OB.OBPFCI.ClientSideEventHandlers = {};
    OB.OBPFCI.PRODUCT_CATEGORY_HEADER_TAB = '189';
     
    OB.OBPFCI.ClientSideEventHandlers.showMessage = function (view, form, grid, extraParameters, actions) {
      var data = extraParameters.data;
     
      view.messageBar.keepOnAutomaticRefresh = true;
      if (extraParameters.isNewRecord) {
        // Save flow
        view.messageBar.setMessage(isc.OBMessageBar.TYPE_SUCCESS, 'New Record', 'Created Product Category with name ' + data.name);
      } else {
        // Update flow
        view.messageBar.setMessage(isc.OBMessageBar.TYPE_INFO, 'Updated Record', 'Updated Product Category with name ' + data.name);
      }
      OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
    };
     
    OB.EventHandlerRegistry.register(OB.OBPFCI.PRODUCT_CATEGORY_HEADER_TAB, OB.EventHandlerRegistry.POSTSAVE, OB.OBPFCI.ClientSideEventHandlers.showMessage, 'OBPFCI_ShowMessage');

As you can see, the action is placed in a global object, in this case the module's **dbprefix** is used. 

!!!important
    You should not use **var** before the global object definition, otherwise your var is not global. This is because the global javascript code included in Etendo is in fact executed within a function.

This kind of actions receives 5 arguments:

  * **view** : the standard view (OBStandardView) which provides access to the complete window and tab structure in a loaded window. 
  * **form** : the  OBViewForm  which contains the fields, the form can also be the form used in inline grid editing. 
  * **grid** : the  OBViewGrid  which contains the list of records loaded for the tab. 
  * **extraParameters** : extra information provided by the event handler. Its content depends on the type of event. 
  * **actions** : the stack of actions to be executed. It must **not be modified**. It must be used just for invoking `OB.EventHandlerRegistry.callbackExecutor` as shown in the code above. This ensures the correct execution of all actions. 

!!!info
    Each action is responsible of invoking `OB.EventHandlerRegistry.callbackExecutor`. If an action does not call it, the subsequent actions (if any) will not be executed.  

##  Registering, Setting an Action for an Event within a Tab

A client event handler action is linked to an event launched in a particular tab. This link is created by registering the action programmatically. Thus, it is possible to:

  * Add more than one action for a particular event in a tab 
  * Override/overwrite actions defined by other modules 

A client event handler action is registered through the `OB.EventHandlerRegistry.register` method. It expects 4 parameters:

  * **tab id**
  * **event type** : the type of event that will cause the execution of the action 
  * **callback function** : the client event handler action itself 
  * **action id** : can be used to overwrite an existing action registered using the same id 
    
    OB.EventHandlerRegistry.register(OB.OBPFCI.PRODUCT_CATEGORY_HEADER_TAB, OB.EventHandlerRegistry.POSTSAVE, OB.OBPFCI.ClientSideEventHandlers.showMessage, 'OBPFCI_ShowMessage');

Some comments about this code:

  * `OB.OBPFCI.PRODUCT_CATEGORY_HEADER_TAB` is a constant we have defined which holds the ID of the Product Category  header tab. 
  * `OB.EventHandlerRegistry.POSTSAVE` is the event type. 

The **event types** currently supported are:

  * **OB.EventHandlerRegistry.PRESAVE** : the action will be launched before creating or updating a record in a tab of a standard window. 
  * **OB.EventHandlerRegistry.POSTSAVE** : the action will be launched after creating or updating a record in a tab of a standard window. 
  * **OB.EventHandlerRegistry.PREDELETE** : the action will be launched before deleting a record in a tab of a standard window.

In the case of PRESAVE and POSTSAVE, the **extraParameters** argument will contain the following information:

  * **data**: the values of the record (before saving it in the case of **PRESAVE** and after saving it in the case of **POSTSAVE** ) 
  * **isNewRecord**: a flag that indicates if the record is new. It can be used to distinguish between the **save** and **update** events. 

In the case of PREDELETE the **extraParameters** argument will contain the following information:

  * **recordsToDelete** : the selected records in the grid which are going to be deleted, with the values of each record. 

####  Multiple Actions Functions per Event, Call Order

The client event handler actions can have a sort property to control the call-order, if there are multiple actions for one event in the same tab.

It is, for example, set like this:

    
    
    OB.OBPFCI.ClientSideEventHandlers.showMessage.sort = 20;

Actions with a lower sort value will be executed before actions with a higher one. If an action does not have a sort defined, it gets the sort 100 by default.

####  Overriding/Replacing an Action

An action can be registered using an ID (**action id**). If there is already an action registered with the same ID for the same tab and event type then it is replaced by the new registration.

##  Examples

###  Post-save Action: Open a Tab

The following example shows how to open a new tab **after** saving a record.

    
    
     
    OB.OBPFCI.PRODUCT_HEADER_TAB = '180';
    OB.OBPFCI.ClientSideEventHandlers.openTab = function (view, form, grid, extraParameters, actions) {
      if (extraParameters.isNewRecord) {
        // Save flow
        OB.Utilities.openDirectTab(OB.OBPFCI.PRODUCT_HEADER_TAB);
      }
      OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
    };
     
    OB.OBPFCI.ClientSideEventHandlers.openTab.sort = 120;
    OB.EventHandlerRegistry.register(OB.OBPFCI.PRODUCT_CATEGORY_HEADER_TAB, OB.EventHandlerRegistry.POSTSAVE, OB.OBPFCI.ClientSideEventHandlers.openTab, 'OBPFCI_OpenTab');

In this case we are opening the  Product  window after creating a new  Product Category  . We use _extraParameters.isNewRecord_ to identify the save flow. Finally we are invoking _OB.EventHandlerRegistry.callbackExecutor_ to ensure
the execution of the subsequent actions. In addition, we are giving a sort number of 120.

###  Post-save Action: Refresh the Grid

The following example shows how to refresh the grid **after** saving or updating a record.

    
    
     
    OB.OBPFCI.COUNTRY_HEADER_TAB = '135';
    OB.OBPFCI.ClientSideEventHandlers.refreshGrid = function (view, form, grid, extraParameters, actions) {
      var viewInGridMode = !view.isShowingForm,
          callback;
     
      callback = function () {
        OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
      };
     
      if (viewInGridMode) {
        grid.refreshGridFromClientEventHandler(callback);
      }
    };
     
    OB.EventHandlerRegistry.register(OB.OBPFCI.COUNTRY_HEADER_TAB, OB.EventHandlerRegistry.POSTSAVE, OB.OBPFCI.ClientSideEventHandlers.refreshGrid, 'OBPFCI_RefreshGrid');

Note that we are making use of a function of the grid called _refreshGridFromClientEventHandler_ , that is a special grid refresh method adapted to be used within this type of actions.

This way, we are forcing the grid in the header of the  Country and Region window to be refreshed every time a new record is created/updated on it by using the grid view.

###  Pre-save Action: Client Validation

In this example, we are checking a user's e-mail **before** saving/updating a record.

    
    
     
    OB.OBPFCI.USER_HEADER_TAB = '118';
    OB.OBPFCI.ClientSideEventHandlers.validateEmail = function (view, form, grid, extraParameters, actions) {
      var data = extraParameters.data,
          emailPattern = /^\w+([\.\-]?\w+)*@\w+([\.\-]?\w+)*(\.\w{2,3})+$/;
     
      if (data.email && !emailPattern.test(data.email)) {
        view.messageBar.setMessage(isc.OBMessageBar.TYPE_ERROR, 'Invalid Email', 'The email address ' + data.email + ' is not valid');
        return; // Interrupting save action: not calling OB.EventHandlerRegistry.callbackExecutor
      }
      OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
    };
     
    OB.EventHandlerRegistry.register(OB.OBPFCI.USER_HEADER_TAB, OB.EventHandlerRegistry.PRESAVE, OB.OBPFCI.ClientSideEventHandlers.validateEmail, 'OBPFCI_ValidateEmail');

Note that if the e-mail is not valid, we do not call _OB.EventHandlerRegistry.callbackExecutor_ so the save operation will **not** be performed.

###  Pre-save Action: Calling Server Side

In this case we are going to call a server side action **before** saving a Goods Shipment  line. To understand this example is important to know the concept of  Action Handler  .

    
    
     
    OB.OBPFCI.GOODS_SHIPMENT_LINES_TAB = '258';
    OB.OBPFCI.ClientSideEventHandlers.checkStorageBin = function (view, form, grid, extraParameters, actions) {
      var data = extraParameters.data,
          callback, storageBin;
     
      if (data.storageBin) {
        storageBin = data.storageBin;
      }
     
      callback = function (response, cdata, request) {
        var row, stack, level;
        if (cdata && cdata.storageBinInfo) {
          row = cdata.storageBinInfo.row;
          stack = cdata.storageBinInfo.stack;
          level = cdata.storageBinInfo.level;
          if (row !== '0') {
            view.messageBar.setMessage(isc.OBMessageBar.TYPE_ERROR, 'Invalid Storage Bin', 'Only storage bins with Row 0 are allowed');
            return; // Interrupting save action: not calling OB.EventHandlerRegistry.callbackExecutor
          }
          view.messageBar.setMessage(isc.OBMessageBar.TYPE_INFO, 'Shipment Line Saved', 'Storage Bin Info: Row ' + row + ', Stack ' + stack + ', Level ' + level);
          OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
        }
      };
     
      // Calling action handler
      OB.RemoteCallManager.call('org.openbravo.platform.ci.actionhandler.GoodsShipmentLinesActionHandler', {
        storageBinId: storageBin
      }, {}, callback);
     
    };
     
    OB.EventHandlerRegistry.register(OB.OBPFCI.GOODS_SHIPMENT_LINES_TAB, OB.EventHandlerRegistry.PRESAVE, OB.OBPFCI.ClientSideEventHandlers.checkStorageBin, 'OBPFCI_CheckStorageBin');

The above example calls to  GoodsShipmentLinesActionHandler  . This action handler returns the row, stack and level of the storage bin whose id has been sent in the request. This id has been retrieved from the goods shipment line
that we are about to save.

The record will **not** be saved if the storage bin row is not 0. Otherwise, we show a message with the storage bin information.

###  Pre-delete Action: Client Validation
  
In this case we are going to call a server side action **before** deleting a Sales Order  line. As in the previous example, to understand this one is important to know the concept of  Action Handler  .

    
     
    OB.CancelAndReplace.ClientSideEventHandlersPreDelete.showMessage = function (view, form, grid, extraParameters, actions) {
      var selectedRecords = extraParameters.recordsToDelete,
          record, replacementRecords = [],
          record, deliveredQuantity;
     
      view.messageBar.keepOnAutomaticRefresh = true;
     
      callback = function (response, cdata, request) {
        for (i = 0; i < cdata.result.length; i++) {
          record = cdata.result[i].record;
          deliveredQuantity = cdata.result[i].deliveredQuantity;
          if (deliveredQuantity !== 0) {
            var msgInfo = [];
            msgInfo.push(record.lineNo);
            msgInfo.push(record.product$_identifier);
            view.messageBar.setMessage(isc.OBMessageBar.TYPE_ERROR, null, OB.I18N.getLabel('CannotDeleteLineWithDeliveredQtyInReplacementLine', msgInfo));
            return;
          }
        }
        OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
      };
     
      if (view.getParentRecord().documentStatus === 'TMP') {
        for (i = 0; i < selectedRecords.length; i++) {
          record = selectedRecords[i];
          if (record.replacedorderline) {
            replacementRecords.push(record);
          }
        }
     
        if (replacementRecords.length) {
          //Calling action handler
          OB.RemoteCallManager.call('org.openbravo.common.actionhandler.CancelAndReplaceGetCancelledOrderLine', {
            records: replacementRecords
          }, {}, callback);
        } else {
          OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
        }
      } else {
        OB.EventHandlerRegistry.callbackExecutor(view, form, grid, extraParameters, actions);
      }
    };
     
    OB.EventHandlerRegistry.register(OB.CancelAndReplace.SALES_ORDERLINES_TAB, OB.EventHandlerRegistry.PREDELETE, OB.CancelAndReplace.ClientSideEventHandlersPreDelete.showMessage, 'OBCancelAndReplace_ShowMessage');

---

This work is a derivative of [How to Create Client Event Handler Actions](http://wiki.openbravo.com/wiki/How_to_create_client_event_handler_actions){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.