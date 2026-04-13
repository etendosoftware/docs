---
title: CRM Lead Management
status: beta
tags:
    - CRM
    - Lead Management
    - Lead Status
    - Lead Source
    - System Administrator
---

# CRM Lead Management

:octicons-package-16: Javapackage: `com.etendoerp.crm`

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

## Overview

This page explains how to export the CRM master data (statuses and sources) as part of a development module. These operations must be performed with the `System Administrator` role. For day-to-day configuration without module export, see the [CRM Lead Management User Guide](../../../../../user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm-lead-management.md).

---

## Lead Status
:material-menu: `Application` > `CRM` > `Lead Status`

In this window, the lead statuses that define the commercial pipeline lifecycle are managed. The module seeds the following default statuses:

| Search Key | Name |
|---|---|
| `NEW` | New |
| `CONT` | Contacted |
| `QUAL` | Qualified |
| `CONV` | Converted |
| `DEAD` | Dead |

Developers with `System Administrator` role can add custom statuses and export them in a development module.

!!! info
    The `CONV` status triggers the lead conversion process automatically. Custom statuses added here will not trigger conversion.

!!! warning
    The base probability assigned to each status is determined by its Search Key: New=10%, Contacted=25%, Qualified=50%, Converted=70%, Dead=0%. Custom statuses will default to 0% base probability. Note that the final calculated probability also applies a -20 inactivity penalty when no tasks or status changes are recorded, so a newly created lead will start lower than its base value (e.g., a New lead starts at 0%).

**Fields to note:**

- **Module**: The module where this component will be exported.
- **Search Key**: Unique identifier for the status. The system uses this key to determine the base probability for probability calculations.
- **Name**: Display name shown in the Lead window.
- **Active**: Checkbox to enable or disable this status.

---

## Lead Source
:material-menu: `Application` > `CRM` > `Lead Source`

In this window, the origin channels through which leads are captured are defined (e.g., Web, Referral, Cold Call, Event, Social Media).

Developers with `System Administrator` role can add custom sources and export them in a development module.

!!! info
    At least one Lead Source must exist before creating a Lead, as this field is required.

**Fields to note:**

- **Module**: The module where this component will be exported.
- **Search Key**: Unique identifier for the source.
- **Name**: Display name shown in the Lead window.
- **Active**: Checkbox to enable or disable this source.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
