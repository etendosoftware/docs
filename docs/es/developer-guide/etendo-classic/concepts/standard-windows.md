---
tags:
  - Concepts
  - Ventanas estándar
  - Diccionario de la Aplicación
  - Ventana
  - Solapa
  - Campo
---

# Ventanas estándar

## Visión general

Las **Ventanas estándar** son las ventanas definidas completamente en el **Diccionario de la Aplicación**. Permiten visualizar y editar registros en tablas.

Después de definir (o modificar) una ventana estándar, el sistema debe reconstruirse (`./gradlew smartbuild`). Durante este proceso `WAD` genera automáticamente el código `Java`, `XSQL`, `HTML` y `XML` para esa ventana y se compila. Esto significa que la definición completa de las ventanas estándar está dentro del Diccionario de la Aplicación sin necesidad de desarrollos manuales. Esto tiene una serie de beneficios:

  * No es necesario escribir código manual: esto reduce la posibilidad de introducir errores.
  * Desarrollo más rápido: como la creación de una ventana consiste únicamente en definirla en el Diccionario de la Aplicación, es más rápido que hacerlo manualmente.
  * Inclusión automática de nuevas funcionalidades y correcciones de errores: siempre que `WAD` corrige un error o añade una nueva funcionalidad, esto se propaga automáticamente a todas las ventanas estándar cuando se reconstruye el sistema, sin necesidad de recodificar o redefinir nada.

## Estructura: Ventanas, Solapas y Campos

