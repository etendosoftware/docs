---
title: Etendo Testing Plugin
tags:
  - Plugin
  - Gradle
  - Testing
  - JUnit
  - Spock
---

## Overview

This article describes how to use the Etendo Testing Plugin. This plugin provides a standardized test environment compatible with Groovy, Spock, JUnit 4/5, and Mockito for Etendo Classic projects.

---

## Installation

Add the plugin to your `build.gradle` file:

```groovy title="build.gradle"
plugins {
    id 'com.etendoerp.testing.gradleplugin' version '<version>'
}
```

!!! info
    Check the available plugin versions in the [Release Notes](../../../whats-new/release-notes/etendo-classic/plugins/etendo-testing-plugin/release-notes.md).


## Test structure

The plugin includes the following test directories by default:

```
src-test/
├── src/          → Java test sources
├── test/groovy/  → Groovy/Spock tests
├── resources/    → Test resources
```

It also dynamically includes test sources from:

- `modules/**/src-test/src`
- `modules_core/**/src-test`

---

## Example usage

Run tests:

```bash
./gradlew test
```

Generate reports:

- Spock HTML reports are enabled via `spock-reports`
- Use standard Gradle test reports in `build/reports/tests/test/index.html`

---

## Advanced options

You can add additional libraries to `lib/test/` and they will be automatically included:

```groovy
testImplementation fileTree(project.projectDir) {
    include "lib/test/*.jar"
}
```

The plugin also registers an optional helper task:

```bash
./gradlew depsTest
```

Which injects compile-time dependencies into `testImplementation`.

---

## Technologies used

- Groovy 3.0.9  
- Spock Framework 2.0 (Groovy 3)
- JUnit 4.13.1 + JUnit Platform
- Mockito 5.0.0
- Spock Reports 2.0

---

## Compatibility

| Plugin Version | Gradle | Java |
|----------------|--------|------|
| 1.0.0          | 7.0+   | 11+  |
| 2.0.0          | 8.0+   | 17+  |

---
