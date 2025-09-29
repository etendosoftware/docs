---
tags:
  - How to
  - Partitioning
  - Database Extended
  - PostgreSQL
  - Performance
  - Etendo
---

# How to Partition Tables with Etendo Database Extended Module

## Overview

!!!warning "BETA MODULE"
    The Etendo Database Extended module is currently in **BETA**. Features may change without notice. Do not use in production without prior validation.

This guide explains how to partition large PostgreSQL tables using the **Etendo Database Extended** module (module id: `com.etendoerp.db.extended`). Table partitioning improves performance and maintenance for high‑volume tables (faster range queries, smaller indexes, easier archival).

You will:

- Configure a table for yearly range partitioning (by a date / timestamp column) in Application Dictionary (AD).
- Execute the orchestration script `migrate.py` to create the partitioned structure and migrate existing data.
- Refresh the data model so Etendo is aware of structural changes.
- (Optional) Revert partitioning using `unpartition.py` for development or `export.database` operations.

## Prerequisites

- PostgreSQL 16+
- Python 3 (available in the environment)
- Etendo with DBSM 1.2.0+ properly configured
- Etendo Database Extended module installed
- Ability to stop Tomcat temporarily (recommended for consistency)

## Components Involved

### Application Dictionary (AD)
`Partitioned Table Config` window: defines the target table and the date/timestamp column used as the partition key.

### Module Tools (Python)
- `tool/migrate.py`: Orchestrates partition creation and data migration.
- `tool/unpartition.py`: Reverts a partitioned table back to a plain (non‑partitioned) structure (needed before running `export.database`).

### PostgreSQL
Creates the parent partitioned table, yearly partitions, migrates data, and re‑attaches dependencies (indexes, triggers, foreign keys, views).

### DBSM / Gradle
`./gradlew update.database -Dforce=yes smartbuild` aligns the data model metadata with the new physical structure after partitioning or reverting.

## End-to-End Flow (High Level)

```
[1] Define in AD (table + date column)
        |
        v
[2] Stop Tomcat (recommended)
        |
        v
[3] Orchestrate
    $ python3 modules/com.etendoerp.db.extended/tool/migrate.py
        - Validates & prepares
        - Creates parent + yearly partitions
        - Migrates data & re‑attaches dependencies
        |
        v
[4] Refresh Model
    $ ./gradlew update.database -Dforce=yes smartbuild
```

To revert:
```
$ python3 modules/com.etendoerp.db.extended/tool/unpartition.py "table1,table2"
$ ./gradlew update.database -Dforce=yes smartbuild
```

## Internal Operation of migrate.py (Step by Step)

### 1. Configuration & Connection
- Reads database credentials from Etendo environment.
- Reads `Partitioned Table Config` AD entries.

### 2. Pre-Validations
- Ensures table exists and is not already partitioned.
- Validates the partition column exists and is of type `date` or `timestamp`.
- Collects dependent objects (indexes, triggers, foreign keys, views).

### 3. Related Tables Preparation (If Needed)
- Adds missing auxiliary date columns in related tables (when required to maintain referential/temporal integrity).

### 4. Transformation
- Starts a transaction (safe rollback on failure).
- Creates partitioned parent table (mirrors original structure).
- Pre-creates yearly RANGE partitions (e.g. `FOR VALUES FROM ('2023-01-01') TO ('2024-01-01')`).
- Migrates data from original table (automatic routing into partitions).
- Swaps names so the new parent table retains the original logical table name.

### 5. Dependency Re-Attachment
- Recreates indexes.
- Rebuilds triggers.
- Rebinds foreign keys to the new parent.
- Ensures views remain valid.

### 6. Finalization
- Commits on success (rollback otherwise, original table preserved).
- Requires: `./gradlew update.database -Dforce=yes smartbuild` afterward.

## Operational Procedure

### 1. Prepare Environment
```bash
./gradlew update.database smartbuild
python3 -m venv modules/com.etendoerp.db.extended/.venv
source modules/com.etendoerp.db.extended/.venv/bin/activate
pip3 install pyyaml psycopg2-binary
```

### 2. Configure Partition Definition in AD
`Application`>`Partition`>`Partitioned Table Config`

