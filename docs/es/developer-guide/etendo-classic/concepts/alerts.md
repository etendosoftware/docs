---
title: Alertas
tags:
  - Concepts
  - alerts
  - system administration
  - alert rules
  - data-driven alerts
  - user notifications
---

# Alertas


##  Visión general

Las alertas son la forma en que Etendo Classic puede informar a los usuarios sobre prácticamente cualquier evento
que ocurra en el sistema (si se crea una regla de alerta adecuada). Puede ser
definida por el Administrador del sistema (y exportada a un módulo) o por un Administrador de Cliente/Organización.

Estas notificaciones se muestran en la barra superior, justo al lado del menú de Aplicación.

![]( ../../../assets/developer-guide/etendo-classic/concepts/Alerts-0.png)


##  Regla de alerta

La definición de la _Regla de alerta_ se realiza en la ventana _Alertas_ (`General Setup` > `Application ` >`Alert`).

##  Basadas en datos

El Administrador puede definir una consulta para comprobar un escenario concreto, por ejemplo: productos sin precio definido, productos por debajo del stock, clientes con el crédito excedido, etc.

El flujo de las alertas basadas en datos es el siguiente:

  * El Administrador crea *reglas de alerta*, que incluyen una cláusula SQL que define el evento que se va a monitorizar, y los *receptores* de las alertas. 
  * Un *proceso en segundo plano* comprueba permanentemente si la condición definida en cada una de las reglas de alerta activas devuelve algún registro; en ese caso, se creará una nueva *instancia de alerta* para cada uno de los registros devueltos. 
  * Cuando un usuario inicia sesión en la aplicación, existe otro proceso que comprueba constantemente si hay instancias de alerta para este usuario y las muestra. 

!!!info
    Para más información, consulte [cómo crear una alerta](../../../developer-guide/etendo-classic/how-to-guides/How_to_create_an_Alert.md).

###  Definición

  * SQL: Ejemplo de la regla "Productos sin precio definido" 

    
    
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
    UNION                  
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

  * La consulta SQL debe tener las siguientes columnas: 
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

  * Solapa: desde la ventana de gestión de alertas puede navegar directamente a un registro. Desde la solapa se puede definir a qué solapa se navegará. 

  * Cláusula de filtro: esta es una cláusula SQL WHERE no obligatoria que se utilizará para filtrar las alertas que se mostrarán al usuario. 

###  Rendimiento

Los comandos SQL definidos en las reglas de alerta se ejecutarán periódicamente en
su sistema. Por lo tanto, es muy importante definirlos de forma eficiente en términos de rendimiento.

Si no lo son, ralentizarán su sistema de forma notable.


##  Receptor de Alerta

La solapa Receptor de Alerta gestiona la administración de los receptores de alertas. Puede
definir el Rol que será notificado, o un usuario específico. También puede
definir si el/los usuario(s) deben ser notificados por correo electrónico.

---

Este trabajo es una obra derivada de [Alertas](https://wiki.openbravo.com/wiki/Alerts){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.