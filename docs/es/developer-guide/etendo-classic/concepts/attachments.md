---
title: Adjuntos
tags:
    - Adjunto
    - Registros
    - API

status: beta
---

#  Adjuntos

##  Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

Etendo tiene un modelo de adjuntos integrado en el que puede adjuntar cualquier número de registros a un registro en particular, como Pedido de venta, Remito, Facturas, etc. Todos los adjuntos pueden descargarse o eliminarse desde el propio registro.

##  API para obtener adjuntos

Hay 2 API que obtienen el directorio de un adjunto y también obtienen el directorio donde debe almacenarse un nuevo adjunto.

###  API para obtener adjuntos existentes

El adjunto puede obtenerse mediante un método de API en TabAttachments. El método **TabAttachments.getAttachmentDirectory** puede utilizarse para obtener un adjunto en particular. Los argumentos que deben pasarse son:

* UUID de la ad_table 
* UUID del registro 
* fileName 

Devuelve la ruta del adjunto relativa al directorio de adjuntos. El directorio de adjuntos puede obtenerse desde las propiedades de Etendo en código java usando OBPropertiesProvider. ?

Por ejemplo, para obtener un adjunto `test.txt` del recordId `0F3A10E019754BACA5844387FB37B0D5`, tableId `259`, el método puede utilizarse de la siguiente manera:
    
```
String attachmentDirectory = TabAttachments.getAttachmentDirectory("259","0F3A10E019754BACA5844387FB37B0D5","test.txt");
```

La API también gestiona el caso en el que el adjunto se almacena usando el modelo anterior de `tableId`- `recordId`.

###  API para obtener el directorio para guardar nuevos adjuntos

Al guardar nuevos adjuntos, el método **TabAttachments.getAttachmentDirectoryForNewAttachments** puede utilizarse para obtener el directorio en el que debe almacenarse el adjunto. Los argumentos que deben pasarse son:

* `tableId` 
* `recordId` 

El valor devuelto es el directorio para guardar el `record.Note` que el directorio devuelto es relativo al directorio de adjuntos de Etendo.

##  Migración de adjuntos del modelo anterior al modelo mejorado

Los adjuntos existentes que siguen el modelo anterior pueden migrarse al último modelo mejorado usando una tarea ant `migrate.attachments`.

---

Este trabajo es una obra derivada de [Adjuntos](http://wiki.openbravo.com/wiki/Attachments){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.