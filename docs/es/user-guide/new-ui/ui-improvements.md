---
title: Mejoras de la interfaz de usuario
tags:
    - Nueva UI
    - Mejoras
    - Etendo
    - Interfaz de usuario
    - Copilot
status: new
---

# Mejoras de la interfaz de usuario { #user-interface-improvements }

## Descripción general { #overview }

Esta página documenta las mejoras de la interfaz de usuario disponibles en la **Etendo New UI**. Cada sección describe una funcionalidad específica, su comportamiento y cómo utilizarla.

## Formato de fecha regional { #regional-date-formatting }

Todas las fechas que se muestran en la interfaz de usuario se adaptan automáticamente a la configuración regional del navegador del usuario. Esto ofrece a cada usuario una vista localizada de la información de fechas sin necesidad de configuración manual.

!!! warning

    **Nota para administradores:** El formato de fecha que se muestra en pantalla está controlado por la configuración del navegador. El formato utilizado para almacenar datos en el sistema lo configura por separado el administrador del sistema. Si observa una discrepancia entre lo que ve y lo que está almacenado, contacte con su administrador — los usuarios estándar no necesitan realizar ninguna acción.

**Ejemplo de la UI clásica de Etendo**

<figure markdown="span">
    ![Formato de fecha en Etendo Classic](../../assets/user-guide/newui/classic-date-1.png)
    <figcaption>UI clásica de Etendo: las fechas se muestran en el formato estándar configurado en el sistema.</figcaption>
</figure>

**Ejemplo de la Etendo New UI con configuración regional (en-US):**

<figure markdown="span">
    ![Formato de fecha en la New UI con configuración regional](../../assets/user-guide/newui/newui-date-1.png)
    <figcaption>Etendo New UI: la misma tabla muestra las fechas formateadas automáticamente. En este ejemplo se aplica `en-US` (Estados Unidos), por lo que las fechas aparecen en formato `MM/DD/YYYY`.</figcaption>
</figure>

## Gestión de archivos adjuntos { #attachment-management }

La **Etendo New UI** presenta un sistema de gestión de archivos adjuntos completamente rediseñado. Ofrece una forma más ágil, visual e integral de gestionar adjuntos, tanto desde la **vista de formulario** como directamente desde los **registros de la grilla**.

**Sección de adjuntos en la vista de formulario**

La sección de adjuntos se ha rediseñado para ser más intuitiva. Los archivos se muestran como etiquetas o chips, lo que permite identificarlos rápidamente.

<figure markdown="span">
    ![Sección de adjuntos expandida](../../assets/user-guide/newui/attachment-section-expanded-1.png)
    <figcaption>La sección de adjuntos en la vista de formulario, mostrando los archivos como chips para una identificación rápida.</figcaption>
</figure>

**Carga de archivos**

![Vista previa del modal de carga](../../assets/user-guide/newui/upload-modal-preview-1.png){align=right width=300}

Hay dos formas principales de cargar archivos dentro de un registro:

1. **Arrastrar y soltar:** arrastre uno o varios archivos directamente desde su equipo a la **Drop Zone** punteada en la sección de adjuntos.

    !!! note
        Al soltar el archivo, se abre un modal de confirmación. Verifique el archivo seleccionado y añada una descripción opcional antes de cargarlo.

2. **Explorador de archivos:** haga clic en la zona de carga (o en el icono de carga) para abrir el selector de archivos de su sistema operativo.

**Vista previa y edición rápida**

![Modal de carga con archivo](../../assets/user-guide/newui/upload-modal-with-file-1.png){align=right width=300}

Haga clic en el nombre de cualquier adjunto cargado para abrir una ventana de vista previa avanzada.

Funciones disponibles en la vista previa:

- **Visor integrado:** visualice imágenes y documentos PDF directamente sin necesidad de descargarlos.
- **Edición de la descripción:** modifique la descripción del archivo en el momento. Haga clic en el icono de **lápiz**, edite el texto y guárdelo con el icono de **verificación** — todo sin salir de la vista previa.
- **Gestión individual:** botones dedicados para **Descargar** o **Eliminar** el archivo que está visualizando.

**Acciones masivas sobre adjuntos**

<figure markdown="span">
    ![Acciones masivas](../../assets/user-guide/newui/bulk-actions-1.png)
    <figcaption>Botones de acción global en el encabezado de la sección de adjuntos para gestionar múltiples archivos a la vez.</figcaption>
