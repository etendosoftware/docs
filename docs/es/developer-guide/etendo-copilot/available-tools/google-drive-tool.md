---
tags:
    - Copilot
    - IA
    - Tool
    - Google Drive
---

# Herramienta de Google Drive { #google-drive-tool }
:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general { #overview }

La **Herramienta de Google Drive** proporciona una interfaz directa para interactuar con el Google Drive de un usuario. Permite al agente realizar operaciones con archivos en dos modos principales:

  - **`list`**: Busca y lista archivos de un tipo específico que sean accesibles mediante las credenciales proporcionadas.
  - **`upload`**: Sube un archivo local desde el sistema al Google Drive del usuario.

Esta herramienta es esencial para flujos de trabajo que requieren leer o escribir archivos en Google Drive como parte de un proceso automatizado.

## Configuración y autenticación { #setup-authentication }

Para utilizar esta herramienta, debe preconfigurarse un token de **Google OAuth** e identificarse mediante un `alias`. Este `alias` es un parámetro obligatorio para cada solicitud, ya que se utiliza para autenticarse de forma segura con la **API de Google Drive**.

## Parámetros { #parameters }

El comportamiento de la herramienta se controla mediante el parámetro `mode`. En función del modo seleccionado, pueden requerirse otros parámetros.

### Parámetros generales { #general-parameters }

  - `alias` (string, required): El alias del token OAuth preconfigurado que se utilizará para la autenticación.
  - `mode` (string, required): La acción a realizar. Los valores admitidos son `'list'` o `'upload'`.

### Parámetros del modo `list` { #list-mode-parameters }

  - `file_type` (string, optional): El tipo de archivo por el que filtrar (p. ej., `spreadsheet`, `document`, `pdf`, `folder`). **Por defecto, `spreadsheet`**.

### Parámetros del modo `upload` { #upload-mode-parameters }

  - `file_path` (string, required): La ruta local del archivo que se subirá.
  - `name` (string, optional): El nombre que se asignará al archivo una vez subido a Google Drive. Si no se proporciona, por defecto se utilizará el nombre de archivo original de `file_path`.
  - `mime_type` (string, optional): El tipo MIME del archivo (p. ej., `application/pdf`, `image/png`). Si no se proporciona, por defecto se utilizará `application/octet-stream`.

## Modos de funcionamiento { #modes-of-operation }

### Modo de listado (`mode='list'`) { #list-mode-modelist }

Este modo se utiliza para encontrar y mostrar archivos en Google Drive.

  - **Proceso**: Consulta Google Drive para obtener archivos que coincidan con el `file_type` especificado y que sean accesibles para el usuario asociado al `alias`.
  - **Salida**: Si se realiza correctamente, devuelve una lista formateada de nombres de archivo y sus correspondientes IDs de Google Drive. Si no se encuentran archivos, devuelve un mensaje de notificación.

**Solicitud de ejemplo:**

```json
{
    "alias": "my_google_token",
    "mode": "list",
    "file_type": "pdf"
}
```

**Respuesta de éxito de ejemplo:**

```
📂 Archivos de tipo 'pdf':
- Q1_Report.pdf (ID: 1a2b3c4d5e6f...)
- Project_Proposal.pdf (ID: 7g8h9i0j1k2l...)
```

### Modo de subida (`mode='upload'`) { #upload-mode-modeupload }

Este modo se utiliza para subir un archivo a Google Drive.

  - **Proceso**: Toma un `file_path` local, lee el archivo y lo sube a la raíz del Google Drive del usuario.
  - **Salida**: Si la subida se realiza correctamente, devuelve un mensaje de confirmación que incluye el nombre del archivo subido y un enlace directo para compartirlo en Google Drive.

**Solicitud de ejemplo:**

```json
{
    "alias": "my_google_token",
    "mode": "upload",
    "file_path": "/path/to/local/image.png",
    "name": "My Vacation Photo.png",
    "mime_type": "image/png"
}
```

**Respuesta de éxito de ejemplo:**

```
✅ Archivo 'My Vacation Photo.png' subido correctamente.
🔗 Enlace: https://drive.google.com/file/d/1x2y3z4a5b6c.../view
```

## Gestión de errores { #error-handling }

La herramienta devolverá un `ToolOutputError` si:

  - Se proporciona un `mode` no admitido.
  - Falta un parámetro obligatorio para un modo específico (p. ej., `file_path` para el modo `upload`).
  - Se produce cualquier otra excepción durante el proceso, como un fallo de autenticación o un error de archivo no encontrado.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.