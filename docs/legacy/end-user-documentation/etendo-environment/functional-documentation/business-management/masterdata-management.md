---
title: Master Data Management
---

## Overview

This section describes the Master Data Management process. One of the steps to take while setting up Etendo is to define the master data to be used across other Etendo application areas.

Master Data Management helps to organize and centralize in a single repository the key data of the organization.

Having a single repository of data avoids data duplication, provides a unique way of data coding and is a key aspect for guaranteeing the coherence and tracking of business processes of any type.

!!! info
    Master data creation is one part of the overall Business Setup flow in Etendo and, as any other setup, it is required prior to entering transactions.

## Business Partner

#### **Introduction**

Business partner master data window is the place where the user can easily organize and centralize business partner data.

Nowadays, organizations deal with many third parties such as customers, suppliers, creditors, etc., therefore it is recommended to _import large number of business partners_ instead of creating them one by one using the Import Data module.

Etendo allows the user to enter business partner master data information whenever it is needed as the business takes place, therefore the procedure described within this section explains how to set up a single business partner of any type.

### **Business Partner**

There are many business partner types such as customers, suppliers and employees you can define and configure.

There is one key field in the business partner header window, which is the "Business Partner Category".

The user should select a category which the business partner is going to belong to.

To learn more about "Business Partner Category", visit the Business Partner Category section.

