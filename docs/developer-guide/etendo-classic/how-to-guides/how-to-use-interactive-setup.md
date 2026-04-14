---
tags:
  - How to
  - Etendo Classic
  - Interactive Setup
  - Configuration
---

# How to Use the Interactive Setup

## Overview

The Interactive Setup is an alternative to `setup.applyTemplates` that guides the developer through each configuration property individually, with inline help, validation, and a confirmation step before applying any changes.

Key features:

- Step-by-step guidance with inline help for every property.
- Sensitive input (passwords, tokens) is detected and hidden.
- Settings are grouped by category (Database, Security, Application, etc.).
- Built-in validation and a confirmation step before applying changes.
- Automatic backups of existing configuration files before updates.

!!! info
    For a faster setup using predefined templates, see the [Local Development](../getting-started/installation/local-development.md) or [Server Installation](../getting-started/installation/production-server.md) guides, which use `setup.applyTemplates` as the primary method.

## Requirements

- [System requirements](../getting-started/installation/requirements.md)
- [PostgreSQL configured](../getting-started/installation/postgresql-configuration.md)
- [GitHub credentials](../getting-started/installation/use-of-repositories-in-etendo.md)
- Etendo Gradle Plugin [2.1.0](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) or higher. For more information, visit [Etendo Gradle Plugin](../developer-tools/etendo-gradle-plugin.md).

## Start Interactive Configuration

Launch the interactive configuration assistant:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

## Navigate the Configuration Menu

The main configuration menu is displayed:

```
🎛️  Interactive Setup - Main Menu
============================================================

📋 Choose configuration option:

1️⃣  Default configuration (use current/default values)
2️⃣  Group configuration:
   📦 a. all - Configure all groups
   📋 b. Database Configuration
   📋 c. Security Settings
   📋 d. Application Settings
3️⃣  Exit without saving

🎯 Select an option:
```

## Configure Properties

When selecting a configuration group, each property is presented individually:

```
📋 Database Configuration
==================================================

🔧 Property: bbdd.host
   ℹ️  Database server hostname or IP address
   Current value: localhost
✏️  New value: [Enter to keep current, or type new value]

🔧 Property: bbdd.port
   ℹ️  Database server port number
   Current value: 5432
✏️  New value: [Enter to keep current, or type new value]

🔧 Property: bbdd.password
   ℹ️  Database connection password
   Current value:
🔐 New value (hidden): [Password input is hidden]
```

!!! tip "Property Configuration Tips"
    - **Press Enter** to keep the current/default value.
    - **Type new values** to override defaults.
    - **Sensitive properties** (passwords, tokens) will hide your input.
    - **Required properties** must have a value to proceed.

## Review Configuration Summary

Before applying changes, a complete summary is shown:

```
📊 Configuration Summary
============================================================

📋 Database Configuration:
   🔧 bbdd.host = localhost
   🔧 bbdd.port = 5432
   🔧 bbdd.password = ********

📋 Security Settings:
   🔧 githubToken = ********
   🔧 nexusPassword = ********

📋 Application Settings:
   🔧 context.name = etendo

📊 Total: 6 properties configured
🔐 Including 3 sensitive properties (shown masked)

✅ Confirm configuration? (Y/N):
```

After confirming, properties are saved to `gradle.properties` (with automatic backup) and `./gradlew setup` runs automatically.

## Re-running Interactive Configuration

The interactive configuration can be run again at any time to modify settings or review the current values:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

This shows the current configuration values, allows modifying any setting, and creates a new backup before applying changes.

## Debug Mode

For troubleshooting, enable debug output:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --debug --console=plain
```

## Custom Modules Properties

If the project includes custom modules with a `config.gradle` file, their configuration properties are added automatically to the interactive setup. Property names are preserved exactly as declared in `config.gradle`, and custom keys in `gradle.properties` are supported.

!!! info
    For details about Interactive Configuration for custom modules, visit the [Etendo Interactive Configuration](../developer-tools/etendo-interactive-configuration.md) guide.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
