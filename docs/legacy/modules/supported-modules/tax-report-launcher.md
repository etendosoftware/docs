---
title: Tax Report Launcher
---
## Overview
### Purpose

The aim of this document is to describe the functional specifications for a new extension module which is the “Tax report launcher".
The tax report launcher module allows the end users to create and submit tax reports to the tax authorities as required by the in-country tax authorities.
These functional specifications will be later on implemented according to the Technical documentation. 

!!! info
    It is important to note that this functional specification is oriented to the Spanish Professional localization pack by now, mainly in relation to the setup and scenarios covered, regardless Tax Launcher report feature must be implemented as generic as possible in order to cover other countries scenarios.

 
It is also a matter of fact that the current specification is mainly related to the Spanish needs as those are the ones currently known, therefore current documentation and tax report launcher implementation will be enhanced or adjusted later on if needed.

### Scope
Tax report launcher is an **extended tax module** which allows the end-user:
1. to set up different **“tax parameters” **as well as **"tax report parameters"** depending on the tax type and on the tax report requirements, respectively
2. to set up different **“tax reports”** in a unique window and according to the in-country tax requirements
3. to "launch" a selected tax report for a specific period
4. and to get the required **"tax output as a file"** to be submitted to the tax authorities in a valid format.

Besides, Tax report Launcher is a **framework** which will allow the end-user to develop new tax reports as required.

## Design Considerations
### Dependencies
As there should probably be more new tax reports to implement for the same country or others and even the existing ones might probably change, the tax report launcher module has to be implemented in a way that each tax report business logic is isolated from the rest, so in case there is a need of modifying an existing tax report, that change will not affect the rest and in case there are new tax reports to be implemented, those new ones will have its own business logic.
### Constraints
Etendo already provides tax setup, tax transactions and in general tax related features, therefore and in order to be consistent, the existing tax related features are taken into account as part of this new module. Besides, it could be that some of the existing tax features have to be enhanced in order to get the tax information required for this extension module to work.
### Delivery
!!! info
    This feature is going to be delivered as a module. Configuration data will be delivered as an additional module which could be imported by the end-user, containing by default setup; besides every report will be included in a particular module.

## Functional Requirements
### User roles & profiles
The following roles are involved:

- Accounting manager (Mary): Mary is the accounting manager. She must know which tax reports need to be submitted to the tax authorities depending on the in-country tax authorities requirements as well as the business specifics. Therefore she must be sure that once the "Configuration Data" extension delivered as an additional module to the Tax Report Launcher is installed, the default data or setup required for the specific tax reports she needs to submit to the tax authorities is properly set up in the system. Mary will do that in collaboration with Peter.
- Accounting staff (Peter): Peter is an employee part of the accounting staff. He will be responsible for helping Mary by checking or setting up the parameters needed, as well as entering the correspondent accounting transactions in collaboration with sales (Mike) and purchase staff (Alice) and launching the tax reports and finally, getting the tax report output to be submitted to the tax authorities.

### Report types
Tax report launcher module allows to define below described type of tax reports:

- **statement tax reports**, which are the reports intended just to **list a specific type of tax transactions** so tax authorities are informed about it. For example, tax authorities need to be informed about every sales and/or purchase transaction exceeding a specific amount or the ones within EU countries.
- tax reports, which are the reports intended to collect tax base amounts, tax rates and tax amounts in a way to get the net amounts of **tax assessment or tax revenue** or any other kind of tax output.

The most common and relevant tax reports to be submitted to the tax authorities are:
- Value Added tax (VAT)
- and Withholding tax reports
in relation to those tax there are some important concepts to take into account listed below:

- **Value added tax** is an indirect tax on consumption and applicable to supplies of services or goods, goods imports and intra-community goods acquisitions, therefore VAT tax setup depends on the transaction type and the goods/services type being purchased and/or sold.
- **Withholdings** are amounts subtracted by the retainer (i.e. a company) to the tax payer (i.e and employee) for incomes paid (i.e. a salary) which are paid by the retainer as an “advance” amount to the tax which the tax payer has to pay at the end of the fiscal year to the tax authorities, therefore Withholding tax setup depends on who generates an income as well as the type of income itself.

In some countries, like Spain, there is another type of withholding commonly known as Payments on account. **Payment on account** is a withholding. It is an amount “paid” by the companies to the tax authorities for certain items of income (goods) as an advance of the tax amount to be paid by the beneficiary of that income, therefore payment on account tax setup depends on who generated an income as well as the type of income itself.
- **Income types** can be “cash” (monetary/by example a salary or a fee paid to a professional) or “goods” (not monetary/by example a company car or a company flat)
- **Withholding** term applies to **cash incomes**
and **Payment on account** term applies to **goods incomes** in some countries like Spain.

### User stories
Mary is the Accounting manager of a Spanish located company responsible for deciding which tax reports need to be submitted to the tax authorities. For sure VAT and Withholding tax reports will have to be submitted to the tax authorities. Based on "in-country tax types" as well as in-country tax authorities requirements and the type of business running, Mary should know exactly which VAT and withholding tax reports have to be mandatory submitted to the tax authorities by her company.

Mary knows that as an overall rule **VAT** related tax reports **recognize tax liability** at the time goods are delivered and therefore invoiced or at the time services have been executed and therefore invoiced and **withholding** tax reports **recognize tax liability** at the time goods or services invoice are posted but in other countries like Spain at the time cash or goods incomes already invoiced and post are satisfied or paid.

Therefore, and having into account her company is located in Spain, Etendo has to fulfill her accounting needs which are:

**VAT tax amounts must be posted** and therefore included in accounting, **at the time an invoice** containing VAT **is posted** whenever invoice date is the same as goods expedition date or service execution date
**Withholding tax amounts must be posted** and therefore included in accounting, **at the time an invoice containing Withholding is posted** as there are some countries like Spain where withholding tax amounts must be posted at the same as VAT tax amounts, that is at the time an invoice containing withholding tax is posted, regardless tax liability for this type of taxes is recognize at the time that invoice is paid.

Mary should also be aware of the fact that most taxable transactions will be entered in the system either as a purchase or sales transaction and therefore as a purchase or sales invoice but there will also be some of them which will not have an invoice behind. Those last cases are mainly related to withholding tax, which will have to be entered in the system as **manual settlements linked to the correspondent G/L items.**
**Manual settlement will generate withholding tax posting** in the case of withholding which do not have an invoice linked to them and therefore should be entered in the system as a manual settlement which will imply a cash or bank payment afterward.
 
#### Overall system Setup
Mary lets accounting staff know which tax reports need to be submitted to the tax authorities by the company so Peter can either check or set up the tax parameters, business partner tax categories and the tax reports and tax report parameters needed; after that enter the correspondent accounting transactions in collaboration with sales and purchase staff in order to finally launch the tax reports and get the tax report output to be submitted to the tax authorities.

##### First step:
The **first** step that Peter should perform is either **to check the setup** or **to set up** the tax parameters required according to the work flow listed below:

1. Peter goes to **Financial Management / Accounting / Setup / Business Partner Tax category** to create the **business partner tax categories** needed depending on who generated a sales or purchase transaction subject to VAT or who generated an income subject to withholding. For example, he should enter as BP tax category: National Vendor, EU Vendor, International Vendor, National customer, EU Customer, International customer, Employees, Non-resident employees, Professionals, EU Professionals, International Professional, Renting, Economic Activities and so on so forth. 
2. Peter goes to **Financial Management / Accounting / Setup / Transaction code** to check that the required VAT "Transaction codes" for either purchase or sales transactions are set up by default. As already said most common ones are => Supplies (For example, this type of transaction code in Spain is ="E") and Acquisitions (For example, this type of transaction code in Spain is ="A")
3. After that, Peter goes to **Financial Management / Accounting / Setup / Tax key** to check that the required **Tax keys and sub-keys** are set up by default depending on the type of income and the business partner who generated that income. For example, in the case of the Spanish tax report 110, he should know that he has to create a Tax key = "A" for employment incomes, a Tax key = "G" for professional activities incomes, a Tax key = "K" for prizes and so on and so forth. 
4. Once the above is done Peter goes to **Financial Management / Accounting / Setup / Tax Category** as it could be new Tax categories have to be created. For example VAT (in case of purchase VAT), SalesVAT, IntraVAT, SalesIntraVAT, ImportVAT, ExportVAT, VAT+EC, SalesVAT+EC, WSalary, WProfessionals, WPrizes, PSalary, PProfessionals,PPrizes.
5. And once the above is done, Peter goes to **Financial Management / Accounting / Setup / Tax rates** as it could be new **VAT tax rates** and new **Withholding rates** have to be created. VAT tax rates depend on the type of transaction, whether it is a purchase or a sale, and the type of goods being purchased or sold and Withholding rates depends on the type of income being paid and the business partner who generated that income.

!!! info
    By using this way of withholding set up Peter has to make sure he is willing to post withholding at the time an invoice containing an income subject to withhold is posted, regardless of which withholding liability will be recognized at the payment date, and not at the time that invoice is paid. Tax rates have to be linked to the correspondent BP tax category and the correspondent accounting must be setup.



VAT rates = for example VAT21%, VAT10%, VAT4%, VAT21%+EC4%, VAT10%+EC1,5%, VAT4%+EC0,5%, SalesVAT21%, SalesVAT10%, SalesVAT4%, SalesVAT21%+EC4%, SalesVAT10%+EC1,5%, SalesVAT4%+EC0,5%, Intra-VAT21%/-21%, Intra-VAT0%, ImportVAT21%, ExportVAT0%. Besides the existing and new VAT rates will have to be **linked** to the correspondent **Transaction Codes** depending on the VAT direction. 
Withholding rates = for example WSalary35%, WPrizes18%, WProfessionals15%, WProfessionals7%. Besides the existing and new withholding and payment on account tax rates have to be **linked** to the correspondent Tributary **keys and sub-keys** depending on the tax reports those tax rates are going to be included. 


6. Above step could be also done by Peter from **Master data Management / Business partner setup / Withholding**. He will have to choose this way and not above one in relation to withholding rates in case he needs to post withholding amounts at the time an invoice is paid and not at the time the invoice is posted. For example WSalary35%, WPrizes18%, WProfessionals15%, WProfessionals7%. Besides the existing and new withholding rates have to be **linked** to the correspondent Tributary **keys and sub-keys** depending on the tax reports those tax rates are going to be included. 

##### Second step:
The **second** step that Peter should perform is to check that the **tax reports** and the **tax report parameters** are properly set up by default. To get this done he will have to navigate to **Financial Management / Accounting / Setup / Tax report.**
 
**Tax Report.** There should be a record for each tax report which needs to be submitted to the tax authorities. Each tax report should have below information:

a) **Tax Report groups.** For some countries such Spain withholding tax reports have a fixed section structure named Tax report groups. For example, in the case of Spain, withholding tax reports have 7 default section which are:
(1) Identification
(2) Accrual
(3) Tax assessment
(4) Tax revenue
(5) Negative declaration
(6) Complementary declaration and
(7) Signature.

!!! info
    In general VAT reports do not have those kinds of sections because they are not tax reports as such but statement tax reports, so a unique output section must be created for this type of reports. 

 b) **Tax report parameters**. Each tax report will have specific tax report parameters Peter should be aware of in order to get the right setup
