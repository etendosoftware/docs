---
tags:
  - Etendo RX
  - oAuth
  - Middleware
---

# How to Use GoogleServiceUtil

> :octicons-package-16: **Package**: `com.etendoerp.etendorx.utils`  
> :octicons-search-24: **Class**: `GoogleServiceUtil` (all-static utility)

## Overview

`GoogleServiceUtil` is a **stateless** Java helper that centralizes authenticated access to **Google Sheets** and **Google Drive** using an OAuth2 **Bearer** token stored in `ETRXTokenInfo` and refreshed through **Etendo Middleware**. It sets sensible **timeouts** and **exponential backoff**, validates/refreshes tokens, and provides small convenience methods.

### Key capabilities

- Build authenticated **Sheets** and **Drive** clients (20s connect / 60s read, **backoff** on 429/5xx).
- Read sheet/tab names and A1 ranges in Sheets.
- Find a tab by name (**case-insensitive**) and read its rows.
- List Drive files by **friendly type** (`spreadsheet`, `doc`, `slides`, `pdf/pdfs`) with **Shared Drives** support.
- Create **Google Workspace** files (Sheets/Docs/Slides).
- Update cell ranges in Sheets using `valueInputOption=RAW`.
- Validate and **refresh** tokens via Etendo Middleware, persisting `validUntil`.

!!!note  
    The class is **static and concurrency-safe**. It injects `Authorization: Bearer …`, applies timeouts, and enables exponential backoff for transient HTTP errors.

---

## Quickstart

### Prerequisites

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

### Minimal Example: Read a Range

```java
ETRXTokenInfo token = GoogleServiceUtil.getMiddlewareToken(provider, "drive", user, org);
String accountId = SystemInfo.getSystemIdentifier();

List<List<Object>> values =
    GoogleServiceUtil.readSheet(token, accountId, "<FILE_ID>", "Sheet1!A1:C10");

for (List<Object> row : values) {
    System.out.println(row);
}
```

### List PDFs in Drive (first 100)

```java
JSONArray pdfs =
    GoogleServiceUtil.listAccessibleFiles(GoogleServiceUtil.PDF, token, accountId);
```

### Update Cells (RAW)

```java
List<List<Object>> rows = List.of(
    List.of("SKU", "Qty"),
    List.of("ABC-001", 10)
);

JSONObject result =
    GoogleServiceUtil.updateSpreadsheetValues("<FILE_ID>", token, accountId, "Sheet1!A1:B2", rows);
// => updatedRange, updatedRows, updatedColumns, updatedCells
```

---

## Configuration

```properties title="gradle.properties"
sso.auth.type=Middleware
sso.middleware.url=https://sso.etendo.cloud
sso.middleware.redirectUri=http://your-domain/oauth/secureApp/LoginHandler.html
```

### Token Storage & Retrieval

`ETRXTokenInfo getMiddlewareToken(ETRXoAuthProvider provider, String scope, User user, Organization org)`  
Looks up a token by `(provider / scope / user / org)` (the `scope` matches the **middleware provider** case-insensitively), gets `accountId` from `SystemInfo`, and returns a **valid** token (refreshing if required).

---

## Usage

- Authenticated Clients

```java
Sheets sheets = GoogleServiceUtil.getSheetsService(accessTokenString);
Drive  drive  = GoogleServiceUtil.getDriveService(accessTokenString);
```

- Adds `Authorization: Bearer …`
- **Connect timeout**: 20s, **read timeout**: 60s
- **Exponential backoff** on HTTP 429/5xx

- Extract a Google Sheets file ID safely

```java
String fileId = GoogleServiceUtil.extractSheetIdFromUrl(
    "https://docs.google.com/spreadsheets/d/FILE_ID/edit"
);
```

Supports canonical `docs.google.com/spreadsheets/d/...` (and the `a/<domain>/spreadsheets` variant) and `drive.google.com/open?id=...`.  
Invalid formats → `OBException(ETRX_WrongSheetURL)`.

- Read tab name by index

```java
String title = GoogleServiceUtil.getTabName(0, fileId, token, accountId);
```

- Spreadsheet without tabs → localized `ETRX_SheetHasNoTabs`
- Index out of range → localized `ETRX_WrongTabNumber`
- Errors are logged; the method ultimately throws `OBException`.

- Find a tab by name (case-insensitive) and read its rows

```java
List<List<Object>> rows =
    GoogleServiceUtil.findSpreadsheetAndTab(fileId, "My Tab", token, accountId);
```

- Missing tab → `OBException(ETRX_TabNotFound)` (localized)
- Existing but empty → returns `List.of()` and logs a WARN

- Read an arbitrary range (A1 notation)

```java
List<List<Object>> rows =
    GoogleServiceUtil.readSheet(token, accountId, fileId, "Sheet1!A1:Z100");
```

Blank/`null` `range` → defaults to **`A1:Z1000`**.

- Update a range (RAW)

```java
JSONObject resp =
    GoogleServiceUtil.updateSpreadsheetValues(fileId, token, accountId, "Sheet1!A1:B2", rows);
// Keys: updatedRange, updatedRows, updatedColumns, updatedCells
```

Uses `valueInputOption=RAW` to preserve values as provided.

- Drive: list by friendly type

