---
title: Financial Extensions Bundle | Technical Documentation
---
:octicons-package-16: Javapackage: `com.etendoerp.financial.extensions`

## Overview

In this section, the user can find technical information about the Financial Extensions Bundle.

## Banking Pool

:octicons-package-16: Javapackage: `com.etendoerp.bankingpool`

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

![](../../../assets/drive/O0wwVyzJUyoTZblrURHjjOMPgcwQ1-NPr8XlI1qaE37Mo0PQ1WVVdHlOV1YPDpBjbzzeDaOgIsWoS01ptNgGT3_VintShkcxoZGdioZ8jTNuk-CyXUxZNjmSa8YaEKwlP58Gv3AXBmqEmdG2IQ.png)

By simply filling in the Class Name field, the Create New Funding Plan and Update Funding Plan button will be visible.

![](../../../assets/drive/aq3IBl8B85MUhWR_N0Buo6qjtcxAhESwYOpGkh8Hn1X-ka9jGGVpgfaW3jzbzfuY2Bca2F3O-zPaU3GEtdYEVLy2_u0_f1wVNF3rjteWPBBbCFIM4Lv_ZW5FEMni5EVA2IKgtiOckQPrzhSa1g.png)

![](../../../assets/drive/_r4oVdOsDGq8rLR2_c2foimTnGGh66TGlUIs1J_ZiWG4yuSXnNNMLDFAwtN4D6w_GU_XjgJ8Ix5s9KF4jrTAKHsdLliRdPS06BqHgl8hPYmf9QvYfbg9oOwWRUp9pBNbhcIDN6KOtS07OornYw.png)

There is no need to modify any of the 2 buttons, as they automatically execute the Exec method of the Java class specified in the Financial Type.

## Advanced Financial Docs. Processing

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.financial.docs.processing.template`

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


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.