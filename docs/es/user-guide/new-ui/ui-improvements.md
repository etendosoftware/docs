---
title: Mejoras de la interfaz de usuario
tags:
    - Nueva UI
    - Mejoras
status: new
---

# Mejoras de la interfaz de usuario { #user-interface-improvements }

## Visión general { #overview }

Esta sección detalla las mejoras de la interfaz de usuario disponibles en la **Nueva UI de Etendo**.

## Mejoras y ampliaciones de la UI de Etendo { #etendo-ui-improvements-and-enhancements }

### Formato regional de fechas { #regional-date-formatting }

Todas las fechas mostradas en la interfaz de usuario ahora se adaptan automáticamente a la configuración regional de su navegador. Esto proporciona una vista personalizada y localizada de la información de fechas, haciendo que la interfaz sea más intuitiva y fácil de leer para usuarios de distintas regiones.

!!! warning

    Este formato regional se aplica exclusivamente a la capa de visualización de la interfaz de usuario. El procesamiento de datos subyacente sigue estas reglas:

    - **Visualización/Vista:** las fechas se formatean según la configuración regional de su navegador
    - **Operaciones de backend:** los valores de fecha se procesan y almacenan usando la configuración especificada en `gradle.properties`
    - **Las fechas se muestran automáticamente en su formato regional preferido** sin configuración manual.

**Ejemplo de UI clásica de Etendo**

<figure markdown="span">
    ![Formato de fecha en Etendo Classic](../../assets/user-guide/newui/classic-date-1.png)
    <figcaption>UI clásica de Etendo: las fechas en la UI clásica de Etendo se muestran en el formato estándar configurado en el sistema.
    </figcaption>
</figure>

**Ejemplo de UI de Etendo con configuración regional (en-US):**

<figure markdown="span">
    ![Formato de fecha en la Nueva UI con configuración regional](../../assets/user-guide/newui/newui-date-1.png)
    <figcaption>UI de Etendo: en la UI de Etendo, la misma tabla muestra las fechas formateadas automáticamente. En este ejemplo se aplica `en-US` (Estados Unidos), por lo que las fechas aparecen en formato `MM/DD/YYYY`. </figcaption>
</figure>

### Gestión de adjuntos { #attachment-management }

La **UI de Etendo** introduce un sistema de gestión de adjuntos completamente rediseñado que proporciona una forma más ágil, visual e integral de gestionar archivos adjuntos, tanto desde la **vista de formulario** como directamente desde los **registros de la cuadrícula**.

#### Sección de adjuntos en la vista de formulario { #attachments-section-in-form-view }

La sección de adjuntos se ha rediseñado para ser más intuitiva. Los archivos ahora se muestran como etiquetas o chips, lo que permite una identificación rápida.

![Sección de adjuntos expandida](../../assets/user-guide/newui/attachment-section-expanded-1.png)

**Carga de archivos**

![Vista previa del modal de carga](../../assets/user-guide/newui/upload-modal-preview-1.png){align=right width=300}

Hay dos formas principales de cargar archivos dentro de un registro:

1. **Arrastrar y soltar:** arrastre uno o varios archivos directamente desde su equipo a la **zona de suelta** punteada en la sección de adjuntos.

    !!! note
        Al soltar el archivo, se abrirá un modal de confirmación donde puede verificar el archivo seleccionado y añadir una descripción opcional antes de cargarlo.

2. **Explorador de archivos:** haga clic en la zona de carga (o en el icono de carga) para abrir el selector de archivos de su sistema operativo.

#### Vista previa y edición rápida { #preview-and-quick-edit }

![Modal de carga con archivo](../../assets/user-guide/newui/upload-modal-with-file-1.png){align=right width=300}

Al hacer clic en el nombre de cualquier adjunto cargado, se abrirá una ventana de vista previa avanzada.

**Funcionalidades dentro de la vista previa:**

