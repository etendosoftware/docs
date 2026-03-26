---
title: CRM Lead Management
status: beta
tags:
    - CRM
    - Gestión de leads
    - Conversión de leads
    - Business Partner
    - Ventas
    - Copilot
    - CRM Agent
---

# Gestión de leads de CRM

:octicons-package-16: Javapackage: `com.etendoerp.crm`

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsala **bajo tu propia responsabilidad**.

## Visión general

El módulo **CRM Lead Management** proporciona capacidades nativas de seguimiento de leads dentro de Etendo ERP. Permite al equipo comercial registrar prospectos, gestionar su ciclo de vida completo mediante estados configurables, organizar tareas de seguimiento y convertir leads cualificados en Terceros — integrándose directamente con el flujo de Ventas (presupuestos → pedidos → facturas).

## Configuración inicial

Antes de usar el módulo, deben configurarse los siguientes datos maestros:

### Lead Status

:material-menu: `Aplicación` > `CRM` > `Lead Status`

Los estados que definen las etapas del embudo comercial pueden gestionarse desde esta ventana. Se pueden añadir nuevos estados para adaptar el embudo a las necesidades de la organización.

!!! info
    Si es necesario exportar estados personalizados como parte de un módulo, esto debe hacerse usando el rol **System Administrator**. Consulta la [CRM Lead Management Developer Guide](../../../../../developer-guide/etendo-classic/bundles/sales-extensions/crm-lead-management.md#lead-status) para más detalles.

### Lead Source

:material-menu: `Aplicación` > `CRM` > `Lead Source`

Los canales de origen a través de los cuales se capturan leads (p. ej., Web, Referencia, Evento, WhatsApp) pueden gestionarse desde esta ventana. Se pueden añadir nuevos orígenes según sea necesario y aparecerán como opciones en el campo **Source** del formulario de Lead.

!!! info
    Si es necesario exportar orígenes personalizados como parte de un módulo, esto debe hacerse usando el rol **System Administrator**. Consulta la [CRM Lead Management Developer Guide](../../../../../developer-guide/etendo-classic/bundles/sales-extensions/crm-lead-management.md#lead-source) para más detalles.

### Clasificación de leads

:material-menu: `Aplicación` > `CRM` > `Lead Classification`

Agrupación opcional para leads. Las clasificaciones se crean desde esta ventana y pueden utilizarse para segmentar leads por sector, región, nivel de valor potencial o cualquier otra categoría de negocio relevante. Una vez creadas, aparecen como opciones en el campo **Clasificación** del formulario de Lead.

![Lead Classification grid showing example classifications](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-classification-grid.png)

---

## Ventana Lead

:material-menu: `Aplicación` > `CRM` > `Lead`

Esta es la ventana principal del módulo. Cada registro representa un prospecto comercial en el embudo de ventas. Desde aquí, el equipo comercial puede registrar nuevos leads, seguir su progreso por estados, registrar tareas de seguimiento y lanzar la conversión a Tercero cuando el lead esté listo.

![Lead form view](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-form-view.png)

**Campos a tener en cuenta:**

- **Nombre**: nombre del contacto.
- **Apellidos**: apellidos del contacto.
- **Correo electrónico**: correo del contacto. Debe tener un formato de email válido.
- **Teléfono**: número de teléfono del contacto.
- **Cargo**: puesto de trabajo del contacto en la empresa.
- **Company**: nombre de la empresa. **Requerido** para realizar la conversión a Tercero.
- **Dirección**: dirección física. **Requerido** para realizar la conversión a Tercero.
- **Responsible**: usuario de Etendo asignado como comercial para este lead.
- **Business Partner**: Tercero vinculado. Se completa automáticamente tras la conversión.
- **Estado**: estado actual del lead.
- **Source**: origen del lead (desde los datos maestros de Lead Source).

    !!! info
        Esta lista puede ampliarse según sea necesario — ver [CRM Lead Management Developer Guide](../../../../../developer-guide/etendo-classic/bundles/sales-extensions/crm-lead-management.md) para más detalles.

    
- **Clasificación**: agrupación opcional (desde los datos maestros de Lead Classification).
- **Descripción**: descripción en texto libre.
- **Estimated Value**: calculado automáticamente a partir de los presupuestos de venta vinculados.
- **Success Probability**: calculado automáticamente (0–100%) en función del estado, las tareas y los presupuestos.
- **Opportunity Status**: Open / Won / Lost.
- **Estimated Close Date**: fecha prevista de cierre de la oportunidad.


### Solapas

#### Tareas

Muestra las tareas de seguimiento asociadas al lead. Cada tarea representa una actividad comercial como una llamada, un email o una reunión. Utiliza el botón **Generate Task** de la barra de herramientas para crear una tarea directamente desde el lead.

![Generate Task dialog](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/generate-task-dialog.png)

**Campos a tener en cuenta:**

- **Task No.**: identificador autogenerado.
- **Task Type**: tipo de actividad. El módulo incluye los siguientes tipos por defecto: *Call*, *Email*, *Meeting*, *Follow-up* y *Sales Quotation*. Esta lista puede ampliarse según sea necesario — ver [Task Developer Guide](../../../../../developer-guide/etendo-classic/bundles/platform/task.md) para más detalles.
- **Estado**: estado actual de la tarea (En progreso, Completada, etc.).
- **Assigned User**: comercial responsable de la tarea.
- **Prioridad**: Baja / Media / Alta.
- **Fecha inicio**: fecha de inicio planificada.
- **Fecha de vencimiento**: fecha límite de la tarea.

![Tasks tab showing generated task](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-tasks-tab.png)

#### Historial de estado

Registro automático de cada transición de estado del lead. Cada registro muestra el estado anterior, el nuevo estado, la fecha del cambio y la tarea asociada (cuando el cambio se disparó al completar una tarea).

Esta solapa proporciona trazabilidad completa del ciclo de vida comercial del lead.

![Status History tab](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-status-history.png)

#### Notas

Notas en texto libre asociadas al lead para comentarios internos de seguimiento.

---

## Ciclo de vida del lead

El lead sigue una progresión por estados que representan la etapa del embudo comercial:

![Lead lifecycle diagram](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/lead-lifecycle.png)

Los estados por defecto y su significado son:

- **New**: lead recién creado, aún no contactado ni evaluado.
- **Contacted**: el lead ha sido contactado a través de al menos un canal.
- **Totalmente correcta**: lead revisado y validado como una oportunidad real de venta.
- **Converted**: lead convertido correctamente en un Tercero.
- **Dead**: lead descartado — sin más acción comercial.

Reglas adicionales:

- Cualquier estado puede transicionar a cualquier otro estado.
- Cambiar el estado siempre genera un registro en la solapa **Historial de estado**.
- Cambiar a **Dead** establece automáticamente el Opportunity Status en **Lost**.
- Transicionar **from Dead** a cualquier otro estado restablece automáticamente el Opportunity Status a **Open**.
- Cambiar a **Converted** dispara el [Proceso de conversión de lead](#proceso-de-conversión-de-lead).

Utiliza el botón **Cambiar Estado** de la barra de herramientas para abrir el diálogo de cambio de estado y seleccionar el estado destino.

![Change Status dialog with available statuses](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/change-status-dialog.png)

---

## Proceso de conversión de lead

Cuando el estado de un lead se cambia a **Converted**, el sistema crea automáticamente un Tercero a partir de los datos del lead.

> **Requisitos previos:** para que la conversión funcione correctamente, debe existir al menos un **Grupos de terceros** activo disponible para la organización. También deben estar configuradas, a nivel de organización, una **Tarifas de venta** activa por defecto y unas **Condiciones de pago** — se asignarán automáticamente al Tercero recién creado.

### Requisitos antes de convertir

- El lead debe tener un nombre de **Company**.
- El lead debe tener **Dirección**.
- El lead no debe estar ya en estado *Converted*.

Al seleccionar *Converted* en el diálogo de Cambiar Estado, aparece un campo opcional **Grupos de terceros** para clasificar el BP recién creado.

![Change Status dialog — Converted with BP Category](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/change-status-converted.png)

### Qué ocurre durante la conversión

1. El sistema comprueba si el lead ya tiene un Tercero vinculado.
   - **Si lo tiene:** se actualiza el BP existente con los valores por defecto de cliente (si aún no es cliente) y se añaden al BP la dirección y el contacto del lead.
   - **Si no lo tiene:** se crea un nuevo Tercero.

2. Al crear un nuevo Tercero:
   - El nombre del BP se toma del campo **Company**.
   - Se genera automáticamente una clave de búsqueda con el formato `Lead/<sequence_number>`.
   - El BP se marca como **Cliente**.
   - Se asignan por defecto las condiciones de facturación, la tarifa y las condiciones de pago.
   - Se crea una **BP Location** a partir de la dirección y el teléfono del lead.
   - Se crea un **BP Contact** (Usuario) a partir del nombre, apellidos, correo electrónico, teléfono y cargo del lead.

3. El campo **Business Partner** del lead se completa con el BP creado/actualizado.
4. El estado del lead se establece en **Converted**.
5. Se añade un registro en la solapa **Historial de estado**.

Tras una conversión correcta, aparece un banner de confirmación en verde y se completa el campo **Business Partner** del lead. La solapa **Historial de estado** registra la transición y pasa a estar disponible una solapa **Presupuesto de ventas** para vincular presupuestos directamente.

!!! info
    Tras la conversión, el Tercero queda totalmente disponible en el flujo de Gestión de Ventas para crear presupuestos, pedidos y facturas.

---

## Seguimiento de oportunidades

Cada lead registra dos métricas calculadas que se actualizan automáticamente:

### Success Probability

Un valor entre 0% y 100% que representa la probabilidad de que el lead se convierta en una venta.

Se calcula automáticamente en base a:

- **Lead Status**: probabilidad base por estado — New: 10%, Contacted: 25%, Qualified: 50%, Converted: 70%, Dead: 0%.
- **Completed task in last 7 days**: +10 puntos.
- **No activity in last 30 days**: -20 puntos. La actividad se define como una actualización de tarea o un cambio de estado. Si el lead no tiene ninguna actividad registrada (p. ej., recién creado, sin tareas), esta penalización se aplica inmediatamente.
- **Quotations**: hasta +20 puntos en función de su estado. Los presupuestos en estado Order Created cuentan al 100%, los Under Evaluation cuentan con un peso del 50% y los Rejected cuentan como 0 — reduciendo la puntuación global de presupuestos sin aplicar una penalización directa.

!!! info
    Dado que la penalización por inactividad (-20) se aplica cuando no hay actividad registrada, un lead recién creado comienza con una probabilidad inferior a la que sugiere el valor base de su estado. Por ejemplo, un lead New comienza en 0% (10 - 20, limitado) hasta que se registre una tarea o un cambio de estado.

!!! info
    La probabilidad se recalcula automáticamente en cada guardado. La edición manual del campo se sobrescribirá en el siguiente cambio.

### Estimated Value

La suma de los totales de todos los presupuestos de venta activos vinculados al lead que estén en estado **Under Evaluation** o **Order Created**. Se actualiza automáticamente cuando cambian los importes o los estados de los presupuestos.

### Opportunity Status

- **Open**: por defecto cuando se crea el lead. Se establece automáticamente.
- **Won**: el lead resultó en una venta cerrada. Se establece automáticamente cuando un presupuesto genera un pedido, o manualmente con validación.
- **Lost**: el lead no resultará en una venta. Se establece automáticamente cuando el estado del lead se establece en *Dead*, o manualmente.

!!! info
    Para establecer manualmente el Opportunity Status en **Won**, el lead debe tener al menos un presupuesto en estado *Order Created*, o un pedido de venta completado creado después de la fecha de conversión del lead.

---

## Integración con Presupuesto de ventas

Los presupuestos de venta (del módulo de Gestión de Ventas) pueden vincularse a un lead seleccionando el lead en el campo **Lead** de la cabecera del presupuesto.

Cuando se selecciona un lead en un presupuesto:

- El campo **Business Partner** se completa automáticamente a partir del BP vinculado al lead.
- Los cambios de estado del presupuesto actualizan automáticamente el **Success Probability** y el **Estimated Value** del lead.
- Cuando un presupuesto alcanza el estado *Order Created*, el **Opportunity Status** del lead se establece automáticamente en **Won**.

---

## Mobile App

El módulo CRM Lead Management incluye una aplicación móvil que permite al equipo comercial gestionar sus leads desde cualquier dispositivo, sin necesidad de acceder al ERP de escritorio.

La experiencia móvil está **orientada a tareas**: la app muestra las tareas asignadas al usuario que ha iniciado sesión, y todas las interacciones con el lead —incluyendo actualizaciones de datos y cambios de estado— se realizan a través de esas tareas.

### Task List

Al abrir la app, el usuario ve la lista de tareas de CRM asignadas, ordenadas por prioridad y fecha de vencimiento. Cada tarea muestra el lead al que pertenece, el tipo de tarea y su estado actual.

![Mobile task list](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/mobile-task-list.png)

### Lead Detail

Al tocar una tarea se abre la vista de detalle del lead, donde el usuario puede:

- Revisar y actualizar la información de contacto y de la empresa del lead.
- Ver el estado actual y los datos de oportunidad.
- Consultar el historial completo de estados.

![Mobile lead detail](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/mobile-lead-detail.png)

### Changing Lead Status

Desde la vista de detalle del lead, el usuario puede cambiar el estado del lead usando la acción **Cambiar Estado**. Se aplican las mismas reglas que en el escritorio: cambiar a *Converted* dispara la creación del tercero y cambiar a *Dead* establece la oportunidad como *Lost*.

![Mobile change status](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/sales-extensions/crm/mobile-change-status.png)

### Completing a Task

Una vez realizada la actividad, el usuario puede marcar la tarea como completada directamente desde la app. Completar una tarea la registra como actividad reciente, lo que impacta positivamente en el cálculo de **Success Probability** del lead.

!!! warning
    Actualmente no se soporta la creación de presupuestos de venta desde la app móvil. Los presupuestos deben gestionarse desde Etendo ERP.

---

## CRM Agent

El **CRM Agent** es un asistente de Copilot especializado en analítica de CRM para Etendo ERP. Permite al equipo comercial consultar y analizar datos de CRM usando lenguaje natural, sin necesidad de crear informes o consultas manualmente.

!!! info
    El CRM Agent solo lee datos. No puede crear, modificar ni eliminar ningún registro.

### Qué puedes preguntar

El agente puede responder a preguntas de negocio en cuatro áreas:

#### Leads

Estado del embudo, origen, clasificación, probabilidad, valor estimado e histórico de conversión.

- *"Show my leads in Qualified status"*
- *"How many leads were converted this month?"*
- *"What is the total estimated value of leads in progress?"*

#### Actividades (tareas de CRM)

Tareas de seguimiento vinculadas a leads, tareas vencidas, asignación de tareas y estado.

- *"Show my pending tasks for today"*
- *"Show all overdue activities assigned to the sales team"*

#### Clientes (Terceros)

Aquí, clientes se refiere a Terceros que se originaron a partir de un lead convertido. El agente soporta:

- **New customers**: Terceros creados a partir de un lead en un periodo dado.
- **Segmentation**: clientes agrupados por región o sector.
- **Latest interaction**: tarea más reciente vinculada a cada cliente a través de su lead asociado.
- **Inactivity alerts**: clientes sin actividad registrada dentro de un número de días especificado.

Consultas de ejemplo:

- *"New customers this month"*
- *"List customers by industry"*
- *"Show the last interaction per customer"*
- *"Customers without contact in the last 30 days"*

#### Conversión y rendimiento

Métricas que miden la efectividad del proceso de ventas a través de las etapas del ciclo de vida.

- **Conversion rates**:
    - Lead → Qualified: porcentaje de leads que alcanzaron el estado Qualified en un periodo.
    - Qualified → Converted: porcentaje de leads Qualified que se convirtieron.
    - Converted → Sale: porcentaje de leads Converted que generaron al menos un Pedido de venta.
- **Average time per stage**: número medio de días entre creación → Qualified, Qualified → Converted y Converted → Sale.
- **Sales performance ranking**: usuarios clasificados por número de leads convertidos, ventas cerradas, valor total de ventas o tasa de conversión.

Consultas de ejemplo:

- *"What is the lead conversion rate this month?"*
- *"What is the conversion rate from Qualified to Converted?"*
- *"What is the average closing time of a converted lead?"*
- *"Show me the sales performance ranking"*
- *"Who has the highest conversion rate this quarter?"*

### Comportamientos clave

- **Idioma**: responde en el mismo idioma utilizado por el usuario (español o inglés).
- **Pronombres personales**: cuando usas "my", "mine", "mis", "tengo", etc., el agente filtra automáticamente los resultados por tu usuario — mostrando solo tus leads o tus tareas asignadas.
- **Transparencia SQL**: por defecto el agente devuelve solo los resultados. Si quieres ver la consulta subyacente, pídelo explícitamente ("show me the query" / "muéstrame la consulta").
- **Límites de resultados**: las consultas de listado están limitadas a 100 registros por defecto para evitar sobrecarga.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

---