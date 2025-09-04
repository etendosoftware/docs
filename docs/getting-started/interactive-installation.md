---
title: Install Etendo - Interactive Guide

tags:
    - Etendo Installation
    - Installation Guide
    - Docker Management
    - PostgreSQL Setup
    - Etendo Environment
    - Install
    - Interactive Installation

status: beta
---
# Install Etendo - Interactive Guide

## Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments. 

This section explains how to install Etendo Classic using the **Interactive Configuration System**. An intuitive assistant that guides users through the setup process step by step.

The Etendo Interactive Configuration System offers several advantages over manual configuration:

- **Guided Setup**: Step-by-step assistant with clear documentation for each property.
- **Secure Input**: Automatic detection and hidden input for sensitive data (passwords, tokens).
- **Organized Configuration**: Properties grouped by category (Database, Security, Application, etc.).
- **Built-in Validation**: Validation and confirmation before applying changes.
- **Safe Updates**: Automatic backup of existing configuration files.
- **Faster Setup**: Reduces configuration errors and setup time.

## Requirements

Before starting, it is necessary to have:

- [System requirements](../getting-started/requirements.md).
- [PostgreSQL properly configured](../developer-guide/etendo-classic/getting-started/installation/postgresql-configuration.md). 
- GitHub credentials ready. Get access to the [setup developer guide](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md). 
- Etendo Gradle Plugin [2.1.0](../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) or higher. 

!!!info
    For more information, visit [Etendo Gradle Plugin](../developer-guide/etendo-classic/developer-tools/etendo-gradle-plugin.md).

## Interactive Installation Process

### Prepare the Environment

Choose the installation format and prepare the base files:

=== ":material-language-java: JAR Format"

    1. Clone Etendo Base project:
        ```bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Copy sources to the installation directory:
        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Add GitHub credentials to `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Uncomment the core dependency in `build.gradle`:
        ```groovy title="build.gradle"
        implementation('com.etendoerp.platform:etendo-core:<version>')
        ```

=== ":octicons-file-zip-24: Source Format"

    1. Clone Etendo Base project:
        ```bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Copy sources to the installation directory:
        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Add GitHub credentials to `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Expand Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```

=== ":material-docker: Docker Format"

    1. Clone Etendo Base project:
        ```bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Copy sources to the installation directory:
        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Add GitHub credentials to `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Add Platform Extensions bundle dependency:
        ```groovy title="build.gradle"
        dependencies {
            implementation ('com.etendoerp:platform.extensions:2.6.0') // 2.6.0 or higher.
        }
        ```

    5. Expand Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```

### Start Interactive Configuration

Launch the interactive configuration assistant:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

### Navigate the Configuration Menu

It will be possible to see the main configuration menu:

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

**Configuration Options:**

- **Option 1 (Default)**: Use existing or default values for all properties.
- **Option 2a (All Groups)**: Configure all properties step by step.
- **Option 2b-2d (Specific Groups)**: Configure only selected categories.
- **Option 3**: Exit without making changes.

### Configure Properties

When selecting a configuration group, you will be guided through each property:

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

### Review Configuration Summary

Before applying changes, a complete summary will be shown:

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

**Review Checklist**

- [X] All required properties have values.
- [X] Database connection details are correct.
- [X] GitHub/Nexus credentials are properly set.
- [X] Application context name is as desired.

### Complete Installation

After confirming the configuration:

1. **Properties are saved** to `gradle.properties` (with automatic backup).
2. **Traditional setup runs** automatically.
3. **Installation continues** with the configured settings.

Complete the installation process:

=== ":material-language-java: JAR Format"

    ```bash title="Terminal"
    # Dependencies
    ./gradlew dependencies
    
    # Installation
    ./gradlew install smartbuild
    
    # Start Tomcat
    sudo /etc/init.d/tomcat start
    ```

=== ":octicons-file-zip-24: Source Format"

    ```bash title="Terminal"
    # Installation
    ./gradlew install smartbuild
    
    # Start Tomcat
    sudo /etc/init.d/tomcat start
    ```

=== ":material-docker: Docker Format"

    ```bash title="Terminal"
    # Launch Docker services
    ./gradlew resources.up
    
    # Installation
    ./gradlew install smartbuild
    ```

### Access Your Installation

Open the browser and navigate to:

- **Standard Installation**: `https://<Public server IP>/<Context Name>`
- **Local Development**: `http://localhost:8080/etendo`


## Advanced Features

### Re-running Interactive Configuration

It is possible to run the interactive configuration again at any time:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

This will:

- Show the current configuration values.
- Allow the user to modify any settings.
- Create new backups before applying changes.

### Debug Mode

For troubleshooting, enable debug output:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --debug --console=plain
```

### Using with Custom Modules

If the project includes custom modules with `config.gradle` files, they will automatically appear in the configuration groups. The new system preserves property names exactly as written and supports custom gradle.properties keys through the optional `name` field. 

!!! info 
    Visit the [Developer Guide](../developer-guide/etendo-classic/developer-tools/etendo-interactive-configuration.md) for details about Interactive Configuration to custom modules.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