</figure>

Los botones de acción global en el encabezado de la sección de adjuntos permiten gestionar múltiples archivos a la vez:

- **Descargar todo:** genera y descarga un archivo comprimido (`.zip`) que contiene todos los adjuntos asociados al registro.
- **Eliminar todo:** elimina todos los adjuntos del registro en un solo paso (requiere confirmación de seguridad).

**Carga rápida desde la grilla (arrastrar y soltar en filas)**

Adjunte archivos sin necesidad de abrir cada registro individualmente. Desde la vista principal de la grilla, arrastre y suelte archivos directamente sobre cualquier fila.

<figure markdown="span">
    ![Carga rápida desde la grilla](../../assets/user-guide/newui/drop-file-in-grid-1.gif)
    <figcaption>Arrastrar y soltar un archivo directamente sobre una fila de la grilla para adjuntarlo a ese registro.</figcaption>
</figure>

## Filtros avanzados { #advanced-filters }

<figure markdown="span">
    ![Modal de Advanced Filters](../../assets/user-guide/newui/advanced-filters-modal.png)
    <figcaption>El modal de Advanced Filters, que muestra los grupos de filtros y los selectores de operadores lógicos.</figcaption>
</figure>

El modal de **Advanced Filters** es un componente de filtrado potente. Permite crear filtros complejos de múltiples condiciones directamente desde la interfaz de la grilla, mediante operadores lógicos y múltiples grupos de filtros.

### Operadores compatibles por tipo de campo { #supported-operators-by-field-type }

| Tipo de campo | Operadores compatibles |
|--------------|------------------------|
| **Cadena** | `=` Igual<br>`≠` Distinto<br>Contiene<br>No contiene<br>Empieza por<br>Termina en<br>Está vacío<br>No está vacío |
| **Número** | `=` Igual<br>`≠` Distinto<br>`>` Mayor que<br>`<` Menor que<br>`≥` Mayor o igual<br>`≤` Menor o igual |
| **Fecha** | `=` Igual<br>`≠` Distinto<br>Antes de<br>Después de<br>Hoy<br>Esta semana<br>Este mes |
| **Booleano** | sí<br>no |
| **Selección (desplegable)** | `=` Igual<br>`≠` Distinto |

El panel de Advanced Filters permite combinar múltiples condiciones de búsqueda — por ejemplo, mostrar solo las facturas de un cliente específico que además estén vencidas. Es posible agrupar condiciones y elegir si todas deben cumplirse (AND) o basta con que se cumpla alguna (OR).

**Uso de los Advanced Filters**

1. Haga clic en el **icono de filtro** en el encabezado de la grilla para abrir el modal de Advanced Filters.
2. Seleccione una columna en el desplegable de la primera fila de filtro.
3. Elija un operador adecuado para el tipo de campo.
4. Introduzca o seleccione un valor según el tipo de operador.
5. Añada más condiciones haciendo clic en **Add Condition**.
6. Cree grupos de filtros para lógica compleja usando **Add Group**.
7. Revise sus filtros — el indicador de estado muestra el número de filtros activos.
8. Haga clic en **Apply Filters** para ejecutar la consulta.
9. Haga clic en **Clear All** para restablecer todos los filtros y empezar de nuevo.

**Ejemplos de escenarios**

<figure markdown="span">
    ![Ejemplo 1 de Advanced Filters](../../assets/user-guide/newui/advanced-filters-modal-1-example.png)
    <figcaption>Ejemplo 1: filtro simple con una condición que selecciona una organización específica.</figcaption>
</figure>

<figure markdown="span">
    ![Ejemplo 2 de Advanced Filters](../../assets/user-guide/newui/advanced-filters-modal-2-example.png)
    <figcaption>Ejemplo 2: múltiples condiciones combinadas con lógica AND para acotar los resultados de búsqueda.</figcaption>
</figure>

<figure markdown="span">
    ![Ejemplo 3 de Advanced Filters](../../assets/user-guide/newui/advanced-filters-modal-3-example.png)
    <figcaption>Ejemplo 3: filtro complejo con una condición agrupada. El filtro principal comprueba si el Estado doc. es Registrado, y el grupo comprueba si el Importe bruto total es mayor que 10 y menor que 100.</figcaption>
</figure>

## Vistas guardadas { #saved-views }