La estructura de las ventanas estándar consiste en `Ventana`, `Solapa` y `Campo`.

  * [**Ventana**](#ventana): las ventanas son contenedores de solapas. Su propósito principal es agrupar un conjunto de solapas relacionadas. Se pueden añadir al menú de la aplicación.
  * [**Solapa**](#solapa): las solapas se ubican dentro de las ventanas y pueden ordenarse jerárquicamente. Cada solapa está vinculada a una única [Tabla del Diccionario de la Aplicación](../concepts/data-model.md#tables-in-application-dictionary) y contiene un número de campos.
  * [**Campo**](#campo): los campos están contenidos dentro de las solapas. Cada campo está asociado a una [Columna](../concepts/data-model.md#columns_in_application_dictionary) en la misma tabla que su solapa.

![](../../../assets/developer-guide/etendo-classic/concepts/Standard_Windows-0.png)

Las siguientes secciones explican cómo se definen **Ventana**, **Solapa** y **Campo**. Se gestionan desde la ventana `Diccionario de la Aplicación` > `Windows, Tabs, and Fields`.

## Ventana

Las ventanas se generan automáticamente por `WAD` a partir de su definición en el Diccionario de la Aplicación; todas las ventanas tienen un diseño común.

### Menú

Las ventanas se pueden añadir al [Menú de la aplicación](../concepts/application_menu.md).

## Solapa

Las `Solapa` se incluyen dentro de `Ventana`. Cada solapa está limitada a una única `Table` del Diccionario de la Aplicación. Las siguientes subsecciones detallan algunos temas importantes que deben tenerse en cuenta al crear una solapa.

### Jerarquía de solapas

Las `Solapa` se muestran jerárquicamente; se definen en forma de árbol. Esto significa que una solapa puede tener subsolapas (es la solapa padre de ellas); en consecuencia, una solapa también puede ser hija de otra, y es posible tener varias solapas al mismo nivel.

Esta jerarquía se especifica usando dos campos en la solapa:

  * `Nivel solapa`: indica el nivel en la jerarquía, siendo 0 el nivel superior, 1 las solapas hijas de las de nivel 0, etc. Normalmente hay una única solapa en el nivel 0 y el resto de solapas de la ventana son subsolapas de esta.
  * `Sequence Number`: es un número que define el orden en el que se muestran las solapas. Se ordenan de forma ascendente, por lo que los valores más bajos quedan a la izquierda y los más altos a la derecha. Es una buena idea no usar números consecutivos para permitir la inclusión de nuevas solapas entre las existentes.

La combinación de estos dos valores proporciona la posición y la jerarquía de cada solapa. Veamos mediante un ejemplo cómo podría definirse la siguiente estructura de solapas:

```
     A
     |-A1
     |  |-A11
     |-A2
     |  |-A21
     |  |-A22
     |     |-A221
     |-A3
```

| Solapa | Número de secuencia | Nivel solapa |
|-----|-----------------|-----------|
| A   | 10              | 0         |
| A1  | 20              | 1         |
| A11 | 30              | 2         |
| A2  | 40              | 1         |
| A21 | 50              | 2         |
| A22 | 60              | 2         |
| A221| 70              | 3         |
| A3  | 80              | 1         |

Al crear subsolapas, es necesario establecer qué columna en la solapa padre va a ser la columna maestra para la subsolapa, con el fin de mostrar en las subsolapas únicamente los registros que están vinculados al registro actual en la solapa padre. Por ejemplo, supongamos que la solapa A es una solapa para la tabla `C_Invoice` y la solapa A1 es para `C_InvoiceLine`; en este caso, `C_Invoice.C_Invoice_ID` en la solapa A debe ser la columna maestra para la solapa A1, mostrando en A1 únicamente los registros vinculados al registro seleccionado en A.

Existen tres formas posibles de establecer cuál es la columna maestra en la solapa padre:

  1. Usando el check `AD_Column.IsParent` en la tabla utilizada en la subsolapa. Cuando una tabla en una solapa contiene columnas marcadas como `Link to Parent Column`, se busca en la solapa padre una columna con el mismo nombre y, si se encuentra, esa será la maestra.
  2. Por `name`. En caso de que la tabla en la subsolapa tenga una columna con el mismo nombre que la `primary key` de la tabla padre, el enlace se generará usándolas.
  3. Usando `AD_Tab.WhereClause`. En caso de que no sea posible usar #1 o #2, la relación debe establecerse en el campo `Where Clause` de la solapa hija. Para más información sobre esta cláusula, consulte el documento sobre [Expresiones dinámicas](../concepts/dynamic_expressions.md). En estos casos, es posible marcar el indicador `Disable Parent Key Property`; al hacerlo, solo se usará la cláusula where para crear la relación, sin añadir ningún otro criterio.

#### Mecanismo de bloqueo

Todas las solapas generadas por `WAD` implementan un mecanismo simple de [bloqueo optimista](https://en.wikipedia.org/wiki/Optimistic_concurrency_control){target="\_blank"}.

Cuando un registro se carga en modo edición, se almacena su `timestamp` de actualización. Si el registro se modifica y se guarda, este timestamp almacenado se compara con el actual en base de datos para ese registro. En caso de que sean diferentes, ese registro ha sido modificado por otro usuario o proceso y la aplicación no permite guardar las modificaciones actuales. De lo contrario, las modificaciones realizadas desde que se cargó el registro hasta el momento actual se sobrescribirían.

![](../../../assets/developer-guide/etendo-classic/concepts/Standard_Windows-1.png)

##### Ventanas transaccionales

Las ventanas para documentos pueden configurarse como `Transactional`. Los documentos tienen un estado, que inicialmente es **Borrador**.
Cuando se accede a una ventana transaccional, aparece filtrada por defecto. Esto se visualiza mediante un `message` y un pequeño icono de `embudo` en la parte superior derecha.

![](../../../assets/developer-guide/etendo-classic/concepts/Standard_Windows-2.png)

El filtro aplicado incluye todos los documentos con estado Borrador o cuya fecha esté dentro del `Transaction Range` definido. Para limpiar el filtro, haga clic en el icono de `embudo`.

Para definir una ventana como transaccional, vaya a `Diccionario de la Aplicación` > `Windows, Tabs, and Fields` > solapa `Ventana` y seleccione el `Window Type` como `Transaction`.

Para definir el **Rango de transacciones**, vaya a `General Setup` > `Application` > `Session Preferences` y defina en `Transaction Range` el número máximo de días durante los cuales se mostrarán los documentos procesados.

##### Tablas de alto volumen

Cuando una tabla se define como `High Volume` (en `Diccionario de la Aplicación` > `Tables and Columns` > solapa `Table`) y la solapa que la muestra está configurada para mostrarse por defecto en modo edición (`Default Edit Mode` en `Diccionario de la Aplicación` > `Windows, Tabs, and Fields` > `Window` > solapa `tab`), al acceder a la solapa se muestra un filtro.

##### Filtro en la solapa

En `Diccionario de la Aplicación` > `Windows, Tabs, and Fields` > `Window` > solapa `tab` existe un campo **Filtro**, `HQL Filter Clause`. Este campo permite utilizar `HQL where clauses` como filtro por defecto para la solapa. Cuando se accede a la solapa, este filtro se aplica; para eliminarlo, simplemente haga clic en el icono de filtro `embudo`.

!!!note
    Este campo es diferente de `HQL Where Clause`, que también acepta cláusulas where, pero esa cláusula es permanente y no puede ser eliminada por el usuario.

## Campo

Los `Campo` están contenidos en las solapas; cada campo tiene asociada una `column` (de la misma `table` que la de la solapa). Muestra y permite editar el valor de la columna. La forma en que un campo se muestra dentro de la solapa viene determinada por la [referencia](../concepts/data-model.md#references) que tenga la columna asociada.

Algunas de las cosas que deben tenerse en cuenta al configurar un campo son:

  * `Read Only Logic`, que permite determinar si el campo es de solo lectura (aplica solo cuando el campo es de lectura-escritura). El solo lectura indica que este campo solo puede leerse. No puede actualizarse. Tenga en cuenta que se define a nivel de Columna en el Diccionario de la Aplicación. Es una [Expresión dinámica](../concepts/dynamic_expressions.md).
  * `Display Logic`, que permite mostrar u ocultar el campo en función de los valores de otros campos. Es una [Expresión dinámica](../concepts/dynamic_expressions.md).
    * La lógica de visualización se tiene en cuenta en `grid view` como la lógica de solo lectura, aplicándose únicamente cuando un registro se edita en la vista de cuadrícula.
  * `Central Maintenance`, cuyo funcionamiento se explica en el documento sobre [Elementos y sincronizar terminología](../concepts/Element_and_Synchronize_Terminology.md).
  * [`Callout`](../concepts/data-model.md#callout), aunque no se define en los campos, les afecta directamente porque se disparan cuando se modifican los valores de los campos.
  * `Field group`: los campos pueden asignarse a un grupo de campos; cuando un conjunto de campos tiene un grupo de campos, se muestra un separador en la solapa. Los grupos de campos se definen en `Diccionario de la Aplicación` > `Setup` > solapa `Field Category`.

---

Este trabajo es una obra derivada de [Ventanas estándar](http://wiki.openbravo.com/wiki/Standard_Windows){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.