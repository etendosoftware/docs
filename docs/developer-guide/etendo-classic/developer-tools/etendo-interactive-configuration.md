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
    This feature is available from the Etendo Gradle Plugin [2.1.0](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md). For more information, visit [Etendo Gradle Plugin](../developer-tools/etendo-gradle-plugin).
    

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
   - **Module `config.gradle` files**: Discovers module-specific configuration with metadata including descriptions, default values, security settings, and process properties

2. **Guides** you through configuration with:
   - **Clear documentation for each property**: Shows descriptive help text explaining what each property does and its purpose
   - **Current/default values shown in prompts**: Displays existing values in parentheses, allowing you to press Enter to keep them or type new values
   - **Secure input for sensitive properties**: Automatically detects passwords, tokens, and secrets, hiding input during typing
   - **Process property execution**: Offers to execute Gradle tasks for automated configuration of complex settings
   - **Properties organized by logical groups**: Groups related settings (Database, Security, API, etc.) for easier navigation

3. **Confirms** your configuration with:
   - **Complete summary of all settings**: Shows a comprehensive overview of all configured properties organized by group
   - **Process execution results**: Displays properties automatically configured by process executions
   - **Sensitive values masked for security**: Displays sensitive properties as asterisks (********) to protect credentials
   - **Ability to review before applying changes**: Requires explicit confirmation (Y/N) before writing any changes to files

4. **Applies** configuration by:
   - **Writing to `gradle.properties` with automatic backup**: Creates timestamped backup files before making changes
   - **Preserving existing comments and structure**: Maintains file formatting, comments, and organization while updating values
   - **Marking executed processes**: Adds `EXECUTED:` markers to process properties that have been run
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
        help = "Full URL including protocol and port. Example: https://api.example.com:8443/v1"
        sensitive = false
        required = true
        group = "API Configuration"
        name = "api.base.url"
        order = 10
    }
    
    apiKey {
        description = "API key for authentication with external service"
        value = ""
        help = "Secret key obtained from your API provider dashboard"
        sensitive = true
        required = false
        group = "API Configuration"
        name = "API_SECRET_KEY"
        order = 20
    }
    
    timeout {
        description = "API request timeout in seconds"
        value = "30"
        help = "Maximum time to wait for API responses before timing out"
        sensitive = false
        required = false
        group = "API Configuration"
        name = "api.timeout.seconds"
        order = 30
    }
    
    // Example using custom name field for specific gradle.properties key
    customEndpoint {
        description = "Custom API endpoint URL"
        value = ""
        name = "custom.api.endpoint"  // Maps to custom.api.endpoint in gradle.properties
        help = "Alternative endpoint for specialized API operations"
        sensitive = false
        required = false
        group = "API Configuration"
        order = 40
    }
}

// Process Properties - Automated Configuration
automation {
    databaseSetup {
        description = "Automated database configuration"
        value = ""
        help = "Executes database setup tasks including schema creation and connection pooling"
        sensitive = false
        required = false
        process = true  // This is a process property
        group = "Automated Setup"
        name = "database.setup.automated"
        order = 10
    }
    
    apiIntegration {
        description = "API integration setup process"
        value = ""
        help = "Automatically configures API endpoints, credentials, and feature flags"
        sensitive = false
        required = false
        process = true  // This will execute automation.apiIntegration task
        group = "Automated Setup"
        name = "api.integration.configure"
        order = 20
    }
}

// Feature Settings
features {
    enableAdvancedReporting {
        description = "Enable advanced reporting features"
        value = "false"
        help = "Activates enhanced reporting capabilities with chart generation"
        sensitive = false
        required = false
        group = "Feature Settings"
        name = "features.advanced.reporting.enabled"
        order = 10
    }
    
    maxReportSize {
        description = "Maximum report size in MB"
        value = "10"
        help = "Limits the size of generated reports to prevent memory issues"
        sensitive = false
        required = false
        group = "Feature Settings"
        name = "features.reports.max.size.mb"
        order = 20
    }
}

