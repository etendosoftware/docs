---
tags:
  - How to
  - Etendo classic
  - Table
  - Tree
  - Fields
  - Application dictionary
---

# Cómo definir una tabla como un árbol

## Visión general

Si una tabla contiene datos que deben representarse jerárquicamente mediante un árbol, el desarrollador puede definir **categorías de árbol** para ella.

Definir categorías de árbol para una tabla tiene dos ventajas:

  * Permite utilizar la vista de cuadrícula de árbol para las pestañas asociadas a esa tabla.
  * Permite utilizar esa tabla en los selectores de árbol.

## Subpestaña Categoría de árbol de tabla

La pestaña Categoría de árbol de tabla permite **definir categorías de árbol para tablas**. Es posible definir varias categorías de árbol para una tabla, si puede expresarse de diferentes formas jerárquicamente.

### Habilitar la subpestaña Categoría de árbol de tabla

Categoría de árbol de tabla es una subpestaña de la pestaña de cabecera de las ventanas Tablas y columnas. Está oculta por defecto; para habilitarla, el usuario debe marcar el indicador Is Tree de la tabla.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-1.png)

### Estructura de árbol

Hay tres estructuras de árbol disponibles:

#### Estructura de árbol AD

Si se utiliza esta estructura, la información necesaria para gestionar la jerarquía de los datos del árbol se almacenará internamente en Etendo en las tablas `AD_Tree` y `AD_TreeNode`.

#### Estructura de árbol enlazada al padre

Esta estructura debe utilizarse si la tabla contiene una columna que representa el nodo padre del registro. Por ejemplo, considere una tabla llamada `Employee`, que tiene una columna llamada `reportsTo`. Esta columna apunta al empleado al que el empleado actual debe reportar.

#### Estructura de árbol personalizada

Puede haber otros casos en los que la información necesaria para gestionar la jerarquía se almacena dentro de la tabla, pero por medios distintos a una columna que apunte directamente al nodo padre. Por ejemplo, este es el caso de la tabla `AD_Tab`, donde la jerarquía de las pestañas se define utilizando las columnas `seqNo` y `tabLevel`. En este caso, el usuario debe proporcionar una fuente de datos manual para gestionar la jerarquía del árbol.

### Campos comunes para todas las estructuras de árbol

Los siguientes campos se aplican a todos los árboles, independientemente de su estructura de árbol:

  * **Nombre**: Nombre del árbol. Este es el campo de visualización que se muestra en las referencias a esta tabla desde las pestañas y la referencia de árbol.
  * **Estructura de árbol**: Estructura de árbol que utilizará este árbol.
  * **Está ordenado**: Este indicador especifica si el árbol está ordenado, es decir, si importa el orden de los nodos dentro de su nodo padre.
  * **Permitir selección de nodos no hoja**: Si es falso, entonces las referencias de árbol que apunten a este árbol solo permitirán seleccionar nodos hoja. En caso contrario, será posible seleccionar tanto nodos carpeta como nodos hoja.
  * **Es árbol principal**: Se pueden definir varios árboles para una tabla, pero solo uno de ellos puede ser el árbol principal. Cada árbol puede definir un comportamiento diferente para la creación y eliminación de nodos, pero solo se tendrá en cuenta el comportamiento definido por el árbol principal.
  * **Aplicar cláusula HQL where a los nodos hijo**: Si esta propiedad está establecida, entonces si hay una cláusula HQL Where definida para la tabla, se aplicará a todos los nodos. Si no está marcada, entonces se aplicará solo a los nodos raíz. Este campo solo debería desmarcarse cuando la vista de cuadrícula de árbol deba mostrar registros que no se muestran en la vista de cuadrícula estándar. Por ejemplo, considere una subpestaña llamada Hijos, que muestra los hijos de una persona. La cláusula HQL Where de la tabla se encarga de mostrar solo los hijos de la persona seleccionada en la pestaña padre. El usuario podría decidir que quiere ver todos los descendientes de la persona en la vista de cuadrícula de árbol, por lo que la cláusula HQL Where solo debería aplicarse a los nodos raíz.
  * **Política de borrado de nodos**: Hay dos opciones:
    * **Reasignar nodos hijo al padre**: Si se elimina un nodo, todos sus nodos hijo se transfieren a su nodo padre.
    * **No permitir si tiene hijos**: Un nodo con hijos no se puede eliminar.

### Campos de la estructura ADTree

  * **Gestionar nodos manualmente**: Cada vez que se crea o elimina un nuevo registro en una tabla que contiene un `ADTree`, debe crearse o eliminarse, respectivamente, un nodo `ADTree`. El desarrollador puede definir mediante este indicador si Etendo debe crear y eliminar automáticamente los nodos `ADTree`, o si los nuevos nodos se van a gestionar manualmente (es decir, usando triggers o manejadores de eventos).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-2.png)

### Campos de la estructura LinkToParent

  * **Columna padre**: Columna que apunta al nodo padre del registro.
  * **Columna de ID de nodo**: Columna apuntada por la Columna padre. En la mayoría de los casos debe utilizarse la columna clave de la tabla.
  * **Tiene nodos con varios nodos padre**: En algunos casos la tabla contiene datos jerárquicos que no son estrictamente un árbol porque cada registro puede tener varios nodos padre. Considere, por ejemplo, una tabla que representa paquetes de productos. Cada paquete puede contener varios paquetes (tiene varios hijos) y estar contenido en varios otros paquetes (tiene varios padres). Solo si este es el caso debe marcarse este indicador.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-3.png)

### Campos de la estructura de árbol personalizada

  * **Fuente de datos**: Una fuente de datos que gestionará todas las operaciones del árbol. 
  
!!!info
    Para más información, visite [Cómo crear un árbol personalizado](../how-to-guides/How_to_Create_a_Custom_Tree.md).

## Habilitar la vista de cuadrícula de árbol en una pestaña

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-4.png)

Para habilitar la vista de cuadrícula de árbol en una pestaña, el administrador del sistema debe seleccionar una categoría de árbol en el campo Categoría de árbol de tabla.

Por defecto, los nodos raíz serán aquellos cuyo padre sea null o '0'. El usuario puede sobrescribir esto definiendo una cláusula HQL Where para nodos raíz que se utilizará para seleccionar los nodos raíz de esta pestaña.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-5.png)

## Definir un selector de árbol

Las tablas que tienen árboles definidos están destinadas a utilizarse en **selectores de árbol**. Los selectores de árbol son una variante de los selectores de Etendo, que aprovechan los datos jerárquicos de las tablas, permitiendo utilizar árboles para filtrar y seleccionar registros.

!!!info
    Para más información, visite [Cómo crear un selector de árbol](../../etendo-classic/how-to-guides/How_to_Create_a_Tree_Selector.md). 

Este trabajo es una obra derivada de [Cómo definir una tabla como un árbol](https://wiki.openbravo.com/wiki/How_to_Define_a_Table_as_a_Tree){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.