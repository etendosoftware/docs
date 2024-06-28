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

[**SQL Expert**](../../user-guide/etendo-copilot/bundles/sql-expert.md)

In the version [1.1.0](../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the SQL Expert has been included.
With this assistant, you will be allowed to **formulate questions** in natural language, and the system will automatically generate the necessary SQL query to return data in code or natural language.

---

## April 2024

### Copilot Extensions

[**Purchase Expert Assistant**](../../user-guide/etendo-copilot/bundles/copilot-purchase-expert.md)

In the version [1.1.0](../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the Purchase Expert Assistant has been included.
Your purchase orders are made easier with the new Copilot assistant. Interact via **text or by uploading images or PDFs** with the purchase order data, and the assistant will automatically generate a draft.

### Spanish Localization

**Optimizations**

As of version [1.9.4](../../whats-new/release-notes/etendo-classic/bundles/localization-spain-extensions/release-notes.md) of this bundle, we have simplified maintenance by replacing the `org.openbravo.util.saaj.impl` and `org.openbravo.util.javax.xml.soap` module dependencies with the new Maven dependencies [**Jakarta SOAP Implementation**](https://mvnrepository.com/artifact/com.sun.xml.messaging.saaj/saaj-impl/1.5.3){target="_blank"} and [**Jakarta SOAP with Attachments API**](https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2){target="_blank"}.

To take advantage of these enhancements, when upgrading to version 1.9.4 or higher, be sure to manually remove the old modules from the `/modules` directory so that the new build will use the new dependencies.

---

## March 2024

### Etendo Classic

**Optimizations**

As of version [24.1.0](../../whats-new/release-notes/etendo-classic/release-notes.md), the support for [**Tomcat 9**](https://tomcat.apache.org/download-90.cgi){target="_blank"} has been updated.

### Copilot Extensions

[**OCR Tool**](../../developer-guide/etendo-copilot/available-tools/ocr-tool.md)

In the version [1.0.0](../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md) of the Copilot Extensions bundle, the OCR Tool has been included.
With this tool designed for **optical character recognition**, you will be able to extract text from images or PDF files.

### Procurement Extensions

[**Purchase Invoice Validation**](../../user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchase-invoice-validation.md)

In the version [1.0.0](../../whats-new/release-notes/etendo-classic/bundles/procurement-extensions/release-notes.md) of the Procurement Extensions bundle, the Purchase Invoice Validation functionality has been included. Now, you will be able to **avoid the duplication of purchase invoices** through established rules and automatic validations.

### Platform Extensions

**Optimizations**

As of version [1.13.2](../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) of this bundle, the module dependency `org.openbravo.util.javax.xml.soap` has been removed as it was not needed for any module in this bundle. In case this dependency is needed for development, we recommend using the Maven dependency [**Jakarta SOAP with Attachments API**](https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2){target="_blank"}
