---
tags:
    - Copilot
    - Tools
    - Documentation
    - Index
---

# Available Tools - Complete List

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

This document provides a comprehensive list of all available tools in the Etendo Copilot ecosystem. Each tool is designed to extend the capabilities of the Copilot assistant, enabling it to perform specific tasks and interact with various systems and services.

!!!info
    To be able to include most of these functionalities, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Tools Categories

### 🔧 System Integration Tools

| Tool Name | Description | Key Features |
|-----------|-------------|--------------|
| [API Call Tool](api-call-tool.md) | Execute HTTP API calls to external services | REST API integration, authentication support |
| [Client Init Tool](client-init-tool.md) | Initialize client configurations | Client setup, configuration management |
| [Docker Tool](docker-tool.md) | Manage Docker containers and images | Container lifecycle, image management |
| [Load OAuth Token Tool](load-oauth-token-tool.md) | Securely fetch and manage OAuth tokens | Token management, secure authentication |
| [Org Init Tool](org-init-tool.md) | Initialize organization settings | Organization setup, configuration |

### 📁 File Management Tools

| Tool Name | Description | Key Features |
|-----------|-------------|--------------|
| [Attach File Tool](attach-file-tool.md) | Attach files to conversations or processes | File attachment, metadata handling |
| [File Copy Tool](file-copy-tool.md) | Copy files between locations | File operations, path management |
| [File Downloader Tool](file-downloader-tool.md) | Download files from URLs | HTTP downloads, file saving |
| [Print Directory Tool](print-directory-tool.md) | List and display directory contents | Directory navigation, file listing |
| [Read File Tool](read-file-tool.md) | Read contents of text files | File reading, content extraction |
| [Uncompress Tool](uncompress-tool.md) | Extract compressed files and archives | Archive extraction, multiple formats |
| [Write File Tool](write-file-tool.md) | Write and edit text files | File creation, content writing, backups |

### 🧠 AI & Data Processing Tools

| Tool Name | Description | Key Features |
|-----------|-------------|--------------|
| [Audio Tool](audio-tool.md) | Process and analyze audio files | Audio processing, speech recognition |
| [Memory Tool](memory-tool.md) | Manage persistent memories using vector database | CRUD operations, semantic search, user isolation |
| [OCR Tool](ocr-tool.md) | Optical Character Recognition for images | Text extraction, image processing |
| [PDF to Images Tool](pdf-to-images-tool.md) | Convert PDF pages to image formats | PDF processing, image conversion |
| [Tavily Tool](tavily-tool.md) | Perform web searches using Tavily search engine | Internet search, information retrieval |

### 📊 Document & Spreadsheet Tools

| Tool Name | Description | Key Features |
|-----------|-------------|--------------|
| [Google Drive Tool](google-drive-tool.md) | Interact with Google Drive services | Cloud storage, file management |
| [Google Spreadsheet Tool](google-spreadsheet-tool.md) | Manage Google Sheets documents | Spreadsheet operations, data manipulation |
| [Template Tool](template-tool.md) | Generate documents from templates | Template processing, document generation |
| [XLS Tool](xls-tool.md) | Handle Excel spreadsheet files | Excel processing, data extraction |

### 📧 Communication Tools

| Tool Name | Description | Key Features |
|-----------|-------------|--------------|
| [Send Email Tool](send-email-tool.md) | Send emails through configured services | Email delivery, attachment support |

### 🏗️ Development & Testing Tools

| Tool Name | Description | Key Features |
|-----------|-------------|--------------|
| [Codbar Tool](codbar-tool.md) | Generate and process barcodes | Barcode generation, various formats |
| [Process Definition Jasper Tool](process-definition-jasper-tool.md) | Handle Jasper report definitions | Report processing, definition management |
| [Task Creator Tool](task-creator-tool.md) | Create and define new tasks | Task creation, workflow management |
| [Task Management Tool](task-management-tool.md) | Manage existing tasks and workflows | Task operations, status management |
| [Test Run Tool](test-run-tool.md) | Execute tests and validation procedures | Test execution, result reporting |

### 🌐 Translation & Localization Tools

| Tool Name | Description | Key Features |
|-----------|-------------|--------------|
| [XML Translation Tool](xml-translation-tool.md) | Translate XML content and structure | XML processing, translation services |

## Tool Selection Guidelines

### When to Use Each Tool

#### For File Operations
- Use **Read File Tool** when you need to examine file contents
- Use **Write File Tool** when creating or modifying files
- Use **File Copy Tool** for duplicating files
- Use **File Downloader Tool** for fetching remote files

#### For Data Processing
- Use **Memory Tool** for persistent information storage across conversations
- Use **OCR Tool** for extracting text from images
- Use **Audio Tool** for speech and audio analysis
- Use **Tavily Tool** for web search and information gathering

#### For Integration
- Use **API Call Tool** for REST API interactions
- Use **Google Drive Tool** and **Google Spreadsheet Tool** for Google Workspace integration
- Use **Send Email Tool** for notifications and communication
- Use **Load OAuth Token Tool** for secure authentication

#### For Development
- Use **Task Creator Tool** and **Task Management Tool** for workflow automation
- Use **Test Run Tool** for validation and testing
- Use **Docker Tool** for containerized environments

## Best Practices

### Security Considerations
- Always validate input parameters before using tools
- Use appropriate authentication mechanisms (OAuth tokens, API keys)
- Ensure user permissions are respected for file operations
- Sanitize file paths and URLs to prevent security vulnerabilities

### Performance Optimization
- Cache frequently accessed data using the Memory Tool
- Use batch operations when possible (e.g., multiple file operations)
- Consider file size limitations for processing tools
- Optimize search queries for better performance

### Error Handling
- Always check tool responses for error conditions
- Implement fallback mechanisms for critical operations
- Log errors appropriately for debugging
- Provide meaningful error messages to users

## Configuration Requirements

Most tools require specific configuration settings:

### Environment Variables
- API keys for external services (Tavily, Google APIs)
- Authentication tokens and credentials
- File system permissions (`COPILOT_WRITE_RULE`)
- Service endpoints and URLs

### Dependencies
- Chroma vector database for Memory Tool
- Docker runtime for Docker Tool
- Python libraries for various processing tools
- Network access for API and download tools

## Support and Troubleshooting

For issues with specific tools:

1. Check the individual tool documentation for configuration requirements
2. Verify all required environment variables are set
3. Ensure proper permissions for file system operations
4. Validate network connectivity for external service tools
5. Review error logs for detailed debugging information

For additional support, refer to the [Etendo Copilot Documentation](../../../index.md) or contact the development team.
