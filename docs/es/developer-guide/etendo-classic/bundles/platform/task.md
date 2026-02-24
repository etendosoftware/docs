---
title: Mantenimiento - Guía del desarrollador
tags:

  - Mantenimiento
  - Mantenimientos personalizados
  - Tipo de mantenimiento
  - Estado del mantenimiento
  - Prioridad del mantenimiento
  - Debezium
  - Kafka
---

# Mantenimiento
:octicons-package-16: Paquete Java: `com.etendoerp.task`

## Visión general
Esta página explica cómo configurar y gestionar mantenimientos asíncronos y configurables en Etendo Platform. Los mantenimientos pueden activarse automáticamente en función de eventos de base de datos (como `INSERT` o `UPDATE`) y pueden ejecutar una secuencia de acciones definidas, como validaciones, notificaciones o asignaciones. Estos mantenimientos se gestionan dinámicamente mediante un conjunto de ventanas de configuración.

El sistema procesa los mantenimientos en respuesta a eventos que ocurren dentro de Etendo, como la creación de un pedido o una incidencia. En función de estos eventos, los mantenimientos se generan automáticamente, se asignan y se procesan a través de una secuencia predefinida de estados y acciones.

## Configuración inicial

### Configuración de PostgreSQL para el uso de Connect (Debezium)

```sql title="PostgreSQL"
ALTER SYSTEM SET wal_level = logical;
ALTER TABLE etask_task REPLICA IDENTITY FULL;
```

Estos comandos preparan la base de datos PostgreSQL para trabajar con **Debezium**, una herramienta para capturar cambios en tablas.

!!! warning "**El servicio de PostgreSQL debe reiniciarse** después de aplicar este cambio" 

| Comando                 | Descripción                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `wal_level = logical`   | Establece el nivel de Write-Ahead Logging (WAL) en `logical`. Esto es necesario para que Debezium transmita cambios lógicos desde la base de datos. |
| `REPLICA IDENTITY FULL` | Habilita la identidad de réplica completa en la tabla `etask_task`, permitiendo que Debezium acceda a los valores anteriores de las filas cuando se producen operaciones `UPDATE`. |

Estos comandos son **requisitos previos obligatorios** para que Debezium detecte y propague eventos a Kafka, que a su vez desencadena el procesamiento de mantenimientos en Etendo.

### Iniciar servicios RX

1. Configure las siguientes variables en `Gradle.properties` para habilitar e iniciar los servicios requeridos:

    ```groovy title="Gradle.properties"
    docker_com.etendoerp.etendorx=true
    docker_com.etendoerp.etendorx_async=true
    kafka.enable=true
    kafka.connect.bbdd.host=host.docker.internal
    kafka.connect.host=kafka
    kafka.connect.tables=public.etask_task,public.<table>
    authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
    ```

    !!! info "Notas importantes"

        - `docker_com.etendoerp.etendorx`: Habilita los servicios RX.  
        - `docker_com.etendoerp.etendorx_async`: Habilita los servicios de Kafka y Connect.  
        - `kafka.enable`: Activa el servicio de Kafka.  
        - `kafka.connect.bbdd.host`: Host de PostgreSQL. Por defecto `host.docker.internal`. Si PostgreSQL se ejecuta en un contenedor Docker en la misma red, puede usar el nombre del contenedor (p. ej., `db`) gracias al DNS interno de Docker.  
        - `kafka.connect.host`: Host de Kafka. Por defecto `kafka` cuando se ejecuta en Docker. En otros entornos, especifique el host correcto.  
        - `kafka.connect.tables`: Lista de tablas a monitorizar separadas por comas. `public.etask_task` es **Obligatorio**. Añada cualquier tabla adicional que necesite rastrear.  
        - `authentication.class`: Clase utilizada para obtener el token SWS requerido para la autenticación.  

2. Aplique la configuración ejecutando la tarea de configuración de Gradle:

    ```bash title="Terminal"
    ./gradlew setup --info 
    ```

3. Inicie los servicios Docker:

    ```bash title="Terminal"
    ./gradlew resources.up
    ```

4. Cree la conexión entre Connect y Kafka ejecutando:

    ```bash title="Terminal"
    ./gradlew kafkaConnectSetup --info
    ```

### Compilar el entorno e iniciar Tomcat


```bash title="Terminal"
./gradlew update.database compile.complete smartbuild --info 
```



## Ventana Tipo de mantenimiento
:material-menu: `Aplicación` > `Configuración General` > `Gestión de mantenimientos` > `Tipo de mantenimiento`

En esta ventana se definen los tipos de mantenimiento. En este componente se definen los eventos de base de datos que crean automáticamente un nuevo mantenimiento, la secuencia de estados que debe seguir y las acciones que se ejecutarán en cada estado. 

