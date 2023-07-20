---
title: Using Git Flow to Handle Releases
---
## Overview

This guide will explain how to use Git Flow to handle releases, with a focus on Etendo modules.

For Etendo/Openbravo modules, having a releases workflow allows for more organized module updates, but also gives a defined space to update its version number, avoiding cases where a module grows old while always staying in version 1.0.0. It is also useful to know what version of the module the user has installed, and avoids confusion when updating. This can lead to better bug tracking and organization.

> **Requirements**
> -Git
> -Git Flow AVH
> -A module with a Git repository initialized (either from scratch or an existing one with commits)
!!! info
    -Optional: Sublime Merge (This is a GUI for Git, which also supports Git Flow commands)

## Handling a release

> Read these articles to make sure you are familiar with Git Flow commands and workflow:
> 
> [https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
> 
> [https://jeffkreeftmeijer.com/git-flow/](https://jeffkreeftmeijer.com/git-flow)
> 
> After you have read those, you can keep a reference on Git Flow’s usage by checking their wiki.
> 
!!! info
    The articles linked above already give a general sense on how features, bugfixes, hotfixes and releases are handled. In the context of an Openbravo/Etendo module, a release will include these particular steps:

1.  Start a release:

```plaintext

git flow release start 1.0.5
```

2.  Edit `AD_MODULE.xml`. Change module’s Version and Update Info fields.

```plaintext

- <!--FA87F05028C7488D894C44726474CA35-->  <VERSION><![CDATA[1.0.4]]></VERSION>
+ <!--FA87F05028C7488D894C44726474CA35-->  <VERSION>]<![CDATA[1.0.5]]></VERSION>
```

```plaintext

- <!--FA87F05028C7488D894C44726474CA35-->  <UPDATEINFO><![CDATA[First module release]]></UPDATEINFO>
+ <!--FA87F05028C7488D894C44726474CA35-->  <UPDATEINFO><![CDATA[Added pagination support to the Synchronization process]]></UPDATEINFO>
```

!!! info
    Make sure to always have the Update Info field updated with a description of the latest changes. This is useful to the user when installing/updating the module, as they can see a brief description of what was changed in the latest version.

3.  Update module’s `build.gradle`. Change the version tag:

```plaintext

- version = '1.0.4'
+ version = '1.0.5'
```

4.  Finish the release:

```plaintext

git flow release finish -m 1.0.5 1.0.5
```

!!! info
    It is useful to create tags when finishing releases with the above command. Tags allow to organize releases much more easily. Later, anyone can switch to a specific version inside the repo by using its tag.