![](https://lh3.googleusercontent.com/esJo49kYMnRjEA-vGVWUkzbiHYlQDZdE80wtPZiv7opgty2fS8GNWLqzJNiudJzr-Y_iqCBI3CRcfQlY34v5stDNyGFxIHH9US5FY-W0KYxBTx127DgPUaYMluLuyTJZZVqP3mlroJ2XnZSSvw)

The rest of fields at header level are common fields which require to enter basic business partner information such as:

- the **Search Key** or short name which will help you to identify and search a given business partner
- the **Commercial Name**
- the **Fiscal Name,** if known. If it is known, it is the one used in "official" documents such as invoices and tax reports, otherwise the commercial name will be used instead.
- a brief **Description,** if needed
- the business partner **URL,** if known
- a **Reference No** which can be used as an additional way to identify a business partner
- the **Consumption Days** information, which will be used while creating sales or purchase orders for that particular business partner, by using a process named "Copy Lines".  
  To learn more about that process, visit Sales Order and Purchase Order sections.
- and finally "**Credit Line Limit**". Etendo will inform whenever the credit limit entered in this field for the business partner is over while booking sales invoices.

A new check named Consent for Customer Data Processing has been created in the business partner data model, to reflect whether a given contact consents or not that their data can be used by the organization.

It is not the same to enter and configure a customer than a supplier/creditor or an employee, that is the reason why "Business Partner" window has three main tabs and therefore sub-tabs which allow you to set up each main business partner type separately:

- **Customer** tab
  - **Customer Accounting** sub-tab
- **Vendor** tab
  - **Vendor Accounting** sub-tab
- **Employee** tab
  - **Employee Accounting** sub-tab

The tabs and sub-tabs mentioned above are described in the next chapters of this section.

Finally, it is very important to remark that there could be other types of business partners which require to be set up as business partners in this window; business partners which have nothing to do with either a customer, or a supplier/creditor or an employee.

That is the case of banks. Banks need to be created in the business partner window header by just entering basic header information and no data in any of the business partner window tabs, but Location and Contact. The reason for this is that "Bank" type business partners are needed in the "Remittance" financial workflow.

To learn more about this workflow, visit Financial Account.

##### **Set New Currency**

"Set New Currency" process allows the user to change business' partner currency.

Business partner currency is automatically filled in with the currency of the "Price List" assigned to the business partner. Once filled in, it can be changed if required by running "Set New Currency" process.

Normally, business partner currency is the same as the currency of the price list assigned to it. However, it can happen that a business partner having, for instance, an EUR price list assigned, might have USD as its by default currency.

In that case, all the transactions booked in EUR for that business partner, will be exchanged to USD, therefore, the business partner balance is calculated in USD.

Set New Currency process allows defining:

- a new currency for the business partner
- as well as the currency conversion rate to be used to exchange customer balance to the new currency.

![](https://lh3.googleusercontent.com/qMRCmdApUN-s9LYIxySdzxh9-vQezR1tP5kqzLUpO62BELBpiwE71zR3QJW9tn2RbSdVXCj5Po2IAXX5AzeBX4QkyQb6G6ns7jw4UTzPUMEeqUPYjfAjvO4jkMueDO_Ko1855ty312Mk3e2JPQ)

At first, the currency shown in the "Set New Currency" window is business partner price list currency, in our example "USD".

Business partner's new currency can be entered in the field "Currency", for instance "EUR".

Checkbox "Use default conversion rate" uses the conversion rate defined in Conversion Rates window, to recalculate business partner balance from USD to EUR, in our case.

If this check is not selected, a new field "Rate" is shown to allow entering a specific conversion rate.

Additionally, a business partner might have available credit in a given currency.

If that is the case, Etendo informs the user because business partner available credit will have to be exchanged to the new currency, therefore it can be consumed in the new currency.

![](https://lh3.googleusercontent.com/sYcrvJb1PKlU9FPBStEkFIPdTCVTXSXCUte3iY1-kwfVGSiu8Xwux1DvZRxu9tseG0neDLmagLfVpiec4qQaNTLiheq908gynQ9p8Dh7eUOU8MyZ_pGFHICKaAiZwl_5jE0aIHyOfbDb38EVSw)

This process automatically creates three new payments, in case business partner has available credit:

- a _GL Item payment_ in EUR, that moves credit amount to the ledger account defined in the selected "G/L Item", in the CREDIT.
- a _refunded payment_ in EUR, that moves credit amount to a prepayment account in the DEBIT
- and a "Zero" amount payment that is a credit payment in USD (new currency). This credit payment moves the credit amount to a prepayment account in the CREDIT.

Let us take as an example a business partner having a price list in EUR.

- This business partner has a current balance of 306.00 EUR and a generated credit of 100.00 EUR, which decreases its balance to 206.00 EUR.
- After that, "Set New Currency" process is run for this business partner, because its currency needs to change to USD
- "Set New Currency" process informs us that there is available credit for the business partner in the old currency (EUR). That available credit needs to be exchanged to the new currency (USD), therefore a conversion rate needs to be used. In this example, system conversion rate is used, that is 1.13 EUR to USD.
- Once "Set New Currency" process ends, business partner:
  - current balance shown changes to 232.78 USD (206.00 EUR \* 1.13 EUR/USD).
  - currency shown is USD.
  - and three new payments are created, as described above, to exchange available credit into the new currency.
- After that, a new sales invoice is booked for the business partner in EUR, as the business partner price list is in EUR. Sales invoice total gross amount is 41.50 EUR.
- This new sales invoice, once booked, will change business partner balance to 279.68 USD, that is (sales invoice amount 41.50 EUR \* 1.13 EUR to USD) + 232.78 USD.
- After that, a new sales invoice for an amount of 100.00 USD is booked for the business partner. While completing this new sales invoice, a new window appears showing business partner USD credit available, in our case 100 EUR \* 1.13 EUR to USD = 113.00 USD.

![](https://lh4.googleusercontent.com/fAiMfanae3I2XAvLdbf3yFYkZhAbN8Me-A2kv3uSF62Q3HaBTz9wyfXBL-22RDXeKgdrNxTLeLDnECldDFwjhkEG-m4Uzgc-JNUrtasuWPvrKKGeTmlRg-Lrc9wqtQDG17R-trrmm8EbG70bgg)

### **Customer**

!!! info
    Customer related data can be entered and configured once the "Customer" checkbox is enabled.

![](/docs.etendo.software/assets/drive/1gybs8XJw1B6pJZRr-mzWO9fEUm6ylwFr.png)

As shown in the image above, there is a list of relevant data to be entered for customers together with current _customer balance_ information:

You could either select any data such as "Price List" from a previously created list of values, or create it "ad hoc" by navigating to the corresponding window, and then select it.

- **Price List** - the one selected will be the one applied while creating sales documents such as sales orders or sales invoices for that customer.  
  To learn more, visit Price List.  
  Price lists are defined in a given currency, which could be the same as customer currency or not.  
  In case it is not, customer balance will be calculated by taking into account either the conversion rate defined in the Conversion Rates window or the one entered in the process "**Set New Currency**" which can be run to change the currency of a business partner.
- **Payment method** - the one selected will be the one applied while creating and managing the payments received from that customer.  
  If a Financial Account is linked to the customer, the payment method to select here will be one of the payment methods linked to the financial account.  
  To learn more, visit Payment Method.
- **Payment Terms** - the one selected will be the one used while managing sales invoices payment plan.  
  To learn more, visit Payment Term
- **Financial account** - the one selected will be the one use while collecting and reconciling the payments made by that customer.  
  To learn more about "Financial Account", visit Financial Account
- **Invoice terms** - there are few invoice terms which can be used while generating sales invoices.  
  To learn more, visit Generate Invoices
  - **After Order Delivered** - the invoice could be automatically generated once all the goods of the sales order have been shipped
  - **After Delivery** - the goods of the sales order will be automatically invoiced as they are shipped, even if there are partial shipments
  - **Do not invoice** - no invoice will be generated automatically
  - **Immediate** - the invoice will be generated on the next run of the Generate Invoices process.
  - **Customer Schedule after Delivery** - the invoice will be generated according to the calendar agreed with the customer and once the goods ordered have been shipped.  
    If this is the option selected, a new field named "Invoice Schedule" is automatically displayed for you to select the corresponding "Invoice Schedule" or calendar.  
    To learn more, visit Invoice Schedule
- **Credit Line limit** - If the sum of all pending payments is over the credit limit specified for a customer, the system will alert you by saying that this customer has reached the credit limit whenever this business partner is selected in a sales document (order, shipment or invoice).
- A customer can be defined as "Tax Exempt" whenever applicable, therefore only those Tax rates also defined as exempt apply.
- **Sales Representative** - you can select here a customer sales representative. A sales representative is an employee set as such.
- **SO BP Tax Category** - this field can be found under the "More Information" section.  
  You can use a business partner tax category to get that the sales documents created for a customer can only have a specific set of tax rates linked to that tax category.  
  To learn more, visit Business Partner Tax Category
- **On Hold** - this checkbox allows blocking a customer, therefore some specific documents cannot be fulfilled for it. If checked, the On Hold section is shown with the following setup, which can obviously be changed as required:
  - **Sales Order:** Blocked
  - **Goods Shipment:** Blocked
  - **Sales invoice:** Blocked
  - **Payment In:** Not blocked

Above defaulted configuration means that it is not possible to complete either a sales order, a goods shipment or a sales invoice for the customer but to receive a payment.

### **Customer Accounting**

Customer accounting tab allows the user to configure the ledger accounts to be used while posting customer related transactions such as customer receivables and customer advances to the general ledger.

![](https://lh4.googleusercontent.com/609fyigYTKbQyThG3K-Cd8GKw2Z-Y_02gsIaYELEwALpv3XCRgCgWeEXZqKvgYrhJWv1xDKvQ9zOTYRiF_ozw9D3xjh6OQIUt2vl1V17dfi8bHY2GoKLs7aXuZXVv3FALP8lA3Mqh6LFdfskaQ)

As shown in the screen above, you can configure for each customer and general ledger the accounts to be used in:

- the **Customer Receivables** transactions such as sales invoices posting.  
  To learn more, visit Sales Invoice
- the **Customer Prepayment** transactions, such as those cases when the company shipping the goods requires the customer to advance part or full amount of the debt.  
  To learn more, visit Customer Pre-payments

At first, these accounts are inherited from the Defaults accounts of the organization's general ledger for which the business partner is being created. The end-user can always change them.

Besides, it is important to remark that it is possible to configure the creation of new correlative accounts for the business partners as described in the General Ledgers tab of the Organization window.

### **Vendor/Creditor**

Vendor or Creditor related data can be entered and configured once the "Vendor" checkbox is enabled.

![](https://lh4.googleusercontent.com/ZyKWCq0lO9Z1oggC86Qw1sYw6EACIoC7WNSXCgMczxoJFp9uppOasgk0YlwMWVjxCBSHouebT0uSxObUKBBd9A0TwRj-957-_D37S4p3-xrOMZlqI33LOXr18EDJBwBI0Z36Hxp0hmgQ4tcp-g)

As shown in the image above, there is a list of relevant data to be entered for suppliers or creditors, also known as vendors:

- **Purchase Price List** - the one selected will be the one applied while creating purchase documents such as purchase orders or invoices for that vendor.  
  If a Business Partner has already generated Credit, it will not be possible to select a Price List in a different Currency from the generated Credit. In that case, it is possible to convert Credit to a different Currency.  
  To learn more, visit Price List.
- **Payment method** - the one selected will be the one applied while creating and managing the payments made to that vendor.  
  If a financial account is linked to the vendor, the payment method to select will be a payment method linked to that financial account.  
  To learn more, visit Payment Method
- **Payment Terms** - the one selected will be the one used while managing supplier invoices payment plans.  
  To learn more, visit Payment Term
- **PO Maturity Date 1** - as indicated in the Payment Term the PO Maturity Date is used in combination with the Fixed Due Date in the payment term to be set to Y and the Next Business Day set to N. The due date of the payment is based on the payment term defined in combination with the PO Maturity Date.
  - For example, the defined payment term is 30 days and the PO Maturity Date 1 is set to 10. If the invoice date is the 1st of the month, based on the 30 days payment term, the payment due date is the 1st of the next month, but since the PO Maturity Date is set to 10, the payment due date as a result is the 10th of next month.
- **PO Maturity Date 2** - a second PO Maturity Date can be set to be combined with the payment term and the first PO Maturity Date.
  - For example, the payment term is 30 days, the PO Maturity Date 1 the value is 10, the PO Maturity Date 2 is 20. The example given in PO Maturity Date 1 will remain the same. However, if the invoice date is the 11th of the month, the payment due date will be the 20th of next month: the 30 days of the payment terms are taken into account and since the 10th of the month is passed the second maturity date of the 20th is taken into account.
- **PO Maturity Date 3** - a third PO Maturity Date can be set to be combined with the payment term and the first and second PO Maturity Date.
- **Financial account** - the one selected will be the one used while withdrawing and reconciling the payments made to a supplier.  
  To learn more, visit Financial Account
- **Tax Category** - you can use a business partner tax category to get that the purchase documents registered from a vendor can only have a specific set of tax rates linked to that tax category.  
  To learn more, visit Tax Category
- **On Hold** - this checkbox allows blocking a vendor, therefore some specific documents cannot be fulfilled for it. If checked, the On Hold section is shown with the following setup which can obviously be changed as required:
  - **Purchase Order:** Blocked
  - **Goods Receipt:** Not blocked
  - **Purchase Invoice:** Blocked
  - **Payment Out:** Blocked

Above defaulted configuration means that it is not possible to complete either a purchase order, a purchase invoice or to make a payment but to receive goods sent by the vendor.

As already mentioned if a business partner of any type is blocked it is not possible to Complete (or book) some document types however it is always possible to Void them.

You will realize that Etendo shows an error message stating that it is not possible to complete a document for a business partner set as "on hold".

#### **Vendor Accounting**

Vendor accounting tab allows the user  to configure the ledger accounts to be used while posting vendor related transactions such as vendor liabilities and vendor advance payments to the general ledger.

![](https://lh3.googleusercontent.com/9Z371emBdqUmHgSvKroREH9tZsP4bV-9Eh6T9I-DOkp9x8n4iCFvpI_wOp3copFLr0lNnuogVezfXzQuQV4U6cukoVQJ6oYp1GLt3oxL-iE1TU1LhXIC0rghK_ctPI89l3Lg0u9Shcbj4Q8Aiw)

The user can configure for each supplier or creditor and available accounting schema, the ledger accounts to be used in:

- the **Vendor Liability** transactions such as purchase invoices posting.  
  To learn more, visit Purchase Invoice
- the **Vendor Prepayment** transactions such as those cases when the supplier of the goods requires the company to pay in advance part or full amount of the debt.  
  To learn more, visit Vendor Prepayments

At first, these accounts are inherited from the Defaults accounts of the Accounting Schema assigned to the Organization for which the business partner is being created. The end-user can always change them.

Besides, it is important to remark that it is possible to configure the creation of new correlative accounts for the business partners being created as described in the Org Schema tab of the Organization window.

### **Employee**

A business partner can be set up as employee once the checkbox "Employee" is enabled.

![](/docs.etendo.software/assets/drive/1cmnf61sr6kJcPLISrzVR8kzSbcw5Pugv.png)

Employee tab allows the user to set which of your business partners are "Employees".

An employee can be:

- appointed as **sales representative** of a customer
- defined as the **responsible of a company project/s**.  
  To learn more, visit Projects and Services Management
- allocated to a **production process** as a resource.  
  To learn more, visit Production Management
- and can **issue expense's sheets** as part of his/her involvement in a company project.  
  To learn more, visit Expense Sheet

#### **Employee Accounting**

The ledger accounts to be used while posting employee related transactions such as paryroll accounting could be added in this tab.

![](https://lh3.googleusercontent.com/7kuCcxhGxEGWIpNYq-d8j3hysWa9ru8o2SoKJnxq9Cvkf3G-j1W0M5KDMw4Wq7IiNtKftE3U8GFbFZYUHDBompw3guyv-yamRyKg6-gUoNb1wibWRp0AAj1KQg3S1FGeiPmyyIJnUJOBSE4WQw)

As you can see in the image above, nowadays there is no ledger account required to be defined for employee accounting. This is due to the fact that there is no transaction susceptible of being posted for employees.

Anyway, this is the place where "Human Resources" related modules or features should point to while defining the accounts to be used in any employee transaction susceptible of being posted.

### **Bank Account**

Bank account tab allows the user to list and set up business partner bank accounts.

It is possible to configure and properly set up business partner bank accounts to be used while making or receiving business partner payments of any type.

Therefore, we strongly recommend the user to properly set up bank accounts as those will be used by Etendo as required within Etendo payment management processes.

![](https://lh4.googleusercontent.com/XzJTDeFWNJTAq361dyKR7owq_NSU41d06F7NgoVmM6MLjHaSxUc-M2q19MuXNkz90__zk-C6KFFYTIWyuh_D8d5KzJ9R1rGraYBU_y1LJj3uczO0V5DLgUtLQbqitNkiC_E8_Iyp89-X8EnhoA)

The "bank account" related data you can enter is:

- the **Bank Name**
- **Active** flag - We recommend you to set as "Active" only one bank account, if possible, in order to avoid errors; otherwise you should keep an eye on the right bank account used.
- **Country** - you can select a country from the list to specify if the bank account is a domestic bank account or a foreign bank account.
- **User/Contact** - in case you want to associate a contact for this bank account
- **Bank Account Format** - List that contains all the possible values for generating the Displayed Account Number, which will be later on used by other reports or processes to get the account identifier. Possible values are: _Use Generic Account No._, _Use IBAN_ or _Use SWIFT + Generic Account No._ Note: _Other options can be added by other modules that extend the supported Bank Account Format_.
- **Generic Account No** - a generic account number to identify the bank account can be introduced here. This field must be mandatory filled in case either _Use Generic Account No._ or _Use SWIFT + Generic Account No._ is selected at the Bank Account Format field.
- **IBAN** - The International Bank Account Number (IBAN) is an international standard for numbering bank accounts.  
  The IBAN consists of a two letter ISO 3166-1 country code, followed by two check digits, and up to thirty alphanumeric characters for the domestic bank account number, called the BBAN (Basic Bank Account Number). This field must be mandatory filled in case _Use IBAN_ is selected at the Bank Account Format field. The IBAN code will be automatically validated when inserting/updating the record taking into account the rules for the country bank defined.
- **SWIFT Code** - Corresponds to the ISO 9362 international bank code identifier. It must be mandatory filled in case _Use SWIFT + Generic Account No._ is selected at the Bank Account Format field.
- **Displayed Account**: It is automatically generated based on the value selected into the Bank Account Format. This field is read only, and it is used by other reports or processes.

#### Advanced Remittance

!!! info
    To be able to include this functionality, the Advanced Remittance module of the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}.

If the Advanced Remittance module is installed, in this tab, the user can find a “default” checkbox that, if checked, indicates that the selected bank account is the default one, instead of the other options the business partner can have. This means that if the bank account field is not manually populated, Etendo automatically fills the field with the default bank account.

![bank_account_default.png](/docs.etendo.software/assets/legacy/bank_account_default.png)

> **Important**:
> -If no bank account is selected as default, the one created last is used when no bank account is selected in orders/invoices.
!!! warning
    -Only one bank account can be selected as default for each business partner.

### **Location/Address**

Business partner locations and full address details can be set up in this tab.

Business partners might have different address details depending on location/address used for either "Goods Receipts/Shipments" purposes or location/address used for "Invoices" purposes.

![](https://lh4.googleusercontent.com/ZC4Jc3vlmJB6aVN4fG94bMjafw4pv7IYzCE40ZEhZxA0JPkN2AwFK942M4o-fXhEliP9jHCKO_WSdNBNY8NWi6MyqLM00BmX2YsjHjUPs8B3SNg2UfGAAQETAczHpvwV-Ng93qjIvj3X2zVtyA)

Etendo allows the user to define any type of business partner address, by filling in the information below:

- **Location/Address** - if you click in this field the location selector box opens, there you can enter the information below:
  - the **address 1st line**
  - the **address 2nd line**, if needed
  - the **Postal Code**
  - the **City**
  - the **Country** - you can select one from the list, if any
  - the **Region** - once the country is selected, you can select one region of the country selected, from the list, if any.
    - Once the location entered is saved, it's listed in the "Location" window. To learn more, visit Location
- the **Phone** number
- an **Alternative Phone** number, if any
- the address **Name** - this field is automatically filled in by Etendo, once the location / Address information has been configured. The user could change it as needed.
- the **Fax** number
- **Ship to Address** checkbox - the user should flag this one if the address being set up must be used for Goods Receipts/Shipments related transactions.
- **Invoice to Address** checkbox - the user should flag this one if the address being setup must be used for sales or purchase invoices transactions.

### **Contact**

Contact tab allows the user to add and configure the business partner contacts you deal with.

![](https://lh6.googleusercontent.com/Hy8AxFtV7E5iAuum7OaH5J2uRp3T6WeI-AjoxfZQKr0R1VyPJ-Br_PvqEJZ3ps8HuwJDDlFJZW6s1P4_h-U36j583nFJR86R3Qu7DqqaPcOl_8AgjtZAR2iCq_FHNt_HMFc3cqhF2l2Y1YLBUg)

As you can see in the image above, basic "Contact" data such as:

- **First and Last Name** of the contact
- as well as his/her **Position** in the business partner

can be configured in this tab.

### **Basic Discount**

Basic Discount tab allows the user to add and configure business partner Basic Discounts.

![](https://lh5.googleusercontent.com/2xUfGNVKL2MuKaMd8-0-MAdpaJiPFnOlExD6jrfVaicmThNDW7WV_C3Ve31HTwTENiUJ2TxGKnDRm9__SGlVoDralznQ9o0EfTxYl4xIKcTOhQpRU_pkeP1a-g_jrvcixL2FvJsM-MwK0_2EQQ)

It is possible to enter as many **Discounts** as agreed with your business partners, by filling in the information below:

- the **Discount** to be applied while creating sales / purchase transactions for that business partner can be selected from the list (if any) or created by navigating to the **Discount** window.
- **Customer:** this checkbox must be selected if the discount is going to be applied to a Business Partner set as "Customer"
- **Vendor:** this checkbox must be selected if the discount is going to be applied to a Business Partner set as "Vendor"
- **Apply in Order:** this check box must be selected in case the discount can be applied in sales or purchase orders as applicable.
- **Cascade** calculation of the discount. For instance, if first discount is 10% and second one is 5%, a cascade calculation of the total discount won’t be 15% but 14.5%

A discount not applied in Cascade means that it affects the full quantity of the Document Line. A Discount applied in Cascade means that affects the quantity of the Document Line that remains after applying all the discounts that come before it.

An example to explain the difference between a Cascade and not Cascade Discount is the following one:

Three Discounts, each one of 10%, the first two ones are defined as not Cascade and the third one as Cascade. Over an Invoice Line of 1.000 USD

- The first discount will create a line of -100 USD (10% of 1.000 USD)
- The second discount will also create a line of -100 USD (10% of 1.000 USD)
- The third one, however, will create a discount based on applying the previous discounts on cascade, so:
  - 1.000 USD - 10% = 900 USD (applying the 1st discount on Cascade)
  - 900 USD - 10% = 810 USD (applying the 2nd discount on Cascade)
  - 10% of 810 USD = 81 USD. So the third discount will be -81 USD.

In total -100 -100 -81 = -281 USD for all three discounts (a total discount of 28.1%)

### Advanced Business Partner

!!! info
    To be able to include this functionality, the Essentials Bundle must be installed. To do that, follow the instructions from the [Marketplace](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="\_blank"}.

The “Advanced Business Partner” module allows the user to have a general view of business partners information and to assign sequence numbers to business partners.

#### Business Partner General View

In this window, it is possible to see all the business partner information of each record, grouped in the customer, vendor/creditor and employee sections of the header. In the original window “Business Partner”, this information is found in different tabs.

![image_3.png](/docs.etendo.software/assets/legacy/image_3.png)

This change implies, in grid view, the user is able to create, modify and filter business partner information according to their needs.

![image_4.png](/docs.etendo.software/assets/legacy/image_4.png)

#### Sequence Number by Business Partner Category

In this window, it is also possible to create a sequence number for each business partner based on its category. This sequence number can be found in the Document No. field.

![image_5.png](/docs.etendo.software/assets/legacy/image_5.png)

For this, you have to set some preferences and configure the sequence number first, as explained below.

#### Preferences

To be able to configure a business partner sequence number, two preferences are set by default. These can be found in the “Preference” window.

##### Auto Business Partner Document No

![image_6.png](/docs.etendo.software/assets/legacy/image_6.png)

This property allows the automatic generation of sequence numbers for business partners. The default value is Y and, in case it is necessary to disable this automatic generation, a new preference must be created, but with the value N and the option “Selected” checked. In this case, the Document No field will be left blank.

##### Allow Jumps in Business Partner Document No

![image_1.png](/docs.etendo.software/assets/legacy/image_1.png)

This property allows jumping among the different document numbers. The default value is N, so, it is not allowed to remove business partners or change business partner categories. However, it is possible to create a new preference with value Y to enable this option. When the business partner category is changed, the document number is also changed according to the corresponding document sequence.

#### How to Configure Sequences Number

To configure the Sequence Number, go to the “Document Sequence” window, create a new record for each organization and category, set the corresponding table, column and business partner category, and save the record. The table and column fields must be filled with the options seen below.

![image_2.png](/docs.etendo.software/assets/legacy/image_2.png)

!!! info
    For more information, visit [Sequences](https://docs.etendo.software/en/technical-documentation/etendo-environment/platform/sequences).

### Advanced Rappels

!!! info
    To be able to include this functionality, the Advanced Rappels module of the Sales Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36).

With this functionality, the user can find the tab “Rappel Configurations” in the business partners included in the Rappel configurations. Also, in the Business Partner window, the user is able to create rappels using the button “Create Rappel”.

![bp_window.png](/docs.etendo.software/assets/legacy/bp_window.png)

To be able to do this, it is necessary to configure certain aspects in the “Rappel Configurations” window.

!!! info
    For more information, visit [Rappel Configurations](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/masterdata-management#rappel-configurations).

#### Rappel Configuration Tab

The “Rappel configuration” tab can be found in the tabs section of the Business Partner window. In this tab, the user can find the configured rappels for each business partner.

To create a new rappel, the user must select one of the available configurations in this tab and click the **"Create Rebate"** button. A pop-up window will appear in which the user can select a trading partner to which the Rappel will be assigned, and also configure a date period in which the consumptions will be taken into account to calculate the discounts, determined by the "date from" and the "date to" information.

![bp_pop_up_new.png](/docs.etendo.software/assets/legacy/bp_pop_up_new.png)

When the rappel is created, a [sales invoice](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/masterdata-management#sales-invoice) is created automatically, as seen below.

![created_rappel.png](/docs.etendo.software/assets/legacy/created_rappel.png)

#### Sales Invoice

Each time a rappel is granted to a business partner, a new sales invoice is automatically generated in order to show the amount of the discount. This invoice has a specific sequence to distinguish it from the rest, according to the options entered when configuring the sequence, and a negative amount since it is a discount. The status of this invoice is “draft”.

!!! info
    For more information, visit [Sales Invoice](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/sales-management#advanced-rappels).

## Business Partner Info

#### **Introduction**

In this section, the user can view information related to business partner orders, receipts/shipments, invoices, and assets.

### **Partner Selection**

The user can select a business partner to begin viewing related transactions.

![](https://lh3.googleusercontent.com/4OnjuhWdUoTUGTSu8zWxiV2-AAuj2bKugSYsd0tnIK9CgAS12oX62u4KgxFW35THxZKqIH0Epr-E-q5w4w4y4kbkWR3wCKNTQFosue5bPRC3CMXbOgCNgkzsvXCtZ7OsB53ZD69KhpH-BmTZbQ)

#### **Partner Orders**

The user can view orders related to a specific business partner.

![](https://lh6.googleusercontent.com/pwcD_Hw4nDDMhW7FDa69spb3uNGrBrfB8AwS8Ni77RyIi6_uPAsIWmWPzkvPoCBe5IIcW_GeFmxgvB4KPxoI6TmwiK2nAsFyOKd7GvbMXzpAyt2DwTPDnyKijbLgejiWZYCnj28D9-y9hZNuDw)

### **Partner Shipments**

The user can view shipments related to a specific business partner.

![](https://lh5.googleusercontent.com/DKEnqi6tY-_9PGf13-ntaqJCDwbfHlm8mJl2k4WwaIJ8dZibpai1E-LZhuf8DkUS4dSX2sm5eua0uzGLLdXreV-YW1KnyHvSI1zWRcJDHEjh0DJVslYgN3RBEuTiqjK0g5qpe02UP8ZUf24qyw)

### **Partner Invoices**

The user can view invoices related to a specific business partner.

![](https://lh6.googleusercontent.com/GVk5WiJ9CXXVM8khajRov6_24IGCsm0l8nD6ARDMyUL6Os5gle_r3LDHUsq1i-2lAXyf5aZRlgxep-kCgSGkbjMCoGNKVMCDwp-R5Z2pK1-5VYxgk4bswYEc4tcJ_iZGuh5Toi2DcEQIWz9Lsw)

## Currency Converters

In the Currency Converters window, the necessary Apilayer data has to be configured with the following information:

- Classname: com.smf.currency.apiconfig.CurrencyLayerConverter
- URL: http://apilayer.net/api/
- Token
- User
- Password

![](/docs.etendo.software/assets/drive/1L7bYs_0DYQCfU6cu-cbssJ1AwjTXtE1a.png)

## Product

#### **Introduction**

Product master data window is the place where you can easily organize and centralize the key data of the items of any type you might manage as part of the organization processes and/or activities.

Organizations deal with a variety of different items that may be required by an organization for the performance of its daily activities.

It is possible to load Product information into Etendo en masse using the Import Data module, or one by one using the Product window.

This section describes how to set up Products individually.

#### **Product**

Product window allows the creation of items such as products, raw materials, resources, services, etc.

The information required to create a Product in Etendo is determined by the nature of the Product, its Product Type.

There are four product types available:

- **Item**. The most frequently used product type is "Item". Inventory held for resale, materials that are placed into a production process, and semifinished or finished goods created through production are examples of products defined using the product type "Item".
  - An item should be flagged as "**Stocked**", if quantity tracking is required for the item, otherwise there is no need to flag the item as "Stocked".
  - An item should be flagged as "**Production**", if the item is used in manufacturing.
  - If an item is an intermediate or finished good, its bill of material (BOM) should be detailed on the Bill of Materials tab.
- **Service**. This product type is used to identify such provisions as professional services, transportation, telephony, and other items which do not correspond with material goods.
  - Therefore, a Service is not stockable but can be purchased or sold.
  - A service can have a bill of materials to be defined in the Bill of Materials tab.
- **Resource** and **Expense**. These product types can be used to distinguish between different types of products which can be purchased or sold but cannot be stocked.
  - Resource type can be used to configure resources such as Financial, Legal or Natural resources used by the organization.
  - Expense type can be used to configure expenses such as travel expenses to be used while reporting Employee expenses.

Product types do not confer different accounting treatments. In other words, all product types account the same way while being purchased, stocked or sold.

All of them use the ledger accounts defined in the Accounting tab of the Product window.

![](https://lh5.googleusercontent.com/BP3_HION2Ye59yb2o2KNzsNK4o72pdd_v6DVNj5SsrL_3bZCZbH-OG4Snsia_DB_BItoQaJxuJf4vOe1jlrwPhZTswRuf1I8aUTCLlHP1s-NU-625ScthOFj8fgeIrknNz2MdE6kbDgecxTFSw)

Additional key data to fill in are:

- **UOM**, that is the unit of measure to be used while purchasing, storing and selling a product, for instance "Units".  
  A product can also have alternative UOM besides product's UOM.
- **Product Category**, it is mandatory to select a product category to which the product is going to belong to.  
  To learn more, visit Product Category
- **Tax Category**, this category is key for managing the taxes related to the product. Taxes such as VAT depends on the type of product.  
  To learn more, visit Tax Category
- **Purchase** checkbox can be selected to indicate that the product can be purchased to an external supplier. This checkbox is mainly an informative one, as it does not add any business logic behind but regarding MRP.  
  In that case, if selected, MRP will then purchase the product if needed, otherwise it will produce it.
- **Sales** checkbox can be selected to indicate that the product is sold or can be sold to an external parties or customers. This checkbox is an informative one, as it does not add any business logic behind.
- **Stocked** checkbox is selected if the product is part of the inventory, therefore proper inventory movement transactions are registered in Etendo.  
  This flag can not be changed anymore for a product, if that product is part of any sales, purchase, inventory or production document related, whatever document status is.
- **Production** checkbox is selected if the product is part of a production process. Once selected, an additional field appears to select a "Process Plan".  
  To learn more, visit [Process Plan](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/production-management-setup#process-plan)
- **Attribute Set**, a product can have a group of features or an attribute set, such as "**Color and Size**", to take into account while ordering or storing the product.
  - If an Attribute Set is selected here, Etendo displays a new field named "Attribute Set Value".  
    To learn more, visit Attribute Set
- **Attribute Set Value**, if an Attribute Set value such as "Blue and Large" is selected, Etendo displays a new field named "Use Attribute Set Value As".
- **Attribute Set Value As**, once an attribute set has been selected, that one could be used as described below depending on the criteria selected in this field:
  - **Default**: This means that the attribute set value defined will be defaulted in each of the transactions, but it is allowed to be changed.  
    In other words, the user will not have to care about setting it each time when creating transactions such as goods receipts and shipments.
    - For instance, it can be set to default the value of the attribute set Size of a product to Medium (because it is the most commonly used).  
      This way, each time that that product is selected, its attribute set value will be set to Medium (unless selected from stock, in which case the attribute set value is set to the value in which the product is stored).  
      It is possible to overwrite this attribute set value, to Small or Large for example.
  - **Overwrite Specification**: This means that the attribute set value will specify completely the product nevertheless, the attribute set value can be changed for this product.
    - For instance, product Alcohol Free Beer is given the attribute set Alcoholic Proof and the attribute set value 0% in the Product window. This definition specifies completely the product: the Alcohol Free Beer is supposed to have a 0% alcoholic proof. But, in the production process, some deviations can happen, and this alcoholic proof can go to 0.01%. Using Overwrite Specification option, the production manager will be allowed to register this deviation in the Production process for Alcohol Free Beer product.
  - **Specification**: This means that the attribute set value will specify completely the product. The attribute set value will always have this value and no other value will be allowed for it.
    - For instance, product Large Blue Jeans is given the attribute set Size & Color with values Large and Blue. This defines the product and will not change. Transactions are done and completed with this product, without forcing to re-set the attribute set value. User can then query all products having Large size or Blue color without having to query the transactions but only the product definition.  
      To learn more about attributes, visit How to Manage Attributes and Attribute Sets article.
- **UPC/EAN**, used to store bar-code information
- **Bill of Materials** checkbox is selected when the product is a bundle of other products as listed in the Bill of Materials tab.
- **Deferred Revenue**: this flag is visible only for products having the Sale flag checked and indicates that _by default_, revenues for sales of this product need to be deferred. When this flag is checked, the Revenue Plan field group becomes visible, allowing users to configure the next two fields.
  - **Revenue Plan Type**: this field specifies the default frequency of the revenue distribution. At the moment, only monthly revenue plans are supported.
  - **Period Number**: this field specifies the default duration of a revenue plan. For example, an annual subscription to a magazine will be defined with a revenue plan of 12 monthly periods, while a season ski pass will have revenue plan of 5 monthly periods.
  - **Default Period**: this field specifies the first period in which revenue is going to be recognized. The options available are:
    - _Current Month_. This option will set the Revenue Plan Starting Period to the same period as the invoice accounting period.
    - _Next Month_. This option will set the Revenue Plan Starting Period to the invoice accounting next period.
    - _Manual_. This option will not set any revenue plan starting period, therefore a starting period can be selected while creating the sales invoice line.
- **Deferred Expense**: this flag is visible only for products having the Purchase flag checked and indicates that _by default_, revenues for sales of this product need to be deferred. When this flag is checked, the Expense Plan field group becomes visible, allowing users to configure the next two fields.
  - **Expense Plan Type**: this field specifies the default frequency of the expense distribution. At the moment, only monthly expense plans are supported.
  - **Period Number**: this field specifies the default duration of an expense plan.
  - **Default Period**: this field specifies the first period in which expense is going to be recognized. The options available are:
    - _Current Month_. This option will set the Expense Plan Starting Period to the same period as the invoice accounting period.
    - _Next Month_. This option will set the Expense Plan Starting Period to the invoice accounting next period.
    - _Manual_. This option will not set any expense plan starting period, therefore a starting period can be selected while creating the purchase invoice line.

These values are used when an invoice is created for a product having an expense plan and/or a revenue plan.

In the same way, these values are also used when an invoice is created from another document (for example: the Generated Invoices process that creates invoices from sales orders). In the same way, these values can be modified on a transaction by transaction basis.

To learn more, visit the How to manage deferred revenue and expenses article.

- **Book Using Purchase Order Price**: This flag is used when posting a Goods Receipt or a Matched Invoice document to the ledger.  
  Normally, the product cost is used while posting those transactions, however this checkbox allows using the product purchase price instead.  
  This feature only works for "Expense" product type not having the "Sales" checkbox selected.

!!! info
    Notice that in this case a Purchase Order needs to be related to the Goods Receipt, otherwise an error message will be shown as the purchase product price is required.

- **Returnable**:This flag is used to indicate if a product can be returned and, in the case that it is, a new field called. When trying to return a non-returnable product from the Return from Customer window, an error will be shown.

![](https://lh5.googleusercontent.com/8P_B_7zs64s6GpnSTeK9UQ6lBzvVnqGD9qOV3QR0WnAk_vPEZtjWJclvPzCvLx2HhU2oJuV4AjbxdhmspKkr3cWr20QacqX-VnigfqEjCIv9_blgPk1mEIloiZOBk5oCT6y41jQh9JI7HKA5vQ)

- **Overdue Return Days**:In this field, it is possible to configure the maximum amount of days before a product can not be returned. If the field is left blank, the product can be returned without time limitations. When trying to return a product whose period has expired, a warning message will appear.

![](https://lh5.googleusercontent.com/QyvN8QXk9YDUur102n0wpiAY2QPyWux7iOpGMyvUkSVWGsoatyBdBBoMx5sxfWxo7dLX--2yo9cchrXV5yDH9nwpLqtOKLW9bsm4j0XFN9rCTCuusTntdbtxsRzu9Pu5pUinLOQ17lH_GAOymA)

!!! info
    **Note**: If stocked is not checked and BOM is checked, the product price should be 0. Because in that special case, the product price is the sum of the prices of the bill of materials components it consists of. If promotion wanted to create, 'Discounts and Promotions' should be used.

##### **Variants**

Product can be marked as **Is Generic**. This means that variants of this product will be created based on some characteristics such as colour, size, etc. The definition of these characteristics takes place in the generic product, so it can be said that a generic product is like a template where new variants will inherit all the attributes (taxes, prices, image) of this product. Due to this, a generic product cannot be used for transactions but its variants.

!!! info
    Note:Products that are marked as generic cannot be used in transactions operations such as sales orders, purchase orders, goods receipts, etc.

When this flag is marked, two buttons are shown:

![](https://lh5.googleusercontent.com/XpdGDkmZecBZmb-qxyiA42-f6IdA9oTfYqig24hQZtSRsKLgItWO3U5jf-8kuTgHlMfKrUU9BQBSPfay8YoWSPKaYr74W9TXIgzumMG6T2sjq1g1w7zA9N2e2xZHPlGCykvLXWfU-wyAyH_5cw)

- It shows all variants that have been created or not for that specific generic product. It is very useful when:
  - The user does not want to generate all variants but just some of them. The button allows the user to select the possible combinations
  - The user adds one more value, for example, red when having before green and white and the variants were already created in the past. It will show the new combinations

For example, imagine generic product T-Shirt Model A has the characteristics:

- Color: Blue, White
- Size: S,M,L

But still variants have not been created. If you press the button, you can see all possible combinations:

![](https://lh4.googleusercontent.com/YysrJ-lndKNj6qUEzE5IIaNziDxMduILgMa9XP3Vde2NskD-oIug-d3Ce12C4gZSJCDuqDqyXcTXL0IPRSEkRP3ezOIsF321Zy1pizzXHcUKuWlzNUPivH7sfIyDZhFxOcZUzCprjCYdNRs3Ag)

Then all combinations can be selected or just pick some of them. Once the selection takes place pressing Done, combinations will be created as Products. These new products will have the Generic Product field filled with the product that was marked as generic. We can say it is their parent product

![](https://lh4.googleusercontent.com/1aZDzwrJXxLjUZhwgGhhHarCA-AsNLDbdSpLvVj2LzAvReay3gMmfC33auIHYoELn1pSKNSYrBWIckgesfl75Lza6jjZVMfXeNw1236dsTpVUMp0Aqmm19kJjAzp0ZRElYQc4F9iujwJ1X-P0A)

- It creates/explode all product variants, that is, all combinations based on the characteristics defined

Another button that might appear is ![](https://lh6.googleusercontent.com/ZBo4NfiZAG6XK2iCAGS7jK--_4wffCzZHmp5z-8S0KrHU0Qs1U2_HkeL6MWD6KRZAFaYzjui8tmsOW9NKMbp3OkOLM27pUoQXBMC0YcHdCSLzQojA3Twi5IWuQwHEAcwlmjD4bnRYlMJ915Gpg). It only shows up when the generic product or the new product variant has a non-variant characteristic related. Two scenarios:

1.  **Generic product**: This button allows entering the value of that characteristic.  
    Imagine the characteristic is Fashion Line that has three values: Sport, Vintage, Classic.  
    Unlike the characteristics that are variants users cannot enter the value through the Characteristic Configuration tab
2.  **Variant Product**: This button allows the user to enter/update the characteristic that is not variant.

Once a variant has been created, its characteristics and values can be viewed either in the grid or in form view:

- Grid view: There is a new column **Characteristic Description**. This column is calculated and is not editable. It shows the characteristics with their values as a text. This column has a new search-selector in order to find product variants based on its characteristics

![](https://lh3.googleusercontent.com/uxKcLraqzQTO5YQDc1QPoXzbekSyMuKoCGy0FpkRmreW9hbxKJOcZm-4R2kHVRAf7h-VaVYDoMlqncOk-iCWOZv5d7Nyo6OJIjsJXdlA1e276uJ2iD7YbUTpyY3R8BMUphQJGPqHG9z8Q3oCRw)

Press the button ![](https://lh4.googleusercontent.com/XY6pNhuZ1_Zz62KSiGF0yVwR7duvGEGLzXb-sj8RZ0wfgcF2VLemqd37yK-hJshznCtz8tSACOFULk0CQo4f4CVrbR2W8-8CaBBUOtxsLXq2rnyATymb5aOTZaihm1mdEJEopKzbefJYQnNLrA) and it opens a pop-up to select values:

![](https://lh6.googleusercontent.com/Wtk1v4OXf3cYQZQRJVMZZu6bvKWAF94yM7GMeugxV3zLYTJez8HaVSdzgIFurmZ4Y_-kCpYQnv58HewpHMGgyqom8Xtn30PLliwlV8zGlfmMmqPg0yqLfFhLLvB7Mij9Ro9gs7SY4lz-zqhJXg)

- Form view: Product variants have a new section named _Characteristic Description_. This section contains as many fields as different characteristics the product has.

There is a preference **Show Product Characteristics Parents**: Values can be 1,2,3,4, etc. The number means how many levels in the hierarchy tree the user wants to show in form view in the Product window. For example, if the tree is: Color->Green->Green light->0034

New values of an existing characteristic can be added. For example, colour red when already having Blue and White. When it happens, this new value is automatically added to all generic products that already have the characteristic Color. This new value will be present in the configuration tab but deactivated. If the user wants to use it in a specific product in order to create new variants he can just activate the value and use the button "Manage Characteristics"

##### **Modify Tax**

- **Modify Tax**: This check allows services to modify the taxes of the product linked to. This allows modifying taxes calculation of a product depending on a service condition. For example, a new kitchen furniture is sold to a customer, the taxes applied to the furniture might change if the installation of the furniture is also provided by the seller of the furniture. Also, this functionality applies only to Orders. The documents that are created afterwards will take the information from the Order document.

This tax modification is implemented through a service linked to the product. This service has to be marked as able to modify taxes of the products linked to, and the configuration of the products to modify taxes and the new tax to apply must be also specified.

To configure it, go to the Product window and create a new service. A service is just a product with the field Product Type set to Service. It has to be activated also the field Linked To Product and the field Modify Tax. When this field is activated, a new tab named Modify taxes categories is visible. In this tab, it is defined the configuration of the tax categories of products this service will modify when linked and the new tax category to apply.

![](https://lh3.googleusercontent.com/260ftQHLj7KxqXuouydWqLebx8YSli0i-k7OQh7rvpv1tfbcFB7zqhatrWcMd2F8tFMwLJEA-7xbc9LAtOdi1MNYioVlWheErN2eiFnhvq77HU-oyLHyiUTvrE_T1ruWbkDwOAPwpytv6_sM5w)

To ease the configuration process, two components have been added:

1.- Modify Tax for Product Category (Button): Pick and Execute window to assign the product categories and tax categories in the same action.

![](https://lh3.googleusercontent.com/8ToxP9o606fpE3T0LM-yFPrDkN_UcfbtRPVfoZvh6Oa_riBLBhSKHPfMvurIv4ijKgDJWyVFo4Bqjxe9tP0uzGw_GUbOBHq5j_s26JnOYPHDpzmwnQnxrdWC4yeQJfjs9glD0TVmOro6OA1wDg)

2.- Copy Service Modify Tax Configuration (Button): Pick and Execute window where services which modify taxes are displayed. The user can select one or many services, and current configuration will be assigned to selected services. Once the process has been executed, the old configuration (if it exists) will be deleted and a new one will be added. This process helps in deploying the same configuration to multiple services.

![](https://lh6.googleusercontent.com/kiBwqlQgDgPUsbPgVV_vcxX_KBYPiHR4IO7ESfJQQOz6oZqgYal_8hA6Umn-Ik7g_ZfacpN64S_51WsHE-uruqBmRsEHWDRw94xVzBKRwBUiC_WGyGV8E_H3-ZLIVpb1kYpIFggvv_VmQz8n2w)

### **Price**

A product can be part of many Price List Versions which are valid for a given time period.

![](https://lh5.googleusercontent.com/djRxxYVfhjv8e71EzysdOeoAUbQHqZSVuQbECB5EJ88BVtBo7FJ5weuwe6rrpxjxcXMKUX8pZKFgAE_lj5WdhmABdxh0Q09e9wdLPK8VBKNf6jBK8E56qbc6oQRtDcmHgxnxclqBQGsbm2B_rg)

There are two ways in which the user can get a product to be part of a Price List:

1.  by **selecting the Price List/s** and entering both the "Net Unit Price" and the "Net List Price" values in the Price List tab, while creating the product.  
    As a consequence of that, the product being created will also be part of the Price List selected.
2.  by **selecting the product** and entering both the "Net Unit Price" and the "Net List Price" values, while creating the "Price List".  
    As a consequence of that, the Price List as well as both "Net Unit Price" and "Net List Price" values will be automatically shown in the "Price List" tab of the product.  
    To learn more, visit Price List.

#### **Price Rule Version**

This tab will only be available when field Is Price Rule Based is selected. This tab gives the possibility of adding Service Price Rules to the Service starting from a certain date.

![](https://lh6.googleusercontent.com/oKeZYS9ty3rxPOvfQd1nAc-VteGicSiOkI71kDF0mKBqomlsHjkbrtbMU3I36bDAbhM22cr0vlpMQ9FohG59E2YDtYddX5mFScwzgxcCvihP_y3C7SNdYqdnyIKewEei_gERVk0Nq-e4Gp_7Bg)

In this window it is also possible to define a maximum and minimum amounts that will be taken into account when showing services.

Those amounts define an interval between product prices so that the service will only be available to be added in case the sum of the selected products is between the interval.

For services of quantity rule: Unique Quantity the quantity of the line matters, as it will be only added one service.

For services of quantity rule: As per Product the quantity of the line does not matter, the price of the product only matters as there will be added as many services as products are selected. Only if all the products prices are between the tranche, the service will be shown.

Also, if once a service (not yet delivered) has been added to the receipt, the price of the related product changes, a validation will be triggered, and in case the service no longer meets the tranche rules, it will be removed from the current receipt and a pop-up will be shown saying so.

### **Accounting**

Accounting tab allows the user to configure the ledger accounts to be used while posting product related transactions such as product purchase or sales to the general ledger.

![](https://lh5.googleusercontent.com/bLlVeOrdKF3rI3NdVa69a-CAwtO63JpdbyF0fzkMEG1pdmZU8u7bOlhffyM-HCwVnYA_y0kd51iPvCELamYYdp5RA9a7wVithXN1EWh_T73K304xQYB-gApjFi0-6vcof5HZBzUyIUrkpT82JQ)

As shown in the screen above, you can configure for each product and general ledger some accounts to be used in the below listed transactions:

- **Product Assets**: this field stores the default account to be used to record inventory transactions such as:
  - Inventory Counts
  - Inventory Movements
  - and Goods Receipt

This account is typically an asset account.

- **Product Expense**: this field stores the default account to be used to record product's purchases:
  - Normally, this account can be configured as an "Expense" account type in case of not managing "Perpetual Inventory".  
    In that case, the expense is accounted at the time the goods are purchased at the purchase price.  
    The revenue is accounted at the time the goods are sold at the sales price.  
    Not managing "Perpetual Inventory" implies the need of manually adjusting the inventory value at the end of the year.  
    That inventory adjustment implies calculating the difference between the "Final Inventory Value" and the "Initial Inventory Value".
  - However, this account can also be configured as an "Asset" account in case of "Perpetual Inventory" management.  
    In that case, the expense needs to be accounted when the product is sold to the customer as "Cost of the Goods Sold" at the product cost.  
    In Etendo, the revenue is accounted at the time the goods are sold at the sales price and the cost of the goods sold is accounted at the time of shipping the goods at the product cost.  
    Managing "Perpetual Inventory" does not imply the need of adjusting the inventory value at the end of the year.
- **Product Deferred Expense**: this field stores the default account to be used to record deferred expenses.  
  This account is typically an asset account.
- **Product Revenue**: this field stores the default account to be used to record product sales revenues.  
  This account is typically a revenue account.
- **Product Deferred Revenue**: this field stores the default account to be used to record deferred revenues.  
  This account is typically a liability account.
- **Product COGS**: this field stores the default account to be used to record the cost of the goods sold.  
  This account is typically an expense account.
- **Product Revenue Return**: this field stores the default account to be used to record sales returns.  
  This account is typically a revenue account.
- **Product COGS Return**: this field stores the default account to be used to record.  
  This account is typically an expense account.
- **Invoice Price Variance**: this field stores the default account to be used to record price differences between posted Goods Receipts and booked Purchase Invoices.  
  This account is typically an asset account.

At first, these accounts are inherited from the Defaults accounts of the organization's general ledger configuration for which the product is being created. The end-user can always change them.

!!! info
    Besides, it is important to remark that it is possible to configure the creation of new correlative accounts for the products as described in the General Ledgers tab of the Organization window.

#### **Bill of Materials**

This tab allows editing the bill of materials components the selected product consists of.

Bill of Materials apply to products flagged as **Bill of Materials**.

This tab provides information of the list of products contained and its quantity for the Bill of Materials production.

If the product Tax_Category is flagged as **As per BOM**, this tab also provides information for the price of each product in the Bill of Materials list. The price and quantity in this list is used to perform the division of the base amount to calculate the taxes based on the taxes configured for each product of the list.

![](https://lh5.googleusercontent.com/s-cRF1Q5kJQ4sPgBi-R9mMhT6v5JerM6U2qcFr0KgUyU79r0KE3mbTxN5oifJP1_M7XiW8G4j-vLYv6CSF8kr0XnyfO4DVGmazBfVB0aTjpfKS5qgLbYc6ZcBGUki-fBkZNVWmn9pYbVOqlIzw)

### **Costing Rule**

Costing rule tab allows the user to review the costing rules that apply to the product within a given date range.

Costing Rules apply to products set as "Item" type flagged as Stocked.

This tab provides information about the validated costing rule(s) which applies on a given date range to the product, as well as the Costing Algorithm defined for that rule.

Costing rules can be created and validated in the Costing Rules window related to the corresponding legal entity / organization.

Currency used by the costing rule is the currency set for the organization.

![](https://lh4.googleusercontent.com/pUP_Yr9n3YIRGELLgfbQGwgdZ2Hbfpn79YXYVdLLoqnm0fsbUkFho_XUijntiFcDgbpRUNu323utJkWNYXS2b9KaazDnoEfi9kr-p_Mr3XD-gRh5udUjkbV1y6IBy3xPiUuQ-w0PW6Wk45oSVw)

### **Costing**

Costing tab collects and summarizes product cost related information as a result of every product transaction. Product's costs are valid during a fixed date range and can be calculated either by using an Average or a Standard costing algorithm.

One of the first things to do while creating or importing a product into Etendo is to inform Etendo about:

1.  the initial **Cost** of the products, if any, by entering it in this tab.  
    Keep reading to learn how to do it.
2.  and the initial **Stock** of the products, if any, by creating and booking a Physical Inventory.

Overall, this tab allows to:

- **define the Cost** of stockable products, that cost can either be a standard cost or an average cost.
- **define the Cost** of non stockable products, that needs to be a standard cost.

In the same way, either a "Standard" or an "Average" Costing Rule needs also to be defined for the Organization as the way to calculate the cost of the products' transactions within that organization.

- **review the average cost** calculated by the [](http://wiki.openbravo.com/wiki/Costing_Server)Costing Server when using an "Average" Costing Algorithm.

> Note that when using a "Standard" costing algorithm the cost of every product transaction is the "default standard cost" entered in this tab.  
!!! info
    The "default standard cost" can be used by the Default Cost method whenever it is not possible to get the price of a transaction for which its cost needs to be calculated.

Average algorithms override the behavior of the "Default Cost" method prioritizing the use of the current "Average Cost" if any.

- and finally to have a view of all the input transactions of the product which have impacted on product cost calculation.
  - Input transactions such as vendor receipts are the ones which impact on product cost calculation, therefore the "Inventory Transaction" field clearly reflects those one by one.
  - Similarly, a "permanent" manual cost adjustment executed in an output transaction, such as a "Goods Movement From" (M-) impacts on product cost calculation, therefore the "Inventory Transaction" field clearly reflects these type of output transactions.
  - The very last transaction informs about:
    - the last cost, valid until a given ending date
    - and the total amount of units of that product which are valued at that cost.

Here, the costs calculated by the "legacy" engine are also visible.

It is possible to recognize them by their cost type:

- **Legacy Average**
- and **Legacy Standard**.

![](https://lh6.googleusercontent.com/N1fWn0tV0yzS8dZULfJfiKeIOSvJzfYe-IBCo_TJSVqUavfD-zU4UlJlAhkg7CGNOV5uT__6-46NOHmWzyI3DBaYGwH_2TNdoblDMnC6VwDRzWILLf1k6YWZ8PRAPNWEjcMpSzqz81vqpObEBw)

The way to define the **Cost** of a product implies to enter below detailed information:

- The **Organization** for which the calculated costs apply to. Note that the organization needs to be a *Legal Entity*type organization.
- The **Cost Type**. There are two cost types available _Standard_ and _Average_.
- The **Cost** of the product, that cost can either be the standard unit cost of the product or the average unit cost of the product.
- An **Starting Date** when the initial product cost entered is valid from.
- An **Ending Date**, when the initial product cost entered is valid until, i.e. 31-12-9999.  
  That is the same as saying that the cost entered is valid until a new movement of that product is dated on a given date prior to 31-12-9999. Obviously that new input movement will change the product cost.

Besides:

- the **Manual flag**, allows the user to differentiate the cost transactions you have manually entered from the ones automatically created by Etendo.
  - manual ones created by you while entering default product cost information should be checked as Manual.
  - automatic ones related to Material Transactions bookings will not be checked as Manual.
- the **Permanent flag** blocks the ability to delete the cost manually. All costs should be set as Permanent.
- the **Warehouse** allows having a different cost by warehouse when desired and whenever the Costing Rule defined allows to do that.

!!! warning
    Note that you should not fill this field if the Costing Rule does not have the Warehouse Dimension field checked.

### **Transactions**

Transaction tab is a summarized view of all the transactions of a product.

There is not a way for the user to directly create new product transactions in the transactions tab.

Product transactions of any type are automatically saved and listed in this tab as they are booked in Etendo.

![](https://lh4.googleusercontent.com/20u-EUxoETZhWKS6geaudh3OZbjEc0CvxOFx_0njFvaHCzsro7CxBXExfQSPgKnKNX4eRyw4uvcYUIXZSBINAPMX-3nGhUoqA1K08zWlRefUU00gCNAQEvXbU-7RboBfWCxzGUK4OrStxUZ3kQ)

As shown in the image above, Etendo saves and informs us about below relevant data for each product transaction type:

- **Storage Bin** where the product has been stored in or taken from
- **Movement Quantity**, as the number of product units moved internally or either in or out
- **Movement Date**, as the date of the product transaction
- **Movement Type**, such as:
  - **Customer Shipment**, this type can have:
    - a negative movement quantity whenever a product is shipped to a customer in a Goods Shipment document.
    - a positive movement quantity whenever a product is returned from a customer in a Return Material Receipt.
  - Internal Consumption, as the units consumed in internal activities such as projects, reparations. This type can be:
    - **Positive** if the units of the product reduce stock from the warehouse
    - or **Negative** if an internal consumption transaction is canceled, this works like when a shipment is canceled.
  - Inventory In, this one relates to a Physical Inventory Count higher than the Stock booked for a product in Etendo.
  - Inventory Out, this one relates to a Physical Inventory Count lower than the Stock booked for a product in Etendo.
  - Movement From, this one relates to Goods Movements from a Warehouse & Storage Bin
  - Movement To, this one relates to Goods Movements to a Warehouse & Storage Bin
  - Production, as the units of a product included in a work effort. This type can be:
    - **Positive**, for P+ when products are added to the warehouse
    - or **Negative**, for P- when products are consumed
  - **Vendor Receipts**, this type can have:
    - a positive movement quantity whenever a product is received from a vendor in a Goods Receipt document.
    - a negative movement quantity whenever a product is returned to a vendor in a Return to Vendor Shipment.

Etendo also informs us about the specific:

- **Goods Receipt/Shipment Line**
- **Physical Inventory Line**
- **Movement Line**
- **Production Line**
- or **Project Issue**

information of the product transaction, as applicable.

It is also possible to review:

1\. The **Costing Status** of a transaction.

Costing status of a transaction can be any of the ones listed below and has a lot to do with the Costing Background Process:

- **Not Calculated**. This status means that the costing background process has not taken the transaction yet to calculate its cost.
- **Cost Calculated**. This status means that the costing background process has already taken the transaction and its cost has been calculated.
- **Pending**. This status has been implemented to get that the costing background process does not throw an error whenever it is not possible to calculate the cost of a transaction.  
  This status is not used by the Costing Algorithms currently implemented in Etendo but can be used by other costing algorithms such as FIFO for those cases where a product output transaction is booked without booking its corresponding product input transaction.
- **Skip**. This status has been implemented to make the costing background process not taking into account the transactions set as "Skip" while calculating costs.  
  This status is not used by the Costing Algorithms currently implemented in Etendo but could be used by other costing algorithms.

2\. and **whether the cost of a transaction has been calculated or not**.

As soon as a product transaction gets its cost calculated by the Costing Background Process the field "Is Cost Calculated" gets the value "Yes".

Once the cost of a transaction is calculated you can also view the:

- **Trx Original Cost**, that is the original cost of the transaction
- **Total Cost**, that is the sum of the original cost of the transaction and all adjustment costs of any type.
- **Unit Cost**, that is the sum of the original cost and all the "unit cost" type adjustments.
- **Currency** used for the calculations.

Additionally, "**Is Cost Permanent**" field informs whether the cost of a transaction is permanent or not. In case it is permanent, it will not be changed anymore.

Finally, it is important to remark that in the case of "Average" cost algorithm, the "average" cost of a product is calculated as "Moving Average".

The average cost of a product is calculated based on the product's transaction flow, therefore it is the sum or subtraction of the "Total Cost" of the transactions listed for the product, divided by the sum of the "Total Movement Quantity" of the transactions.

For instance the average cost of a product which transactions are listed below is equal to 23.33 = (2000.00-1000.00+2500.00)/(100-50+100):

- goods receipt for Movement Qty 100 for a Total cost of 2000
- goods shipment for Movement Qty -50 for a Total cost of 1000
- goods receipt for Movement Qty 100 for a Total cost of 2500

##### **Manual Cost Adjustment**

Additionally, the cost of a transaction can be modified by clicking the Manual Cost Adjustment process button. After clicking this button, a new popup is opened:

![](https://lh4.googleusercontent.com/qDJuH3rx2ZvsvrA9Tjl0WZZjwJors5Xu2P2UgEjiBK_jhHX9vbYN3ZKcvH1mLIMWqUTNtrP4iKcFtp3VTDiwTHyLRpzsk4TUvxWl4QXo-ErSsQ4LbqtWnkCi2TWf1ftOhyL97RTpP5BbSEjL-Q)

This pop-up allows entering below detailed data:

- **Total Cost Amount**: that is the new total cost of the product transaction
- **Accounting Date**: that is the date when this manual change which will imply a cost adjustment is going to be post to the ledger
- **Incremental**:
  - if not checked, the amount entered in the total cost amount field is the new Total Cost of the transaction which, besides that, will be set as a "Permanent" cost which cannot be adjusted anymore.
  - if checked, the amount entered in the total cost amount field is going to be added to the current total cost, besides "Unit Cost" checkbox is shown.
- **Unit Cost**: This checkbox is shown only if "Incremental" checkbox is selected.
  - if not checked, the incremental amount entered in the field total cost amount is not going to be considered part of the transaction unit cost but total cost. This is like entering an "extra" cost such as "Landed Cost", which does not change the unit cost of that transaction but the total cost.
  - if checked, the incremental amount entered in the field total cost amount is going to be considered part of the unit cost of the transaction.

For additional information about which cost adjustment is, or it is not unit cost, please review the section Cost Adjustments - Introduction.

Once done, a "manual cost correction" cost adjustment will be created.

This cost adjustment can be reviewed and posted to the ledger in the Cost Adjustment window.

In the same way, this cost adjustment can also be reviewed in the Transaction Cost tab.

#### **Transaction Costs**

Transaction Costs records are automatically created by the Costing Background Process and then listed for the product in this tab.

As soon as a product transaction gets its cost calculated, a new record is created in this tab.

As soon as a product transaction gets its cost adjusted, a new record is created in this tab referring to a "Cost Adjustment Line".

![](https://lh4.googleusercontent.com/4lIc4FKc7VmCIoWFVPcV9fVkCqtBn2xTicXNsiin-P85rYySX2jwvUPGUAd3IdEaCUCSQo2hSgp_fuUP2Pp1HhXd6jUX03CePAe2AxypVuOVORVnJejwASLUrEmAGQyLBDCNm1GBXWaYr1N8ew)

Some relevant fields to note are:

- **Cost Date**: that is the date when the cost has been calculated (i.e. accounting date of a goods receipt)
- **Cost**: that is the total cost calculated by the costing background process
- **Currency**: that is the currency used to calculate the cost.  
  Currency cost is legal entity currency, therefore product transaction having a different currency (price list in USD currency for instance) gets its cost calculated in the legacy currency (i.e. EUR)
- **Cost Adjustment Line**: if a calculated cost comes from a cost adjustment, this field populates the cost adjustment line that causes that cost.  
  At the end, the total cost of a product transaction is the sum of all the costs listed in this tab, original and adjusted ones which could be part of the unit cost or not (i.e landed costs).
- **Unit Cost**: this field details whether the calculated cost is part of the unit cost of the product or not.
- **Accounting Date**: that is the accounting date when the cost has been calculated and post to the ledger (i.e. accounting date of a goods receipt post to the ledger)

### **Purchasing**

Purchasing tab information is used for products that are planned by the purchasing plan.

In this tab, the information that is required for the creation of the Purchasing plan and of the automatic creation of Purchase Orders from the Purchasing Plan is entered.

Also, the Requisition process uses the Business Partner information for the automatic creation of Purchase Orders.

![](https://lh3.googleusercontent.com/jUizYPPOFt4WfdpL71z7Pxe8z7aMWc7Qnzz0rYE488WWt0fvBY9jKgswYbddRYo1rOzmYGsAmV0zOCGvwuo2BfwWDr4gG94qfwrNTjpfcA3XYq1sNH2wNg495KlwPCY52uGyT_FhGRQWxDzbMw)

- **Business Partner**, the vendor that will appear on the Purchase Order when created automatically from the Requisition or from the Purchasing Plan.
- **Quality Rating**: quality rating of the vendor. Information only field that is not used by the MRP process.
- **Current Vendor checkbox**: indication of the default vendor that will be taken into account by the MRP process.
- **UPC/EAN**: Universal Product Code/European Article Number (barcode) of the product as used by the selected vendor. Information only, this information does not appear on a created Purchase Order.
- **Currency**: currency of the purchase order.
- **Net List Price**: information only field of the Net List Price that has to be updated manually on the automatically created Purchase Order from the Purchasing Plan.
- **Price Effective From**: the date that the entered prices became valid. Information only, not used by the MRP process.
- **Purchase Order Price**: information only field of the Net Unit Price that has to be updated manually on the automatically created Purchase Order from the Purchasing Plan.
- **Last Purchase Order Price**: the Net Unit Price on the most recently added Purchase Order.
- **Last Invoice Price**: the Net Unit Price on the most recently added Purchase Invoice.
- **UOM**: the unit of measure of the product.
- **Minimum Order Qty.**: a minimum order quantity for the vendor. In the Purchasing plan, the quantity for suggested purchase orders is this value or above.
- **Quantity per Package**: information only for the packaging of the product. This information is not taken into account for the creation of the information in the Purchasing Plan nor for the creation of Purchase Orders.
- **Purchasing Lead Time**: time in calendar days between when the product is ordered from the vendor and when it is received in stock. In the Purchasing Plan, this information is used to calculate when purchase orders should be placed, resulting in the Planned Order Date for the suggested purchase order.
- **Fixed Cost per Order**: information only field of a fixed amount that has to be added manually to the automatically created Purchase Order from the Purchasing Plan.
- **Vendor Product No.**: the vendor reference for the product
- **Vendor Category**: information-only field to add vendor category information.
- **Discontinued**: information-only field to indicate that this product is no longer used. The Purchasing Plan does not take this set up into account when generating the plan and when creating Purchase Orders. When selected, the field Discontinued by date to indicate when the product is discontinued. For information-only purposes.
- **Quantity Type**:
  - **Exact**: each suggested purchase order is for the exact required quantity. For example, if the demand is for 85 units, the quantity for the suggested purchase order is 85 units.
  - **Multiple**: the quantity that appears as the quantity for the suggested purchase order is a multiple of the standard quantity (as defined on this screen). For example, if the standard quantity is 20 units and the demand is for 85 units, the quantity for the suggested purchase order is 100.
- **Manufacturer**: information-only field to indicate the manufacturer of the product.
- **Standard Quantity**: quantity that is taken into account in combination with the Quantity Type for the quantity value for the suggested purchase order.
- **Capacity**: quantity per day the vendor is able to supply. Based on this field and the lead time, the purchase order date is calculated. The number of days is calculated as the max value of the lead time and the required quantity / capacity.

### **Manufacturing**

Manufacturing tab is used for products that are planned by the manufacturing plan.

The information in this tab is mainly used by MRP to process the Manufacturing Plan and Purchasing Plan. The storage bin field is filled out for products in production to indicate the default storage bin the product will be stored in when coming out of production.

- **Storage Bin**: default location in the warehouse of the product.
- **Planning Method**: definition of the elements of supply and demands that are taken into account and with which percentage for the creation of the Manufacturing Plan and Purchasing Plan. For more details, see the Planning Method section.
- **Planner**: the person responsible for the execution of the MRP plan of the product. For more details, see the planner section.
- **Capacity**: production capacity per day for the product.
- **Min. Quantity:** minimum quantity to be entered on a work requirement.
  - **Exact**: each suggested work requirement is for the standard quantity (as defined on this screen). Multiple suggested work requirements appear for the total demand. For example, if the standard quantity is 20 units and the demand is for 85 units, 5 lines of suggested work requirements with quantity 20 appear.
  - **Multiple**: the quantity that appears as the quantity for the suggested work requirement is a multiple of the standard quantity (as defined on this screen). For example, if the standard quantity is 20 units and the demand is for 85 units, the quantity for the suggested work requirement is 100.
- **Standard Quantity**: quantity that is taken into account in combination with the Quantity Type for the quantity value for the suggested work requirement.
- **Minimum Lead Time**: manufacturing lead time of the product.
- **Safety Stock**: the minimum level of stock that has to always be in the warehouse. For example, if there is a safety stock for 1000 units and stock is 900 units, a work requirement (Manufacturing Plan) or purchase order (Purchasing Plan) is suggested for 100 units. Typically, low cost products or products with a very long lead time are set up with a safety stock level.
- **Max not reserved stock**: Maximum stock without taking into account the pre-reserved stock. This field is only visible when Stock reservation feature is enabled. See the below example to understand how it works:

1.  _Safety stock_ and _Max not reserved stock_ are 200 and 1000 units, respectively
2.  There are several sales orders to be delivered by 3000 units in total
3.  These sales orders will generate the corresponding purchase orders (pre-reserved) when launching the MRP
4.  There are currently in stock 80 units
5.  When MRP is launched it will create the corresponding pre-reserved and because being after below safety stock it will create another purchase order:
    1.  As the _Max not reserved stock_ is defined, the system will create a purchase order of 920 units (1000-80)
    2.  If this parameter was not defined, it would work as usual and it would create a purchase order of 120 units (200-80)

- **Abc**: value used in warehouse management to indicate a combination of the stock level and the cost of a part. The value is calculated by running the Pareto Product Report.

### **Translation**

Product names can be translated to any language.

The way to get that is as simple as:

- select first the language required
- and then enter the product name translated into that language.

#### **Characteristics**

Relation of characteristics assigned to the Product.

Fields:

- **Sequence number**: Order of the characteristics
- **Characteristic**: List all the characteristic defined in _Product Characteristics_ window
- **Variant**: When it is marked, it will explode/create combinations with its values. If it is not marked, it will not create combinations with other characteristics. For example
  - Characteristic Color: Variant marked with value Blue and White
  - Characteristic Size: Variant marked with value M and L
  - Characteristic Fashion line: Variant not marked with value Sport
  - It will create four variants/products and for all of them with the characteristic Sport
- **Explode Configuration Tab**: Flag available on Generic Products and Variant Characteristics. When it is checked, the values of the selected variant characteristic are automatically inserted in the _Characteristic Configuration_ tab. If it is not checked, the values must be added manually.
- **Defines Price**: Every value of that characteristic will define the price of the new product. It will overwrite the price defined for the generic product. This price is defined in the _Characteristic Configuration_ tab
- **Price List Type**: It is shown when _Defines Price_ is marked. It allows the user to select in which type of price list you want to overwrite the price. For example:
  - The generic product has two price lists: One is for sales and the other for purchase
  - You select _Sales Price List_ value. Then when creating the product variants it will only overwrite the price in price lists defined as Sales
  - The opposite if the value selected is _Purchase Price List_
- **Define image**: Every value of that characteristic will define the image of the new product. It will overwrite the image of the generic product. This image is defined in the _Characteristic Configuration_ tab
- **Characteristic Subset**: List all the subsets included for the selected Characteristic (i.e. Pants)

Once the record is saved, all the values of the characteristic are populated into the characteristic configuration tab

**Characteristic Configuration**

Characteristic Configuration tab contains the available values for each characteristic assigned to the generic product. Price modifiers to create the variants are defined in this tab as well.

Fields to take into account:

- **Characteristic value**: Cannot be editable since it is populated automatically when selecting the characteristic
- **Code**: Code for the value. It inherits what has been defined in product characteristic window
- **Unit price**: This field is displayed when the characteristic is marked as _Defines Price_. The aim of this field is to have different prices per value. For example, depending on the Sizes
- **Image**: This field is displayed when the characteristic is marked as _Defines Image_. The aim of this field is to have different images per value. For example, depending on the colour.

### **Stock**

This Tab shows the available Stock for this Product in the application. It only shows Storage Bins for which the quantity available of the Product is not 0

For each not empty storage bin, it also shows information about the:

- reserved quantity
- and the allocated quantity

### **Unit Cost**

Unit Cost Tab displays information about the actual "Unitary Cost" (Unit Cost) of the product.

The "Unitary Cost" of a Product is the value of each stocked unit of the product no matter the costing algorithm used to calculate the cost of that product.

This cost is calculated using the "Total Stock" of a product and the "Total Value" of the stock of the product, as per formula below:

- Unit Cost = Total Stock Value / Total Stock

This way, the unitary cost calculated is independent of the "Costing Algorithm" used to calculate the cost of each transaction and product, therefore this unitary cost is compatible with all "Costing Algorithms" (Average, Standard, FIFO, ...)

In this Tab, there is going to be a record for:

- each Organization that is a Legal Entity that has a Costing Rule defined
- or each Organization and Warehouse, whenever Warehouse Dimension is defined as a costing dimension of the current Costing Rule defined for the "Legal Entity".

![](https://lh5.googleusercontent.com/KaTTAE01N7KuTheqE-4REVj2b6H1QQnWqxpNvt2oNR_y9sqdYUsBOhQw1RHg_KP10n4NoI5gVpUXfgb0KPHOYx5Ab-RCWIAWvUyboKczDdnTHaWWVfw-bhUDAE4pMsAvEyt3qNtfHeKj7DAQ5A)

#### **Product Categories**

The user can define if a product of a certain product category can be related to a product of 'Service' type by creating a relation between an Order Line of the Service product and another Sales Order Line of the product belonging to included/excluded product categories.

This tab will only be available when the field ‘Included Product Categories’ of the Service has a value. It contains all the product categories related to the service.

![](https://lh6.googleusercontent.com/PYJo6PQVwfGTLbk5f39Z5opQ3qM4D81lk9qWKX7k1Z-E9RzZC5ZnB9EK4fcWtb37L_ZP_fcJbcnAQdXMF1vLAzXuhseG993zL5eDG2xL-nt-jexrA3D-d4VupddMJEeKGixjbQZFXUBoayzGQQ)

The following information about related products is available in the tab:

- **Search Key**: Search Key of the Product Category.
- **Name**: Name of the Product Category.
- **Description**: Description of the Product Category.

This tab is not editable, it is not possible to add records manually or edit them. It only allows to delete records. To add new records, it is necessary to click the ‘Relate Prod Categories’ button (Visible only when the field ‘Included Product Categories’ has a value). This button will open a Pick & Edit displaying all product categories not related to the service.

![](https://lh6.googleusercontent.com/n_0U2RkOiXABiP8XeiREnMyOPLHm9-Xsu9hNM-PE6c248gNtomNeOzXROYJJzMpkuRJvKH0GnNDpOp3FSaBOAVURspU8rHeGLY_dhWofqyWmnQ00gJ8yGwuTDxy_PZ_SyzDTmPk6vf2eBeXEDQ)

#### **Category Price Rule Version**

#### **Products**

The user can define if a product can be related to a product of 'Service' type by creating a relation between an Order Line of the Service product and another Sales Order Line of the product included/excluded.

This tab will only be available when the field ‘Included Products’ of the Service has a value. It contains all the products related to the service.

![](https://lh4.googleusercontent.com/QhyN8Mqa2ybLbU9ny5se3_Z-JsGEIYGIAma4LQhBS4U4TUdZWUQTe3-Y3NP7bwlaQSxr6Fea2aB0K2g-slUF8XLmuN6aDN-3LCgqCjfSl0cl4uyn1c8YgL-w_AuZi8t4jXcDyF-cr2CpqKm-xg)

The following information about related products is available in the tab:

- **Search Key**: Search Key of the Product.
- **Name**: Name of the Product.
- **Brand**: Brand Key of the Product.
- **Product Category**: Product Category to which belongs the product.
- **Generic Product**: Generic Product of the Product, if it has any.
- **Characteristic Description**: Characteristics of the Product, if it has any.

This tab is not editable, it is not possible to add records manually or edit them. It only allows to delete records. To add new records, it is necessary to click the  ‘Relate Products’ button (Visible only when the field ‘Included Products’ has a value). This button will open a Pick & Edit displaying all products not related to the service.

![](https://lh5.googleusercontent.com/LB2xjm1Lcu3JfY4eab8BA9hFgvjRLJCvaIW52jrLlGSoox67pJL73fBfqhzWBAVBGBGnXAOiaIu7F4O8bYsnbRWsmbZj3ddYGqWZ0vFpcJZdbTdSWIMtGuLFMcFDTONgqvFSgqwm3eW0fNIFxw)

#### **Product Price Rule Version**

#### **Alternate UOM**

!!! info
    The user must enable this preference by entering the Preference window, checking the Property list checkbox, choosing “Enable UOM Management” in the Property field with value Y.

![](https://lh5.googleusercontent.com/zu1QFJc_LPSBeJOGOOGHLNMjKi-WsPgjKPEaD4-BnQJEKbvhU1jz0WXeW-RHyDOEXYAx67_-Z7F6SIGVxBkGdZT828fkrjzAeu35psYO4H_dSFcw8YosbJailPqSWhZyjhCsN01vu0kqIyTG1g)

Fields to note:

- **UOM**, that is the alternative unit of measure of the product, for instance "Pallet".  
  It is important to remark that any unit of measure needs to be created and configured in Unit of Measure window.
- **Conversion Rate**, that is the conversion between product's alternative unit of measure (AUM) to product's unit of measure.  
  For instance, if product's AUM conversion to product's UOM is 50; that means that 1 Pallet represents 50 Units.
- **Gtin**, that is the "Global Trade Item Number" for the product defined in the corresponding AUM
- **Sales**, **Purchase** and **Logistics**, those fields allow defining the use of product's AUM within Sales, Purchase and Inventory flows.  
  Values allowed are:
  - **Primary**: Product's AUM defined in this tab is used as default unit of measure in the selected flow (Sales or Purchase), when creating a sales or purchase document such as an order or receipt/shipment.  
    Only one Primary AUM can be defined per Product and flow.  
    For instance, if "Pallet" is the primary AUM defined for a product within Purchase flow, that means that every time that a purchase document is created, "Pallet" will be the default unit of measure shown.
  - **Secondary**. Product's AUM defined in this tab can be selected for the selected flow when creating a Document.  
    For instance, if "Pallet" is the secondary AUM defined for a product within Sales flow, while "Pack" is primary one; that means that every time that a sales document is created, "Pack" will be the default unit of measure shown, but end-user can change it to "Pallet".
  - **Not Applicable**. The AUM defined in this tab for the product will not be available for selection when creating Documents for the selected flow.  
    That is the option to select for "Logistics" as the use of alternative units of measure is currently implemented just for sales and purchase. Inventory transactions/documents always refer to the product's unit of measure.

#### **Modify Taxes Categories**

It defines tax modification for products linked to service. Products linked to this service that belong to the configured category will change the tax category when linked to this service.

## Business Partner Setup

#### **Introduction**

Business partners can be grouped into different categories with the aim of helping their management and analysis.

You may want to group the suppliers of a certain type of products within the same category, in order for you to compare the purchase prices your company got from them in relation to the same type of products.

Or you may want to group the customers located in your country within the same category, a different one than the one which groups the customers located abroad, in order for you to compare national and foreign sales figures.

All of the above is possible due to the fact that Business Partner Group is a dimension of Purchase and Sales Reports.

To learn more, visit Procurement Analysis Tools and Sales Analysis Tools.

Finally, it is also important for you to take into account that each business partner category allows the user to set up a different set of ledger accounts to be used while posting transactions such as customer receivables or vendor liabilities.

### **Business Partner Set**

#### Introduction

In this window the user can define lists of business partners to use in other functionalities.

#### Header

In the Business Partner Set header the fields to complete are the organization and the name of the list of business partners. It is also possible to add a description when necessary.

#### Lines

The lines tab allows the user to add the required business partners to the corresponding business partner set.

![](https://lh4.googleusercontent.com/8ZKuObE2Ho1XC21yS8iC2Y_OpEE2O90ARCMJbxiSHrqbvwIeoi03nkb_k4uo2xp5B7gbzB2cnINPV2kjKyK-8pkyMz4NNhduzwIAmCwe4ijlZ_wzZU5mefhkcGPg-4DmOdAdc0_fDmHBhC3Gl78)

### **Business Partner Category**

Business partner category window allows the user to create and configure every business partner category your organization may need.

![](https://lh6.googleusercontent.com/yiAWq21ZqaNFnysyzjUGdcU9RY9FIVQqQct184kzcnC2D6uQMWfucDd08L5YaVtSd1HtwvLRG2Vdqv9VJ1UrACm7AgCKwAXsZ6n4jWINbhoOqPVy5RpM4jnL_WheUZwDBroliExjc4cd8Z4NjQ)

As shown in the image above, the creation of a business partner category requires entering below listed information for each category:

- a Search Key or short name which helps to easily find a category
- a Name
- and a Description

#### **Accounting**

Each business partner category allows the user to configure a different set of ledger accounts.

![](https://lh6.googleusercontent.com/sEas2U1BqTJtpng8QicgZUyvuochrM-jHjiTbEioeEE48ThFV3xNzGAjuMyqxy1SPVwtEqeG5z6lgwu9qZQ2pt162aFt9kfCvkp6rNE1NK_ecgSgqNIa12wrcfNKeuPwetZKmA8s3xiNPOjBEQ)

There are several business partner related accounts which need to be properly set up for the organization's general ledger configuration.

The "Copy Accounts" process of the Defaults tab of the General Ledger Configuration screen allows the user to automatically populate at least the mandatory ones shown in the image above.

The accounts automatically defaulted by Etendo can always be changed if required.

These ledger accounts are the ones to be used while posting business partner related transactions such as:

- Customer Receivables, sales invoices posting.  
  To learn more, visit Sales Invoice
- Customer Prepayments, customer payments in advanced posting.  
  To learn more, visit Payment In
- Vendor Liabilities, purchase invoices posting.  
  To learn more, visit Purchase Invoice
- Vendor Prepayments, vendor payments in advanced posting.  
  To learn more, visit Payment Out
- Non-invoiced Goods Receipts, Goods Receipt posting  
  To learn more, visit Goods Receipt
- Write-off amounts, or amounts your company expected to get paid by a customer which are not going to be paid anymore.  
  To learn more, visit Payment In
- Revenue Write-off amounts, or amounts to be paid by your company to a supplier which are not going to be paid anymore.  
  To learn more, visit Payment Out
- Doubtful Debt Account, doubtful debts posting.  
  To learn more, visit Doubtful Debt Run
- Bad Debt Expense Account, expense amount classified as bad debt.  
  To learn more, visit Doubtful Debt Run
- Bad Debt Revenue Account, revenue amount classified as bad debt.  
  To learn more, visit Doubtful Debt Run
- Allowance for Doubtful Debt Account, amount used to provision against possible bad debts.  
  To learn more, visit Doubtful Debt Run

The "Copy Accounts" action button allows the user to copy the accounts defaulted in this window to either:

- the Customer Accounting tab
- or the Vendor Accounting tab

### **Invoice Schedule**

#### **Introduction**

Invoice schedule window allows the user to define and configure how often and by when an organization can issue invoices to be sent to customers.

#### **Invoice Schedule**

An organization can agree and therefore define specific schedules for issuing invoices, schedules which will then need to be linked to the corresponding customers.

![](https://lh6.googleusercontent.com/0W4ihla_EA-tyKPr-LD48QtQ8tA-NXalUc6vNw45JFtUQQSqURKxkirYyxbrbtM9533FjdnfxdOMsOdjdBfLx7M20MSpnNzG3YW5qfZ_zyxxEI8_4X01V2G7Mu6yAJtgwGqXzGMtDO1J46IKgg)

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

### **Title**

#### **Introduction**

Title window allows the user to set up business partner titles such as Mr or Madame to be used while contacting business partners.

The same applies to any type of "Contacts" entered in Etendo.

This is an "Advanced Feature". To be reviewed, as I do not see where Titles can be assigned to business partners and contacts.

#### **Title**

There are many titles to use while contacting business partners of any type as well as contacts.

![](https://lh6.googleusercontent.com/gZHYP7ZHyy6V6WbHltJU8h76GrjkhZX8GTD5xnejWTe8gkLjvlcS9hWiNn8l1NdakL9w5BX7btruUJB4krE5jnDGuSzJd4HTEChxeL7JKXNfUqttcv8_KlpV0sUs27nyb0BW2SjTMbBu4Dd7JQ)

Once the required titles have been properly entered and configured, you can link them to the corresponding business Partner "Contact/s" in the Business Partner window.

#### **Translation**

Business partner titles can be translated to any language required.

The way to get that is as simple as:

- select first the language required
- and then enter the title name translated into that language.

### **Payment Term**

#### **Introduction**

A payment term specifies the period allowed to pay off an amount due.

A vendor or a customer may demand a deferred payment period of 30 days or may even demand to partially pay their debts or collect in two or more deferred periods.

Therefore "Payment Terms" will generate a list of scheduled payment/s against an invoice, each payment/s will have a due date and a due or expected amount to be paid.

In other words, each payment term line and/or header is a different scheduled payment against an invoice.

The way it works is:

1.  Payment terms must be first properly created and configured as described in this section.
2.  Then payment terms must be linked to each business partner as described in the "Master Data Management // Business Partner" section.
3.  Finally, every time an invoice is booked for that business partner the payment terms setup by default will be applied and therefore used for the creation of the corresponding Invoice "Payment In/Out Plan".  
    A payment in/out plan lists as many scheduled payments against an invoice as due dates configured in the payment term associated with that invoice.

#### **Header**

Payment Term window allows the user to create and configure the payment terms to be linked to the business partners.

![](https://lh3.googleusercontent.com/Hbh0E3N6Stf3wHCPcTc9GOj6Er8So-o0y49I-7c-G8MuPjkbnJphTN9worhzR1U9oMFyxPfXLMu7uwo4_EFRuJKOlNtM_199vb43qX9IasL8IqkalNo8C42CQddbjwQ8bZ3EqQAxGLFOiiLq2w)

As shown in the screen above a payment term which only has a deferred period such as "100% in 120 days", can be created by entering below data in the payment term header window:

- an **"Offset Month Due"** which is the length of the payment period agreed in months, by example "4" as four months.
- or an **"Overdue Payment Days Rule"** which is also the length of the payment period agreed but in days, by example "120" as one hundred and twenty days.
- **Fixed Due Date** flag allows you to enter a fixed maturity payment date, such as 20th of each month, by example.
- **Next Business Day** flag allows you to set as payment date not exactly the corresponding due date but the next business day, this helps avoid due dates calculation over the weekend.
- **Overdue Payment Day Rule** allows you to enter a fixed payment day.

It is important to remark that in the case of defining a payment term split into more than one deferred period such as "50% in 30 days and 50% in 60 days", the second one (or the latest one in case of more than 2 deferred periods) must be setup in the header not in the lines as shown in the image below:

![](https://lh5.googleusercontent.com/WiK0QfJlcL1hhV_wm--ADnkVzNO8_O857PO7qGn1hV_3-1vz-WZCWM4DB2HPzQAaDhRNtHM8LE2ZgsVjUZW-A1udQ4Lq6BDpsbztFPRTv_S0t2mUPFLdaJsE_KB9TYOeGbo0xjlDuYBbDG1jiw)

#### **Translation**

Payment Terms can be translated to the language required.

The way to get that is as simple as:

- selecting first the language required
- and then entering the payment term name translated into that language.

#### **Lines**

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

### **Reject Reasons**

#### **Introduction**

In this window you can configure different reasons because either you return goods or the customer returns goods. This is the reason why these values are used in Return to Vendor and Return from Customer windows

#### **Return Reasons**

This window is in Application||Master Data Management||Business Partner Setup||Return Reasons

![](https://lh6.googleusercontent.com/EzeqfjlMA4oiTgUiCE4PQ55leA117l1-VAHRWpjrdBf9Xu78XqC37OMUN3o-VwsC3hzzOmm1zE-xHSJYs5z_7cplRZfNhWZs_zszBRwRfyLgaeaguly1pXDSeej1LpjJ8UIJbgmtpyqyldKCXw)

Fields:

- **Return from customer**: When this flag is marked, the value will be available in the window Return from Customer window
- **Return to vendor**: When this flag is marked, the value will be available in the window Return to vendor window

### **Volume Discount**

#### **Introduction**

Volume discounts are discounts which apply after getting a certain volume of sales of specific products or product groups.

Volume discounts are incentives intended to encourage the purchase of goods in greater quantities. This incentive is normally offered to pass on some of the economic efficiencies gained through larger orders, to improve customer relations, and to increase total volume of sales.

#### **Volume Discounts**

Volume Discount window allows the user to create and properly configure volume discounts related to specific products and/or product groups, which are later on assigned to selected business partners.

![](https://lh6.googleusercontent.com/g1bbTT-LAss3Ji167-5259AeMmavJ1HccPLrLUC5l5wjx-iHjnU027a0on1_mjXa4h9lQfVwD9iTKjgQpexYx80NLIrTsNYpbtFO5bzduuJAGE80BoVL2OO5LWRKPweoqPvDlAdg0uFcGnriPA)

As shown in the image above, a volume discount can be created by just entering below data in the "Volume Discount" header window:

- the "**Name**" of the volume discount
- the "**Currency**"
- the "**Included Products**" to which the volume discount will apply. Available options are:
  - Only those defined - which means applicable to all the products defined in the "Product" tab below.
  - or All excluding defined - which means all products but the ones defined in the "Product" tab below.
- the "**Included Product Categories**" to which the volume discount will apply. Available options are:
  - Only those defined - which means applicable to all the product categories defined in the "Product Category" tab below.
  - or All excluding defined - which means all product groups but the ones defined in the "Product Category" tab below.
- **Scaled** - A volume discount can be scaled which means that it is possible to define a set of amount ranges having a different discount. To learn more, visit the "Volume Discount Parameters" tab below.

#### **Product Category**

A volume discount can be configured for a set of product categories or can be configured for all product categories but for a set of them.

Therefore, and depending on the criteria taken, you could select here the products to either include or exclude of a given volume discount.

#### **Product**

A volume discount can be configured for a set of products or can be configured for all products but a set of them.

Therefore, and depending on the criteria taken, you could select here the product groups to either get included or excluded of a given volume discount.

#### **Volume Discount Parameters**

Volume discount parameters are a discount % as well as the minimum amount up to which the discount % is applied.

Besides, it is also possible to configure not just a minimum amount up to which a given discount % will apply, but a set of amount ranges to which a different discount % will apply.

As an example, you could configure a volume discount which applies:

- a 2% to the amount range =0,00 to 9,999.99
- a 5% to the amount range = 10,000.00 to 24,999.99
- and a 10% to a minimum amount up to 25,000.00

#### **Business Partners**

Volume Discounts can be assigned to selected business partners within a given time period.

You can also get a volume discount applied to a selected business partner starting from a given "Valid From Date".

Regardless volume discount makes more sense for "Sales Transaction", it is also possible to create and configure volume discounts to be applied to selected suppliers or vendors by:

- removing the "Sales Transactions" flag
- and by removing the filter "Customer" while selecting business partners in the business partner selector.

### **Basic Discount**

A Basic Discount is a deduction from the total amount of an order or an invoice.

#### **Introduction**

Discounts of this type means a sum of the total order / invoice discount amounts, excluding taxes per each tax rate.

Discounts tab can be found in the Purchase & Sales Order / Invoice windows and allows the user to add discounts manually or to review the ones automatically applied by Etendo based on the Business Partner Discount tab configuration.

![](https://lh6.googleusercontent.com/G7GmkLbSq2r0kuQXVluq9Gle5khzHQbG0d1QvHtMBGM5WamIJWzmRqqUaFuQ5Or4N6IEPltXrTgJsaI4DhDEG6it6WKTfkin8tRip2JqNW2TKa2e7fip7OK9gwUNLlbfTCXPAv1UOfSu2wVX-A)

Discounts

- When an order or an invoice is in _Draft_ status, the total amounts are the totals amounts including tax, but excluding discounts.
- Once the order/invoice is _Processed_, Etendo calculates the monetary value of the corresponding discounts and shows them as new order/invoice lines.
  - Discount lines have no product nor account but the discount product (see below).
  - Besides, Etendo creates as many new invoice lines as discounts included in the invoice as well as tax rates (%).
  - Discount lines have an ordered quantity equal to "1" and a Net Unit Price equal to the calculated discount amount with an opposite sign to the invoice amount (normally negative) in order to reduce it.
- Finally, discounts can be calculated in cascade.
  - Cascade calculation implies that the first discount is applied to the total net amount and the second discount is applied to the total net amount already decreased by the first discount amount, and so on. Configured in the Business Partner Discount tab.

**Example 1. Purchase invoice containing just one tax rate:**

- Let us imagine a purchase invoice containing two invoice lines for a net line amount of _1,000.00_ each.
- A _18%_ tax rate applies to both purchase order lines.
- There is a _10%_ Discount assigned to the supplier, therefore that discount is shown in the Discounts tab.
- Once above purchase invoice is booked:
  - Etendo shows just one new line with below information:
    - **Product** named _Discount 10%_ which is the one created and linked to the discount.
    - **Invoiced Quantity** equals to _1_.
    - **Net Unit price** equal to the applicable discount amount, which in our example is _\-200_ (10% of the total net amount _2,000.00_).

**Example 2. Purchase invoice containing two different tax rates:**

- Let us imagine a purchase invoice containing two invoice lines for a net line amount of _1,000.00_ each.
- A _18%_ tax rate applies to the first purchase invoice line, and an _8%_ tax rate applies to the second one.
- There is a _5%_ Discount assigned to the supplier, therefore that discount is shown in the **Discounts** tab.
- Once above purchase invoice is booked:
  - Etendo shows two new lines, each of them with below information:
    - **Product** named _Discount 5%_ which is the one created and linked to the "Discount".
    - **Invoiced Quantity** equals to _1_.
    - **Net Unit Price** equals the applicable discount amount, which in our example is _\-50_ (_5%_ of the total net amount at a given tax rate _1,000.00_).

#### **Basic Discount**

A total discount can be created and configured by entering a discount name, a discount product and a discount %.

![](https://lh5.googleusercontent.com/DY-WYecWhUy0pS3Vt255iFAJmuQspg8xhaQ-_l6mt7aoBrp-igyJbmacjFzPbH6BSh7OEw6uLZgJPBDxOtcvd96_QLfGJmSTt1pSkUUxXcvxuvdDbb6hGps_1G6qR1JLiYVSTCrAtuw-tug3fA)

Fields to note:

- Previously created Product you could name the same as the discount name. That product is the one to be filled in the new orders / invoice line/s to manage this type of discounts (see above).

### **Salary Category**

#### **Introduction**

Create salary categories to be applied to your employees/workers.

The salary category and related cost is used in the **Production** module for the calculation of the cost of a product that is the result of the production process.

All operations in the production process consist of activities. These activities have a cost center defined and how much time of that cost center is used. Each cost center has the employees that are part of the cost center, defined by salary category in the employee tab. The employee is set up as an operator in the employee tab of the business partner. Apart from the employee cost, also the machines cost used in the cost center and any indirect cost, such as electricity, is set up. Based on these components, a cost per hour related to the cost center can be defined. Based on the use of the cost center during production, a cost per produced unit is added to the total cost of the unit.

The salary category and related cost is also used in the **Project and Service management** module to calculate the profitability of a project. The cost related to a salary category for Project Management has to be defined with the 'per hour' unit of measure.

The setup of the salary category of the employee is done in the \[Cost Salary Category\] tab underneath the \[Employee\] tab of the Business Partner

#### **Salary Category**

It defines costs and date ranges for a specified salary category.

For the use of the salary category for the cost calculation in the Production and Project and Service management module, the cost applied checkbox is selected.

#### **Cost**

It creates a salary category.

**Cost UOM**: for Project and Service Management, the salary is set up per Hour, so that when the time expenses are entered, the cost of that time can be added to the profitability report.

### Rappel Configurations

!!! info
    To be able to include this functionality, the Advanced Rappels module of the Sales Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36).

Rappels are discounts based on the volume of consumption of a business partner in a given period of time. This functionality allows the user to configure and grant rappels to business partners.

#### Requirements

Before the user is able to use this functionality, it is necessary to configure a new document sequence and a new document type to be used for Rappels.

##### Document sequence

A specific document sequence for rappels is necessary to distinguish them from other transactions.
In this window, create a new record and fill the corresponding fields:

- **Organization**: The name of the corresponding organization.
- **Name**: The name of the document sequence, in this case, “Rappel sequence”
- **Active**: Yes
- **Auto Numbering**: Yes
- **Increment by**: 1
- **Next assigned number**: 1,000,000
- **Prefix**: It is optional and, in this case, “RAP-” is entered to indicate that these transactions are Rappels.

Save the record and the document sequence for rappels is available.

![document_sequence_new.png](/docs.etendo.software/assets/legacy/document_sequence_new.png)

!!! info
    For more information, visit [Document Sequence](https://docs.etendo.software/en/financial-management-setup-accounting#document-sequence)

##### Document type

A specific document type is necessary for rappels.
In this window, create a new record and fill the corresponding fields:

- **Organization**: The name of the corresponding organization
- **Name**: The name of the document type, in this case, “Rappel”
- **G/L Category**: In this case, select “AR invoice”
- **Print text**: In this case, “Rappel”
- **Document Category**: “AR Invoice”
- **Sequenced Document**: Yes
- **Document Sequence**: In this case, “Rappel sequence”
- **Table**: C_invoice
- **Sales Transaction**: Yes
- **Is rappel**: Yes

Save the record and the document type for rappels is available.
After saving it, it is necessary to select “rappel” in the field “Document Cancelled” and save again.

![document_type_new.png](/docs.etendo.software/assets/legacy/document_type_new.png)

> **Important**:
!!! warning
    For each organization, it is possible to configure only one "rappel" document type.

!!! info
    For more information, visit [Document Type](https://docs.etendo.software/en/financial-management-setup-accounting#document-type)

#### Rappel Configurations

In this window, the user can configure all the necessary aspects to grant rappels to certain business partners.

![rappel_configuration_window_new.png](/docs.etendo.software/assets/legacy/rappel_configuration_window_new.png)

##### Header

This window contains the general data of the configuration. The relevant fields are described below:

- **Name**: It indicates the name assigned to the rappel.
- **Currency**: The user can select the currency of the rappel.
- **Include Products**: The user can define if the selected products are to be included or excluded (“all excluding defined” or “only those defined”).
- **Include Product categories**: The user can define if the selected product categories are to be included or excluded (“all excluding defined” or “only those defined”).
- **Include Brands**: The user can select certain brands to be included or excluded (“all excluding defined” or “only those defined”).
- **Include Locations**: The user can select certain locations to be included or excluded (“all excluding defined” or “only those defined”).
- **Warehouse**: It provides information about the warehouse of the products. By default, this field is empty. This is the case except for invoices created from goods shipments.
- **Periodicity**: It provides information about the suggested periodicity of the rappel (“annual”, “biannual”, “monthly” or “quarterly”).
- **Type of Rappel**: The user can select the type of rappel, it can be according to the amount of the consumption or the quantity of products consumed (“amount” or “quantity”).

Once this information is completed, the user is able to save the configuration and use the buttons in the window to configure specific aspects of each rappel.

##### Buttons

At the top of this window, four different buttons can be found.

- **Add product categories**: With this button, the user can select one or more product categories and add them to the rappel.
- **Add products**: With this button, the user can add one or more products to the rappel.
- **Add partners**: With this button, the user can add one or more partners to the rappel, and a date from and a date to must be assigned to determine the validity period for the created rappel.
- **Copy rappel**: With this button, the user can copy the characteristics of an existing rappel to the selected rappel.

##### Tabs

- **Product Category**: In this tab, product categories assigned to the Rappel are shown. It is also possible to assign new categories from this tab.
- **Product**: In this tab, products assigned to the Rappel are shown. It is also possible to assign new products from this tab.
- **appel Parameters**: In this tab, the discount percentage, minimum and maximum amounts can be assigned to the rappel.
- **Business Partners**: In this tab, the business partner to which the Rappel applies is shown. Here, it is possible to select the “from date” and “to date”. This tab also contains a sub tab called “B. Partners Location”, where the location of the business partner is indicated.
- **Brand**: In this tab, the brands of the products to which the Rappel applies or not can be selected.

> **Important:**
> Remember that the options selected in the tabs “Product Category”,“Product”, and “Brand” must follow a certain logic: the priority is the option selected in the tab “Product Category”. This means that more specific filters apply to the included or excluded product categories.
>
> **Examples:**
> -When selecting the option “only those defined” in the fields “include product categories” and “include products” of the header, if in the “product category” tab the user selects “water”, and in the “product” tab the user selects “white wine”, the rappel will only include the products belonging to the category “water” and not “white wine”.
>
!!! warning
    -When selecting the option “All excluding defined” in the “Include product categories” field and the option “Only those defined” in the “include products” field, if in the “product category” tab the user selects “water”, and in the “product” tab the user selects “sparkling water”, the rappel will not include the product “sparkling water” despite what is defined in the “product” tab, since the priority is in the defined “product category”.

## Product Setup

### **Product Characteristic**

#### **Introduction**

Product Characteristic can be defined to complete the definition of a product using variants.

_Product Characteristics_ are attributes that can be added to the product definition to extend the description of each product. Examples of Characteristics are _Size_, _Color_, _Quality_, _Shape_ or _Weight_. These characteristics can be used later to filter or search products.

Once the definition of the characteristics is created, these can be assigned to a product and then create other products or SKU based on this **Generic Product** and its characteristics. This is a generic product where common attributes like tax or prices are defined. By default, products inherit all the attributes of the _Generic Product_ such as taxes, prices, etc. They can be overridden on each product. Generic products cannot be purchased or sold or used in any document.

For example, the Generic product _Shirts Summer Season 2013 by My Provider_ implements the Characteristics _Size_ and _Color_ as variants. This _Generic Product_ will have as Product Variant each combination of Color and Size.

#### **Characteristic**

**Characteristic Definition**

Field to take into account:

- **Variant**: When it is marked, it will explode/create combinations with its values. If it is not marked, it will not create combinations with other characteristics. For example:
  - Characteristic Color: Variant marked with value Blue and White
  - Characteristic Size: Variant marked with value M and L
  - Characteristic Fashion line: Variant is not marked with value Sport, Classic, Vintage
- **Explode Configuration Tab**: Flag available on Variant Characteristics. When it is checked, the values of the selected variant characteristic are automatically inserted in the _Characteristic Configuration_ tab when the variant is assigned to a generic product. If it is not checked, the values must be added manually.

These three characteristics are assigned to the product in this way:

- Color: Blue, White
- Size: M,L
- Fashion line: Sport

It will create four variants/products and for all of them with the characteristic Sport. We can say that a characteristic that is not a variant is like a tag that is added to each new product.

![](https://lh6.googleusercontent.com/cdjlrR76mBK3wKqB3XQ6bNRK_KDGSQ0EVVtc3t_SAYwPU_JW9f9aTb3RyiWfBiICaOuta8k49CiQN8FZ0--XfpKZ22cROG1FySev_r2sTdzSxoo_aegpn6sseo2efzfQXglibd6WknWTX05Ymg)

#### **Value**

Each of the values of a characteristic.

![](https://lh6.googleusercontent.com/T08VPSpQt04CjFcMqUGY5stqRukgrwkmbvB4vvZkbroD_H2vXSgKGlb5E8R8mFz7PPfOlxRatH0AQeNQ9iF0ciK6puVW5M7dn8PvXC25R8vcSfoxYDilZ3r8n985hnZN3evM1FuRxdMlUQdBpg)

Fields to be into account:

- Name: Value
- Code: To be used later when creating the variant. It will put in the _Search Key_ field
- Summary level: It is allowed to create a tree structure. For example, if the characteristic is color and for the same value(i.e Green) there are different references depending on the supplier:

![](https://lh5.googleusercontent.com/30qiD3TYly1aHtadA8da6N1on2NsS-24GPTMc4awiD1PJp8YlesaDaIZWxHD6GroXrmmQqlO009SZ21glwlNUwhVU3AWsNKyuyy-D-P0sypHrPr6pbXSI6Tzxn2WAF5dVFffLzWR_KFKSynaSA)

##### **Button Add Products**

The " Add Products" button is shown when a product characteristic value is NOT a "Variant", therefore it can be assigned to any product.

![](https://lh4.googleusercontent.com/IzWGMoCZ3c1nUm2OmvW-MWssK6KzQ1vdmYkLEjwqtOs4aLa_KnRpnZy-kA9YruqEuqstoyo7te-LG9nF3DVjHt7G08DzacTuATqMXW9SeVJ94VywvnPyTEywXyS9h4OaYv2BCAVbb0jy5eCD4Q)

It does not update current values. That is why the button only shows products where the characteristic is not assigned to.

- Scenario 1:
  - Product A has the characteristic Color (defined as variant) with values White, Pink, Blue and Black
  - After creating the product variants, the user creates the non-variant characteristic Fashion line: Women, Men
  - Non-variant characteristic can be assigned to the product in Product window by using Update Characteristics process button.
- Scenario 2:
  - Not variant product characteristic is created in Product Characteristic window as "Variant" = No.
  - Once a product characteristic has been entered in "Value" tab, a process button "Add Products" is shown.
  - "Add Products" button opens a pick/execute window where any product or set of products can be related to that product characteristic value.

#### **Subset**

A subset is a collection of values of a Product Characteristic.

Subset feature is a powerful functionality that allows the user to share the same characteristics for different purposes. For example, lots of colors and sizes can be created for different products:

- Color:
  - Green
  - Gray
  - White
  - Blue
  - Yellow
  - Red
  - Orange

But finally you have different products, for example t-shirts and pants:Subsets:

- Pants
  - Green
  - White
  - Gray
  - Blue
- T-shirts
  - Green
  - White
  - Orange
  - Blue

The aim of this feature is to avoid having duplicate values (blue, blue, green, green) because of different purposes. With this subset when selecting a product that is a pant, for example, instead of selecting the characteristic _Color_ you select the subset _Pants_. This way, instead of retrieving seven values, it will retrieve just four. Another advantage of doing this is when searching for variants instead of having blue two times (and you would not know if the blue is for pants or t-shirts), you will have blue one time. So when searching for variants which have the characteristics _Blue,_ the system will retrieve pants and t-shirts.

#### **Subset Value**

Each of the values of the product characteristic assigned to the subset.

![](https://lh6.googleusercontent.com/8qzF_YI5MuZAL78CRMbdJSNZ8du0swgIEukOgIlHQ_8LTQr1rvbhX2RtOoq9CkprpZaV-Y2nIJQZH40wX_ipyG5uIjKf7bGbA40ZwGQc_U2y1mUFllwYkid1BrbpCRn1ia5FpvwSSqGJCjI5nA)

- Sequence number: To order the way of seeing the values
- Name: Value. Notice that only values from the characteristic can be selected.
- Code: If it is filled, it will overwrite the code setup in the characteristic

#### **Filtering**

Fields based on columns whose reference is Product Characteristics can be filtered in grid assisted with a popup where the tree of available characteristics is displayed.

![](https://lh6.googleusercontent.com/c1KyrMrnAS9Ci-UjCi9mCzmMjtHi1layEkYHZWFvgdMoGTGyDW73G28ts-enKErw0xV02TJilqP4GYtWnvWU2VTw1-3CaLmwK_MkXzZd0ECboTr-10RBLFqT4vz4IrFIWZjpvW4kySrV734lkQ)

!!! info
    The characteristics available in this popup are limited to the ones applicable to data filtered in the grid where it is displayed with the current filtering criteria for the rest of the fields.

#### **Configuration**

Product Characteristics is ready to be used out of the box.

Anyway, some new features can be displayed as well with some simple configuration options (these changes need to be exported to the template).

##### **Improving product selector**

You can select between the different product characteristics using the product selector. There you have a column showing product characteristics description (See image).

![](https://lh4.googleusercontent.com/HuSSbpe8wKiBb3z_zy1u3J3Vpade6eOyRQSP28xLwU7-oWoIvIj3RtRDxCG73vVdQMRuN6AaJx51b0AZxqTaO7fJrqFbhd9mdRlXX7W99lFC6ZAVVV6GaRLGesNJZ-6drk9EVJnsd3fqCtsmUQ)

That is not the case when selecting from the suggestion box. There, just product names are used. Taking into account that the product with the characteristics share the name, it becomes impossible to distinguish one from another (See image).

![](https://lh3.googleusercontent.com/HpBpfokkfU8331lBrHV76V0Jx-n2fECiBH5Fi7-nTB8eghX3S9JBXgt7SNj3xbuJJJQ6pXfZ_k5nHqbcfAos8JUfAIDT-KcidMmxmYXh409vMtUHljjiqgokBwJwBLzJSYR0VposKg3MH2E9Iw)

User experience in this case would be completely different if products could be identified from the suggestion box (See image).

![](https://lh3.googleusercontent.com/toMnI_Io2di0EJVl4hcg8FejMI1Mji4mE4WwDzzA6F1xQtwVYVnCfXq63Y_irQ-Kd3kL6oBVE9oQ9AYk6OQ3bPgbY3wOivZK6LMsMRCJfpkydJzFTYSvMZt2wLpp-NrFIovQM4NEX0T_T3Ki4Q)

This can be easily improved by enabling some options of the selector.

Follow these simple steps to enable this configuration, and please do not forget to export those changes to your template.

- Log as System Administrator
- Go To Tables and Columns and select C_OrderLine
- Go to lines tab and select product (M_Product_ID)
- Navigate to selector (see image)

![](https://lh6.googleusercontent.com/N1WJZnz1jvs6oMx3ujSTNn9w6CBuKf1fzCFDRc8f8utnUhODwr8DIg8sz4kePzN-GQEClRIVfmV976AfLmAdd4lgmTLnrOt17IsBXRVvUwzw3C8mKGtsK3shjz_WhIhUvDTyJ5nzzTQ9tXpmIQ)

- Go to Defined Selector tab and then to Defined Selector field tab and select Characteristics Description field.
- Edit and flag "Search in suggestion box" and "Show in Picklist" check boxes (See image)

![](https://lh4.googleusercontent.com/VeWmotz-vCwIybOp0GCuBP7Bix5SLKwHh68bX2NpVZV1R4Co_k8pAfTI9dLENbG2XPf4RJ1RDg3cro74LxzywXIsLN8RkmjNvDXaDYrkXEazCJRZg3mkZt0oxNuBCGluasJb_00MRnN8KP-0ug)

- Last point would be to export these changes to the template. This is really important to avoid problems in future update processes and to keep these changes after the update.

### **Update Product Characteristics Description**

#### **Introduction**

Every variant has its product _Characteristic Description_ and this field is calculated automatically when:

- Variants are created
- When the value of a characteristic is change, for example from _Blue_ to _Hard Blue_

For example, if the characteristics of a variant are Color and Size and the values are Blue and XL the result of the description would be: _Color: Blue, Size: XL_

If later on you change Blue for Hard Blue, the new description would be _Color: Hard Blue, Size: XL_

In all of these scenarios, the _Characteristic Description_ is updated without the need of coming to this process.

This process should be used just in some special cases:

- When the name of the Characteristic is changed, for example from Color to Tint
- When through the database characteristics or values are changed

### **Unit of Measure**

#### **Introduction**

A unit of measure is a standard unit or combination of units to be used alongside the quantity of a product.

There are many units of measure which can be used to count product quantity on hand, or to purchase or sell a product.

Units of measure can also be used for measuring time. There are products such as services or resources which must be measured that way.

Below, you can find a list of the unit of measure you could setup in Etendo:

- **Unit**
- **Box**
- **Hour**
- **Kilogram**
- **KWh** (Kilowatt hour)
- **Litre**
- **Pallet**
- **Pack**
- etc.

#### **Unit of Measure**

Products of any type are managed in non-monetary units of measure.

![](https://lh5.googleusercontent.com/Iw-lfQm_nO_kWlUX4lMKyP1PLsGc2gK0pR-gdpvkELwuNVzmGdIs8uFhBLSMbGk9vlooN8WI_HV4cppv96lpvgGE6jy40utYqvHjJZI8RVyNSbAA0USOej4f1ZcyYslRe9mH3rMAwQhd31dvmw)

As shown in the image above, a non-monetary unit of measure can be created in Etendo by filling in below relevant data:

- the **EDI Code**, if any.
- the **UOM Name**
- the **Standard Precision** to be used while rounding calculated quantities of the products having that unit of measure
- the **Costing Precision** to be used while rounding calculated cost of the products having that unit of measure.
- and the **Symbol** or commonly used unit of measure abbreviation

#### **Translation**

Units of Measure can be translated to any language required.

The way to get that is as simple as:

- select first the language required
- and then enter the unit of measure translated into that language.

#### **Conversion**

Edit the conversion rate of one unit of measure into another one.

### **Product Category**

#### **Introduction**

Similar products can be grouped into different categories, which must be created with the aim of helping their management and analysis.

You may want to group similar products within the same category in order to get procurement and sales information summarized by each category. This is possible due to the fact that "Product Group" is one of the "Dimensions" of Purchase and Sales Reports.

To learn more, visit Procurement Analysis Tools and Sales Analysis Tools.

Besides, each product category allows the user to set up a different set of ledger accounts to be used while posting product related transactions such as purchase and sales invoices.

#### **Product Category**

Product category window allows the user to create and configure every product group your company may need.

![](https://lh5.googleusercontent.com/G_gS1HUEVZE4UMppe7SkmQXsZazw9xWDG8mQE-m9fmGzYn_Bwn8DdEE3m1I81RBebq9f7kD2NMrn6QhLMNAMNAu4_SAgrFv5Ag0h2bJLVb0K9ows2xpaDQLz3mtHsAceVkrMhPUcYBmNdZf_wg)

As shown in the image above, the creation of a product category requires entering below listed information for each category:

- a **Search Key** or short name which helps to easily find the category
- a **Name**
- a **Description**
- and the **Summary Level** flag which helps to arrange product categories into a hierarchical structure.

Product categories can be arranged into a hierarchical structure, which can be later on exploited by other reports or processes. For more information about how to work with trees, visit the Tree structure section.

#### **Accounting**

Each product category allows the user to configure a different set of ledger accounts.

![](https://lh5.googleusercontent.com/Ueek0FRoMRRlbjH2kzHNqRc-x6COVWDiR7oOOvRG3Z5zpeDyPJ1qV_cTafjT_eENf56h-1M7L3L4RkifbsuhC9-MGUexELBuzvaQwZkcpsYVT8sKuJAbcA0z28vzDPj7Lz9JVBFoFNRCLwKe9g)

There is a set of product related accounts which needs to be properly set up for the organization's general ledger configuration.

The "Copy Accounts" process of the Defaults tab of the General Ledger Configuration screen allows to automatically populate at least the mandatory ones shown in the image above.

The accounts automatically defaulted by Etendo can always be changed if required.

The whole list of product related accounts is:

- **Product Assets**: this field stores the default account to be used to record inventory transactions such as:
  - Inventory Counts
  - Inventory Movements
  - and Goods Receipt

This account is typically an asset account.

- **Product Expense**: this field stores the default account to be used to record product purchase expenses.  
  This account is typically an expense account.
- **Product Deferred Expense**: this field stores the default account to be used to record deferred expenses.  
  This account is typically an asset account.
- **Product Revenue**: this field stores the default account to be used to record product sales revenues.  
  This account is typically a revenue account.
- **Product Deferred Revenue**: this field stores the default account to be used to record deferred revenues.  
  This account is typically a liability account.
- **Product COGS**: this field stores the default account to be used to record the cost of the goods sold.  
  This account is typically an expense account.
- **Product Revenue Return**: this field stores the default account to be used to record sales returns.  
  This account is typically a revenue account.
- **Product COGS Return**: this field stores the default account to be used to record return material receipts.  
  This account is typically an expense account.
- **Invoice Price Variance**: this field stores the default account to be used to record price differences between posted Goods Receipts and booked Purchase Invoices.  
  This account is typically an asset account.

!!! info
    The "Copy Accounts" action button allows the user to copy the accounts defaulted in this window to the Product Accounting tab.

#### **Assigned Products**

Assigned products is a view of all the products which belong to a product category.

As a side note, not real products such as discount products should belong to a specific product group, named by example "Others", as a way of keeping them isolated from the real ones.

To learn more about discount products, visit Discount.

#### **Translation**

It maintains translations of Product Categories to different languages.

### **Attribute**

#### **Introduction**

Products can have an attribute or a set of attributes which makes them different to the rest.

An attribute is a feature of a product, such as color or size.

The capacity for managing product attributes allows a proper definition of the products and besides assure compliance with the tracking requirements imposed by the majority of industries.

Etendo allows managing product attributes by following below steps:

1.  Creation of every Product Attribute. An Attribute can be a unique identifier such as a Serial Number, or can have a predefined list of values such as blue, white and red colors.  
    To learn more, keep reading this section.
2.  Creation of Attribute Set/s which can contain just one attribute or mix a set of attributes.  
    To learn more, visit Attribute Set
3.  Set up the relationship between the product and the attribute set.  
    To learn more, visit Product

#### **Attribute**

Attribute window allows the user to create and edit attributes such as color or size to be assigned to attribute sets.

![](https://lh5.googleusercontent.com/KgY7LbRbBSeTKiXl8B-P3rCchmCaJNIgLI3-PCgZZTgJrWVJdtXsYP7yRTR6tYNF3i_T6LtO8PMtzJ8FTiu1P5KtQvQD1SacDNeHwRbNWnGPzOPv9tZ56WT-Fo05Nkxt-unkwXF9BBe0ag8sbw)

As shown in the image above, an attribute can be easily defined by entering the relevant data below:

- the **Name** of the attribute
- a short **Description** if required
- If the attribute is unique for each instance of the product, for example a lot number or a serial number, select the **Instance Attribute** checkbox.
- **List** flag allows the user to state that the attribute has a predefined list of values to be entered in the "Attribute Value" tab.  
  To learn more, visit Attribute Value.
- **Mandatory** flag defines the attribute as mandatory, therefore it must always be specified for the product.

#### **Attribute Value**

An attribute can have several values or individual characteristics to be detailed for each attribute.

Above applies to attributes such as color or size.

Attribute Value tab allows the creation of as many attribute values as required for an attribute.

### **Attribute Set**

#### **Introduction**

An attribute set can be defined by a single attribute or by a set of attributes to apply to specific products.

If **an attribute set** includes among others **an attribute which is unique for each instance of the product**, for example, a lot number or a serial number, this window is the place to define which **Lot Number Sequence** or **Serial Number Sequence** must apply to get that unique attribute.

The steps to follow are:

- **Creation of the Lot Number Sequence/s**. To learn how, visit Lot Number Sequence
- **Creation of the Serial Number Sequence/s**. To learn how, visit Serial Number Sequence
- **Set up the relationship between** the previously created **Lot/Serial Number Sequence/s** and the **Attribute Set**, in the Attribute Set window.  
  To learn how, keep reading this section.

#### **Attribute Set**

Attribute Set window allows creating as many combinations of attributes as required to define products with few or multiple characteristics.

![](https://lh5.googleusercontent.com/eFfHmZoippBAg2UAyKfVODqUewZCKUFQwC-0lr71L_P1uTZIN8khQzaIzN7cPdDoP7ZrlW7RkGUjq24Y2SB3vwd4_zYLHPYxEDxttakbcdEVhUm_oIMyzQeLAByyByHFmOZYit4L2GHp0fHJgg)

As shown in the image above, an attribute set to be assigned to a specific product/s can contain:

- a **Name** of the attribute Set
- a brief **Description** if needed
- a **Lot** or unique identifier given to a particular quantity of that product.  
  If **Lot flag is checked,** a new field named "**Lot Control**" is shown for you to select the Lot Number Sequence to follow by the products linked to that particular attribute set.
- a **Serial No** or a unique identifier given to each unit of the product.  
  If **Serial No flag is checked,** a new field named "**Serial No Control**" is shown for you to select the Serial Number Sequence to follow by the products linked to that particular attribute set.
- an **Expiration Date** or date upon which product quality is guaranteed.  
  If **Expiration Date flag is checked,** a new field named "**Guaranteed Days**" is shown for you to enter the number of days a product can be guaranteed.
- finally, the flag "**Require At Least One Value**" implies that at least one attribute set value will be required in product related transactions.

#### **Assigned Attribute**

An attribute set can have a single or a set of attributes assigned.

![](https://lh4.googleusercontent.com/JKPixcSV3hgLjW-UlwcYfpGHyrKD1pT39o4XAyHeltD26-0fx1Kn5wXESm5DPoJtrVMistsa0OaXEZKaYLcxAfOG--fJgVgcXZzDWVGvU5xemPX_SiOMMirw-aIuq17LxKfgKlQ0Q3w4q7N3nA)

As shown in the image above, an attribute set can have only one attribute, for example Color or as many attributes as required, for example Size, Lot Number and Serial Number.

The way to get that is just to select the previously created attributes in this tab.

You should take into account that:

- if one of the selected attributes is a "Lot" or a "Serial N?" type attribute, the corresponding Number Sequence must have been properly set up in the Attribute Set window.

### **Lot Number Sequence**

#### **Introduction**

A product attribute can be a Lot Number.

Some products require lot numbering to assure compliance with the tracking requirements imposed by the majority of industries, which implies that a given quantity of a product has always to be linked to a unique lot number.

#### **Lot Control**

A Lot Number is a unique number given to a particular quantity of a product, which can be defined to have a prefix or a suffix among other characteristics.

![](https://lh3.googleusercontent.com/zxXMUjr6dqf-ED398clHXDSahfNlz0oql8RmrUh4LopzsnqQ-wFiN-dP8Ss4YSbnYNA5k8UA1wdTE8uYU0SflUrJjuxkcBqgLrjxAb2yVTvglixLgh4gLQpu4gu9dASMfFCVavnkQldZGOvGGQ)

A Lot Number Sequence can be setup:

- by defining the first number or **Starting Number** that will be used as Lot Number
- by specifying the value by which the Lot Number will be **incremented by**
- by defining which is the **Next Assigned Number** that will be used. Etendo updates the next assigned number value as the Lot Numbers are assigned.
- by entering a **Prefix** such as **Lot N?/** which easily helps to understand that the number in question is a lot number.
- by entering a **Suffix** such as **/2011** which helps to provide additional information if needed.

### **Serial Number Sequence**

#### **Introduction**

A product attribute can be a serial number.

Some products require serial numbering to assure compliance with the tracking requirements imposed by the majority of industries which implies that:

- each unit of a product has always to be linked to a unique serial number.

#### **Number Control**

A Serial Number is a unique number given to each unit of a product/item which can be defined to have a prefix or a suffix among other characteristics.

![](https://lh6.googleusercontent.com/_I2P7xT_wcIiLPx2GnSTR3Ne4sqAemn-eWLFVQ1NKaTt_qHVVuQwKso1kczmCmlG6a3AyZeKI8iwolANuoRbYSd3RE0Fg5lmAIWc0kdvdjvPtgtD7cokdzHpLZ2yn3vrm9JM4nRAxYppGdOm8w)

A Serial Number Sequence can be setup:

- by defining the first number or **Starting Number** that will be used as Serial Number
- by specifying the value by which the Serial Number will be **incremented by**.  
  In the case of Serial Numbers it will always be "1".
- by defining which is the **Next Assigned Number** that will be used. Etendo updates the next assigned number value as the Serial Numbers are assigned.
- by entering a **Prefix** such as **Serial N?/** which easily helps to understand that the number in question is a serial number.
- by entering a **Suffix** such as **/2011** which helps to provide additional information if needed.

### **Brand**

#### Introduction

This window allows the user to enter brands associated with one product.
The brands are manufacturers or commercial names used by manufacturers to identify a product line.

#### Header

To use this functionality, select an organization and add a new brand in the corresponding fields. It is also possible to enter a description when necessary.

![](https://lh4.googleusercontent.com/aZfc6Qanmv-C8prh4FgF0KT-ykE3xADBzz57qx01JIBzwouPawsewFcMRjpJ5sN5_kT2VTxnNlwcTCnEYDNswMyijThPC8K634MtikPrLKcmBqYSQ08OH6ZYPedFBlir-8rueg7FQgv1ykKgekY)

## Pricing

### **Price List Schema**

#### **Introduction**

A price list schema is a template used to automatically populate a new version of a price list.

Price List management is not an easy task to handle, mainly in competitive markets where the margins are very tight.

Nowadays, organizations have to deal with a huge variety of products, which have different prices depending on the season and other pricing variables.

Etendo manages prices through three pricing related concepts:

- the **Price List**
- the **Price List Schema**
- and the **Price List Version**

And it allows the creation of:

- **General** Sales and/or Purchase Price List
- **Specific** Price Lists for a specific supplier or customer, or a group of them.
- **Based on cost** Price list based on product cost

The way these concepts work in Etendo is described below:

1.  **Creation of Price List/s**:
    1.  A "Default Price List Schema", with no configuration at all, is created by default after creating an organization.
    2.  The "Default Price List Schema" is the schema to be used in the creation of the price lists which are NOT a "Price List Version".
    3.  The Price Lists linked to the "Default Price List Schema" might contain both the net list price and the net unit prices of the products.  
        To learn more, visit Price List.
    4.  The Price list/s created can be linked to the business partners as required.  
        To learn more, visit Business Partner
2.  **Creation of Price List Schema/s**:
    1.  New Price List Schema can be created as a way to configure a set of commercial rules to be applied to existing price lists.  
        To Learn how, keep reading.
3.  **Creation of Price List Version/s**:
    1.  A new version of an existing Price List is created as a combination of a base price list and a given "Price List Schema".  
        To learn more, visit Price List.
    2.  The Price list/s versions created can be linked to the business partners as required.  
        To learn more, visit Business Partner.

#### **Header**

Price list schema window supports the creation of as many price list schemas as required with the aim of obtaining an easy management of price lists and price list versions.

![](https://lh4.googleusercontent.com/8dm__0RGCoicJS7A0HIQ2wiXDhVxmgxLG0KI3K3QcCW8LIHOvh-QaKXy12rE-WHLQkVlr476bjI-t7tX7Q877O_4-ek18q8CU8MGnz_tTNhFahwOAvn9co79yD-EKha4_NQvAfHwLOmGt0J49g)

As shown in the image below, the creation of a price list schema is as easy as to create it and give it a Name.

The set of price and discount rules which might apply to a set of product categories or specific products must be configured in the "Lines" tab.

#### **Lines**

Price list schema lines tab allows defining a set of price rules such as to apply a discount % to the net unit price of a given product category or specific product.

![](https://lh5.googleusercontent.com/1xuN1UnuUBcuYhWnHvIFMpKJ-OufSVW9rM0t-Otml29IRjyIQ5gjF3gIHNu1BdwLNikv9n3_5XmZ3rxWMDvg6Ig80WHdzCkEQI2q4cLeQ4Cbl_W3KVnYszYbQHJffZumj85Y1Q1RJjd_bFOp7w)

First thing to notice is that, as shown in the image above, "Lines" tab is split into two sections:

- the first section allows the user to:
  - Inform Etendo about:
    - the "Business Partner" and/or
    - the "Product Category" and/or
    - the "Product"  
      to which the price/discount rules to be defined in the next section are going to apply.
- the second section allows the user to:
  - configure which price of the existing price list is going to be taken as "Base List Price" in the new price list version. The options available are:
    - **Net List Price** which is the price published in the price list
    - **Net Unit Price** which is the final price used in purchase and sales order/invoice lines
    - **Fixed Price**, as it is possible to configure that for the new price list version, therefore the net list price is equal to a given fixed price.
    - **Cost**, which is the price published in the price list, will be the product cost (costing tab in product window) and a margin.
    - **Fixed Price or Cost Based** combines the previous two options with the following condition:
      - If the fixed price is higher than the cost, then the defined fixed price is selected.
      - If the fixed price is lower than the cost, then the cost (plus the defined margin) is selected.
    - **Fixed Price or Cost plus Margin Based** combines fixed price and cost options with the following condition:
      - If the set fixed List/Unit price is higher than the current cost plus List/unit Price margin, the price list will be created with the fixed price.
      - If the set fixed List/Unit price is lower than the current cost plus List/Unit Price margin, then the price list will be created using the cost plus the margin.
  - configure which price of the existing price list is going to be taken as "Base Unit Price" in the new price list version. The options available are the same as above:
    - **Net List Price**
    - **Net Unit Price**
    - **Fixed Price**, as it is possible to configure that for the new price list version, the net unit price is equal than a given fixed price
    - **Cost**
    - **Fixed Price or Cost based**
    - **Fixed Price or Cost plus Margin Based**
  - configure the discounts if any to apply to the net unit price and/or to the net list price in the fields:
    - **List Price Discount %**
    - **Unit Price Discount %**
  - configure the margin on the product cost to apply to the net unit price and/or to the net list price in the fields:
    - **List Price Margin %**
    - **Unit Price Margin %**

Second thing to notice is that the set of price rules and/or discounts could be configured in a "hierarchical" way, that's line by line or applying the last valid price rule (non-hierarchical way).

!!! info
    The Enable Hierarchical Price List preference is available in order to select the desired behavior applying the price list rules.

Let us imagine that the rules which need to be part of a price list schema are:

- to apply a net unit price discount of 5% to the products which belong to a Product Category X.
- to apply a net unit price discount of a 10% to the products which belong to the Product Category Y.
- to apply a net unit price discount of 15% to the Product X that belongs to Product Category X.

The way this works in Etendo is:

- the price list schema must contain 2 lines one per each discount rule to be applied:
  - First Line will contain information such as:
    - Sequence Number = 10
    - Conversion Rate Type = Spot
    - Product Category = Product Category X
    - Base Net Unit Price = Net Unit Price
    - Net Unit Price Discount = 5.00
  - Second Line will contain information such as:
    - Sequence Number = 20
    - Conversion Rate Type = Spot
    - Product Category = Product Category Y
    - Base Net Unit Price = Net Unit Price
    - Net Unit Price Discount = 10.00
  - Third Line will contain information such as:
    - Sequence Number = 30
    - Conversion Rate Type = Spot
    - Product Category = Product Category X
    - Product = Product X
    - Base Net Unit Price = Net Unit Price
    - Net Unit Price Discount = 15.00

Using hierarchical behavior:

- unit price discount of 5% is applied to the products which belong to a Product Category X.
- unit price discount of 10% is applied to the products which belong to a Product Category Y.
- unit price discount 15% is applied to Product X, in addition to the 5% discount for belonging to Product Category X.

Using non-hierarchical behavior:

- unit price discount of 5% is applied to the products which belong to a Product Category X, except to Product X.
- unit price discount of 10% is applied to the products which belong to a Product Category Y.
- unit price discount of 15% is applied to Product X.

### **Price List**

#### **Introduction**

A price list is a listing of prices for different products or services.

!!! info
    It is possible to create as many price list and price list versions as required depending on the organization's needs.

The process of creating a price list is slightly different to the process of creating a price list version.

Price List creation:

1.  Price List Name and Type (sales or purchase) is detailed in the Price List window header. It is also mandatory to define whether the price includes taxes or not.
2.  There exists the possibility of Price list based on cost, for this, the price list should be a sales price list.
3.  The Default Price List Schema with no configuration at all, as well as the valid from date information, must be detailed in the Price List Version tab
4.  The Unit / List price of each product which must be included in the price list is detailed in the Product Price sub-tab.
5.  The price list is ready and can be linked to the business partners as required and used.

Price List version creation:

1.  Price List Name and Type (sales or purchase) is detailed in the Price List window header.
2.  A Price List Schema which contains the new commercial rules to apply, the valid from date and the Base Price List for which the price list version is created and must be detailed in the Price List Version tab.
3.  The process Create Price list populates the "Product Price" tab by including:
    1.  every product contained in the original price list
    2.  each product will have a new unit and/or list price, depending on what was configured in the price list schema used.
4.  The price list version is ready and can be linked to the business partners as required and therefore used.
5.  Documents will automatically default the most recent version of a price list.
6.  There is no end date on price list versions, but old versions can be deactivated.

#### **Price List**

Price List window allows creating purchase and sales price lists to be assigned to the business partners for its use in purchase and sales transactions such as orders and invoices.

![](https://lh5.googleusercontent.com/bHmRBT-3YqtSLK2PErojCQx8-FE-6UJK0_A3mkisnphxh5R2A7qev8UsVYgo9x7o8xbHuvmIhYY9ijGcJ9tymlAeIUqaNHJCOVNlXTv58MpI1iBTJ3ppDjXB0s_3ZXMro8cp8tS3d4oqD4_hHw)

As shown in the image above, a price list or a price list version can be created by just entering below relevant information:

- By selecting the field "**Sales Price List**" it will be for sales transactions, otherwise it will be a purchase price list.
- **Default** field allows defining a given price list as the default one to be used in case a business partner does not have a specific price list assigned.
- **Price list based on cost**, this field is shown if the price list is a Sales Price List. This option allows creating a price list based on the cost price plus a margin.
  - the cost price is the one defined in the Costing tab of the product window.
  - the margin is defined in the Price List Schema window.
  - when the price list is a price list based on cost, the price list schema should be configured with cost and a margin.
- **Price includes taxes**. This flag is very important and depending on this the behavior of sales and procurement flows will be affected.
  - If it is marked, then the price defined is the gross unit price
  - If it is not marked, then the price defined is the net unit price

**How does this affect the flows?**

- When the price list includes taxes, the _gross unit price_ and _line gross amount_ are filled and the _net unit price_ is calculated based on the _gross unit price_ and the corresponding tax rate. What cannot be changed is the gross and, due to this, there might be some rounding issues that the system automatically handles adding or subtracting these differences in the tax amount.

As an example : If price inclusive of tax is originally 135.50 and rate is 4.5 % then the rounded price before tax would be 129.67

The order line would stay:

Quantity: 1 Net Unit Price: 129.67 Line Net Amount: 129.67 Gross Unit Price: 135.50 Line Gross Amount: 135.50

But the total gross amount (calculated by the system) would be 135.51 (tax base amount:129.67 + tax amount:5.84) and what it has to be clear is that the final result must be 135.50 (The customer bought 1 unit whose price is 135.50). This difference is going to be solved adjusting taxes:

The system will adjust the difference by summing or subtracting this difference with the tax that has the highest amount. So, in this example, instead of having a tax line where the amount is €5.84, the amount will be €5.83 (5.84-0.01)

Finally, the total gross amount for the sales order would be 135.50 (129.67+5.83) which is the desired amount.

Due to this (Net amount vs Gross amount), when using prices that include taxes, it is recommended to work with greater precision (price precision) to avoid rounding differences.

- When the price list does not include taxes, the _gross unit price_ and _line gross amount_ fields are not displayed and both fields are not calculated at all in the line of the document. The final gross amount of the document will be the result of the sum of the lines net amounts plus the tax amounts.
- The price list is defined at document level (header) so there cannot be lines where the price includes taxes and others where not. This is clear for orders, but for invoices where orders can be grouped in one just invoice the rule is also applied. One invoice cannot have orders where the price list includes taxes and orders where the price list does not include taxes.

#### **Price List Version**

There could be as many versions of an existing price list as required, versions which can be valid for a given time period and which can be defined according to certain commercial rules.

![](https://lh3.googleusercontent.com/ix0WIF0unAQdEluAH0VKvAHPQFFb5f6V5DlOMcJlQVi54MtuV41UG8GUHy1aHghfH4CH5Iz100WDv3Q8-fF_rPaNDGuFvqWwnTmVKxdNDFCSXnQFM3TAhlcxHapRGH4a7K2nXQVkk0lkuPJ1NQ)

As shown in the image above, there are two types of "Price List Versions":

- generic and original ones linked to the "Default Price List Schema"
- further price list versions (not based on the cost) which requires both:
  - a Price List Schema
  - and a Base Price List version
- price list versions based on cost require a Price List Schema with Cost configuration in Base list price and Base unit price.

The process button named "Create Price List" must be used only in the case of creating further price list versions as it requires a Base Price List if the price list is not based on cost. If the price list is based on cost, it is mandatory to select the price list schema and optionally the base version.

- if Base version is blank, the application calculates the unit price and list price for all the products (excluding discounts products) plus the margin defined.
- if Base version value is selected, the application calculates the unit price and list price for all the products defined in the base price list as cost plus margin.

#### **Product Price**

Product Price tab allows the user to either add or edit products and their prices for a selected price list.

![](https://lh3.googleusercontent.com/rapFdQYs8ZYQ3c9wO_nEZ-tTniv5PDDLmdlXZ03ByVKh6Im-Jwt2KIB1Rj1Hm1agjXK55WcmCR6Xok4iO4s3zlRoP1TK-C6rh6oJSIBNVEdEcBRJB4OHbEtWV-7ZE8slY7CahOj4x7wU9GBuow)

In other words:

- Add products in the case of creating a price list
- Edit products in the case of modifying a price list version:
  - as the required products at their new prices are automatically populated by Etendo in this tab while running the process "Create Price List".

Overall, this tab includes two main fields:

- 'the _List Price'_ field, as the price used as a reference in a given price list or price list version. This price can be the result of a discount or any other commercial rule applied by a Price List Schema.
- and the **Unit Price** field, as the final price used in documents such as orders and invoices. This price can be the result of a discount or any other commercial rule applied by a Price List Schema.

### Create all price lists

#### Introduction

On daily sales, especially on retail and distribution, price lists are very important. Therefore, Etendo includes plenty of information to manage and update price list versions per business partner.

This functionality includes different price lists, price list versions per each price list and price list schemes. Have a look at these concepts to better understand Create all Price Lists functionality.

Etendo allows hierarchical price list structure and this hierarchy is based on price list schemes.

##### Functionality

Follow this example about what _Create all Price Lists_ is used for:

Example 1:

Imagine you own a bakery and you sell different bread types to different customers. You may have French bread, rolls, bagels, etc. And for each type you may have different sizes small, medium and extra.

You use a main price list (with a price list version) containing a price per bread when they are medium size. Based on this price list we build 2 other price lists applying a price list schema. For small bread, 5% off and for extra breads 4% more. This way, you will be able to manage price updates easily. Suppose flour price rises 10%, and you want to increase all prices for all breads. You could follow this steps:

- Create a new price list schema increasing the price 10%.
- Create a new version for the main price list, based on the new price list schema.
- Regenerate all price lists based on the main price list automatically. For this third step, you may use the Create All Price Lists feature.

##### Process

The Create All Price Lists generates all price lists pending from the selected price list. The process checks for all child price lists, and applying the defined price list schema, it generates a new version for each price list.

![](/docs.etendo.software/assets/drive/1gcdIPde692fCVAn9cq0PEXTyJBTBR9vT.png)

![](/docs.etendo.software/assets/drive/1JC58tbBLqjqN5hDZv5Puwp_lAmDafJqd.png)

### **Discounts and Promotions**

#### **Introduction**

Discounts and Promotions is a mechanism that allows the user to adjust prices based on different rules. External modules can extend this definition by providing additional rules (Discount Types) implementations.

Discounts and Promotions, formerly Price Adjustments, defines rules to be applied to invoice and order lines to adjust prices.

![](https://lh6.googleusercontent.com/ls88i8jyKuvAYSUkKg3hrJyY9FkEKi8kj9CkQI0hn-YdEggr1Qd25cPG13CO5Y-jVh5L6w6X-Nlnc7l_7ht0zRV8_4TYSYs-_V7JrZxIkIxmK5XS_KS60noJsXVwMK5FWbeKtEctt6kpiZsEqw)

This feature requires to set as "Active":

- the "Read-Only" Tab "Discounts and Promotions" is found in below listed windows:
  - Purchase Order
  - Sales Order
  - Purchase Invoice
  - Sales Invoice
  - and Sales Quotation

##### **How Promotions are applied**

Rules are applied to order or invoice lines based on the filters in that rule, for example to a specific Business Partner Category acquiring a concrete set of products during a fixed period of time.

When the line is saved, the actual price shown in it does not take into account promotions. Promotions are calculated when the invoice/order is processed or by clicking the _Calculate Promotions_ button.

!!! info
    _Promotions and Discounts_ can be extended to implement complex rules that attend not to a single line but to all lines in the invoice, being impossible for those to be calculated in advance. 

Etendo manages prices in 3 chunks:

- Price List: it is the base price defined as Product Price. It is the base price reference.
- Price Standard: it is the first discount applied to the price. It can come directly from the Price List, or can be manually edited while entering the line.
- Actual price: it is the real price that will be used in the document. Promotions are applied to the Price Standard to obtain this one.

Multiple promotions can be chained in cascade, in this case the one applied in 2nd position will use as base the actual price obtained after applying the first one. An alternative mechanism to apply promotions in _WebPOS_ is implemented by the Promotions Best Deal Case module.

##### **How Promotions are defined**

The main fields to take into account when defining a promotion are:

- _Name_ and _Printed Name_: is the way to identify the promotion. _Printed Name_ is used to display the rule to the final user, whereas name is intended for internal usage, although in case _Printed Name_ is empty, _Name_ is used instead.
- _Filter Options_ section: filter options configure in which cases it can be applied.
  - _Starting_ and _Ending_ dates: The period of time the promotion is valid.
  - _Priority_: As explained in the previous section, multiple promotions can be applied in cascade. _Priority_ field defines which is the order these promotions are applied in. When more than one promotion can be applied to a single line, these promotions are sorted by ascending priority, this is, the promotion with priority 1 will be applied before the one with priority 2.

!!! info
    Note it is very important to set priority in case of defining rules that can be applied in cascade.

- _Apply Next_: It allows stopping the promotion cascade chain. When it is flagged, in case   there is another promotion that is applicable, after applying the current promotion, it will be applied. If it is not flagged, this rule will be the last in the chain.
- _Included method_: There are 6 drop down fields to define how _Business Partner Categories_, _Business Partners_, _Product Categories_, _Products_, _Price Lists_ and _Organizations_ are filtered. The actual values for the filters are added in the subtabs with the same names, these fields only define the strategy to filter each of them, values here can be:
  - _All excluding defined_ (default value). It removes from the filter the items selected. For example if we set it to products and add product A, the promotion will apply to any product but A. Note this is the default value for all filters, in case it is left as it is for all of them, and no filter option is added in any sub tab, the promotion will be always applicable.
  - _Only those defined_: Restricts the filter to just the items that are included in the correspondent sub tab.
- _Definition_ section: Fields shown in this section vary depending on the selected promotion type. Here it is typically defined how much to discount and additional conditions to be met to apply the rule.

##### **Price Adjustment**

_Price Adjustment_ is the promotion type included by default, it behaves almost in the same way _Price Adjustments_ did before they were extended to _Promotions and Discounts_.

As opposed to the rest of Promotions and Discounts, in order to maintain backwards compatibility, prices with adjustments are calculated while the order/invoice line is being edited. So the final price is shown there even before processing it. Promotions and Discounts lines are not created until the document is processed.

!!! warning
    Due to this different behavior between Price Adjustments and the rest of Discounts and Promotions, it is advisable not to use both of them together, so in case Price Adjustments are defined and applied, do not define other types to be applied to the same products.

To define a promotion of _Price Adjustment_ type, follow the indications in the section above for filtering. In the _Definition_ section these are the fields to be taken into account:

- _Discount Amount_: It is a fixed amount discounted to the price.
- _Discount %_: Percentage discounted to the price. In case _Discount Amount_ field is not 0, percentage is applied to the price obtained after subtracting _Discount Amount_ value.
- _Fixed Unit Price_: Sets the price per unit. If this field is set, the two mentioned above are not used.
- _Min_ and _Max_ quantities: Specifies which is the quantity range to apply the rule, values here are included and any (or both) of them can be empty. For example, a promotion with _Min Quantity_ 5 to product A (which UOM is unit) would apply whenever there is a line with 5 or more units of product A.

#### **Discounts and Promotions**

Defines the Discounts and Promotions main characteristics such as Discount Type, how it is filtered and actual discount information based on type.

#### **Translation**

Maintains translations of Discounts and Promotions to different languages.

#### **Business Partner Category**

The user can add business partner categories in order to include or exclude them from a selected Promotion/Discount.

#### **Business Partner**

The user can add business partners in order to include or exclude them from a selected Promotion/Discount.

#### **Business Partner Set**

The user can define business partner sets for the discount.

#### **Product Category**

The user can add product categories in order to include or exclude them from a selected Promotion/Discount.

#### **Products**

The user can add products in order to include or exclude them from a selected Promotion/Discount..

#### **Price List**

The user can add price lists in order to include or exclude them from a selected Promotion/Discount.

#### **Organization**

The user can add organizations in order to include or exclude them from a selected Promotion/Discount.

### **Service Price Rule**

#### **Introduction**

In this window Price Rules assigned to Price Rule Based services will be configured. Instead of having a fixed price, there will be rules that will determine the price of the Service.

#### **Service Price Rule**

![](https://lh6.googleusercontent.com/X9LCI62xbhWb8fv-Kd56CnOQGzy2Bw1KXj1frgulzwbMa3UkXVFW2GtKdR1a0-BIXVVRePT4wgfzFCFI8LpQAZv66zLqQTzVV_5LuiBKK8wZecnNvki6Pu3rJ-4OBccqbSfCm45H2zJ4eX4xgw)

Configuration fields:

- **Name**: Name of the Service Price Rule.
- **Description**: Description of the Service Price Rule.
- **Rule Type**: There are two values to select in the dropdown
  - Percentage: If selected, a Percentage field will be displayed allowing to set a Percentage. To determine the price of the service, this amount will be applied to the amount of the lines related to the service.
    - **Percentage**: Percentage to be applied.
    - **After Discounts**: If selected, the percentage will be applied after adding the discounts to the ticket.
  - **Ranges**: If selected, a new tab Ranges will be displayed allowing to create different Ranges based on the amount of the related lines.

#### **Ranges**

![](https://lh4.googleusercontent.com/QwjLn0C5fh2kKYl7P1q381tMurECKsFm_xLVCviWtFqf48yaxSa0PfpjwM80ji2kQQmDQC3VQVL6YQYyRu9y39AgLl19QBGYO4E2iAXV7cC1qINdvHtHTYAQGmQCDrVeqBr-Jnhd_TVcKDDWcw)

In this tab, different Ranges can be created based on the amount of the related order lines. Configuration fields:

- **Amount Up To**: If the summed amount of related order lines is equal or less than this amount, the configuration of this range will be taken into account.
- **Rule Type**: There are two values to select in the dropdown
  - Percentage: If selected, a Percentage field will be displayed allowing to set a Percentage. To determine the price of the service, this amount will be applied to the amount of the lines related to the service.
    - **Percentage**: Percentage to be applied.
    - **After Discounts**: If selected, the percentage will be applied after adding the discounts to the ticket.
  - **Fixed Price**: If selected, a field ‘Price List’ will be displayed.
    - **Price List**: Price List from which the price of the service will be obtained.
