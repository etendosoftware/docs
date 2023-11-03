---
title: Etendo Gradle Plugin
tags:
    - Release Notes
    - Etendo
    - Version
    - Gradle
    - Plugin
---
## Overview

| Version | Publication Date | Status |
| --- | --- | --- |
| 1.2.2 | 20/10/2023 | CS |
| 1.2.1 | 18/10/2023 | C  |
| 1.2.0 | 17/10/2023 | C  |
| 1.1.3 | 31/08/2023 | C  |
| 1.1.2 | 31/07/2023 | C  |
| 1.1.1 | 10/07/2023 | C  |
| 1.1.0 | 30/05/2023 | C  |
| 1.0.7 | 05/04/2023 | C  |

## Release Notes

### 1.2.2
-  [EPL-1054](https://github.com/etendosoftware/com.etendoerp.gradleplugin/issues/18) Bug Fix for copilot translation task. The copilot.translation task should require an -Parg  parameter instead of -Ppkg.

### 1.2.1
-  [EPL-1047](https://github.com/etendosoftware/com.etendoerp.gradleplugin/issues/16) Bug Fix for copilot translation task. When the copilot.translate task is executed and API fails, it ends with build successful.

### 1.2.0
-  Add copilot tasks in [Etendo Gradle Plugin](/developer-guide/etendo-classic/developer-tools/etendo-gradle-plugin/#copilot)

### 1.1.3
- EPL-855: Bug fix for compilation of Etendo on Windows, resolving `"File name or file extension is too long"` error.

### 1.1.2
- EPL-818: Bug fix related to duplication of `beans.xml` entry in the resources when setting `etendo-resources` as `sourceSets.main.resources.srcDirs` in the module.

### 1.1.1
- EPL-439: Bug fix for compilation of Etendo on Windows, resolving unexpected behavior and errors encountered during the execution of `compile.complete`
- EPL-740: Bug fix related to downloading dependencies from Nexus. This fix restores the ability to resolve dependencies from Nexus after migration to GitHub, fixing regression.

### 1.1.0
- EPL-597: New features for Github dependency resolution. (Migration bundles to Github)
 
### 1.0.7
- EPL-574: Upgrade Gradle to version 7.3.2 :zap: