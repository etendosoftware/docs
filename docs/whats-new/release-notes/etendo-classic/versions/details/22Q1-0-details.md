---
title: Details 22Q1.0
---

## EPL-3

#### JARs format supported in Core and Modules.

This allows Etendo to be installed and deployed using compiled Java distributed in JAR format, without losing compatibility with the legacy source format. For this, we work on the tasks of publishing, compiling and deploying the code supported as a JAR.  
If you work with Etendo in JAR format, you will only visualize some configuration and modules directories, all the rest is in build volatile folder.

You can read more about how to install Etendo modules in JAR format reading [Install modules in Etendo](/docs/legacy/technical-documentation/etendo-environment/setup-and-upgrade/modules/22q1/install-modules-in-etendo) page.

You can read the [Publish modules to a Nexus repository](/docs/legacy/technical-documentation/etendo-environment/platform/22q1/publish-modules-to-a-nexus-repository) page to find out about the new way of publishing.

We developed a tool that searches for JARs in the source code and verifies if it exists in maven central, after that, it generates a file in which it declares the dependencies found. You will be able to remove all these heavy dependencies and let Gradle do its job. Read more in [Search JARs Tool](/docs/legacy/technical-documentation/etendo-environment/requirements-and-tools/developer-tools/22q1/search-jars-tool)

You can migrate the Core format from Source to JAR and the other way around. Read more information in \[Core format migration\][core-format-migration](/docs/legacy/technical-documentation/etendo-environment/setup-and-upgrade/installation/22q1/core-format-migration)

You can upgrade Etendo to new versions in only a few steps following the [Upgrade Etendo](/docs/legacy/technical-documentation/etendo-environment/setup-and-upgrade/upgrade) guide.

## EPL-50

#### Property Fields are executing callouts when they should not

**Issue Description**
When there is a property field defined for certain window, the callout of the referenced field gets executed. This is wrong.
For example, defining a property field in the Sales Invoice window referencing a field of the Sales Order window, will execute a Sales Order callout, an it will likely fail with an exception.

**Solution Design**
FormInitializationComponent should be making a special consideration when determining which fields have a callout, by checking if the current field is a property field or not.

## EPL-56

#### Error when trying to unpost a document without accounting lines

**Error's description**  
When trying to unpost a document that did not generate any accounting lines (fact_acct records), an error is raised.  
An example of a document that does not have any accounting lines after being posted is a Goods Shipment without price (in its related Sales Order).

**Solution Design**  
The root issue is a null pointer exception in the ResetAccounting class. The Posted class will try to select the organization and client of the accounting records, and given that there are none, the values are sorted as empty strings. This leads to the NullPointerException down the line.

Either class should check their input so that the exception is not raised, but the document should also be left as Posted = 'N' without errors facing the user.

**Affected Version**  
21Q4

## EPL-72

#### Some configuration files are overwritten after expanding Core Version

**Error description: **
After doing a version update of Etendo core the Openbravo.properties configuration file is completely overwritten by modifying the following points:

- attach.path
- context.name
- source.path
- bbdd.url
- bbdd.sid
- allow.root

The Format.xml file was also modified, probably for the same as point 1).

**Steps to reproduce the error:**
./gradlew expandCore (in the main directory of the ERP)

**Expected result:**
A clean update with no overwritten settings.

**Affected Version:**
Specifically snapshot 20.2.1.1636372732–20211108.135711–2

## EPL-73

#### Old sequences are used instead of the new ones generated

**Error's description**  
When the sequence defined with the new process is used and the mask to include dates or some prefix is changed, the old sequence is called and generates a wrong result.

**Steps to reproduce the error**

- Log-in as system administrator.
- Go to tables and columns and search ‘c_invoice' table and modify 'DocumentNo’ record:
- Reference: Transactional Sequence.
- Run './gradlew martbuild'
- Change role to 'QA Testing'
- Go to General Setup || Application || Create Sequences
- Select '\*' organization and click 'Done' (Execute the process which creates the sequences).
- Go to Financial Management || Accounting || Setup || Document Sequence
- pen as form the register (Spain, Invoice-Document No., AR Invoice).
- Change the mask: Mask: y-###-##### and Save.
- Create a new sales invoice register

**Expected result**  
The documentNo record should show a preview like “2021-100-0001“

**Affected Version**  
Etendo 21Q4

## EPL-91

#### Transactionality is not guaranteed when modifying the document type

**Error's description**  
When a document is saved and the sequence is generated, if the document type is changed, the callout changes the documentNo and the transactionality is broken

**Steps to reproduce the error**  
-Create a new invoice and save it

-Change the document type and save again

**Expected result**  
An error message should be shown

**Solution Design**  
Auto generate event observers in the compilation time (like the contributors generation) and throw an exception in case of updating the transactional sequence field.

**Affected Version**  
21Q4

## EPL-94

#### The sequence preview is not masked correctly

**Error's description**
When a new document is created, the preview in the documentNo field only shows the next number but not masked (because a legacy callout is called)

**Steps to reproduce the error**
Create a new invoice

**Expected result**
The documentNo field preview shows the same sequence as when the document is saved

**Solution Design**
Modify the legacy callout to identify if the field is a transactional sequence reference and avoid to execute the logic.

**Affected Version:**
21Q4

## EPL-97

