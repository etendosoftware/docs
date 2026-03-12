---
tags:
    - Copilot
    - Memoria
    - Herramienta
    - Base de datos vectorial
    - CRUD
    - Chroma
---

# Herramienta de Memoria

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de Memoria** es una herramienta integral para gestionar memorias de usuario en una base de datos vectorial utilizando Chroma como almacenamiento de backend. Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para memorias específicas por usuario con capacidades de búsqueda por similitud vectorial, lo que permite a los asistentes almacenar y recuperar información contextual a lo largo de las conversaciones.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta permite a los asistentes mantener memoria persistente a lo largo de las conversaciones almacenando información importante en una base de datos vectorial. Admite capacidades de búsqueda semántica, lo que permite una recuperación inteligente de memorias relevantes en función del contexto y la similitud. La herramienta está acotada por usuario, garantizando el aislamiento de datos y la privacidad.

Las funcionalidades clave incluyen:

- **Persistencia de memoria**: almacenar información importante que persiste entre sesiones de conversación
- **Búsqueda semántica**: encontrar memorias relevantes mediante búsqueda por similitud vectorial
- **Aislamiento de usuario**: las memorias de cada usuario se almacenan por separado y de forma segura
- **Operaciones CRUD**: conjunto completo de operaciones para la gestión de memorias
- **Generación automática de ID**: se asignan automáticamente identificadores únicos a cada memoria

## Operaciones compatibles

### Modo Añadir
Crea una nueva memoria con generación automática de ID.

- **Parámetros obligatorios**: `mode` (establecido en "add"), `memory` (contenido a almacenar)
- **Devolución**: mensaje de éxito con el ID de memoria generado

### Modo Selector
Encuentra memorias mediante búsqueda por similitud vectorial.

- **Parámetros obligatorios**: `mode` (establecido en "search"), `query` (cadena de búsqueda)
- **Parámetros opcionales**: `k` (número máximo de resultados, por defecto: 3)
- **Devolución**: lista de memorias coincidentes con sus IDs

### Modo Actualizar
Modifica el contenido de una memoria existente preservando los metadatos.

- **Parámetros obligatorios**: `mode` (establecido en "update"), `memory_id` (memoria objetivo), `memory` (nuevo contenido)
- **Devolución**: mensaje de éxito confirmando la actualización

### Modo Eliminar
Elimina una memoria específica de la base de datos.

- **Parámetros obligatorios**: `mode` (establecido en "delete"), `memory_id` (memoria objetivo)
- **Devolución**: mensaje de éxito confirmando la eliminación

## Ejemplos de uso

### Añadir una memoria

Para almacenar una nueva memoria:

```json
{
    "mode": "add",
    "memory": "User prefers dark theme and 24-hour time format"
}
```

**Salida esperada:**
```json
{
    "result": "Memory added for user_id user123: User prefers dark theme and 24-hour time format (memory_id: 550e8400-e29b-41d4-a716-446655440000)"
}
```

### Buscar memorias

Para encontrar memorias relevantes:

```json
{
    "mode": "search",
    "query": "user preferences",
    "k": 5
}
```

**Salida esperada:**
```json
{
    "result": "- User prefers dark theme and 24-hour time format (memory_id: 550e8400-e29b-41d4-a716-446655440000)\n- User likes concise responses (memory_id: 550e8400-e29b-41d4-a716-446655440001)"
}
```

### Actualizar una memoria

Para modificar el contenido de una memoria existente:

```json
{
    "mode": "update",
    "memory_id": "550e8400-e29b-41d4-a716-446655440000",
    "memory": "User prefers dark theme, 24-hour time format, and compact layout"
}
```

**Salida esperada:**
```json
{
    "result": "Memory updated for user_id user123: User prefers dark theme, 24-hour time format, and compact layout (memory_id: 550e8400-e29b-41d4-a716-446655440000)"
}
```

### Eliminar una memoria

Para eliminar una memoria específica:

```json
{
    "mode": "delete",
    "memory_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Salida esperada:**
```json
{
    "result": "Memory with memory_id 550e8400-e29b-41d4-a716-446655440000 deleted for user_id user123"
}
```

## Implementación técnica

### Base de datos vectorial
La herramienta utiliza Chroma como backend de base de datos vectorial, configurado con:

- Almacenamiento persistente en directorios específicos por usuario
- Funciones de embeddings para búsqueda semántica
- Vectorización automática de documentos

### Aislamiento de usuario
Las memorias se aíslan por usuario mediante:

- Colecciones de almacenamiento vectorial específicas por usuario (`{assistant_id}_memories`)
- Filtrado de metadatos basado en `user_id` desde el contexto del hilo
- Control de acceso seguro que garantiza que los usuarios solo puedan acceder a sus propias memorias

### Variables de contexto
La herramienta requiere las siguientes variables de contexto:

- `assistant_id`: identificador único para la instancia del asistente
- `ad_user_id`: identificador de usuario de Active Directory

## Gestión de errores

La herramienta incluye una gestión de errores integral para:

- Modos de operación no válidos
- Falta de parámetros obligatorios
- Validación de variables de contexto
- Fallos en operaciones de base de datos
- Verificación de permisos de usuario

Respuestas de error comunes:

- `"Invalid mode 'xyz'. Use 'add', 'search', 'update', or 'delete'."`
- `"The 'memory' parameter is required for 'add' mode."`
- `"No memory found with memory_id xyz for user_id user123"`
- `"assistant_id or ad_user_id not found in Payload."`