---
title: Cómo conectar un Etendo Copilot Agent a un Telegram bot con n8n
status: beta
tags:
  - Etendo Copilot
  - Telegram
  - n8n
  - Automatización
  - Integración de bots
---

# Cómo conectar un Etendo Copilot Agent a un Telegram bot con n8n

## Visión general

Esta guía explica cómo exponer un **Etendo Copilot Agent** existente como un **Telegram bot** interactivo utilizando la plataforma de automatización **n8n**. 

Los usuarios envían mensajes a un Telegram bot. n8n los recibe, reenvía el texto al endpoint de Copilot y devuelve la respuesta generada al mismo chat. El mismo patrón puede adaptarse a otros canales (p. ej., WhatsApp vía Twilio) sustituyendo los nodos de disparador/envío.

## Arquitectura

```
Usuario de Telegram  →  Telegram Bot  →  Flujo de trabajo de n8n  →  Etendo Copilot (Agent)
      ↑                                                     ↓
      └──────────────────────── Respuesta (texto) ──────────┘
```

Conceptos clave:

- El nodo **Telegram Trigger** escucha nuevos mensajes.
- El nodo **HTTP Request** llama al endpoint REST de Etendo Copilot.
- El nodo **Send Message** responde al chat de origen.
- **conversation_id** mantiene el contexto conversacional por chat de Telegram.

## Requisitos previos

- Una instancia operativa de **Etendo Classic** con **Etendo Copilot** instalado y configurado.
- Un **Copilot Agent** configurado (obtenga su ID interno desde el encabezado de la ventana del agente).
- Un **Telegram Bot Token** (cree un bot con `@BotFather`).
- Una instancia de **n8n** en ejecución (cloud o autoalojada) con acceso a la URL de la instancia de Etendo.
- Un **usuario de Etendo + token Bearer** (o token de API) dedicado, con únicamente los permisos necesarios para el caso de uso del agente (principio de mínimo privilegio).
- Acceso de red: n8n debe alcanzar `ETENDO_INSTANCE_URL` por HTTPS.

!!! warning "Seguridad"
    Para bots públicos, cree un usuario de Etendo con privilegios mínimos (p. ej., acceso de solo lectura a consultas de stock) para evitar exponer datos sensibles.

## Especificación del endpoint

Endpoint de preguntas de Etendo Copilot:

`POST ETENDO_INSTANCE_URL/etendo/sws/copilot/question`

Encabezados:

- `Authorization: Bearer <TOKEN>`
- `Content-Type: application/json`

Cuerpo (JSON):
```json
{
  "question": "<user message>",
  "app_id": "<AGENT_ID>",
  "conversation_id": "<CHAT_ID>"
}
```

Descripción de campos:

- **question**: Texto sin procesar del usuario de Telegram.
- **app_id**: ID interno del Copilot Agent a invocar.
- **conversation_id**: Identificador estable para mantener el contexto del hilo. Use el `chat.id` de Telegram.

## Flujo de trabajo de n8n: paso a paso

### 1. Nodo Telegram Trigger

Propósito: capturar mensajes entrantes.

Configuración:

- Recurso: `Message`
- Secuencia: `On Update` (mensajes nuevos por defecto)
- Credenciales: su credencial de Telegram Bot (p. ej., `Telegram account 2`).
- Tipos de actualización: `message`

No se requieren parámetros personalizados para un flujo básico de texto.

### 2. Nodo HTTP Request (puente hacia Etendo Copilot)

Propósito: enviar el mensaje del usuario al Copilot Agent.

Configuración:

- **Method**: `POST`
- **URL**: `ETENDO_INSTANCE_URL/etendo/sws/copilot/question`
- **Authentication**: HTTP Bearer (proporcione el token de Etendo)
- **Response Format**: `JSON`
- **Body Content Type**: `JSON / Application JSON`
- **JSON Body** (expresiones habilitadas):

  - `question`: `={{ $json["message"]["text"] }}`
  - `app_id`: codifique de forma fija el ID de su agente (p. ej., `1234567890`) o use una variable de entorno.
  - `conversation_id`: `={{ $json["message"]["chat"]["id"] }}`

