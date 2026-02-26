---
tags:
  - How to
  - OAuth
  - Authentication
  - Etendo RX
  - SSO
  - Google
  - Token Management
status: beta
---

# Cómo implementar la autenticación OAuth y la gestión de tokens en Etendo RX

## Visión general

Esta guía describe cómo integrar la autenticación de inicio de sesión único (SSO) y la gestión de tokens de acceso OAuth 2.0 entre Etendo RX (ERP) y un Middleware externo (EtendoAuth) que intermedia la identidad (Auth0 u otro IdP OpenID Connect) y las APIs de Google (Drive, Picker, etc.).

Cubre la arquitectura, el modelo de datos, el flujo de autenticación, la obtención de tokens, la persistencia, la renovación, el manejo de errores, los procedimientos operativos, las referencias de código y una lista de verificación de soporte.

## 1. Arquitectura y responsabilidades

### Etendo RX (ERP)

- Mantiene la configuración de proveedores OAuth (endpoints, credenciales, scopes).
- Delega la autenticación de usuario y los flujos de consentimiento OAuth de Google al Middleware cuando está configurado.
- Persiste los tokens de acceso recibidos y los metadatos relacionados.
- Limpia los tokens anteriores para el mismo usuario + proveedor antes de guardar uno nuevo.

### Middleware (EtendoAuth)

- Proporciona SSO mediante Auth0 (o cualquier IdP OIDC): construye la URL de autorización, intercambia el código de autorización, valida el ID Token (JWKS) y devuelve el control al ERP.
- Orquesta el consentimiento OAuth 2.0 de Google y el intercambio / refresco de tokens.
- Emite códigos de autorización internos de corta duración (efímeros) para un intercambio seguro por canal de backchannel (opcional).
- Almacena los refresh tokens de forma segura (en producción use una base de datos cifrada, no un mapa en memoria).

### Modelo de datos (Etendo RX)

| Tabla | Propósito |
|-------|-----------|
| `ETRX_OAUTH_PROVIDER` | Metadatos del proveedor OAuth (client id/secret, endpoints, tipo de grant, URI de redirección, URI de userinfo, URL de JWKS, scopes, flags). |
| `ETRX_TOKEN_INFO` | Token de acceso, validez, contexto de scope del proveedor, vinculación con el usuario, flags (p. ej. `APPROVE_GOOGLE_DOC`). |
| `ETRX_TOKEN_USER` | Relación usuario ↔ token según el modelo de seguridad. |
| `ETRX_INSTANCE_CONNECTOR` | Registro de instancia de middleware externa (URL base, tipo de autorización, credenciales/token si se requiere). |

## 2. Flujo de autenticación (SSO vía Auth0)

Objetivo: autenticar al usuario y, opcionalmente, devolver un código interno de corta duración para la vinculación de sesión del ERP.

Secuencia de alto nivel:

1. El ERP redirige al usuario al Middleware `/login?provider=auth0&redirect_uri=<erp_return>&account_id=<account>`.
2. El Middleware construye la URL de Auth0 `/authorize` (scope: `openid profile email`) y redirige al usuario.
3. El IdP (Auth0) autentica al usuario y redirige al Middleware `/callback?code=...&state=...`.
4. El Middleware intercambia `code` por tokens (`id_token`, `access_token`).
5. El Middleware valida la firma de `id_token` (JWKS), el issuer, el audience, `exp`, `iat`.
6. El Middleware redirige al `redirect_uri` original del ERP con información del usuario o con un `code` interno efímero (si se utiliza el flujo `/authorize`).
7. El ERP (opcional) hace POST del `code` efímero a `/authorize` para recuperar claims (sub, email, account).
8. El ERP crea / actualiza la sesión interna y asocia el usuario.

Notas:
- El ERP también puede aceptar Bearer JWT directamente en las solicitudes entrantes (las pruebas referencian `SWSAuthenticationManagerTest`).
- Los códigos efímeros se almacenan durante un TTL corto (p. ej. 10 minutos) en el almacén en memoria del Middleware.

## 3. Generación y gestión de tokens OAuth (Google)

Objetivo: obtener y mantener tokens de acceso válidos para las APIs de Google (p. ej. scope de Drive `drive.file`).

Secuencia de alto nivel:

