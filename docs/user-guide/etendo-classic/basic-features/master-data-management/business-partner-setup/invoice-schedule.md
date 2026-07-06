---
title: Invoice Schedule
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Invoice
---

## Invoice Schedule

:material-menu: `Application` > `Master Data Management` > `Business Partner Setup` > `Invoice Schedule`

### Overview


Invoice schedule window allows the user to define and configure how often and by when an organization can issue invoices to be sent to customers.

### Invoice Schedule

An organization can agree and therefore define specific schedules for issuing invoices, schedules which will then need to be linked to the corresponding customers.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/invoice-schedule/invoice-schedule-1.png)

As shown in the screen above, an invoice schedule can be easily created by entering below data:

- a **Name** for the invoice schedule
- a **Description** if needed
- the **Invoice Frequency** which defines how often sales invoices are going to be issued. The values allowed are:
  - **Daily** - a daily invoice schedule does not require any additional setup as it implies a daily generation of sales invoices.
  - **Monthly** or **Twice Monthly** - a monthly or twice monthly invoice schedule requires to enter additional data such as:
    - **Day of the Month** - this is the day when the invoice is generated, by example: 1st February.
    - **Invoice Cut-Off Day** - this is the last day for including the orders to be invoiced, by example: 31st January
  - **Weekly** - a weekly invoice schedule requires to enter additional data such as:
    - **Day of the Week** - when the invoice is going to be generated, by example: Saturday
    - **Day off the Week Cut-Off** - this is the last day of the week for including the orders to be invoiced, by example: Friday.

The process "**Generate Invoices**" takes into account both:

- the "**Invoice Terms**",  
  to learn more about "Invoice Terms" visit "Master Data Management // Business Partner // Customer tab".
- as well as the **"Invoice Schedule"**

agreed and therefore assigned to each customer.

To learn more about this process, visit "Sales Management // Transactions".
