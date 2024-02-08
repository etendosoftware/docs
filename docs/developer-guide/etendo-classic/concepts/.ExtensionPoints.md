![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  ExtensionPoints

##  Contents

  * 1  Extension Points 
    * 1.1  C_Order_Post - Finish Process Extension Point 
    * 1.2  C_Order_Post - Validation Process 
    * 1.3  C_Invoice_Post - Finish_Process Extension Point 
    * 1.4  M_Inout_Post - Finish_Process Extension Point 
    * 1.5  M_Inout_Create - Calling Post Process 
    * 1.6  M_Inout_Cancel - Calling Post Process 
    * 1.7  MA_Copy_Version - Finish Process 
    * 1.8  MA_Workrequirement_Process - Finish Process 
    * 1.9  MA_Productionrun_Standard - Finish Process 
    * 1.10  MA_Workeffort_Validate - Finish Process 
    * 1.11  M_Get_Stock - Finish Process 
    * 1.12  M_PriceList_Create - Finish Process 

  
---  
  
##  Extension Points

This is the list of available  Extension Points  on core procedures.

###  C_Order_Post - Finish Process Extension Point

This extension point is called at the end of the C_Order_Post1 function, the
function that processes orders

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). c_order_id of the order that is being processed. 
    * DocAction (p_String). Action performed during the order process. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  C_Order_Post - Validation Process

This extension point is called at the beginning of the C_Order_Post1 function,
the function that processes orders

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). c_order_id of the order that is being processed. 
    * DocAction (p_String). Action performed during the order process. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  C_Invoice_Post - Finish_Process Extension Point

This extension point is called at the end of the C_Invoice_Post function, the
function that processes invoices

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). c_invoice_id of the invoice that is being processed. 
    * DocAction (p_String). Action performed during the order process. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  M_Inout_Post - Finish_Process Extension Point

This extension point is called at the end of the M_Inout_Post function, the
function that completes shipments

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). m_inout_id of the shipment that is being processed. 
    * DocAction (p_String). Action performed during the order process. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  M_Inout_Create - Calling Post Process

This extension point is called inside the M_Inout_Create function, the
function that creates shipments from orders. It allows depending on the result
returned to call the function to complete the shipment created or not and
leave the shipment in draft status.

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). c_invoice_id of the invoice that is being processed. 
    * DocAction (p_String). Action performed during the order process. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Result (p_Number). Integer to set the result of the process (NULL, execute the shipment complete process. Other value, do not execute the shipment complete process) 

###  M_Inout_Cancel - Calling Post Process

This extension point is called inside the M_Inout_Cancel function, the
function that cancels shipments from orders. It allows depending on the result
returned to call the function to complete the shipment created or not and
leave the shipment in draft status.

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). c_invoice_id of the invoice that is being processed. 
    * DocAction (p_String). Action performed during the order process. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Result (p_Number). Integer to set the result of the process (NULL, execute the shipment complete process. Other value, do not execute the shipment complete process) 

###  MA_Copy_Version - Finish Process

This extension point is called at the end of the MA_Copy_Version function, the
function that copy process plan versions.

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). MA_Processplan_ID of the Process Plan that is being copied. 
    * MA_Processplan_Version_ID (p_String). MA_Processplan_Version_ID of the Process Plan Version that is being copied. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  MA_Workrequirement_Process - Finish Process

This extension point is called at the end of the MA_Workrequirement_Process
function, the function that processes Works Requirements

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). MA_WorkRequirement_ID of the Work Requirement that is being processed. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  MA_Productionrun_Standard - Finish Process

This extension point is called at the end of the MA_Productionrun_Standard
function, the function used by Create Standards process

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). M_ProductionPlan_ID of the Production Plan that is being processed. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  MA_Workeffort_Validate - Finish Process

This extension point is called at the end of the MA_Workeffort_Validate
function, the function that validates Works Efforts

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). MA_WorkEffort_ID of the Work Effort that is being processed. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  M_Get_Stock - Finish Process

This extension point is called at the end of the M_Get_Stock function, the
function that gets stock from the Warehouse. This function is used in
Warehouse Stock Management  functionality.

From **3.0MP10** it is possible to  customize the stock  that Warehouse Stock
Management proposes.

  * Parameters: 
    * AD_Pinstance_Stock_ID (p_String). AD_Pinstance_ID of the AD_PINSTANCE process from M_Get_Stock 
    * Record_ID. Record_ID of the entity who calls M_Get_Stock. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

###  M_PriceList_Create - Finish Process

This extension point is called at the end of the M_Pricelist_Create function,
the function that create prices based on parameters of the price list version.
See  Price List Version

  * Parameters: 
    * Record_ID (p_String column of AD_EP_Instance_Para). M_PriceList_Version_ID of the Price List Version that is being processed. 
    * DeleteOld (p_String). DeleteOld parameter taken from AD_PInstance_Para. 
    * User (p_String). AD_User_Id who has launched the process. 
    * Message (p_Text). Variable to set a message if needed. 
    * Result (p_Number). Integer to set the result of the process (1 success, 0 error, 2 warning) 

Message and Result have to be retrieved after the procedures have been
launched as they might be changed by those procedures to set warnings and
messages to the user.

Retrieved from "  http://wiki.openbravo.com/wiki/ExtensionPoints  "

This page has been accessed 8,667 times. This page was last modified on 26
January 2018, at 09:01. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

