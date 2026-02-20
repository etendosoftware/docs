---
title: Cómo realizar una consulta compleja usando el DAL
tags:
    - Consulta compleja 
    - DAL
    - SQL 
status: beta
---

# Cómo realizar una consulta compleja usando el DAL
 
!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
## Visión general

Esta sección ilustra cómo se puede programar una consulta compleja utilizando construcciones de la Capa de Acceso a Datos (DAL). La solución utilizará [Hibernate HQL](https://docs.hibernate.org/orm/3.5/reference/en/html/queryhql.html){target="\_blank"}, por lo que, antes de leer este procedimiento, asegúrese de que **conoce los conceptos básicos de HQL**.

El procedimiento comienza con una consulta SQL del formulario de solicitud a pedido dentro de la Gestión de Aprovisionamiento y de la recepción de mercancías pendiente, y la traduce a una representación en HQL. Se tratan distintos aspectos del uso de HQL y de la DAL, incluidos aspectos de rendimiento y depuración.
## Configurar un caso de prueba

Existe un procedimiento independiente sobre cómo crear casos de prueba utilizando la Capa de Acceso a Datos (consulte [aquí](./how-to-create-testcases/how-to-create-junit-testcases.md)). En este procedimiento, solo proporcionaremos un resumen.

El caso de prueba que utilizaremos se crea dentro del directorio de módulos del proyecto de desarrollo de Etendo. En realidad no crearemos un nuevo módulo en la base de datos, pero es mejor colocar el código personalizado separado del árbol de fuentes principal de Etendo. Para crear una nueva carpeta de código fuente en IntelliJ, haga clic con el botón derecho en `project/modules` y seleccione **Nuevo** y, a continuación, carpeta de código fuente.

En la carpeta de código fuente, cree un nuevo paquete (haga clic con el botón derecho en la nueva carpeta y seleccione Nuevo > paquete): `org.openbravo.howto.query`. Dentro de este paquete cree un archivo Java `QueryTest.java`. Este archivo tiene el siguiente contenido:

``` java
package org.openbravo.howto.query;

import org.openbravo.test.base.OBBaseTest;

/**
* Complex queries howto.
*/

public class QueryTest extends OBBaseTest {

public void testQueryOne() {
    // this sets the user to the Etendo Admin
    setUserContext("100");

    // here we will be doing our stuff...

    commitTransaction();
}
}
```

Este caso de prueba hereda de la clase `OBBaseTest` proporcionada por Etendo. La clase base de pruebas proporciona un contexto de usuario y gestión de transacciones. Hay un método de prueba en la clase: `testQueryOne`. Este método primero selecciona el contexto de usuario. El `commitTransaction()` al final confirma la transacción. Si se produce una excepción durante la prueba, entonces esta sentencia no se ejecutará y la transacción se revierte automáticamente.

Puede hacer clic con el botón derecho en el archivo Java en IntelliJ y, a continuación, ejecutar como > caso de prueba JUnit; debería ver la barra verde en la vista de JUnit:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-do-a-complex-queryusing-dal/how-to-do-a-complex-query-using-dal-1.png)
  
Esta es la configuración principal del caso de prueba. La siguiente sección añadirá algo de código a los casos de prueba para consultar la DAL y mostrar algunos resultados.
## Consulta SQL de solicitud de compra

La siguiente consulta SQL se traducirá a HQL:

``` sql
SELECT M_REQUISITIONLINE_ID, M_REQUISITIONLINE.NEEDBYDATE,
M_REQUISITIONLINE.QTY - M_REQUISITIONLINE.ORDEREDQTY AS QTYTOORDER,
M_REQUISITIONLINE.PRICEACTUAL AS PRICE,
AD_COLUMN_IDENTIFIER(to_char('C_BPartner'),
    to_char(COALESCE(M_REQUISITIONLINE.C_BPARTNER_ID, M_REQUISITION.C_BPARTNER_ID)), ?) AS VENDOR,
AD_COLUMN_IDENTIFIER(to_char('M_PriceList'), to_char(COALESCE(M_REQUISITIONLINE.M_PRICELIST_ID, 
M_REQUISITION.M_PRICELIST_ID)), ?) AS PRICELISTID,
AD_COLUMN_IDENTIFIER(to_char('M_Product'), 
    to_char(M_REQUISITIONLINE.M_PRODUCT_ID), ?) AS PRODUCT,
AD_COLUMN_IDENTIFIER(to_char('M_AttributeSetInstance'), 
    to_char(M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID), ?) AS ATTRIBUTE,
AD_COLUMN_IDENTIFIER(to_char('AD_User'), to_char(M_REQUISITION.AD_USER_ID), ?) AS REQUESTER
FROM M_REQUISITIONLINE, M_REQUISITION, C_BPARTNER
WHERE M_REQUISITIONLINE.M_REQUISITION_ID = M_REQUISITION.M_REQUISITION_ID
AND COALESCE(M_REQUISITIONLINE.C_BPARTNER_ID,M_REQUISITION.C_BPARTNER_ID) = C_BPARTNER.C_BPARTNER_ID
AND C_BPARTNER.PO_PAYMENTTERM_ID IS NOT NULL
AND M_REQUISITION.ISACTIVE = 'Y'
AND M_REQUISITIONLINE.ISACTIVE = 'Y'
AND M_REQUISITION.DOCSTATUS = 'CO'
AND M_REQUISITIONLINE.REQSTATUS = 'O'
AND (M_REQUISITIONLINE.LOCKEDBY IS NULL OR 
                    COALESCE (M_REQUISITIONLINE.LOCKDATE, TO_DATE('01-01-1900', 'DD-MM-YYYY')) < (now()-3))
AND M_REQUISITION.AD_CLIENT_ID IN ?
AND M_REQUISITIONLINE.AD_ORG_ID IN ?
AND M_REQUISITIONLINE.NEEDBYDATE >= ?
AND M_REQUISITIONLINE.NEEDBYDATE < ?
AND M_REQUISITIONLINE.M_PRODUCT_ID = ?
AND M_REQUISITION.AD_USER_ID = TO_CHAR(?)
AND ((M_REQUISITIONLINE.C_BPARTNER_ID = ? OR M_REQUISITION.C_BPARTNER_ID = ?) OR 
    (M_REQUISITIONLINE.C_BPARTNER_ID IS NULL AND M_REQUISITION.C_BPARTNER_ID IS NULL))
ORDER BY M_REQUISITIONLINE.NEEDBYDATE, M_REQUISITIONLINE.M_PRODUCT_ID, M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID
```

Esta consulta se utiliza en el formulario de conversión de solicitud de compra a pedido dentro de Gestión de aprovisionamiento. Devuelve la información de la línea de solicitud de compra con los identificadores de su tercero, producto, tarifa, etc.

