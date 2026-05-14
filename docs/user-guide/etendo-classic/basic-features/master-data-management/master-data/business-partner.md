---
title: Business Partner
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Customer
  - Vendor
---

## Business Partner

:material-menu: `Application` > `Master Data Management` > `Business Partner`

### Overview

Business partner master data window is the place where the user can easily organize and centralize business partner data.

Etendo allows the user to enter business partner master data information whenever it is needed as the business takes place, therefore the procedure described below explains how to set up a single business partner of any type.

### Header

Here, the user can define and configure business partners to be later used in transactions.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-1.png)

Fields to note:

- **[Business Partner Category](../business-partner-setup/business-partner-category.md)**: Key field for the user to select a category which the business partner is going to belong to, under the following types:

    - Customers
    - Suppliers
    - Employees

- **Search Key**: or short name which will help you to identify and search a given business partner
- **Commercial Name**
- **Fiscal Name**: if known. If it is known, it is the one used in official documents such as invoices and tax reports, otherwise the commercial name will be used instead.
- **Description**:  used to describe the business partner, if needed.
- **URL**: The business partner URL, if known.
- **Reference No**: which can be used as an additional way to identify a business partner.
- **Consumption Days**: information which will be used while creating sales or purchase orders for that particular business partner, by using a process named *Copy Lines*.  
    
    !!! info
        For more information about this process, visit [Sales Order](../sales-management/transactions.md#sales-order) and [Purchase Order](../procurement-management/transactions.md#purchase-order) sections.

- **Credit Line Limit**: Etendo will inform whenever the credit limit entered in this field for the business partner is over while booking sales invoices.
- **Consent for Customer Data Processing**: Checkbox in the business partner data model, to reflect whether a given contact consents or not that their data can be used by the organization. 

### Buttons

**Set New Currency**

Business partner currency is automatically filled in with the currency of the Price List assigned to the business partner. Once filled in, it can be changed, if required, by using the **Set New Currency** button.

!!! note
    Normally, business partner currency is the same as the currency of the price list assigned to it. However, it can happen that a business partner having, for instance, an EUR price list assigned, might have USD as its by default currency. In that case, all the transactions booked in EUR for that business partner, will be exchanged to USD, therefore, the business partner balance is calculated in USD.

The **Set New Currency** process allows defining:

- a new currency for the business partner
- as well as the currency conversion rate to be used to exchange customer balance to the new currency.

    ![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-2.png)

Fields to note:

- **Currency**: Business partner's new currency can be entered here, for instance *EUR*. At first, the currency shown in the Set New Currency window is business partner price list currency, in our example *USD*.

- **Set Amount**: Checkbox. If selected, Etendo will update the Business Partner's balance with the amount entered in the Foreign Amount field, so they stay consistent with the new currency. 

- **Foreign Amount**: Only shown if the **Set Amount** checkbox is selected. Here, Etendo allows the user to manually enter the equivalent amount in the new currency that will replace or update the Business Partner's balance.

- **Use default conversion rate**: Checkbox. It uses the conversion rate defined in [Conversion Rates](../general-setup/application/conversion-rates.md) window, to recalculate business partner balance from USD to EUR, in our case. If this check is not selected, a new field *Rate* is shown to allow entering a specific conversion rate.

Additionally, a business partner might have **available credit in a given currency**. If that is the case, Etendo informs the user because business partner available credit will have to be exchanged to the new currency, therefore it can be consumed in the new currency.

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-3.png)

This process automatically creates three new payments, in case business partner has available credit:

- a **GL Item payment** in EUR, that moves credit amount to the ledger account defined in the selected G/L Item, in the *CREDIT*.
- a **refunded payment** in EUR, that moves credit amount to a prepayment account in the *DEBIT*.
- and a **Zero** amount payment that is a credit payment in USD (new currency). This credit payment moves the credit amount to a prepayment account in the *CREDIT*.

