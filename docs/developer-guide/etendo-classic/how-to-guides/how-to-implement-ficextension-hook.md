---
title: How To Implement FICExtension Hook
tags: 
    - implement
    - FICExtension
    - hook

status: beta
---

#  How To Implement FICExtension Hook

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

This document explains how to implement the **FICExtension** Hook. The hook is executed in the _execute_ method of the **FormInitializationComponent** class just before the response is built.

##  Hook Implementation

This hook is implemented by extending the `FICExtension` class. It has just one void method to implement: `execute`. This method receives as parameters the instances of the objects used to build the response.

- **mode**: The execution mode. 
- **tab**: The `Tab` owner of the _Form_ that it is being executed. 
- **columnValues**: `Map` with the values of forms columns. 
- **row**: The `BaseOBObject` that it is being edited in the form. 
- **changeEventCols**: The `List` of dynamic columns that fire the CHANGE event mode. 
- **calloutMessages**: The `List` of messages returned by the callouts that have been executed. 
- **attachments**: The `List` with the attachments related to the record that it is being edited. 
- **jsExcuteCode**: The `List` of JavaScript code returned by the callouts to be executed in the client. 
- **hiddenInputs**: The `Map` with all the hidden fields with their values. 
- **noteCount**: Count of notes available on the record that it is being edited. 
- **overwrittenAuxiliaryInputs**: The `List` of the Auxiliary Inputs overriden by callouts.   

##  Example

This example shows a message every time a new product is edited. You can find the code described below in the `org.openbravo.platform.features` module.

```
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

This work is a derivative of [How To Implement FICExtension Hook](http://wiki.openbravo.com/wiki/How_To_Implement_FICExtension_Hook){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.