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
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Overview

Esta página explica cómo exportar los datos maestros de CRM (estados y orígenes) como parte de un módulo de desarrollo. Estas operaciones deben realizarse con el rol `System Administrator`. Para la configuración diaria sin exportación de módulos, consulte la [CRM Lead Management User Guide](../../../../../user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm-lead-management.md).

---

## Lead Status
:material-menu: `Aplicación` > `CRM` > `Lead Status`

En esta ventana se gestionan los estados de oportunidad que definen el ciclo de vida del pipeline comercial. El módulo crea los siguientes estados predeterminados:

| Search Key | Name |
|---|---|
| `NEW` | New |
| `CONT` | Contacted |
| `QUAL` | Qualified |
| `CONV` | Converted |
| `DEAD` | Dead |

Los desarrolladores con rol `System Administrator` pueden añadir estados personalizados y exportarlos en un módulo de desarrollo.

!!! info
    El estado `CONV` activa automáticamente el proceso de conversión de la oportunidad. Los estados personalizados añadidos aquí no activarán la conversión.

!!! warning
    La probabilidad base asignada a cada estado se determina por su Search Key: New=10%, Contacted=25%, Qualified=50%, Converted=70%, Dead=0%. Los estados personalizados tendrán por defecto una probabilidad base del 0%. Tenga en cuenta que la probabilidad final calculada también aplica una penalización de inactividad de -20 cuando no se registran tareas ni cambios de estado, por lo que una oportunidad recién creada comenzará por debajo de su valor base (por ejemplo, una oportunidad New comienza en 0%).

**Fields to note:**

- **Módulo**: El módulo en el que se exportará este componente.
- **Search Key**: Identificador único del estado. El sistema usa esta clave para determinar la probabilidad base en los cálculos de probabilidad.
- **Nombre**: Nombre mostrado en la ventana de oportunidad.
- **Activo**: Casilla para habilitar o deshabilitar este estado.

---

## Lead Source
:material-menu: `Aplicación` > `CRM` > `Lead Source`

En esta ventana se definen los canales de origen a través de los cuales se capturan las oportunidades (por ejemplo, Web, Referral, Cold Call, Event, Social Media).

Los desarrolladores con rol `System Administrator` pueden añadir orígenes personalizados y exportarlos en un módulo de desarrollo.

!!! info
    Debe existir al menos un Lead Source antes de crear una oportunidad, ya que este campo es obligatorio.

**Fields to note:**

- **Módulo**: El módulo en el que se exportará este componente.
- **Search Key**: Identificador único del origen.
- **Nombre**: Nombre mostrado en la ventana de oportunidad.
- **Activo**: Casilla para habilitar o deshabilitar este origen.

---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.