1. El usuario dispara la acción "Obtener token del Middleware" en el ERP y selecciona un scope.
2. El ERP construye un payload `state` `{ userId, redirect }` (redirect = endpoint del servlet del ERP `SaveTokenFromMiddleware`).
3. El ERP redirige al Middleware `/oauth/google/start?state=<base64url>`.
4. El Middleware decide si solicitar consentimiento (refresh token ausente o primera vez) y redirige al endpoint de autorización de Google.
5. Google vuelve al Middleware `/oauth/google/callback?code=...&state=...`.
6. El Middleware intercambia el código de autorización en `https://oauth2.googleapis.com/token`.
7. El Middleware almacena el `refresh_token` (si es nuevo) y el `access_token` actual con su expiración.
8. El Middleware redirige al ERP a la URL `redirect` con parámetros de token (o de error).
9. El servlet del ERP `SaveTokenFromMiddleware` persiste el token en `ETRX_TOKEN_INFO` (tras eliminar el token anterior para el mismo usuario/proveedor).

Refresco transparente:
- La función del Middleware `ensureAccessToken(userId)` comprueba la expiración; si está expirado, usa el `refresh_token` almacenado para obtener un nuevo `access_token` y actualiza la caché.

## 4. Configuración del ERP (Etendo RX)

### `ETRX_OAUTH_PROVIDER`

Campos clave:

- `AUTHORIZATION_URI`, `TOKEN_URI`, `USER_INFO_URI`, `JWKSETURI`
- `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI`
- `AUTHORIZATION_GRANT_TYPE` (p. ej. `authorization_code`)
- `CLIENT_AUTHENTICATION_METHOD` (p. ej. `client_secret_basic`)
- `CODE_CHALLENGE_METHOD` (PKCE `S256` si es un cliente público)
- `USERNAMEATTRIBUTE` (p. ej. `email` o `sub`)
- `PROVIDER_SCOPE`
- `GET_MIDDLEWARE_TOKEN` (flag para delegar al flujo predefinido del Middleware)

### `ETRX_TOKEN_INFO`
Almacena:

- `AD_USER_ID`, `ETRX_OAUTH_PROVIDER_ID`
- `TOKEN` (token de acceso), `VALID_UNTIL`
- `MIDDLEWARE_PROVIDER` (p. ej. `google - drive.file`)
- Flags (p. ej. `APPROVE_GOOGLE_DOC`)

### `ETRX_INSTANCE_CONNECTOR`
Registra:

- URL base del Middleware
- Tipo de autorización y credenciales (token / usuario y contraseña basic)

## 5. Resumen de endpoints del Middleware

| Endpoint | Método | Propósito |
|----------|--------|-----------|
| `/login` | GET | Iniciar SSO con Auth0. Parámetros: `provider`, `redirect_uri`, `account_id?` |
| `/callback` | GET | Callback de Auth0: intercambiar código → tokens, validar JWT, redirigir al ERP |
| `/authorize` | POST | Intercambiar código interno efímero por claims del usuario (backchannel seguro) |
| `/oauth/google/start` | GET | Iniciar consentimiento de Google. Requiere `state` |
| `/oauth/google/callback` | GET | Intercambiar código de Google → tokens; redirigir al ERP |
| `/picker` | GET | Ejemplo de Google Picker; asegura un token de acceso válido |
| `/jwks` | GET | Exposición de JWKS (si el Middleware firma tokens) |
| `/logout`, `/register` | Var | Flujos secundarios |

## 6. Manejo de errores y trazabilidad

### Middleware

- Prefijos de log estructurados: `[LOGIN]`, `[CALLBACK]`, `[AUTHORIZE]`, `[GOOGLE]`.
- Errores comunes:

  - Falta `state` → 400
  - Falta `refresh_token` y no hay ninguno en caché → 400
  - Fallo en el intercambio de token → 500 (`token_exchange_failed`)
  - Firma / audience / issuer inválidos del ID Token → 401

### ERP

- `SaveTokenFromMiddleware` interpreta los parámetros de query `error` y `error_description`.
- Convierte códigos técnicos (p. ej. `access_denied`) en mensajes amigables para el usuario.
- Elimina los registros de tokens anteriores antes de insertar (evitar duplicados / tokens obsoletos).

## 7. Buenas prácticas de implementación

Seguridad:

- Imponga HTTPS de extremo a extremo.
- Mantenga el `refresh_token` solo en el Middleware (no expuesto a la UI del ERP). Proporcione únicamente tokens de acceso cuando sea estrictamente necesario.
- Valide `iss`, `aud`, `exp`, `iat` de los ID Tokens.
- Limite los scopes (principio de mínimo privilegio, p. ej. `drive.file`).
- Rote los client secrets; almacénelos en un gestor de secretos.
- Use PKCE (`S256`) para clientes públicos.
- Configure CORS estricto y cookies seguras.

