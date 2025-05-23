---
title: How to Create Jobs and Actions
tags:
    - How to
    - Jobs
    - Actions
---

## Overview

Etendo introduces the concept of Jobs which is about one or more Actions executed in sequence. These Actions are standard processes which enable the user to create and store Jobs for later usage. Jira Automations and iOS Shortcuts are similar concepts.

!!! note
    The GUI to create and execute jobs is coming soon to a newer version of Etendo. At present, it is only possible to define Actions which act as standard processes available in the existing UI nevertheless, they will also support the newer UI when released.

## Create an Action

!!! info
    Actions are based on the existing Standard Process architecture.

1.  Create a new record in the Process Definition window:

    ![createjobs1.png](../../../assets/legacy/technicaldocumentation/platform/createjobs1.png)

2.  Define UI Pattern as Action. The process has to be marked as multi record. All actions must support multi record input. The rest of the definitions are analogous to any Standard Process. Parameters, onLoad functions, etc. are supported.
3.  Create a column and a field to run the Action from a button in the current UI, or a menu entry to run the process from the menu.
4.  The Java class associated with the new Action must extend the Action type (`com.smf.jobs.Action`).

Your IDE of choice should prompt you to fill the required methods:

- `ActionResult action(JSONObject parameters, MutableBoolean isStopped)`
- `Class<T> getInputClass()`

The first `action()` method is where the main process logic happens. You will receive the process parameters in a json object, and a boolean to check if the process was requested to stop. Once the logic is done, your code should return an `ActionResult` type detailing if the execution was successfully finished or not. There will also be a message for the user.

The `getInputClass()` method must return the class type this Actions supports as an input. For example `Invoice.class:`

```plaintext

import org.openbravo.model.common.invoice.Invoice;
/* ... */
@Override
protected Class<Invoice> getInputClass() {
    return Invoice.class;
}
```

The input data (the user selected record(s), or the result of another Action) can be obtained with the method `getInputContents()`. By default, this method will return a list of `BaseOBObject`, but it can be parametrized using the previous `getInputClass()` method (or the class directly).
For example:

```plaintext

// Assuming getInputClass() returns Invoice.class
List<Invoice> invoices = getInputContents(getInputClass());
```

The `ActionResult` type can be used to show a message to the user:

```plaintext

result.setType(Result.Type.ERROR);
result.setMessage(OBMessageUtils.getI18NMessage("Success"));
/* ... */
return result;
```

The result object can also set an output to be used as input for the next job, when the new Job UI is implemented:

```plaintext

List<Invoices> invoices = processInvoices();
result.setOutput(invoices);
```

For more complex operations present in standard processes, the `setResponseActionsBuilder()` method can be used to set a response builder. This follows the same existing logic when using a `BaseProcessActionHandler` class.

The main logic of the process can be constructed as any process which previously extended the `BaseProcessActionHandler` class. It should be trivial to port existing processes to Actions.

Examples of other Actions implemented in Etendo are usually present in the `com.smf.jobs.defaults` package.

A full example of an Action java class is shown below:

