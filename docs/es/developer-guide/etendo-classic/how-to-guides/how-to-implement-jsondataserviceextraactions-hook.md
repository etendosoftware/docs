---
title: Cómo implementar el hook JsonDataServiceExtraActions
tags: 
    - implementar
    - JsonDataServiceExtraActions
    - hook
---

# Cómo implementar el hook JsonDataServiceExtraActions

## Visión general

Esta sección explica cómo implementar el hook **JsonDataServiceExtraActions**. Este hook se invoca antes y después de cada operación de la clase `DefaultJSONDataService`.

## Implementación del hook

El hook se implementa extendiendo la clase `JsonDataServiceExtraActions`. Esta clase tiene dos métodos que implementar:

- Método **doPreAction**: Este método void se invoca al inicio de cada acción de `DefaultJSONDataService`. Tiene 3 parámetros:

    - **parameters**: el Map con los parámetros de la llamada a `DataSource`. 
    - **data**: `JSONArray` con los registros que se van a insertar, actualizar o eliminar. Modifique este objeto en caso de que sea necesario modificar los datos antes de ejecutar la acción. Las operaciones de obtención (fetch) reciben un array vacío. 
    - **action**: valor del enum `DataSourceAction` con la Acción de la llamada a DataSource. Los valores posibles son `FETCH`, `ADD`, `UPDATE` y `REMOVE`. 

- Método **doPostAction**: Este método void se invoca al final de cada acción de `DefaultJSONDataService`. Tiene 4 parámetros:

    - **parameters**: el Map con los parámetros de la llamada a DataSource. 
    - **content**: `JSONObject` con el Contenido actual que se devuelve al cliente. Modifique este objeto en caso de que sea necesario modificar los datos antes de que se devuelvan. 
    - **action**: valor del enum `DataSourceAction` con la Acción de la llamada a DataSource. Los valores posibles son `FETCH`, `ADD`, `UPDATE` y `REMOVE`. 
    - **originalObject**: String `JSONObject` disponible solo en `ADD` y `UPDATE` con los valores originales de los datos. 

## Ejemplo

Este ejemplo registra una línea cada vez que se carga una ventana. Puede encontrar el código descrito a continuación en el módulo [org.openbravo.platform.features](../../../assets/developer-guide/etendo-classic/how-to-guides/org.openbravo.platform.features.zip).

``` java
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
Este trabajo es una obra derivada de [Cómo implementar el hook JsonDataServiceExtraActions](http://wiki.openbravo.com/wiki/How_To_Implement_JsonDataServiceExtraActions_Hook){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.