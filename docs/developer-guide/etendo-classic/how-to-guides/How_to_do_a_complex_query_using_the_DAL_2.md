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

  

#  How to do a complex query using the DAL-2

##  Contents

  * 1  Objective 
  * 2  Setup a test case 
  * 3  Order line SQL query 
  * 4  Translating to HQL 
  * 5  The result 
  * 6  The executed SQL, the N+1 select problem 
  * 7  How you can see what SQL statements are executed 
  * 8  An alternative HQL approach 
  * 9  Conclusion 

  
---  
  
##  Objective

This how-to illustrates how a complex query can be programmed using  Data
Access Layer  constructs. The solution will be using  Hibernate HQL  , so
before reading this how-to make sure that you know the basics of HQL.

This how-to is the second page in a 2-page series on complex queries and the
DAL. Each of the 2 pages discuss a different query, the 2 pages can be read
separately.

In this how-to we will show how to develop a complex query using the Hibernate
query API and Hibernate HQL. The how-to starts with an SQL query from pending
goods receipt and translates it to a HQL representation. Different aspects of
using HQL and the  DAL  are discussed, including performance and debugging
aspects.

##  Setup a test case

There is a separate how-to on creating test cases using the Data Access Layer
(see  here  ). In this how-to we will just give a summary.

The test case which we will be using is created inside of the modules
directory of the Openbravo ERP development project. We won't actually create a
new module in the database but it is best to place custom code separated from
the main Openbravo ERP source tree. To create a new source folder in Eclipse
right-click on the project and select _New_ and then source folder.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_do_a_complex_query_using_the_DAL_2-0.png){: .legacy-image-style}

  
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

This test case inherits from the  OBBaseTest  class provided by Openbravo ERP.
The base test class provides a user context and transaction handling. There is
one test method in the class: testQueryOne. This method first selects the user
context. The commitTransaction() at the end commits the transaction, if an
exception occurs during the test then this statement won't be executed and the
transaction is automatically rolled back.

You can right-click the Java file in Eclipse and then run as > junit testcase,
you should see the green bar in the junit view:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_do_a_complex_query_using_the_DAL_2-1.png){: .legacy-image-style}

  
This was the main test case setup. The next section will add some code to the
test cases to query the DAL and show some results.

##  Order line SQL query

The following SQL query will be translated to a DAL representation:

    
    
     
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

This query is from the goods receipt pending manual.

When translating this query to a  Hibernate Query Language  query the
following aspects have to be taken into account:

  * Hibernate does not support the usage of select aliases inside the where clause. 
  * Hibernate does not support the use of a select, which selects results from another select. 
  * With HQL we can query for complete business objects and navigate the object graph after the query to retrieve additional results. 

With this in mind we will use a slightly different query approach in HQL. Most
information in the select part is related to the Order Line. So in HQL the
query will be used to filter the main object: the OrderLine, and then retrieve
the required information from the Order Line. In a second step we discuss how
to make the query more efficient to prevent the well-known  N + 1 select
problem  .

Let's look at what the above query does:

  * It queries for the sum of the quantity on the matched PO's for a certain order line and filters order lines which have an order quantity unequal to this sum. 
  * The order line is further filtered using some other parameters (business partner, document status, etc.) 
  * Then the results are displayed in a certain order, the ordering of the inner select is not important, as the outer select re-orders also. 

The next step is to translate this approach to HQL. We will ignore the select
part initially because this information is retrieved from the Order Lines
business objects returned from the HQL.

##  Translating to HQL

In this section the above SQL is translated to HQL. For HQL we will be using
the Entity/Property concept versus the Table/Column concept for SQL. See  here
for a complete listing of Openbravo entities and their relations to the table
and Java code.

The query and its results have been tested against the _Small Bazaar_ test
data. It uses the Openbravo Admin user, this user has been set to the
Openbravo Admin role as displayed below (note: check the default box).

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_do_a_complex_query_using_the_DAL_2-2.png){: .legacy-image-style}

  
First, set the user context to the Standard Openbravo Admin user. The query
will be build using a StringBuilder. The where-clause starts with 'as ol',
this is because we know that we will query for the  OrderLine  entity and use
the alias 'ol' in the rest of the where-clause.

    
    
     
        setUserContext("100");
     
        // create the where clause
        final StringBuilder whereClause = new StringBuilder();
        // set the alias, the OrderLine will be added by the DAL
        whereClause.append(" as ol ");