```java

package com.smf.jobs.defaults;

import com.smf.jobs.ActionResult;
import com.smf.jobs.Result;
import com.smf.jobs.Action;
import org.apache.commons.lang.mutable.MutableBoolean;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;
import org.openbravo.advpaymentmngt.ProcessInvoiceUtil;
import org.openbravo.base.weld.WeldUtils;
import org.openbravo.client.kernel.RequestContext;
import org.openbravo.erpCommon.utility.OBDateUtils;
import org.openbravo.erpCommon.utility.OBError;
import org.openbravo.model.common.invoice.Invoice;
import org.openbravo.service.db.DalConnectionProvider;
import org.openbravo.service.json.JsonUtils;

import javax.inject.Inject;
import java.text.ParseException;

/**
 * Action for processing invoices.
 * Allows for the same actions available in the UI as part of a Job.
 */
public class ProcessInvoices extends Action {
    Logger log = LogManager.getLogger();

    @Inject
    private WeldUtils weldUtils;

    @Override
    protected ActionResult action(JSONObject parameters, MutableBoolean isStopped) {
        var result = new ActionResult();

        try {
            var input = getInputContents(getInputClass());
            var documentAction = parameters.getString("DocAction");
            var voidDate = parameters.isNull("VoidDate") ? null : parameters.getString("VoidDate");
            var voidAcctDate = parameters.isNull("VoidAccountingDate") ? null : parameters.getString("VoidAccountingDate");
            var processMessages = new StringBuilder();
            int errors = 0;

            result.setType(Result.Type.SUCCESS);

            for (Invoice invoice : input) {
                var message = processInvoice(invoice, documentAction, voidDate, voidAcctDate);
                if (message.getType().equals("Error")) {
                    errors++;
                }
                if (message.getMessage().isBlank()) {
                    processMessages.append(invoice.getDocumentNo()).append(": ").append(message.getTitle()).append("\n");
                } else {
                    processMessages.append(invoice.getDocumentNo()).append(": ").append(message.getMessage()).append("\n");
                }
            }

            if (errors == input.size()) {
                result.setType(Result.Type.ERROR);
            } else if (errors > 0) {
                result.setType(Result.Type.WARNING);
            }

            if (input.size() > 1) {
                // Show the message in a pop up when more than one invoice was selected, for better readability.
                var jsonMessage = new JSONObject();
                jsonMessage.put("message", processMessages.toString().replaceAll("\n",""));
                result.setResponseActionsBuilder(getResponseBuilder().addCustomResponseAction("smartclientSay", jsonMessage));
            }

            result.setMessage(processMessages.toString());
            result.setOutput(getInput());


        } catch (JSONException | ParseException e) {
            log.error(e.getMessage(), e);
            result.setType(Result.Type.ERROR);
            result.setMessage(e.getMessage());
        }

        return result;
    }

    private OBError processInvoice(Invoice invoice, String docAction, String _strVoidDate, String _strVoidAcctDate) throws ParseException {

        var processor = weldUtils.getInstance(ProcessInvoiceUtil.class);
        var strVoidDate = "";
        var strVoidAcctDate = "";

        if (_strVoidDate != null && _strVoidAcctDate != null) {
            // Convert from the JSON date format to the OBProperties date format
            var voidDate = JsonUtils.createDateFormat().parse(_strVoidDate);
            var voidAcctDate = JsonUtils.createDateFormat().parse(_strVoidAcctDate);

            strVoidDate = OBDateUtils.formatDate(voidDate);
            strVoidAcctDate = OBDateUtils.formatDate(voidAcctDate);
        }

        return processor.process(
                invoice.getId(),
                docAction,
                strVoidDate,
                strVoidAcctDate,
                RequestContext.get().getVariablesSecureApp(),
                new DalConnectionProvider(false)
        );
    }

    @Override
    protected Class<Invoice> getInputClass() {
        return Invoice.class;
    }
}
```

### Extend and Execute Actions

It is also possible to extend actions by adding new functionality.  
The following is an example of extending the `com.smf.jobs.defaults.ProcessOrders` class found inside the standard actions distributed with Etendo.

```Java
public class ExtendProcessOrder extends com.smf.jobs.defaults.ProcessOrders {

  public ExtendProcessOrder() {
    super();
  }

  public ActionResult run(Data input, JSONObject param, MutableBoolean stopped) {
    setParameters(param);
    return super.run(input, stopped);
  }

}

public static void executeProcessOrderAction(Order order) {
    try {
      ExtendProcessOrder process = WeldUtils.getInstanceFromStaticBeanManager(ExtendProcessOrder.class);
      JSONObject jsonData = new JSONObject();
      jsonData.put("DocAction", "CO");
      Data data = new Data(jsonData, Order.class);
      List<BaseOBObject> orderList = new LinkedList<>();
      OBDal.getInstance().refresh(order);
      orderList.add(order);
      data.setContents(orderList);

      final MutableBoolean mutableBoolean = new MutableBoolean(false);
      var result = process.run(data, jsonData, mutableBoolean);
      if (result.getType().equals(Result.Type.ERROR)) {
        throw new OBException(result.getMessage());
      }
    } catch (Exception e) {
      throw new OBException(e.getMessage());
    }
  }
```

It is necessary to implement a method that gets and executes the current action, in our example we implement `executeProcessOrderAction(Order order)` which dynamically gets an instance of the `ExtendProcessOrder` class and executes it.
It is also possible to add validations and override the original methods.

## How to extend an Action using preAction and postAction hooks
There is a way to extend an Action without modifying it. This is done by implementing the pre and post hooks that are available in the `com.smf.jobs.Action` class.

When an Action is executed, all the implementation of the PreActionHook are executed before the run method of the Action, and all the implementation of the PostActionHook, are executed. This allows for the extension of the Action without modifying the original code, to add validations, or to execute additional logic.

