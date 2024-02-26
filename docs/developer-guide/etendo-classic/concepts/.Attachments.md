![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  Attachments

##  Contents

  * 1  Introduction 
  * 2  Improvements to Attachment Model 
  * 3  API for fetching attachments 
    * 3.1  API for fetching existing attachments 
    * 3.2  API to fetch directory to save new attachments 
  * 4  Migrating attachments from earlier model to improved model 

  
---  
  
##  Introduction

Openbravo has an inbuilt attachment model where you can attach any number of
records to a particular record like Sales Order, Goods Shipment, Invoices etc.
All the attachments can be then downloaded or deleted from the record itself.

##  Improvements to Attachment Model

Before 3.0MP26, the attachments were stored in the attachments directory (the
attach.path property in Openbravo.properties). They were stored in this folder
structure

  * AttachDirectory 
    * tableId-recordId 
      * Attachment. 

But in few file systems like ext3 this would exceed the maximum number of
folders allowed.

To overcome this, the attachment model has been updated to save the attachment
from 3.0MP26. For eg, for table Id "259", recordId
"0F3A10E019754BACA5844387FB37B0D5", the file directory returned is
"259/0F3/A10/E01/975/4BA/CA5/844/387/FB3/7B0/D5". i.e,

  * AttachDirectory 
    * 259 
      * 0F3 
        * A10 
          * E01 
            * 975 
              * 4BA 
                * CA5 
                  * 844 
                    * 387 
                      * FB3 
                        * 7B0 
                          * D5 
                            * Attachment 

Note that the attachments can be still be stored using the previous model by
enabling the preference 'SaveAttachmentsOldWay' to 'Y'. For more information
on using preferences refer  here

##  API for fetching attachments

2 API's have been added to fetch the directory of an attachment and also to
fetch the directory where a new attachment needs to be stored.

###  API for fetching existing attachments

The attachment can be fetched through an API method in TabAttachments. The
method **TabAttachments.getAttachmentDirectory** can be used to fetch a
particular attachment. The arguments to be passed are:

  * UUID of the ad_table 
  * UUID of the record 
  * fileName 

It returns the path of the attachment relative to the attachment directory.
The attachment directory can be fetched from Openbravo properties in java code
using  OBPropertiesProvider  .

For eg., to fetch an attachment test.txt of recordId
0F3A10E019754BACA5844387FB37B0D5, tableId 259, the method can be used as
follows:

    
    
    String attachmentDirectory = TabAttachments.getAttachmentDirectory("259","0F3A10E019754BACA5844387FB37B0D5","test.txt");
    

The API also handles the case where the attachment is stored using the earlier
model of tableId-recordId.

###  API to fetch directory to save new attachments

When saving new attachments, the method
**TabAttachments.getAttachmentDirectoryForNewAttachments** can be used to
fetch the directory in which the attachment has to be stored. The arguments to
be passed are,

  * tableId 
  * recordId 

The value returned is the directory to save the record.Note that the directory
returned is relative from the attachment directory of Openbravo.

##  Migrating attachments from earlier model to improved model

The existing attachments that follows the earlier model can be migrated to the
latest improved model using an ant task **migrate.attachments** . The task has
been briefly described  here  .

Retrieved from "  http://wiki.openbravo.com/wiki/Attachments  "

This page has been accessed 9,670 times. This page was last modified on 16
August 2019, at 11:58. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