!!! Example
  
    Let us take as an **example** a business partner having a price list in EUR

    - Price list currency: EUR
    - Current balance: 306.00 EUR
    - Available credit: 100.00 EUR

    Because the credit reduces the balance, the net balance is 206.00 EUR (306.00 – 100.00).

    **Running Set New Currency**

    The company decides that this Business Partner should now operate in USD, so the user runs the Set New Currency process and selects USD as the new currency.

    Etendo detects that the partner still has available credit in EUR.
    That credit must be converted into the new currency, so the system applies the conversion rate 1 EUR = 1.19 USD.

    **What Etendo Does Automatically**

    Once the process finishes:

    - The Business Partner's currency changes from EUR to USD.
    - The current balance becomes 245.14 USD, calculated as 206.00 EUR × 1.19 = 245.14 USD
    - Etendo also creates three automatic payments to properly move the available credit from EUR to USD, keeping accounting consistent.

    **Future Transactions**

    Now that the Business Partner's currency is USD, let's see what happens with new invoices:

    - You create a new sales invoice in EUR (because the price list is still in EUR).

        - Invoice total: 41.50 EUR
        - Etendo converts it to USD: 41.50 × 1.19 = 49.38 USD

    - The Business Partner's new balance becomes: 245.14 + 49.38 = 294.52 USD

    - Later, you create another sales invoice in USD for 100.00 USD. While completing it, Etendo shows that the partner has available credit in USD, converted from the old EUR credit: 100 EUR × 1.19 = 119.00 USD

    ![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-4.png)

    In short, the Set New Currency process updates the Business Partner's currency and converts balances and credits to the new currency using the chosen rate, existing balances and available credit are recalculated so everything matches the new currency and future transactions, even if created in the old currency (EUR), will still be correctly converted and reflected in the Business Partner's new currency (USD).


### Tabs and Subtabs

It is not the same to enter and configure a customer than a supplier/creditor or an employee, that is the reason why the Business Partner window has three main tabs and therefore subtabs which allow you to set up each main business partner type separately:

- **Customer** 
    - Customer Accounting
- **Vendor**
    - Vendor Accounting
- **Employee**
    - Employee Accounting

The tabs and subtabs mentioned above are described in the next chapters of this section.

!!! Important
    
    There could be other types of business partners which require to be set up as business partners in this window; business partners which have nothing to do with either a customer, or a supplier/creditor or an employee.

    That is the case of banks. Banks need to be created in the business partner window header by just entering basic header information and no data in any of the business partner window tabs, but Location and Contact. The reason for this is that *Bank* type business partners are needed in the [Remittance](../financial-management/receivables-and-payables/transactions/remittance.md) financial workflow.

    For more information about this workflow, visit [Financial Account](../financial-management/receivables-and-payables/transactions/financial-account.md).

#### Customer

!!! note
    Customer related data can be entered and configured once the **Customer** checkbox is enabled.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-5.png)

As shown above, there is a list of relevant data to be entered for customers together with current customer balance information. You could either select any data such as Price List from a previously created list of values, or, if necessary, create it by navigating to the corresponding window, and then select it.

Fields to note:

- **Price List**: The one selected will be the one applied while creating sales documents such as sales    orders or sales invoices for that customer.  

    !!! info
        For more information, visit [Price List](../pricing/price-list.md).

    Price lists are defined in a given currency, which could be the same as customer currency or not.  
    In case it is not, customer balance will be calculated by taking into account either the conversion rate defined in the [Conversion Rates](../general-setup/application/conversion-rates.md) window or the one entered in the process **Set New Currency** which can be run to change the currency of a business partner.

- **Payment Method**: The one selected will be the one applied while creating and managing the payments received from that customer.  
    If a Financial Account is linked to the customer, the payment method to select here will be one of the payment methods linked to the financial account.

    !!! info  
        For more information, visit [Payment Method](../financial-management/receivables-and-payables/setup/payment-method.md).

- **Payment Terms**: The one selected will be the one used while managing sales invoices payment plan.

    !!! info
        For more information, visit [Payment Term](../business-partner-setup/payment-term.md).

