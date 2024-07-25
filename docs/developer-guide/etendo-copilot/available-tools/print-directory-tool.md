---
tags:
    - Copilot
    - IA
    - Tool
    - Print
    - Directory
---

# Print Directory Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Print Directory Tool** is a tool designed to print files and directories from the current directory or from a specified upstream directory. It allows the option to list the contents recursively.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).
    
This tool is extremely valuable for file system management and monitoring. It makes it easy to view the directory structure, either locally or upwards, and allows for detailed audits of the structure. Its ability to ignore specific directories common in development environments ensures that listings are relevant and clean, making the tool efficient and practical.

## Functionality

This tool is used when you need to get a clear view of the file and directory structure in a specific directory on the system, either the current directory or one of its parent directories. It can be useful for:

- Auditing and reviewing the file structure.
- Automate operations that depend on the existence of certain files.
- Obtain directory listings for further processing.

This process consists of the following actions:

- **Receiving Parameters**

    The tool receives two key parameters:

    - Recursive (boolean): It indicates whether to list subdirectories recursively.
    - `parent_doubledot_qty` (integer): It specifies how many parent directories to ascend from the current directory.

    **Input example**

    ```
    {
    "recursive": true,
    "parent_doubledot_qty": 2
    }
    ```

    Calculation of the Directory to List:

    - Calculates the directory path based on the number of parents specified.
    - For example, if `parent_doubledot_qty` is 2, it will go up two levels from the current directory (../../).

- **Directory list**

    - If recursive is True, it will use `os.walk` to list all files and subdirectories recursively.
    - If recursive is False, it will use `os.listdir` to list only the contents of the specified directory.

- **Returning the Result**

    It returns a dictionary with the list of files and directories under the message key.

## Usage Example

If you want to recursively list the files and directories in the grandparent directory of the current directory:

- **Input**
```
{ "recursive": true, "parent_doubledot_qty": 2 }
```
- **Output**
```
{ "message": ["/path/to/parent/dir/file1", "/path/to/parent/dir/subdir/file2", ...] }
```