- **Visor integrado:** visualice imágenes y documentos PDF directamente sin necesidad de descargarlos.
- **Edición de la descripción:** puede modificar la descripción del archivo _in situ_. Haga clic en el icono de **lápiz**, edite el texto y guarde los cambios con el icono de **Comprobación**, todo sin salir de la vista previa.
- **Gestión individual:** botones dedicados para **Descargar** o **Eliminar** el archivo que está visualizando.

#### Acciones masivas de adjuntos { #attachments-bulk-actions }

![Acciones masivas](../../assets/user-guide/newui/bulk-actions-1.png)

Para facilitar la gestión de múltiples archivos, se han incorporado botones de acción global en el encabezado de la sección de adjuntos:

- **Descargar todo:** genera y descarga un archivo comprimido (`.zip`) que contiene todos los adjuntos asociados al registro.
- **Eliminar todo:** permite eliminar todos los adjuntos del registro en un solo paso (requiere confirmación de seguridad).

#### Carga rápida desde la cuadrícula (arrastrar y soltar en filas) { #quick-upload-from-grid-drag-drop-on-rows }

Es posible adjuntar archivos sin necesidad de entrar en cada registro. Desde la vista principal de la cuadrícula:

![](../../assets/user-guide/newui/drop-file-in-grid-1.gif)

### Filtro Avanzado { #advanced-filters }

![](../../assets/user-guide/newui/advanced-filters-modal.png)

El modal de **Filtro Avanzado** es un componente de filtrado potente que permite a los usuarios crear filtros complejos de múltiples condiciones directamente desde la interfaz de la cuadrícula. Proporciona una forma intuitiva de construir consultas sofisticadas usando operadores lógicos y múltiples grupos de filtros.

!!! info "Funcionalidades clave"
    - **Múltiples tipos de filtro:** compatibilidad con campos de tipo cadena, número, fecha, booleano y selección.
    - **Operadores lógicos:** combine condiciones usando operadores AND/OR.
    - **Grupos de filtros:** anide múltiples condiciones dentro de grupos para una lógica de consulta compleja.
    - **Operadores dinámicos:** los operadores disponibles cambian según el tipo de campo seleccionado.
    - **Añadir/eliminar condiciones:** añada o elimine dinámicamente condiciones de filtro individuales.
    - **Añadir/eliminar grupos:** cree grupos de filtros anidados para organizar lógica compleja.
    - **Borrar todo:** restablezca todos los filtros para empezar de nuevo.
    - **Aplicar/validación:** solo se aplican condiciones válidas (con columna, operador y valor).

#### Operadores compatibles por tipo de campo { #supported-operators-by-field-type }

| Tipo de campo | Operadores compatibles |
|-----------|---------------------|
| **Cadena** | - `=` Igual<br> - `≠` Distinto<br>Contiene<br>No contiene<br>Empieza por<br>Termina en<br>Está vacío<br>No está vacío |
| **Número** | `=` Igual<br>`≠` Distinto<br>`>` Mayor que<br>`<` Menor que<br>`≥` Mayor o igual<br>`≤` Menor o igual |
| **Fecha** | `=` Igual<br>`≠` Distinto<br>Antes de<br>Después de<br>Hoy<br>Esta semana<br>Este mes |
| **Booleano** | sí<br>no |
| **Selección (desplegable)** | `=` Igual<br>`≠` Distinto |

#### Uso del Filtro Avanzado { #using-the-advanced-filters }

1. **Haga clic en el icono de filtro** en el encabezado de la cuadrícula para abrir el modal de Filtro Avanzado.
2. **Seleccione una columna** en el desplegable de la primera fila de filtro.
3. **Elija un operador** adecuado para el tipo de campo.
4. **Introduzca o seleccione un valor** según el tipo de operador.
5. **Añada más condiciones** haciendo clic en el botón *Añadir condición*.
6. **Cree grupos de filtros** para lógica compleja usando el botón *Añadir grupo*.
7. **Revise sus filtros**: el estado muestra el número de filtros activos.
8. **Haga clic en el botón Aplicar filtros** para ejecutar la consulta.
9. **Limpie los filtros** haciendo clic en el botón *Borrar todo* para restablecer y empezar de nuevo.

