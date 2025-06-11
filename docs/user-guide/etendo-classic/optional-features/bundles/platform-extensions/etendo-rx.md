---
tags: 
    - oAuth Authentication 
    - Provider
    - Bank information
    - API oAuth URL
    - Etendo RX
---

# Etendo RX
:octicons-package-16: Javapackage: `com.etendoerp.etendorx`

## Overview

## SSO Etendo Login

Etendo allows you to authenticate using these external provider accounts: **Google**, **Microsoft**, **LinkedIn** **GitHub** and **Facebook**. This is possible due to the integration with the **EtendoAuth** middleware or Auth0 custom implementation.

### 1. Logging into Etendo Classic with an external provider

When accessing the Etendo Classic login screen, you’ll see buttons for the **available providers** to authenticate with.

- They are represented by their respective logos and names.
- These are the same providers available for linking.

    - Middleware  
        ![Etendo Login Middleware](Auth0DocImages/EtendoLoginMiddleware.png)

    - Auth0  
        ![Etendo Login Auth0](Auth0DocImages/EtendoLoginAuth0.png)

        Once you click on "Login with external providers", you’ll need to choose the provider you've configured:  
            ![Login Auth0](Auth0DocImages/LoginAuth0.png)


## 2. First login attempt with an external provider

If it’s the **first time** you're using one of these providers, you’ll see a message like:

>  No User linked - You need to log in with an Etendo Classic user and then, link the SSO account.

![No User Link](Auth0DocImages/NoUserLink.png)

This means that you haven’t yet linked your Etendo Classic account with your external provider account.


## 3. How to link your Etendo Classic account with an external account

1. Log into Etendo Classic as usual with your **username and password**.  
2. Go to your **user profile** (icon in the upper left corner).  
3. You’ll see a section called **"Link user with"**.  
4. Click on the provider you want to link.

    - Middleware  
        ![Link User With Middleware](Auth0DocImages/LinkUserWithMiddleware.png)

    - Auth0  
        ![Link User With Auth0](Auth0DocImages/LinkUserWithAuth0.png)


## 4. Logging in with an external provider

When selecting a provider:

- The **provider’s login screen** will open (Google, Microsoft, etc.).
- Log in with your personal or corporate account.
- Once authenticated, Etendo Classic will automatically link your user account with that external account.

## 5. Future logins with an external account

Next time you log into Etendo Classic:

- Click on the **provider’s button** on the login screen.
- If it’s already linked, you’ll be logged in automatically **without needing your Etendo Classic username and password**.


## 6. Logging out (Complete logout)

When you log out from the Etendo Classic:

1. Your internal Etendo Classic session will be closed.  
2. The Etendo Classic will communicate with the **EtendoAuth middleware**.  
3. The session with the external provider will be closed automatically.  
4. A small **popup will appear for a few seconds** confirming the external logout.


## Additional Notes

- You can link multiple providers to the same user.
- Authentication is securely managed via Auth0.