---
title: Gestión de Leads CRM | Guía del Desarrollador
tags:
    - CRM
    - Gestión de Leads
    - Lead Status
    - Lead Source
    - Administrador del Sistema
---

# Gestión de Leads CRM

:octicons-package-16: Paquete Java: `com.etendoerp.crm`

## Overview

Esta página explica cómo configurar los datos maestros requeridos por el módulo CRM Lead Management. Estas configuraciones deben ser realizadas por un desarrollador con el rol `Administrador del Sistema` y exportadas en un módulo de desarrollo.

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

**Fields to note:**

- **Módulo**: El módulo donde se exportará este componente.
- **Identificador**: Identificador único del estado.
- **Nombre**: Nombre visible mostrado en la ventana de Lead.
- **Base Probability**: Valor numérico (0–100) usado como punto de partida al calcular la probabilidad de éxito del lead.
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