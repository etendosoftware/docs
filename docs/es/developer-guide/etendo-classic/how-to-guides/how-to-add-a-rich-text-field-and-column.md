---
title: Cómo añadir un campo y una columna de texto enriquecido
tags:
  - Cómo hacer
  - Campo de texto enriquecido
  - Columna
  - Base de datos
  - Referencia
---

# Cómo añadir un campo y una columna de texto enriquecido
  
## Visión general

Esta sección de procedimientos explica cómo añadir un campo y una columna de texto enriquecido a Etendo Classic.

Los pasos para obtener un campo de texto enriquecido en su ventana constan de dos pasos: 

- [Añadir una columna a una tabla](../../../developer-guide/etendo-classic/how-to-guides/how-to-add-columns-to-a-table.md)
- [Añadir un campo a una solapa](../../../developer-guide/etendo-classic/how-to-guides/how-to-add-a-field-to-a-window-tab.md)

También puede crear una nueva tabla y una nueva ventana/solapa, por supuesto.
Este procedimiento solo se centrará en la parte específica de un campo de texto enriquecido.

  
##  Ejemplo 

Para este procedimiento, utilizaremos la redefinición del campo de descripción en la ventana de pedido de venta. Por lo tanto, puede que necesite hacer un *smartbuild* después de los cambios para ver el resultado.


  
###  Añadir una columna

Primero, tiene que [añadir una columna a la tabla existente](../../../developer-guide/etendo-classic/how-to-guides/how-to-add-columns-to-a-table.md).


!!!note
    Como el texto enriquecido se almacena como HTML dentro de la base de datos, se debe utilizar el tipo de columna varchar. Además, el desarrollador debe tener en cuenta que 100 caracteres de texto enriquecido requieren más de 100 caracteres de almacenamiento dentro de la base de datos debido al marcado HTML. Normalmente, un factor de 2 será suficiente; por ejemplo, si se quiere permitir que el usuario introduzca 1000 caracteres de texto con formato enriquecido, la columna de la base de datos debería tener un tipo varchar(2000).  

  
Al introducir la nueva columna en el diccionario de aplicación, se debe seleccionar la referencia correcta, es decir, la nueva referencia de _Texto enriquecido_:


![](../../../assets/developer-guide/etendo-classic/how-to-guides/how_to_add_a_rich_text_field_and_column-1.png)

###  Crear un campo: configurar col y rowspan

A continuación, [cree un campo](../../../developer-guide/etendo-classic/how-to-guides/how-to-add-a-field-to-a-window-tab.md) dentro de la solapa/ventana. Para un campo de texto enriquecido también puede configurar col y rowspan (solo se muestran cuando la columna correspondiente está definida como texto enriquecido):

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_rich_text_field_and_column-2.png) 


###  El resultado

El resultado se visualiza como un editor de texto enriquecido en la vista de formulario:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_rich_text_field_and_column-3.png) 

  

!!!info
    Los campos de texto enriquecido no se pueden editar en modo rejilla (al pasar el cursor se muestra el contenido). Siempre se muestran como campos de solo lectura.  

  
---

Este trabajo es una obra derivada de [Cómo añadir un campo y una columna de texto enriquecido](http://wiki.openbravo.com/wiki/How_to_add_a_rich_text_field_and_column){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.