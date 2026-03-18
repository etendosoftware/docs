---
tags:
  - Getting Started
  - Installation
  - Server
  - Production
  - ISO
---

# Install Etendo - Server Installation

## Overview

This guide covers installing Etendo on a production server using the **Etendo ISO**, which automates the operating system setup and base environment configuration. Copilot and Main UI are included in the base installation and are configured as part of this process.

## Prerequisites

- [GitHub credentials](use-of-repositories-in-etendo.md)
- **OpenAI API Key** — required for Copilot. Use your own key from [OpenAI](https://platform.openai.com/account/api-keys){target="_blank"} or contact [Etendo](https://etendo.software){target="_blank"} to get one. For details on supported providers, see the [Copilot Installation guide](../../../etendo-copilot/installation.md#configuration-variables).

!!! info
    The ISO configures the full stack (OS, PostgreSQL, Docker, Tomcat) automatically. No additional system setup is required.

## Installation

### 1. Download the ISO

Download the latest Etendo ISO from the [Etendo ISO - Release Notes](../../../../whats-new/release-notes/etendo-classic/iso.md) page.

### 2. Provision the Server

How you use the ISO depends on your infrastructure:

- **Bare metal / physical server**: burn the ISO to a USB drive using [balenaEtcher](https://etcher.balena.io/#download-etcher){target="_blank"} (Linux/macOS) or [Rufus](https://rufus.ie/en/){target="_blank"} (Windows), then boot from the USB.
- **AWS**: an official Etendo AMI is published alongside each ISO release. Find the AMI ID in the [Etendo ISO - Release Notes](../../../../whats-new/release-notes/etendo-classic/iso.md) page, then [launch a new EC2 instance from it](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html){target="_blank"}.
- **Hetzner Cloud**: upload the ISO as a custom image from the Hetzner Cloud Console and create a new server from it. Refer to the [Hetzner documentation](https://docs.hetzner.com){target="_blank"} for details.
- **Scaleway**: upload the ISO and use [custom boot modes](https://www.scaleway.com/en/docs/instances/how-to/use-boot-modes/){target="_blank"} to provision an instance from it.
- **Other cloud providers**: upload the ISO as a custom image and create a new instance from it. Refer to your provider's documentation for importing custom OS images.
- **Virtual machine**: mount the ISO directly in your hypervisor. [Qemu](https://www.qemu.org/download/){target="_blank"} with [Virt-Manager (Linux)](https://virt-manager.org/download.html){target="_blank"} or [UTM (macOS)](https://mac.getutm.app/){target="_blank"} are recommended options.

### 3. Boot and Install the OS

Start the system from the ISO. Follow the prompts:

- **Network Connections**: verify an IP address is correctly assigned and internet access is available.
- **Storage Configuration**: select the target disk.
- **Profile Setup**: enter your name, server name, and a password for the `etendo` user.

Wait for the operating system installation and server upgrade to complete. When prompted, select **Reboot Now**.

After the restart, the final server configuration runs automatically. Wait for it to complete — the base environment will be ready.

!!! info "Installing without internet connection"
    If no internet connection is available during installation, select **Continue without internet** at the network configuration step. After the OS installation and reboot, configure the network, connect to the internet, log in as superuser (`sudo su`), and run `etendo-install`.

### 4. Add GitHub Credentials

Once the server is ready, navigate to the project directory and add your GitHub credentials to `gradle.properties`. To generate them, follow the [Use of Repositories in Etendo](use-of-repositories-in-etendo.md) guide.

```bash title="Terminal"
cd /opt/EtendoERP
```

```groovy title="gradle.properties"
githubUser=<username>
githubToken=<*******>
```

### 5. Apply the Server Template

Run the following task to configure all required variables for the server environment:

```bash title="Terminal"
./gradlew setup.applyTemplates --template=server
```

When prompted, provide:

- **Etendo ERP URL** — the full URL of your installation (e.g., `http://myserver.com/etendo`). The context name and host are derived automatically.
- **OpenAI API Key** — your key for Copilot integration (input is masked).

!!! info
    For details about available templates, options, and advanced usage, see the [How to Use Setup Apply Templates](../../how-to-guides/how-to-use-setup-apply-templates.md) guide.

!!! tip "Alternative: Interactive Setup"
    For a fully guided, property-by-property configuration, run the interactive setup instead:
    ```bash
    ./gradlew setup -Pinteractive=true --console=plain
    ```
    For more details, see the [How to Use the Interactive Setup](../../how-to-guides/how-to-use-interactive-setup.md) guide.

### 6. Compile and Deploy

```bash title="Terminal"
./gradlew update.database smartbuild --info
```

### 7. Configure Apache

From the `/opt/EtendoERP` directory, run the Apache configuration script:

```bash title="Terminal"
cd utils
sudo ./apache-config.sh <domain>
```

This configures Apache as a reverse proxy for the server. Once complete, the Main UI and Classic UI URLs are set automatically based on the domain provided.

### 8. Start Docker Services

```bash title="Terminal"
./gradlew resources.up
```

This starts the **Copilot** and **Main UI** containers.

### 9. Start Tomcat

```bash title="Terminal"
sudo /etc/init.d/tomcat start
```

## Access the Installation

Once all services are running:

| Interface | URL |
|---|---|
| **Main UI** | `https://<server-address>/` |
| **Classic UI** | `https://<server-address>/<context-name>` |

!!! tip "Default credentials"
    User: `admin`
    Password: `admin`

    Change the default password immediately after the first login in a production environment.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
