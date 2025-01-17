---
title: Use of Repositories in Etendo
tags:
    - Repositories
    - Packages
    - Access Token
---

# Use of Repositories in Etendo

## Overview

While Etendo supports any Maven package repository, we will focus on explaining how to configure Etendo's standard repositories credentials.

By default, Etendo Core and extension packages will be downloaded from the GitHub repositories.

## Using a Personal Access Token in Etendo Projects

When working with Etendo projects, it is important to have the necessary credentials to access GitHub repositories. One way to do this is by using a Personal Access Token. In this guide, we will walk through the steps of setting up and using a Personal Access Token in an Etendo project.

### Generating a Personal Access Token

!!! info
    Along your Etendo License, you will receive an email to join the **Etendo Partners Team** in GitHub, you have to create or associate a GitHub account with the email invited, and your user will have read access to all the Etendo Repositories.

To generate a Personal Access Token, follow these steps:

1. Log in to your GitHub account.
2. Click on your profile picture in the top right corner and select *Settings.*
3. Select *Developer settings* from the left menu and click on *Personal access tokens.*
4. In the developer settings page, click on *Personal access tokens*

    ![personal-access-tokens.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/use-of-repositories-in-etendo/personal-access-tokens.png) 

5. Click the *Generate new token (classic)* button. 

6. Give your token a name and select the permissions you want to grant it. In this case, select *read:packages* check.

    !!! warning
        It is strongly recommended to set an expiration date, but it is also posible to set an undefined expiration.

    ![new-personal-access-token.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/use-of-repositories-in-etendo/new-personal-access-token.png) 

6. Click *Generate token* and take note of the token value.

    !!! warning
            You will not be able to see this value again, so be sure to copy it and keep it in a secure location.

### Setting Up the Personal Access Token in Etendo Projects

Once you have generated a Personal Access Token, you will need to set it up in your Etendo project. Follow these steps:

1. Open the `gradle.properties` file in your project.
2. Add the following lines to the file, replacing `YOUR_GITHUB_USERNAME` and `YOUR_PERSONAL_ACCESS_TOKEN` with your actual GitHub username and Personal Access Token:
        
    ``` bash title="gradle.properties"
    nexusUser=
    nexusPassword=
    githubUser=YOUR_GITHUB_USERNAME
    githubToken=YOUR_PERSONAL_ACCESS_TOKEN
    context.name=etendo
    bbdd.sid=etendo
    bbdd.port=5432
    ```

3. Save the `gradle.properties` file.

### Using the Personal Access Token in Gradle Tasks

With the *Personal Access Token* set up in your Etendo project, you can now use it to access GitHub repositories in your Gradle tasks. For example, if you are using the task

``` bash title="Terminal"
./gradlew dependencies
```

to resolve dependencies, it will use your *Personal Access Token* to authenticate with GitHub.

### Revoking a Personal Access Token

If you no longer need a personal access token or believe it has been compromised, you should revoke it immediately. To do so, follow these steps:

1. Go to your *Settings* page in GitHub.
2. Click *Developer settings* in the left-hand sidebar.
3. Click *Personal access tokens*.
4. Find the token you want to revoke and click the *Revoke* button.
5. Confirm that you want to revoke the token.

Your token will be immediately invalidated and will no longer work.