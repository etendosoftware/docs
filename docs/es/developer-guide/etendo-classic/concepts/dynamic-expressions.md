---
title: Expresiones dinámicas
tags:
    - Dinámicas
    - Expresiones
    - Variables
    - Accesibilidad

status: beta
---

#  Expresiones dinámicas

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

##  Visión general

Las **Expresiones dinámicas** se utilizan para obtener valores que pueden depender de valores de sesión. Por ejemplo, pueden utilizarse para filtrar los registros que aparecen en una solapa por aquellos que fueron creados por el usuario que ha iniciado sesión en la aplicación.

##  Valores de sesión (Variables Sesión)
:material-menu:  `Configuración General` > `Aplicación` > `Variables Sesión`

Dependiendo de cómo se definan, existen diferentes tipos de valores de sesión. Es posible comprobar (como **Administrador del sistema**) todos los valores actuales cargados en sesión en la ventana `Configuración General` > `Aplicación` > `Variables Sesión`.

###  Variables globales de sesión

Estos valores son generados por clases `Java` y son accesibles desde cualquier parte de la aplicación.

###  Columna

Los valores de todas las columnas utilizadas en una solapa son accesibles como variables de sesión dentro de esa solapa. Adicionalmente, también es posible establecer explícitamente una columna como valor de sesión configurando su atributo `Stored in Session`. Esto hará que este valor sea accesible no solo para su solapa, sino también para todas las solapas de esa ventana.

###  Preferencias
:material-menu: `Configuración General` > `Aplicación` > `Preferencias`

Las **Preferencias** permiten definir valores de sesión. Es posible definir preferencias para una única ventana o para todas (dejando en blanco el campo ventana) y para un usuario o para todos. Las preferencias se definen en la ventana `Configuración General` > `Aplicación` > `Preferencias`.

Cuando el valor del atributo coincide con un nombre de columna, se utilizará como valor por defecto para esa columna, sobrescribiendo el valor por defecto estándar de dicha columna.

Las preferencias pueden definirse para una ventana y un usuario. Si no se selecciona ninguna ventana, la preferencia se aplica globalmente a toda la aplicación; si se selecciona una, solo se aplicará en esa ventana. De forma similar, en caso de que el usuario esté en blanco, la preferencia se compartirá entre todos los usuarios; en caso contrario, la preferencia se aplicará únicamente al usuario seleccionado.

Para ver una lista de las preferencias actuales del sistema, visite la página [Preferencias](../../../user-guide/etendo-classic/basic-features/general-setup/application/preference.md).

**Definición**

Existen dos formas de definir una preferencia; se puede alternar usando el campo de comprobación **Lista de Propiedades**:

- **Propiedad**. (**Lista de Propiedades** marcada). La preferencia puede tomarse de una lista fija. Es una [lista valores](../concepts/data-model.md#list) llamada `Property Configuration`. Los módulos pueden añadir nuevos elementos a esta lista con el propósito de que otros módulos puedan establecer valores para ellos. 
- **Atributo**. (**Lista de Propiedades** desmarcada). La preferencia se define mediante el campo `Atributo`, que es un cuadro de entrada de texto libre. 

**Visibilidad**

La visibilidad de una preferencia define en qué casos se utilizará la preferencia. Puede definirse en diferentes niveles. Todos ellos pueden configurarse o dejarse en blanco; en caso de que un nivel de visibilidad esté vacío, no se aplica, por lo que es visible desde cualquier valor de ese nivel; por ejemplo, si el parámetro de usuario está vacío, cualquier usuario podrá ver esa preferencia. En caso de que la misma preferencia tenga valores en diferentes niveles, se utilizará el más específico. Los niveles son los siguientes:

- **Entidad**. Define la entidad; si está vacío o es **Sistema**, la preferencia será visible desde cualquier entidad. 
- **Organización**. Define la visibilidad desde la organización con la que se ha iniciado sesión. 
    !!!Note
        La organización no es la organización del documento, sino la utilizada durante el inicio de sesión. Por tanto, si un rol tiene acceso a las organizaciones A y B, ambas organizaciones tienen un valor para la misma preferencia y el usuario inicia sesión en la aplicación con ese rol y la organización A, se utilizará el valor definido para esa organización, incluso al crear un documento (por ejemplo, una factura) en la organización B. Si está vacío o es * será visible desde todas las organizaciones. La visibilidad para organizaciones se calcula teniendo en cuenta el árbol de organizaciones; es decir, si el árbol de organizaciones tiene A con una organización hija A1, las preferencias definidas para A serán visibles desde A y A1 en caso de que A1 no tenga un valor para ellas. 
- **Usuario** y **Rol**. El usuario/rol que podrá utilizar la preferencia. 
- **Ventana**. Desde qué ventana será visible la preferencia. 

**Obtener/establecer valores de Preferencias**

Al iniciar sesión en la aplicación o cambiar de rol, las preferencias visibles para ese usuario/rol/entidad/organización se almacenan en sesión; esos valores pueden obtenerse usando el método `org.openbravo.erpCommon.utility.Utility.getContext`.

Adicionalmente, es posible buscar el valor de una preferencia consultando la base de datos mediante el método
`org.openbravo.erpCommon.businessUtility.Preferences.getPreferenceValue`. Este método lanza una excepción en caso de que la propiedad no tenga un valor definido visible desde el nivel de visibilidad actual (pasado como parámetros); también lanza una excepción en caso de conflicto (más de un valor definido para la propiedad en el nivel de visibilidad actual).

Las preferencias pueden establecerse mediante programación a través del método `org.openbravo.erpCommon.businessUtility.Preferences.setPreferenceValue`.

**Conflictos**

Se produce un conflicto para una preferencia en caso de que la misma preferencia se defina con valores diferentes en el mismo nivel de visibilidad. Cuando esto sucede, uno de ellos se almacenará en sesión al iniciar sesión en la aplicación o al cambiar el rol.
Si se intenta obtener el valor de la preferencia usando el método `org.openbravo.erpCommon.businessUtility.Preferences.getPreferenceValue`, se lanzará una `PropertyConflictException`.

Los conflictos pueden resolverse manualmente por el usuario, marcando el campo `selected` de la preferencia. En este caso, el valor de la preferencia seleccionada prevalecerá sobre el resto.

**Modularidad**

Las preferencias pueden asignarse opcionalmente a un módulo. En este caso, se exportarán como parte del módulo. Esto tiene sentido en caso de que se quiera definir en un módulo una configuración general que se reutilizará.

###  Inputs auxiliares

:material-menu: `Diccionario de la Aplicación` > `Configuración` > `Inputs auxiliares`

Los **Inputs auxiliares** se utilizan para crear un valor de sesión para una solapa concreta. Este valor puede calcularse usando una Expresión dinámica y su propósito es utilizarlo en otras Expresiones dinámicas dentro de la solapa para la que se define.

Los Inputs auxiliares se definen en la solapa `Diccionario de la Aplicación` > `Configuración` > `Inputs auxiliares`.

###  Accesibilidad

Es posible que existan diferentes tipos de valores de sesión con el mismo nombre que sean accesibles en el mismo punto; en este caso (a menos que se especifique explícitamente tomar el valor en un valor global de sesión) el valor se tomará siguiendo el siguiente enfoque:

1. Intentar obtener una preferencia con el nombre especificado para la ventana actual. 
2. Si no se ha obtenido ningún valor, intentar obtener un valor asociado a la ventana actual. 
3. Si no se ha obtenido ningún valor, buscar un valor global de sesión. 

##  Sintaxis y tipos en Expresiones dinámicas

###  Uso de valores de sesión

En las Expresiones dinámicas, los valores de sesión se obtienen por su nombre rodeado por símbolos arroba (@). Así, para obtener el contenido de un valor de sesión llamado `myValue`, se haría escribiendo `@myValue@`. Hacerlo de esta manera seguiría la [accesibilidad](#accesibilidad) descrita anteriormente, pero es posible obtener explícitamente el valor global (si existe) sin tener en cuenta los otros; para ello, el valor tendría un símbolo almohadilla (#) como prefijo. En el ejemplo anterior sería `@#myValue@`.

###  Tipos de Expresiones dinámicas

Existen diferentes tipos de Expresión dinámica; cada tipo puede utilizarse dependiendo del objeto del Diccionario de la Aplicación en el que se defina. Una lista completa de todos los objetos y qué tipo de expresión puede usar se define en la siguiente sección.

Los tipos son:

###  Constante

Puede ser un valor constante o un valor almacenado en sesión; este tipo puede ser utilizado por todos los objetos. Para establecer este tipo, no se necesita prefijo.

Ejemplo:

```
@#AD_User_ID@
```
    

###  SQL

Algunos objetos aceptan expresiones SQL. Este tipo debe tener un prefijo `@SQL=` seguido de la cláusula SQL. También acepta valores de sesión.

Ejemplo:

```
@SQL=SELECT DOCSUBTYPESO 
        FROM C_DOCTYPE 
        WHERE C_DOCTYPE_ID = @C_DOCTYPETARGET_ID@
```

###  WhereClause

Es una cláusula where de SQL; en este caso no es necesario añadir el prefijo `@SQL=`.

###  Comprobación

Se utiliza para obtener un valor booleano. No tiene ningún prefijo. Su sintaxis es `Javascript` pero los comparadores son:

-  `=` en lugar de `==` 
- `!` en lugar de `!=` 
- `&` en lugar de `&&`
- `|` en lugar de `||` 

###  Expresiones dinámicas utilizadas en objetos del Diccionario de la Aplicación

AD Column  |  Tipo  
---|---  
`AD_AlertRule.FilterClause`  |  WhereClause  
`AD_AuxiliarInput.Code`  |  SQL  
`AD_Column.ReadOnlyLogic`  |  Comprobación  
`AD_Dataset_Table.WhereClause`  |  WhereClause  
`AD_Field.DisplayLogic ` |  Comprobación  
`AD_Ref_Table.OrderByClause`  |  WhereClause (cláusula order by)  
`AD_Ref_Table.WhereClause`  |  WhereClause  
`AD_Tab.FilterClause ` |  WhereClause  
`AD_Tab.OrderByClause`  |  WhereClause (cláusula order by)  
`AD_Tab.WhereClause`  |  WhereClause  
`AD_Val_Rule.Code`  |  SQL  
  
---

Este trabajo es una obra derivada de [Expresiones dinámicas](http://wiki.openbravo.com/wiki/Dynamic_Expressions){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.