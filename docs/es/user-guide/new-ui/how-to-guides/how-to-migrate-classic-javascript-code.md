---
tags:
  - Cómo hacerlo
  - New UI
  - Migración de JavaScript
  - Definición de proceso

status: new
---

# Cómo migrar el JavaScript de procesos Classic a la nueva UI { #how-to-migrate-classic-process-javascript-to-the-new-ui }

## Visión general { #overview }

En **Etendo Classic**, un *Proceso definido* (un proceso configurado en el Diccionario de la Aplicación, con o
sin parámetros) puede llevar JavaScript escrito a mano que personaliza su diálogo: rellenar campos
previamente cuando se abre, validar y transformar la entrada a medida que el usuario escribe, condicionar la ejecución a una
confirmación, mostrar banners dentro del diálogo, lanzar procesos anidados o post-procesar la respuesta
del servidor. En Classic este JavaScript se ejecuta dentro del entorno de ejecución de SmartClient.

La **nueva Workspace UI** reproduce ese comportamiento **sin SmartClient**. El JavaScript personalizado ya no
está vinculado a un módulo de SmartClient; en su lugar se almacena como texto plano en un conjunto de columnas de metadatos
del proceso y de sus parámetros. En tiempo de ejecución, la nueva UI compila ese texto y lo ejecuta sobre
un contexto curado que emula las APIs de Classic que los scripts esperan. Esto hace que la capacidad sea
**totalmente controlada por metadatos**: cualquier proceso se vuelve programable simplemente rellenando sus columnas — no se
despliega código nuevo en la UI.

Esta guía explica **cómo migrar el JavaScript de un Proceso definido** de Classic a la nueva UI en
su propio entorno. Si usted mantiene una instancia productiva con Procesos definidos personalizados cuyo JavaScript de Classic
personaliza su comportamiento, esos scripts **no** se ejecutarán en la nueva UI hasta que se
migren a las columnas de metadatos. Este documento es su referencia para hacerlo.

