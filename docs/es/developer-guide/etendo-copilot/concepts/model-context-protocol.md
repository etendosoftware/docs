---
title: Guía del desarrollador - Model Context Protocol (MCP)
status: beta
tags:
    - Copilot
    - MCP
    - Model Context Protocol
    - Arquitectura
    - Visión general
    - IA
---

## Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

El **Model Context Protocol (MCP)** es un protocolo abierto desarrollado por Anthropic que estandariza cómo las aplicaciones de IA proporcionan contexto a los modelos de lenguaje de gran tamaño (LLM). MCP actúa como un puerto USB-C para aplicaciones de IA, permitiendo que los modelos se conecten de forma uniforme con fuentes de datos externas, herramientas y servicios.

Esta guía ofrece una introducción completa a los conceptos y la arquitectura de MCP, así como a su implementación dentro del ecosistema de Etendo Copilot, ayudando a los desarrolladores a comprender cómo aprovechar este protocolo para crear integraciones de IA escalables y seguras.

## ¿Qué es MCP?

MCP es un protocolo que resuelve el problema de fragmentación en el ecosistema de IA, donde cada aplicación requería integraciones personalizadas para conectarse con diferentes fuentes de datos y herramientas. Con MCP, tanto los desarrolladores como las organizaciones pueden crear conectores reutilizables que funcionan en múltiples aplicaciones y plataformas. Entre sus características principales se incluyen:

- **Protocolo abierto**: disponible para toda la comunidad de desarrolladores
- **Estandarización**: interfaz uniforme para la integración de contexto y herramientas
- **Escalabilidad**: arquitectura modular que permite una extensión sencilla
- **Seguridad**: controles de permisos y autenticación integrados
- **Flexibilidad**: compatibilidad con múltiples tipos de transporte y formatos de datos

## Arquitectura de MCP

MCP utiliza una arquitectura cliente-servidor que facilita la comunicación entre aplicaciones de IA y fuentes de datos externas.

### Componentes principales

**Hosts**  
Los hosts son las aplicaciones principales a través de las cuales los usuarios interactúan con el protocolo:
- **Función**: ejecutar modelos de IA y gestionar la interfaz de usuario.

- **Responsabilidades**: 
    - Iniciar conexiones con servidores MCP.
    - Controlar permisos y restricciones de seguridad.
    - Gestionar el flujo de la conversación.
    - Gestionar el consentimiento del usuario para el intercambio de datos.

**Clients**  
Los clientes actúan como intermediarios entre los hosts y los servidores MCP:

- **Función**: facilitar la comunicación entre hosts y servidores.

- **Responsabilidades**:
    - Enviar solicitudes a los servidores.
    - Negociar capacidades con los servidores.
    - Gestionar solicitudes de ejecución de herramientas.
    - Procesar y mostrar respuestas a los usuarios.

**Servers**  
Los servidores MCP proporcionan acceso a herramientas, recursos y datos específicos:

- **Función**: gestionar solicitudes del cliente y proporcionar las respuestas adecuadas.

- **Responsabilidades**:
    - Registrar funcionalidades disponibles (recursos, prompts, herramientas).
    - Ejecutar llamadas a herramientas desde el cliente.
    - Proporcionar información contextual.
    - Mantener el estado entre interacciones cuando sea necesario.

### Flujo de información

1. **Inicio de conexión**: el host establece una conexión con un servidor MCP
2. **Negociación de capacidades**: el cliente y el servidor intercambian información sobre las funcionalidades compatibles
3. **Solicitud del usuario**: el usuario interactúa con el host proporcionando un prompt o comando
4. **Uso de recursos/herramientas**: el cliente solicita contexto adicional o ejecuta herramientas del servidor
5. **Ejecución del servidor**: el servidor ejecuta las operaciones solicitadas y devuelve resultados
6. **Generación de respuesta**: el cliente integra las respuestas del servidor en la interacción del modelo
7. **Presentación del resultado**: el host presenta la salida final al usuario

## Funcionalidades técnicas

### Protocolo base
- **Formato de mensaje**: JSON-RPC 2.0 para una estructura consistente
- **Conexiones con estado**: las sesiones MCP mantienen el estado a través de múltiples solicitudes
- **Negociación de capacidades**: intercambio de información sobre funcionalidades compatibles durante la configuración

### Funcionalidades del servidor

**Recursos** representan datos contextuales y fuentes de información disponibles para los modelos:

- Archivos locales (`file://log.txt`)
- Esquemas de base de datos (`database://schema`)
- APIs externas
- Bases de conocimiento

**Herramientas** permiten a los modelos realizar acciones específicas:

- Búsquedas web
- Cálculos matemáticos
- Acceso a base de datos
- Operaciones del sistema de archivos

**Prompts** son plantillas predefinidas que agilizan los flujos de trabajo:

```markdown
Generate a product slogan based on the following {{product}} with the following {{keywords}}
```

### Funcionalidades del cliente

**Sampling** permite a los servidores iniciar comportamientos autónomos e interacciones recursivas con LLM, permitiendo:

- Comportamientos de agente iniciados por el servidor
- Interacciones recursivas con LLM
- Solicitudes de completados adicionales del modelo

## Tipos de entrada MCP compatibles con Etendo Copilot

