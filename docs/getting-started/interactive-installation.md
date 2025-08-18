---
title: Install Etendo Classic - Interactive Guide

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
# Interactive Installation Guide

## Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments. 

This guide demonstrates how to install Etendo Classic using the **Interactive Configuration System** - an intuitive wizard that guides you through the setup process step by step.

## Why Use Interactive Installation?

The Etendo Interactive Configuration System offers several advantages over manual configuration:

- **Guided Setup**: Step-by-step wizard with clear documentation for each property
- **Secure Input**: Automatic detection and hidden input for sensitive data (passwords, tokens)
- **Organized Configuration**: Properties grouped by category (Database, Security, Application, etc.)
- **Built-in Validation**: Validation and confirmation before applying changes
- **Safe Updates**: Automatic backup of existing configuration files
- **Faster Setup**: Reduces configuration errors and setup time

## Prerequisites

Before starting, ensure you have:

- [System requirements](../getting-started/requirements.md) met
- [PostgreSQL properly configured](../developer-guide/etendo-classic/getting-started/installation/postgresql-configuration.md)
- GitHub credentials ready ([setup guide](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md))
- Etendo Gradle Plugin [2.1.0](../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) or higher. For more information, visit [Etendo Gradle Plugin](../developer-guide/etendo-classic/developer-tools/etendo-gradle-plugin#etendo-plugin).

## Interactive Installation Process

### Step 1: Prepare Your Environment

Choose your installation format and prepare the base files:

=== ":material-language-java: JAR Format"

    1. Clone Etendo Base project:
        ```bash title="Terminal"
        cd /tmp
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Copy sources to your installation directory:
        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Add your GitHub credentials to `gradle.properties`:
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

    2. Copy sources to your installation directory:
        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Add your GitHub credentials to `gradle.properties`:
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

    2. Copy sources to your installation directory:
        ```bash title="Terminal"
        mv EtendoERP/* /opt/EtendoERP/
        cd /opt/EtendoERP
        ```

    3. Add your GitHub credentials to `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Add Platform Extensions bundle dependency:
        ```groovy title="build.gradle"
        dependencies {
            implementation ('com.etendoerp:platform.extensions:2.6.0')
        }
        ```

    5. Expand Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```

### Step 2: Start Interactive Configuration

Launch the interactive configuration wizard:

```bash title="Terminal"
./gradlew setup --interactive --console=plain
```

### Step 3: Navigate the Configuration Menu

You'll see the main configuration menu:

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

- **Option 1 (Default)**: Use existing or default values for all properties
- **Option 2a (All Groups)**: Configure all properties step by step
- **Option 2b-2d (Specific Groups)**: Configure only selected categories
- **Option 3**: Exit without making changes

### Step 4: Configure Properties

When you select a configuration group, you'll be guided through each property:

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
    - **Press Enter** to keep the current/default value
    - **Type new values** to override defaults
    - **Sensitive properties** (passwords, tokens) will hide your input
    - **Required properties** must have a value to proceed

### Step 5: Review Configuration Summary

Before applying changes, you'll see a complete summary:

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

- [X] All required properties have values
- [X] Database connection details are correct
- [X] GitHub/Nexus credentials are properly set
- [X] Application context name is as desired

### Step 6: Complete Installation

After confirming your configuration:

1. **Properties are saved** to `gradle.properties` (with automatic backup).
2. **Traditional setup runs** automatically.
3. **Installation continues** with your configured settings.

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

### Step 7: Access Your Installation

Open your browser and navigate to:

- **Standard Installation**: `https://<Public server IP>/<Context Name>`
- **Local Development**: `http://localhost:8080/etendo`


## Configuration Groups Reference

### Database Configuration

- `bbdd.host` - Database server hostname
- `bbdd.port` - Database server port (5432 for PostgreSQL, 5434 for Docker)
- `bbdd.sid` - Database name
- `bbdd.systemUser` - Database admin user
- `bbdd.systemPassword` - Database admin password
- `bbdd.user` - Application database user
- `bbdd.password` - Application database password

### Security Settings

- `githubUser` - GitHub username for repository access
- `githubToken` - GitHub personal access token
- `nexusUser` - Nexus repository username
- `nexusPassword` - Nexus repository password

### Application Settings

- `context.name` - Web application context name
- `allow.root` - Allow root user access
- `org.gradle.jvmargs` - JVM arguments for Gradle

### Docker Settings (when using Docker format)

- `docker_com.etendoerp.tomcat` - Enable Dockerized Tomcat
- `docker_com.etendoerp.docker_db` - Enable Dockerized PostgreSQL
- `docker_com.etendoerp.tomcat_port` - Tomcat port (default: 8080)

## Advanced Features

### Re-running Interactive Configuration

You can run the interactive configuration again at any time:

```bash title="Terminal"
./gradlew setup --interactive --console=plain
```

This will:

- Show your current configuration values
- Allow you to modify any settings
- Create new backups before applying changes

### Debug Mode

For troubleshooting, enable debug output:

```bash title="Terminal"
./gradlew setup --interactive --debug --console=plain
```

### Using with Custom Modules

If your project includes custom modules with `config.gradle` files, they will automatically appear in the configuration groups. The new system preserves property names exactly as written and supports custom gradle.properties keys through the optional `name` field. 

!!! info 
    See the [Etendo Interactive Configuration](../developer-guide/etendo-classic/developer-tools/etendo-interactive-configuration.md) guide for details on adding configuration to custom modules.

## Troubleshooting

### Common Issues

**Interactive Mode Not Starting**

```bash
# Ensure you're using the correct flags
./gradlew setup --interactive --console=plain

# If issues persist, stop Gradle daemon and retry
./gradlew --stop
./gradlew setup --interactive --console=plain
```

**Password Input Visible**

- Use a proper terminal (not IDE console)
- Ensure TTY allocation for remote sessions: `ssh -t`

**Configuration Not Applied**

- Check file permissions on `gradle.properties`
- Look for backup files indicating partial success
- Verify no temporary files remain
