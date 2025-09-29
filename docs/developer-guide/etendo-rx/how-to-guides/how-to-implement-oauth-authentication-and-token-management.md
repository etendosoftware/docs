---
tags:
  - How to
  - OAuth
  - Authentication
  - Etendo RX
  - SSO
  - Google
  - Token Management
---

# How to Implement OAuth Authentication and Token Management in Etendo RX

## Overview

This guide describes how to integrate Single Sign-On (SSO) authentication and OAuth 2.0 access token management between Etendo RX (ERP) and an external Middleware (EtendoAuth) that brokers identity (Auth0 or another OpenID Connect IdP) and Google APIs (Drive, Picker, etc.).

It covers architecture, data model, authentication flow, token acquisition, persistence, renewal, error handling, operational procedures, code references, and a support checklist.

## 1. Architecture and Responsibilities

### Etendo RX (ERP)

- Maintains OAuth providers configuration (endpoints, credentials, scopes).
- Delegates user authentication and Google OAuth consent flows to the Middleware when configured.
- Persists received access tokens and related metadata.
- Cleans previous tokens for the same user + provider before saving a new one.

### Middleware (EtendoAuth)

- Provides SSO via Auth0 (or any OIDC IdP): builds authorize URL, exchanges authorization code, validates ID Token (JWKS), and returns control to the ERP.
- Orchestrates Google OAuth 2.0 consent and token exchange / refresh.
- Issues short‑lived internal authorization codes (ephemeral) for secure backchannel exchange (optional).
- Stores refresh tokens securely (in production use an encrypted database, not in‑memory map).

### Data Model (Etendo RX)

| Table | Purpose |
|-------|---------|
| `ETRX_OAUTH_PROVIDER` | OAuth provider metadata (client id/secret, endpoints, grant type, redirect URI, userinfo URI, JWKS URL, scopes, flags). |
| `ETRX_TOKEN_INFO` | Access token, validity, provider scope context, user linkage, flags (e.g. `APPROVE_GOOGLE_DOC`). |
| `ETRX_TOKEN_USER` | User ↔ token relationship depending on security model. |
| `ETRX_INSTANCE_CONNECTOR` | External middleware instance registration (base URL, authorization type, credentials/token if required). |

## 2. Authentication Flow (SSO via Auth0)

Objective: authenticate the user and optionally return an internal short‑lived code for ERP session linkage.

High-level sequence:

1. ERP redirects user to Middleware `/login?provider=auth0&redirect_uri=<erp_return>&account_id=<account>`.
2. Middleware builds Auth0 `/authorize` URL (scope: `openid profile email`) and redirects user.
3. IdP (Auth0) authenticates user and redirects to Middleware `/callback?code=...&state=...`.
4. Middleware exchanges `code` for tokens (`id_token`, `access_token`).
5. Middleware validates `id_token` signature (JWKS), issuer, audience, `exp`, `iat`.
6. Middleware redirects to original ERP `redirect_uri` with either user info or an internal ephemeral `code` (if `/authorize` flow is used).
7. ERP (optional) POSTs the ephemeral `code` to `/authorize` to retrieve claims (sub, email, account).
8. ERP creates / updates the internal session and associates the user.

Notes:
- ERP may also accept Bearer JWT directly in incoming requests (tests reference `SWSAuthenticationManagerTest`).
- Ephemeral codes are stored for a short TTL (e.g. 10 minutes) in Middleware memory store.

## 3. OAuth Token Generation and Management (Google)

Objective: obtain and maintain valid Google API access tokens (e.g. Drive scope `drive.file`).

High-level sequence:

1. User triggers "Get Middleware Token" in ERP and selects a scope.
2. ERP builds a `state` payload `{ userId, redirect }` (redirect = ERP servlet endpoint `SaveTokenFromMiddleware`).
3. ERP redirects to Middleware `/oauth/google/start?state=<base64url>`.
4. Middleware decides whether to request consent (missing or first time refresh token) and redirects to Google authorize endpoint.
5. Google returns to Middleware `/oauth/google/callback?code=...&state=...`.
6. Middleware exchanges the authorization code at `https://oauth2.googleapis.com/token`.
7. Middleware stores `refresh_token` (if new) and current `access_token` with expiry.
8. Middleware redirects to ERP `redirect` URL with token (or error) parameters.
9. ERP servlet `SaveTokenFromMiddleware` persists token in `ETRX_TOKEN_INFO` (after deleting previous token for same user/provider).

Transparent Refresh:
- Middleware function `ensureAccessToken(userId)` checks expiry; if expired, uses stored `refresh_token` to obtain a new `access_token` and updates cache.

## 4. ERP Configuration (Etendo RX)

### `ETRX_OAUTH_PROVIDER`

Key fields:
- `AUTHORIZATION_URI`, `TOKEN_URI`, `USER_INFO_URI`, `JWKSETURI`
- `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI`
- `AUTHORIZATION_GRANT_TYPE` (e.g. `authorization_code`)
- `CLIENT_AUTHENTICATION_METHOD` (e.g. `client_secret_basic`)
- `CODE_CHALLENGE_METHOD` (PKCE `S256` if public client)
- `USERNAMEATTRIBUTE` (e.g. `email` or `sub`)
- `PROVIDER_SCOPE`
- `GET_MIDDLEWARE_TOKEN` (flag to delegate to Middleware predefined flow)

### `ETRX_TOKEN_INFO`
Stores:
- `AD_USER_ID`, `ETRX_OAUTH_PROVIDER_ID`
- `TOKEN` (access token), `VALID_UNTIL`
- `MIDDLEWARE_PROVIDER` (e.g. `google - drive.file`)
- Flags (e.g. `APPROVE_GOOGLE_DOC`)

