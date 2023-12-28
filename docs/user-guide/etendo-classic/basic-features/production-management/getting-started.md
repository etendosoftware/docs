---
tags: 
 - getting started
 - production management
 - process plan
 - work requirement
 - work effort
---

![cover-getting-started.png](/assets/getting-started/overview/cover-getting-started.png)

## Overview

The Production Management module allows managing the standard productive process: production plan, work requirement, end products report and its direct and indirect costs. It is also possible to manage quality control and machine maintenance in production.

## Production Management

The main documents to manage the production process are:

- the Process Plan
- the Work Requirement
- the Work Effort

![](/assets/drive/1lCJc82jrHhfKt3KS2Eg9SS0aoPpYMsD7.png)

#### **Configuration**

Apart from the setup screens in the Production module, additional setups are required.

For Production, there are different products that are set up:

- Raw material used in production
  - the Production checkbox is selected to indicate that the product is used for production
  - the process plan is selected
  - the default storage bin that is used for P- raw materials is defined in the [_Manufacturing_](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) tab.
- Finished products manufactured in production
  - the Production checkbox is selected to indicate the product is manufactured in production
  - the process plan is selected
  - the default storage bin that is used for the product is defined in the [_Manufacturing_](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) tab
- based on [cost calculations](/user-guide/etendo-classic/basic-features/production-management/transactions/#calculate-standard-costs), a "theoretical" standard cost can be determined for the finished product
- a safety stock level is determined and entered for the product

Any semi finished products are created directly in the process plan by copying the information of a raw material product used in the operation. Once created, the default storage bin is defined in the [_Manufacturing_](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) tab.

!!! info
    For more information about the configuration of products, please refer to the [_Product_](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#product) section.

Also, Business Partners are configured for production:

In the Employee tab, any employees that are involved in the production process have the operator checkbox selected.

Likewise, the [_Salary category_](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#salary-category) configured for employees is very important since they are included in the final cost calculations.

!!! info
    For more information about the configuration of business partners, please refer to the [_Business Partner_](/user-guide/etendo-classic/basic-features/master-data-management/master-data/#business-partner) section.

Work Efforts can be posted to the [_General Ledger Journal_](/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/#gl-journal). In order to facilitate the posting, the **MaterialMgmtProductionTransaction** table is activated in the [_Active Tables_](/user-guide/etendo-classic/basic-features/financial-management/accounting/setup/#glconfig) tab of the General Ledger configuration.

#### **Execution**

Sales staff enters Sales Order for the product with the quantity required and the date by when it needs to be delivered. If the product is not in stock, it needs to be produced.

Also, if the stock level is below the safety stock level, products have to be produced.

The information about the demand from sales orders and safety stock is handled in 2 ways:

- automatically in MRP
- manually by a production manager

Ideally, the information is handled by MRP. If not, a production manager reviews if production of the product is required by reviewing the total demand:

- the outstanding sales orders
- the safety stock level

and compare it with the total supply:

- the stock level
- scheduled Work Requirements

If the demand is higher than the supply, or the dates of scheduled Work Requirements are not matching the dates of the outstanding sales orders, the product needs to be produced and a production manager executes:

- review of the stock of the raw material. If needed, the raw material will be requested and used in the [_procurement management_](/user-guide/etendo-classic/basic-features/procurement-management/transactions/) process.
- entry of the Work Requirement for the required quantity with the required quantity and the planned date
- generate Work Efforts from the Work Requirement.

The staff responsible for executing the production can see on the Production Run Status Report what production has to be executed.

At the end of each shift, the production managers enter the information of what is produced in the [_Production Run_](/user-guide/etendo-classic/basic-features/production-management/transactions/#production-run_1) screen.

## Relationship with other areas

Production Management interacts with the following modules:

- [_Procurement Management_](/user-guide/etendo-classic/basic-features/procurement-management/getting-started): raw material required for use in production is bought using the Procure to Pay process
- [_Sales Management_](/user-guide/etendo-classic/basic-features/sales-management/getting-started): demand for the products that are produced are generated through the Order to Cash process
- [_Warehouse Management_](/user-guide/etendo-classic/basic-features/warehouse-management/getting-started):
    - raw material is taken from the warehouse to be used in production
    - end products that come out of production are put into stock
- [_MRP_](/user-guide/etendo-classic/basic-features/material-requirement-planning/transactions/): Work Requirements can be a result of MRP
- [_Financial Management_](/user-guide/etendo-classic/basic-features/financial-management/getting-started): Cost related to Production is calculated for finance.
