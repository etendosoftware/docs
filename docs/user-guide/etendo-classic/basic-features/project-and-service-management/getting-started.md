---
tags: 
 - getting started
 - project
 - service
 - management
 - transactions
 - setup
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
#

## Overview

HOW IS THIS USEFUL?

The Project and Service Management module consists of:

- Multiphase Project to manage project with phases and tasks
- Expense Sheets to manage cost related to projects

VA - IMAGE TO EDIT - ALE

ADD EXPLANATION

### Configuration

The following is entered in the application for the project and service management module:

- **Project Dimension**: in order to be able to select projects on orders and invoices, the project [dimension](../financial-management/accounting/setup.md#general-ledger-configuration#dimension) is created as a new record with type Project in the Dimension tab of the [General Ledger Configuration]() window.

- [**Product**](../master-data-management/master-data.md#product):
    - Product type Service and Expense Type: for the expense sheet products with product type Service (for time) and product type Expense Type (for expenses) are set up.
    - Product type Item: the standard [procure to pay](../procurement-management/getting-started.md#procure-to-pay-business-flow) process is used for the purchase or products related to the project.

- [**Business Partner**](../master-data-management/master-data.md#business-partner):
    - Customer: the third party for whom the project is executed is set up as a customer.
    - Vendor: the third party that supplies products related to the project is set up as a vendor.
    - Employee:
        - The vendor information is filled out in order to create purchase invoices to reimburse expenses.
        - The salary category is filled out to calculate cost for the time spend on the project as documented in time sheets.

- **Project Type**: a template with standard phases and tasks can be created to easily generate phases and tasks on a multiphase project.

### Execution

The [Multiphase Project]() has the following sequence of events:

- the creation of the Multiphase Project with the following information:
    - planned amounts and margins related to the project
    - information needed to create a Sales Order
    - product information related to the project (?)
    - optionally a Project Type is created or an existing one is used to create the phases and tasks. Alternatively without using a project type, phases and tasks are created manually on the Multiphase Project.
    - start and end dates for the overall project and for phases and tasks
    - project status is changed to Order
- planned versus actual cost is monitored on the Project Profitability report based on the following:
    - time sheets and item expenses are reported in Expense Sheets related to the project. Based on the salary category of the employee at the time of the project, the cost of the time spend is calculated by the application.
    - any purchases, outsourcing cost or expenses reimbursement related to the project reference the project name on the Purchase Invoice
    - any Sales Invoice created as a result of the Expense Sheets have the project name refereced
    - at the end of each phase a Sales Order related to the phase is created from the Multiphase Project. This results in the creation of a Sales Invoice
- progress of the project is monitored in the Project Progress report
- after completion of all phases the Multiphase Project status is changed to Order Closed.

The key project and service management concepts mentioned in this chapter are:

- Business Partner:
    - Supplier: third party that supplies goods and/or services. In project and service management the supplier is the vendor of provided goods related to the project, the consultancy company that consultancy services were outsourced to and the employee that is reimbursed for expenses related to a project.
    - Customer: the party that goods or services are sold to. In project and service management the customer is who gets charged for the cost and expenses of the project.
    - Employee: person that works in the company.In project and service management, the employee information is used for the cost calculation of the project, based on time sheets.
- Sales Order: document that lists goods and/or services provided to a customer and the conditions of the sale.
- Sales Invoice: document used to administer a right to collect. The document lists the goods and/or services provided to a customer and the conditions of the sale.
- Purchase Invoice: document used to administer an obligation to pay. The document lists goods and/or services provided by a supplier.
- Project Type: template used to easily create phases and tasks on a multiphase project.
- Multiphase Project: form used to registrate a project, the planned expenses, marges, who the project will be executed for and the phases and tasks of the project.
- Project Phase: a time period during which certain activities are executed.
- Project Task: activities that are executed during a project phase.
- Expense Sheet: form used to register item expenses and time for a project.

## Relationship with other areas

Project and Service Management interacts with the following modules:

- [Procurement Management](../procurement-management/getting-started.md):
    - materials related to the project are ordered using the Procure to Pay process
    - purchase invoices are generated for expenses paid to employees and for good ordered from vendors
- [Sales Management](../sales-management/getting-started.md): sales orders and sales invoices are generated for the customer for whom the project is executed.
- [Warehouse Management](../warehouse-management/getting-started.md): materials ordered for the project may be received into stock.
- [Financial Management](../financial-management/getting-started.md): the information of the created sales and purchase invoices is send to accounts payables and receivables.

---

This work is a derivative of ["Project and Service Management"](https://wiki.openbravo.com/wiki/Project_and_Service_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.