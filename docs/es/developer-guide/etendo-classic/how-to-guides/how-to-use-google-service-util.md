---
tags:
  - Etendo RX
  - oAuth
  - Middleware
---

# Cómo usar GoogleServiceUtil

:octicons-package-16: **Paquete**: `com.etendoerp.etendorx.utils`

## Visión general

`GoogleServiceUtil` es un asistente Java **sin estado** que centraliza el acceso autenticado a las APIs de [Google Sheets](https://developers.google.com/workspace/sheets/api/reference/rest){target="_blank"} y [Google Drive](https://developers.google.com/workspace/drive/api/guides/about-sdk){target="_blank"} usando un token **Bearer** de OAuth2 almacenado en `ETRXTokenInfo` y renovado a través de **Etendo Middleware**. Inyecta la cabecera `Authorization`, valida/renueva tokens y proporciona métodos de conveniencia para leer rangos/solapas en Sheets, listar archivos de Drive por tipo y crear archivos de Google Workspace.

### Funcionalidades clave

- Construir clientes autenticados de **Sheets** y **Drive**.
- Leer rangos A1 y obtener nombres de solapas en Sheets.
- Encontrar una solapa por nombre (**sin distinguir mayúsculas/minúsculas**) y leer todas sus filas.
- Listar archivos de Drive por **tipo amigable** (`spreadsheet`, `doc`, `slides`, `pdf/pdfs`) con soporte de **Unidades compartidas** (primeros 100).
- Crear archivos de **Google Workspace** (Sheets/Docs/Slides).
- Actualizar rangos de celdas en Sheets usando [`valueInputOption=RAW`](https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueInputOption){target="_blank"}.
- Validar y **renovar** tokens mediante Etendo Middleware, persistiendo `validUntil` (+1 hora).

!!!note
    La clase es **estática y segura para la concurrencia**. Inyecta `Authorization: Bearer …` en cada solicitud.

---
## Inicio rápido

### Requisitos previos

!!!warning
    Para aprovechar al máximo este artículo, es útil si ya ha revisado el [flujo oAuth en Etendo ERP.](https://docs.etendo.software/developer-guide/etendo-classic/bundles/platform/etendo-rx/#get-access-token)

- Una fila válida en `ETRXTokenInfo` (emitida por el middleware).
- **Ámbitos**:
    - De forma predeterminada, los tokens se emiten con `https://www.googleapis.com/auth/drive.file`.  
    Este ámbito es suficiente para:
        - Usar la **API de Sheets** (lectura/escritura) en archivos que la **aplicación creó** o que el **usuario seleccionó/compartió explícitamente** con la aplicación.
        - Usar la **API de Drive** para esos archivos y metadatos básicos.
    - Si necesita acceder a **archivos arbitrarios del usuario** (más allá de los creados/seleccionados por la aplicación):
        - Solo lectura: `https://www.googleapis.com/auth/drive.readonly` **o** `https://www.googleapis.com/auth/spreadsheets.readonly`
        - Lectura/escritura: `https://www.googleapis.com/auth/drive` **o** `https://www.googleapis.com/auth/spreadsheets`
    - Opcional (listado solo de metadatos): `https://www.googleapis.com/auth/drive.metadata.readonly`
- Propiedad **`sso.middleware.url`** configurada en **`gradle.properties`**.
## Configuración

```properties title="gradle.properties"
sso.auth.type=Middleware
sso.middleware.url=https://sso.etendo.cloud
sso.middleware.redirectUri=http://your-domain/oauth/secureApp/LoginHandler.html
```

---
## Uso

### Entidad

#### Entidad autenticados

- Métodos:

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

- Ejemplo:

    ```java
    Sheets sheets = GoogleServiceUtil.getSheetsService(accessTokenString);
    Drive  drive  = GoogleServiceUtil.getDriveService(accessTokenString);
    ```

- Añade `Authorization: Bearer …` mediante un `HttpRequestInitializer`.
- Nombres de la aplicación:
  - Para `getSheetsService` / `getDriveService`: `"Google Sheets Java Integration"`
  - Para `readSheet`: `"Etendo Google Picker Integration"` (véase más abajo).

### Tokens

#### Almacenamiento y recuperación de tokens

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

Busca un token por `(provider / scope / user / org)` (el `scope` coincide con el **proveedor de middleware** sin distinguir mayúsculas/minúsculas), obtiene `accountId` desde `SystemInfo` (aviso si está vacío) y devuelve un token **válido** (refrescándolo si es necesario).

#### Validación y actualización de tokens

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

1. Llama a `validateAccessToken(accessToken.getToken())`. Si es **200**, se devuelve el token existente.  
2. En caso de fallo (p. ej., caducado/no válido), registra `ETRX_RefreshingToken`, llama al middleware:
   `GET {{sso.middleware.url}}/oauth-integrations/refresh-token?account_id=<accountId>`,
   establece el nuevo access token, **establece `validUntil` = now + 1 hour**, persiste con `OBDal.save` y lo devuelve.

Otros auxiliares:

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

#### Leer un rango

- Método:

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

- Comportamiento:

    - Obtiene internamente un token **reciente/válido**.
    - Construye un cliente de Sheets con el nombre de aplicación `"Etendo Google Picker Integration"` (tenga en cuenta que difiere de los otros constructores).
    - `range` en blanco/`null` → por defecto **`"A1:Z1000"`**.
    - Devuelve un `List<List<Object>>` con los valores (puede ser `null` si el rango no tiene valores).

- Ejemplo:

    ```java
    ETRXTokenInfo token = GoogleServiceUtil.getMiddlewareToken(provider, "drive", user, org);
    String accountId = SystemInfo.getSystemIdentifier();

    List<List<Object>> values =
        GoogleServiceUtil.readSheet(token, accountId, "<FILE_ID>", "Sheet1!A1:C10");

    for (List<Object> row : values) {
        System.out.println(row);
    }
    ```

- `range` en blanco/`null` → por defecto **`A1:Z1000`**.

#### Actualizar celdas (RAW)

- Método:

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

- Ejemplo:

    ```java
    List<List<Object>> rows = List.of(
        List.of("SKU", "Qty"),
        List.of("ABC-001", 10)
    );

    JSONObject result =
        GoogleServiceUtil.updateSpreadsheetValues("<FILE_ID>", token, accountId, "Sheet1!A1:B2", rows);
    // => updatedRange, updatedRows, updatedColumns, updatedCells
    ```

- Usa `valueInputOption=RAW` para conservar los valores tal como se proporcionan.

#### Leer el nombre de una pestaña por índice

- Método:

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

- Ejemplo:

    ```java
    String title = GoogleServiceUtil.getTabName(0, fileId, token, accountId);
    ```

- Hoja de cálculo sin pestañas → `ETRX_SheetHasNoTabs` (localizado)
- Índice fuera de rango → `ETRX_WrongTabNumber` (localizado)
- Los errores se registran; el método finalmente lanza `OBException`.

#### Buscar una pestaña por nombre (sin distinguir mayúsculas/minúsculas) y leer sus filas

- Método:

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

- Uso:

    ```java
    List<List<Object>> rows =
        GoogleServiceUtil.findSpreadsheetAndTab(fileId, "My Tab", token, accountId);
    ```

- Comportamiento:

    - Comprueba si un título de hoja coincide con `tabName` **sin distinguir mayúsculas/minúsculas**.
    - Pestaña inexistente → `OBException(ETRX_TabNotFound)` (localizado) — incluye el nombre que falta.
    - Si se encuentra, llama a `spreadsheets().values().get(sheetId, tabName)`.
    - Si la pestaña no tiene datos, devuelve `List.of()` y registra un **WARN**.

#### Recuperar un valor de una hoja

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

### Drive

#### Listar archivos de Drive por tipo amigable (primeros 100)

- Método:

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

- Ejemplo:

    ```java
    JSONArray pdfs =
        GoogleServiceUtil.listAccessibleFiles(GoogleServiceUtil.PDF, token, accountId);
    ```

- **Mapa de palabra clave → MIME:**

    - `spreadsheet` → `application/vnd.google-apps.spreadsheet`
    - `doc` → `application/vnd.google-apps.document`
    - `slides` → `application/vnd.google-apps.presentation`
    - `pdf` / `pdfs` → `application/pdf`

- Internos:

    - Usa `listAccessibleFilesByMimeType(...)` llamando a Drive `files.list` con:
    `supportsAllDrives=true`, `includeItemsFromAllDrives=true`, `corpora=allDrives`, `pageSize=100`.
    - Campos de respuesta: **`files(id,name,mimeType)`** (este método no expone `nextPageToken`).
    - Distinto de 200 → `ETRX_ErrorGettingAccessFiles` (localizado) con estado/mensaje HTTP.

#### Crear un archivo de Google Workspace

- Método:

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

- Ejemplo:

    ```java
    JSONObject created = GoogleServiceUtil.createDriveFile(
        "My Report",
        GoogleServiceUtil.MIMETYPE_SPREADSHEET,
        token, accountId
    );
    ```

- Comportamiento:
  - Creación de **metadatos** simple (`POST /drive/v3/files`) con `{name, mimeType}`.

!!!important
    Solo se aceptan [**tipos MIME de Google Workspace**](https://developers.google.com/workspace/drive/api/guides/mime-types?hl=es-419) (`application/vnd.google-apps.*`).  
    Un MIME que no sea de Google (p. ej., `application/pdf`) requiere **carga de medios**, y este método lanza `OBException(ETRX_FailedToCreateFile)`.

### Utilidades

#### Extraer de forma segura el ID de archivo de Google Sheets

- Método:

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

- Ejemplo:

    ```java
    String fileId = GoogleServiceUtil.extractSheetIdFromUrl(
        "https://docs.google.com/spreadsheets/d/FILE_ID/edit"
    );
    ```

    Admite una URL canónica como `docs.google.com/spreadsheets/d/...` (y la variante `a/<domain>/spreadsheets`) y `drive.google.com/open?id=...`.  
    Formatos no válidos → `OBException(ETRX_WrongSheetURL)`.
## Referencia de API (superficie pública)

- **Constantes (subconjunto)**

    - Encabezados: `BEARER`, `AUTHORIZATION`, `ACCEPT`, `APPLICATION_JSON`
    - Tipos amigables: `SPREADSHEET`, `DOC`, `SLIDES`, `PDF`, `PDFS`

- **Servicios**

    - `static Sheets getSheetsService(String accessToken)`
    - `static Drive  getDriveService(String accessToken)`

- **Tokens**

    - `static ETRXTokenInfo getMiddlewareToken(ETRXoAuthProvider provider, String scope, User user, Organization org)`
    - `static ETRXTokenInfo getValidAccessTokenOrRefresh(ETRXTokenInfo token, String accountId)`
    - `static void validateAccessToken(String accessToken)`
    - `static String refreshAccessToken(String accountId)`

- **Hojas de cálculo**

    - `static String getTabName(int index, String sheetId, ETRXTokenInfo token, String accountID)`
    - `static List<List<Object>> findSpreadsheetAndTab(String sheetId, String tabName, ETRXTokenInfo token, String accountID)`
    - `static List<List<Object>> readSheet(ETRXTokenInfo token, String accountID, String fileId, String range)`
    - `static String getCellValue(List<Object> row, int index)`

- **Drive**

    - `static JSONArray listAccessibleFiles(String type, ETRXTokenInfo token, String accountID)`
    - `static JSONObject createDriveFile(String name, String mimeType, ETRXTokenInfo token, String accountID)`
    - *(protegido)* `static JSONArray listAccessibleFilesByMimeType(String mimeType, ETRXTokenInfo token, String accountID)`

- **Utilidades**

    - `static String extractSheetIdFromUrl(String url)`

    !!!note
        Puede ver la implementación completa en el archivo del repositorio: [GoogleServiceUtil](https://github.com/etendosoftware/com.etendoerp.etendorx/blob/main/src/com/etendoerp/etendorx/utils/GoogleServiceUtil.java){target="_blank"}
## Claves de mensajes I18N

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
    - `getTabName` compone mensajes localizados para casos de índice fuera de rango/hoja vacía, y los errores finalmente se lanzan como `OBException`.
    - Otros métodos lanzan `OBException` o `IllegalArgumentException` localizadas, según se indica.
## Resolución de problemas

| Síntoma | Causa probable | Solución |
| --- | --- | --- |
| `ETRX_WrongSheetURL` | Formato de URL no compatible | Proporcione una **URL de Sheets** canónica como `https://docs.google.com/spreadsheets/d/<ID>` o extraiga primero el **ID de archivo** |
| `ETRX_SheetHasNoTabs` / `ETRX_WrongTabNumber` | Sin pestañas / índice fuera de rango | Verifique la estructura de la hoja de cálculo y el índice |
| `ETRX_TabNotFound` | El nombre no coincide | La búsqueda de pestañas **no distingue entre mayúsculas y minúsculas**, pero requiere una coincidencia exacta del título |
| `ETRX_ExpiredToken` | Token de acceso no válido/caducado | Asegúrese de que el endpoint de refresh del middleware sea accesible/esté configurado |
| Solo se devuelven 100 archivos | `pageSize=100` en el listado de Drive | Añada un nuevo helper para gestionar `pageToken` si necesita paginación |
| `ETRX_FailedToCreateFile` | MIME no Google o scope insuficiente | Use `application/vnd.google-apps.*` o implemente el flujo de carga de medios |

---
## Notas de implementación

- **Cabecera de autenticación**: Añadida por `bearerTokenInitializer` para todas las solicitudes.
- **Nombres de la aplicación**: `"Google Sheets Java Integration"` para `getSheetsService` / `getDriveService`; `"Etendo Google Picker Integration"` en `readSheet`.
- **Compatibilidad con Shared Drives**: El listado de Drive establece `supportsAllDrives=true`, `includeItemsFromAllDrives=true`, `corpora=allDrives`.
- **Persistencia del token**: Al refrescar, actualiza `token` y establece `validUntil` a **ahora + 1 hora**; persiste mediante `OBDal`.
- **Gestión de errores**: Las respuestas distintas de 200 se convierten en `OBException` localizadas con claves significativas.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.