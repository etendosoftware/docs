---
tags:
  - Database Management  
  - Etendo Module
  - com.etendoerp.db.extended (BETA MODULE)
---
# com.etendoerp.db.extended — BETA MODULE


> 🚧 **IMPORTANT:** This is a **BETA module**. It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**, especially in production environments.

---

## Overview

The `com.etendoerp.db.extended` module expands the database functionalities of the Etendo ERP system.  
This **BETA** module is designed to provide advanced and robust tools to manage complex database structures, such as partitioned tables.

Partitioning improves the performance and scalability of large datasets in PostgreSQL by organizing data into smaller, more manageable sections.

This document outlines the module's requirements, setup instructions, and usage details for partitioning and unpartitioning database tables.

> ⚠️ **Warning:** This module is currently in **BETA** status. It should be used with **caution**, and you should always **validate backups** before executing any critical operation.

---

## Main Features

The module delivers the following key functionalities:

- Tools for partitioning PostgreSQL database tables.
- Tools for unpartitioning PostgreSQL database tables.
- Advanced management of database table structures and metadata.

> 🚨 **Reminder:** These tools are experimental. Behavior may change between versions as the module evolves during the **BETA** phase.

---

## Requirements

The following prerequisites must be met to use the module:

- Python version 3.
- PostgreSQL database.
- Python Virtual Environment (`python3 -m venv`).
- DBSM (Database Source Manager) version **1.2.0** (ensure it is configured in the `artifacts.list.COMPILATION.gradle` file).

---

## Setting up the Python Environment

To prepare the Python environment necessary for this module:

1. **Create a virtual environment:**

    ```bash
    python3 -m venv modules/com.etendoerp.db.extended/.venv
    ```

2. **Activate the virtual environment:**

    ```bash
    source ./modules/com.etendoerp.db.extended/.venv/bin/activate
    ```

3. **Install the required Python packages:**

    ```bash
    pip3 install pyyaml psycopg2-binary
    ```

---

## Usage

The module provides tools for partitioning and unpartitioning database tables. Proper steps and precautions are outlined below.

> **Best Practice:** Test all operations in a **safe environment** first. Partitioning logic in the BETA module may evolve.

---

### Partition a Table

Partitioning a table alters its physical structure to improve query performance for very large datasets. This process must be executed cautiously and requires appropriate permissions.

#### Steps to Configure a Partitioned Table

1. Log in as **System Administrator**.
2. Ensure you have the necessary privileges to modify system-level configurations.
3. Access the **Partitioned Table Config** Window.
4. Define how tables should be partitioned:
   - Create a new configuration record.
   - Select the table you wish to partition.
   - Choose a column for partitioning (**must reference a date**).
   - Save the configuration.

#### Apply the Partitioning

1. Stop the **Tomcat server**.
2. Execute the following commands to partition the table(s):

    ```bash
    python3 modules/com.etendoerp.db.extended/tool/migrate.py
    ./gradlew update.database -Dforce=yes smartbuild
    ```

- The first command executes the partitioning process based on the configuration set in the data dictionary or a YAML file.
- The second command updates the database by regenerating the table structures to reflect the partitioning.

> **Suggested Screenshot:** Navigate to the "Partitioned Table Config" UI in Etendo ERP, showcasing a new record being created with table and column selection.

---

### Unpartition a Table

In some scenarios, such as exporting the database in development environments, tables may need to be restored to their original, non-partitioned form. The unpartitioning tool enables this.

#### Steps to Unpartition a Table

1. Execute the following command, replacing `"table_name"` with the name of the table to be unpartitioned:

    ```bash
    python3 modules/com.etendoerp.db.extended/tool/unpartition.py "table_name"
    ```

    **Example:**

    ```bash
    python3 modules/com.etendoerp.db.extended/tool/unpartition.py "etpur_archive"
    ```

2. **Regenerate the Database Structure:**

    After unpartitioning, run the following command to update the database metadata:

    ```bash
    ./gradlew update.database -Dforce=yes smartbuild
    ```

This step restores the database to a consistent and functional state by reflecting the changes made during the unpartitioning process.

> **Suggested Screenshot:** Screenshot of command-line execution for unpartitioning a table (e.g., showing `"etpur_archive"` in progress).

---

## Recommendations and Precautions

- 📦 Always perform a **full database backup** before partitioning or unpartitioning operations.
- 🧠 Partitioning should be **planned carefully**, with a clear understanding of its benefits and impact.
- 🧪 Use these commands only in **test or development environments**, unless fully validated in a production context.
- ✅ Verify all configurations and ensure that relevant staff are informed about adopted practices.

> 📢 **Need Help?** For further details, consult the module's supplementary documentation or reach out to the **Etendo support team**.

---

> ⚠️ **Final Note:** This module is in **BETA**. Its behavior may change without notice. Do not use it in production environments without thorough validation.