#### Escenarios de ejemplo { #example-scenarios }

<figure markdown="span">
    ![Ejemplo 1 de Filtro Avanzado](../../assets/user-guide/newui/advanced-filters-modal-1-example.png)
    <figcaption>Ejemplo 1: filtro simple con una condición seleccionando una organización específica.</figcaption>
</figure>

<figure markdown="span">
    ![Ejemplo 2 de Filtro Avanzado](../../assets/user-guide/newui/advanced-filters-modal-2-example.png)
    <figcaption>Ejemplo 2: múltiples condiciones combinadas con lógica AND para acotar los resultados de búsqueda.</figcaption>
</figure>

<figure markdown="span">
    ![Ejemplo 3 de Filtro Avanzado](../../assets/user-guide/newui/advanced-filters-modal-3-example.png)
    <figcaption>Ejemplo 3: filtro complejo con una condición agrupada. El filtro principal comprueba si el estado del documento es contabilizado, Y el grupo comprueba si el importe bruto total es mayor que 10 Y menor que 100.</figcaption>
</figure>

### Vistas guardadas { #saved-views }

Desde el toolbar de cualquier grilla o tabla, los usuarios pueden acceder al menú **Guardar vista** para persistir y gestionar configuraciones personalizadas de la grilla.

![Vistas guardadas](../../assets/user-guide/newui/saved-views.png)

!!! info "Funcionalidades clave"
    - **Guardar vista actual:** captura el estado completo de la grilla — filtros aplicados, columnas visibles, orden de columnas y ordenamiento — con un nombre personalizado (máx. 100 caracteres). La configuración se persiste en el backend.
    - **Aplicar vistas guardadas:** al abrir el menú se muestran todas las vistas disponibles para el tab actual. Un clic aplica instantáneamente toda la configuración guardada.
    - **Marcar como predeterminada:** cualquier vista puede marcarse como predeterminada mediante el icono de estrella. La vista predeterminada se carga automáticamente cada vez que se abre ese tab. Solo se permite una vista predeterminada por tab.
    - **Restablecer a estándar:** restaura el estado original de la grilla sin filtros ni configuración personalizada.
    - **Eliminar vistas:** al pasar el cursor sobre una vista se muestra un botón de eliminar con confirmación.

### Dashboard configurable con Widgets { #configurable-dashboard-with-widgets }

La pantalla de inicio se ha rediseñado como un dashboard completamente configurable donde los usuarios pueden agregar, eliminar y reorganizar widgets.

![Vista general del dashboard](../../assets/user-guide/newui/dashboard-overview.png)

#### Gestión del dashboard { #dashboard-management }

- Grilla responsiva de widgets con **arrastrar y soltar** para reposicionar.
- Botón **Agregar Widget** que abre un diálogo con los tipos de widgets disponibles.
- Cada widget tiene un botón de eliminar (**X**), y algunos incluyen una opción de **Editar parámetros** para personalizar sus datos.

![Diálogo de agregar widget](../../assets/user-guide/newui/dashboard-add-widget.png)

#### Tipos de widgets disponibles { #available-widget-types }

| Widget | Descripción |
|--------|-------------|
| **KPI** | Muestra un valor numérico grande con unidad, etiqueta e indicador de tendencia (verde para positivo, rojo para negativo). |
| **Calendario** | Interfaz de calendario con eventos programados. |
| **Proceso** | Información sobre procesos y flujos de trabajo. |
| **Lista de consulta** | Tabla con paginación, columnas ordenables y navegación click-through a la ventana relacionada. |
| **HTML** | Contenido HTML personalizado. |
| **URL** | Contenido externo embebido mediante iframe. |
| **Alerta de stock** | Alertas de inventario con indicadores de estado. |
| **Notificación** | Notificaciones y mensajes. |
| **Favoritos** | Ventanas favoritas mostradas como chips clickeables (ver abajo). |
| **Vistos recientemente** | Documentos vistos recientemente. |
| **Documentos recientes** | Actividad reciente de documentos. |

