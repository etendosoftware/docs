---
title: Guía del desarrollador - Configurar tokens de API para Etendo Copilot
status: beta
tags:
    - Cómo hacer
    - Tokens de API
    - Autenticación
    - Integración de Copilot
    - Seguridad
---

# Cómo configurar tokens de API para Etendo Copilot

## Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

Esta guía explica cómo configurar y utilizar **tokens de API** en **Etendo Copilot** para una autenticación segura con servicios externos. Los tokens de API permiten que los agentes se autentiquen con APIs de terceros manteniendo la seguridad mediante una gestión adecuada de tokens y mecanismos de sustitución.

### ¿Qué son los tokens de API en Etendo Copilot?

Los tokens de API en Etendo Copilot son credenciales seguras que permiten que los agentes se autentiquen con servicios externos y APIs. Estos tokens son:

- **Con reconocimiento de contexto**: se pueden asignar distintos tokens en función del usuario, el rol o la configuración global
- **Priorizados**: el sistema selecciona automáticamente el token más adecuado según el contexto
- **Seguros**: los tokens se almacenan de forma segura y solo se exponen durante el procesamiento del prompt
- **Flexibles**: admite múltiples alias para distintos servicios

### Sistema de prioridad de tokens de API

El sistema implementa un mecanismo sofisticado de prioridad para la selección de tokens:

1. **Específico de usuario + rol**: tokens asignados tanto a un usuario como a un rol específicos (máxima prioridad)
2. **Específico de usuario**: tokens asignados solo a un usuario específico
3. **Específico de rol**: tokens asignados solo a un rol específico
4. **Global**: tokens sin asignación de usuario ni de rol (mínima prioridad)

Esto garantiza que siempre se utilice el token más apropiado según el contexto.

## Configuración

### Crear un nuevo token de API

:material-menu: `Aplicación` > `Servicios` > `Copilot API Tokens`

Etendo debe abrirse utilizando el rol al que se va a añadir la clave. El acceso suele estar restringido a la ventana de configuración para administradores; sin embargo, esto puede variar en función del nivel de acceso y la configuración asignada a cada rol.

![Configuración de tokens de API](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-configure-api-tokens/api-token-configuration.png)

Cree un nuevo registro con estos campos:

- **Organización (Obligatorio)**: la organización que tendrá acceso a este token.
- **Alias (Obligatorio)**: nombre utilizado para referenciar el token en prompts/configuraciones. Nombre único para el token (p. ej., `OPENAI_API`, `GITHUB_TOKEN`).
- **Token (Obligatorio)**: la clave de API o el valor del token. (p. ej., `sk-abc123...`)
- **Usuario/Contacto (Opcional)**: usuario con acceso al token. Asigne a un usuario específico (déjelo vacío para un alcance más amplio).
- **Rol (Opcional)**: rol autorizado a utilizar el token. Asigne a un rol específico (déjelo vacío para un alcance más amplio).

### Uso de tokens en prompts

**Formato del marcador de posición del token**

Los tokens de API se referencian en los prompts utilizando el siguiente formato:

```
@TOKEN_ALIAS@
```

El alias se convierte automáticamente a mayúsculas para la coincidencia del marcador de posición.

#### Ejemplo de uso

**En prompts de agente**
```
Use the OpenAI API with key @OPENAI_API@ to generate a response.
Access GitHub repository using token @GITHUB_TOKEN@.
Connect to Salesforce with @SALESFORCE_API@ credentials.
```

**En configuraciones de herramientas**
```json
{
  "api_key": "@OPENAI_API@",
  "base_url": "https://api.openai.com/v1",
  "headers": {
    "Authorization": "Bearer @OPENAI_API@"
  }
}
```

**En autenticación del servidor MCP**

Los tokens de API pueden utilizarse en configuraciones del servidor MCP:

```json
{
  "command": "npx",
  "args": ["custom-mcp-server"],
  "env": {
    "API_KEY": "@CUSTOM_API@",
    "AUTH_TOKEN": "@SERVICE_TOKEN@"
  }
}
```

### Proceso de sustitución de tokens

Cuando se procesan los prompts, el sistema:

1. **Identifica** todos los marcadores de posición de tokens con el formato `@ALIAS@`
2. **Evalúa** el contexto del usuario y del rol actuales
3. **Selecciona** el token de mayor prioridad para cada alias
4. **Sustituye** los marcadores de posición por los valores reales del token
5. **Procesa** el prompt con credenciales autenticadas

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.