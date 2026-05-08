---
tags:
    - Copilot
    - IA
    - Tool
    - Google Spreadsheets
---

# Herramienta de Google Spreadsheets { #google-spreadsheets-tool }
:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general { #overview }

La herramienta **Google Spreadsheets** es una potente utilidad para interactuar directamente con Google Sheets. Permite al agente gestionar hojas de cálculo de forma programática a través de las **API de Google Drive y Google Sheets**.

La herramienta funciona mediante cinco modos distintos:

  - **`list`**: Lista todas las hojas de cálculo de Google Spreadsheets accesibles para el usuario.
  - **`create`**: Crea una nueva hoja de cálculo vacía.
  - **`upload`**: Carga datos desde un archivo CSV local a una nueva hoja de Google.
  - **`read`**: Lee datos de un rango de celdas especificado dentro de una hoja de cálculo.
  - **`download`**: Descarga el contenido de una hoja de cálculo a un archivo CSV local.

## Configuración y autenticación { #setup-authentication }

Esta herramienta requiere un token de **Google OAuth** preconfigurado identificado por un `alias`. Este `alias` debe proporcionarse en cada solicitud para autenticarse con los servicios de Google.

## Parámetros { #parameters }

La funcionalidad de la herramienta viene determinada por el parámetro `mode`. Los parámetros obligatorios y opcionales cambian en función del modo seleccionado.

### Parámetros generales { #general-parameters }

  - `alias` (string, required): El alias del token OAuth preconfigurado.
  - `mode` (string, required): La acción a realizar. Valores admitidos: `list`, `create`, `upload`, `read`, `download`.

### Parámetros específicos por modo { #mode-specific-parameters }

  - `name` (string): El nombre para una hoja de cálculo.

      - Obligatorio para el modo `create`.
      - Opcional para el modo `upload` (si no se proporciona, por defecto se usa el nombre del archivo CSV cargado).

  - `file_id` (string): El ID único de la hoja de cálculo de destino (se encuentra en su URL).

      - Obligatorio para los modos `read` y `download`.

  - `range` (string, optional): El rango de celdas sobre el que operar (p. ej., `Sheet1!A1:B10`).

      - Se utiliza en los modos `read` y `download`.
      - Si no se proporciona, por defecto es `A1:Z1000`.

  - `file_path` (string): La ruta local a un archivo `.csv`.

      - Obligatorio para el modo `upload`.

## Modos de funcionamiento { #modes-of-operation }

### `list`

Lista todas las hojas de Google Sheets a las que puede acceder el usuario autenticado.

  - **Parámetros**: `alias`, `mode='list'`
  - **Solicitud de ejemplo**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "list"
    }
    ```
  - **Respuesta de éxito de ejemplo**:
    ```
    Hojas de cálculo encontradas:
    - Monthly Budget (ID: 1a2b3c...)
    - Project Plan (ID: 4d5e6f...)
    ```

### `create`

Crea una nueva hoja de cálculo en blanco con un nombre determinado.

  - **Parámetros**: `alias`, `mode='create'`, `name`
  - **Solicitud de ejemplo**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "create",
      "name": "Q3 Sales Report"
    }
    ```
  - **Respuesta de éxito de ejemplo**:
    ```
    Spreadsheet 'Q3 Sales Report' created with ID: 1a2b3c.... Can be accessed at: https://docs.google.com/spreadsheets/d/1a2b3c.../edit
    ```

### `upload`

Carga un archivo CSV local y lo convierte en una nueva hoja de Google.

  - **Parámetros**: `alias`, `mode='upload'`, `file_path`, `name` (optional)
  - **Solicitud de ejemplo**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "upload",
      "file_path": "/path/to/data.csv",
      "name": "Imported Sales Data"
    }
    ```
  - **Respuesta de éxito de ejemplo**:
    ```
    ✅ CSV file 'Imported Sales Data' uploaded successfully.
    🔗 Link: https://docs.google.com/spreadsheets/d/4d5e6f.../edit
    ```

### `read`

Lee y devuelve los datos de un rango específico dentro de una hoja.

  - **Parámetros**: `alias`, `mode='read'`, `file_id`, `range` (optional)
  - **Solicitud de ejemplo**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "read",
      "file_id": "1a2b3c...",
      "range": "A1:B2"
    }
    ```
  - **Respuesta de éxito de ejemplo**:
    ```
    Spreadsheet content:
    Header1, Header2
    Value1, Value2
    ```

### `download`

Descarga una hoja (o un rango específico) y la guarda como un archivo CSV en una ruta local temporal.

  - **Parámetros**: `alias`, `mode='download'`, `file_id`, `range` (optional)
  - **Solicitud de ejemplo**:
    ```json
    {
      "alias": "my_google_token",
      "mode": "download",
      "file_id": "1a2b3c..."
    }
    ```
  - **Respuesta de éxito de ejemplo**:
    ```
    ✅ CSV file downloaded at: /tmp/copilotAttachedFiles/some-uuid/sheet_data.csv
    ```

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.