Ejemplo de cuerpo en bruto (con expresiones):
```json
{
  "question": "={{ $json.message.text }}",
  "app_id": "1234567890",
  "conversation_id": "={{ $json.message.chat.id }}"
}
```

!!! note "Gestión de errores"
    Añada un nodo **IF** (o **Switch**) adicional después del HTTP Request para detectar estados no 2xx. Enrute los fallos a un mensaje alternativo (p. ej., "Servicio temporalmente no disponible").

### 3. Nodo Send Telegram Message

Propósito: entregar al usuario la respuesta de Copilot.

Configuración:

- **Chat ID**: `={{ $json["message"]["chat"]["id"] }}` (o desde el primer nodo según las conexiones)
- **Texto**: `={{ $json["response"] }}` (asumiendo que el servicio de Copilot devuelve `{ "response": "..." }`).

Si la estructura de salida del nodo HTTP Request anida el JSON (p. ej., en `data`), ajuste la expresión en consecuencia (`={{ $json.data.response }}`).

### 4. (Opcional) Limitación de tasa / moderación

Inserte un nodo Function o Code para:

- Limitar solicitudes (evitar abusos)
- Filtrar mensajes vacíos o solo de comandos
- Forzar una longitud máxima de mensaje

## Ejemplo mínimo de flujo de trabajo (exportación de n8n)

Sustituya los marcadores de posición antes de importar.

```json
{
  "name": "Copilot Telegram Bridge",
  "nodes": [
    {
      "id": "TelegramTrigger",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [200, 300],
      "parameters": {
        "updates": ["message"]
      },
      "credentials": {
        "telegramApi": "YOUR_TELEGRAM_CREDENTIAL"
      }
    },
    {
      "id": "CopilotRequest",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [520, 300],
      "parameters": {
        "method": "POST",
        "url": "https://ETENDO_INSTANCE_URL/etendo/sws/copilot/question",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpBearerAuth",
        "jsonParameters": true,
        "options": {},
        "bodyParametersJson": "{\n  \"question\": \"={{ $json.message.text }}\",\n  \"app_id\": \"1234567890\",\n  \"conversation_id\": \"={{ $json.message.chat.id }}\"\n}"
      },
      "credentials": {
        "httpBearerAuth": "ETENDO_BEARER_TOKEN"
      }
    },
    {
      "id": "SendMessage",
      "name": "Send Telegram Message",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [840, 300],
      "parameters": {
        "resource": "message",
        "operation": "sendMessage",
        "chatId": "={{ $json.message.chat.id }}",
        "text": "={{ $json.response }}"
      },
      "credentials": {
        "telegramApi": "YOUR_TELEGRAM_CREDENTIAL"
      }
    }
  ],
  "connections": {
    "Telegram Trigger": { "main": [ [ { "node": "HTTP Request", "type": "main", "index": 0 } ] ] },
    "HTTP Request": { "main": [ [ { "node": "Send Telegram Message", "type": "main", "index": 0 } ] ] }
  }
}
```

!!! info "Ajuste de nombres de campos"
    Si el servicio de Copilot cambia su esquema de respuesta, inspeccione la salida del nodo HTTP Request y actualice la expresión utilizada en el nodo de envío.

## Pruebas

1. Active el flujo de trabajo en n8n (`Active = true`).
2. Envíe un mensaje al Telegram bot (p. ej., `Hello` o una pregunta del dominio como: *Listar pedidos de venta abiertos*).
3. Observe el registro de ejecución en n8n. Confirme:
   - Estado 200 del HTTP Request
   - El JSON de respuesta contiene un campo `response`
4. Valide que el bot responde en el mismo chat.
5. Envíe varios mensajes para confirmar la continuidad de la conversación (reutilización de contexto vía `conversation_id`).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.