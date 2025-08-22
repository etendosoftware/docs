---
title: How to Install Etendo Main UI
status: beta
tags:
  - Development
  - Installation
  - Main UI
  - Docker
  - Etendo Classic
---

# How to Install Etendo Main UI

## Overview

!!!warning "Beta Version"
    **IMPORTANT: THIS IS A BETA VERSION**
    
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

This guide provides instructions to install and run the Etendo Main UI, a modern React/TypeScript-based user interface that provides a new frontend experience for EtendoERP. The Main UI runs as a containerized service alongside your Etendo Classic instance.

## Requirements

1. **Etendo Classic** project properly set up
2. This project depends on the following tools:
    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: version `26.0.0` or higher
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: version `2.26.0` or higher
3. **Java** properly configured for Gradle tasks
4. **Git** for version control

!!!info
    The [Docker Management](../../../etendo-classic/bundles/platform/docker-management.md) module, included as a dependency allows for the distribution of the infrastructure within Etendo modules, which include Docker containers for each service.

## Installation

Etendo Main UI is distributed within the [Platform Extensions](../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) bundle, which includes the **Main UI Infrastructure** and all required backend modules for the new interface.

!!!info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Platform Extensions - Release notes](../../../etendo-classic/bundles/platform/overview.md).

## Running Etendo Main UI