### Example of an Action 
The following is an example of an Action that puts information in a Singleton class.

```Java
package com.smf.jobs;

import java.util.HashMap;

import org.apache.commons.lang.mutable.MutableBoolean;
import org.codehaus.jettison.json.JSONObject;
import org.openbravo.base.structure.BaseOBObject;

public class TestAction extends Action {
  private HashMap<String, Boolean> metadata = new HashMap<>();

  @Override
  protected ActionResult action(JSONObject parameters, MutableBoolean isStopped) {
    SingletonToTestHooks.getInstance().setMetadata("actionExecuted", true);
    var res = new ActionResult();
    res.setType(Result.Type.SUCCESS);
    res.setMessage("Test action executed");

    return res;
  }


  @Override
  protected Class<?> getInputClass() {
    return BaseOBObject.class;
  }
}
```

### Implementing the PreActionHook
The following is an example of a PreActionHook that introduce a logic before the Action is executed.

```Java
package com.smf.jobs;

import javax.enterprise.context.ApplicationScoped;

import org.codehaus.jettison.json.JSONObject;
import org.openbravo.client.kernel.ComponentProvider;

import com.smf.jobs.interfaces.PreActionHook;

/**
 * PreActionHook that sets a property in a singleton instance, before the action: TestAction is
 * executed.
 */
@ApplicationScoped
@ComponentProvider.Qualifier("com.smf.jobs.TestAction")
public class TestActionPreHook implements PreActionHook {

  /**
   * Returns the priority of this pre-action hook.
   * <p>
   * This method returns the priority value which determines the order in which the hook is executed.
   *
   * @return The priority value of this pre-action hook.
   */
  @Override
  public int getPriority() {
    return 121;
  }

  /**
   * Checks if this pre-action hook applies to the given parameters.
   * <p>
   * This method determines if the pre-action hook should be applied based on the provided parameters.
   *
   * @param parameters
   *     The JSON object containing the parameters.
   * @return true if the pre-action hook applies, false otherwise.
   */
  @Override
  public boolean applies(JSONObject parameters) {
    return true;
  }

  /**
   * Executes the pre-action hook with the given action.
   * <p>
   * This method runs the pre-action hook logic using the provided action JSON object.
   *
   * @param action
   *     The JSON object containing the action data.
   */
  @Override
  public void run(JSONObject action) {
    SingletonToTestHooks.getInstance().setMetadata("propAddedByPreHook", true);
  }
}
```

### Implementing the PostActionHook
The following is an example of a PostActionHook that introduce a logic after the Action is executed. Its pretty similar to the PreActionHook.

```Java
package com.smf.jobs;

import javax.enterprise.context.ApplicationScoped;

import org.codehaus.jettison.json.JSONObject;
import org.openbravo.client.kernel.ComponentProvider;

import com.smf.jobs.interfaces.PostActionHook;

/*
 * PostActionHook that sets a property in a singleton instance, after the action: TestAction is
 * executed.
 */
@ApplicationScoped
@ComponentProvider.Qualifier("com.smf.jobs.TestAction")
public class TestActionPostHook implements PostActionHook {

  /**
   * Returns the priority of this post-action hook.
   * <p>
   * This method returns the priority value which determines the order in which the hook is executed.
   *
   * @return The priority value of this post-action hook.
   */
  @Override
  public int getPriority() {
    return 10;
  }

  /**
   * Checks if this post-action hook applies to the given parameters.
   * <p>
   * This method determines if the post-action hook should be applied based on the provided action and result.
   *
   * @param action
   *     The JSON object containing the action data.
   * @param result
   *     The ActionResult object containing the result data.
   * @return true if the post-action hook applies, false otherwise.
   */
  @Override
  public boolean applies(JSONObject action, ActionResult result) {
    return true;
  }

  /**
   * Executes the post-action hook with the given action and result.
   * <p>
   * This method runs the post-action hook logic using the provided action and result JSON objects.
   *
   * @param actionParam
   *     The JSON object containing the action data.
   * @param result
   *     The ActionResult object containing the result data.
   */
  @Override
  public void run(JSONObject actionParam, ActionResult result) {
    SingletonToTestHooks.getInstance().setMetadata("propAddedByPostHook", true);
  }
}
```
After the Action is executed, the SingletonToTestHooks instance will have the properties `propAddedByPreHook`, `propAddedByPostHook` and `actionExecuted` set to `true`.