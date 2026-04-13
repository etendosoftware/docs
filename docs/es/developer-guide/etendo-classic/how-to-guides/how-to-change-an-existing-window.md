---
title: Cómo cambiar una ventana existente
tags: 
    - Cómo hacer
    - Diccionario de aplicación
    - Personalización de la UI
    - Inventario físico
    - Desarrollo de módulos
---

#  Cómo cambiar una ventana existente

##  Visión general

Los elementos de la aplicación ([ventanas, solapas y campos](../../../developer-guide/etendo-classic/concepts/modularity-concepts.md#windows-tabs-and-fields.md)) son susceptibles de cambiar repetidamente durante las fases de desarrollo o mantenimiento de un proyecto.
Etendo es capaz de gestionar estos cambios porque su arquitectura está adaptada al desarrollo iterativo. Las definiciones de todas las ventanas, solapas y campos generados se almacenan como metadatos en el Diccionario de aplicación (AD).

Cambiar la ventana de una aplicación existente es un proceso sencillo de modificar la definición del AD.

Al utilizar la UI de Etendo, los cambios se pueden ver inmediatamente al cambiar de rol y, a continuación, al volver a abrir la ventana modificada.

Al utilizar la ventana clásica, es necesario un paso de compilación.  

Este procedimiento explica cómo modificar elementos existentes de una ventana. Si solo se deben añadir nuevos elementos (como nuevos campos) a una ventana, no es necesario utilizar una Plantilla. En su lugar, esos nuevos elementos pueden añadirse usando un módulo normal, tal y como se explica en el otro procedimiento sobre [Cómo añadir un campo a una solapa de una ventana](../../../developer-guide/etendo-classic/how-to-guides/how-to-add-a-field-to-a-window-tab.md). 
 


##  Objetivo

El objetivo de este procedimiento es ilustrar cómo realizar cambios en ventanas generadas existentes en términos de apariencia y comportamiento. La ventana utilizada en el ejemplo es la ventana de Inventario físico y los cambios que se muestran serán:

  * Ocultar un campo 
  * Reordenar la secuencia del diseño 

[Inventario físico](../../../user-guide/etendo-classic/basic-features/warehouse-management/transactions.md#physical-inventory) es una ventana que pertenece a Etendo Classic.
Consta de:

  * 1 ventana: Inventario físico. 
  * 2 solapas: Cabecera y Líneas. 
  * Una solapa Cabecera tiene 19 campos, 10 de los cuales se muestran (algunos se muestran de forma condicional).

Antes de realizar cualquier cambio, la solapa de cabecera tiene el siguiente aspecto:


![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_change_an_existing_Window-1.png)


!!!info
    Para personalizar estas ventanas en un contexto de modularidad, se necesita un nuevo módulo de tipo
    *Plantilla*.



##  Cambiar la ventana

Vaya a la ventana `Diccionario de aplicación` > `Ventanas, solapas y campos` y seleccione el registro de _Inventario físico_.

En la solapa _Campo_ ahora podemos realizar los cambios necesarios para adaptar el diseño según se desee:

  * Campo _Descripción_: desmarque la casilla _Mostrar_ para ocultar el campo en la solapa. 
  * Campo _Organización_: cambie el número de secuencia a _200_ y marque la casilla _Empezar en nueva línea_. Esto mueve el campo por debajo de todos los demás que se muestran normalmente. 

  
Para probar el diseño modificado, cambie desde el rol *Administrador del sistema* a, por ejemplo, el rol *Administrador de F &B International Group* y vuelva a abrir la ventana *Inventario físico*. Como la instancia contiene nuestro módulo marcado como *En desarrollo*, el diseño de la ventana se recarga cada vez que se abre la ventana, por lo que
podemos ver el diseño modificado de forma inmediata, tal y como se muestra a continuación:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_change_an_existing_Window-2.png)


  
Para aplicar los mismos cambios de diseño a la ventana en *modo UI clásico*, es necesario recompilar las ventanas, desplegar los cambios en Tomcat y reiniciar Tomcat. El paso de compilación y despliegue puede realizarse usando `./gradlew smartbuild`, que recompilará todas las ventanas modificadas y desplegará los cambios.

  

##  Exportar los cambios

El paso final es exportar los cambios al módulo para que queden persistidos.

!!!note
    Al exportar cambios a una plantilla, es importante que solo la *plantilla esté en desarrollo* y que el módulo que contiene el objeto modificado (es decir, la ventana) no lo esté.

Tras asegurarse de ello, la exportación de los cambios consta de los dos pasos siguientes:

``` bash title="Terminal"
  1. _./gradlew export.database_ , same steps as for any other module 
```

``` bash title="Terminal"
  2. _./gradlew export.config.script_ , analyses the changes done and creates a special file _configScript.xml_ in the module to contain them. 
```

---

Este trabajo es una obra derivada de [Cómo cambiar una ventana existente](http://wiki.openbravo.com/wiki/How_to_change_an_existing_Window){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.