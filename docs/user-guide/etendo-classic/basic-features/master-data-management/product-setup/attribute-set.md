---
title: Attribute Set
tags:
  - Master Data Management
  - Etendo Classic
  - Product
  - Attributes
  - Lot
  - Serial Number
---

## Attribute Set

:material-menu: `Application` > `Master Data Management` > `Product Setup` > `Attribute Set`

### Overview

An attribute set can be defined by a single attribute or by a set of attributes to apply to specific products.

If **an attribute set** includes among others **an attribute which is unique for each instance of the product**, for example, a lot number or a serial number, this window is the place to define which **Lot Number Sequence** or **Serial Number Sequence** must apply to get that unique attribute.

The steps to follow are:

- **Creation of the Lot Number Sequence/s**. To learn how, visit Lot Number Sequence
- **Creation of the Serial Number Sequence/s**. To learn how, visit Serial Number Sequence
- **Set up the relationship between** the previously created **Lot/Serial Number Sequence/s** and the **Attribute Set**, in the Attribute Set window.  
  To learn how, keep reading this section.

### Attribute Set

Attribute Set window allows creating as many combinations of attributes as required to define products with few or multiple characteristics.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/product-setup/attribute-set/attribute-set-1.png)

As shown in the image above, an attribute set to be assigned to a specific product/s can contain:

- a **Name** of the attribute Set
- a brief **Description** if needed
- a **Lot** or unique identifier given to a particular quantity of that product.  
  If **Lot flag is checked,** a new field named "**Lot Control**" is shown for you to select the Lot Number Sequence to follow by the products linked to that particular attribute set.
- a **Serial No** or a unique identifier given to each unit of the product.  
  If **Serial No flag is checked,** a new field named "**Serial No Control**" is shown for you to select the Serial Number Sequence to follow by the products linked to that particular attribute set.
- an **Expiration Date** or date upon which product quality is guaranteed.  
  If **Expiration Date flag is checked,** a new field named "**Guaranteed Days**" is shown for you to enter the number of days a product can be guaranteed.
- finally, the flag "**Require At Least One Value**" implies that at least one attribute set value will be required in product related transactions.

### Assigned Attribute

An attribute set can have a single or a set of attributes assigned.

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/product-setup/attribute-set/attribute-set-2.png)

As shown in the image above, an attribute set can have only one attribute, for example Color or as many attributes as required, for example Size, Lot Number and Serial Number.

The way to get that is just to select the previously created attributes in this tab.

You should take into account that:

- if one of the selected attributes is a "Lot" or a "Serial N?" type attribute, the corresponding Number Sequence must have been properly set up in the Attribute Set window.