Para adaptarse a configuraciones procedentes de diferentes editores/clientes (que a menudo utilizan estructuras y nombres de campo distintos), **Etendo Copilot** incluye un normalizador de configuración llamado **`MCPConfigNormalizer`**. Esta clase acepta *cualquier* `JSON` de servidor MCP, lo convierte en un **esquema unificado** y aplica valores por defecto razonables y validaciones ligeras para que las integraciones se mantengan consistentes y fiables.

**Formatos de entrada aceptados**

Se reconocen múltiples formas y anidamientos:

- `mcpServers: { <name>: { ... } }`
- `mcp.servers` como un **array** o un **map**
- `servers` en el nivel raíz (**array** o **map**)
- `context_servers` (formato **Zed**)
- Envoltorios como `{ mcp: { ... } }`, `{ server: { ... } }`

**Alias de propiedades aceptados**

Se reconocen alias comunes y se mapean al esquema estándar:

- **URL**: `url` | `uri` | `endpoint` | `baseUrl` | `serverUrl` | `httpUrl`
- **Comando**: `command` | `cmd` | `bin` | `executable` | `path`
- **Args**: `args` | `argv` | `arguments` | `cmdArgs`
- **Cabecera**: `headers` | `httpHeaders`
- **Otros**: `cwd` | `workingDir` | `workdir`, `env` | `environment` | `envVars`

**Detección y normalización del transporte**

Todas las fuentes se normalizan al conjunto compatible con el cliente Python:

- `stdio`, `sse`, `websocket`, `streamable_http`

Alias reconocidos:

- `http`/`https` → **`streamable_http`** (evita “Unsupported transport: http”)
- `ws` → **`websocket`**

Si se omite `transport`, se **infiere** a partir de los campos disponibles:

- Presencia de `command` ⇒ `stdio`
- `ws://` o `wss://` ⇒ `websocket`
- URL que contenga `/sse` ⇒ `sse`
- `host`/`port` ⇒ `streamable_http`
- Último recurso ⇒ `stdio`

**Esquema de salida unificado**

El resultado siempre incluye un **`name`** (del registro de la base de datos). Si el origen utilizó una subclave (p. ej., `context7`), el nombre queda **con espacio de nombres** como `DBName::context7`.

- **STDIO**
  ```json
  {
    "name": "DBName[::subkey]",
    "transport": "stdio",
    "command": "…",
    "args": ["…"],
    "env": { "…": "…" },
    "cwd": "…"
  }
  ```

- **SSE / WebSocket / Streamable HTTP**
  ```json
  {
    "name": "DBName[::subkey]",
    "transport": "sse | websocket | streamable_http",
    "url": "https://…",
    "headers": { "Authorization": "…" },
    "timeoutMs": 120000
  }
  ```

**Ejemplo de normalización**

Entrada (VS Code / remoto):
```json
{
  "mcp": {
    "servers": {
      "context7": {
        "type": "http",
        "url": "https://mcp.context7.com/mcp"
      }
    }
  }
}
```

Salida normalizada:
```json
{
  "name": "DBName::context7",
  "transport": "streamable_http",
  "url": "https://mcp.context7.com/mcp"
}
```

**Garantías y comportamiento**

- `getMCPConfigurations()` devuelve configuraciones **uniformes y fiables**, independientemente del formato original.
- Los nombres se **conservan**, se aplican **valores por defecto** razonables y las entradas no válidas **no rompen** el resto.
- Se validan parámetros básicos y los errores de “transporte no compatible” se mitigan mediante alias e inferencia.

## Seguridad y autorización

MCP incluye múltiples mecanismos de seguridad para garantizar interacciones seguras:

**Control de permisos de herramientas**

- Los clientes pueden especificar qué herramientas puede utilizar un modelo durante una sesión.
- Permisos configurables dinámicamente en función de las políticas de la organización.
- Reducción del riesgo de operaciones no intencionadas o inseguras.

**Autenticación**

- Los servidores pueden requerir autenticación antes de conceder acceso.
- Compatibilidad con claves API, tokens OAuth y otros esquemas de autenticación.
- Garantiza que solo clientes y usuarios de confianza puedan invocar capacidades del lado del servidor.

**Validación de parámetros**

- Validación obligatoria para todas las invocaciones de herramientas.
- Cada herramienta define los tipos, formatos y restricciones esperados para sus parámetros.
- Prevención de entradas malformadas o maliciosas.

**Limitación de tasa**

- Implementación de límites de tasa para llamadas a herramientas y acceso a recursos.
- Límites aplicables por usuario, por sesión o de forma global.
- Protección frente a ataques de denegación de servicio.

## Casos de uso

### En el contexto de Etendo Copilot

MCP en Etendo Copilot permite a los agentes acceder de forma estandarizada a:

- **Base de datos**: esquemas y consultas de la base de datos de Etendo
- **APIs**: servicios web de Etendo y sistemas externos
- **Archivos**: documentos, logs y configuraciones del sistema
- **Herramientas personalizadas**: funcionalidades específicas de Etendo

En el contexto de Etendo Copilot, MCP permite una integración más fluida entre agentes de IA y sistemas empresariales, proporcionando acceso estandarizado a los datos y funcionalidades de Etendo, a la vez que mantiene la seguridad y el control necesarios para entornos empresariales.

!!!info
    Para más información sobre MCP, visite:

    - [Documentación oficial de MCP](https://modelcontextprotocol.io/){target="_blank"}
    - [Repositorio de la especificación de MCP](https://github.com/modelcontextprotocol/specification){target="_blank"}
    - [Guía del servidor MCP](../concepts/model-context-protocol.md){target="_blank"}

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.