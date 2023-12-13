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

  

#  How to Create a Custom Tree

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available from **Openbravo PR14Q2**  
---|---  
  
##  Contents

  * 1  Introduction 
  * 2  TreeDatasourceService class 
    * 2.1  addNewNode 
    * 2.2  deleteNode 
    * 2.3  moveNode 
    * 2.4  fetchNodeChildren 
    * 2.5  nodeConformsToWhereClause 
    * 2.6  getJSONObjectByRecordId 
  * 3  Example: AD_TAB table 

  
---  
  
##  Introduction

Openbravo supports native support for the ADTree and LinkToParent structures
(more info  here  ). Openbravo also provides support for defining manual
datasources to handle trees whose structure it not ADTree nor LinkToParent.
This manual describes how to create a manual datasource to handle a custom
tree table.

##  TreeDatasourceService class

All the datasources from custom tables must be a subclass of
TreeDatasourceService  . This datasource is used in the following events:

  * When a record is created in a tree table, if this tree category is set as Main Tree. 
  * When a record is deleted in a tree table, if this tree category is set as Main Tree. 
  * When the tree grid view associated with this tree table needs to fetch nodes 
  * When a node is moved in the tree grid view associated with this tree table. 

The TreeDatasource class exposes the following abstract methods:

###  addNewNode

    
    
    protected void addNewNode(JSONObject bobProperties)

This method is invoked when a new record is added using DAL to a table whose
main tree is the custom tree. All the bob properties of the new record are
available from the bobProperties parameter.

The implementation of this method should take all the action needed to add the
new record to the tree structure. For instance, if the custom tree is going to
use the ADTree and ADTree node tables, at this point the ADTree node should be
created for the new record.

###  deleteNode

    
    
    protected void deleteNode(JSONObject bobProperties)

This method is invoked when a new record is delete using DAL from a table
whose main tree is the custom tree. All the bob properties of the deleted
record are available from the bobProperties parameter.

The implementation of this method should take all the action needed to remove
the new record to the tree structure. For instance, removing an ADTree node,
reparenting the children of the deleted node, etc.

###  moveNode

    
    
    JSONObject moveNode(Map<String, String> parameters, String nodeId, String newParentId,
          String prevNodeId, String nextNodeId) throws Exception

This method is invoked when a node is moved using the tree grid view. It has
these parameters:

  * Map<String, String> parameters: all the parameters sent from the tree grid view to the datasource 
  * String nodeId: the id of the node being moved 
  * String prevNodeId: the id of the node that will be placed adjacently just before the node. It will be null if the node is moved to the first position of its new parent. 
  * String nextNodeId: the id of the node that will be placed adjacently just after the node. It will be null if the node is moved to the last position of its new parent. 

This method is in charge of making the change needed to keep the tree
structure updated after the change (i.e. updating the node sequence number,
etc)

###  fetchNodeChildren

    
    
    protected JSONArray fetchNodeChildren(Map<String, String> parameters,
          Map<String, Object> datasourceParameters, String parentId, String hqlWhereClause,
          String hqlWhereClauseRootNodes) throws JSONException, TooManyTreeNodesException

This method is invoked when the tree grid view or the tree selector need to
fetch the children of a node.

It has the following parameters:

  * Map<String, String> parameters: All the parameters sent from the tree grid view or tree selector to the datasource. 
  * Map<String, Object> datasourceParameters: The parameters specific to this datasource 
  * String parentId: The id of the node whose childrens are being fetched. It will be "-1" when the tree root nodes are fetched. 
  * hqlWhereClause: hql where clause to be applied when obtaining the children nodes. 
  * hqlWhereClauseRootNodes: hql where clause to be used to fetch the root nodes. It is defined in the Table Tree Category and in the Tree Reference. Most custom datasource will not use it because they have their own means to fetch the root nodes. 

The Openbravo trees do not support pagination for fetching the nodes of a tree
yet. This means that the datasource is asked for all the children. If the
datasource were to return a number of nodes higher than the number stored in
the TreeDatasourceFetchLimit preference, the TooManyTreeNodesException
exception should be thrown.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Note: Starting from **PR18Q2** , in case of the TreeDatasourceFetchLimit
preference is not defined, the maximum number of nodes that can be fetched by
default is defined with the constant OB.Constants.TREE_DS_DEFAULT_FETCH_LIMIT.  
---|---  
  
This method should return a json object that contains all the properties of
the records associated with the returned nodes plus:

  * nodeId: the id of the node. Unless the tree needs to support nodes with several parents, the id of the record should be used to set the nodeId 
  * parentId: the id of the parent of the record. Most of the times the parentId parameter should be used to set this property. 
  * seqno: if the tree is ordered, the sequence number of the node should be set. 
  * _hasChildren: a boolean to specify if the node has children on its own. 

###  nodeConformsToWhereClause

    
    
    protected boolean nodeConformsToWhereClause(TableTree tableTree, String nodeId,
          String hqlWhereClause)

This method is invoked when the tree grid is filtered. This method is in
charge of cheking if a particular node of a table tree should be filtered out
by a HQL Where Clause.

It has the following parameters:

  * TableTree tableTree: The Table Tree Category associated with the tab/selector being filtered. 
  * String nodeId: The id of the node to be checked 
  * String hqlWhereClause: the hql where clause that has to be applied to the provided node. 

This method should return true if the node conforms to the HQL where clause,
false otherwise.

###  getJSONObjectByRecordId

    
    
    protected JSONObject getJSONObjectByRecordId(Map<String, String> parameters,
          Map<String, Object> datasourceParameters, String bobId)

This method is invoked when a tree table is being filtered. Its purpose is to
return the full JSON representation of a node based on the node id. It has
these parameters:

  * Map<String, String> parameters: The parameters sent from the tree grid to the datasource. 
  * Map<String, Object> datasourceParameters: The specific parameteres of this datasource. 
  * String recordId: The id of the record whose JSON representation is to be returned. 

This method should return a json object that contains all the properties of
the requested record plus: nodeId: the id of the node. Unless the tree needs
to support nodes with several parents, the id of the record should be used to
set the nodeId parentId: the id of the parent of the record. Most of the times
the parentId parameter should be used to set this property. seqno: if the tree
is ordered, the sequence number of the node should be set. _hasChildren: a
boolean to specify if the node has children on its own.

##  Example: AD_TAB table

In this section a custom tree datasource for the ADTab table is going to be
described.

The ADTab table stores tabs, which are structured hierarchy in a window. All
windows have a header tab, that may have subtabs. Each of these subtabs can
have subtabs can also have subtabs of their own, and so on.

The ADTab table builds the hierarchy of the tabs using the Tab Level and
Sequence Number fields like this:

  * The tab with level 0 is the header tab 
  * If the tab level of a tab is **tl** and its sequence number is **sn** , its parent tab will be the tab with tab level = **tl-1** whose sequence number is the highest of those tabs with sequence number < **sn** . 

This tree must be custom because:

  * The information to build the hierarchy is stored in the ADTab table, so there is no need to use ADTree 
  * The ADTab table does not have a column that points directly to the parent node of a record, so the LinkToParent tree structure is not suitable. 

This is the result:

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_a_Custom_Tree-2.png){: .legacy-image-style}

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_Create_a_Custom_Tree
"

This page has been accessed 6,120 times. This page was last modified on 23
January 2018, at 09:11. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

