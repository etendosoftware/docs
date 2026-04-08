---
title: Gestión de Leads de CRM
status: beta
tags:
    - CRM
    - Gestión de Leads
    - Conversión de Leads
    - Tercero
    - Ventas
    - Copilot
    - Agente CRM
---

# Gestión de Leads de CRM

:octicons-package-16: Javapackage: `com.etendoerp.crm`

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsala **bajo tu propia responsabilidad**.

!!! info
    Esta funcionalidad está disponible a partir de la versión **4.0.0** del Sales Extensions Bundle, desde **Etendo 26.1**. Para poder incluir esta funcionalidad, el Sales Extensions Bundle debe estar instalado. Para ello, sigue las instrucciones del marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con core y las nuevas funcionalidades, visita [Sales Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/sales-extensions/release-notes.md).

## Overview

El módulo **Gestión de Leads de CRM** proporciona capacidades nativas de seguimiento de leads dentro de Etendo ERP. Permite al equipo comercial registrar prospectos, gestionar su ciclo de vida completo mediante estados configurables, organizar tareas de seguimiento y convertir leads cualificados en Terceros, integrándose directamente con el flujo de Ventas (presupuestos → pedidos → facturas).

## Initial Setup

Antes de usar el módulo, deben configurarse los siguientes datos maestros:

### Lead Status

:material-menu: `Aplicación` > `Conector CRM` > `Lead Status`

Los estados que definen las etapas del pipeline comercial se pueden gestionar desde esta ventana. Se pueden añadir nuevos estados para adaptar el pipeline a las necesidades de la organización.

