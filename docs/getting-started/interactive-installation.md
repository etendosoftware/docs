---
title: Install Etendo - Quick Installation Guide

tags:
    - Etendo Installation
    - Installation Guide
    - Docker Management
    - PostgreSQL Setup
    - Etendo Environment
    - Install
    - Quick Installation

status: beta
---
# Install Etendo - Quick Installation Guide

## Overview

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments. 

Use the Quick Installation feature to install and configure Etendo. The assistant walks you through each setting, applies safe defaults, and performs changes only after you confirm them.

Key benefits:

- Step-by-step guidance with inline help for every property.
- Sensitive input (passwords, tokens) is detected and hidden.
- Settings are grouped by category (Database, Security, Application, etc.).
- Built-in validation and a confirmation step before applying changes.
- Automatic backups of existing configuration files before updates.
- Faster, less error-prone setup compared to manual editing.

## Requirements

Before starting, it is necessary to have:

- [System requirements](../getting-started/requirements.md).
- [PostgreSQL properly configured](../developer-guide/etendo-classic/getting-started/installation/postgresql-configuration.md). 
- GitHub credentials ready. Get access to the [Use of Repositories in Etendo - Developer Guide](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md). 
    
    
        

- Etendo Gradle Plugin [2.1.0](../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) or higher.  For more information, visit [Etendo Gradle Plugin](../developer-guide/etendo-classic/developer-tools/etendo-gradle-plugin.md).

## Quick Installation

Use the `setup.applyTemplates` task to configure and install Etendo in a few steps using predefined templates. Select the tab that matches your environment:

=== ":material-laptop: Local Development"

    1. Clone the Etendo Base project:
        ```bash title="Terminal"
        cd /path/to/workspace
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        cd /path/to/workspace/EtendoERP
        ```

    2. Add GitHub credentials to `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    3. Expand Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```

    4. Apply the local template:
        ```bash title="Terminal"
        ./gradlew setup.applyTemplates --template=local
        ```
        When prompted, enter your **OpenAI API Key**.

    5. Run the installation:
        ```bash title="Terminal"
        ./gradlew install smartbuild
        ```

    6. Start Tomcat:
        ```bash title="Terminal"
        sudo /etc/init.d/tomcat start
        ```

    7. Open the browser and navigate to `http://localhost:8080/etendo`.

=== ":material-server: Server"

    1. Clone the Etendo Base project:
        ```bash title="Terminal"
        cd /opt/
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        cd /opt/EtendoERP
        ```

    2. Add GitHub credentials to `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    3. Expand Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```

    4. Apply the server template:
        ```bash title="Terminal"
        ./gradlew setup.applyTemplates --template=server
        ```
        When prompted, provide:

        - **Etendo ERP URL** — the full address of your installation (e.g., `http://myserver.com/etendo`). The context name and host are derived automatically.
        - **OpenAI API Key** — your key for Copilot integration (input is masked).

    5. Run the installation:
        ```bash title="Terminal"
        ./gradlew install smartbuild
        ```

    6. Start Tomcat:
        ```bash title="Terminal"
        sudo /etc/init.d/tomcat start
        ```

    7. Open the browser and navigate to `https://<Public server IP>/<Context Name>`.

!!! info
    For more details on available templates, options, and advanced usage see the [Setup Apply Templates guide](../developer-guide/etendo-classic/how-to-guides/how-to-use-setup-apply-templates.md).

## Advanced Features

### Interactive Installation Process

For a fully guided, step-by-step installation with per-property prompts and a confirmation summary, use the interactive configuration assistant instead of `setup.applyTemplates`.

#### Prepare the Environment

Choose the installation format and prepare the base files:

=== ":octicons-file-zip-24: Source Format"

    1. Clone Etendo Base project in `/opt` directory:
        ```bash title="Terminal"
        cd /opt/
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Move to the installation directory:
        ```bash title="Terminal"
        cd /opt/EtendoERP
        ```

    3. Add GitHub credentials to `gradle.properties` file:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Expand Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```
=== ":material-language-java: JAR Format"

    1. Clone Etendo Base project in `/opt` directory:
        ```bash title="Terminal"
        cd /opt/
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Move to the installation directory:
        ```bash title="Terminal"
        cd /opt/EtendoERP
        ```

    3. Add GitHub credentials to `gradle.properties` file:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Uncomment the core dependency in `build.gradle`:
        ```groovy title="build.gradle"
        implementation('com.etendoerp.platform:etendo-core:<version>')
        ```

=== ":material-docker: Docker Format"

    1. Clone Etendo Base project in `/opt` directory:
        ```bash title="Terminal"
        cd /opt/
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Move to the installation directory:
        ```bash title="Terminal"
        cd /opt/EtendoERP
        ```

    3. Add GitHub credentials to `gradle.properties` file:
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

#### Start Interactive Configuration

Launch the interactive configuration assistant:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

#### Navigate the Configuration Menu

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

#### Configure Properties

When selecting a configuration group, you will be guided through each property, for example:

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

#### Review Configuration Summary

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

#### Complete Installation

After confirming the configuration:

1. **Properties are saved** to `gradle.properties` (with automatic backup).
2. **Traditional setup runs** automatically.
3. **Installation continues** with the configured settings.

Complete the installation process:

=== ":octicons-file-zip-24: Source Format"

    ```bash title="Terminal"
    # Installation
    ./gradlew install smartbuild

    # Start Tomcat
    sudo /etc/init.d/tomcat start
    ```

=== ":material-language-java: JAR Format"

    ```bash title="Terminal"
    # Dependencies
    ./gradlew dependencies

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

#### Access Your Installation

Open the browser and navigate to:

- **Standard Installation**: `https://<Public server IP>/<Context Name>`
- **Local Development**: `http://localhost:8080/etendo`

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
### Custom Modules Properties Configuration

If your project includes custom modules with a `config.gradle` file, their configuration properties are added automatically to the interactive setup. Property names are preserved exactly as declared in `config.gradle`, and custom keys in `gradle.properties` are supported.

!!! info 
    Visit the [Developer Guide](../developer-guide/etendo-classic/developer-tools/etendo-interactive-configuration.md) for details about Interactive Configuration to custom modules.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