El [Lenguaje de consulta de Hibernate](https://docs.hibernate.org/core/3.5/reference/en/html/queryhql.html){target="\_blank"} permite consultar un objeto de negocio completo. Las columnas especificadas en la cláusula select anterior están todas relacionadas con la Línea de solicitud de compra. Por tanto, en **HQL** la consulta se utilizará para filtrar el objeto principal: la Línea de solicitud de compra, y después recuperar la información requerida desde el objeto Línea de solicitud de compra. Un segundo paso describe cómo hacer la consulta más eficiente para evitar el problema de selección N + 1.

!!! Note
    En HQL, se utiliza el concepto de Entidad y Propiedades.

### Traducción a HQL

Esta sección muestra cómo traducir la consulta SQL anterior a una consulta HQL utilizando la Capa de Acceso a Datos.

La consulta y sus resultados se han probado contra los datos de prueba de Small Bazaar. Utiliza el usuario *Admin* de Etendo; este usuario se ha configurado con el rol *F&B Admin* tal como se muestra a continuación (Nota: se ha marcado el campo por defecto). Para mostrar resultados, se han introducido nuevas solicitudes de compra en Etendo para el producto y el tercero utilizados en este procedimiento.
  
- Comience estableciendo el contexto de usuario al usuario estándar Admin de Etendo. La consulta se construirá utilizando un `StringBuilder`. La cláusula where comienza con 'as rl', esto se debe a que sabemos que consultaremos `RequisitionLine` y utilizaremos el alias `rl` en el resto de la cláusula where. La [DAL](../concepts/data-access-layer.md) añadirá la cláusula select automáticamente más adelante.

    ``` java
    setUserContext("100");
     
    // create the where clause stringbuilder
    final StringBuilder whereClause = new StringBuilder();
    // rl is used as the alias for the RequisitionLine
    whereClause.append(" as rl");
     
    // Initialize the parameter map, will be used to
    // add parameters to the query
    final Map<String, Object> parameters = new HashMap<>(6);
    ```

- A continuación, añada un left outer join sobre la propiedad de tercero de la línea de solicitud de compra y de la solicitud de compra:

    ``` java
    // do a left outer join on business partner as it can be null
    // in both the requisition line and the requisition
    whereClause.append(" left outer join rl.businessPartner ");
    whereClause.append(" left outer join rl.requisition.businessPartner ");
    ```

    !!!note
        El `HQL` utiliza nombres de propiedades y entidades de los objetos de negocio de Etendo. Consulte el manual de referencia del Modelo de Entidades para obtener un listado completo de todas las entidades. También puede encontrar los nombres correctos revisando el código generado en la carpeta `src-gen`. Puede buscar en esta carpeta usando los nombres de tabla para encontrar la entidad correcta.  

    El left outer join es necesario porque en la cláusula where habrá expresiones que utilizan propiedades del tercero. Si no se especifica un left outer join explícito, entonces Hibernate utilizará un inner join. Con un inner join, si el tercero es nulo para una línea de solicitud de compra, entonces no se devuelven resultados.

- La siguiente cláusula utiliza el tercero unido.

    ``` java
    // AND COALESCE(M_REQUISITIONLINE.C_BPARTNER_ID,M_REQUISITION.C_BPARTNER_ID) = C_BPARTNER.C_BPARTNER_ID
    // AND C_BPARTNER.PO_PAYMENTTERM_ID IS NOT NULL
    whereClause.append(" where (rl.businessPartner.pOPaymentTerms != null or rl.requisition.businessPartner.pOPaymentTerms != null)");
    ```

- Las siguientes líneas añaden más cláusulas where; tenga en cuenta que la Capa de Acceso a Datos añadirá automáticamente un filtro por activo:

    ``` java
    // AND M_REQUISITION.ISACTIVE = 'Y'
    whereClause.append(" and rl.requisition.active=true");
     
    // AND M_REQUISITIONLINE.ISACTIVE = 'Y' <-- is done by the DAL Layer
     
    // AND M_REQUISITION.DOCSTATUS = 'CO'
    whereClause.append(" and rl.requisition.documentStatus='CO'");
     
    // AND M_REQUISITIONLINE.REQSTATUS = 'O'
    whereClause.append(" and rl.requisitionLineStatus='O'");
    ```

- A continuación, añada el filtro `lockedBy` y `lockDate`. El coalesce se traduce en un or; la fecha se añade como un parámetro usando un objeto Date de Java. Tenga en cuenta que HQL soporta coalesce (aunque aquí no lo utilizaremos).

    ``` java
    // AND (M_REQUISITIONLINE.LOCKEDBY IS NULL OR
    // COALESCE (M_REQUISITIONLINE.LOCKDATE, TO_DATE('01-01-1900', 'DD-MM-YYYY')) < (now()-3))
    whereClause.append(" and (rl.lockedBy = null or rl.lockDate<:lockDate or rl.lockDate = null)");   
    final long threeDays = 1000 * 3600 * 24 * 3;
    parameters.put("lockDate", new Date(System.currentTimeMillis() - threeDays));
    ```

- La Capa de Acceso a Datos añade automáticamente el filtrado por organización/cliente; el filtro `needByDate` se realiza añadiendo dos parámetros:

    ```java
    // AND M_REQUISITION.AD_CLIENT_ID IN ? <-- Done by the DAL
    // AND M_REQUISITIONLINE.AD_ORG_ID IN ? <-- Done by the DAL
     
    // AND M_REQUISITIONLINE.NEEDBYDATE >= ?
    whereClause.append(" and rl.needByDate>=:needByDateFrom");
    // needByDate from, set at 30 days back
    final long thirtyDays = threeDays * 10;
    parameters.put("needByDateFrom", new Date(System.currentTimeMillis() - thirtyDays));
     
    // AND AND M_REQUISITIONLINE.NEEDBYDATE < ?
    whereClause.append(" and rl.needByDate<:needByDateTo");
    // needByDate to, set at 30 days in the future
    parameters.put("needByDateTo", new Date(System.currentTimeMillis() + thirtyDays));
    ```

- El filtro de producto y de contacto de usuario se añade así. Tenga en cuenta que los valores reales dependen de la base de datos utilizada:

    ``` java
    // AND M_REQUISITIONLINE.M_PRODUCT_ID = ?
    whereClause.append(" and rl.product.id=:productId");
    parameters.put("productId", "1000010");
     
    // AND M_REQUISITION.AD_USER_ID = TO_CHAR(?)
    whereClause.append(" and rl.requisition.userContact.id=:userId");
    parameters.put("userId", "100");
    ```

- El filtro por tercero se añade como se muestra a continuación. Tenga en cuenta que el tercero de la solicitud de compra también puede ser nulo:

    ``` java
    // AND ((M_REQUISITIONLINE.C_BPARTNER_ID = ? OR M_REQUISITION.C_BPARTNER_ID = ?) OR
    // (M_REQUISITIONLINE.C_BPARTNER_ID IS NULL AND M_REQUISITION.C_BPARTNER_ID IS NULL))
    // ORDER BY M_REQUISITIONLINE.NEEDBYDATE, M_REQUISITIONLINE.M_PRODUCT_ID,
    // M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID
    whereClause
        .append(" and ((rl.businessPartner.id = :bpId or rl.requisition.businessPartner.id = :bpId) or "
            + "(rl.businessPartner = null and rl.requisition.businessPartner = null))");
    parameters.put("bpId", "1000011");
    ```

    En este código el id del tercero es `1000011`; esto puede ser diferente en distintas bases de datos.

- En la última parte de la construcción de la consulta se añade el order by, se crea la consulta y se establecen los parámetros:

    ``` java
    // ORDER BY M_REQUISITIONLINE.NEEDBYDATE, M_REQUISITIONLINE.M_PRODUCT_ID,
    // M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID
    whereClause.append(" order by rl.needByDate, rl.product.id, rl.attributeSetValue.id");
     
    final OBQuery<RequisitionLine> obQuery = OBDal.getInstance().createQuery(RequisitionLine.class,
        whereClause.toString());
     
    obQuery.setNamedParameters(parameters);
    ```

- El HQL total es:

``` sql
SELECT rl 
FROM ProcurementRequisitionLine  AS rl 
    LEFT OUTER JOIN rl.businessPartner  
    LEFT OUTER JOIN rl.requisition.businessPartner  
WHERE ( (rl.businessPartner.pOPaymentTerms != NULL OR rl.requisition.businessPartner.pOPaymentTerms != NULL) 
AND rl.requisition.active=true 
AND rl.requisition.documentStatus='CO' 
AND rl.requisitionLineStatus='O' 
AND (rl.lockedBy = NULL OR rl.lockDate<:lockDate OR rl.lockDate = NULL) 
AND rl.needByDate>=:needByDateFrom AND rl.needByDate<:needByDateTo 
AND rl.product.id=:productId 
AND rl.requisition.userContact.id=:userId 
AND ((rl.businessPartner.id = :bpId OR rl.requisition.businessPartner.id = :bpId) 
    OR (rl.businessPartner = NULL AND rl.requisition.businessPartner = NULL)) ) 
AND rl.organization.id  IN ('1000007', '1000008', '1000009', '0', '1000000', '1000002', '1000003', 
        '1000004', '1000005', '1000006') 
AND rl.client.id  IN ('1000000', '0') 
AND rl.active='Y' 
ORDER BY rl.needByDate, rl.product.id, rl.attributeSetValue.id
```

### Ejecución de la consulta HQL y recuperación de resultados

El HQL se ejecuta cuando se llama al método list sobre el objeto de consulta. Esto se hace en un bucle for para procesar todos los resultados. Como puede ver, el método `list()` devuelve una lista con conversión de tipo de objetos `RequisitionLine`. Esto hace que desarrollar contra el resultado de una consulta sea muy sencillo y además seguro en cuanto a tipos.

``` java
// now print the select clause parts
for (RequisitionLine requisitionLine : obQuery.list()) {
```

Dentro del bucle for se obtiene y se imprime la información de `RequisitionLine`.

``` java
// now print the information from the select clause
// SELECT M_REQUISITIONLINE_ID, M_REQUISITIONLINE.NEEDBYDATE,
System.err.println(requisitionLine.getId());
System.err.println(requisitionLine.getNeedByDate());
 
// M_REQUISITIONLINE.QTY - M_REQUISITIONLINE.ORDEREDQTY AS QTYTOORDER,
if (requisitionLine.getOrderQuantity() != null) {       
System.err.println(requisitionLine.getQuantity().min(requisitionLine.getOrderQuantity()));
}
 
// M_REQUISITIONLINE.PRICEACTUAL AS PRICE,
System.err.println(requisitionLine.getUnitPrice());
```

El identificador de un objeto se recupera llamando al método `getIdentifier()`; esto es diferente de antes, que requería llamar a una función de base de datos:

``` java
// AD_COLUMN_IDENTIFIER(to_char('C_BPartner'),
// to_char(COALESCE(M_REQUISITIONLINE.C_BPARTNER_ID, M_REQUISITION.C_BPARTNER_ID)), ?) AS
// VENDOR,
if (requisitionLine.getBusinessPartner() != null) {
System.err.println(requisitionLine.getBusinessPartner().getIdentifier());
} else if (requisitionLine.getRequisition().getBusinessPartner() != null) {       
System.err.println(requisitionLine.getRequisition().getBusinessPartner().getIdentifier());
}
 
// AD_COLUMN_IDENTIFIER(to_char('M_PriceList'),
// to_char(COALESCE(M_REQUISITIONLINE.M_PRICELIST_ID,
// M_REQUISITION.M_PRICELIST_ID)), ?) AS PRICELISTID,
if (requisitionLine.getPriceList() != null) {
System.err.println(requisitionLine.getPriceList().getIdentifier());
} else if (requisitionLine.getRequisition().getPriceList() != null) {
System.err.println(requisitionLine.getRequisition().getPriceList().getIdentifier());
}
 
// AD_COLUMN_IDENTIFIER(to_char('M_Product'),
// to_char(M_REQUISITIONLINE.M_PRODUCT_ID), ?) AS PRODUCT,
System.err.println(requisitionLine.getProduct().getIdentifier());
 
// AD_COLUMN_IDENTIFIER(to_char('M_AttributeSetInstance'),
// to_char(M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID), ?) AS ATTRIBUTE,
if (requisitionLine.getAttributeSetValue() != null) {
System.err.println(requisitionLine.getAttributeSetValue().getIdentifier());
}
 
// AD_COLUMN_IDENTIFIER(to_char('AD_User'), to_char(M_REQUISITION.AD_USER_ID), ?) AS REQUESTER
System.err.println(requisitionLine.getRequisition().getUserContact().getIdentifier());
}
```

### El resultado

El código anterior produce la siguiente salida:

``` txt
2FA597B938EF4007A6AE5E85068BD98B
2009-04-01 00:00:00.0
0.94
Bell Phone Company
Purchase
Screwdriver
Etendo
10000000 Screwdriver 10 2009-04-01 00:00:00.0
```

### El SQL ejecutado, el problema de selección N+1

Ahora veamos el SQL real que se ejecuta. Esto también mostrará que la implementación anterior podría sufrir el problema de selección N+1.

La consulta SQL se ejecuta cuando se llama al método `list()` sobre el objeto de consulta (el inicio del bucle for). Hibernate genera la siguiente consulta SQL:

``` sql
SELECT procuremen0_.M_Requisitionline_ID AS M1_297_, procuremen0_.AD_Client_ID AS AD2_297_, procuremen0_.AD_Org_ID AS AD3_297_, 
    procuremen0_.IsActive AS IsActive297_, procuremen0_.Created AS Created297_, procuremen0_.Createdby AS Createdby297_, 
    procuremen0_.Updated AS Updated297_, procuremen0_.Updatedby AS Updatedby297_, procuremen0_.M_Requisition_ID AS M9_297_, 
    procuremen0_.M_Product_ID AS M10_297_, procuremen0_.Qty AS Qty297_, procuremen0_.PriceList AS PriceList297_, 
    procuremen0_.LineNetAmt AS LineNetAmt297_, procuremen0_.C_BPartner_ID AS C14_297_, procuremen0_.C_UOM_ID AS C15_297_, 
    procuremen0_.M_Product_Uom_Id AS M16_297_, procuremen0_.QuantityOrder AS Quantit17_297_, procuremen0_.M_AttributeSetInstance_ID AS M18_297_, 
    procuremen0_.Reqstatus AS Reqstatus297_, procuremen0_.Orderedqty AS Orderedqty297_, procuremen0_.Description AS Descrip21_297_, 
    procuremen0_.Changestatus AS Changes22_297_, procuremen0_.Internalnotes AS Interna23_297_, procuremen0_.Suppliernotes AS Supplie24_297_, 
    procuremen0_.Dateplanned AS Datepla25_297_, procuremen0_.Needbydate AS Needbydate297_, 
    procuremen0_.PriceActual AS PriceAc27_297_, procuremen0_.Discount AS Discount297_, 
    procuremen0_.C_Currency_ID AS C29_297_, procuremen0_.Lockedby AS Lockedby297_, procuremen0_.Lockqty AS Lockqty297_, 
    procuremen0_.Lockprice AS Lockprice297_, procuremen0_.M_PriceList_ID AS M33_297_, procuremen0_.Lockdate AS Lockdate297_, 
    procuremen0_.Lockcause AS Lockcause297_, procuremen0_.Line AS Line297_ 
FROM M_RequisitionLine procuremen0_ 
    LEFT OUTER JOIN C_BPartner businesspa1_ ON procuremen0_.C_BPartner_ID=businesspa1_.C_BPartner_ID 
    LEFT OUTER JOIN M_Requisition procuremen2_ ON procuremen0_.M_Requisition_ID=procuremen2_.M_Requisition_ID 
    LEFT OUTER JOIN C_BPartner businesspa3_ ON procuremen2_.C_BPartner_ID=businesspa3_.C_BPartner_ID 
WHERE (businesspa1_.PO_PaymentTerm_ID IS NOT NULL OR businesspa3_.PO_PaymentTerm_ID IS NOT NULL) 
AND procuremen2_.IsActive='Y' 
AND procuremen2_.DocStatus='CO' 
AND procuremen0_.Reqstatus='O' 
AND (procuremen0_.Lockedby IS NULL OR procuremen0_.Lockdate<? OR procuremen0_.Lockdate IS NULL) 
AND procuremen0_.Needbydate>=? AND procuremen0_.Needbydate<? 
AND procuremen0_.M_Product_ID=? 
AND procuremen2_.AD_User_ID=? 
AND (procuremen0_.C_BPartner_ID=? OR procuremen2_.C_BPartner_ID=? OR 
    (procuremen0_.C_BPartner_ID IS NULL) AND (procuremen2_.C_BPartner_ID IS NULL)) 
AND (procuremen0_.AD_Org_ID IN ('1000007' , '1000008' , '1000009' , '0' , '1000000' , '1000002' , '1000003' , '1000004' , '1000005' , '1000006')) 
AND (procuremen0_.AD_Client_ID IN ('1000000' , '0')) 
AND procuremen0_.IsActive='Y' 
ORDER BY procuremen0_.Needbydate, procuremen0_.M_Product_ID, procuremen0_.M_AttributeSetInstance_ID
```

Al comparar este SQL con el SQL original, la principal diferencia es que se selecciona mucha más información. Esto se debe a que en este enfoque se elige seleccionar el objeto `RequisitionLine` completo. Esto hace que la consulta HQL sea mucho más sencilla, pero también menos eficiente. También es posible seleccionar los campos individuales de `RequisitionLine`; en ese caso debe utilizarse una consulta directa de Hibernate.

Ahora, veamos qué ocurre cuando se solicita información desde el objeto `RequisitionLine`. El objeto `OrderLine` referencia otros objetos que se cargan de forma diferida (bajo demanda). Por tanto, lo que verá es que Hibernate lanza consultas adicionales (este es el problema de selección N+1).

Cuando en el bucle for se ejecuta la siguiente sentencia:

``` java
} else if (requisitionLine.getRequisition().getBusinessPartner() != null) {
```

Entonces Hibernate lanza esta sentencia SQL:

``` sql
SELECT procuremen0_.M_Requisition_ID AS M1_263_0_, procuremen0_.AD_Client_ID AS AD2_263_0_, 
.... (list of COLUMNS abbreviated FOR clarity)
FROM M_Requisition procuremen0_ WHERE procuremen0_.M_Requisition_ID=?
```

Hibernate hace esto porque el objeto Requisition (en la Línea de solicitud de compra) inicialmente se carga de forma **lazy loaded**; esto significa que la instancia de Requisition se ha creado, pero sus datos aún no se han recuperado de la base de datos. El código Java anterior accede a la solicitud de compra (recuperando el tercero) y, por tanto, inicia la carga del objeto Requisition.

La misma situación ocurre al acceder al tercero, producto y tarifa en las siguientes sentencias Java:

``` java
System.err.println(requisitionLine.getRequisition().getBusinessPartner().getIdentifier());
....
System.err.println(requisitionLine.getPriceList().getIdentifier());
.....
System.err.println(requisitionLine.getRequisition().getPriceList().getIdentifier());
.....
System.err.println(requisitionLine.getProduct().getIdentifier());
```

Dando como resultado cuatro consultas adicionales para recuperar la información requerida. Por tanto, para cada `RequisitionLine` potencialmente se realizan 5 consultas adicionales. Esto puede resultar en un rendimiento inferior.

Hibernate ofrece una forma de resolver este problema: usar left join fetch en la consulta original; en este enfoque, la información referenciada se recupera junto con la consulta principal. Esto se trata a continuación. 

Para habilitar el left join fetch para los objetos relacionados, se debe añadir lo siguiente a la cláusula where (sustituyendo el left outer join utilizado anteriormente):

``` java
whereClause.append(" left join fetch rl.product");
whereClause.append(" left join fetch rl.businessPartner");
whereClause.append(" left join fetch rl.businessPartner.language");
whereClause.append(" left join fetch rl.requisition");
whereClause.append(" left join fetch rl.priceList");
whereClause.append(" left join fetch rl.requisition.businessPartner");
whereClause.append(" left join fetch rl.requisition.businessPartner.language");
```

Esto resuelve el problema N+1 para este caso. Sin embargo, es evidente que esto añade muchos joins a la consulta.
## Consulta SQL de línea de pedido

La siguiente consulta SQL se traducirá a una representación DAL:

``` sql
SELECT ID, C_ORDER_ID, DOCUMENTNO, DATEORDERED, C_BPARTNER_ID, PARTNER_NAME, PRODUCT_NAME, DESCRIPTION, TOTAL_QTY, 
QTYORDERED, ISACTIVE, ? AS DATE_FORMAT
FROM(
SELECT C_ORDERLINE.C_ORDERLINE_ID AS ID, C_ORDER.C_ORDER_ID AS C_ORDER_ID, 
C_ORDER.DOCUMENTNO AS DOCUMENTNO, C_ORDER.DATEORDERED AS DATEORDERED,
C_BPARTNER.C_BPARTNER_ID AS C_BPARTNER_ID, C_BPARTNER.NAME AS PARTNER_NAME,
AD_COLUMN_IDENTIFIER(TO_CHAR('M_Product'), TO_CHAR(C_ORDERLINE.M_PRODUCT_ID), TO_CHAR(?)) AS PRODUCT_NAME, 
M_ATTRIBUTESETINSTANCE.DESCRIPTION AS DESCRIPTION, C_ORDERLINE.QTYORDERED AS TOTAL_QTY,
C_ORDERLINE.QTYORDERED-SUM(COALESCE(M_MATCHPO.QTY,0)) AS QTYORDERED, '-1' AS ISACTIVE
FROM C_ORDERLINE LEFT JOIN M_MATCHPO ON C_ORDERLINE.C_ORDERLINE_ID = M_MATCHPO.C_ORDERLINE_ID
AND M_MATCHPO.M_INOUTLINE_ID IS NOT NULL
LEFT JOIN M_ATTRIBUTESETINSTANCE ON C_ORDERLINE.M_ATTRIBUTESETINSTANCE_ID = M_ATTRIBUTESETINSTANCE.M_ATTRIBUTESETINSTANCE_ID,
C_ORDER, C_BPARTNER
WHERE C_ORDER.C_BPARTNER_ID = C_BPARTNER.C_BPARTNER_ID
AND C_ORDER.C_ORDER_ID = C_ORDERLINE.C_ORDER_ID
AND C_ORDER.AD_CLIENT_ID IN ('1')
AND C_ORDER.AD_ORG_ID IN ('1')
AND C_ORDER.ISSOTRX='N'
AND C_BPARTNER.C_BPARTNER_ID = ?
AND C_ORDER.DOCSTATUS = 'CO'
GROUP BY C_ORDERLINE.C_ORDERLINE_ID, C_ORDER.C_ORDER_ID, C_ORDER.DOCUMENTNO, C_ORDER.DATEORDERED, C_BPARTNER.C_BPARTNER_ID,
C_BPARTNER.NAME, C_ORDERLINE.M_PRODUCT_ID, M_ATTRIBUTESETINSTANCE.DESCRIPTION, C_ORDERLINE.QTYORDERED
ORDER BY PARTNER_NAME, DOCUMENTNO, DATEORDERED)
WHERE QTYORDERED <>0
ORDER BY C_BPARTNER_ID, ID
```

Esta consulta procede del manual de recepción de mercancías pendiente.

Al traducir esta consulta a una consulta de [Hibernate Query Language](https://docs.hibernate.org/core/3.5/reference/en/html/queryhql.html){target="\_blank"}, deben tenerse en cuenta los siguientes aspectos:

- Hibernate no admite el uso de alias de `select` dentro de la cláusula `where`.
- Hibernate no admite el uso de un `select` que seleccione resultados de otro `select`.
- Con HQL podemos consultar objetos de negocio completos y navegar por el grafo de objetos después de la consulta para recuperar resultados adicionales.

Con esto en mente, utilizaremos un enfoque de consulta ligeramente diferente en HQL. La mayor parte de la información en la parte `select` está relacionada con la línea de pedido. Por tanto, en HQL la consulta se utilizará para filtrar el objeto principal: `OrderLine`, y después recuperar la información requerida desde la línea de pedido. En un segundo paso, se analiza cómo hacer la consulta más eficiente para evitar el conocido problema de selección N + 1.

Veamos qué hace la consulta anterior:

- Consulta la suma de la cantidad en los PO emparejados para una determinada línea de pedido y filtra las líneas de pedido cuya cantidad pedida es distinta de esa suma.
- La línea de pedido se filtra además usando otros parámetros (tercero, estado del documento, etc.).
- Después, los resultados se muestran en un orden determinado; la ordenación del `select` interno no es importante, ya que el `select` externo vuelve a ordenar.

El siguiente paso es traducir este enfoque a HQL. Inicialmente ignoraremos la parte `select` porque esta información se recupera de los objetos de negocio de líneas de pedido devueltos por el HQL.

### Traducción a HQL

En esta sección, el SQL anterior se traduce a HQL. Para HQL, utilizaremos el concepto Entidad/Propiedad frente al concepto Tabla/Columna de SQL.

La consulta y sus resultados se han probado con los datos de prueba de **Small Bazaar**. Utiliza el usuario Etendo Admin; a este usuario se le ha asignado el rol Etendo Admin tal y como se muestra a continuación (nota: marque la casilla por defecto).

En primer lugar, establezca el contexto de usuario al usuario estándar Etendo Admin. La consulta se construirá usando un `StringBuilder`. La cláusula `where` comienza con `as ol`; esto se debe a que sabemos que consultaremos la entidad `OrderLine` y usaremos el alias `ol` en el resto de la cláusula `where`.

``` java
setUserContext("100");
 
// create the where clause
final StringBuilder whereClause = new StringBuilder();
// set the alias, the OrderLine will be added by the DAL
whereClause.append(" as ol ");
```

A continuación, añada el filtrado sobre la suma de las cantidades de los PO emparejados. Observe el uso del alias en la _cláusula where_ del subselect.

``` java
// the subselect to filter on the matched purchase invoices, only orders with a
// different order quantity are returned.
whereClause.append(" where ol.orderedQuantity <> ");
whereClause.append(" (select sum(quantity) from ProcurementPOInvoiceMatch ").append(" where goodsShipmentLine is not null and salesOrderLine=ol)");
```

!!!note
    El HQL utiliza nombres de propiedades y entidades de los objetos de negocio de Etendo. También puede encontrar los nombres correctos revisando el código generado en la carpeta `src-gen`. Puede buscar en esta carpeta usando los nombres de tabla para encontrar la entidad correcta.
  
Añada otras opciones de filtrado; el filtrado por organización y cliente lo realiza la Capa de Acceso a Datos, por lo que no es necesario tenerlo en cuenta explícitamente. La columna de transacción de ventas en la base de datos contiene `'Y'` o `'N'`, pero como en Java usamos booleanos, podemos usar `true` o `false` en la cláusula `where` (aquí es `false`).

``` java
// Other filtering options:
// AND C_ORDER.AD_CLIENT_ID IN ('1') <-- these are done automatically by the dal
// AND C_ORDER.AD_ORG_ID IN ('1') <-- these are done automatically by the dal
 
// AND C_ORDER.ISSOTRX='N'
whereClause.append(" and ol.salesOrder.salesTransaction=false ");
```

Añada el filtrado por tercero y estado del documento. El parámetro de tercero se añade a continuación.

``` java
// AND C_BPARTNER.C_BPARTNER_ID = ?
// note the value of the parameter is set below
whereClause.append(" and ol.salesOrder.businessPartner.id=:bpId ");
 
// AND C_ORDER.DOCSTATUS = 'CO'
whereClause.append(" and ol.salesOrder.documentStatus='CO' ");
```

Añada el `order by`.

``` java
// ORDER BY C_BPARTNER_ID, ID
whereClause.append(" order by ol.salesOrder.businessPartner.id, ol.id");
```

Ahora ya estamos listos para crear el objeto `OBQuery` usando la clase principal que estamos consultando (la `OrderLine.class`) y la cláusula `where`. También se añade el parámetro de tercero. Se utiliza el id de tercero 1000017; esto puede variar en función de los datos de la base de datos.

``` java
// final Session session = OBDal.getInstance().getSession();
// session.createQuery(hql.toString());
final OBQuery<OrderLine> qry = OBDal.getInstance().createQuery(OrderLine.class,
    whereClause.toString());
 
// set the business partner parameter
final Map<String, Object> parameters = new HashMap<>(1);
parameters.put("bpId", "1000017");
qry.setNamedParameters(parameters);
```

La cláusula `where` anterior da como resultado la siguiente consulta HQL global (que no es visible directamente, ya que se mantiene dentro del objeto `OBQuery`):

``` sql
SELECT ol FROM OrderLine  AS ol 
WHERE ( ol.orderedQuantity <>  (SELECT sum(quantity) FROM  
    ProcurementPOInvoiceMatch WHERE goodsShipmentLine IS NOT NULL AND salesOrderLine=ol) 
AND ol.salesOrder.salesTransaction=false  
AND ol.salesOrder.businessPartner.id=:bpId  
AND ol.salesOrder.documentStatus='CO') 
AND ol.organization.id  IN ('1000007', '1000008', '1000009', '0', 
    '1000000', '1000002', '1000003', '1000004', '1000005', '1000006') 
AND ol.client.id  IN ('1000000', '0')
AND ol.active='Y'
ORDER BY ol.salesOrder.businessPartner.id, ol.id
```

Tenga en cuenta lo siguiente:

- La consulta es mucho más sencilla que el SQL original.
- La DAL ha añadido automáticamente filtrado adicional de organización/cliente.

En este punto, la consulta está lista para ejecutarse. Se utiliza un bucle `for`. Dentro del bucle `for` se recuperan distintos datos desde `OrderLine`. Los datos recuperados se corresponden con la información solicitada en la cláusula `select` del SQL. Se utilizará una consulta separada para recuperar la suma de los PO emparejados (véase más abajo).

``` java
for (OrderLine ol : qry.list()) {
 
    // C_ORDERLINE.C_ORDERLINE_ID AS ID, C_ORDER.C_ORDER_ID AS C_ORDER_ID
    System.err.println(ol.getId());
    System.err.println(ol.getSalesOrder().getId());
 
    // C_ORDER.DOCUMENTNO AS DOCUMENTNO, C_ORDER.DATEORDERED AS DATEORDERED,
    System.err.println(ol.getSalesOrder().getDocumentNo());
    System.err.println(ol.getSalesOrder().getOrderDate());
 
    // C_BPARTNER.C_BPARTNER_ID AS C_BPARTNER_ID, C_BPARTNER.NAME AS PARTNER_NAME,
    System.err.println(ol.getSalesOrder().getBusinessPartner().getId());
    System.err.println(ol.getSalesOrder().getBusinessPartner().getName());
 
    // AD_COLUMN_IDENTIFIER(TO_CHAR('M_Product'), TO_CHAR(C_ORDERLINE.M_PRODUCT_ID),
    // TO_CHAR(?)) AS PRODUCT_NAME,
    System.err.println(ol.getProduct().getIdentifier());
    System.err.println(ol.getProduct().getId());
    System.err.println(ol.getProduct().getName());
 
    // M_ATTRIBUTESETINSTANCE.DESCRIPTION AS DESCRIPTION,
    if (ol.getAttributeSetValue() != null) {
    System.err.println(ol.getAttributeSetValue().getDescription());
    }
 
    // C_ORDERLINE.QTYORDERED AS TOTAL_QTY,
    System.err.println(ol.getOrderedQuantity());
```

Para obtener la suma de los PO emparejados, es necesario usar una segunda consulta. Esto se hace dentro del bucle `for`. Es evidente que esto es menos óptimo que la sentencia SQL directa; a continuación se analiza un enfoque diferente.

!!!Note 
    El objeto `ol` se pasa como parámetro. Usamos un parámetro con nombre (`orderLine`) para establecerlo.

``` java
// C_ORDERLINE.QTYORDERED-SUM(COALESCE(M_MATCHPO.QTY,0)) AS QTYORDERED, '-1' AS ISACTIVE
// todo this we have to repeat the sum query, we use direct hql for this
final String hql = "select sum(quantity) from ProcurementPOInvoiceMatch "
    + "where goodsShipmentLine is not null and salesOrderLine=:orderLine";
final Session session = OBDal.getInstance().getSession();
final Query query = session.createQuery(hql);
query.setParameter("orderLine", ol);
final BigDecimal sum = (BigDecimal) query.uniqueResult();
System.err.println(sum);
}
```

### El resultado

El código anterior produce la siguiente salida:

``` txt
1000045
1000032
800007
2006-04-12 00:00:00.0
1000017
Neil Riley Productions (invoice monthly)
Block of Wood
1000022
Block of Wood
30
60
```

### El SQL ejecutado, el problema de selección N+1

Ahora, veamos el SQL real que se ejecuta. Esto también mostrará que la implementación anterior podría sufrir el problema de selección N+1.

La consulta SQL se ejecuta cuando se llama al método `list()` en el objeto de consulta (el inicio del bucle `for`). Esto da como resultado la siguiente consulta:

``` sql
SELECT orderline0_.C_OrderLine_ID AS C1_462_, orderline0_.AD_Client_ID AS AD2_462_, orderline0_.AD_Org_ID AS AD3_462_, 
    orderline0_.IsActive AS IsActive462_, orderline0_.Created AS Created462_, orderline0_.CreatedBy AS CreatedBy462_, 
    orderline0_.Updated AS Updated462_, orderline0_.UpdatedBy AS UpdatedBy462_, orderline0_.C_Order_ID AS C9_462_, 
    orderline0_.Line AS Line462_, orderline0_.C_BPartner_ID AS C11_462_, orderline0_.C_BPartner_Location_ID AS C12_462_, 
    orderline0_.DateOrdered AS DateOrd13_462_, orderline0_.DatePromised AS DatePro14_462_, 
    orderline0_.DateDelivered AS DateDel15_462_, orderline0_.DateInvoiced AS DateInv16_462_, orderline0_.Description AS Descrip17_462_, 
    orderline0_.M_Product_ID AS M18_462_, orderline0_.M_Warehouse_ID AS M19_462_, orderline0_.DirectShip AS DirectShip462_, 
    orderline0_.C_UOM_ID AS C21_462_, orderline0_.QtyOrdered AS QtyOrdered462_, orderline0_.QtyReserved AS QtyRese23_462_, 
    orderline0_.QtyDelivered AS QtyDeli24_462_, orderline0_.QtyInvoiced AS QtyInvo25_462_, orderline0_.M_Shipper_ID AS M26_462_, 
    orderline0_.C_Currency_ID AS C27_462_, orderline0_.PriceList AS PriceList462_, 
    orderline0_.PriceActual AS PriceAc29_462_, orderline0_.PriceLimit AS PriceLimit462_, 
    orderline0_.LineNetAmt AS LineNetAmt462_, orderline0_.Discount AS Discount462_, orderline0_.FreightAmt AS FreightAmt462_, 
    orderline0_.C_Charge_ID AS C34_462_, orderline0_.ChargeAmt AS ChargeAmt462_, orderline0_.C_Tax_ID AS C36_462_, 
    orderline0_.S_ResourceAssignment_ID AS S37_462_, orderline0_.Ref_OrderLine_ID AS Ref38_462_, orderline0_.M_AttributeSetInstance_ID AS M39_462_, 
    orderline0_.IsDescription AS IsDescr40_462_, orderline0_.QuantityOrder AS Quantit41_462_, orderline0_.M_Product_Uom_Id AS M42_462_, 
    orderline0_.M_Offer_ID AS M43_462_, orderline0_.PriceStd AS PriceStd462_ 
FROM C_OrderLine orderline0_, C_Order order2_ 
WHERE orderline0_.C_Order_ID=order2_.C_Order_ID 
    AND orderline0_.QtyOrdered<>(SELECT sum(procuremen1_.Qty) FROM M_MatchPO procuremen1_ WHERE (procuremen1_.M_InOutLine_ID IS NOT NULL) 
        AND procuremen1_.C_OrderLine_ID=orderline0_.C_OrderLine_ID) 
    AND order2_.IsSOTrx='N' AND order2_.C_BPartner_ID=? AND order2_.DocStatus='CO' 
    AND (orderline0_.AD_Org_ID IN ('1000007' , '1000008' , '1000009' , '0' , '1000000' , '1000002' , 
        '1000003' , '1000004' , '1000005' , '1000006')) 
    AND (orderline0_.AD_Client_ID IN ('1000000' , '0'))
    AND orderline0_.IsActive='Y'
ORDER BY order2_.C_BPartner_ID, orderline0_.C_OrderLine_ID
```

Al comparar este SQL con el SQL original, la principal diferencia es que se selecciona mucha más información. Esto se debe a que, en este enfoque, elegimos seleccionar el objeto completo de línea de pedido. Esto hace que la consulta HQL sea mucho más sencilla, pero también menos eficiente. También es posible seleccionar los campos individuales de la línea de pedido; en ese caso debe utilizarse una consulta directa de Hibernate.

Ahora, comprobemos qué ocurre cuando se solicita información desde el objeto de línea de pedido. El objeto de línea de pedido referencia otros objetos que se cargan de forma diferida (bajo demanda). Por tanto, lo que verá es que Hibernate lanza consultas adicionales (este es el problema de selección N+1).

Cuando en el bucle `for` se ejecuta la siguiente sentencia:

``` java
System.err.println(ol.getSalesOrder().getBusinessPartner().getId());
```

entonces Hibernate lanzará las dos consultas siguientes (cláusula `select` abreviada para mayor claridad):

``` sql
SELECT businesspa0_.C_BPartner_ID AS C1_98_0_, businesspa0_.AD_Client_ID AS AD2_98_0_, 
.... (ALL business partner COLUMNS are retrieved)
FROM C_BPartner businesspa0_ WHERE businesspa0_.C_BPartner_ID=?
 
SELECT adlanguage0_.AD_Language_ID AS AD1_247_0_, adlanguage0_.AD_Language AS AD2_247_0_, 
.... (ALL COLUMNS of adlanguage are being retrieved)
FROM AD_Language adlanguage0_ WHERE adlanguage0_.AD_Language=?
```

En la siguiente sentencia Java:

``` java
System.err.println(ol.getProduct().getIdentifier());
```

Hibernate lanzará este SQL:

``` sql
SELECT product0_.M_Product_ID AS M1_31_0_, product0_.AD_Client_ID AS AD2_31_0_, product0_.AD_Org_ID AS AD3_31_0_,
.... (ALL COLUMNS of M_Product are retrieved)
FROM M_Product product0_ WHERE product0_.M_Product_ID=?
```

Esto significa que, para cada línea de pedido, Hibernate lanzará múltiples consultas adicionales. Por eso se denomina el problema de selección N+1: se utiliza una consulta para obtener los resultados globales y, después, para cada resultado se realizan una o más consultas (N consultas si el primer conjunto de resultados tiene N resultados).

Hibernate ofrece diferentes formas de resolver este problema:

1. Usar una caché de segundo nivel: si Hibernate puede encontrar el objeto referenciado en la caché de segundo nivel, entonces no se lanza ninguna consulta. Usar una caché de segundo nivel es una mejora importante de rendimiento porque, en la práctica, la información no cambia muy a menudo; la mayoría (a menudo alrededor del 95%) de los accesos son de lectura.

2. Usar `left join fetch` en la consulta original: en este enfoque, la información referenciada se recupera junto con la consulta principal. Esto se analiza a continuación.

Para habilitar `left join fetch` para el producto y el tercero, debe añadirse lo siguiente a la cláusula `where`:

``` java
whereClause.append(" left join fetch ol.product ");
whereClause.append(" left join fetch ol.salesOrder ");
whereClause.append(" left join fetch ol.businessPartner ");
whereClause.append(" left join fetch ol.businessPartner.language ");
```

Esto debe añadirse justo después de la parte `as ol`.

Ahora, al ejecutar la consulta y el bucle `for`, se ejecutan consultas adicionales. La consulta original de línea de pedido ahora tendrá una cláusula `from` con la información adicional unida:

``` sql
FROM C_OrderLine orderline0_ LEFT OUTER JOIN M_Product product1_ ON orderline0_.M_Product_ID=product1_.M_Product_ID 
    LEFT OUTER JOIN C_Order order2_ ON orderline0_.C_Order_ID=order2_.C_Order_ID 
    LEFT OUTER JOIN C_BPartner businesspa3_ ON orderline0_.C_BPartner_ID=businesspa3_.C_BPartner_ID 
    LEFT OUTER JOIN AD_Language adlanguage5_ ON businesspa3_.AD_Language=adlanguage5_.AD_Language
```

Así, esto resuelve el problema de selección N+1.

!!! Note
    Como se ha mencionado anteriormente, también tiene sentido usar la caché de segundo nivel de Hibernate, ya que esto aporta otros beneficios de rendimiento (los datos se recuperan desde memoria, lo cual es mucho más rápido que consultar, en general).
## Cómo puede ver qué sentencias SQL se ejecutan

Tenga en cuenta que, para ver las consultas SQL lanzadas por Hibernate, debe configurarse la siguiente propiedad de log4j:
    
```
### log just the SQL
log4j.logger.org.hibernate.SQL=debug
```

Si no le funciona, es posible que el archivo `log4j.properties` se esté leyendo desde otra ubicación distinta a la que usted espera. Para ver desde dónde lee log4j sus propiedades, configure este parámetro de la JVM:
 
```
-Dlog4j.debug
```

### Conclusión

Con esto finaliza la descripción de esta consulta compleja en HQL. Algunas conclusiones importantes que pueden extraerse:

- Al realizar consultas más complejas usando **Hibernate**, es fundamental analizar el SQL generado por Hibernate. 
- Al realizar joins con propiedades que pueden ser nulas, utilice siempre sentencias `left join` en el HQL. 
- Con Hibernate puede tener sentido trasladar parte del procesamiento y la lógica a Java. Aunque existen inconvenientes de rendimiento, el código y las consultas resultantes son mucho más simples. Esto se traduce en menos errores y en un desarrollo más productivo, lo que a su vez deja tiempo para mejoras de rendimiento en otras áreas. 
- Considere utilizar `left join fetch` para controlar la cantidad de consultas adicionales realizadas por Hibernate.
## Un enfoque alternativo de HQL

El enfoque anterior se centró en consultar el objeto `OrderLine` completo.

La principal ventaja de este enfoque es que el código Java que procesa los resultados es mucho más significativo y fácil de entender. Sin embargo, este enfoque tiene dos inconvenientes de rendimiento:

- las consultas tienen cláusulas `select` muy grandes; se devuelven todas las columnas, aunque quizá solo se utilice un subconjunto
- esto implica que la consulta de la suma de los `PO` coincidentes debe repetirse; el motivo es que no es práctico listar todas las propiedades de `OrderLine` y sus entidades relacionadas en la cláusula `group by`

El enfoque anterior vuelve a consultar la suma de los `PO` coincidentes dentro del bucle `for`. Esto es menos óptimo que consultar directamente en la base de datos. Un enfoque diferente consiste en reescribir el HQL anterior para devolver la suma directamente en la sentencia `select` y utilizar una cláusula `group by` en el HQL. Esto es ciertamente posible en HQL, con las siguientes consideraciones:

- En lugar de usar `OBQuery`, debe utilizarse el objeto de consulta de Hibernate; este objeto puede recuperarse desde el objeto de sesión (como se ilustra arriba).
- Al usar el objeto de consulta de Hibernate, el filtrado por organización y cliente no se aplica automáticamente. Por tanto, estos filtros deben añadirse manualmente a la consulta de Hibernate.

Teniendo esto en cuenta, el siguiente HQL consultará prácticamente la misma información que la listada anteriormente:

``` sql
SELECT ol.id, ol.salesOrder.id, ol.salesOrder.documentNo, ol.salesOrder.orderDate,  ol.salesOrder.businessPartner.id, 
    ol.salesOrder.businessPartner.name, ol.product.name,  ol.orderedQuantity, sum(matchPO.quantity) AS totalQty 
FROM OrderLine ol, ProcurementPOInvoiceMatch matchPO  
WHERE ol.orderedQuantity <>  (SELECT sum(quantity) FROM ProcurementPOInvoiceMatch WHERE goodsShipmentLine IS NOT NULL AND salesOrderLine=ol) 
    AND ol = matchPO.salesOrderLine  
    AND ol.salesOrder.salesTransaction=false  
    AND ol.salesOrder.businessPartner.id=:bpId  
    AND ol.salesOrder.documentStatus='CO'  
    AND ol.organization IN ('1000007', '1000008', '1000009', '0', '1000000', '1000002', '1000003', '1000004', '1000005', '1000006') 
    AND ol.client  IN ('1000000', '0') 
    AND ol.active=true 
GROUP BY ol.id, ol.salesOrder.id, ol.salesOrder.documentNo, ol.salesOrder.orderDate,  ol.salesOrder.businessPartner.id,
    ol.salesOrder.businessPartner.name, ol.product.name,  ol.orderedQuantity 
ORDER BY ol.salesOrder.businessPartner.id, ol.id
```

!!! note
    La clase `OBDal` ofrece dos métodos de conveniencia para crear las cláusulas de filtro de cliente y organización en el HQL:
    
    ``` java
    OBDal.getInstance().getReadableOrganizationsInClause();
    OBDal.getInstance().getReadableClientsInClause();
    ```
  
Para usar HQL directamente, puede obtener el objeto `Session` de Hibernate desde la instancia de `OBDal` y llamar a `createQuery` (la variable `hql` contiene el HQL anterior). El resultado de la consulta anterior es, en realidad, un array de objetos:

``` java
final Query query = OBDal.getInstance().getSession().createQuery(hql);
query.setParameter("bpId", "1000017");
 
for (Object o : query.list()) {
    final Object[] os = (Object[]) o;
    for (Object result : os) {
    System.err.println(result);
    }
}
```

El SQL ejecutado por el HQL anterior también es más simple que antes:

``` sql
SELECT orderline0_.C_OrderLine_ID AS col_0_0_, orderline0_.C_Order_ID AS col_1_0_, order2_.DocumentNo AS col_2_0_, 
    order2_.DateOrdered AS col_3_0_, order2_.C_BPartner_ID AS col_4_0_, businesspa6_.Name AS col_5_0_, product7_.Name AS col_6_0_, 
    orderline0_.QtyOrdered AS col_7_0_, sum(procuremen1_.Qty) AS col_8_0_ 
FROM C_OrderLine orderline0_, C_Order order2_, C_BPartner businesspa6_, M_Product product7_, M_MatchPO procuremen1_ 
WHERE orderline0_.C_Order_ID=order2_.C_Order_ID 
AND order2_.C_BPartner_ID=businesspa6_.C_BPartner_ID 
AND orderline0_.M_Product_ID=product7_.M_Product_ID 
AND orderline0_.QtyOrdered<>(SELECT sum(procuremen8_.Qty) FROM M_MatchPO procuremen8_ WHERE (procuremen8_.M_InOutLine_ID IS NOT NULL) 
        AND procuremen8_.C_OrderLine_ID=orderline0_.C_OrderLine_ID) 
AND orderline0_.C_OrderLine_ID=procuremen1_.C_OrderLine_ID 
AND order2_.IsSOTrx='N' AND order2_.C_BPartner_ID=? 
AND order2_.DocStatus='CO' 
AND (orderline0_.AD_Org_ID IN ('1000007' , '1000008' , '1000009' , '0' , '1000000' , '1000002' , '1000003' , '1000004' , '1000005' , '1000006')) 
AND (orderline0_.AD_Client_ID IN ('1000000' , '0')) 
AND orderline0_.IsActive='Y' 
GROUP BY orderline0_.C_OrderLine_ID , orderline0_.C_Order_ID , order2_.DocumentNo , order2_.DateOrdered , 
    order2_.C_BPartner_ID , businesspa6_.Name , product7_.Name , orderline0_.QtyOrdered 
ORDER BY order2_.C_BPartner_ID, orderline0_.C_OrderLine_ID
```

Hay algunas cosas a tener en cuenta sobre este SQL *más simple*:

- como HQL no permite que un alias de `select` se utilice en la cláusula `where`, la suma de las cantidades de `PO` coincidentes se repite en la cláusula `where`
- el SQL original también se encargaba de obtener el identificador de un producto y el valor del conjunto de atributos. Esto no es posible al hacer HQL con este enfoque. Cuando los valores de identificador son importantes, entonces el anterior enfoque de *consultar el objeto `OrderLine` completo* puede tener más sentido.

---
Este trabajo es una obra derivada de [Cómo hacer una consulta compleja usando el DAL-1](http://wiki.openbravo.com/wiki/How_to_do_a_complex_query_using_the_DAL-1){target="\_blank"} y [Cómo hacer una consulta compleja usando el DAL-2](http://wiki.openbravo.com/wiki/How_to_do_a_complex_query_using_the_DAL-2){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.