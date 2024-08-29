---
tags: 
 - Etendo Mobile
 - Apps
 - Sub-apps
 - Etendo Classic
---

![alt text](../../assets/user-guide/etendo-mobile/getting-started/cover-getting-started-mobile.png)

# Etendo Mobile

## Overview

Etendo Mobile is a **mobile app** in which the user can access to sub-applications via mobile devices in a fast and practical way. By enabling seamless integration between Etendo Classic and mobile sub-applications, Etendo Mobile allows users to log in to Etendo Classic and configure **dynamic applications** tailored to specific user roles, enhancing productivity and efficiency.

!!!info
    To be able to access to the sub-applications, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes/).


Etendo Mobile is available in both Play and App Store:

=== ":simple-homeassistantcommunitystore: Play store"

    The app is available in Play Store and the download site can be accessed through [_Download the App here._](https://play.google.com/store/apps/details?id=com.smf.mobile.etendo_app_loader){target=_blank}

    ![](../../assets/user-guide/etendo-mobile/user-interface/EtendoPlayStore.png)

=== ":simple-appstore: App Store "

    The app is available in App Store and the download site can be accessed through [_Download the App here._](https://apps.apple.com/us/app/etendo/id6451114033){target=_blank}

    <a href="https://apps.apple.com/us/app/etendo/id6451114033" target="_blank"><img src="/assets/user-guide/etendo-mobile/user-interface/EtendoAppStore.png" alt="EtendoAppStore.png"></a>
    

## Initial Configuration

In order to use the app, the user must access Etendo Classic in `Client>Secure Web Service Configuration` since the app uses Secure Web Services to authentizate itself. So, as the System Administrator role, generate a token by clicking on the **generate key** button, this token is usedto start the session in the app.

![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-0.png)

## Server URL

Once the app is downloaded, the first step will be setting up the **Etendo server URL**.

For this, the gear icon shown in the welcome window allows the user to enter the configuration window. In Settings, click the Add new Link button, enter the URL and click **Add new Link** again.

![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-1.jpg)

!!!info
    In the Add new link field, it is possible to add other URLs to connect the app from different servers. It is also possible to modify or remove URLs.

## Log In

Once the server URL is configured, the user must log in entering **the user and the password** assigned by the system administrator.

The user will remain logged in, the system will require reentering the credentials only in case the session is ended (through the option Log out in the navigation menu) or the server URL is changed.

![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-2.jpg)

!!!info
    Etendo Mobile offers the possibility to connect to a demo server to test the app. In this case, the **demo try** button must be pressed so the user can enter the app without credential requirements.

## Dynamic App Role Configuration


