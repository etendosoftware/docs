---
title: Currency Converters
tags:
  - Master Data Management
  - Etendo Classic
  - Currency
  - Financial Extensions
  - Bank Account Management
---

# Currency Converters

:material-menu: `Application` > `Master Data Management` > `Currency Converters`

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Overview

The **Currency Converters** window stores the connection configuration for external currency rate APIs. The [Conversion Rate Downloader](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rate-downloader.md) module reads this configuration to connect to an external API and automatically retrieve exchange rates.

This module supports different currency-conversion APIs. By default, it integrates with [APILayer – Currency Data API](https://marketplace.apilayer.com/currency_data-api?utm_source=apilayermarketplace&utm_medium=featured){target="_blank"}.

Each record in this window represents one API integration. Only the record with **Selected** set to **True** is active for the download process.

## Fields

<figure markdown="span">
  ![Currency Converters window showing the configuration fields for the APILayer Currency Data API integration](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/currency-converters.png)
  <figcaption>Currency Converters window with an APILayer Currency Data API configuration.</figcaption>
</figure>

`Service Classname`
:   Java class that handles the connection to the API. The default value for the APILayer integration is `com.smf.currency.apiconfig.CurrencyLayerConverter`.

`Client`
:   Client allowed to use this configuration.

`Organization`
:   Organization allowed to use this configuration. Enter `*` to allow all organizations.

`Service Name`
:   Identifier for this configuration record, for example `Currency Data API`.

`Service URL`
:   API endpoint used to retrieve exchange rate data. The default value for the APILayer integration is `https://api.apilayer.com/currency_data/`.

`Token`
:   Access token obtained from the API provider. Register at [APILayer](https://marketplace.apilayer.com/){target="_blank"} and subscribe to the **Currency Data API** to generate a token. The free plan provides 100 monthly requests, which is sufficient for multiple daily updates.

`User` *(optional)*
:   Authentication username. Not required for the default APILayer configuration.

`Password` *(optional)*
:   Authentication password. Not required for the default APILayer configuration.

`Selected`
:   Indicates which configuration the Conversion Rate Downloader uses. Set to **True** to activate this configuration for the download process. Only one record is active at a time.

`Active`
:   Controls whether this record is available in the system. Set to **True** to make the configuration available.

## Full Setup Workflow

The Currency Converters window is one step in the overall exchange rate automation setup. For the complete configuration workflow, including how to schedule automatic downloads and define conversion rules, visit the [Conversion Rate Downloader](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rate-downloader.md) page.

## Related Windows

- [Currency](../../../../../user-guide/etendo-classic/basic-features/general-setup/application/currency.md) — Define the currencies available in the system.
- [Conversion Rates](../../../../../user-guide/etendo-classic/basic-features/general-setup/application/conversion-rates.md) — View and manage the exchange rates retrieved by the downloader.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
