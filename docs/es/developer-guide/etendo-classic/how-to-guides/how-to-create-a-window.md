---
title: Cómo crear una Ventana
tags:
  - Cómo hacer
  - Creación de Ventana
  - Desarrollo
  - Creación de tabla de base de datos
---

# Cómo crear una Ventana

## Visión general

El objetivo de esta sección es mostrar cómo puede crear una nueva ventana desde cero. 

!!!info
    Esta sección se basa en dos secciones anteriores que explican
    [Cómo crear un Módulo](../how-to-guides/How_To_Create_a_Module.md) y [Cómo crear una Tabla](../how-to-guides/How_to_create_a_Table.md).

## Módulo y tabla

Como se mencionó anteriormente, este tutorial se basa en dos tutoriales previos y asume que los siguientes objetivos ya se han completado:

  * Creación de un nuevo módulo
  * Creación + registro en el AD de una nueva tabla

##  Creación de la nueva Ventana

Usando el rol *System Administrator* navegue a `Application Dictionary` > `Windows, Tabs and Fields`. 
Cree un nuevo registro tal y como se indica en la captura de pantalla siguiente:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_0.png) 


Los campos principales de esta ventana son:


  - *Módulo*: define el módulo al que pertenecerá este elemento.
  - *Nombre*: define el nombre que Etendo utiliza para reconocer esta ventana. 
  - *Descripción*: proporciona una breve descripción de la tabla. 
  - *Ayuda/Comentario*: define el texto que se muestra en la ventana de Ayuda. 
  - *Tipo de ventana*: define algunas particularidades de la interfaz de usuario para una ventana: 
    - _Mantener_ : se utiliza para ventanas con pocas entradas. 
    - _Transacción_ : para ventanas transaccionales. Es el tipo de ventana que se utiliza para mostrar la información de tablas con un gran volumen de datos. Por defecto, esta ventana filtra documentos antiguos (n días – configuración de la ventana `General Setup` > `Application` > `Session Preferences`) y documentos procesados. La tabla subyacente de la solapa de cabecera debe contener las columnas PROCESSED y UPDATED (para que funcionen los filtros de datos).
    - _Solo consulta_ : para ventanas de sólo lectura que únicamente permiten visualizar datos. 

  
Guarde este registro y vaya a la solapa *Solapa*. Cree un nuevo registro como se muestra
a continuación, creando la primera solapa:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_1.png)  


Los campos principales de esta ventana son:

  * *Módulo*: define el módulo al que pertenecerá este elemento.
  * *Nombre*: define el nombre que Etendo utiliza para reconocer esta solapa. 
  * *Descripción*: proporciona una breve descripción de la tabla. 
  * *Ayuda/Comentario*: define el texto que se muestra en la ventana de Ayuda. 
  * *Tabla*: especifica la tabla de la que la solapa mostrará los datos. 
  * *Nivel de tabla*: define la jerarquía de solapas, siendo _0_ el nivel más alto. 
  * *Patrón de UI* Este desplegable ofrece las siguientes opciones: 
    * _Estándar_ \- interfaz estándar donde se pueden añadir, ver y editar múltiples registros 
    * _Sólo lectura_ \- esta opción deshabilita cualquier capacidad de edición/creación para cualquier usuario dentro de esta solapa 
    * _Registro único_ \- esta opción fuerza una relación uno a uno entre una solapa padre y una solapa hija, permitiendo al usuario introducir como máximo un registro en la solapa 
  * *Cláusula Where HQL*: usando este filtro HQL, el usuario nunca podrá ver datos que no cumplan los criterios. Al referirse a propiedades de la entidad mostrada en la solapa, utilice el prefijo *e*. En nuestro caso, utilizamos este campo para mostrar únicamente terceros que sean nuestros empleados (usando la propiedad _employee_). 
  * *Cláusula Where SQL* Igual que la cláusula Where HQL pero usando sintaxis SQL y utilizada para filtrar en _ventanas clásicas_. 