Fiabilidad:

- Sustituya el almacén de tokens en memoria por almacenamiento persistente cifrado en producción.
- Sincronice relojes (evitar rechazos por expiración prematura).
- Implemente reintentos con backoff para errores de red transitorios hacia Google / Auth0.

Observabilidad:

- Correlacione logs usando un ID de solicitud propagado desde ERP → Middleware.
- Enmascare valores sensibles (tokens, client secrets) en los logs.

## 8. Procedimiento operativo (paso a paso)

### A. Registrar proveedor OAuth en el ERP

1. Cree un registro en `ETRX_OAUTH_PROVIDER` con endpoints y credenciales del IdP.
2. Configure `REDIRECT_URI` al endpoint del servlet del ERP que gestiona el retorno del token (p. ej. `/etendorx/SaveTokenFromMiddleware`).
3. Habilite `GET_MIDDLEWARE_TOKEN` si delega la obtención del token al Middleware.
4. (Opcional) Configure `JWKSETURI` para validación directa de JWT.

### B. Probar SSO (Auth0)

1. Dispare la acción de SSO del ERP → llama al Middleware `/login`.
2. Autentíquese mediante Auth0 → vuelve al Middleware `/callback` → redirige al ERP.
3. Confirme que se crea la sesión del ERP y que el usuario se mapea por `email` o `sub`.

### C. Obtener token de Google (ejemplo de Drive)

1. En el ERP invoque la acción "Obtener token del Middleware" seleccionando el scope (p. ej. `drive.file`).
2. Flujo: `/oauth/google/start` → consentimiento de Google → `/oauth/google/callback` → redirección al ERP.
3. Valide una nueva entrada en `ETRX_TOKEN_INFO` con el valor correcto de `MIDDLEWARE_PROVIDER` y su expiración.
4. Pruebe la integración con la API de Google / Picker; el Middleware refresca los tokens de forma transparente.

## 9. Referencias de código

### ERP (Etendo RX)

- Servlet: `src/com/etendoerp/etendorx/SaveTokenFromMiddleware.java`
- Tablas:

  - `src-db/database/model/tables/ETRX_OAUTH_PROVIDER.xml`
  - `src-db/database/model/tables/ETRX_TOKEN_INFO.xml`
  - `src-db/database/model/tables/ETRX_TOKEN_USER.xml`
  - `src-db/database/model/tables/ETRX_INSTANCE_CONNECTOR.xml`

### Middleware (EtendoAuth)

- Rutas de Auth0: `src/routes/login.ts`, `src/routes/callback.ts`, `src/routes/authorize.ts`
- Servicio de Auth0: `src/services/auth0.ts` (URL de autorización, intercambio de token, validación de JWT)
- Rutas de Google: `src/routes/oauth_google.ts`
- Lógica de Google: `src/googleAuth.ts` (`exchangeCodeForTokens`, `ensureAccessToken`, `refreshAccessToken`)
- Almacén de tokens (sustituir en producción): `src/tokenStore.ts`
- Ejemplo de Google Picker: `src/routes/picker.ts`

## 10. Lista de verificación de soporte

- Variables de entorno de Auth0: `AUTH0_DOMAIN`, `AUTH0_CLIENT_ID`, `AUTH0_CLIENT_SECRET` configuradas.
- Variables de entorno de Google: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`, `GOOGLE_API_KEY` configuradas.
- ERP `ETRX_OAUTH_PROVIDER` configurado o `GET_MIDDLEWARE_TOKEN = Y`.
- URL base del Middleware registrada en `ETRX_INSTANCE_CONNECTOR` (si se utiliza).
- `REDIRECT_URI` coincide con la configuración del IdP y de la consola de Google.
- Relojes del sistema sincronizados.
- Certificados TLS válidos.
- Los logs del Middleware muestran la secuencia esperada `[LOGIN]` → `[CALLBACK]`.
- En errores `access_denied`: verifique el consentimiento del usuario, los scopes y la política del IdP.

## Resumen

Este documento centraliza los pasos y las estructuras necesarias para implementar SSO OAuth seguro y la gestión de tokens de Google en Etendo RX usando una capa de Middleware dedicada. Siga las buenas prácticas para garantizar seguridad, fiabilidad y mantenibilidad.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.