***In parameters**. Those are specific tax report parameters which are needed by the time a tax report or a statement tax report is launched, therefore this type of parameters will have to be **manually entered** by him while launching a tax report
For example "Tax report file name", "contact person" or others more specific depending on the type of tax report.
***Constant parameters.** Specific constant tax report parameters which must be **set up by default** as there will always be the same
For example, in the case of the Spanish tax report 110, he should check that "Tax model" constant parameter is entered as "110", and "01" as page number.
***Out parameters**. Peter should know that out parameters are tax report parameters which will get information from the system, such as "Company Name", "Company Tax ID number" as well as more complex data/output related to transactions linked to a specific **"Tax keys and/or sub-keys"** for example. It is time for him to check that those output parameters are set up by default properly and linked to a specific tax report.


#### Specific setup and transactions

In collaboration with sales (Mike) and purchase staff (Alice), Peter needs to enter in the system the normal activity transactions which will be included in one or another tax report depending on the type of transaction we are talking about:

##### Purchase – Overall scenario

Alice creates a **requisition** based on the company or entity's items and / or services needs. As soon as requisitions are confirmed by Dan, the Purchase manager, she converts the requisition/s into a/some **purchase orders** and sends them to the correspondent business partner (vendor or creditor or professional).
Once the **goods have been received** by her company or once the **services have been executed** by the creditor as requested by her company, the vendor or creditor will issue an invoice. That invoice will have to be entered by Alice in the system as a **purchase invoice**.
In general, purchase transactions and therefore purchase invoice could be the result of goods acquisition or services provided by vendors located in Spain or located in the EU or located abroad, so depending on the origin of the goods and the type of goods/services exchanged, the VAT rate to pay (VAT-fiscal credit) as well as the transactions code will be different.
Besides, there are some kind of purchase transactions for which withholding tax will be applicable as well as the correspondent tributary keys depending on the type of income generated and the type of business partner who generated them.

##### Purchase - Specific scenarios & setup required

Alice could enter in the system any of the purchase invoices listed below as those are very common purchase scenarios for a small-medium size company located in an EU country like Spain. Peter and Alice will have to check that at least the information listed below per purchase invoice transaction is correctly set up before entering any purchase transaction.

1- **Goods purchase to a national vendor**
1. System path: Procurement management / Transactions / Purchase invoices
2. Business partner tax category: National vendor
3. Tax category : VAT
4. Tax rate (Purchase tax) : VAT21% and/or VAT10% and/or VAT4%
5. Tax rate - transaction code: "A" (acquisition)

2- **Goods purchase to a national vendor (EC scenario)**
1. Business partner tax category: National vendor
2. Tax category (purchase tax) : VAT+EC
3. Tax rate (Purchase tax) : VAT21%+EC4% and/or VAT10%+EC1,5% and/or VAT4%+EC0,5%
4. Tax rate - Transaction code: "A"(acquisition)

3- **Goods purchase to an EU vendor**
1. System path: Procurement management / Transactions / Purchase invoices
2. Business partner tax category: EU vendor
3. Tax category : IntraVAT
4. Tax rate (Purchase tax and Sales VAT) : IntraVAT21%/-21%
5. Tax rate - transaction code: "A" (acquisition)

4- **Goods purchase to an international vendor**

1. System path: Procurement management / Transactions / Purchase invoices
2. Business partner tax category: International vendor
3. Tax category : ImportVAT
4. Tax rate (Purchase tax) : ImportVAT21%
5. Tax rate - transaction code: "A" (acquisition)

5- **Purchase of professional services to a national professional**
1. System path: Procurement management / Transactions / Purchase invoices
2. Business partner tax category: National professionals
3. Tax category : VAT+WProfessionals
4. Tax rate (Purchase tax) : VAT21%+WProfessionals15%
5. Tax rate - Tributary key: "G-01 or G-02 or G-03
6. Tax rate - transaction code: "A" (acquisition)

6- **Purchase of professional services to an UE professional**
1. System path: Procurement management / Transactions / Purchase invoices
2. Business partner tax category: EU professionals
3. Tax category : IntraVAT+WProfessionals
4. Tax rate (purchase VAT and sales VAT): IntraVAT21%/-21%+WProfessionals24%
5. Tax rate - tributary key: "19"
6. Tax rate - transaction code: "A" (acquisition)

7- **Purchase of professional services to an international professional**
1. System path: Procurement management / Transactions / Purchase invoices
2. Business partner tax category: International professionals
3. Tax category : ImportVAT+WProfessionals
4. Tax rate (Purchase tax) :ImportVAT21%+WProfessionals24%
5. Tax rate - tributary key: "19"
6. Tax rate - transaction code: "A" (acquisition)


###### Goods Purchase invoices

While entering a Goods purchase invoice in the system, Alice must be sure VAT tax is going to be calculated properly as described above:
National vendor:
Invoice amount = 100.000 € => Tax base amount = 100.000 €
VAT21% = 100.000 € x 21% = 21.000 € => VAT amount = 21.000 €
Total invoice amount to be paid to the vendor = 121.000 €
EU vendor;
Invoice amount = 100.000 € => Tax base amount = 100.000 €
IntraVAT21%/-21% = [100.000 € x 21% = 21.000] + [100.000 € x -21% = -21.000] = 0 € => VAT amount = 0 €
Total invoice amount to be paid to the vendor = 100.000 €
International vendor:
Invoice amount = 100.000 € => Tax base amount = 100.000 €
ImportVAT21% = 100.000 € x 21% = 21.000 € => VAT amount = 21.000 €
Total invoice amount to be paid to the vendor = 121.000 €

