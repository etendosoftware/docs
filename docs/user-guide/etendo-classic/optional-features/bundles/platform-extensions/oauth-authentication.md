---
tags: 
    - OAuth Authentication 
    - Provider
    - Bank statement
    - API OAuth URL
    - PSD2 Bank integration
---
# OAuth Authentication

## Overview

This section describes the OAuth Authentication module included in the Platform Extensions bundle.

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes/).


OAuth Authentication process facilitates the **type provider configuration** which allows users to **securely authenticate and authorize access** to their bank information using their preferred provider.

OAuth facilitates an authentication method through a security protocol for obtaining a token needed to make **API calls** to access specific resorces on behalf of their owner. This authentication will allow Etendo to get the necessary bank information to access the bank statements.

The functionality described in this section, is a complementary configuration section of the **PSD2 Bank Integration process**. So, before configuring the preferred bank type provider authentication from the OAuth Provider window, go to the [Financial Account window](../financial-extensions/psd2-bank-integration.md) to start the Functional process.


## OAuth Provider

Once in the OAuth Provider window in `application`> `oauth-provider`, it is necessary to add the user authentication URL in the **API OAuth URL field**. This URL is taken from the user’s bank provider. 

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/oauthprovider-0.png)

The other fields will be completed with data referring to the corresponding provider.


!!!info
        Once the necessary fields are configured in the OAuth Provider window, go back to the [PSD2 Bank Integration](../financial-extensions/psd2-bank-integration.md#get-token) section to continue with the bank statement generation process. 

