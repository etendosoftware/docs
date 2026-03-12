---
title: Cómo integrar Copilot con Jira mediante MCP
status: beta
tags:
  - Cómo hacer
  - Etendo Copilot
  - Jira
  - MCP
  - Integración
  - Automatización
---

# Cómo integrar Copilot con Jira mediante MCP

## Visión general

!!! note "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

La integración de **Etendo Copilot** con **Jira** permite a los agentes crear, actualizar y consultar incidencias de Jira directamente desde la interfaz del ERP. Esto evita cambiar entre aplicaciones y habilita un flujo de trabajo conversacional unificado.

Esta guía explica cómo configurar un servidor de **Model Context Protocol (MCP)** que actúa como puente entre Copilot y la API REST de Jira utilizando la implementación MCP de Atlassian.

### Capacidades clave

- Crear incidencias individuales o en lote.
- Actualizar campos de incidencias (transiciones de estado, comentarios, registros de trabajo, enlaces, versiones, épicas).
- Consultar incidencias, proyectos, tableros, sprints y registros de cambios.
- Descargar adjuntos.
- Mantener un acceso contextual y seguro mediante Etendo Copilot.

### Cuándo usar esta integración
Úsela cuando los equipos de desarrollo, soporte u operaciones gestionen su backlog en Jira y deseen acceso conversacional desde Etendo para acelerar la clasificación de tareas, el seguimiento o la elaboración de informes.

## Requisitos previos

- Etendo y **Etendo Copilot** instalados.
- Usuario de Jira válido con API Token.
- Acceso de red desde el servidor de Etendo a `*.atlassian.net`.
- API Token almacenado en Etendo como un registro de **API Token** (ver más abajo).

!!! info
    Almacene el API token de Jira usando la guía: [Cómo configurar API Tokens](./how-to-configure-api-tokens.md). Use el alias `JIRA_TOKEN` (recomendado).

## Paso 1. Crear (o reutilizar) el API Token de Jira

1. Abra Atlassian Account Settings > Security > API tokens.
2. Cree un nuevo token (etiquétele para el uso de Etendo Copilot).
3. Copie el token.
4. En Etendo, abra :material-menu: `Aplicación` > `Servicios` > `Copilot API Tokens` y cree un registro:

   - Organización: seleccione el ámbito adecuado.
   - Alias: `JIRA_TOKEN`.
   - Token: pegue el valor copiado.
   - (Opcional) Usuario / Rol: restrinja el ámbito si es necesario.

## Paso 2. Registrar el servidor MCP de Jira

:material-menu: `Aplicación` > `Servicios` > `Copilot` > `MCP Servers Configuration`

Cree un nuevo registro y pegue el siguiente JSON (ajuste `JIRA_URL`, `JIRA_USERNAME` si es necesario). El marcador de posición del token se sustituirá automáticamente en tiempo de ejecución usando el sistema de prioridad de API Token.

```json
{
  "transport": "stdio",
  "command": "uvx",
  "args": [
    "--from", "etendo-mcp-atlassian==0.1.10",
    "etendo-mcp-atlassian",
    "--enabled-tools=jira_search,jira_get_issue,jira_get_all_projects,jira_get_project_issues,jira_get_worklog,jira_get_transitions,jira_search_fields,jira_get_agile_boards,jira_get_board_issues,jira_get_sprints_from_board,jira_get_sprint_issues,jira_get_link_types,jira_batch_get_changelogs,jira_get_user_profile,jira_download_attachments,jira_get_project_versions,jira_create_issue,jira_update_issue,jira_batch_create_issues,jira_add_comment,jira_transition_issue,jira_add_worklog,jira_link_to_epic,jira_create_issue_link"
  ],
  "env": {
    "JIRA_URL": "https://yourcompany.atlassian.net",
    "JIRA_USERNAME": "user@example.com",
    "JIRA_API_TOKEN": "@JIRA_TOKEN@",
    "LOG_LEVEL": "INFO"
  }
}
```

Campos explicados:

- `transport`: comunicación MCP basada en STDIO.
- `command` / `args`: usa `uvx` para ejecutar el paquete MCP de Atlassian en la versión especificada.
- `--enabled-tools`: lista separada por comas de capacidades de Jira expuestas a Copilot.
- Variables de `env`:
  - `JIRA_URL`: URL base de Jira Cloud (o Server).
  - `JIRA_USERNAME`: usuario de Jira (correo electrónico para Cloud).
  - `JIRA_API_TOKEN`: marcador de posición resuelto al token almacenado.
  - `LOG_LEVEL`: ajuste (`DEBUG`, `INFO`, etc.).

!!! warning
    No pegue el API token en bruto directamente. Use siempre el marcador de posición (p. ej., `@JIRA_TOKEN@`). Esto garantiza el ámbito adecuado, la gestión de prioridades y la ocultación de secretos.

## Paso 3. Vincular el MCP a un agente

:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Agent`

1. Abra (o cree) el agente objetivo.
2. Vaya a la pestaña **MCP Servers**.
3. Añada una nueva línea seleccionando el servidor MCP de Jira.
4. Guarde y haga clic en **Sync Agent**.

## Paso 4. Probar la integración

Ejemplos de prompts:

```
Create a Jira issue in project ERP with summary "Add tax validation" and assign it to me.
Search Jira issues with status = In Progress assigned to current user ordered by updated date.
Transition issue ERP-123 to In Progress and add a comment "Work started".
Add a worklog of 2h to issue ERP-456 for today's date.
Link issue ERP-789 to epic ERP-22.
```

!!! success
    Si está configurado correctamente, el agente responde con datos estructurados de la incidencia (clave, resumen, estado) o con la confirmación de las acciones realizadas.

## Herramientas de Jira disponibles (habilitadas en el ejemplo)

- Búsqueda / consulta: `jira_search`, `jira_search_fields`
- Incidencias: `jira_get_issue`, `jira_create_issue`, `jira_update_issue`, `jira_batch_create_issues`
- Comentarios y enlaces: `jira_add_comment`, `jira_create_issue_link`, `jira_link_to_epic`
- Flujo de trabajo: `jira_get_transitions`, `jira_transition_issue`
- Proyectos y tableros: `jira_get_all_projects`, `jira_get_project_issues`, `jira_get_agile_boards`, `jira_get_board_issues`
- Sprints: `jira_get_sprints_from_board`, `jira_get_sprint_issues`
- Registros de cambios: `jira_batch_get_changelogs`
- Registros de trabajo: `jira_get_worklog`, `jira_add_worklog`
- Versiones: `jira_get_project_versions`
- Adjuntos: `jira_download_attachments`
- Usuario: `jira_get_user_profile`

Deshabilite las herramientas no utilizadas eliminándolas de la lista `--enabled-tools` para reducir la superficie de exposición y el ruido.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.