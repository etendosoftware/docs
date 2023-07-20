---
title: Publish OTA Updates to Etendo Mobile App
---
## Overview

The Etendo mobile application is using AppCenter’s Code Push to deploy OTA updates. This article explains:

-   How to deploy new OTA
-   How to rollback an OTA

> **Requirements**
> 
!!! info
    Install the [App Center CLI](https://docs.microsoft.com/en-us/appcenter/distribution/codepush/)

> **App owner and names**
> 
!!! info
    Useful when using the `--app` flag. Owner name is always `FutitServices`

> **iOS**: `Futit-Services/Mobile-Openbravo`
> 
!!! info
    **Android**: `Futit-Services/Mobile-Openbravo-1`

## How to deploy new OTA

1.  Staging:

> For iOS only:  
> Change the package.json "name" field to "Etendo Mobile".  
!!! warning
    Do not commit this change.

2.  Validate that it works.
3.  Promote to production:

```plaintext

appcenter codepush promote
```

3.  Deploy to certain percentage of users:

-   Promote from staging to production to the 20% of Users:

```plaintext

appcenter codepush promote -a <ownerName>/<appName> -s Staging -d Production -r 20
```

-   Expand promoted update to all users:

```plaintext

appcenter codepush patch -a <ownerName>/<appName> Production -r 100
```

## How to rollback an OTA

```plaintext

appcenter codepush rollback
```

## Links

[Multi-Deployment Testing](https://docs.microsoft.com/en-us/appcenter/distribution/codepush/rn-deployment#multi-deployment-testing)