---
tags:
  - Etendo RX
  - oAuth
  - Middleware
---

# How to Use Google Service Util

:octicons-package-16: **Package**: `com.etendoerp.etendorx.utils`

## Overview

`GoogleServiceUtil` is a **stateless** Java helper that centralizes authenticated access to **[Google Sheets](https://developers.google.com/workspace/sheets/api/reference/rest)** and **[Google Drive](https://developers.google.com/workspace/drive/api/guides/about-sdk)** using an OAuth2 **Bearer** token stored in `ETRXTokenInfo` and refreshed through **Etendo Middleware**. It injects the `Authorization` header, validates/refreshes tokens, and provides convenience methods to read ranges/tabs in Sheets, list Drive files by type, and create Google Workspace files.

### Key Features

- Build authenticated **Sheets** and **Drive** clients.
- Read A1 ranges and fetch tab names in Sheets.
- Find a tab by name (**case-insensitive**) and read all its rows.
- List Drive files by **friendly type** (`spreadsheet`, `doc`, `slides`, `pdf/pdfs`) with **Shared Drives** support (first 100).
- Create **Google Workspace** files (Sheets/Docs/Slides).
- Update cell ranges in Sheets using [`valueInputOption=RAW`](https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueInputOption).
- Validate and **refresh** tokens via Etendo Middleware, persisting `validUntil` (+1 hour).

!!!note
    The class is **static and concurrency-safe**. It injects `Authorization: Bearer …` on every request.

---

## Quickstart

### Prerequisites

!!!warning
    To make the most of this article, it helps if you’ve already reviewed the [oAuth flow in Etendo ERP.](https://docs.etendo.software/developer-guide/etendo-classic/bundles/platform/etendo-rx/#get-access-token)

- A valid row in `ETRXTokenInfo` (issued by the middleware).
- **Scopes**:
    - By default, tokens are minted with **`https://www.googleapis.com/auth/drive.file`**.  
    This scope is enough to:
        - Use the **Sheets API** (read/write) on files the **app created** or the **user explicitly selected/shared** with the app.
        - Use the **Drive API** for those files and basic metadata.
    - If you need to access **arbitrary user files** (beyond app-created/selected):
        - Read-only: `https://www.googleapis.com/auth/drive.readonly` **or** `https://www.googleapis.com/auth/spreadsheets.readonly`
        - Read/write: `https://www.googleapis.com/auth/drive` **or** `https://www.googleapis.com/auth/spreadsheets`
    - Optional (metadata-only listing): `https://www.googleapis.com/auth/drive.metadata.readonly`
- Property **`sso.middleware.url`** configured in **`gradle.properties`**.

## Configuration

```properties title="gradle.properties"
sso.auth.type=Middleware
sso.middleware.url=https://sso.etendo.cloud
sso.middleware.redirectUri=http://your-domain/oauth/secureApp/LoginHandler.html
```

---

## Usage

### Clients

#### Authenticated Clients

- Methods:

    ```java
    /**
     * Creates a Google Sheets API client instance using the provided OAuth2 access token.
    *
    * @param accessToken OAuth2 Bearer token with sufficient scope (e.g. spreadsheets.readonly).
    * @return an authenticated instance of the Google Sheets client.
    */
    public static Sheets getSheetsService(String accessToken)

    /**
     * Creates a Google Drive API client instance using the provided OAuth2 access token.
    *
    * @param accessToken OAuth2 Bearer token with sufficient scope (e.g. drive.metadata.readonly).
    * @return an authenticated instance of the Google Drive client.
    */
    public static Drive getDriveService(String accessToken)
    ```

- Example:

    ```java
    Sheets sheets = GoogleServiceUtil.getSheetsService(accessTokenString);
    Drive  drive  = GoogleServiceUtil.getDriveService(accessTokenString);
    ```

- Adds `Authorization: Bearer …` via a `HttpRequestInitializer`.
- Application names:
  - For `getSheetsService` / `getDriveService`: `"Google Sheets Java Integration"`
  - For `readSheet`: `"Etendo Google Picker Integration"` (see below).

### Tokens

#### Token Storage & Retrieval

```java
/**
 * Retrieves a middleware access token associated with the given provider, scope, user,
 * and organization. If a valid token exists in the database, it will be returned;
 * otherwise, the method attempts to refresh the token before returning it.
 *
 * <p>The method performs the following steps:</p>
 * <ul>
 *   <li>Searches for an existing {@link ETRXTokenInfo} matching the specified
 *       {@code provider}, {@code scope}, {@code user}, and {@code organization}.</li>
 *   <li>Obtains the system identifier from {@link SystemInfo} to be used as the
 *       account ID. Logs a warning if the identifier is empty.</li>
 *   <li>Returns a valid token, refreshing it if required, via
 *       {@link #getValidAccessTokenOrRefresh(ETRXTokenInfo, String)}.</li>
 * </ul>
 *
 * @param provider the OAuth provider associated with the token (not {@code null}).
 * @param scope    the scope of the token, used to identify the middleware provider (case-insensitive).
 * @param user     the user linked to the token.
 * @param org      the organization linked to the token.
 * @return a valid {@link ETRXTokenInfo} object containing access and refresh token information,
 * or {@code null} if no matching token exists and refresh cannot be performed.
 * @throws OBException if an error occurs while retrieving the system identifier
 *                     or during token validation/refresh.
 */
ETRXTokenInfo getMiddlewareToken(ETRXoAuthProvider provider, String scope, User user, Organization org)
```  

Looks up a token by `(provider / scope / user / org)` (the `scope` matches the **middleware provider** case-insensitively), obtains `accountId` from `SystemInfo` (warning on empty), and returns a **valid** token (refreshing if required).

#### Token validation & refresh

```java
/**
 * Validates the token and refreshes it automatically if expired.
 *
 * @param accessToken The current access token
 * @param accountId   The account ID used for refreshing (needed for /refresh-token)
 * @return A valid access token (either original or refreshed)
 */
public static ETRXTokenInfo getValidAccessTokenOrRefresh(ETRXTokenInfo accessToken, String accountId)
```

1. Calls `validateAccessToken(accessToken.getToken())`. If **200**, the existing token is returned.  
2. On failure (e.g., expired/invalid), logs `ETRX_RefreshingToken`, calls middleware:
   `GET {{sso.middleware.url}}/oauth-integrations/refresh-token?account_id=<accountId>`,
   sets the new access token, **sets `validUntil` = now + 1 hour**, persists with `OBDal.save`, and returns it.

Other helpers:

```java
/**
 * Checks if the provided OAuth 2.0 access token is valid and not expired.
 * Uses Google's public token info endpoint.
 *
 * @param accessToken the OAuth access token to validate
 * @throws OBException if the token is invalid or expired
 */
public static void validateAccessToken(String accessToken) throws OBException
```

```java
/**
 * Refreshes the access token using the refresh_token stored in EtendoMiddleware.
 *
 * @param accountId the ID used to associate the refresh_token (e.g. user/org ID)
 * @return the new access token
 * @throws OBException if the refresh fails
 */
public static String refreshAccessToken(String accountId) throws OBException
```

### Sheets

#### Read a Range

- Method:

    ```java
    /**
     * Reads cell values from a specified range in a Google Spreadsheet.
     * <p>
     * This method uses the Google Sheets API to retrieve the contents of a given range
     * from a spreadsheet identified by its file ID. If no range is provided, it defaults to {@code "A1:Z1000"}.
     * The method returns the values as a list of rows, where each row is a list of cell values.
     * </p>
     *
     * @param accessToken a valid OAuth 2.0 access token with permission to read from Google Sheets (e.g., {@code https://www.googleapis.com/auth/spreadsheets.readonly})
     * @param accountID   the internal account identifier used to refresh the token if necessary.
     * @param fileId      the ID of the Google Spreadsheet to read from
     * @param range       the A1-notation range to read (e.g., {@code "Sheet1!A1:C10"}); if blank or null, defaults to {@code "A1:Z1000"}
     * @return a {@link List} of rows, where each row is a {@link List} of cell values ({@code Object})
     * @throws IOException if a network error occurs or the API request fails
     */
    public static List<List<Object>> readSheet(ETRXTokenInfo accessToken, String accountID, String fileId, String range)
        throws IOException
    ```
- Behavior:
  - Fetches a **fresh/valid** token internally.
  - Builds a Sheets client with app name `"Etendo Google Picker Integration"` (note this differs from the other builders).
  - Blank/`null` `range` → defaults to **`"A1:Z1000"`**.
  - Returns a `List<List<Object>>` with the values (may be `null` if the range has no values).

- Example:

    ```java
    ETRXTokenInfo token = GoogleServiceUtil.getMiddlewareToken(provider, "drive", user, org);
    String accountId = SystemInfo.getSystemIdentifier();

    List<List<Object>> values =
        GoogleServiceUtil.readSheet(token, accountId, "<FILE_ID>", "Sheet1!A1:C10");

    for (List<Object> row : values) {
        System.out.println(row);
    }
    ```

- Blank/`null` `range` → defaults to **`A1:Z1000`**.

#### Update Cells (RAW)

- Method:

    ```java
    /**
     * Updates the content of a Google Spreadsheet within a specified cell range.
     * <p>
     * This method sends a PUT request to the Google Sheets API to overwrite the values
     * in the given range with the provided 2D list of objects. The update is performed using
     * the "RAW" input option, meaning values are written exactly as they are passed without formatting.
     * </p>
     *
     * @param fileId      the unique identifier of the Google Spreadsheet (found in the URL of the sheet)
     * @param accessToken a valid OAuth 2.0 access token with permissions to edit the spreadsheet
     * @param accountID   the internal account identifier used to refresh the token if necessary
     * @param range       the A1 notation of the range to update (e.g., "Sheet1!A1:C5")
     * @param values      a 2D list of values to write, where each inner list represents a row
     * @return a {@link JSONObject} containing the response from the Google Sheets API,
     * including updated range and cell count information
     * @throws IOException   if an I/O error occurs while sending or receiving data
     * @throws JSONException if there is an error parsing the API response or constructing the request body
     * @throws OBException   if the API responds with a non-200 HTTP status code, indicating failure
     */
    public static JSONObject updateSpreadsheetValues(String fileId, ETRXTokenInfo accessToken, String accountID, String range,
                                                    List<List<Object>> values) throws IOException, JSONException
    ```

- Example:

    ```java
    List<List<Object>> rows = List.of(
        List.of("SKU", "Qty"),
        List.of("ABC-001", 10)
    );

    JSONObject result =
        GoogleServiceUtil.updateSpreadsheetValues("<FILE_ID>", token, accountId, "Sheet1!A1:B2", rows);
    // => updatedRange, updatedRows, updatedColumns, updatedCells
    ```

- Uses `valueInputOption=RAW` to preserve values as provided.

#### Read tab name by index

- Method:

    ```java
    /**
     * Retrieves the name (title) of a specific tab (sheet) in a Google Spreadsheet by its index.
     *
     * <p>This method performs the following steps:
     * <ul>
     *   <li>Validates or refreshes the given access token associated with the specified account.</li>
     *   <li>Builds an authorized Google Sheets service instance.</li>
     *   <li>Fetches the spreadsheet data using the provided {@code sheetId}.</li>
     *   <li>Checks whether the spreadsheet contains any tabs (sheets).</li>
     *   <li>Ensures that the given index is within the valid range of existing sheets.</li>
     *   <li>Returns the title of the sheet at the specified index.</li>
     * </ul>
     *
     * @param index     Zero-based index of the tab to retrieve.
     * @param sheetId   The ID of the target Google Spreadsheet.
     * @param token     The access token used to authenticate with the Google Sheets API.
     * @param accountID The ID of the account used to validate or refresh the token.
     * @return The title of the sheet at the given index.
     * @throws OBException If the spreadsheet has no sheets or if the index is out of bounds.
     */
    public static String getTabName(int index, String sheetId, ETRXTokenInfo token, String accountID) throws OBException
    ```

- Example:

    ```java
    String title = GoogleServiceUtil.getTabName(0, fileId, token, accountId);
    ```

- Spreadsheet without tabs → localized `ETRX_SheetHasNoTabs`
- Index out of range → localized `ETRX_WrongTabNumber`
- Errors are logged; the method ultimately throws `OBException`.

#### Find a tab by name (case-insensitive) and read its rows

- Method:

    ```java
    /**
     * Retrieves the cell values from a specific tab (sheet) within a Google Spreadsheet.
     * <p>
     * This method connects to the Google Sheets API using the provided access token and attempts to find
     * a tab (sheet) by name in the specified spreadsheet. The tab name comparison is case-insensitive.
     * If the tab exists, it returns all cell values from that tab. If the tab does not exist,
     * an {@link OBException} is thrown. If the tab exists but has no data, an empty list is returned.
     * </p>
     *
     * @param sheetId
     *     the ID of the Google Spreadsheet (not the full URL)
     * @param tabName
     *     the name of the tab (sheet) to search for (case-insensitive)
     * @param token
     *     a valid OAuth 2.0 access token with Sheets read access
     * @param accountID
     *     the internal account identifier used to refresh the token if necessary.
     * @return a list of rows from the tab; each row is a list of cell values. Returns an empty list if the tab is found but contains no data.
     * @throws OBException
     *     if the specified tab name does not exist in the spreadsheet
     * @throws IOException
     *     if an error occurs while communicating with the Google Sheets API
     */
    public static List<List<Object>> findSpreadsheetAndTab(String sheetId, String tabName,
        ETRXTokenInfo token, String accountID) throws IOException
    ```

- Usage:

    ```java
    List<List<Object>> rows =
        GoogleServiceUtil.findSpreadsheetAndTab(fileId, "My Tab", token, accountId);
    ```

- Behavior:
  - Checks if a sheet title matches `tabName` **ignoring case**.
  - Missing tab → `OBException(ETRX_TabNotFound)` (localized) — includes the missing name.
  - If found, calls `spreadsheets().values().get(sheetId, tabName)`.
  - If the tab has no data, returns `List.of()` and logs a **WARN**.

#### Retrive a value from a Sheet

```java
/**
 * Safely retrieves a cell value from a given row at the specified index.
 *
 * @param row
 *     the row list containing cell values.
 * @param index
 *     the zero-based column index.
 * @return the cell value as a string, or an empty string if the cell is missing.
 */
public static String getCellValue(List<Object> row, int index)
```

---

### Drive

#### List Drive files by friendly type (first 100)

- Method:

    ```java
    /**
     * Retrieves a list of accessible files from the user's Google Drive, filtered by a simplified file type keyword.
    * <p>
    * This method maps a user-friendly type keyword (e.g., {@code "spreadsheet"}, {@code "doc"}, {@code "slides"}, {@code "pdf"})
    * to its corresponding MIME type and queries the Google Drive API for matching files. It simplifies Drive file filtering
    * for common file types supported by Google Workspace and standard uploads.
    * </p>
    *
    * <p>Supported keywords and their corresponding file types:</p>
    * <ul>
    *   <li>{@code "spreadsheet"} → Google Sheets ({@code application/vnd.google-apps.spreadsheet})</li>
    *   <li>{@code "doc"} → Google Docs ({@code application/vnd.google-apps.document})</li>
    *   <li>{@code "slides"} → Google Slides ({@code application/vnd.google-apps.presentation})</li>
    *   <li>{@code "pdf"}, {@code "pdfs"} → PDF files uploaded to Drive ({@code application/pdf})</li>
    * </ul>
    *
    * @param type        a simplified keyword representing the file type to retrieve
    * @param accessToken a valid OAuth 2.0 access token with access to the user's Drive
    *                    (e.g., {@code drive.file} or {@code drive.readonly})
    * @param accountID   the internal account identifier used to refresh the token if necessary.
    * @return a {@link JSONArray} containing the matching files,
    * where each file is represented as a {@link JSONObject}
    * with fields {@code id}, {@code name}, and {@code mimeType}
    * @throws IllegalArgumentException if the provided type keyword is not supported
    * @throws IOException              if a network or API error occurs during the request
    * @throws JSONException            if an error occurs parsing the API response
    */
    public static JSONArray listAccessibleFiles(String type, ETRXTokenInfo accessToken, String accountID)
        throws JSONException, IOException
    ```

- Example:

    ```java
    JSONArray pdfs =
        GoogleServiceUtil.listAccessibleFiles(GoogleServiceUtil.PDF, token, accountId);
    ```

- **Keyword → MIME map:**
  - `spreadsheet` → `application/vnd.google-apps.spreadsheet`
  - `doc` → `application/vnd.google-apps.document`
  - `slides` → `application/vnd.google-apps.presentation`
  - `pdf` / `pdfs` → `application/pdf`
- Internals:
  - Uses `listAccessibleFilesByMimeType(...)` hitting Drive `files.list` with:
    `supportsAllDrives=true`, `includeItemsFromAllDrives=true`, `corpora=allDrives`, `pageSize=100`.
  - Response fields: **`files(id,name,mimeType)`** (no `nextPageToken` exposed by this method).
  - Non-200 → localized `ETRX_ErrorGettingAccessFiles` with HTTP status/message.

#### Create a Google Workspace file

- Method:

    ```java
    /**
     * Creates a new file in the user's Google Drive with the specified name and MIME type.
     * <p>
     * This method sends a POST request to the Google Drive API to create a file in the root
     * directory of the user's Drive. The file is created with the given name and MIME type.
     * It supports both Google Workspace file types (like spreadsheets, documents, and presentations)
     * and standard MIME types (like plain text or PDF).
     * </p>
     *
     * <p>Supported Google Workspace MIME types include:
     * <ul>
     *   <li>{@code application/vnd.google-apps.spreadsheet} – Google Sheets</li>
     *   <li>{@code application/vnd.google-apps.document} – Google Docs</li>
     *   <li>{@code application/vnd.google-apps.presentation} – Google Slides</li>
     * </ul>
     * </p>
     *
     * @param name
     *     the desired name for the new file
     * @param mimeType
     *     the MIME type of the file to be created; determines the file type in Drive
     * @param accessToken
     *     a valid OAuth 2.0 access token with sufficient permissions (e.g., {@code drive.file} scope)
     * @param accountID
     *     the internal account identifier used to refresh the token if necessary.
     * @return a {@link JSONObject} containing metadata of the created file, such as {@code id}, {@code name}, and {@code mimeType}
     * @throws IOException
     *     if an I/O error occurs during communication with the API
     * @throws JSONException
     *     if there is an error constructing the request or parsing the response
     * @throws OBException
     *     if the API returns a non-200 HTTP status code, indicating the file creation failed
     */
    public static JSONObject createDriveFile(String name, String mimeType, ETRXTokenInfo accessToken, String accountID)
        throws IOException, JSONException
    ```

- Example:

    ```java
    JSONObject created = GoogleServiceUtil.createDriveFile(
        "My Report",
        GoogleServiceUtil.MIMETYPE_SPREADSHEET,
        token, accountId
    );
    ```

- Behavior:
  - Plain **metadata create** (`POST /drive/v3/files`) with `{name, mimeType}`.

!!!important
    Only [**Google Workspace** MIME types](https://developers.google.com/workspace/drive/api/guides/mime-types?hl=es-419) (`application/vnd.google-apps.*`) are accepted.  
    Non-Google MIME (e.g., `application/pdf`) requires **media upload**, and this method throws `OBException(ETRX_FailedToCreateFile)`.

### Utilities

#### Extract a Google Sheets file ID safely

- Method:

    ```java
    /**
     * Extracts the spreadsheet ID from a full Google Sheets URL.
     *
     * @param url
     *     the full URL of a Google Spreadsheet (e.g. <a href="https://docs.google.com/spreadsheets/d/SheetID/edit">https://docs.google.com/spreadsheets/d/SheetID/edit</a>).
     * @return the spreadsheet ID as a string.
     * @throws IllegalArgumentException
     *     if the URL format is invalid or the ID cannot be extracted.
     */
    public static String extractSheetIdFromUrl(String url) throws IllegalArgumentException
    ```

- Example:

    ```java
    String fileId = GoogleServiceUtil.extractSheetIdFromUrl(
        "https://docs.google.com/spreadsheets/d/FILE_ID/edit"
    );
    ```

    Supports canonical URL like `docs.google.com/spreadsheets/d/...` (and the `a/<domain>/spreadsheets` variant) and `drive.google.com/open?id=...`.  
    Invalid formats → `OBException(ETRX_WrongSheetURL)`.

## API Reference (public surface)

- **Constants (subset)**
  - Headers: `BEARER`, `AUTHORIZATION`, `ACCEPT`, `APPLICATION_JSON`
  - Friendly types: `SPREADSHEET`, `DOC`, `SLIDES`, `PDF`, `PDFS`

- **Services**
  - `static Sheets getSheetsService(String accessToken)`
  - `static Drive  getDriveService(String accessToken)`

- **Tokens**
  - `static ETRXTokenInfo getMiddlewareToken(ETRXoAuthProvider provider, String scope, User user, Organization org)`
  - `static ETRXTokenInfo getValidAccessTokenOrRefresh(ETRXTokenInfo token, String accountId)`
  - `static void validateAccessToken(String accessToken)`
  - `static String refreshAccessToken(String accountId)`

- **Sheets**
  - `static String getTabName(int index, String sheetId, ETRXTokenInfo token, String accountID)`
  - `static List<List<Object>> findSpreadsheetAndTab(String sheetId, String tabName, ETRXTokenInfo token, String accountID)`
  - `static List<List<Object>> readSheet(ETRXTokenInfo token, String accountID, String fileId, String range)`
  - `static String getCellValue(List<Object> row, int index)`

- **Drive**
  - `static JSONArray listAccessibleFiles(String type, ETRXTokenInfo token, String accountID)`
  - `static JSONObject createDriveFile(String name, String mimeType, ETRXTokenInfo token, String accountID)`
  - *(protected)* `static JSONArray listAccessibleFilesByMimeType(String mimeType, ETRXTokenInfo token, String accountID)`

- **Utilities**
  - `static String extractSheetIdFromUrl(String url)`

!!!note
    You can see the full implementation in the repository file: [GoogleServiceUtil](https://github.com/etendosoftware/com.etendoerp.etendorx/blob/main/src/com/etendoerp/etendorx/utils/GoogleServiceUtil.java)

---

## I18N message keys

- `ETRX_SheetHasNoTabs`
- `ETRX_WrongTabNumber`
- `ETRX_TabNotFound`
- `ETRX_WrongSheetURL`
- `ETRX_UnsupportedFileType`
- `ETRX_FailedToCreateFile`
- `ETRX_RefreshingToken`
- `ETRX_ExpiredToken`
- `ETRX_ErrorRefreshingAccessToken`
- `ETRX_ErrorGettingAccessFiles`
- `ETRX_401RefreshToken`
- `ETRX_FailedToUpdateSheet`


!!!note
    - `getTabName` composes localized messages for out-of-range/empty-sheet, and errors are ultimately thrown as `OBException`.
    - Other methods throw localized `OBException` or `IllegalArgumentException` as indicated.

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `ETRX_WrongSheetURL` | Unsupported URL format | Pass a canonical **Sheets URL** like `https://docs.google.com/spreadsheets/d/<ID>` or extract the **file ID** first |
| `ETRX_SheetHasNoTabs` / `ETRX_WrongTabNumber` | No tabs / index out of bounds | Verify spreadsheet structure and index |
| `ETRX_TabNotFound` | Name mismatch | Tab search is **case-insensitive** but requires exact title match |
| `ETRX_ExpiredToken` | Access token invalid/expired | Ensure middleware refresh endpoint is reachable/configured |
| Only 100 files returned | `pageSize=100` on Drive list | Add a new helper to handle `pageToken` if you need pagination |
| `ETRX_FailedToCreateFile` | Non-Google MIME or insufficient scope | Use `application/vnd.google-apps.*` or implement media upload flow |

---

## Implementation Notes

- **Auth header**: Added by `bearerTokenInitializer` for all requests.
- **App names**: `"Google Sheets Java Integration"` for `getSheetsService` / `getDriveService`; `"Etendo Google Picker Integration"` in `readSheet`.
- **Shared Drives support**: Drive listing sets `supportsAllDrives=true`, `includeItemsFromAllDrives=true`, `corpora=allDrives`.
- **Token persistence**: On refresh, updates `token` and sets `validUntil` to **now + 1 hour**; persists via `OBDal`.
- **Error handling**: Non-200 responses are converted into localized `OBException`s with meaningful keys.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.