Una vista guardada registra la configuración preferida del usuario para cualquier tabla — qué columnas son visibles, cómo están ordenadas y qué filtros se han aplicado. Al abrir una vista guardada se restaura la configuración completa con un solo clic. Para crear o gestionar vistas, abra el menú **Save View** desde la barra de herramientas en la parte superior de cualquier tabla.

<figure markdown="span">
  ![Vistas guardadas](../../assets/user-guide/newui/saved-views.png)
  <figcaption>El menú Save View mostrando las configuraciones guardadas, el icono de estrella para establecer una vista predeterminada y el botón de eliminar.</figcaption>
</figure>

!!! info
    - **Guardar vista actual:** captura el estado completo de la grilla — filtros aplicados, columnas visibles, orden de columnas y criterio de ordenación — bajo un nombre personalizado (máx. 100 caracteres). La configuración se guarda en el backend.
    - **Aplicar vistas guardadas:** al abrir el menú se muestran todas las vistas disponibles para la solapa actual. Un solo clic aplica toda la configuración guardada.
    - **Establecer como predeterminada:** cualquier vista puede marcarse como predeterminada mediante el icono de estrella. La vista predeterminada se carga automáticamente cada vez que se abre la solapa. Solo se permite una vista predeterminada por solapa.
    - **Restablecer a estándar:** restaura el estado original de la grilla sin filtros ni configuración personalizada.
    - **Eliminar vistas:** al situar el cursor sobre una vista se muestra un botón de eliminar con solicitud de confirmación.

## Panel de inicio configurable con widgets { #configurable-dashboard-with-widgets }

La pantalla de inicio es un panel configurable. Añada, elimine y reorganice widgets para configurar su espacio de trabajo. Es la primera pantalla que se muestra al iniciar sesión en Etendo.

<figure markdown="span">
  ![Vista general del panel](../../assets/user-guide/newui/dashboard-overview.png)
  <figcaption>El panel de la pantalla de inicio con múltiples widgets organizados en la grilla.</figcaption>
</figure>

**Gestión del panel**

- La grilla de widgets admite **arrastrar y soltar** para reposicionar los widgets.
- El botón **Add Widget** abre un diálogo con todos los tipos de widgets disponibles.
- Cada widget dispone de un botón para eliminarlo (**X**). Algunos widgets incluyen una opción **Edit Parameters** para personalizar sus datos.

<figure markdown="span">
  ![Diálogo de Add Widget](../../assets/user-guide/newui/dashboard-add-widget.png)
  <figcaption>El diálogo de Add Widget con la lista de tipos de widgets disponibles.</figcaption>
</figure>

**Tipos de widgets disponibles**

- **KPI** — Muestra un valor numérico grande con unidad, etiqueta e indicador de tendencia (verde para positivo, rojo para negativo).
- **Calendar** — Interfaz de calendario con eventos programados.
- **Process** — Muestra el estado o el progreso de un proceso en segundo plano que se ejecuta en el sistema.
- **Query List** — Tabla con paginación, columnas ordenables y navegación mediante clic a la ventana relacionada.
- **HTML** — Muestra un bloque de texto o contenido con formato personalizado diseñado por su administrador.
- **URL** — Muestra una página web o herramienta externa directamente dentro de su panel, sin salir de Etendo.
- **Stock Alert** — Alertas de inventario con indicadores de estado.
- **Notification** — Notificaciones y mensajes.
- **Favorites** — Ventanas favoritas mostradas como chips sobre los que se puede hacer clic (véase más abajo).
- **Recently Viewed** — Documentos vistos recientemente.
- **Recent Documents** — Actividad reciente de documentos.

**Widget de Favorites**

Un widget dedicado que muestra todas las ventanas favoritas del usuario como chips compactos sobre los que se puede hacer clic.

<figure markdown="span">
  ![Widget de Favorites](../../assets/user-guide/newui/dashboard-favorites-widget.png)
  <figcaption>El widget de Favorites mostrando las ventanas guardadas como chips sobre los que se puede hacer clic.</figcaption>
</figure>

- Haga clic en cualquier chip para abrir esa ventana en una nueva solapa.
- El widget se actualiza en tiempo real cuando el usuario marca o desmarca favoritos desde cualquier parte de la UI (icono de estrella en la barra lateral).

<figure markdown="span">
  ![Estrella de Favorites](../../assets/user-guide/newui/dashboard-favorites-star.png)
  <figcaption>El icono de estrella en la barra lateral que se usa para marcar o desmarcar una ventana como favorita.</figcaption>
