---
title: Puntos de extensión
tags:
    - Puntos de extensión
    - Validación
    - Proceso
status: beta
---

# Puntos de extensión

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
    
## Visión general

Esta es la lista de Puntos de extensión disponibles en procedimientos del core.

### `C_Order_Post` - Punto de extensión de finalización del proceso

Este punto de extensión se llama al final de la función `C_Order_Post1`, la función que procesa pedidos.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_order_id` del pedido que se está procesando. 
    * `DocAction` (`p_String`). Acción realizada durante el proceso del pedido. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `C_Order_Post` - Proceso de validación

Este punto de extensión se llama al inicio de la función `C_Order_Post1`, la función que procesa pedidos.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_order_id` del pedido que se está procesando. 
    * `DocAction` (`p_String`). Acción realizada durante el proceso del pedido. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `C_Invoice_Post` - Punto de extensión de finalización del proceso

Este punto de extensión se llama al final de la función `C_Invoice_Post`, la función que procesa facturas.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_invoice_id` de la factura que se está procesando. 
    * `DocAction` (`p_String`). Acción realizada durante el proceso del pedido. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `M_Inout_Post` - Punto de extensión de finalización del proceso

Este punto de extensión se llama al final de la función `M_Inout_Post`, la función que completa los albaranes.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `m_inout_id` del albarán que se está procesando. 
    * `DocAction` (`p_String`). Acción realizada durante el proceso del pedido. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `M_Inout_Create` - Llamada al postproceso

Este punto de extensión se llama dentro de la función `M_Inout_Create`, la función que crea albaranes a partir de pedidos. Permite, en función del resultado devuelto, llamar o no a la función para completar el albarán creado y dejar el albarán en estado borrador.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_invoice_id` de la factura que se está procesando. 
    * `DocAction` (`p_String`). Acción realizada durante el proceso del pedido. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (NULL, ejecutar el proceso de completar albarán. Otro valor, no ejecutar el proceso de completar albarán) 

### `M_Inout_Cancel` - Llamada al postproceso

Este punto de extensión se llama dentro de la función `M_Inout_Cancel`, la función que anula albaranes a partir de pedidos. Permite, en función del resultado devuelto, llamar o no a la función para completar el albarán creado y dejar el albarán en estado borrador.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `c_invoice_id` de la factura que se está procesando. 
    * `DocAction` (`p_String`). Acción realizada durante el proceso del pedido. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (NULL, ejecutar el proceso de completar albarán. Otro valor, no ejecutar el proceso de completar albarán) 

### `MA_Copy_Version` - Finalización del proceso

Este punto de extensión se llama al final de la función `MA_Copy_Version`, la función que copia versiones del plan de proceso.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `MA_Processplan_ID` del plan de proceso que se está copiando. 
    * `MA_Processplan_Version_ID` (`p_String`). `MA_Processplan_Version_ID` de la versión del plan de proceso que se está copiando. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `MA_Workrequirement_Process` - Finalización del proceso

Este punto de extensión se llama al final de la función `MA_Workrequirement_Process`, la función que procesa requisitos de trabajo.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `MA_WorkRequirement_ID` del requisito de trabajo que se está procesando. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `MA_Productionrun_Standard` - Finalización del proceso

Este punto de extensión se llama al final de la función `MA_Productionrun_Standard`, la función utilizada por el proceso Crear estándares.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `M_ProductionPlan_ID` del plan de producción que se está procesando. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `MA_Workeffort_Validate` - Finalización del proceso

Este punto de extensión se llama al final de la función `MA_Workeffort_Validate`, la función que valida esfuerzos de trabajo.

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `MA_WorkEffort_ID` del esfuerzo de trabajo que se está procesando. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `M_Get_Stock` - Finalización del proceso

Este punto de extensión se llama al final de la función `M_Get_Stock`, la función que obtiene stock del almacén. Esta función se utiliza en la funcionalidad de gestión de stock de almacén.

Es posible personalizar el stock que propone la gestión de stock de almacén.

* Parámetros: 
    * `AD_Pinstance_Stock_ID` (`p_String`). `AD_Pinstance_ID` del proceso `AD_PINSTANCE` de `M_Get_Stock` 
    * `Record_ID`. `Record_ID` de la entidad que llama a `M_Get_Stock`. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

### `M_PriceList_Create` - Finalización del proceso

Este punto de extensión se llama al final de la función `M_Pricelist_Create`, la función que crea precios en base a los parámetros de la versión de tarifa. Consulte [Versión de tarifa](../../../user-guide/etendo-classic/basic-features/master-data-management/pricing.md#price-list-version).

* Parámetros: 
    * `Record_ID` (`p_String` column of `AD_EP_Instance_Para`). `M_PriceList_Version_ID` de la versión de tarifa que se está procesando. 
    * `DeleteOld` (`p_String`). Parámetro `DeleteOld` tomado de `AD_PInstance_Para`. 
    * `User` (`p_String`). `AD_User_Id` que ha lanzado el proceso. 
    * `Message` (`p_Text`). Variable para establecer un mensaje si es necesario. 
    * `Result` (`p_Number`). Entero para establecer el resultado del proceso (1 éxito, 0 error, 2 advertencia) 

`Message` y `Result` deben recuperarse después de que se hayan lanzado los procedimientos, ya que podrían ser modificados por dichos procedimientos para establecer advertencias y mensajes al usuario.

---

Este trabajo es una obra derivada de [Puntos de extensión](http://wiki.openbravo.com/wiki/ExtensionPoints){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.