---
title: Tabla
tags:
  - Conceptos
  - Tabla
  - Base de datos
  - Columnas comunes
  - Clave primaria
  - Convenciones de nomenclatura
---
# Tabla

## Visión general

Las tablas físicas de la base de datos son la base sobre la que se construye el Modelo de Datos del Diccionario de Aplicación. Este documento analiza las particularidades que deben tener todas las tablas en Etendo ERP.

## Columnas comunes

Todas las tablas en Etendo deben tener algunas columnas comunes. Todas estas columnas deben definirse como no nulas.

### Clave primaria

Todas las tablas en Etendo tienen una clave primaria de una sola columna. Esta columna se rellenará automáticamente con un UUID generado, por lo tanto el tipo para esta columna debe ser _VARCHAR2(32)_.

La columna de clave primaria debe nombrarse como su tabla con un sufijo ID. Por lo tanto, la columna de clave primaria para la tabla *HT Salary* sería *HT Salary ID*.

Esta columna también debe establecerse como clave primaria en la base de datos; no es suficiente con definirla como ID en el Diccionario de Aplicación.

### Cliente/Organización

Como Etendo ERP es una aplicación [multi cliente y multi organización](multi-client-and-multi-org.md), todos los datos pertenecen a un cliente y a una organización, por lo que todas las tablas deben tener estas dos columnas:  

  * _AD_Client_ID_
  * _AD_Org_ID_

Estas columnas son una clave externa a las tablas *AD Client* y *AD Org*. Por lo tanto, sus tipos también deben ser *VARCHAR2(32)*, y debe existir una clave externa a estas tablas.

### Información de auditoría

Por último, hay algunas columnas que almacenan información sobre si un registro está activo y cuándo y quién lo creó y lo modificó por última vez. Esta información se mantiene en las siguientes columnas:

  * _IsActive_: Es un valor booleano (Y/N) que indica si el registro está activo o no. Su tipo debe ser _CHAR(1)_ y, por lo general, su valor por defecto es 'Y'. También es una buena práctica crear una restricción de comprobación que fuerce su valor a ser 'Y' o 'N'.
  * _Created_: Contiene la fecha y hora en la que se creó el registro. Su tipo es _DATE_.
  * _CreatedBy_: Indica el usuario que creó el registro. Es una clave externa a *AD User*, por lo que su tipo es _VARCHAR2(32)_.
  * _Upated_: Contiene la última fecha y hora en la que se modificó el registro (o se creó si no se realizó ninguna modificación posteriormente). Su tipo es _DATE_.
  * _UpdatedBy_: Indica el último usuario que actualizó el registro. Es una clave externa a *AD User*, por lo que su tipo es _VARCHAR2(32)_.

## Convenciones de nomenclatura

Al crear nuevas tablas es necesario prestar especial atención a los nombres asignados a tablas y columnas, particularmente en lo relativo a la modularidad.

### Tabla

El único elemento a tener en cuenta es el DB Prefix del módulo. El nombre de la tabla debe comenzar con este DB Prefix seguido del carácter de subrayado (_).

Los siguientes prefijos de tabla son utilizados por Etendo y no está permitido que sean usados por ningún módulo:

Table prefix  |  Descripción  
---|---  
A  |  gestión de activos  
AD  |  diccionario de aplicación  
C  |  funcionalidad núcleo  
I  |  tablas y procesos temporales de importación  
M  |  gestión de materiales  
FACT  |  contabilidad  
GL  |  libro mayor  
MA  |  fabricación  
MRP  |  recursos de materiales  
S  |  gestión de servicios  
AT,AU,EM,FIN,I,MA,R,RV,T  |  otros prefijos del núcleo  
CUS, PD, US, ZZ  |  desarrollos personales  
APRM  |  gestión avanzada de pagos y cobros  
OBUIAPP, NAVBA  |  aplicación de interfaz de usuario  
OBCHW  |  widget HTML  
OBCLFRE, OBCLKER  |  kernel de cliente de interfaz de usuario  
OBKMO  |  espacio de trabajo y widgets  
OBCQL  |  widget de consulta/lista  
OBSERDS  |  fuente de datos JSON  
OBJSON  |  servicio web REST JSON  
OBUISEL  |  selector de interfaz de usuario  
OBUISC  |  Smartclient  
FINPR  |  pedidos pendientes de entrega  

### Columna

#### Modularidad

En caso de que la columna pertenezca al mismo módulo que su tabla, no debe seguirse ninguna regla especial para su nombre. Pero si la columna se va a añadir a una tabla que pertenece a un módulo diferente, el nombre de la columna debe comenzar con *EM más* el *DB Prefix* del módulo al que pertenece la columna. Por ejemplo, `EM_MYMODULEDBPREFIX_COLUMNNAME`.

!!!note
    El nombre de la columna no debe superar los 30 caracteres, lo que incluye el EM más el DB Prefix del módulo.

!!!info
    En PostgreSQL, todos los nombres de columna deben definirse en minúsculas.  

Esta restricción también se aplica a la nomenclatura de restricciones, triggers y funciones.

#### Columna de clave primaria

!!!info
    La nomenclatura de la columna de clave primaria se explica en la sección [Clave primaria](#clave-primaria) de este documento.

#### Columnas de clave externa

Es una buena práctica nombrar, si es posible, las columnas de clave externa de la misma manera que la columna de clave primaria de la tabla a la que enlazan. La razón de esto es que, en Oracle, los nombres de las claves externas (y del resto de las restricciones de base de datos) deben ser únicos a nivel de base de datos. Así, por ejemplo, si tenemos en nuestra tabla una columna que contiene un tercero, debería llamarse *C_BPartner_ID* porque es una clave externa a la columna *C_BPartner*.*C_BPartner_ID*. Esto no es posible cuando hay en la misma tabla más de una columna que enlaza a la misma tabla o cuando se añaden columnas en un módulo diferente al de la tabla.

Seguir esta regla de nomenclatura permite definir referencias estándar como *TableDir* cuando la columna se define en el Diccionario de Aplicación.

#### Nomenclatura de columnas y la Capa de Acceso a Datos

En Etendo, se generan clases Java a partir de la definición de las tablas. Se genera una entidad DAL a partir de cada tabla definida en el Diccionario de Aplicación.

!!!info
    Para más información, visite [Data Access Layer](../concepts/Data_Access_Layer.md).

Es importante que tenga esto en cuenta al pensar en los nombres de sus columnas. Las columnas que defina en una tabla se corresponderán con propiedades Java en una clase Java generada. Por lo tanto, *no debe elegir nombres que colisionen con palabras clave de Java*, como *class*, *if*, *int*, ...

!!!info
    Aquí puede encontrar una lista de las [palabras clave de Java](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html){target="\_blank"}.

## Tipos de datos de columna soportados

`DBSourceManager`, la utilidad que Etendo utiliza para gestionar operaciones relacionadas con la base de datos, soporta un subconjunto de los tipos de datos que soportan las bases de datos Oracle y PostgreSQL. A continuación incluimos los tipos de datos soportados actualmente:

Oracle  |  PostgreSQL  
---|---  
(n)char  |  char  
(n)varchar(2)  |  varchar  
blob  |  bytea  
date  |  timestamp  
number  |  numeric  
clob  |  text  

---

Este trabajo es una obra derivada de [Tabla](http://wiki.openbravo.com/wiki/Tables){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.