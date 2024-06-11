---
tags:
  - Etendo classic
  - Table
  - Tree
  - Fields
  - Application dictionary
---

# How to Define a Table as a Tree

## Overview

If a table contains data that is bound to be represented hierarchically using a tree, the developer can define tree categories for it.

Defining tree categories for a table has two advantages:

  * It enables using the tree grid view for tabs associated with that table.
  * It enables using that table in Tree Selectors.

## Table Tree Category subtab

The Table Tree Category tab allows to define tree categories for tables. It is possible to define several tree categories for a table, if it can be expresses in different ways hierarchically.

### Enabling the Table Tree Category subtab

The Table Tree Category is a subtab of the header tab of the Tables and Columns windows. It is hidden by default, in order to enable it the user has to check the table Is Tree flag.

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-1.png)

### Tree Structures

There are three tree structures available:

#### AD Tree Structure

If this structure is used, the information needed to handle the hierarchy of the tree data will be stored internally by Etendo in the `AD_Tree` and `AD_TreeNode` tables.

#### Link to Parent Tree Structure

This structure should be used if the table contains a column that represents the parent node of the record. For instance, consider a table called `Employee`, that has a column called `reportsTo`. This column points to the employee who the current employee must report to.

#### Custom Tree Structure

There may be other cases where the information needed to handle the hierarchy is stored within the table but by means other than a column pointing directly to the parent node. For instance, this is the case of the `AD_Tab` table, where the hierarchy of the tabs is defined using the `seqNo` and `tabLevel` columns. In this case, the user has to provide a manual datasource to handle the tree hierarchy.

### Common Fields for all Tree Structures

The following fields apply to all trees, regardless of its tree structure:

  * **Name**: Name of the tree. This is the display field shown in the references to this table from the Tabs and the Tree Reference.
  * **Tree Structure**: Tree structure that this tree will use
  * **Is Ordered**: This flag specifies if the tree is ordered, that is, if it matters the order of the nodes within its parent node.
  * **Is Parent Selection Allowed**: If false, then in the tree references that point to this tree will only allow to pick leaf nodes. Otherwise it will be possible to select both folder and leaf nodes.
  * **Is Main Tree**: Several trees can be defined for a table, but only one of them can be the main tree. Each tree can define a different behavior for the creation and deletion of nodes, but only the behavior defined by the main tree will be taken into account.
  * **Apply HQL Where Clause to Child Nodes**: If this property is set, then if there is a HQL Where Clause defined for the table, it will be applied to all nodes. If it is unchecked, then it will be applied only to the root nodes. This field should only be unchecked in the tree grid view should show records that are not shown in the standard grid view. For instance, consider a sub tab called Children, that shows the children of a person. The HQL Where Clause of the table is in charge of showing only the children of the person selected in the parent tab. The user might decide that he wants to see all the person descendants in the tree grid view, so the HQL Where Clause should only be applied to the root nodes.
  * **Node Deletion Policy** (Etendo PR14Q3): The are two options:
    * "Reparent Child Nodes": If a node is deleted, all its child nodes are transfered to its parent node.
    * "Do Not Allow If Has Children": A node with children cannot be deleted.

### ADTree Structure Fields

  * **Handle Nodes Manually**: Each time a new record is created or deleted in a table that contains an `ADTree`, an `ADTree` node must be created or deleted respectively. The developer can define using this flag if Etendo should automatically create and delete the `ADTree` nodes, or if the new nodes are going to be handled manually (i.e. using triggers or event handlers).

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-2.png)

### LinkToParent Structure Fields

  * **Link to Parent Column**: Column that points to the parent node of the record.
  * **Node Id Column Column**: Column pointed by the Link to Parent Column. In most cases the key column of the table should be used.
  * **Has Multiparent nodes**: In some cases the table contains hierarchical data that is not strictly a tree because each record may have several parent nodes. Consider for instance a table that represents product bundles. Each bundle can contain several bundles (has several children), and be contained in several other bundlers (has several parents). Only if this is the case should this flagged be checked.

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-3.png)

### Custom Tree Structure Fields

  * **Datasource**: A datasource that will handle all the tree operations. For more details, click [here](./How_to_Create_a_Custom_Tree.md).

## Enabling the Tree Grid View in a Tab

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-4.png)

In order to enable the Tree Grid View in a Tab, the system admin has to pick a tree category in the Table Tree Category field.

By default, the root nodes will be those whose parent is null or '0'. The user can overwrite this by defining a HQL Where Clause for Root Nodes that will be used to pick the root nodes for this tab.

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_Define_a_Table_as_a_Tree-5.png)

## Defining a Tree Selector

Tables that have trees defined are bound to be used in Tree Selectors. Tree Selector are a variant of the Etendo selectors, that take advantage of the hierarchical data of the tables, allowing to use trees for filtering and picking records.

The documentation on how to define a tree selector can be found [here](./How_to_Create_a_Tree_Selector.md)

This work is a derivative of [How to define a table as a tree](https://wiki.openbravo.com/wiki/How_to_Define_a_Table_as_a_Tree){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.