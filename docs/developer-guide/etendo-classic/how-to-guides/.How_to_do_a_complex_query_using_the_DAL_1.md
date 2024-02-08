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

  

#  How to do a complex query using the DAL-1

##  Contents

  * 1  Objective 
  * 2  Setup a test case 
  * 3  Requisition SQL query 
  * 4  Translating to HQL 
  * 5  Executing the HQL query and retrieving results 
  * 6  The Result 
  * 7  How you can see what SQL statements are executed 
  * 8  The executed SQL, the N+1 Select problem 
  * 9  Conclusion 

  
---  
  
##  Objective

This how-to illustrates how a complex query can be programmed using Data
Access Layer constructs. The solution will be using  Hibernate HQL  so before
reading this how-to make sure you know the basics of HQL.

This how-to is the first page of a 2-page series on more complex queries using
the DAL. The 2 pages each describe a different query and pages can be read
separately.

The how-to starts with an SQL query from the requisition-to-order form inside
Procurement Management and translates it to a HQL representation. Different
aspects of using HQL and the DAL are discussed including performance and
debugging aspects.

##  Setup a test case

There is a separate how-to on creating test cases using the Data Access Layer
(see  here  ). In this how-to we will only give a summary.

The test case which we will be using is created inside of the modules
directory of the Openbravo ERP development project. We won't actually create a
new module in the database but it is best to place custom code separate from
the main Openbravo ERP source tree. To create a new source folder in Eclipse,
right-click on the project and select _New_ and then source folder.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_do_a_complex_query_using_the_DAL_1-0.png){: .legacy-image-style}

  
In the source folder create a new package (right click on the new folder and
select New > package): org.openbravo.howto.query. Inside of this package
create a java file QueryTest.java. This file has the following content:

    
    
     
     package org.openbravo.howto.query;
     
     import org.openbravo.test.base.OBBaseTest;
     
     /**
      * Complex queries howto.
      */
     
     public class QueryTest extends OBBaseTest {
     
       public void testQueryOne() {
         // this sets the user to the Openbravo Admin
         setUserContext("100");
     
         // here we will be doing our stuff...
     
         commitTransaction();
       }
    }

This test case inherits from the OBBaseTest class provided by Openbravo ERP.
The base test class provides a user context and transaction handling. There is
one test method in the class: testQueryOne. This method first selects the user
context. The commitTransaction() at the end commits the transaction If an
exception occurs during the test then this statement won't be executed and the
transaction is automatically rolled back.

You can right-click the Java file in Eclipse and then run as > junit testcase,
you should see the green bar in the junit view:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_do_a_complex_query_using_the_DAL_1-1.png){: .legacy-image-style}

  
This is the main testcase setup. The next section will add some code to the
testcases to query the DAL and show some results.

##  Requisition SQL query

The following SQL query will be translated to HQL:

    
    
     
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
       AND AND M_REQUISITIONLINE.NEEDBYDATE < ?
       AND M_REQUISITIONLINE.M_PRODUCT_ID = ?
       AND M_REQUISITION.AD_USER_ID = TO_CHAR(?)
       AND ((M_REQUISITIONLINE.C_BPARTNER_ID = ? OR M_REQUISITION.C_BPARTNER_ID = ?) OR 
         (M_REQUISITIONLINE.C_BPARTNER_ID IS NULL AND M_REQUISITION.C_BPARTNER_ID IS NULL))
     ORDER BY M_REQUISITIONLINE.NEEDBYDATE, M_REQUISITIONLINE.M_PRODUCT_ID, M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID

This query is used in the Requisition-to-order form inside Procurement
Management. It returns the  requisition line  info with the identifiers of its
business partner, product, pricelist etc.

The  Hibernate Query Language  supports querying for a complete business
object. The columns specified in the select clause above are all related to
the  Requisition Line  . So in HQL the query will be used to filter the main
object: the Requisition Line, and then retrieve the required information from
the Requisition Line object. A second step describes how to make the query
more efficient to prevent the  N + 1 select problem  .

Note that in HQL we use the concept of an Entity and Properties. See  here
for an overview of the Requisition Line Entity.

##  Translating to HQL

This section show how to translate the above SQL query to a HQL query using
the Data Access Layer.

The query and its results have been tested against the Small Bazaar test data.
It uses the Openbravo Admin user, this user has been set to the F&B Admin role
as displayed below (note: the default field has been checked). To show
results, new requisitions have been entered in Openbravo for the product and
business partner used in this how-to.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_do_a_complex_query_using_the_DAL_1-2.png){: .legacy-image-style}

  
Begin by setting the user context to the Standard Openbravo Admin user. The
query will be build using a StringBuilder. The where-clause starts with 'as
rl', this is because we know that we will query for the RequisitionLine and
use the alias 'rl' in the rest of the where-clause. The  DAL  will add the
select clause automatically later.

    
    
     
        setUserContext("100");
     
        // create the where clause stringbuilder
        final StringBuilder whereClause = new StringBuilder();
        // rl is used as the alias for the RequisitionLine
        whereClause.append(" as rl");
     
        // Initialize the parameter map, will be used to
        // add parameters to the query
        final Map<String, Object> parameters = new HashMap<>(6);