Next add the filtering on the sum of the quantities of matched PO's. Note the
use of the alias in the _where clause_ of the subselect.

    
    
     
        // the subselect to filter on the matched invoices, only orders with a
        // different order quantity are returned.
        whereClause.append(" where ol.orderedQuantity <> ");
        whereClause.append(" (select sum(quantity) from ProcurementPOInvoiceMatch ").append(" where goodsShipmentLine is not null and salesOrderLine=ol)");

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
**NOTE:** the HQL uses property and entity names of Openbravo business
objects. See the  Entity Model reference manual  for a complete listing of all
entities. The Order Line entity is described  here  . You can also find the
correct names by checking out the generated code in the src-gen folder. You
can search this folder using the table names to find the correct entity.  
---|---  
  
  
Add other filter options, the organisation and client filtering are done by
the Data Access Layer so do not need to be taken into account explicitly. The
Sales Transaction column in the database holds 'Y' or 'N', but because in Java
we use booleans we can use true or false in the where-clause (here it's
false).

    
    
     
        // Other filtering options:
        // AND C_ORDER.AD_CLIENT_ID IN ('1') <-- these are done automatically by the dal
        // AND C_ORDER.AD_ORG_ID IN ('1') <-- these are done automatically by the dal
     
        // AND C_ORDER.ISSOTRX='N'
        whereClause.append(" and ol.salesOrder.salesTransaction=false ");

Add the filtering on business partner and document status. The business
partner parameter is added below.

    
    
     
        // AND C_BPARTNER.C_BPARTNER_ID = ?
        // note the value of the parameter is set below
        whereClause.append(" and ol.salesOrder.businessPartner.id=:bpId ");
     
        // AND C_ORDER.DOCSTATUS = 'CO'
        whereClause.append(" and ol.salesOrder.documentStatus='CO' ");

Add the order by.

    
    
     
        // ORDER BY C_BPARTNER_ID, ID
        whereClause.append(" order by ol.salesOrder.businessPartner.id, ol.id");

Now we are ready to create the OBQuery object using the main class we are
querying (the OrderLine.class) and the where-clause. The business partner
parameter is also added. The business partner id 1000017 is used, this can
differ based on the data in the database.

    
    
     
        // final Session session = OBDal.getInstance().getSession();
        // session.createQuery(hql.toString());
        final OBQuery<OrderLine> qry = OBDal.getInstance().createQuery(OrderLine.class,
            whereClause.toString());
     
        // set the business partner parameter
        final Map<String, Object> parameters = new HashMap<>(1);
        parameters.put("bpId", "1000017");
        qry.setNamedParameters(parameters);

The above where-clause results in the following overall HQL query (which is
not directly visible as it is held inside the OBQuery object):

    
    
     
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

Note the following:

  * The query is much simpler than the original SQL. 
  * The DAL has automatically added extra organization/client filtering. 

At this point the query is ready to be 'fired'. A for-loop is used. Within the
for-loop different data is retrieved from the OrderLine. The data retrieved
corresponds to the information requested in the SQL select clause. A separate
query will be used to retrieve the sum of the matched PO's (see below).

    
    
     
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
     

To get the sum of the matched PO's a second query needs to be used. This is
done within the for-loop. It is clear that this is less optimal than the
direct SQL statement, a different approach is discussed below.

Note that the ol object is passed as a parameter. We use a named parameter (
_orderLine_ ) to set it.

    
    
     
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

##  The result

The above code results in the following output:

    
    
     
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

##  The executed SQL, the N+1 select problem

Now let's look at the actual SQL which is executed. This will also show that
the above implementation might suffer from the N+1 select problem.

The SQL query is executed when the list() method is called on the query object
(the start of the for-loop). This results in the following query:

    
    
     
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

When comparing this SQL with the original SQL the main difference is that much
more information is selected. This is because in this approach we choose to
select the complete Order Line object. This makes the HQL query much simpler
but also less efficient. It is also possible to select the individual Order
Line fields, in this case a direct Hibernate query has to be used.

Now let's check what happens when information is requested from the Order Line
object. The Order Line object references other objects which are lazily loaded
(up-on-request). So the thing you will see is that additional queries are
fired by Hibernate (this is the N+1 select problem!).

when in the for-loop the following statement is executed:

    
    
     
          System.err.println(ol.getSalesOrder().getBusinessPartner().getId());

then Hibernate will fire the following two queries (select clause abbreviated
for clarity):

    
    
     
    SELECT businesspa0_.C_BPartner_ID AS C1_98_0_, businesspa0_.AD_Client_ID AS AD2_98_0_, 
    .... (ALL business partner COLUMNS are retrieved)
    FROM C_BPartner businesspa0_ WHERE businesspa0_.C_BPartner_ID=?
     
    SELECT adlanguage0_.AD_Language_ID AS AD1_247_0_, adlanguage0_.AD_Language AS AD2_247_0_, 
    .... (ALL COLUMNS of adlanguage are being retrieved)
    FROM AD_Language adlanguage0_ WHERE adlanguage0_.AD_Language=?

In the next Java statement;

    
    
     
          System.err.println(ol.getProduct().getIdentifier());

Hibernate will fire this SQL:

    
    
     
    SELECT product0_.M_Product_ID AS M1_31_0_, product0_.AD_Client_ID AS AD2_31_0_, product0_.AD_Org_ID AS AD3_31_0_,
    .... (ALL COLUMNS of M_Product are retrieved)
    FROM M_Product product0_ WHERE product0_.M_Product_ID=?

This means that for every Order Line, Hibernate will fire multiple additional
queries. This is why it is called the N+1 select problem, one query is used
for getting the overall results, and then for each result one or more queries
are done (N queries if the first result-set has N results).

