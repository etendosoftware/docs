---
title: Cómo implementar Crear nuevo en el selector
tags: 
    - implementar
    - crear nuevo
    - selectores
status: beta
---

# Cómo implementar Crear nuevo en el selector

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-implementcreate-new-in-selector/how-to-implement-create-new-in-selector-0.png)
 
![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-implementcreate-new-in-selector/how-to-implement-create-new-in-selector-1.png)

El módulo [org.openbravo.platform.features](../../../assets/developer-guide/etendo-classic/how-to-guides/org.openbravo.platform.features.zip) implementa un selector de ejemplo llamado **Terceros (Añadir nuevo)** en la ventana `Sales Order`.

Revisemos paso a paso cómo se ha construido este selector, centrándonos en los pasos que implementa este proyecto.

- Cree un nuevo selector de **Terceros**. Este es al que se adjuntará el proceso. Aquí tiene un ejemplo: 

    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-implementcreate-new-in-selector/how-to-implement-create-new-in-selector-2.png)

- Cree un nuevo **Selector de categoría de terceros**. Este se utilizará dentro del proceso. Aquí tiene un ejemplo: 

    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-implementcreate-new-in-selector/how-to-implement-create-new-in-selector-3.png)

- Cree el proceso de **Creación de terceros**. Este proceso se encargará de:

    - Gestionar, en caso de que exista, el valor escrito actualmente en la entrada del selector o en los filtros del selector en el popup. 
    - Realizar la creación del nuevo registro de **Terceros** 
    - Añadir y seleccionar el **Terceros** creado en el elemento de formulario del selector 

- Tras la creación de este proceso, en el selector de **Terceros** creado previamente, este proceso debe seleccionarse en el desplegable **Proceso para Añadir Registros**. 

    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-implementcreate-new-in-selector/how-to-implement-create-new-in-selector-4.png)

- Dentro del proceso de **Creación de terceros**, la **Función 'On Load'** se encargará de gestionar, en caso de que exista, el contenido escrito actualmente en la entrada del selector o en los filtros del selector en el popup. Este contenido se mostrará en el formulario del proceso en cada campo correspondiente. Aquí tiene un ejemplo: 


    ``` javascript
    OB.OBPF.BPCreation = function (processWindow) {
        var i, j, theFormItems;
        if (!processWindow || !processWindow.enteredValues || !processWindow.theForm || !processWindow.theForm.items) {
            return;
        }
        theFormItems = processWindow.theForm.items;
        for (i = 0; i < theFormItems.length; i++) {
            for (j = 0; j < processWindow.enteredValues.length; j++) {
                    if (processWindow.enteredValues[j][theFormItems[i].name]) {
                    theFormItems[i].setValue(processWindow.enteredValues[j][theFormItems[i].name]);
                    theFormItems[i].validate();
                }
            }
        }
    };
    ```

    Dado que en este caso el nombre de los elementos del formulario es igual al nombre de las columnas del selector, existe una lógica iterativa para hacer coincidir cada `enteredValue` con cada elemento del formulario del proceso.

- Dentro del proceso de **Creación de terceros**, el `Handler` se encargará de la creación del nuevo registro de terceros. Además, debe seleccionar este registro creado en el selector. 

    ``` java
    public class BPCreationActionHandler extends BaseProcessActionHandler {
        private static final Logger log = Logger.getLogger(BPCreationActionHandler.class);
     
        @Override
        protected JSONObject doExecute(Map<String, Object> parameters, String content) {
        JSONObject result = new JSONObject();
        OBContext.setAdminMode();
        try {
            result.put("refreshParent", false);
            String clientId = OBContext.getOBContext().getCurrentOrganization().getId();
            String orgId = OBContext.getOBContext().getCurrentClient().getId();
     
            JSONObject request = new JSONObject(content);
            if (request.has("inpadClientId")) {
            clientId = request.getString("inpadClientId");
            }
            if (request.has("inpadOrgId")) {
            orgId = request.getString("inpadOrgId");
            }
     
            JSONObject params = request.getJSONObject("_params");
            String searchKey = params.getString("searchKey");
            String name = params.getString("name");
            String bpCategoryId = params.getString("BPCat");
     
            BusinessPartner bp = OBProvider.getInstance().get(BusinessPartner.class);
            bp.setClient(OBDal.getInstance().get(Client.class, clientId));
            bp.setOrganization(OBDal.getInstance().get(Organization.class, orgId));
            bp.setSearchKey(searchKey);
            bp.setName(name);
            bp.setBusinessPartnerCategory(OBDal.getInstance().get(Category.class, bpCategoryId));
     
            OBDal.getInstance().save(bp);
            OBDal.getInstance().flush();
     
            JSONObject setSelectorValueFromRecord = new JSONObject();
            JSONObject record = new JSONObject();
            JSONObject responseActions = new JSONObject();
     
            record.put("value", bp.getId());
            record.put("map", bp.getIdentifier());
            setSelectorValueFromRecord.put("record", record);
            responseActions.put("setSelectorValueFromRecord", setSelectorValueFromRecord);
            result.put("responseActions", responseActions);
        } catch (JSONException e) {
            log.error("Error in process", e);
        } catch (Exception e) {
            try {
            Throwable ex = DbUtility.getUnderlyingSQLException(e);
            String message = OBMessageUtils.translateError(ex.getMessage()).getMessage();
            JSONObject msg = new JSONObject();
            JSONObject responseActions = new JSONObject();
            msg.put("msgType", "error");
            msg.put("msgTitle", "Error");
            msg.put("msgText", message);
            msg.put("force", true);
            responseActions.put("showMsgInProcessView", msg);
            result.put("responseActions", responseActions);
            result.put("retryExecution", true);
            } catch (JSONException ex) {
            log.error("Error in process", e);
            }
        } finally {
            OBContext.restorePreviousMode();
        }
        return result;
        }
    }
    ```

    Aquí, con `params.getString`, se obtienen los valores introducidos en el formulario y luego se establecen en `bp` (terceros). Después de guardar la instancia, se construye y devuelve el `record`, con el `id` como `value` y el `identifier` como `map`. También hay cierta lógica para capturar errores y mostrarlos como un mensaje.

---
Este trabajo es una obra derivada de [Cómo implementar Crear nuevo en selectores](http://wiki.openbravo.com/wiki/How_to_implement_Create_New_In_Selectors){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.