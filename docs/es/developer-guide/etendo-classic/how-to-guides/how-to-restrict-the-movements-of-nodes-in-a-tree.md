---
title: Cómo restringir los movimientos de nodos en un árbol
tags: 
    - Restringir
    - Movimientos
    - Nodo
    - Árbol
status: beta
---
  
# Cómo restringir los movimientos de nodos en un árbol

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

La **vista de cuadrícula de árbol** permite mover un nodo a otro padre o a otra posición dentro de su nodo padre actual.

Algunos árboles pueden tener restricciones sobre cómo se puede mover un nodo a otra posición del árbol. Por ejemplo, el árbol de **Organización** no permite mover un nodo si pertenece a una organización que está lista, y el árbol de menú no permite mover un nodo si pertenece a un elemento de menú cuyo módulo no está en desarrollo.

Los desarrolladores pueden restringir los movimientos de nodos de un árbol en particular mediante la creación de una subclase de la clase `CheckTreeOperationManager`.

## Clase CheckTreeOperationManager

### Sobrescritura del método checkNodeMovement

`CheckTreeOperationManager` es una clase abstracta que expone un método:

``` java
public abstract ActionResponse checkNodeMovement(Map<String, String> parameters, String nodeId,
    String newParentId, String prevNodeId, String nextNodeId);
```

Este método comprueba si un movimiento de nodo en particular es válido. Tiene los siguientes parámetros:

  - **parameters**: parámetros enviados desde la cuadrícula de árbol a `TreeDatasourceService`. 
  - **nodeId**: id del nodo que se está moviendo. 
  - **newParentId**: id del nuevo padre del nodo que se está moviendo. 
  - **prevNodeId**, **nextNodeId**: ids de los nodos que quedarán respectivamente antes y después del nodo si el movimiento es válido. 

El método `checkNodeMovement` devuelve un objeto de una clase de utilidad llamada `ActionResponse`, que tiene tres atributos:

``` java
private boolean success;
private String messageType;
private String message;
```

El atributo success representa si el movimiento del nodo es válido. Los atributos `messageType` y message pueden utilizarse para mostrar un mensaje en la barra de mensajes del cliente independientemente de la validez del movimiento del nodo.

El método `checkNodeMovement` es ejecutado por `TreeDatasourceService` después de cada movimiento de nodo si se ha definido un `CheckTreeOperationManager` para el árbol al que pertenece el nodo. Si el método `checkNodeMovement` devuelve un `ActionResponse` con success = true, entonces el movimiento del nodo se confirmará y el nodo se mostrará en el lado del cliente en su posición actualizada. 
Si devuelve un Action response con `success = false`, el movimiento del nodo se cancelará y el nodo volverá a su posición original en el lado del cliente.

### Asociar un `CheckTreeOperationManager` con un árbol en particular

Los `CheckTreeOperationManagers` se instancian usando [inyección de dependencias](../concepts/etendo-architecture.md#introducing-weld-dependency-injection-and-more).

Todas las implementaciones de `CheckTreeOperationManagers` deben tener alcance de aplicación y deben tener el nombre de la tabla asociada con el árbol como un calificador. Por ejemplo, el `CheckTreeOperationManager` utilizado para el árbol de menú tiene las siguientes anotaciones:

``` java
    @ApplicationScoped
    @Qualifier("ADMenu")
```

## Ejemplo: Árbol de Organización

En el árbol definido para la tabla Organización, no se permite mover nodos si pertenecen a una organización que está marcada como lista.

Esta es la implementación completa de su `CheckTreeOperationManager`:

``` java
package org.openbravo.service.datasource.treeChecks;
 
import java.util.Map;
 
import javax.enterprise.context.ApplicationScoped;
 
import org.openbravo.client.kernel.ComponentProvider.Qualifier;
import org.openbravo.dal.service.OBDal;
import org.openbravo.erpCommon.utility.OBMessageUtils;
import org.openbravo.model.common.enterprise.Organization;
import org.openbravo.service.datasource.CheckTreeOperationManager;
 
@ApplicationScoped
@Qualifier("Organization")
public class OrganizationTreeOperationManager extends CheckTreeOperationManager {
 
    /**
     * Only allows to move a node if it belong to a organization that is not set as ready
     */
    @Override
    public ActionResponse checkNodeMovement(Map<String, String> parameters, String nodeId,
        String newParentId, String prevNodeId, String nextNodeId) {
        Organization organization = OBDal.getInstance().get(Organization.class, nodeId);
        if (organization.isReady()) {
            return new ActionResponse(false, "error", OBMessageUtils.messageBD("OrgIsReady"));
        } else {
            return new ActionResponse(true);
        }
    }
}
```

Estas anotaciones garantizan que este `CheckTreeOperationManager` se utilizará para comprobar si un movimiento de nodo es válido para el árbol de Organización:

``` java
    @ApplicationScoped
    @Qualifier("Organization")
```

El parámetro `nodeId` representa el id del nodo que se está moviendo. En este punto se sabe que el nodo pertenece al árbol de Organización. Esta línea obtiene la organización asociada con el nodo basándose en el nodeId:

``` java
Organization organization = OBDal.getInstance().get(Organization.class, nodeId);
```

Una vez que la organización está disponible, es lo suficientemente sencillo devolver un `ActionResponse` adecuado dependiendo de si la organización está marcada como lista o no:
``` java   
if (organization.isReady()) {
    return new ActionResponse(false, "error", OBMessageUtils.messageBD("OrgIsReady"));
} else {
    return new ActionResponse(true);
}
```
Si un usuario intentara mover un nodo asociado a una organización marcada como lista, este mensaje se mostrará en su barra de mensajes:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-restrict-the-movements-of-nodes-in-a-tree/moveorganization.png)

---
Este trabajo es una obra derivada de [Cómo restringir los movimientos de nodos en un árbol](http://wiki.openbravo.com/wiki/How_to_Restrict_the_Movements_of_Nodes_in_a_Tree){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.