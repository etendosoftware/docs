---
title: Payment Term
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Payment Terms
---

## Payment Term

:material-menu: `Application` > `Master Data Management` > `Business Partner Setup` > `Payment Term`

### Overview

A payment term specifies the period allowed to pay off an amount due.

A vendor or a customer may demand a deferred payment period of 30 days or may even demand to partially pay their debts or collect in two or more deferred periods.

Therefore "Payment Terms" will generate a list of scheduled payment/s against an invoice, each payment/s will have a due date and a due or expected amount to be paid.

In other words, each payment term line and/or header is a different scheduled payment against an invoice.

The way it works is:

1.  Payment terms must be first properly created and configured as described in this section.
2.  Then payment terms must be linked to each business partner as described in the "Master Data Management // Business Partner" section.
3.  Finally, every time an invoice is booked for that business partner the payment terms setup by default will be applied and therefore used for the creation of the corresponding Invoice "Payment In/Out Plan".  
    A payment in/out plan lists as many scheduled payments against an invoice as due dates configured in the payment term associated with that invoice.

### Header

Payment Term window allows the user to create and configure the payment terms to be linked to the business partners.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/payment-term/payment-term-1.png)

As shown in the screen above a payment term which only has a deferred period such as "100% in 120 days", can be created by entering below data in the payment term header window:

- an **"Offset Month Due"** which is the length of the payment period agreed in months, by example "4" as four months.
- or an **"Overdue Payment Days Rule"** which is also the length of the payment period agreed but in days, by example "120" as one hundred and twenty days.
- **Fixed Due Date** flag allows you to enter a fixed maturity payment date, such as 20th of each month, by example.
- **Next Business Day** flag allows you to set as payment date not exactly the corresponding due date but the next business day, this helps avoid due dates calculation over the weekend.
- **Overdue Payment Day Rule** allows you to enter a fixed payment day.

It is important to remark that in the case of defining a payment term split into more than one deferred period such as "50% in 30 days and 50% in 60 days", the second one (or the latest one in case of more than 2 deferred periods) must be setup in the header not in the lines as shown in the image below:

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/payment-term/payment-term-2.png)

### Translation

Payment Terms can be translated to the language required.

The way to get that is as simple as:

- selecting first the language required
- and then entering the payment term name translated into that language.

### Lines

It is possible to split payment terms into more than just one payment term line.

The information you can enter for each payment term line is:

- **Percentage Due** - or the percentage of the due amount to be paid each time or for each payment term line.
  - Etendo first shows a "100.00 %". That value can always be changed as needed for the lines.
  - Etendo sums up the percentage enter for each payment term line
  - therefore the remaining % up to 100.00%" is the one which will apply to the very last payment term set up in the header.
- **Offset Month Due** - or the length of the deferred period in months
- **Overdue Payment Days Rule** - or the length of the deferred period in days
- **Fixed Due Date** - this one allows you to enter a fixed maturity payment date such as 20th of each month.
- **Payment Method** - you can get that a payment term line uses a specific payment method which would overwrite the overall one used at invoice level.
- **Rest** - this flag implies that the due amount calculated is not the total amount of the invoice but the total amount of the invoice decreased by the previous due amount
  - therefore the very last due amount will just be the remaining amount.
- **Exclude Tax** - if a payment term line is marked as "exclude tax" the corresponding schedule payment will not include taxes.
  - that time the amount due is the \[total net due amount \* percentage due\]
  - those taxes will be taken into account in the very last payment together with the remaining due amount including taxes.
- **Fixed Week Day** - a fixed day of the week can be selected to get that calculated due dates matches exactly that day of the week.
- **Next Business Day** - allows you to set as payment date not exactly the due date but the next business day.
