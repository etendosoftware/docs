---
tags:
  - Extension Points
  - Core procedures
  - Orders
  - Shipments
  - Invoice Post
  - Order Post
  - Warehouse Stock
  - Price List
---

# Extension Points

This is the list of **available Extension Points** on core procedures.

### `C_Order_Post` - Finish Process Extension Point

This extension point is called at the end of the `C_Order_Post1` function, the function that **processes orders**

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_order_id` of the order that is being processed.
    * `DocAction` (`p_String`). Action performed during the order process.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

### `C_Order_Post` - Validation Process

This extension point is called at the beginning of the `C_Order_Post1` function, the function that **processes orders**

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_order_id` of the order that is being processed.
    * `DocAction` (`p_String`). Action performed during the order process.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

### `C_Invoice_Post` - Finish Process Extension Point

This extension point is called at the end of the `C_Invoice_Post` function, the function that **processes invoices**

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_invoice_id` of the invoice that is being processed.
    * `DocAction` (`p_String`). Action performed during the order process.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

### `M_Inout_Post` - Finish Process Extension Point

This extension point is called at the end of the `M_Inout_Post` function, the function that **completes shipments**

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `m_inout_id` of the shipment that is being processed.
    * `DocAction` (`p_String`). Action performed during the order process.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

### `M_Inout_Create` - Calling Post Process

This extension point is called inside the `M_Inout_Create` function, the function that **creates shipments from orders**. It allows, depending on the returned result, to call the function to complete the shipment created or not and leave the shipment in draft status.

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_invoice_id` of the invoice that is being processed.
    * `DocAction` (`p_String`). Action performed during the order process.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Result` (`p_Number`). `Integer` to set the result of the process (**NULL**, execute the shipment complete process. **Other value**, do not execute the shipment complete process).

### `M_Inout_Cancel` - Calling Post Process

This extension point is called inside the `M_Inout_Cancel` function, the function that **cancels shipments from orders**. It allows, depending on the returned result, to call the function to complete the shipment created or not and leave the shipment in draft status.

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_invoice_id` of the invoice that is being processed.
    * `DocAction` (`p_String`). Action performed during the order process.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Result` (`p_Number`). `Integer` to set the result of the process (**NULL**, execute the shipment complete process. **Other value**, do not execute the shipment complete process).

### `MA_Copy_Version` - Finish Process

This extension point is called at the end of the `MA_Copy_Version` function, the function that **copy process plan versions**.

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `MA_Processplan_ID` of the Process Plan that is being copied.
    * `MA_Processplan_Version_ID` (`p_String`). `MA_Processplan_Version_ID` of the Process Plan Version that is being copied.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

### `MA_Workrequirement_Process` - Finish Process

This extension point is called at the end of the `MA_Workrequirement_Process` function, the function that **processes Work Requirements**

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `MA_WorkRequirement_ID` of the Work Requirement that is being processed.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.

!!!info
      Message needs to be retrieved after the procedures have been launched as they might be changed by those procedures to send warnings and messages to the user.

### `MA_Productionrun_Standard` - Finish Process

This extension point is called at the end of the `MA_Productionrun_Standard` function, the function used by **Create Standards process**

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `M_ProductionPlan_ID` of the Production Plan that is being processed.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

### `MA_Workeffort_Validate` - Finish Process

This extension point is called at the end of the `MA_Workeffort_Validate` function, the function that **validates Work Efforts**

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `MA_WorkEffort_ID` of the Work Effort that is being processed.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

### `M_Get_Stock` - Finish Process

This extension point is called at the end of the `M_Get_Stock` function, the function that *gets stock from the Warehouse*. This function is used in [Warehouse Stock Management functionality]().

  * Parameters:
    * `AD_Pinstance_Stock_ID` (`p_String`). `AD_Pinstance_ID` of the `AD_PINSTANCE` process from `M_Get_Stock`
    * `Record_ID`. `Record_ID` of the entity who calls `M_Get_Stock`.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `AD_Client_ID`. `ID` of a client entity.
    * `AD_Org_ID`. `ID` of an organization entity.
    * `M_Product_ID`. `ID` of the entity whose stock will be retrieved.
    * `C_Uom_ID`. `ID` of entity that defines units of measure.
    * `M_Product_Uom_ID`. `ID` of entity that defines a unit of measurement for a given product.
    * `M_Warehouse_ID`. `ID` of a Warehouse entity for a given organization.
    * `M_Locator_ID`. `ID` of a storage bin entity for a selected warehouse.
    * `M_AttributesetInstance_ID`. `ID` of an attribute entity associated with a product as part of an attribute set.
    * `Quantity`. `NUMERIC` for a selected product whose stock will be retrieved.
    * `Priority_Warehouse_ID`. `ID` of a selected warehouse assigned as priotity from which the stock will be retrieved.
    * `M_Warehouse_Rule_ID`. `ID` entity that defines a Warehouse Rule to be applied when getting stock from the warehouse.
    * `TableId`. `ID` referencing a specific `AD_TABLE` entity.
    * `AuxID`. `ID` entity that, if present, will insert values from auxiliar stock.
    * `LineNo`. `NUMERIC` line number of the product line.
    * `M_Reservation_ID`. `ID` of entity that defines that, if a reservation is given, will first consume allocated stock.
    * `Available`. `CHAR` reflects if the inventory status is available (`Yes/No`).
    * `Nettable`. `CHAR` inventory status information where any stock of it held can be netted against the product's gross requirements to determine its net requirements (`Yes/No`).
    * `OverIssue`. `CHAR` If it's allowed to be overissued (`Yes/No`).
    * `ProcessID`. `ID`
    * `Message`. (`p_Text`). The result message of the execution.

!!!info
      Message needs to be retrieved after the procedures have been launched as they might be changed by those procedures to send warnings and messages to the user.

### `M_PriceList_Create` - Finish Process

This extension point is called at the end of the `M_Pricelist_Create` function, the function that creates prices based on parameters of the **price list version**.

!!!info
      For more information, see [Price List Version](../../basic-features/master-data-management/pricing.md#price-list).

  * Parameters:
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `M_PriceList_Version_ID` of the Price List Version that is being processed.
    * `DeleteOld` (`p_String`). `DeleteOld` parameter taken from `AD_PInstance_Para`.
    * `User` (`p_String`). `AD_User_Id` who has launched the process.
    * `Message` (`p_Text`). `Variable` to set a message if needed.
    * `Result` (`p_Number`). `Integer` to set the result of the process (`1 success`, `0 error`, `2 warning`).

!!!info
      Message and Result have to be retrieved after the procedures have been launched as they might be changed by those procedures to set warnings and messages to the user.

This work is a derivative of [Extension Points](http://wiki.openbravo.com/wiki/ExtensionPoints){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.