Next, left outer join on the business partner property of the requisition line
and requisition:

    
    
     
        // do a left outer join on business partner as it can be null
        // in both the requisition line and the requisition
        whereClause.append(" left outer join rl.businessPartner ");
        whereClause.append(" left outer join rl.requisition.businessPartner ");

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
**NOTE:** The HQL uses property and entity names of Openbravo business
objects. See the  Entity Model reference manual  for a complete listing of all
entities. The Requisition Line entity is described  here  . You can also find
the correct names by checking out the generated code in the src-gen folder.
You can search this folder using the table names to find the correct entity.  
---|---  
  
The left outer join is required because in the where-clause there will be
expressions which use properties of the business partner. If no explicit left-
outer-join is specified then Hibernate will use an inner-join. With an inner-
join, if the business partner is null for a requisition line then no results
are returned.

The next clause uses the joined business partner.

    
    
     
        // AND COALESCE(M_REQUISITIONLINE.C_BPARTNER_ID,M_REQUISITION.C_BPARTNER_ID) = C_BPARTNER.C_BPARTNER_ID
        // AND C_BPARTNER.PO_PAYMENTTERM_ID IS NOT NULL
        whereClause.append(" where (rl.businessPartner.pOPaymentTerms != null or rl.requisition.businessPartner.pOPaymentTerms != null)");

The following lines add more where clauses, note that the Data Access Layer
will automatically add a filter on active:

    
    
     
        // AND M_REQUISITION.ISACTIVE = 'Y'
        whereClause.append(" and rl.requisition.active=true");
     
        // AND M_REQUISITIONLINE.ISACTIVE = 'Y' <-- is done by the DAL Layer
     
        // AND M_REQUISITION.DOCSTATUS = 'CO'
        whereClause.append(" and rl.requisition.documentStatus='CO'");
     
        // AND M_REQUISITIONLINE.REQSTATUS = 'O'
        whereClause.append(" and rl.requisitionLineStatus='O'");

