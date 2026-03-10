---
tags:
  - Cómo hacer
  - Campo de propiedad
  - Información derivada
  - Reglas de validación
--- 

#  Cómo usar campos de propiedad

##  Visión general

Un **campo de propiedad** le permite mostrar información derivada en una cuadrícula/formulario. Un campo de propiedad es muy similar a un campo normal en una solapa. La única diferencia es que, en lugar de la columna, se define una propiedad (ruta).

Los campos de propiedad permiten:

  * mostrar información relacionada en una cuadrícula/formulario 
  * filtrar y ordenar por esta información relacionada 
  * mostrar información del padre en una solapa hija y filtrar/ordenar por esta información del padre 
  * crear ventanas de Etendo que muestren una tabla hija en la raíz de la ventana, haciendo posible, por ejemplo, crear una única cuadrícula que muestre todas las líneas de factura de venta a través de múltiples facturas de venta y filtrar usando información tanto del padre como del hijo. 

##  Módulo de ejemplo

Esta sección se apoya en un módulo de ejemplo que muestra ejemplos del código mostrado y comentado en esta sección.

El código del módulo de ejemplo se puede descargar desde este repositorio: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

##  Definición de campos de propiedad

Los campos de propiedad se definen de la misma forma que un campo normal en una solapa de Etendo. La única diferencia es que, en lugar de seleccionar una columna, se establece una propiedad.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_use_property_fields-1.png)
  
La propiedad puede constar de múltiples pasos separados por un punto; el sistema le ayudará a establecer el valor correcto de la propiedad. Si comete un error tipográfico, el sistema informará de un error.

Los campos de propiedad no son editables en la interfaz de usuario; sin embargo, se actualizan automáticamente al insertar o actualizar un registro en el sistema.

!!!note
      Los campos de propiedad están pensados para mostrar información derivada. No deben utilizarse para mostrar el contenido de una columna almacenada en la tabla asociada a la solapa donde se está definiendo el campo de propiedad.  

  
###  Uso en reglas de validación

Los campos de propiedad pueden utilizarse en Validaciones. En este caso, el código de validación que referencia el campo de propiedad debe tener este aspecto: `@_propertyField_ _fieldName_ _columnname_@`, donde `fieldname` es el nombre de la propiedad del campo (en minúsculas y eliminando espacios en blanco) y `columnname` es el nombre de la columna referenciada.

Como las propiedades de campo solo se calculan cuando el registro se guarda, pero no se vuelven a evaluar ante cambios de campo, en las validaciones solo deberían usarse en caso de que hagan referencia a una ruta que provenga de la cabecera del registro. Por ejemplo, en Línea de pedido podría usar cualquier campo de propiedad que tome los datos de su cabecera de pedido.

##  Uso en lógica de visualización

Puede establecer una lógica de visualización que haga referencia a un campo de propiedad. La forma de establecer la lógica de visualización que referencia un campo de propiedad es la siguiente: `@inp_propertyField_NameOfThePropertyField_ColumnName@`. Por ejemplo:

  * Imagine que tiene un campo de propiedad llamado Documento con nombre de columna **DocumentStatus**. 
  * Tiene otro campo *Campo A* que quiere mostrar solo cuando el campo de propiedad **Documento** tenga el estado **DR**. 
  * En la lógica de visualización del campo *Campo A*, debería escribir: `@inp_propertyField_Document_DocumentStatus@ = 'DR'`

##  Caso de uso: mostrar información relacionada

El primer uso de un campo de propiedad es mostrar información relacionada en la interfaz de usuario. El ejemplo de la sección anterior mostró cómo definir un nuevo campo de categoría de tercero en la ventana/solapa de cabecera de factura de venta. Esto se visualiza de la siguiente manera en la interfaz de usuario:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_use_property_fields-2.png)

Y puede ordenar y filtrar por el campo relacionado/derivado:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_use_property_fields-3.png)

Y también mostrarlo en el formulario:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_use_property_fields-4.png)

!!!note
      Tenga en cuenta que el enlace directo también funciona para campos derivados, por lo que en este ejemplo puede “saltar” directamente a la ventana de categoría de tercero para la categoría de tercero.

##  Caso de uso: mostrar tabla hija en la parte superior de la ventana

Un gran uso del concepto de campo de propiedad es mostrar registros hijos (por ejemplo: líneas de factura de venta) en la raíz de una ventana. Esto hace posible filtrar y ordenar los registros hijos a través de múltiples padres (por ejemplo: cabeceras de factura de venta).

La captura de pantalla siguiente muestra un ejemplo de una ventana de líneas de factura de venta que muestra todas las líneas de factura de venta a través de múltiples cabeceras de factura de venta. Esto facilita mucho filtrar y ordenar a través de todas las líneas de factura de venta del sistema.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_use_property_fields-5.png)
  
Algunas cosas a tener en cuenta al crear este tipo de ventanas:

  * La principal restricción para este tipo de cuadrículas es que no es posible insertar registros; sin embargo, la edición y la eliminación no suponen ningún problema. Por tanto, para este tipo de ventanas/solapas establezca el patrón de UI en **Solo edición**. 
  * Para editar, es posible que ciertos campos necesiten información de contexto del padre u otra información de contexto. Esta información de contexto debe añadirse como campos a la solapa. Si no quiere que estos campos de información de contexto se muestren en la cuadrícula o el formulario, establezca las siguientes propiedades en no (desmarcadas): mostrado y mostrar en vista de cuadrícula. 
  Vea la captura de pantalla siguiente, que muestra cómo se añade la organización a la solapa como un campo, para que los combos muestren la información correcta al editar las líneas de factura de venta:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_use_property_fields-6.png)

---

Este trabajo es una obra derivada de [Cómo añadir un campo canvas a un formulario o cuadrícula](http://wiki.openbravo.com/wiki/How_to_use_property_fields){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.