---
title: Cómo crear una alerta
tags: 
  - Cómo hacer
  - Creación de alertas
  - Receptor de Alerta
  - Notificación del sistema
---

#  Cómo crear una alerta

##  Visión general

El objetivo de este procedimiento es ilustrar cómo puede añadir nuevas alertas a
Etendo. Las alertas son mensajes informativos no intrusivos para usuarios
individuales o grupos (roles) sobre cualquier aspecto dentro del sistema. Se
puede definir un número ilimitado de alertas para distintos estados, errores,
fines informativos, recordatorios, etc.

Algunos ejemplos son:

  * Errores en el diccionario de aplicación sobre los que debe alertarse al *Administrador del sistema* (p. ej., una tabla sin un identificador)‏
  * Errores en los datos maestros (p. ej., un tercero sin una dirección)‏
  * Notificaciones sobre situaciones críticas (p. ej., pagos vencidos)‏

y muchos más.

##  Definición de la alerta

En primer lugar, es necesario definir la condición bajo la cual aparece la
alerta. Esto se realiza mediante una sentencia SQL que debe seguir ciertas
convenciones.

Para crear una nueva regla de alerta, use el rol _*Administrador del sistema*_
para navegar a la ventana `Configuración general` > `Aplicación` > `Alerta`.
Dependiendo de cómo haya instalado Etendo, es posible que ya tenga algunas
alertas aquí. Si es así, intente encontrar la de _Clientes con crédito excedido_
y haga doble clic sobre ella. Si no, cree un nuevo registro como se indica a
continuación:

  
![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how_to_create_an_alert-0.png)


donde este es el código exacto para el campo *SQL*:

    
    
     
     SELECT c_bpartner_id AS referencekey_id,
         ad_column_identifier('C_BPartner', c_bpartner_id, 'en_US') AS record_id,
         0 AS ad_role_id,
         NULL AS ad_user_id,
         ad_column_identifier('C_BPartner', c_bpartner_id, 'en_US') ||' has '||SO_CreditLimit||' as limit and has reached '||SO_CreditUsed AS description,
         'Y' AS isActive,
          ad_org_id, 
          ad_client_id, 
          now() AS created,  
          0 AS createdBy,  
          now() AS updated,
          0 AS updatedBy
     FROM c_bpartner 
     WHERE SO_CreditLimit < SO_CreditUsed
     AND iscustomer='Y'
     AND SO_CreditLimit!=0

Los campos en cuestión aquí son:

  * *Nombre* es un nombre descriptivo para una alerta
  * *SQL* son las sentencias SQL reales cuyos resultados (registros individuales) serán los elementos sobre los que se alertará
  * *Pestaña* es una pestaña de una ventana específica a la que se debe llevar al usuario para mostrarle el elemento en cuestión generado por la sentencia SQL

##  Definición de receptores

Cambie al rol _*Administrador del sistema*_ (o su rol de "administrador"
definido), navegue a _`Configuración general` > `Aplicación` > `Alerta`_,
seleccione la alerta _Clientes con crédito excedido_ y cambie a la pestaña
*Receptor de Alerta*. Añada un nuevo registro como se indica a continuación:

  
![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how_to_create_an_alert-1.png)

  
!!!note
    Tenga en cuenta que se puede añadir un rol (que incluye a varios usuarios) o
    un usuario específico.

##  Programación del proceso en segundo plano de alertas

Para que las alertas se evalúen y se disparen, es necesario programar el
proceso en segundo plano. Usando el rol _*Administrador del sistema*_ (o su rol
de "administrador" definido) navegue a _`Configuración general` > `Programación de procesos` > `Solicitud de proceso`_ e introduzca un nuevo registro:

![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how_to_create_an_alert-2.png)

##  El resultado

Por último, cierre sesión y vuelva a iniciarla y seleccione el rol
_*Administrador del sistema*_ (o su rol de administrador definido). Debería
poder ver una alerta en la barra de navegación. Al hacer clic sobre ella, se le
llevará automáticamente a la ventana _*Gestión de Alertas*_ que debería verse
más o menos así:

  

![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how_to_create_an_alert-3.png)

  

##  Explicación del código SQL

Para escribir cualquier tipo de alerta, el enfoque es muy similar. Volvamos a
ver el código SQL que describe la condición:

    
    
     
     SELECT c_bpartner_id AS referencekey_id,
         ad_column_identifier('C_BPartner', c_bpartner_id, 'en_US') AS record_id,
         '0' AS ad_role_id,
         NULL AS ad_user_id,
         ad_column_identifier('C_BPartner', c_bpartner_id, 'en_US') ||' has '||SO_CreditLimit||' as limit and has reached '||SO_CreditUsed AS description,
         'Y' AS isActive,
          ad_org_id, 
          ad_client_id, 
          now() AS created,  
          '0' AS createdBy,  
          now() AS updated,
          '0' AS updatedBy
     FROM c_bpartner 
     WHERE SO_CreditLimit < SO_CreditUsed
     AND iscustomer='Y'
     AND SO_CreditLimit!=0

Cada sentencia SQL básicamente simula una tabla de Etendo, por lo que necesita
tener definidas todas las columnas anteriores:

  * *referencekey_id* \- este es el ID (clave primaria) del registro que requiere atención y es la causa de la alerta. En nuestro caso, sería el C_BPartner_ID de Neil Reiley.
  * *record_id* \- esta es una etiqueta descriptiva para el elemento que está en cuestión con el referencekey_id. Use la función _ad_column_identifier_ como se muestra para recuperar todos los valores de columna necesarios para identificar de forma única el registro problemático dentro de la tabla específica.
  * ad_role_id - siempre debe establecerse en 0
  * ad_user_id - siempre debe establecerse en null
  * *description* \- este es el mensaje que se muestra al usuario describiendo cuál es el problema. Debe construir este mensaje de acuerdo con el objetivo de la alerta, indicando al usuario qué causó la alerta y cuál es el problema. De nuevo, use la función _ad_column_identifier_ como se muestra para recuperar todos los valores de columna necesarios para identificar de forma única el registro problemático dentro de la tabla específica.
  * isActive - siempre debe establecerse en 'Y'
  * ad_org_id - debe heredarse del registro real que dispara la alerta, en este caso, el registro de la tabla C_BPartner
  * ad_client_id - debe heredarse del registro real que dispara la alerta, en este caso, el registro de la tabla C_BPartner
  * created - siempre debe establecerse en now()
  * createdBy - siempre debe establecerse en 0
  * updated - siempre debe establecerse en now()
  * updatedBy - siempre debe establecerse en 0

Por último, la cláusula WHERE describe la condición que dispara la alerta. En
nuestro caso, la sentencia SELECT devolverá todos los terceros (FROM
c_bpartner) que son clientes (iscustomer='Y') y han excedido su límite de crédito
(`SO_CreditLimit < SO_CreditUsed`), el cual debe ser distinto de cero
(`SO_CreditLimit!=0`).

En otras palabras, cualquier cosa que pueda describir en una sentencia SQL puede
definirse como una alerta.

Este trabajo es una obra derivada de [Cómo crear una alerta](http://wiki.openbravo.com/wiki/How_to_create_an_Alert){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.