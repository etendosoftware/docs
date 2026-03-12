---
title: Mensajes
tags:
    - Mensajes 
    - Tipos
    - Información
    - Éxito
    - Fallo
    - Advertencia

status: beta
---

#  Mensajes

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

##  Visión general

Los mensajes se utilizan para mostrar información al usuario; normalmente se muestran cuando se completa un proceso o cuando ocurre un evento (por ejemplo, un error).

##  Tipos de mensajes

Los diferentes tipos de mensajes que se pueden mostrar con Etendo son:

- Mensajes de éxito 
- Mensajes de fallo 
- Mensajes de advertencia 
- Mensajes de información 

###  Mensajes de éxito

Estos mensajes se mostrarán después de la ejecución de un proceso en caso de éxito.

![](../../../assets/developer-guide/etendo-classic/concepts/messages-0.png)

###  Mensajes de fallo

Estos mensajes se mostrarán después de la ejecución de un proceso en caso de error.

![](../../../assets/developer-guide/etendo-classic/concepts/messages-1.png)

###  Mensajes de advertencia

Estos mensajes se mostrarán cuando el usuario deba tener en cuenta determinadas condiciones, como por ejemplo un mensaje que indique que todavía hay algunas acciones pendientes de procesar, etc.

![](../../../assets/developer-guide/etendo-classic/concepts/messages-2.png)

###  Mensajes de información

Estos mensajes se mostrarán para comunicar cualquier información al usuario, como por ejemplo la funcionalidad de la ventana, etc.

![](../../../assets/developer-guide/etendo-classic/concepts/messages-3.png)