El botón *Copiar campos de una solapa* puede utilizarse para copiar campos desde una solapa existente a la nueva.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_2.png) 

El botón *Crear campos* puede utilizarse para crear campos para la nueva solapa basándose en su tabla asociada.
  
Vaya a la solapa *Campo* para ver los campos creados.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_3.png)  
  
Si fuese necesario, se podrían realizar cambios en estos campos o añadir nuevos manualmente. 

!!!note
    Para las solapas que no son de cabecera, es muy importante no eliminar el campo
    que apunta al campo ID de su solapa padre, ya que haría imposible crear registros en esta solapa usando la vista de rejilla. 


Ahora, vuelva a la solapa *Solapa* y cree un nuevo registro que representará la
solapa hija de la solapa Operarios donde se gestionarán los salarios:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_4.png) 

Lo más importante es asegurarse de seleccionar:

  * *Tabla* = `HT_Salary`
  * *Nivel de tabla* = _1_


Al hacer clic y confirmar el diálogo *Crear campos*, la aplicación
insertará automáticamente las columnas de la tabla seleccionada en la solapa de campos de la solapa
*Salario*.

  
Para ordenar las columnas de acuerdo con el aspecto habitual de otras ventanas, ahora cambiamos las propiedades de algunos campos de vista, tal y como se puede ver en la siguiente captura de pantalla.

  * Ocultar el campo _c_bpartner_id_
  * Reordenar campos (usando la secuencia), para que _isactive_ quede después de todos los demás campos 
  * Marcar _amount_ e _isactive_ como *Iniciar en nueva línea*

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_5.png) 


  
Para que Etendo cree enlaces (etiquetas que aparecen en azul) a elementos de tabla, el sistema necesita saber qué ventana representa la tabla donde reside un determinado elemento.

Para indicarlo, vaya a la ventana `Application Dictionary` > `Tables and Columns`, busque la tabla correspondiente y establezca la *Ventana* como se indica a continuación:

  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_6.png)

##  Creación del elemento de menú

Se requiere un elemento de menú para que el usuario pueda abrir la nueva ventana. Usando el rol System Administrator navegue a `General Setup` > `Application` > `Menu` y cree un nuevo registro:

  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_7.png)
  
Los campos principales de esta ventana son:

  * *Módulo*: define el módulo al que pertenecerá este elemento.
  * *Nombre*: define el nombre que Etendo utiliza para reconocer este elemento de menú. 
  * *Descripción*: proporciona una breve descripción de la tabla. 
  * *Nivel resumen*: define una carpeta que contiene elementos de menú (ventanas, procesos, informes, etc.). 
  * *Acción*: define el tipo de elemento de menú. 
  * *URL* Si _Acción_ es _Enlace externo_ o _Enlace interno_, define la _URL_ a enlazar. 
  * *Formulario especial*: Si _Acción_ es _Formulario_, define el formulario a enlazar. 
  * *Proceso*: Si _Acción_ es _Proceso_, define el proceso a ejecutar. 
  * *Informe*: Si _Acción_ es _Informe_, define el informe a enlazar. 
  * *Ventana*: Si _Acción_ es _Ventana_, define la ventana a enlazar. 

Guarde este registro y luego haga clic en el icono _Árbol_ ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_8.png)


Aquí puede arrastrar y soltar el nuevo elemento de menú en cualquiera de los
otros grupos de menú.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_9.png)


##  Compilación de la aplicación con la nueva Ventana

Finalmente, la aplicación necesita recompilarse para generar el código de la nueva ventana y desplegarlo en Tomcat. 

```bash
./gradlew smartbuild
```

##  El resultado

Usando el rol *F&B International Group Admin*, seleccione el enlace a la nueva ventana desde el menú. 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Create_a_Window_10.png)
  
!!!success
    Ahora ha creado correctamente su propia ventana nueva y ha visto cómo cobra vida dentro de Etendo. 

---

Este trabajo es una obra derivada de [Cómo crear una ventana](http://wiki.openbravo.com/wiki/How_to_Create_a_Window){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.