The simplest configuration we are going to follow as an example is to mount Main UI Dockerized and Tomcat running as a local service. Other configurations are detailed in the section, [Advanced Configurations](#advanced-development-setup).


```bash
cd modules
git clone <repository_url>
```

### 1. Configure Services

Add the following lines to your `gradle.properties` file:

```properties
docker_com.etendoerp.mainui=true
ETENDO_CLASSIC_URL=http://your.etendo.instance/etendo
```

Replace `your.etendo.instance` with your actual Etendo Classic URL.

#### If Running Etendo Classic via Docker

To enable Docker services for Etendo Classic, also add these lines:

```properties
docker_com.etendoerp.docker_db=true
docker_com.etendoerp.tomcat=true
```

### 2. Set Up the Module

Run the following commands to set up the module and update resources:

```bash
./gradlew setup
./gradlew resources.up
```

### 3. Start Services

Start the Docker services:

```bash
./gradlew resources.up
```

This will start the Main UI container along with any other configured Docker services.

### 4. (If Running in Docker) Set Up the Database

If this is your first time running Etendo Classic via Docker, install the database:

```bash
./gradlew install
```

!!!note "Installation Note"
    The `install` task is only needed if running Etendo Classic via Docker for the first time.

## Accessing the Main UI

Once all services are running, the Main UI will be available at:

`http://localhost:3000` (default port)

The exact URL may vary depending on your Docker configuration.

## Troubleshooting

### Common Issues

**Services not starting:**

- Ensure Docker and Docker Compose are properly installed and running
- Check that required ports are not already in use
- Verify your `gradle.properties` configuration

**Authentication issues:**

- Confirm that the Platform Extensions Bundle is properly installed
- Verify that all required modules are active
- Check that the `ETENDO_CLASSIC_URL` points to your running Etendo Classic instance

**Database connection problems:**

- Ensure the database service is running if using Docker
- Verify database credentials and connection settings
- Check Docker logs for specific error messages

### Getting Help

If you encounter issues during installation:

1. Check the Docker logs: `docker-compose logs`
2. Verify all requirements are met
3. Ensure the Platform Extensions Bundle is properly installed
4. Review the configuration in `gradle.properties`

## Advanced Configuration

For developers who need to set up a development environment to work directly on the Main UI codebase, see the [Advanced Development Setup](#advanced-development-setup) section below.

---

# Advanced Development Setup

This section is for developers who want to contribute to or customize the Main UI codebase directly.

## Requirements for Development

1. **Node.js** version ^18.0.0 or higher
2. **pnpm** version ^9.15.2 (package manager)
3. All requirements from the basic installation above

## Manual Module Installation (Development Only)

For development environments, you may need to install the required modules manually:

- `com.etendoerp.openapi`
- `com.etendoerp.etendorx`
- `com.etendoerp.metadata`
- `com.etendoerp.metadata.template`

### Quick Clone Commands

```bash
cd modules

# Clone required modules for development
git clone git@github.com:etendosoftware/com.etendoerp.etendorx.git
git clone git@github.com:etendosoftware/com.etendoerp.metadata.git
git clone git@github.com:etendosoftware/com.etendoerp.metadata.template.git
```

!!!note "OpenAPI Module"
    The `com.etendoerp.openapi` module should be installed through the standard Etendo module installation process.

### Development Configuration

After installing `com.etendoerp.etendorx`, configure the authentication manager by adding the following line to your `Openbravo.properties` file:

```properties
authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
```

## Development Project Structure

The workspace is organized as a monorepo with multiple packages:

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

## Development Installation Steps

### 1. Clone the Development Repository

Clone the Main UI development repository:

```bash
git clone https://github.com/etendosoftware/com.etendorx.workspace-ui.git
cd com.etendorx.workspace-ui
```

### 2. Install Dependencies

Install all project dependencies using pnpm:

```bash
pnpm install
```

This command will install dependencies for all packages in the workspace.

### 3. Environment Configuration

Create environment configuration files for development:

Create a `.env.local` file in the `packages/MainUI` directory:

```bash
cd packages/MainUI
touch .env.local
```

Add your backend configuration:

```env
NEXT_PUBLIC_BACKEND_URL=http://localhost:8080/etendo
NEXT_PUBLIC_API_BASE_URL=http://localhost:8080/etendo
```

Replace the URLs with your actual EtendoERP backend URLs.

### 4. Build Dependencies

Build the required packages in the correct order:

```bash
# Build API Client first (dependency for other packages)
pnpm --filter @workspaceui/api-client build

# Build Component Library
pnpm --filter @workspaceui/componentlibrary build
```

### 5. Start Development Server

Launch the development server for the Main UI:

```bash
pnpm dev
```

The application will be available at `http://localhost:3000` by default.

## Development Workflow

### Root-Level Commands (Recommended)

The workspace provides convenient aliases at the root level for common tasks:

```bash
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

### Individual Package Commands

Each package can also be run independently using pnpm workspace commands:

```bash
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

### Linting and Formatting

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

## Package Details

### API Client (`@workspaceui/api-client`)

Contains TypeScript definitions and API functions for communicating with the EtendoERP backend. Provides:

- Authentication APIs
- Metadata APIs
- Datasource APIs
- Copilot integration APIs

### Component Library (`@workspaceui/componentlibrary`)

A collection of reusable React components built with Material-UI. Includes:

- Form components (inputs, selectors, etc.)
- Navigation components
- Modal and dialog components
- Data display components

### Main UI (`@workspaceui/mainui`)

The main Next.js application that provides the complete user interface. Features:

- Modern React/TypeScript architecture
- Server-side rendering with Next.js
- Material-UI theme integration
- Responsive design

## Development Troubleshooting

### Common Development Issues

**Dependencies not installing properly:**

- Ensure you're using pnpm version ^9.15.2
- Clear node_modules and reinstall: `rm -rf node_modules && pnpm install`

**Build failures:**

- Make sure to build packages in the correct order (api-client first, then component-library)
- Check that all peer dependencies are satisfied

**Backend connection issues:**

- Verify your `.env.local` configuration
- Ensure the EtendoERP backend is running and accessible
- Check that the required backend modules are installed and active

**Authentication problems:**

- Confirm the authentication manager is properly configured in `Openbravo.properties`
- Verify that the metadata module is installed and active

## Next Steps for Development

After successful development setup:

1. **Explore the Component Library:** Navigate to the ComponentLibrary package to see available components
2. **Review the API Documentation:** Check the api-client package for available APIs
3. **Start Development:** Begin customizing or extending the UI components
4. **Run Tests:** Execute the test suites to ensure everything works correctly

```bash
# Run all tests
pnpm test

# Build for production
pnpm build
```

The development environment is now ready for building and customizing the Etendo Main UI.

---

!!!warning "Beta Version Notice"
    Remember that this is a beta version under active development. Features may change, and the API is not yet stable. Always backup your work and test thoroughly before deploying any customizations.