Next add the lockedBy and lockDate filter. The coalesce is translated into an
or, the date is added as a parameter using a java Date object. Note that HQL
supports coalesce (although we won't use it here).

    
    
     
        // AND (M_REQUISITIONLINE.LOCKEDBY IS NULL OR
        // COALESCE (M_REQUISITIONLINE.LOCKDATE, TO_DATE('01-01-1900', 'DD-MM-YYYY')) < (now()-3))
        whereClause.append(" and (rl.lockedBy = null or rl.lockDate<:lockDate or rl.lockDate = null)");   
        final long threeDays = 1000 * 3600 * 24 * 3;
        parameters.put("lockDate", new Date(System.currentTimeMillis() - threeDays));

The Data Access Layer adds the organization/client filtering automatically,
the neededDate filter is done by adding two parameters:

    
    
     
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

The product and user contact filter are added like this. Note that the actual
values depend on the database used:

    
    
     
        // AND M_REQUISITIONLINE.M_PRODUCT_ID = ?
        whereClause.append(" and rl.product.id=:productId");
        parameters.put("productId", "1000010");
     
        // AND M_REQUISITION.AD_USER_ID = TO_CHAR(?)
        whereClause.append(" and rl.requisition.userContact.id=:userId");
        parameters.put("userId", "100");

The filter on business partner is added like below. Note that also the
requisitions business partner can be null:

    
    
     
        // AND ((M_REQUISITIONLINE.C_BPARTNER_ID = ? OR M_REQUISITION.C_BPARTNER_ID = ?) OR
        // (M_REQUISITIONLINE.C_BPARTNER_ID IS NULL AND M_REQUISITION.C_BPARTNER_ID IS NULL))
        // ORDER BY M_REQUISITIONLINE.NEEDBYDATE, M_REQUISITIONLINE.M_PRODUCT_ID,
        // M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID
        whereClause
            .append(" and ((rl.businessPartner.id = :bpId or rl.requisition.businessPartner.id = :bpId) or "
                + "(rl.businessPartner = null and rl.requisition.businessPartner = null))");
        parameters.put("bpId", "1000011");

In this code the business partner id is 1000011, this can be different for
different databases.

In the last part of building the query the order by is added, the query is
created and the parameters are set:

    
    
     
        // ORDER BY M_REQUISITIONLINE.NEEDBYDATE, M_REQUISITIONLINE.M_PRODUCT_ID,
        // M_REQUISITIONLINE.M_ATTRIBUTESETINSTANCE_ID
        whereClause.append(" order by rl.needByDate, rl.product.id, rl.attributeSetValue.id");
     
        final OBQuery<RequisitionLine> obQuery = OBDal.getInstance().createQuery(RequisitionLine.class,
            whereClause.toString());
     
        obQuery.setNamedParameters(parameters);

The total HQL is:

    
    
     
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

##  Executing the HQL query and retrieving results

The HQL is executed when the list method is called on the query object. This
is done in a for-loop to process all the results. As you can see the list()
method returns a type-casted list of RequisitionLine objects. This makes
developing against a query result very easy and also type safe.

    
    
     
        // now print the select clause parts
        for (RequisitionLine requisitionLine : obQuery.list()) {
     

Within the for-loop the information from the RequisitionLine is fetched and
printed.

    
    
     
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

The identifier of an object is retrieved by calling the getIdentifier()
method, this is different from before, which required calling a database
function:

    
    
     
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

##  The Result

The above code results in the following output:

    
    
     
    2FA597B938EF4007A6AE5E85068BD98B
    2009-04-01 00:00:00.0
    0.94
    Bell Phone Company
    Purchase
    Screwdriver
    Openbravo
    10000000 Screwdriver 10 2009-04-01 00:00:00.0

##  How you can see what SQL statements are executed

In the next section we will analyze the SQL generated by Hibernate. To see the
SQL queries fired by Hibernate, the following log4j property has to be set:

    
    
     
    ### log just the SQL
    log4j.logger.org.hibernate.SQL=debug

If it does not work for you, it is possible that the log4j.properties file is
read from another location than you expect. To see where log4j reads its
properties from set this jvm parameter:

    
    
     
    -Dlog4j.debug

##  The executed SQL, the N+1 Select problem

Now let's look at the actual sql which is executed. This will also show that
the above implementation might suffer from the N+1 select problem.

The SQL query is executed when the for list() method is called on the query
object (the start of the for-loop). Hibernate generates the following SQL
query:

    
    
     
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

When comparing this SQL with the original SQL the main difference is that much
more information is selected. This is because in this approach we choose to
select the complete RequisitionLine object. This makes the HQL query much
simpler but also less efficient. It is also possible to select the individual
RequisitionLine fields, in this case a direct Hibernate query has to be used.

Now let's check what happens when information is requested from the
RequesitionLine object. The OrderLine object references other objects which
are lazily loaded (up-on-request). So the thing you will see is that
additional queries are fired by Hibernate (this is the N+1 select problem!).

when in the for-loop the following statement is executed:

    
    
     
          } else if (requisitionLine.getRequisition().getBusinessPartner() != null) {

Then Hibernate fires this sql statement:

    
    
     
    SELECT procuremen0_.M_Requisition_ID AS M1_263_0_, procuremen0_.AD_Client_ID AS AD2_263_0_, 
    .... (list of COLUMNS abbreviated FOR clarity)
    FROM M_Requisition procuremen0_ WHERE procuremen0_.M_Requisition_ID=?

Hibernate does this because the Requisition object (in the Requisition Line)
is initially lazy loaded, this means that the Requisition instance has been
created but its data has not yet been retrieved from the database. The above
Java code accesses the requisition (retrieving the business partner) and
therefore initiates a load of the Requisition object.

The same situation occurs when accessing the business partner, product and
price list in the following Java statements:

    
    
     
    System.err.println(requisitionLine.getRequisition().getBusinessPartner().getIdentifier());
    ....
    System.err.println(requisitionLine.getPriceList().getIdentifier());
    .....
    System.err.println(requisitionLine.getRequisition().getPriceList().getIdentifier());
    .....
    System.err.println(requisitionLine.getProduct().getIdentifier());

Resulting in four additional queries to retrieve the required information. So
for each RequisitionLine potentially 5 additional queries are done. This can
result in lesser performance.

Hibernate offers a way to solve this issue:

  1. Use left join fetching in the original query: in this approach the referred-to information is retrieved together with the main query. This is discussed next. 

To enable left join fetching for the related objects the following has to be
added to the where clause (replacing the left outer join used above):

    
    
     
    whereClause.append(" left join fetch rl.product");
    whereClause.append(" left join fetch rl.businessPartner");
    whereClause.append(" left join fetch rl.businessPartner.language");
    whereClause.append(" left join fetch rl.requisition");
    whereClause.append(" left join fetch rl.priceList");
    whereClause.append(" left join fetch rl.requisition.businessPartner");
    whereClause.append(" left join fetch rl.requisition.businessPartner.language");

This solves the N+1 problem for this case. However, it is clear that this adds
many joins to the query.

##  Conclusion

This concludes the description of this complexer query in HQL. Some important
conclusions which can be drawn:

  * When performing more complex querying using Hibernate it is critical to analyze the SQL generated by Hibernate. 
  * When joining with nullable properties always use left join statements in the HQL. 
  * With Hibernate it can make sense to actually move part of the processing and logic to Java. Although there are performance drawbacks, the resulting code and queries are much simpler. This results in less errors, and a more productive development. Which again leaves time for performance improvements in other areas. 
  * Consider to use 'left join fetching' to control the amount of additional queries done by Hibernate. 

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_do_a_complex_query_using_the_DAL-1  "

This page has been accessed 14,278 times. This page was last modified on 17
July 2018, at 08:48. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

