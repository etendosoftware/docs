---
tags:
    - Copilot
    - IA
    - Herramienta
    - Herramienta de carga de token OAuth
---

# Herramienta de carga de token OAuth
:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de carga de token OAuth** es una utilidad clave de seguridad y gestión de sesión. Su función principal es obtener de forma segura un **token OAuth** preconfigurado desde el backend de Etendo y cargarlo en la memoria de la conversación actual.

Esta herramienta no ejecuta una acción por sí misma, sino que actúa como un primer paso necesario para cualquier flujo de trabajo que requiera **autenticación OAuth2** (p. ej., acceder a Google Drive o Google Sheets). Al cargar el token y devolver únicamente un `alias`, permite que otras herramientas utilicen la credencial sin exponer nunca el valor sensible del token al modelo de IA ni al usuario.

## Flujo de trabajo previsto

Esta herramienta está diseñada para ser la primera llamada en un proceso de varios pasos. El flujo de trabajo típico es el siguiente:

1.  Un usuario solicita al agente que realice una acción que requiere un servicio externo autenticado (como Google Drive).
2.  El agente primero llama a `LoadOAuthTokenTool`.
3.  Esta herramienta obtiene el token OAuth desde Etendo y lo almacena en la memoria de la conversación, devolviendo un `alias` seguro.
4.  A continuación, el agente llama a la herramienta requerida (p. ej., `GoogleDriveTool`) y pasa el `alias` que acaba de recibir.
5.  `GoogleDriveTool` utiliza el `alias` para recuperar el token real desde la memoria de la conversación y completa la solicitud del usuario.

## Parámetros

  - `al` (string, opcional): Un alias (un nombre personalizado) para el token OAuth.
      - Si se proporciona un alias, el token se cargará en memoria bajo ese nombre específico.
      - Si este parámetro **no se proporciona**, se generará automáticamente un alias único y aleatorio (p. ej., `TOKEN_1234abcd-....`).
      - En ambos casos, el alias utilizado se devuelve en el mensaje final de éxito.

## Funcionalidad

La herramienta ejecuta los siguientes pasos:

1.  **Determina el alias**: utiliza el `al` proporcionado por el usuario o genera uno nuevo si no existe.
2.  **Obtiene el token**: realiza una llamada segura del lado del servidor a un webhook de Etendo (`/webhooks/ReadOAuthToken`) para recuperar el token OAuth preconfigurado. Un administrador de la organización debe haber configurado este token previamente en el backend de Etendo.
3.  **Almacena el token**: almacena el token obtenido en el contexto de la conversación actual (`ThreadContext`) en un diccionario, utilizando el alias como clave.
4.  **Devuelve el alias**: devuelve un mensaje de éxito al agente, confirmando que el token está cargado y listo para su uso mediante el alias devuelto.

## Ejemplos de uso

### Ejemplo 1: Cargar un token con un alias generado

Cuando no necesita un nombre específico para el token, puede llamar a la herramienta sin parámetros.

**Solicitud:**

```json
{}
```

**Ejemplo de respuesta de éxito:**

```
OAuth token loaded successfully with alias: TOKEN_a1b2c3d4-e5f6-7890-gh12-i3j4k5l6m7n8. You can now use this alias to access the token.
```

### Ejemplo 2: Cargar un token con un alias personalizado

Esto es útil si desea referirse al token con un nombre fácil de recordar.

**Solicitud:**

```json
{
  "al": "my_work_google_account"
}
```

**Ejemplo de respuesta de éxito:**

```
OAuth token loaded successfully with alias: my_work_google_account. You can now use this alias to access the token.
```

### Ejemplo 3: Flujo de trabajo conceptual en dos pasos

A continuación se muestra cómo un agente utilizaría esta herramienta en la práctica para listar archivos de Google Drive.

  - **Paso 1: Cargar el token**

      - **Llamada a la herramienta:** `LoadOAuthTokenTool()`
      - **Resultado:** el agente recibe el mensaje: "OAuth token loaded successfully with alias: `TOKEN_a1b2...`"

  - **Paso 2: Usar el alias en la herramienta de destino**

      - **Llamada a la herramienta:** `GoogleDriveTool(alias="TOKEN_a1b2...", mode="list")`
      - **Resultado:** `GoogleDriveTool` lista correctamente los archivos porque pudo acceder al token usando el alias proporcionado.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.