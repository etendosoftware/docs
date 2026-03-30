## Navegación 

Para acceder a una ventana, escriba una parte de su nombre en el **botón Crear nuevo** o en el **botón Inicio rápido**. Etendo también ofrece un menú en árbol para facilitar la exploración.

### Inicio rápido

!!! info
    Para obtener más información sobre las funcionalidades de Inicio rápido, consulte la sección Menú rápido en la sección Barra de navegación superior.


### Estructura en árbol del menú de la aplicación

El menú de la aplicación se utiliza para hacer accesibles al usuario todos los elementos de la aplicación. Además, las tres últimas búsquedas se muestran en esta ventana.

![Navegación del menú de la aplicación](../../assets/getting-started/user-interface/navigation/application-menu.png)

#### Referencias de iconos

Existen diferentes tipos de elementos de menú que se identifican con distintos iconos:

|     |     |
| --- | --- |
| ![](../../assets/getting-started/user-interface/navigation/icon-folder.png) | Las carpetas se utilizan para organizar otros elementos dentro de ellas. Se pueden expandir o contraer para mostrar su contenido haciendo clic en ellas. |
| ![](../../assets/getting-started/user-interface/navigation/icon-report.png) | Los informes desglosan información de Etendo Classic. |
| ![](../../assets/getting-started/user-interface/navigation/icon-process.png) | Los procesos permiten realizar operaciones complejas. Algunos ejemplos serían importar datos desde un archivo o la creación automática de facturas a partir de pedidos de compra. |
| ![](../../assets/getting-started/user-interface/navigation/icon-window.png) | Las ventanas permiten al usuario crear, modificar o consultar registros. Por registros se entiende cualquier entidad que tenga sus propios datos dentro de Etendo Classic, como un producto, un pedido, una factura, etc. |

## Áreas de la aplicación 

Etendo se divide en diferentes áreas de la aplicación. Cada área está representada por una carpeta independiente accesible desde el menú de la aplicación en el área de pantalla de **la navegación superior**.

### Estructura de la ventana

La barra de herramientas contiene botones de acción y botones de proceso. Los botones de acción son genéricos y pueden aplicarse a casi todos los registros seleccionados. Los botones de proceso son específicos del registro y dependen del estado del registro y del nivel activo (cabecera o líneas o inferior).

![Estructura de la ventana](../../assets/getting-started/user-interface/navigation/window-structure.png)

|     |     |
| --- | --- |
| 1   | Botones de acción |
| 2   | Botones de proceso |

### Botones

Los botones de acción realizan las siguientes acciones:  
 

|     |     |
| --- | --- |
| ![Crear nuevo registro](../../assets/getting-started/user-interface/navigation/btn-create-new-record.png) | Crear un nuevo registro en un formulario 
| ![Insertar nueva fila](../../assets/getting-started/user-interface/navigation/btn-insert-new-row.png) | Insertar una nueva fila en la vista de cuadrícula 
| ![Guardar sus cambios](../../assets/getting-started/user-interface/navigation/btn-save.png) | Guardar sus cambios en la base de datos 
| ![Cerrar el registro actual](../../assets/getting-started/user-interface/navigation/btn-close-record.png) | Cerrar el registro actual y volver a la vista de cuadrícula 
| ![Cancelar cambios](../../assets/getting-started/user-interface/navigation/btn-cancel.png) | Cancelar los cambios y volver al último estado guardado 
| ![Eliminar el registro actual](../../assets/getting-started/user-interface/navigation/btn-delete.png) | Eliminar el/los registro(s) seleccionado(s) actualmente de la base de datos |
| ![Actualizar los datos actuales](../../assets/getting-started/user-interface/navigation/btn-refresh.png) | Actualizar los datos actuales desde la base de datos 
| ![Exportar a hoja de cálculo](../../assets/getting-started/user-interface/navigation/btn-export-spreadsheet.png) | Exportar a hoja de cálculo 
| ![Subir nuevo adjunto](../../assets/getting-started/user-interface/navigation/btn-upload-attachment.png) | Subir nuevo adjunto 
| ![Copiar registro](../../assets/getting-started/user-interface/navigation/btn-copy-record.png) | Copiar registro 
| ![Imprimir registro](../../assets/getting-started/user-interface/navigation/btn-print.png) | Imprimir registro 
| ![Enviar correo electrónico](../../assets/getting-started/user-interface/navigation/btn-email.png) | Correo electrónico 
| ![Mostrar rastro de auditoría](../../assets/getting-started/user-interface/navigation/btn-audit-trail.png) | Mostrar rastro de auditoría 
| ![Obtener un enlace directo](../../assets/getting-started/user-interface/navigation/btn-direct-link.png) | Obtener un enlace directo a esta vista o registro 
| ![Personalización del formulario](../../assets/getting-started/user-interface/navigation/btn-form-personalization.png) | Personalización del formulario 
| ![Guardar vista](../../assets/getting-started/user-interface/navigation/btn-save-view.png) | Guardar vista |.png
| ![Mostrar tabla y formulario](../../assets/getting-started/user-interface/navigation/btn-table-and-form.png) | Mostrar tabla y formulario |.png

