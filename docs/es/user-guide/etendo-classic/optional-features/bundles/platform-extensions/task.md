---
title: Mantenimiento - Guía de usuario
tags: 
    - Mantenimiento 
    - Gestión de tareas
---

# Mantenimiento
:octicons-package-16: Javapackage: `com.etendoerp.task`

## Visión general

La infraestructura de mantenimiento en Etendo permite la creación, asignación y gestión automáticas de tareas basadas en eventos de base de datos, como la inserción o actualización de registros. Está diseñada para ayudar a las organizaciones a automatizar procesos de negocio mediante la definición de tipos de tarea, algoritmos de asignación y acciones automatizadas que se activan cuando ocurren eventos específicos. Esta funcionalidad es útil para casos en los que se requiere un seguimiento consistente, validación o acciones del usuario, como la gestión de pedidos, el seguimiento de incidencias o las actualizaciones del estado del cliente.

!!! warning
    Para poder utilizar esta infraestructura de mantenimiento es necesario definir tipos de tarea, algoritmos de asignación y automatizaciones, así como la configuración inicial de la infraestructura. Puede encontrar más información en la [Guía del desarrollador - Mantenimiento](../../../../../developer-guide/etendo-classic/bundles/platform/task.md)


## Ventana de Mantenimiento
:material-menu: `Aplicación` > `Configuración General` > `Gestión de tareas` > `Mantenimiento`

Esta ventana muestra todos los **Mantenimiento** creados por triggers definidos en la definición de [Tipo de tarea](../../../../../developer-guide/etendo-classic/bundles/platform/task.md#task-type-window) y permite crear o gestionar tareas manualmente.
En esta ventana puede gestionar tareas. Estas tareas son genéricas y, por lo tanto, representan un concepto al que cualquier entidad puede referirse o extender según corresponda.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/task/task-window.png)
**Campos a tener en cuenta:**

- **Nº de tarea**: Identificador único autogenerado para la tarea.
- **Tipo de tarea**: Desplegable con opciones de tipo de tarea.
- **Estado**: Estados disponibles para una tarea. Los estados distribuidos son `Pendiente`, `En progreso`, `Completado` y `Cerrado` y el estado inicial por defecto es `Pendiente`.
- **Usuario asignado**: Usuario responsable de realizar la tarea.
- **Rol asignado**: Rol asociado al usuario asignado a la tarea, utilizado para el control de acceso y permisos.
- **Prioridad**: Nivel de importancia asignado a la tarea (p. ej., `Crítica`, `Mayor`, `Menor` y `Trivial`). Esto ayuda a organizar y priorizar el trabajo.
- **Fecha inicio**: La fecha en la que se espera que comience la tarea.
- **Fecha de vencimiento**: La fecha límite en la que debe completarse la tarea.
- **Activo**: Casilla de verificación para habilitar o deshabilitar esta tarea.
- **Fecha Creación**: Campo de solo lectura con la fecha y hora de creación de la tarea.

!!!note 
    Módulos específicos pueden añadir campos contextuales a la ventana de mantenimiento.

#### Solapa Registros

Esta solapa muestra un registro detallado de todos los procesos asíncronos que se han ejecutado como parte del flujo de trabajo de esta tarea. Cada entrada de registro representa una ejecución de proceso activada por transiciones de estado o eventos definidos en la configuración del tipo de tarea.

**Campos a tener en cuenta:**

- **Nivel**: Número secuencial que determina el orden de las entradas de registro para esta tarea tras la ejecución de un proceso asíncrono.
- **Definición del Proceso**: Referencia a la implementación de la definición del proceso utilizando la infraestructura Process with 3.0.
- **Organización**: La unidad organizativa asociada a la entrada de registro (p. ej., tienda, departamento). Los datos pueden compartirse entre organizaciones.
- **Activo**: Indica si el registro está activo o desactivado. Los registros desactivados no están disponibles para su selección, pero permanecen disponibles para informes.
- **Comienzo**: La marca de tiempo cuando se inició la ejecución del proceso.
- **Fin**: La marca de tiempo cuando finalizó la ejecución del proceso.
- **Mensaje**: El mensaje devuelto por la ejecución del proceso asíncrono. El formato de este mensaje puede variar dependiendo del proceso (texto/JSON/XML, etc.).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

---