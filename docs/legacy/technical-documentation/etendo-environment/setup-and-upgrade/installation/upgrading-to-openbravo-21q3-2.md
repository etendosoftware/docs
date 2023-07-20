---
title: Upgrading to Openbravo 21Q3.2
---
## Overview

This guide explains how to upgrade your current Openbravo environment to version 21Q3.2. This involves two main steps:

-   Identify and extract custom patches made to your current version of Openbravo
-   Upgrade to Openbravo 21Q3.2

!!! info
    This upgrade is required in order to migrate Openbravo to Etendo.

## How to upgrade to Openbravo 21Q3.2

> **Requirements**
> -Git
!!! info
    -A diffing/merging tool if patches need to be generated

### Identify and extract custom patches made to your current version of Openbravo

1.  Clone core repository in the new version

```plaintext

git clone --depth 1 --branch YOURVERSIONTAG git@gitlab.com:openbravo/product/openbravo.git
```

!!! info
    Replace *YOURVERSIONTAG* tag with your current Openbravo version, e.g.: 3.0PR19Q4

2.  Identify patches applied to core in current installation, to be re-applied later:

-   Use a diffing tool like Meld or Kdiff3 to compare the differences between your environment and the standard Openbravo you just cloned.
-   Extract custom patches (avoid generating patches for changes that are bugfixes, since they should be included in the new version).

### Upgrade to Openbravo 21Q3.2

1.  Clone core repository in the new version:

```plaintext

git clone --depth 1 --branch 3.0PR21Q3.2 git@gitlab.com:openbravo/product/openbravo.git
```

2.  Configure Openbravo.properties and other files to match your current installation.
3.  Copy all modules from your previous installation to the new environment.
4.  Apply patches extracted on previous steps (they may need to be adapted to the new version).
5.  Do a full compilation:

```plaintext

ant update.database compile.complete.deploy
```

6.  Fix problems with custom modules.

!!! warning
    Check [Openbravo’s Release Notes](http://wiki.openbravo.com/wiki/Release_Notes/3.0PR21Q3.2) for API changes and other considerations when upgrading.

7.  Start server.
8.  Test for functional or runtime errors and fix them.

> Your environment is ready to be migrated to Etendo.  
!!! success
    Check the [migration tool’s guide](https://docs.etendo.software/en/technical-documentation/etendo-environment/setup-and-upgrade/installation/migrating-to-etendo-from-openbravo).