---
title: Cómo crear un árbol personalizado
tags:
    - Datasource de árbol personalizado  
    - Estructuras de árbol 
    - Implementación manual de árbol 
    - TreeDatasourceService 
status: beta
---

# Cómo crear un árbol personalizado
 
!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Etendo proporciona soporte nativo para estructuras jerárquicas mediante los modelos **ADTree y LinkToParent**. Sin embargo, no todos los datos basados en árboles encajan en estas estructuras estándar. Para esos casos, Etendo permite a los desarrolladores definir **datasources manuales** que gestionan árboles almacenados en tablas personalizadas con su propia lógica de jerarquía.

Esta sección explica cómo **crear y configurar** un datasource manual para trabajar con una tabla de árbol personalizada, habilitando la navegación completa del árbol, la carga y la interacción fuera de los frameworks ADTree y LinkToParent.

## Clase TreeDatasourceService

Todos los datasources de tablas personalizadas deben ser una subclase de **TreeDatasourceService**. Este datasource se utiliza en los siguientes eventos:

- Cuando un registro es **Creado** en una tabla de árbol, si esta categoría de árbol está configurada como Árbol principal. 
- Cuando un registro es **eliminado** en una tabla de árbol, si esta categoría de árbol está configurada como Árbol principal. 
- Cuando la vista de cuadrícula de árbol asociada a esta tabla de árbol necesita **obtener nodos**. 
- Cuando un nodo es **movido** en la vista de cuadrícula de árbol asociada a esta tabla de árbol. 

La clase TreeDatasource expone los siguientes métodos abstractos:

### addNewNode

``` java 
protected void addNewNode(JSONObject bobProperties)
```

Este método se invoca cuando se **añade usando DAL a una tabla** un nuevo registro cuyo árbol principal es el árbol personalizado. Todas las propiedades bob del nuevo registro están disponibles a través del parámetro `bobProperties`.

La implementación de este método debe realizar todas las acciones necesarias para añadir el nuevo registro a la estructura de árbol. Por ejemplo, si el árbol personalizado va a usar **ADTree** y las **tablas de nodos de ADTree**, en este punto debería crearse el nodo de ADTree para el nuevo registro.

### deleteNode

``` java 
protected void deleteNode(JSONObject bobProperties)
```

Este método se invoca cuando se **elimina usando DAL de una tabla** un registro cuyo árbol principal es el árbol personalizado. Todas las propiedades bob del registro eliminado están disponibles a través del parámetro `bobProperties`.

La implementación de este método debe realizar todas las acciones necesarias para eliminar el registro de la estructura de árbol. Por ejemplo, eliminar un **nodo de ADTree**, reasignar el padre de los hijos del nodo eliminado, etc.

### moveNode

``` java
JSONObject moveNode(Map<String, String> parameters, String nodeId, String newParentId,
        String prevNodeId, String nextNodeId) throws Exception
```

Este método se invoca cuando un nodo es **movido usando la vista de cuadrícula de árbol**. Tiene estos parámetros:

- `Map<String,String>` parameters: todos los parámetros enviados desde la vista de cuadrícula de árbol al datasource. 
- String `nodeId`: el id del nodo que se está moviendo. 
- String `prevNodeId`: el id del nodo que se colocará adyacente justo antes del nodo. Será null si el nodo se mueve a la primera posición de su nuevo padre. 
- String `nextNodeId`: el id del nodo que se colocará adyacente justo después del nodo. Será null si el nodo se mueve a la última posición de su nuevo padre. 

Este método se encarga de realizar el cambio necesario para mantener la estructura de árbol actualizada tras el cambio (p. ej., actualizar el número de secuencia del nodo, etc.). 

### fetchNodeChildren

    
    
``` java 
protected JSONArray fetchNodeChildren(Map<String, String> parameters,
    Map<String, Object> datasourceParameters, String parentId, String hqlWhereClause,
    String hqlWhereClauseRootNodes) throws JSONException, TooManyTreeNodesException
```
Este método se invoca cuando la vista de cuadrícula de árbol o el selector de árbol necesitan **obtener los hijos de un nodo**.

Tiene los siguientes parámetros:

- `Map<String,String>` parameters: todos los parámetros enviados desde la vista de cuadrícula de árbol o el selector de árbol al datasource. 
- `Map<String,Object>` `datasourceParameters`: los parámetros específicos de este datasource. 
- `String parentId`: el id del nodo cuyos hijos se están obteniendo. Será **-1** cuando se obtengan los nodos raíz del árbol. 
- `hqlWhereClause`: cláusula where HQL que se aplicará al obtener los nodos hijos. 
- `hqlWhereClauseRootNodes`: cláusula where HQL que se usará para obtener los nodos raíz. Se define en la Categoría de árbol de tabla y en la Referencia de árbol. La mayoría de los datasource personalizados no la usarán porque tienen sus propios medios para obtener los nodos raíz. 

