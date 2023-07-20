---
title: Sales Quotation Module
---
## **Sales Quotation**

Through this window, the user can generate sales quotations and create the corresponding orders from those quotations. 

### **Header**

The main header numerates the terms and conditions related with the sales quotation which will be used in the printed copy header and, later on, in its order, goods receipt and invoice process

![Header](https://drive.google.com/uc?export=view&id=1ZSKWjl6QaIGgvBRpKkq4g9_--VFCgEIF)

The main tab lists the main terms and conditions related to the sales quotation that will be used in the header of your hard copy and later in your order, packing slip and invoicing process.

In this section, the fields to fill in are the following: 

-   Transaction document: this will be the specific document type to use. In this case, it is called "Quotation".
-   Document No: quotation identification number. It will be generated automatically.
-   Quotation date: the date of the quotation. By default, it will be the current date.
-   Business partner: the client to whom the quotation is being made will be selected.
-   Partner address: in the drop-down list, you can select those customer addresses that have the "Shipping address" option checked.
-   Price list: you can select among all the available sales rates. By default, it will bring the rate configured for that third party in its master.
-   Link Order (Check): if this check is checked, when cloning the quotation (Copy record button) or when executing the "Change customer, rate and currency" process, the "Origin Order" field of the new quotation created, modifying the previous one, will be set with the number of the original quotation, i.e. the one being cloned or modified, which will be in "Closed-rejected" status. In turn, a record will be generated in the History tab of this last (original) quotation, each time there are modifications related to it.
-   Quantity/Time Unit: the validity date of the quotation will be defined based on a period of time: 10 days, 1 week, 2 months, etc.
-   Valid Until: expiration date of the quotation stipulated according to the Quantity and Time Unit fields.
-   Delivery time/Unit of Measure of Delivery Time: the delivery date will be defined from a period of time. For example: 3 weeks.
-   Payment method: will be filled by default with the payment method associated to the selected third party with the possibility to be edited.
-   Payment terms: will be filled by default with the payment method associated with the selected third party with the possibility to be edited.
-   Warehouse: will be the warehouse from which the products to be delivered to the customer will be shipped.
-   Reject reason: this is a drop-down menu where a rejection reason can be selected in case the quotation is rejected. The different rejection reasons will be defined by the user.
-   Sales representative: you can select from a drop-down list the employee who is making the quotation to the customer. It must be configured as a third party with the check "Employee" and "Is sales representative". 
-   Origin order: when the "Copy record" or "Change customer, rate and currency" button is executed and the "Link order" check is checked, this field will be set in the new quotation created, modifying the previous one, with the number of the original quotation, that is, the one being copied or modified; which will be in "Closed-rejected" status. 
-   Description: is a space to write additional related information.

#### Status bar

This bar shows the following information:

-   Document status: the possible statuses for a quotation will be:

\-Draft : it will be allowed to enter, delete and modify lines in this status. This status will be reached after clicking on the New button or when reactivating the document.

\-Under  evaluation : this status will be reached after registering the quotation. At this stage, the document cannot be modified. 

\-Closed - Order created : after creating the sales order, the document will reach this status. Once reached, no further actions will be allowed.

\-Closed - Rejected : this status will appear in case the quotation is rejected by the customer. It will be mandatory to enter a reason for rejection. Once this status is reached, no further actions will be allowed.

-   Total gross amount: will indicate the final monetary amount of the quotation, including taxes.
-   Total net amount: will indicate the final monetary amount of the quotation, excluding taxes.
-   Currency: shall indicate in which currency the quotation is defined. This field will be filled in according to the selected tariff.

### **Lines tab**

Once the header is completed, the lines must be added.

#### Basic discounts

Basic discount: this is the percentage reduction that will be applied to the list price.

Cascade: this is any additional discount based on the total remaining after applying previous discounts.

Active: this is a check that indicates whether this record is available for use or disabled.

#### Tax 

This tab summarizes the information related to the taxes involved in the quotation.

It contains as many records as there are tax categories involved in the quotation.

Line number: will indicate the position of the line in the document.

Tax: indicates the tax rate that is applicable to a given product.

Taxable amount: indicates the amount on which the tax will be calculated.

Tax amount: indicates the amount of tax resulting from the Tax and Taxable amount fields.

#### History tab

When the "Copy record" or "Change customer, rate and currency" button is clicked on a quotation and the "Link order" check is checked, a record will be created in this tab with the data of the new quotation created and, in turn, one for each of the successive modifications to the original quotation.

The information shown in each record is as follows: 

-   Document number of the new quotation.
-   Date of quotation.
-   Original amount of the quotation.

![History tab](https://drive.google.com/uc?export=view&id=1FyAdM85tTmm98wW02SpP3XAMmnN8kQ8x)

#### Actions

Register: this action allows the user to generate the budget.

Reactivate: this action allows the user to add, remove or modify one or more lines of the quotation. 

Create a sales order: this action converts the quotation into a sales order. To do so, the document type of the quotation must be configured correctly. This means that it requires a document type (i.e. standard order) to be defined in the "Order document type" field. 

This button will appear when the status of the quotation is "In evaluation".

The status of the newly created sales order will be "Registered". In this instance, it will be possible to change the "Billing Terms" as well as "Reactivate" it if it needs to be modified.

Before creating the order, the system will display a check called "Firm Quote", which is marked as default:

![Firm quote](https://drive.google.com/uc?export=view&id=1_XJmrKhdgK1rN4Pajy6p7asOMt0TSP0h)

If selected, it establishes a commitment to the customer for the supply of a certain quantity of goods at a quoted price, so the sales order will be identical to the quotation.

If not selected, a change in the price list at a later date will change the quoted prices in the same way on the sales order. Discounts and promotions will also be recalculated and reapplied to the new ones based on the transaction date (date the button is executed).

!!! info
    *Only one sales order can be created for the same quotation.* 


Reject : this action allows you to cancel or reject the quotation. A reason for rejection is mandatory for this action.

##### **Change customer, rate and currency button**

This process allows changes to be made to the third party, rate and/or currency of the document, whether the document is in draft or registered. One or several variables can be modified at the same time.
If the business partner is changed, the tax will be updated in the lines (If necessary).
In the pop-up window opened when this process is executed, the user will see the “do not apply conversion rate” check. If changing the quotation currency is intended, with the conversion to the official exchange rate included, the box must be unchecked when selecting the Currency option. Otherwise, the box must be checked in order for the system to show the quotation amount in the intended currency, defining prices in accordance with the price list configured by default in such currency.
Once executed, the quotation will be closed and a new one will be created with the changes made in the state “under evaluation”.

![Change window](https://drive.google.com/uc?export=view&id=1QEI9Z0QEHjghPagrkg3GC_JeEVZaOeVV)


##### Adjust button

This process allows the user to adjust the price of one or more budget lines, either by applying discount or surcharge through an adjustment factor. It can only be executed while the document is in draft.

![Adjust window](https://drive.google.com/uc?export=view&id=139RbgjIEjRsdrCO1DsOZD6ve5M3KlnsH)