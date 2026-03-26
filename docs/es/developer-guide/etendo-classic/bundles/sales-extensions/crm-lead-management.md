---
title: Gestión de Leads CRM | Guía del Desarrollador
status: beta
tags:
    - CRM
    - Gestión de Leads
    - Lead Status
    - Lead Source
    - Administrador del Sistema
---

# Gestión de Leads CRM

:octicons-package-16: Paquete Java: `com.etendoerp.crm`

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsala **bajo tu propia responsabilidad**.

## Overview

Esta página explica cómo exportar los datos maestros de CRM (estados y orígenes) como parte de un módulo de desarrollo. Estas operaciones deben realizarse con el rol `Administrador del Sistema`. Para la configuración diaria sin exportación de módulo, consulta la [Guía de Usuario de CRM Lead Management](../../../../../user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm-lead-management.md).

---

## Lead Status
:material-menu: `Aplicación` > `Conector CRM` > `Lead Status`

En esta ventana se gestionan los estados del lead que definen el ciclo de vida del pipeline comercial. El módulo incluye los siguientes estados por defecto:

| Identificador | Nombre | Base Probability |
|---|---|---|
| `NEW` | Nuevo | 10 |
| `CONT` | Contactado | 25 |
| `QUAL` | Cualificado | 50 |
| `CONV` | Convertido | 70 |
| `DEAD` | Perdido | 0 |

Los desarrolladores con el rol `Administrador del Sistema` pueden añadir estados personalizados y exportarlos en un módulo de desarrollo.

!!! info
    El estado `CONV` dispara automáticamente el proceso de conversión del lead. Los estados personalizados añadidos aquí no dispararán la conversión.

!!! warning
    La probabilidad base asignada a cada estado se determina por su Identificador: Nuevo=10%, Contactado=25%, Cualificado=50%, Convertido=70%, Perdido=0%. Los estados personalizados tendrán por defecto una probabilidad base del 0%. Ten en cuenta que la probabilidad final calculada también aplica una penalización de inactividad de -20 cuando no se registran tareas ni cambios de estado, por lo que un lead recién creado comenzará por debajo de su valor base (por ejemplo, un lead Nuevo comienza en 0%).

**Fields to note:**

- **Módulo**: El módulo donde se exportará este componente.
- **Identificador**: Identificador único del estado. El sistema usa este identificador para determinar la probabilidad base en los cálculos de probabilidad.
- **Nombre**: Nombre visible mostrado en la ventana de Lead.
- **Activo**: Casilla para habilitar o deshabilitar este estado.

---

## Lead Source
:material-menu: `Aplicación` > `Conector CRM` > `Lead Source`

En esta ventana se definen los canales de origen a través de los cuales se capturan los leads (p. ej., Web, Referencia, Llamada en frío, Evento, Redes sociales).

Los desarrolladores con el rol `Administrador del Sistema` pueden añadir orígenes personalizados y exportarlos en un módulo de desarrollo.

!!! info
    Debe existir al menos un Lead Source antes de crear un Lead, ya que este campo es obligatorio.

**Fields to note:**

- **Módulo**: El módulo donde se exportará este componente.
- **Identificador**: Identificador único del origen.
- **Nombre**: Nombre visible mostrado en la ventana de Lead.
- **Activo**: Casilla para habilitar o deshabilitar este origen.

---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.