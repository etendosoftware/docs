---
title: Configuración de Proyectos y Servicios
tags: 
    - Proyecto multifase
    - Tipo de proyecto
    - Configuración
    - Plantilla de proyecto
---
# Configuración de Proyectos y Servicios

## Visión general

Esta sección describe la ventana que se utiliza para configurar el proceso de Gestión de Proyectos y Servicios en Etendo: Tipo de proyecto.

## Tipo de proyecto

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Configuración` > `Tipo de proyecto`

### Visión general

Esta ventana se utiliza para definir tipos de proyecto con fases y tareas típicas que se utilizarán en los proyectos.

Un Tipo de proyecto es una plantilla con las fases y tareas típicas que son aplicables a un determinado tipo de proyecto. Durante la introducción de un proyecto multifase, se puede seleccionar un tipo de proyecto para añadir automáticamente las fases y tareas asociadas a ese tipo de proyecto. Esto es esencial para las empresas que utilizan los mismos procesos estándar en muchas ocasiones.

!!!info 
    El uso de esta ventana no es obligatorio, pero se recomienda, ya que permite completar el proyecto multifase de una manera más sencilla. Si no se utiliza, cada proyecto multifase, sus fases y tareas, deberán completarse manualmente.

### Cabecera

Aquí se puede definir un tipo de proyecto y, para ello, el campo principal es el Nombre del tipo de proyecto. Se debe asignar un nombre intuitivo para que, una vez introducido el proyecto multifase, el usuario pueda reconocer fácilmente el tipo de proyecto que podría utilizarse para generar las fases y tareas.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/setup/project-type.png)

### Pestaña de fase estándar

En esta pestaña, el usuario puede definir las fases y los productos requeridos durante cada fase, para incluirlos en este tipo. Cada fase se añade creando una línea.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/setup/standard-phase.png)

Los campos de esta pestaña son:

- Número de secuencia: numeración de las líneas introducidas. Por defecto 10,20,30,..etc.
- Nombre: nombre de la fase.
- Producto: producto o servicio que se vende en la fase.
- Cantidad estándar: cantidad del producto que se venderá en la fase. Por ejemplo, si el producto es Consultoría de ventas con una unidad de medida establecida en horas, la cantidad 10 introducida en este campo indica que se venden 10 horas de Consultoría de ventas en esta fase.
- Duración estándar en días: la duración planificada de la fase. En base a esta configuración, cuando el tipo de proyecto se utiliza para un proyecto multifase, las fechas de inicio y fin de cada fase se basan en esta configuración. Si se deja en blanco a nivel de fase, la fecha de inicio se completará en base a la fecha de inicio del proyecto y la fecha de fin se dejará en blanco.
- Casilla de verificación Activo: indicación de validez de la línea.
- Descripción: campo de notas para la fase.

### Subpestaña de tarea estándar

Aquí, el usuario puede definir las tareas que se deben completar durante cada fase. Cada tarea se añade creando una línea.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/setup/standard-task.png)

Los campos de las tareas son:

- Número de secuencia: numeración de las líneas introducidas. Por defecto 10,20,30,..etc.
- Nombre: nombre de la tarea.
- Producto: producto o servicio que se vende relacionado con esta tarea.
- Cantidad estándar: cantidad del producto que se venderá para la tarea. Por ejemplo, si el producto es Consultoría de ventas con una unidad de medida establecida en horas, la cantidad 10 introducida en este campo indica que se venden 10 horas de Consultoría de ventas relacionadas con esta tarea.
- Duración estándar en días: la duración planificada de la tarea.
- Casilla de verificación Activo: indicación de validez de la línea.
- Descripción: campo de notas para la fase.

---

Este trabajo es una obra derivada de [Gestión de Proyectos y Servicios](https://wiki.openbravo.com/wiki/Project_and_Service_Management){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.