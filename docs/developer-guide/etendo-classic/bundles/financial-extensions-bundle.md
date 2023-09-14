---
title: Financial Extensions Bundle | Technical Documentation
---
## Overview

In this section, the user can find technical information about the Financial Extensions Bundle.

## Conversion Rate Downloader

:octicons-package-16: Javapackage: com.smf.currency.conversionrate

### Technical Aspects

In the Currency Converters window, the necessary Apilayer data has to be configured:

-   Classname: com.smf.currency.apiconfig.CurrencyLayerConverter
-   URL: [http://apilayer.net/api/](http://apilayer.net/api/)
-   Token
-   User
-   Password

In the Conversion Rate Downloader Rule window, the configuration includes which conversions are required from which currency to which currency, what is the tolerance, etc.  
The "Conversion Rate Downloader" process in the background also needs to be configured. This is the one that will obtain the conversion and insert it in the Conversion Rates window.

## Business Partner Settlement

:octicons-package-16: Javapackage: org.openbravo.financial.bpsettlement

### **Introduction**

In this document, all the developments that need to be delivered to fulfill the Business Partner Settlement project are described in detail.

The document is structured in the different main processes that are included in the project.

-   Module definition
-   BP Settlement window
-   Add Credit Payments Pick and Execute
-   Add Pending Invoices Pick and Execute
-   Process/Cancel/Reopen Process Definition

### Module Definition

**Module Name**

Business Partner Settlements

**Description**

This module provides the ability to settle Available Credit or Pending Payments of a Business Partner that is both Customer and Provider.

**License**

OBPL

**DB Prefix**

OBFBPS

**javapackage**

`org.openbravo.financial.bpsettlement`

**Translation Required**

Yes

**Dependant Modules**

`*Openbravo 3.0 Framework* PR14Q3.1 (2.1.24019)`

**datapackage**

`org.openbravo.financial.bpsettlement`

### **BP Settlement window**

-   **Window Name**:Business Partner Settlement
-   **Help**: Window to manage settlements that cancels available credit or pending Payments of a Business Partner.
-   **Type**: Maintain
-   **Menu folder**: Financial Management >> Receivables and Payables >> Transactions. Just above 'Financial Account' window

#### **Header Tab**

-   **Name**: Header
-   **Help**: Definition of each settlement created for a business partner.
-   **UI Pattern**: Standard
-   **Table**: OBFBPS\_Settlement
-   **Sequence**: 10
-   **Tab level**: 0

Table Definition:

-   **Name**: OBFBPS\_Settlement
-   **TableName**: OBFBPS\_Settlement
-   **Java Class Name**: BPSettlement
-   **Window**: Business Partner Settlement

| **Name** | **Column Name** | **Mandatory** | **SeqNo** | **Reference** | **Show in Grid (seq)** | **Default** | **Definition** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Organization** | AD\_Org\_ID | Yes | 10  | Table Dir only allow transactional Orgs | Yes (10) |     |     |
| **Settlement Type** | BP\_Settlement\_Type | Yes | 20  | List new *BP\_Settlement Type*:  <br>  <br>\- *Credit* (CR), *Invoice* (INV) | Yes (20) |     | Stored In session: Yes  <br>  <br>Do not allow to change when there are lines. Using an Event Handler |
| **Settlement Date** | SettlementDate | Yes | 30  | Date | Yes (30) | *SYSDATE / now()* |     |
| **Business Partner** | C\_BPartner\_ID | Yes | 40  | Selector new *Customer/Vendor Business Partner*:  <br>  <br>\- HQL Filter by customer = 'Y' and vendor = 'Y'  <br>\- Grid fields: Name, Search Key, Category | Yes (40) |     | Do not allow to change when there are lines. Using an Event Handler |
| **GL Item** | C\_GLItem\_ID | Yes | 50  | GL Item Selector | Yes (50) |     |     |
| **Settlement Payment In** | FIN\_Payment\_In\_ID | No  | 60  | Payment selector | Yes (60) |     | Read Only Yes |
| **Settlement Payment Out** | FIN\_Payment\_Out\_ID | No  | 70  | Payment selector | Yes (70) |     | Read Only Yes |
| **Description** | Description | No  | 80  | Text. Length: 2000 | No  |     |     |
| **Status** | BP\_Settlement\_Status | Yes | 1010 | List new *BP Settlement Status*:  <br>  <br>\- Values: *Draft* (DR), *Processed* (CO), *Canceled* (VO) | Yes (80) | DR  | Show In Status Bar Yes  <br>  <br>Stored In Session: Yes |
| **Incoming Amount** | Incoming\_Amt  <br>  <br>(Defined in the ad\_column, but not physically in the DB) | No  | 1020 | Computed field: Sum of incoming amounts (Credit In and Sales Invoice) | Yes (90) |     | Show In Status Bar: Yes |
| **Outgoing Amount** | Outgoing\_Amt  <br>  <br>(Defined in the ad\_column, but not physically in the DB) | No  | 1030 | Computed field: Sum of outgoing amounts (Credit Out and Purchase Invoice) | Yes (100) |     | Show In Status Bar: Yes |
| **Add Credit Payments** | Add\_Credit\_Payments\_Process  <br>  <br>(AD\_Column.Name: Add Credit Payments Process) | No  | 2010 | Button (Char 1) | No  | Y   | Display Logic: type credit and status Draft |
| **Add Not Paid Invoices** | Add\_Invoices\_Process  <br>  <br>(AD\_Column.Name: Add Invoices Process) | No  | 2020 | Button (Char 1) | No  | Y   | Display Logic: type invoice and status Draft |
| **Process Settlement** | Process\_Settlement | No  | 2030 | Button (Char 60) new *BP Settlement Action* List:  <br>  <br>\- Values: *CO* Process, *VO* Cancel, *RE* Reactivate | No  | *CO* |     |

##### **OBFBPS\_Settlement\_trg trigger**

Trigger to avoid modifying any field when the Settlement is in status Processed or Canceled.

When the status is changing from *CO* to any other it should allow setting `FIN\_Payment\_In\_ID` and `FIN\_Payment\_Out\_ID`  to null.

#### **Credit In Tab**

-   **Name**: Credit In
-   **Help**: Each Payment In with available credit to consume that it is canceled in this settlement.
-   **UI Pattern**: Read Only
-   **Table**: OBFBPS\_Credit\_Payment
-   **Sequence**: 20
-   **Tab level**: 1
-   **Display Logic**: Settlement Type Credit
-   **Auxiliary Input**: *IsSoTrxTab* value *Y*

Table Definition:

-   **Name**: OBFBPS\_Credit\_Payment
-   **TableName**: OBFBPS\_Credit\_Payment
-   **Java Class Name**: CreditPayment
-   **Window**: Business Partner Settlement

| **Name** | **Column Name** | **Mandatory** | **SeqNo** | **Reference** | **Show in Grid (seq)** | **Default** | **Definition** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Credit Payment** | FIN\_Payment\_ID | Yes | 10  | Payment Selector | Yes (10) |     |     |
| **Settlement Amount** | Settlement\_Amt | Yes | 20  | Amount | Yes (20) |     |     |
| **Is Sales Transaction** | IsSOTrx | Yes |     | Yes/No | No  | @IsSoTrxTab@ (Auxiliary Input value) | Hidden Field |

##### **OBFBPS\_Credit\_Payment trigger**

Trigger to avoid modifying any field when the Settlement is in status Processed or Canceled.

When the status is changing from *CO* to any other, it should allow setting `FIN\_Payment\_In\_ID` and `FIN\_Payment\_Out\_ID` to null.

#### **Credit Out Tab**

It is the same as Credit In with these differences:

-   **Name**: Credit Out
-   **Help**: Each Payment Out with available credit to consume that it is canceled in this settlement.
-   **Sequence**: 30
-   **Tab level**: 1
-   **Auxiliary Input**: *IsSoTrxTab* value *N*

#### **Sales Invoice Tab**

-   **Name**: Sales Invoices
-   **Help**: Each not paid Sales Invoice that it is canceled in this settlement.
-   **UI Pattern**: Read Only
-   **Table**: OBFBPS\_Invoice
-   **Sequence**: 40
-   **Tab level**: 1
-   **Display Logic**: Settlement Type Invoice
-   **Auxiliary Input**: *IsSoTrxTab* value *Y*

Table Definition:

-   **Name**: OBFBPS\_Invoice
-   **TableName**: OBFBPS\_Invoice
-   **Java Class Name**: SettledInvoice
-   **Window**: Business Partner Settlement

| **Name** | **Column Name** | **Mandatory** | **SeqNo** | **Reference** | **Show in Grid (seq)** | **Default** | **Definition** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Invoice** | C\_Invoice\_ID | Yes | 10  | Invoice Selector | Yes (10) |     |     |
| **Settlement Amount** | Settlement\_Amt | Yes | 20  | Amount | Yes (20) |     |     |
| **Is Sales Transaction** | IsSOTrx | Yes |     | Yes/No | No  | @IsSOTrxTab@ (Auxiliary Input value) | Hidden Field |

##### **OBFBPS\_Invoice\_Trg trigger**

Trigger to avoid modifying any field when the Settlement is in status Processed or Canceled.

#### **Purchase Invoice Tab**

Same as Sales Invoice with these differences:

-   **Name**: Purchase Invoice
-   **Help**: Each not paid Purchase Invoice that it is canceled in this settlement.
-   **Sequence**: 50
-   **Tab level**: 1
-   **Auxiliary Input**: *IsSoTrxTab* value *N*

### **Process/Cancel/Reopen Report and Process**

*Report and Process* to manage bp settlements.

-   Name: BP Settlement Process.
-   UI Pattern: Standard
-   Data access level: Organization
-   All flags to *false*
-   Parameter *Action*
    -   Reference *List*. *BP Settlement Action*, the list assigned to the button.
    -   Validation *BP Settlement Valid Actions*. Filters the available actions based on the *BP\_Settlement\_Status* column value.
        -   Status *Draft (DR)*: *Process (CO)*
        -   Status *Processed (CO)*: *Cancel (VO)*, *Reactivate (RE)*
        -   Status *Canceled (VO)*: None (the button should be hidden as well).
    -   Default value: value of `Process\_Settlement` column.
-   Process class: `org.openbravo.financial.bpsettlement.process.BPSettlementProcess`
-   Similar example in *Payment Process* Report and Process.

#### ***BPSettlementProcess*** **java class**

Extends `org.openbravo.service.db.DalBaseProcess`.

Validations:

-   Status - action validation.
    -   Settlements in status *DR* can only be processed.
    -   Settlements in status *CO* can only be canceled or reactivated.
    -   Settlements in status *VO* cannot be modified.

##### ***Process CO*** **action**

This action does an extra validation:

-   When it is an invoice settlement type, ensure that there are invoices and total amounts for purchase and sales invoices are the same.
    -   If it is a credit settlement type, the same check with credit payments.
-   Ensure that there are no invoices and credit payments in the same settlement.

###### **Invoice type**

Create and process a Payment In with all the sales Payment Schedule Details included in the `OBFBPS\_Invoice` table for the settlement. Create a similar Payment Out with the purchase Payment Schedule Details.

Add a Payment Detail on each payment using the *GL Item* defined in the settlement, so the total amount of each payment is Zero.

Set the generated payment ids on `FIN\_Payment\_In\_ID` and `FIN\_Payment\_Out\_ID` columns.

Set the `BP\_Settlement\_Status` to *CO* and the `Process\_Settlement` to *VO*

To build the Payments based on the selected Payment Schedule details, use the following public method:

```java
org.openbravo.advpaymentmngt.process.FIN\_AddPayment.savePayment(FIN\_Payment \_payment, boolean isReceipt, DocumentType docType, String strPaymentDocumentNo, BusinessPartner businessPartner, FIN\_PaymentMethod paymentMethod, FIN\_FinancialAccount finAccount, String strPaymentAmount, Date paymentDate, Organization organization, String referenceNo, List<FIN\_PaymentScheduleDetail> selectedPaymentScheduleDetails, HashMap<String, BigDecimal> selectedPaymentScheduleDetailsAmounts, boolean isWriteoff, boolean isRefund, Currency paymentCurrency, BigDecimal finTxnConvertRate, BigDecimal finTxnAmount)
```


To add the GL Item payment details use the following public method:

```java
org.openbravo.advpaymentmngt.process.FIN\_AddPayment.saveGLItem(FIN\_Payment payment, BigDecimal glitemAmount, GLItem glitem)
```

To process the payment use the following public method (strAction: *P*):

```java
org.openbravo.advpaymentmngt.process.FIN\_AddPayment.processPayment(VariablesSecureApp vars, ConnectionProvider conn, String strAction, FIN\_Payment payment)
```

###### **Credit type**

Create and process a Payment In with all the sales credit payments included in the `OBFBPS\_Credit\_Payment` table. A similar Payment Out is created with the purchase credit payments.

For each selected credit payment, update its description with the new payment document number and increment the Used Credit amount by the settled amount. Link the credit payment to the new payment.

Add a Payment Detail on each payment using the *GL Item* defined in the settlement, so the total amount of each payment is Zero.

See an example on how to add the selected credit payments to the new payments in the following method:

```java
org.openbravo.advpaymentmngt.actionHandler.AddPaymentActionHandler.addCredit(FIN\_Payment payment, JSONObject jsonparams)
```

Note that to link the credit payments with the new payment, it is used the public method:

```java
org.openbravo.advpaymentmngt.process.FIN\_PaymentProcess.linkCreditPayment(FIN\_Payment newPayment, BigDecimal usedAmount, FIN\_Payment creditPayment)
```

##### ***Cancel VO*** **action**

It cancels the Payments generated in this settlement and stored in `FIN\_Payment\_In\_ID` and `FIN\_Payment\_Out\_ID` columns.

To cancel the payment, use the following public method (strAction: *V*):

```java
org.openbravo.advpaymentmngt.process.FIN\_AddPayment.processPayment(VariablesSecureApp vars, ConnectionProvider conn, String strAction, FIN\_Payment payment)
```

Sets the `BP\_Settlement\_Status` to *VO* and the `Process\_Settlement` to *VO*

##### ***Reactivate RE*** **action**

As in *Cancel* action cancels the payment generated on the settlement.

Sets the `BP\_Settlement\_Status` to *DR* and the `Process\_Settlement` to *CO*

Sets to null the `FIN\_Payment\_In\_ID` and `FIN\_Payment\_Out\_ID` columns.

## Banking Pool

:octicons-package-16: Javapackage: com.etendoerp.bankingpool

### Overview

This document covers how to create a process that automatically generates a new Finance Plan or updates a Finance Plan from the Financial Management >> Accounting >> Transactions >> Financial Type Configuration window.  It also provides a structure that should be considered when creating the Java class that is responsible for performing these new processes.

### Creating the new Java Class

The Java class in charge of creating the financing plan must extend the Java `FinanceTypeTemplate` class. It provides some abstract methods to be performed and other methods that are useful when creating the new process. The basic structure that the new Java class must follow is the following:

```java
package com.etendoerp.bankingpool.types;
import com.etendoerp.bankingpool.FinancialTypeConfiguration;
import java.math.BigDecimal;
import java.util.Date;
public class NewFinancialType extends FinanceTypeTemplate {
 @Override
 public void exec(FinancialTypeConfiguration configuration, Date date,
     boolean isNewFinancePlan) {
   if (isNewFinancePlan) {
     for (int paymentNo = 0; paymentNo < configuration.getInstallmentNo(); paymentNo++) {
       //Implement the creation of the new Financing Plan
     }
   } else {
     for (int paymentNo = 0; paymentNo < configuration.getInstallmentNo(); paymentNo++) {
       //Implement the update of the Financing Plan
     }
   }
 }
 @Override
 public BigDecimal getInstallment(FinancialTypeConfiguration configuration,
     BigDecimal totalAmortization, int totalInstallment) {
   //Calculate the value of the Installment
   return null;
 }
 @Override
 public BigDecimal getRecalculatedInstallment(FinancialTypeConfiguration configuration,
     BigDecimal totalAmortization, BigDecimal residualValue, int totalInstallment) {
   //Calculate the value of the installment recalculation
   return null;
 }
}
```

The Exec method is the method executed when a new Finance Plan is created or the Finance Plan is to be modified.

The Exec method receives 3 parameters:

-   configuration: The record of the Financial Type Configuration window to which the new finance Plan is created or modified.
-   date: The date that is passed as a parameter when creating a finance Plan.
-   isNewFinancePlan: Check that indicates whether a new finance plan is being created or updated. If called from the Create Finance Plan button this parameter will be True and if called from the Update Finance Plan button the parameter will be False.

The abstract class `FinanceTypeTemplate` has implemented several methods that can be useful, among them can be found:

-   newFinancePlan: Creates a new installment of the finance plan
-   setDate:  Assigns a date to the date field in a finance plan record
-   setAllDates: Assigns the date to the new Financing plan taking into account the payment date and frequency defined in the header
-   getLastFinancePlanWithInvoice: Obtains the last installment of the financing plan with an invoice
-   getLastFinancePlanWithPayment: Obtains the last installment of the financing plan with a payment
-   getMonthlyInterest: Performs the calculation (% Annual Interest/(12/frequency))
-   getCapitalizedInterest: (1+% monthly Interest)^Installment Nro^
-   getResidualValueDivideCapitalizedInterest: Performs the calculation Residual Value/Capitalized Interest.
-   setAmortizationRenting: Performs the calculation Installment - Interest
-   setTotalAmortization: Calculates the total amount paid up to that point in the finance plan
-   setPendingAmortization: Calculates the outstanding amount to be paid in the finance plan
-   setInterest: Performs the calculation ((last Pending Amortization\*% annual Interest)/12)\*frequency
-   setCommission: Assigns the commission defined in the header
-   setBusinessPartner: Assigns the Financial Bank/Entity defined in the header
-   setProject: Assigns the Project defined in the header
-   setCostCenter: Assigns the Cost Center defined in the header
-   setFirstPendingAmortization: Method of calculating the outstanding amortization for the first installment
-   getFinancePlanToRecalculate: Method that obtains all the financing plan installments to be updated if you want to update a finance plan

The abstract methods must be implemented in the new Java class and, if required, an override can be made on any of the methods of the `FinanceTypeTemplate` class.

### Creating the new Financial Type

In the Financial Type window a new record is created with the new Financial Type and in the Class Name field the package of the Java class that was implemented is entered followed by the Java class name.

![](/assets/drive/O0wwVyzJUyoTZblrURHjjOMPgcwQ1-NPr8XlI1qaE37Mo0PQ1WVVdHlOV1YPDpBjbzzeDaOgIsWoS01ptNgGT3_VintShkcxoZGdioZ8jTNuk-CyXUxZNjmSa8YaEKwlP58Gv3AXBmqEmdG2IQ.png)

By simply filling in the Class Name field, the Create New Funding Plan and Update Funding Plan button will be visible.

![](/assets/drive/aq3IBl8B85MUhWR_N0Buo6qjtcxAhESwYOpGkh8Hn1X-ka9jGGVpgfaW3jzbzfuY2Bca2F3O-zPaU3GEtdYEVLy2_u0_f1wVNF3rjteWPBBbCFIM4Lv_ZW5FEMni5EVA2IKgtiOckQPrzhSa1g.png)

![](/assets/drive/_r4oVdOsDGq8rLR2_c2foimTnGGh66TGlUIs1J_ZiWG4yuSXnNNMLDFAwtN4D6w_GU_XjgJ8Ix5s9KF4jrTAKHsdLliRdPS06BqHgl8hPYmf9QvYfbg9oOwWRUp9pBNbhcIDN6KOtS07OornYw.png)

There is no need to modify any of the 2 buttons, as they automatically execute the Exec method of the Java class specified in the Financial Type.

## Advanced Financial Docs. Processing

:octicons-package-16: Javapackage: com.etendoerp.advanced.financial.docs.processing

:octicons-package-16: Javapackage: com.etendoerp.advanced.financial.docs.processing.template

### Undo Closed orders / Unvoid voided invoices hooks

New hooks have been added to the 'Undo Close' and 'Unvoid' processes, from the Sales/Purchase orders and invoices respectively. 
These hooks allow the developer to add new validations before and/or after the action is executed, and thus create new automations more easily.

### How to define an UnvoidInvoiceHook instance
- Define the class for hook, implementing the `UnvoidInvoiceHook`  interface. This hook is executed when a user tries to unvoid a voided invoice:

```
public class UnvoidInvoiceImpl implements UnvoidInvoiceHook {
  @Override
  public OBError preProcess(Invoice invoice) {
    System.out.println("This is an example of pre method hook");
    return new OBError();
  }

  @Override
  public OBError postProcess(Invoice invoice) {
    System.out.println("This is an example of post method hook");
    return new OBError();
  }
}
```

### How to define a UndoCloseOrderHook instance
- Define the class for hook, implementing the UndoCloseOrderHook interface. This hook is executed when a user tries to undo a closed order:

```
public class UndoOrderImpl implements UndoCloseOrderHook {

  @Override
  public OBError preProcess(Order order) {
    System.out.println("This is an example of pre method hook");
    return new OBError();
  }

  @Override
  public OBError postProcess(Order order) {
    System.out.println("This is an example  of post method hook");
    return new OBError();
  }
}
```

