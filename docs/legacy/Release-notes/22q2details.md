---
title: Details 22Q2
---

## EPL-57

### Posting a goods shipment with non accounting / error message displayed.

**Error's description**
When posting a goods shipment with non accounting, even though this functionality works well, an error message is shown with the correct text.

**Steps to reproduce the error**
Post a goods shipment that does not generate accounting.

**Expected result**
A success message in green is shown.

**Environment**
Etendo 21.4.0

## EPL-61

### Errors in "Add details" process displayed columns

**Error's description**
When you want to Add Details in a ‘Payment In', in the grid:

1. The column ‘c_ob_selected’ does not have label.
2. The columns Creation Date and Created By are empty.

**Steps to reproduce the error**

- Go to 'Payment In'
- Select record in status 'Awaiting Payment'
- Click on 'Add Details'
- Click right on columns
- View that column ‘c_ob_selected’ doesn’t have label
- Check columns ‘Creation Date' and 'Created By’
- View in grid that the columns are empty

**Expected Result:**

- The column 'c_ob_selected' has label
- The columns ‘Creation Date’ and ‘Created By’ are not empty

**Environmnet**
Etendo 21.4.0

## EPL-194

### Remove "External Point of Sales" view and its documentation

**Error's description:**
Showing the external point of sales window, but this window belongs to integration with POS.

**Steps to reproduce**
Search the external point of sales windows or go to Application -> Sales Management -> Setup -> External point of sales.

**Expected behavior**
Do not show External point of sales windows.

**Affected Version**
Etendo 21Q4.1

## EPL-228

### The system loses the selection order when adding lines to a new order

**Error's description**
The error occurs in windows such as the order window. Sometimes, when saving the header of a new order and want to add a line, the toolbar buttons are disabled.

**Steps to reproduce the error**

- Go to 'Sales Order' windows
- Clear filters
- Create a new sales order
- Save header
- Click on lines
- See that the toolbar buttons are disabled and it is not possible to add lines.

**Expected behaviour**
It should be possible to click the button to add a new line.

**Affected version**
Etendo 21.4.2
Etendo 22.1.0

## EPL-237

### Accounting templates defined for the m_costadjustment table are not executed

**Error's description**
In case a new accounting template is defined in the m_costadjustment table, it is never executed, and only the core one is executed.

**Steps to reproduce the error**

- Define a new accounting template for the m_costadjustment table.
- Execute the process.
- Verify in debug mode that the defined template is set but not executed. The defined for core is executed.

**Expected behavior**
The new accounting template defined must be executed.

**Affected Version**
Etendo 22.1.0

## EPL-263

### Error ocurred in payments in and payments out when payment date is null

**Error's description**
A pop up with error when pressing “Add Details“ in payment in or payment out

**Steps to reproduce the error**

- Create a payment in or payment out, remove the payment date and press the button “Add Details“.
- See a pop up with the following error.

**Expected behavior**
Show a pop up with invoices and orders.
Disappear the pop up with the error.

**Affected Version**
Etendo 22.1.0

## EPL-112

### EtendoRX - Integrations

The main objective of this new solution is to complement the existing ERP: “Etendo Classic”, making usage of new technologies and applying proved patterns and good practices while maintaining the best features it has to create integrations with third-party applications by an easy way.
Etendo has been integrated with Zapier as concept.
Zapier is a tool that allows users to integrate programs and web applications, making it possible to move information between platforms and perform combined actions.
To try it, you can read [Create a Zap using Etendo Integration](/docs.etendo.software/legacy/end-user-documentation/integrations/zapier)

## EPL-218

### Add task to compile style changes

**Issue Description:**
For a partner to be able to make modifications to the styles, it is necessary to add a gradle task that compiles the .scss files.
In addition, problems with the kubernetes plugin need to be solved. When running a smartbuild on a server the antWar and deployK8s tasks are not running.

**Solution Design:**

- In web/skins/Default/Openbravo_ERP_250.scss in line 20 change /modules/ to /modules_core/.
- Add to the build.gradle the task cssCompile in etendo_gradle_plugin

## EPL-203

### Refactor the Offer Pick Action handlers to jobs

**Issue Description**
Refactor the Offer Pick Action handlers to jobs

**Solution Design**

Convert to jobs the following classes:
OfferPickOrgActionHandler.java
OfferPickProductCategoryActionHandler.java
OfferPickAndExecBaseActionHandler.java
OfferPickProductActionHandler.java

**Use/Test Cases**

- Case 1
  Given: a discount and promotion
  When: you execute the button Add organization
  Then: this allows adding multiple organizations implemented by jobs

- Case 2
  Given: a discount and promotion
  When: the button Add Product Category is executed
  Then: this allows adding multiple Product Category implemented by jobs

- Case 3
  Given: a discount and promotion
  When: the button Add Product is executed
  Then: this allows adding multiples Product implemented by jobs

## EPL-201

### Move "Valued Stock Report" to a process definition, the report only can be downloaded in Exel and PDF formatts

**Issue Description**

- Refactor "Valued Stock Report" to a process definition maintaining the functionality.
- The report only can be downloaded in Exel and PDF formatts.

**Solution Design**

For the report valuation stock, move to process definition and remove the possibility that export in html
remove the menu and form, and the following files
src/org/openbravo/erpCommon/ad_reports/ReportValuationStock2.xml
src/org/openbravo/erpCommon/ad_reports/ReportValuationStock2.html

**Use/Test Cases**
Given: Etendo environment.
When: Execute the report valuation stock.
Then: The process should return the same result.

## EPL-199

### Refactor the process 'Payment execution' to a process definition

**Issue Description**

Refactor the process 'Payment execution' to a process definition.

**Solution Design**

modules_core/org.openbravo.advpaymentmngt/src/org/openbravo/advpaymentmngt/ad_forms/BatchPaymentExecution.html

**Use/Test Cases**

Search the process with the ‘Payment execution’ name. This opens a window where the ‘Payments’ with status ‘RPAE’ (If you want to see some values set the payment status to RPAE in DB) can be filtered.

To define a ‘process execution’ go to the financial account window and select a payment method in the ‘payment method’ tab. Set the payment execution type to Automatic and select a ‘execution process’.

**Automatic tests definition**

**Refresh grid test**

Given: A user sending a request with the search button value.
when: The user sends the request to the process handler.
then: The response should contain the retry execution.
and: The response actions should contain the refresh grid values.

**Lines not selected test**

given: A user sending the a request with the process button value.
when: The user sends the request to the process handler without selected lines.
then: The response should contain a error for the missing lines.

**Execution process not found test**

given: "A user sending a request with a selected payment".
when: "The user send the request to the process handler".
then: "The response should contain a error for the missing 'execution process'".

**Generate popup and execute the process for a custom payment**

given: The user wanting to run the execution process for a payment with automatic execution type.
when: The user sends the request to the process handler.
then: The response should contain the information of the popup.

when: The user sends the execution command for the process to be run
then: The process will execute successfully
and: The message will show the documentNo of the processed payment
and: The payment status will be diferent of 'RPAE'.

#

##
