---
tags: 
 - getting started
 - material requirement planning
 - process plan
 - product
 - work requirement
---

![cover-getting-started.png](/assets/getting-started/overview/cover-getting-started.png)

## Overview

In Material Requirement Planning the application is used to automatically review the demand and display suggestions concerning required supply. In the *Manufacturing Plan*, the application suggests required *Work Requirements* and *Requisitions*. In the *Purchasing Plan*, the application suggests required *Purchase Orders*.

## Material Requirement Planning

The Master Requirement Planning consists of two plans:

- Manufacturing Plan: plan to display calculations related to products that go through Production. The suggested documents to be created in this plan are the [Work Requirement](/user-guide/etendo-classic/basic-features/production-management/transactions/#work-requirement) and the [Requisition](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#requisition).
- Purchasing Plan: plan to display calculations related to products that are procured. The suggested document to be created in this plan is the [Purchase Order](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#purchase-order).

*Planning Methods* are entered to define what supply components are taken into account with the calculations of these plans.

### **Configuration**

Apart from the set up screens in the MRP module that are configured, additional set ups are required.
For the products that are planned in the *Manufacturing Plan*, the following configurations are required:

- the [Process plan](/user-guide/etendo-classic/basic-features/production-management/setup/#process-plan)  is set up for the product.
- the production checkbox and the Process Plan name are selected in the [Product](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) screen.
the [Manufacturing](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#manufacturing) tab in the Product screen is filled out with the information required for MRP to make the calculations for the Manufacturing plan.

For the products that are planned in the *Purchasing Plan*, the following configurations are required:

- the purchase checkbox is selected in the [Product](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) screen.
- the [price](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#price) of the product is defined for the price list of the vendor that is entered in the Purchasing tab.
- the [Purchasing](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#purchasing)  tab in the Product screen is filled out with the information required for MRP to make the calculations for the Purchasing Plan.
- the vendor that is reflected as the Business Partner in the above mentioned Purchasing tab is filled out in the Business Partner screen:


    - [Vendor/Creditor](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#vendorcreditor) tab with at least the following fields filled out:
        - Purchase Price List
        - PO Payment Method
        - PO Payment Terms
    - [Location/Address](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#vendorcreditor) tab

- The [Manufacturing](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#manufacturing) tab in the Product screen is filled out with the *Planning Method* and *Planner* information.

### **Execution** 

The material planner enters a Manufacturing Plan for a product for a certain time period and processes the plan.
In the created overview the material planner reviews and analyzes the lines. Based on the information that is processed by MRP, the plan suggests *Work Requirements* and *Requisitions* for certain quantities and certain dates.

- If required, adjustments to the set ups, for example the planning method, are done. The lines of the plan are recalculated by clicking the Recalculate Dates/Quantities button.
- If required, manual changes to the created lines with regards to quantities and dates are made.
- once the plan is correct, any suggested requisitions are created by clicking the Generate Material Requisitions button and any suggested Work Requirements are created by clicking the Generate Work Requirements button.
- the material planner completes the created requisition(s) and processes the created Work Requirement(s).


The material planner then enters a Purchasing Plan for a product for a certain time period and processes the plan.
In the created overview the material planner reviews and analyzes the lines. Based on the information that is processed by MRP, the plan suggests *Purchase Orders* for certain quantities and certain dates.

- If required, adjustments to the set ups, for example the planning method, are done. The lines of the plan are deleted and the plan is reprocessed.
- If required, manual changes to the created lines with regards to quantities and dates are made.
- once the plan is correct, any suggested purchase orders are created by clicking the *Create Purchase Orders* button.
- the material planner completes the created purchase order.

## Relationship with other areas

The MRP interacts with the following modules:

- [Procurement Management](/user-guide/etendo-classic/basic-features/procurement-management/getting-started/):
    - [Requisitions](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#requisition) are created from the Manufacturing Plan
    - [Purchase Orders](/user-guide/etendo-classic/basic-features/procurement-management/transactions/#purchase-order) are created from the Purchasing Plan
- [Sales Management](/user-guide/etendo-classic/basic-features/sales-management/getting-started/):
    - [Sales Orders](/user-guide/etendo-classic/basic-features/sales-management/transactions/#sales-order) are optionally taken into account in the calculations of both plans
- [Warehouse Management](/user-guide/etendo-classic/basic-features/warehouse-management/getting-started/):
    - [Stock levels](/user-guide/etendo-classic/basic-features/warehouse-management/analysis-tools/#stock-report) are automatically taken into account in the calculations of both plans
- [Production Management](/user-guide/etendo-classic/basic-features/production-management/getting-started/):
    - the [Process Plan](/user-guide/etendo-classic/basic-features/production-management/setup/#process-plan) is used for the calculation of the Manufacturing Plan
    - [Work Requirements](/user-guide/etendo-classic/basic-features/production-management/transactions/#work-requirement) are created from the Manufacturing Plan





