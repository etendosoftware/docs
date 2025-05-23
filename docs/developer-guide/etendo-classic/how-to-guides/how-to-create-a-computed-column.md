---
title: How to Create a Computed Column
tags:
  - How to
  - Computed column
  - SQL logic
  - Etendo classic
---

# How to Create a Computed Column

## Overview

A computed column is a column of a table which is computed using an _SQL_ expression and which does not exist explicitly in the database schema.

Computed columns have these characteristics:

  * Computed when a record is read from the database.
  * Not persisted, there is no real column in the database schema for a computed column.
  * Is computed using an SQL expression which can use columns from the application dictionary table definition in which the column is defined.
  * Can be used in the definition of a field (in the same way as a 'normal' column), it is sortable and filterable but not editable.

## Example Module

This section is supported by an example module which shows examples of the code shown and discussed.

The code of the example module can be downloaded from this repository: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

!!!Note
    The example module also contains implementations of other guides.

## Defining a Computed Column

Defining a computed column is simple.

1. Go to the **Tables and Columns** window.
2. Go to the table in which you want to add the computed column.
3. Then, in the column child tab, create a new column and set the sqllogic field.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-1.png)


The sqlLogic field must be an SQL expression:

  * If it is a select sql expression, then all the tables in the from clause need to use an alias.
  * You can refer to other columns of the table using their non-aliased name.

This is an example of the total line quantity column shown above:

```hql
(SELECT sum(ol.qtyOrdered) FROM c_orderline ol WHERE ol.c_order_id=c_order_id)
```

What you can see is that the from clause uses an aliased table, the `c_order_id` at the end is the non-aliased column of the main table.

!!!Note
    * A computed column can be used in the definition of a field for an Etendo column, just like every other column.
    * A computed column that uses a _String reference_ should have a length greater than zero. Because this is the number of characters which are going to be displayed in form view.
    * The field is always read-only, it is recomputed/set automatically when updating or inserting a record.
    * Filtering and sorting on computed columns/fields is possible.

## Use case: show totals on a header

In the 'Defining a computed column' section an example sql expression was shown. The above example computes the sum of the quantities of a line. You can add a computed column as a field to a tab/window:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-2.png)

and display it in the grid:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-3.png)

or the form:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-4.png)

## Performance Implications

### Filtering and Sorting

When computed columns are used to filter or sort the grid, their value needs to be computed for all existing rows before any pagination limit can be applied, this can have a very important impact in terms of performance.

In general, when defining computed columns, they should be made not filterable nor sortable. The only exception to this rule is when it is guaranteed the number of records in the table they are created for is going to be always reduced or it will always be displayed as a subtab, where the number of rows per parent record cannot be big.

### Lazy Evaluation

Computed columns are lazily evaluated. This means their query is not executed when the entity they are defined in is retrieved but when one of them is accessed.

For example, **Delivery Status** is a computed column of **Order** entity:

```java
// load one order
OBCriteria<Order> qOrder = OBDal.getInstance().createCriteria(Order.class);
qOrder.setMaxResults(1);
Order order = qOrder.list().get(0);
```

The code above loads an order, at this stage **Delivery Status** is not already computed meaning the SQL has not been executed in database.

If afterwards we have this code:

```java
// load computed columns
System.out.println(order.getDeliveryStatus());
``` 

is at this point when the computed column query is executed in database and **Delivery Status** property takes value.

!!!Note
    In case there are many computed columns in the same entity, they are evaluated all together when the first one is calculated.

#### Limitations

In order to make computed columns lazy, they are mapped in their entity as a `many-to-one` property (named `computedColumns`) linked to a virtual entity, is this virtual entity where the actual computed columns are located as hibernate formula properties.

![](../../../assets/developer-guide/etendo-classic/how-to- guides/How_to_create_a_Computed_Column-6.png)

This extra complexity is transparent when working with generated _DAL_ Java classes, as seen before, `order.getDeliveryStatus()` populates the value of the computed column, though behind the scenes it is retrieving it from the virtual entity.

But this model imposes also some limitations to be taken into account when manipulating computed columns in filters or sorting.

!!!Note
    When using computed columns in HQL to do filtering or sorting, they are evaluated. This needs to be done carefully (or even avoided if possible) because it might have performance implications.

When working with HQL (i.e. `OBQuery`), computed columns cannot be directly accessed as they are not properties of the entity.

---
This work is a derivative of [How to Create a Computed Column](http://wiki.openbravo.com/wiki/How_to_create_a_Computed_Column){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.