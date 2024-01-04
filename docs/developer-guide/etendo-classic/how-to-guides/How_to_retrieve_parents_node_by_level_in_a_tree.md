![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  How to retrieve parents node by level in a tree

##  Contents

  * 1  Objective 
  * 2  Recommended articles 
  * 3  Execution Steps 
  * 4  Result 

  
---  
  
##  Objective

In a tree, from a node, retrieve the node's parent in the level indicated.

##  Recommended articles

In Openbravo ERP you can create a  tree structure  to use in a custom window

##  Execution Steps

There are two database functions:

  * function AD_GET_NODE_TREE_BYLEVEL 

input params: ad_tree_id (VARCHAR(32)), node_id (VARCHAR(32)), level (NUMERIC)  
output: node (VARCHAR(32))  
This function returns one parent of the node. This parent is in the level
indicated, where the level 0 is the first node of tree, in level 1 are the
sons of this first node, etc...

  * function AD_GET_LEVEL_NODE_TREE 

input params: ad_tree_id (VARCHAR(32)), node_id (VARCHAR(32))  
output: level (NUMERIC)  
Returns the level of the node in the tree, where the level 0 is the first node
of tree, in level 1 are the sons of this first node, etc...

  * Example 

The projects can be managed in a tree. So, you can group the projects in
differents levels, allowing obtain info by level In this case, the nodes in
first level are the main projects, and the projects in second level, are the
secundary projects. The normal projects (leaf nodes) belong to a main project
and a secundary project. The revenues and expenses are reported to the normal
project (leaf nodes), and you can obtain information in the level of parent
nodes. One example is represented in picture.

tree T:  ![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_retrieve_parents_node_by_level_in_a_tree-0.png){: .legacy-image-style}

AD_GET_NODE_TREE_BYLEVEL ('T', 'E', 1) -> 'C'  
AD_GET_NODE_TREE_BYLEVEL ('T', 'E', 0) -> 'A'  
AD_GET_LEVEL_NODE_TREE ('T', 'B') -> 1  
AD_GET_LEVEL_NODE_TREE ('T', 'D') -> 2  

Sometimes, it is interesting to know what is the main and secundary project of
a project.

##  Result

The functions return the ID of parent node in level indicated, and the level
of the node in the tree.

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_retrieve_parents_node_by_level_in_a_tree
"

This page has been accessed 5,841 times. This page was last modified on 9 May
2013, at 11:57. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