Los árboles de Etendo todavía no soportan paginación para obtener los nodos de un árbol. Esto significa que al datasource se le solicitan todos los hijos. Si el datasource devolviera un número de nodos superior al número almacenado en la preferencia `TreeDatasourceFetchLimit`, debería lanzarse la excepción `TooManyTreeNodesException`.

!!!info
    En caso de que la preferencia **TreeDatasourceFetchLimit** no esté definida, el número máximo de nodos que se pueden obtener por defecto se define con la constante `OB.Constants.TREE_DS_DEFAULT_FETCH_LIMIT`.  

  
Este método debe devolver un objeto json que contenga todas las propiedades de los registros asociados a los nodos devueltos, además de:

- `nodeId`: el id del nodo. A menos que el árbol necesite soportar nodos con varios padres, debe usarse el id del registro para establecer el nodeId.
- `parentId`: el id del padre del registro. La mayoría de las veces debe usarse el parámetro parentId para establecer esta propiedad. 
- `seqno`: si el árbol está ordenado, debe establecerse el número de secuencia del nodo. 
- `_hasChildren`: un booleano para especificar si el nodo tiene hijos por sí mismo. 

### nodeConformsToWhereClause
    
``` java 
protected boolean nodeConformsToWhereClause(TableTree tableTree, String nodeId,
        String hqlWhereClause)
```

Este método se invoca cuando **se filtra la cuadrícula de árbol**. Este método se encarga de comprobar si un nodo concreto de un árbol de tabla debe ser filtrado mediante una cláusula where HQL.

Tiene los siguientes parámetros:

- `TableTree tableTree`: la Categoría de árbol de tabla asociada a la solapa/selector que se está filtrando. 
- `String nodeId`: el id del nodo que se va a comprobar. 
- `String hqlWhereClause`: la cláusula where HQL que debe aplicarse al nodo proporcionado. 

Este método debe devolver true si el nodo cumple la cláusula where HQL; en caso contrario, false.

### getJSONObjectByRecordId

``` java
protected JSONObject getJSONObjectByRecordId(Map<String, String> parameters,
    Map<String, Object> datasourceParameters, String bobId)
```

Este método se invoca cuando **se está filtrando una tabla de árbol**. Su propósito es devolver la representación JSON completa de un nodo basándose en el id del nodo. Tiene estos parámetros:

- `Map<String,String> parameters`: los parámetros enviados desde la cuadrícula de árbol al datasource. 
- `Map<String,Object> datasourceParameters`: los parámetros específicos de este datasource. 
- `String recordId`: el id del registro cuya representación JSON se va a devolver. 

Este método debe devolver un objeto json que contenga todas las propiedades del registro solicitado, además de: 

- `nodeId`: el id del nodo. A menos que el árbol necesite soportar nodos con varios padres, debe usarse el id del registro para establecer el `nodeId` `parentId`: el id del padre del registro. La mayoría de las veces debe usarse el parámetro `parentId` para establecer esta propiedad. 
- `seqno`: si el árbol está ordenado, debe establecerse el número de secuencia del nodo. 
- `_hasChildren`: un booleano para especificar si el nodo tiene hijos por sí mismo.

## Ejemplo: tabla AD_TAB

En esta sección se va a describir un **datasource de árbol personalizado para la tabla ADTab**.

La tabla **ADTab** almacena solapas, que están estructuradas jerárquicamente en una ventana. Todas las ventanas tienen una solapa de cabecera, que puede tener subsolapas. Cada una de estas subsolapas puede tener subsolapas y también puede tener subsolapas propias, y así sucesivamente.

La tabla ADTab **construye la jerarquía** de las solapas usando los campos Nivel de solapa y Número de secuencia de esta forma:

- La solapa con nivel 0 es la solapa de cabecera.
- Si el nivel de solapa de una solapa es **tl** y su número de secuencia es **sn** , su solapa padre será la solapa con nivel de solapa = **tl-1** cuyo número de secuencia sea el más alto entre aquellas solapas con número de secuencia < **sn** . 

Este árbol debe ser personalizado porque:

- La información para construir la jerarquía se almacena en la tabla ADTab, por lo que no es necesario usar ADTree. 
- La tabla `ADTab` no tiene una columna que apunte directamente al nodo padre de un registro, por lo que la estructura de árbol LinkToParent no es adecuada. 

---
Este trabajo es una obra derivada de [Cómo crear un árbol personalizado](http://wiki.openbravo.com/wiki/How_to_Create_a_Custom_Tree){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.