</figure>

- Muestra un guion (**—**) como estado vacío cuando no hay favoritos configurados.

!!! note
    El widget de Favorites no existe en Etendo Classic. Es una funcionalidad exclusiva de la Etendo New UI.

## Correo electrónico desde la barra de herramientas { #email-from-toolbar }

La barra de herramientas incluye un modal de correo electrónico. Úselo para redactar y enviar correos electrónicos directamente desde el contexto del registro actual.

<figure markdown="span">
  ![Modal de correo electrónico](../../assets/user-guide/newui/email-modal.png)
  <figcaption>El modal de redacción de correo electrónico abierto desde la barra de herramientas de un registro.</figcaption>
</figure>

**Campos del formulario**

| Campo | Detalles |
|-------|----------|
| **Para** (obligatorio) | Dirección del destinatario, precargada desde el contexto del registro actual. |
| **CCO** | Los destinatarios añadidos aquí reciben el correo pero están ocultos para el resto de destinatarios. No pueden ver las direcciones de los demás y nadie ve quién fue incluido en CCO. |
| **Responder a** | Dirección de respuesta. |
| **CC** | Los destinatarios añadidos aquí reciben una copia del correo y son visibles para todos los destinatarios de los campos **Para** y **CC**. Disponible en **Mostrar más campos**. |
| **Asunto** (obligatorio) | Línea de asunto del correo electrónico. |
| **Cuerpo** | Área de texto con un panel de referencia que muestra los tokens de plantilla disponibles. |

**Tokens de plantilla**

Para personalizar el correo electrónico, escriba cualquier marcador de posición directamente en el cuerpo del mensaje. Al enviar el correo, cada marcador se sustituye automáticamente por los datos reales del registro actual — sin necesidad de introducirlos manualmente. Por ejemplo, escriba `Dear @cus_nam@,` y aparecerá "Dear Acme Corp," según el registro.

| Marcador | Lo que inserta en el correo |
|----------|----------------------------|
| `@cus_ref@` | Número de referencia del cliente |
| `@our_ref@` | Referencia interna de su empresa |
| `@cus_nam@` | Nombre del cliente |
| `@sal_nam@` | Nombre del comercial |
| `@bp_nam@` | Nombre del tercero |
| `@doc_date@` | Fecha del documento |
| `@doc_desc@` | Descripción del documento |
| `@doc_nextduedate@` | Fecha del próximo vencimiento |
| `@doc_lastduedate@` | Fecha del último vencimiento |

**Plantillas**

Un selector desplegable permite elegir plantillas predefinidas que rellenan automáticamente el cuerpo y otros campos.

**Adjuntos**

La sección de adjuntos muestra archivos de informe, adjuntos del registro y archivos cargados en una tabla.

- Añada archivos locales desde su equipo.
- Cargue adjuntos asociados al registro desde la base de datos.
- Active la casilla **Archive** en los archivos de informe.
- Elimine adjuntos individuales mediante el botón **X**.

## Selector de imágenes { #image-selector }

Los campos de imagen en formularios disponen de un flujo completo de carga, vista previa y edición.

<figure markdown="span">
    ![Campos del selector de imágenes](../../assets/user-guide/newui/image-selector-fields.png)
    <figcaption>Campos de imagen en un formulario, mostrando los controles de carga y vista previa.</figcaption>
</figure>

**Carga**

<figure markdown="span">
    ![Diálogo de carga de imagen](../../assets/user-guide/newui/image-upload-dialog.png)
    <figcaption>El diálogo de carga de imagen, con soporte para arrastrar y soltar y retroalimentación de validación de dimensiones.</figcaption>
</figure>

- Haga clic en un campo de imagen para abrir el diálogo de carga.
- Admite **arrastrar y soltar** o selección de archivo.
- Valida las dimensiones de la imagen respecto a las restricciones configuradas (mínimo/máximo).

!!! warning "Validación de dimensiones"
    - Si se incumplen restricciones obligatorias, se muestra un **error** con las dimensiones actuales frente a las requeridas.
    - Si las restricciones son recomendadas, un **diálogo de confirmación** permite continuar o cancelar.
    - Existe una función opcional de **redimensionamiento automático**, con una confirmación que muestra las dimensiones original y final.

**Vista previa y edición**

