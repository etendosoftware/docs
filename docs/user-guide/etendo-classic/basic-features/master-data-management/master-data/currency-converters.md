---
title: Currency Converters
tags:
  - Master Data Management
  - Etendo Classic
  - Currency
  - Financial Extensions
  - Exchange Rates
  - Currency Conversion
---

# Currency Converters

:material-menu: `Application` > `Master Data Management` > `Currency Converters`

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Overview

The **Currency Converters** window is where you enter the credentials needed for Etendo to connect to an external service that provides daily exchange rates. Once set up, the system can download current rates automatically instead of requiring you to enter them manually. The [Conversion Rate Downloader](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rate-downloader.md) module uses this configuration to retrieve those rates.

This module supports different currency-conversion services. An API is a standardized connection that lets two software systems exchange data automatically. By default, it integrates with [APILayer – Currency Data API](https://marketplace.apilayer.com/currency_data-api?utm_source=apilayermarketplace&utm_medium=featured){target="_blank"}.

Each record in this window represents one API integration. Only the record with **Selected** set to **True** is active for the download process.

Exchange rates are used throughout Etendo whenever a transaction is recorded in a foreign currency. For example, when you create a purchase order or a sales invoice in a foreign currency, Etendo applies the current exchange rate to convert the amount into your company's base currency. The same conversion applies to financial reports. All figures appear in your company's base currency, no matter what currency was used in the original transaction. Keeping exchange rates up to date ensures that these conversions reflect real market values.

## Fields

<figure markdown="span">
  ![Currency Converters window showing the configuration fields for the APILayer Currency Data API integration](../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/currency-converters.png)
  <figcaption>Currency Converters window with an APILayer Currency Data API configuration.</figcaption>
</figure>

`Service Classname`
:   Pre-filled by the system. Do not change this value unless instructed by your system administrator.

`Client`
:   The company account in Etendo that this configuration belongs to. In most setups, this is filled in automatically when you log in.

`Organization`
:   The organizational unit within Etendo that can use this configuration. To make it available across all units in your company, enter `*`. To restrict access to a specific department or branch, select that organization from the list.

`Service Name`
:   Identifier for this configuration record, for example `Currency Data API`.

`Service URL`
:   Pre-filled by the system. Do not change this value unless instructed by your system administrator.

`Token`
:   Your API access key. To obtain it, register at [APILayer](https://marketplace.apilayer.com/){target="_blank"} and subscribe to the **Currency Data API**. Copy the token provided and paste it here.

`User` *(optional)*
:   Authentication username. Leave blank for the default APILayer configuration.

`Password` *(optional)*
:   Authentication password. Leave blank for the default APILayer configuration.

`Selected`
:   Set to **True** to use this configuration for the download process. Only one record can be selected at a time.

`Active`
:   Set to **True** to make this configuration available in the system.

## Full Setup Workflow

The Currency Converters window is one step in the overall exchange rate automation setup. For the complete configuration workflow, including how to schedule automatic downloads and define conversion rules, visit the [Conversion Rate Downloader](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rate-downloader.md) page.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
