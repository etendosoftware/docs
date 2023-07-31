---
title: Bulk Posting
---
## Bulk Posting 

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Financial Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558)

> **Important:**
!!! warning
    Before using this functionality, remember that this module's background process can affect the performance of the system.

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button. Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

This functionality is available in the following windows:
- [Amortization](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/financial-management-assets#bulk-posting) 
- [Goods Movements](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/warehouse-management#bulk-posting-1)
- [Financial Account](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/financial-management#bulk-posting-2)
- [Matched Invoices](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/procurement-management#bulk-posting-2)
- [Cost Adjustment](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/warehouse-management#bulk-posting-3)
- [Bill of Materials Production](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/warehouse-management#bulk-posting-2)
- [Internal Consumption](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/production-management#bulk-posting-1)
- [Doubtful Debt](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/financial-management#bulk-posting-3)
- [Landed Cost](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/procurement-management#bulk-posting-4)
- [G/L Journal](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/financial-management-accounting#bulk-posting-1)
- [Simple G/L Journal](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/financial-management-accounting#bulk-posting)
- [Work Effort](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/production-management#bulk-posting)
- [Goods Receipt](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/procurement-management#bulk-posting)
- [Goods Shipment](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/sales-management#bulk-posting)
- [Return Material Receipt](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/sales-management#bulk-posting-1)
- [Return to Vendor Shipment](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/procurement-management#bulk-posting-3)
- [Sales Invoice](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/sales-management#bulk-posting-2)
- [Purchase Invoice](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/procurement-management#bulk-posting-1)
- [Payment In](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/financial-management#bulk-posting-1)
- [Payment Out](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/financial-management#bulk-posting)
- [Physical Inventory](https://docs.etendo.software/en/end-user-documentation/etendo-environment/functional-documentation/business-management/warehouse-management#bulk-posting)


### Accounting Status

All the records existing previously to the installation of this new functionality have a default “pending refresh” value in the column Accounting Status. To set the correct value for this column, it is necessary to configure the following preference to indicate the amount of days to be considered by the process to set the correct values of the previous records.

#### Preference Configuration

To configure the preference, go to the “Preference” window and create a new record with the property “Days Back to Refresh Accounting” and the default value “90”. If necessary, it is possible to create another preference by entering a new value and checking the “selected” box.

#### Background Process

It is necessary to run the “Refresh Accounting Status” background process to update the accounting status column.

![](/docs.etendo.software/assets/drive/17KafE0qvtuAe21aVvs7mDN58V_BCDScO.png)