- **Financial Account**: The one selected will be the one used while collecting and reconciling the payments made by that customer. 

    !!! info
        For more information, visit [Financial Account](../financial-management/receivables-and-payables/transactions/financial-account.md).

- **Invoice Terms**: There are few invoice terms which can be used while generating sales invoices.

    !!! info
        For more information, visit [Generate Invoices](../sales-management/transactions.md#generate-invoices).

    - **After Order Delivered**: The invoice could be automatically generated once all the goods of the sales order have been shipped
    - **After Delivery**: The goods of the sales order will be automatically invoiced as they are shipped, even if there are partial shipments
    - **Do not invoice**: No invoice will be generated automatically
    - **Immediate**: The invoice will be generated on the next run of the Generate Invoices process.
    - **Customer Schedule after Delivery**: The invoice will be generated according to the calendar agreed with the customer and once the goods ordered have been shipped.  If this is the option selected, a new field named *Invoice Schedule* is automatically displayed for you to select the corresponding *Invoice Schedule* or calendar.

        !!! info 
            For more information, visit [Invoice Schedule](../business-partner-setup/invoice-schedule.md).

- **Credit Line limit**: If the sum of all pending payments is over the credit limit specified for a customer, the system will alert you by saying that this customer has reached the credit limit whenever this business partner is selected in a sales document (order, shipment or invoice).

- **Tax Exempt**: To define a customer as Tax Exempt whenever applicable, therefore only those Tax rates also defined as exempt apply.

- **Sales Representative**: Here, the user can select a customer sales representative. A sales representative is an employee set as such.

- **On Hold**: This checkbox allows blocking a customer, therefore some specific documents cannot be fulfilled for it. If checked, the On Hold section is shown with the following setup, which can obviously be changed as required:
    - **Sales Order:** Blocked
    - **Goods Shipment:** Blocked
    - **Sales invoice:** Blocked
    - **Payment In:** Not blocked

    Above defaulted configuration means that it is not possible to complete either a sales order, a goods shipment or a sales invoice for the customer, only receiving a payment is possible.

**More information** section

- **SO BP Tax Category**: This field can be found under the *More Information* section.  
    You can use a business partner tax category to get that the sales documents created for a customer can only have a specific set of tax rates linked to that tax category.  
    
    !!! info
        For more information, visit [Business Partner Tax Category](../financial-management/accounting/setup/business-partner-tax-category.md).

- **Maturity Date 1**: It indicates the day of the month, the first deadline, that invoices are due.

- **Maturity Date 2**: It indicates the day of the month, the second deadline, that invoices are due.

- **Maturity Date 3**: It indicates the day of the month, the third deadline, that invoices are due. 

- **Birthdate**: Data about the customer.

- **Birthplace**: Data about the customer.

**Customer Accounting**

The Customer Accounting tab allows the user to configure the ledger accounts to be used while posting customer related transactions such as customer receivables and customer advances to the general ledger.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-6.png)

As shown above, you can configure, for each customer and general ledger, the accounts to be used in:

- the **Customer Receivables** transactions such as sales invoices posting.

    !!! info  
        For more information, visit [Sales Invoice](../sales-management/transactions.md#sales-invoice).

- the **Customer Prepayment** transactions, such as those cases when the company shipping the goods requires the customer to advance part or full amount of the debt.  

At first, these accounts are inherited from the Defaults accounts of the organization's general ledger for which the business partner is being created. The user can always change them.

!!! important
    It is possible to configure the creation of new correlative accounts for the business partners as described in the General Ledgers tab of the [Organization](../general-setup/enterprise-model/organization.md) window.

#### Vendor/Creditor

!!! note
    Vendor or Creditor related data can be entered and configured once the **Vendor** checkbox is enabled.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-7.png)

As shown in the image above, there is a list of relevant data to be entered for suppliers or creditors, also known as vendors:

- **Purchase Price List**: The one selected will be the one applied while creating purchase documents such as purchase orders or invoices for that vendor.  
    If a Business Partner has already generated Credit, it will not be possible to select a Price List in a different Currency from the generated Credit. In that case, it is possible to convert Credit to a different Currency.  
    
    !!! info
        For more information, visit [Price List](../pricing/price-list.md).

- **Payment method**: The one selected will be the one applied while creating and managing the payments    made to that vendor.  
    If a financial account is linked to the vendor, the payment method to select will be a payment method linked to that financial account.  
  
    !!! info
        For more information, visit [Payment Method](../financial-management/receivables-and-payables/setup/payment-method.md).

- **Payment Terms**: The one selected will be the one used while managing supplier invoices payment plans. 

    !!! info
        For more information, visit [Payment Term](../master-data-manageme../business-partner-setup/payment-term.md).

- **PO Maturity Date 1**: As indicated in the Payment Term, the PO Maturity Date is used in combination with the Fixed Due Date in the payment term to be set to Y and the Next Business Day set to N. The due date of the payment is based on the payment term defined in combination with the PO Maturity Date.
    
    !!! example
        For example, the defined payment term is 30 days and the PO Maturity Date 1 is set to 10. If the invoice date is the 1st of the month, based on the 30 days payment term, the payment due date is the 1st of the next month, but since the PO Maturity Date is set to 10, the payment due date as a result is the 10th of next month.

- **PO Maturity Date 2**: A second PO Maturity Date can be set to be combined with the payment term and the first PO Maturity Date.
    
    !!! example
        For example, the payment term is 30 days, the PO Maturity Date 1 the value is 10, the PO Maturity Date 2 is 20. The example given in PO Maturity Date 1 will remain the same. However, if the invoice date is the 11th of the month, the payment due date will be the 20th of next month: the 30 days of the payment terms are taken into account and since the 10th of the month is passed the second maturity date of the 20th is taken into account.

- **PO Maturity Date 3**: A third PO Maturity Date can be set to be combined with the payment term and the first and second PO Maturity Date.

- **Financial account**: The one selected will be the one used while withdrawing and reconciling the payments made to a supplier.

    !!! info
        For more information, visit [Financial Account](../financial-management/receivables-and-payables/transactions/financial-account.md).

- **Tax Category**: You can use a business partner tax category to get that the purchase documents registered from a vendor can only have a specific set of tax rates linked to that tax category.  
    
    !!! info
        For more information, visit [Tax Category](../financial-management/accounting/setup/tax-category.md).

- **On Hold**: This checkbox allows blocking a vendor, therefore some specific documents cannot be fulfilled for it. If checked, the On Hold section is shown with the following setup which can be changed as required:

    - **Purchase Order:** Blocked
    - **Goods Receipt:** Not blocked
    - **Purchase Invoice:** Blocked
    - **Payment Out:** Blocked

    Above defaulted configuration means that it is not possible to complete either a purchase order, a purchase invoice or to make a payment but to receive goods sent by the vendor.

    As already mentioned if a business partner of any type is blocked, it is not possible to Complete (or book) some document types. However, it is always possible to Void them. Etendo shows an error message stating that it is not possible to complete a document for a business partner set as **on hold**.

**Vendor Accounting**

Vendor accounting tab allows the user to configure the ledger accounts to be used while posting vendor related transactions such as vendor liabilities and vendor advance payments to the general ledger.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-8.png)

The user can configure for each supplier or creditor and available accounting schema, the ledger accounts to be used in:

- the **Vendor Liability** transactions such as purchase invoices posting.  
    
    !!! info
        For more information, visit [Purchase Invoice](../procurement-management/transactions.md#purchase-invoice).

- the **Vendor Prepayment** transactions such as those cases when the supplier of the goods requires the company to pay in advance part or full amount of the debt.  
    
    !!! info
        For more information, visit [Vendor Prepayments](../financial-management/receivables-and-payables/transactions/payment-out.md).

At first, these accounts are inherited from the Defaults accounts of the Accounting Schema assigned to the Organization for which the business partner is being created. The user can always change them.

!!! important
    It is possible to configure the creation of new correlative accounts for the business partners being created as described in the Org Schema tab of the [Organization](../general-setup/enterprise-model/organization.md) window.

#### Employee

!!! note
    A business partner can be set up as employee once the checkbox **Employee** is enabled.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-9.png)