##  Definición en el Diccionario de la Aplicación
:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Mensaje`

Todos los mensajes se mantienen en la ventana `Diccionario de la Aplicación` > `Mensaje` (tabla `AD_Message`). Básicamente, un mensaje consta de una `Clave de búsqueda` o valor, un `Tipo de mensaje` que establece el tipo de mensaje (la apariencia del mensaje mostrado —tal y como se describe en la sección anterior— depende de ello) y un `Texto del mensaje` que contiene el texto que se mostrará dentro del cuadro. Adicionalmente, los mensajes se pueden traducir a diferentes idiomas. Para añadir traducciones a un mensaje, utilice la solapa `Traducción`.

El campo `Clave de búsqueda` es un identificador único para el mensaje; no se muestra al usuario, pero se utiliza internamente para identificar el mensaje. Así, por ejemplo, cuando una clase Java necesita mostrar un mensaje, se utiliza el valor de la clave de búsqueda para seleccionar el mensaje.

El campo Clave de búsqueda sigue las reglas de nomenclatura de modularidad. Por lo tanto, debe comenzar con el dbprefix del módulo, seguido de un "_". Por tanto, un valor correcto para un mensaje en el `módulo org.openbravo.client.application` sería `_OBUIAPP_MyMessage_`.

##  Uso de mensajes

Dependiendo del objeto que genere el mensaje, deben tenerse en cuenta algunas consideraciones diferentes.

###  Procesos de base de datos

Tal y como se explica en la sección de procesos PL/SQL de esta guía, el resultado final, así como el mensaje que se mostrará al usuario desde un proceso PL, se almacena en el `registro AD_PInstance` que se utilizó para invocarlo.

Este mensaje puede ser una cadena estática que se mostrará tal cual en la UI:
 
```
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', 1, 'Show this static text');
```

Este tipo de mensaje no hace uso de los mensajes definidos en la ventana `Mensaje`. Para utilizarlos, es necesario establecer el identificador del mensaje (`Valor de clave de búsqueda`) rodeado por símbolos de arroba (@):
    
```
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', 1, '@HR_MyMessage1@');
```
  
En la línea anterior, cuando el proceso finalice, la aplicación intentará encontrar un mensaje cuyo valor sea `HR_Message1` y mostrará el texto que contiene.

!!!Note
    Como los mensajes son traducibles, si el usuario ha iniciado sesión en la aplicación con uno de los idiomas a los que se ha traducido el mensaje, verá el texto en ese idioma.

Además, es posible combinar más de un mensaje y texto estático. Por ejemplo:
 
```
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', 1, '@Success@, 5 @LinesCreated@');
```

Este mensaje concatenará el texto del mensaje con identificador `Success` con el texto estático ', 5 ' y con el texto del mensaje `LinesCreated`.

Todas las excepciones generadas por los procesos deben capturarse para gestionarlas e insertar un mensaje adecuado en `PInstance`.

####  Excepciones de base de datos

Las excepciones son especialmente útiles para los triggers. Cuando se lanza una excepción dentro de un trigger, la transacción actual se revierte. Esto permite realizar algunas comprobaciones antes de actualizar o insertar una fila en una tabla y, en caso de que algunas verificaciones no se satisfagan, se puede lanzar una excepción provocando que la fila no se inserte/actualice.

**Oracle**

Oracle identifica cada error mediante un código numérico; el rango entre -20000 y -20999 pertenece a errores personalizados y, utilizando el procedimiento RAISE_APPLICATION_ERROR, se pueden asociar a un mensaje.

Cuando Etendo captura uno de estos errores, intenta encontrar un mensaje con la misma `Clave de búsqueda` que el número de código; si existe, mostrará el texto del mismo modo que se explicó en la versión anterior para reemplazar el mensaje entre símbolos de arroba (@) por el mensaje correspondiente.

No está permitido utilizar estos números de código para gestionar mensajes porque:

- No pueden definirse dentro de módulos. Como el único identificador que tienen es un valor numérico, no hay forma de incluirlos en módulos sin el riesgo de que dos módulos diferentes utilicen el mismo número para fines distintos. 
- Esto es específico de Oracle y no puede utilizarse en PostgreSQL; por lo tanto, no funcionarán del mismo modo en PostgreSQL. 

Por tanto, la forma correcta de hacerlo es utilizar un número que no tenga un mensaje asociado e insertar dentro del texto el identificador del mensaje que se va a utilizar. Con esta intención, no existe ningún mensaje para el valor `20000`, por lo que cuando se utilice, el mensaje se tomará del segundo parámetro:

```
RAISE_APPLICATION_ERROR(-20000, '@HR_MyErrorMessage@');
```

**PostgreSQL**

La única forma de identificar un mensaje que se mostrará al trabajar con Etendo en PostgreSQL es identificarlo por su `Clave de búsqueda`.
 
```
RAISE EXCEPTION '%', '@HR_MyErrorMessage@';
```

####  Comprobaciones de base de datos y claves foráneas

Las restricciones de comprobación se definen en la base de datos para garantizar la integridad de los datos; definen alguna restricción que los datos deben cumplir. En caso de que, al insertar o actualizar datos en la base de datos, no se satisfaga una restricción, se genera un error.

Cuando se intenta insertar un dato en una tabla con una restricción de comprobación y ese dato no sigue las reglas definidas por dicha restricción, se genera un error de base de datos. De forma predeterminada, si no hay un Mensaje del Diccionario de la Aplicación asociado a esa restricción, se mostrará un mensaje de error genérico en la UI.

Es posible refinar ese error añadiendo un nuevo mensaje con la misma `Clave de búsqueda` que el nombre de la restricción. En este caso, en lugar de mostrar ese mensaje genérico, se mostrará el nuevo.

Lo mismo se aplica a las claves foráneas. Cuando se insertan, modifican o eliminan datos, una clave foránea podría incumplirse. En ese caso, si existe un mensaje específico para ello en el Diccionario de la Aplicación, se mostrará. De lo contrario, se mostrará un error genérico.


---

Este trabajo es una obra derivada de [Mensajes](http://wiki.openbravo.com/wiki/Messages){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.