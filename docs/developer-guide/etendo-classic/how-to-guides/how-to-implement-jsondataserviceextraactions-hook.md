---
title: How To Implement JsonDataServiceExtraActions Hook
tags: 
    - implement
    - JsonDataServiceExtraActions
    - hook

status: beta
---

#  How To Implement JsonDataServiceExtraActions Hook

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

This section explains how to implement **JsonDataServiceExtraActions** Hook. This hook is called before and after each operation of `DefaultJSONDataService` class.

##  Hook Implementation

The hook is implemented by extending the `JsonDataServiceExtraActions` class. This class has two methods to implement:

- **doPreAction** method: This void method is called at the beginning of each `DefaultJSONDataService` action. It has 3 parameters:

    - **parameters**: The Map with the parameters of the DataSource call. 
    - **data**: `JSONArray` with the records that are going to be inserted, updated or deleted. Modify this object in case it is required to modify the data before executing the action. Fetch operations receive an empty array. 
    - **action**: `DataSourceAction` enum value with the action of the DataSource call. Possible values are FETCH, ADD, UPDATE and REMOVE. 

- **doPostAction** method: This void method is called at the end of each `DefaultJSONDataService` action. It has 4 parameters:

    - **parameters**: The Map with the parameters of the DataSource call. 
    - **content**: `JSONObject` with the current content that is returned to the client. Modify this object in case it is required to modify the data before is returned. 
    - **action**: `DataSourceAction` enum value with the action of the DataSource call. Possible values are FETCH, ADD, UPDATE and REMOVE. 
    - **originalObject**: `JSONObject` String available only on ADD and UPDATE with the original values of the data. 

##  Example

This example logs a line every time a window is loaded. You can find the code described below in the `org.openbravo.platform.features` module.

```
public class JsonDataServiceExtraActionsExample implements JsonDataServiceExtraActions {
    private static final Logger log = LoggerFactory
        .getLogger(JsonDataServiceExtraActionsExample.class);
 
    @Override
    public void doPreAction(Map<String, String> parameters, JSONArray newData, DataSourceAction action) {
    log.debug("JsonDataServiceExtraActionsExample doPreAction implementation");
    }
 
    @Override
    public void doPostAction(Map<String, String> parameters, JSONObject content,
        DataSourceAction action, String originalObject) {
    }
}
```

---

This work is a derivative of [How To Implement JsonDataServiceExtraActions Hook](http://wiki.openbravo.com/wiki/How_To_Implement_JsonDataServiceExtraActions_Hook){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.