---
tags:
    - Copilot
    - Gestión de tareas
    - Flujo de trabajo
    - Utilidades
---

# Herramienta de gestión de tareas

:octicons-package-16: Paquete Java: `com.etendoerp.copilot`

## Visión general

La Herramienta de gestión de tareas es una utilidad para gestionar tareas de forma dinámica dentro del estado de una conversación. Proporciona operaciones flexibles de cola de tareas, como añadir, recuperar, comprobar el estado y marcar tareas como completadas. Esta herramienta es especialmente útil en flujos de trabajo orquestados donde se requiere la gestión de tareas en varios pasos.

!!!info
    Esta herramienta forma parte del Framework de Copilot y normalmente se utiliza dentro de agentes multiagente o basados en flujos de trabajo.

## Funcionalidad

Esta herramienta permite la **gestión centralizada de la cola de tareas** utilizando diferentes modos de operación:

### Modos compatibles:
- `get_next`: Recupera y establece la siguiente tarea que se va a procesar.
- `add_tasks`: Añade una o más tareas nuevas a la cola de procesamiento.
- `status`: Recupera el estado actual de la cola de tareas, incluidas las tareas actuales, pendientes y completadas.
- `mark_done`: Marca la tarea actual como completada y la mueve a la lista de finalizadas.

La herramienta funciona modificando y almacenando datos relacionados con las tareas en el estado compartido del agente, lo que la hace ideal para orquestar flujos de trabajo paso a paso en sistemas multiagente.

### Parámetros

| Nombre        | Tipo   | Descripción                                                                 |
|-------------|--------|-----------------------------------------------------------------------------|
| `mode`      | string | Modo de operación: `get_next`, `add_tasks`, `status` o `mark_done`.         |
| `state`     | dict   | Estado inyectado que contiene colas de tareas y estados.                    |
| `tool_call_id` | string | ID único de llamada a la herramienta utilizado para el seguimiento de mensajes. |
| `new_tasks` | list   | Opcional. Lista de tareas nuevas que se van a añadir (requerido para el modo `add_tasks`). |

## Resumen de comportamiento

- **get_next**: Extrae la siguiente tarea de la cola y la establece como `current_task`.
- **add_tasks**: Añade una lista de tareas a la cola de tareas.
- **status**: Devuelve un recuento y una instantánea actual de todas las colas de tareas.
- **mark_done**: Mueve la tarea actual a la lista de tareas completadas.

## Caso de uso de ejemplo

Un ejemplo típico podría ser un proceso de validación de facturas en varios pasos. Cada factura es una tarea independiente, y esta herramienta ayuda a:

- Cargar todas las tareas de facturas de una sola vez.
- Recuperar cada tarea de forma secuencial.
- Realizar el seguimiento y marcarlas como completadas a medida que se procesan.

## Formato de respuesta de la herramienta

La herramienta devuelve un objeto **Comando** que incluye:

- Estado compartido actualizado (listas de tareas).
- Un `ToolMessage` que describe lo que se ha hecho (utilizado para el registro o el enrutamiento posterior).

!!!note
    Esta herramienta debe utilizarse con LangGraph u otros motores de orquestación de varios pasos de LangChain.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.