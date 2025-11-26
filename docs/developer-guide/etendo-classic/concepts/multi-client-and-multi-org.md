---
title: Multi-Client and Multi-Org
tags:
    - Multi-Client
    - Multi-Org
    - Concepts
    - Data Access Layer

status: beta
---

#  Multi-Client and Multi-Org

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.
  
##  Overview

This document describes multi-client and multi-organization from the development perspective. For a functional comprehension about these features read the [Functional Documentation](../../../user-guide/etendo-classic/basic-features/general-setup/getting-started.md).

##  Structure

At database and application dictionary level, all tables must have the structure needed to support multi-client and multi-org. It is described in the [Database Tables document](../concepts/tables.md#clientorganization).

##  Filtering data

This section explains the code needed to properly filter data regarding client and organization in order to avoid accesses to not allowed information. These filters are different in case the development is using XSQL or DAL.

###  Data Access Layer

The [Data Access Layer](../concepts/data-access-layer.md)  provides several interfaces to make it easier to query for data:  OBCriteria  and  OBQuery ??? . These service classes take care of security and automatic filtering on readable clients and organizations.

The filtering on readable clients and organizations can be disabled by calling the relevant methods (`setFilterReadableOrganizations/setFilterReadableClients`).

When querying directly for one object (the OBDal.get method) then no filtering on readable client/organization is done.

The data access layer also checks read access when accessing an object in-memory. These checks make a difference between readable and derived-readable entities. For derived readable entities a user may only see the value of identifier properties. See  here  for more information.

There are also cases where it makes sense to create your own HQL queries and execute them directly. To support this the OBDal service provides two convenience methods which can be used to add eadableClients/readableOrganizations in-clauses to the where-clause:

```
OBDal.getInstance().getReadableOrganizationsInClause();
OBDal.getInstance().getReadableClientsInClause();
```

The data access layer also checks for write access to clients/organizations when an object is inserted/updated. This check is done for each object which is saved (see [here](../concepts/data-access-layer.md#write-access) for more information). An additional check which is done is that an object may only refer to objects in the natural tree of its own organization.

###  OrganizationStructureProvider

The OrganizationStructureProvider class is a Java utility class designed to help in very common organization-related tasks. For example, this class contains methods to find if an organization belongs to the natural tree of another organization, to find out the parent natural tree of an organization,
or the children tree of an organization.

It is strongly advisable that if the DAL is being used, this class should be used too if any of these tasks needs to be done.

###  XSQL - Definition

All queries used to show or modify data should include filter by client and organization. The only exception to this rule are the queries that affect only to rows selected by a known ID (which has been obtained, in most cases, from a query following the rule), in this case as that row is known to be accessible by the user the filter is not needed.

In the XSQL the where clause the query must look like:

```
SELECT ...     
    FROM ...
WHERE ...
    AND AD_CLIENT_ID IN ('1')
    AND AD_ORG_ID IN ('1')
        ...
```

And the parameters section: 

<Parameter name="adClientId" optional="true" type="replace" after="AND AD_CLIENT_ID IN (" text="'1'"/>

<Parameter name="adOrgId" optional="true" type="replace" after="AND AD_ORG_ID IN (" text="'1'"/>

This will create a couple of parameters: `adClientId` and `adOrgID`, how to pass them is explained in the following section.

### XSQL - Java Usage

#### Client

Only the current logged client is accessible even though the role has permission for different clients. Additionally, depending on the user level defined for the role and on the access level for the table which is being accessed access to client 0 (system) is granted or denied.

In order to obtain the list of accessible clients (current client and 0 in case it can be accessed), the `Utility.getContext` method is used, it has the following structure:

```
public static String getContext(ConnectionProvider conn, VariablesSecureApp vars, String context, String window)
```

or

```
public static String getContext(ConnectionProvider conn, VariablesSecureApp vars, String context, String window, int accessLevel)
```

In the first case, access level is not passed so it is not taken into account to calculate if client 0 is accessible. This is the way it is generally used for manual code. A standard call to this method would be:

```
String strClient = Utility.getContext(this, vars, "#User_Client", "");
```
  
The second one receives accesslevel for the table which is being accessed, this is the way WAD windows obtain the client list.

####  Organization

There are three levels for organization access **Editable** , **Accessible** and **Referenceable** .

#####  Editable

Only data in an editable organization can be modified. Editable organizations are those explicitly granted to the role.

The list of editable organizations is obtained with:

```
Utility.getContext(conn, vars, "#User_Org", windowId, accesslevel)
```

This type must be used when displaying data which the user can modify. For example a process window that shows records the user can do an action with them.

#####  Accessible

Accessible data can be viewed but not modified. The list of accessible organizations consists in the standard tree of his orgList, this is, all the granted organizations, their ancestors and their descendants organizations. To obtain it:

```
Utility.getContext(conn, vars, "#AccessibleOrgTree", windowId, accesslevel)
```

This type should be used when displaying information data. For example in reports. It is also used for combos in filters. For example a combo shown in a filter for a report.

#####  Referenceable

A record can make reference to other records with data defined in the standard tree of the parent record organization.

```
Utility.getReferenceableOrg(vars, currentOrg)
```
  

#####  Selectors (Searchs)

Selectors are a case that deserves a specif attention, they have two main elements: **Filter** and **Data**.

######  Filter

When a combo is used in a filter the list of organizations it receives is the accessible one:

```
Utility.getContext(conn, vars, "#AccessibleOrgTree", windowId, accesslevel)
```

If another selector is used within the filter, no organization should be passed to it (it has no effect in the current implementation, see following chapter).

######  Data

As main purpose of selectors is to select data to be referred from other records, they implement **Referenceable** filtering.

When a selector is called from a window which will not receive a record to reference to (for example a filter in a report) it will not filter by referenceable organizations but by accessible ones.

The implementation for selectors require:

* Add an input variable to all selectors to get the organization (defined in Application Dictionary || Reference || Reference >> Selector Reference >> Selector Reference Columns) 
* In the _DEFAULT_ and _KEY_ commands read this variable with: 

```
vars.getStringParameter("inpAD_Org_ID");
```

* Add a new hidden variable in the HTML and store the read value there. 
* In the _DATA_ command read information from the hidden HTML input and use it to obtain the referenceable list of orgs using: 

```
Utility.getSelectorOrgs(conn, vars, readOrg);
```

* Use the obtained list to filter the query. 

The previously mentioned `Utility.getSelectorOrgs` method returns the referenceable organizations or the accessible ones depending whether the passed organization is empty or not.

This implementation allows to automatically obtain the referenceable list of orgs for the wad windows and, by default, the accessible ones for manual code. If it were desirable for any manual window to get the referenceable list instead the accessible one it only would be necessary to modify the javascript
calling the selector to include the organization.

###  SQL - AD_IsOrgIncluded

`AD_IsOrgIncluded` is a database stored function that can be used to know whether two organizations belong to the same tree or not.

It receives 3 parameters:

* `p_orgid`. Checks that this organization is a descendant for the `p_parentorgid` organization. 
* `p_parentorgid`. Checks that this organization is a ascendant for the `p_orgid` organization. 
* `p_clientid`. It is the client where both organizations are expected to be in. 

This function returns -1 in case 2nd organization is not an ascendant for 1st one or the level in the hierarchy in case it is.

##  Transactions

When developing transactional processes it must be taken into account that those processes should only affect rows in editable client and organizations. They also must check that all objects involved in the process are in a correct organization (for example using `AD_IsOrgIncluded` function).

###  Organization specific data

It is possible to define a structure that allows to define objects in a organization and change some of their attributes for another organization lower in the organization tree hierarchy. Currently Etendo core implements it for  products  using the  `M_Product_Org`  table. In this case it is possible to define products for example in organization *, and overwrite some of their attributes for other organizations. The effect would be that by default attributes defined for product in organization * are used except in the case they are overwritten in the current organization. This management must be done manually when developing processes using these tables.

For example this query is part of the `MRP_ProcessPlan_Recalculate` process, it looks for the values that are overwritten in the current organization and takes them if they exist:

```
SELECT QTY, planneddate, plannedorderdate, M_PRODUCT.M_PRODUCT_ID,
            COALESCE(M_PRODUCT_ORG.CAPACITY, M_PRODUCT.CAPACITY) AS CAPACITY,
            COALESCE(M_PRODUCT_ORG.DELAYMIN, M_PRODUCT.DELAYMIN, 0) AS DELAYMIN,
            COALESCE(M_PRODUCT_ORG.QTYTYPE, M_PRODUCT_ORG.QTYTYPE, 'E') AS qtytype,
            COALESCE(M_PRODUCT_ORG.QTYMIN, M_PRODUCT_ORG.QTYMIN, 0) AS qtymin,
            COALESCE(M_PRODUCT_ORG.QTYSTD, M_PRODUCT_ORG.QTYSTD, 1) AS qtystd
        INTO v_Qty, v_planneddate, v_plannedorderdate, v_Product,
            v_capacity, v_delaymin, v_qtytype, v_qtymin, v_qtystd
    FROM M_PRODUCT INNER JOIN MRP_RUN_PRODUCTIONLINE ON MRP_RUN_PRODUCTIONLINE.M_PRODUCT_ID = M_PRODUCT.M_PRODUCT_ID
                                                    AND MRP_RUN_PRODUCTIONLINE_ID = p_Run_ProductionLine_ID
                    LEFT JOIN M_PRODUCT_ORG ON M_PRODUCT.M_PRODUCT_ID = M_PRODUCT_ORG.M_PRODUCT_ID
                                            AND M_PRODUCT_ORG.AD_ORG_ID = MRP_RUN_PRODUCTIONLINE.AD_ORG_ID;
```

---

This work is a derivative of [Multi-Client and Multi-Org](http://wiki.openbravo.com/wiki/Multi-Client_and_Multi-Org){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.