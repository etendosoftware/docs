---
tags:
    - Copilot
    - IA
    - Tool
    - File Copy
---

# File Copy Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **File Copy Tool** receives two paths: one from a file and one from a directory. Its function is to copy the specified file to the specified directory and return the path of the copied file.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool is useful when you need to duplicate files in different locations within the file system. This can be essential for backup tasks, file organization, or preparing files for processing in specific locations. This simplifies the process of copying files and managing directories, ensuring the existence of the destination directory and providing clear feedback with the path of the copied file.

This process consists of the following actions:

- **Receiving Parameters**

    The tool receives an input object containing two keys:

    - `source_path`: path to the source file to be copied.
    - `destination_directory`: path to the destination directory where you want to copy the file.

- **Creating the Output Directory**

    If the output directory does not exist, the tool automatically creates it to ensure that the copy operation does not fail due to a missing path.

- **Copying the file**

    Use Python's `shutil.copy` function to copy the source file to the target directory.

- **Returning the Result**

    Once the process is complete, the tool returns an object containing the full path to the copied file in the output directory.

## Usage Example

If you have a file in `/home/user/file.txt` and you want to copy it to the `/home/user/destination_directory` directory, you would use the tool as follows:

- **Input**
```
{"source_path": "/home/user/file.txt", "destination_directory": "/home/user/destination_directory"}
```

- **Output**
```
{"file_path": "/home/user/destination_directory/file.txt"}
```