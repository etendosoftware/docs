---
title: Warehouse Extensions Bundle
---

**This bundle includes enhancements for the Warehouse Management functionalities in Etendo.**

The Warehouse Extensions bundle includes the following modules:

## Modules

### Stock History

It provides updated information about the daily history stock of the products. 

!!! info
    For more information, visit [the Stock History user guide](/docs/products/etendo-classic/user-guide/warehouse-management/analysis-tools#stock-history) and [the Stock History developer guide](/docs/developer-guide/etendo-classic/bundles/warehouse-extensions-bundle#stock-history).

### Reactivate Warehouse Documents
<iframe width="560" height="315" src="https://www.youtube.com/embed/ghH3tBjoN9c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality is part of the Warehouse Extensions Bundle and it is useful when the user needs to reactivate documents such as Goods Movements, Goods Receipts, Goods Shipments and Physical Inventories. 

!!! info
        For more information, visit:

        - [Goods Movements](/docs/products/etendo-classic/user-guide/warehouse-management/transactions#how-to-reactivate-goods-movements)
        - [Goods Receipts](/docs/products/etendo-classic/user-guide/procurement-management/transactions#how-to-reactivate-goods-receipts)
        - [Goods Shipments](/docs/products/etendo-classic/user-guide/sales-management/transactions#how-to-reactivate-goods-shipments)
        - [Physical Inventory](/docs/products/etendo-classic/user-guide/warehouse-management/transactions#how-to-reactivate-physical-inventories)

### Uninstall bundle

To uninstall the bundle and prevent future problems with orphan records, a sequence of steps must be followed:

1. Run the following query in the environment's database
```
DELETE FROM OBUIAPP_GC_TAB 
WHERE AD_TAB_ID = 'C3DB551F2BCA40A79AAF21DBD6D06309';
```

2. After the query successfully finishes, delete the bundle by the way corresponding to the installation method (Sources/JARs)

## Translations

### Spanish [Warehouse Extensions ES](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}