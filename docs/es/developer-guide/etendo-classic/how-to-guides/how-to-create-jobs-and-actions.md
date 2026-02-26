---
title: Cómo crear trabajos y acciones
tags:
    - Cómo hacer
    - Trabajos
    - Acciones
---

## Visión general

Etendo introduce el concepto de Trabajos, que consiste en una o más Acciones ejecutadas en secuencia. Estas Acciones son procesos estándar que permiten al usuario crear y almacenar Trabajos para su uso posterior. Las automatizaciones de Jira y los Atajos de iOS son conceptos similares.

!!! note
    La GUI para crear y ejecutar trabajos llegará pronto en una versión más reciente de Etendo. En la actualidad, solo es posible definir Acciones que actúan como procesos estándar disponibles en la UI existente; no obstante, también serán compatibles con la nueva UI cuando se publique.

## Crear una acción

!!! info
    Las Acciones se basan en la arquitectura existente de Proceso estándar.

1.  Cree un nuevo registro en la ventana Definición de proceso:

    ![createjobs1.png](../../../assets/legacy/technicaldocumentation/platform/createjobs1.png)

2.  Defina el Patrón de UI como Acción. El proceso debe marcarse como multirregistro. Todas las acciones deben admitir entrada multirregistro. El resto de definiciones son análogas a cualquier Proceso estándar. Se admiten parámetros, funciones onLoad, etc.
3.  Cree una columna y un campo para ejecutar la Acción desde un botón en la UI actual, o una entrada de menú para ejecutar el proceso desde el menú.
4.  La clase Java asociada a la nueva Acción debe extender el tipo Action (`com.smf.jobs.Action`).

Su IDE de preferencia debería solicitarle que complete los métodos requeridos:

- `ActionResult action(JSONObject parameters, MutableBoolean isStopped)`
- `Class<T> getInputClass()`

El primer método `action()` es donde ocurre la lógica principal del proceso. Recibirá los parámetros del proceso en un objeto json, y un booleano para comprobar si se solicitó detener el proceso. Una vez finalizada la lógica, su código debe devolver un tipo `ActionResult` detallando si la ejecución finalizó correctamente o no. También habrá un mensaje para el usuario.

El método `getInputClass()` debe devolver el tipo de clase que esta Acción admite como entrada. Por ejemplo `Invoice.class:`

```plaintext

import org.openbravo.model.common.invoice.Invoice;
/* ... */
@Override
protected Class<Invoice> getInputClass() {
    return Invoice.class;
}
```

Los datos de entrada (el/los registro(s) seleccionado(s) por el usuario, o el resultado de otra Acción) se pueden obtener con el método `getInputContents()`. De forma predeterminada, este método devolverá una lista de `BaseOBObject`, pero puede parametrizarse usando el método `getInputClass()` anterior (o la clase directamente).
Por ejemplo:

```plaintext

// Assuming getInputClass() returns Invoice.class
List<Invoice> invoices = getInputContents(getInputClass());
```

El tipo `ActionResult` puede utilizarse para mostrar un mensaje al usuario:

```plaintext

result.setType(Result.Type.ERROR);
result.setMessage(OBMessageUtils.getI18NMessage("Success"));
/* ... */
return result;
```

El objeto result también puede establecer una salida para ser utilizada como entrada para el siguiente trabajo, cuando se implemente la nueva UI de Trabajos:

```plaintext

List<Invoices> invoices = processInvoices();
result.setOutput(invoices);
```

Para operaciones más complejas presentes en procesos estándar, el método `setResponseActionsBuilder()` puede utilizarse para establecer un response builder. Esto sigue la misma lógica existente al usar una clase `BaseProcessActionHandler`.

La lógica principal del proceso puede construirse como cualquier proceso que anteriormente extendiera la clase `BaseProcessActionHandler`. Debería ser trivial portar procesos existentes a Acciones.

Los ejemplos de otras Acciones implementadas en Etendo suelen estar presentes en el paquete `com.smf.jobs.defaults`.

A continuación se muestra un ejemplo completo de una clase Java de Acción:

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

### Ampliar y ejecutar acciones

También es posible ampliar acciones añadiendo nueva funcionalidad.  
A continuación se muestra un ejemplo de ampliación de la clase `com.smf.jobs.defaults.ProcessOrders` que se encuentra dentro de las acciones estándar distribuidas con Etendo.

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

Es necesario implementar un método que obtenga y ejecute la acción actual; en nuestro ejemplo implementamos `executeProcessOrderAction(Order order)`, que obtiene dinámicamente una instancia de la clase `ExtendProcessOrder` y la ejecuta.
También es posible añadir validaciones y sobrescribir los métodos originales.

## Cómo ampliar una acción usando hooks preAction y postAction
Existe una forma de ampliar una Acción sin modificarla. Esto se realiza implementando los hooks pre y post que están disponibles en la clase `com.smf.jobs.Action`.

Cuando se ejecuta una Acción, todas las implementaciones de PreActionHook se ejecutan antes del método run de la Acción, y se ejecutan todas las implementaciones de PostActionHook. Esto permite ampliar la Acción sin modificar el código original, para añadir validaciones o ejecutar lógica adicional.

### Ejemplo de una acción 
A continuación se muestra un ejemplo de una Acción que introduce información en una clase Singleton.

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

### Implementación de PreActionHook
A continuación se muestra un ejemplo de un PreActionHook que introduce una lógica antes de que se ejecute la Acción.

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

### Implementación de PostActionHook
A continuación se muestra un ejemplo de un PostActionHook que introduce una lógica después de que se ejecute la Acción. Es bastante similar al PreActionHook.

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
Después de ejecutar la Acción, la instancia SingletonToTestHooks tendrá las propiedades `propAddedByPreHook`, `propAddedByPostHook` y `actionExecuted` establecidas en `true`.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.