#### Post button gets the message "Error" when it should indicate "Document Disabled" when posting a payment/collection.

**Error's description:**
When trying to post a Collection, being disabled for accounting the table fin_payment, it remains in 'Error', when it should be in 'Document disabled'
According to the log, the error is in the module com.smf.jobs

**Steps to reproduce the error:**

1. Disable accounting for the Fin_Payment table
2. Create a payment in/payment out, complete it and then post it.

**Expected behaviour**:
When accounting is not enabled for that window in the posting button, after an attempt is made to post it, it should be shown as "Document Disabled".

**Affected Version:**
Etendo 21Q3 - 21Q4

## EPL-98

#### Unexpected error with the Etendo logo and Etendo favicon.

**Error's description:**

1\. The Openbravo logo is shown when the system does not find the page you try to visit.

2\. The Openbravo favicon is shown when the system does not find the page you are trying to visit, but if the page is found, the Etendo favicon is not shown and it remains blank.

3\. The Etendo logo is not shown in the login page.

**Affected Version:**  
Etendo  21Q4

## EPL-109

#### When a translation version module is updated, the changes are not applied

**Error's description**
If changes were made to an installed module, these changes are not applied when an update.database is run.

**Steps to reproduce the error**

- Install a translation module, e.g. moduleDeps ('com.etendoerp:quotation.es_ES:latest.release@zip')
- Make a change in this module and change the version in AD_MODULE.xml
- Run ./gradlew update.database smartbuild
- Verify the change is not applied

**Expected behaviour**  
The change has been applied

**Affected Version**  
Etendo 21Q4.1

## EPL-118

#### Filter nexus credentials in Setup task

**Error's description**  
When the setup task is executed and the credentials are configured in the gradle.properties, they are copied to the Openbravo.properties.

**Steps to reproduce the error**  
Add nexus credentials in build.gradle and execute ./gradlew setup task.

**Expected behaviour**  
The credentials must not be added in Openbravo properties file

**Affected Version**  
21Q4.1 >> Plugin 1.0.0

## EPL-119

#### Delete ad_error_log from the compilation tasks

**Error's description**  
\[ant:sql\] Failed to execute: DELETE FROM ad_error_log where system_status=(select system_status from ad_system_info)\[ant:sql\] org.postgresql.util.PSQLException: ERROR: relation "ad_error_log" does not exist

**Steps to reproduce the error**  
When compilation tasks are executed, this error is shown, because this relation was deleted.

**Expected behaviour**  
Description of the expected behaviour without the bug.

**Affected Version**  
Develop - 22Q1

**Solution Design**  
Find the task that executes this sql and delete it.

## EPL-192

#### Accounting status field is editable

**Error's description:**
Etendo has the new functionality of the 'Accounting Status' field which details the accounting status of the records. Currently, it is editable by the user and should be in read-only mode.It is visible in the c_invoice, m_inout, fin_payment, m_inventory and fin_finacc_transaction tables.

**Steps to reproduce the error**

- Go to 'Sales Invoice' window
- Open a record in form mode
- Verify that 'Accounting Status' is editable

**Expected behavior**
The 'Accounting status' field must be read-only.

**Affected Version**
Etendo 21Q4.1

## EPL-193

#### The 'Posted' column has no default value

**Error's description:**
In the ‘M_Inventory’ and ‘M_InOut’ tables, the 'Posted' column has no default value set.

**Steps to reproduce the error**

- Login as ‘System administrator’
- Go to 'Tables and Columns'
- Select 'M_InOut' table
- Verify that 'Posted' column has not defaulted value
- Go to 'Reference'
- Open 'ALL_ACCOUNTING STATUS'
- Sort 'LIST REFERENCE' alphabetically
- Verify that the first value is 'Cost Not Calculated'
- Login as 'F&B International Group Admin'
- Go to 'Goods Shipment'
- Create a new Good Shipment
- Verify that the value of the 'Accounting Status' field is 'Cost Not Calculated'.

**Expected behavior**
The 'Accounting Status' field must have a default value.

**Affected Version**
Etendo 21Q4.1

## EPL-195

#### Landscape balance sheet and profit & loss and only with headings

**Issue Description**
Allow download the pdf from balance sheet and profit & loss in landscape mode.

**Solution Design**

- Add a new check for select if the report should be downloaded in landscape or not.
-
- Create a new jrxml in landscape mode for balance sheet report
-
- Create a new jrxml in landscape mode for profit & loss report
-
- Modify the java implementation for print one jrxml or jrxml in landscape depending the new check created previously

**Use/Test Cases**

- Given: “Balance Sheet AND P&L Structure Process“
- When: Generate the pdf to print the balance sheet report or profit & loss report and select the check for print in landscape in true
- Then: Generate the pdf to print the balance sheet report or profit & loss report and select the check for print in landscape in true And you should see the pdf downloaded are in landscape with the new jrxml created

## EPL-220

#### buildValidations and moduleScript classes missing in modules_core

**Error description **
The buildValidation and modulesScript of the modules_core are not being distributed in the core.

**Steps to reproduce the error**
Run update.database

**Expected behaviour**
The buildValidationsand modulesScript cases are found in the project and executed.

**Affected version**
21Q4

**Solution design**
Compile the buildValidations and mosduleScript and add them to the core repository.
