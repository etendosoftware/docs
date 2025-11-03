---
title: Install Etendo Main UI
tags:
  - Development
  - Installation
  - Main UI
  - Docker
  - Etendo
status: beta
---

# Install Etendo Main UI

## Overview

!!! example " **IMPORTANT: THIS IS A BETA VERSION**"
    - It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**, especially in production environments.
    - It should be used with **caution**, and you should always **validate backups** before executing any critical operation.

This guide provides instructions to install and run the Etendo Main UI, a modern React/TypeScript-based user interface that provides a new frontend experience for Etendo. The Main UI runs as a containerized service alongside your Etendo instance.

## Requirements

1. **Etendo** project properly set up.
2. This project depends on the following tools:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: version `26.0.0` or higher
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: version `2.26.0` or higher

    !!! info
        The [Docker Management](../../bundles/platform/docker-management.md) module, included as a dependency, allows for the distribution of the infrastructure within Etendo modules, which include Docker containers for each service.

## Installation

Etendo Main UI is distributed within the [Platform Extensions](../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) bundle, which includes the **Main UI Infrastructure** and all required backend modules for the new interface.

!!!info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](../../bundles/platform/overview.md).

## Running Etendo Main UI

The simplest configuration we are going to follow as an example is to mount **Main UI Dockerized** and **Tomcat** running as a local service. Other configurations are detailed in the section [Advanced Configurations](#advanced-configuration).

1. Add the following lines to the `gradle.properties` file:

    ``` title="gradle.properties"
    docker_com.etendoerp.mainui=true
    ETENDO_CLASSIC_URL=http://your.etendo.instance/etendo
    authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
    ws.maxInactiveInterval=seconds-number
    ```

    !!! warning
        The `ws.maxInactiveInterval` variable accepts numeric values representing the seconds a session will last before expiring in the new Main UI interface. Note that this configuration is also used by Secure Web Services and does not affect session expiration in the classic Etendo interface. The recommended value is 3600, representing one hour, but you can modify the value as needed.

2. Replace `your.etendo.instance` with your actual Etendo URL.

    For example: 

    ``` title="Etendo URL"
    docker_com.etendoerp.mainui=true
    ETENDO_CLASSIC_URL=http://localhost:8080/etendo
    authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
    ws.maxInactiveInterval=3600
    ```

3. Run the following commands to set up the module and update resources:

    ```bash
    ./gradlew setup
    ./gradlew resources.up
    ```

4. Start the Docker services:

    ```bash
    ./gradlew resources.up
    ```

This will start the **Main UI** container along with any other configured Docker services.


## Accessing the Main UI

Once all services are running, the Main UI will be available at:

[http://localhost:3000](http://localhost:3000) (default port)

!!!info
    The exact URL may vary depending on your Docker configuration.

## Advanced Configuration

This section is for developers who want to contribute to or customize the **Main UI** codebase directly.

### Requirements for Development

1. **Node.js** version ^18.0.0 or higher
2. **pnpm** version ^9.15.2 (package manager)
3. All requirements from the basic installation above.

### Manual Module Installation (Development Only)

For development environments, you need to install the required modules manually:

- `com.etendoerp.openapi`
- `com.etendoerp.etendorx`
- `com.etendoerp.metadata`
- `com.etendoerp.metadata.template`

**Quick Clone Commands**

```bash
cd modules

# Clone required modules for development
git clone git@github.com:etendosoftware/com.etendoerp.etendorx.git
git clone git@github.com:etendosoftware/com.etendoerp.openapi.git 
git clone git@github.com:etendosoftware/com.etendoerp.metadata.git
git clone git@github.com:etendosoftware/com.etendoerp.metadata.template.git
```

### Development Project Structure

The workspace is organized as a unique environment with multiple packages:

```
com.etendorx.workspace-ui/
├── packages/
│   ├── api-client/          # API client for backend communication
│   ├── ComponentLibrary/    # Reusable UI components
│   └── MainUI/             # Main application
├── package.json
├── pnpm-workspace.yaml
└── README.md
```

### Development Installation Steps

1. Clone the Main UI development repository:

    ```bash
    git clone https://github.com/etendosoftware/com.etendorx.workspace-ui.git
    cd com.etendorx.workspace-ui
    ```

2. Install all project dependencies using `pnpm`:

    ```bash
    pnpm install
    ```

    This command will install dependencies for all packages in the workspace.

3. Create a `.env.local` file in the `packages/MainUI` directory:

    ```bash
    cd packages/MainUI
    touch .env.local
    ```

4. Add your backend configuration:

    ```env
    NEXT_PUBLIC_BACKEND_URL=http://localhost:8080/etendo
    NEXT_PUBLIC_API_BASE_URL=http://localhost:8080/etendo
    ```
    !!!info
        Replace the URLs with your actual Etendo backend URLs.

5. Build the required packages in the correct order:

    ```bash
    # Build API Client first (dependency for other packages)
    pnpm --filter @workspaceui/api-client build

    # Build Component Library
    pnpm --filter @workspaceui/componentlibrary build
    ```

6. Launch the development server for the Main UI:

    ```bash
    pnpm dev
    ```

    The application will be available at [http://localhost:3000](http://localhost:3000) by default.

### Development Workflow

**Root-Level Commands (Recommended)**

The workspace provides convenient aliases at the root level for common tasks:

```bash title="Aliases"
# Start Main UI development server
pnpm dev

# Build all packages
pnpm build

# Run tests across all packages
pnpm test

# Lint all packages
pnpm lint

# Fix lint issues automatically
pnpm lint:fix

# Format code across all packages
pnpm format

# Auto-fix formatting issues
pnpm format:fix

# Clean all build artifacts
pnpm clean

# Install dependencies
pnpm install
```

**Individual Package Commands**

Each package can also be run independently using pnpm workspace commands:

```bash title="Commands"
# Run MainUI development server
pnpm --filter @workspaceui/mainui dev

# Build API Client
pnpm --filter @workspaceui/api-client build

# Build Component Library
pnpm --filter @workspaceui/componentlibrary build

# Run tests for API Client
pnpm --filter @workspaceui/api-client test

# Lint specific package
pnpm --filter @workspaceui/mainui lint
```

**Linting and Formatting**

The project uses Biome for linting and formatting across all packages:

```bash
# Lint all packages
pnpm lint

# Fix lint issues
pnpm lint:fix

# Format code
pnpm format

# Auto-fix formatting
pnpm format:fix
```

### Package Details

**API Client (`@workspaceui/api-client`)**

Contains TypeScript definitions and API functions for communicating with the Etendo backend. Provides:

- Authentication APIs
- Metadata APIs
- Datasource APIs
- Copilot integration APIs

**Component Library (`@workspaceui/componentlibrary`)**

A collection of reusable React components built with Material-UI. Includes:

- Form components (inputs, selectors, etc.)
- Navigation components
- Modal and dialog components
- Data display components

**Main UI (`@workspaceui/mainui`)**

The main Next.js application that provides the complete user interface. Features:

- Modern React/TypeScript architecture
- Server-side rendering with Next.js
- Material-UI theme integration
- Responsive design


### Run Tests

Execute the test suites to ensure everything works correctly

```bash
# Run all tests
pnpm test

# Build for production
pnpm build
```

The development environment is now ready for building and customizing the Etendo Main UI.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.