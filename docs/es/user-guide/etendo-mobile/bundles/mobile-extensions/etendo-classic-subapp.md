---
tags:
 - Etendo Classic
 - Extensión móvil
 - Gestión de registros
 - Escaneo de inventario
 - Navegación de usuario
---

# Subapp de Etendo Classic
:octicons-package-16: Javapackage: `com.etendoerp.subapp.classic`   


## Visión general 

La **Subapp de Etendo Classic** proporciona a los usuarios una forma eficiente de acceder a la información clave de las ventanas del sistema en función de los roles de usuario, garantizando el acceso de lectura. Aunque se permite la edición de registros, se recomienda realizar la creación y gestión de datos principalmente en Etendo Classic.

La subaplicación de Etendo Classic permite a los usuarios acceder y gestionar la información de su cliente directamente desde Etendo Mobile, proporcionando una forma rápida y eficiente de **ver datos** y realizar ediciones sencillas. Además, gracias a funcionalidades como el **escaneo**, los usuarios pueden ver una demostración de la gestión de inventario escaneando productos durante el inventario físico.

!!! info
    - Para poder incluir la subaplicación, debe estar instalado el bundle Mobile Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Mobile Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=55A7EF64F7FA43449B249DA7F8E14589){target="_blank"}. <br>
    Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Mobile Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-mobile/bundles/mobile-extensions/release-notes.md).


## Configuración inicial

### Mostrar ventanas en móvil
:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Rol`

Por defecto, no se mostrará ninguna ventana en la subapp. Para permitir que las ventanas de Etendo sean visibles: 

1. El usuario debe acceder a Etendo Classic con el rol de **Administrador**.
2. Seleccione el rol que le dará acceso para mostrar ventanas en la subaplicación.
3. En la pestaña `Rol`>`Acceso a ventana`, filtre las ventanas y marque el indicador **Mostrar en móvil** en las ventanas requeridas para que se muestren en la app.

![alt text](../../../../assets/user-guide/etendo-mobile/bundles/etendo-classic-subapp/show-in-mobile.png)

### Edición de identificadores en tarjetas y filtros 
:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Ventanas, pestañas y campos`

![alt text](../../../../assets/user-guide/etendo-mobile/bundles/etendo-classic-subapp/cards.jpg){ align=right width="300" }

