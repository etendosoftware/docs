---
tags:
    - Copilot
    - IA
    - Tool
    - Read
    - File
---

# Read File Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Read File Tool** is designed to read the contents of files given a filepath parameter. It provides a simple way to access the contents of text files on the local system.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool is especially useful to access the contents of a file for processing or viewing. It can be used in several situations, such as:

- Reading configuration files.
- Accessing logs and log files.
- Viewing or processing data stored in text files.

This process consists of the following actions.

- **Receiving Parameters**

    The tool receives an input parameter called `filepath` which is the path to the file to be read.

- **Reading File**
    - It opens the file specified by `filepath`.
    - It reads the entire contents of the file.

- **Returning the Result**
    It returns a dictionary with the contents of the file under the `message` key.

## Usage Example

If you want to read the contents of the `/tmp/test.txt` file:
    
- **Input**
```
{ "filepath": "/tmp/test.txt" }
```
- **Output**
```
{ "message": "Content of the read file..." }
```