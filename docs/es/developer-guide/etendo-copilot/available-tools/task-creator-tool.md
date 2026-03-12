---
tags:
    - Etendo Copilot
    - Automatización de tareas
    - Procesamiento de CSV
    - Procesamiento de Excel
    - Procesamiento de ZIP
    - Herramienta
---

# Herramienta de creación de tareas

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de creación de tareas** automatiza la creación de tareas en función del contenido de un archivo. Admite los formatos **ZIP**, **CSV**, **XLS** y **XLSX**. Cada archivo o fila extraída de la entrada se convierte en una tarea independiente, lo que la hace ideal para la creación masiva de tareas basada en datos estructurados.

!!!info
    Para poder incluir esta funcionalidad, debe instalarse el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

!!! tip
    Para saber cuándo es el mejor momento para usar esta herramienta o cómo se ejecutan estas tareas, consulte la guía [Cómo crear tareas masivas para Copilot](../how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot.md).

Esta herramienta proporciona al agente:

  - Creación masiva de tareas: genera automáticamente múltiples tareas a partir de un archivo.
  - Compatibilidad multiformato: funciona con `.zip`, `.csv`, `.xls` y `.xlsx`.
  - Valores predeterminados inteligentes: detecta y crea automáticamente tipos de tarea o estados faltantes si no se proporcionan, y utiliza IDs predeterminados para grupos y agentes.
  - Ejecución en paralelo: crea tareas de forma concurrente para un mejor rendimiento.

Es especialmente útil para la colaboración en equipo, la incorporación a proyectos, los flujos de trabajo de entrada de datos y las configuraciones recurrentes de tareas estructuradas.

## Configuración

La herramienta no requiere variables de entorno específicas por parte del usuario. Sin embargo, depende de la configuración interna de Etendo para la obtención del token y del host, utilizando internamente los valores `ETENDO_TOKEN` y `ETENDO_HOST`. Estos valores se gestionan de forma segura y **nunca se exponen al modelo**.

### Formatos de archivo compatibles

  - **ZIP**: se crea una tarea por cada archivo extraído.
  - **CSV / Excel (XLS, XLSX)**: se crea una tarea por cada fila (excluyendo la cabecera), con los datos mapeados como cadenas clave-valor.
  - **Otros archivos**: se crea una única tarea utilizando la ruta completa del archivo.

## Funcionalidad

La herramienta sigue estos pasos principales:

  - **Procesamiento de entrada**

    Acepta los siguientes parámetros:

      - `question`: descripción o solicitud que se utilizará como base de la tarea. Se recomienda que sea una pregunta en singular. Por ejemplo: "Procesar el producto".
      - `file_path`: ruta al archivo de entrada (ZIP, CSV, XLS o XLSX).
      - `group_id`: ID de grupo opcional. Si no se establece, utiliza el ID de la conversación.
      - `groupby`: lista opcional de nombres de columna para agrupar filas al procesar archivos CSV/XLS/XLSX. Si se proporciona, las filas que compartan los mismos valores para estas columnas se agruparán y se enviarán como una única tarea. El elemento de la tarea será una cadena de un array JSON que contiene todas las filas del grupo. Esto es útil cuando varias filas pertenecen a la misma entidad (p. ej., todas las líneas de pedido para el mismo número de documento de pedido). Acepta una lista o una cadena separada por comas.
      - `task_type_id`: ID de tipo de tarea opcional. Si no se proporciona, utiliza el tipo de tarea predeterminado "Copilot" (ID: `A83E397389DB42559B2D7719A442168F`).
      - `status_id`: ID de estado opcional. Si no se proporciona, utiliza el estado predeterminado "Pendiente" (ID: `D0FCC72902F84486A890B70C1EB10C9C`).
      - `agent_id`: ID opcional del agente que procesará la tarea. Si no se proporciona, utiliza el ID del agente principal actual.
      - `preview`: booleano opcional. Si es true, devuelve los nombres de las columnas (o el contenido del archivo para ZIP) en lugar de crear tareas.

  - **Extracción de archivos**

    Dependiendo del tipo de archivo:

      - ZIP: descomprime y lista las rutas de los archivos.
      - CSV/XLS/XLSX: lee y convierte cada fila a una representación en cadena.

  - **Generación de tareas**

    Para cada elemento extraído (ruta de archivo o fila), genera una tarea con:

      - La `question` base + ":" + el contenido del elemento.
      - El `task_type`, `status`, `group_id` asociados y el `agent_id` asignado.

  - **Uso seguro del token**

    La herramienta recupera el token de acceso de Etendo usando `ETENDO_TOKEN`, garantizando que los valores sensibles se resuelven de forma segura **antes de la ejecución** y **no son visibles para el modelo**.

  - **Ejecución en paralelo**

    Las tareas se crean en paralelo utilizando hasta 10 hilos concurrentes para optimizar el rendimiento.

  - **Respuesta final**

    Devuelve:

    ```json
    {
        "message": "Bulk Task creation process completed, the tasks from this batch group has the group id: <group_id>"
    }
    ```

## Ejemplo de uso

### Ejemplo 1: Uso básico

Usted tiene un archivo `.csv` con una lista de comentarios de clientes. Cada fila debe convertirse en una tarea independiente dentro del mismo grupo. Usted introduciría:

  - `question`: Revisar comentarios
  - `file_path`: /path/to/feedback.csv
  - `group_id`: 123456789
  - `task_type_id`: (opcional)
  - `status_id`: (opcional)
  - `agent_id`: (opcional)

La Herramienta de creación de tareas procesará cada fila y generará una tarea con la pregunta base + los datos de la fila. Si un parámetro no se establece, la herramienta utiliza su valor predeterminado.

### Ejemplo 2: Agrupación por valores de columna

Usted tiene un archivo `.xlsx` con líneas de pedido donde varias filas pertenecen al mismo documento de pedido. En lugar de crear una tarea por línea, usted quiere crear una tarea por pedido que contenga todas sus líneas.

**Archivo de Excel de ejemplo:**

| DocumentNo | Producto | Cantidad | Precio |
|------------|---------|----------|-------|
| ORD-001    | Producto A | 10 | 100 |
| ORD-001    | Producto B | 5 | 50 |
| ORD-002    | Producto C | 20 | 200 |
| ORD-002    | Producto D | 15 | 150 |

**Parámetros de entrada:**

  - `question`: Procesar pedido
  - `file_path`: /path/to/orders.xlsx
  - `group_id`: 123456789
  - `groupby`: ["DocumentNo"]
  - `agent_id`: (opcional)

**Resultado:**

La herramienta creará **2 tareas** (una por pedido):

1. **Tarea 1** con los datos del elemento como un array JSON que contiene ambas líneas de ORD-001
2. **Tarea 2** con los datos del elemento como un array JSON que contiene ambas líneas de ORD-002

Esto le ayuda a automatizar la generación de tareas a gran escala en un solo paso, ahorrando tiempo y evitando la entrada manual, al tiempo que mantiene la agrupación lógica de los datos relacionados.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.