#### Widget de Favoritos { #favorites-widget }

Un widget dedicado que muestra todas las ventanas favoritas del usuario como chips compactos y clickeables.

![Widget de Favoritos](../../assets/user-guide/newui/dashboard-favorites-widget.png)

- Al hacer clic en cualquier chip se abre esa ventana en un nuevo tab.
- El widget se actualiza en tiempo real cuando el usuario marca o desmarca favoritos desde cualquier parte de la UI (icono de estrella en el sidebar).

![Estrella de Favoritos](../../assets/user-guide/newui/dashboard-favorites-star.png)
- Muestra un guion (**—**) como estado vacío si no hay favoritos configurados.

!!! note
    El concepto de widget de Favoritos no existe en Etendo Classic. Es una funcionalidad exclusiva de la UI de Etendo.

### Email desde Toolbar { #email-from-toolbar }

Un modal de envío de email accesible desde el toolbar, que permite a los usuarios componer y enviar correos electrónicos directamente desde el contexto del registro actual.

![Modal de email](../../assets/user-guide/newui/email-modal.png)

#### Campos del formulario { #form-fields }

| Campo | Detalles |
|-------|----------|
| **Para** (obligatorio) | Dirección del destinatario, pre-cargada desde el contexto del registro actual. |
| **CCO** | Copia oculta. |
| **Responder a** | Dirección de respuesta. |
| **CC** | Copia de carbón, disponible bajo **Mostrar más campos**. |
| **Asunto** (obligatorio) | Línea de asunto del email. |
| **Cuerpo** | Área de texto con un panel de referencia que muestra los tokens de plantilla disponibles. |

#### Tokens de plantilla { #template-tokens }

El campo de cuerpo proporciona un panel de referencia con los tokens disponibles que se reemplazan dinámicamente al enviar el email:

`@cus_ref@`, `@our_ref@`, `@cus_nam@`, `@sal_nam@`, `@bp_nam@`, `@doc_date@`, `@doc_desc@`, `@doc_nextduedate@`, `@doc_lastduedate@`

#### Plantillas { #templates }

Un selector desplegable permite elegir plantillas predefinidas que auto-completan el cuerpo y otros campos.

#### Adjuntos { #email-attachments }

La sección de adjuntos muestra archivos de reporte, adjuntos del registro y archivos subidos en una tabla. Los usuarios pueden:

- Agregar archivos locales desde su equipo.
- Cargar adjuntos asociados al registro desde la base de datos.
- Activar la casilla de **Archivar** en archivos de reporte.
- Eliminar adjuntos individuales mediante el botón **X**.

### Selector de imagen { #image-selector }

Los campos de imagen en formularios ahora cuentan con un flujo completo de carga, vista previa y edición.

![Campos de selector de imagen](../../assets/user-guide/newui/image-selector-fields.png)

#### Carga { #image-upload }

![Diálogo de carga de imagen](../../assets/user-guide/newui/image-upload-dialog.png)

- Al hacer clic en un campo de imagen se abre un diálogo de carga.
- Soporta **arrastrar y soltar** o selección de archivo.
- Valida las dimensiones de la imagen contra las restricciones configuradas (mínimo/máximo).

!!! warning "Validación de dimensiones"
    - Si se violan restricciones obligatorias, se muestra un **error** con las dimensiones actuales vs. las requeridas.
    - Si las restricciones son recomendadas, un **diálogo de confirmación** permite al usuario continuar o cancelar.
    - Se puede aplicar un **redimensionamiento automático** opcional, con una confirmación que muestra las dimensiones original y final.

#### Vista previa y edición { #image-preview-and-editing }

![Modal de vista previa de imagen](../../assets/user-guide/newui/image-preview-modal.png)

