---
title: CRM Lead Management | Developer Guide
tags:
    - CRM
    - Lead Management
    - Lead Status
    - Lead Source
    - System Administrator
---

# CRM Lead Management

:octicons-package-16: Javapackage: `com.etendoerp.crm`

## Overview

This page explains how to configure the master data required by the CRM Lead Management module. These configurations must be performed by a developer with the `System Administrator` role and exported in a development module.

---

## Lead Status
:material-menu: `Application` > `CRM` > `Lead Status`

In this window, the lead statuses that define the commercial pipeline lifecycle are managed. The module seeds the following default statuses:

| Search Key | Name | Base Probability |
|---|---|---|
| `NEW` | New | 10 |
| `CONT` | Contacted | 25 |
| `QUAL` | Qualified | 50 |
| `CONV` | Converted | 70 |
| `DEAD` | Dead | 0 |

Developers with `System Administrator` role can add custom statuses and export them in a development module.

!!! info
    The `CONV` status triggers the lead conversion process automatically. Custom statuses added here will not trigger conversion.

**Fields to note:**

- **Module**: The module where this component will be exported.
- **Search Key**: Unique identifier for the status.
- **Name**: Display name shown in the Lead window.
- **Base Probability**: Numeric value (0–100) used as the starting point when calculating the lead's success probability.
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
