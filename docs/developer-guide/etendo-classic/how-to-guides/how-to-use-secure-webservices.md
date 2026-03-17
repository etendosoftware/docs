---
tags:
  - How to
  - Swagger
  - Secure Web Services
  - Secure Webservices
  - Web Services
---

# How to Use Secure Web Services

## Overview

This module allows calling any standard **Etendo web service** in the same way as calling the `/ws` endpoint, but using token authentication.

This authentication method also allows defining the context for the calls by choosing the role and or organization when requesting a token. It is also possible to renew a token to refresh the expiration date or change the role/organization.

Besides the authentication implementation, the module includes utilities for developers and useful web services, such as jsonDal (to access the OB Data Access Layer with json).

## Setup

!!! Warning
    A valid domain name and `SSL/TLS` certificate are required to use **Secure Web Services**. Please install a certificate or contact your administrator to avoid runtime errors when generating tokens in server instances.

!!! Info
    By default, the **ES256 encryption algorithm** is used. To switch to a legacy algorithm, create a preference with the property `Encryption Algorithm` and set its value to `HS256`.

### Token Configuration

:material-menu: `Application` > `General Setup` > `Client` > `Client`

In the **Secure Web Service Configuration** tab, the *System Administrator* can manage the SWS key and configure token expiration.

Starting from **Etendo 26.1**, the key is automatically generated during `./gradlew install` — no manual action is required for new installations. For earlier versions or to rotate the key, use one of the following methods:

1. **From the command line:**

    ```bash
    ./gradlew generate.sws.keys
    ```

2. **From the UI:** Open the **Secure Web Service Configuration** tab and click **Generate Key**.

!!! warning
    Both methods **overwrite the existing SWS key**. All tokens signed with the previous key are immediately invalidated.

The **Token expiration** field controls how long tokens remain valid, expressed in **minutes** (`0` = no expiration).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)

!!! warning "Security recommendation"
    Non-expiring tokens pose a risk in production — a compromised token remains valid indefinitely. Set a reasonable expiration time and rotate tokens periodically.

## Secure Web Services Swagger

!!! info
    For more information, visit [Secure Web Services Swagger](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/#/Login/post_sws_login){target="_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
