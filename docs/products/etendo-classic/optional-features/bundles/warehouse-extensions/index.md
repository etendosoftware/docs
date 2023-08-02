---
title: Warehouse Extensions Bundle
---

**This bundle includes enhancements for the Warehouse Management functionalities in Etendo.**

The Warehouse Extensions bundle includes the following modules:


## Stock History

It provides updated information about the daily history stock of the products. 

!!! info
    For more information visit [Functional documentation](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-management/warehouse-reports#stock-history) and [Technical documentation](https://docs/en/technical-documentation/bundles/warehouse-extensions-bundle)

## Reactivate Warehouse Documents
<iframe width="560" height="315" src="https://www.youtube.com/embed/ghH3tBjoN9c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This functionality is part of the Warehouse Extensions Bundle and it is useful when the user needs to reactivate documents such as Goods Movements, Goods Receipts, Goods Shipments and Physical Inventories. 

!!! info
        For more information, visit Functional Documentation about:
        - [Goods Movements](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-management/warehouse-management#how-to-reactivate-goods-movements)
        - [Goods Receipts](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-management/procurement-management#how-to-reactivate-goods-receipts)
        - [Goods Shipments](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-management/sales-management#how-to-reactivate-goods-shipments)
        - [Physical Inventory](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-management/warehouse-management#how-to-reactivate-physical-inventories)

## Uninstall bundle

To uninstall the bundle and prevent future problems with orphan records, a sequence of steps must be followed:

1. Run the following query in the environment's database
```
DELETE FROM OBUIAPP_GC_TAB 
WHERE AD_TAB_ID = 'C3DB551F2BCA40A79AAF21DBD6D06309';
```

2. After the query successfully finishes, delete the bundle by the way corresponding to the installation method (Sources/JARs)