!!! info
    Si es necesario exportar estados personalizados como parte de un módulo, esto debe hacerse usando el rol **System Administrator**. Consulta la [CRM Lead Management Developer Guide](../../../../../developer-guide/etendo-classic/bundles/sales-extensions/crm-lead-management.md#lead-status) para más detalles.

### Lead Source

:material-menu: `Aplicación` > `Conector CRM` > `Lead Source`

Los canales de origen a través de los cuales se capturan los leads (por ejemplo, Web, Referencia, Evento, WhatsApp) se pueden gestionar desde esta ventana. Se pueden añadir nuevas fuentes según sea necesario y aparecerán como opciones en el campo **Source** del formulario de Lead.

!!! info
    Si es necesario exportar fuentes personalizadas como parte de un módulo, esto debe hacerse usando el rol **System Administrator**. Consulta la [CRM Lead Management Developer Guide](../../../../../developer-guide/etendo-classic/bundles/sales-extensions/crm-lead-management.md#lead-source) para más detalles.

### Lead Classification

:material-menu: `Aplicación` > `Conector CRM` > `Lead Classification`

Agrupación opcional para leads. Las clasificaciones se crean desde esta ventana y se pueden usar para segmentar leads por sector, región, nivel de valor potencial o cualquier otra categoría de negocio relevante. Una vez creadas, aparecen como opciones en el campo **Classification** del formulario de Lead.

![Lead Classification grid showing example classifications](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-classification-grid.png)

---

## Lead Window

:material-menu: `Aplicación` > `Conector CRM` > `Lead`

Esta es la ventana principal del módulo. Cada registro representa un prospecto comercial en el pipeline de ventas. Desde aquí, el equipo comercial puede registrar nuevos leads, seguir su progreso a través de estados, registrar tareas de seguimiento y activar la conversión a Tercero cuando el lead esté listo.

![Lead form view](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-form-view.png)

**Campos a tener en cuenta:**

- **First Name**: Nombre del contacto.
- **Last Name**: Apellidos del contacto.
- **Email**: Correo electrónico del contacto. Debe tener un formato de correo electrónico válido.
- **Phone**: Teléfono del contacto.
- **Position**: Cargo del contacto en la empresa.
- **Company**: Nombre de la empresa. **Obligatorio** para realizar la conversión a Tercero.
- **Location / Address**: Dirección física. **Obligatorio** para realizar la conversión a Tercero.
- **Responsible**: Usuario de Etendo asignado como comercial responsable de este lead.
- **Business Partner**: Tercero vinculado. Se completa automáticamente después de la conversión.
- **Status**: Estado actual del lead.
- **Source**: Origen del lead (desde los datos maestros de Lead Source).

    !!! info
        Esta lista se puede ampliar según sea necesario — consulta la [CRM Lead Management Developer Guide](../../../../../developer-guide/etendo-classic/bundles/sales-extensions/crm-lead-management.md) para más detalles.

    
- **Classification**: Agrupación opcional (desde los datos maestros de Lead Classification).
- **Description**: Descripción de texto libre.
- **Estimated Value**: Calculado automáticamente a partir de los presupuestos de ventas vinculados.
- **Success Probability**: Calculado automáticamente (0–100%) en función del estado, las tareas y los presupuestos.
- **Opportunity Status**: Open / Won / Lost.
- **Estimated Close Date**: Fecha prevista de cierre de la oportunidad.


### Tabs

#### Tasks

Muestra las tareas de seguimiento asociadas al lead. Cada tarea representa una actividad comercial como una llamada, un correo electrónico o una reunión. Usa el botón **Generate Task** en la barra de herramientas para crear una tarea directamente desde el lead.

![Generate Task dialog](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/generate-task-dialog.png)

**Campos a tener en cuenta:**

- **Task No.**: Identificador generado automáticamente.
- **Task Type**: Tipo de actividad. El módulo incluye los siguientes tipos predeterminados: *Call*, *Email*, *Meeting*, *Follow-up* y *Sales Quotation*. Esta lista se puede ampliar según sea necesario — consulta la [Task Developer Guide](../../../../../developer-guide/etendo-classic/bundles/platform/task.md) para más detalles.
- **Status**: Estado actual de la tarea (In Progress, Completed, etc.).
- **Assigned User**: Comercial responsable de la tarea.
- **Priority**: Low / Medium / High.
- **Start Date**: Fecha de inicio planificada.
- **Due Date**: Fecha límite de la tarea.

![Tasks tab showing generated task](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-tasks-tab.png)

#### Status History

Registro automático de cada transición de estado del lead. Cada registro muestra el estado anterior, el nuevo estado, la fecha del cambio y la tarea asociada (cuando el cambio se activó al completar una tarea).

Esta solapa proporciona trazabilidad completa del ciclo de vida comercial del lead.

![Status History tab](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-status-history.png)

#### Notes

Notas de texto libre asociadas al lead para comentarios internos de seguimiento.

---

## Lead Lifecycle

El lead sigue una progresión a través de estados que representan la etapa del pipeline comercial:

![Lead lifecycle diagram](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-lifecycle.png)

Los estados predeterminados y su significado son:

- **New**: Lead recién creado, aún no contactado ni evaluado.
- **Contacted**: Se ha contactado con el lead a través de al menos un canal.
- **Qualified**: Lead revisado y validado como una oportunidad de venta real.
- **Converted**: Lead convertido correctamente en un Tercero.
- **Dead**: Lead descartado — no se realizará ninguna acción comercial adicional.

Reglas adicionales:

- Cualquier estado puede transicionar a cualquier otro estado.
- Cambiar el estado siempre genera un registro en la solapa **Status History**.
- Cambiar a **Dead** establece automáticamente el Opportunity Status en **Lost**.
- Pasar **from Dead** a cualquier otro estado restablece automáticamente el Opportunity Status a **Open**.
- Cambiar a **Converted** activa el [Lead Conversion Process](#lead-conversion-process).

Usa el botón **Change Status** en la barra de herramientas para abrir el diálogo de cambio de estado y seleccionar el estado de destino.

![Change Status dialog with available statuses](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/change-status-dialog.png)

---

## Lead Conversion Process

Cuando el estado de un lead se cambia a **Converted**, el sistema crea automáticamente un Tercero a partir de los datos del lead.

> **Prerequisites:** Para que la conversión funcione correctamente, debe haber al menos una **Business Partner Category** activa disponible para la organización. También deben estar configuradas en el ámbito de la organización una **Sales Price List** y unas **Payment Terms** activas por defecto; se asignarán automáticamente al nuevo Tercero creado.

### Requirements Before Converting

- El lead debe tener un nombre de **Company**.
- El lead debe tener una **Location / Address**.
- El lead no debe estar ya en estado *Converted*.

Al seleccionar *Converted* en el diálogo Change Status, aparece un campo opcional **Business Partner Category** para clasificar el nuevo Tercero creado.

![Change Status dialog — Converted with BP Category](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/change-status-converted.png)

### What Happens During Conversion

1. El sistema comprueba si el lead ya tiene un Tercero vinculado.
   - **If it does:** el Tercero existente se actualiza con los valores predeterminados de cliente (si aún no es cliente) y se añaden al Tercero la ubicación y el contacto del lead.
   - **If it doesn't:** se crea un nuevo Tercero.

2. Al crear un nuevo Tercero:
   - El nombre del Tercero se toma del campo **Company**.
   - Se genera automáticamente una clave de búsqueda usando el formato `Lead/<sequence_number>`.
   - El Tercero se marca como **Customer**.
   - Se asignan los valores predeterminados de Invoice Terms, Price List y Payment Terms.
   - Se crea una **BP Location** a partir de la dirección y el teléfono del lead.
   - Se crea un **BP Contact** (User) a partir del nombre, apellidos, correo electrónico, teléfono y cargo del lead.

3. El campo **Business Partner** del lead se completa con el Tercero creado/actualizado.
4. El estado del lead se establece en **Converted**.
5. Se añade un registro a la solapa **Status History**.

Tras una conversión correcta, aparece un banner verde de confirmación y el campo **Business Partner** del lead se completa. La solapa **Status History** registra la transición y una solapa **Sales Quotation** pasa a estar disponible para vincular presupuestos directamente.

!!! info
    Después de la conversión, el Tercero queda completamente disponible en el flujo de Sales Management para crear presupuestos, pedidos y facturas.

---

## Opportunity Tracking

Cada lead registra dos métricas calculadas que se actualizan automáticamente:

### Success Probability

Un valor entre 0% y 100% que representa la probabilidad de que el lead se convierta en una venta.

Se calcula automáticamente en función de:

- **Lead Status**: Probabilidad base por estado — New: 10%, Contacted: 25%, Qualified: 50%, Converted: 70%, Dead: 0%.
- **Completed task in last 7 days**: +10 puntos.
- **No activity in last 30 days**: -20 puntos. La actividad se define como una actualización de tarea o un cambio de estado. Si el lead no tiene ninguna actividad registrada en absoluto (por ejemplo, recién creado, sin tareas), esta penalización se aplica inmediatamente.
- **Quotations**: Hasta +20 puntos según su estado. Los presupuestos en estado Order Created cuentan al 100%, los de Under Evaluation al 50% y los presupuestos rechazados cuentan como 0, reduciendo la puntuación global de presupuestos sin aplicar una penalización directa.

!!! info
    Como la penalización por inactividad (-20) se aplica cuando no hay actividad registrada, un lead recién creado comienza con una probabilidad inferior a la que sugiere su valor base por estado. Por ejemplo, un lead New comienza en 0% (10 - 20, limitado) hasta que se registra una tarea o un cambio de estado.

!!! info
    La probabilidad se recalcula automáticamente en cada guardado. La edición manual del campo se sobrescribirá en el siguiente cambio.

### Estimated Value

La suma de los totales de todos los presupuestos de ventas activos vinculados al lead que estén en estado **Under Evaluation** o **Order Created**. Se actualiza automáticamente cuando cambian los importes o los estados de los presupuestos.

### Opportunity Status

- **Open**: Valor predeterminado cuando se crea el lead. Se establece automáticamente.
- **Won**: El lead ha dado lugar a una venta cerrada. Se establece automáticamente cuando un presupuesto genera un pedido, o manualmente con validación.
- **Lost**: El lead no dará lugar a una venta. Se establece automáticamente cuando el estado del lead se fija en *Dead*, o manualmente.

!!! info
    Para establecer manualmente Opportunity Status en **Won**, el lead debe tener al menos un presupuesto en estado *Order Created*, o un pedido de venta completado creado después de la fecha de conversión del lead.

---

## Sales Quotation Integration

Los presupuestos de ventas (del módulo Sales Management) se pueden vincular a un lead seleccionando el lead en el campo **Lead** del encabezado del presupuesto.

Cuando se selecciona un lead en un presupuesto:

- El campo **Business Partner** se completa automáticamente con el Tercero vinculado al lead.
- Los cambios de estado del presupuesto actualizan automáticamente la **Success Probability** y el **Estimated Value** del lead.
- Cuando un presupuesto alcanza el estado *Order Created*, el **Opportunity Status** del lead se establece automáticamente en **Won**.

---

## Mobile App

El módulo Gestión de Leads de CRM incluye una aplicación móvil que permite al equipo comercial gestionar sus leads desde cualquier dispositivo, sin necesidad de acceder al ERP de escritorio.

La experiencia móvil está **task-driven**: la app muestra las tareas asignadas al usuario conectado, y todas las interacciones con el lead —incluidas las actualizaciones de datos y los cambios de estado— se realizan a través de esas tareas.

### Task List

![Mobile task list](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/mobile-task-list.png){align=right width=300}

Al abrir la app, el usuario ve la lista de tareas de CRM asignadas, ordenadas por prioridad y fecha de vencimiento. Cada tarjeta de tarea muestra:

- **Task No**: Identificador único de la tarea
- **Company Name**: La empresa asociada al lead
- **Status**: Estado de la tarea (por ejemplo, New, Converted) con una insignia codificada por color
- **Task Type**: Tipo de actividad (por ejemplo, Email, Meeting)
- **Priority**: Nivel de prioridad de la tarea (por ejemplo, Critical, Major) con una insignia codificada por color
- **Task Due Date**: Fecha de vencimiento de la tarea

<br clear="all">

### Lead Detail

Al pulsar una tarea se abre la vista de detalle del lead, donde el usuario puede:

- Revisar y actualizar la información de contacto y empresa del lead.
- Ver el estado actual y los datos de la oportunidad.
- Consultar el historial completo de estados.

![Mobile lead detail](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/mobile-lead-detail.png)

### Changing Lead Status

Desde la vista de detalle del lead, el usuario puede cambiar el estado del lead usando la acción **Change Status**. Se aplican las mismas reglas que en escritorio: cambiar a *Converted* activa la creación del tercero y cambiar a *Dead* establece la oportunidad en *Lost*.

![Mobile change status](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/mobile-change-status.png)

### Completing a Task

Una vez realizada la actividad, el usuario puede marcar la tarea como completada directamente desde la app. Completar una tarea la registra como actividad reciente, lo que impacta positivamente en el cálculo de la **Success Probability** del lead.

!!! warning
    Actualmente no se admite la creación de presupuestos de ventas desde la aplicación móvil. Los presupuestos deben gestionarse desde Etendo ERP.

---

## CRM Agent

El **CRM Agent** es un asistente de Copilot especializado en analítica de CRM para Etendo ERP. Permite al equipo comercial consultar y analizar datos de CRM usando lenguaje natural, sin necesidad de escribir informes o consultas manualmente.

!!! info
    El CRM Agent solo lee datos. No puede crear, modificar ni eliminar ningún registro.

### What You Can Ask

El agente puede responder preguntas de negocio en cuatro áreas:

#### Leads

Estado del pipeline, origen, clasificación, probabilidad, valor estimado e historial de conversión.

- *"Show my leads in Qualified status"*
- *"How many leads were converted this month?"*
- *"What is the total estimated value of leads in progress?"*

#### Activities (CRM Tasks)

Tareas de seguimiento vinculadas a leads, tareas vencidas, asignación de tareas y estado.

- *"Show my pending tasks for today"*
- *"Show all overdue activities assigned to the sales team"*

#### Customers (Business Partners)

Customers aquí se refiere a Terceros que se originaron a partir de un lead convertido. El agente admite:

- **New customers**: Terceros creados a partir de un lead en un periodo determinado.
- **Segmentation**: clientes agrupados por región o sector.
- **Latest interaction**: tarea más reciente vinculada a cada cliente a través de su lead asociado.
- **Inactivity alerts**: clientes sin actividad registrada dentro de un número determinado de días.

Ejemplos de consultas:

- *"New customers this month"*
- *"List customers by industry"*
- *"Show the last interaction per customer"*
- *"Customers without contact in the last 30 days"*

#### Conversion & Performance

Métricas que miden la eficacia del proceso de ventas a lo largo de las etapas del ciclo de vida.

- **Conversion rates**:
    - Lead → Qualified: porcentaje de leads que alcanzaron el estado Qualified en un periodo.
    - Qualified → Converted: porcentaje de leads Qualified que fueron convertidos.
    - Converted → Sale: porcentaje de leads Converted que generaron al menos un Sales Order.
- **Average time per stage**: número medio de días entre creación → Qualified, Qualified → Converted y Converted → Sale.
- **Sales performance ranking**: usuarios clasificados por número de leads convertidos, ventas cerradas, valor total de ventas o tasa de conversión.

Ejemplos de consultas:

- *"What is the lead conversion rate this month?"*
- *"What is the conversion rate from Qualified to Converted?"*
- *"What is the average closing time of a converted lead?"*
- *"Show me the sales performance ranking"*
- *"Who has the highest conversion rate this quarter?"*

### Key Behaviors

- **Language**: responde en el mismo idioma usado por el usuario (español o inglés).
- **Personal pronouns**: cuando uses "my", "mine", "mis", "tengo", etc., el agente filtra automáticamente los resultados por tu usuario — mostrando solo tus leads o tus tareas asignadas.
- **SQL transparency**: por defecto el agente devuelve solo los resultados. Si quieres ver la consulta subyacente, pídelo explícitamente ("show me the query" / "muéstrame la consulta").
- **Result limits**: las consultas de listado se limitan a 100 registros por defecto para evitar sobrecarga.

---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.