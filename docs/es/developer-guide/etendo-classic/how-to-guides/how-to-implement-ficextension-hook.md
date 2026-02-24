---
title: Cómo implementar el hook de FICExtension
tags: 
    - implementar
    - FICExtension
    - hook
---

# Cómo implementar el hook de FICExtension


## Visión general

Este documento explica cómo implementar el hook de **FICExtension**. El hook se ejecuta en el método *execute* de la clase **FormInitializationComponent** justo antes de que se construya la respuesta.

## Implementación del hook

Este hook se implementa extendiendo la clase `FICExtension`. Solo tiene un método void para implementar: `execute`. Este método recibe como parámetros las instancias de los objetos utilizados para construir la respuesta.

- **mode**: El modo de ejecución. 
- **tab**: La `Solapa` propietaria del _Formulario_ en el que se está ejecutando. 
- **columnValues**: `Map` con los valores de las columnas de los formularios. 
- **row**: El `BaseOBObject` que se está editando en el formulario. 
- **changeEventCols**: La `List` de columnas dinámicas que disparan el modo de evento CHANGE. 
- **calloutMessages**: La `List` de mensajes devueltos por los callouts que se han ejecutado. 
- **attachments**: La `List` con los adjuntos relacionados con el registro que se está editando. 
- **jsExcuteCode**: La `List` de código JavaScript devuelto por los callouts para ejecutarse en el cliente. 
- **hiddenInputs**: El `Map` con todos los campos ocultos con sus valores. 
- **noteCount**: Recuento de notas disponibles en el registro que se está editando. 
- **overwrittenAuxiliaryInputs**: La `List` de entradas auxiliares sobrescritas por callouts.   

## Ejemplo

Este ejemplo muestra un mensaje cada vez que se edita un producto nuevo. Puede encontrar el código descrito a continuación en el módulo `org.openbravo.platform.features`.

``` java
public class ProductFICExtensionExample implements FICExtension {
 
@Override
     public void execute(String mode, Tab tab, Map<String, JSONObject> columnValues, BaseOBObject row,
     List<String> changeEventCols, List<JSONObject> calloutMessages, List<JSONObject> attachments,
     List<String> jsExcuteCode, Map<String, Object> hiddenInputs, int noteCount,
     List<String> overwrittenAuxiliaryInputs) throws OBException {
     if ("180".equals(tab.getId())) {
     JSONObject jsonMessage = new JSONObject();
     try {
          jsonMessage.put("severity", "TYPE_WARNING");
          jsonMessage.put("text", "Product form opened");
     } catch (JSONException ignore) {
     }
     calloutMessages.add(jsonMessage);
     }
     }
}
```

---

Este trabajo es una obra derivada de [Cómo implementar el hook de FICExtension](http://wiki.openbravo.com/wiki/How_To_Implement_FICExtension_Hook){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.