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

OAuth facilitates an authentication method through a security protocol for obtaining a token needed to give consent to the bank. This authentication will allow Etendo to get the necessary bank information to access the bank statements.

The functionality described in this section, is a complementary configuration section of the **PSD2 Bank Integration process**. So, before configuring the preferred bank type provider authentication from the OAuth Provider window, go to the [Financial Account window](../financial-extensions/psd2-bank-integration.md) to start the Functional process.


## OAuth Provider

Once in the OAuth Provider window in `application`> `oauth-provider`, there are some necessary fields to configure: 

- **API OAuth URL**: the URL to add in this field corresponds to the user authentication.

- **API Resource URL field in Bank Integration PSD2 section**: add the URL from where the user will get the data after the authentication process. 

!!!info
        Both URLs are taken from the user’s bank provider.


- **Provider Type**: Choose the preferred provider type from where the token will be generated and the consent given to get the bank statement information needed. 

![alt text](<../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/oauthprovider-0 .png>)




