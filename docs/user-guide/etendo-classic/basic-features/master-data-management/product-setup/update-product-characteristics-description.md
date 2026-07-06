---
title: Update Product Characteristics Description
tags:
  - Master Data Management
  - Etendo Classic
  - Product
  - Product Characteristic
---

## Update Product Characteristics Description

:material-menu: `Application` > `Master Data Management` > `Product Setup` > `Update Product Characteristics Description`

### Overview

Every variant has its product _Characteristic Description_ and this field is calculated automatically when:

- Variants are created
- When the value of a characteristic is change, for example from _Blue_ to _Hard Blue_

For example, if the characteristics of a variant are Color and Size and the values are Blue and XL the result of the description would be: _Color: Blue, Size: XL_

If later on you change Blue for Hard Blue, the new description would be _Color: Hard Blue, Size: XL_

In all of these scenarios, the _Characteristic Description_ is updated without the need of coming to this process.

This process should be used just in some special cases:

- When the name of the Characteristic is changed, for example from Color to Tint
- When through the database characteristics or values are changed