Hibernate offers different ways to solve this issue:

  1. Use a second-level cache, if hibernate can find the refered-to object in the second-level cache then no query is fired. Using a second-level cache is an important performance improvement because in practice information does not change very often, most (often like 95%) access is read-access. 
  2. Use left join fetching in the original query: in this approach the referred-to information is retrieved together with the main query. This is discussed next. 

To enable left join fetching for the Product and Business Partner the
following has to be added to the where clause:

    
    
     
        whereClause.append(" left join fetch ol.product ");
        whereClause.append(" left join fetch ol.salesOrder ");
        whereClause.append(" left join fetch ol.businessPartner ");
        whereClause.append(" left join fetch ol.businessPartner.language ");

This has to be added just after the 'as ol' part.

Now when executing the query and for-loop additional queries are executed. The
original Order Line query will now have a 'from' clause with the additional
joined information:

    
    
     
    FROM C_OrderLine orderline0_ LEFT OUTER JOIN M_Product product1_ ON orderline0_.M_Product_ID=product1_.M_Product_ID 
       LEFT OUTER JOIN C_Order order2_ ON orderline0_.C_Order_ID=order2_.C_Order_ID 
       LEFT OUTER JOIN C_BPartner businesspa3_ ON orderline0_.C_BPartner_ID=businesspa3_.C_BPartner_ID 
       LEFT OUTER JOIN AD_Language adlanguage5_ ON businesspa3_.AD_Language=adlanguage5_.AD_Language

So this solves the N+1 select problem. Note that as mentioned above it also
makes sense to use the Hibernate second-level cache as this has other
performance benefits (data is retrieved from in-memory which is much faster
than querying, overall).

##  How you can see what SQL statements are executed

Note to see the SQL queries fired by Hibernate, the following log4j property
has to be set:

    
    
     
    ### log just the SQL
    log4j.logger.org.hibernate.SQL=debug

If it does not work for you, it is possible that the log4j.properties file is
read from another location than you expect. To see where log4j reads its
properties from set this jvm parameter:

    
    
     
    -Dlog4j.debug

##  An alternative HQL approach

The above approach focused on querying for the complete OrderLine object.

The main advantage of this approach is that the java code which processes the
results is much more meaningfull and easier to understand. However, this
approach has two performance drawbacks:

  * the queries have very large select clauses, all columns are returned, eventhough maybe only a subset is used 
  * this means that the sum of the matched PO's query has to be repeated, the reason is that it is not practical to list all properties of the OrderLine and its related entities in the group by clause. 

The above approach re-queries for the sum of the matched PO's inside the for-
loop. This is less optimal than querying directly in the database. A different
approach is to rewrite the HQL above to return the sum directly in the select
statement and use a group by clause in the HQL. This is certainly possible in
HQL, with the following remarks:

  * Instead of using OBQuery the Hibernate query object should be used, this object can be retrieved from the session object (as illustrated above). 
  * When using the Hibernate query object, organisation and client filtering is not automatically applied. So these filters have to be manually added to the hibernate query. 

With this in mind the following HQL will query for practically the same
information as listed above:

    
    
     
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

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
**NOTE:** The  OBDal  class offers two convenience methods to create the
client and organization filter clauses in the HQL:

    
    
     
    OBDal.getInstance().getReadableOrganizationsInClause();
    OBDal.getInstance().getReadableClientsInClause();  
  
---|---  
  
To use HQL directly you can get the Hibernate Session object from the OBDal
instance and call createQuery (the hql variable contains the above HQL). The
result of the above query is actually an Object array:

    
    
     
        final Query query = OBDal.getInstance().getSession().createQuery(hql);
        query.setParameter("bpId", "1000017");
     
        for (Object o : query.list()) {
          final Object[] os = (Object[]) o;
          for (Object result : os) {
            System.err.println(result);
          }
        }

The SQL executed by the above HQL is also simpler than before:

    
    
     
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

There are a few things to note about this 'simpler' SQL:

  * because HQL does not allow a select alias to be used in the where-clause, the sum on the matched PO quantities is repeated in the where clause 
  * the original SQL also took care of getting the identifier of a product and attribute set value. This is not possible when doing HQL in this approach. When the identifier values are important then the earlier 'query complete OrderLine object' can make more sense. 

##  Conclusion

This concludes the description of this complexer query in HQL. Some important
conclusions which can be drawn:

  * when performing more complex querying using Hibernate it is critical to analyze the SQL generated by Hibernate. 
  * with Hibernate it can make sense to actually move part of the processing and logic to Java. Although there are performance drawbacks, the resulting code and queries are much simpler. This results in less errors, and a more productive development. Which again leaves time for performance improvements in other areas. 
  * it really makes sense to use second-level caching to improve performance. 
  * consider to use 'left join fetching' to make control the amount of additional queries to be done. 

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_do_a_complex_query_using_the_DAL-2  "

This page has been accessed 13,082 times. This page was last modified on 17
July 2018, at 11:14. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