Employee tab allows the user to set which of your business partners are *Employees*.

An employee can be:

- appointed as **sales representative** of a customer.

- defined as the **responsible of a company project/s**.  
    
    !!! info
        For more information, visit [Projects and Services Management](../project-and-service-management/getting-started.md).

- allocated to a **production process** as a resource.  
    
    !!! info
        For more information, visit [Production Management](../production-management/getting-started.md).

- and can **issue expense's sheets** as part of his/her involvement in a company project.  
    
    !!! info
        For more information, visit [Expense Sheet](../project-and-service-management/transactions.md#expense-sheet).

**Employee Accounting**

In this tab, the user can add the ledger accounts to be used while posting employee related transactions such as payroll accounting.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-10.png)

As you can see in the image above, nowadays there is no ledger account required to be defined for employee accounting. This is due to the fact that there is no transaction susceptible of being posted for employees.

Anyway, this is the place where *Human Resources* related modules or features should point to while defining the accounts to be used in any employee transaction susceptible of being posted.

**Cost Salary Category**

In this tab, the user can set up the salary category of the employee by selecting one of the options which were previously defined in the [Salary Category](../business-partner-setup/salary-category.md) window.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-11.png)

#### Bank Account

The Bank Account tab allows the user to list and set up business partner bank accounts.

It is possible to configure and properly set up business partner bank accounts to be used while making or receiving business partner payments of any type.

!!! important
    It is strongly recommended for the user to properly set up bank accounts as those will be used by Etendo as required within Etendo payment management processes.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-12.png)

Fields to note:

- **Bank Name**
- **Active** flag: It is recommended to keep only one bank account Active to avoid errors; otherwise ensure the correct bank account is used.
- **Country**: Here, the user can select a country from the list to specify if the bank account is a domestic bank account or a foreign bank account.
- **User/Contact**: In case you want to associate a contact for this bank account.
- **Bank Account Format**: List that contains all the possible values for generating the Displayed Account Number, which will be later on used by other reports or processes to get the account identifier. Possible  values are: 
    - _Use Generic Account No._
    - _Use IBAN_
    - _Use SWIFT + Generic Account No._ 

    !!! note 
        Other options can be added by other modules that extend the supported Bank Account Format.

- **Generic Account No**: A generic account number to identify the bank account can be introduced here. This field must be mandatory filled in case either _Use Generic Account No._ or _Use SWIFT + Generic Account No._ is selected at the Bank Account Format field.

- **IBAN**: The International Bank Account Number (IBAN) is an international standard for numbering bank accounts.  
    The IBAN consists of a two letter ISO 3166-1 country code, followed by two check digits, and up to thirty alphanumeric characters for the domestic bank account number, called the BBAN (Basic Bank Account Number). This field must be mandatory filled in case _Use IBAN_ is selected at the Bank Account Format field. The IBAN code will be automatically validated when inserting/updating the record taking into account the rules for the country bank defined.
- **SWIFT Code**: Corresponds to the ISO 9362 international bank code identifier. It must be mandatory filled in case _Use SWIFT + Generic Account No._ is selected at the Bank Account Format field.
- **Displayed Account**: It is automatically generated based on the value selected into the Bank Account Format. This field is read only, and it is used by other reports or processes.

**Advanced Bank Account Management**

!!! info
    To be able to include this functionality, the Advanced Bank Account Management module of the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

This functionality introduces the possibility to mark a bank account as Default within the Bank Account tab of the Business Partner window. Here, it is possible to check the Default Account checkbox in order to set the account to be used in the documents for different transactions. 

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-13.png)

!!! note
    If no bank account is selected as default, the one created last is used when no bank account is selected in orders/invoices.

