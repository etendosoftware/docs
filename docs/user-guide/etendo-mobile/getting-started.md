---
title: User Guide - Etendo Mobile - Getting Started
tags:
    - Etendo Mobile
    - Mobile Apps
    - Dynamic Sub-apps
    - Configuration
    - App Integration
---

![alt text](../../assets/user-guide/etendo-mobile/getting-started/cover-getting-started-mobile.png)

# User Guide - Etendo Mobile - Getting Started

## Overview

Etendo Mobile is a **mobile app** in which the user can access to sub-applications via mobile devices in a fast and practical way. By enabling seamless integration between Etendo Classic and mobile sub-applications, Etendo Mobile allows users to log in to Etendo Classic and configure **dynamic applications** tailored to specific user roles, enhancing productivity and efficiency.


Etendo Mobile is available in both Play and App Store:

=== ":simple-homeassistantcommunitystore: Play store"

    The app is available in Play Store and the download site can be accessed through [_Download the App here._](https://play.google.com/store/apps/details?id=com.smf.mobile.etendo_app_loader){target=_blank}

    ![](../../assets/user-guide/etendo-mobile/user-interface/EtendoPlayStore.png)

=== ":simple-appstore: App Store "

    The app is available in App Store and the download site can be accessed through [_Download the App here._](https://apps.apple.com/us/app/etendo/id6451114033){target=_blank}

    <a href="https://apps.apple.com/us/app/etendo/id6451114033" target="_blank"><img src="/assets/user-guide/etendo-mobile/user-interface/EtendoAppStore.png" alt="EtendoAppStore.png"></a>
    

## Initial Configuration
:material-menu: `Application` > `General Setup` > `Client` > `Client`

In order to use the Etendo Mobile app, the user must access Etendo Classic as `System Administrator` role in `Client`>`Secure Web Service Configuration` since the app uses Secure Web Services to authentizate itself and generate a token by clicking on the **Generate Key** button, this token is used to start the session in the app.

![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-0.png)

## Server URL

![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-1.jpg){ width="250" align="right" }

Once the app is downloaded, the first step will be setting up the **Etendo server URL**.

For this, the gear icon shown in the welcome window allows the user to enter the configuration window. In Settings, click the Add new Link button, enter the URL and click **Add new Link** again.


!!!info
    In the Add new link field, it is possible to add other URLs to connect the app from different servers. It is also possible to modify or remove URLs.


<br>
<br>
<br>
<br>

## Log In


![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-2.jpg){ width="250" align="left" }

Once the server URL is configured, the user must log in entering **the user and the password** assigned by the system administrator.

!!!info
    The user will enter with their default **Role, Organization, Client and Warehouse** setup.

!!!note
    The user will remain logged in unless the session is ended through Log out option.  

!!!info
    Etendo Mobile offers the possibility to connect to a demo server to test the app. In this case, the **Demo Try** button must be pressed so the user can enter the app without credential requirements.


## Sub-Applications Distributed by Etendo


### Mobile Extensions bundle

- [Etendo Classic Subapp](./bundles/mobile-extensions/etendo-classic-subapp.md) 
- [Documents Manager Subapp](./bundles/mobile-extensions/overview.md)

### Copilot Extensions bundle

- [Etendo Copilot Subapp](../etendo-copilot/bundles/overview.md#etendo-copilot-subapp) 

!!! info
    In order to be able to configure the dynamic sub-applications, it is necessary to install the corresponding bundle. [Mobile Extensions](https://marketplace.etendo.cloud/#/product-details?module=55A7EF64F7FA43449B249DA7F8E14589){target="\_blank"} bundle or [Copilot Extensions](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"} bundle

## Role Configuration - Dynamic App 

:material-menu: `Application` > `General Setup` > `Security` > `Role`

Etendo Mobile allows the creation and configuration of mobile sub-applications. 

Once the sub-application bundle is installed, go to the **Role window** and create a configuration register in the **Dynamic Apps** tab for each sub-app to be configured. This action sets the access to the sub-applications according to the role.  

Fields to note:

- **App:** This dropdown displays the available applications based on the installed modules. Selecting an application grants access to that application for the role.
- **Version:** Assign the version of the application to be used in this role.
- **Active:** Select if this application is active or not.

![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-3.png)



## Share Files

![](../../assets/user-guide/etendo-mobile/getting-started/share-files.gif){ width="250" align="right" }

Etendo mobile allows **receiving files** from external applications and being used by sub-applications.  

- The [Documents Manager Subapp](./bundles/mobile-extensions/overview.md#documents-manager-subapp) is a sample implementation capable of receiving external files and rendering them within Etendo Mobile. 
- The [Etendo Copilot Subapp](../etendo-copilot/bundles/overview.md#etendo-copilot-subapp), able to receive any external file as input and in one simple step be processed by the agents.

!!! warning
    The file sharing functionality enables the files for any sub-application and then displays a selector capable of opening the corresponding sub-application.

!!! info
    For more technical information visit [Create New Sub-application](../../developer-guide/etendo-mobile/tutorials/create-new-subapplication.md) guide


