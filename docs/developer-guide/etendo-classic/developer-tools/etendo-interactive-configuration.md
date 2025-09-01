---
title: Etendo Interactive Setup

tags:
    - Etendo Installation
    - Installation Guide
    - Docker Management
    - PostgreSQL Setup
    - Etendo Environment
    - Install
    - Etendo Install
    - Interactive Installation

status: beta
---
# Etendo Interactive Setup

## Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

!!! info
    This feature is available from the Etendo Gradle Plugin [2.1.0](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md). For more information, visit [Etendo Gradle Plugin](../developer-tools/etendo-gradle-plugin#etendo-plugin).
    

The **Etendo Interactive Configuration** system provides a user-friendly command-line wizard for configuring Etendo projects. Built into the Etendo Gradle Plugin, it guides developers through property configuration with intelligent defaults, secure handling of sensitive data, and organized presentation of configuration options.

## Quick Start

### Basic Usage

```bash
# Run interactive configuration (recommended)
./gradlew setup -Pinteractive=true --console=plain

# Standard setup
./gradlew setup
```

### What the Interactive Setup Does

1. **Scans** your project for configurable properties from:
    - **Existing `gradle.properties` file**: Reads current property values and identifies configurable settings
    - **Module `config.gradle` files**: Discovers module-specific configuration with metadata including descriptions, default values, and security settings

2. **Guides** you through configuration with:
    - **Clear documentation for each property**: Shows descriptive help text explaining what each property does and its purpose
    - **Current/default values shown in prompts**: Displays existing values in parentheses, allowing you to press Enter to keep them or type new values
    - **Secure input for sensitive properties**: Automatically detects passwords, tokens, and secrets, hiding input during typing
    - **Properties organized by logical groups**: Groups related settings (Database, Security, API, etc.) for easier navigation

3. **Confirms** your configuration with:
    - **Complete summary of all settings**: Shows a comprehensive overview of all configured properties organized by group
    - **Sensitive values masked for security**: Displays sensitive properties as asterisks (********) to protect credentials
    - **Ability to review before applying changes**: Requires explicit confirmation (Y/N) before writing any changes to files

4. **Applies** configuration by:
    - **Writing to `gradle.properties` with automatic backup**: Creates timestamped backup files before making changes
    - **Preserving existing comments and structure**: Maintains file formatting, comments, and organization while updating values
    - **Continuing with normal setup process**: Seamlessly integrates with existing Etendo setup workflow

## Configuration Interface

**Choose the main configuration mode**

The interactive setup presents three main configuration modes:

- Default configuration (use current/default values)
- Group configuration:

    a. All - Configure all groups
    b. Database Configuration
    c. Security Settings
    d. Application Settings
- Exit without saving

**Configure properties**

When configuring properties, the system provides rich context. For example:

```
📋 Database Configuration
==================================================

🔧 Property: bbdd.host
   ℹ️  Database server hostname or IP address
   Current value: localhost
✏️  New value: [Enter to keep current, or type new value]

🔧 Property: bbdd.password
   ℹ️  Database connection password
   Current value: ********
🔐 New value (hidden): [Password input is hidden]
```

**Confirm configuration**

Before applying changes, you'll see a complete summary:

```
📊 Configuration Summary
============================================================

📋 Database Configuration:
   🔧 bbdd.host = localhost
   🔧 bbdd.password = ********

📋 Security Settings:
   🔧 githubToken = ********

📊 Total: 3 properties configured
🔐 Including 2 sensitive properties (shown masked)

✅ Confirm configuration? (Y/N):
```

## Adding Configuration to Custom Modules

**Creating a config.gradle File**

To add interactive configuration support to your custom module, create a `config.gradle` file in your module's root directory:

``` title="config.gradle"
    modules/
    ├── com.yourcompany.yourmodule/
    │   ├── config.gradle          ← Configuration file
    │   ├── src/
    │   └── build.gradle
```

**Configuration File Structure**

The `config.gradle` file uses Groovy's ConfigSlurper format, providing structured, type-safe configuration:

```groovy
// modules/com.yourcompany.yourmodule/config.gradle

/**
* Interactive configuration for Your Custom Module
*/

// API Configuration
api {
    baseUrl {
        description = "Base URL for the external API service"
        value = "https://api.example.com"
        sensitive = false
        required = true
        group = "API Configuration"
    }
    
    apiKey {
        description = "API key for authentication with external service"
        value = ""
        sensitive = true
        required = false
        group = "API Configuration"
    }
    
    timeout {
        description = "API request timeout in seconds"
        value = "30"
        sensitive = false
        required = false
        group = "API Configuration"
    }
    
    // Example using custom name field for specific gradle.properties key
    customEndpoint {
        description = "Custom API endpoint URL"
        value = ""
        name = "custom.api.endpoint"  // Maps to custom.api.endpoint in gradle.properties
        sensitive = false
        required = false
        group = "API Configuration"
    }
}

// Feature Settings
features {
    enableAdvancedReporting {
        description = "Enable advanced reporting features"
        value = "false"
        sensitive = false
        required = false
        group = "Feature Settings"
    }
    
    maxReportSize {
        description = "Maximum report size in MB"
        value = "10"
        sensitive = false
        required = false
        group = "Feature Settings"
    }
}

// Database Settings (if your module needs separate DB config)
database {
    connectionPool {
        description = "Database connection pool size for module operations"
        value = "5"
        sensitive = false
        required = false
        group = "Database Settings"
    }
}
```

**Configuration Properties Reference**

Each property in your `config.gradle` file supports the following metadata:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | String | Yes | Human-readable description shown to users |
| `value` | String | Yes | Default value for the property |
| `sensitive` | Boolean | No | `true` for passwords, tokens, secrets (default: `false`) |
| `required` | Boolean | No | `true` for mandatory properties (default: `false`) |
| `group` | String | No | Display group name (default: auto-generated from block name) |

**Property Naming and Mapping**

The system preserves property names exactly as written, with optional custom naming:

```groovy
// Default mapping (names preserved exactly as written)
api.baseUrl → api.baseUrl
api.apiKey → api.apiKey
features.enableAdvancedReporting → features.enableAdvancedReporting
database.connectionPool → database.connectionPool

// Custom mapping using name field
api {
    baseUrl {
        name = "api.base.url"  // Custom gradle.properties key
        // Other properties...
    }
    
    // Property names are NOT automatically transformed
    myCustomAPIKey {
        description = "My custom API key"
        value = ""
        // Results in gradle.properties key: api.myCustomAPIKey (no transformation)
    }
}
```

!!! Important "Important Changes"

    - **No automatic transformation**: Property names like `systemUser` remain as `systemUser` (not transformed to `system.user`).
    - **Preserved naming**: All property names are kept exactly as written in the `config.gradle` file.
    - **Optional custom mapping**: Use the `name` field when you need specific `gradle.properties` keys for compatibility.

**Sensitive Property Handling**

The system automatically detects sensitive properties based on:

- **Explicit marking**: `sensitive = true` in configuration
- **Pattern detection**: Properties containing keywords like: `password`, `secret`, `token`, `key`, `credential`, `auth`, `private`, `secure`

Example of sensitive property configuration:

```groovy
security {
    databasePassword {
        description = "Database password for module-specific operations"
        value = ""
        sensitive = true  // Explicitly marked as sensitive
        required = true
        group = "Security Settings"
    }
    
    jwtSecret {
        description = "JWT signing secret for token generation"
        value = ""
        sensitive = true  // Will be automatically detected due to 'secret' keyword
        required = true
        group = "Security Settings"
    }
}
```


## Testing Your Configuration

1. Test that your `config.gradle` file is properly discovered:

    ```bash
    # Run with debug output to see property scanning
    ./gradlew setup -Pinteractive=true --debug --console=plain | grep "config.gradle"

    # Expected output:
    # DEBUG - ✓ Processing config.gradle in modules/com.yourcompany.yourmodule
    # DEBUG - Loaded 5 properties from modules/com.yourcompany.yourmodule/config.gradle
    ```

2. After running interactive setup, verify that properties are correctly written to `gradle.properties`:

    ```bash
    # Check that your module's properties appear in gradle.properties
    cat gradle.properties | grep "api\."

    # Example output with preserved naming:
    # api.baseUrl=https://api.example.com
    # api.apiKey=your_secret_key
    # api.customEndpoint=custom_value
    # custom.api.endpoint=value_with_custom_name
    ```

3. Run the interactive setup and verify your module's properties appear:

    ```bash
    ./gradlew setup -Pinteractive=true --console=plain
    ```

You should see your module's property groups in the configuration menu and be able to configure them individually or as part of "all groups" configuration.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.