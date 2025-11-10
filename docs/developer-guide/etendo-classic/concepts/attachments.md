---
title: Attachments
tags:
    - Attachment
    - Records
    - API

status: beta
---

#  Attachments

##  Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

Etendo has an inbuilt attachment model where you can attach any number of records to a particular record like Sales Order, Goods Shipment, Invoices, etc. All the attachments can be then downloaded or deleted from the record itself.

##  API for Fetching Attachments

There are 2 APIs that fetch the directory of an attachment and also fetch the directory where a new attachment needs to be stored.

###  API for Fetching Existing Attachments

The attachment can be fetched through an API method in TabAttachments. The method **TabAttachments.getAttachmentDirectory** can be used to fetch a particular attachment. The arguments to be passed are:

* UUID of the ad_table 
* UUID of the record 
* fileName 

It returns the path of the attachment relative to the attachment directory. The attachment directory can be fetched from Etendo properties in java code using OBPropertiesProvider. ?

For example, to fetch an attachment `test.txt` of recordId `0F3A10E019754BACA5844387FB37B0D5`, tableId `259`, the method can be used as follows:
    
```
String attachmentDirectory = TabAttachments.getAttachmentDirectory("259","0F3A10E019754BACA5844387FB37B0D5","test.txt");
```

The API also handles the case where the attachment is stored using the earlier model of `tableId`- `recordId`.

###  API to Fetch Directory to Save New Attachments

When saving new attachments, the method **TabAttachments.getAttachmentDirectoryForNewAttachments** can be used to fetch the directory in which the attachment has to be stored. The arguments to be passed are,

* `tableId` 
* `recordId` 

The value returned is the directory to save the `record.Note` that the directory returned is relative from the attachment directory of Etendo.

##  Migrating Attachments from Earlier Model to Improved Model

The existing attachments that follows the earlier model can be migrated to the latest improved model using an ant task `migrate.attachments`.

---

This work is a derivative of [Attachments](http://wiki.openbravo.com/wiki/Attachments){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 