!!! warning
    Only one bank account can be selected as default for each business partner.


#### Document Type

<iframe width="560" height="315" src="https://www.youtube.com/embed/8-MOprz-4FI?si=rc5geP_xaKmKvjsK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    This feature is available in Etendo 25.3 or later versions.

This tab introduces flexibility by customizing document type assignments to invoices, orders, shipments and receipts, specifically based on the business partner.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-14.png)

This functionality provides granular control over assigning transactional documents, overriding the default document type configured at the organization level. This is useful since each country, region, and even each company may use different types of documents with their respective printable and even personalized sequence numbers.

When a transaction document (order, invoice, shipment or receipt) is created and linked to a business partner, the system first checks the Document Type Tab for the correct configuration. This setup can significantly enhance the user experience when documents are created repeatedly.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-15.png)

Fields to note:

1. **Organization**: Specifies the organization to which this specific document assignment rule applies (e.g., F&B US Inc.).
2. **Document Category**: Select the type of transaction document, such as order, invoice, or shipment/receipt.
3. **Sales Transaction**: Checkbox used to distinguish document direction.

    - Checked: Corresponds to sales documents (e.g., sales orders, sales invoices, good shipments).
    - Unchecked: Corresponds to purchasing documents (e.g., purchase orders, purchase invoices, goods receipts).

4. **Document Type**: Select the specific document type available for the chosen category and transaction direction.

**Document Type Selection Priority**

1. Exact Match: Etendo searches for a direct rule defined for the business partner and the specific organization.
2. Organizational Tree: If no exact match is found, Etendo navigates up the organizational tree to find a match.
3. Default: If no rule exists, Etendo uses the default document type configured for the organization.

!!! warning
     This functionality is not available for documents created with a background/button process such as "Generate Invoice from Shipment" in the Goods Shipment window. In this case, the document type to be used is the one defined at organization level, instead of the one defined at Document Type tab level.

#### Location/Address

Business partner locations and full address details can be set up in this tab.

Business partners might have different address details depending on location/address used for either *Goods Receipts/Shipments* purposes or location/address used for *Invoices* purposes.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-16.png)

Fields to note:

- **Location/Address**: If you click in this field, the location selector box opens, there you can enter the information below:
    - the **address 1st line**
    - the **address 2nd line**, if needed
    - the **Postal Code**
    - the **City**
    - the **Country**: One from the list can be selected, if any
    - the **Region**: Once the country is selected, you can select one region of the country selected, from the list, if any.

- **Phone**: The phone number to contact the business partner.
- **Alternative Phone**: for an alternative phone, if any.
- **Name**: Referred to the Address name. This field is automatically filled in by Etendo, once the Location/Address information has been configured. The user could change it as needed.
- **Fax**: The fax number to contact the business partner.
- **Ship to Address** checkbox: The user should flag this one if the address being set up must be used for Goods Receipts/Shipments related transactions.
- **Invoice to Address** checkbox: The user should flag this one if the address being setup must be used for sales or purchase invoices transactions.

**Advanced Bank Account Management**

!!! info
    To be able to include this functionality, the Advanced Bank Account Management module of the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The Advanced Bank Account Management field is introduced in the Location/Address tab of the Business Partners window to **associate specific bank accounts** to the different locations.  

!!! warning
    In case of having both a default bank account and a location with a defined bank account, when generating a new document, the location bank account is prioritized over the default one.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-17.png)

#### Contact

Contact tab allows the user to add and configure the business partner contacts you deal with.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-18.png)

Fields to note:

- **First** and **Last Name** of the contact.
- **Email** of the contact.
- **Phone** of the contact.
- **Alternative Phone** of the contact.
- **Position** in the business partner.
- **Comments**: To enter additional information.
- **Active** flag: to indicate if this contact is available for use or disabled.
- **Default** flag: marks this contact as the default one for the business partner. This contact's email address will be automatically suggested in the email popup when sending emails from documents related to the business partner.
- **Commercial Authorization**: This checkbox is selected to indicate or not whether customer wants or does not want to receive commercial information from the organization.
- **Default**: Checkbox that marks this contact as the default recipient when sending documents by email. When selected, this contact's email address is automatically preloaded in the *To* field of the Email Options popup. If no contact has this flag set, the system falls back to the last used email for the business partner or, if none exists, to the first active contact ordered alphabetically.

    !!! info
        Only one contact per Business Partner should have this checkbox selected to ensure a deterministic preselection.

