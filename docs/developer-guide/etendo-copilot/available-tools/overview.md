---
title: Available Tools - Overview
tags:
    - Copilot
    - Tools
    - Documentation
    - Index
---

# Available Tools - Overview

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

This document provides a comprehensive list of all available tools in the **Etendo Copilot** ecosystem. Each tool is designed to extend the capabilities of the Copilot assistant, enabling it to perform specific tasks and interact with various systems and services.

!!!info
    To be able to include most of these functionalities, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Tools Categories

### System Integration Tools

| Tool Name | Description | Key Features | When to Use |
|-----------|-------------|--------------|-------------|
| [API Call Tool](api-call-tool.md) | Execute HTTP API calls to external services | REST API integration, authentication support | Use for REST API interactions |
| [Client Init Tool](client-init-tool.md) | Initialize client configurations | Client setup, configuration management |  |
| [Docker Tool](docker-tool.md) | Manage Docker containers and images | Container lifecycle, image management | Use for containerized environments |
| [Load OAuth Token Tool](load-oauth-token-tool.md) | Securely fetch and manage OAuth tokens | Token management, secure authentication | Use for secure authentication |
| [Org Init Tool](org-init-tool.md) | Initialize organization settings | Organization setup, configuration |  |

### File Management Tools

| Tool Name | Description | Key Features | When to Use |
|-----------|-------------|--------------|-------------|
| [Attach File Tool](attach-file-tool.md) | Attach files to conversations or processes | File attachment, metadata handling |  |
| [File Copy Tool](file-copy-tool.md) | Copy files between locations | File operations, path management | Use for duplicating files |
| [File Downloader Tool](file-downloader-tool.md) | Download files from URLs | HTTP downloads, file saving | Use for fetching remote files |
| [Print Directory Tool](print-directory-tool.md) | List and display directory contents | Directory navigation, file listing |  |
| [Read File Tool](read-file-tool.md) | Read contents of text files | File reading, content extraction | Use to examine file contents |
| [Uncompress Tool](uncompress-tool.md) | Extract compressed files and archives | Archive extraction, multiple formats |  |
| [Write File Tool](write-file-tool.md) | Write and edit text files | File creation, content writing, backups | Use when creating or modifying files |

### AI & Data Processing Tools

| Tool Name | Description | Key Features | When to Use |
|-----------|-------------|--------------|-------------|
| [Audio Tool](audio-tool.md) | Process and analyze audio files | Audio processing, speech recognition | Use for speech and audio analysis |
| [Memory Tool](memory-tool.md) | Manage persistent memories using vector database | CRUD operations, semantic search, user isolation | Use for persistent information storage |
| [OCR Tool](ocr-tool.md) | Optical Character Recognition for images | Text extraction, image processing | Use for extracting text from images |
| [PDF to Images Tool](pdf-to-images-tool.md) | Convert PDF pages to image formats | PDF processing, image conversion |  |
| [Tavily Tool](tavily-tool.md) | Perform web searches using Tavily search engine | Internet search, information retrieval | Use for web search and information gathering |

### Document & Spreadsheet Tools

| Tool Name | Description | Key Features | When to Use |
|-----------|-------------|--------------|-------------|
| [Etendo SQL to CSV Tool](etendo-sql-to-csv-tool.md) | Execute SQL queries in Etendo and export results to CSV | Database queries, CSV export, security validation | Use for database queries and export |
| [Google Drive Tool](google-drive-tool.md) | Interact with Google Drive services | Cloud storage, file management | Use for Google Workspace integration |
| [Google Spreadsheet Tool](google-spreadsheet-tool.md) | Manage Google Sheets documents | Spreadsheet operations, data manipulation | Use for Google Workspace integration |
| [Template Tool](template-tool.md) | Generate documents from templates | Template processing, document generation |  |
| [XLS Tool](xls-tool.md) | Handle Excel spreadsheet files | Excel processing, data extraction |  |

### Communication Tools

| Tool Name | Description | Key Features | When to Use |
|-----------|-------------|--------------|-------------|
| [Send Email Tool](send-email-tool.md) | Send emails through configured services | Email delivery, attachment support | Use for notifications and communication |

### Development & Testing Tools

| Tool Name | Description | Key Features | When to Use |
|-----------|-------------|--------------|-------------|
| [Codbar Tool](codbar-tool.md) | Generate and process barcodes | Barcode generation, various formats |  |
| [Process Definition Jasper Tool](process-definition-jasper-tool.md) | Handle Jasper report definitions | Report processing, definition management |  |
| [Task Creator Tool](task-creator-tool.md) | Create and define new tasks | Task creation, workflow management | Use for workflow automation |
| [Task Management Tool](task-management-tool.md) | Manage existing tasks and workflows | Task operations, status management | Use for workflow automation |
| [Test Run Tool](test-run-tool.md) | Execute tests and validation procedures | Test execution, result reporting | Use for validation and testing |

### Translation & Localization Tools

| Tool Name | Description | Key Features | When to Use |
|-----------|-------------|--------------|-------------|
| [XML Translation Tool](xml-translation-tool.md) | Translate XML content and structure | XML processing, translation services |  |



!!! tip "Troubleshooting"

    For issues with specific tools:

    - Check the individual tool documentation for configuration requirements.
    - Verify all required environment variables are set.
    - Ensure proper permissions for file system operations.
    - Validate network connectivity for external service tools.
    - Review error logs for detailed debugging information.


