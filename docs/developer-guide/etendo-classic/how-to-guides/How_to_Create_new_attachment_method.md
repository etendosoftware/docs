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

  

#  How to Create new attachment method

##  Introduction

Note that this how to is developers focused. It describes how to implement a
new attachment method that integrates any CMS or ECM with Openbravo.

##  Attachment Method window

As system administrator the new _Attachment Method_ must be created in that
window. The _Search Key_ is used to identify the Java class implementing the
method.

##  AttachImplementation class

The class that implements the attachment method must implement the
_AttachImplementation_ abstract class. This class defines some methods that
must be implemented to have a fully functional attachment method.

The class must have a qualifier to identify it. The name must be the search
key set in the Attachment Method window. It has to follow this structure:

    
    
     @ComponentProvider.Qualifier("CMSSearchKey")

.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Don't use _Default_ qualifier as it is the one used by Core's default
attachment method.  
---|---  
  
Once the implementation have been developed, the following guide could be used
to  configure an attachment method  .

    
    
     
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

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_Create_new_attachment_method  "

This page has been accessed 4,709 times. This page was last modified on 18
April 2016, at 16:12. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

