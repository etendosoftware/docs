---
tags:
    - Copilot
    - IA
    - Tool
    - Google Spreadsheets
---

# Google Spreadsheets Tool
:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Google Spreadsheets** tool is a powerful utility for interacting directly with Google Sheets. It allows the agent to manage spreadsheets programmatically through the **Google Drive and Google Sheets APIs**.

The tool operates using five distinct modes:

  - **`list`**: Lists all Google Spreadsheets accessible to the user.
  - **`create`**: Creates a new, empty spreadsheet.
  - **`upload`**: Uploads data from a local CSV file to a new Google Sheet.
  - **`read`**: Reads data from a specified cell range within a spreadsheet.
  - **`download`**: Downloads the content of a spreadsheet to a local CSV file.

## Setup & Authentication

This tool requires a pre-configured **Google OAuth** token identified by an `alias`. This `alias` must be provided in every request to authenticate with Google's services.

## Parameters

The tool's functionality is determined by the `mode` parameter. The required and optional parameters change depending on the selected mode.

### General Parameters

  - `alias` (string, required): The alias of the pre-configured OAuth token.
  - `mode` (string, required): The action to perform. Supported values: `list`, `create`, `upload`, `read`, `download`.

### Mode-Specific Parameters

  - `name` (string): The name for a spreadsheet.

      - Required for `create` mode.
      - Optional for `upload` mode (if not provided, defaults to the name of the uploaded CSV file).

  - `file_id` (string): The unique ID of the target spreadsheet (found in its URL).

      - Required for `read` and `download` modes.

  - `range` (string, optional): The cell range to operate on (e.g., `Sheet1!A1:B10`).

      - Used in `read` and `download` modes.
      - If not provided, it defaults to `A1:Z1000`.

  - `file_path` (string): The local path to a `.csv` file.

      - Required for `upload` mode.

## Modes of Operation

### `list`

Lists all Google Sheets the authenticated user can access.

  - **Parameters**: `alias`, `mode='list'`
  - **Example Request**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "list"
    }
    ```
  - **Example Success Response**:
    ```
    Spreadsheets found:
    - Monthly Budget (ID: 1a2b3c...)
    - Project Plan (ID: 4d5e6f...)
    ```

### `create`

Creates a new, blank spreadsheet with a given name.

  - **Parameters**: `alias`, `mode='create'`, `name`
  - **Example Request**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "create",
      "name": "Q3 Sales Report"
    }
    ```
  - **Example Success Response**:
    ```
    Spreadsheet 'Q3 Sales Report' created with ID: 1a2b3c.... Can be accessed at: https://docs.google.com/spreadsheets/d/1a2b3c.../edit
    ```

### `upload`

Uploads a local CSV file and converts it into a new Google Sheet.

  - **Parameters**: `alias`, `mode='upload'`, `file_path`, `name` (optional)
  - **Example Request**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "upload",
      "file_path": "/path/to/data.csv",
      "name": "Imported Sales Data"
    }
    ```
  - **Example Success Response**:
    ```
    ✅ CSV file 'Imported Sales Data' uploaded successfully.
    🔗 Link: https://docs.google.com/spreadsheets/d/4d5e6f.../edit
    ```

### `read`

Reads and returns the data from a specific range within a sheet.

  - **Parameters**: `alias`, `mode='read'`, `file_id`, `range` (optional)
  - **Example Request**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "read",
      "file_id": "1a2b3c...",
      "range": "A1:B2"
    }
    ```
  - **Example Success Response**:
    ```
    Spreadsheet content:
    Header1, Header2
    Value1, Value2
    ```

### `download`

Downloads a sheet (or a specific range) and saves it as a CSV file in a temporary local path.

  - **Parameters**: `alias`, `mode='download'`, `file_id`, `range` (optional)
  - **Example Request**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "download",
      "file_id": "1a2b3c..."
    }
    ```
  - **Example Success Response**:
    ```
    ✅ CSV file downloaded at: /tmp/copilotAttachedFiles/some-uuid/sheet_data.csv
    ```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.