#### Correo electrónico

Al hacer clic en el botón **Correo electrónico** se abre el popup **Email Options**, que permite enviar un correo electrónico directamente desde el documento actual al contacto del tercero.

![Popup de correo electrónico](../../assets/getting-started/user-interface/navigation/email-popup.png)

El popup contiene los siguientes campos:

- **Desde**: la dirección de correo electrónico del remitente, completada automáticamente en función de la configuración de correo electrónico del sistema. Solo lectura.
- **To**: campo de texto editable para la dirección de correo electrónico del destinatario. Incluye un botón **Select recipient** que abre un selector de contactos para elegir entre los contactos del tercero. Cuando existen varios contactos, el sistema precarga el correo electrónico siguiendo el siguiente orden:
    1. El contacto marcado como **Valor por defecto** en la pestaña Contacto de la ventana Tercero.
    2. Si no existe un contacto Valor por defecto, el último contacto modificado de la lista.
- **Asunto**: línea de asunto del correo electrónico.
- **CC**: destinatarios adicionales a copiar en el correo electrónico.
- **BCC**: destinatarios copiados sin ser visibles para los demás.
- **Reply-to**: dirección de correo electrónico a la que se dirigirán las respuestas si es diferente de la dirección Desde.
- **Message Body**: cuerpo de texto libre del correo electrónico. Se pueden utilizar las siguientes referencias y se sustituirán automáticamente por los valores del documento al enviar:

    | Referencia | Descripción |
    | --- | --- |
    | `@cus_ref@` | La referencia del cliente |
    | `@our_ref@` | La referencia del documento |
    | `@cus_nam@` | El nombre del cliente |
    | `@sal_nam@` | El nombre del comercial. |
    | `@bp_nam@` | El nombre del tercero |
    | `@doc_date@` | La fecha del documento |
    | `@doc_desc@` | La descripción del documento |
    | `@doc_nextduedate@` | La siguiente fecha de vencimiento (si existe) |
    | `@doc_lastduedate@` | La última fecha de vencimiento (si existe) |

- **Template to use**: desplegable para seleccionar una plantilla de correo electrónico predefinida, que completará automáticamente el asunto y el cuerpo.
- **Attached Documents**: lista los documentos ya adjuntos al registro. Cada adjunto puede archivarse opcionalmente. Se pueden adjuntar archivos adicionales mediante el botón **Add Attachment**.

!!! tip
    Para asegurarse de que el destinatario correcto se precarga automáticamente, marque el contacto deseado como **Valor por defecto** en la pestaña Contacto de la ventana Tercero.

Se pueden añadir varios destinatarios en los campos **To**, **CC** y **BCC** separando las direcciones de correo electrónico con `;` o `,`. El sistema valida todas las direcciones antes de enviar: si alguna no es válida, la acción de envío se bloquea y se muestra un mensaje de validación.

---
Este trabajo es una obra derivada de [Introducción a la interfaz de usuario](http://wiki.openbravo.com/wiki/User_Interface_Introduction){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.

---