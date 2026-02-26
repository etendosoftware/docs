---
title: Cómo crear un enlace navegable
tags: 
  - Cómo
  - Crear
  - Navegable
  - Enlace
---

#  Cómo crear un enlace navegable

## Visión general

Esta sección explica cómo crear un enlace navegable en Etendo Classic, implementando una ClientClass. Una ClientClass le permite añadir componentes visuales a un formulario o a una fila de una cuadrícula. Esto es útil para añadir campos calculados a formularios y cuadrículas, integrando elementos como botones, enlaces o etiquetas dinámicas.

En este caso, implementaremos una ClientClass navegable para que el documentNo en la ventana **Crear factura desde pedidos** permita abrir directamente el pedido de venta correspondiente en la ventana Pedido de venta.

Esta sección muestra cómo utilizar la información del registro y del formulario para obtener datos dinámicos en la cuadrícula o en el formulario. 

!!! info
    La implementación de estos campos requiere conocimientos de JavaScript.


## Pasos principales para crear una nueva ClientClass

1. Implementar la ClientClass en JavaScript:

    - Cree el archivo JavaScript con la clase correspondiente y colóquelo en el directorio adecuado. La convención es colocar los archivos `.js` en:

        ```web/[module.java.package]/js```

    - Registre el archivo JavaScript (junto con otros recursos estáticos como archivos CSS) en un ComponentProvider.


2. Especificar la clase JavaScript en la definición del campo:

    - Configure el campo en la solapa/ventana donde se aplicará la funcionalidad.


## Implementación de la ClientClass en JavaScript

El primer paso es definir la clase en JavaScript en dos etapas:

1. Crear la clase JavaScript y calcular `tabId` y `recordId`.
    En este caso, la lógica se implementa en la clase `DirectTabLink`, que gestiona la apertura de la ventana, pasando los valores de `tabId` y `recordId`.

    ``` javascript title="direct-tab-link.js"
    isc.ClassFactory.defineClass('DirectTabLink', isc.OBGridFormLabel);


    isc.DirectTabLink.addProperties({
    height: 1,
    width: 1,
    overflow: 'visible',


    // Method that subclasses must override
    getTabAndRecordId: function(record, callback) {
    callback({ tabId: null, recordId: null });
    },


    setRecord: function(record) {
    var value = record[this.field.name];


    // Call the asynchronous function from the subclass
    this.getTabAndRecordId(record, function(result) {
        var tabId = result.tabId;
        var recordId = result.recordId;


        if (!value || !tabId || !recordId) {
        this.setContents("");
        return;
        }


        // Create the inline function for onclick
        var linkHTML =
        "<a href='#' style='color:blue; text-decoration:underline;' " +
        "onclick='OB.Utilities.openDirectTab(\"" + tabId + "\", \"" + recordId + "\"); return false;'>" +
        value + "</a>";


        this.setContents(linkHTML);


        // Force grid redraw
        if (this.grid && this.grid.body) {
        this.grid.body.markForRedraw();
        }
    }.bind(this));
    }
    });

    ```

2. Implementación específica de la ClientClass

    En nuestro ejemplo, la ventana de destino es Pedido de venta. Dado que el `tabId` es fijo y no cambia, puede dejarse como un valor estático.

    El `recordId`, por otro lado, contiene el identificador único de cada pedido, lo que facilita la navegación sin necesidad de cálculos adicionales.

    ``` javascript title="sales-order-tab-link.js"
    isc.ClassFactory.defineClass('SalesOrderTabLink', DirectTabLink);
    isc.SalesOrderTabLink.addProperties({
    getTabAndRecordId: function(record, callback) {
    var tabId = "186"; // Fixed tab ID for "Sales Order"
    var recordId = record.id;


    if (!recordId) {
        console.error("Error: Record ID not found in the record.");
        callback({ tabId: null, recordId: null });
        return;
    }


    callback({ tabId: tabId, recordId: recordId });
    }
    });
    ```

## Casos especiales: Cálculo de `recordId` con Java

En algunos casos, la información de `recordId` no está disponible directamente en el registro, por lo que debe calcularse. Esto puede lograrse mediante una clase Java que determine el `recordId` correspondiente.