!!! info "Para quién es esta guía y cuál es su rol"
    Esta guía está escrita para desarrolladores que deben migrar el JavaScript de procesos Classic **sin acceso al
    código fuente de la nueva UI**. Sus herramientas son **esta documentación**, la **referencia de
    arquitectura** a la que apunta y el **"New UI Migrations" Team**. Concretamente, su trabajo consiste en:

    1. Producir el código migrado (manualmente, o con el **"New UI Migrations" Team** — consulte
       [Migrar con el "New UI Migrations" Team](#migrating-with-the-new-ui-migrations-team)).
    2. Pegarlo en los campos de metadatos correctos (consulte [Los campos de metadatos](#the-metadata-fields-where-the-migrated-code-goes)).
    3. **Validar el resultado manualmente** en el diálogo en ejecución.
    4. Si algo no funciona, **notificar el problema** — describir exactamente qué falla y dónde.

!!! warning "La automatización es asistida, no autónoma"
    El **"New UI Migrations" Team** acelera la migración, pero **puede cometer errores**. Toda migración que produzca
    **debe ser validada manualmente** por un desarrollador antes de considerarse terminada. Trate la salida del equipo
    como un primer borrador a verificar, nunca como un resultado terminado y confiable.

---

## Antecedentes: los cinco puntos de enganche de Classic { #background-the-five-classic-hook-points }

Un Proceso definido de Classic puede asociar comportamiento en hasta cinco puntos. La nueva UI asigna cada uno a una
columna de metadatos:

| # | Hook de Classic | Se dispara cuando… | Ámbito |
|---|---|---|---|
| 1 | `onLoad` | Se abre el diálogo del proceso | Process(`OBUIAPP_Process`) |
| 2 | `onProcess` | El usuario pulsa el botón de ejecutar / OK | Process(`OBUIAPP_Process`) |
| 3 | `onRefresh` | El diálogo necesita volver a obtener sus datos (p. ej. después de que se cierra un proceso anidado) | Process(`OBUIAPP_Process`) |
| 4 | `onChange` | Se confirma el valor de un parámetro | Parameter(`OBUIAPP_Parameter`) |
| 5 | `onGridLoad` | Un parámetro de grilla embebida termina de cargar las filas | Parameter(`OBUIAPP_Parameter`) |

Más allá de estos puntos de entrada, un archivo de proceso de Classic es un único *módulo* de JavaScript: los puntos de entrada llaman a
funciones auxiliares compartidas, constantes y estado de clausura declarados en el mismo archivo. La nueva UI reproduce esto con
una columna dedicada de **ámbito de módulo** (consulte [`em_etmeta_payscript_logic`](#4-em_etmeta_payscript_logic-shared-module-scope)).

El **objetivo de la migración es la paridad de comportamiento**: un proceso migrado debe comportarse igual que su
contraparte de Classic, con el JavaScript residiendo en los metadatos en lugar de en un módulo de SmartClient.

---

## Qué puede hacer la nueva UI { #what-the-new-ui-can-do }

Esta sección describe las capacidades disponibles para los scripts migrados — el **qué**, el **por qué** y
**cómo se usan** — sin entrar en cómo se implementan internamente. Si un script toca
algo que la nueva UI no implementa, lanza un error claro `"<api> is not implemented yet"` en lugar de
fallar silenciosamente, de modo que las carencias afloran durante la migración en lugar de en producción.

### El contrato del modelo de ejecución que debe respetar { #the-execution-model-contract-you-must-respect }

Unas pocas reglas rigen todos los campos. No son opcionales — un cuerpo que las rompa no se ejecutará:

- **Cada hook es una expresión de función flecha simple.** El valor de un campo debe ser una única función flecha tal
  como `async (process, view) => { … }`. **No** debe estar envuelto en una expresión de función invocada
  inmediatamente (IIFE, p. ej. `(async () => { … })()`) y **no** debe ser un literal de objeto. Cualquier cosa que no evalúe a
  una función se rechaza en tiempo de compilación.
- **`onLoad` / `onProcess` / `onChange` / `onGridLoad` son funciones flecha; el ámbito de módulo es diferente.**
  El campo de ámbito de módulo (`em_etmeta_payscript_logic`) es un *cuerpo de módulo* — una secuencia de declaraciones
  que termina en `return { … };` — no una función flecha. Consulte la descripción de su campo más abajo.
- **Las funciones auxiliares se resuelven por su nombre simple.** Cualquier cosa devuelta desde el campo de ámbito de módulo está disponible, por su
  nombre simple, dentro de los cinco hooks. Globales como `OB`, `callAction`, `confirm`, `messageBar` y
  `BigDecimal` se inyectan igualmente y se pueden llamar directamente.
- **`onChange` no se dispara durante el sembrado inicial.** Igual que en Classic, el `onChange` de un parámetro se ejecuta solo
  ante un cambio genuino del usuario, nunca mientras el diálogo siembra sus valores iniciales/por defecto. Coloque el cálculo de tiempo de
  carga en `em_etmeta_onload`, no en `on_parameter_change`.

### Catálogo de capacidades { #capability-catalog }

| Capacidad | Qué aporta a los scripts migrados |
|---|---|
| **El objeto `view`** | Refleja el `OBStandardView` de Classic. El contexto de solo lectura (`view.theForm`, `view.messageBar`, `view.getContextInfo()`, `view.selectedRecords`, `view.tabId`, …) está siempre disponible; los métodos de acción (`view.refresh()`, `view.openProcess(...)`, `view.executeProcess()`, los botones de pie, el botón OK) están disponibles dentro de los hooks que los necesitan. |
| **Proxies `form`, `item`** | `view.theForm.getItem(name)` y métodos de campo: `getValue()` / `setValue(v)`, `show()` / `hide()` / `isVisible()`, `setRequired(bool)` / `setDisabled(bool)`, `setTitle(text)`, `setValueMap(map)` / `getValueMap()`, `setValueFromRecord({ id, _identifier })`, y más. Los parámetros numéricos devuelven `number`s reales, por lo que las comparaciones de Classic siguen funcionando. |
| **Proxy `grid`** | Para grillas embebidas (Window-Reference / Pick&Execute): selección (`getSelectedRecords`, `selectRecord`, …), lecturas de filas, valores de edición (`setEditValue`, `getEditValues`), visibilidad (`show()` / `hide()`), botones de acción por fila, y hooks de tiempo de ejecución registrados desde `onGridLoad` (`onRecordChange`, `onSelectionToggle`, `setColumnOnChange`, `setColumnValidator`, `fireOnPause`). |
| **Ejecución en el servidor — `view.executeProcess()`** | El equivalente en la nueva UI del `actionHandlerCall()` de Classic. Construye el payload de ejecución estándar y lo envía a la clase Java configurada del proceso. Úselo en `onProcess` en lugar de construir un payload a mano. |
| **Funciones auxiliares HTTP** | `callAction(handler, payload)`, `callDatasource(entity, payload)`, `callServlet(path, payload)` — POST a handlers/datasources del backend con la autenticación y el CSRF gestionados automáticamente. |
| **Diálogos modales** | `confirm` / `warn` / `say` (e `isc.confirm` / `ask` / `warn` / `say`). Basados en Promesas y también aceptan la forma de callback de Classic. |
| **Barra de mensajes dentro del diálogo** | `view.messageBar.setMessage(severity, title, text, actions?)` y `view.messageBar.hide()`, con severidades `OB.MessageBar.TYPE_*` / `isc.OBMessageBar.TYPE_*`. Los enlaces clicables deben expresarse como un array estructurado `actions`, no como HTML `<a onclick>` en línea. |
| **Procesos anidados** | `view.openProcess(params)` (y `view.standardWindow.openProcess(...)`) superpone otro diálogo de proceso encima; el `onRefresh` del padre se dispara cuando el hijo se cierra. |
| **El shim `OB.*`** | Un espacio de nombres `OB` compartido que refleja los globales de Classic: `OB.I18N.getLabel`, `OB.Format.*`, `OB.Utilities.Number.JSToOBMasked`, `OB.Utilities.Action.set/execute/executeJSON`, `OB.PropertyStore`, `OB.RemoteCallManager.call` (adaptador callback↔Promise), `OB.Datasource.create`, `OB.Constants`, constantes de severidad. |
| **Aritmética decimal — `BigDecimal`** | El `BigDecimal` de Classic se inyecta como global, de modo que los cálculos monetarios (`add`, `subtract`, `multiply`, `divide`, `compareTo`, `setScale`, …) se migran textualmente. **Nunca** reescriba los cálculos monetarios con `Number` / `parseFloat`, que se desvían y rompen la paridad con el servidor. |
| **Despachador de action-JSON** | `OB.Utilities.Action.executeJSON(actions)` despacha un array `responseActions` del backend (barra de mensajes, toast, navegar a una pestaña, refrescar grilla, descargar/visualizar informe, …). |
| **Componente de UI personalizado** | Cuando se establece la marca de componente personalizado del proceso, `onLoad` devuelve un *esquema* de UI y el diálogo renderiza un componente a medida en lugar del formulario de parámetros estándar. |

### Qué no se admite (aún) { #what-is-not-yet-supported }

La nueva UI es genérica y controlada por metadatos, **sin tratamientos especiales por proceso**. Un puñado de mecanismos de Classic
están intencionadamente cambiados o no se admiten:

- **El HTML con onclick en línea en los mensajes** no está permitido. El texto de los mensajes se sanea (solo etiquetas de formato);
  use el array estructurado `actions` para los elementos clicables.
- **Las primitivas de UI de SmartClient** (`isc.ClassFactory.defineClass`, `isc.DynamicForm`, `isc.OBPopup`, …)
  no están disponibles. Sus equivalentes son los declarativos `grid.setRowActions(...)` y
  `openDynamicForm({ fields })`.
- **Cualquier cosa que la plataforma no implemente** lanza `"<api> is not implemented yet"`. Si encuentra tal
  error durante la validación, eso es una carencia de capacidad a **notificar** (consulte
  [Notificar problemas](#reporting-issues)) — no algo a sortear en su entorno.

---

## Los campos de metadatos (dónde va el código migrado) { #the-metadata-fields-where-the-migrated-code-goes }

Siete columnas personalizadas llevan el código migrado. Cuatro pertenecen al **proceso**, dos a cada **parámetro**,
y una es una marca de renderizado en el proceso. Usted introduce el JavaScript migrado en el campo correspondiente
a cada columna en la ventana **Definición de proceso** (y su pestaña **Parámetros**) del Diccionario de la Aplicación.

| Campo (columna) | Entidad | Hook | Forma del código |
|---|---|---|---|
| `em_etmeta_onload` | Process | `onLoad` | `async (process, view) => { … }` |
| `em_etmeta_onprocess` | Process | `onProcess` | `async (process, view) => { … }` |
| `em_etmeta_on_refresh` | Process | `onRefresh` | `(view) => { … }` |
| `em_etmeta_payscript_logic` | Process | ámbito de módulo compartido | cuerpo de módulo que termina en `return { … };` |
| `em_etmeta_on_parameter_change` | Parameter | `onChange` | `(item, view, form, grid) => { … }` |
| `em_etmeta_on_grid_load` | Parameter | `onGridLoad` | `(grid, view, parameters) => { … }` |
| `em_etmeta_custom_component` | Process | marca de renderizado | booleano (Sí/No) |

!!! tip "Cualquier campo puede dejarse vacío"
    Un proceso rara vez usa los cinco hooks. Rellene solo los campos que correspondan a los hooks que el archivo de Classic
    realmente implementa; deje el resto vacíos. Un campo vacío simplemente significa "sin script para este hook".

A continuación se muestra el propósito, la firma y un ejemplo sencillo para cada campo.

### 1. `em_etmeta_onload` — `onLoad` del proceso { #1-em_etmeta_onload-process-onload }

- **Entidad:** process · **Firma:** `async (process, view) => { … }`
- **Se dispara:** una vez, cuando se abre el diálogo, después de que los valores por defecto se hayan sembrado y antes de que el formulario sea
  interactivo.
- **Propósito:** sembrar o calcular valores por defecto, ocultar o requerir campos, preseleccionar filas de grilla, condicionar la
  apertura a un `confirm`, o (con la marca de componente personalizado) devolver un esquema de UI.
- **Devuelve (opcional):** un mapa de pares `paramName: value` para sembrar campos; un retorno falsy es una operación sin efecto.

```js
async (process, view) => {
  const form = view.theForm;
  // Hide an advanced field unless the launching record is a sales transaction.
  const ctx = view.getContextInfo();
  if (ctx.inpissotrx !== 'Y') {
    form.getItem('credit_to_use').hide();
  }
  // Seed a sensible default and make a field mandatory.
  form.getItem('payment_date').setValue(ctx.inpdateordered);
  form.getItem('reference_no').setRequired(true);
};
```

### 2. `em_etmeta_onprocess` — `onProcess` del proceso { #2-em_etmeta_onprocess-process-onprocess }

- **Entidad:** process · **Firma:** `async (process, view) => { … }`
- **Se dispara:** cuando el usuario pulsa el botón de ejecutar / OK.
- **Propósito:** validación del lado del cliente antes del envío, llamada al backend y post-procesamiento de la
  respuesta.
- **Regla clave:** llame a `view.executeProcess()` para ejecutar la propia clase Java del proceso (el equivalente del
  `actionHandlerCall()` de Classic). Para abortar con un error, devuelva `{ severity: 'error', text }`.

```js
async (process, view) => {
  const form = view.theForm;
  const amount = form.getItem('actual_payment').getValue(); // numeric → a real number
  if (amount <= 0) {
    const text = OB.I18N.getLabel('ETP_AmountMustBePositive');
    view.messageBar.setMessage(isc.OBMessageBar.TYPE_ERROR, null, text);
    return { severity: 'error', text }; // aborts; the modal stays open
  }
  const response = await view.executeProcess(); // = actionHandlerCall()
  return response && response.message;
};
```

!!! note "Los procesos Pick&Execute / Window-Reference se comportan de forma diferente"
    Para un proceso cuyo patrón es Pick&Execute, o que tiene un parámetro de grilla Window-Reference, la
    plataforma envía la selección de la grilla por sí misma. Allí, `onProcess` se ejecuta como un **hook de validación
    previa al envío**: devuelva `{ severity: 'error', text }` para abortar, o `undefined` para dejar que el envío continúe —
    y **no** llame a `view.executeProcess()` (provocaría un envío doble).

### 3. `em_etmeta_on_refresh` — `onRefresh` del proceso { #3-em_etmeta_on_refresh-process-onrefresh }

- **Entidad:** process · **Firma:** `(view) => { … }`
- **Se dispara:** cuando el diálogo necesita volver a obtener sus datos — por ejemplo, cuando se cierra un proceso anidado, el
  `onRefresh` del padre se invoca automáticamente.
- **Propósito:** refrescar los datos de grilla/formulario después de un cambio externo.

```js
(view) => {
  // Re-pull the embedded grid after a nested process modified the data.
  view.theForm.getItem('order_invoice').canvas.viewGrid.invalidateCache();
};
```

### 4. `em_etmeta_payscript_logic` — ámbito de módulo compartido { #4-em_etmeta_payscript_logic-shared-module-scope }

- **Entidad:** process · **Forma:** un **cuerpo de módulo** (declaraciones y funciones auxiliares) que termina con
  `return { … };` — **no** una función flecha.
- **Propósito:** contener todo lo que el archivo de Classic declaraba a nivel de módulo — funciones auxiliares compartidas, constantes y
  estado de clausura — que los puntos de entrada referencian por su nombre simple. Se evalúa una vez por apertura del diálogo, y
  lo que devuelva se pone a disposición dentro de los cinco hooks.

```js
const PAID_FULLY = 'PPM';

function remaining(form) {
  const total = new BigDecimal(String(form.getItem('total').getValue()));
  const paid = new BigDecimal(String(form.getItem('actual_payment').getValue()));
  return total.subtract(paid);
}

return { PAID_FULLY, remaining };
```

!!! tip "Auto-registro con espacio de nombres"
    Si el archivo de Classic registra un espacio de nombres como `OB.APRM.AddPayment = { … }`, usted puede hacer lo mismo
    dentro de este cuerpo de módulo; el shim `OB` tolera escrituras `OB.<Module>.<Process>`.

### 5. `em_etmeta_on_parameter_change` — `onChange` del parámetro { #5-em_etmeta_on_parameter_change-parameter-onchange }

- **Entidad:** parameter (uno por parámetro que tenga un onChange) · **Firma:**
  `(item, view, form, grid) => { … }` — `item` es el campo cambiado; `grid` es `null` para los
  parámetros escalares.
- **Se dispara:** cuando el usuario confirma el valor del parámetro (nunca durante el sembrado inicial).
- **Propósito:** reaccionar ante un cambio de valor — recalcular campos dependientes, alternar requerido/deshabilitado, refrescar un
  mapa de valores, mostrar un banner.

```js
(item, view, form) => {
  // When the document type changes, recompute the suggested amount.
  const isCredit = item.getValue() === 'CR';
  form.getItem('credit_amount').setDisabled(!isCredit);
  if (!isCredit) {
    form.getItem('credit_amount').setValue(0);
  }
};
```

### 6. `em_etmeta_on_grid_load` — `onGridLoad` del parámetro { #6-em_etmeta_on_grid_load-parameter-ongridload }

- **Entidad:** parameter (el parámetro de grilla) · **Firma:** `(grid, view, parameters) => { … }`
- **Se dispara:** cada vez que la grilla embebida recibe un resultado de datasource entregado (incluido un resultado
  **vacío**, exactamente una vez).
- **Propósito:** post-procesar las filas cargadas (selección por defecto, componentes por fila, columnas derivadas), registrar
  hooks/validadores de edición por columna, o reaccionar ante una grilla vacía (p. ej. un banner informativo cuando ninguna fila coincide).

```js
(grid, view) => {
  if (grid.getData().getLength() === 0) {
    view.messageBar.setMessage(isc.OBMessageBar.TYPE_INFO, null,
      OB.I18N.getLabel('ETP_NoOutstandingDocuments'));
    return;
  }
  // Recompute a total whenever an editable amount cell changes.
  grid.onRecordChange((record, changes) => {
    // …re-sum settlement amounts over the selected rows…
  });
};
```

### 7. `em_etmeta_custom_component` — marca de componente personalizado { #7-em_etmeta_custom_component-custom-component-flag }

- **Entidad:** process · **Tipo:** booleano (Sí/No).
- **Propósito:** selecciona *cómo se renderiza el diálogo del proceso*:
    - **`No` (false) — el caso normal.** El diálogo renderiza el **formulario estándar basado en
      metadatos**: los parámetros del proceso, sus metadatos y los hooks de JavaScript migrados
      (`onLoad`, `onProcess`, `onChange`, …) descritos en esta guía. Esto es lo que usted utiliza para
      prácticamente todas las migraciones.
    - **`Sí` (true) — una UI a medida.** El diálogo **no** renderiza el formulario de parámetros
      estándar. En su lugar, la nueva UI debe contener un **componente personalizado construido
      específicamente para ese proceso**, y `onLoad` devuelve el esquema que lo gobierna. Esto refleja
      el comportamiento de Classic, donde un proceso así también dispone de su propia UI construida a
      mano en lugar de un diálogo de parámetros genérico. Se reserva para el caso poco frecuente de un
      proceso cuyo diálogo no es una lista plana de campos (por ejemplo, un selector especializado).

!!! warning "Un componente personalizado no se puede producir solo con metadatos"
    Establecer esta marca en `Sí` **no** es una migración que usted pueda completar rellenando campos.
    Un componente personalizado es código real que debe añadirse a la nueva UI para ese proceso
    concreto, y usted **no** dispone de acceso al código fuente de la nueva UI. Si un proceso realmente
    necesita un componente personalizado, **comuníquese con el equipo de plataforma** para que lo
    construya. Para todos los demás procesos, deje esta marca en `No` y realice la migración utilizando
    los campos estándar descritos arriba.

---

## Migrar con el "New UI Migrations" Team { #migrating-with-the-new-ui-migrations-team }

Para la mayoría de los procesos usted no tiene que escribir la migración a mano. El **"New UI Migrations" Team**
proporcionado por Fyso traduce un archivo JavaScript de un Proceso definido de Classic a las columnas de metadatos descritas
arriba, usando su agente de migración interno. Usted interactúa con él **en español** (el mensaje de activación
y sus entregables están en español), como se muestra en los pasos a continuación.

!!! note "Migrar a mano"
    Los pasos 4 a 6 también se aplican a usted: sustituya sus propios cuerpos migrados por los bloques de código etiquetados del equipo,
    y derive su propio plan de pruebas manual en lugar de la lista de comprobación del equipo.

### Qué hace — y qué no hace — el equipo { #what-the-team-does-and-does-not-do }

**El equipo hace:** lee el archivo `.js` de Classic y los metadatos del proceso; comprueba la viabilidad contra el
documento de arquitectura; genera el código migrado para cada columna como una función flecha simple; autocomprueba
que cada cuerpo compila; y le entrega una salida por columna lista para pegar, junto con una lista de comprobación de
pruebas manuales.

**El equipo nunca:** pega el código en la UI por usted (eso lo hace usted); cambia el código fuente de la aplicación; hace commit
o push de nada; ni inventa soporte de plataforma que no existe. Si un proceso usa algo que la nueva UI
no puede hacer, el equipo **se detiene y notifica la carencia** en lugar de producir código que parece migrado pero se rompe.

!!! warning "Usted aún debe validar"
    La salida del equipo es un **borrador a verificar**, no un resultado terminado. Puede malinterpretar un caso límite o un
    modismo de Classic. Ejecute siempre la lista de comprobación manual antes de considerar la migración terminada, y
    [notifique](#reporting-issues) cualquier cosa que falle.

### Paso 1 — Identificar las entradas { #step-1-identify-the-inputs }

Usted necesita dos cosas:

1. **La ruta al archivo `.js` de Classic** del Proceso definido (el archivo que contiene su JavaScript
   personalizado).
2. **El id del proceso** — el `obuiapp_process_id` de 32 caracteres del Proceso definido. Puede leerlo
   desde el registro de la ventana Definición de proceso, o desde la URL/ayuda de ese registro.

### Paso 2 — Activar el equipo { #step-2-engage-the-team }

El agente de migración del equipo solo actúa cuando su mensaje coincide con su plantilla de activación **exactamente** (las
comillas pueden ser simples o dobles). Envíele, en español, la ruta del archivo y el id del proceso:

```text
Quiero migrar el javascript del proceso definido. El path del archivo original es '<path>' y el id del proceso es '<process-id>'.
```

Por ejemplo:

```text
Quiero migrar el javascript del proceso definido. El path del archivo original es 'modules/com.example.payments/web/js/ob-myprocess.js' y el id del proceso es '9BED7889E1034FE68BD85D5D16857320'.
```

Si el mensaje no coincide con la plantilla, el equipo no actuará — simplemente reformulará la plantilla que usted
debe usar.

### Paso 3 — Revisar la salida del equipo { #step-3-review-the-teams-output }

El equipo devuelve, en español para los entregables:

- Un **informe de cobertura**: una tabla que clasifica cada API de Classic que el archivo usa como *admitida*,
  *de mejor esfuerzo* o *no admitida*. **Si algo no está admitido, el equipo se detiene aquí** y explica exactamente
  qué le falta a la nueva UI — eso es una carencia a notificar, no a sortear.
- El **código migrado por columna**, cada uno en su propio bloque de código, claramente etiquetado con la columna a la que
  va. Las columnas sin código se marcan como **"LEAVE EMPTY"**.
- Una lista de **advertencias** (código muerto eliminado, notas de clonación, diferencias semánticas).
- Una **lista de comprobación de pruebas manuales** — los pasos concretos que usted debe ejecutar para confirmar la paridad.

Lea el informe de cobertura y las advertencias antes de pegar nada. Le dicen qué esperar y qué
probar.

### Paso 4 — Pegar el código en los campos { #step-4-paste-the-code-into-the-fields }

Para cada bloque etiquetado, copie el cuerpo en el campo correspondiente de la ventana Definición de proceso (o su
pestaña Parámetros), siguiendo [Los campos de metadatos](#the-metadata-fields-where-the-migrated-code-goes).
Pegue **solo** el código que el equipo entregó, exactamente como se proporcionó, en la columna indicada. Guarde el registro.

!!! danger "Haga coincidir el campo con la columna"
    Pegar un cuerpo `onProcess` en el campo `onLoad` (o un hook de parámetro en el parámetro equivocado)
    producirá un comportamiento incorrecto difícil de diagnosticar. Compruebe dos veces la etiqueta de cada bloque contra el
    campo que está editando.

### Paso 5 — Validar manualmente { #step-5-validate-manually }

Abra el diálogo del proceso en la nueva UI y ejecute **cada** elemento de la lista de comprobación de pruebas manuales del equipo: confirme
que el diálogo se abre correctamente, que ocurrió el sembrado/ocultamiento de `onLoad`, que cada `onChange` reacciona como en
Classic, que las grillas cargan y validan como se espera, y que la ejecución devuelve el mismo resultado que Classic.
Compare lado a lado con el diálogo de Classic siempre que sea posible.

### Paso 6 — Notificar problemas (no corregir) { #step-6-report-problems-do-not-fix }

Si una prueba falla — un hook no se dispara, un valor es incorrecto, o ve un error `"… is not implemented yet"`
— **notifíquelo**. Describa el síntoma con precisión (qué proceso, qué hook, qué hizo, qué
esperaba, qué ocurrió) e incluya cualquier texto de error. Si activó el **"New UI Migrations" Team**, también puede decirle
`"el test X falló: <síntoma>"` y reanalizará y reemitirá los campos corregidos para ese
proceso.

**No** intente parchear la nueva UI en su entorno. Las carencias de capacidad y los errores del sustrato se
resuelven por el equipo de la plataforma; su contribución es un informe claro y reproducible.

---

## Notificar problemas { #reporting-issues }

Como usted no tiene acceso al código fuente de la nueva UI, un buen informe es lo más valioso que
puede producir cuando una migración no se comporta como Classic. Incluya:

- **El proceso** — nombre y `obuiapp_process_id`.
- **El hook / campo** involucrado (`onLoad`, `onProcess`, el `onChange` de un parámetro específico, etc.).
- **Pasos para reproducir** — exactamente lo que hizo en el diálogo.
- **Esperado vs real** — qué hace Classic frente a qué hace la nueva UI.
- **Cualquier texto de error** mostrado en el diálogo o en la consola del navegador (especialmente
  `"<api> is not implemented yet"`, que nombra la capacidad que falta).
- **El cuerpo migrado relevante** que pegó, y el informe de cobertura si activó el **"New UI Migrations" Team**.

---

## Referencia { #reference }

- **Referencia de arquitectura y capacidades (fuente de verdad):**
  [new-javascript-code.md](https://github.com/etendosoftware/com.etendorx.workspace-ui/blob/main/docs/process/definition/new-javascript-code.md)
  — la descripción autoritativa de cada API admitida, firma y regla de migración.
- **El "New UI Migrations" Team:** consulte la [lista completa de agentes disponibles](https://fyso.world/app/teams/),
  incluido el agente de migración utilizado para traducir el JavaScript de procesos Classic.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
