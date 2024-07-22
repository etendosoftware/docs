---
tags:
    - Copilot
    - IA
    - Machine Learning
    - Tool
    - File Downloader
---

# File Downloader Tool

## Overview

The **File Downloader Tool** is designed to receive a URL and download the corresponding file to a temporary directory, returning the path to the temporary file. This tool is extremely valuable for any application that needs to dynamically interact with files on the web. It allows you to efficiently download files and store them temporarily, facilitating their later use and manipulation without the need to worry about file management in the system. In addition, it handles different types of content (text and binary) automatically, making the operation transparent and simple for the user.

## Functionality

This tool is especially useful when you need to download files from the web for further processing without worrying about managing the files on the local system. It can be useful for tasks such as:

- Downloading images, documents or other files for analysis and processing.
- Getting files for temporary storage, avoiding the need for direct file system management.

This process consists of the following actions:

- **Receiving Parameters**
    
    The tool receives a URL as a string via the `file_path_or_url` parameter.

- **Verifying URL**
    
    It checks if the entry is a valid URL (starts with `http://` or `https://`).

- **Downloading File**

    - It performs an HTTP GET request to the URL.
    - If the request is successful (status code 200):
        - It attempts to determine the file name from the URL.
        - If the name cannot be determined, it determines a generic name such as
        `downloaded_file`.
        - It determines the content type of the file (text or binary):
            - If text, it writes the contents to a temporary file with the extension `.txt`, if it does not have one.
            - If binary, it copies the content to a temporary file.

- **Returning the Result**
    
    It returns a dictionary with the path to the temporary file created under the `temp_file_path` key.

- **Handling the Error**

    If the URL is invalid or the download fails, it returns a relevant error message.

## Usage Example

If you have a file hosted at `https://example.com/file.txt` and you want to download it temporarily:

- **Input**

```
file_path_or_url: "https://example.com/file.txt"
```

- **Output**

```
{"temp_file_path": "/path/to/temp/downloaded_file.txt"}
```