#### Basic Discount

Basic Discount tab allows the user to add and configure business partner Basic Discounts.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-19.png)

It is possible to enter as many **Discounts** as agreed with your business partners, by filling in the information below:

- the **Discount** to be applied while creating sales/purchase transactions for that business partner can be selected from the list (if any) or created by navigating to the **Discount** window.
- **Customer:** this checkbox must be selected if the discount is going to be applied to a Business Partner set as *Customer*.
- **Vendor:** this checkbox must be selected if the discount is going to be applied to a Business Partner set as *Vendor*.
- **Apply in Order:** this checkbox must be selected in case the discount can be applied in sales or purchase orders as applicable.
- **Cascade** calculation of the discount. For instance, if first discount is 10% and second one is 5%, a cascade calculation of the total discount won't be 15% but 14.5%.

    A discount not applied in Cascade means that it affects the full quantity of the Document Line. A Discount applied in Cascade means that affects the quantity of the Document Line that remains after applying all the discounts that come before it.

    !!! example
        An example to explain the difference between a Cascade and not Cascade Discount is the following one:

        Three Discounts, each one of 10%, the first two ones are defined as not Cascade and the third one as Cascade. Over an Invoice Line of 1.000 USD

        - The first discount will create a line of -100 USD (10% of 1.000 USD)
        - The second discount will also create a line of -100 USD (10% of 1.000 USD)
        - The third one, however, will create a discount based on applying the previous discounts on cascade, so:
        - 1.000 USD - 10% = 900 USD (applying the 1st discount on Cascade)
        - 900 USD - 10% = 810 USD (applying the 2nd discount on Cascade)
        - 10% of 810 USD = 81 USD. So the third discount will be -81 USD.
        - In total -100 -100 -81 = -281 USD for all three discounts (a total discount of 28.1%)


#### Rappel Configuration

!!! info
    To be able to include this functionality, the Advanced Rappels module of the Sales Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Sales Extensions - Release notes](../../../../whats-new/release-notes/etendo-classic/bundles/sales-extensions/release-notes.md).

Rappels are discounts based on the volume of consumption of a business partner in a given period of time. This functionality allows the user to configure and grant rappels to business partners.

With this functionality, the tab "Rappel Configurations" is shown in the business partners included in the Rappel configurations. Also, in the Business Partner window, the user is able to create rappels using the button **Create Rappel**.

![bp_window.png](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-20.png)

To be able to do this, it is necessary to configure certain aspects in the **Rappel Configurations** window.

!!! info
    For more information, visit [Rappel Configurations](../business-partner-setup/rappel-configurations.md).

The **Rappel configuration** tab can be found in the tabs section of the Business Partner window. In this tab, the user can find the configured rappels for each business partner.

To create a new rappel, the user must select one of the available configurations in this tab and click the **Create Rappel** button. A pop-up window will appear in which the user can select a trading partner to which the Rappel will be assigned, and also configure a date period in which the consumptions will be taken into account to calculate the discounts, determined by the *date from* and the *date to* information.

![bp_pop_up_new.png](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-21.png)

When the rappel is created, a sales invoice is created automatically, as seen below.

![created_rappel.png](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/business-partner/business-partner-22.png)

Each time a rappel is granted to a business partner, a new sales invoice is automatically generated in order to show the amount of the discount. This invoice has a specific sequence to distinguish it from the rest, according to the options entered when configuring the sequence, and a negative amount since it is a discount. This invoice is in Draft status.

!!! info
    For more information, visit [Sales Invoice](../sales-management/transactions.md#advanced-rappels).
