---
title: Cómo añadir un campo de texto enmascarado
tags: 
    - Campo de texto enmascarado
    - Referencia enmascarada
    - Crear campo
    - Añadir columna
---

# Cómo añadir un campo de texto enmascarado

## Visión general

Esta sección explica cómo añadir un **campo y columna de texto enmascarado** al sistema Etendo. Un texto enmascarado puede utilizarse para obligar al usuario a introducir valores de texto/cadena en el formato correcto.

Los pasos para obtener un campo de texto enmascarado en la ventana constan de los siguientes pasos: 

1. crear una referencia definiendo la máscara.
2. añadir una columna a una tabla usando la referencia.
3. añadir un campo a una solapa.    

Los 2 últimos pasos se definen en detalle en las siguientes secciones:

- [Cómo añadir una nueva columna a una tabla en el sistema](./how-to-add-columns-to-a-table.md).
- [Definir y cómo añadir un nuevo campo a una solapa](./how-to-add-a-field-to-a-window-tab.md).

Esta sección se centrará únicamente en las partes específicas de un **campo de texto enmascarado**.
 
  
## Módulo de ejemplo

Esta sección se apoya en un módulo de ejemplo que muestra un ejemplo del código mostrado y comentado en esta sección.

El módulo de ejemplo añade un campo de texto enmascarado a la ventana de cabecera del pedido de venta.


El código del módulo de ejemplo puede descargarse desde este repositorio
Mercurial:
[https://github.com/etendosoftware/com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="\_blank"}

  
## Definición de la referencia de máscara

El primer paso es crear una referencia específica para la máscara y, a continuación, establecer la máscara en la solapa **hija de referencia de máscara**.

La referencia de máscara debe tener `Masked String` como referencia padre y no puede ser una referencia base. A continuación, cree un registro en la solapa hija **Referencia de máscara** definiendo la máscara.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-masked-test-field/how-to-add-masked-text-field-1.png)

  
!!! info 
    Para obtener información sobre cómo definir una máscara, consulte la descripción en la referencia padre `Masked String`.
    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-masked-test-field/how-to-add-masked-text-field-2.png)

## Añadir una columna

Para obtener un campo de texto enmascarado, lo primero que debe hacer es seleccionar la **referencia correcta y la clave de búsqueda de la referencia** al añadir una columna:


![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-masked-test-field/how-to-add-masked-text-field-3.png)

  
## Crear un campo

A continuación, cree un campo dentro de la solapa/ventana:

![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-masked-test-field/how-to-add-masked-text-field-4.png)

  
## El resultado

El resultado se visualiza como un editor de texto enmascarado en la vista de formulario:
  
![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-masked-test-field/how-to-add-masked-text-field-5.png)


Este trabajo es una obra derivada de [Cómo añadir un campo de texto enmascarado](http://wiki.openbravo.com/wiki/How_to_add_a_masked_text_field){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.