// Database Settings (if your module needs separate DB config)
database {
    connectionPool {
        description = "Database connection pool size for module operations"
        value = "5"
        help = "Number of concurrent database connections for this module"
        sensitive = false
        required = false
        group = "Database Settings"
        name = "database.connection.pool.size"
        order = 10
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
| `process` | Boolean | No | `true` for process properties that execute Gradle tasks (default: `false`) |
| `help` | String | No | Extended help text with usage details and examples |
| `group` | String | No | Display group name (default: auto-generated from block name) |
| `order` | Integer | No | Display order within group (recommended: 10, 20, 30...) |
| `name` | String | No | Variable name for gradle.properties OR task name for process properties |

### Property Display Order

Properties are displayed in the interactive setup following these rules:

1. **Process properties first**: All properties with `process = true` are shown before regular properties
2. **Then by order field**: Properties are sorted by their `order` value within each type (process vs regular)

```groovy
database {
    // This process property will appear first (process = true)
    setup {
        description = "Automated database setup"
        process = true
        order = 10
    }
    
    // Regular properties appear after process properties, sorted by order
    host {
        description = "Database hostname"
        order = 10  // First regular property
    }
    
    port {
        description = "Database port"
        order = 20  // Second regular property
    }
    
    password {
        description = "Database password"
        order = 30  // Third regular property
    }
}
```

### Property Naming and Mapping

The `name` field has different purposes depending on the property type:

#### For Regular Properties
Use the `name` field to specify the exact variable name that will be written to `gradle.properties`:

```groovy
// Example with custom name field
myModule {
    debugMode {
        description = "Enable debug mode"
        help = "🔧 Enable verbose debugging for module development and troubleshooting"
        value = "false"
        sensitive = false
        required = false
        group = "MyModule Configuration (Advanced)"
        order = 20
        name = "MYMODULE_DEBUG"          // This will be the variable name in gradle.properties
    }
}
```

**Result in gradle.properties:**
```properties
MYMODULE_DEBUG=false
```

#### For Process Properties
Use the `name` field to specify the exact Gradle task name to execute:

```groovy
// Example with custom task name
automation {
    setupDatabase {
        description = "Database configuration setup"
        value = ""
        help = "Executes automated database configuration"
        process = true
        group = "Automation"
        name = "database.configure.production"  // This will execute the task: database.configure.production
    }
}
```

#### Default vs Custom Naming

```groovy
api {
    baseUrl {
        description = "API Base URL"   
        value = "https://api.example.com"
        // No 'name' field = defaults to "api.baseUrl"
    }
    
    apiKey {
        description = "API Key"
        value = ""
        name = "API_TOKEN"             // Custom name: "API_TOKEN"
    }
}

automation {
    databaseSetup {
        description = "Setup database"
        process = true
        // No 'name' field = defaults to task "automation.databaseSetup"
    }
    
    customSetup {
        description = "Custom setup process"
        process = true
        name = "my.custom.task"        // Custom task name: "my.custom.task"
    }
}
```

**Results:**
```properties
# Regular properties in gradle.properties
api.baseUrl=https://api.example.com
API_TOKEN=

# Process properties execute tasks
# automation.databaseSetup → executes task "automation.databaseSetup"  
# automation.customSetup → executes task "my.custom.task"
```

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

## Process Properties

### Overview

Process properties are a special type of property that execute Gradle tasks to gather configuration values automatically. Instead of asking users to manually input complex configuration, these properties run automated processes that can:

- Execute external commands
- Query APIs or services  
- Generate configuration files
- Set up integrations
- Configure complex multi-step processes

### How Process Properties Work

1. **Definition**: Mark a property with `process = true` in your configuration
2. **Task Execution**: When selected, the system executes the corresponding Gradle task
3. **Result Collection**: The task outputs configuration to a JSON file
4. **Property Updates**: Results are automatically applied to gradle.properties
5. **Execution Tracking**: Completed processes are marked with `EXECUTED:` markers

### Process Property Lifecycle

```bash
# User selects process property in interactive setup
myModule.variables.setup = "" (process property)

# System prompts for execution
"Execute myModule variables setup process? (Y/n): Y"

# Task execution
"Executing task: myModule.variables.setup..."

# Results applied automatically
myModule.api.endpoint = "https://api.mymodule.com"
myModule.api.key = "********"
myModule.workspace.id = "ws_abc123"

# Original property marked as executed
myModule.variables.setup = "EXECUTED:3_properties_configured"
```

### Creating Process Properties

#### Basic Process Property Configuration

**Important**: The property name (key) in the configuration **must match the Gradle task name** that will be executed. The system automatically maps the property key to the corresponding Gradle task.

```groovy
// Process property that executes automated configuration
myModule {
    variables {
        setup {
            description = "MyModule variables configuration"
            value = ""
            help = "Executes automated setup to configure module integration variables"
            process = true  // Marks this as a process property
            sensitive = false
            required = false
            group = "MyModule Integration"
            order = 1
            // This will execute the Gradle task: "myModule.variables.setup"
        }
    }
}

// Database setup process
database {
    setup {
        description = "Automated database configuration"
        value = ""
        help = "Configures database connection settings and initializes schema"
        process = true
        sensitive = false
        required = false
        group = "Database Configuration"
        order = 1
        // This will execute the Gradle task: "database.setup"
    }
}

// Alternative naming for complex task names
databaseMigration {
    description = "Database migration and schema updates"
    value = ""
    help = "Runs database migrations and schema updates"
    process = true
    group = "Database Configuration" 
    order = 2
    // This will execute the Gradle task: "databaseMigration"
}
```

#### Task Naming Convention

- **Property key = Task name**: `myModule.variables.setup` → executes task `myModule.variables.setup`
- **Hierarchical properties**: `database.setup` → executes task `database.setup`  
- **Simple names**: `databaseMigration` → executes task `databaseMigration`

### Task Implementation for Process Properties

Process properties require corresponding Gradle tasks that follow this pattern:

#### Required Task Features

1. **Must accept output parameter**: Tasks **must** receive an `output` parameter that specifies where to write results
2. **Use writeResultsForInteractiveSetup utility**: Use the provided utility method to write results
3. **Provide meaningful feedback**: Include progress messages for user awareness
4. **Handle errors gracefully**: Provide clear error messages when configuration fails

!!!warning "Critical Requirement"
    Process property tasks **must** accept an `output` parameter. This is where the task writes its configuration results that will be applied to gradle.properties.

#### Using writeResultsForInteractiveSetup Utility

The Interactive Setup system provides a utility method `writeResultsForInteractiveSetup` to standardize how tasks communicate their configuration results back to the setup process.

```groovy
// Example task for myModule.variables.setup process property
task 'myModule.variables.setup' {
    description = "Configures MyModule integration variables"
    
    doLast {
        try {
            // Get the output parameter (REQUIRED)
            def outputPath = project.findProperty('output')
            if (!outputPath) {
                throw new RuntimeException("Missing required 'output' parameter")
            }
            
            // Execute configuration logic
            println "🔧 Configuring MyModule integration..."
            
            // Your custom configuration logic here
            def apiEndpoint = "https://api.mymodule.com"
            def workspaceId = generateWorkspaceId()
            def apiKey = generateApiKey()
            
            // Prepare results for the interactive setup
            def results = [
                "myModule.api.endpoint": apiEndpoint,
                "myModule.workspace.id": workspaceId,
                "myModule.api.key": apiKey,
                "myModule.features.enabled": "true",
                "myModule.version": "1.0.0"
            ]
            
            // Use the reusable function for JSON output (if called from interactive setup)
            boolean wasWrittenAsJson = false
            if (com.etendoerp.legacy.interactive.InteractiveSetupManager != null) {
                try {
                    wasWrittenAsJson = com.etendoerp.legacy.interactive.InteractiveSetupManager
                        .writeResultsForInteractiveSetup(project, results, outputPath)
                } catch (Exception e) {
                    // Fallback if the method call fails - assume direct execution
                    project.logger.debug("Failed to call InteractiveSetupManager.writeResultsForInteractiveSetup: ${e.message}")
                    wasWrittenAsJson = false
                }
            }
            
            if (wasWrittenAsJson) {
                println "✅ MyModule configuration completed: ${results.size()} properties configured"
            } else {
                throw new RuntimeException("Failed to write configuration results")
            }
            
        } catch (Exception e) {
            throw new RuntimeException("MyModule setup failed: ${e.message}", e)
        }
    }
}
```

#### writeResultsForInteractiveSetup Method Signature

```groovy
/**
 * Writes results for interactive setup tasks in JSON format.
 *
 * @param project The Gradle project context
 * @param results Map of property keys to values that were configured
 * @param outputPath Optional custom output file path (uses project.output if not provided)
 * @return boolean true if results were written successfully, false otherwise
 */
static boolean writeResultsForInteractiveSetup(
    Project project, 
    Map<String, String> results, 
    String outputPath = null
)
```

#### Benefits of Using the Utility

- **Standardized output format**: Ensures consistent JSON structure
- **Automatic file handling**: Creates directories and manages file paths
- **Error handling**: Graceful handling of write failures
- **Debug logging**: Automatic logging of results for troubleshooting
- **Path resolution**: Automatically uses the `output` parameter from the interactive setup

### Process Property Best Practices

1. **Task Naming**: Task names should match the property key (e.g., `myModule.variables.setup` → `myModule.variables.setup`)

2. **Accept output parameter**: Tasks **must** accept an `output` parameter to specify where results are written

3. **JSON Output**: Always write results as JSON to the output file specified by `output` parameter

4. **Error Handling**: Provide meaningful error messages when processes fail

5. **User Feedback**: Include progress messages to inform users what's happening

6. **Result Validation**: Ensure all generated properties are valid and properly formatted

### Process Property Example in Interactive Setup

When users encounter process properties in the interactive setup:

```bash
=== MyModule Integration ===
(2 properties)

🔧 Property: myModule.variables.setup [PROCESS]
   ℹ️  MyModule variables configuration
   💡 Help: Executes automated setup to configure module integration variables
   
🎯 Execute process? (Y/n): Y

🚀 Executing task: myModule.variables.setup...
🔧 Configuring MyModule integration...
✅ MyModule configuration completed: 5 properties configured

📊 Process Results Applied:
   🔧 myModule.api.endpoint = https://api.mymodule.com
   🔧 myModule.api.key = ********
   🔧 myModule.workspace.id = ws_abc123
   🔧 myModule.features.enabled = true
   🔧 myModule.version = 1.0.0

🔖 Process property marked as: EXECUTED:5_properties_configured
```


## Best Practices

### Property Organization

1. **Group Related Properties**: Use logical groups like "API Configuration", "Database Settings", "Security Settings"

2. **Clear Descriptions**: Write descriptive help text that explains the property's purpose and any constraints

3. **Sensible Defaults**: Provide reasonable default values that work for most users

4. **Use Order Field**: Always specify `order` values in increments of 10 (10, 20, 30...) to allow insertion of new properties

5. **Mark Sensitive Data**: Always mark credentials, passwords, and tokens as sensitive

### Naming Conventions

1. **Property names are preserved exactly**: Use any naming convention you prefer - names are not transformed
2. **Be Descriptive**: Use clear, descriptive property names
3. **Avoid Reserved Words**: Don't use Gradle or Java reserved keywords
4. **Use name field for custom mapping**: When you need specific gradle.properties keys or task names

```groovy
// Good examples - include name field and order for clarity
api {
    baseUrl { 
        description = "API base URL"
        value = "https://api.example.com"
        name = "api.base.url"
        order = 10
    }
    connectionTimeout { 
        description = "Connection timeout in seconds"
        value = "30"
        name = "api.connection.timeout"
        order = 20
    }
    retryAttempts { 
        description = "Number of retry attempts"
        value = "3"
        name = "api.retry.attempts"
        order = 30
    }
    
    // Legacy compatibility example
    systemUser {
        description = "System user for API access"
        value = "etendo_system"
        name = "api.system.user"  // → api.system.user (custom mapping)
        order = 40
    }
}

// Still avoid
api {
    url { /* too generic */ }
    timeout { /* unclear which timeout */ }
    class { /* reserved word */ }
}
```

### Configuration Validation

The system provides type safety through ConfigSlurper's structured format. All properties are validated for proper syntax and required fields during the scanning process.

## Summary

The Etendo Interactive Configuration system provides a powerful, user-friendly way to configure Etendo projects and custom modules. By creating `config.gradle` files with structured metadata, you can provide users with guided configuration experiences while maintaining the flexibility and power of Gradle-based builds.

Key benefits for module developers:

- **Easy Integration**: Simply add a `config.gradle` file to your module
- **Rich Metadata**: Provide descriptions, defaults, security markers, and help text
- **Process Properties**: Enable automated configuration through Gradle task execution
- **Automatic Discovery**: Properties are automatically discovered and presented
- **Secure Handling**: Sensitive data is automatically protected
- **Order Preservation**: Properties maintain their definition order
- **Backward Compatible**: Existing setup processes remain unchanged

### Property Types Supported

1. **Regular Properties**: Standard configuration values entered by users
2. **Sensitive Properties**: Secure values with hidden input (passwords, tokens, keys)
3. **Required Properties**: Properties that must have values before setup completes
4. **Process Properties**: Automated configuration executors that run Gradle tasks
5. **Help-Enhanced Properties**: Properties with extended help text and usage examples

The system automatically handles all property types, providing appropriate prompts, validation, and security measures for each type.

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