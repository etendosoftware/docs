:octicons-package-16: Class: `GoogleDriveTool`

## Overview

The **Google Drive Tool** provides a direct interface to interact with a user's Google Drive. It enables the assistant to perform file operations in two primary modes:

  - **`list`**: Searches for and lists files of a specific type that are accessible via the provided credentials.
  - **`upload`**: Uploads a local file from the system to the user's Google Drive.

This tool is essential for workflows that require reading from or writing files to Google Drive as part of an automated process.

## Setup & Authentication

To use this tool, a Google OAuth token must be pre-configured and identified by an `alias`. This `alias` is a mandatory parameter for every request, as it is used to securely authenticate with the Google Drive API.

## Parameters

The tool's behavior is controlled by the `mode` parameter. Depending on the selected mode, other parameters may be required.

### General Parameters

  - `alias` (string, required): The alias of the pre-configured OAuth token to be used for authentication.
  - `mode` (string, required): The action to perform. Supported values are `'list'` or `'upload'`.

### `list` Mode Parameters

  - `file_type` (string, optional): The type of file to filter by (e.g., `spreadsheet`, `document`, `pdf`, `folder`). **Defaults to `spreadsheet`**.

### `upload` Mode Parameters

  - `file_path` (string, required): The local path to the file that will be uploaded.
  - `name` (string, optional): The name to assign to the file once uploaded to Google Drive. If not provided, it defaults to the original filename from the `file_path`.
  - `mime_type` (string, optional): The MIME type of the file (e.g., `application/pdf`, `image/png`). If not provided, it defaults to `application/octet-stream`.

## Modes of Operation

### List Mode (`mode='list'`)

This mode is used to find and display files in Google Drive.

  - **Process**: It queries Google Drive for files matching the specified `file_type` that are accessible to the user associated with the `alias`.
  - **Output**: If successful, it returns a formatted list of file names and their corresponding Google Drive IDs. If no files are found, it returns a notification message.

**Example Request:**

```json
{
    "alias": "my_google_token",
    "mode": "list",
    "file_type": "pdf"
}
```

**Example Success Response:**

```
📂 Files of type 'pdf':
- Q1_Report.pdf (ID: 1a2b3c4d5e6f...)
- Project_Proposal.pdf (ID: 7g8h9i0j1k2l...)
```

### Upload Mode (`mode='upload'`)

This mode is used to upload a file to Google Drive.

  - **Process**: It takes a local `file_path`, reads the file, and uploads it to the root of the user's Google Drive.
  - **Output**: If the upload is successful, it returns a confirmation message including the name of the uploaded file and a direct, shareable link to it in Google Drive.

**Example Request:**

```json
{
    "alias": "my_google_token",
    "mode": "upload",
    "file_path": "/path/to/local/image.png",
    "name": "My Vacation Photo.png",
    "mime_type": "image/png"
}
```

**Example Success Response:**

```
✅ File 'My Vacation Photo.png' uploaded successfully.
🔗 Link: https://drive.google.com/file/d/1x2y3z4a5b6c.../view
```

## Error Handling

The tool will return a `ToolOutputError` if:

  - An unsupported `mode` is provided.
  - A required parameter for a specific mode is missing (e.g., `file_path` for `upload` mode).
  - Any other exception occurs during the process, such as an authentication failure or file not found error.