### `ETRX_INSTANCE_CONNECTOR`
Registers:
- Middleware base URL
- Authorization type and credentials (token / basic user & password)

## 5. Middleware Endpoints Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/login` | GET | Start SSO with Auth0. Params: `provider`, `redirect_uri`, `account_id?` |
| `/callback` | GET | Auth0 callback: exchange code → tokens, validate JWT, redirect ERP |
| `/authorize` | POST | Exchange ephemeral internal code for user claims (secure backchannel) |
| `/oauth/google/start` | GET | Begin Google consent. Requires `state` |
| `/oauth/google/callback` | GET | Exchange Google code → tokens; redirect ERP |
| `/picker` | GET | Google Picker example; ensures valid access token |
| `/jwks` | GET | JWKS exposure (if Middleware signs tokens) |
| `/logout`, `/register` | Var | Secondary flows |

## 6. Error Handling and Traceability

### Middleware

- Structured log prefixes: `[LOGIN]`, `[CALLBACK]`, `[AUTHORIZE]`, `[GOOGLE]`.
- Common errors:
  - Missing `state` → 400
  - Missing `refresh_token` and none cached → 400
  - Token exchange failure → 500 (`token_exchange_failed`)
  - Invalid ID Token signature / audience / issuer → 401

### ERP

- `SaveTokenFromMiddleware` interprets `error` and `error_description` query parameters.
- Converts technical codes (e.g. `access_denied`) to user-friendly messages.
- Deletes previous token records before insertion (avoid duplicates / stale tokens).

## 7. Implementation Best Practices

Security:
- Enforce HTTPS end-to-end.
- Keep `refresh_token` only in Middleware (not exposed to ERP UI). Provide only access tokens when strictly required.
- Validate `iss`, `aud`, `exp`, `iat` of ID Tokens.
- Limit scopes (principle of least privilege, e.g. `drive.file`).
- Rotate client secrets; store in secret manager.
- Use PKCE (`S256`) for public clients.
- Configure strict CORS and secure cookies.

Reliability:
- Replace in-memory token store with encrypted persistent storage in production.
- Synchronize clocks (avoid premature expiry rejections).
- Implement retry with backoff for transient network errors to Google / Auth0.

Observability:
- Correlate logs using a request ID propagated from ERP → Middleware.
- Mask sensitive values (tokens, client secrets) in logs.

## 8. Operational Procedure (Step-by-Step)

### A. Register OAuth Provider in ERP
1. Create record in `ETRX_OAUTH_PROVIDER` with IdP endpoints and credentials.
2. Set `REDIRECT_URI` to the ERP servlet endpoint handling token return (e.g. `/etendorx/SaveTokenFromMiddleware`).
3. Enable `GET_MIDDLEWARE_TOKEN` if delegating token acquisition to Middleware.
4. (Optional) Set `JWKSETURI` for direct JWT validation.

### B. Test SSO (Auth0)
1. Trigger ERP SSO action → calls Middleware `/login`.
2. Authenticate via Auth0 → returns to Middleware `/callback` → redirects ERP.
3. Confirm ERP session created and user mapped by `email` or `sub`.

### C. Obtain Google Token (Drive Example)
1. In ERP invoke action "Get Middleware Token" selecting scope (e.g. `drive.file`).
2. Flow: `/oauth/google/start` → Google consent → `/oauth/google/callback` → ERP redirect.
3. Validate new entry in `ETRX_TOKEN_INFO` with correct `MIDDLEWARE_PROVIDER` value and expiry.
4. Test Google API / Picker integration; Middleware refreshes tokens transparently.

## 9. Code References

### ERP (Etendo RX)
- Servlet: `src/com/etendoerp/etendorx/SaveTokenFromMiddleware.java`
- Tables:
  - `src-db/database/model/tables/ETRX_OAUTH_PROVIDER.xml`
  - `src-db/database/model/tables/ETRX_TOKEN_INFO.xml`
  - `src-db/database/model/tables/ETRX_TOKEN_USER.xml`
  - `src-db/database/model/tables/ETRX_INSTANCE_CONNECTOR.xml`

### Middleware (EtendoAuth)
- Auth0 Routes: `src/routes/login.ts`, `src/routes/callback.ts`, `src/routes/authorize.ts`
- Auth0 Service: `src/services/auth0.ts` (authorize URL, token exchange, JWT validation)
- Google Routes: `src/routes/oauth_google.ts`
- Google Logic: `src/googleAuth.ts` (`exchangeCodeForTokens`, `ensureAccessToken`, `refreshAccessToken`)
- Token Store (replace in production): `src/tokenStore.ts`
- Google Picker Example: `src/routes/picker.ts`

## 10. Support Checklist

- Auth0 env vars: `AUTH0_DOMAIN`, `AUTH0_CLIENT_ID`, `AUTH0_CLIENT_SECRET` set.
- Google env vars: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`, `GOOGLE_API_KEY` set.
- ERP `ETRX_OAUTH_PROVIDER` configured or `GET_MIDDLEWARE_TOKEN = Y`.
- Middleware base URL registered in `ETRX_INSTANCE_CONNECTOR` (if used).
- `REDIRECT_URI` matches IdP and Google console configuration.
- System clocks synchronized.
- Valid TLS certificates.
- Middleware logs show expected sequence `[LOGIN]` → `[CALLBACK]`.
- On `access_denied` errors: verify user consent, scopes, and IdP policy.

## Summary

This document centralizes the steps and structures required to implement secure OAuth SSO and Google token management in Etendo RX using a dedicated Middleware layer. Follow best practices to ensure security, reliability, and maintainability.