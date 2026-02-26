---
title: Cómo crear un nuevo método de adjuntos
tags: 
    - Personalización
    - Puntos de extensión Java
    - Gestión de adjuntos 
status: beta
---

# Cómo crear un nuevo método de adjuntos

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.


## Visión general

Esta sección explica cómo crear un **método de adjuntos personalizado** en Etendo para integrar sistemas externos de **CMS o ECM**. Describe cómo registrar el nuevo método de adjuntos en la aplicación, implementar la clase Java requerida extendiendo `AttachImplementation` y definir las operaciones principales para subir, descargar, actualizar y eliminar adjuntos. Este enfoque permite a Etendo gestionar archivos utilizando almacenamiento alternativo o **soluciones de gestión de contenidos** más allá del mecanismo de adjuntos por defecto.

## Ventana Método de adjuntos

Como **Administrador del sistema**, el nuevo Método de adjuntos debe crearse en esa ventana. El **Identificador** se utiliza para identificar la clase Java que implementa el método.

## Clase `AttachImplementation`

La **clase** que implementa el método de adjuntos debe implementar la clase abstracta `AttachImplementation`. Esta clase define algunos métodos que deben implementarse para disponer de un método de adjuntos completamente funcional.

La clase debe tener un calificador para identificarla. El nombre debe ser el identificador configurado en la ventana Método de adjuntos. Debe seguir esta estructura:

``` java    
     @ComponentProvider.Qualifier("CMSSearchKey")
```


!!! note
    No utilice el calificador **Valor por defecto**, ya que es el utilizado por el método de adjuntos por defecto del Core.  

Una vez que se haya desarrollado la implementación, puede utilizarse la siguiente guía para configurar un método de adjuntos.

    
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



Este trabajo es una obra derivada de [Cómo crear un nuevo método de adjuntos](http://wiki.openbravo.com/wiki/How_to_Create_new_attachment_method){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/How_To_Create_a_Trigger){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.