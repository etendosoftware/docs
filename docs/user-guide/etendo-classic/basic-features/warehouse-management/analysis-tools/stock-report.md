---
title: Stock Report
---

## Stock Report

:material-menu: `Application` > `Warehouse Management` > `Analysis Tools` > `Stock Report`

### **Overview**

The Stock Report shows current stock levels for all products with inventory different from zero (including negative on-hand quantities). Data is grouped by product category, with each row displaying the product, warehouse, and storage bin location. This report provides quick visibility into how inventory is distributed across warehouses and bins.

Regularly reviewing the Stock Report helps maintain inventory accuracy and supports better purchasing decisions. By identifying products that are running low or accumulating beyond expected levels, users can take timely action to avoid stockouts that delay operations or overstock situations that tie up capital and warehouse space. This makes the report a practical tool for keeping inventory aligned with actual business demand.

### **Parameters Window**

The outcome of this report can be filtered by using the following parameters:

-   **Date**: Filters transactions up to the selected date.
-   **Product Category**: Limits the report to a specific product category.
-   **Product**: Filters the report to a specific product.
-   **Storage Bin**: Limits the report to a specific storage bin location.

![Stock Report](../../../../../assets/drive/1OgkmMsGjuADw-Sbqn1tfJ5WkCbq_AGx5.png)

The outcome of this report can be viewed in HTML, PDF, and Excel format.

### **Sample Report Output**

![Stock Report](../../../../../assets/drive/1jjN-TjQjeY-38odbT6xBRYCpACEmMUxz.png)

The report output includes the following columns:

-   **Article**: Name or code of the article.
-   **Quantity**: Current quantity on hand.
-   **Unit**: Unit of measure for the product.
-   **Attribute**: Product characteristics such as size, color, or lot number, if defined for the product.
-   **X**: Row position within the storage bin (horizontal location).
-   **Y**: Stack position within the storage bin (depth location).
-   **Z**: Level position within the storage bin (vertical location).
-   **Other**: Additional product information, if applicable.
-   **Warehouse**: Warehouse where the stock is located.

!!! info
    **X**, **Y**, **Z** columns in the report correspond to **Row (X)**, **Stack (Y)** and **Level (Z)** of the Storage Bin.

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