Ejemplo:
Si el registro no tiene el `recordId` de los comandos directamente, podemos calcularlo llamando a una clase Java específica:

``` java title="sales-order-tab-link-with-java.js"
isc.ClassFactory.defineClass('SalesOrderTabLink', DirectTabLink);
isc.SalesOrderTabLink.addProperties({
 getTabAndRecordId: function(record, callback) {
   var tabId = "186"; // Predefined Tab ID for "Sales Order"
   var documentNo = record.documentNo; // Retrieve documentNo from the record


   if (!documentNo) {
     console.error("Error: documentNo not found in the record.");
     callback({ tabId: null, recordId: null });
     return;
   }
   // Call the Openbravo Action Handler to retrieve the recordId
   OB.RemoteCallManager.call(
     'org.openbravo.client.application.GetSalesOrderIdActionHandler', // Java Action Handler class name
     { documentNo: documentNo }, // Parameter sent to the backend
     {},
     function(response, data, request) {
       if (data.success && data.recordId) {
         callback({ tabId: tabId, recordId: data.recordId }); // Use predefined tabId
       } else {
         console.error("Error retrieving recordId: " + (data.errorMessage || "Invalid response"));
         callback({ tabId: null, recordId: null });
       }
     }
   );
 }
});
```

En Java:

``` java title="GetSalesOrderIdActionHandler.java"
import org.openbravo.dal.service.OBCriteria;
import org.openbravo.dal.service.OBDal;
import org.openbravo.model.common.order.Order;


/**
* Action handler to retrieve the sales order ID based on a given document number.
*/
public class GetSalesOrderIdActionHandler extends BaseActionHandler {


 private static final String DOCUMENT_NO = "documentNo";
 private static final String SUCCESS = "success";
 private static final String RECORD_ID = "recordId";
 private static final String ERROR_MESSAGE = "errorMessage";


 /**
  * Executes the action to retrieve the sales order ID based on the provided document number.
  *
  * @param parameters A map containing execution parameters.
  * @param content A JSON string containing the document number.
  * @return A JSON object containing the sales order ID and status of the operation.
  */
 @Override
 protected JSONObject execute(Map<String, Object> parameters, String content) {
   JSONObject result = new JSONObject();
   try {
     final JSONObject jsonData = new JSONObject(content);


     if (!jsonData.has(DOCUMENT_NO) || jsonData.isNull(DOCUMENT_NO)) {
       result.put(SUCCESS, false);
       result.put(ERROR_MESSAGE, "The 'documentNo' parameter is required.");
       return result;
     }


     String documentNo = jsonData.getString(DOCUMENT_NO);


     OBCriteria<Order> orderOBCriteria = OBDal.getInstance().createCriteria(Order.class);
     orderOBCriteria.add(Restrictions.eq(Order.PROPERTY_DOCUMENTNO, documentNo));
     orderOBCriteria.setMaxResults(1);


     Order order = (Order) orderOBCriteria.uniqueResult();
     result.put(RECORD_ID, order.getId());
     result.put(SUCCESS, true);


   } catch (Exception e) {
     try {
       result.put(SUCCESS, false);
       result.put(ERROR_MESSAGE, e.getMessage());
     } catch (Exception ex) {
       throw new OBException(e);
     }
   }
   return result;
```

## Registro del archivo JavaScript en el ComponentProvider

Una vez creada la clase JavaScript, es necesario registrarla en el ComponentProvider del módulo correspondiente.

``` javascript title="UIComponentProvider.java"
/** JavaScript files required for UI navigation. */
protected static final String[] JS_FILES = new String[]{
   "direct-tab-link.js",
   "sales-order-tab-link.js"
};
```

## Definición de la ClientClass en el campo de la solapa (ADField)

El último paso es añadir la implementación en el campo donde se aplicará la funcionalidad y configurar su ClientClass.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-navigable-link.png)

## Resultado final

Como se muestra a continuación, utilizando el enlace creado, puede abrir directamente el pedido de venta enlazado en la ventana Pedido de venta.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/createinvoicesfromorders.gif)


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.