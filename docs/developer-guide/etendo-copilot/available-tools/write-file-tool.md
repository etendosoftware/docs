---
tags:
    - Copilot
    - IA
    - Tool
    - Write
    - File
---

# Write File Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Write File Tool** is a tool for writing and editing files. It allows specifying the file you want to write, the content to write and the option to overwrite the file or not. It also allows you to specify the exact line where you want to write the content. This tool returns a message indicating the result of the operation.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md){target="\_blank"}.

## Functionality

This tool is useful in any application or system that needs to manipulate text files programmatically. It can be used to edit settings, record data, create log files, among other things. This makes it easier for the user to handle:

- File Manipulation: It facilitates editing and manipulation of text files without the need to manually open the files in an editor.
- Task Standardization: It standardizes writing files from different parts of an application.
- Security: It creates automatic backups when writing existing files, preventing data loss.

Using this tool consists of the following actions:

- **Processing Arguments**

    It takes the following input parameters:

    - `filepath`: It specifies the file (file path)
    - `content`: The content to write
    - `override`: Whether the file should be overwritten
    - `lineno`: The line on which the content should be written

- **Creating the File**

    If the specified file does not exist, it creates it.

- **Backup**

    If the file exists, it reads it and creates a backup copy of it by adding a timestamp to the file name (`.bak%timestamp%`).

- **Writing the Content**
    - Override: If the override option is enabled, the file is cleaned up and the specified content is written, either at the end of the file (if line number is not specified) or on a specific line.
    - No Override: If no override is chosen, the content is appended to the end of the existing file.

- **Returning the Result**
    It returns a message including the file path and whether a backup was created. For example:
    ```
    { “message”: “File /tmp/test.txt written successfully, backup: True”}
    ```
    if the file was modified and a backup was created.
    ```
    { “message”: “File /tmp/test.txt written successfully, backup: False”}
    ```
    if a backup did not need to be created.

## Usage Example

Imagine we want to write *Hello World* in the file `/tmp/test.txt`, overwriting its contents, in the first line of the file. Our entry could be:
- filepath: /tmp/test.txt
- content: Hello World
- override: True
- lineno: 1

The Write File Tool will process these parameters, write *Hello World* to the first line of the `/tmp/test.txt` file and return a message indicating that the operation completed successfully and whether a backup was created.