###### Equivalence Charge

In this case, Alice's company (Etendo legal entity) is a retailer company which buys goods to National vendors only and under this specific VAT regimen.
While Alice's company is not forced to keep tracking of the VAT-fiscal credit and the VAT-fiscal debit and it is not forced to settle VAT, Alice's company is forced to tell its vendors they are subject to EC special regimen with the aim of allowing their vendors to charge them with an additional tax rate named EC tax rate.
While entering a Goods purchase invoice in the system under this specific VAT regimen, Alice must be sure VAT and EC taxes are calculated properly as described above:

Invoice amount = 100.000 € => Tax base amount = 100.000 €
VAT21% = 100.000 € x 21% = 21.000 => VAT amount = 21.000 €
EC4% = 100.000 € x 4% = 4.000 €
Total invoice amount to be paid to national vendor = 100.000 € + 21.000 € + 4.000 € = 125.000 €

###### Professional Service Purchase Invoices

While entering a services purchase invoice in the system, Alice must be sure VAT tax and withholding tax are going to be calculated properly as described above:

Invoice amount = 100.000 € => Tax base amount = 100.000 €
VAT21% = 100.000 € x 21% = 21.000 => VAT amount = 21.000 €
W-18% = 100.000 € x -15% = -15.000 => Withholding amount = -15.000 €
Total invoice amount to be paid to a professional vendor = 100.000 € + 21.000 € -15.000 € = 106.000 €

###### Reverse charge

Alice should know that an IntraVAT tax rate could be checked as “Reverse Charge” just in the case of services provided by UE professionals because it is not mandatory for UE goods acquisitions anymore. In that case the company will have to create and Auto-Invoice after receiving services purchase invoice with a VAT tax rate = 0%
Therefore, there will have to be 3 entries for each invoice under this scenario with an operation code = "I":

- the line for the Auto-invoice of the VAT-fiscal credit (IntraVAT21%=21%)
- the line for the Auto-invoice of the VAT-fiscal debit (SalesIntraVAT=-21%)
- and the line for the original purchase Invoice as import or exempt (ImportVAT = 0%).

!!! info
    Notice that the line for VAT-fiscal credit and the line for import or exempt VAT will be shown and stored as purchase/received VAT (VAT-fiscal credit) while the VAT-fiscal debit line will be shown and stored as sales/issued VAT.


##### Purchase credit notes

In case there is any error in the purchase invoices for goods or services provided by a business partner or in the case any goods have to be returned back to a vendor due to lack of quality or any other kind of error, Alice and the accounting staff will have to void the correspondent purchase invoice and create and post a new purchase credit invoice (purchase credit memo). In this case the applicable scenarios are the same as described in section above, but:
1. Purchase credit invoices amounts will be negative amounts
2. Peter needs to be sure similar purchase credit invoices are not grouped while being included in VAT tax reports.

##### Sales - Overall scenario

Mike creates a **sales order** based on a customer/s need/s. Once the **goods have been sent** by his company through a Good shipment, it is possible for him to issue a **sales invoice** and send it to the customer together with good shipment documentation, for example a packing slip.
In general, sales transactions and therefore **sales invoices** could be the result of goods shipments or services provide by a company to a customer or third party located in Spain or located in the EU or located abroad, so depending on the destination of the goods and the type of goods/services provided, the VAT rate to collect (VAT-fiscal debit) as well as the transactions code will be different.
Besides, there are some kinds of sales transactions for which withholding tax will be applicable as well as the correspondent tributary keys depending on the type of income generated.

##### Sales - Specific scenarios & setup required

Mike could enter in the system any of the sales transactions listed below as those are very common sales scenarios for a small-medium size company located in an EU country like Spain. Peter and Mike will have to check that at least the information listed below per sales invoice transaction is correctly set up before entering any sales transaction.

1- **Sales of goods to a National customer(Spain)**
1. System path: Sales Management / Transactions / Sales Invoice
2. Business partner tax category: National customer
3. Tax category : SalesVAT
4. Tax rate (Sales tax) : SalesVAT21% and/or SalesVAT10% and/or SalesVAT4%
5. Tax rate - transaction code: "E" (Supply)


2- **Sales of goods to a National retailed (EC scenario)**
1. And Business partner tax category: National retailer
2. Tax category : SalesVAT+EC
3. Tax rate (Sales tax) : SalesVAT21%+EC4% and/or SalesVAT10%+EC1,5% and/or SalesVAT4%+EC0,5%
4. Tax rate - Transaction code: "E"(supply)

3- **Sales of goods to an EU customer**
1. System path: Sales Management / Transactions / Sales Invoice
2. Business partner tax category: EU customer
3. Tax category : SalesIntraVAT
4. Tax rate (Sales tax) : SalesIntraVAT0%
5. Tax rate - transaction code: "E" (supply)

4- **Sales of goods to an international customer**
1. System path: Procurement management / Transactions / Purchase invoices
2. Business partner tax category: International vendor
3. Tax category : ExportVAT
3. Tax rate (Sales tax) : ExportVAT0%
4. Tax rate - transaction code: "E" (Supply)

