---
title: How to Create a new Attachment Method
tags: 
    - Customization
    - Java Extension Points
    - Attachment Management 
status: beta
---

# How to Create a new Attachment Method

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.


## Overview

This section explains how to create a **custom attachment method** in Etendo to integrate external **CMS or ECM** systems. It describes how to register the new attachment method in the application, implement the required Java class by extending `AttachImplementation`, and define the core operations for uploading, downloading, updating, and deleting attachments. This approach allows Etendo to manage files using alternative storage or **content management solutions** beyond the default attachment mechanism.

## Attachment Method window

As **System Administrator** the new Attachment Method must be created in that window. The **Search Key** is used to identify the Java class implementing the method.

## `AttachImplementation` Class

The **class** that implements the attachment method must implement the `AttachImplementation` abstract class. This class defines some methods that must be implemented to have a fully functional attachment method.

The class must have a qualifier to identify it. The name must be the search key set in the Attachment Method window. It has to follow this structure:

``` java    
     @ComponentProvider.Qualifier("CMSSearchKey")
```


!!! note
    Don't use **Default** qualifier as it is the one used by Core's default attachment method.  

Once the implementation have been developed, the following guide could be used to configure an attachment method.

    
``` java    
     
    /**
    * Public class to allow extend the functionality
    */
    
    public abstract class AttachImplementation {
    
    /**
    * Abstract method to upload files
    * 
    * @param attachment
    *          The attachment created in c_file with empty metadata
    * @param strDataType
    *          DataType of the attachment
    * @param parameters
    *          A map with the metadata and its values to be updated in the corresponding file
    *          management system and in the attachment
    * @param file
    *          The file to be uploaded
    * @param strTab
    *          The tabID where the file is attached
    * @param parameterValues
    *          List of metadata saved in database
    * @throws OBException
    *           Thrown when any error occurs during the upload
    */
    public abstract void uploadFile(Attachment attachment, String strDataType,
        Map<String, Object> parameters, File file, String strTab) throws OBException;
    
    /**
    * Abstract method to download a single file
    * 
    * @param attachment
    *          The attachment that will be downloaded
    * @return The file being to download
    * @throws OBException
    *           Thrown when any error occurs during the download
    */
    public abstract File downloadFile(Attachment attachment) throws OBException;
    
    /**
    * Abstract method to delete a file
    * 
    * @param attachment
    *          The attachment that want to be removed
    * @throws OBException
    *           Thrown when any error occurs when deleting the file
    */
    public abstract void deleteFile(Attachment attachment) throws OBException;
    
    /**
    * Abstract method to update file's metadata
    * 
    * @param attachment
    *          The attachment to be modified
    * @param strTab
    *          The tabID where the file was attached
    * @param parameters
    *          The metadata to be modified
    * @param parameterValues
    *          List of metadata saved in database
    * @throws OBException
    *           Thrown when any error occurs when updating the file
    */
    public abstract void updateFile(Attachment attachment, String strTab,
        Map<String, Object> parameters) throws OBException;
    
    /**
    * This method is used to know whether the attach method is creating a temporary file in the temp
    * directory of Openbravo server when downloading a file. If it is true, the process will remove
    * the temporary file. If it s false, the process will not remove the file
    * 
    * @return true if the attachment method creates a temporary file in Openbravo server.
    */
    public abstract boolean isTempFile();
    
    }
```



This work is a derivative of [How To Create a new Attachment Method](http://wiki.openbravo.com/wiki/How_to_Create_new_attachment_method){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/How_To_Create_a_Trigger){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
