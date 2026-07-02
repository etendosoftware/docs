---
title: Service Price Rule
tags:
  - Master Data Management
  - Etendo Classic
  - Pricing
  - Service Price Rule
---

## Service Price Rule

:material-menu: `Application` > `Master Data Management` > `Picing` > `Service Price Rule`

### Overview

In this window Price Rules assigned to Price Rule Based services will be configured. Instead of having a fixed price, there will be rules that will determine the price of the Service.

### Service Price Rule

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/service-price-rule/service-price-rule-1.png)

Configuration fields:

- **Name**: Name of the Service Price Rule.
- **Description**: Description of the Service Price Rule.
- **Rule Type**: There are two values to select in the dropdown
  - Percentage: If selected, a Percentage field will be displayed allowing to set a Percentage. To determine the price of the service, this amount will be applied to the amount of the lines related to the service.
    - **Percentage**: Percentage to be applied.
    - **After Discounts**: If selected, the percentage will be applied after adding the discounts to the ticket.
  - **Ranges**: If selected, a new tab Ranges will be displayed allowing to create different Ranges based on the amount of the related lines.

### Ranges

![](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/service-price-rule/service-price-rule-2.png)

In this tab, different Ranges can be created based on the amount of the related order lines. Configuration fields:

- **Amount Up To**: If the summed amount of related order lines is equal or less than this amount, the configuration of this range will be taken into account.
- **Rule Type**: There are two values to select in the dropdown
  - Percentage: If selected, a Percentage field will be displayed allowing to set a Percentage. To determine the price of the service, this amount will be applied to the amount of the lines related to the service.
    - **Percentage**: Percentage to be applied.
    - **After Discounts**: If selected, the percentage will be applied after adding the discounts to the ticket.
  - **Fixed Price**: If selected, a field 'Price List' will be displayed.
    - **Price List**: Price List from which the price of the service will be obtained.

---

This work is a derivative of [Master Data Management](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
