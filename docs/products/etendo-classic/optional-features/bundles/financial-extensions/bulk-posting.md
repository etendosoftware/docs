---
title: Bulk Posting
hide:
    - navigation
---

## **Introduction**

This section describes the Bulk Posting module included in the Etendo Financial Extensions bundle.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mgE-NnDLlA0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

!!! warning
    Before using this functionality, remember that this module's background process can affect the performance of the system.

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button. Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

This functionality is available in the following windows:

- [Amortization](/products/etendo-classic/user-guide/financial-management/assets/overview/#bulk-posting)
- [Goods Movements](/products/etendo-classic/user-guide/warehouse-management/transactions/#bulk-posting_1)
- [Financial Account](/products/etendo-classic/user-guide/financial-management/receivables-and-payables/transactions/#bulk-posting_2)
- [Matched Invoices](/products/etendo-classic/user-guide/procurement-management/transactions/#bulk-posting_2)
- [Cost Adjustment](/products/etendo-classic/user-guide/warehouse-management/transactions/#bulk-posting_3)
- [Bill of Materials Production](/products/etendo-classic/user-guide/warehouse-management/transactions/#bulk-posting_2)
- [Internal Consumption](/products/etendo-classic/user-guide/production-management/transactions/#bulk-posting_1)
- [Doubtful Debt](/products/etendo-classic/user-guide/financial-management/receivables-and-payables/transactions/#bulk-posting_3)
- [Landed Cost](/products/etendo-classic/user-guide/procurement-management/transactions/#bulk-posting_4)
- [G/L Journal](/products/etendo-classic/user-guide/financial-management/accounting/transactions/#bulk-posting_1)
- [Simple G/L Journal](/products/etendo-classic/user-guide/financial-management/accounting/transactions/#bulk-posting)
- [Work Effort](/products/etendo-classic/user-guide/production-management/transactions/#bulk-posting)
- [Goods Receipt](/products/etendo-classic/user-guide/procurement-management/transactions/#bulk-posting)
- [Goods Shipment](/products/etendo-classic/user-guide/sales-management/transactions/#bulk-posting)
- [Return Material Receipt](/products/etendo-classic/user-guide/sales-management/transactions/#bulk-posting_1)
- [Return to Vendor Shipment](/products/etendo-classic/user-guide/procurement-management/transactions/#bulk-posting_3)
- [Sales Invoice](/products/etendo-classic/user-guide/sales-management/transactions/#bulk-posting_2)
- [Purchase Invoice](/products/etendo-classic/user-guide/procurement-management/transactions/#bulk-posting_1)
- [Payment In](/products/etendo-classic/user-guide/financial-management/receivables-and-payables/transactions/#bulk-posting_1)
- [Payment Out](/products/etendo-classic/user-guide/financial-management/receivables-and-payables/transactions/#bulk-posting)
- [Physical Inventory](/products/etendo-classic/user-guide/warehouse-management/transactions/#bulk-posting)


### Accounting Status

All the records existing previously to the installation of this new functionality have a default “pending refresh” value in the column Accounting Status. To set the correct value for this column, it is necessary to configure the following preference to indicate the amount of days to be considered by the process to set the correct values of the previous records.

#### Preference Configuration

To configure the preference, go to the “Preference” window and create a new record with the property “Days Back to Refresh Accounting” and the default value “90”. If necessary, it is possible to create another preference by entering a new value and checking the “selected” box.

#### Background Process

It is necessary to run the “Refresh Accounting Status” background process to update the accounting status column.

![](/assets/drive/17KafE0qvtuAe21aVvs7mDN58V_BCDScO.png)