Un desarrollador, con el rol `System Administrator`, debe definir los tipos de mantenimiento, estados y eventos, y deben exportarse en un módulo en desarrollo.

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/platform/task/task-type.png)

**Campos a tener en cuenta:**

- **Organización**: Define el alcance de la organización.
- **Módulo**: El módulo donde se exportará este componente.
- **Identificador**: Un identificador único del tipo de mantenimiento.
- **Nombre**: Nombre legible para el tipo de mantenimiento.
- **Activo**: Casilla para habilitar o deshabilitar este tipo de mantenimiento.
- **Algoritmo de usuario**: Desplegable para seleccionar el algoritmo de asignación automática de mantenimientos. Estos algoritmos se configuran en la ventana [Ventanas Algoritmo de usuario disponible](#ventanas-algoritmo-de-usuario-disponible). Las opciones por defecto son:

    - **Algoritmo Round-Robin**: Distribuye los mantenimientos equitativamente en secuencia, sin considerar la carga de trabajo. Úselo cuando los mantenimientos y los recursos sean similares.
    - **Algoritmo Round-Robin por carga de trabajo**: Asigna los mantenimientos al recurso con la menor carga actual. Úselo cuando el tamaño de los mantenimientos o la capacidad de los recursos varíe.

### Solapa Tabla
En esta solapa se especifica la tabla observada y el evento (insert o update) que activará la creación del mantenimiento. 
Además, se pueden definir filtros opcionales (JEXL) asociados a los campos de la tabla o incluso filtros avanzados definidos como acciones. 

!!!warning
    En caso de que se definan múltiples tablas o filtros, debe asegurarse que sean mutuamente excluyentes, ya que podría crearse más de un mantenimiento por evento ocurrido.

**Campos a tener en cuenta:**

- **Módulo**: El módulo donde se exportará este componente.
- **Tabla**: La tabla de base de datos monitorizada (debe incluirse en `table.include.list` de Debezium).
- **Acción**: La acción de base de datos que desencadena el mantenimiento (`INSERT` o `UPDATE`).
- **Filtro**: Una [Expresión JEXL](https://commons.apache.org/proper/commons-jexl/reference/syntax.html){target="\_blank"} dinámica para acotar las condiciones de disparo.
- **Acción de filtro**: Validación avanzada opcional implementada como [Acción](../../how-to-guides/how-to-create-jobs-and-actions.md) de filtro.
- **Activo**: Casilla para habilitar o deshabilitar este disparador de tabla.

### Solapa Estado
Define el ciclo de vida del mantenimiento listando los posibles estados (p. ej., Pendiente, En progreso, Cerrado) en una secuencia específica. 
Cuando se crea un mantenimiento, se le asigna el **primer estado** de la secuencia. Asignar o cambiar el estado de un mantenimiento desencadena los **eventos** definidos en la siguiente subsolapa.

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/platform/task/status-events-tab.png)

**Campos a tener en cuenta:**

- **Módulo**: El módulo donde se exportará este componente.
- **Nivel**: Se utiliza para determinar el orden de los estados y para determinar cuál es el estado inicial cuando se crean los mantenimientos.
- **Estado**: Desplegable de estados reutilizables definidos en la ventana [Ventana Estado del mantenimiento](#ventana-estado-del-mantenimiento).
- **Activo**: Casilla para habilitar o deshabilitar este estado.

#### Subsolapa Eventos

Esta solapa define jobs asíncronos que se ejecutan automáticamente cuando el mantenimiento entra en un estado específico. Los jobs pueden publicar mensajes en topics de Kafka como parte del flujo de trabajo.

- **Módulo**: El módulo donde se exportará este componente.
- **Nivel**: Determina el orden de encolado, aunque al ser procesos asíncronos pueden ejecutarse en paralelo.
- **Job**: Referencia al job que se ejecutará (debería configurarse como asíncrono); para más información, consulte la documentación de [Jobs asíncronos]().
- **Activo**: Casilla para habilitar o deshabilitar este evento.


## Ventana Estado del mantenimiento
:material-menu: `Aplicación` > `Configuración General` > `Gestión de mantenimientos` > `Estado del mantenimiento`

Esta ventana le permite crear estados reutilizables para tipos de mantenimiento. Los valores por defecto incluyen `Pendiente`, `En progreso`, `Completada` y `Cerrado`. Los desarrolladores con el rol `System Administrator` pueden añadir estados personalizados y exportarlos en un módulo en desarrollo. En la ventana Tipo de mantenimiento se utilizan estos estados, permitiendo al motor de flujo de trabajo rastrear y desencadenar transiciones de estado y eventos asociados (incluidas notificaciones de Kafka).

![](../../../../assets/developer-guide/etendo-classic/bundles/platform/task/task-status-windows.png)

**Campos a tener en cuenta:**

- **Módulo**: El módulo donde se exportará este componente.
- **Identificador**: Un identificador único para el estado.
- **Nombre**: El nombre visible que se mostrará al usar este estado.
- **Descripción**: Descripción opcional del estado.
- **Activo**: Casilla para habilitar o deshabilitar este estado.

## Ventana Prioridad del mantenimiento
:material-menu: `Aplicación` > `Configuración General` > `Gestión de mantenimientos` > `Prioridad del mantenimiento`

Esta ventana le permite crear prioridades reutilizables para mantenimientos. Las prioridades ayudan a organizar y categorizar los mantenimientos por nivel de importancia. Los desarrolladores con el rol `System Administrator` pueden añadir prioridades personalizadas y exportarlas en un módulo en desarrollo. Estas prioridades pueden asignarse a los mantenimientos para indicar su importancia relativa.

![](../../../../assets/developer-guide/etendo-classic/bundles/platform/task/task-priority-windows.png)

**Campos a tener en cuenta:**

- **Módulo**: El módulo donde se exportará este componente.
- **Identificador**: Un identificador único para la prioridad.
- **Nombre**: El nombre visible que se mostrará al usar esta prioridad.
- **Descripción**: Descripción opcional de la prioridad.
- **Secuencia**: Valor numérico que determina el orden o el peso de la prioridad (p. ej., 20).
- **Color (Hex)**: Código de color hexadecimal para la identificación visual de la prioridad en la interfaz (p. ej., `#F57C00`).
- **Activo**: Casilla para habilitar o deshabilitar esta prioridad.

## Ventanas Algoritmo de usuario disponible
:material-menu: `Aplicación` > `Configuración General` > `Gestión de mantenimientos` > `Algoritmo de usuario disponible`

En esta ventana, puede configurar los diferentes algoritmos que permiten determinar la disponibilidad de usuarios para la asignación del mantenimiento.

Solo es necesario definir un nombre y la ruta Java donde se encuentra la implementación del algoritmo. Esta implementación debe extender la interfaz `UserAvailabilityStrategy`.

![available-user-algorithm](../../../../assets/developer-guide/etendo-classic/bundles/platform/task/available-user-algorithm.png)

**Campos a tener en cuenta:**

- **Módulo**: El módulo donde se exportará este componente.
- **Nombre**: El nombre visible que se mostrará al usar este algoritmo.
- **Implementación Java**: Ruta del archivo Java donde se encuentra la implementación del algoritmo; esta implementación debe extender la interfaz `UserAvailabilityStrategy`.
- **Activo**: Casilla para habilitar o deshabilitar este algoritmo.


## Flujo de trabajo de ejemplo

Si revisa la documentación de las diferentes ventanas, puede ver que se está siguiendo un ejemplo de cómo usar los mantenimientos.
La idea es que, una vez configurado este tipo de mantenimiento, cuando se complete el primer pedido de venta de un tercero con la casilla International marcada, se cree un nuevo mantenimiento en estado pendiente. Se asocia automáticamente a un usuario usando el algoritmo definido.
Cuando se crea el mantenimiento, se dispara el Evento asociado al estado inicial del mantenimiento **Pendiente**; este evento lanza un job encargado de marcar al cliente como asociado al programa de fidelización.  
Luego, asumiendo que el usuario asignado para hacer el seguimiento de este cliente (agente de ventas) determina que el cliente ya ha facturado lo suficiente, puede mover el mantenimiento al estado **en progreso** y la automatización lo marca automáticamente como cliente **Gold**.

Ahora revisaremos la configuración:

1. En la configuración de ejemplo mostrada en esta documentación, definimos un nuevo tipo de mantenimiento llamado `Business Partner Management` y asignamos el `Algoritmo Round-Robin` para la asignación de usuario.
2. Como podemos ver en la solapa **Tabla**, está configurado para detectar la acción `UPDATE` en la tabla `c_order`, filtrando solo cuando un **Pedido de venta** está **Completada**.
3. Se configuran dos estados, **Pendiente** y **En progreso** en ese orden, lo que significa que cuando se crea un nuevo mantenimiento se le asignará automáticamente el estado `Pendiente`.
4. Se seleccionan dos jobs en la subsolapa **Eventos**, **Establecer tercero como programa de fidelización** cuando el mantenimiento está `pendiente`, y **Establecer tercero como Gold** cuando el mantenimiento está `En progreso`, respectivamente.

!!! info
    En la sección [Mantenimiento - Guía de usuario](../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/task.md) puede ver cómo los mantenimientos se crean automáticamente, se asignan a usuarios y cómo cambiar su estado desde la ventana con el mismo nombre.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.