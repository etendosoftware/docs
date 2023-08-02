---
title: Hotfixes
---

## Overview

This article explains how to solve a Hotfix in Etendo.

> A Hotfix is an error in a supported version (one year of support since deployment) that must be fixed. Then a new minor version has to be deployed.

## Solving Hotfixes

1.  Checkout to the version release where the bug was reported.  
    A git tag can be run to show all version tags available:

```plaintext

git checkout <lastTag>
./gradlew update.database compile.complete
```

2.  Replicate the bug and create a new branch in the Etendo Core project directory (this command has to create a new branch from the master branch).  
    The Hotfix name should be the same as the main tag but ending with a timestamp as a minor.  
    For example, if the tag is 1.0.x, run the following command to generate the branch with the timestamp:

```plaintext

git branch "hotfix/1.0.$(date +"%s")"
```

3.  Solve the bug.
4.  Run the following command:

```plaintext

./gradlew compile.complete.deploy
```

5.  When the project compiles correctly, commit and create a pull request with other Etendo developers as reviewers.
6.  When the pull request is approved and merged, deploy a minor version following these steps:  
    In the `version.properties` file, you have to change the version with the Hotfix name. You can check the Hotfix name with `git branch` command:

```plaintext

git branch
  develop
* hotfix/1.0.1617814452 >-- New Version
  master
```

For example, if the old version is 1.0.0 you have to change it for the new version 1.0.1617814452:

```plaintext

version.ts=1620760331
```

Finally, publish the version using the Nexus admin credentials and create a patch to apply in other releases:

```plaintext

./gradlew publish

git checkout master
git merge
git tag
git checkout develop
git merge master
git push
git push --tags
```

> The Hotfixes have to be extended to all supported versions ([read how to port the Hotfix to other releases](https://incidencias.atlassian.net/browse/ERP-336)). It could be necessary to refactor code for a specific release.

> **The Hotfix has been solved.**  
> Notify the client to run `expandCore` command and the bug will be solved.

## Port a Hotfix to other releases

When you create a new Hotfix, there is also a patch that has to be applied to each supported release:

![hotfixes.jpeg](/docs/assets/legacy/technicaldocumentation/securityandbugs/hotfixes.jpeg)

1.  Move to each release tag and create a new branch with timestamp as a minor. For example:

```plaintext

git checkout 1.0.0
git branch "hotfix/1.0.$(date +"%s")"
<apply patch>
```

> If the patch is applied but has conflicts, refactor this code to fix it.

2.  Publish a new minor release with the branch name as version. Run `git branch` to see all branches, e.g.:

```plaintext

git branch
  develop
* hotfix/1.0.5433 >-- new version
  master
```

For example, if the old version is 1.0.0 and you have to change it for 1.0.5433:

```plaintext

plugins {
    id 'java'
    id 'maven-publish'
    id 'war'
    id 'idea'
}

apply from: 'https://repo.futit.cloud/repository/static-public-releases/com/etendo/etendo/latest/etendo-latest.gradle'

group = 'com.smf.classic.core'
version = '1.0.5433' >-- new version

...
```

3.  Publish the new version using the Nexus admin credentials:

```plaintext

git tag <new version>
git push
git push --tags
./gradlew publish
```
