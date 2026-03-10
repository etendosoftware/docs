---
title: Cómo recuperar el nodo padre por nivel en un árbol
tags: 
    - Recuperar
    - Padres
    - Nodo
    - Árbol

status: beta
---

# Cómo recuperar el nodo padre por nivel en un árbol

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Esta sección explica cómo recuperar el nodo padre de un nodo en un árbol, en el nivel indicado.

## Funciones

Existen dos funciones de base de datos:

- Función `AD_GET_NODE_TREE_BYLEVEL`:

    parámetros de entrada: `ad_tree_id (VARCHAR(32))`, `node_id (VARCHAR(32))`, `level (NUMERIC)` salida: `node (VARCHAR(32))`  
    Esta función devuelve un padre del nodo. Este padre se encuentra en el nivel indicado, donde el nivel 0 es el primer nodo del árbol, en el nivel 1 están los hijos de este primer nodo, etc...

- Función `AD_GET_LEVEL_NODE_TREE`:

    parámetros de entrada: `ad_tree_id (VARCHAR(32))`, `node_id (VARCHAR(32))`  salida: `level (NUMERIC)`  
    Devuelve el nivel del nodo en el árbol, donde el nivel 0 es el primer nodo del árbol, en el nivel 1 están los hijos de este primer nodo, etc...

## Ejemplo:

    Los proyectos pueden gestionarse en un árbol. Por lo tanto, puede agrupar los proyectos en diferentes niveles, lo que permite obtener información por nivel. En este caso, los nodos en el primer nivel son los proyectos principales, y los proyectos en el segundo nivel son los proyectos secundarios. Los proyectos normales (nodos hoja) pertenecen a un proyecto principal y a un proyecto secundario. Los ingresos y gastos se informan al proyecto normal (nodos hoja), y puede obtener información en el nivel de los nodos padre. Un ejemplo se representa en la imagen siguiente.

    **Árbol T**:  ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-retrieve-parents-node-by-level-in-a-tree.png)

    ```
    AD_GET_NODE_TREE_BYLEVEL('T', 'E', 1) -> 'C'  
    AD_GET_NODE_TREE_BYLEVEL('T', 'E', 0) -> 'A'  
    AD_GET_LEVEL_NODE_TREE('T', 'B') -> 1  
    AD_GET_LEVEL_NODE_TREE('T', 'D') -> 2  
    ```
    Las funciones devuelven el `ID` del nodo padre en el nivel indicado, y el nivel del nodo en el árbol.

---

Este trabajo es una obra derivada de [Cómo recuperar el nodo padre por nivel en un árbol](http://wiki.openbravo.com/wiki/How_to_retrieve_parents_node_by_level_in_a_tree){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.