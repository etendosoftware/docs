---
tags:
    - Copilot
    - IA
    - Tool
    - Uncompress files
---

# Uncompress Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Uncompress Tool** is a utility designed to uncompress various types of compressed files and return the paths of the uncompressed files. It supports common file types including `zip`, `gzip`, `bzip2`, and `rar`.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md){target="\_blank"}.

## Functionality

The primary purpose of the this tool is to streamline the process of extracting files from compressed formats. It is particularly useful in scenarios where automated file extraction is needed, such as data processing pipelines, backup restoration, and file management systems. By supporting multiple common compression formats and providing a straightforward interface for file extraction, it simplifies workflows involving compressed files and ensures efficient handling of data archives.

This process consists of the following actions.

- **Receiving Parameters**
    The tool expects a single input parameter:

    `compressed_file_path` : Path to the compressed file that needs to be uncompressed.

- **Determining the File Type**

    The tool inspects the file extension to determine the type of compressed file and selects the appropriate uncompression method.

- **Creating the Output Directory**

    The tool creates an output directory based on the name of the compressed file to store the uncompressed contents.

- **Uncompressing the File**

    The tool supports multiple compression formats and uses corresponding Python libraries to uncompress files:

    - `gzip` : Uses the `gzip` library to uncompress `.gz` files.

    - `bzip2` : Utilizes the `bz2` library to handle `.bz2` files.

    - `rar` : Employs the rarfile library to extract `.rar` files.

    - `zip` : Leverages the `zipfile` library to uncompress `.zip` files.

- **Returning the Result**

    After successfully uncompressing the files, the tool returns an object containing the paths of the uncompressed files.

## Usage Example

If there is a compressed file at `/home/user/archive.zip` and it is necessary to uncompress it, the tool would be used as follows:

- **Input**:

```
{"compressed_file_path": "/home/user/archive.zip"}
```

- **Output**:

```
{"uncompressed_files_paths": ["/home/user/archive/file1.txt", "/home/user/archive/file2.jpg", ...]}
```