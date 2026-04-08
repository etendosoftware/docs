---
title: Valued Stock Report
---

## Valued Stock Report

:material-menu: `Application` > `Warehouse Management` > `Analysis Tools` > `Valued Stock Report`

### **Overview**

The **Valued Stock Report** provides a comprehensive view of the inventory held in each warehouse along with its monetary value. It is an essential tool for understanding how much capital is tied up in stock, supporting key business processes such as:

- **Financial reporting**: Determining the total value of inventory for balance sheets and period-end closing.
- **Accounting reconciliation**: Comparing stock valuations against general ledger entries to identify discrepancies.
- **Cost analysis**: Evaluating unit costs across products and warehouses to support purchasing and pricing decisions.
- **Multi-warehouse visibility**: Reviewing stock values across multiple warehouses, either consolidated at the organization level or broken down by individual warehouse.

The valuation is calculated by summing the cost of every [material transaction](../transactions.md) for each product in the warehouse. Transaction costs are determined by the [Costing Server](../getting-started.md) process.

### **Parameters Window**

![Material Transaction Report](../../../../../assets/drive/1HGDsUBdSrfe3_Nzk_ojKq3Ck-aGvIAdx.png)

Before generating the report, configure the following parameters:

-   **Organization**: Select the organization to report on. Only organizations of type *Legal with Accounting* or *Generic* are available.
-   **Warehouse**: When a *Generic* organization is selected, all warehouses belonging to that organization are listed. When a *Legal with Accounting* organization is selected, no specific warehouse selection is available.
-   **Date**: The report displays inventory information up to and including this date.
-   **Consolidated Warehouse**: When checked, stock information is consolidated at the organization level. When unchecked, the report shows a breakdown by individual warehouse.
-   **Product Category**: Optionally filter the report to show only products belonging to a specific [category](../../master-data-management/product-setup.md#product-category).
-   **Currency**: Sets the [currency](../../general-setup/application/currency.md) in which all monetary values (such as cost and valuation) are displayed.

!!! warning
    A [conversion rate](../../general-setup/application/conversion-rates.md) to the selected report currency must be defined for the report to generate correctly. Verify that the appropriate currency conversion rates are configured before running the report.

### **Output Window**

![Material Transaction Report](../../../../../assets/drive/1btCDeLvHaczMWt9lE05E0J8RFjePTZFM.png)

The report output includes the following columns:

-   **Product**: The name of the product.
-   **Quantity**: The stock quantity of the product as of the selected date.
-   **Unit**: The unit of measure in which the stock quantity is expressed.
-   **Unit Cost**: The cost per individual unit. It is calculated by dividing the total valuation by the stock quantity.
-   **Valuation**: The total monetary value of the stock. It is calculated by adding the valuations of all material transactions that have occurred in the warehouse for that product.
-   **Actual Average/Standard Algorithm Cost**: The most recently calculated Average or Standard cost for the product.
-   **Actual Average/Standard Algorithm Valuation**: The stock valuation based on the current Average or Standard cost. It is calculated by multiplying the stock quantity by the current cost.

### **Improving Report Performance (Data Pre-Calculation)**

!!! note
    This step is **optional**. The Valued Stock Report works without it. However, if your report takes a long time to generate because your system has a large volume of transactions, enabling data pre-calculation can significantly reduce waiting times.

The system can summarize (pre-calculate) inventory data for each closed [accounting period](../../financial-management/accounting/setup/openclose-period-control.md) in advance, so the report does not have to process every individual transaction each time it runs. For this feature to work:

- Accounting periods must be defined in the [Fiscal Calendar](../../financial-management/accounting/setup/fiscal-calendar.md).
- At least some periods must be in *Closed* or *Permanently Closed* status.

!!! info
    To enable this feature, schedule the background process named *Generate Aggregated Data Background* through the [Process Request](../../general-setup/process-scheduling/process-request.md) window.

The pre-calculation covers all transactions up to the most recent closed period. Transactions occurring after that period are still calculated in real time. If there is a long span of open periods with many transactions, the report may still experience slower performance.

The image below shows the Process Request window configured to run the data pre-calculation process.

![Valued Stock Report - Process Request scheduling window](../../../../../assets/drive/1_mjP-Y6k-QGbCLm8FeIQI08YLJghMAfM.png)

!!! info
    It is recommended to schedule this process to run daily during a period of low system activity. The process only generates new pre-calculated data when an additional period has been closed or permanently closed since the last run.

#### **Limitations**

When the system pre-calculates data for a closed period, it combines all transactions in that period into a single summary. The original date of each individual transaction is not kept.

**What this means for multi-currency reports:** If you run the report in a currency different from your organization's base currency, the system converts the pre-calculated totals using the exchange rate on the period's closing date — not the exchange rate on the date each transaction originally occurred.

As a result, you may see small differences in currency values compared to running the report without pre-calculation enabled, where each transaction would be converted at its own date's exchange rate.

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
