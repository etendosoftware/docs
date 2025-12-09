---
title: How to Retrieve Parents Node by Level in a Tree
tags: 
    - Retrieve
    - Parents
    - Node
    - Tree

status: beta
---

# How to Retrieve Parents Node by Level in a Tree

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

## Overview

This section explains how to retrieve the node's parent in a tree, from a node, in the level indicated.

## Functions

There are two database functions:

- Function `AD_GET_NODE_TREE_BYLEVEL`:

    input params: `ad_tree_id (VARCHAR(32))`, `node_id (VARCHAR(32))`, `level (NUMERIC)` output: `node (VARCHAR(32))`  
    This function returns one parent of the node. This parent is in the level indicated, where the level 0 is the first node of tree, in level 1 are the sons of this first node, etc...

- Function `AD_GET_LEVEL_NODE_TREE`:

    input params: `ad_tree_id (VARCHAR(32))`, `node_id (VARCHAR(32))`  output: `level (NUMERIC)`  
    Returns the level of the node in the tree, where the level 0 is the first node of tree, in level 1 are the sons of this first node, etc...

## Example:

    The projects can be managed in a tree. So, you can group the projects in different levels, allowing obtaining information by level. In this case, the nodes in first level are the main projects, and the projects in second level, are the secondary projects. The normal projects (leaf nodes) belong to a main project and a secondary project. The revenues and expenses are reported to the normal project (leaf nodes), and you can obtain information in the level of parent nodes. One example is represented in image below.

    **Tree T**:  ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-retrieve-parents-node-by-level-in-a-tree.png)

    ```
    AD_GET_NODE_TREE_BYLEVEL('T', 'E', 1) -> 'C'  
    AD_GET_NODE_TREE_BYLEVEL('T', 'E', 0) -> 'A'  
    AD_GET_LEVEL_NODE_TREE('T', 'B') -> 1  
    AD_GET_LEVEL_NODE_TREE('T', 'D') -> 2  
    ```
    The functions return the `ID` of parent node in level indicated, and the level of the node in the tree.

---

This work is a derivative of [How to Retrieve Parents Node by Level in a Tree](http://wiki.openbravo.com/wiki/How_to_retrieve_parents_node_by_level_in_a_tree){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.