---
tags:
  - Development
  - Installation
  - Main UI
  - Workspace UI
  - React
  - TypeScript
---

# How to Install Etendo Main UI for Development

## Overview

**IMPORTANT: THIS IS A BETA VERSION**

It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

This guide provides step-by-step instructions to clone and set up the Etendo Main UI repository for development purposes. The Etendo Main UI is a modern React/TypeScript-based user interface that provides a new frontend experience for EtendoERP.

## Prerequisites

Before starting the installation, ensure you have the following requirements:

- **Node.js** version ^18.0.0 or higher
- **pnpm** version ^9.15.2 (package manager)
- **Git** for version control
- **EtendoERP** backend with the required modules installed:
  - `com.etendoerp.metadata` 
  - `com.etendoerp.openapi`
  - `com.etendoerp.etendorx`
  - `com.etendoerp.metadata.template`

## Project Structure

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

## Installation Steps

### 1. Clone the Repository

Clone the Etendo Workspace UI repository to your local machine:

```bash
git clone https://github.com/etendosoftware/com.etendorx.workspace-ui.git
cd com.etendorx.workspace-ui
```

### 2. Install Dependencies

Install all project dependencies using pnpm:

```bash
pnpm install
```

This command will install dependencies for all packages in the workspace, including:
- Main UI application dependencies
- Component Library dependencies  
- API Client dependencies
- Development tools and TypeScript types

### 3. Backend Configuration

Configure your EtendoERP backend to work with the new UI:

Add the following configuration to your `Openbravo.properties` file:

```properties
authentication.class=com.etendoerp.metadata.auth.AuthenticationManager
```

This configuration enables token-based authentication required by the new frontend.

### 4. Environment Setup

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

### 5. Build Packages

Build the required packages in the correct order:

```bash
# Build API Client first (dependency for other packages)
pnpm --filter @workspaceui/api-client build

# Build Component Library
pnpm --filter @workspaceui/componentlibrary build
```

### 6. Start Development Server

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

## Troubleshooting

### Common Issues

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

### Getting Help

If you encounter issues during installation or development:

1. Check the console output for specific error messages
2. Verify all prerequisites are met
3. Ensure the backend modules are properly installed
4. Review the environment configuration

## Next Steps

After successful installation:

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