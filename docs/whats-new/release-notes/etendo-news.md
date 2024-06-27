---
tags:
  - Etendo News
  - New Developments
  - Release Notes
  - Functional Documentation
  - Versions
---

![](../../assets/whats-new/etendo-news/etendo-news-0.png)

#

## May 2024

### Copilot Extensions

<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <a href="/user-guide/etendo-copilot/bundles/sql-expert/"><strong>SQL Expert</strong></a><br>
    With the SQL Expert, you will be allowed to <strong>formulate questions</strong> in natural language, and the system will automatically generate the necessary SQL query to return data in code or natural language.
  </div>
</div>

---

## April 2024

### Copilot Extensions

<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <a href="/user-guide/etendo-copilot/bundles/copilot-purchase-expert/"><strong>Purchase Expert Assistant</strong></a><br>
    Your purchase orders are made easier with the new Copilot assistant. Interact via <strong>text or by uploading images or PDFs</strong> with the purchase order data, and the assistant will automatically generate a draft.
  </div>
</div>

### Spanish Localization

<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <strong>Optimizations</strong></a><br>
    As of Etendo version 1.9.4 of our bundle, we have simplified maintenance by replacing the <code>org.openbravo.util.saaj.impl</code> and <code>org.openbravo.util.javax.xml.soap</code> module dependencies with the new Maven dependencies <a href="https://mvnrepository.com/artifact/com.sun.xml.messaging.saaj/saaj-impl/1.5.3" target="\_blank"><strong>Jakarta SOAP Implementation</strong></a> and <a href="https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2" target="\_blank"><strong>Jakarta SJOAP with Attachments API</strong></a>.
    To take advantage of these enhancements, when upgrading to version 1.9.4 or higher, be sure to manually remove the old modules from the <strong>modules directory</strong></a> so that the new build will use the new dependencies.
  </div>
</div>

---


## March 2024

### Etendo Classic

<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <strong>Optimizations</strong></a><br>
    As of Etendo version 24.1.0, support for <a href="https://tomcat.apache.org/download-90.cgi/" target="\_blank"><strong>Tomcat 9</strong></a> has been updated.
  </div>
</div>

### Copilot Extensions

<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <a href="/developer-guide/etendo-copilot/available-tools/ocr-tool/"><strong>OCR Tool</strong></a><br>
    With the OCR Tool designed for <strong>optical character recognition</strong>, you will be able to extract text from images or PDF files.
  </div>
</div>

### Procurement Extensions


<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <a href="/user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchase-invoice-validation/"><strong>Purchase Invoice Validation </strong></a><br>
    In the Etendo version 1.0.0, the following improvement has been included. Now, you will be able to <strong>avoid the duplication of purchase invoices</strong> through established rules and automatic validations.
  </div>
</div>

### Platform Extensions

<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <strong>Optimizations</strong></a><br>
    As of Etendo version 1.13.2, the module dependency <code>org.openbravo.util.javax.xml.soap</code> has been removed as it was not needed for any module in this bundle. In case this dependency is needed for development, we recommend using the <a href="https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2" target="\_blank"><strong>Maven Jakarta SOAP with Attachments API dependency</strong></a>.
  </div>
</div>


 

 