- La imagen cargada aparece como una **miniatura** en el formulario.
- Al hacer clic en la miniatura se abre un **modal de vista previa a pantalla completa**.
- En el modal de vista previa:
    - **Zoom** con la rueda del mouse (0.5x a 5x).
    - **Arrastrar** para panear por la imagen.
    - Botón de **restablecer zoom** para volver a la vista predeterminada.
    - **Re-cargar** para reemplazar la imagen actual.
    - **Eliminar** con confirmación.

### Atajos de teclado { #keyboard-shortcuts }

Un sistema centralizado de atajos de teclado para acciones comunes en la UI de Etendo.

| Atajo | Acción |
|-------|--------|
| `Arrow Up` / `Arrow Down` | Navegar entre filas de la tabla sin usar el mouse. |
| `Ctrl + S` | Guardar el registro actual. |
| `Ctrl + N` | Crear un nuevo registro. |

!!! info "Detalles de comportamiento"
    - Los atajos **no se activan** cuando el foco está en campos de entrada, áreas de texto o desplegables (salvo configuración explícita).
    - Se **previene el comportamiento predeterminado** del navegador (ej: `Ctrl + S` no abre el diálogo "Guardar página" del navegador).
    - Los atajos son **sensibles al contexto**: solo se disparan dentro de la región de UI apropiada.

### Sistema de foco y guardado previo { #focus-system-and-prior-saving }

Un sistema automático de gestión de estado que maneja los cambios no guardados al cambiar entre tabs o ventanas.

![Sistema de foco](../../assets/user-guide/newui/focus-system.png)

- Al cambiar de tab o ventana, los **cambios no guardados** del área previamente enfocada se **guardan automáticamente** (de forma asíncrona).
- El sistema rastrea qué tab o ventana está activo actualmente.
- Los tabs en segundo plano **mantienen su estado**, permitiendo cambios instantáneos sin pérdida de datos.
- Los usuarios pueden navegar libremente entre tabs abiertos sin perder trabajo en curso; la navegación es fluida y los datos se mantienen consistentes.

### Navegación con teclas de dirección en tablas { #arrow-key-navigation-in-tables }

Navegación mejorada por teclado en las filas de tabla usando las teclas de dirección.

- `Arrow Up`: mueve la selección a la fila anterior.
- `Arrow Down`: mueve la selección a la fila siguiente.
- La navegación **se detiene en los límites de la tabla** — no pasa de la primera ni la última fila.
- Solo funciona cuando hay una **única fila seleccionada**.
- Pulsaciones rápidas avanzan filas de forma fluida (con debounce para evitar lag).
- **Deshabilitado en modo edición**.
- El sistema distingue entre navegación por teclado y clic de mouse para optimizar el rendimiento.

### Agentes destacados en Copilot { #featured-agents-in-copilot }

En el selector de asistentes del Copilot:

- Sección **Agentes destacados**: ciertos agentes aparecen resaltados en la parte superior de la lista, visualmente distinguidos con un badge o estilo especial que indica que son recomendados.
- Sección **Agentes regulares**: los agentes no destacados aparecen debajo.
- Esta organización ayuda a los usuarios a encontrar rápidamente los asistentes más útiles sin necesidad de recorrer toda la lista.

### Mejoras en el chat de Copilot { #copilot-chat-improvements }

La experiencia de chat del Copilot se ha mejorado con varias mejoras de usabilidad:

!!! info "Funcionalidades clave"
    - **Lista de conversaciones:** sidebar con el historial de conversaciones pasadas.
    - **Archivar/eliminar:** las conversaciones se pueden archivar o eliminar.
    - **Nueva conversación:** botón para iniciar una conversación nueva.
    - **Buscar conversaciones:** búsqueda en el historial de conversaciones.
    - **Renombrar conversaciones:** títulos editables para mejor organización.
    - **UI mejorada:** mejor formateo de mensajes, espaciado y jerarquía visual.
    - **Estados claros:** indicadores de estado vacío, carga y error.
    - **Streaming:** las respuestas se muestran en tiempo real mientras el agente las genera.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"} by [Futit Services S.L](https://etendo.software){target="\_blank"}.