---
title: Material Requirement Planning Setup
---
## Overview

In order to initiate the Material Requirement Planning (MRP) process, the Planning Method and the Planner sections must be configured: 

!!! info
    For this, Aaditional setups are required. Check the information in the [Overview section of MRP module](/docs/products/etendo-classic/user-guide/material-requirement-planning/transactions/). 


## Planning Method

### Overview

Define how transaction types will be dealt with in the application.

A Planning Method is used to define the **optional components of supply and demand and their percentage to be taken into account** during the execution of the MRP process creating the **Manufacturing Plan** and **Purchasing Plan**. Each product that is planned in either the Manufacturing plan or the Purchasing Plan has a Planning Method defined in the product setup.

By **default**, MRP takes **stock** and **safety stock** into account when creating the plans, but the following transactions are optional and are configured in the Planning Method:

-   **Material Requirement**: demand for the product on requisitions in completed status. 
!!! info
    For more details, see the [_Requisition_](/docs/products/etendo-classic/user-guide/master-data-management/master-data/#product) section.

- **Sales Forecast**: prevision of future demand for the product. 
!!! info
    For more details, see the [_Sales Forecast_](/docs/products/etendo-classic/user-guide/material-requirement-planning/transactions/#mrp-forecast) section.

-   **Pending Sales Order**: demand for the product on sales orders in booked status that are not shipped yet. 
!!! info
    For more details, see the [_Sales Order_](/docs/products/etendo-classic/user-guide/sales-management/transactions/#sales-order) section.

-   **Pending Work Requirement**: supply for the product on a processed work requirement. 
!!! info
    For more details, see the [_Work Requirement_](/docs/products/etendo-classic/user-guide/production-management/transactions/#work-requirement) section.

-   **Pending Purchase Order**: supply for the product on a booked purchase order that is not received yet. 
!!! info
    For more details, see the [_Purchase Order_](/docs/products/etendo-classic/user-guide/procurement-management/transactions/#purchase-order) section.


### **Header**

Use the header to create a planning method.

In this tab, the organization and the **name of the planning method** is entered. A general planning method can be entered to include all components of the optional demand and supply, because any components that are not applicable for a certain product will just not appear in the plan, while any components that are left out by mistake result in incorrect and incomplete calculations of the plan.

![](/docs/assets/drive/r-sIhmWnmoYNZsemrEKq3Il7LQsg1iDrcrq5K3H2HprddfyVZa7wiE5nmb6uaDHTpzSWHiHnvCetwhHQ_RBq1NJP3cIv17F96ZxBnqmyeWowc_zmB432U68KEEtdZbheLdRHdx9w00xaewhcEybYe4E.png)

### **Lines**

Add transactions to be included in your plan. Each transaction is shown on its own line.

In this tab, the applicable transactions are entered on separate lines. For each transaction type, it is possible to define whether transactions are considered for the whole **time horizon** on the Manufacturing plan and Purchasing Plan or just a part:

-   **days from start**: the number of days from the beginning of the time horizon to the start of the transaction time frame being considered.
-   **days to end**: the number of days from the beginning of the time horizon to the end of the transaction time frame being considered.

Also, a percentage of the quantity to be considered by MRP is configured with the **Weighting**. If a sales forecast for 100 units is entered with a weighing of 0.9, only 90 units are reflected in the Manufacturing plan or Purchasing plan. Likewise, a value above 1 can be entered to include a higher number in the plans.

![](/docs/assets/drive/r3xp-vXHNSPnrw9FA7ashqCDRgL0s5LE9i_8sNTRssgBQiOX5bDavCyyxMCmCXIUKzvbPdxvrp6wkfXKLFftUwcqNn3u57H56hpHgKp4z0YkfjBobN-fV1M_gGf09M7MyrjutIBaZzR40_IdhQn8fb0.png)

## **Planner**

### **Overview** 

Define the entity in charge of managing the purchase or production of specific products.

An **optional filter on both the Manufacturing Plan and the Purchasing Plan** is the planner. The information that is entered in this screen has no relation with the Business Partner set up. After the planner is created, the planner information is entered in the [Product](/docs/products/etendo-classic/user-guide/master-data-management/master-data/#product) tab in the Master Data Management section.

### **Planner**

Define the planner in charge of managing the purchase or production of specific products.

![](/docs/assets/drive/2IK-YKaAHZYtnh4V1r_P9QgY4oU3-wDlu73TD8YZffxiibZ-JWkhjD_fCnJLzntBSgBhJSLbMx3IOsYOPFoDahYodIPGEq1P8LytGAg9aCEylB2iknxNfhnwCH8MgxgF1F6CYXVQxBPfF7KuArrucc4.png)