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

The Project and Service Management functionality is essential for businesses to handle projects, services, or both. It helps organizations plan, execute, monitor, and optimize projects and services efficiently by integrating them with other functionalities such as Procurement Management, Sales Management, Financial Management, etc.

The Project and Service Management module consists of:

- [Multiphase Project](../project-and-service-management/transactions.md#multiphase-project) to manage project with phases and tasks.
- [Expense Sheets](../project-and-service-management/transactions.md#expense-sheet) to manage cost related to projects.

DIAGRAM - IMAGE TO EDIT - ALE

As seen in this diagram, after setting up the information shown [below](#configuration), in order to manage a project, the user should enter a [Multiphase project](../project-and-service-management/transactions.md#multiphase-project) in the corresponding window. This window allows registering the progress of a project in different [phases](../project-and-service-management/transactions.md#project-phase-tab). Each project includes one or more phases and, in each phase, one or more [tasks](../project-and-service-management/transactions.md#project-task-subtab). For each of these phases, it is possible to perform a [Procure to Pay](../procurement-management/getting-started.md#procure-to-pay-business-flow) process, for necessary purchases in the project, or an [Order to Cash](../sales-management/getting-started.md#order-to-cash-business-flow) process  for necessary sales in the project. For registering required project expenses, the [expense sheet](../project-and-service-management/transactions.md#expense-sheet) window is used. Once one phase is closed, the user can review profitability by using the available [analysis tools](../project-and-service-management/analysis-tools.md). This flow is done for each of the phases of a project, and once all the phases are completed, the project can be [closed](../project-and-service-management/transactions.md#process-buttons).

### Key Concepts

The key project and service management concepts mentioned in this chapter are:

- [Business Partner](../master-data-management/master-data.md#business-partner):
    - Supplier: third party that supplies goods and/or services. In project and service management the supplier is the vendor of provided goods related to the project, the consultancy company that consultancy services were outsourced to and the employee that is reimbursed for expenses related to a project.
    - Customer: the party that goods or services are sold to. In project and service management the customer is who gets charged for the cost and expenses of the project.
    - Employee: person that works in the company.In project and service management, the employee information is used for the cost calculation of the project, based on [time sheets](../project-and-service-management/transactions.md#expense-sheet).
- [Sales Order](../sales-management/transactions.md#sales-order): document that lists goods and/or services provided to a customer and the conditions of the sale.
- [Sales Invoice](../sales-management/transactions.md#sales-invoice): document used to administer a right to collect. The document lists the goods and/or services provided to a customer and the conditions of the sale.
- [Purchase Invoice](../procurement-management/transactions.md#purchase-invoice): document used to administer an obligation to pay. The document lists goods and/or services provided by a supplier.
- [Project Type](../project-and-service-management/setup.md#project-type): template used to easily create phases and tasks on a multiphase project. This is specially useful to automatically complete phases and tasks according to the template without doing the process manually.
- [Multiphase Project](../project-and-service-management/transactions.md#multiphase-project): form used to registrate a project, the planned expenses, margins, who the project will be executed for and the phases and tasks of the project.
- [Project Phase](../project-and-service-management/transactions.md#project-phase-tab): a time period during which certain activities are executed.
- [Project Task](../project-and-service-management/transactions.md#project-task-subtab): activities that are executed during a project phase.
- [Expense Sheet](../project-and-service-management/transactions.md#expense-sheet): form used to register item expenses and time for a project.

### Configuration

The following is entered in the application for the project and service management module:

- [**Project Dimension**](../financial-management/accounting/setup.md#general-ledger-configuration#dimension): in order to be able to select projects on orders and invoices, the project dimension is created as a new record with type Project in the Dimension tab of the [General Ledger Configuration](../financial-management/accounting/setup.md#general-ledger-configuration) window.

- [**Product**](../master-data-management/master-data.md#product):
    - **Service** and **Expense Type** Products Types: for the expense sheet products with product type Service (for time) and product type Expense Type (for expenses) are set up.
    - **Item** Product type: the standard [procure to pay](../procurement-management/getting-started.md#procure-to-pay-business-flow) process is used for the purchase or products related to the project.

- [**Business Partner**](../master-data-management/master-data.md#business-partner):
    - Customer: the third party for whom the project is executed is set up as a customer.
    - Vendor: the third party that supplies products related to the project is set up as a vendor.
    - Employee:
        - The vendor information is filled out in order to create purchase invoices to reimburse expenses.
        - The salary category is filled out to calculate cost for the time spend on the project as documented in time sheets.

- [**Project Type**](../project-and-service-management/setup.md#project-type): a template with standard phases and tasks can be created to easily generate phases and tasks on a multiphase project.

### Execution

The [Multiphase Project](../project-and-service-management/transactions.md#multiphase-project) has the following sequence of events:

- The creation of the Multiphase Project with the following information:
    - Planned amounts and margins related to the project in the Amounts section of the header.
    - Information needed to create a Sales Order in the More Information section of the header.
    - Optionally, with the [**Set Project Type**](../project-and-service-management/transactions.md#process-buttons) button, an existing Project Type is used to create the phases and tasks. Alternatively without using a project type, phases and tasks are created manually on the Multiphase Project.
    - Start and end dates for the overall project and for phases and tasks.
    - Once this information is entered, the project status is changed to [Order](../project-and-service-management/transactions.md#process-buttons).
- Planned versus actual cost is monitored on the [Project Profitability](../project-and-service-management/analysis-tools.md#project-profitability) report based on the following:
    - Time sheets and item expenses are reported in [Expense Sheets](../project-and-service-management/transactions.md#expense-sheet) related to the project. Based on the salary category of the employee at the time of the project, the cost of the time spend is calculated by the application.
    - Purchase invoices are created for any purchases, outsourcing cost or expenses reimbursement related to the project. This is done through the [Create AP Expense Invoices](../project-and-service-management/transactions.md#create-ap-expense-invoices).
    - Sales invoices are created as a result of the Expense Sheets of the project. This is done through the [Create Sales Orders from Expenses](../project-and-service-management/transactions.md#create-sales-orders-from-expenses).
    - At the end of each phase, a Sales Order related to the phase is created from the Multiphase Project using the [Create Sales Order from Project Phase](../project-and-service-management/transactions.md#process-button). The information for the creation of the Sales Order is taken from the definition of the Project and it is made for whom the project is executed. This results in the creation of a Sales Invoice. ??
- The progress of the project is monitored in two ways. For each project, the [phases](../project-and-service-management/transactions.md#project-phase-tab) and [tasks](../project-and-service-management/transactions.md#project-task-subtab) can be marked as completed in the checkbox for this purpose. Also, the [Project Progress](../project-and-service-management/analysis-tools.md#project-progress) report can be used. Remember the accuracy of the information in the report depends on the Complete checkboxes use in the Phase and Task tabs.
- After completion of all phases, the Multiphase Project status is changed to [Order Closed](../project-and-service-management/transactions.md#process-buttons).

!!!info
    Remember this is a general overview of the Project and Service Management, visit the [Setup](../project-and-service-management/setup.md), [Transactions](../project-and-service-management/transactions.md) and [Analysis Tools](../project-and-service-management/analysis-tools.md) sections for more specific information.

## Relationship with other areas

Project and Service Management interacts with the following modules:

- [Procurement Management](../procurement-management/getting-started.md):
    - Materials related to the project are ordered using the Procure to Pay process.
    - Purchase invoices are generated for expenses paid to employees and for good ordered from vendors.
- [Sales Management](../sales-management/getting-started.md): Sales orders and sales invoices are generated for the customer for whom the project is executed.
- [Warehouse Management](../warehouse-management/getting-started.md): Materials ordered for the project may be received into stock.
- [Financial Management](../financial-management/getting-started.md): The information of the created sales and purchase invoices is send to accounts payables and receivables.

---

This work is a derivative of ["Project and Service Management"](https://wiki.openbravo.com/wiki/Project_and_Service_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.