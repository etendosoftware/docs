---
tags:
  - Etendo RX
  - oAuth
  - SSO Login
  - Middleware
---

# Etendo RX 
:octicons-package-16: Javapackage: `com.etendoerp.etendorx`

## oAuth Provider

This section describes the oAuth Authentication module included in the Platform Extensions bundle.

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes/).


oAuth Authentication process facilitates the **provider type configuration** which allows users to **securely authenticate and authorize access** to their information using their preferred provider.

oAuth facilitates an authentication method through a security protocol for obtaining a token needed to make **API calls** to access specific resources on behalf of their owner. This authentication will allow Etendo to get the necessary information to access to third party applications. 

### oAuth Provider Window

In the oAuth Provider window in :material-menu: `Application`> `Etendo RX`> `oAuth Provider`, set the preferred type provider by adding the user authentication URL in the **API oAuth URL field**. This URL can be found in the provider documentation API.  

The other fields will be completed with data referring to the corresponding provider.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/oauthprovider-1.png)


## Etendo SSO Login

### Set up Etendo to Login with External Providers

To enable login to **Etendo Classic** using external providers (Google, Microsoft, LinkedIn, GitHub or Facebook), you need to perform two main steps:

1. **Enable the SSO (Single Sign-On) feature through a system preference**
2. **Configure the connection settings in `gradle.properties`**

For the authentication class, you need to add:

``` title="gradle.properties"
authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
```

Depending on whether you're using **EtendoAuth Middleware** or **Auth0 directly**, the configuration will vary slightly.

### 1. Enable the SSO Login Preference

1. Log in as **System Administrator**
2. Go to the **Preferences** window
3. Create a new preference with the following settings:

   - **Property**: `Allow SSO Login`  
   - **Selected**: Yes  
   - **Value**: `Y`

   ![SSO Preference](Auth0DocImages/NewSSOPreference.png)

### 2. Configure EtendoAuth Middleware Integration

To authenticate via the **EtendoAuth Middleware**, follow these steps:

1. Open the `gradle.properties` file
2. Add the following properties:

  ```properties
  sso.auth.type=Middleware
  sso.middleware.url=https://sso.etendo.cloud
  sso.middleware.redirectUri=http://localhost:8080/oauth/secureApp/LoginHandler.html
  ```

With these settings, Etendo Classic will be able to authenticate users through external login providers using the middleware.


#### Warning: Potential SSO Configuration Mismatch
  
  In certain cases, a mismatch may occur in the Single Sign-On (SSO) configuration. For example, the SSO preference might be created, but the corresponding SSO type is not defined in the gradle.properties file — or the opposite.
  When this happens, attempting to log in using an external provider will display the following error message:

    SSO Configuration Error
    There is a misconfiguration in the SSO setup. Please contact your administrator.

  ![Misconfigured SSO](Auth0DocImages/MissconfigError.png)

  To resolve this issue, ensure that both the SSO preference and the corresponding entry in gradle.properties are correctly configured and consistent with each other.


## How to Integrate Auth0 Social Login with Etendo Classic

Follow this guide to configure an Auth0 application to enable social login in Etendo Classic.


### 1. Create a New Auth0 Application

1. Go to the Auth0 Dashboard: [https://manage.auth0.com/dashboard](https://manage.auth0.com/dashboard)  
2. Sign up or log in to your Auth0 account.  
3. Create a new application for the Etendo Classic integration:
   - On the **Getting Started** page, click **Create Application**.

      ![Auth0 Dashboard](Auth0DocImages/GettingStarted.png)
   
   - Select **Regular Web Application** and give it a name.

      ![Create App](Auth0DocImages/RegularWebApp.png)

   Alternatively:

   - In the left-hand menu, go to **Applications** → **Applications**.
   - Click **Create Application** in the top-right corner.

      ![Applications](Auth0DocImages/Applications.png)

   - Choose a name and select **Regular Web Application**.


### 2. Choose the Technology Stack

4. After creating the application, choose the technology used in your project. For Etendo Classic, select **Java**.

  ![Choose Technology](Auth0DocImages/ProjectTechnology.png)

5. You will be redirected to the **Quick Start** tab of the newly created application.

  ![App Quick Start](Auth0DocImages/AppQuickStart.png)


### 3. Configure Social Login Providers

6. In the left-hand menu, go to **Authentication** → **Social**.

  ![Social](Auth0DocImages/SocialConnection.png)

7. Click **Create Social Connection**.
8. Choose the desired social login providers (Google, Facebook, etc.).

  ![New Social Connection](Auth0DocImages/NewSocialConnection.png)

9. Follow the configuration steps provided by Auth0 for each provider.

  ![Config New Social Connection](Auth0DocImages/ConfigNewSocialConn.png)

10. After setup, go to the **Applications** tab within the connection and link it to your application.

  ![Link Social With App](Auth0DocImages/SocialAppSelected.png)

11. Repeat this process for every provider you want to enable.


### 4. Retrieve and Set Credentials

12. Return to your application and go to the **Settings** tab.

  ![App Settings](Auth0DocImages/AppSettings.png)

13. Locate the following credentials:
    - **Domain**
    - **Client ID**
    - **Client Secret**

14. Add them to your `gradle.properties` file in the following format:

```properties
sso.domain.url=your-domain.auth0.com
sso.client.id=your-client-id
sso.client.secret=your-client-secret
```

- Also, add the Authentication type
  ```properties
  sso.auth.type=Auth0
  ```


### 5. Configure Callback and Logout URLs

15. In the **Settings** tab, configure the following allowed URLs:

- **Allowed Callback URLs:**
  The URLs Auth0 redirects to after a successful login.
  ```
  http://localhost:8080/etendo/secureApp/LoginHandler.html,
  http://localhost:8080/etendo/,
  http://localhost:8080/etendo/web/com.etendoerp.etendorx/LinkAuth0Account.html
  ```

- **Allowed Logout URLs:**
  The URLs Auth0 redirects to after the user logs out.
  ```
  http://localhost:8080/etendo/
  http://localhost:8080/etendo/web/com.etendoerp.entendorx/resources/logout-auth0.html
  ```

    ![Application URIs](Auth0DocImages/AllowedURIs.png)

!!!note
  During development, you can use `localhost`. However, for production, set your actual domain in **Application Login URI**. If you're still in development, you may leave it blank.


### 6. Set the Callback URL

16. Add the callback URL to your `gradle.properties`:

```properties
sso.callback.url=http://localhost:8080/etendo/secureApp/LoginHandler.html
```

### 7. Compile the Project

17. Once all properties are configured, compile the project:

```bash
./gradlew setup smartbuild
```

### 8. Log In via External Providers

18. Start your Tomcat server.
19. Open the Etendo Classic login page and click **Login with external providers**.
20. Here you will see the Auth0 login page with the configured providers.

  ![Auth0 Login](Auth0DocImages/UniversalLoginCustom.png)

!!!info
  Customize your login screen in **Branding** > **Universal Login** in the Auth0 dashboard.

22. The first time you try to log in, you'll likely see an error.

  ![Auth0 Link Error](Auth0DocImages/NoUserLink.png)

23. This is expected, as your external account is not yet linked to an Etendo Classic user.


### 9. Link an External Provider to a User

24. Log in using your standard credentials.
25. Go to your user profile and click **Link user with external providers**.
26. The Auth0 login page will appear allowing you to select the provider to link.
27. After granting permission, you’ll be redirected back to the Etendo Workspace.
28. On future logins, you can now use the linked provider directly.