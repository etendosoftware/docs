---
title: Alerts
---
  
##  Introduction

Alerts are the way Etendo Classic can inform users about virtually any event
that happens in the system (if an appropriate alertrule is created). It can be
defined by the System Administrator (and exported to a module) or by a Client/Organization Administrator.
 This notifications are shown in the top bar, just beside the Application menu.

![](/assets/developer-guide/etendo-classic/concepts/Alerts-0.png){: .legacy-image-style}

##  Alert Rules

The definition of the _Alert Rules_ is made in the _Alert_ window ( _General
Setup || Application || Alert_ ).

##  Data Driven

The Administrator can define a query to test a particular scenario, e.g. Products without defined price, Products under stock, Customers with exceeded credit, etc.

The flow for data driven alerts is as follows:

  * The Administrator creates **alert rules** , which include a SQL clause defining the event that is going to be monitored and the **recipients** for the alerts. 
  * A **background process** is permanently checking if the condition defined in each of the active alert rules return any record, in this case a new **alert instance** will be created for each one of the returned record. 
  * When a user logs in the application there is another process that constantly checks whether there are alert instances for this user and shows them. 

You can find more information about how to define Alerts in  this document.

###  Definition

  * SQL: Example of 'Products without defined price' rule 

    
    
  ```sql
    SELECT m_product_id AS referencekey_id,
           p.name AS record_id,
           '0' AS ad_role_id,
           NULL AS ad_user_id,
           p.name ||' is not in any Purchase price list' AS description,
           'Y' AS isActive,
            ad_org_id, 
            ad_client_id, 
            now() AS created,  
            '0' AS createdBy,  
            now() AS updated,
            '0' AS updatedBy
     FROM m_product p
    WHERE p.ispurchased='Y'
    AND NOT EXISTS (SELECT 1 
                        FROM m_productprice pp,
                             m_pricelist_version pv,
                             m_pricelist pl
                      WHERE p.m_product_id = pp.m_product_id
                      AND pv.m_pricelist_version_id = pv.m_pricelist_version_id
                      AND pv.m_pricelist_id = pl.m_pricelist_id
                      AND issopricelist='N')
    union                  
    SELECT m_product_id AS referencekey_id,
           p.name AS record_id,
           '0' AS ad_role_id,
           NULL AS ad_user_id,
           p.name ||' is not in any Sales price list' AS description,
           'Y' AS isActive,
            ad_org_id, 
            ad_client_id, 
            now() AS created,  
            '0' AS createdBy,  
            now() AS updated,
            '0' AS updatedBy
     FROM m_product p
    WHERE p.ispurchased='N'
    AND NOT EXISTS (SELECT 1 
                        FROM m_productprice pp,
                             m_pricelist_version pv,
                             m_pricelist pl
                      WHERE p.m_product_id = pp.m_product_id
                      AND pv.m_pricelist_version_id = pv.m_pricelist_version_id
                      AND pv.m_pricelist_id = pl.m_pricelist_id
                      AND issopricelist='Y')
  ```

  * The SQL query must have the following columns: 
    * referencekey_id 
    * record_id 
    * ad_role_id 
    * ad_user_id 
    * description 
    * isactive 
    * ad_org_id 
    * ad_client_id 
    * created 
    * createdby 
    * updated 
    * updatedby 

  * Tab: The Alert management window you can navigate directly to a record. In the Tab you define to which tab you'll navigate to. 

  * Filter clause: This is a non-mandatory SQL whereclause which will be used to filter the alerts which will be shown to the user. 

###  Performance

The sql commands you define in alert rules will be executed periodically in
your system. Therefore, it is very important to define them as performance-
efficient.

If they are not, they will slow down your system noticeably.



##  Alert Recipient

The Alert Recipient tab handles the alert recipients management. You can
define the Role whom will be notified, or an specific user. Also you can
define if the user(s) should be notified by email.