5- **Service provided to National customer**
1. System path: Sales Management / Transactions / Sales Invoice
2. Business partner tax category: National customers
3. Tax category : SalesVAT+SalesW
4. Tax rate (sales tax9 : SalesVAT21%+SalesWProfessionals15%
5. Tax rate - Tributary key: not applicable
5. Tax rate - transaction code: "E" (Supply)

6- **Service provided to an UE customer**
1. System path: Sales Management / Transactions / Sales Invoice
2. Business partner tax category: EU customer
3. Tax category : SalesIntaVAT+SalesW
4. Tax rate (Sales tax) : SalesIntraVAT0%+SalesWProfessionals15%
5. Tax rate - tributary key: not applicable
6. Tax rate - transaction code: "E" (Supply)

7- **Service provided to an International customer**
1. S1. ystem path: Sales Management / Transactions / Sales Invoice
2. Business partner tax category: International customers
3. Tax category : ExportVAT+SalesW
4. Tax rate (Sales tax) :ExportVAT0%+SalesWProfessionals15%
5. Tax rate - tributary key: not applicable
6. Tax rate - transaction code: "E" (Supply)


###### Goods Sales invoices
While entering a Goods Sales invoice in the system, Mike must be sure Sales VAT tax is going to be calculated properly as described above:
National customer:
Invoice amount = 100.000 € => Tax base amount = 100.000 €
SalesVAT21% = 100.000 € x 21% = 21.000 => Sales VAT amount = 21.000 €
Total invoice amount to be collected from the customer = 121.000 €
EU vendor;
Invoice amount = 100.000 € => Tax base amount = 100.000 €
SalesIntraVAT0% = 100.000 € x 0% = 0 €=> Sales VAT amount = 0 €
Total invoice amount to be collected from the customer = 100.000 €
International vendor:
Invoice amount = 100.000 € => Tax base amount = 100.000 €
Export0% = 100.000 € x 0% = 0 € => VAT amount = 0 €
Total invoice amount to be collected from the customer = 100.000 €

###### Equivalence Charge

In this case, Mike's company sells goods to a national retailer company he must charge them with an additional tax rate named EC tax rate.
Therefore while entering a Goods sales invoice in the system under this specific VAT regimen, Mike must be sure Sales VAT and EC taxes are calculated properly as described above:
Invoice amount = 100.000 € => Tax base amount = 100.000 €
SalesVAT21% = 100.000 € x 21% = 21.000 € => Sales VAT amount = 21.000 €
EC4% = 100.000 € x 4% = 4.000 €
Total invoice amount to be collected from the retailer = 100.000 € + 21.000 € + 4.000 € = 125.000 €

###### Professional Service Sales Invoices

While entering a services sales invoice in the system, Mike must be sure Sales VAT tax and withholding tax are going to be calculated properly as described above:
Invoice amount = 100.000 € => Tax base amount = 100.000 €
Sales VAT21% = 100.000 € x 21% = 21.000 => VAT amount = 21.000 €
SalesWProfessionals15% = 100.000 € x -15% = -15.000 => Withholding amount = -15.000 €
Total invoice amount to be collected from the customer = 100.000 € + 21.000 € -15.000 € = 106.000 €


##### Sales credit invoices

In case there is an error in the sales invoices of goods or services Mike's company is providing to his customers or in case a customer wants to return back any goods due to lack of quality or any other kind of error, Mike and the accounting staff will have to void the correspondent sales invoice and create and post a new sales credit invoice (sales credit memo). In this case the applicable scenarios are the same as described in section above, but:
1. Sales credit invoices amounts will be negative amounts
2. Mike needs to be sure similar sales credit invoices are not grouped while being included in VAT tax reports.

##### Manual Settlements

Peter will have to use Etendo Manual Settlements feature for **entering in the system the rest of taxable incomes** **which can not be entered in the system** either as a purchase transaction and therefore as a purchase invoice or as a sales transaction and therefore as a sales invoice.
Peter will have to use **G/L items** while entering manual settlements as there is not going to be an invoice behind this type of transactions but a business partner and an income satisfied or paid by his company or an income collected by his company; therefore Peter will have to create as much G/L items as required depending on the **type of incomes** either collected or paid and the **type of business partners** involved in the income generation.

**G/L items creation is mainly related to Withholding tax reports** as those reports are the ones containing income taxable transactions not supported by either purchase or sales invoices.
!!! info
    Peter will have to make sure that G/L items are linked to the correspondent tax rate and withholding rates if applicable, and besides Peter will have to make sure that G/L items have the correspondent accounting setup in advance.

Scenarios below explain that Peter will have to create at least two G/L items per transaction, he will not use direct posting feature as these types of withholding tax, the ones entered in the system as manual settlement, can be only posted at the time of payment via cash journal or payment journal.

###### Employee salary payments

Peter knows that Etendo does not automate payroll payment transactions so, in order to get in the system an employee salary payment transaction, Peter will have to use the "manual settlement" feature as a first step and then settle or pay it by using either a cash payment or a bank payment.
While doing that, he needs to be sure that the transaction is linked to the specific G/L items created for that reason and besides Peter must enter the correspondent withholding tax as those kinds of payment are subject to withholding which must be submitted to the tax authorities later on.

To accomplish above scenario, Peter will have to navigate to:

- Financial Management / Accounting / setup / **Business Partner Tax Category** to create the BP tax category => "Employee" (Need to be discussed)
- Financial Management / Accounting / setup / **Tax category** to create the Tax category => "WSalary"
- Financial Management / Accounting / setup / **Tax key** to check the correspondent Tax key and sub-keys is setup by default => "A = Employment Income"
- Financial Management / Accounting / setup / **Tax rate** to create the Tax rate => "WSalary35%", in this same screen and under **"Tax parameter"** tab Peter must setup the correspondent Tax Report Parameter so the tax rate can be linked to the correspondent tax report (110), tax report group (Assessments), tax parameter (Withholding and payments on account) and tributary key (A-Employment income).
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item = > "Employee income in cash withholding" which must be linked to Tax rate "WSalary35%" and the correspondent accounting setup.
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item ="Outstanding salary payments" with the correspondent accounting setup.


Once the above is setup in the system Peter must navigate to Financial Management /Receivable & Payable / Transactions / Manual settlement and create a new manual settlement as described below:
Transaction date => 26-June-2021
Accounting date => 30-June-2021
Description => Alice's salary

Then Peter goes to "Create Payment" window and enter two new ones as described below:
Business Partner => Alice (previously created as and employee with BP tax category = Employee
Description => Alice's salary June
Amount => 1000
Receipt => No
Direct posting => No

Then Peter goes to "Balance Payment" window and enter a new one as described below:
G/L item => Employment income in cash withholding
Debit amount => 350
and G/L item => "Outstanding salary payments"
Debit amount => 650

Once all of the above is done, Peter process the manual settlement and navigate to Financial Management / Receivable & Payable / Transactions / Cash Journal and create a new one and enters:
Transaction date=> 30-June-2021
Accounting date=> 30-June-2021

and then go to Lines and creates a new one as:
Cash Type => Debt-payment and then click in Debt/payment feature to get into Debt Payment Selector.

Once in the Debt Payment Selector Peter has to remove "Receipt" check and search by pending ones to select the one just entered.

After that Peter processes and posts.
Peter can navigate to the journal entry and then to the cash journal lines, and then to the payment, and once there Peter can select and post the "Settlement Canceled" in order to generate and check the final posting.

Finally, Peter has to verify that the correspondent Withholding tax reports is showing a withholding amount of 350 linked to WSalary35% rate.

###### Prizes payments

Peter's company organized a competition between their employees. Alice won that prize which was an "in cash" prize of 500 €, which has to be included in the system. For doing that Peter will have to use the "manual settlement" feature as a first step and then settle or pay it by using either a cash payment or a bank payment.
While doing that he needs to be sure that the transaction is linked to the specific G/L items created for that reason and besides Peter must enter the correspondent withholding tax as those kinds of payment are subject to withholding which must be submitted to the tax authorities later on.

To accomplish above scenario, Peter will have to navigate to:

- Financial Management / Accounting / setup / **Business Partner Tax Category** to create the BP tax category => "Employee"
- Financial Management / Accounting / setup / **Tax category** to create the Tax category => "WPrize"
- Financial Management / Accounting / setup / **Tax key** to create the correspondent Tax key and sub-keys => "K_01=Prizes_01"
- Financial Management / Accounting / setup / **Tax rate** to create the Tax rate => "WPrize18%", in this same screen and under **"Tax parameter"** tab Peter must setup the correspondent Tax Report Parameter so the tax rate can be linked to the correspondent tax report (110), tax report group (Assessments), tax parameter (Withholding and payments on account) and tributary key (K_01 - Prizes 01).
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item = > "Prizes income in cash withholding" which must be linked to Tax rate "WPrize18%" and the correspondent accounting.
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item => "Prizes in cash" with the correspondent accounting setup.

Once the above is setup in the system Peter must navigate to Financial Management /Receivable & Payable / Transactions / Manual settlement and create a new manual settlement as described below:

Transaction date => 01-July-2021
Accounting date => 01-July-2021
Description => Alice's prize (best product X design)

Then Peter goes to "Create Payment" window and enter a new one as described below:
Business Partner => Alice (previously created as and employee with BP tax category = Employee
Description => Alice's prize
Amount => 500
Receipt => No
Direct posting => No

Then Peter goes to "Balance Payment" window and enter two new ones as described below:
G/L item => Prizes in cash
Debit amount => 450
and G/L item => Prizes income in cash withholding
Debit amount => 50

Once all of the above is done, Peter process the manual settlement and navigate to Financial Management / Receivable & Payable / Transactions / Cash Journal and create a new one and enters:
Transaction date=> 01-July-2021
Accounting date=> 01-July-2021
and then go to Lines and creates a new one as:

Cash Type => Debt-payment and then click in Debt/payment feature to get into Debt Payment Selector.

Once in the Debt Payment Selector Peter has to remove "Receipt", check and search by pending ones, so "prize" one just created can be selected.

After that Peter processes and posts.
Peter can navigate to the journal entry and then to the cash journal lines, and then to the payment, and once there Peter can select and post the "Settlement Canceled" in order to generate and check the final posting.

Finally, Peter has to verify that the correspondent Withholding tax reports is showing a withholding amount of 50 linked to WPrize18% rate.

**Building Renting in case of 3rd party building**

Peter's company rents a 3rd party owned building in which Peter's company office is located. The owner of that building issues a "statement or a receipt" to Peter's company every month in order to be paid for that rent. Peter's company has to pay that rent and enter in the system the correspondent statement and payment, therefore Peter will have to use the "manual settlement" feature as a first step and then pay it by using either a cash payment or a bank payment.

!!! info
    While doing that he needs to be sure that the transaction is linked to the specific G/L items created for that reason and besides Peter must enter the correspondent withholding tax as those kinds of payment are subject to withholding which must be submitted to the tax authorities later on.

To accomplish above scenario, Peter will have to navigate to:

- Financial Management / Accounting / setup / **Business Partner Tax Category** to create the BP tax category => "Lessor"
- Financial Management / Accounting / setup / **Tax category** to create the Tax category => "WRenting"
- Financial Management / Accounting / setup / **Tax key** to create the correspondent Tax key and sub-keys => "P -Renting"
- Financial Management / Accounting / setup / **Tax rate** to create the Tax rate => "WRenting18%", in this same screen and under **"Tax parameter"** tab Peter must setup the correspondent Tax Report Parameter so the tax rate can be linked to the correspondent tax report (115), tax report group (Assessments), tax parameter (Withholding and payments on account) and tributary key (P-Renting).
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item = > "3rd party rent in cash Withholding" which must be linked to Tax rate "WRenting18%" and the correspondent accounting setup.
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item => "3rd party rent" with the correspondent accounting setup.

Once the above is setup in the system Peter must navigate to Financial Management /Receivable & Payable / Transactions / Manual settlement and create a new manual settlement as described below:

Transaction date => 29-August-2021
Accounting date => 01-September-2021
Description => September renting

Then Peter goes to "Create Payment" window and enter a new one as described below:
Business Partner => Lessor BP (previously created as a creditor and with BP tax category = Lessor
Description => September renting
Amount => 2000
Receipt => No
Direct posting => No

Then Peter goes to "Balance Payment" window and enter two new ones as described below:
G/L item => "3rd party rent in cash withholding"
Debit amount => 360
G/L item => "3rd party rent in cash"
Debit amount => 1640

Once all of the above is done, Peter process the manual settlement and navigate to Financial Management / Receivable & Payable / Transactions / Cash Journal and create a new one and enters:

Transaction date=> 01-September-2021
Accounting date=> 01-September-2021
and then go to Lines and creates a new one as:
Cash Type => Debt-payment and then click in Debt/payment feature to get into Debt Payment Selector.

Once in the Debt Payment Selector Peter has to remove "Receipt", check and search by pending ones, so "rent" one just created can be selected.

After that Peter processes and posts.
Peter can navigate to the journal entry and then to the cash journal lines, and then to the payment, and once there Peter can select and post the "Settlement Canceled" in order to generate and check the final posting.

Finally, Peter has to verify that the correspondent Withholding tax reports is showing a withholding amount of 360 linked to WRenting18% rate.


###### Renting in case of a building do not linked to an economic activity
Peter's company owns a building not related to Peter's company's economic activity. That building is being rented to a 3rd party or lessee. Peter's company issues a statement or a receipt and sends it to the lessee in order to be paid on a monthly basis. Peter's company must collect the money and enter in the system the correspondent payment, in order to get that in the system, Peter will have to use the "manual settlement" feature as a first step and then get it paid by using either a cash payment or a bank payment.

!!! info
    While doing that he needs to be sure that the transaction is linked to a specific G/L item created for that reason and besides Peter must enter the correspondent withholding tax as those kinds of payment are subject to withholding which must be submitted to the tax authorities later on.

To accomplish above scenario, Peter will have to navigate to:

- Financial Management / Accounting / setup / **Business Partner Tax Category** to create the BP tax category => "Lessee"
- Financial Management / Accounting / setup / **Tax category** to create the Tax category => "WPropertyRent"
- Financial Management / Accounting / setup / **Tax key** to create the correspondent Tax key and sub-keys => "C_04-Property Rent"
- Financial Management / Accounting / setup / **Tax rate** to create the Tax rate => "WPropertyRent18%", in this same screen and under **"Tax parameter"** tab Peter must setup the correspondent Tax Report Parameter so the tax rate can be linked to the correspondent tax report (123), tax report group (Assessments), tax parameter (Withholding and payments on account) and tributary key (C_04-Property Rent).
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item = > "Property Rent in cash withholding" which must be linked to Tax rate "WPropertyRent18%"
- Financial Management / Accounting / setup / **G/L Item** to create the G/L item => "Property Rent in cash" with the correspondent accounting setup.


Once the above is setup in the system Peter must navigate to Financial Management /Receivable & Payable / Transactions / Manual settlement and create a new manual settlement as described below:

Transaction date => 29-September-2021
Accounting date => 01-October-2021
Description => October renting

Then Peter goes to "Create Payment" window and enter a new one as described below:
Business Partner => Lessee BP (previously created as a creditor and with BP tax category = Lessee)
Description => October renting
Amount => -3500
Receipt => Yes
Direct posting => No

Then Peter goes to "Balance Payment" window and enter two new ones as described below:
G/L item => "Property Rent in cash withholding"
Debit amount => -630
G/L item => "Property Rent in cash"
Debit amount => -2870

Once all of the above is done, Peter process the manual settlement and navigate to Financial Management / Receivable & Payable / Transactions / Cash Journal and create a new one and enters:
Transaction date=> 01-October-2021
Accounting date=> 01-October-2021
and then go to Lines and creates a new one as:
Cash Type => Debt-payment and then click in Debt/payment feature to get into Debt Payment Selector.

Once in the Debt Payment Selector Peter has to check "Receipt" and search by pending ones, so " proprietary rent" one just created can be selected.

After that Peter processes and posts.
Peter can navigate to the journal entry and then to the cash journal lines, and then to the payment, and once there Peter can select and post the "Settlement Canceled" in order to generate and check the final posting.

Finally, Peter has to verify that the correspondent Withholding tax reports is showing a withholding amount of 630 linked to WPropertyRent18% rate.


### Tax Report Launcher setup

As described above, Mary, the accounting manager, must decide which tax reports need to be submitted to the tax authorities depending on her company's business and in-country tax authorities requirements. Peter would help her here as he is responsible for checking the default setup and/or setting up the tax parameters, tax reports and tax report parameters as well as entering the correspondent accounting transactions in collaboration with sales (Mike) and purchase staff (Alice). Last thing for him to do will be to launch the tax reports and finally, to get the tax report output to be submitted to the tax authorities.

Once Peter knows which tax reports must be submitted to the tax authorities by talking to Mary, He will have to **install the configuration data module** delivered as part of the Tax Report Launcher module, once done he must navigate to Financial Management / Accounting / Setup / Tax Report Launcher to check that the default set up for each tax report is setup as described below:

1-Peter will have to check that there is a **new record for each tax report** which needs to be submitted to the tax authorities, containing the info below:

1. **Search key** = tax report id (in our example the Spanish tax report "110")
2. **Name** = Name of the tax report (in our example " Withholdings and payments on account of income tax (IRPF) - Spain")
3. **Description** = Description of the tax report by including tax report type and main purpose "Withholdings and payments on account made on income satisfied by Companies during a period of time "
4. **Period** = it could be either monthly, quarterly or yearly depending on tax authorities requirements and company size.
5. **Java Class Name** = separate Java class per tax report has to be entered here.
6. **Active** = set to "Yes"

2- For a specific report (the one just being created) and once the above is done, Peter will have to navigate to **"Tax Report Group"** tab and check that below 7 tax report groups are created for withholding reports, as well as 1 output tax report group is created in case of VAT reports:

1. **Identification** (1) - This tax report group must contain general data like company name, tax id number, address and so on and so forth depending on the tax report being entered in the system.
*Those data are considered **tax report parameters** for that specific tax report group; therefore Peter will have to navigate to the tax report parameter tab and check the parameters. Every parameter should be either a **"constant"**, in that case a constant value will have to be entered in the correspondent field; or an "input parameter", in that case an input type parameter will have to be selected from a list (Check box or text); or "output parameter", in that case either a Tributary key and tributary sub-key or a transaction code will have to be selected.

*Identification section will have all kind of tax parameters, **"constant"** parameters as "tax report id", **"in parameters"** to be entered by the user while launching the report, such as "contact name", as well as **"out parameters"** got from the system such as "Organization/Entity name" and "Organization/Entity tax id" as well as those tax transactions linked to a tax key and sub-key or a transaction code (in case of VAT section, see note below).

2. **Accrual** (2) - This section must contain year and period data depending on when a specific tax report has to be launched and submitted to the tax authorities.
*Those data are "in parameters" which will have to be entered by him while launching the report from Financial Management / Accounting / Analysis tools / Tax Report Launcher".

3. **Tax assessment** (3) - This section must contain tax related information such as the number of beneficiaries of an income, income type, income amounts and tax amounts for a given period. The content of this section would depend on the tax report we are entering in the system.

*Those data are considered **tax report parameters** for that specific tax report group; therefore Peter will have to navigate to the tax report parameter tab and check that the correspondent parameters are there.

*Tax assessment section will have **"in parameters"** to be entered by the user, such as "Amount to deduct only in case of complementary declaration scenario"; in general "in parameters" will be all kind of tax information needed for the tax report group which can not be obtained from the system because there is not a business logic behind. Besides, it will also have **"out parameters"** such as the sum of all the "monetary income amounts linked to a specific tax rate" regardless of the way it was entered in the system (either as a purchase or sales invoice or as a manual settlement). In general "out parameters" will be all those parameters whose value can be obtained from the system as there is a business logic behind.

4. T**ax revenue** (4) - This section must contain mainly the net tax amount to be paid to the tax authorities based on section (3) result
* Those data are considered **tax report parameters** for that specific tax report group; therefore Peter will have to navigate to the tax report parameter tab and check that the correspondent parameters are there.

* Tax revenue section will have **"in parameters"** to be entered by the user while launching a tax report, such a "X" in the case positive tax revenue is going to be paid by cash or "D" in case positive tax revenue is going to be paid by a direct debit. In general "in parameters" will be all kinds of tax information needed for the tax report group which can not be obtained from the system because there is not a business logic behind. Besides, it will also have **"out parameters"** such as "tax revenue amount" whose value will have to be a calculated value depending on section (3). In general "out parameters" will be all those parameters whose value can be obtained from the system as there is a business logic behind.

5. **Negative declaration** (5) - This section will be shown in a withholding report only in case the calculated net tax amount (Tax revenue section (4)) is = 0 , therefore this section will only have an "out parameter" based on the tax revenue value.

6. **Complementary declaration** (6) - This section will be shown in a withholding report only in case the tax report being launched is a complementary tax report to one or more tax reports already submitted to the tax authorities by the same concept and for the same period.

* Those data are considered **tax report parameters** for that specific tax report group; therefore Peter will have to navigate to the tax report parameter tab and check that the correspondent parameters are there in the case he needs to create a complementary tax report.

* Complementary declaration section will have **"in parameters"** to be entered by the user, such as "Former tax report electronic code".

7. and **Signature** (7). This section will contain a retainer/declarator (company) signature which is only needed in case of printed format not while generating an electronic format therefore there is no need for us to create this tax report group.

!!! info
    VAT tax reports do not have those kinds of above sections because they are not tax reports as such but statement tax reports, therefore a generic tax group will have to be created linked to a generic Output tax report parameter related to Transaction code parameter, for that type of VAT tax reports. 


### Tax Report Output

Tax reports can be submitted to the tax authorities either as *.pdf files, which means a printed format or as a *.txt files, which means an electronic presentation that can be sent to the tax authorities via Internet. Both formats have to comply with tax authorities well known requirements so after getting the correspondent output files Peter will have to verify that the formats are the correct ones.

Besides *.txt files can be submitted to the tax authorities by using tax authorities web applications so Peter has to make sure he gets the correspondent tax certification required to submit the files as well as he has to make sure that the files are not rejected.

Peter has also to be aware that depending on the number of transactions to be included in a tax reports as well as the company size, presentation format should be either mandatory printed format or mandatory electronic format.

Peter will have to navigate to Financial Management / Accounting / Analysis tools / Tax Report Launcher to get tax report outputs.
Once there, the information which Peter will have to enter as input parameters is:
- Organization
- Tax report
- Accounting schema
- Year
- Period
- and *.txt file name for example as an Input Parameter
Once the above is filled-in Peter can press "Generate Electronic file" to generate the *.txt file.
