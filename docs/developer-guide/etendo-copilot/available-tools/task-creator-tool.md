---
tags:
    - Etendo Copilot
    - Task Automation
    - CSV Processing
    - Excel Processing
    - ZIP Processing
    - Tool
---

# Task Creator Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Task Creator Tool** automates the creation of tasks based on the content of a file. It supports **ZIP**, **CSV**, **XLS**, and **XLSX** formats. Each file or row extracted from the input becomes a separate task, making it ideal for bulk task creation based on structured data.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

!!! tip
    To know when is the best time to use this tool or how these tasks are executed, check the [How to create bulk tasks for Copilot](../how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot.md) guide.

This tool provides the agent with:

  - Bulk Task Creation: Automatically generate multiple tasks from one file.
  - Multi-format Support: Works with `.zip`, `.csv`, `.xls`, and `.xlsx`.
  - Smart Defaults: Automatically detects and creates missing task types or statuses if not provided, and uses default IDs for groups and agents.
  - Parallel Execution: Creates tasks concurrently for better performance.

It is especially useful for team collaboration, project onboarding, data entry workflows, and recurring structured task setups.

## Setup

The tool doesn’t require specific environment variables from the user. However, it depends on the internal Etendo configuration for token and host retrieval, using the `ETENDO_TOKEN` and `ETENDO_HOST` values internally. These values are handled securely and **are never exposed to the model**.

### Supported File Formats

  - **ZIP**: A task is created for each extracted file.
  - **CSV / Excel (XLS, XLSX)**: A task is created for each row (excluding the header), with data mapped as key-value strings.
  - **Other Files**: A single task is created using the full file path.

## Functionality

The tool follows these main steps:

  - **Input Processing**

    Accepts the following parameters:

      - `question`: Description or request that will be used as the task base. It is recommended that this be a singularized question. For example: "Process the product".
      - `file_path`: Path to the input file (ZIP, CSV, XLS, or XLSX).
      - `group_id`: Optional group ID. If not set, it uses the conversation ID.
      - `groupby`: Optional list of column names to group rows by when processing CSV/XLS/XLSX files. If provided, rows that share the same values for these columns will be grouped together and sent as a single task. The task item will be a JSON array string containing all rows in the group. This is useful when multiple rows belong to the same entity (e.g., all order lines for the same order document number). Accepts a list or comma-separated string.
      - `task_type_id`: Optional task type ID. If not provided, it uses the default "Copilot" task type (ID: `A83E397389DB42559B2D7719A442168F`).
      - `status_id`: Optional status ID. If not provided, it uses the default "Pending" status (ID: `D0FCC72902F84486A890B70C1EB10C9C`).
      - `agent_id`: Optional ID of the agent to process the task. If not provided, it uses the current main agent's ID.
      - `preview`: Optional boolean. If true, returns the column names (or file contents for ZIP) instead of creating tasks.

  - **File Extraction**

    Depending on the file type:

      - ZIP: Unzips and lists file paths.
      - CSV/XLS/XLSX: Reads and converts each row to a string representation.

  - **Task Generation**

    For each extracted item (file path or row), it generates a task with:

      - The base `question` + ":" + item content.
      - The associated `task_type`, `status`, `group_id`, and the assigned `agent_id`.

  - **Secure Token Use**

    The tool retrieves the Etendo access token using `ETENDO_TOKEN`, ensuring sensitive values are resolved securely **before execution** and **are not visible to the model**.

  - **Parallel Execution**

    Tasks are created in parallel using up to 10 concurrent threads to optimize performance.

  - **Final Response**

    Returns:

    ```json
    {
        "message": "Bulk Task creation process completed, the tasks from this batch group has the group id: <group_id>"
    }
    ```

## Usage Example

### Example 1: Basic Usage

You have a `.csv` file with a list of customer feedback. Each row should become a separate task under the same group. You would input:

  - `question`: Review feedback
  - `file_path`: /path/to/feedback.csv
  - `group_id`: 123456789
  - `task_type_id`: (optional)
  - `status_id`: (optional)
  - `agent_id`: (optional)

The Task Creator Tool will process each row and generate a task with the base question + the row's data. If a parameter is not set, the tool uses its default value.

### Example 2: Grouping by Column Values

You have a `.xlsx` file with order lines where multiple rows belong to the same order document. Instead of creating one task per line, you want to create one task per order containing all its lines.

**Sample Excel file:**

| DocumentNo | Product | Quantity | Price |
|------------|---------|----------|-------|
| ORD-001    | Product A | 10 | 100 |
| ORD-001    | Product B | 5 | 50 |
| ORD-002    | Product C | 20 | 200 |
| ORD-002    | Product D | 15 | 150 |

**Input parameters:**

  - `question`: Process order
  - `file_path`: /path/to/orders.xlsx
  - `group_id`: 123456789
  - `groupby`: ["DocumentNo"]
  - `agent_id`: (optional)

**Result:**

The tool will create **2 tasks** (one per order):

1. **Task 1** with item data as a JSON array containing both lines for ORD-001
2. **Task 2** with item data as a JSON array containing both lines for ORD-002

This helps you automate large-scale task generation in just one step, saving time and avoiding manual entry, while maintaining the logical grouping of related data.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