Cuando abre una ventana, observará que los registros se muestran en tarjetas con cierta información que es configurable. Para más información sobre las tarjetas, consulte la sección [Interfaz de Usuario - Vista de tarjetas y formulario](#vista-de-tarjetas-y-formulario).
Por defecto, se muestra un identificador de título y, opcionalmente, campos secundarios. 

Para editar esta información, puede hacerse desde Etendo Classic mediante configuraciones. 

!!!warning
    Recomendamos que esta configuración la realice un desarrollador o alguien con conocimientos técnicos. 

1. Inicie sesión como `Administrador del sistema`.
2. Vaya a la ventana `Ventanas, pestañas y campos`.
3. Filtre la ventana que desea modificar y seleccione la pestaña principal; puede tener el mismo nombre que la ventana o llamarse `cabecera`.
4. En la pestaña `Configuración móvil`, encontrará un registro de **Configuración por defecto**; debe eliminarlo y crear una nueva configuración para exportarla en un nuevo módulo en desarrollo.
5. Cree una línea por cada campo que quiera mostrar como identificador en las tarjetas; debe tener en cuenta que el primer registro creado será el título y los demás campos serán subtítulos, y el orden se respeta según la fecha de creación.
6. Debe tener en cuenta que las búsquedas pueden filtrar por cada uno de estos campos definidos como identificadores; solo se permite la búsqueda exacta o igual. También puede añadir un máximo de 5 identificadores.


Por ejemplo, por defecto la ventana `Pedido de venta` muestra los identificadores `Nº de documento` como título, `Fecha del pedido` y `Importe bruto total` como subtítulo. 

En este caso crearemos una vista personalizada, con el nombre `Pedido de venta - Vista personalizada` y se exportará en un nuevo módulo llamado `Mobile Customizations`. 

Añada 5 líneas: la primera como título será `Tercero`, y luego `Moneda`, `Estado del documento`, `Importe bruto total`, `Método de pago` y `Fecha del pedido` como subtítulos.

!!!warning 
    Recuerde que el orden de los identificadores depende de la fecha de creación y que se puede mostrar un máximo de 5 identificadores.

 ![alt text](../../../../assets/user-guide/etendo-mobile/bundles/etendo-classic-subapp/custom-view-back.png)
 ![alt text](../../../../assets/user-guide/etendo-mobile/bundles/etendo-classic-subapp/custom-view-cards.png)


## Interfaz de Usuario

### Menú de navegación


Al acceder a la subapp de **Etendo Classic**, en el inicio el usuario puede encontrar una opción de menú desde la cual puede:

- En la sección superior del menú se mostrará la imagen del usuario.
- Acceder a diferentes ventanas permitidas según su rol.
- Volver atrás, opción para regresar a Etendo Mobile.

![](../../../../assets/user-guide/etendo-mobile/bundles/etendo-classic-subapp/home-nav.png)


### Vista de tarjetas y formulario

![](../../../../assets/drive/XZFZ8AALW9g42_1StbQnRpAvIszHoPZrp6QoLw1XUQ68kz4iU5nBYCR6XVwC0k4bGJjZFRbjaGMKfOA7lUVXCtz7At6Tt5p8sJtlYHNny4Z6yn_jfHrthRnxym2n_M0GhXLWDR2p.png){ align=right width="180" }

- El usuario, según el rol, tendrá acceso a determinadas ventanas, y estas son configurables como puede verse en la sección [Mostrar ventanas en móvil](#mostrar-ventanas-en-móvil). <br> 
Algunas de las ventanas más comunes son: Producto, Tercero, Factura de venta, Pedido de venta, Factura de compra, Pedido de compra, entre otras.<br> <br> 

- Cada ventana mostrará su contenido dividiendo los registros en tarjetas, que contendrán una vista previa de los datos principales de esos registros. Estos datos se configuran por defecto y será necesaria una personalización en caso de que el usuario quiera añadir más campos o eliminar alguno de ellos, teniendo en cuenta que solo se puede mostrar un máximo de 5 campos. Para más información, visite [Edición de identificadores en tarjetas y filtros](#edición-de-identificadores-en-tarjetas-y-filtros) <br><br><br>

![](../../../../assets/drive/akwqHJKCawDOW20SxB5sxjm_wPN2hW8PfKsU8wAgfYqebtFGAbyTib-mQcX_fUuRhCz9RTDX0Utt1pY0GUF1HuzfwGig3LaOdFdHHLMK2p0DjLUWcvxxYW2agJCmHTx_JRB-8sgp.png){ align=left width="180" }

- El mismo campo presente en la vista previa será el criterio por el cual filtrar si el usuario quiere buscar un registro. Tomando como ejemplo la ventana Factura de venta, la vista previa de cada registro proporciona información relativa al número de documento y la fecha de la factura. <br><br><br>


- Los registros pueden buscarse insertando un valor o palabra clave en la barra superior **Selector**. Cada ventana tendrá disponibles ciertos filtros por campo que coincidirán con aquellos campos configurados por defecto para mostrarse en la vista previa de cada registro. En caso de que el usuario necesite añadir más filtros o eliminar algunos, será necesaria una personalización.<br><br><br><br><br> 

![](../../../../assets/drive/PY4-klREGqUyi4CtP-0Pp3gn95-eE8hr2lCDLVA4uiYTTYNTnx3exMDsx-LHTSXK5NQBo0z0Xy4sxXera3xgCpISdVbxwMzB3QjurnDInYR5oSvUqfBYDtvbElXXneXCZi8AzJmA.png){align=right width="180" }

- Al hacer clic en cualquiera de esas cajas, se mostrará información detallada sobre los registros y podrá editarse. Los campos se mostrarán uno debajo del otro. Aquellos con este símbolo “(\*)” en su título son obligatorios y aquellos con un icono de lápiz son editables.<br><br><br><br><br><br><br><br><br>
    
![](../../../../assets/drive/3tj34fwiEnwX6YiWsfv8x8ApOWqEjbtQDFERLIEqZJ6LZsXwvlkJffOm-UYEhS1y0onXLf3rtWKy75WpIqy_pn8KSITpMqW6Olqx5CNaGo5vGpex61Tj7WuCy0NxSAjdGUM0hqyt.png){ align=left  width="180" }

- Para crear un nuevo registro, el usuario debe hacer clic en el icono con el símbolo “+” y completar los campos deseados. Aquellos con el símbolo (\*) son obligatorios. Para editar un campo, el usuario debe hacer clic en el icono del lápiz. Si el campo es de tipo lista, haga clic en el icono de búsqueda para mostrar las opciones posibles. Tras seleccionar los datos correctos, pulse el botón “Hecho”.<br><br><br><br><br><br><br><br>

![](../../../../assets/drive/pJrdHx58VtWi5NCkN446WAu-Fjg1rHgWe5JJLKGFn7DJxasB8uXnXAtSPrI6gAD_Oe_3ZwkK0Pw9JYVPY6GX0R1a2-mUuYESxwzPpWOf02V0T1jskkbxUy5IddR1m2glXXbcBpJd.png){ align=right  width="180" }

- Si el campo es de tipo fecha, al seleccionar el icono de búsqueda se mostrará un calendario para seleccionar la fecha deseada. Los campos de texto libre se editan seleccionando el campo e introduciendo el valor deseado.<br><br>
- Una vez que el usuario haya introducido los datos requeridos, haga clic en el icono de guardar. Es importante tener en cuenta que el documento siempre permanecerá en estado **Borrador** y solo podrá completarse a través de Etendo Classic.<br><br><br><br> 

![](../../../../assets/drive/dGqkvbLqxGUxpuU75pgKmYjRffl9bHRLmydMSokrcPVdjhBcnIrUNzxvHzGCvCD_2QDmdE2NlAmc0FuXi11ZeNoUPvwhavOdv1jvTD1IyRgA4MKF9mhD6nCmIU-xV7mEV8DrFnb7.png){ align=left width="180" }

- Para eliminar un registro, púlselo y arrástrelo hacia la izquierda o manténgalo pulsado, seleccione todos los registros deseados y luego el icono de eliminar. Cada vez que se elimina un registro en la App, el mismo registro se eliminará también en Etendo Classic.<br><br><br><br><br><br><br><br><br><br><br>

### Botón Carpetas

![](../../../../assets/drive/Q0C8H4uO8zHgfmSaWfGMKR5tKMbWlVLOUwUMYG-_qpJBj471MxMFwx0is-MGR0WqleOE4QcqHhWhIhTfeo2xwIX-ftECC3QyeKdI-ygG7o2kGhHJ4CgAoWEgfc1KZnEHHXpaegHG.png){ align=right  width="180" }

- Al seleccionar el botón Carpetas, el usuario puede acceder a las diferentes pestañas de la ventana con información sobre los registros que se están consultando.
- Al entrar en cualquiera de las pestañas, la vista será la misma que en la ventana padre; es decir, los registros se mostrarán en cajas pequeñas y, al entrar en estas, los campos se mostrarán uno debajo del otro.<br><br>

![](../../../../assets/drive/XKeIfzzgutwdnJr5kmBVSifBZ1luxaWe3mqYM_U3uHurbAe_0TXkpjjvF5x0RWpIKXRsqYcEifdxpVeNHZjgHZ5-s6uGm8FjIf9RGIfAZoHXZAxlCqzC5H00RUmPBX01SvFgW8v2.png){  align=left width="180" }

- Para navegar en diferentes niveles, el usuario puede recurrir a los botones del sistema (Android) o a la flecha en la esquina superior izquierda o al gesto (ambos sistemas).
- Además, la **ruta o migas de pan** de qué registros y pestañas se están navegando puede mostrarse en la parte superior de la pantalla.<br><br><br><br><br><br>


### Botón Acción

A través de este botón, el usuario puede acceder a la lista de procesos disponibles correspondientes a la ventana que se está consultando y ejecutarlos.

## Asistentes de escaneo de la App móvil

:octicons-package-16: Javapackage: `com.smf.mobile.scan`

### Visión general

Los **Asistentes de escaneo de la App móvil** permiten usar la cámara para escanear códigos en la App de [Etendo Mobile](../../../../user-guide/etendo-mobile/getting-started.md).

### Ejemplos de uso

 El módulo incluye por defecto el proceso Escaneo de inventario, que se encarga de escanear este código desde un móvil y, de este modo, cambiar valores de las líneas de Inventario físico.

 A continuación, se mostrará un ejemplo desde la aplicación Etendo Mobile:

 Al entrar en la ventana Inventario físico y seleccionar un registro, será posible ver el botón **Acción**.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/PhysicalInventoryActions.jpeg)

En este botón, es posible ver el proceso que incorpora, llamado Escaneo de inventario.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ActionsInventoryScan.png)

 Al pulsar esta acción, realiza las funciones de escaneo para poder modificar valores del ítem de inventario físico que se ha seleccionado.
 
 ![](../../../../assets/developer-guide/etendo-classic/bundles/CameraScanner.png) 

Cuando se selecciona la flecha para continuar, el código del hueco de almacén en el que se encuentra el producto debe introducirse manualmente o escanearse.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/StorageBinBarCode.png) 

 Tras seleccionar el hueco de almacén, debe escanearse o seleccionarse el producto a modificar.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ProductBarcode.jpg) 

 Finalmente, introduzca la cantidad necesaria a añadir de ese producto, pulse Hecho y Guardar.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ProductQuantity.png) 

 Mientras tanto, en Etendo Classic se añadirá una línea en la pestaña **Escaneo** de la línea de inventario físico, sobre el escaneo y la cantidad que se ha establecido.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/QuantityCount.png) 

En la cabecera del inventario físico, al seleccionar una línea de escaneo, puede ejecutarse el proceso Recuento de inventario. Este se encarga de añadir al stock la cantidad que se ha establecido en el producto escaneado.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/Process.png) 

Y aquí se observarán las cantidades antes del proceso:

 ![](../../../../assets/developer-guide/etendo-classic/bundles/QuantityBefore.png) 

 Y después:

 ![](../../../../assets/developer-guide/etendo-classic/bundles/QuantityAfter.png) 

También se observará que el stock del producto se ha actualizado en el hueco de almacén indicado con la cantidad del producto:

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ProductStockAfterProcess.png) 

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.