<figure markdown="span">
    ![Modal de vista previa de imagen](../../assets/user-guide/newui/image-preview-modal.png)
    <figcaption>El modal de vista previa a pantalla completa, con controles de zoom, desplazamiento, recarga y eliminación.</figcaption>
</figure>

- La imagen cargada aparece como una **miniatura** en el formulario.
- Haga clic en la miniatura para abrir un **modal de vista previa a pantalla completa**.
- En el modal de vista previa:
    - **Zoom** con la rueda del ratón (0,5x a 5x).
    - **Arrastrar** para desplazarse por la imagen.
    - **Restablecer zoom** para volver a la vista predeterminada.
    - **Volver a cargar** para sustituir la imagen actual.
    - **Eliminar** con solicitud de confirmación.

## Atajos de teclado { #keyboard-shortcuts }

Un sistema centralizado de atajos de teclado cubre las acciones más habituales en la Etendo New UI.

| Atajo | Acción |
|-------|--------|
| `Arrow Up` / `Arrow Down` | Navegar entre filas de la tabla sin usar el ratón. |
| `Ctrl + S` | Guardar el registro actual. |
| `Ctrl + N` | Crear un nuevo registro. |

!!! info "Detalles de comportamiento"
    - Los atajos **no se activan** cuando el foco está en campos de entrada, áreas de texto o desplegables (salvo que estén configurados explícitamente).
    - El comportamiento predeterminado del navegador **queda bloqueado** (por ejemplo, `Ctrl + S` no abre el diálogo "Guardar página" del navegador).
    - Los atajos son **sensibles al contexto**: solo se activan dentro de la región de la UI correspondiente.

## Sistema de enfoque y guardado previo { #focus-system-and-prior-saving }

El sistema de enfoque guarda automáticamente los cambios sin guardar al cambiar entre solapas o ventanas.

- Al cambiar de solapa o ventana, los **cambios sin guardar** en el área previamente activa se **guardan automáticamente** (de forma asíncrona).
- El sistema registra qué solapa o ventana está activa en cada momento.
- Las solapas en segundo plano **mantienen su estado**, lo que permite cambiar entre ellas al instante sin pérdida de datos.
- Navegue libremente entre las solapas abiertas sin perder el trabajo en curso. La navegación es fluida y los datos permanecen coherentes.

## Navegación con teclas de flecha en tablas { #arrow-key-navigation-in-tables }

Las teclas de flecha permiten navegar por el teclado entre las filas de una tabla.

- `Arrow Up`: mueve la selección a la fila anterior.
- `Arrow Down`: mueve la selección a la fila siguiente.
- La navegación **se detiene en los límites de la tabla** — no pasa de la primera ni de la última fila.
- Solo funciona cuando hay **una única fila seleccionada**.
- Las pulsaciones rápidas avanzan filas de forma fluida (con debounce para evitar lag).
- **Deshabilitado en modo edición**.
- El sistema distingue entre la navegación por teclado y los clics del ratón para optimizar el rendimiento.

## Agentes destacados en Copilot { #featured-agents-in-copilot }

El selector de asistentes de Copilot organiza los agentes en dos grupos para un acceso más rápido.

- Sección **Agentes destacados**: ciertos agentes aparecen resaltados en la parte superior de la lista, distinguidos visualmente con un distintivo o estilo especial que indica que son recomendados.
- Sección **Agentes regulares**: los agentes no destacados aparecen a continuación.
- Esta organización ayuda a los usuarios a encontrar rápidamente los asistentes más útiles sin tener que recorrer toda la lista.

## Mejoras en el chat de Copilot { #copilot-chat-improvements }

La interfaz de chat de Copilot incluye varias mejoras de usabilidad.

!!! info "Funciones principales"
    - **Lista de conversaciones:** barra lateral que muestra el historial de conversaciones anteriores.
    - **Archivar/Eliminar:** las conversaciones se pueden archivar o eliminar.
    - **Nueva conversación:** botón para iniciar una conversación nueva.
    - **Buscar conversaciones:** búsqueda en el historial de conversaciones.
    - **Renombrar conversaciones:** títulos editables para una mejor organización.
    - **UI mejorada:** mejor formato de mensajes, espaciado y jerarquía visual.
    - **Estados claros:** indicadores para el estado vacío, la carga y las condiciones de error.
    - **Streaming:** las respuestas se muestran en tiempo real mientras el agente las genera.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"} by [Futit Services S.L](https://etendo.software){target="\_blank"}.