Select:
- Table
- Date/Timestamp Column (high cardinality, e.g. `dateordered`, `created`)

### 3. Execute Partitioning
```bash
# 1) Stop Tomcat (recommended)
# 2) Run migration
python3 modules/com.etendoerp.db.extended/tool/migrate.py
# 3) Refresh model
./gradlew update.database -Dforce=yes smartbuild
```

## ModuleScript: PartitionedConstraintsHandling.java
This ModuleScript runs during `./gradlew update.database ...` and automates constraint adjustments when a table is partitioned or reverted.

### Purpose
- Creates safety backups in schema `etarc_backups` (`<table>_backup_<timestamp>`).
- Maintains `backup_metadata` (auto cleans old backups: retention ~7 days / max 5 per table).
- Rebuilds Primary Key (PK): composite `(id, <partition_column>)` if partitioned; simple `id` if not.
- Recreates Foreign Keys (FKs) in child tables, adding helper column `etarc_<partition_column>__<fkname>` when needed for composite references.

### Process Outline
- Detects partition state via `pg_partitioned_table`.
- Reads XML model definitions for PK/FK metadata.
- Performs controlled DROP / ADD of PK and FKs.
- Adds and (when possible) populates helper columns in child tables.
- Generates detailed, sectioned logs for traceability.

### Log Signals to Look For
- Banner separators: `=======================================================`
- Titles: `Partitioning process info`, `Partitioning processing summary (ms)`
- Backup messages: creation & cleanup details
- Constraint messages: `Recreating constraints for <table>`, `Added helper column ...`

### Common Issues
- Missing PK definition in XML → verify entity XML.
- Permission errors creating `etarc_backups` schema.
- Unexpected FK naming or multi-column FKs.
- Helper column NULL (cannot infer) → populate manually before enforcing composite FK.

## Reverting (Des-Partitioning)
`export.database` does not support partitioned tables. Revert before exporting or for development resets.

```bash
# One or multiple tables (comma separated, no spaces)
python3 modules/com.etendoerp.db.extended/tool/unpartition.py "c_order,c_invoice"
./gradlew update.database -Dforce=yes smartbuild
```

### Internal Steps of unpartition.py
- Creates a non-partitioned replacement table.
- Copies data from parent + partitions.
- Recreates indexes / FKs / triggers.
- Drops partition hierarchy and leaves a flat table with the original logical name.

## Best Practices & Warnings
- Always test in staging first (BETA module).
- Choose a partition key with good distribution and frequent range predicates.
- Plan creation of future yearly partitions proactively.
- Consider per-partition indexes (PostgreSQL lacks global indexes).
- Stop Tomcat during transformation to avoid concurrent writes.
- Keep conventional FK names (simplifies scripted replacement).
- Validate business logic can infer the partition key for child rows.

## Quick Success Checklist
- `\d+ <table>` in `psql` shows `Partitioned table` with yearly partitions (e.g. 2023, 2024 ...).
- Range queries read fewer blocks (partition pruning visible in `EXPLAIN`).
- `./gradlew update.database -Dforce=yes smartbuild` finishes without errors.
- Application operates transparently against the same logical table name.

## Executive Flow Summary
1. Define partition in AD (table + date column).
2. Run `migrate.py` (validates, creates parent, yearly partitions, migrates data, re‑attaches dependencies).
3. Run `update.database` to sync model.
4. (Optional) Run `unpartition.py` + `update.database` to revert.

## Verification Queries (Examples)
```sql
-- Check partitioned status
SELECT relname FROM pg_partitioned_table pt
JOIN pg_class c ON c.oid = pt.partrelid
WHERE relname = 'c_order';

-- List partitions
SELECT inhrelid::regclass AS partition
FROM pg_inherits WHERE inhparent = 'c_order'::regclass
ORDER BY 1;

-- Explain pruning
EXPLAIN ANALYZE SELECT * FROM c_order WHERE dateordered >= '2024-01-01' AND dateordered < '2024-07-01';
```

## Related Documentation
- [Etendo Database Extended Module](../developer-tools/etendo-database-extended-module.md)

