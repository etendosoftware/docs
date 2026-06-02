---
title: Currency Converters
tags:
  - Master Data Management
  - Etendo
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

The **Currency Converters** window is where you enter the access details (such as a URL and API key) that Etendo needs to connect to an external service that provides daily exchange rates. Once set up, the system can download current rates automatically instead of requiring you to enter them manually. The [Conversion Rate Downloader](../../../optional-features/bundles/financial-extensions/conversion-rate-downloader.md) module uses this configuration to retrieve those rates.


<figure markdown="span">
  ![Currency Converters window showing the configuration fields for the APILayer Currency Data API integration](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/currency-converters.png)
  <figcaption>Currency Converters window with an APILayer Currency Data API configuration.</figcaption>
</figure>


!!! info 
    The Currency Converters window is one step in the overall exchange rate automation setup. For the complete configuration workflow, including how to schedule automatic downloads and define conversion rules, visit the [Conversion Rate Downloader](../../../optional-features/bundles/financial-extensions/conversion-rate-downloader.md) page.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
