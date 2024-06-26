---
tags:
  - multi selector
  - standard process
  - Etendo Classic
---

#  How to Create a Multi Selector
  
##  Overview

**Multi Selector** is a reference that allows to select multiple items at the same time. It is intended to be used as parameter of [Standard Process Definition](../how-to-guides/how-to-create-a-standard-process-definition.md) and it is defined as regular selectors (which allow to select a single value). 

##  Example Module

This section is supported by an example module which shows examples of the code shown and discussed.

The code of the example module can be downloaded here.

##  Steps to Implement the Process

This section explains how to create a Multi Order selector.

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Multi_Selector-1.png)

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Multi_Selector-2.png)

###  Defining the Selector

  1. As **System Administrator**, open the **Reference** window. 
  2. Create a new record. 
    * Name: Multi Order Selector 
    * Parent Reference: `OBUISEL_Multi` Selector Reference 
  3. In **Defined Selector** tab, set the properties for the selector: 
    * Template: Selector Template 
    * Table: `C_Order` 

###  Adding Fields to Selector's Pop Up

The last step is to define which are the fields that will be present in the popup to select records.

  1. Go to **Defined Selector Field** tab 
  2. Create records: 
    * Name: it is the name the user will see (i.e. Business Partner) 
    * Property: actual property to retrieve information from (i.e. businessPartner) 
    * Sorting of columns in the grid: Position of this column in the grid (i.e. 20) 

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Multi_Selector-3.png)

###  Using the Selector

This selector can be used as parameter for a Process Definition. It is used in [this section](../how-to-guides/how-to-create-a-standard-process-definition.md#adding-parameters).

###  Retrieving Values in Backend

In backend, the Java implementing the process receives a `JSONArray` with the IDs of all selected rows. In case no row is selected, an empty array is received.
    
     
    //...
    JSONArray orders = params.getJSONArray("orders"); // get the array
    

    // iterate it
    for (int i = 0; i < orders.length(); i++) {
        // ...
    }

## Using custom query selector

When using a custom query to define the selector, there must be an alias in the query named `_identifier` which will be used as user readable identifier for the selected records and another one named `id` which will be sent to backend as id of the selected records. Fields for these query columns with the same names are also required.

!!!important
    Multi Selectors can only be used as parameters in **Standard Process Definition**, they cannot be included in **Standard Windows**.

---

This work is a derivative of [How to Create a Multi Selector](http://wiki.openbravo.com/wiki/How_to_create_a_Multi_Selector){target="\_blank"} by [Openbravo Wiki](https://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.