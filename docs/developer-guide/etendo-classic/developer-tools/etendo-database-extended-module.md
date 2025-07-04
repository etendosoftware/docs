---
tags:
  - Database Management  
  - Etendo Module
  - com.etendoerp.db.extended (BETA MODULE)
---
# Extended Database Utilities — BETA MODULE


!!! info
    🚧 **IMPORTANT:** This is a **BETA module**. It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**, especially in production environments.

---

## Overview

The `com.etendoerp.db.extended` module expands the database functionalities of the Etendo ERP system.  
This **BETA** module is designed to provide advanced and robust tools to manage complex database structures, such as partitioned tables.

Partitioning improves the performance and scalability of large datasets in PostgreSQL by organizing data into smaller, more manageable sections.

This document outlines the module's requirements, setup instructions, and usage details for partitioning and unpartitioning database tables.

!!!warning
    This module is currently in **BETA** status. It should be used with **caution**, and you should always **validate backups** before executing any critical operation.

---

## Benefits of table partition.

EtendoERP manages large volumes of transactional data that grow over time, which can impact performance.
Table partitioning helps by:

- **Boosting performance:** Queries filter only the relevant partitions (e.g., by year), reducing processing time.
- **Improving data management:** Data is organized logically, making it easier to maintain and archive.
- **Enabling scalability:** Keeps the system efficient even as data grows.

Using partitioning ensures better long-term performance and maintainability of the database.

---

## Recommendations and Precautions

- 📦 Always perform a **full database backup** before partitioning or unpartitioning operations.
- 🧠 Partitioning should be **planned carefully**, with a clear understanding of its benefits and impact.
- 🧪 Use these commands only in **test or development environments**, unless fully validated in a production context.
- ✅ Verify all configurations and ensure that relevant staff are informed about adopted practices.

---

## Main Features

The module delivers the following key functionalities for PostgreSQL databases:

- Tools for partitioning PostgreSQL database tables.
- Tools for unpartitioning PostgreSQL database tables.
- Advanced management of database table structures and metadata.

!!!warning
    These tools are experimental. Behavior may change between versions as the module evolves during the **BETA** phase.

---

## Requirements

The following prerequisites must be met to use the module:

- [Python version 3.](https://docs.python.org/3.13/)
- [PostgreSQL database.](https://www.postgresql.org/docs/16/index.html)
- [Python Virtual Environment (`python3 -m venv`).](https://docs.python.org/3/library/venv.html)
- DBSM (Database Source Manager) version **1.2.0** (you need to configure it in the `artifacts.list.COMPILATION.gradle` file).

---

## Installing the module

To install the module, first you need to clont it:

```bash
git clone git@github.com:etendosoftware/com.etendoerp.db.extended.git
```

Then, after clone it, you need to compile your envirnoment.

```bash
./gradlew update.database smartbuild
```

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

!!! info
    **Best Practice:** Test all operations in a **safe environment** first. Partitioning logic in the BETA module may evolve.

---

### Partition a Table

Partitioning a table alters its physical structure to improve query performance for very large datasets. This process must be executed cautiously and requires appropriate permissions.

#### Steps to Configure a Partitioned Table

1. Log in as **System Administrator**.
2. Access the **Partitioned Table Config** Window:

    :material-menu: `Application`> `Partition`> `Partitioned Table Config`

3. Define how tables should be partitioned:

    - Create a new configuration record.
    - Select the table you wish to partition.
    - Choose a column for partitioning (**must reference a date**).
    !!! Question "Why a date reference?"
        This is because the partitioning script uses the selected column to extract the year from each record and then groups the data into partitions based on that year. Therefore, the column must have a date reference.
    - Save the configuration.

![Partitioned Tables Config](../../../assets/developer-guide/etendo-classic/developer-tools/partitioned_tables_config.png)

#### Apply the Partitioning

1. Stop the **Tomcat server**.
2. Execute the following commands to partition the table(s):

    ```bash
    python3 modules/com.etendoerp.db.extended/tool/migrate.py
    ./gradlew update.database -Dforce=yes smartbuild
    ```

    - The first command executes the partitioning process based on the configuration set in the data dictionary or a YAML file.
    - The second command updates the database by regenerating the table structures to reflect the partitioning.

        !!! note
            A forced `update.database` is executed here because, after partitioning a table, the database structure changes due to one or more tables being partitioned. This step ensures that the updated structure is correctly applied, including handling of partitioned tables, which the default DB Source Manager would not manage properly.

---

### Unpartition a Table

In some scenarios, such as exporting the database in development environments, tables may need to be restored to their original, non-partitioned form. The unpartitioning tool enables this.

#### Steps to Unpartition a Table

1. Execute the following command, replacing "table_name1", "table_name2", etc., with the name of the table(s) you want to unpartition.
You can unpartition one or multiple tables by listing their names separated by commas (no spaces between names).

    ```bash
    python3 modules/com.etendoerp.db.extended/tool/unpartition.py "table_name1, table_name2 ..."
    ```

    **Example:**

    - Unpartition a single table:

    ```bash
    python3 modules/com.etendoerp.db.extended/tool/unpartition.py "c_order, c_invoice"
    ```

    - Unpartition multiple tables:
    
    ```bash
    python3 modules/com.etendoerp.db.extended/tool/unpartition.py "c_order,c_invoice"
    ```

2. **Regenerate the Database Structure:**

    After unpartitioning, run the following command to update the database metadata:

    ```bash
    ./gradlew update.database -Dforce=yes smartbuild
    ```

This step restores the database to a consistent and functional state by reflecting the changes made during the unpartitioning process.

---

!!!warning
    **Final Note:** This module is in **BETA**. Its behavior may change without notice. Do not use it in production environments without thorough validation.