```java
JSONArray sheets =
    GoogleServiceUtil.listAccessibleFiles(GoogleServiceUtil.SPREADSHEET, token, accountId);
```

**Keyword → MIME map:**

- `spreadsheet` → `application/vnd.google-apps.spreadsheet`
- `doc` → `application/vnd.google-apps.document`
- `slides` → `application/vnd.google-apps.presentation`
- `pdf` / `pdfs` → `application/pdf`

Includes **My Drive + Shared Drives** via:
`supportsAllDrives=true`, `includeItemsFromAllDrives=true`, `corpora=allDrives`, `pageSize=100`.

- Drive: create a Google Workspace file

```java
JSONObject created = GoogleServiceUtil.createDriveFile(
    "My Report",
    GoogleServiceUtil.MIMETYPE_SPREADSHEET,
    token, accountId
);
```

!!!important
    Only **Google Workspace** MIME types (`application/vnd.google-apps.*`) are accepted.  
    Non-Google MIME (e.g., `application/pdf`) requires **media upload**, and this method throws `OBException(ETRX_FailedToCreateFile)`.

- Token validation & refresh

`ETRXTokenInfo getValidAccessTokenOrRefresh(ETRXTokenInfo token, String accountId)`:

1. If `validUntil` is **> now + 2 minutes** (clock skew), reuses current token.
2. Otherwise:
    - Logs `ETRX_RefreshingToken`
    - Calls middleware: `GET {sso.middleware.url}/oauth-integrations/refresh-token?account_id=<accountId>`
    - Sets the returned access token
    - Sets `validUntil = now + 58 minutes` (fixed window)
    - Persists with `OBDal.save`

```java title="Explicit Validation"
GoogleServiceUtil.validateAccessToken(accessTokenString); // throws ETRX_ExpiredToken when status != 200
```

---

## API Reference (public surface)

**Constants (subset)**

- Headers: `BEARER`, `AUTHORIZATION`, `ACCEPT`, `APPLICATION_JSON`
- Friendly types: `SPREADSHEET`, `DOC`, `SLIDES`, `PDF`, `PDFS`
- MIMEs: `MIMETYPE_SPREADSHEET`, `MIMETYPE_DOC`, `MIMETYPE_SLIDES`, `MIMETYPE_PDF`

**Services**

- `static Sheets getSheetsService(String accessToken)`
- `static Drive  getDriveService(String accessToken)`

**Sheets**

- `static String getTabName(int index, String sheetId, ETRXTokenInfo token, String accountID)`
- `static List<List<Object>> findSpreadsheetAndTab(String sheetId, String tabName, ETRXTokenInfo token, String accountID)`
- `static List<List<Object>> readSheet(ETRXTokenInfo token, String accountID, String fileId, String range)`
- `static String getCellValue(List<Object> row, int index)`  
    Returns `""` if the index is out of bounds.

**Drive**

- `static JSONArray listAccessibleFiles(String type, ETRXTokenInfo token, String accountID)`
- `static JSONObject createDriveFile(String name, String mimeType, ETRXTokenInfo token, String accountID)`
- *(protected)* `static JSONArray listAccessibleFilesByMimeType(String mimeType, ETRXTokenInfo token, String accountID)`

**Tokens**

- `static ETRXTokenInfo getMiddlewareToken(ETRXoAuthProvider provider, String scope, User user, Organization org)`
- `static ETRXTokenInfo getValidAccessTokenOrRefresh(ETRXTokenInfo token, String accountId)`
- `static void validateAccessToken(String accessToken)`
- `static String refreshAccessToken(String accountId)`

**Utilities**

- `static String extractSheetIdFromUrl(String url)`

---

## i18n message keys

- `ETRX_SheetHasNoTabs`
- `ETRX_WrongTabNumber`
- `ETRX_TabNotFound`
- `ETRX_WrongSheetURL`
- `ETRX_UnsupportedFileType`
- `ETRX_FailedToCreateFile`
- `ETRX_RefreshingToken`
- `ETRX_ExpiredToken`
- `ETRX_ErrorRefreshingAccessToken`
- *(optional)* `ETRX_FailedToUpdateSheet`

!!!note
    - `getTabName` composes localized messages for out-of-range/empty-sheet, and errors are ultimately thrown as `OBException`.
    - Other methods throw localized `OBException` or `IllegalArgumentException` as indicated.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `ETRX_WrongSheetURL` | Unsupported URL format | Pass the **file ID** or a canonical Sheets URL |
| `ETRX_SheetHasNoTabs` / `ETRX_WrongTabNumber` | No tabs / index out of bounds | Verify spreadsheet structure and index |
| `ETRX_TabNotFound` | Name mismatch | Tab search is **case-insensitive** |
| `ETRX_ExpiredToken` | Access token invalid/expired | Ensure middleware refresh endpoint is reachable/configured |
| Creation error | Non-Google MIME | Use `application/vnd.google-apps.*` or perform media upload |

---

## Implementation

- **Timeouts/Backoff:** 20s connect / 60s read, plus `HttpBackOffUnsuccessfulResponseHandler(new ExponentialBackOff())`.
- **Shared Drives:** Listing uses `supportsAllDrives=true`, `includeItemsFromAllDrives=true`, `corpora=allDrives`.
- **Persistence:** On refresh, updates `token` + `validUntil` and persists via `OBDal`.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.